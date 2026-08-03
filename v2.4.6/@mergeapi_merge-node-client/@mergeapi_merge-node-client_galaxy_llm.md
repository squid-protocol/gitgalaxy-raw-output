# ARCHITECTURAL_BRIEF: @mergeapi_merge-node-client
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/@mergeapi_merge-node-client` |
| **Timestamp** | `2026-08-03T21:08:49.990588+00:00` |
| **Scan Duration** | `30.24s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 6551 malicious artifacts.

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
| Total Artifacts | 10921 |
| Analyzed Artifacts (Scanned) | 6554 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4367 |
| Total LOC | 67285 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 60.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2798 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 24 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 5427 | 45787 | 82.8% |
| JAVASCRIPT | 1124 | 21498 | 17.1% |
| MARKDOWN | 2 | 0 | 0.0% |
| PLAINTEXT | 1 | 0 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.061`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 4170 | 63.6% |
| file_cluster_8 | 1612 | 24.6% |
| file_cluster_11 | 501 | 7.6% |
| file_cluster_16 | 204 | 3.1% |
| file_cluster_2 | 41 | 0.6% |
| file_cluster_4 | 15 | 0.2% |
| file_cluster_6 | 6 | 0.1% |
| file_cluster_17 | 1 | 0.0% |
| file_cluster_5 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4367*

**Composition by Extension & Reason:**
- `.js`: 1723x Excluded (Machine-Generated Source Code Signature: 4 LOC), 637x Excluded (Machine-Generated Source Code Signature: 41 LOC), 295x Excluded (Machine-Generated Source Code Signature: 40 LOC)
- `.ts`: 11x Excluded (Saturation: Line 6 exceeds 500 chars), 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Saturation: Line 17 exceeds 500 chars)
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 134 LOC), 1x Excluded (Monolithic Amalgamation: 38958 LOC exceeds safe regex boundaries)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 15.5 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 6.4 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 1.5 | 1.1 | 2.3 |
| API Exposure | 0.0 | 20.0 | 6.1 | 5.8 | 9.2 |
| Concurrency Exposure | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 13.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 20.7 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 50.5 | 46.7 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 100.0 | 36.1 | 33.9 | 13.3 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/core/fetcher/getFetchFn.js` (Hits: 5)
- `package/core/schemas/builders/object/object.js` (Hits: 4)
- `package/environments.d.ts` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Schema.js** (`package/core/schemas/Schema.js`) — 47 inbound connections
2. **list.js** (`package/core/schemas/builders/list/list.js`) — 14 inbound connections
3. **getErrorMessageForIncorrectType.js** (`package/core/schemas/utils/getErrorMessageForIncorrectType.js`) — 14 inbound connections
4. **createIdentitySchemaCreator.js** (`package/core/schemas/utils/createIdentitySchemaCreator.js`) — 9 inbound connections
5. **maybeSkipValidation.js** (`package/core/schemas/utils/maybeSkipValidation.js`) — 9 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.d.ts** (`package/api/resources/accounting/types/index.d.ts`) — 601 outbound dependencies
2. **index.d.ts** (`package/serialization/resources/accounting/types/index.d.ts`) — 601 outbound dependencies
3. **index.js** (`package/api/resources/accounting/types/index.js`) — 601 outbound dependencies
4. **index.js** (`package/serialization/resources/accounting/types/index.js`) — 601 outbound dependencies
5. **index.d.ts** (`package/api/resources/crm/types/index.d.ts`) — 224 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `stringifyObject` (@ `package/core/url/qs.js`) -> Impact: **302.0** | LOC: 40
- `union` (@ `package/core/schemas/builders/union/union.js`) -> Impact: **281.2** | LOC: 47
- `object` (@ `package/core/schemas/builders/object/object.js`) -> Impact: **253.1** | LOC: 92
- `fetcherImpl` (@ `package/core/fetcher/Fetcher.js`) -> Impact: **158.4** | LOC: 136
- `evaluateRuntime` (@ `package/core/runtime/runtime.js`) -> Impact: **138.8** | LOC: 75
  * *Intent:* /** * A constant that indicates which environment and version the SDK is running in.
- `redactUrl` (@ `package/core/fetcher/Fetcher.js`) -> Impact: **124.4** | LOC: 64
- `getErrorResponseBody` (@ `package/core/fetcher/getErrorResponseBody.js`) -> Impact: **115.9** | LOC: 31
- `record` (@ `package/core/schemas/builders/record/record.js`) -> Impact: **110.9** | LOC: 36
- `getObjectUtils` (@ `package/core/schemas/builders/object/object.js`) -> Impact: **87.8** | LOC: 58
- `getResponseBody` (@ `package/core/fetcher/getResponseBody.js`) -> Impact: **81.6** | LOC: 55

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `read` (@ `package/core/fetcher/stream-wrappers/NodePre18StreamWrapper.js`) -> **O(2^N) [Recursive]**
- `bigint` (@ `package/core/schemas/builders/bigint/bigint.js`) -> **O(2^N) [Recursive]**
- `date` (@ `package/core/schemas/builders/date/date.js`) -> **O(2^N) [Recursive]**
- `getObjectUtils` (@ `package/core/schemas/builders/object/object.js`) -> **O(2^N) [Recursive]**
- `union` (@ `package/core/schemas/builders/union/union.js`) -> **O(2^N) [Recursive]**
- `read` (@ `package/core/fetcher/stream-wrappers/Node18UniversalStreamWrapper.js`) -> **O(2^N) [Recursive]**
- `next` (@ `package/core/fetcher/stream-wrappers/NodePre18StreamWrapper.js`) -> **O(2^N) [Recursive]**
- `read` (@ `package/core/fetcher/stream-wrappers/UndiciStreamWrapper.js`) -> **O(2^N) [Recursive]**
- `stringifyObject` (@ `package/core/url/qs.js`) -> **O(2^N) [Recursive]**
- `resume` (@ `package/core/fetcher/stream-wrappers/Node18UniversalStreamWrapper.js`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `getFetchFn` (@ `package/core/fetcher/getFetchFn.js`) -> DB Complexity: **15**
  * *Intent:* /**
- `getNextPage` (@ `package/core/pagination/CustomPager.js`) -> DB Complexity: **15**
  * *Intent:* /** * @returns whether there is a previous page to load */
- `getPreviousPage` (@ `package/core/pagination/CustomPager.js`) -> DB Complexity: **15**
- `date` (@ `package/core/schemas/builders/date/date.js`) -> DB Complexity: **9**
- `_startReading` (@ `package/core/fetcher/stream-wrappers/Node18UniversalStreamWrapper.js`) -> DB Complexity: **8**
- `_startReading` (@ `package/core/fetcher/stream-wrappers/UndiciStreamWrapper.js`) -> DB Complexity: **8**
- `constructor` (@ `package/core/pagination/CustomPager.js`) -> DB Complexity: **8**
  * *Intent:* /** *
- `setObjectProperty` (@ `package/core/utils/setObjectProperty.js`) -> DB Complexity: **8**
  * *Intent:* /**
- `redactUrl` (@ `package/core/fetcher/Fetcher.js`) -> DB Complexity: **7**
- `constructor` (@ `package/core/fetcher/stream-wrappers/Node18UniversalStreamWrapper.js`) -> DB Complexity: **7**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package/core/fetcher` | 38 | 1688.25 | 33.57% | 29.78% |
| `package/serialization/resources/accounting/types` | 596 | 1532.71 | 7.59% | 0.0% |
| `package/core/fetcher/stream-wrappers` | 8 | 1448.5 | 64.22% | 30.64% |
| `package/api/resources/accounting/types` | 599 | 1339.98 | 2.48% | 0.2% |
| `package/serialization/resources/crm/types` | 224 | 875.84 | 7.82% | 0.0% |
| `package/serialization/resources/ats/types` | 221 | 867.97 | 7.49% | 0.0% |
| `package/serialization/resources/hris/types` | 200 | 829.71 | 7.68% | 0.0% |
| `package/api/resources/crm/types` | 226 | 816.51 | 3.59% | 9.4% |
| `package/api/resources/ats/types` | 222 | 810.83 | 3.71% | 2.08% |
| `package/serialization/resources/ticketing/types` | 178 | 788.29 | 7.72% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/core/fetcher/signals.d.ts` -> **100.0%** Exposure
- `package/core/schemas/builders/union/discriminant.d.ts` -> **100.0%** Exposure
- `package/core/fetcher/EndpointSupplier.js` -> **100.0%** Exposure
- `package/core/fetcher/Supplier.js` -> **100.0%** Exposure
- `package/core/fetcher/getRequestBody.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/core/fetcher/Headers.d.ts` -> **100.0%** Exposure
- `package/api/index.js` -> **100.0%** Exposure
- `package/api/resources/accounting/index.js` -> **100.0%** Exposure
- `package/api/resources/accounting/resources/accountDetails/index.js` -> **100.0%** Exposure
- `package/api/resources/accounting/resources/accountToken/index.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/core/logging/logger.js` -> **0** Orphaned Functions | **8** Duplicates
- `package/core/pagination/CustomPager.js` -> **0** Orphaned Functions | **7** Duplicates
- `package/core/pagination/Page.js` -> **0** Orphaned Functions | **7** Duplicates
- `package/auth/BearerAuthProvider.d.ts` -> **2** Orphaned Functions | **0** Duplicates
- `package/core/logging/logger.d.ts` -> **0** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/api/resources/accounting/types/index.js`** -> AI Confidence: **99.39%**
2. **`package/api/resources/ats/types/index.js`** -> AI Confidence: **99.39%**
3. **`package/api/resources/crm/types/index.js`** -> AI Confidence: **99.39%**
4. **`package/api/resources/filestorage/types/index.js`** -> AI Confidence: **99.39%**
5. **`package/api/resources/hris/resources/employees/types/index.js`** -> AI Confidence: **99.39%**
6. **`package/api/resources/hris/resources/employments/types/index.js`** -> AI Confidence: **99.39%**
7. **`package/api/resources/hris/resources/timeOff/types/index.js`** -> AI Confidence: **99.39%**
8. **`package/api/resources/hris/types/index.js`** -> AI Confidence: **99.39%**
9. **`package/api/resources/ticketing/resources/tickets/types/index.js`** -> AI Confidence: **99.39%**
10. **`package/api/resources/ticketing/types/index.js`** -> AI Confidence: **99.39%**
11. **`package/core/fetcher/Fetcher.js`** -> AI Confidence: **99.39%**
12. **`package/core/schemas/builders/index.js`** -> AI Confidence: **99.39%**
13. **`package/serialization/resources/accounting/types/index.js`** -> AI Confidence: **99.39%**
14. **`package/serialization/resources/ats/types/index.js`** -> AI Confidence: **99.39%**
15. **`package/serialization/resources/crm/types/index.js`** -> AI Confidence: **99.39%**
16. **`package/serialization/resources/filestorage/types/index.js`** -> AI Confidence: **99.39%**
17. **`package/serialization/resources/hris/resources/employees/types/index.js`** -> AI Confidence: **99.39%**
18. **`package/serialization/resources/hris/resources/employments/types/index.js`** -> AI Confidence: **99.39%**
19. **`package/serialization/resources/hris/resources/timeOff/types/index.js`** -> AI Confidence: **99.39%**
20. **`package/serialization/resources/hris/types/index.js`** -> AI Confidence: **99.39%**
21. **`package/serialization/resources/ticketing/resources/tickets/types/index.js`** -> AI Confidence: **99.39%**
22. **`package/serialization/resources/ticketing/types/index.js`** -> AI Confidence: **99.39%**
23. **`package/serialization/resources/accounting/types/Account.d.ts`** -> AI Confidence: **99.31%**
24. **`package/serialization/resources/accounting/types/BalanceSheet.d.ts`** -> AI Confidence: **99.31%**
25. **`package/serialization/resources/accounting/types/BankFeedAccount.d.ts`** -> AI Confidence: **99.31%**
26. **`package/serialization/resources/accounting/types/CashFlowStatement.d.ts`** -> AI Confidence: **99.31%**
27. **`package/serialization/resources/accounting/types/CompanyInfo.d.ts`** -> AI Confidence: **99.31%**
28. **`package/serialization/resources/accounting/types/Contact.d.ts`** -> AI Confidence: **99.31%**
29. **`package/serialization/resources/accounting/types/CreditNote.d.ts`** -> AI Confidence: **99.31%**
30. **`package/serialization/resources/accounting/types/CreditNoteLineItem.d.ts`** -> AI Confidence: **99.31%**
31. **`package/serialization/resources/accounting/types/CreditNoteLineItemRequest.d.ts`** -> AI Confidence: **99.31%**
32. **`package/serialization/resources/accounting/types/Expense.d.ts`** -> AI Confidence: **99.31%**
33. **`package/serialization/resources/accounting/types/ExpenseLine.d.ts`** -> AI Confidence: **99.31%**
34. **`package/serialization/resources/accounting/types/ExpenseLineRequest.d.ts`** -> AI Confidence: **99.31%**
35. **`package/serialization/resources/accounting/types/ExpenseReport.d.ts`** -> AI Confidence: **99.31%**
36. **`package/serialization/resources/accounting/types/ExpenseReportLine.d.ts`** -> AI Confidence: **99.31%**
37. **`package/serialization/resources/accounting/types/ExpenseReportLineRequest.d.ts`** -> AI Confidence: **99.31%**
38. **`package/serialization/resources/accounting/types/ExpenseRequest.d.ts`** -> AI Confidence: **99.31%**
39. **`package/serialization/resources/accounting/types/GeneralLedgerTransaction.d.ts`** -> AI Confidence: **99.31%**
40. **`package/serialization/resources/accounting/types/IncomeStatement.d.ts`** -> AI Confidence: **99.31%**
41. **`package/serialization/resources/accounting/types/Invoice.d.ts`** -> AI Confidence: **99.31%**
42. **`package/serialization/resources/accounting/types/InvoiceLineItem.d.ts`** -> AI Confidence: **99.31%**
43. **`package/serialization/resources/accounting/types/InvoiceLineItemRequest.d.ts`** -> AI Confidence: **99.31%**
44. **`package/serialization/resources/accounting/types/InvoiceRequest.d.ts`** -> AI Confidence: **99.31%**
45. **`package/serialization/resources/accounting/types/Item.d.ts`** -> AI Confidence: **99.31%**
46. **`package/serialization/resources/accounting/types/ItemFulfillment.d.ts`** -> AI Confidence: **99.31%**
47. **`package/serialization/resources/accounting/types/JournalEntry.d.ts`** -> AI Confidence: **99.31%**
48. **`package/serialization/resources/accounting/types/JournalLine.d.ts`** -> AI Confidence: **99.31%**
49. **`package/serialization/resources/accounting/types/JournalLineRequest.d.ts`** -> AI Confidence: **99.31%**
50. **`package/serialization/resources/accounting/types/PatchedPaymentRequest.d.ts`** -> AI Confidence: **99.31%**
51. **`package/serialization/resources/accounting/types/Payment.d.ts`** -> AI Confidence: **99.31%**
52. **`package/serialization/resources/accounting/types/PurchaseOrder.d.ts`** -> AI Confidence: **99.31%**
53. **`package/serialization/resources/accounting/types/PurchaseOrderRequest.d.ts`** -> AI Confidence: **99.31%**
54. **`package/serialization/resources/accounting/types/SalesOrder.d.ts`** -> AI Confidence: **99.31%**
55. **`package/serialization/resources/accounting/types/SalesOrderLine.d.ts`** -> AI Confidence: **99.31%**
56. **`package/serialization/resources/accounting/types/TaxRate.d.ts`** -> AI Confidence: **99.31%**
57. **`package/serialization/resources/accounting/types/Transaction.d.ts`** -> AI Confidence: **99.31%**
58. **`package/serialization/resources/accounting/types/VendorCredit.d.ts`** -> AI Confidence: **99.31%**
59. **`package/serialization/resources/ats/types/Activity.d.ts`** -> AI Confidence: **99.31%**
60. **`package/serialization/resources/ats/types/Application.d.ts`** -> AI Confidence: **99.31%**
61. **`package/serialization/resources/ats/types/Candidate.d.ts`** -> AI Confidence: **99.31%**
62. **`package/serialization/resources/ats/types/CandidateRequest.d.ts`** -> AI Confidence: **99.31%**
63. **`package/serialization/resources/ats/types/Job.d.ts`** -> AI Confidence: **99.31%**
64. **`package/serialization/resources/ats/types/JobPosting.d.ts`** -> AI Confidence: **99.31%**
65. **`package/serialization/resources/ats/types/ScheduledInterview.d.ts`** -> AI Confidence: **99.31%**
66. **`package/serialization/resources/crm/types/Account.d.ts`** -> AI Confidence: **99.31%**
67. **`package/serialization/resources/crm/types/Contact.d.ts`** -> AI Confidence: **99.31%**
68. **`package/serialization/resources/crm/types/Engagement.d.ts`** -> AI Confidence: **99.31%**
69. **`package/serialization/resources/crm/types/Lead.d.ts`** -> AI Confidence: **99.31%**
70. **`package/serialization/resources/crm/types/Note.d.ts`** -> AI Confidence: **99.31%**
71. **`package/serialization/resources/crm/types/Opportunity.d.ts`** -> AI Confidence: **99.31%**
72. **`package/serialization/resources/crm/types/Task.d.ts`** -> AI Confidence: **99.31%**
73. **`package/serialization/resources/filestorage/types/File_.d.ts`** -> AI Confidence: **99.31%**
74. **`package/serialization/resources/hris/types/Employee.d.ts`** -> AI Confidence: **99.31%**
75. **`package/serialization/resources/hris/types/EmployeePayrollRun.d.ts`** -> AI Confidence: **99.31%**
76. **`package/serialization/resources/hris/types/EmployeeRequest.d.ts`** -> AI Confidence: **99.31%**
77. **`package/serialization/resources/hris/types/Employment.d.ts`** -> AI Confidence: **99.31%**
78. **`package/serialization/resources/hris/types/TimeOff.d.ts`** -> AI Confidence: **99.31%**
79. **`package/serialization/resources/ticketing/types/Collection.d.ts`** -> AI Confidence: **99.31%**
80. **`package/serialization/resources/ticketing/types/Comment.d.ts`** -> AI Confidence: **99.31%**
81. **`package/serialization/resources/ticketing/types/PatchedTicketRequest.d.ts`** -> AI Confidence: **99.31%**
82. **`package/serialization/resources/ticketing/types/Ticket.d.ts`** -> AI Confidence: **99.31%**
83. **`package/serialization/resources/ticketing/types/TicketRequest.d.ts`** -> AI Confidence: **99.31%**
84. **`package/api/resources/filestorage/resources/index.js`** -> AI Confidence: **99.31%**
85. **`package/core/index.js`** -> AI Confidence: **99.31%**
86. **`package/core/schemas/builders/object/object.js`** -> AI Confidence: **99.31%**
87. **`package/core/schemas/builders/union/union.js`** -> AI Confidence: **99.31%**
88. **`package/serialization/resources/ats/resources/index.js`** -> AI Confidence: **99.31%**
89. **`package/serialization/resources/crm/resources/index.js`** -> AI Confidence: **99.31%**
90. **`package/serialization/resources/filestorage/resources/index.js`** -> AI Confidence: **99.31%**
91. **`package/serialization/resources/hris/resources/index.js`** -> AI Confidence: **99.31%**
92. **`package/serialization/resources/ticketing/resources/index.js`** -> AI Confidence: **99.31%**
93. **`package/api/resources/accounting/resources/accounts/client/requests/AccountsListRequest.d.ts`** -> AI Confidence: **99.29%**
94. **`package/api/resources/accounting/resources/attachments/client/requests/AttachmentsListRequest.d.ts`** -> AI Confidence: **99.29%**
95. **`package/api/resources/accounting/resources/balanceSheets/client/requests/BalanceSheetsListRequest.d.ts`** -> AI Confidence: **99.29%**
96. **`package/api/resources/accounting/resources/bankFeedTransactions/client/requests/BankFeedTransactionsListRequest.d.ts`** -> AI Confidence: **99.29%**
97. **`package/api/resources/accounting/resources/cashFlowStatements/client/requests/CashFlowStatementsListRequest.d.ts`** -> AI Confidence: **99.29%**
98. **`package/api/resources/accounting/resources/contacts/client/requests/ContactsListRequest.d.ts`** -> AI Confidence: **99.29%**
99. **`package/api/resources/accounting/resources/creditNotes/client/requests/CreditNotesListRequest.d.ts`** -> AI Confidence: **99.29%**
100. **`package/api/resources/accounting/resources/employees/client/requests/EmployeesListRequest.d.ts`** -> AI Confidence: **99.29%**
101. **`package/api/resources/accounting/resources/expenses/client/requests/ExpensesListRequest.d.ts`** -> AI Confidence: **99.29%**
102. **`package/api/resources/accounting/resources/incomeStatements/client/requests/IncomeStatementsListRequest.d.ts`** -> AI Confidence: **99.29%**
103. **`package/api/resources/accounting/resources/journalEntries/client/requests/JournalEntriesListRequest.d.ts`** -> AI Confidence: **99.29%**
104. **`package/api/resources/accounting/resources/payments/client/requests/PaymentsListRequest.d.ts`** -> AI Confidence: **99.29%**
105. **`package/api/resources/accounting/resources/purchaseOrders/client/requests/PurchaseOrdersListRequest.d.ts`** -> AI Confidence: **99.29%**
106. **`package/api/resources/accounting/resources/salesOrders/client/requests/SalesOrdersListRequest.d.ts`** -> AI Confidence: **99.29%**
107. **`package/api/resources/accounting/resources/taxRates/client/requests/TaxRatesListRequest.d.ts`** -> AI Confidence: **99.29%**
108. **`package/api/resources/accounting/resources/trackingCategories/client/requests/TrackingCategoriesListRequest.d.ts`** -> AI Confidence: **99.29%**
109. **`package/api/resources/accounting/types/Account.d.ts`** -> AI Confidence: **99.29%**
110. **`package/api/resources/accounting/types/BalanceSheet.d.ts`** -> AI Confidence: **99.29%**
111. **`package/api/resources/accounting/types/BankFeedAccount.d.ts`** -> AI Confidence: **99.29%**
112. **`package/api/resources/accounting/types/BankFeedTransaction.d.ts`** -> AI Confidence: **99.29%**
113. **`package/api/resources/accounting/types/CashFlowStatement.d.ts`** -> AI Confidence: **99.29%**
114. **`package/api/resources/accounting/types/CompanyInfo.d.ts`** -> AI Confidence: **99.29%**
115. **`package/api/resources/accounting/types/Contact.d.ts`** -> AI Confidence: **99.29%**
116. **`package/api/resources/accounting/types/ContactRequest.d.ts`** -> AI Confidence: **99.29%**
117. **`package/api/resources/accounting/types/CreditNote.d.ts`** -> AI Confidence: **99.29%**
118. **`package/api/resources/accounting/types/CreditNoteRequest.d.ts`** -> AI Confidence: **99.29%**
119. **`package/api/resources/accounting/types/Expense.d.ts`** -> AI Confidence: **99.29%**
120. **`package/api/resources/accounting/types/ExpenseLine.d.ts`** -> AI Confidence: **99.29%**
121. **`package/api/resources/accounting/types/ExpenseReport.d.ts`** -> AI Confidence: **99.29%**
122. **`package/api/resources/accounting/types/ExpenseReportLine.d.ts`** -> AI Confidence: **99.29%**
123. **`package/api/resources/accounting/types/ExpenseReportLineRequest.d.ts`** -> AI Confidence: **99.29%**
124. **`package/api/resources/accounting/types/ExpenseRequest.d.ts`** -> AI Confidence: **99.29%**
125. **`package/api/resources/accounting/types/ExternalTargetFieldApiResponse.d.ts`** -> AI Confidence: **99.29%**
126. **`package/api/resources/accounting/types/FieldMappingApiInstanceResponse.d.ts`** -> AI Confidence: **99.29%**
127. **`package/api/resources/accounting/types/GeneralLedgerTransaction.d.ts`** -> AI Confidence: **99.29%**
128. **`package/api/resources/accounting/types/GeneralLedgerTransactionLine.d.ts`** -> AI Confidence: **99.29%**
129. **`package/api/resources/accounting/types/IncomeStatement.d.ts`** -> AI Confidence: **99.29%**
130. **`package/api/resources/accounting/types/Invoice.d.ts`** -> AI Confidence: **99.29%**
131. **`package/api/resources/accounting/types/InvoiceLineItem.d.ts`** -> AI Confidence: **99.29%**
132. **`package/api/resources/accounting/types/InvoiceLineItemRequest.d.ts`** -> AI Confidence: **99.29%**
133. **`package/api/resources/accounting/types/InvoiceRequest.d.ts`** -> AI Confidence: **99.29%**
134. **`package/api/resources/accounting/types/ItemRequestRequest.d.ts`** -> AI Confidence: **99.29%**
135. **`package/api/resources/accounting/types/JournalEntry.d.ts`** -> AI Confidence: **99.29%**
136. **`package/api/resources/accounting/types/JournalLine.d.ts`** -> AI Confidence: **99.29%**
137. **`package/api/resources/accounting/types/PatchedContactRequest.d.ts`** -> AI Confidence: **99.29%**
138. **`package/api/resources/accounting/types/PatchedItemRequestRequest.d.ts`** -> AI Confidence: **99.29%**
139. **`package/api/resources/accounting/types/PatchedPaymentRequest.d.ts`** -> AI Confidence: **99.29%**
140. **`package/api/resources/accounting/types/PatchedVendorCreditRequest.d.ts`** -> AI Confidence: **99.29%**
141. **`package/api/resources/accounting/types/Payment.d.ts`** -> AI Confidence: **99.29%**
142. **`package/api/resources/accounting/types/PaymentLineItem.d.ts`** -> AI Confidence: **99.29%**
143. **`package/api/resources/accounting/types/PaymentRequest.d.ts`** -> AI Confidence: **99.29%**
144. **`package/api/resources/accounting/types/PurchaseOrder.d.ts`** -> AI Confidence: **99.29%**
145. **`package/api/resources/accounting/types/PurchaseOrderLineItem.d.ts`** -> AI Confidence: **99.29%**
146. **`package/api/resources/accounting/types/PurchaseOrderRequest.d.ts`** -> AI Confidence: **99.29%**
147. **`package/api/resources/accounting/types/RemoteFieldApiResponse.d.ts`** -> AI Confidence: **99.29%**
148. **`package/api/resources/accounting/types/ReportItem.d.ts`** -> AI Confidence: **99.29%**
149. **`package/api/resources/accounting/types/SalesOrderRequestRequest.d.ts`** -> AI Confidence: **99.29%**
150. **`package/api/resources/accounting/types/TaxRate.d.ts`** -> AI Confidence: **99.29%**
151. **`package/api/resources/accounting/types/Transaction.d.ts`** -> AI Confidence: **99.29%**
152. **`package/api/resources/accounting/types/VendorCredit.d.ts`** -> AI Confidence: **99.29%**
153. **`package/api/resources/accounting/types/VendorCreditRequest.d.ts`** -> AI Confidence: **99.29%**
154. **`package/api/resources/ats/resources/applications/client/requests/ApplicationsListRequest.d.ts`** -> AI Confidence: **99.29%**
155. **`package/api/resources/ats/resources/attachments/client/requests/AttachmentsListRequest.d.ts`** -> AI Confidence: **99.29%**
156. **`package/api/resources/ats/resources/candidates/client/requests/CandidatesListRequest.d.ts`** -> AI Confidence: **99.29%**
157. **`package/api/resources/ats/resources/departments/client/requests/DepartmentsListRequest.d.ts`** -> AI Confidence: **99.29%**
158. **`package/api/resources/ats/resources/interviews/client/requests/InterviewsListRequest.d.ts`** -> AI Confidence: **99.29%**
159. **`package/api/resources/ats/resources/jobInterviewStages/client/requests/JobInterviewStagesListRequest.d.ts`** -> AI Confidence: **99.29%**
160. **`package/api/resources/ats/resources/offices/client/requests/OfficesListRequest.d.ts`** -> AI Confidence: **99.29%**
161. **`package/api/resources/ats/resources/rejectReasons/client/requests/RejectReasonsListRequest.d.ts`** -> AI Confidence: **99.29%**
162. **`package/api/resources/ats/resources/scorecards/client/requests/ScorecardsListRequest.d.ts`** -> AI Confidence: **99.29%**
163. **`package/api/resources/ats/resources/tags/client/requests/TagsListRequest.d.ts`** -> AI Confidence: **99.29%**
164. **`package/api/resources/ats/resources/users/client/requests/UsersListRequest.d.ts`** -> AI Confidence: **99.29%**
165. **`package/api/resources/ats/types/Candidate.d.ts`** -> AI Confidence: **99.29%**
166. **`package/api/resources/ats/types/CandidateRequest.d.ts`** -> AI Confidence: **99.29%**
167. **`package/api/resources/ats/types/ExternalTargetFieldApiResponse.d.ts`** -> AI Confidence: **99.29%**
168. **`package/api/resources/ats/types/FieldMappingApiInstanceResponse.d.ts`** -> AI Confidence: **99.29%**
169. **`package/api/resources/ats/types/Job.d.ts`** -> AI Confidence: **99.29%**
170. **`package/api/resources/ats/types/Offer.d.ts`** -> AI Confidence: **99.29%**
171. **`package/api/resources/ats/types/PatchedCandidateRequest.d.ts`** -> AI Confidence: **99.29%**
172. **`package/api/resources/ats/types/RemoteFieldApiResponse.d.ts`** -> AI Confidence: **99.29%**
173. **`package/api/resources/crm/resources/accounts/client/requests/AccountsListRequest.d.ts`** -> AI Confidence: **99.29%**
174. **`package/api/resources/crm/resources/accounts/client/requests/AccountsRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.29%**
175. **`package/api/resources/crm/resources/associationTypes/client/requests/CustomObjectClassesAssociationTypesListRequest.d.ts`** -> AI Confidence: **99.29%**
176. **`package/api/resources/crm/resources/associations/client/requests/CustomObjectClassesCustomObjectsAssociationsListRequest.d.ts`** -> AI Confidence: **99.29%**
177. **`package/api/resources/crm/resources/contacts/client/requests/ContactsListRequest.d.ts`** -> AI Confidence: **99.29%**
178. **`package/api/resources/crm/resources/contacts/client/requests/ContactsRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.29%**
179. **`package/api/resources/crm/resources/customObjectClasses/client/requests/CustomObjectClassesListRequest.d.ts`** -> AI Confidence: **99.29%**
180. **`package/api/resources/crm/resources/customObjects/client/requests/CustomObjectClassesCustomObjectsListRequest.d.ts`** -> AI Confidence: **99.29%**
181. **`package/api/resources/crm/resources/customObjects/client/requests/CustomObjectClassesCustomObjectsRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.29%**
182. **`package/api/resources/crm/resources/engagementTypes/client/requests/EngagementTypesListRequest.d.ts`** -> AI Confidence: **99.29%**
183. **`package/api/resources/crm/resources/engagementTypes/client/requests/EngagementTypesRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.29%**
184. **`package/api/resources/crm/resources/engagements/client/requests/EngagementsRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.29%**
185. **`package/api/resources/crm/resources/leads/client/requests/LeadsListRequest.d.ts`** -> AI Confidence: **99.29%**
186. **`package/api/resources/crm/resources/leads/client/requests/LeadsRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.29%**
187. **`package/api/resources/crm/resources/notes/client/requests/NotesListRequest.d.ts`** -> AI Confidence: **99.29%**
188. **`package/api/resources/crm/resources/notes/client/requests/NotesRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.29%**
189. **`package/api/resources/crm/resources/opportunities/client/requests/OpportunitiesListRequest.d.ts`** -> AI Confidence: **99.29%**
190. **`package/api/resources/crm/resources/opportunities/client/requests/OpportunitiesRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.29%**
191. **`package/api/resources/crm/resources/stages/client/requests/StagesListRequest.d.ts`** -> AI Confidence: **99.29%**
192. **`package/api/resources/crm/resources/stages/client/requests/StagesRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.29%**
193. **`package/api/resources/crm/resources/tasks/client/requests/TasksRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.29%**
194. **`package/api/resources/crm/resources/users/client/requests/UsersListRequest.d.ts`** -> AI Confidence: **99.29%**
195. **`package/api/resources/crm/resources/users/client/requests/UsersRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.29%**
196. **`package/api/resources/crm/types/Account.d.ts`** -> AI Confidence: **99.29%**
197. **`package/api/resources/crm/types/EmailAddress.d.ts`** -> AI Confidence: **99.29%**
198. **`package/api/resources/crm/types/EmailAddressRequest.d.ts`** -> AI Confidence: **99.29%**
199. **`package/api/resources/crm/types/Engagement.d.ts`** -> AI Confidence: **99.29%**
200. **`package/api/resources/crm/types/Lead.d.ts`** -> AI Confidence: **99.29%**
201. **`package/api/resources/crm/types/Opportunity.d.ts`** -> AI Confidence: **99.29%**
202. **`package/api/resources/crm/types/PhoneNumber.d.ts`** -> AI Confidence: **99.29%**
203. **`package/api/resources/crm/types/PhoneNumberRequest.d.ts`** -> AI Confidence: **99.29%**
204. **`package/api/resources/filestorage/resources/drives/client/requests/DrivesListRequest.d.ts`** -> AI Confidence: **99.29%**
205. **`package/api/resources/filestorage/resources/files/client/requests/FilesListRequest.d.ts`** -> AI Confidence: **99.29%**
206. **`package/api/resources/filestorage/resources/users/client/requests/UsersListRequest.d.ts`** -> AI Confidence: **99.29%**
207. **`package/api/resources/hris/resources/bankInfo/client/requests/BankInfoListRequest.d.ts`** -> AI Confidence: **99.29%**
208. **`package/api/resources/hris/resources/benefits/client/requests/BenefitsListRequest.d.ts`** -> AI Confidence: **99.29%**
209. **`package/api/resources/hris/resources/companies/client/requests/CompaniesListRequest.d.ts`** -> AI Confidence: **99.29%**
210. **`package/api/resources/hris/resources/dependents/client/requests/DependentsListRequest.d.ts`** -> AI Confidence: **99.29%**
211. **`package/api/resources/hris/resources/employeePayrollRuns/client/requests/EmployeePayrollRunsListRequest.d.ts`** -> AI Confidence: **99.29%**
212. **`package/api/resources/hris/resources/employees/client/requests/EmployeesListRequest.d.ts`** -> AI Confidence: **99.29%**
213. **`package/api/resources/hris/resources/employerBenefits/client/requests/EmployerBenefitsListRequest.d.ts`** -> AI Confidence: **99.29%**
214. **`package/api/resources/hris/resources/payGroups/client/requests/PayGroupsListRequest.d.ts`** -> AI Confidence: **99.29%**
215. **`package/api/resources/hris/resources/payrollRuns/client/requests/PayrollRunsListRequest.d.ts`** -> AI Confidence: **99.29%**
216. **`package/api/resources/hris/resources/teams/client/requests/TeamsListRequest.d.ts`** -> AI Confidence: **99.29%**
217. **`package/api/resources/hris/resources/timeOff/client/requests/TimeOffListRequest.d.ts`** -> AI Confidence: **99.29%**
218. **`package/api/resources/hris/resources/timesheetEntries/client/requests/TimesheetEntriesListRequest.d.ts`** -> AI Confidence: **99.29%**
219. **`package/api/resources/hris/types/Employee.d.ts`** -> AI Confidence: **99.29%**
220. **`package/api/resources/hris/types/EmployeePayrollRun.d.ts`** -> AI Confidence: **99.29%**
221. **`package/api/resources/hris/types/EmployeeRequest.d.ts`** -> AI Confidence: **99.29%**
222. **`package/api/resources/hris/types/ExternalTargetFieldApiResponse.d.ts`** -> AI Confidence: **99.29%**
223. **`package/api/resources/hris/types/FieldMappingApiInstanceResponse.d.ts`** -> AI Confidence: **99.29%**
224. **`package/api/resources/hris/types/RemoteFieldApiResponse.d.ts`** -> AI Confidence: **99.29%**
225. **`package/api/resources/hris/types/TimeOff.d.ts`** -> AI Confidence: **99.29%**
226. **`package/api/resources/ticketing/resources/accounts/client/requests/AccountsListRequest.d.ts`** -> AI Confidence: **99.29%**
227. **`package/api/resources/ticketing/resources/attachments/client/requests/AttachmentsListRequest.d.ts`** -> AI Confidence: **99.29%**
228. **`package/api/resources/ticketing/resources/collections/client/requests/CollectionsListRequest.d.ts`** -> AI Confidence: **99.29%**
229. **`package/api/resources/ticketing/resources/contacts/client/requests/ContactsListRequest.d.ts`** -> AI Confidence: **99.29%**
230. **`package/api/resources/ticketing/resources/projects/client/requests/ProjectsListRequest.d.ts`** -> AI Confidence: **99.29%**
231. **`package/api/resources/ticketing/resources/roles/client/requests/RolesListRequest.d.ts`** -> AI Confidence: **99.29%**
232. **`package/api/resources/ticketing/resources/tags/client/requests/TagsListRequest.d.ts`** -> AI Confidence: **99.29%**
233. **`package/api/resources/ticketing/resources/teams/client/requests/TeamsListRequest.d.ts`** -> AI Confidence: **99.29%**
234. **`package/api/resources/ticketing/resources/tickets/client/requests/TicketsListRequest.d.ts`** -> AI Confidence: **99.29%**
235. **`package/api/resources/ticketing/resources/tickets/client/requests/TicketsRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.29%**
236. **`package/api/resources/ticketing/resources/users/client/requests/UsersListRequest.d.ts`** -> AI Confidence: **99.29%**
237. **`package/api/resources/ticketing/types/PatchedTicketRequest.d.ts`** -> AI Confidence: **99.29%**
238. **`package/api/resources/ticketing/types/Ticket.d.ts`** -> AI Confidence: **99.29%**
239. **`package/api/resources/ticketing/types/TicketRequest.d.ts`** -> AI Confidence: **99.29%**
240. **`package/core/runtime/runtime.js`** -> AI Confidence: **99.29%**
241. **`package/core/url/qs.js`** -> AI Confidence: **99.29%**
242. **`package/serialization/resources/accounting/types/CreditNoteRequest.d.ts`** -> AI Confidence: **99.24%**
243. **`package/serialization/resources/accounting/types/ExpenseReportRequest.d.ts`** -> AI Confidence: **99.24%**
244. **`package/serialization/resources/accounting/types/GeneralLedgerTransactionLine.d.ts`** -> AI Confidence: **99.24%**
245. **`package/serialization/resources/accounting/types/ItemFulfillmentLineRequest.d.ts`** -> AI Confidence: **99.24%**
246. **`package/serialization/resources/accounting/types/JournalEntryRequest.d.ts`** -> AI Confidence: **99.24%**
247. **`package/serialization/resources/accounting/types/PaymentRequest.d.ts`** -> AI Confidence: **99.24%**
248. **`package/serialization/resources/accounting/types/SalesOrderRequestRequest.d.ts`** -> AI Confidence: **99.24%**
249. **`package/serialization/resources/ats/types/ApplicationRequest.d.ts`** -> AI Confidence: **99.24%**
250. **`package/serialization/resources/crm/types/ContactRequest.d.ts`** -> AI Confidence: **99.24%**
251. **`package/serialization/resources/crm/types/EngagementRequest.d.ts`** -> AI Confidence: **99.24%**
252. **`package/serialization/resources/crm/types/LeadRequest.d.ts`** -> AI Confidence: **99.24%**
253. **`package/serialization/resources/crm/types/PatchedContactRequest.d.ts`** -> AI Confidence: **99.24%**
254. **`package/serialization/resources/crm/types/RemoteFieldClassForCustomObjectClass.d.ts`** -> AI Confidence: **99.24%**
255. **`package/serialization/resources/crm/types/TaskRequest.d.ts`** -> AI Confidence: **99.24%**
256. **`package/serialization/resources/hris/resources/linkToken/client/requests/EndUserDetailsRequest.d.ts`** -> AI Confidence: **99.24%**
257. **`package/serialization/resources/hris/types/TimeOffRequest.d.ts`** -> AI Confidence: **99.24%**
258. **`package/index.js`** -> AI Confidence: **99.24%**
259. **`package/serialization/resources/accounting/resources/linkToken/client/requests/EndUserDetailsRequest.d.ts`** -> AI Confidence: **99.23%**
260. **`package/serialization/resources/accounting/types/AccountRequest.d.ts`** -> AI Confidence: **99.23%**
261. **`package/serialization/resources/accounting/types/ContactRequest.d.ts`** -> AI Confidence: **99.23%**
262. **`package/serialization/resources/accounting/types/ItemFulfillmentLine.d.ts`** -> AI Confidence: **99.23%**
263. **`package/serialization/resources/accounting/types/PatchedContactRequest.d.ts`** -> AI Confidence: **99.23%**
264. **`package/serialization/resources/accounting/types/SalesOrderLineRequest.d.ts`** -> AI Confidence: **99.23%**
265. **`package/serialization/resources/accounting/types/VendorCreditRequest.d.ts`** -> AI Confidence: **99.23%**
266. **`package/serialization/resources/ats/types/Eeoc.d.ts`** -> AI Confidence: **99.23%**
267. **`package/serialization/resources/ats/types/Scorecard.d.ts`** -> AI Confidence: **99.23%**
268. **`package/serialization/resources/crm/types/OpportunityRequest.d.ts`** -> AI Confidence: **99.23%**
269. **`package/serialization/resources/crm/types/RemoteFieldClass.d.ts`** -> AI Confidence: **99.23%**
270. **`package/serialization/resources/ticketing/types/RemoteFieldClass.d.ts`** -> AI Confidence: **99.23%**
271. **`package/api/resources/hris/resources/locations/types/index.js`** -> AI Confidence: **99.23%**
272. **`package/api/resources/hris/resources/payrollRuns/types/index.js`** -> AI Confidence: **99.23%**
273. **`package/serialization/resources/hris/resources/locations/types/index.js`** -> AI Confidence: **99.23%**
274. **`package/serialization/resources/hris/resources/payrollRuns/types/index.js`** -> AI Confidence: **99.23%**
275. **`package/api/resources/accounting/resources/accounts/types/index.js`** -> AI Confidence: **99.22%**
276. **`package/api/resources/accounting/resources/creditNotes/types/index.js`** -> AI Confidence: **99.22%**
277. **`package/serialization/resources/accounting/resources/accounts/types/index.js`** -> AI Confidence: **99.22%**
278. **`package/serialization/resources/accounting/resources/creditNotes/types/index.js`** -> AI Confidence: **99.22%**
279. **`package/api/resources/accounting/index.js`** -> AI Confidence: **99.2%**
280. **`package/api/resources/accounting/resources/contacts/types/index.js`** -> AI Confidence: **99.2%**
281. **`package/api/resources/accounting/resources/expenseReports/types/index.js`** -> AI Confidence: **99.2%**
282. **`package/api/resources/ats/index.js`** -> AI Confidence: **99.2%**
283. **`package/api/resources/ats/resources/offers/types/index.js`** -> AI Confidence: **99.2%**
284. **`package/api/resources/crm/index.js`** -> AI Confidence: **99.2%**
285. **`package/api/resources/crm/resources/opportunities/types/index.js`** -> AI Confidence: **99.2%**
286. **`package/api/resources/filestorage/index.js`** -> AI Confidence: **99.2%**
287. **`package/api/resources/hris/index.js`** -> AI Confidence: **99.2%**
288. **`package/api/resources/ticketing/index.js`** -> AI Confidence: **99.2%**
289. **`package/serialization/resources/accounting/resources/contacts/types/index.js`** -> AI Confidence: **99.2%**
290. **`package/serialization/resources/accounting/resources/expenseReports/types/index.js`** -> AI Confidence: **99.2%**
291. **`package/serialization/resources/ats/resources/offers/types/index.js`** -> AI Confidence: **99.2%**
292. **`package/serialization/resources/crm/resources/opportunities/types/index.js`** -> AI Confidence: **99.2%**
293. **`package/api/resources/accounting/resources/accountingPeriods/client/requests/AccountingPeriodsListRequest.d.ts`** -> AI Confidence: **99.17%**
294. **`package/api/resources/accounting/resources/bankFeedAccounts/client/requests/BankFeedAccountsListRequest.d.ts`** -> AI Confidence: **99.17%**
295. **`package/api/resources/accounting/resources/companyInfo/client/requests/CompanyInfoListRequest.d.ts`** -> AI Confidence: **99.17%**
296. **`package/api/resources/accounting/resources/contacts/client/requests/ContactsRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.17%**
297. **`package/api/resources/accounting/resources/expenseReports/client/requests/ExpenseReportsLinesRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.17%**
298. **`package/api/resources/accounting/resources/expenseReports/client/requests/ExpenseReportsListRequest.d.ts`** -> AI Confidence: **99.17%**
299. **`package/api/resources/accounting/resources/expenseReports/client/requests/ExpenseReportsRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.17%**
300. **`package/api/resources/accounting/resources/expenses/client/requests/ExpensesLinesRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.17%**
301. **`package/api/resources/accounting/resources/expenses/client/requests/ExpensesRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.17%**
302. **`package/api/resources/accounting/resources/fieldMapping/client/requests/PatchedEditFieldMappingRequest.d.ts`** -> AI Confidence: **99.17%**
303. **`package/api/resources/accounting/resources/generalLedgerTransactions/client/requests/GeneralLedgerTransactionsListRequest.d.ts`** -> AI Confidence: **99.17%**
304. **`package/api/resources/accounting/resources/invoices/client/requests/InvoicesLineItemsRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.17%**
305. **`package/api/resources/accounting/resources/invoices/client/requests/InvoicesListRequest.d.ts`** -> AI Confidence: **99.17%**
306. **`package/api/resources/accounting/resources/invoices/client/requests/InvoicesRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.17%**
307. **`package/api/resources/accounting/resources/issues/client/requests/IssuesListRequest.d.ts`** -> AI Confidence: **99.17%**
308. **`package/api/resources/accounting/resources/itemFulfillments/client/requests/ItemFulfillmentsLinesRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.17%**
309. **`package/api/resources/accounting/resources/itemFulfillments/client/requests/ItemFulfillmentsRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.17%**
310. **`package/api/resources/accounting/resources/items/client/requests/ItemsListRequest.d.ts`** -> AI Confidence: **99.17%**
311. **`package/api/resources/accounting/resources/journalEntries/client/requests/JournalEntriesLinesRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.17%**
312. **`package/api/resources/accounting/resources/journalEntries/client/requests/JournalEntriesRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.17%**
313. **`package/api/resources/accounting/resources/linkToken/client/requests/EndUserDetailsRequest.d.ts`** -> AI Confidence: **99.17%**
314. **`package/api/resources/accounting/resources/linkedAccounts/client/requests/LinkedAccountsListRequest.d.ts`** -> AI Confidence: **99.17%**
315. **`package/api/resources/accounting/resources/paymentMethods/client/requests/PaymentMethodsListRequest.d.ts`** -> AI Confidence: **99.17%**
316. **`package/api/resources/accounting/resources/paymentTerms/client/requests/PaymentTermsListRequest.d.ts`** -> AI Confidence: **99.17%**
317. **`package/api/resources/accounting/resources/payments/client/requests/PaymentsLineItemsRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.17%**
318. **`package/api/resources/accounting/resources/payments/client/requests/PaymentsRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.17%**
319. **`package/api/resources/accounting/resources/projects/client/requests/ProjectsListRequest.d.ts`** -> AI Confidence: **99.17%**
320. **`package/api/resources/accounting/resources/purchaseOrders/client/requests/PurchaseOrdersLineItemsRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.17%**
321. **`package/api/resources/accounting/resources/purchaseOrders/client/requests/PurchaseOrdersRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.17%**
322. **`package/api/resources/accounting/resources/salesOrders/client/requests/SalesOrdersLinesRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.17%**
323. **`package/api/resources/accounting/resources/salesOrders/client/requests/SalesOrdersRemoteFieldClassesListRequest.d.ts`** -> AI Confidence: **99.17%**
324. **`package/api/resources/accounting/resources/trackingCategories/client/requests/TrackingCategoriesRetrieveRequest.d.ts`** -> AI Confidence: **99.17%**
325. **`package/api/resources/accounting/resources/transactions/client/requests/TransactionsListRequest.d.ts`** -> AI Confidence: **99.17%**
326. **`package/api/resources/accounting/resources/vendorCredits/client/requests/VendorCreditsListRequest.d.ts`** -> AI Confidence: **99.17%**
327. **`package/api/resources/accounting/types/AccountDetails.d.ts`** -> AI Confidence: **99.17%**
328. **`package/api/resources/accounting/types/AccountRequest.d.ts`** -> AI Confidence: **99.17%**
329. **`package/api/resources/accounting/types/AccountingPeriod.d.ts`** -> AI Confidence: **99.17%**
330. **`package/api/resources/accounting/types/AccountingPhoneNumberRequest.d.ts`** -> AI Confidence: **99.17%**
331. **`package/api/resources/accounting/types/Address.d.ts`** -> AI Confidence: **99.17%**
332. **`package/api/resources/accounting/types/AddressRequest.d.ts`** -> AI Confidence: **99.17%**
333. **`package/api/resources/accounting/types/AdvancedMetadata.d.ts`** -> AI Confidence: **99.17%**
334. **`package/api/resources/accounting/types/BankFeedAccountRequest.d.ts`** -> AI Confidence: **99.17%**
335. **`package/api/resources/accounting/types/BankFeedTransactionRequestRequest.d.ts`** -> AI Confidence: **99.17%**
336. **`package/api/resources/accounting/types/CreditNoteLineItem.d.ts`** -> AI Confidence: **99.17%**
337. **`package/api/resources/accounting/types/CreditNoteLineItemRequest.d.ts`** -> AI Confidence: **99.17%**
338. **`package/api/resources/accounting/types/Employee.d.ts`** -> AI Confidence: **99.17%**
339. **`package/api/resources/accounting/types/ExpenseLineRequest.d.ts`** -> AI Confidence: **99.17%**
340. **`package/api/resources/accounting/types/ExpenseReportRequest.d.ts`** -> AI Confidence: **99.17%**
341. **`package/api/resources/accounting/types/ItemFulfillment.d.ts`** -> AI Confidence: **99.17%**
342. **`package/api/resources/accounting/types/ItemFulfillmentLineRequest.d.ts`** -> AI Confidence: **99.17%**
343. **`package/api/resources/accounting/types/ItemFulfillmentRequestRequest.d.ts`** -> AI Confidence: **99.17%**
344. **`package/api/resources/accounting/types/JournalEntryRequest.d.ts`** -> AI Confidence: **99.17%**
345. **`package/api/resources/accounting/types/JournalLineRequest.d.ts`** -> AI Confidence: **99.17%**
346. **`package/api/resources/accounting/types/PaymentTerm.d.ts`** -> AI Confidence: **99.17%**
347. **`package/api/resources/accounting/types/PurchaseOrderLineItemRequest.d.ts`** -> AI Confidence: **99.17%**
348. **`package/api/resources/accounting/types/RemoteFieldClass.d.ts`** -> AI Confidence: **99.17%**
349. **`package/api/resources/accounting/types/SalesOrder.d.ts`** -> AI Confidence: **99.17%**
350. **`package/api/resources/accounting/types/SalesOrderLineRequest.d.ts`** -> AI Confidence: **99.17%**
351. **`package/api/resources/accounting/types/TrackingCategory.d.ts`** -> AI Confidence: **99.17%**
352. **`package/api/resources/accounting/types/TransactionLineItem.d.ts`** -> AI Confidence: **99.17%**
353. **`package/api/resources/accounting/types/VendorCreditLine.d.ts`** -> AI Confidence: **99.17%**
354. **`package/api/resources/accounting/types/VendorCreditLineRequest.d.ts`** -> AI Confidence: **99.17%**
355. **`package/api/resources/ats/resources/activities/client/requests/ActivitiesListRequest.d.ts`** -> AI Confidence: **99.17%**
356. **`package/api/resources/ats/resources/attachments/client/requests/AttachmentsRetrieveRequest.d.ts`** -> AI Confidence: **99.17%**
357. **`package/api/resources/ats/resources/eeocs/client/requests/EeocsListRequest.d.ts`** -> AI Confidence: **99.17%**
358. **`package/api/resources/ats/resources/fieldMapping/client/requests/PatchedEditFieldMappingRequest.d.ts`** -> AI Confidence: **99.17%**
359. **`package/api/resources/ats/resources/issues/client/requests/IssuesListRequest.d.ts`** -> AI Confidence: **99.17%**
360. **`package/api/resources/ats/resources/jobPostings/client/requests/JobPostingsListRequest.d.ts`** -> AI Confidence: **99.17%**
361. **`package/api/resources/ats/resources/jobs/client/requests/JobsListRequest.d.ts`** -> AI Confidence: **99.17%**
362. **`package/api/resources/ats/resources/linkedAccounts/client/requests/LinkedAccountsListRequest.d.ts`** -> AI Confidence: **99.17%**
363. **`package/api/resources/ats/resources/offers/client/requests/OffersListRequest.d.ts`** -> AI Confidence: **99.17%**
364. **`package/api/resources/ats/types/AccountDetails.d.ts`** -> AI Confidence: **99.17%**
365. **`package/api/resources/ats/types/Activity.d.ts`** -> AI Confidence: **99.17%**
366. **`package/api/resources/ats/types/AdvancedMetadata.d.ts`** -> AI Confidence: **99.17%**
367. **`package/api/resources/ats/types/Application.d.ts`** -> AI Confidence: **99.17%**
368. **`package/api/resources/ats/types/ApplicationRequest.d.ts`** -> AI Confidence: **99.17%**
369. **`package/api/resources/ats/types/Attachment.d.ts`** -> AI Confidence: **99.17%**
370. **`package/api/resources/ats/types/Eeoc.d.ts`** -> AI Confidence: **99.17%**
371. **`package/api/resources/ats/types/JobInterviewStage.d.ts`** -> AI Confidence: **99.17%**
372. **`package/api/resources/ats/types/JobPosting.d.ts`** -> AI Confidence: **99.17%**
373. **`package/api/resources/ats/types/RemoteUser.d.ts`** -> AI Confidence: **99.17%**
374. **`package/api/resources/ats/types/ScheduledInterview.d.ts`** -> AI Confidence: **99.17%**
375. **`package/api/resources/ats/types/Scorecard.d.ts`** -> AI Confidence: **99.17%**
376. **`package/api/resources/ats/types/ScreeningQuestionOption.d.ts`** -> AI Confidence: **99.17%**
377. **`package/api/resources/ats/types/Tag.d.ts`** -> AI Confidence: **99.17%**
378. **`package/api/resources/crm/resources/engagements/client/requests/EngagementsListRequest.d.ts`** -> AI Confidence: **99.17%**
379. **`package/api/resources/crm/resources/fieldMapping/client/requests/PatchedEditFieldMappingRequest.d.ts`** -> AI Confidence: **99.17%**
380. **`package/api/resources/crm/resources/issues/client/requests/IssuesListRequest.d.ts`** -> AI Confidence: **99.17%**
381. **`package/api/resources/crm/resources/linkedAccounts/client/requests/LinkedAccountsListRequest.d.ts`** -> AI Confidence: **99.17%**
382. **`package/api/resources/crm/resources/tasks/client/requests/TasksListRequest.d.ts`** -> AI Confidence: **99.17%**
383. **`package/api/resources/crm/types/AccountDetails.d.ts`** -> AI Confidence: **99.17%**
384. **`package/api/resources/crm/types/Address.d.ts`** -> AI Confidence: **99.17%**
385. **`package/api/resources/crm/types/AddressRequest.d.ts`** -> AI Confidence: **99.17%**
386. **`package/api/resources/crm/types/AdvancedMetadata.d.ts`** -> AI Confidence: **99.17%**
387. **`package/api/resources/crm/types/AssociationType.d.ts`** -> AI Confidence: **99.17%**
388. **`package/api/resources/crm/types/Contact.d.ts`** -> AI Confidence: **99.17%**
389. **`package/api/resources/crm/types/EngagementRequest.d.ts`** -> AI Confidence: **99.17%**
390. **`package/api/resources/crm/types/LeadRequest.d.ts`** -> AI Confidence: **99.17%**
391. **`package/api/resources/crm/types/Note.d.ts`** -> AI Confidence: **99.17%**
392. **`package/api/resources/crm/types/PatchedEngagementRequest.d.ts`** -> AI Confidence: **99.17%**
393. **`package/api/resources/crm/types/RemoteFieldClass.d.ts`** -> AI Confidence: **99.17%**
394. **`package/api/resources/crm/types/RemoteFieldClassForCustomObjectClass.d.ts`** -> AI Confidence: **99.17%**
395. **`package/api/resources/crm/types/Task.d.ts`** -> AI Confidence: **99.17%**
396. **`package/api/resources/crm/types/User.d.ts`** -> AI Confidence: **99.17%**
397. **`package/api/resources/filestorage/resources/fieldMapping/client/requests/PatchedEditFieldMappingRequest.d.ts`** -> AI Confidence: **99.17%**
398. **`package/api/resources/filestorage/resources/files/client/requests/FilesDownloadRequestMetaListRequest.d.ts`** -> AI Confidence: **99.17%**
399. **`package/api/resources/filestorage/resources/folders/client/requests/FoldersListRequest.d.ts`** -> AI Confidence: **99.17%**
400. **`package/api/resources/filestorage/resources/groups/client/requests/GroupsListRequest.d.ts`** -> AI Confidence: **99.17%**
401. **`package/api/resources/filestorage/resources/issues/client/requests/IssuesListRequest.d.ts`** -> AI Confidence: **99.17%**
402. **`package/api/resources/filestorage/resources/linkedAccounts/client/requests/LinkedAccountsListRequest.d.ts`** -> AI Confidence: **99.17%**
403. **`package/api/resources/filestorage/types/AccountDetails.d.ts`** -> AI Confidence: **99.17%**
404. **`package/api/resources/filestorage/types/AdvancedMetadata.d.ts`** -> AI Confidence: **99.17%**
405. **`package/api/resources/filestorage/types/Drive.d.ts`** -> AI Confidence: **99.17%**
406. **`package/api/resources/filestorage/types/File_.d.ts`** -> AI Confidence: **99.17%**
407. **`package/api/resources/filestorage/types/Folder.d.ts`** -> AI Confidence: **99.17%**
408. **`package/api/resources/hris/resources/bankInfo/client/requests/BankInfoRetrieveRequest.d.ts`** -> AI Confidence: **99.17%**
409. **`package/api/resources/hris/resources/employments/client/requests/EmploymentsListRequest.d.ts`** -> AI Confidence: **99.17%**
410. **`package/api/resources/hris/resources/fieldMapping/client/requests/PatchedEditFieldMappingRequest.d.ts`** -> AI Confidence: **99.17%**
411. **`package/api/resources/hris/resources/groups/client/requests/GroupsListRequest.d.ts`** -> AI Confidence: **99.17%**
412. **`package/api/resources/hris/resources/issues/client/requests/IssuesListRequest.d.ts`** -> AI Confidence: **99.17%**
413. **`package/api/resources/hris/resources/linkToken/client/requests/EndUserDetailsRequest.d.ts`** -> AI Confidence: **99.17%**
414. **`package/api/resources/hris/resources/linkedAccounts/client/requests/LinkedAccountsListRequest.d.ts`** -> AI Confidence: **99.17%**
415. **`package/api/resources/hris/resources/locations/client/requests/LocationsListRequest.d.ts`** -> AI Confidence: **99.17%**
416. **`package/api/resources/hris/resources/timeOffBalances/client/requests/TimeOffBalancesListRequest.d.ts`** -> AI Confidence: **99.17%**
417. **`package/api/resources/hris/resources/timeOffBalances/client/requests/TimeOffBalancesRetrieveRequest.d.ts`** -> AI Confidence: **99.17%**
418. **`package/api/resources/hris/types/AccountDetails.d.ts`** -> AI Confidence: **99.17%**
419. **`package/api/resources/hris/types/AdvancedMetadata.d.ts`** -> AI Confidence: **99.17%**
420. **`package/api/resources/hris/types/BankInfo.d.ts`** -> AI Confidence: **99.17%**
421. **`package/api/resources/hris/types/Benefit.d.ts`** -> AI Confidence: **99.17%**
422. **`package/api/resources/hris/types/Deduction.d.ts`** -> AI Confidence: **99.17%**
423. **`package/api/resources/hris/types/Dependent.d.ts`** -> AI Confidence: **99.17%**
424. **`package/api/resources/hris/types/EmployerBenefit.d.ts`** -> AI Confidence: **99.17%**
425. **`package/api/resources/hris/types/Employment.d.ts`** -> AI Confidence: **99.17%**
426. **`package/api/resources/hris/types/Location.d.ts`** -> AI Confidence: **99.17%**
427. **`package/api/resources/hris/types/PayrollRun.d.ts`** -> AI Confidence: **99.17%**
428. **`package/api/resources/hris/types/Tax.d.ts`** -> AI Confidence: **99.17%**
429. **`package/api/resources/hris/types/TimeOffBalance.d.ts`** -> AI Confidence: **99.17%**
430. **`package/api/resources/hris/types/TimeOffRequest.d.ts`** -> AI Confidence: **99.17%**
431. **`package/api/resources/hris/types/TimesheetEntry.d.ts`** -> AI Confidence: **99.17%**
432. **`package/api/resources/ticketing/resources/comments/client/requests/CommentsListRequest.d.ts`** -> AI Confidence: **99.17%**
433. **`package/api/resources/ticketing/resources/fieldMapping/client/requests/PatchedEditFieldMappingRequest.d.ts`** -> AI Confidence: **99.17%**
434. **`package/api/resources/ticketing/resources/issues/client/requests/IssuesListRequest.d.ts`** -> AI Confidence: **99.17%**
435. **`package/api/resources/ticketing/resources/linkedAccounts/client/requests/LinkedAccountsListRequest.d.ts`** -> AI Confidence: **99.17%**
436. **`package/api/resources/ticketing/resources/tickets/client/requests/TicketsLiveSearchRetrieveRequest.d.ts`** -> AI Confidence: **99.17%**
437. **`package/api/resources/ticketing/types/AccountDetails.d.ts`** -> AI Confidence: **99.17%**
438. **`package/api/resources/ticketing/types/AdvancedMetadata.d.ts`** -> AI Confidence: **99.17%**
439. **`package/api/resources/ticketing/types/Attachment.d.ts`** -> AI Confidence: **99.17%**
440. **`package/api/resources/ticketing/types/Collection.d.ts`** -> AI Confidence: **99.17%**
441. **`package/api/resources/ticketing/types/Comment.d.ts`** -> AI Confidence: **99.17%**
442. **`package/api/resources/ticketing/types/Contact.d.ts`** -> AI Confidence: **99.17%**
443. **`package/api/resources/ticketing/types/ExternalTargetFieldApiResponse.d.ts`** -> AI Confidence: **99.17%**
444. **`package/api/resources/ticketing/types/FieldMappingApiInstanceResponse.d.ts`** -> AI Confidence: **99.17%**
445. **`package/api/resources/ticketing/types/Permission.d.ts`** -> AI Confidence: **99.17%**
446. **`package/api/resources/ticketing/types/RemoteFieldApiResponse.d.ts`** -> AI Confidence: **99.17%**
447. **`package/api/resources/ticketing/types/RemoteFieldClass.d.ts`** -> AI Confidence: **99.17%**
448. **`package/api/resources/ticketing/types/Role.d.ts`** -> AI Confidence: **99.17%**
449. **`package/api/resources/ticketing/types/User.d.ts`** -> AI Confidence: **99.17%**
450. **`package/api/index.js`** -> AI Confidence: **99.17%**
451. **`package/api/resources/accounting/resources/accountDetails/index.js`** -> AI Confidence: **99.17%**
452. **`package/api/resources/accounting/resources/accountToken/index.js`** -> AI Confidence: **99.17%**
453. **`package/api/resources/accounting/resources/accountingPeriods/client/index.js`** -> AI Confidence: **99.17%**
454. **`package/api/resources/accounting/resources/accountingPeriods/index.js`** -> AI Confidence: **99.17%**
455. **`package/api/resources/accounting/resources/accounts/client/index.js`** -> AI Confidence: **99.17%**
456. **`package/api/resources/accounting/resources/accounts/index.js`** -> AI Confidence: **99.17%**
457. **`package/api/resources/accounting/resources/addresses/client/index.js`** -> AI Confidence: **99.17%**
458. **`package/api/resources/accounting/resources/addresses/index.js`** -> AI Confidence: **99.17%**
459. **`package/api/resources/accounting/resources/asyncPassthrough/index.js`** -> AI Confidence: **99.17%**
460. **`package/api/resources/accounting/resources/asyncPassthrough/types/index.js`** -> AI Confidence: **99.17%**
461. **`package/api/resources/accounting/resources/asyncTasks/index.js`** -> AI Confidence: **99.17%**
462. **`package/api/resources/accounting/resources/attachments/client/index.js`** -> AI Confidence: **99.17%**
463. **`package/api/resources/accounting/resources/attachments/index.js`** -> AI Confidence: **99.17%**
464. **`package/api/resources/accounting/resources/auditTrail/client/index.js`** -> AI Confidence: **99.17%**
465. **`package/api/resources/accounting/resources/auditTrail/index.js`** -> AI Confidence: **99.17%**
466. **`package/api/resources/accounting/resources/availableActions/index.js`** -> AI Confidence: **99.17%**
467. **`package/api/resources/accounting/resources/balanceSheets/client/index.js`** -> AI Confidence: **99.17%**
468. **`package/api/resources/accounting/resources/balanceSheets/index.js`** -> AI Confidence: **99.17%**
469. **`package/api/resources/accounting/resources/bankFeedAccounts/client/index.js`** -> AI Confidence: **99.17%**
470. **`package/api/resources/accounting/resources/bankFeedAccounts/index.js`** -> AI Confidence: **99.17%**
471. **`package/api/resources/accounting/resources/bankFeedTransactions/client/index.js`** -> AI Confidence: **99.17%**
472. **`package/api/resources/accounting/resources/bankFeedTransactions/index.js`** -> AI Confidence: **99.17%**
473. **`package/api/resources/accounting/resources/cashFlowStatements/client/index.js`** -> AI Confidence: **99.17%**
474. **`package/api/resources/accounting/resources/cashFlowStatements/index.js`** -> AI Confidence: **99.17%**
475. **`package/api/resources/accounting/resources/companyInfo/client/index.js`** -> AI Confidence: **99.17%**
476. **`package/api/resources/accounting/resources/companyInfo/index.js`** -> AI Confidence: **99.17%**
477. **`package/api/resources/accounting/resources/companyInfo/types/index.js`** -> AI Confidence: **99.17%**
478. **`package/api/resources/accounting/resources/contacts/client/index.js`** -> AI Confidence: **99.17%**
479. **`package/api/resources/accounting/resources/contacts/index.js`** -> AI Confidence: **99.17%**
480. **`package/api/resources/accounting/resources/creditNotes/client/index.js`** -> AI Confidence: **99.17%**
481. **`package/api/resources/accounting/resources/creditNotes/index.js`** -> AI Confidence: **99.17%**
482. **`package/api/resources/accounting/resources/deleteAccount/index.js`** -> AI Confidence: **99.17%**
483. **`package/api/resources/accounting/resources/employees/client/index.js`** -> AI Confidence: **99.17%**
484. **`package/api/resources/accounting/resources/employees/index.js`** -> AI Confidence: **99.17%**
485. **`package/api/resources/accounting/resources/expenseReports/client/index.js`** -> AI Confidence: **99.17%**
486. **`package/api/resources/accounting/resources/expenseReports/index.js`** -> AI Confidence: **99.17%**
487. **`package/api/resources/accounting/resources/expenses/client/index.js`** -> AI Confidence: **99.17%**
488. **`package/api/resources/accounting/resources/expenses/index.js`** -> AI Confidence: **99.17%**
489. **`package/api/resources/accounting/resources/expenses/types/index.js`** -> AI Confidence: **99.17%**
490. **`package/api/resources/accounting/resources/fieldMapping/client/index.js`** -> AI Confidence: **99.17%**
491. **`package/api/resources/accounting/resources/fieldMapping/index.js`** -> AI Confidence: **99.17%**
492. **`package/api/resources/accounting/resources/forceResync/index.js`** -> AI Confidence: **99.17%**
493. **`package/api/resources/accounting/resources/generalLedgerTransactions/client/index.js`** -> AI Confidence: **99.17%**
494. **`package/api/resources/accounting/resources/generalLedgerTransactions/index.js`** -> AI Confidence: **99.17%**
495. **`package/api/resources/accounting/resources/generalLedgerTransactions/types/index.js`** -> AI Confidence: **99.17%**
496. **`package/api/resources/accounting/resources/generateKey/client/index.js`** -> AI Confidence: **99.17%**
497. **`package/api/resources/accounting/resources/generateKey/index.js`** -> AI Confidence: **99.17%**
498. **`package/api/resources/accounting/resources/incomeStatements/client/index.js`** -> AI Confidence: **99.17%**
499. **`package/api/resources/accounting/resources/incomeStatements/index.js`** -> AI Confidence: **99.17%**
500. **`package/api/resources/accounting/resources/invoices/client/index.js`** -> AI Confidence: **99.17%**
501. **`package/api/resources/accounting/resources/invoices/index.js`** -> AI Confidence: **99.17%**
502. **`package/api/resources/accounting/resources/invoices/types/index.js`** -> AI Confidence: **99.17%**
503. **`package/api/resources/accounting/resources/issues/client/index.js`** -> AI Confidence: **99.17%**
504. **`package/api/resources/accounting/resources/issues/index.js`** -> AI Confidence: **99.17%**
505. **`package/api/resources/accounting/resources/issues/types/index.js`** -> AI Confidence: **99.17%**
506. **`package/api/resources/accounting/resources/itemFulfillments/client/index.js`** -> AI Confidence: **99.17%**
507. **`package/api/resources/accounting/resources/itemFulfillments/index.js`** -> AI Confidence: **99.17%**
508. **`package/api/resources/accounting/resources/itemFulfillments/types/index.js`** -> AI Confidence: **99.17%**
509. **`package/api/resources/accounting/resources/items/client/index.js`** -> AI Confidence: **99.17%**
510. **`package/api/resources/accounting/resources/items/index.js`** -> AI Confidence: **99.17%**
511. **`package/api/resources/accounting/resources/items/types/index.js`** -> AI Confidence: **99.17%**
512. **`package/api/resources/accounting/resources/journalEntries/client/index.js`** -> AI Confidence: **99.17%**
513. **`package/api/resources/accounting/resources/journalEntries/index.js`** -> AI Confidence: **99.17%**
514. **`package/api/resources/accounting/resources/journalEntries/types/index.js`** -> AI Confidence: **99.17%**
515. **`package/api/resources/accounting/resources/linkToken/client/index.js`** -> AI Confidence: **99.17%**
516. **`package/api/resources/accounting/resources/linkToken/index.js`** -> AI Confidence: **99.17%**
517. **`package/api/resources/accounting/resources/linkToken/types/index.js`** -> AI Confidence: **99.17%**
518. **`package/api/resources/accounting/resources/linkedAccounts/client/index.js`** -> AI Confidence: **99.17%**
519. **`package/api/resources/accounting/resources/linkedAccounts/index.js`** -> AI Confidence: **99.17%**
520. **`package/api/resources/accounting/resources/linkedAccounts/types/index.js`** -> AI Confidence: **99.17%**
521. **`package/api/resources/accounting/resources/passthrough/index.js`** -> AI Confidence: **99.17%**
522. **`package/api/resources/accounting/resources/paymentMethods/client/index.js`** -> AI Confidence: **99.17%**
523. **`package/api/resources/accounting/resources/paymentMethods/index.js`** -> AI Confidence: **99.17%**
524. **`package/api/resources/accounting/resources/paymentTerms/client/index.js`** -> AI Confidence: **99.17%**
525. **`package/api/resources/accounting/resources/paymentTerms/index.js`** -> AI Confidence: **99.17%**
526. **`package/api/resources/accounting/resources/payments/client/index.js`** -> AI Confidence: **99.17%**
527. **`package/api/resources/accounting/resources/payments/index.js`** -> AI Confidence: **99.17%**
528. **`package/api/resources/accounting/resources/payments/types/index.js`** -> AI Confidence: **99.17%**
529. **`package/api/resources/accounting/resources/phoneNumbers/client/index.js`** -> AI Confidence: **99.17%**
530. **`package/api/resources/accounting/resources/phoneNumbers/index.js`** -> AI Confidence: **99.17%**
531. **`package/api/resources/accounting/resources/projects/client/index.js`** -> AI Confidence: **99.17%**
532. **`package/api/resources/accounting/resources/projects/index.js`** -> AI Confidence: **99.17%**
533. **`package/api/resources/accounting/resources/projects/types/index.js`** -> AI Confidence: **99.17%**
534. **`package/api/resources/accounting/resources/purchaseOrders/client/index.js`** -> AI Confidence: **99.17%**
535. **`package/api/resources/accounting/resources/purchaseOrders/index.js`** -> AI Confidence: **99.17%**
536. **`package/api/resources/accounting/resources/purchaseOrders/types/index.js`** -> AI Confidence: **99.17%**
537. **`package/api/resources/accounting/resources/regenerateKey/client/index.js`** -> AI Confidence: **99.17%**
538. **`package/api/resources/accounting/resources/regenerateKey/index.js`** -> AI Confidence: **99.17%**
539. **`package/api/resources/accounting/resources/salesOrders/client/index.js`** -> AI Confidence: **99.17%**
540. **`package/api/resources/accounting/resources/salesOrders/index.js`** -> AI Confidence: **99.17%**
541. **`package/api/resources/accounting/resources/salesOrders/types/index.js`** -> AI Confidence: **99.17%**
542. **`package/api/resources/accounting/resources/scopes/client/index.js`** -> AI Confidence: **99.17%**
543. **`package/api/resources/accounting/resources/scopes/index.js`** -> AI Confidence: **99.17%**
544. **`package/api/resources/accounting/resources/syncStatus/client/index.js`** -> AI Confidence: **99.17%**
545. **`package/api/resources/accounting/resources/syncStatus/index.js`** -> AI Confidence: **99.17%**
546. **`package/api/resources/accounting/resources/taxRates/client/index.js`** -> AI Confidence: **99.17%**
547. **`package/api/resources/accounting/resources/taxRates/index.js`** -> AI Confidence: **99.17%**
548. **`package/api/resources/accounting/resources/trackingCategories/client/index.js`** -> AI Confidence: **99.17%**
549. **`package/api/resources/accounting/resources/trackingCategories/index.js`** -> AI Confidence: **99.17%**
550. **`package/api/resources/accounting/resources/trackingCategories/types/index.js`** -> AI Confidence: **99.17%**
551. **`package/api/resources/accounting/resources/transactions/client/index.js`** -> AI Confidence: **99.17%**
552. **`package/api/resources/accounting/resources/transactions/index.js`** -> AI Confidence: **99.17%**
553. **`package/api/resources/accounting/resources/transactions/types/index.js`** -> AI Confidence: **99.17%**
554. **`package/api/resources/accounting/resources/vendorCredits/client/index.js`** -> AI Confidence: **99.17%**
555. **`package/api/resources/accounting/resources/vendorCredits/index.js`** -> AI Confidence: **99.17%**
556. **`package/api/resources/accounting/resources/vendorCredits/types/index.js`** -> AI Confidence: **99.17%**
557. **`package/api/resources/accounting/resources/webhookReceivers/client/index.js`** -> AI Confidence: **99.17%**
558. **`package/api/resources/accounting/resources/webhookReceivers/index.js`** -> AI Confidence: **99.17%**
559. **`package/api/resources/ats/resources/accountDetails/index.js`** -> AI Confidence: **99.17%**
560. **`package/api/resources/ats/resources/accountToken/index.js`** -> AI Confidence: **99.17%**
561. **`package/api/resources/ats/resources/activities/client/index.js`** -> AI Confidence: **99.17%**
562. **`package/api/resources/ats/resources/activities/index.js`** -> AI Confidence: **99.17%**
563. **`package/api/resources/ats/resources/activities/types/index.js`** -> AI Confidence: **99.17%**
564. **`package/api/resources/ats/resources/applications/client/index.js`** -> AI Confidence: **99.17%**
565. **`package/api/resources/ats/resources/applications/index.js`** -> AI Confidence: **99.17%**
566. **`package/api/resources/ats/resources/applications/types/index.js`** -> AI Confidence: **99.17%**
567. **`package/api/resources/ats/resources/asyncPassthrough/index.js`** -> AI Confidence: **99.17%**
568. **`package/api/resources/ats/resources/asyncPassthrough/types/index.js`** -> AI Confidence: **99.17%**
569. **`package/api/resources/ats/resources/attachments/client/index.js`** -> AI Confidence: **99.17%**
570. **`package/api/resources/ats/resources/attachments/index.js`** -> AI Confidence: **99.17%**
571. **`package/api/resources/ats/resources/auditTrail/client/index.js`** -> AI Confidence: **99.17%**
572. **`package/api/resources/ats/resources/auditTrail/index.js`** -> AI Confidence: **99.17%**
573. **`package/api/resources/ats/resources/availableActions/index.js`** -> AI Confidence: **99.17%**
574. **`package/api/resources/ats/resources/candidates/client/index.js`** -> AI Confidence: **99.17%**
575. **`package/api/resources/ats/resources/candidates/index.js`** -> AI Confidence: **99.17%**
576. **`package/api/resources/ats/resources/candidates/types/index.js`** -> AI Confidence: **99.17%**
577. **`package/api/resources/ats/resources/deleteAccount/index.js`** -> AI Confidence: **99.17%**
578. **`package/api/resources/ats/resources/departments/client/index.js`** -> AI Confidence: **99.17%**
579. **`package/api/resources/ats/resources/departments/index.js`** -> AI Confidence: **99.17%**
580. **`package/api/resources/ats/resources/eeocs/client/index.js`** -> AI Confidence: **99.17%**
581. **`package/api/resources/ats/resources/eeocs/index.js`** -> AI Confidence: **99.17%**
582. **`package/api/resources/ats/resources/eeocs/types/index.js`** -> AI Confidence: **99.17%**
583. **`package/api/resources/ats/resources/fieldMapping/client/index.js`** -> AI Confidence: **99.17%**
584. **`package/api/resources/ats/resources/fieldMapping/index.js`** -> AI Confidence: **99.17%**
585. **`package/api/resources/ats/resources/forceResync/index.js`** -> AI Confidence: **99.17%**
586. **`package/api/resources/ats/resources/generateKey/client/index.js`** -> AI Confidence: **99.17%**
587. **`package/api/resources/ats/resources/generateKey/index.js`** -> AI Confidence: **99.17%**
588. **`package/api/resources/ats/resources/interviews/client/index.js`** -> AI Confidence: **99.17%**
589. **`package/api/resources/ats/resources/interviews/index.js`** -> AI Confidence: **99.17%**
590. **`package/api/resources/ats/resources/interviews/types/index.js`** -> AI Confidence: **99.17%**
591. **`package/api/resources/ats/resources/issues/client/index.js`** -> AI Confidence: **99.17%**
592. **`package/api/resources/ats/resources/issues/index.js`** -> AI Confidence: **99.17%**
593. **`package/api/resources/ats/resources/issues/types/index.js`** -> AI Confidence: **99.17%**
594. **`package/api/resources/ats/resources/jobInterviewStages/client/index.js`** -> AI Confidence: **99.17%**
595. **`package/api/resources/ats/resources/jobInterviewStages/index.js`** -> AI Confidence: **99.17%**
596. **`package/api/resources/ats/resources/jobPostings/client/index.js`** -> AI Confidence: **99.17%**
597. **`package/api/resources/ats/resources/jobPostings/index.js`** -> AI Confidence: **99.17%**
598. **`package/api/resources/ats/resources/jobPostings/types/index.js`** -> AI Confidence: **99.17%**
599. **`package/api/resources/ats/resources/jobs/client/index.js`** -> AI Confidence: **99.17%**
600. **`package/api/resources/ats/resources/jobs/index.js`** -> AI Confidence: **99.17%**
601. **`package/api/resources/ats/resources/jobs/types/index.js`** -> AI Confidence: **99.17%**
602. **`package/api/resources/ats/resources/linkToken/client/index.js`** -> AI Confidence: **99.17%**
603. **`package/api/resources/ats/resources/linkToken/index.js`** -> AI Confidence: **99.17%**
604. **`package/api/resources/ats/resources/linkToken/types/index.js`** -> AI Confidence: **99.17%**
605. **`package/api/resources/ats/resources/linkedAccounts/client/index.js`** -> AI Confidence: **99.17%**
606. **`package/api/resources/ats/resources/linkedAccounts/index.js`** -> AI Confidence: **99.17%**
607. **`package/api/resources/ats/resources/linkedAccounts/types/index.js`** -> AI Confidence: **99.17%**
608. **`package/api/resources/ats/resources/offers/client/index.js`** -> AI Confidence: **99.17%**
609. **`package/api/resources/ats/resources/offers/index.js`** -> AI Confidence: **99.17%**
610. **`package/api/resources/ats/resources/offices/client/index.js`** -> AI Confidence: **99.17%**
611. **`package/api/resources/ats/resources/offices/index.js`** -> AI Confidence: **99.17%**
612. **`package/api/resources/ats/resources/passthrough/index.js`** -> AI Confidence: **99.17%**
613. **`package/api/resources/ats/resources/regenerateKey/client/index.js`** -> AI Confidence: **99.17%**
614. **`package/api/resources/ats/resources/regenerateKey/index.js`** -> AI Confidence: **99.17%**
615. **`package/api/resources/ats/resources/rejectReasons/client/index.js`** -> AI Confidence: **99.17%**
616. **`package/api/resources/ats/resources/rejectReasons/index.js`** -> AI Confidence: **99.17%**
617. **`package/api/resources/ats/resources/scopes/client/index.js`** -> AI Confidence: **99.17%**
618. **`package/api/resources/ats/resources/scopes/index.js`** -> AI Confidence: **99.17%**
619. **`package/api/resources/ats/resources/scorecards/client/index.js`** -> AI Confidence: **99.17%**
620. **`package/api/resources/ats/resources/scorecards/index.js`** -> AI Confidence: **99.17%**
621. **`package/api/resources/ats/resources/scorecards/types/index.js`** -> AI Confidence: **99.17%**
622. **`package/api/resources/ats/resources/syncStatus/client/index.js`** -> AI Confidence: **99.17%**
623. **`package/api/resources/ats/resources/syncStatus/index.js`** -> AI Confidence: **99.17%**
624. **`package/api/resources/ats/resources/tags/client/index.js`** -> AI Confidence: **99.17%**
625. **`package/api/resources/ats/resources/tags/index.js`** -> AI Confidence: **99.17%**
626. **`package/api/resources/ats/resources/users/client/index.js`** -> AI Confidence: **99.17%**
627. **`package/api/resources/ats/resources/users/index.js`** -> AI Confidence: **99.17%**
628. **`package/api/resources/ats/resources/webhookReceivers/client/index.js`** -> AI Confidence: **99.17%**
629. **`package/api/resources/ats/resources/webhookReceivers/index.js`** -> AI Confidence: **99.17%**
630. **`package/api/resources/crm/resources/accountDetails/index.js`** -> AI Confidence: **99.17%**
631. **`package/api/resources/crm/resources/accountToken/index.js`** -> AI Confidence: **99.17%**
632. **`package/api/resources/crm/resources/accounts/client/index.js`** -> AI Confidence: **99.17%**
633. **`package/api/resources/crm/resources/accounts/index.js`** -> AI Confidence: **99.17%**
634. **`package/api/resources/crm/resources/associationTypes/client/index.js`** -> AI Confidence: **99.17%**
635. **`package/api/resources/crm/resources/associationTypes/index.js`** -> AI Confidence: **99.17%**
636. **`package/api/resources/crm/resources/associations/client/index.js`** -> AI Confidence: **99.17%**
637. **`package/api/resources/crm/resources/associations/index.js`** -> AI Confidence: **99.17%**
638. **`package/api/resources/crm/resources/asyncPassthrough/index.js`** -> AI Confidence: **99.17%**
639. **`package/api/resources/crm/resources/asyncPassthrough/types/index.js`** -> AI Confidence: **99.17%**
640. **`package/api/resources/crm/resources/auditTrail/client/index.js`** -> AI Confidence: **99.17%**
641. **`package/api/resources/crm/resources/auditTrail/index.js`** -> AI Confidence: **99.17%**
642. **`package/api/resources/crm/resources/availableActions/index.js`** -> AI Confidence: **99.17%**
643. **`package/api/resources/crm/resources/contacts/client/index.js`** -> AI Confidence: **99.17%**
644. **`package/api/resources/crm/resources/contacts/index.js`** -> AI Confidence: **99.17%**
645. **`package/api/resources/crm/resources/contacts/types/index.js`** -> AI Confidence: **99.17%**
646. **`package/api/resources/crm/resources/customObjectClasses/client/index.js`** -> AI Confidence: **99.17%**
647. **`package/api/resources/crm/resources/customObjectClasses/index.js`** -> AI Confidence: **99.17%**
648. **`package/api/resources/crm/resources/customObjects/client/index.js`** -> AI Confidence: **99.17%**
649. **`package/api/resources/crm/resources/customObjects/index.js`** -> AI Confidence: **99.17%**
650. **`package/api/resources/crm/resources/deleteAccount/index.js`** -> AI Confidence: **99.17%**
651. **`package/api/resources/crm/resources/engagementTypes/client/index.js`** -> AI Confidence: **99.17%**
652. **`package/api/resources/crm/resources/engagementTypes/index.js`** -> AI Confidence: **99.17%**
653. **`package/api/resources/crm/resources/engagements/client/index.js`** -> AI Confidence: **99.17%**
654. **`package/api/resources/crm/resources/engagements/index.js`** -> AI Confidence: **99.17%**
655. **`package/api/resources/crm/resources/engagements/types/index.js`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `package/api/resources/filestorage/resources/index.js` -> **100.0%** Exposure
- `package/core/fetcher/Fetcher.js` -> **100.0%** Exposure
- `package/core/fetcher/Headers.js` -> **100.0%** Exposure
- `package/core/fetcher/stream-wrappers/Node18UniversalStreamWrapper.js` -> **100.0%** Exposure
- `package/core/fetcher/stream-wrappers/NodePre18StreamWrapper.js` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `package/core/fetcher/Fetcher.js` -> **100.0%** Exposure
- `package/core/fetcher/Headers.js` -> **100.0%** Exposure
- `package/core/fetcher/HttpResponsePromise.js` -> **100.0%** Exposure
- `package/core/fetcher/getFetchFn.js` -> **100.0%** Exposure
- `package/core/fetcher/stream-wrappers/Node18UniversalStreamWrapper.js` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `106` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/core/fetcher/stream-wrappers/NodePre18StreamWrapper.js` (JAVASCRIPT) -> Cumulative Risk: **989.73**
- **Archetype:** `file_cluster_4` (Distance: 13.268 IQR)
- **Magnitude:** 269.4 | **LOC:** 127 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `text` (Impact: 56.4), `read` (Impact: 30.5), `unpipe` (Impact: 17.4)

### 2. `package/core/fetcher/getErrorResponseBody.js` (JAVASCRIPT) -> Cumulative Risk: **970.08**
- **Archetype:** `file_cluster_13` (Distance: 13.378 IQR)
- **Magnitude:** 151.36 | **LOC:** 46 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9966%), Documentation (99.9496%), Algorithmic Dos (99.9222%)
- **Heaviest Functions:** `getErrorResponseBody` (Impact: 115.9), `fulfilled` (Impact: 5.2), `rejected` (Impact: 5.2)

### 3. `package/core/fetcher/stream-wrappers/Node18UniversalStreamWrapper.js` (JAVASCRIPT) -> Cumulative Risk: **957.62**
- **Archetype:** `file_cluster_4` (Distance: 13.354 IQR)
- **Magnitude:** 516.54 | **LOC:** 248 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `pipe` (Impact: 48.0), `unpipe` (Impact: 47.9), `_startReading` (Impact: 40.9)

### 4. `package/core/fetcher/stream-wrappers/UndiciStreamWrapper.js` (JAVASCRIPT) -> Cumulative Risk: **953.65**
- **Archetype:** `file_cluster_4` (Distance: 13.299 IQR)
- **Magnitude:** 473.78 | **LOC:** 230 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_startReading` (Impact: 40.9), `pipe` (Impact: 26.3), `text` (Impact: 26.3)

### 5. `package/core/pagination/CustomPager.js` (JAVASCRIPT) -> Cumulative Risk: **940.15**
- **Archetype:** `file_cluster_4` (Distance: 14.289 IQR)
- **Magnitude:** 306.1 | **LOC:** 195 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_a` (Impact: 33.9), `getNextPage` (Impact: 18.8), `getPreviousPage` (Impact: 18.8)

### 6. `package/core/pagination/Page.js` (JAVASCRIPT) -> Cumulative Risk: **938.65**
- **Archetype:** `file_cluster_4` (Distance: 15.193 IQR)
- **Magnitude:** 209.66 | **LOC:** 102 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_a` (Impact: 33.9), `iterMessages` (Impact: 17.6), `step` (Impact: 8.9)

### 7. `package/core/fetcher/stream-wrappers/chooseStreamWrapper.js` (JAVASCRIPT) -> Cumulative Risk: **896.66**
- **Archetype:** `file_cluster_4` (Distance: 14.571 IQR)
- **Magnitude:** 141.08 | **LOC:** 60 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9726%)
- **Heaviest Functions:** `__setModuleDefault` (Impact: 37.5), `chooseStreamWrapper` (Impact: 28.4), `ownKeys` (Impact: 23.0)

### 8. `package/core/fetcher/getFetchFn.js` (JAVASCRIPT) -> Cumulative Risk: **870.84**
- **Archetype:** `file_cluster_4` (Distance: 14.51 IQR)
- **Magnitude:** 139.4 | **LOC:** 69 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__setModuleDefault` (Impact: 37.5), `getFetchFn` (Impact: 28.7), `ownKeys` (Impact: 23.0)

### 9. `package/core/fetcher/HttpResponsePromise.js` (JAVASCRIPT) -> Cumulative Risk: **866.0**
- **Archetype:** `file_cluster_4` (Distance: 14.421 IQR)
- **Magnitude:** 129.0 | **LOC:** 104 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `finally` (Impact: 12.9), `unwrap` (Impact: 6.0), `then` (Impact: 5.3)

### 10. `package/core/logging/logger.js` (JAVASCRIPT) -> Cumulative Risk: **850.13**
- **Archetype:** `file_cluster_8` (Distance: 13.939 IQR)
- **Magnitude:** 182.76 | **LOC:** 145 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `createLogger` (Impact: 29.3), `debug` (Impact: 14.1), `info` (Impact: 14.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/core/fetcher/stream-wrappers/Node18UniversalStreamWrapper.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.354 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.991 IQR)
- **Top Global Matches:** file_cluster_4: 13.354, file_cluster_11: 13.8, file_cluster_17: 13.905
- **Magnitude:** 516.54 | **LOC:** 248 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (96.4554%), Tech Debt (43.2102%)
**Top Internal Functions/Classes:**
  * `pipe` (Impact: 48.0 | O(N^4) | DB: 4)
  * `unpipe` (Impact: 47.9 | O(N^4) | DB: 3)
  * `_startReading` (Impact: 40.9 | O(N^6) | DB: 8)
  * `text` (Impact: 26.3 | O(N^5) | DB: 3)
  * `read` (Impact: 26.2 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 36`, `args: 41`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 145`, `duplicate_logic: 2`
* *Architecture:* `api: 8`, `concurrency: 44`
* *Defense:* `safety: 25`, `immutability_locks: 14`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/api/resources/accounting/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.816 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.898 IQR)
- **Top Global Matches:** file_cluster_13: 11.816, file_cluster_8: 12.174, file_cluster_7: 12.837
- **Magnitude:** 488.11 | **LOC:** 618 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.1405%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 601`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 601`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CashFlowStatement, ExternalTargetFieldApi, PaginatedGeneralLedgerTransactionList, InvoicePaymentTerm, ContactRequestCompany, InvoiceSalesOrdersItem, PaginatedIssueList, ExpenseReportStatusEnum...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/accounting/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.816 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.898 IQR)
- **Top Global Matches:** file_cluster_13: 11.816, file_cluster_8: 12.174, file_cluster_7: 12.837
- **Magnitude:** 488.11 | **LOC:** 618 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.1405%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 601`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 601`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CashFlowStatement, ExternalTargetFieldApi, PaginatedGeneralLedgerTransactionList, InvoicePaymentTerm, ContactRequestCompany, InvoiceSalesOrdersItem, PaginatedIssueList, ExpenseReportStatusEnum...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/api/resources/crm/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.438 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.008 IQR)
- **Top Global Matches:** file_cluster_13: 11.438, file_cluster_8: 11.95, file_cluster_7: 12.627
- **Magnitude:** 480.57 | **LOC:** 241 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.8281%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 224`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 224`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AccountDetailsAndActionsStatusEnum, ExternalTargetFieldApiResponse, NoteResponse, ActivityTypeEnum, ExternalTargetFieldApi, Association, EnabledActionsEnum, RemoteFieldClassForCustomObjectClass...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/crm/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.438 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.008 IQR)
- **Top Global Matches:** file_cluster_13: 11.438, file_cluster_8: 11.95, file_cluster_7: 12.627
- **Magnitude:** 480.57 | **LOC:** 241 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.8281%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 224`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 224`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AccountDetailsAndActionsStatusEnum, ExternalTargetFieldApiResponse, NoteResponse, ActivityTypeEnum, ExternalTargetFieldApi, Association, EnabledActionsEnum, RemoteFieldClassForCustomObjectClass...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/api/resources/ats/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.438 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.011 IQR)
- **Top Global Matches:** file_cluster_13: 11.438, file_cluster_8: 11.953, file_cluster_7: 12.629
- **Magnitude:** 480.49 | **LOC:** 237 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (16.1096%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 220`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 220`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AccountDetailsAndActionsStatusEnum, ExternalTargetFieldApiResponse, AttachmentRequest, ActivityTypeEnum, ScheduledInterviewRequestApplication, ExternalTargetFieldApi, EnabledActionsEnum, JobHiringManagersItem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/ats/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.438 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.011 IQR)
- **Top Global Matches:** file_cluster_13: 11.438, file_cluster_8: 11.953, file_cluster_7: 12.629
- **Magnitude:** 480.49 | **LOC:** 237 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (16.1096%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 220`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 220`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AccountDetailsAndActionsStatusEnum, ExternalTargetFieldApiResponse, AttachmentRequest, ActivityTypeEnum, ScheduledInterviewRequestApplication, ExternalTargetFieldApi, EnabledActionsEnum, JobHiringManagersItem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/api/resources/hris/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.444 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.029 IQR)
- **Top Global Matches:** file_cluster_13: 11.444, file_cluster_8: 11.972, file_cluster_11: 12.628
- **Magnitude:** 480.11 | **LOC:** 218 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (17.657%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 201`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 201`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TimeOffEmployee, AccountDetailsAndActionsStatusEnum, ExternalTargetFieldApiResponse, MaritalStatusEnum, EmployeeManager, ExternalTargetFieldApi, EnabledActionsEnum, EmployeeRequestGroupsItem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/hris/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.444 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.029 IQR)
- **Top Global Matches:** file_cluster_13: 11.444, file_cluster_8: 11.972, file_cluster_11: 12.628
- **Magnitude:** 480.11 | **LOC:** 218 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (17.657%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 201`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 201`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TimeOffEmployee, AccountDetailsAndActionsStatusEnum, ExternalTargetFieldApiResponse, MaritalStatusEnum, EmployeeManager, ExternalTargetFieldApi, EnabledActionsEnum, EmployeeRequestGroupsItem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/api/resources/ticketing/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.462 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.058 IQR)
- **Top Global Matches:** file_cluster_13: 11.462, file_cluster_8: 12.009, file_cluster_11: 12.616
- **Magnitude:** 476.13 | **LOC:** 194 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (20.2802%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 177`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 177`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AccountDetailsAndActionsStatusEnum, ExternalTargetFieldApiResponse, AttachmentRequest, Project, ExternalTargetFieldApi, EnabledActionsEnum, ActionsEnum, TicketRequestContact...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/ticketing/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.462 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.058 IQR)
- **Top Global Matches:** file_cluster_13: 11.462, file_cluster_8: 12.009, file_cluster_11: 12.616
- **Magnitude:** 476.13 | **LOC:** 194 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (20.2802%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 177`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 177`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AccountDetailsAndActionsStatusEnum, ExternalTargetFieldApiResponse, AttachmentRequest, Project, ExternalTargetFieldApi, EnabledActionsEnum, ActionsEnum, TicketRequestContact...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/fetcher/stream-wrappers/UndiciStreamWrapper.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.299 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.197 IQR)
- **Top Global Matches:** file_cluster_4: 13.299, file_cluster_11: 13.748, file_cluster_15: 13.875
- **Magnitude:** 473.78 | **LOC:** 230 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (96.6226%), Tech Debt (47.5456%)
**Top Internal Functions/Classes:**
  * `_startReading` (Impact: 40.9 | O(N^6) | DB: 8)
  * `pipe` (Impact: 26.3 | O(N^4) | DB: 4)
  * `text` (Impact: 26.3 | O(N^5) | DB: 3)
  * `unpipe` (Impact: 26.2 | O(N^4) | DB: 3)
  * `read` (Impact: 26.2 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 36`, `args: 41`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 145`, `duplicate_logic: 2`
* *Architecture:* `api: 9`, `concurrency: 44`
* *Defense:* `safety: 19`, `immutability_locks: 14`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/api/resources/filestorage/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.599 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.159 IQR)
- **Top Global Matches:** file_cluster_13: 11.599, file_cluster_8: 12.195, file_cluster_11: 12.652
- **Magnitude:** 447.01 | **LOC:** 138 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (32.5097%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 121`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 121`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AccountDetailsAndActionsStatusEnum, ExternalTargetFieldApiResponse, ExternalTargetFieldApi, FolderDrive, EnabledActionsEnum, PaginatedDriveList, PaginatedFolderList, PermissionRequestType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/filestorage/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.599 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.159 IQR)
- **Top Global Matches:** file_cluster_13: 11.599, file_cluster_8: 12.195, file_cluster_11: 12.652
- **Magnitude:** 447.01 | **LOC:** 138 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (32.5097%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 121`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 121`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AccountDetailsAndActionsStatusEnum, ExternalTargetFieldApiResponse, ExternalTargetFieldApi, FolderDrive, EnabledActionsEnum, PaginatedDriveList, PaginatedFolderList, PermissionRequestType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/fetcher/Fetcher.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.505 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.692 IQR)
- **Top Global Matches:** file_cluster_13: 11.505, file_cluster_8: 11.562, file_cluster_11: 11.912
- **Magnitude:** 444.1 | **LOC:** 317 | **CtrlFlow:** 73.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (31.6968%), Tech Debt (32.6116%)
**Top Internal Functions/Classes:**
  * `fetcherImpl` (Impact: 158.4 | O(N^6) | DB: 1)
  * `redactUrl` (Impact: 124.4 | O(N^4) | DB: 7)
  * `getHeaders` (Impact: 57.5 | O(N^4) | DB: 3)
  * `redactQueryParameters` (Impact: 18.1 | O(N^3))
  * `redactHeaders` (Impact: 17.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 30`, `args: 13`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 37`, `duplicate_logic: 2`
* *Architecture:* `api: 3`, `concurrency: 2`, `import: 12`
* *Defense:* `safety: 36`, `immutability_locks: 49`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.248
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` RawResponse, makeRequest, getRequestBody, createRequestUrl, logger, requestWithRetries, json, getResponseBody...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/core/schemas/builders/object/object.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.818 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.497 IQR)
- **Top Global Matches:** file_cluster_8: 11.818, file_cluster_13: 11.843, file_cluster_11: 11.984
- **Magnitude:** 398.26 | **LOC:** 275 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (96.291%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `object` (Impact: 253.1 | O(N^6) | DB: 5)
  * `getObjectUtils` (Impact: 87.8 | O(2^N))
  * `isSchemaOptional` (Impact: 24.8 | O(N^3))
  * `isSchemaRequired` (Impact: 1.9 | O(N^1))
  * `validateAndTransformObject` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 63`, `args: 36`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 21`
* *Architecture:* `io: 4`, `api: 2`, `import: 11`
* *Defense:* `safety: 33`, `doc: 1`, `immutability_locks: 37`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` filterObject, keys, index, getErrorMessageForIncorrectType, property, isPlainObject, maybeSkipValidation, Schema...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/core/schemas/builders/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.626 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.384 IQR)
- **Top Global Matches:** file_cluster_13: 13.626, file_cluster_11: 14.044, file_cluster_8: 14.247
- **Magnitude:** 391.37 | **LOC:** 31 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (99.2849%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 14`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 14`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index, index, index, index, index, index, index, index...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/api/resources/ticketing/resources/tickets/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.833 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.314 IQR)
- **Top Global Matches:** file_cluster_13: 13.833, file_cluster_11: 14.191, file_cluster_8: 14.428
- **Magnitude:** 389.81 | **LOC:** 28 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 11`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 11`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TicketsListRequestExpandItem, TicketsRetrieveRequestRemoteFields, TicketsViewersListRequestExpandItem, TicketsListRequestStatus, TicketsListRequestShowEnumOrigins, TicketsRetrieveRequestShowEnumOrigins, TicketsRetrieveRequestExpandItem, TicketsLiveSearchRetrieveRequestShowEnumOrigins...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/ticketing/resources/tickets/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.833 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.314 IQR)
- **Top Global Matches:** file_cluster_13: 13.833, file_cluster_11: 14.191, file_cluster_8: 14.428
- **Magnitude:** 389.81 | **LOC:** 28 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 11`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 11`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TicketsListRequestExpandItem, TicketsRetrieveRequestRemoteFields, TicketsViewersListRequestExpandItem, TicketsListRequestStatus, TicketsListRequestShowEnumOrigins, TicketsRetrieveRequestShowEnumOrigins, TicketsRetrieveRequestExpandItem, TicketsLiveSearchRetrieveRequestShowEnumOrigins...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/api/resources/hris/resources/timeOff/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.066 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.211 IQR)
- **Top Global Matches:** file_cluster_13: 14.066, file_cluster_11: 14.351, file_cluster_8: 14.62
- **Magnitude:** 388.25 | **LOC:** 25 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 8`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 8`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TimeOffListRequestRequestType, TimeOffListRequestStatus, TimeOffRetrieveRequestExpandItem, TimeOffListRequestExpandItem, TimeOffListRequestRemoteFields, TimeOffListRequestShowEnumOrigins, TimeOffRetrieveRequestRemoteFields, TimeOffRetrieveRequestShowEnumOrigins
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/hris/resources/timeOff/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.066 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.211 IQR)
- **Top Global Matches:** file_cluster_13: 14.066, file_cluster_11: 14.351, file_cluster_8: 14.62
- **Magnitude:** 388.25 | **LOC:** 25 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 8`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 8`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TimeOffListRequestRequestType, TimeOffListRequestStatus, TimeOffRetrieveRequestExpandItem, TimeOffListRequestExpandItem, TimeOffListRequestRemoteFields, TimeOffListRequestShowEnumOrigins, TimeOffRetrieveRequestRemoteFields, TimeOffRetrieveRequestShowEnumOrigins
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/api/resources/hris/resources/employees/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.147 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.165 IQR)
- **Top Global Matches:** file_cluster_13: 14.147, file_cluster_11: 14.403, file_cluster_8: 14.682
- **Magnitude:** 387.73 | **LOC:** 24 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 7`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 7`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EmployeesRetrieveRequestRemoteFields, EmployeesRetrieveRequestShowEnumOrigins, EmployeesListRequestShowEnumOrigins, EmployeesRetrieveRequestExpandItem, EmployeesListRequestExpandItem, EmployeesListRequestEmploymentStatus, EmployeesListRequestRemoteFields
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/api/resources/hris/resources/employments/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.147 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.165 IQR)
- **Top Global Matches:** file_cluster_13: 14.147, file_cluster_11: 14.403, file_cluster_8: 14.682
- **Magnitude:** 387.73 | **LOC:** 24 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 7`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 7`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EmploymentsListRequestExpandItem, EmploymentsListRequestRemoteFields, EmploymentsListRequestOrderBy, EmploymentsRetrieveRequestExpandItem, EmploymentsRetrieveRequestShowEnumOrigins, EmploymentsListRequestShowEnumOrigins, EmploymentsRetrieveRequestRemoteFields
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/hris/resources/employees/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.147 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.165 IQR)
- **Top Global Matches:** file_cluster_13: 14.147, file_cluster_11: 14.403, file_cluster_8: 14.682
- **Magnitude:** 387.73 | **LOC:** 24 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 7`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 7`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EmployeesRetrieveRequestRemoteFields, EmployeesRetrieveRequestShowEnumOrigins, EmployeesListRequestShowEnumOrigins, EmployeesRetrieveRequestExpandItem, EmployeesListRequestExpandItem, EmployeesListRequestEmploymentStatus, EmployeesListRequestRemoteFields
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/hris/resources/employments/types/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.147 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.165 IQR)
- **Top Global Matches:** file_cluster_13: 14.147, file_cluster_11: 14.403, file_cluster_8: 14.682
- **Magnitude:** 387.73 | **LOC:** 24 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 5`, `args: 4`, `func_start: 7`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `import: 7`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EmploymentsListRequestExpandItem, EmploymentsListRequestRemoteFields, EmploymentsListRequestOrderBy, EmploymentsRetrieveRequestExpandItem, EmploymentsRetrieveRequestShowEnumOrigins, EmploymentsListRequestShowEnumOrigins, EmploymentsRetrieveRequestRemoteFields
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `package/core/logging/exports.js` (JAVASCRIPT) | Magnitude: 66.64 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 39, indent_spaces: 27, branch: 26, structural_boundaries: 16
- `package/api/index.js` (JAVASCRIPT) | Magnitude: 384.61 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 18, branch: 15, indent_spaces: 9, structural_boundaries: 5
- `package/api/resources/accounting/resources/accountDetails/index.js` (JAVASCRIPT) | Magnitude: 384.61 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 18, branch: 15, indent_spaces: 9, structural_boundaries: 5
- `package/api/resources/accounting/resources/accountToken/index.js` (JAVASCRIPT) | Magnitude: 384.61 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 18, branch: 15, indent_spaces: 9, structural_boundaries: 5
- `package/api/resources/accounting/resources/accountingPeriods/client/index.js` (JAVASCRIPT) | Magnitude: 384.61 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 18, branch: 15, indent_spaces: 9, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/api/resources/accounting/types/Employee.d.ts` (TYPESCRIPT) | Magnitude: 1.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, branch: 5, doc: 4, structural_boundaries: 2
- `package/serialization/resources/accounting/types/AccountToken.d.ts` (TYPESCRIPT) | Magnitude: 1.72 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 5, import: 4, api: 2
- `package/serialization/resources/accounting/types/CommonModelScopesBodyRequest.d.ts` (TYPESCRIPT) | Magnitude: 1.72 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 5, import: 4, api: 2
- `package/serialization/resources/accounting/types/DebugModeLog.d.ts` (TYPESCRIPT) | Magnitude: 1.72 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 5, import: 4, api: 2
- `package/serialization/resources/ats/types/AccountToken.d.ts` (TYPESCRIPT) | Magnitude: 1.72 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 5, import: 4, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `package/core/logging/logger.d.ts` (TYPESCRIPT) | Magnitude: 2.02 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 43, indent_spaces: 28, safety: 24, args: 19
- `package/api/resources/accounting/types/AsyncPostTaskResult.d.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 2, structural_boundaries: 2, indent_spaces: 2, class_start: 1
- `package/api/resources/hris/types/EmployeeRequest.d.ts` (TYPESCRIPT) | Magnitude: 1.64 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 15, indent_spaces: 15, doc: 13, structural_boundaries: 4
- `package/api/resources/accounting/types/ContactRequest.d.ts` (TYPESCRIPT) | Magnitude: 1.53 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 11, indent_spaces: 11, doc: 8, structural_boundaries: 2
- `package/api/resources/accounting/types/PatchedContactRequest.d.ts` (TYPESCRIPT) | Magnitude: 1.53 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 11, indent_spaces: 11, doc: 8, structural_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `package/core/fetcher/Headers.js` (JAVASCRIPT) | Magnitude: 190.78 | Delta: **0.192 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 76, state_mutation: 46, branch: 20, args: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `package/api/resources/crm/resources/leads/client/Client.d.ts` (TYPESCRIPT) | Magnitude: 25.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 16, doc: 15, indent_spaces: 13, branch: 8
- `package/api/resources/crm/resources/notes/client/Client.d.ts` (TYPESCRIPT) | Magnitude: 25.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 16, doc: 15, indent_spaces: 13, branch: 8
- `package/core/schemas/builders/object-like/getObjectLikeUtils.d.ts` (TYPESCRIPT) | Magnitude: 0.47 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 9, generics: 7, ui_framework: 6, args: 2
- `package/api/resources/crm/resources/customObjects/client/Client.d.ts` (TYPESCRIPT) | Magnitude: 25.3 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 19, structural_boundaries: 16, indent_spaces: 13, branch: 8
- `package/api/resources/ats/resources/applications/client/Client.d.ts` (TYPESCRIPT) | Magnitude: 27.9 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 17, structural_boundaries: 16, indent_spaces: 14, branch: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/core/fetcher/getFetchFn.js` (JAVASCRIPT) | Magnitude: 139.4 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 44, branch: 42, state_mutation: 42, structural_boundaries: 25
- `package/core/fetcher/makeRequest.js` (JAVASCRIPT) | Magnitude: 64.38 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, state_mutation: 15, branch: 14, args: 8
- `package/core/fetcher/stream-wrappers/chooseStreamWrapper.js` (JAVASCRIPT) | Magnitude: 141.08 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 43, branch: 42, state_mutation: 42, structural_boundaries: 25
- `package/core/fetcher/requestWithRetries.js` (JAVASCRIPT) | Magnitude: 108.84 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 50, branch: 23, structural_boundaries: 14, immutability_locks: 14
- `package/core/pagination/CustomPager.js` (JAVASCRIPT) | Magnitude: 306.1 | Delta: **0.138 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 147, state_mutation: 111, branch: 54, structural_boundaries: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `package/core/json.js` (JAVASCRIPT) | Magnitude: 7.22 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 3, api: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `package/api/resources/accounting/types/RemoteData.d.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, indent_spaces: 2, branch: 1
- `package/api/resources/ats/types/RemoteData.d.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, indent_spaces: 2, branch: 1
- `package/api/resources/crm/types/RemoteData.d.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, indent_spaces: 2, branch: 1
- `package/api/resources/filestorage/types/RemoteData.d.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, indent_spaces: 2, branch: 1
- `package/api/resources/hris/types/RemoteData.d.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, indent_spaces: 2, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/core/schemas/builders/schema-utils/JsonError.d.ts` (TYPESCRIPT) | Magnitude: 1.77 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 2, args: 1, func_start: 1
- `package/core/schemas/builders/schema-utils/ParseError.d.ts` (TYPESCRIPT) | Magnitude: 1.77 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 2, args: 1, func_start: 1
- `package/api/resources/crm/types/Opportunity.d.ts` (TYPESCRIPT) | Magnitude: 1.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 15, indent_spaces: 15, doc: 12, structural_boundaries: 4
- `package/api/resources/accounting/types/AccountDetailsAndActionsStatusEnum.d.ts` (TYPESCRIPT) | Magnitude: 1.56 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: immutability_locks: 5, structural_boundaries: 4, indent_spaces: 4, api: 2
- `package/api/resources/accounting/types/AsyncPostTaskStatusEnum.d.ts` (TYPESCRIPT) | Magnitude: 1.56 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: immutability_locks: 5, structural_boundaries: 4, indent_spaces: 4, api: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/core/schemas/Schema.js` -> **Severity: 537.797** (Blast Radius: 5.705 * Doc Risk: 94.2676%)
- `package/core/schemas/utils/maybeSkipValidation.js` -> **Severity: 207.799** (Blast Radius: 2.078 * Doc Risk: 99.9993%)
- `package/core/schemas/builders/list/list.js` -> **Severity: 192.356** (Blast Radius: 1.924 * Doc Risk: 99.9772%)
- `package/core/schemas/utils/getErrorMessageForIncorrectType.js` -> **Severity: 174.57** (Blast Radius: 1.746 * Doc Risk: 99.9828%)
- `package/core/schemas/utils/createIdentitySchemaCreator.js` -> **Severity: 82.7** (Blast Radius: 0.827 * Doc Risk: 99.9998%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
