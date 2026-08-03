# ARCHITECTURAL_BRIEF: fineract
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/fineract` |
| **Timestamp** | `2026-08-03T20:15:17.519852+00:00` |
| **Scan Duration** | `27.66s` |
| **Git Branch** | `develop` |
| **Git Commit** | `e6e5a4b6eec5a33d327546c640e6b7f281b5ae42` |
| **Git Remote** | `https://github.com/apache/fineract.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 5884 malicious artifacts.

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
| Total Artifacts | 6858 |
| Analyzed Artifacts (Scanned) | 6335 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 523 |
| Total LOC | 511667 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 92.4% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1891 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 302 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 5814 | 504411 | 91.8% |
| XML | 332 | 0 | 5.2% |
| GROOVY | 48 | 2931 | 0.8% |
| PLAINTEXT | 38 | 1 | 0.6% |
| MARKDOWN | 32 | 0 | 0.5% |
| YAML | 27 | 911 | 0.4% |
| JSON | 19 | 607 | 0.3% |
| SQLITE | 14 | 1575 | 0.2% |
| SHELL | 7 | 296 | 0.1% |
| HTML | 2 | 235 | 0.0% |
| CSS | 1 | 630 | 0.0% |
| BATCH | 1 | 70 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.938`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 3753 | 59.2% |
| file_cluster_8 | 2151 | 34.0% |
| file_cluster_16 | 229 | 3.6% |
| file_cluster_0 | 113 | 1.8% |
| file_cluster_4 | 11 | 0.2% |
| file_cluster_17 | 2 | 0.0% |
| file_cluster_9 | 2 | 0.0% |
| file_cluster_7 | 2 | 0.0% |
| Unknown | 1 | 0.0% |
| file_cluster_11 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 69 | 1.1% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 523*

**Composition by Extension & Reason:**
- `.adoc`: 156x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 4 exceeds 500 chars), 1x Excluded (Saturation: Line 15 exceeds 500 chars)
- `.avsc`: 83x Unsupported Format (.avsc)
- `.feature`: 69x Unsupported Format (.feature)
- `.gradle`: 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 15x Unsupported Format (.undeterminable), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 250 LOC)
- `.xml`: 7x Excluded (Saturation: Line 28 exceeds 500 chars), 2x Excluded (Saturation: Line 32 exceeds 500 chars), 2x Excluded (Massive Static Asset Blob: 3121 LOC)
- `.yml`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.env`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 17x Excluded (Explicitly Denied Extension: '.png')
- `.ftl`: 15x Unsupported Format (.ftl)
- `.sql`: 2x Excluded (Static Asset Blob without Intent: 1921 LOC), 2x Excluded (Static Asset Blob without Intent: 1895 LOC), 1x Excluded (Static Asset Blob without Intent: 1919 LOC)
- `.mustache`: 5x Unsupported Format (.mustache), 1x Excluded (Saturation: Line 47 exceeds 500 chars)
- `.java`: 1x Excluded (Saturation: Line 68 exceeds 500 chars), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 67 exceeds 500 chars)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 2432 LOC), 1x Excluded (Static Asset Blob without Intent: 1073 LOC)
- `.imports`: 4x Unsupported Format (.imports)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 8.6 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 29.3 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 26.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 14.0 | 2.3 | 0.0 |
| API Exposure | 0.0 | 19.7 | 5.2 | 5.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 9.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 72.9 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 85.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 6.1 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 3.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 51.3 | 58.4 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 48.2 | 25.3 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 34.4 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `fineract-db/old-schema-files/0003-mifosx-permissions-and-authorisation-utf8.sql` (Hits: 131)
- `fineract-db/multi-tenant-demo-backups/ceda/ceda-schema-customisations.sql` (Hits: 57)
- `fineract-db/old-schema-files/0002-mifosx-base-reference-data-utf8.sql` (Hits: 37)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **LocalDate.java** (`fineract-validation/src/main/java/org/apache/fineract/validation/constraints/LocalDate.java`) — 994 inbound connections
2. **JsonCommand.java** (`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/api/JsonCommand.java`) — 865 inbound connections
3. **CommandProcessingResult.java** (`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/data/CommandProcessingResult.java`) — 811 inbound connections
4. **Component.java** (`fineract-provider/src/main/java/org/apache/fineract/spm/domain/Component.java`) — 705 inbound connections
5. **NewCommandSourceHandler.java** (`fineract-core/src/main/java/org/apache/fineract/commands/handler/NewCommandSourceHandler.java`) — 459 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **LoanWritePlatformServiceJpaRepositoryImpl.java** (`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanWritePlatformServiceJpaRepositoryImpl.java`) — 207 outbound dependencies
2. **LoanAccountConfiguration.java** (`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/starter/LoanAccountConfiguration.java`) — 170 outbound dependencies
3. **LoansApiResource.java** (`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/api/LoansApiResource.java`) — 168 outbound dependencies
4. **FineractFeignClient.java** (`fineract-client-feign/src/main/java/org/apache/fineract/client/feign/FineractFeignClient.java`) — 156 outbound dependencies
5. **LoanStepDef.java** (`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanStepDef.java`) — 154 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `createChargeAppliedTransaction` (@ `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanChargeService.java`) -> Impact: **1843.2** | LOC: 744
- `applyEarlyPaymentStrategy` (@ `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/AbstractCumulativeLoanScheduleGenerator.java`) -> Impact: **1627.5** | LOC: 830
- `validateForCreate` (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/serialization/LoanProductDataValidator.java`) -> Impact: **968.6** | LOC: 682
- `periodicInterestRate` (@ `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/LoanApplicationTerms.java`) -> Impact: **914.3** | LOC: 70
- `validateForUpdate` (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/serialization/LoanProductDataValidator.java`) -> Impact: **817.2** | LOC: 704
- `validateForCreate` (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanApplicationValidator.java`) -> Impact: **808.1** | LOC: 559
- `importWorkbook` (@ `fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/service/BulkImportWorkbookServiceImpl.java`) -> Impact: **742.0** | LOC: 95
- `validateForModify` (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanApplicationValidator.java`) -> Impact: **685.8** | LOC: 621
- `parseDatatableColumnForUpdate` (@ `fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/service/DatatableWriteServiceImpl.java`) -> Impact: **635.6** | LOC: 102
- `testCreateShareAccountWithCharges` (@ `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/shares/ShareAccountIntegrationTests.java`) -> Impact: **606.2** | LOC: 625

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `decode` (@ `fineract-client-feign/src/main/java/org/apache/fineract/client/feign/FineractErrorDecoder.java`) -> **O(2^N) [Recursive]**
  * *Intent:* * or more contributor license agreements. See the NOTICE file * distributed with this work for additional information * regarding copyright ownership....
- `processCommand` (@ `fineract-core/src/main/java/org/apache/fineract/commands/service/CommandSourceService.java`) -> **O(2^N) [Recursive]**
- `cacheType` (@ `fineract-core/src/main/java/org/apache/fineract/infrastructure/cache/CacheEnumerations.java`) -> **O(2^N) [Recursive]**
  * *Intent:* * or more contributor license agreements. See the NOTICE file * distributed with this work for additional information * regarding copyright ownership....
- `getOperand` (@ `fineract-core/src/main/java/org/apache/fineract/infrastructure/security/utils/ColumnValidator.java`) -> **O(2^N) [Recursive]**
- `update` (@ `fineract-core/src/main/java/org/apache/fineract/portfolio/calendar/domain/Calendar.java`) -> **O(2^N) [Recursive]**
  * *Intent:* /* * If meeting start date is changed then there is possibilities of recurring day may change, so derive the
- `constructRecurrence` (@ `fineract-core/src/main/java/org/apache/fineract/portfolio/calendar/domain/Calendar.java`) -> **O(2^N) [Recursive]**
- `isValidRecurringDate` (@ `fineract-core/src/main/java/org/apache/fineract/portfolio/calendar/domain/Calendar.java`) -> **O(2^N) [Recursive]**
- `getNextRepaymentMeetingDate` (@ `fineract-core/src/main/java/org/apache/fineract/portfolio/calendar/service/CalendarUtils.java`) -> **O(2^N) [Recursive]**
- `status` (@ `fineract-core/src/main/java/org/apache/fineract/portfolio/group/domain/GroupingTypeEnumerations.java`) -> **O(2^N) [Recursive]**
  * *Intent:* * Licensed to the Apache Software Foundation (ASF) under one * or more contributor license agreements. See the NOTICE file * distributed with this wor...
- `calculateInterest` (@ `fineract-core/src/main/java/org/apache/fineract/portfolio/savings/domain/interest/PostingPeriod.java`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `Declarative_Block` (@ `fineract-db/old-schema-files/0003-mifosx-permissions-and-authorisation-utf8.sql`) -> DB Complexity: **386**
  * *Intent:* -- to you under the Apache License, Version 2.0 (the -- "License"); you may not use this file except in compliance -- with the License. You may obtain...
- `getDefaultExternalEventConfigurations` (@ `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/ExternalEventConfigurationHelper.java`) -> DB Complexity: **366**
- `getAllDefaultGlobalConfigurations` (@ `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/GlobalConfigurationHelper.java`) -> DB Complexity: **319**
- `createChargeAppliedTransaction` (@ `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanChargeService.java`) -> DB Complexity: **111**
- `update` (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanProductUpdateUtil.java`) -> DB Complexity: **105**
- `updateLoanRepaymentSchedule` (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanProductRelatedDetailUpdateUtil.java`) -> DB Complexity: **93**
- `build` (@ `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/loans/LoanProductTestBuilder.java`) -> DB Complexity: **90**
- `testLoanImport` (@ `integration-tests/src/test/java/org/apache/fineract/integrationtests/bulkimport/importhandler/loan/LoanImportHandlerTest.java`) -> DB Complexity: **87**
- `update` (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanProductInterestRecalculationDetailsUpdateUtil.java`) -> DB Complexity: **82**
  * *Intent:* * regarding copyright ownership. The ASF licenses this file * to you under the Apache License, Version 2.0 (the * "License"); you may not use this fil...
- `Anonymous_Block` (@ `scripts/split-features.sh`) -> DB Complexity: **79**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `integration-tests/src/test/java/org/apache/fineract/integrationtests` | 227 | 44141.82 | 10.57% | 0.0% |
| `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain` | 73 | 26498.93 | 9.52% | 39.86% |
| `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service` | 46 | 19515.8 | 24.46% | 44.61% |
| `fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service` | 18 | 12249.22 | 11.68% | 15.5% |
| `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain` | 26 | 12079.78 | 7.77% | 35.69% |
| `fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain` | 40 | 11984.06 | 12.09% | 64.7% |
| `fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service` | 27 | 11047.46 | 8.63% | 21.99% |
| `integration-tests/src/test/java/org/apache/fineract/integrationtests/common` | 44 | 9957.88 | 21.41% | 0.0% |
| `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan` | 17 | 8321.98 | 18.2% | 0.0% |
| `fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/service` | 15 | 6018.23 | 18.2% | 39.93% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `config/docker/mysql/docker-entrypoint-initdb.d/01-databases.sql` -> **100.0%** Exposure
- `fineract-db/mifospltaform-tenants-first-time-install.sql` -> **100.0%** Exposure
- `fineract-db/multi-tenant-demo-backups/0001-mifos-platform-shared-tenants.sql` -> **100.0%** Exposure
- `fineract-db/multi-tenant-demo-backups/ceda/ceda-schema-customisations.sql` -> **100.0%** Exposure
- `fineract-db/multi-tenant-demo-backups/ceda/ceda-user-office-product-setup.sql` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `scripts/split-features.sh` -> **100.0%** Exposure
- `scripts/split-tests.sh` -> **100.0%** Exposure
- `fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/service/ProductToGLAccountMappingReadPlatformServiceImpl.java` -> **100.0%** Exposure
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/config/AbstractFineractModuleProperties.java` -> **100.0%** Exposure
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/config/FineractProperties.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanStepDef.java` -> **168** Orphaned Functions | **31** Duplicates
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/loans/LoanTransactionHelper.java` -> **0** Orphaned Functions | **147** Duplicates
- `fineract-progressive-loan/src/test/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculatorTest.java` -> **78** Orphaned Functions | **40** Duplicates
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/AdvancedPaymentAllocationLoanRepaymentScheduleTest.java` -> **80** Orphaned Functions | **6** Duplicates
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/MathUtil.java` -> **0** Orphaned Functions | **75** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepository.java`** -> AI Confidence: **99.48%**
2. **`fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/AccrualBasedAccountingProcessorForLoan.java`** -> AI Confidence: **99.48%**
3. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/serialization/LoanProductDataValidator.java`** -> AI Confidence: **99.48%**
4. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/service/ProductToGLAccountMappingReadPlatformServiceImpl.java`** -> AI Confidence: **99.39%**
5. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/DefaultLoanLifecycleStateMachine.java`** -> AI Confidence: **99.39%**
6. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanTransactionRepository.java`** -> AI Confidence: **99.39%**
7. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/AbstractCumulativeLoanScheduleGenerator.java`** -> AI Confidence: **99.39%**
8. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanChargeService.java`** -> AI Confidence: **99.39%**
9. **`fineract-progressive-loan/src/test/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculatorTest.java`** -> AI Confidence: **99.39%**
10. **`fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/AccrualBasedAccountingProcessorForSavings.java`** -> AI Confidence: **99.39%**
11. **`fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/CashBasedAccountingProcessorForLoan.java`** -> AI Confidence: **99.39%**
12. **`fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/CashBasedAccountingProcessorForSavings.java`** -> AI Confidence: **99.39%**
13. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanProductInterestRecalculationDetailsUpdateUtil.java`** -> AI Confidence: **99.39%**
14. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanProductUpdateUtil.java`** -> AI Confidence: **99.39%**
15. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/self/products/api/SelfLoanProductsApiResource.java`** -> AI Confidence: **99.39%**
16. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/client/feign/tests/FeignLoanAccrualOnClosedLoanTest.java`** -> AI Confidence: **99.39%**
17. **`buildSrc/src/main/groovy/org/apache/fineract/gradle/FineractPlugin.groovy`** -> AI Confidence: **99.35%**
18. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepaymentScheduleProcessingWrapper.java`** -> AI Confidence: **99.35%**
19. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/domain/ProductToGLAccountMappingRepository.java`** -> AI Confidence: **99.34%**
20. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/AprCalculator.java`** -> AI Confidence: **99.34%**
21. **`fineract-charge/src/main/java/org/apache/fineract/portfolio/charge/domain/Charge.java`** -> AI Confidence: **99.31%**
22. **`fineract-charge/src/main/java/org/apache/fineract/portfolio/charge/serialization/ChargeDefinitionCommandFromApiJsonDeserializer.java`** -> AI Confidence: **99.31%**
23. **`fineract-client-feign/src/main/java/org/apache/fineract/client/feign/services/ImagesApi.java`** -> AI Confidence: **99.31%**
24. **`fineract-client-feign/src/main/java/org/apache/fineract/client/util/FeignParts.java`** -> AI Confidence: **99.31%**
25. **`fineract-client/src/main/java/org/apache/fineract/client/util/Parts.java`** -> AI Confidence: **99.31%**
26. **`fineract-command/src/test/java/org/apache/fineract/command/CommandBaseTest.java`** -> AI Confidence: **99.31%**
27. **`fineract-core/src/main/java/org/apache/fineract/batch/command/CommandStrategyProvider.java`** -> AI Confidence: **99.31%**
28. **`fineract-core/src/main/java/org/apache/fineract/commands/service/SynchronousCommandProcessingService.java`** -> AI Confidence: **99.31%**
29. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/data/DataValidatorBuilder.java`** -> AI Confidence: **99.31%**
30. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/serialization/JsonParserHelper.java`** -> AI Confidence: **99.31%**
31. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/database/DatabasePasswordEncryptor.java`** -> AI Confidence: **99.31%**
32. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/database/DatabaseSpecificSQLGenerator.java`** -> AI Confidence: **99.31%**
33. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/security/utils/ColumnValidator.java`** -> AI Confidence: **99.31%**
34. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/security/utils/SQLBuilder.java`** -> AI Confidence: **99.31%**
35. **`fineract-core/src/main/java/org/apache/fineract/portfolio/calendar/service/CalendarUtils.java`** -> AI Confidence: **99.31%**
36. **`fineract-core/src/main/java/org/apache/fineract/portfolio/common/service/CommonEnumerations.java`** -> AI Confidence: **99.31%**
37. **`fineract-core/src/main/java/org/apache/fineract/portfolio/savings/data/SavingsAccountSummaryData.java`** -> AI Confidence: **99.31%**
38. **`fineract-core/src/main/java/org/apache/fineract/portfolio/savings/domain/SavingsHelper.java`** -> AI Confidence: **99.31%**
39. **`fineract-core/src/main/java/org/apache/fineract/portfolio/savings/domain/interest/AnnualCompoundingPeriod.java`** -> AI Confidence: **99.31%**
40. **`fineract-core/src/main/java/org/apache/fineract/portfolio/savings/domain/interest/BiAnnualCompoundingPeriod.java`** -> AI Confidence: **99.31%**
41. **`fineract-core/src/main/java/org/apache/fineract/portfolio/savings/domain/interest/MonthlyCompoundingPeriod.java`** -> AI Confidence: **99.31%**
42. **`fineract-core/src/main/java/org/apache/fineract/portfolio/savings/domain/interest/PostingPeriod.java`** -> AI Confidence: **99.31%**
43. **`fineract-core/src/main/java/org/apache/fineract/portfolio/savings/domain/interest/QuarterlyCompoundingPeriod.java`** -> AI Confidence: **99.31%**
44. **`fineract-core/src/main/java/org/apache/fineract/portfolio/savings/service/SavingsEnumerations.java`** -> AI Confidence: **99.31%**
45. **`fineract-core/src/main/java/org/apache/fineract/portfolio/search/data/AdHocQueryDataValidator.java`** -> AI Confidence: **99.31%**
46. **`fineract-core/src/main/java/org/apache/fineract/portfolio/search/service/SearchUtil.java`** -> AI Confidence: **99.31%**
47. **`fineract-core/src/test/java/org/apache/fineract/batch/service/ResolutionHelperTest.java`** -> AI Confidence: **99.31%**
48. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/helper/ErrorMessageHelper.java`** -> AI Confidence: **99.31%**
49. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/initializer/base/FineractInitializer.java`** -> AI Confidence: **99.31%**
50. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/messaging/event/EventCheckHelper.java`** -> AI Confidence: **99.31%**
51. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/assetexternalization/AssetExternalizationStepDef.java`** -> AI Confidence: **99.31%**
52. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/common/JournalEntriesStepDef.java`** -> AI Confidence: **99.31%**
53. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanDelinquencyStepDef.java`** -> AI Confidence: **99.31%**
54. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanReAgingStepDef.java`** -> AI Confidence: **99.31%**
55. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanReAmortizationStepDef.java`** -> AI Confidence: **99.31%**
56. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanRescheduleStepDef.java`** -> AI Confidence: **99.31%**
57. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/delinquency/service/DelinquencyWritePlatformServiceHelper.java`** -> AI Confidence: **99.31%**
58. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/delinquency/service/LoanDelinquencyDomainServiceImpl.java`** -> AI Confidence: **99.31%**
59. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/data/AccrualPeriodData.java`** -> AI Confidence: **99.31%**
60. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/data/LoanTermVariationsDataWrapper.java`** -> AI Confidence: **99.31%**
61. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanSummary.java`** -> AI Confidence: **99.31%**
62. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/SingleLoanChargeRepaymentScheduleProcessingWrapper.java`** -> AI Confidence: **99.31%**
63. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/AbstractLoanRepaymentScheduleTransactionProcessor.java`** -> AI Confidence: **99.31%**
64. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/impl/DuePenFeeIntPriInAdvancePriPenFeeIntLoanRepaymentScheduleTransactionProcessor.java`** -> AI Confidence: **99.31%**
65. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/impl/DuePenIntPriFeeInAdvancePenIntPriFeeLoanRepaymentScheduleTransactionProcessor.java`** -> AI Confidence: **99.31%**
66. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/impl/EarlyPaymentLoanRepaymentScheduleTransactionProcessor.java`** -> AI Confidence: **99.31%**
67. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/impl/HeavensFamilyLoanRepaymentScheduleTransactionProcessor.java`** -> AI Confidence: **99.31%**
68. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/impl/RBILoanRepaymentScheduleTransactionProcessor.java`** -> AI Confidence: **99.31%**
69. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/DefaultPaymentPeriodsInOneYearCalculator.java`** -> AI Confidence: **99.31%**
70. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/DefaultScheduledDateGenerator.java`** -> AI Confidence: **99.31%**
71. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/LoanApplicationTerms.java`** -> AI Confidence: **99.31%**
72. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanChargeApiJsonValidator.java`** -> AI Confidence: **99.31%**
73. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanDownPaymentTransactionValidator.java`** -> AI Confidence: **99.31%**
74. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanBalanceService.java`** -> AI Confidence: **99.31%**
75. **`fineract-loan/src/test/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepaymentScheduleInstallmentTest.java`** -> AI Confidence: **99.31%**
76. **`fineract-mix/src/main/java/org/apache/fineract/mix/service/MixReportXBRLBuilder.java`** -> AI Confidence: **99.31%**
77. **`fineract-progressive-loan-embeddable-schedule-generator/misc/Main.java`** -> AI Confidence: **99.31%**
78. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/impl/AdvancedPaymentScheduleTransactionProcessor.java`** -> AI Confidence: **99.31%**
79. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/impl/ChangeOperation.java`** -> AI Confidence: **99.31%**
80. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/ProgressiveLoanScheduleGenerator.java`** -> AI Confidence: **99.31%**
81. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculator.java`** -> AI Confidence: **99.31%**
82. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/domain/AdvancedPaymentAllocationsValidator.java`** -> AI Confidence: **99.31%**
83. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/domain/CreditAllocationsValidator.java`** -> AI Confidence: **99.31%**
84. **`fineract-progressive-loan/src/test/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/impl/ChangeOperationTest.java`** -> AI Confidence: **99.31%**
85. **`fineract-progressive-loan/src/test/java/org/apache/fineract/portfolio/loanproduct/calc/data/InterestPeriodTest.java`** -> AI Confidence: **99.31%**
86. **`fineract-progressive-loan/src/test/java/org/apache/fineract/portfolio/loanproduct/calc/data/RepaymentPeriodTest.java`** -> AI Confidence: **99.31%**
87. **`fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/CashBasedAccountingProcessorForShares.java`** -> AI Confidence: **99.31%**
88. **`fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/JournalEntryReadPlatformServiceImpl.java`** -> AI Confidence: **99.31%**
89. **`fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/JournalEntryRunningBalanceUpdateServiceImpl.java`** -> AI Confidence: **99.31%**
90. **`fineract-provider/src/main/java/org/apache/fineract/accounting/productaccountmapping/service/ProductToGLAccountMappingWritePlatformServiceImpl.java`** -> AI Confidence: **99.31%**
91. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/ImportHandlerUtils.java`** -> AI Confidence: **99.31%**
92. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/fixeddeposits/FixedDepositImportHandler.java`** -> AI Confidence: **99.31%**
93. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/recurringdeposit/RecurringDepositImportHandler.java`** -> AI Confidence: **99.31%**
94. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/savings/SavingsImportHandler.java`** -> AI Confidence: **99.31%**
95. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/LoanProductSheetPopulator.java`** -> AI Confidence: **99.31%**
96. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/RecurringDepositProductSheetPopulator.java`** -> AI Confidence: **99.31%**
97. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/jobs/executeemail/ExecuteEmailTasklet.java`** -> AI Confidence: **99.31%**
98. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/service/migration/TenantDatabaseUpgradeService.java`** -> AI Confidence: **99.31%**
99. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/service/DatatableUtil.java`** -> AI Confidence: **99.31%**
100. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/service/DatatableWriteServiceImpl.java`** -> AI Confidence: **99.31%**
101. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/jobs/domain/JobExecutionRepository.java`** -> AI Confidence: **99.31%**
102. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/account/service/AccountNumberGenerator.java`** -> AI Confidence: **99.31%**
103. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/account/service/AccountTransferEnumerations.java`** -> AI Confidence: **99.31%**
104. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/account/service/AccountTransfersReadPlatformServiceImpl.java`** -> AI Confidence: **99.31%**
105. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/account/service/PortfolioAccountReadPlatformServiceImpl.java`** -> AI Confidence: **99.31%**
106. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/calendar/serialization/CalendarCommandFromApiJsonDeserializer.java`** -> AI Confidence: **99.31%**
107. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/calendar/service/CalendarReadPlatformServiceImpl.java`** -> AI Confidence: **99.31%**
108. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/api/ClientsApiResource.java`** -> AI Confidence: **99.31%**
109. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/service/ClientFamilyMembersWritePlatformServiceImpl.java`** -> AI Confidence: **99.31%**
110. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/api/LoanTransactionsApiResource.java`** -> AI Confidence: **99.31%**
111. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/service/LoanScheduleAssembler.java`** -> AI Confidence: **99.31%**
112. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanApplicationValidator.java`** -> AI Confidence: **99.31%**
113. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanAccrualActivityProcessingServiceImpl.java`** -> AI Confidence: **99.31%**
114. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanAccrualsProcessingServiceImpl.java`** -> AI Confidence: **99.31%**
115. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanAssemblerImpl.java`** -> AI Confidence: **99.31%**
116. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanBuyDownFeeAmortizationProcessingServiceImpl.java`** -> AI Confidence: **99.31%**
117. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanCapitalizedIncomeAmortizationProcessingServiceImpl.java`** -> AI Confidence: **99.31%**
118. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanChargeAssembler.java`** -> AI Confidence: **99.31%**
119. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanDisbursementService.java`** -> AI Confidence: **99.31%**
120. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanProductRelatedDetailUpdateUtil.java`** -> AI Confidence: **99.31%**
121. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanRepaymentScheduleService.java`** -> AI Confidence: **99.31%**
122. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/note/service/NoteReadPlatformServiceImpl.java`** -> AI Confidence: **99.31%**
123. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/api/SavingsAccountsApiResource.java`** -> AI Confidence: **99.31%**
124. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/domain/RecurringDepositAccount.java`** -> AI Confidence: **99.31%**
125. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/SavingsAccountInterestPostingServiceImpl.java`** -> AI Confidence: **99.31%**
126. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/search/service/SearchReadPlatformServiceImpl.java`** -> AI Confidence: **99.31%**
127. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/serialization/ShareAccountDataSerializer.java`** -> AI Confidence: **99.31%**
128. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/service/SharesEnumerations.java`** -> AI Confidence: **99.31%**
129. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareproducts/serialization/ShareProductDataSerializer.java`** -> AI Confidence: **99.31%**
130. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/transfer/service/TransferWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.31%**
131. **`fineract-provider/src/test/java/org/apache/fineract/batch/command/internal/AdjustLoanTransactionByExternalIdCommandStrategyTest.java`** -> AI Confidence: **99.31%**
132. **`fineract-provider/src/test/java/org/apache/fineract/batch/command/internal/AdjustLoanTransactionCommandStrategyTest.java`** -> AI Confidence: **99.31%**
133. **`fineract-provider/src/test/java/org/apache/fineract/batch/command/internal/GetLoanTransactionByExternalIdCommandStrategyTest.java`** -> AI Confidence: **99.31%**
134. **`fineract-provider/src/test/java/org/apache/fineract/batch/command/internal/GetLoanTransactionByIdCommandStrategyTest.java`** -> AI Confidence: **99.31%**
135. **`fineract-provider/src/test/java/org/apache/fineract/commands/service/SynchronousCommandProcessingServiceTest.java`** -> AI Confidence: **99.31%**
136. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/core/config/ContentS3ConfigTest.java`** -> AI Confidence: **99.31%**
137. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/jobs/filter/LoanCOBFilterHelperTest.java`** -> AI Confidence: **99.31%**
138. **`fineract-rates/src/main/java/org/apache/fineract/portfolio/floatingrates/serialization/FloatingRateDataValidator.java`** -> AI Confidence: **99.31%**
139. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/interestratechart/domain/InterestRateChartSlabFields.java`** -> AI Confidence: **99.31%**
140. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/data/SavingsProductAccountingDataValidator.java`** -> AI Confidence: **99.31%**
141. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain/DepositTermDetail.java`** -> AI Confidence: **99.31%**
142. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain/SavingsAccountCharge.java`** -> AI Confidence: **99.31%**
143. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain/SavingsAccountRepository.java`** -> AI Confidence: **99.31%**
144. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain/SavingsAccountSummary.java`** -> AI Confidence: **99.31%**
145. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/service/SavingsSchedularInterestPoster.java`** -> AI Confidence: **99.31%**
146. **`fineract-security/src/main/java/org/apache/fineract/infrastructure/security/service/SqlInjectionPreventerServiceImpl.java`** -> AI Confidence: **99.31%**
147. **`fineract-working-capital-loan/src/main/java/org/apache/fineract/portfolio/workingcapitalloanproduct/domain/WorkingCapitalAdvancedPaymentAllocationsValidator.java`** -> AI Confidence: **99.31%**
148. **`fineract-working-capital-loan/src/main/java/org/apache/fineract/portfolio/workingcapitalloanproduct/serialization/WorkingCapitalLoanProductDataValidator.java`** -> AI Confidence: **99.31%**
149. **`fineract-working-capital-loan/src/main/java/org/apache/fineract/portfolio/workingcapitalloanproduct/service/WorkingCapitalLoanProductUpdateUtil.java`** -> AI Confidence: **99.31%**
150. **`fineract-working-capital-loan/src/main/java/org/apache/fineract/portfolio/workingcapitalloanproduct/service/WorkingCapitalLoanProductWritePlatformServiceImpl.java`** -> AI Confidence: **99.31%**
151. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/LoanApplicationScheduleMonthlyTest.java`** -> AI Confidence: **99.31%**
152. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/LoanChargesMultipleDebitAccountsTest.java`** -> AI Confidence: **99.31%**
153. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/LoanFixedPrincipalPercentageAmortizationTest.java`** -> AI Confidence: **99.31%**
154. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/LoanInterestPauseApiTest.java`** -> AI Confidence: **99.31%**
155. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/SqlInjectionReportingServiceIntegrationTest.java`** -> AI Confidence: **99.31%**
156. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/client/feign/tests/FeignLoanCreationTest.java`** -> AI Confidence: **99.31%**
157. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/common/BatchHelper.java`** -> AI Confidence: **99.31%**
158. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/common/shares/ShareAccountIntegrationTests.java`** -> AI Confidence: **99.31%**
159. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/useradministration/users/UserHelper.java`** -> AI Confidence: **99.31%**
160. **`buildSrc/src/main/groovy/org.apache.fineract.dependencies.gradle`** -> AI Confidence: **99.29%**
161. **`buildSrc/src/main/groovy/org.apache.fineract.release.gradle`** -> AI Confidence: **99.29%**
162. **`custom/acme/event/externalevent/dependencies.gradle`** -> AI Confidence: **99.29%**
163. **`custom/acme/event/starter/dependencies.gradle`** -> AI Confidence: **99.29%**
164. **`custom/acme/loan/cob/dependencies.gradle`** -> AI Confidence: **99.29%**
165. **`custom/acme/loan/job/dependencies.gradle`** -> AI Confidence: **99.29%**
166. **`custom/acme/loan/processor/dependencies.gradle`** -> AI Confidence: **99.29%**
167. **`custom/acme/loan/starter/dependencies.gradle`** -> AI Confidence: **99.29%**
168. **`custom/acme/note/service/dependencies.gradle`** -> AI Confidence: **99.29%**
169. **`custom/acme/note/starter/dependencies.gradle`** -> AI Confidence: **99.29%**
170. **`fineract-accounting/dependencies.gradle`** -> AI Confidence: **99.29%**
171. **`fineract-avro-schemas/dependencies.gradle`** -> AI Confidence: **99.29%**
172. **`fineract-branch/dependencies.gradle`** -> AI Confidence: **99.29%**
173. **`fineract-charge/dependencies.gradle`** -> AI Confidence: **99.29%**
174. **`fineract-client-feign/dependencies.gradle`** -> AI Confidence: **99.29%**
175. **`fineract-client/dependencies.gradle`** -> AI Confidence: **99.29%**
176. **`fineract-cob/dependencies.gradle`** -> AI Confidence: **99.29%**
177. **`fineract-command/dependencies.gradle`** -> AI Confidence: **99.29%**
178. **`fineract-core/dependencies.gradle`** -> AI Confidence: **99.29%**
179. **`fineract-document/dependencies.gradle`** -> AI Confidence: **99.29%**
180. **`fineract-investor/dependencies.gradle`** -> AI Confidence: **99.29%**
181. **`fineract-loan-origination/dependencies.gradle`** -> AI Confidence: **99.29%**
182. **`fineract-loan/dependencies.gradle`** -> AI Confidence: **99.29%**
183. **`fineract-mix/dependencies.gradle`** -> AI Confidence: **99.29%**
184. **`fineract-progressive-loan-embeddable-schedule-generator/dependencies.gradle`** -> AI Confidence: **99.29%**
185. **`fineract-progressive-loan/dependencies.gradle`** -> AI Confidence: **99.29%**
186. **`fineract-provider/dependencies.gradle`** -> AI Confidence: **99.29%**
187. **`fineract-rates/dependencies.gradle`** -> AI Confidence: **99.29%**
188. **`fineract-report/dependencies.gradle`** -> AI Confidence: **99.29%**
189. **`fineract-savings/dependencies.gradle`** -> AI Confidence: **99.29%**
190. **`fineract-security/dependencies.gradle`** -> AI Confidence: **99.29%**
191. **`fineract-tax/dependencies.gradle`** -> AI Confidence: **99.29%**
192. **`fineract-validation/dependencies.gradle`** -> AI Confidence: **99.29%**
193. **`fineract-working-capital-loan/dependencies.gradle`** -> AI Confidence: **99.29%**
194. **`integration-tests/dependencies.gradle`** -> AI Confidence: **99.29%**
195. **`oauth2-tests/dependencies.gradle`** -> AI Confidence: **99.29%**
196. **`settings.gradle`** -> AI Confidence: **99.29%**
197. **`twofactor-tests/dependencies.gradle`** -> AI Confidence: **99.29%**
198. **`scripts/verify-signed-commits.sh`** -> AI Confidence: **99.29%**
199. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/configuration/api/GlobalConfigurationConstants.java`** -> AI Confidence: **99.29%**
200. **`fineract-core/src/main/java/org/apache/fineract/portfolio/common/domain/DayOfWeekType.java`** -> AI Confidence: **99.29%**
201. **`integration-tests/src/test/resources/image-text-wrong-content.jsp`** -> AI Confidence: **99.29%**
202. **`buildSrc/src/main/groovy/org/apache/fineract/gradle/service/GpgService.groovy`** -> AI Confidence: **99.24%**
203. **`buildSrc/src/main/groovy/org/apache/fineract/gradle/service/JiraService.groovy`** -> AI Confidence: **99.24%**
204. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/service/ProductToGLAccountMappingHelper.java`** -> AI Confidence: **99.24%**
205. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/service/SavingsProductToGLAccountMappingHelper.java`** -> AI Confidence: **99.24%**
206. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/service/ShareProductToGLAccountMappingHelper.java`** -> AI Confidence: **99.24%**
207. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/rule/domain/AccountingRule.java`** -> AI Confidence: **99.24%**
208. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/rule/service/AccountingRuleWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
209. **`fineract-branch/src/main/java/org/apache/fineract/organisation/teller/domain/Cashier.java`** -> AI Confidence: **99.24%**
210. **`fineract-client-feign/src/main/java/org/apache/fineract/client/feign/FineractMultipartEncoder.java`** -> AI Confidence: **99.24%**
211. **`fineract-client-feign/src/test/java/org/apache/fineract/client/feign/integration/FineractFeignClientIntegrationTest.java`** -> AI Confidence: **99.24%**
212. **`fineract-client-feign/src/test/java/org/apache/fineract/client/feign/performance/ConnectionPoolPerformanceTest.java`** -> AI Confidence: **99.24%**
213. **`fineract-core/src/main/java/org/apache/fineract/accounting/glaccount/domain/GLAccount.java`** -> AI Confidence: **99.24%**
214. **`fineract-core/src/main/java/org/apache/fineract/batch/command/CommandStrategyUtils.java`** -> AI Confidence: **99.24%**
215. **`fineract-core/src/main/java/org/apache/fineract/batch/service/BatchApiServiceImpl.java`** -> AI Confidence: **99.24%**
216. **`fineract-core/src/main/java/org/apache/fineract/batch/service/ResolutionHelper.java`** -> AI Confidence: **99.24%**
217. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/domain/FineractPlatformTenantConnection.java`** -> AI Confidence: **99.24%**
218. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/exception/ErrorHandler.java`** -> AI Confidence: **99.24%**
219. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/serialization/DatatableCommandFromApiJsonDeserializer.java`** -> AI Confidence: **99.24%**
220. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/database/JavaType.java`** -> AI Confidence: **99.24%**
221. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/database/metrics/TenantConnectionPoolMetricsTracker.java`** -> AI Confidence: **99.24%**
222. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/event/business/service/BusinessEventNotifierServiceImpl.java`** -> AI Confidence: **99.24%**
223. **`fineract-core/src/main/java/org/apache/fineract/portfolio/calendar/domain/Calendar.java`** -> AI Confidence: **99.24%**
224. **`fineract-core/src/main/java/org/apache/fineract/portfolio/client/domain/ClientRepository.java`** -> AI Confidence: **99.24%**
225. **`fineract-core/src/main/java/org/apache/fineract/portfolio/group/domain/Group.java`** -> AI Confidence: **99.24%**
226. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanOverrideFieldsStepDef.java`** -> AI Confidence: **99.24%**
227. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanStepDef.java`** -> AI Confidence: **99.24%**
228. **`fineract-e2e-tests-runner/src/test/java/org/apache/fineract/test/initializer/suite/JobSuiteInitializerStep.java`** -> AI Confidence: **99.24%**
229. **`fineract-investor/src/main/java/org/apache/fineract/investor/service/AccountingServiceImpl.java`** -> AI Confidence: **99.24%**
230. **`fineract-loan/src/main/java/org/apache/fineract/accounting/productaccountmapping/service/LoanProductToGLAccountMappingHelper.java`** -> AI Confidence: **99.24%**
231. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/delinquency/helper/DelinquencyEffectivePauseHelperImpl.java`** -> AI Confidence: **99.24%**
232. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/Loan.java`** -> AI Confidence: **99.24%**
233. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepaymentScheduleInstallment.java`** -> AI Confidence: **99.24%**
234. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/CumulativeDecliningBalanceInterestLoanScheduleGenerator.java`** -> AI Confidence: **99.24%**
235. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanCalculateRepaymentPastDueService.java`** -> AI Confidence: **99.24%**
236. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanDownPaymentHandlerServiceImpl.java`** -> AI Confidence: **99.24%**
237. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanScheduleService.java`** -> AI Confidence: **99.24%**
238. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/domain/LoanProduct.java`** -> AI Confidence: **99.24%**
239. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/service/LoanEnumerations.java`** -> AI Confidence: **99.24%**
240. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/calc/data/ProgressiveLoanInterestScheduleModel.java`** -> AI Confidence: **99.24%**
241. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/calc/data/RepaymentPeriod.java`** -> AI Confidence: **99.24%**
242. **`fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/AccountingProcessorHelper.java`** -> AI Confidence: **99.24%**
243. **`fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/JournalEntryWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
244. **`fineract-provider/src/main/java/org/apache/fineract/commands/api/AuditsApiResource.java`** -> AI Confidence: **99.24%**
245. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/accountnumberformat/data/AccountNumberFormatDataValidator.java`** -> AI Confidence: **99.24%**
246. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/loan/LoanImportHandler.java`** -> AI Confidence: **99.24%**
247. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/AbstractWorkbookPopulator.java`** -> AI Confidence: **99.24%**
248. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/chartofaccounts/ChartOfAccountsWorkbook.java`** -> AI Confidence: **99.24%**
249. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/client/ClientEntityWorkbookPopulator.java`** -> AI Confidence: **99.24%**
250. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/service/BulkImportWorkbookServiceImpl.java`** -> AI Confidence: **99.24%**
251. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/email/data/EmailDataValidator.java`** -> AI Confidence: **99.24%**
252. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/jobs/executereportmailingjobs/ExecuteReportMailingJobsTasklet.java`** -> AI Confidence: **99.24%**
253. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/jobs/getdeliveryreportsfromsmsgateway/GetDeliveryReportsFromSmsGatewayTasklet.java`** -> AI Confidence: **99.24%**
254. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/configuration/service/ExternalServicesPropertiesReadPlatformServiceImpl.java`** -> AI Confidence: **99.24%**
255. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/diagnostics/performance/sampling/output/SamplingDataPrinter.java`** -> AI Confidence: **99.24%**
256. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/domain/Report.java`** -> AI Confidence: **99.24%**
257. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/service/EntityDatatableChecksWritePlatformServiceImpl.java`** -> AI Confidence: **99.24%**
258. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/service/GenericDataServiceImpl.java`** -> AI Confidence: **99.24%**
259. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/entityaccess/service/FineractEntityAccessReadServiceImpl.java`** -> AI Confidence: **99.24%**
260. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/event/external/producer/jms/JMSMultiExternalEventProducer.java`** -> AI Confidence: **99.24%**
261. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/gcm/domain/Sender.java`** -> AI Confidence: **99.24%**
262. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/reportmailingjob/service/ReportMailingJobEmailServiceImpl.java`** -> AI Confidence: **99.24%**
263. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/reportmailingjob/validation/ReportMailingJobValidator.java`** -> AI Confidence: **99.24%**
264. **`fineract-provider/src/main/java/org/apache/fineract/organisation/teller/service/TellerManagementReadPlatformServiceImpl.java`** -> AI Confidence: **99.24%**
265. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/account/jobs/executestandinginstructions/ExecuteStandingInstructionsTasklet.java`** -> AI Confidence: **99.24%**
266. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/account/service/AccountAssociationsReadPlatformServiceImpl.java`** -> AI Confidence: **99.24%**
267. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/account/service/AccountTransfersWritePlatformServiceImpl.java`** -> AI Confidence: **99.24%**
268. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/account/service/StandingInstructionHistoryReadPlatformServiceImpl.java`** -> AI Confidence: **99.24%**
269. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/account/service/StandingInstructionReadPlatformServiceImpl.java`** -> AI Confidence: **99.24%**
270. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/data/ClientDataValidator.java`** -> AI Confidence: **99.24%**
271. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/serialization/ClientFamilyMemberCommandFromApiJsonDeserializer.java`** -> AI Confidence: **99.24%**
272. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/service/ClientWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
273. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/group/api/GroupsApiResource.java`** -> AI Confidence: **99.24%**
274. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/group/service/GroupingTypesWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
275. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/interestratechart/data/InterestRateChartSlabDataValidator.java`** -> AI Confidence: **99.24%**
276. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanAccountDomainServiceJpa.java`** -> AI Confidence: **99.24%**
277. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/guarantor/domain/Guarantor.java`** -> AI Confidence: **99.24%**
278. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/guarantor/service/GuarantorWritePlatformServiceJpaRepositoryIImpl.java`** -> AI Confidence: **99.24%**
279. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/jobs/applychargetooverdueloaninstallment/ApplyChargeToOverdueLoanInstallmentTasklet.java`** -> AI Confidence: **99.24%**
280. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/jobs/recalculateinterestforloan/RecalculateInterestForLoanTasklet.java`** -> AI Confidence: **99.24%**
281. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanDisbursementValidator.java`** -> AI Confidence: **99.24%**
282. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanApplicationWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
283. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanChargeWritePlatformServiceImpl.java`** -> AI Confidence: **99.24%**
284. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanProductFloatingRatesUpdateUtil.java`** -> AI Confidence: **99.24%**
285. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanReadPlatformServiceImpl.java`** -> AI Confidence: **99.24%**
286. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/util/BuyDownFeeAmortizationUtil.java`** -> AI Confidence: **99.24%**
287. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/util/CapitalizedIncomeAmortizationUtil.java`** -> AI Confidence: **99.24%**
288. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/meeting/service/MeetingWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
289. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/note/service/NoteWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
290. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/data/DepositAccountDataValidator.java`** -> AI Confidence: **99.24%**
291. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/data/DepositProductDataValidator.java`** -> AI Confidence: **99.24%**
292. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/domain/FixedDepositAccount.java`** -> AI Confidence: **99.24%**
293. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/domain/SavingsAccountAssembler.java`** -> AI Confidence: **99.24%**
294. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/jobs/applyannualfeeforsavings/ApplyAnnualFeeForSavingsTasklet.java`** -> AI Confidence: **99.24%**
295. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/jobs/generateadhocclientschhedule/GenerateAdhocClientScheduleTasklet.java`** -> AI Confidence: **99.24%**
296. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/jobs/payduesavingscharges/PayDueSavingsChargesTasklet.java`** -> AI Confidence: **99.24%**
297. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/jobs/postinterestforsavings/PostInterestForSavingTasklet.java`** -> AI Confidence: **99.24%**
298. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/jobs/updatedepositsaccountmaturitydetails/UpdateDepositsAccountMaturityDetailsTasklet.java`** -> AI Confidence: **99.24%**
299. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/SavingsApplicationProcessWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
300. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/search/SavingsAccountTransactionsSearchServiceImpl.java`** -> AI Confidence: **99.24%**
301. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/domain/ShareAccount.java`** -> AI Confidence: **99.24%**
302. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/jobs/postdividentsforshares/PostDividentsForSharesTasklet.java`** -> AI Confidence: **99.24%**
303. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/service/ShareAccountWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
304. **`fineract-provider/src/main/java/org/apache/fineract/useradministration/service/UserDataValidator.java`** -> AI Confidence: **99.24%**
305. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/core/config/ApiVerificationTest.java`** -> AI Confidence: **99.24%**
306. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/dataqueries/service/DatatableUtilTest.java`** -> AI Confidence: **99.24%**
307. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/sqlbuilder/SqlBuilderStepDefinitions.java`** -> AI Confidence: **99.24%**
308. **`fineract-provider/src/test/java/org/apache/fineract/portfolio/loanaccount/service/LoanChargeWritePlatformServiceImplTest.java`** -> AI Confidence: **99.24%**
309. **`fineract-provider/src/test/java/org/apache/fineract/portfolio/loanaccount/service/reaging/LoanReAgingValidatorTest.java`** -> AI Confidence: **99.24%**
310. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/interestratechart/domain/InterestRateChart.java`** -> AI Confidence: **99.24%**
311. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/data/SavingsAccountDataValidator.java`** -> AI Confidence: **99.24%**
312. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/data/SavingsProductDataValidator.java`** -> AI Confidence: **99.24%**
313. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain/DepositProductAssembler.java`** -> AI Confidence: **99.24%**
314. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain/SavingsAccountTransactionRepository.java`** -> AI Confidence: **99.24%**
315. **`fineract-tax/src/main/java/org/apache/fineract/portfolio/tax/service/TaxUtils.java`** -> AI Confidence: **99.24%**
316. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/CreditBureauTest.java`** -> AI Confidence: **99.24%**
317. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/SmsApiResourceIntegrationTest.java`** -> AI Confidence: **99.24%**
318. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/SurveyIntegrationTest.java`** -> AI Confidence: **99.24%**
319. **`twofactor-tests/src/test/java/org/apache/fineract/twofactortests/TwoFactorAuthenticationTest.java`** -> AI Confidence: **99.24%**
320. **`fineract-core/src/main/java/org/apache/fineract/portfolio/savings/domain/interest/SavingsAccountTransactionDetailsForPostingPeriod.java`** -> AI Confidence: **99.23%**
321. **`fineract-core/src/main/java/org/apache/fineract/util/StreamUtil.java`** -> AI Confidence: **99.23%**
322. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/FixedDepositProductSheetPopulator.java`** -> AI Confidence: **99.23%**
323. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/configuration/service/ExternalServicesReadPlatformServiceImpl.java`** -> AI Confidence: **99.23%**
324. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/gcm/domain/Message.java`** -> AI Confidence: **99.23%**
325. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/client/feign/helpers/FeignAccountHelper.java`** -> AI Confidence: **99.23%**
326. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/common/externalevents/LoanAdjustTransactionBusinessEvent.java`** -> AI Confidence: **99.23%**
327. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/interestratechart/incentive/ClientAttributeIncentiveCalculation.java`** -> AI Confidence: **99.22%**
328. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/financialactivityaccount/service/FinancialActivityAccountWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
329. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/journalentry/JournalEntryMapper.java`** -> AI Confidence: **99.18%**
330. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/serialization/ProductToGLAccountMappingFromApiJsonDeserializer.java`** -> AI Confidence: **99.18%**
331. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/provisioning/service/ProvisioningEntriesReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
332. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/rule/api/AccountingRuleApiResource.java`** -> AI Confidence: **99.18%**
333. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/rule/service/AccountingRuleReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
334. **`fineract-branch/src/main/java/org/apache/fineract/organisation/teller/api/TellerApiResourceSwagger.java`** -> AI Confidence: **99.18%**
335. **`fineract-charge/src/main/java/org/apache/fineract/portfolio/charge/service/ChargeDropdownReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
336. **`fineract-client-feign/src/main/java/org/apache/fineract/client/feign/FineractFeignClientConfig.java`** -> AI Confidence: **99.18%**
337. **`fineract-client-feign/src/test/java/org/apache/fineract/client/feign/integration/EncoderDecoderIntegrationTest.java`** -> AI Confidence: **99.18%**
338. **`fineract-client-feign/src/test/java/org/apache/fineract/client/services/DocumentsApiFixedIntegrationTest.java`** -> AI Confidence: **99.18%**
339. **`fineract-cob/src/main/java/org/apache/fineract/cob/COBBusinessStepServiceImpl.java`** -> AI Confidence: **99.18%**
340. **`fineract-cob/src/main/java/org/apache/fineract/cob/listener/COBExecutionListenerRunner.java`** -> AI Confidence: **99.18%**
341. **`fineract-cob/src/main/java/org/apache/fineract/cob/service/ConfigJobParameterServiceImpl.java`** -> AI Confidence: **99.18%**
342. **`fineract-command/src/main/java/org/apache/fineract/command/implementation/AsynchronousCommandExecutor.java`** -> AI Confidence: **99.18%**
343. **`fineract-command/src/main/java/org/apache/fineract/command/implementation/BaseCommandPipeline.java`** -> AI Confidence: **99.18%**
344. **`fineract-command/src/main/java/org/apache/fineract/command/persistence/mapping/CommandJsonMapper.java`** -> AI Confidence: **99.18%**
345. **`fineract-core/src/main/java/org/apache/fineract/commands/provider/CommandHandlerProvider.java`** -> AI Confidence: **99.18%**
346. **`fineract-core/src/main/java/org/apache/fineract/commands/service/CommandSourceService.java`** -> AI Confidence: **99.18%**
347. **`fineract-core/src/main/java/org/apache/fineract/commands/service/CommandWrapperBuilder.java`** -> AI Confidence: **99.18%**
348. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/businessdate/service/BusinessDateReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
349. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/cache/api/CacheApiResource.java`** -> AI Confidence: **99.18%**
350. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/api/JsonQuery.java`** -> AI Confidence: **99.18%**
351. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/exceptionmapper/IdempotentCommandExceptionMapper.java`** -> AI Confidence: **99.18%**
352. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/filters/CorrelationHeaderFilter.java`** -> AI Confidence: **99.18%**
353. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/filters/IdempotencyStoreFilter.java`** -> AI Confidence: **99.18%**
354. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/database/PostgreSQLQueryService.java`** -> AI Confidence: **99.18%**
355. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/event/external/service/ExternalEventConfigurationValidationService.java`** -> AI Confidence: **99.18%**
356. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/event/external/service/ExternalEventService.java`** -> AI Confidence: **99.18%**
357. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/event/external/service/InternalExternalEventService.java`** -> AI Confidence: **99.18%**
358. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/jobs/TenantAwareEqualsHashCodeAdvice.java`** -> AI Confidence: **99.18%**
359. **`fineract-core/src/main/java/org/apache/fineract/portfolio/calendar/data/CalendarHistoryDataWrapper.java`** -> AI Confidence: **99.18%**
360. **`fineract-core/src/main/java/org/apache/fineract/portfolio/calendar/service/CalendarEnumerations.java`** -> AI Confidence: **99.18%**
361. **`fineract-core/src/main/java/org/apache/fineract/portfolio/client/domain/Client.java`** -> AI Confidence: **99.18%**
362. **`fineract-core/src/main/java/org/apache/fineract/portfolio/paymenttype/service/PaymentTypeWriteServiceImpl.java`** -> AI Confidence: **99.18%**
363. **`fineract-core/src/main/java/org/apache/fineract/portfolio/savings/data/SavingsAccountTransactionData.java`** -> AI Confidence: **99.18%**
364. **`fineract-core/src/main/java/org/apache/fineract/useradministration/domain/AppUserClientMapping.java`** -> AI Confidence: **99.18%**
365. **`fineract-core/src/test/java/org/apache/fineract/batch/service/BatchApiServiceImplTest.java`** -> AI Confidence: **99.18%**
366. **`fineract-document/src/main/java/org/apache/fineract/infrastructure/contentstore/detector/TikaContentDetector.java`** -> AI Confidence: **99.18%**
367. **`fineract-document/src/main/java/org/apache/fineract/infrastructure/contentstore/processor/DataUrlDecoderContentProcessor.java`** -> AI Confidence: **99.18%**
368. **`fineract-document/src/main/java/org/apache/fineract/infrastructure/documentmanagement/api/DocumentApiResource.java`** -> AI Confidence: **99.18%**
369. **`fineract-document/src/main/java/org/apache/fineract/infrastructure/documentmanagement/service/DocumentWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
370. **`fineract-document/src/main/java/org/apache/fineract/infrastructure/documentmanagement/service/ImageWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
371. **`fineract-document/src/test/java/org/apache/fineract/infrastructure/documentmanagement/service/ImageWritePlatformServiceImplTest.java`** -> AI Confidence: **99.18%**
372. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/common/BusinessDateStepDef.java`** -> AI Confidence: **99.18%**
373. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/common/GlobalConfigurationStepDef.java`** -> AI Confidence: **99.18%**
374. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/hook/MessagingHook.java`** -> AI Confidence: **99.18%**
375. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanChargeBackStepDef.java`** -> AI Confidence: **99.18%**
376. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanChargeStepDef.java`** -> AI Confidence: **99.18%**
377. **`fineract-e2e-tests-runner/src/test/java/org/apache/fineract/test/initializer/global/ChargeGlobalInitializerStep.java`** -> AI Confidence: **99.18%**
378. **`fineract-e2e-tests-runner/src/test/java/org/apache/fineract/test/initializer/global/WorkingCapitalLoanProductInitializerStep.java`** -> AI Confidence: **99.18%**
379. **`fineract-e2e-tests-runner/src/test/java/org/apache/fineract/test/initializer/suite/ExternalEventSuiteInitializerStep.java`** -> AI Confidence: **99.18%**
380. **`fineract-investor/src/main/java/org/apache/fineract/investor/cob/loan/LoanAccountOwnerTransferBusinessStep.java`** -> AI Confidence: **99.18%**
381. **`fineract-investor/src/main/java/org/apache/fineract/investor/service/search/mapper/ExternalAssetOwnerSearchDataMapper.java`** -> AI Confidence: **99.18%**
382. **`fineract-investor/src/main/java/org/apache/fineract/investor/service/serialization/serializer/investor/InvestorBusinessEventSerializer.java`** -> AI Confidence: **99.18%**
383. **`fineract-investor/src/test/java/org/apache/fineract/investor/service/ExternalAssetOwnerLoanProductAttributesWriteServiceImplTest.java`** -> AI Confidence: **99.18%**
384. **`fineract-investor/src/test/java/org/apache/fineract/investor/service/LoanAccountOwnerTransferServiceTest.java`** -> AI Confidence: **99.18%**
385. **`fineract-investor/src/test/java/org/apache/fineract/investor/service/LoanTransferabilityServiceImplTest.java`** -> AI Confidence: **99.18%**
386. **`fineract-loan-origination/src/main/java/org/apache/fineract/portfolio/loanorigination/enricher/LoanAccountDataV1OriginatorEnricher.java`** -> AI Confidence: **99.18%**
387. **`fineract-loan-origination/src/main/java/org/apache/fineract/portfolio/loanorigination/enricher/LoanTransactionDataV1OriginatorEnricher.java`** -> AI Confidence: **99.18%**
388. **`fineract-loan-origination/src/main/java/org/apache/fineract/portfolio/loanorigination/service/LoanOriginatorLinkingServiceImpl.java`** -> AI Confidence: **99.18%**
389. **`fineract-loan-origination/src/main/java/org/apache/fineract/portfolio/loanorigination/service/LoanOriginatorWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
390. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/delinquency/domain/LoanDelinquencyActionRepository.java`** -> AI Confidence: **99.18%**
391. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/delinquency/domain/LoanInstallmentDelinquencyTagRepository.java`** -> AI Confidence: **99.18%**
392. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/delinquency/helper/InstallmentDelinquencyAggregator.java`** -> AI Confidence: **99.18%**
393. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/delinquency/service/DelinquencyWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
394. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/interestpauses/handler/CreateInterestPauseCommandHandler.java`** -> AI Confidence: **99.18%**
395. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/interestpauses/handler/DeleteInterestPauseCommandHandler.java`** -> AI Confidence: **99.18%**
396. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/interestpauses/handler/UpdateInterestPauseCommandHandler.java`** -> AI Confidence: **99.18%**
397. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/interestpauses/service/InterestPauseWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
398. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/api/LoanScheduleApiResource.java`** -> AI Confidence: **99.18%**
399. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/data/DisbursementData.java`** -> AI Confidence: **99.18%**
400. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/data/LoanAccountData.java`** -> AI Confidence: **99.18%**
401. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanChargeRepository.java`** -> AI Confidence: **99.18%**
402. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanInstallmentCharge.java`** -> AI Confidence: **99.18%**
403. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanTransaction.java`** -> AI Confidence: **99.18%**
404. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/guarantor/command/GuarantorCommand.java`** -> AI Confidence: **99.18%**
405. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/jobs/setloandelinquencytags/SetLoanDelinquencyTagsTasklet.java`** -> AI Confidence: **99.18%**
406. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/data/LoanScheduleParams.java`** -> AI Confidence: **99.18%**
407. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/mapper/LoanTermVariationsMapper.java`** -> AI Confidence: **99.18%**
408. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/rescheduleloan/service/LoanRescheduleRequestReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
409. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanApplicationTransitionValidator.java`** -> AI Confidence: **99.18%**
410. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanChargeValidator.java`** -> AI Confidence: **99.18%**
411. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/VariableLoanScheduleFromApiJsonValidator.java`** -> AI Confidence: **99.18%**
412. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanArrearsAgingServiceImpl.java`** -> AI Confidence: **99.18%**
413. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanStatusChangeHistoryListener.java`** -> AI Confidence: **99.18%**
414. **`fineract-mix/src/main/java/org/apache/fineract/mix/service/MixTaxonomyReadServiceImpl.java`** -> AI Confidence: **99.18%**
415. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/api/LoanBuyDownFeeApiResource.java`** -> AI Confidence: **99.18%**
416. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/impl/ProgressiveTransactionCtx.java`** -> AI Confidence: **99.18%**
417. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/data/LoanSchedulePlan.java`** -> AI Confidence: **99.18%**
418. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/mapper/LoanConfigurationDetailsMapper.java`** -> AI Confidence: **99.18%**
419. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/repository/CustomizedLoanCapitalizedIncomeBalanceRepositoryImpl.java`** -> AI Confidence: **99.18%**
420. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/BuyDownFeeReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
421. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/CapitalizedIncomeBalanceReadServiceImpl.java`** -> AI Confidence: **99.18%**
422. **`fineract-provider/src/main/java/org/apache/fineract/accounting/common/AccountingDropdownReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
423. **`fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/api/JournalEntriesApiResource.java`** -> AI Confidence: **99.18%**
424. **`fineract-provider/src/main/java/org/apache/fineract/adhocquery/service/AdHocDataValidator.java`** -> AI Confidence: **99.18%**
425. **`fineract-provider/src/main/java/org/apache/fineract/adhocquery/service/AdHocWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
426. **`fineract-provider/src/main/java/org/apache/fineract/batch/command/internal/AdjustChargeByChargeExternalIdCommandStrategy.java`** -> AI Confidence: **99.18%**
427. **`fineract-provider/src/main/java/org/apache/fineract/batch/command/internal/AdjustChargeCommandStrategy.java`** -> AI Confidence: **99.18%**
428. **`fineract-provider/src/main/java/org/apache/fineract/batch/command/internal/GetChargeByChargeExternalIdCommandStrategy.java`** -> AI Confidence: **99.18%**
429. **`fineract-provider/src/main/java/org/apache/fineract/batch/command/internal/GetChargeByIdCommandStrategy.java`** -> AI Confidence: **99.18%**
430. **`fineract-provider/src/main/java/org/apache/fineract/batch/command/internal/GetLoanTransactionByExternalIdCommandStrategy.java`** -> AI Confidence: **99.18%**
431. **`fineract-provider/src/main/java/org/apache/fineract/batch/command/internal/GetLoanTransactionByIdCommandStrategy.java`** -> AI Confidence: **99.18%**
432. **`fineract-provider/src/main/java/org/apache/fineract/batch/command/internal/GetSavingsAccountByIdCommandStrategy.java`** -> AI Confidence: **99.18%**
433. **`fineract-provider/src/main/java/org/apache/fineract/cob/api/LoanCOBCatchUpApiResource.java`** -> AI Confidence: **99.18%**
434. **`fineract-provider/src/main/java/org/apache/fineract/cob/loan/AbstractLoanItemWriter.java`** -> AI Confidence: **99.18%**
435. **`fineract-provider/src/main/java/org/apache/fineract/cob/loan/AddPeriodicAccrualEntriesBusinessStep.java`** -> AI Confidence: **99.18%**
436. **`fineract-provider/src/main/java/org/apache/fineract/cob/loan/CheckLoanRepaymentDueBusinessStep.java`** -> AI Confidence: **99.18%**
437. **`fineract-provider/src/main/java/org/apache/fineract/cob/loan/RetrieveAllNonClosedLoanIdServiceImpl.java`** -> AI Confidence: **99.18%**
438. **`fineract-provider/src/main/java/org/apache/fineract/cob/savings/RetrieveSavingsIdServiceImpl.java`** -> AI Confidence: **99.18%**
439. **`fineract-provider/src/main/java/org/apache/fineract/cob/service/InlineLoanCOBExecutorServiceImpl.java`** -> AI Confidence: **99.18%**
440. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/accountnumberformat/api/AccountNumberFormatsApiResource.java`** -> AI Confidence: **99.18%**
441. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/accountnumberformat/service/AccountNumberFormatWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
442. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/center/CenterImportHandler.java`** -> AI Confidence: **99.18%**
443. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/chartofaccounts/ChartOfAccountsImportHandler.java`** -> AI Confidence: **99.18%**
444. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/guarantor/GuarantorImportHandler.java`** -> AI Confidence: **99.18%**
445. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/recurringdeposit/RecurringDepositTransactionImportHandler.java`** -> AI Confidence: **99.18%**
446. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/users/UserImportHandler.java`** -> AI Confidence: **99.18%**
447. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/centers/CentersWorkbookPopulator.java`** -> AI Confidence: **99.18%**
448. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/fixeddeposits/FixedDepositWorkbookPopulator.java`** -> AI Confidence: **99.18%**
449. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/loan/LoanWorkbookPopulator.java`** -> AI Confidence: **99.18%**
450. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/recurringdeposit/RecurringDepositWorkbookPopulator.java`** -> AI Confidence: **99.18%**
451. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/savings/SavingsWorkbookPopulator.java`** -> AI Confidence: **99.18%**
452. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/service/BulkImportWorkbookPopulatorServiceImpl.java`** -> AI Confidence: **99.18%**
453. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/email/data/EmailConfigurationValidator.java`** -> AI Confidence: **99.18%**
454. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/email/service/EmailCampaignDomainServiceImpl.java`** -> AI Confidence: **99.18%**
455. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/email/service/EmailMessageJobEmailServiceImpl.java`** -> AI Confidence: **99.18%**
456. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/email/service/EmailReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
457. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/email/service/EmailWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
458. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/sms/service/SmsCampaignReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
459. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/codes/serialization/CodeValueCommandFromApiJsonDeserializer.java`** -> AI Confidence: **99.18%**
460. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/codes/service/CodeValueWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
461. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/codes/service/CodeWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
462. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/configuration/api/GlobalConfigurationApiResource.java`** -> AI Confidence: **99.18%**
463. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/configuration/serialization/ExternalServicesPropertiesCommandFromApiJsonDeserializer.java`** -> AI Confidence: **99.18%**
464. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/configuration/service/GlobalConfigurationPropertyUpdateService.java`** -> AI Confidence: **99.18%**
465. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/config/SpringConfig.java`** -> AI Confidence: **99.18%**
466. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/diagnostics/performance/sampling/output/SamplingScheduler.java`** -> AI Confidence: **99.18%**
467. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/diagnostics/security/SecurityFilterChainDiagnostics.java`** -> AI Confidence: **99.18%**
468. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/domain/AuditorAwareImpl.java`** -> AI Confidence: **99.18%**
469. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/jersey/JerseyJacksonConverterConfig.java`** -> AI Confidence: **99.18%**
470. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/jersey/serializer/JacksonLocalDateBeanSerializerModifier.java`** -> AI Confidence: **99.18%**
471. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/service/GmailBackedPlatformEmailService.java`** -> AI Confidence: **99.18%**
472. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/service/migration/TenantDatabaseStateVerifier.java`** -> AI Confidence: **99.18%**
473. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/creditbureau/service/CreditReportWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
474. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/creditbureau/service/ThitsaWorksCreditBureauIntegrationWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
475. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/service/DatatableReadServiceImpl.java`** -> AI Confidence: **99.18%**
476. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/entityaccess/service/FineractEntityAccessUtil.java`** -> AI Confidence: **99.18%**
477. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/hooks/processor/ElasticSearchHookProcessor.java`** -> AI Confidence: **99.18%**
478. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/hooks/processor/WebHookProcessor.java`** -> AI Confidence: **99.18%**
479. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/jobs/api/SchedulerApiResource.java`** -> AI Confidence: **99.18%**
480. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/jobs/config/FineractDataFieldMaxValueIncrementerFactory.java`** -> AI Confidence: **99.18%**
481. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/jobs/filter/LoanCOBApiFilter.java`** -> AI Confidence: **99.18%**
482. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/jobs/service/JobSchedulerServiceImpl.java`** -> AI Confidence: **99.18%**
483. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/jobs/service/JobStarter.java`** -> AI Confidence: **99.18%**
484. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/jobs/service/StuckJobListener.java`** -> AI Confidence: **99.18%**
485. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/jobs/service/aggregationjob/JournalEntryAggregationJobExecutionDecider.java`** -> AI Confidence: **99.18%**
486. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/reportmailingjob/service/ReportMailingJobWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
487. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/security/service/TwoFactorServiceImpl.java`** -> AI Confidence: **99.18%**
488. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/sms/service/SmsWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
489. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/springbatch/InputChannelInterceptor.java`** -> AI Confidence: **99.18%**
490. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/springbatch/messagehandler/StepExecutionRequestHandler.java`** -> AI Confidence: **99.18%**
491. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/survey/service/ReadSurveyServiceImpl.java`** -> AI Confidence: **99.18%**
492. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/survey/service/WriteLikelihoodServiceImpl.java`** -> AI Confidence: **99.18%**
493. **`fineract-provider/src/main/java/org/apache/fineract/interoperation/data/InteropTransactionData.java`** -> AI Confidence: **99.18%**
494. **`fineract-provider/src/main/java/org/apache/fineract/interoperation/data/InteropTransactionsData.java`** -> AI Confidence: **99.18%**
495. **`fineract-provider/src/main/java/org/apache/fineract/interoperation/data/MoneyData.java`** -> AI Confidence: **99.18%**
496. **`fineract-provider/src/main/java/org/apache/fineract/interoperation/service/InteropServiceImpl.java`** -> AI Confidence: **99.18%**
497. **`fineract-provider/src/main/java/org/apache/fineract/notification/service/NotificationReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
498. **`fineract-provider/src/main/java/org/apache/fineract/organisation/holiday/service/HolidayReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
499. **`fineract-provider/src/main/java/org/apache/fineract/organisation/holiday/service/HolidayWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
500. **`fineract-provider/src/main/java/org/apache/fineract/organisation/office/serialization/OfficeCommandFromApiJsonDeserializer.java`** -> AI Confidence: **99.18%**
501. **`fineract-provider/src/main/java/org/apache/fineract/organisation/office/service/OfficeReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
502. **`fineract-provider/src/main/java/org/apache/fineract/organisation/office/service/OfficeWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
503. **`fineract-provider/src/main/java/org/apache/fineract/organisation/provisioning/domain/ProvisioningCriteria.java`** -> AI Confidence: **99.18%**
504. **`fineract-provider/src/main/java/org/apache/fineract/organisation/provisioning/serialization/ProvisioningCriteriaDefinitionJsonDeserializer.java`** -> AI Confidence: **99.18%**
505. **`fineract-provider/src/main/java/org/apache/fineract/organisation/provisioning/service/ProvisioningCategoryWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
506. **`fineract-provider/src/main/java/org/apache/fineract/organisation/provisioning/service/ProvisioningCriteriaAssembler.java`** -> AI Confidence: **99.18%**
507. **`fineract-provider/src/main/java/org/apache/fineract/organisation/provisioning/service/ProvisioningCriteriaWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
508. **`fineract-provider/src/main/java/org/apache/fineract/organisation/staff/service/StaffWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
509. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/account/api/StandingInstructionApiResource.java`** -> AI Confidence: **99.18%**
510. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/accountdetails/service/AccountDetailsReadPlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
511. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/address/domain/Address.java`** -> AI Confidence: **99.18%**
512. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/address/service/AddressReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
513. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/calendar/domain/CalendarInstanceRepository.java`** -> AI Confidence: **99.18%**
514. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/charge/service/ChargeReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
515. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/api/ClientChargesApiResource.java`** -> AI Confidence: **99.18%**
516. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/api/ClientIdentifiersApiResource.java`** -> AI Confidence: **99.18%**
517. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/api/ClientTransactionsApiResource.java`** -> AI Confidence: **99.18%**
518. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/domain/ClientCharge.java`** -> AI Confidence: **99.18%**
519. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/service/ClientChargeReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
520. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/service/ClientChargeWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
521. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/service/ClientIdentifierWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
522. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/service/ClientTransactionReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
523. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/service/ClientTransactionWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
524. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/collateral/service/CollateralAssembler.java`** -> AI Confidence: **99.18%**
525. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/collateralmanagement/service/ClientCollateralManagementWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
526. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/collateralmanagement/service/LoanCollateralAssembler.java`** -> AI Confidence: **99.18%**
527. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/collectionsheet/data/CollectionSheetTransactionDataValidator.java`** -> AI Confidence: **99.18%**
528. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/collectionsheet/service/CollectionSheetReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
529. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/fund/service/FundWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
530. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/group/service/CenterReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
531. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/group/service/GroupReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
532. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/group/service/GroupRolesWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
533. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/interestratechart/data/InterestRateChartDataValidator.java`** -> AI Confidence: **99.18%**
534. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/api/LoansApiResource.java`** -> AI Confidence: **99.18%**
535. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/api/request/ReAgePreviewRequest.java`** -> AI Confidence: **99.18%**
536. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/guarantor/domain/GuarantorFundingDetails.java`** -> AI Confidence: **99.18%**
537. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/guarantor/service/GuarantorReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
538. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/jobs/addperiodicaccrualentriesforloanswithincomepostedastransactions/AddPeriodicAccrualEntriesForLoansTasklet.java`** -> AI Confidence: **99.18%**
539. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/jobs/applyholidaystoloans/ApplyHolidaysToLoansTasklet.java`** -> AI Confidence: **99.18%**
540. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/jobs/generateloanlossprovisioning/GenerateLoanlossProvisioningTasklet.java`** -> AI Confidence: **99.18%**
541. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/service/LoanScheduleHistoryReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
542. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/rescheduleloan/service/LoanReschedulePreviewPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
543. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanScheduleValidator.java`** -> AI Confidence: **99.18%**
544. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanAccountServiceImpl.java`** -> AI Confidence: **99.18%**
545. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanBuyDownFeeAmortizationEventService.java`** -> AI Confidence: **99.18%**
546. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanPointInTimeServiceImpl.java`** -> AI Confidence: **99.18%**
547. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanProductGuaranteeDetailsUpdateUtil.java`** -> AI Confidence: **99.18%**
548. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanProductInterestRecalculationDetailsAssembler.java`** -> AI Confidence: **99.18%**
549. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanProductVariableInstallmentConfigUpdateUtil.java`** -> AI Confidence: **99.18%**
550. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
551. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/reaging/LoanReAgingService.java`** -> AI Confidence: **99.18%**
552. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/reaging/LoanReAgingValidator.java`** -> AI Confidence: **99.18%**
553. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/api/LoanProductsApiResource.java`** -> AI Confidence: **99.18%**
554. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/productmix/service/ProductMixWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
555. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/service/LoanProductReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
556. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/meeting/service/MeetingReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
557. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/rate/service/RateAssembler.java`** -> AI Confidence: **99.18%**
558. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/rate/service/RateWriteServiceImpl.java`** -> AI Confidence: **99.18%**
559. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/repaymentwithpostdatedchecks/service/RepaymentWithPostDatedChecksWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
560. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/api/SavingsAccountTransactionsApiResource.java`** -> AI Confidence: **99.18%**
561. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/api/SavingsProductsApiResource.java`** -> AI Confidence: **99.18%**
562. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/domain/SavingsAccountDomainServiceJpa.java`** -> AI Confidence: **99.18%**
563. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/jobs/transferinteresttosavings/TransferInterestToSavingsTasklet.java`** -> AI Confidence: **99.18%**
564. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/DepositAccountOnHoldTransactionReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
565. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/DepositAccountWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
566. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/FixedDepositProductWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
567. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/RecurringDepositProductWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
568. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/SavingsAccountTemplateReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
569. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/SavingsProductWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
570. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/self/account/data/SelfAccountTransferDataValidator.java`** -> AI Confidence: **99.18%**
571. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/self/account/service/SelfBeneficiariesTPTWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
572. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/self/client/data/SelfClientDataValidator.java`** -> AI Confidence: **99.18%**
573. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/self/device/service/DeviceRegistrationWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
574. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/self/loanaccount/data/SelfLoansDataValidator.java`** -> AI Confidence: **99.18%**
575. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/domain/ShareAccountCharge.java`** -> AI Confidence: **99.18%**
576. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/service/ShareAccountCommandsServiceImpl.java`** -> AI Confidence: **99.18%**
577. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/service/ShareAccountDividendReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
578. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/service/ShareAccountReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
579. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareproducts/service/ShareProductWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
580. **`fineract-provider/src/main/java/org/apache/fineract/spm/util/LookupTableMapper.java`** -> AI Confidence: **99.18%**
581. **`fineract-provider/src/main/java/org/apache/fineract/template/api/TemplatesApiResource.java`** -> AI Confidence: **99.18%**
582. **`fineract-provider/src/main/java/org/apache/fineract/template/domain/Template.java`** -> AI Confidence: **99.18%**
583. **`fineract-provider/src/main/java/org/apache/fineract/template/service/JpaTemplateDomainService.java`** -> AI Confidence: **99.18%**
584. **`fineract-provider/src/main/java/org/apache/fineract/useradministration/api/PermissionsApiResource.java`** -> AI Confidence: **99.18%**
585. **`fineract-provider/src/main/java/org/apache/fineract/useradministration/api/RolesApiResource.java`** -> AI Confidence: **99.18%**
586. **`fineract-provider/src/main/java/org/apache/fineract/useradministration/service/PermissionWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
587. **`fineract-provider/src/main/java/org/apache/fineract/useradministration/service/RoleWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
588. **`fineract-provider/src/test/java/org/apache/fineract/batch/command/CommandStrategyProviderTest.java`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `buildSrc/src/main/groovy/org/apache/fineract/gradle/FineractPlugin.groovy` -> **100.0%** Exposure
- `custom/acme/loan/processor/src/main/java/com/acme/fineract/loan/processor/AcmeLoanRepaymentScheduleTransactionProcessor.java` -> **100.0%** Exposure
- `custom/acme/loan/starter/src/test/java/com/acme/fineract/loan/starter/TestDefaultConfiguration.java` -> **100.0%** Exposure
- `fineract-accounting/src/main/java/org/apache/fineract/accounting/accrual/api/AccrualAccountingApiResource.java` -> **100.0%** Exposure
- `fineract-accounting/src/main/java/org/apache/fineract/accounting/closure/api/GLClosuresApiResource.java` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `fineract-accounting/src/main/java/org/apache/fineract/accounting/provisioning/service/ProvisioningEntriesReadPlatformServiceImpl.java` -> **100.0%** Exposure
- `fineract-accounting/src/main/java/org/apache/fineract/accounting/rule/service/AccountingRuleReadPlatformServiceImpl.java` -> **100.0%** Exposure
- `fineract-command/src/main/java/org/apache/fineract/command/implementation/DisruptorCommandExecutor.java` -> **100.0%** Exposure
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/PaginationHelper.java` -> **100.0%** Exposure
- `fineract-core/src/main/java/org/apache/fineract/organisation/monetary/service/CurrencyReadPlatformServiceImpl.java` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `buildSrc/src/main/groovy/org/apache/fineract/gradle/FineractPlugin.groovy` -> **100.0%** Exposure
- `buildSrc/src/main/groovy/org/apache/fineract/gradle/service/GpgService.groovy` -> **100.0%** Exposure
- `scripts/split-tests.sh` -> **100.0%** Exposure
- `fineract-accounting/src/main/java/org/apache/fineract/accounting/closure/service/GLClosureReadPlatformServiceImpl.java` -> **100.0%** Exposure
- `fineract-accounting/src/main/java/org/apache/fineract/accounting/financialactivityaccount/service/FinancialActivityAccountReadPlatformServiceImpl.java` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `16` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `64285` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `fineract-accounting/src/main/java/org/apache/fineract/accounting/provisioning/service/ProvisioningEntriesReadPlatformServiceImpl.java` (JAVA) -> Cumulative Risk: **932.29**
- **Archetype:** `file_cluster_13` (Distance: 11.293 IQR)
- **Magnitude:** 386.68 | **LOC:** 358 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `retrieveProvisioningEntries` (Impact: 63.6), `retrieveProvisioningEntryData` (Impact: 36.4), `LoanProductProvisioningEntryMapper` (Impact: 28.8)

### 2. `fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/service/ProductToGLAccountMappingReadPlatformServiceImpl.java` (JAVA) -> Cumulative Risk: **911.62**
- **Archetype:** `file_cluster_13` (Distance: 13.353 IQR)
- **Magnitude:** 1139.1 | **LOC:** 488 | **CtrlFlow:** 70.5% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `fetchAccountMappingDetailsForLoanProduct` (Impact: 328.2), `setAccrualPeriodicSavingsProductToGLAcco` (Impact: 114.5), `setCashSavingsProductToGLAccountMaps` (Impact: 86.2)

### 3. `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/ProgressiveLoanInterestRefundServiceImpl.java` (JAVA) -> Cumulative Risk: **902.08**
- **Archetype:** `file_cluster_13` (Distance: 12.254 IQR)
- **Magnitude:** 268.7 | **LOC:** 157 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `totalInterestByTransactions` (Impact: 103.6), `simulateRepaymentForDisbursements` (Impact: 50.4), `recalculateTotalInterest` (Impact: 40.0)

### 4. `fineract-provider/src/main/java/org/apache/fineract/infrastructure/configuration/service/ConfigurationReadPlatformServiceImpl.java` (JAVA) -> Cumulative Risk: **892.6**
- **Archetype:** `file_cluster_13` (Distance: 10.312 IQR)
- **Magnitude:** 87.56 | **LOC:** 116 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `retrieveGlobalConfiguration` (Impact: 31.5), `mapRow` (Impact: 16.3), `ConfigurationReadPlatformServiceImpl` (Impact: 4.4)

### 5. `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/InterestScheduleModelRepositoryWrapperImpl.java` (JAVA) -> Cumulative Risk: **888.21**
- **Archetype:** `file_cluster_13` (Distance: 12.185 IQR)
- **Magnitude:** 156.88 | **LOC:** 144 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getSavedModel` (Impact: 25.2), `extractModel` (Impact: 23.8), `readProgressiveLoanInterestScheduleModel` (Impact: 21.4)

### 6. `fineract-provider/src/main/java/org/apache/fineract/infrastructure/sms/scheduler/SmsMessageScheduledJobServiceImpl.java` (JAVA) -> Cumulative Risk: **886.91**
- **Archetype:** `file_cluster_13` (Distance: 10.619 IQR)
- **Magnitude:** 223.04 | **LOC:** 180 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `sendTriggeredMessages` (Impact: 111.4), `sendTriggeredMessage` (Impact: 31.2), `connectAndSendToIntermediateServer` (Impact: 28.8)

### 7. `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/api/jersey/PageableParamProvider.java` (JAVA) -> Cumulative Risk: **876.1**
- **Archetype:** `file_cluster_4` (Distance: 11.892 IQR)
- **Magnitude:** 272.44 | **LOC:** 108 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `PageableFunction` (Impact: 182.7), `getPriority` (Impact: 3.2)

### 8. `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepaymentScheduleInstallment.java` (JAVA) -> Cumulative Risk: **859.68**
- **Archetype:** `file_cluster_0` (Distance: 13.307 IQR)
- **Magnitude:** 1924.02 | **LOC:** 1303 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 30.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getPaymentFunction` (Impact: 198.1), `resetDerivedComponents` (Impact: 53.7), `reduceAdvanceAndLateTotalsForRepaymentPe` (Impact: 49.0)

### 9. `fineract-command/src/main/java/org/apache/fineract/command/implementation/DefaultCommandAuditor.java` (JAVA) -> Cumulative Risk: **846.69**
- **Archetype:** `file_cluster_13` (Distance: 11.034 IQR)
- **Magnitude:** 228.24 | **LOC:** 185 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `fallback` (Impact: 28.1), `onStartup` (Impact: 26.5), `setError` (Impact: 21.1)

### 10. `fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/sms/service/SmsCampaignDomainServiceImpl.java` (JAVA) -> Cumulative Risk: **834.14**
- **Archetype:** `file_cluster_13` (Distance: 11.344 IQR)
- **Magnitude:** 680.1 | **LOC:** 460 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9952%)
- **Heaviest Functions:** `sendSmsForLoanRepayment` (Impact: 199.1), `sendSmsForSavingsTransaction` (Impact: 124.1), `notifyRejectedLoanOwner` (Impact: 39.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepository.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.388 IQR)
- **Top Global Matches:** file_cluster_0: 10.388, file_cluster_16: 10.532, file_cluster_8: 10.651
- **Magnitude:** 7305.13 | **LOC:** 289 | **CtrlFlow:** 85.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (26.4695%), Tech Debt (15.3095%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 18`, `args: 47`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 36`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `import: 14`
* *Defense:* `safety: 3`, `doc: 2`, `test: 3`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.44
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` org.springframework.data.jpa.repository.Query, org.apache.fineract.accounting.common.AccountingRuleType, org.springframework.data.jpa.repository.JpaRepository, org.apache.fineract.portfolio.accountdetails.domain.AccountType, org.springframework.data.jpa.repository.JpaSpecificationExecutor, org.apache.fineract.cob.data.LoanDataForExternalTransfer, java.util.Optional, java.util.List...
  * `Imported By (In-Degree: 43):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanTransactionRepository.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.586 IQR)
- **Top Global Matches:** file_cluster_8: 9.586, file_cluster_0: 9.979, file_cluster_16: 10.158
- **Magnitude:** 5341.36 | **LOC:** 485 | **CtrlFlow:** 75.3% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.4403%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 23`, `args: 51`, `func_start: 62`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 1`, `import: 17`
* *Defense:* `safety: 7`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.324
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` org.springframework.data.jpa.repository.Query, org.apache.fineract.infrastructure.codes.domain.CodeValue, org.springframework.data.jpa.repository.JpaRepository, java.util.Set, org.springframework.data.jpa.repository.JpaSpecificationExecutor, java.util.Optional, java.util.List, org.apache.fineract.portfolio.loanaccount.data.CumulativeIncomeFromIncomePosting...
  * `Imported By (In-Degree: 57):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/AbstractCumulativeLoanScheduleGenerator.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.252 IQR)
- **Top Global Matches:** file_cluster_8: 12.252, file_cluster_13: 12.371, file_cluster_16: 12.446
- **Magnitude:** 5315.18 | **LOC:** 2861 | **CtrlFlow:** 74.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (43.7223%), Tech Debt (24.4831%)
**Top Internal Functions/Classes:**
  * `applyEarlyPaymentStrategy` (Impact: 1627.5 | O(N^6) | DB: 45)
  * `applyLoanTermVariations` (Impact: 461.5 | O(N^6) | DB: 20)
  * `generate` (Impact: 429.7 | O(N^6) | DB: 23)
  * `handleRecalculationForNonDueDateTransact` (Impact: 418.5 | O(N^6) | DB: 16)
  * `applyExceptionLoanTermVariations` (Impact: 290.7 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 498`, `structural_boundaries: 172`, `args: 73`, `func_start: 160`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 74`, `state_mutation: 344`, `dead_code: 7`, `planned_debt: 4`, `duplicate_logic: 4`, `orphaned_logic: 8`
* *Architecture:* `api: 9`, `import: 46`
* *Defense:* `safety: 2`, `doc: 44`, `immutability_locks: 312`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` org.apache.fineract.portfolio.loanaccount.domain.LoanTransaction, java.util.HashSet, java.math.MathContext, org.apache.fineract.portfolio.loanaccount.data.OutstandingAmountsDTO, java.util.ArrayList, org.apache.fineract.portfolio.loanaccount.loanschedule.data.LoanScheduleModelDownPaymentPeriod, org.apache.fineract.portfolio.loanaccount.loanschedule.exception.ScheduleDateException, java.math.BigDecimal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-provider/src/main/resources/keystore.jks` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-progressive-loan/src/test/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculatorTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.11 IQR)
- **Top Global Matches:** file_cluster_8: 12.11, file_cluster_0: 12.494, file_cluster_13: 12.612
- **Magnitude:** 4939.06 | **LOC:** 5294 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (13.1312%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_balance_correction_on0215_disbursed` (Impact: 60.7 | O(N^4) | DB: 6)
  * `test_emi_calculator_performance` (Impact: 57.5 | O(N^4) | DB: 12)
  * `test_two_reschedules_disbursedAmt100_day` (Impact: 57.1 | O(N^4))
  * `test_reschedule_disbursedAmt100_dayInYea` (Impact: 57.0 | O(N^4))
  * `test_reschedule_partial_period_disbursed` (Impact: 57.0 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 686`, `structural_boundaries: 278`, `args: 165`, `func_start: 1463`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 138`, `state_mutation: 182`, `duplicate_logic: 40`, `orphaned_logic: 78`
* *Architecture:* `api: 104`, `import: 49`
* *Defense:* `safety: 1`, `doc: 7`, `test: 878`, `immutability_locks: 594`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` org.apache.fineract.portfolio.loanaccount.domain.LoanTransaction, org.apache.fineract.portfolio.loanaccount.loanschedule.domain.DefaultScheduledDateGenerator, org.apache.fineract.portfolio.loanproduct.calc.data.OutstandingDetails, java.math.MathContext, org.junit.jupiter.api.Nested, java.util.ArrayList, lombok.extern.slf4j.Slf4j, java.math.BigDecimal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanStepDef.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.46 IQR)
- **Top Global Matches:** file_cluster_0: 13.46, file_cluster_8: 13.498, file_cluster_13: 13.501
- **Magnitude:** 4635.94 | **LOC:** 5999 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 18.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 55
- **Risk Profile:** Cognitive Load (23.1873%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fetchValuesOfRepaymentSchedule` (Impact: 305.0 | O(N^6) | DB: 15)
  * `fetchValuesOfTransaction` (Impact: 231.9 | O(N^6) | DB: 11)
  * `fetchValuesOfFilteredTransaction` (Impact: 167.3 | O(N^5) | DB: 9)
  * `fetchValuesOfLoanTermVariations` (Impact: 158.8 | O(N^6) | DB: 8)
  * `fetchValuesOfBuyDownFees` (Impact: 140.7 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 519`, `structural_boundaries: 672`, `args: 551`, `func_start: 572`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 228`, `state_mutation: 371`, `duplicate_logic: 31`, `orphaned_logic: 168`
* *Architecture:* `api: 223`, `import: 154`
* *Defense:* `safety: 46`, `doc: 2`, `test: 247`, `immutability_locks: 628`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 61):` org.apache.fineract.avro.loan.v1.LoanStatusEnumDataV1, org.apache.fineract.test.messaging.event.loan.transaction.LoanTransactionContractTerminationPostBusinessEvent, org.apache.fineract.client.models.LoanProductChargeData, org.apache.fineract.test.data.loanproduct.DefaultLoanProduct.LP2_ADV_PYMNT_ACCELERATE_MATURITY_CHARGE_OFF_BEHAVIOUR, org.apache.fineract.test.messaging.config.JobPollingProperties, lombok.extern.slf4j.Slf4j, org.junit.jupiter.api.Assertions.assertTrue, java.math.BigDecimal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/serialization/LoanProductDataValidator.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.342 IQR)
- **Top Global Matches:** file_cluster_8: 10.342, file_cluster_7: 10.906, file_cluster_13: 10.961
- **Magnitude:** 4489.62 | **LOC:** 3019 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (12.0154%), Tech Debt (16.8586%)
**Top Internal Functions/Classes:**
  * `validateForCreate` (Impact: 968.6 | O(N^6))
  * `validateForUpdate` (Impact: 817.2 | O(N^6))
  * `validateInterestRecalculationParams` (Impact: 353.5 | O(N^6))
  * `validatePartialPeriodSupport` (Impact: 246.6 | O(N^6))
  * `validateBorrowerCycleVariations` (Impact: 235.2 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 543`, `structural_boundaries: 146`, `args: 38`, `func_start: 89`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 178`, `state_mutation: 16`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 55`, `import: 60`
* *Defense:* `doc: 2`, `immutability_locks: 353`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.077
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 42):` org.apache.fineract.portfolio.loanproduct.domain.RecalculationFrequencyType, org.apache.fineract.portfolio.loanaccount.domain.LoanChargeOffBehaviour, java.util.HashSet, org.apache.commons.lang3.StringUtils, com.google.gson.JsonArray, java.util.ArrayList, java.util.Arrays, org.apache.fineract.portfolio.loanproduct.domain.LoanProductValueConditionType...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/LoanApplicationTerms.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.732 IQR)
- **Top Global Matches:** file_cluster_8: 10.732, file_cluster_13: 11.16, file_cluster_7: 11.213
- **Magnitude:** 4110.28 | **LOC:** 2272 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 30.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (16.4434%), Tech Debt (45.0817%)
**Top Internal Functions/Classes:**
  * `periodicInterestRate` (Impact: 914.3 | O(2^N))
  * `calculateTotalInterestForPeriod` (Impact: 297.2 | O(N^6))
  * `calculateTotalPrincipalForPeriod` (Impact: 181.5 | O(N^6))
  * `calculatePeriodsBetweenDates` (Impact: 143.0 | O(N^6) | DB: 6)
  * `calculatePeriodsInOneYear` (Impact: 129.9 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 341`, `structural_boundaries: 253`, `args: 194`, `func_start: 192`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 39`, `planned_debt: 6`, `duplicate_logic: 10`
* *Architecture:* `api: 241`, `import: 48`
* *Defense:* `safety: 1`, `doc: 10`, `immutability_locks: 351`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.313
  * `Choke Point (Betweenness):` 0.001205 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 39):` org.apache.fineract.portfolio.loanproduct.domain.RecalculationFrequencyType, org.apache.fineract.portfolio.loanproduct.domain.LoanProductRelatedDetail, org.apache.fineract.portfolio.loanaccount.data.LoanTermVariationsDataWrapper, org.apache.fineract.portfolio.loanaccount.domain.LoanChargeOffBehaviour, java.util.HashSet, java.math.MathContext, java.util.ArrayList, java.math.BigDecimal...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/AccrualBasedAccountingProcessorForLoan.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.903 IQR)
- **Top Global Matches:** file_cluster_8: 11.903, file_cluster_13: 12.266, file_cluster_7: 12.306
- **Magnitude:** 3952.76 | **LOC:** 2198 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (34.1683%), Tech Debt (38.5574%)
**Top Internal Functions/Classes:**
  * `createJournalEntriesForRepaymentWhenLoan` (Impact: 512.1 | O(N^6) | DB: 5)
  * `createJournalEntriesForLoan` (Impact: 305.3 | O(N^6))
  * `createJournalEntriesForLoanRepayments` (Impact: 305.2 | O(N^6) | DB: 21)
  * `createJournalEntriesForLoanCapitalizedIn` (Impact: 208.6 | O(N^6))
    * *Intent:* // create debit entries
  * `createJournalEntriesForLoanBuyDownFeeAmo` (Impact: 208.6 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 457`, `structural_boundaries: 108`, `args: 58`, `func_start: 153`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 295`, `planned_debt: 2`, `duplicate_logic: 9`
* *Architecture:* `api: 19`, `import: 24`
* *Defense:* `doc: 23`, `immutability_locks: 378`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` org.apache.fineract.accounting.journalentry.data.LoanDTO, org.apache.fineract.portfolio.PortfolioProductType, java.util.ArrayList, java.math.BigDecimal, java.util.LinkedHashMap, org.apache.fineract.accounting.producttoaccountmapping.domain.ProductToGLAccountMapping, org.apache.fineract.infrastructure.core.service.MathUtil, java.util.Objects...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `fineract-core/src/main/java/org/apache/fineract/portfolio/savings/service/SavingsEnumerations.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.86 IQR)
- **Top Global Matches:** file_cluster_8: 9.86, file_cluster_13: 10.255, file_cluster_7: 10.456
- **Magnitude:** 3814.08 | **LOC:** 841 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (33.2229%), Tech Debt (99.9996%)
**Top Internal Functions/Classes:**
  * `transactionType` (Impact: 578.6 | O(N^6))
  * `status` (Impact: 328.2 | O(N^6))
  * `subStatus` (Impact: 215.5 | O(N^6))
  * `compoundingInterestPeriodType` (Impact: 187.9 | O(N^6))
  * `interestPostingPeriodType` (Impact: 186.9 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 359`, `structural_boundaries: 179`, `args: 77`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`, `duplicate_logic: 43`
* *Architecture:* `api: 58`, `import: 21`
* *Defense:* `doc: 1`, `immutability_locks: 94`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.271
  * `Choke Point (Betweenness):` 0.000177 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` java.util.ArrayList, org.apache.fineract.portfolio.savings.DepositAccountOnClosureType, java.util.List, org.apache.fineract.portfolio.savings.DepositAccountOnHoldTransactionType, org.apache.fineract.infrastructure.core.data.EnumOptionData, org.apache.fineract.portfolio.savings.domain.SavingsAccountSubStatusEnum, org.apache.fineract.portfolio.savings.data.SavingsAccountTransactionEnumData, org.apache.fineract.accounting.common.AccountingEnumerations...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/service/DatatableWriteServiceImpl.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.48 IQR)
- **Top Global Matches:** file_cluster_13: 11.48, file_cluster_8: 11.704, file_cluster_0: 11.749
- **Magnitude:** 3167.82 | **LOC:** 1430 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (41.4169%), Tech Debt (51.9953%)
**Top Internal Functions/Classes:**
  * `parseDatatableColumnForUpdate` (Impact: 635.6 | O(N^6) | DB: 4)
  * `updateDatatable` (Impact: 325.4 | O(N^6) | DB: 1)
  * `updateDatatableEntry` (Impact: 270.6 | O(N^6) | DB: 6)
  * `createDatatable` (Impact: 219.8 | O(N^6) | DB: 2)
  * `parseDatatableColumnForAdd` (Impact: 180.2 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 347`, `structural_boundaries: 246`, `args: 74`, `func_start: 101`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 98`, `state_mutation: 82`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 8`
* *Architecture:* `api: 25`, `concurrency: 18`, `import: 95`
* *Defense:* `safety: 38`, `doc: 5`, `test: 2`, `immutability_locks: 265`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` org.apache.commons.lang3.StringUtils, org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate, com.google.gson.JsonArray, lombok.extern.slf4j.Slf4j, org.apache.fineract.infrastructure.event.business.domain.datatable.DatatableEntryDeletedBusinessEvent, java.math.BigDecimal, org.apache.fineract.infrastructure.dataqueries.api.DataTableApiConstant.API_PARAM_DROPCOLUMNS, org.apache.fineract.infrastructure.core.exception.PlatformServiceUnavailableException...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanApplicationValidator.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.608 IQR)
- **Top Global Matches:** file_cluster_8: 10.608, file_cluster_13: 10.858, file_cluster_7: 11.168
- **Magnitude:** 3049.94 | **LOC:** 2267 | **CtrlFlow:** 59.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (15.8361%), Tech Debt (45.9529%)
**Top Internal Functions/Classes:**
  * `validateForCreate` (Impact: 808.1 | O(N^6) | DB: 2)
  * `validateForModify` (Impact: 685.8 | O(N^6) | DB: 3)
  * `validateApproval` (Impact: 146.5 | O(N^6) | DB: 2)
  * `validatePartialPeriodSupport` (Impact: 143.3 | O(N^6))
  * `validateLoanMultiDisbursementDate` (Impact: 140.8 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 369`, `structural_boundaries: 250`, `args: 51`, `func_start: 83`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 105`, `state_mutation: 30`, `dead_code: 3`, `planned_debt: 6`, `duplicate_logic: 11`
* *Architecture:* `api: 26`, `import: 113`
* *Defense:* `doc: 3`, `sync_locks: 1`, `immutability_locks: 295`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 95):` org.apache.fineract.portfolio.accountdetails.domain.AccountType, org.apache.fineract.organisation.holiday.domain.Holiday, org.apache.fineract.organisation.holiday.domain.HolidayStatusType, org.apache.fineract.portfolio.loanaccount.exception.MultiDisbursementDataRequiredException, org.apache.commons.lang3.StringUtils, org.apache.fineract.portfolio.group.exception.ClientNotInGroupException, com.google.gson.JsonArray, lombok.extern.slf4j.Slf4j...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculator.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.332 IQR)
- **Top Global Matches:** file_cluster_17: 13.332, file_cluster_11: 13.344, file_cluster_13: 13.386
- **Magnitude:** 3043.6 | **LOC:** 2137 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 36.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (20.4565%), Tech Debt (65.0473%)
**Top Internal Functions/Classes:**
  * `calculateRateFactorPerPeriodForInterest` (Impact: 144.0 | O(N^6))
  * `calculateLastUnpaidRepaymentPeriodEMI` (Impact: 137.9 | O(2^N) | DB: 9)
  * `calculateRateFactorPerPeriod` (Impact: 104.5 | O(N^6))
  * `calculatePeriodRatio` (Impact: 103.8 | O(N^6) | DB: 1)
  * `attachTemporaryScheduleModelReAgedPeriod` (Impact: 97.1 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 213`, `args: 277`, `func_start: 205`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 209`, `dead_code: 5`, `planned_debt: 7`, `duplicate_logic: 12`
* *Architecture:* `api: 61`, `concurrency: 42`, `import: 48`
* *Defense:* `safety: 43`, `doc: 59`, `immutability_locks: 323`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` jakarta.annotation.Nonnull, org.apache.fineract.portfolio.loanaccount.domain.LoanTransaction, java.util.function.Function, org.apache.fineract.portfolio.loanproduct.calc.data.OutstandingDetails, java.math.MathContext, java.util.Iterator, java.util.ArrayList, java.math.BigDecimal...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/service/LoanScheduleAssembler.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.125 IQR)
- **Top Global Matches:** file_cluster_13: 12.125, file_cluster_8: 12.275, file_cluster_16: 12.652
- **Magnitude:** 2864.54 | **LOC:** 1607 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 70
- **Risk Profile:** Cognitive Load (61.2883%), Tech Debt (42.9722%)
**Top Internal Functions/Classes:**
  * `adjustExistingVariations` (Impact: 411.0 | O(N^6) | DB: 16)
  * `assempleVariableScheduleFrom` (Impact: 390.6 | O(N^6) | DB: 12)
  * `assembleLoanApplicationTermsFrom` (Impact: 370.5 | O(N^6) | DB: 1)
  * `updateLoanApplicationAttributes` (Impact: 270.1 | O(N^6) | DB: 70)
  * `createInterestRecalculationCalendarInsta` (Impact: 172.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 188`, `args: 38`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 267`, `planned_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 22`, `import: 121`
* *Defense:* `safety: 3`, `doc: 2`, `immutability_locks: 285`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 97):` org.apache.fineract.portfolio.accountdetails.domain.AccountType, org.apache.fineract.organisation.holiday.domain.Holiday, org.apache.fineract.portfolio.floatingrates.data.FloatingRatePeriodData, org.apache.fineract.organisation.holiday.domain.HolidayStatusType, org.apache.commons.lang3.StringUtils, org.apache.fineract.portfolio.loanaccount.data.OutstandingAmountsDTO, org.apache.fineract.portfolio.loanproduct.domain.LoanProductVariableInstallmentConfig, com.google.gson.JsonArray...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/Loan.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.908 IQR)
- **Top Global Matches:** file_cluster_0: 11.908, file_cluster_13: 12.07, file_cluster_8: 12.197
- **Magnitude:** 2714.84 | **LOC:** 1848 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 38.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (19.2272%), Tech Debt (29.885%)
**Top Internal Functions/Classes:**
  * `Loan` (Impact: 210.9 | O(N^5) | DB: 1)
  * `getNextPossibleRepaymentDateForReschedul` (Impact: 63.9 | O(N^6))
  * `findLastAssignmentHistoryRecord` (Impact: 59.6 | O(N^5))
  * `hasMonetaryActivityAfter` (Impact: 52.1 | O(N^5))
  * `getDisbursedAmount` (Impact: 48.9 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 309`, `args: 300`, `func_start: 218`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 98`, `state_mutation: 107`, `planned_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 353`, `import: 64`
* *Defense:* `safety: 7`, `doc: 18`, `immutability_locks: 193`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.329
  * `Choke Point (Betweenness):` 0.004479 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` org.apache.fineract.portfolio.loanproduct.domain.LoanProductRelatedDetail, org.apache.fineract.portfolio.accountdetails.domain.AccountType, java.util.Comparator, java.util.HashSet, lombok.AccessLevel, org.apache.fineract.infrastructure.core.domain.AbstractAuditableWithUTCDateTimeCustom, org.apache.commons.lang3.StringUtils, org.apache.fineract.portfolio.fund.domain.Fund...
  * `Imported By (In-Degree: 315):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanAccrualsProcessingServiceImpl.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.643 IQR)
- **Top Global Matches:** file_cluster_13: 12.643, file_cluster_0: 12.806, file_cluster_11: 12.816
- **Magnitude:** 2708.74 | **LOC:** 1304 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (28.5474%), Tech Debt (73.6346%)
**Top Internal Functions/Classes:**
  * `addAccruals` (Impact: 348.0 | O(N^6) | DB: 2)
  * `addAccruals` (Impact: 293.5 | O(2^N) | DB: 2)
  * `reprocessPeriodicAccruals` (Impact: 136.3 | O(N^6) | DB: 21)
    * *Intent:* // add charges paid by mappings
  * `determineFeeDetails` (Impact: 130.6 | O(N^6) | DB: 11)
  * `addInterestAccrual` (Impact: 122.8 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 268`, `structural_boundaries: 188`, `args: 87`, `func_start: 89`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 145`, `dead_code: 2`, `planned_debt: 3`, `duplicate_logic: 6`, `orphaned_logic: 10`
* *Architecture:* `api: 12`, `concurrency: 8`, `import: 74`
* *Defense:* `safety: 73`, `doc: 9`, `immutability_locks: 219`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 46):` org.apache.fineract.accounting.common.AccountingRuleType, org.apache.fineract.portfolio.loanaccount.loanschedule.domain.LoanScheduleGenerator, org.apache.fineract.portfolio.loanaccount.domain.LoanTransaction, org.apache.fineract.portfolio.loanproduct.domain.LoanProductRelatedDetail, org.apache.fineract.portfolio.loanaccount.domain.LoanTransactionType.ACCRUAL_ADJUSTMENT, java.util.Comparator, org.apache.fineract.portfolio.loanaccount.domain.LoanRepositoryWrapper, org.apache.fineract.portfolio.loanaccount.domain.LoanTransactionComparator...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/impl/AdvancedPaymentScheduleTransactionProcessor.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.319 IQR)
- **Top Global Matches:** file_cluster_13: 13.319, file_cluster_17: 13.36, file_cluster_11: 13.395
- **Magnitude:** 2625.2 | **LOC:** 4170 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 22.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (47.2368%), Tech Debt (10.0491%)
**Top Internal Functions/Classes:**
  * `handleCreditBalanceRefund` (Impact: 259.8 | O(2^N) | DB: 7)
  * `reprocessProgressiveLoanTransactions` (Impact: 172.7 | O(N^6) | DB: 6)
  * `liftOutstandingBalances` (Impact: 161.3 | O(N^6) | DB: 23)
  * `updateRepaymentPeriodsAfterAccelerateMat` (Impact: 122.5 | O(N^6) | DB: 9)
  * `processLatestTransaction` (Impact: 110.6 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 238`, `args: 217`, `func_start: 103`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 198`, `dead_code: 5`, `planned_debt: 9`
* *Architecture:* `api: 46`, `concurrency: 120`, `import: 107`
* *Defense:* `safety: 25`, `doc: 9`, `immutability_locks: 199`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 62):` org.apache.fineract.portfolio.loanaccount.domain.LoanChargeOffBehaviour, org.apache.fineract.portfolio.loanproduct.calc.data.OutstandingDetails, org.apache.fineract.portfolio.loanproduct.domain.AllocationType, org.apache.fineract.portfolio.loanaccount.data.OutstandingAmountsDTO, lombok.extern.slf4j.Slf4j, java.math.BigDecimal, org.apache.fineract.portfolio.loanaccount.domain.LoanRepaymentScheduleProcessingWrapper, org.apache.fineract.portfolio.loanaccount.domain.ChangedTransactionDetail...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/helper/ErrorMessageHelper.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.669 IQR)
- **Top Global Matches:** file_cluster_8: 10.669, file_cluster_16: 11.039, file_cluster_13: 11.131
- **Magnitude:** 2381.88 | **LOC:** 1002 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 31.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (21.043%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wrongValueInLineInJournalEntries` (Impact: 33.9 | O(N^4))
  * `wrongValueInLineInJournalEntry` (Impact: 33.8 | O(N^4))
  * `wrongAmountInDeferredCapitalizedIncome` (Impact: 30.6 | O(N^4))
  * `wrongValueInLineInRepaymentSchedule` (Impact: 28.3 | O(N^4))
  * `wrongValueInLineInTransactionsTab` (Impact: 28.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 186`, `args: 195`, `func_start: 168`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 17`, `duplicate_logic: 19`
* *Architecture:* `api: 315`, `import: 12`
* *Defense:* `doc: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` java.time.format.DateTimeFormatter, org.apache.fineract.client.models.BatchResponse, java.util.Set, java.io.IOException, org.apache.fineract.client.models.Header, org.apache.commons.lang3.StringUtils, java.util.List, org.apache.fineract.client.models.LoanAccountLockResponseDTO...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/loans/LoanTransactionHelper.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.006 IQR)
- **Top Global Matches:** file_cluster_0: 12.006, file_cluster_11: 12.153, file_cluster_13: 12.191
- **Magnitude:** 2369.36 | **LOC:** 3220 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (21.6663%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getDisburseLoanAsJSON` (Impact: 23.3 | O(N^3) | DB: 7)
    * *Intent:* // TODO: Rewrite to use fineract-client instead! // Example: org.apache.fineract.integrationtests.co...
  * `applyLoanCommand` (Impact: 21.4 | O(N^3) | DB: 2)
  * `createInterestPause` (Impact: 20.2 | O(2^N))
  * `updateInterestPauseByLoanId` (Impact: 20.2 | O(N^4))
  * `updateInterestPauseByExternalId` (Impact: 20.2 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 560`, `args: 425`, `func_start: 420`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 113`, `state_mutation: 268`, `planned_debt: 180`, `duplicate_logic: 147`
* *Architecture:* `io: 4`, `api: 392`, `import: 91`
* *Defense:* `doc: 7`, `test: 25`, `immutability_locks: 890`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.791
  * `Choke Point (Betweenness):` 0.000416 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` org.apache.fineract.integrationtests.common.Utils, lombok.extern.slf4j.Slf4j, org.junit.jupiter.api.Assertions.assertTrue, java.math.BigDecimal, java.io.ByteArrayInputStream, io.restassured.specification.ResponseSpecification, org.apache.fineract.client.models.GetLoansApprovalTemplateResponse, org.apache.fineract.client.models.GetLoanProductsResponse...
  * `Imported By (In-Degree: 119):` (Excluded from Brief to save tokens)

### `integration-tests/src/test/java/org/apache/fineract/integrationtests/ClientLoanIntegrationTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.7 IQR)
- **Top Global Matches:** file_cluster_8: 11.7, file_cluster_13: 12.054, file_cluster_16: 12.23
- **Magnitude:** 2332.98 | **LOC:** 8361 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (10.9303%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `verifyLoanRepaymentScheduleForEqualPrinc` (Impact: 376.4 | O(N^4))
  * `verifyLoanRepaymentScheduleForEqualPrinc` (Impact: 339.3 | O(N^4))
  * `verifyLoanRepaymentSchedule` (Impact: 154.3 | O(N^4))
  * `verifyLoanRepaymentSchedule` (Impact: 88.0 | O(N^5))
  * `testLoanScheduleWithInterestRecalculatio` (Impact: 52.9 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 499`, `args: 229`, `func_start: 1068`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 161`, `state_mutation: 151`, `duplicate_logic: 38`, `orphaned_logic: 32`
* *Architecture:* `api: 32`, `import: 100`
* *Defense:* `safety: 22`, `doc: 8`, `test: 874`, `immutability_locks: 454`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` org.apache.fineract.integrationtests.common.savings.SavingsStatusChecker, org.apache.fineract.integrationtests.common.Utils, io.restassured.http.ContentType, org.junit.jupiter.api.Assertions.assertTrue, java.math.BigDecimal, org.apache.fineract.integrationtests.common.loans.LoanTransactionHelper, org.apache.fineract.integrationtests.common.savings.SavingsProductHelper, io.restassured.specification.ResponseSpecification...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/SavingsAccountWritePlatformServiceJpaRepositoryImpl.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.979 IQR)
- **Top Global Matches:** file_cluster_13: 10.979, file_cluster_8: 11.059, file_cluster_0: 11.132
- **Magnitude:** 2322.9 | **LOC:** 1930 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (11.1957%), Tech Debt (20.1878%)
**Top Internal Functions/Classes:**
  * `inactivateCharge` (Impact: 184.9 | O(2^N) | DB: 2)
  * `undoTransaction` (Impact: 159.9 | O(2^N))
  * `postInterest` (Impact: 158.8 | O(2^N))
  * `close` (Impact: 149.7 | O(2^N) | DB: 1)
  * `postInterest` (Impact: 149.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 286`, `args: 56`, `func_start: 118`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 68`, `state_mutation: 78`, `dead_code: 1`, `duplicate_logic: 7`
* *Architecture:* `api: 66`, `import: 114`
* *Defense:* `safety: 25`, `doc: 4`, `immutability_locks: 363`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 79):` org.apache.fineract.portfolio.savings.SavingsApiConstants, org.springframework.data.domain.PageRequest, org.apache.fineract.portfolio.savings.data.SavingsAccountTransactionDataValidator, org.apache.fineract.portfolio.savings.SavingsApiConstants.chargeIdParamName, org.apache.commons.lang3.StringUtils, org.apache.fineract.portfolio.savings.SavingsApiConstants.SAVINGS_ACCOUNT_CHARGE_RESOURCE_NAME, org.apache.fineract.portfolio.savings.SavingsApiConstants.dueAsOfDateParamName, com.google.gson.JsonArray...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanReadPlatformServiceImpl.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.628 IQR)
- **Top Global Matches:** file_cluster_13: 11.628, file_cluster_8: 11.718, file_cluster_0: 11.813
- **Magnitude:** 2319.72 | **LOC:** 2309 | **CtrlFlow:** 39.9% | **Authorship Centralization:** 30.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (14.5301%), Tech Debt (79.156%)
**Top Internal Functions/Classes:**
  * `retrieveLoanTransactionTemplate` (Impact: 395.1 | O(2^N))
  * `retrieveAll` (Impact: 143.6 | O(N^5) | DB: 7)
  * `fetchLoansForInterestRecalculation` (Impact: 100.6 | O(N^6))
  * `retrieveAllOverdueInstallmentsForLoan` (Impact: 87.7 | O(N^6) | DB: 1)
  * `fetchLoansForInterestRecalculation` (Impact: 79.4 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 335`, `args: 106`, `func_start: 101`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 140`, `state_mutation: 92`, `planned_debt: 5`, `duplicate_logic: 19`
* *Architecture:* `io: 8`, `api: 117`, `import: 140`
* *Defense:* `safety: 22`, `doc: 2`, `immutability_locks: 627`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 113):` org.apache.fineract.infrastructure.core.api.ApiFacingEnum, org.apache.fineract.portfolio.accountdetails.domain.AccountType, org.apache.fineract.portfolio.accountdetails.service.AccountDetailsReadPlatformService, org.apache.fineract.portfolio.loanaccount.domain.LoanChargeOffBehaviour, org.apache.commons.lang3.StringUtils, org.apache.fineract.portfolio.loanaccount.data.OutstandingAmountsDTO, org.apache.fineract.useradministration.domain.AppUser, lombok.extern.slf4j.Slf4j...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanChargeService.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.715 IQR)
- **Top Global Matches:** file_cluster_13: 12.715, file_cluster_8: 12.88, file_cluster_11: 12.939
- **Magnitude:** 2310.1 | **LOC:** 965 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 111
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (13.3879%)
**Top Internal Functions/Classes:**
  * `createChargeAppliedTransaction` (Impact: 1843.2 | O(N^6) | DB: 111)
  * `recalculateLoanCharge` (Impact: 48.2 | O(N^5))
  * `recalculateLoanCharge` (Impact: 43.2 | O(N^5))
  * `makeChargePayment` (Impact: 22.9 | O(N^4))
  * `recalculateAllCharges` (Impact: 15.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 103`, `args: 61`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 277`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 24`, `import: 38`
* *Defense:* `doc: 3`, `immutability_locks: 160`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.089
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` org.apache.fineract.portfolio.loanaccount.domain.SingleLoanChargeRepaymentScheduleProcessingWrapper, org.apache.fineract.portfolio.loanaccount.domain.LoanTransaction, org.apache.fineract.portfolio.loanaccount.domain.LoanOverdueInstallmentCharge, java.util.HashSet, java.util.ArrayList, org.apache.fineract.portfolio.loanaccount.domain.LoanLifecycleStateMachine, java.math.BigDecimal, java.util.LinkedHashMap...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanChargeWritePlatformServiceImpl.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.027 IQR)
- **Top Global Matches:** file_cluster_13: 11.027, file_cluster_8: 11.167, file_cluster_0: 11.479
- **Magnitude:** 2231.44 | **LOC:** 1450 | **CtrlFlow:** 45.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (16.2678%), Tech Debt (13.8521%)
**Top Internal Functions/Classes:**
  * `waiveLoanCharge` (Impact: 403.0 | O(2^N) | DB: 3)
  * `waiveLoanCharge` (Impact: 256.8 | O(2^N) | DB: 2)
  * `payLoanCharge` (Impact: 145.5 | O(N^6))
  * `addLoanCharge` (Impact: 139.3 | O(N^6) | DB: 1)
  * `applyChargeToOverdueLoanInstallment` (Impact: 113.0 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 258`, `args: 48`, `func_start: 53`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 91`, `state_mutation: 84`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 25`, `import: 118`
* *Defense:* `safety: 13`, `doc: 1`, `immutability_locks: 185`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 101):` org.apache.fineract.portfolio.loanaccount.loanschedule.domain.DefaultScheduledDateGenerator, org.apache.fineract.portfolio.loanaccount.exception.InvalidLoanTransactionTypeException, org.apache.commons.lang3.StringUtils, org.apache.fineract.organisation.monetary.exception.InvalidCurrencyException, lombok.extern.slf4j.Slf4j, org.apache.fineract.portfolio.loanaccount.domain.LoanLifecycleStateMachine, java.math.BigDecimal, org.apache.fineract.portfolio.loanaccount.domain.LoanRepaymentScheduleProcessingWrapper...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/BatchHelper.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.427 IQR)
- **Top Global Matches:** file_cluster_13: 14.427, file_cluster_11: 14.645, file_cluster_7: 14.681
- **Magnitude:** 2179.64 | **LOC:** 1758 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (39.842%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `applyLoanRequest` (Impact: 153.6 | O(N^4) | DB: 5)
  * `applyLoanRequestWithClientIdAndExternalI` (Impact: 112.9 | O(N^4) | DB: 4)
  * `transitionLoanStateByExternalId` (Impact: 88.1 | O(N^5) | DB: 6)
    * *Intent:* /** * Creates and returns a Batch Request with given requestId and reference * * @param requestId * ...
  * `createActiveClientRequest` (Impact: 57.4 | O(N^4) | DB: 4)
    * *Intent:* /** * Returns a list of BatchResponse with query parameter enclosing transaction set to true by post...
  * `createClientRequest` (Impact: 53.1 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 166`, `args: 108`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 537`, `planned_debt: 7`, `duplicate_logic: 23`
* *Architecture:* `api: 123`, `import: 23`
* *Defense:* `doc: 330`, `test: 3`, `immutability_locks: 328`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.098
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` com.google.gson.Gson, java.util.ArrayList, org.apache.fineract.batch.command.internal.CreateTransactionLoanCommandStrategy, org.apache.fineract.client.util.JSON, io.restassured.specification.ResponseSpecification, org.slf4j.LoggerFactory, java.util.List, jakarta.ws.rs.HttpMethod...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `fineract-charge/src/main/java/org/apache/fineract/portfolio/charge/api/ChargesApiResourceSwagger.java` (JAVA) | Magnitude: 133.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 225, api: 102, doc: 85, decorators: 83
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/products/api/ProductsApiResource.java` (JAVA) | Magnitude: 111.14 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 109, structural_boundaries: 56, decorators: 46, import: 36
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/organisation/StaffHelper.java` (JAVA) | Magnitude: 150.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 104, immutability_locks: 46, structural_boundaries: 32, state_mutation: 32
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/rates/RatesHelper.java` (JAVA) | Magnitude: 70.76 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 57, immutability_locks: 23, structural_boundaries: 21, api: 14
- `fineract-loan-origination/src/main/java/org/apache/fineract/portfolio/loanorigination/api/LoanOriginatorApiResourceSwagger.java` (JAVA) | Magnitude: 44.94 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 70, api: 29, doc: 27, decorators: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/domain/FineractEvent.java` (JAVA) | Magnitude: 10.18 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 7, api: 4, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/database/metrics/TenantConnectionPoolMetricsTracker.java` (JAVA) | Magnitude: 113.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 96, immutability_locks: 26, encapsulation: 23, structural_boundaries: 18
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/LoanRefundTransactionTest.java` (JAVA) | Magnitude: 90.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 156, structural_boundaries: 58, args: 33, func_start: 32
- `fineract-accounting/src/main/java/org/apache/fineract/accounting/journalentry/domain/JournalEntry.java` (JAVA) | Magnitude: 42.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 88, immutability_locks: 33, decorators: 29, structural_boundaries: 23
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/domain/ShareAccountChargePaidBy.java` (JAVA) | Magnitude: 42.94 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 16, api: 14, args: 8
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/serialization/ShareAccountDataSerializer.java` (JAVA) | Magnitude: 1467.34 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 873, branch: 200, structural_boundaries: 167, state_mutation: 107

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `fineract-core/src/main/java/org/apache/fineract/portfolio/charge/data/ChargeData.java` (JAVA) | Magnitude: 55.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, immutability_locks: 46, encapsulation: 42, structural_boundaries: 23
- `fineract-command/src/test/java/org/apache/fineract/command/sample/service/DefaultDummyTenantService.java` (JAVA) | Magnitude: 17.34 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 6, api: 4, args: 2
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/diagnostics/performance/MeasuringUtil.java` (JAVA) | Magnitude: 32.5 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 12, generics: 7, args: 6
- `fineract-accounting/src/main/java/org/apache/fineract/accounting/journalentry/domain/JournalEntryRepository.java` (JAVA) | Magnitude: 332.93 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, branch: 10, structural_boundaries: 9, func_start: 9
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepositoryWrapper.java` (JAVA) | Magnitude: 514.44 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 212, structural_boundaries: 71, api: 61, args: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculator.java` (JAVA) | Magnitude: 3043.6 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 1557, immutability_locks: 323, branch: 310, args: 277
- `fineract-core/src/main/java/org/apache/fineract/portfolio/savings/SavingsCompoundingInterestPeriodType.java` (JAVA) | Magnitude: 122.88 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 40, branch: 14, structural_boundaries: 13, func_start: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/LoanManualInterestRefundResponseStructureTest.java` (JAVA) | Magnitude: 136.96 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 117, concurrency: 66, structural_boundaries: 42, func_start: 33
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/LoanCapitalizedIncomeTest.java` (JAVA) | Magnitude: 718.6 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1002, func_start: 418, concurrency: 414, structural_boundaries: 121
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/LoanContractTerminationTest.java` (JAVA) | Magnitude: 87.32 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 83, concurrency: 42, structural_boundaries: 32, func_start: 24
- `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/mapper/AdvancedPaymentDataMapper.java` (JAVA) | Magnitude: 34.78 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 18, structural_boundaries: 15, indent_spaces: 11, import: 9
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/database/DatabaseTypeResolver.java` (JAVA) | Magnitude: 56.58 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 18, concurrency: 18, api: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `fineract-security/src/main/java/org/apache/fineract/infrastructure/security/package-info.java` (JAVA) | Magnitude: 10.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 1
- `fineract-provider/src/main/java/org/apache/fineract/infrastructure/gcm/GcmConstants.java` (JAVA) | Magnitude: 44.62 | Delta: **0.152 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 43, doc: 42, api: 41, immutability_locks: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/data/LoanRepaymentPastDueData.java` (JAVA) | Magnitude: 16.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: scientific: 6, structural_boundaries: 5, immutability_locks: 5, encapsulation: 5
- `fineract-provider/src/test/java/org/apache/fineract/portfolio/delinquency/service/DelinquencyReadPlatformServiceImplTest.java` (JAVA) | Magnitude: 57.22 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 107, structural_boundaries: 60, time_date_logic: 32, import: 25
- `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/ProgressiveLoanTransactionValidatorImpl.java` (JAVA) | Magnitude: 696.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 427, structural_boundaries: 111, func_start: 64, immutability_locks: 59
- `fineract-provider/src/main/java/org/apache/fineract/infrastructure/entityaccess/service/FineractEntityAccessWriteService.java` (JAVA) | Magnitude: 31.21 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, args: 5, func_start: 5, indent_spaces: 5
- `fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/data/ClientChargePaymentDTO.java` (JAVA) | Magnitude: 16.26 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, immutability_locks: 5, encapsulation: 5, indent_spaces: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `fineract-document/src/main/java/org/apache/fineract/infrastructure/documentmanagement/api/ImageApiConstants.java` (JAVA) | Magnitude: 9.0 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: api: 7, immutability_locks: 7, indent_spaces: 7, globals: 6
- `fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/constants/ChargeConstants.java` (JAVA) | Magnitude: 7.08 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 6, api: 5, immutability_locks: 5, globals: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculator.java` -> Churn: **88.24%** | Cog Load: 20.4565% | Debt: 65.0473%
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanReadPlatformServiceImpl.java` -> Churn: **75.27%** | Cog Load: 14.5301% | Debt: 79.156%
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanWritePlatformServiceJpaRepositoryImpl.java` -> Churn: **63.05%** | Cog Load: 11.4799% | Debt: 54.5404%
- `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanReAgingStepDef.java` -> Churn: **62.37%** | Cog Load: 77.477% | Debt: 0.0%
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepaymentScheduleInstallment.java` -> Churn: **61.61%** | Cog Load: 92.8249% | Debt: 96.3744%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepository.java` -> **Adam Saghy** (100.0% isolated ownership) | Magnitude: 7305.13
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/SavingsAccountWritePlatformServiceJpaRepositoryImpl.java` -> **Juan-Pablo-Alvarez** (100.0% isolated ownership) | Magnitude: 2322.9
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/BatchHelper.java` -> **Adam Saghy** (100.0% isolated ownership) | Magnitude: 2179.64
- `fineract-core/src/main/java/org/apache/fineract/portfolio/calendar/service/CalendarUtils.java` -> **Aman-Mittal** (100.0% isolated ownership) | Magnitude: 1575.78
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/serialization/ShareAccountDataSerializer.java` -> **Wilfred Kigenyi** (100.0% isolated ownership) | Magnitude: 1467.34

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/data/LoanAccountData.java` -> **Severity: 0.051** (Bridge: 0.0005 * Flux: 99.9994%)
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/Loan.java` -> **Severity: 0.048** (Bridge: 0.0045 * Flux: 10.7961%)
- `fineract-core/src/main/java/org/apache/fineract/organisation/monetary/domain/MoneyHelper.java` -> **Severity: 0.03** (Bridge: 0.0003 * Flux: 99.9436%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/MathUtil.java` -> **Severity: 0.029** (Bridge: 0.0004 * Flux: 63.3372%)
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/data/LoanPointInTimeData.java` -> **Severity: 0.027** (Bridge: 0.0016 * Flux: 16.7982%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `fineract-validation/src/main/java/org/apache/fineract/validation/constraints/LocalDate.java` -> **Severity: 2341.551** (Blast Radius: 37.198 * Doc Risk: 62.9483%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/domain/ExternalId.java` -> **Severity: 2214.321** (Blast Radius: 22.145 * Doc Risk: 99.9919%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/api/JsonCommand.java` -> **Severity: 1720.8** (Blast Radius: 17.208 * Doc Risk: 100.0%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/data/CommandProcessingResult.java` -> **Severity: 1473.097** (Blast Radius: 14.731 * Doc Risk: 99.9998%)
- `fineract-provider/src/main/java/org/apache/fineract/spm/domain/Component.java` -> **Severity: 1342.396** (Blast Radius: 13.424 * Doc Risk: 99.9997%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
