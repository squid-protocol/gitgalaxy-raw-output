# ARCHITECTURAL_BRIEF: fineract
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/fineract` |
| **Timestamp** | `2026-08-07T04:35:37.888469+00:00` |
| **Scan Duration** | `26.05s` |
| **Git Branch** | `develop` |
| **Git Commit** | `e6e5a4b6eec5a33d327546c640e6b7f281b5ae42` |
| **Git Remote** | `https://github.com/apache/fineract.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 5884 malicious artifacts.

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
| file_cluster_8 | 2150 | 33.9% |
| file_cluster_16 | 229 | 3.6% |
| file_cluster_0 | 115 | 1.8% |
| file_cluster_4 | 11 | 0.2% |
| file_cluster_17 | 2 | 0.0% |
| file_cluster_9 | 2 | 0.0% |
| file_cluster_7 | 2 | 0.0% |
| Unknown | 1 | 0.0% |

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
| Cognitive Load Exposure | 0.0 | 100.0 | 8.4 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 29.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.6 | 2.3 | 0.0 |
| API Exposure | 0.0 | 19.7 | 5.2 | 5.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 9.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 72.9 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 85.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 6.0 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 3.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 33.6 | 19.6 | 0.0 |
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

- `createChargeAppliedTransaction` (@ `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanChargeService.java`) -> Impact: **553.2** | LOC: 744
- `applyEarlyPaymentStrategy` (@ `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/AbstractCumulativeLoanScheduleGenerator.java`) -> Impact: **494.7** | LOC: 830
- `testCreateShareAccountWithCharges` (@ `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/shares/ShareAccountIntegrationTests.java`) -> Impact: **313.0** | LOC: 627
- `validateForCreate` (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/serialization/LoanProductDataValidator.java`) -> Impact: **301.1** | LOC: 682
- `rescheduleNextInstallments` (@ `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/AbstractCumulativeLoanScheduleGenerator.java`) -> Impact: **299.8** | LOC: 566
- `validateForUpdate` (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/serialization/LoanProductDataValidator.java`) -> Impact: **258.6** | LOC: 704
- `validateForCreate` (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanApplicationValidator.java`) -> Impact: **250.9** | LOC: 559
- `validateForModify` (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanApplicationValidator.java`) -> Impact: **218.1** | LOC: 621
- `retrieveTransactionTemplate` (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/api/LoanTransactionsApiResource.java`) -> Impact: **181.9** | LOC: 98
- `getNextStatus` (@ `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/DefaultLoanLifecycleStateMachine.java`) -> Impact: **174.6** | LOC: 132

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `integration-tests/src/test/java/org/apache/fineract/integrationtests` | 227 | 26182.32 | 10.75% | 0.0% |
| `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain` | 73 | 20372.46 | 9.52% | 39.9% |
| `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service` | 46 | 8065.4 | 24.42% | 51.86% |
| `fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain` | 40 | 6454.56 | 12.09% | 67.0% |
| `integration-tests/src/test/java/org/apache/fineract/integrationtests/common` | 44 | 6019.38 | 21.43% | 0.0% |
| `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain` | 26 | 5487.18 | 7.46% | 37.72% |
| `fineract-provider/src/main/resources` | 9 | 5038.24 | 0.56% | 0.0% |
| `fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service` | 18 | 4872.82 | 11.68% | 34.48% |
| `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan` | 17 | 4757.98 | 17.57% | 0.0% |
| `fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service` | 27 | 4455.06 | 8.58% | 32.42% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `buildSrc/src/main/groovy/org/apache/fineract/gradle/FineractPlugin.groovy` -> **100.0%** Exposure
- `buildSrc/src/main/groovy/org/apache/fineract/gradle/service/SubversionService.groovy` -> **100.0%** Exposure
- `config/docker/mysql/docker-entrypoint-initdb.d/01-databases.sql` -> **100.0%** Exposure
- `fineract-db/mifospltaform-tenants-first-time-install.sql` -> **100.0%** Exposure
- `fineract-db/multi-tenant-demo-backups/0001-mifos-platform-shared-tenants.sql` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `scripts/split-features.sh` -> **100.0%** Exposure
- `scripts/split-tests.sh` -> **100.0%** Exposure
- `fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/service/ProductToGLAccountMappingReadPlatformServiceImpl.java` -> **100.0%** Exposure
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/config/AbstractFineractModuleProperties.java` -> **100.0%** Exposure
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/config/FineractProperties.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanStepDef.java` -> **168** Orphaned Functions | **36** Duplicates
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/loans/LoanTransactionHelper.java` -> **0** Orphaned Functions | **204** Duplicates
- `fineract-progressive-loan/src/test/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculatorTest.java` -> **78** Orphaned Functions | **48** Duplicates
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/AdvancedPaymentAllocationLoanRepaymentScheduleTest.java` -> **80** Orphaned Functions | **9** Duplicates
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
17. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepaymentScheduleProcessingWrapper.java`** -> AI Confidence: **99.35%**
18. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/domain/ProductToGLAccountMappingRepository.java`** -> AI Confidence: **99.34%**
19. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/AprCalculator.java`** -> AI Confidence: **99.34%**
20. **`buildSrc/src/main/groovy/org/apache/fineract/gradle/FineractPlugin.groovy`** -> AI Confidence: **99.31%**
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
160. **`buildSrc/src/main/groovy/org.apache.fineract.release.gradle`** -> AI Confidence: **99.29%**
161. **`scripts/verify-signed-commits.sh`** -> AI Confidence: **99.29%**
162. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/configuration/api/GlobalConfigurationConstants.java`** -> AI Confidence: **99.29%**
163. **`fineract-core/src/main/java/org/apache/fineract/portfolio/common/domain/DayOfWeekType.java`** -> AI Confidence: **99.29%**
164. **`integration-tests/src/test/resources/image-text-wrong-content.jsp`** -> AI Confidence: **99.29%**
165. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/service/ProductToGLAccountMappingHelper.java`** -> AI Confidence: **99.24%**
166. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/service/SavingsProductToGLAccountMappingHelper.java`** -> AI Confidence: **99.24%**
167. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/service/ShareProductToGLAccountMappingHelper.java`** -> AI Confidence: **99.24%**
168. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/rule/domain/AccountingRule.java`** -> AI Confidence: **99.24%**
169. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/rule/service/AccountingRuleWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
170. **`fineract-branch/src/main/java/org/apache/fineract/organisation/teller/domain/Cashier.java`** -> AI Confidence: **99.24%**
171. **`fineract-client-feign/src/main/java/org/apache/fineract/client/feign/FineractMultipartEncoder.java`** -> AI Confidence: **99.24%**
172. **`fineract-client-feign/src/test/java/org/apache/fineract/client/feign/integration/FineractFeignClientIntegrationTest.java`** -> AI Confidence: **99.24%**
173. **`fineract-client-feign/src/test/java/org/apache/fineract/client/feign/performance/ConnectionPoolPerformanceTest.java`** -> AI Confidence: **99.24%**
174. **`fineract-core/src/main/java/org/apache/fineract/accounting/glaccount/domain/GLAccount.java`** -> AI Confidence: **99.24%**
175. **`fineract-core/src/main/java/org/apache/fineract/batch/command/CommandStrategyUtils.java`** -> AI Confidence: **99.24%**
176. **`fineract-core/src/main/java/org/apache/fineract/batch/service/BatchApiServiceImpl.java`** -> AI Confidence: **99.24%**
177. **`fineract-core/src/main/java/org/apache/fineract/batch/service/ResolutionHelper.java`** -> AI Confidence: **99.24%**
178. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/domain/FineractPlatformTenantConnection.java`** -> AI Confidence: **99.24%**
179. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/exception/ErrorHandler.java`** -> AI Confidence: **99.24%**
180. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/serialization/DatatableCommandFromApiJsonDeserializer.java`** -> AI Confidence: **99.24%**
181. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/database/JavaType.java`** -> AI Confidence: **99.24%**
182. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/database/metrics/TenantConnectionPoolMetricsTracker.java`** -> AI Confidence: **99.24%**
183. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/event/business/service/BusinessEventNotifierServiceImpl.java`** -> AI Confidence: **99.24%**
184. **`fineract-core/src/main/java/org/apache/fineract/portfolio/calendar/domain/Calendar.java`** -> AI Confidence: **99.24%**
185. **`fineract-core/src/main/java/org/apache/fineract/portfolio/client/domain/ClientRepository.java`** -> AI Confidence: **99.24%**
186. **`fineract-core/src/main/java/org/apache/fineract/portfolio/group/domain/Group.java`** -> AI Confidence: **99.24%**
187. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanOverrideFieldsStepDef.java`** -> AI Confidence: **99.24%**
188. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanStepDef.java`** -> AI Confidence: **99.24%**
189. **`fineract-e2e-tests-runner/src/test/java/org/apache/fineract/test/initializer/suite/JobSuiteInitializerStep.java`** -> AI Confidence: **99.24%**
190. **`fineract-investor/src/main/java/org/apache/fineract/investor/service/AccountingServiceImpl.java`** -> AI Confidence: **99.24%**
191. **`fineract-loan/src/main/java/org/apache/fineract/accounting/productaccountmapping/service/LoanProductToGLAccountMappingHelper.java`** -> AI Confidence: **99.24%**
192. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/delinquency/helper/DelinquencyEffectivePauseHelperImpl.java`** -> AI Confidence: **99.24%**
193. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/Loan.java`** -> AI Confidence: **99.24%**
194. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepaymentScheduleInstallment.java`** -> AI Confidence: **99.24%**
195. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/CumulativeDecliningBalanceInterestLoanScheduleGenerator.java`** -> AI Confidence: **99.24%**
196. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanCalculateRepaymentPastDueService.java`** -> AI Confidence: **99.24%**
197. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanDownPaymentHandlerServiceImpl.java`** -> AI Confidence: **99.24%**
198. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanScheduleService.java`** -> AI Confidence: **99.24%**
199. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/domain/LoanProduct.java`** -> AI Confidence: **99.24%**
200. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/service/LoanEnumerations.java`** -> AI Confidence: **99.24%**
201. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/calc/data/ProgressiveLoanInterestScheduleModel.java`** -> AI Confidence: **99.24%**
202. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/calc/data/RepaymentPeriod.java`** -> AI Confidence: **99.24%**
203. **`fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/AccountingProcessorHelper.java`** -> AI Confidence: **99.24%**
204. **`fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/JournalEntryWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
205. **`fineract-provider/src/main/java/org/apache/fineract/commands/api/AuditsApiResource.java`** -> AI Confidence: **99.24%**
206. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/accountnumberformat/data/AccountNumberFormatDataValidator.java`** -> AI Confidence: **99.24%**
207. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/loan/LoanImportHandler.java`** -> AI Confidence: **99.24%**
208. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/AbstractWorkbookPopulator.java`** -> AI Confidence: **99.24%**
209. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/chartofaccounts/ChartOfAccountsWorkbook.java`** -> AI Confidence: **99.24%**
210. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/client/ClientEntityWorkbookPopulator.java`** -> AI Confidence: **99.24%**
211. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/service/BulkImportWorkbookServiceImpl.java`** -> AI Confidence: **99.24%**
212. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/email/data/EmailDataValidator.java`** -> AI Confidence: **99.24%**
213. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/jobs/executereportmailingjobs/ExecuteReportMailingJobsTasklet.java`** -> AI Confidence: **99.24%**
214. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/jobs/getdeliveryreportsfromsmsgateway/GetDeliveryReportsFromSmsGatewayTasklet.java`** -> AI Confidence: **99.24%**
215. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/configuration/service/ExternalServicesPropertiesReadPlatformServiceImpl.java`** -> AI Confidence: **99.24%**
216. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/diagnostics/performance/sampling/output/SamplingDataPrinter.java`** -> AI Confidence: **99.24%**
217. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/domain/Report.java`** -> AI Confidence: **99.24%**
218. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/service/EntityDatatableChecksWritePlatformServiceImpl.java`** -> AI Confidence: **99.24%**
219. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/service/GenericDataServiceImpl.java`** -> AI Confidence: **99.24%**
220. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/entityaccess/service/FineractEntityAccessReadServiceImpl.java`** -> AI Confidence: **99.24%**
221. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/event/external/producer/jms/JMSMultiExternalEventProducer.java`** -> AI Confidence: **99.24%**
222. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/gcm/domain/Sender.java`** -> AI Confidence: **99.24%**
223. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/reportmailingjob/service/ReportMailingJobEmailServiceImpl.java`** -> AI Confidence: **99.24%**
224. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/reportmailingjob/validation/ReportMailingJobValidator.java`** -> AI Confidence: **99.24%**
225. **`fineract-provider/src/main/java/org/apache/fineract/organisation/teller/service/TellerManagementReadPlatformServiceImpl.java`** -> AI Confidence: **99.24%**
226. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/account/jobs/executestandinginstructions/ExecuteStandingInstructionsTasklet.java`** -> AI Confidence: **99.24%**
227. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/account/service/AccountAssociationsReadPlatformServiceImpl.java`** -> AI Confidence: **99.24%**
228. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/account/service/AccountTransfersWritePlatformServiceImpl.java`** -> AI Confidence: **99.24%**
229. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/account/service/StandingInstructionHistoryReadPlatformServiceImpl.java`** -> AI Confidence: **99.24%**
230. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/account/service/StandingInstructionReadPlatformServiceImpl.java`** -> AI Confidence: **99.24%**
231. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/data/ClientDataValidator.java`** -> AI Confidence: **99.24%**
232. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/serialization/ClientFamilyMemberCommandFromApiJsonDeserializer.java`** -> AI Confidence: **99.24%**
233. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/service/ClientWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
234. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/group/api/GroupsApiResource.java`** -> AI Confidence: **99.24%**
235. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/group/service/GroupingTypesWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
236. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/interestratechart/data/InterestRateChartSlabDataValidator.java`** -> AI Confidence: **99.24%**
237. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanAccountDomainServiceJpa.java`** -> AI Confidence: **99.24%**
238. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/guarantor/domain/Guarantor.java`** -> AI Confidence: **99.24%**
239. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/guarantor/service/GuarantorWritePlatformServiceJpaRepositoryIImpl.java`** -> AI Confidence: **99.24%**
240. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/jobs/applychargetooverdueloaninstallment/ApplyChargeToOverdueLoanInstallmentTasklet.java`** -> AI Confidence: **99.24%**
241. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/jobs/recalculateinterestforloan/RecalculateInterestForLoanTasklet.java`** -> AI Confidence: **99.24%**
242. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanDisbursementValidator.java`** -> AI Confidence: **99.24%**
243. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanApplicationWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
244. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanChargeWritePlatformServiceImpl.java`** -> AI Confidence: **99.24%**
245. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanProductFloatingRatesUpdateUtil.java`** -> AI Confidence: **99.24%**
246. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanReadPlatformServiceImpl.java`** -> AI Confidence: **99.24%**
247. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/util/BuyDownFeeAmortizationUtil.java`** -> AI Confidence: **99.24%**
248. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/util/CapitalizedIncomeAmortizationUtil.java`** -> AI Confidence: **99.24%**
249. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/meeting/service/MeetingWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
250. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/note/service/NoteWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
251. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/data/DepositAccountDataValidator.java`** -> AI Confidence: **99.24%**
252. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/data/DepositProductDataValidator.java`** -> AI Confidence: **99.24%**
253. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/domain/FixedDepositAccount.java`** -> AI Confidence: **99.24%**
254. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/domain/SavingsAccountAssembler.java`** -> AI Confidence: **99.24%**
255. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/jobs/applyannualfeeforsavings/ApplyAnnualFeeForSavingsTasklet.java`** -> AI Confidence: **99.24%**
256. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/jobs/generateadhocclientschhedule/GenerateAdhocClientScheduleTasklet.java`** -> AI Confidence: **99.24%**
257. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/jobs/payduesavingscharges/PayDueSavingsChargesTasklet.java`** -> AI Confidence: **99.24%**
258. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/jobs/postinterestforsavings/PostInterestForSavingTasklet.java`** -> AI Confidence: **99.24%**
259. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/jobs/updatedepositsaccountmaturitydetails/UpdateDepositsAccountMaturityDetailsTasklet.java`** -> AI Confidence: **99.24%**
260. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/SavingsApplicationProcessWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
261. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/search/SavingsAccountTransactionsSearchServiceImpl.java`** -> AI Confidence: **99.24%**
262. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/domain/ShareAccount.java`** -> AI Confidence: **99.24%**
263. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/jobs/postdividentsforshares/PostDividentsForSharesTasklet.java`** -> AI Confidence: **99.24%**
264. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/service/ShareAccountWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.24%**
265. **`fineract-provider/src/main/java/org/apache/fineract/useradministration/service/UserDataValidator.java`** -> AI Confidence: **99.24%**
266. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/core/config/ApiVerificationTest.java`** -> AI Confidence: **99.24%**
267. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/dataqueries/service/DatatableUtilTest.java`** -> AI Confidence: **99.24%**
268. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/sqlbuilder/SqlBuilderStepDefinitions.java`** -> AI Confidence: **99.24%**
269. **`fineract-provider/src/test/java/org/apache/fineract/portfolio/loanaccount/service/LoanChargeWritePlatformServiceImplTest.java`** -> AI Confidence: **99.24%**
270. **`fineract-provider/src/test/java/org/apache/fineract/portfolio/loanaccount/service/reaging/LoanReAgingValidatorTest.java`** -> AI Confidence: **99.24%**
271. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/interestratechart/domain/InterestRateChart.java`** -> AI Confidence: **99.24%**
272. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/data/SavingsAccountDataValidator.java`** -> AI Confidence: **99.24%**
273. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/data/SavingsProductDataValidator.java`** -> AI Confidence: **99.24%**
274. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain/DepositProductAssembler.java`** -> AI Confidence: **99.24%**
275. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain/SavingsAccountTransactionRepository.java`** -> AI Confidence: **99.24%**
276. **`fineract-tax/src/main/java/org/apache/fineract/portfolio/tax/service/TaxUtils.java`** -> AI Confidence: **99.24%**
277. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/CreditBureauTest.java`** -> AI Confidence: **99.24%**
278. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/SmsApiResourceIntegrationTest.java`** -> AI Confidence: **99.24%**
279. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/SurveyIntegrationTest.java`** -> AI Confidence: **99.24%**
280. **`twofactor-tests/src/test/java/org/apache/fineract/twofactortests/TwoFactorAuthenticationTest.java`** -> AI Confidence: **99.24%**
281. **`fineract-core/src/main/java/org/apache/fineract/portfolio/savings/domain/interest/SavingsAccountTransactionDetailsForPostingPeriod.java`** -> AI Confidence: **99.23%**
282. **`fineract-core/src/main/java/org/apache/fineract/util/StreamUtil.java`** -> AI Confidence: **99.23%**
283. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/FixedDepositProductSheetPopulator.java`** -> AI Confidence: **99.23%**
284. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/configuration/service/ExternalServicesReadPlatformServiceImpl.java`** -> AI Confidence: **99.23%**
285. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/gcm/domain/Message.java`** -> AI Confidence: **99.23%**
286. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/client/feign/helpers/FeignAccountHelper.java`** -> AI Confidence: **99.23%**
287. **`integration-tests/src/test/java/org/apache/fineract/integrationtests/common/externalevents/LoanAdjustTransactionBusinessEvent.java`** -> AI Confidence: **99.23%**
288. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/interestratechart/incentive/ClientAttributeIncentiveCalculation.java`** -> AI Confidence: **99.22%**
289. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/financialactivityaccount/service/FinancialActivityAccountWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
290. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/journalentry/JournalEntryMapper.java`** -> AI Confidence: **99.18%**
291. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/serialization/ProductToGLAccountMappingFromApiJsonDeserializer.java`** -> AI Confidence: **99.18%**
292. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/provisioning/service/ProvisioningEntriesReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
293. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/rule/api/AccountingRuleApiResource.java`** -> AI Confidence: **99.18%**
294. **`fineract-accounting/src/main/java/org/apache/fineract/accounting/rule/service/AccountingRuleReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
295. **`fineract-branch/src/main/java/org/apache/fineract/organisation/teller/api/TellerApiResourceSwagger.java`** -> AI Confidence: **99.18%**
296. **`fineract-charge/src/main/java/org/apache/fineract/portfolio/charge/service/ChargeDropdownReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
297. **`fineract-client-feign/src/main/java/org/apache/fineract/client/feign/FineractFeignClientConfig.java`** -> AI Confidence: **99.18%**
298. **`fineract-client-feign/src/test/java/org/apache/fineract/client/feign/integration/EncoderDecoderIntegrationTest.java`** -> AI Confidence: **99.18%**
299. **`fineract-client-feign/src/test/java/org/apache/fineract/client/services/DocumentsApiFixedIntegrationTest.java`** -> AI Confidence: **99.18%**
300. **`fineract-cob/src/main/java/org/apache/fineract/cob/COBBusinessStepServiceImpl.java`** -> AI Confidence: **99.18%**
301. **`fineract-cob/src/main/java/org/apache/fineract/cob/listener/COBExecutionListenerRunner.java`** -> AI Confidence: **99.18%**
302. **`fineract-cob/src/main/java/org/apache/fineract/cob/service/ConfigJobParameterServiceImpl.java`** -> AI Confidence: **99.18%**
303. **`fineract-command/src/main/java/org/apache/fineract/command/implementation/AsynchronousCommandExecutor.java`** -> AI Confidence: **99.18%**
304. **`fineract-command/src/main/java/org/apache/fineract/command/implementation/BaseCommandPipeline.java`** -> AI Confidence: **99.18%**
305. **`fineract-command/src/main/java/org/apache/fineract/command/persistence/mapping/CommandJsonMapper.java`** -> AI Confidence: **99.18%**
306. **`fineract-core/src/main/java/org/apache/fineract/commands/provider/CommandHandlerProvider.java`** -> AI Confidence: **99.18%**
307. **`fineract-core/src/main/java/org/apache/fineract/commands/service/CommandSourceService.java`** -> AI Confidence: **99.18%**
308. **`fineract-core/src/main/java/org/apache/fineract/commands/service/CommandWrapperBuilder.java`** -> AI Confidence: **99.18%**
309. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/businessdate/service/BusinessDateReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
310. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/cache/api/CacheApiResource.java`** -> AI Confidence: **99.18%**
311. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/api/JsonQuery.java`** -> AI Confidence: **99.18%**
312. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/exceptionmapper/IdempotentCommandExceptionMapper.java`** -> AI Confidence: **99.18%**
313. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/filters/CorrelationHeaderFilter.java`** -> AI Confidence: **99.18%**
314. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/filters/IdempotencyStoreFilter.java`** -> AI Confidence: **99.18%**
315. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/database/PostgreSQLQueryService.java`** -> AI Confidence: **99.18%**
316. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/event/external/service/ExternalEventConfigurationValidationService.java`** -> AI Confidence: **99.18%**
317. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/event/external/service/ExternalEventService.java`** -> AI Confidence: **99.18%**
318. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/event/external/service/InternalExternalEventService.java`** -> AI Confidence: **99.18%**
319. **`fineract-core/src/main/java/org/apache/fineract/infrastructure/jobs/TenantAwareEqualsHashCodeAdvice.java`** -> AI Confidence: **99.18%**
320. **`fineract-core/src/main/java/org/apache/fineract/portfolio/calendar/data/CalendarHistoryDataWrapper.java`** -> AI Confidence: **99.18%**
321. **`fineract-core/src/main/java/org/apache/fineract/portfolio/calendar/service/CalendarEnumerations.java`** -> AI Confidence: **99.18%**
322. **`fineract-core/src/main/java/org/apache/fineract/portfolio/client/domain/Client.java`** -> AI Confidence: **99.18%**
323. **`fineract-core/src/main/java/org/apache/fineract/portfolio/paymenttype/service/PaymentTypeWriteServiceImpl.java`** -> AI Confidence: **99.18%**
324. **`fineract-core/src/main/java/org/apache/fineract/portfolio/savings/data/SavingsAccountTransactionData.java`** -> AI Confidence: **99.18%**
325. **`fineract-core/src/main/java/org/apache/fineract/useradministration/domain/AppUserClientMapping.java`** -> AI Confidence: **99.18%**
326. **`fineract-core/src/test/java/org/apache/fineract/batch/service/BatchApiServiceImplTest.java`** -> AI Confidence: **99.18%**
327. **`fineract-document/src/main/java/org/apache/fineract/infrastructure/contentstore/detector/TikaContentDetector.java`** -> AI Confidence: **99.18%**
328. **`fineract-document/src/main/java/org/apache/fineract/infrastructure/contentstore/processor/DataUrlDecoderContentProcessor.java`** -> AI Confidence: **99.18%**
329. **`fineract-document/src/main/java/org/apache/fineract/infrastructure/documentmanagement/api/DocumentApiResource.java`** -> AI Confidence: **99.18%**
330. **`fineract-document/src/main/java/org/apache/fineract/infrastructure/documentmanagement/service/DocumentWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
331. **`fineract-document/src/main/java/org/apache/fineract/infrastructure/documentmanagement/service/ImageWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
332. **`fineract-document/src/test/java/org/apache/fineract/infrastructure/documentmanagement/service/ImageWritePlatformServiceImplTest.java`** -> AI Confidence: **99.18%**
333. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/common/BusinessDateStepDef.java`** -> AI Confidence: **99.18%**
334. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/common/GlobalConfigurationStepDef.java`** -> AI Confidence: **99.18%**
335. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/hook/MessagingHook.java`** -> AI Confidence: **99.18%**
336. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanChargeBackStepDef.java`** -> AI Confidence: **99.18%**
337. **`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanChargeStepDef.java`** -> AI Confidence: **99.18%**
338. **`fineract-e2e-tests-runner/src/test/java/org/apache/fineract/test/initializer/global/ChargeGlobalInitializerStep.java`** -> AI Confidence: **99.18%**
339. **`fineract-e2e-tests-runner/src/test/java/org/apache/fineract/test/initializer/global/WorkingCapitalLoanProductInitializerStep.java`** -> AI Confidence: **99.18%**
340. **`fineract-e2e-tests-runner/src/test/java/org/apache/fineract/test/initializer/suite/ExternalEventSuiteInitializerStep.java`** -> AI Confidence: **99.18%**
341. **`fineract-investor/src/main/java/org/apache/fineract/investor/cob/loan/LoanAccountOwnerTransferBusinessStep.java`** -> AI Confidence: **99.18%**
342. **`fineract-investor/src/main/java/org/apache/fineract/investor/service/search/mapper/ExternalAssetOwnerSearchDataMapper.java`** -> AI Confidence: **99.18%**
343. **`fineract-investor/src/main/java/org/apache/fineract/investor/service/serialization/serializer/investor/InvestorBusinessEventSerializer.java`** -> AI Confidence: **99.18%**
344. **`fineract-investor/src/test/java/org/apache/fineract/investor/service/ExternalAssetOwnerLoanProductAttributesWriteServiceImplTest.java`** -> AI Confidence: **99.18%**
345. **`fineract-investor/src/test/java/org/apache/fineract/investor/service/LoanAccountOwnerTransferServiceTest.java`** -> AI Confidence: **99.18%**
346. **`fineract-investor/src/test/java/org/apache/fineract/investor/service/LoanTransferabilityServiceImplTest.java`** -> AI Confidence: **99.18%**
347. **`fineract-loan-origination/src/main/java/org/apache/fineract/portfolio/loanorigination/enricher/LoanAccountDataV1OriginatorEnricher.java`** -> AI Confidence: **99.18%**
348. **`fineract-loan-origination/src/main/java/org/apache/fineract/portfolio/loanorigination/enricher/LoanTransactionDataV1OriginatorEnricher.java`** -> AI Confidence: **99.18%**
349. **`fineract-loan-origination/src/main/java/org/apache/fineract/portfolio/loanorigination/service/LoanOriginatorLinkingServiceImpl.java`** -> AI Confidence: **99.18%**
350. **`fineract-loan-origination/src/main/java/org/apache/fineract/portfolio/loanorigination/service/LoanOriginatorWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
351. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/delinquency/domain/LoanDelinquencyActionRepository.java`** -> AI Confidence: **99.18%**
352. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/delinquency/domain/LoanInstallmentDelinquencyTagRepository.java`** -> AI Confidence: **99.18%**
353. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/delinquency/helper/InstallmentDelinquencyAggregator.java`** -> AI Confidence: **99.18%**
354. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/delinquency/service/DelinquencyWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
355. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/interestpauses/handler/CreateInterestPauseCommandHandler.java`** -> AI Confidence: **99.18%**
356. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/interestpauses/handler/DeleteInterestPauseCommandHandler.java`** -> AI Confidence: **99.18%**
357. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/interestpauses/handler/UpdateInterestPauseCommandHandler.java`** -> AI Confidence: **99.18%**
358. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/interestpauses/service/InterestPauseWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
359. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/api/LoanScheduleApiResource.java`** -> AI Confidence: **99.18%**
360. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/data/DisbursementData.java`** -> AI Confidence: **99.18%**
361. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/data/LoanAccountData.java`** -> AI Confidence: **99.18%**
362. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanChargeRepository.java`** -> AI Confidence: **99.18%**
363. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanInstallmentCharge.java`** -> AI Confidence: **99.18%**
364. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanTransaction.java`** -> AI Confidence: **99.18%**
365. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/guarantor/command/GuarantorCommand.java`** -> AI Confidence: **99.18%**
366. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/jobs/setloandelinquencytags/SetLoanDelinquencyTagsTasklet.java`** -> AI Confidence: **99.18%**
367. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/data/LoanScheduleParams.java`** -> AI Confidence: **99.18%**
368. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/mapper/LoanTermVariationsMapper.java`** -> AI Confidence: **99.18%**
369. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/rescheduleloan/service/LoanRescheduleRequestReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
370. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanApplicationTransitionValidator.java`** -> AI Confidence: **99.18%**
371. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanChargeValidator.java`** -> AI Confidence: **99.18%**
372. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/VariableLoanScheduleFromApiJsonValidator.java`** -> AI Confidence: **99.18%**
373. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanArrearsAgingServiceImpl.java`** -> AI Confidence: **99.18%**
374. **`fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanStatusChangeHistoryListener.java`** -> AI Confidence: **99.18%**
375. **`fineract-mix/src/main/java/org/apache/fineract/mix/service/MixTaxonomyReadServiceImpl.java`** -> AI Confidence: **99.18%**
376. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/api/LoanBuyDownFeeApiResource.java`** -> AI Confidence: **99.18%**
377. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/impl/ProgressiveTransactionCtx.java`** -> AI Confidence: **99.18%**
378. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/data/LoanSchedulePlan.java`** -> AI Confidence: **99.18%**
379. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/mapper/LoanConfigurationDetailsMapper.java`** -> AI Confidence: **99.18%**
380. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/repository/CustomizedLoanCapitalizedIncomeBalanceRepositoryImpl.java`** -> AI Confidence: **99.18%**
381. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/BuyDownFeeReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
382. **`fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/CapitalizedIncomeBalanceReadServiceImpl.java`** -> AI Confidence: **99.18%**
383. **`fineract-provider/src/main/java/org/apache/fineract/accounting/common/AccountingDropdownReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
384. **`fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/api/JournalEntriesApiResource.java`** -> AI Confidence: **99.18%**
385. **`fineract-provider/src/main/java/org/apache/fineract/adhocquery/service/AdHocDataValidator.java`** -> AI Confidence: **99.18%**
386. **`fineract-provider/src/main/java/org/apache/fineract/adhocquery/service/AdHocWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
387. **`fineract-provider/src/main/java/org/apache/fineract/batch/command/internal/AdjustChargeByChargeExternalIdCommandStrategy.java`** -> AI Confidence: **99.18%**
388. **`fineract-provider/src/main/java/org/apache/fineract/batch/command/internal/AdjustChargeCommandStrategy.java`** -> AI Confidence: **99.18%**
389. **`fineract-provider/src/main/java/org/apache/fineract/batch/command/internal/GetChargeByChargeExternalIdCommandStrategy.java`** -> AI Confidence: **99.18%**
390. **`fineract-provider/src/main/java/org/apache/fineract/batch/command/internal/GetChargeByIdCommandStrategy.java`** -> AI Confidence: **99.18%**
391. **`fineract-provider/src/main/java/org/apache/fineract/batch/command/internal/GetLoanTransactionByExternalIdCommandStrategy.java`** -> AI Confidence: **99.18%**
392. **`fineract-provider/src/main/java/org/apache/fineract/batch/command/internal/GetLoanTransactionByIdCommandStrategy.java`** -> AI Confidence: **99.18%**
393. **`fineract-provider/src/main/java/org/apache/fineract/batch/command/internal/GetSavingsAccountByIdCommandStrategy.java`** -> AI Confidence: **99.18%**
394. **`fineract-provider/src/main/java/org/apache/fineract/cob/api/LoanCOBCatchUpApiResource.java`** -> AI Confidence: **99.18%**
395. **`fineract-provider/src/main/java/org/apache/fineract/cob/loan/AbstractLoanItemWriter.java`** -> AI Confidence: **99.18%**
396. **`fineract-provider/src/main/java/org/apache/fineract/cob/loan/AddPeriodicAccrualEntriesBusinessStep.java`** -> AI Confidence: **99.18%**
397. **`fineract-provider/src/main/java/org/apache/fineract/cob/loan/CheckLoanRepaymentDueBusinessStep.java`** -> AI Confidence: **99.18%**
398. **`fineract-provider/src/main/java/org/apache/fineract/cob/loan/RetrieveAllNonClosedLoanIdServiceImpl.java`** -> AI Confidence: **99.18%**
399. **`fineract-provider/src/main/java/org/apache/fineract/cob/savings/RetrieveSavingsIdServiceImpl.java`** -> AI Confidence: **99.18%**
400. **`fineract-provider/src/main/java/org/apache/fineract/cob/service/InlineLoanCOBExecutorServiceImpl.java`** -> AI Confidence: **99.18%**
401. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/accountnumberformat/api/AccountNumberFormatsApiResource.java`** -> AI Confidence: **99.18%**
402. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/accountnumberformat/service/AccountNumberFormatWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
403. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/center/CenterImportHandler.java`** -> AI Confidence: **99.18%**
404. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/chartofaccounts/ChartOfAccountsImportHandler.java`** -> AI Confidence: **99.18%**
405. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/guarantor/GuarantorImportHandler.java`** -> AI Confidence: **99.18%**
406. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/recurringdeposit/RecurringDepositTransactionImportHandler.java`** -> AI Confidence: **99.18%**
407. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/users/UserImportHandler.java`** -> AI Confidence: **99.18%**
408. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/centers/CentersWorkbookPopulator.java`** -> AI Confidence: **99.18%**
409. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/fixeddeposits/FixedDepositWorkbookPopulator.java`** -> AI Confidence: **99.18%**
410. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/loan/LoanWorkbookPopulator.java`** -> AI Confidence: **99.18%**
411. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/recurringdeposit/RecurringDepositWorkbookPopulator.java`** -> AI Confidence: **99.18%**
412. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/populator/savings/SavingsWorkbookPopulator.java`** -> AI Confidence: **99.18%**
413. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/service/BulkImportWorkbookPopulatorServiceImpl.java`** -> AI Confidence: **99.18%**
414. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/email/data/EmailConfigurationValidator.java`** -> AI Confidence: **99.18%**
415. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/email/service/EmailCampaignDomainServiceImpl.java`** -> AI Confidence: **99.18%**
416. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/email/service/EmailMessageJobEmailServiceImpl.java`** -> AI Confidence: **99.18%**
417. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/email/service/EmailReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
418. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/email/service/EmailWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
419. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/sms/service/SmsCampaignReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
420. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/codes/serialization/CodeValueCommandFromApiJsonDeserializer.java`** -> AI Confidence: **99.18%**
421. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/codes/service/CodeValueWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
422. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/codes/service/CodeWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
423. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/configuration/api/GlobalConfigurationApiResource.java`** -> AI Confidence: **99.18%**
424. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/configuration/serialization/ExternalServicesPropertiesCommandFromApiJsonDeserializer.java`** -> AI Confidence: **99.18%**
425. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/configuration/service/GlobalConfigurationPropertyUpdateService.java`** -> AI Confidence: **99.18%**
426. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/config/SpringConfig.java`** -> AI Confidence: **99.18%**
427. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/diagnostics/performance/sampling/output/SamplingScheduler.java`** -> AI Confidence: **99.18%**
428. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/diagnostics/security/SecurityFilterChainDiagnostics.java`** -> AI Confidence: **99.18%**
429. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/domain/AuditorAwareImpl.java`** -> AI Confidence: **99.18%**
430. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/jersey/JerseyJacksonConverterConfig.java`** -> AI Confidence: **99.18%**
431. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/jersey/serializer/JacksonLocalDateBeanSerializerModifier.java`** -> AI Confidence: **99.18%**
432. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/service/GmailBackedPlatformEmailService.java`** -> AI Confidence: **99.18%**
433. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/service/migration/TenantDatabaseStateVerifier.java`** -> AI Confidence: **99.18%**
434. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/creditbureau/service/CreditReportWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
435. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/creditbureau/service/ThitsaWorksCreditBureauIntegrationWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
436. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/service/DatatableReadServiceImpl.java`** -> AI Confidence: **99.18%**
437. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/entityaccess/service/FineractEntityAccessUtil.java`** -> AI Confidence: **99.18%**
438. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/hooks/processor/ElasticSearchHookProcessor.java`** -> AI Confidence: **99.18%**
439. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/hooks/processor/WebHookProcessor.java`** -> AI Confidence: **99.18%**
440. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/jobs/api/SchedulerApiResource.java`** -> AI Confidence: **99.18%**
441. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/jobs/config/FineractDataFieldMaxValueIncrementerFactory.java`** -> AI Confidence: **99.18%**
442. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/jobs/filter/LoanCOBApiFilter.java`** -> AI Confidence: **99.18%**
443. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/jobs/service/JobSchedulerServiceImpl.java`** -> AI Confidence: **99.18%**
444. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/jobs/service/JobStarter.java`** -> AI Confidence: **99.18%**
445. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/jobs/service/StuckJobListener.java`** -> AI Confidence: **99.18%**
446. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/jobs/service/aggregationjob/JournalEntryAggregationJobExecutionDecider.java`** -> AI Confidence: **99.18%**
447. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/reportmailingjob/service/ReportMailingJobWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
448. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/security/service/TwoFactorServiceImpl.java`** -> AI Confidence: **99.18%**
449. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/sms/service/SmsWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
450. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/springbatch/InputChannelInterceptor.java`** -> AI Confidence: **99.18%**
451. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/springbatch/messagehandler/StepExecutionRequestHandler.java`** -> AI Confidence: **99.18%**
452. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/survey/service/ReadSurveyServiceImpl.java`** -> AI Confidence: **99.18%**
453. **`fineract-provider/src/main/java/org/apache/fineract/infrastructure/survey/service/WriteLikelihoodServiceImpl.java`** -> AI Confidence: **99.18%**
454. **`fineract-provider/src/main/java/org/apache/fineract/interoperation/data/InteropTransactionData.java`** -> AI Confidence: **99.18%**
455. **`fineract-provider/src/main/java/org/apache/fineract/interoperation/data/InteropTransactionsData.java`** -> AI Confidence: **99.18%**
456. **`fineract-provider/src/main/java/org/apache/fineract/interoperation/data/MoneyData.java`** -> AI Confidence: **99.18%**
457. **`fineract-provider/src/main/java/org/apache/fineract/interoperation/service/InteropServiceImpl.java`** -> AI Confidence: **99.18%**
458. **`fineract-provider/src/main/java/org/apache/fineract/notification/service/NotificationReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
459. **`fineract-provider/src/main/java/org/apache/fineract/organisation/holiday/service/HolidayReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
460. **`fineract-provider/src/main/java/org/apache/fineract/organisation/holiday/service/HolidayWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
461. **`fineract-provider/src/main/java/org/apache/fineract/organisation/office/serialization/OfficeCommandFromApiJsonDeserializer.java`** -> AI Confidence: **99.18%**
462. **`fineract-provider/src/main/java/org/apache/fineract/organisation/office/service/OfficeReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
463. **`fineract-provider/src/main/java/org/apache/fineract/organisation/office/service/OfficeWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
464. **`fineract-provider/src/main/java/org/apache/fineract/organisation/provisioning/domain/ProvisioningCriteria.java`** -> AI Confidence: **99.18%**
465. **`fineract-provider/src/main/java/org/apache/fineract/organisation/provisioning/serialization/ProvisioningCriteriaDefinitionJsonDeserializer.java`** -> AI Confidence: **99.18%**
466. **`fineract-provider/src/main/java/org/apache/fineract/organisation/provisioning/service/ProvisioningCategoryWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
467. **`fineract-provider/src/main/java/org/apache/fineract/organisation/provisioning/service/ProvisioningCriteriaAssembler.java`** -> AI Confidence: **99.18%**
468. **`fineract-provider/src/main/java/org/apache/fineract/organisation/provisioning/service/ProvisioningCriteriaWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
469. **`fineract-provider/src/main/java/org/apache/fineract/organisation/staff/service/StaffWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
470. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/account/api/StandingInstructionApiResource.java`** -> AI Confidence: **99.18%**
471. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/accountdetails/service/AccountDetailsReadPlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
472. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/address/domain/Address.java`** -> AI Confidence: **99.18%**
473. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/address/service/AddressReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
474. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/calendar/domain/CalendarInstanceRepository.java`** -> AI Confidence: **99.18%**
475. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/charge/service/ChargeReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
476. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/api/ClientChargesApiResource.java`** -> AI Confidence: **99.18%**
477. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/api/ClientIdentifiersApiResource.java`** -> AI Confidence: **99.18%**
478. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/api/ClientTransactionsApiResource.java`** -> AI Confidence: **99.18%**
479. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/domain/ClientCharge.java`** -> AI Confidence: **99.18%**
480. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/service/ClientChargeReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
481. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/service/ClientChargeWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
482. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/service/ClientIdentifierWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
483. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/service/ClientTransactionReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
484. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/client/service/ClientTransactionWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
485. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/collateral/service/CollateralAssembler.java`** -> AI Confidence: **99.18%**
486. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/collateralmanagement/service/ClientCollateralManagementWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
487. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/collateralmanagement/service/LoanCollateralAssembler.java`** -> AI Confidence: **99.18%**
488. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/collectionsheet/data/CollectionSheetTransactionDataValidator.java`** -> AI Confidence: **99.18%**
489. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/collectionsheet/service/CollectionSheetReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
490. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/fund/service/FundWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
491. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/group/service/CenterReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
492. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/group/service/GroupReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
493. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/group/service/GroupRolesWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
494. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/interestratechart/data/InterestRateChartDataValidator.java`** -> AI Confidence: **99.18%**
495. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/api/LoansApiResource.java`** -> AI Confidence: **99.18%**
496. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/api/request/ReAgePreviewRequest.java`** -> AI Confidence: **99.18%**
497. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/guarantor/domain/GuarantorFundingDetails.java`** -> AI Confidence: **99.18%**
498. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/guarantor/service/GuarantorReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
499. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/jobs/addperiodicaccrualentriesforloanswithincomepostedastransactions/AddPeriodicAccrualEntriesForLoansTasklet.java`** -> AI Confidence: **99.18%**
500. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/jobs/applyholidaystoloans/ApplyHolidaysToLoansTasklet.java`** -> AI Confidence: **99.18%**
501. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/jobs/generateloanlossprovisioning/GenerateLoanlossProvisioningTasklet.java`** -> AI Confidence: **99.18%**
502. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/service/LoanScheduleHistoryReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
503. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/rescheduleloan/service/LoanReschedulePreviewPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
504. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanScheduleValidator.java`** -> AI Confidence: **99.18%**
505. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanAccountServiceImpl.java`** -> AI Confidence: **99.18%**
506. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanBuyDownFeeAmortizationEventService.java`** -> AI Confidence: **99.18%**
507. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanPointInTimeServiceImpl.java`** -> AI Confidence: **99.18%**
508. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanProductGuaranteeDetailsUpdateUtil.java`** -> AI Confidence: **99.18%**
509. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanProductInterestRecalculationDetailsAssembler.java`** -> AI Confidence: **99.18%**
510. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanProductVariableInstallmentConfigUpdateUtil.java`** -> AI Confidence: **99.18%**
511. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
512. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/reaging/LoanReAgingService.java`** -> AI Confidence: **99.18%**
513. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/reaging/LoanReAgingValidator.java`** -> AI Confidence: **99.18%**
514. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/api/LoanProductsApiResource.java`** -> AI Confidence: **99.18%**
515. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/productmix/service/ProductMixWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
516. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/service/LoanProductReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
517. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/meeting/service/MeetingReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
518. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/rate/service/RateAssembler.java`** -> AI Confidence: **99.18%**
519. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/rate/service/RateWriteServiceImpl.java`** -> AI Confidence: **99.18%**
520. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/repaymentwithpostdatedchecks/service/RepaymentWithPostDatedChecksWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
521. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/api/SavingsAccountTransactionsApiResource.java`** -> AI Confidence: **99.18%**
522. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/api/SavingsProductsApiResource.java`** -> AI Confidence: **99.18%**
523. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/domain/SavingsAccountDomainServiceJpa.java`** -> AI Confidence: **99.18%**
524. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/jobs/transferinteresttosavings/TransferInterestToSavingsTasklet.java`** -> AI Confidence: **99.18%**
525. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/DepositAccountOnHoldTransactionReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
526. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/DepositAccountWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
527. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/FixedDepositProductWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
528. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/RecurringDepositProductWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
529. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/SavingsAccountTemplateReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
530. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/SavingsProductWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
531. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/self/account/data/SelfAccountTransferDataValidator.java`** -> AI Confidence: **99.18%**
532. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/self/account/service/SelfBeneficiariesTPTWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
533. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/self/client/data/SelfClientDataValidator.java`** -> AI Confidence: **99.18%**
534. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/self/device/service/DeviceRegistrationWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
535. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/self/loanaccount/data/SelfLoansDataValidator.java`** -> AI Confidence: **99.18%**
536. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/domain/ShareAccountCharge.java`** -> AI Confidence: **99.18%**
537. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/service/ShareAccountCommandsServiceImpl.java`** -> AI Confidence: **99.18%**
538. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/service/ShareAccountDividendReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
539. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/service/ShareAccountReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
540. **`fineract-provider/src/main/java/org/apache/fineract/portfolio/shareproducts/service/ShareProductWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
541. **`fineract-provider/src/main/java/org/apache/fineract/spm/util/LookupTableMapper.java`** -> AI Confidence: **99.18%**
542. **`fineract-provider/src/main/java/org/apache/fineract/template/api/TemplatesApiResource.java`** -> AI Confidence: **99.18%**
543. **`fineract-provider/src/main/java/org/apache/fineract/template/domain/Template.java`** -> AI Confidence: **99.18%**
544. **`fineract-provider/src/main/java/org/apache/fineract/template/service/JpaTemplateDomainService.java`** -> AI Confidence: **99.18%**
545. **`fineract-provider/src/main/java/org/apache/fineract/useradministration/api/PermissionsApiResource.java`** -> AI Confidence: **99.18%**
546. **`fineract-provider/src/main/java/org/apache/fineract/useradministration/api/RolesApiResource.java`** -> AI Confidence: **99.18%**
547. **`fineract-provider/src/main/java/org/apache/fineract/useradministration/service/PermissionWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
548. **`fineract-provider/src/main/java/org/apache/fineract/useradministration/service/RoleWritePlatformServiceJpaRepositoryImpl.java`** -> AI Confidence: **99.18%**
549. **`fineract-provider/src/test/java/org/apache/fineract/batch/command/CommandStrategyProviderTest.java`** -> AI Confidence: **99.18%**
550. **`fineract-provider/src/test/java/org/apache/fineract/batch/command/internal/LoanStateTransistionsByExternalIdCommandStrategyTest.java`** -> AI Confidence: **99.18%**
551. **`fineract-provider/src/test/java/org/apache/fineract/batch/command/internal/ModifyLoanApplicationByExternalIdCommandStrategyTest.java`** -> AI Confidence: **99.18%**
552. **`fineract-provider/src/test/java/org/apache/fineract/batch/command/internal/ModifyLoanApplicationCommandStrategyTest.java`** -> AI Confidence: **99.18%**
553. **`fineract-provider/src/test/java/org/apache/fineract/cob/loan/CheckDueInstallmentsBusinessStepTest.java`** -> AI Confidence: **99.18%**
554. **`fineract-provider/src/test/java/org/apache/fineract/cob/loan/RetrieveAllNonClosedLoanIdServiceImplTest.java`** -> AI Confidence: **99.18%**
555. **`fineract-provider/src/test/java/org/apache/fineract/cob/service/InlineLoanCOBExecutorServiceImplTest.java`** -> AI Confidence: **99.18%**
556. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/core/LiquibaseStepDefinitions.java`** -> AI Confidence: **99.18%**
557. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/dataqueries/service/DatatableReadServiceImplTest.java`** -> AI Confidence: **99.18%**
558. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/event/external/jobs/SendAsynchronousEventsTaskletTest.java`** -> AI Confidence: **99.18%**
559. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/event/external/service/ExternalEventConfigurationValidationServiceTest.java`** -> AI Confidence: **99.18%**
560. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/event/external/service/serialization/mapper/support/AvroDateTimeMapperTest.java`** -> AI Confidence: **99.18%**
561. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/event/external/service/serialization/serializer/document/DocumentBusinessEventSerializerTest.java`** -> AI Confidence: **99.18%**
562. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/event/external/service/serialization/serializer/loan/LoanAccountDelinquencyRangeEventSerializerTest.java`** -> AI Confidence: **99.18%**
563. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/event/external/service/serialization/serializer/loan/LoanRepaymentBusinessEventSerializerTest.java`** -> AI Confidence: **99.18%**
564. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/event/external/service/serialization/serializer/loan/LoanTransactionBusinessEventSerializerTest.java`** -> AI Confidence: **99.18%**
565. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/jobs/handler/ExecuteJobCommandHandlerTest.java`** -> AI Confidence: **99.18%**
566. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/jobs/service/JobStarterTest.java`** -> AI Confidence: **99.18%**
567. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/jobs/service/aggregationjob/listener/JournalEntryAggregationJobListenerTest.java`** -> AI Confidence: **99.18%**
568. **`fineract-provider/src/test/java/org/apache/fineract/infrastructure/jobs/service/aggregationjob/services/JournalEntryAggregationWriterServiceImplTest.java`** -> AI Confidence: **99.18%**
569. **`fineract-provider/src/test/java/org/apache/fineract/portfolio/delinquency/validator/DelinquencyActionParseAndValidatorTest.java`** -> AI Confidence: **99.18%**
570. **`fineract-provider/src/test/java/org/apache/fineract/portfolio/loanaccount/domain/DefaultLoanLifecycleStateMachineTest.java`** -> AI Confidence: **99.18%**
571. **`fineract-provider/src/test/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/impl/DuePenFeeIntPriInAdvancePriPenFeeIntLoanRepaymentScheduleTransactionProcessorTest.java`** -> AI Confidence: **99.18%**
572. **`fineract-provider/src/test/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/impl/DuePenIntPriFeeInAdvancePenIntPriFeeLoanRepaymentScheduleTransactionProcessorTest.java`** -> AI Confidence: **99.18%**
573. **`fineract-provider/src/test/java/org/apache/fineract/portfolio/loanaccount/service/LoanAccrualActivityProcessingServiceImplTest.java`** -> AI Confidence: **99.18%**
574. **`fineract-provider/src/test/java/org/apache/fineract/portfolio/loanaccount/service/LoanStatusChangeHistoryListenerTest.java`** -> AI Confidence: **99.18%**
575. **`fineract-provider/src/test/java/org/apache/fineract/portfolio/loanproduct/LoanProductValidationStepDefinitions.java`** -> AI Confidence: **99.18%**
576. **`fineract-provider/src/test/java/org/apache/fineract/useradministration/service/AppUserWritePlatformServiceJpaRepositoryImplTest.java`** -> AI Confidence: **99.18%**
577. **`fineract-rates/src/main/java/org/apache/fineract/portfolio/floatingrates/service/FloatingRateWritePlatformServiceImpl.java`** -> AI Confidence: **99.18%**
578. **`fineract-rates/src/main/java/org/apache/fineract/portfolio/floatingrates/service/FloatingRatesReadPlatformServiceImpl.java`** -> AI Confidence: **99.18%**
579. **`fineract-report/src/main/java/org/apache/fineract/infrastructure/report/provider/ReportingProcessServiceProvider.java`** -> AI Confidence: **99.18%**
580. **`fineract-savings/src/main/java/org/apache/fineract/interoperation/data/InteropAccountData.java`** -> AI Confidence: **99.18%**
581. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/interestratechart/domain/InterestRateChartSlab.java`** -> AI Confidence: **99.18%**
582. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/data/DepositAccountData.java`** -> AI Confidence: **99.18%**
583. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain/DepositAccountInterestRateChart.java`** -> AI Confidence: **99.18%**
584. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain/DepositPreClosureDetail.java`** -> AI Confidence: **99.18%**
585. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain/SavingsAccountChargePaidBy.java`** -> AI Confidence: **99.18%**
586. **`fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain/SavingsProductAssembler.java`** -> AI Confidence: **99.18%**
587. **`fineract-security/src/main/java/org/apache/fineract/infrastructure/security/filter/TenantAwareAuthenticationFilter.java`** -> AI Confidence: **99.18%**
588. **`fineract-security/src/main/java/org/apache/fineract/infrastructure/security/filter/TwoFactorAuthenticationFilter.java`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `16` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `64285` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/domain/AdvancedPaymentAllocationsValidator.java` (JAVA) -> Cumulative Risk: **695.7**
- **Archetype:** `file_cluster_4` (Distance: 11.535 IQR)
- **Magnitude:** 206.9 | **LOC:** 139 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.8641%)
- **Heaviest Functions:** `validate` (Impact: 20.2), `validatePairOfOrderAndPaymentAllocationT` (Impact: 12.1), `validateAllocationType` (Impact: 11.6)

### 2. `scripts/split-features.sh` (SHELL) -> Cumulative Risk: **673.61**
- **Archetype:** `file_cluster_4` (Distance: 13.505 IQR)
- **Magnitude:** 15.75 | **LOC:** 149 | **CtrlFlow:** 73.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9889%), Safety Score (99.591%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 67.6), `__global_context__` (Impact: 15.8), `Anonymous_Block` (Impact: 5.2)

### 3. `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepaymentScheduleInstallment.java` (JAVA) -> Cumulative Risk: **663.6**
- **Archetype:** `file_cluster_0` (Distance: 13.177 IQR)
- **Magnitude:** 1247.82 | **LOC:** 1303 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 30.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9939%), State Flux (99.9389%)
- **Heaviest Functions:** `getPaymentFunction` (Impact: 66.4), `resetDerivedComponents` (Impact: 27.7), `reduceAdvanceAndLateTotalsForRepaymentPe` (Impact: 17.1)

### 4. `fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/service/ProductToGLAccountMappingReadPlatformServiceImpl.java` (JAVA) -> Cumulative Risk: **662.84**
- **Archetype:** `file_cluster_13` (Distance: 13.295 IQR)
- **Magnitude:** 591.9 | **LOC:** 488 | **CtrlFlow:** 70.5% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.1499%), Cognitive Load (96.7148%)
- **Heaviest Functions:** `fetchAccountMappingDetailsForLoanProduct` (Impact: 98.3), `setAccrualPeriodicSavingsProductToGLAcco` (Impact: 34.5), `setCashSavingsProductToGLAccountMaps` (Impact: 26.1)

### 5. `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/api/jersey/PageableParamProvider.java` (JAVA) -> Cumulative Risk: **660.72**
- **Archetype:** `file_cluster_4` (Distance: 11.891 IQR)
- **Magnitude:** 148.94 | **LOC:** 108 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9999%), Cognitive Load (95.6988%)
- **Heaviest Functions:** `apply` (Impact: 58.9), `getPriority` (Impact: 2.5)

### 6. `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanChargeService.java` (JAVA) -> Cumulative Risk: **658.3**
- **Archetype:** `file_cluster_13` (Distance: 12.658 IQR)
- **Magnitude:** 1566.4 | **LOC:** 965 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9487%), Safety Score (96.258%), Tech Debt (87.3291%)
- **Heaviest Functions:** `createChargeAppliedTransaction` (Impact: 553.2), `update` (Impact: 69.8), `update` (Impact: 65.4)

### 7. `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/ProgressiveLoanInterestRefundServiceImpl.java` (JAVA) -> Cumulative Risk: **649.75**
- **Archetype:** `file_cluster_13` (Distance: 12.226 IQR)
- **Magnitude:** 118.7 | **LOC:** 157 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9987%), State Flux (99.8641%), Safety Score (94.5979%)
- **Heaviest Functions:** `totalInterestByTransactions` (Impact: 20.9), `simulateRepaymentForDisbursements` (Impact: 15.3), `recalculateTotalInterest` (Impact: 12.0)

### 8. `fineract-command/src/main/java/org/apache/fineract/command/implementation/DefaultCommandAuditor.java` (JAVA) -> Cumulative Risk: **624.29**
- **Archetype:** `file_cluster_13` (Distance: 11.006 IQR)
- **Magnitude:** 123.74 | **LOC:** 185 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.3601%), Safety Score (92.7766%)
- **Heaviest Functions:** `onStartup` (Impact: 12.6), `getResponseByIdempotencyKey` (Impact: 11.3), `fallback` (Impact: 7.4)

### 9. `fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/diagnostics/performance/sampling/core/AbstractSamplingService.java` (JAVA) -> Cumulative Risk: **617.5**
- **Archetype:** `file_cluster_4` (Distance: 11.288 IQR)
- **Magnitude:** 61.58 | **LOC:** 77 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9985%), State Flux (98.136%)
- **Heaviest Functions:** `sample` (Impact: 9.3), `AbstractSamplingService` (Impact: 4.8), `reset` (Impact: 2.5)

### 10. `fineract-core/src/main/java/org/apache/fineract/commands/service/SynchronousCommandProcessingService.java` (JAVA) -> Cumulative Risk: **603.7**
- **Archetype:** `file_cluster_13` (Distance: 11.594 IQR)
- **Magnitude:** 374.68 | **LOC:** 397 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9953%), State Flux (95.4978%), Concurrency (89.8989%)
- **Heaviest Functions:** `findCommandHandler` (Impact: 123.4), `publishHookEvent` (Impact: 34.7), `executeCommand` (Impact: 29.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepository.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.886 IQR)
- **Top Global Matches:** file_cluster_0: 9.886, file_cluster_16: 10.031, file_cluster_8: 10.153
- **Magnitude:** 7305.13 | **LOC:** 289 | **CtrlFlow:** 85.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (26.4695%), Tech Debt (15.3095%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 18`, `args: 47`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 36`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `import: 14`
* *Defense:* `safety: 3`, `doc: 2`, `test: 3`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.44
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` org.springframework.data.jpa.repository.JpaSpecificationExecutor, java.time.LocalDate, java.util.List, java.util.Collection, org.springframework.data.jpa.repository.Query, org.apache.fineract.portfolio.accountdetails.domain.AccountType, org.springframework.data.repository.query.Param, org.springframework.data.jpa.repository.JpaRepository...
  * `Imported By (In-Degree: 43):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanTransactionRepository.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.189 IQR)
- **Top Global Matches:** file_cluster_8: 9.189, file_cluster_0: 9.609, file_cluster_16: 9.787
- **Magnitude:** 5438.89 | **LOC:** 485 | **CtrlFlow:** 75.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (9.4403%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 23`, `args: 53`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 1`, `import: 17`
* *Defense:* `safety: 7`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.324
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` java.util.Set, org.apache.fineract.portfolio.loanaccount.data.CumulativeIncomeFromIncomePosting, java.time.LocalDate, org.springframework.data.jpa.repository.JpaSpecificationExecutor, org.apache.fineract.portfolio.loanaccount.data.UnpaidChargeData, java.util.List, java.util.Collection, org.apache.fineract.portfolio.loanaccount.data.LoanScheduleDelinquencyData...
  * `Imported By (In-Degree: 57):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/resources/keystore.jks` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_8` (Drift: 12.116 IQR)
- **Top Global Matches:** file_cluster_8: 12.116, file_cluster_0: 12.477, file_cluster_13: 12.583
- **Magnitude:** 3104.66 | **LOC:** 5294 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 38.5%
- **Risk Profile:** Cognitive Load (13.1312%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkPeriod` (Impact: 148.3)
  * `checkPeriod` (Impact: 146.2)
  * `checkPeriod` (Impact: 121.2)
  * `verifyAllPeriods` (Impact: 85.3)
  * `checkPeriod` (Impact: 67.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 686`, `structural_boundaries: 278`, `args: 155`, `func_start: 1126`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 138`, `state_mutation: 182`, `duplicate_logic: 48`, `orphaned_logic: 78`
* *Architecture:* `api: 104`, `import: 49`
* *Defense:* `safety: 1`, `doc: 7`, `test: 878`, `immutability_locks: 594`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` org.junit.jupiter.api.Assertions, org.junit.jupiter.api.Test, java.math.RoundingMode, org.apache.fineract.portfolio.loanaccount.domain.LoanRepaymentScheduleInstallment, org.apache.fineract.portfolio.loanproduct.calc.data.PeriodDueDetails, org.apache.fineract.organisation.monetary.domain.MonetaryCurrency, org.apache.fineract.organisation.monetary.domain.MoneyHelper, org.apache.fineract.portfolio.loanproduct.calc.data.EqualAmortizationValues...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/AbstractCumulativeLoanScheduleGenerator.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.154 IQR)
- **Top Global Matches:** file_cluster_8: 12.154, file_cluster_13: 12.266, file_cluster_16: 12.35
- **Magnitude:** 2712.68 | **LOC:** 2861 | **CtrlFlow:** 74.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (43.2837%), Tech Debt (99.8442%)
**Top Internal Functions/Classes:**
  * `applyEarlyPaymentStrategy` (Impact: 494.7)
  * `rescheduleNextInstallments` (Impact: 299.8)
  * `applyLoanTermVariations` (Impact: 136.2)
  * `generate` (Impact: 135.7)
  * `handleRecalculationForNonDueDateTransact` (Impact: 128.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 498`, `structural_boundaries: 172`, `args: 73`, `func_start: 109`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 74`, `state_mutation: 342`, `dead_code: 7`, `planned_debt: 4`, `duplicate_logic: 47`, `orphaned_logic: 11`
* *Architecture:* `api: 9`, `import: 46`
* *Defense:* `safety: 2`, `doc: 44`, `immutability_locks: 312`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` org.apache.fineract.organisation.workingdays.domain.RepaymentRescheduleType, org.apache.fineract.portfolio.loanaccount.data.DisbursementData, java.util.Collection, org.apache.fineract.portfolio.loanaccount.loanschedule.exception.MultiDisbursementEmiAmountException, org.apache.fineract.portfolio.loanaccount.domain.LoanRepaymentScheduleInstallment, org.apache.fineract.portfolio.loanaccount.domain.LoanRepaymentScheduleProcessingWrapper.isBeforePeriod, org.apache.fineract.organisation.monetary.domain.MonetaryCurrency, java.util.HashMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanStepDef.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.401 IQR)
- **Top Global Matches:** file_cluster_0: 13.401, file_cluster_8: 13.441, file_cluster_13: 13.444
- **Magnitude:** 2628.84 | **LOC:** 5999 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (22.3279%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fetchValuesOfRepaymentSchedule` (Impact: 88.5)
  * `fetchValuesOfTransaction` (Impact: 67.3)
  * `fetchValuesOfFilteredTransaction` (Impact: 56.5)
  * `getActualValuesList` (Impact: 43.5)
  * `fetchValuesOfBuyDownFees` (Impact: 41.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 519`, `structural_boundaries: 672`, `args: 552`, `func_start: 286`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 228`, `state_mutation: 371`, `duplicate_logic: 36`, `orphaned_logic: 168`
* *Architecture:* `api: 223`, `import: 154`
* *Defense:* `safety: 46`, `doc: 2`, `test: 247`, `immutability_locks: 628`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 61):` org.apache.fineract.client.models.GetLoansLoanIdTimeline, org.apache.fineract.test.data.TransactionProcessingStrategyCode.ADVANCED_PAYMENT_ALLOCATION, org.apache.fineract.test.messaging.event.loan.transaction.LoanAdjustTransactionBusinessEvent, org.apache.fineract.client.models.PostClientsResponse, java.util.Collection, org.apache.fineract.client.models.GetLoansLoanIdLoanChargePaidByData, java.util.HashMap, org.apache.fineract.avro.loan.v1.LoanChargePaidByDataV1...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-core/src/main/java/org/apache/fineract/commands/service/CommandWrapperBuilder.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.769 IQR)
- **Top Global Matches:** file_cluster_8: 9.769, file_cluster_7: 10.462, file_cluster_1: 10.726
- **Magnitude:** 2436.76 | **LOC:** 3905 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 22.2%
- **Risk Profile:** Cognitive Load (6.4812%), Tech Debt (32.7384%)
**Top Internal Functions/Classes:**
  * `commonDatatableSettings` (Impact: 6.5)
  * `payLoanCharge` (Impact: 5.8)
  * `recoverFromGuarantor` (Impact: 5.3)
  * `activateClient` (Impact: 5.3)
  * `closeClient` (Impact: 5.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 478`, `args: 455`, `func_start: 458`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 108`, `state_mutation: 7`, `planned_debt: 1`, `duplicate_logic: 16`
* *Architecture:* `api: 865`, `import: 13`
* *Defense:* `doc: 2`, `immutability_locks: 462`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.613
  * `Choke Point (Betweenness):` 4.6e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` java.util.Set, org.apache.fineract.useradministration.service.AppUserConstants.REPEAT_PASSWORD, org.apache.fineract.infrastructure.core.domain.ExternalId, java.util.HashSet, org.apache.fineract.useradministration.service.AppUserConstants.PASSWORD, org.apache.fineract.commands.domain.CommandWrapper, org.apache.fineract.portfolio.self.pockets.api.PocketApiConstants, org.apache.fineract.useradministration.api.PasswordPreferencesApiConstants...
  * `Imported By (In-Degree: 126):` (Excluded from Brief to save tokens)

### `fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/domain/ProductToGLAccountMappingRepository.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.488 IQR)
- **Top Global Matches:** file_cluster_0: 9.488, file_cluster_16: 9.585, file_cluster_8: 9.65
- **Magnitude:** 1958.44 | **LOC:** 114 | **CtrlFlow:** 83.7% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (14.7918%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 8`, `args: 20`, `func_start: 3`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` org.springframework.data.jpa.repository.JpaSpecificationExecutor, java.util.List, org.springframework.data.jpa.repository.Query, org.springframework.data.repository.query.Param, org.springframework.data.jpa.repository.JpaRepository
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/loans/LoanTransactionHelper.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.932 IQR)
- **Top Global Matches:** file_cluster_0: 11.932, file_cluster_11: 12.085, file_cluster_13: 12.121
- **Magnitude:** 1789.56 | **LOC:** 3220 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (21.868%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `printRepaymentSchedule` (Impact: 11.7)
  * `evaluateLastLoanTransactionData` (Impact: 9.7)
  * `undoDisbursal` (Impact: 9.4)
    * *Intent:* // TODO: Rewrite to use fineract-client instead! // Example: org.apache.fineract.integrationtests.co...
  * `undoLastDisbursal` (Impact: 9.4)
  * `noAccrualTransactionForRepayment` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 560`, `args: 361`, `func_start: 372`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 113`, `state_mutation: 268`, `planned_debt: 180`, `duplicate_logic: 204`
* *Architecture:* `io: 4`, `api: 440`, `import: 91`
* *Defense:* `doc: 7`, `test: 25`, `immutability_locks: 890`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.791
  * `Choke Point (Betweenness):` 0.000416 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` org.apache.fineract.client.models.GetLoansLoanIdSummary, java.util.HashMap, org.apache.fineract.client.models.GetLoansApprovalTemplateResponse, org.junit.jupiter.api.Assertions.assertEquals, org.junit.jupiter.api.Assertions.assertThrows, org.apache.fineract.client.models.GetDelinquencyActionsResponse, org.apache.fineract.client.models.DeleteLoansLoanIdChargesChargeIdResponse, org.apache.fineract.client.models.GetLoansLoanIdTransactionsResponse...
  * `Imported By (In-Degree: 119):` (Excluded from Brief to save tokens)

### `fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain/SavingsAccountRepository.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.973 IQR)
- **Top Global Matches:** file_cluster_8: 8.973, file_cluster_0: 9.084, file_cluster_13: 9.1
- **Magnitude:** 1615.24 | **LOC:** 151 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (14.431%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 18`, `args: 20`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 1`, `import: 14`
* *Defense:* `doc: 1`, `test: 1`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` org.springframework.data.jpa.repository.JpaSpecificationExecutor, java.time.LocalDate, java.util.List, java.util.Collection, org.apache.fineract.portfolio.savings.data.SavingsAccrualData, org.springframework.data.domain.Page, org.springframework.data.jpa.repository.Query, org.springframework.data.domain.Pageable...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanChargeService.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.658 IQR)
- **Top Global Matches:** file_cluster_13: 12.658, file_cluster_8: 12.841, file_cluster_11: 12.887
- **Magnitude:** 1566.4 | **LOC:** 965 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (81.4701%), Tech Debt (87.3291%)
**Top Internal Functions/Classes:**
  * `createChargeAppliedTransaction` (Impact: 553.2)
  * `update` (Impact: 69.8)
  * `update` (Impact: 65.4)
  * `populateDerivedFields` (Impact: 56.3)
  * `update` (Impact: 53.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 103`, `args: 54`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 277`, `dead_code: 1`, `duplicate_logic: 14`
* *Architecture:* `api: 30`, `import: 38`
* *Defense:* `doc: 3`, `immutability_locks: 160`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.089
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` org.apache.fineract.portfolio.loanaccount.domain.LoanOverdueInstallmentCharge, java.util.Collection, org.apache.fineract.portfolio.charge.domain.ChargePaymentMode, org.apache.fineract.portfolio.loanaccount.domain.LoanRepaymentScheduleInstallment, org.apache.fineract.portfolio.charge.domain.Charge, org.apache.fineract.organisation.monetary.domain.MonetaryCurrency, java.util.HashMap, java.util.LinkedHashMap...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/AccrualBasedAccountingProcessorForLoan.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.733 IQR)
- **Top Global Matches:** file_cluster_8: 11.733, file_cluster_13: 12.113, file_cluster_7: 12.151
- **Magnitude:** 1557.16 | **LOC:** 2198 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (34.1683%), Tech Debt (99.9777%)
**Top Internal Functions/Classes:**
  * `createJournalEntriesForRepaymentWhenLoan` (Impact: 154.3)
  * `createJournalEntriesForLoan` (Impact: 97.9)
  * `createJournalEntriesForLoanRepayments` (Impact: 92.8)
  * `createJournalEntriesForLoanCapitalizedIn` (Impact: 63.6)
    * *Intent:* // create debit entries
  * `createJournalEntriesForLoanBuyDownFeeAmo` (Impact: 63.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 457`, `structural_boundaries: 108`, `args: 48`, `func_start: 72`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 295`, `planned_debt: 2`, `duplicate_logic: 50`
* *Architecture:* `api: 9`, `import: 24`
* *Defense:* `doc: 23`, `immutability_locks: 378`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` org.apache.fineract.accounting.journalentry.data.AdvancedMappingtDTO, java.util.LinkedHashMap, org.apache.fineract.accounting.closure.domain.GLClosure, org.apache.fineract.accounting.journalentry.data.ChargePaymentDTO, org.apache.fineract.portfolio.loanaccount.data.LoanTransactionEnumData, org.apache.fineract.accounting.glaccount.domain.GLAccount, org.apache.fineract.infrastructure.core.service.MathUtil, java.math.BigDecimal...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/serialization/LoanProductDataValidator.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.306 IQR)
- **Top Global Matches:** file_cluster_8: 10.306, file_cluster_7: 10.872, file_cluster_13: 10.922
- **Magnitude:** 1546.82 | **LOC:** 3019 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (15.9614%), Tech Debt (85.309%)
**Top Internal Functions/Classes:**
  * `validateForCreate` (Impact: 301.1)
  * `validateForUpdate` (Impact: 258.6)
  * `validateInterestRecalculationParams` (Impact: 108.5)
  * `validatePartialPeriodSupport` (Impact: 73.3)
  * `validateBorrowerCycleVariations` (Impact: 70.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 543`, `structural_boundaries: 146`, `args: 38`, `func_start: 89`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 178`, `state_mutation: 16`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 29`
* *Architecture:* `api: 55`, `import: 60`
* *Defense:* `doc: 2`, `immutability_locks: 353`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.077
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 42):` org.apache.fineract.portfolio.loanproduct.exception.EqualAmortizationUnsupportedFeatureException, org.apache.fineract.portfolio.loanaccount.domain.LoanChargeOffBehaviour, com.google.gson.JsonArray, java.util.HashMap, java.util.Locale, org.apache.fineract.infrastructure.core.exception.GeneralPlatformDomainRuleException, org.apache.fineract.portfolio.calendar.service.CalendarUtils, org.apache.fineract.portfolio.common.domain.PeriodFrequencyType...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/LoanApplicationTerms.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.727 IQR)
- **Top Global Matches:** file_cluster_8: 10.727, file_cluster_13: 11.155, file_cluster_7: 11.208
- **Magnitude:** 1526.18 | **LOC:** 2272 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (16.4434%), Tech Debt (45.0817%)
**Top Internal Functions/Classes:**
  * `periodicInterestRate` (Impact: 133.6)
  * `calculateTotalInterestForPeriod` (Impact: 87.2)
  * `calculateTotalPrincipalForPeriod` (Impact: 52.9)
  * `getPeriodEndDate` (Impact: 50.1)
  * `calculatePeriodsBetweenDates` (Impact: 43.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 341`, `structural_boundaries: 253`, `args: 189`, `func_start: 192`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 39`, `planned_debt: 6`, `duplicate_logic: 10`
* *Architecture:* `api: 241`, `import: 48`
* *Defense:* `safety: 1`, `doc: 10`, `immutability_locks: 351`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.313
  * `Choke Point (Betweenness):` 0.001205 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 39):` org.apache.fineract.portfolio.loanaccount.data.DisbursementData, org.apache.fineract.portfolio.calendar.domain.Calendar, org.apache.fineract.portfolio.loanaccount.domain.LoanChargeOffBehaviour, org.apache.fineract.organisation.monetary.domain.MoneyHelper, org.apache.fineract.portfolio.calendar.service.CalendarUtils, org.apache.fineract.portfolio.common.domain.PeriodFrequencyType, org.apache.fineract.portfolio.loanaccount.domain.LoanBuyDownFeeStrategy, org.apache.fineract.portfolio.common.domain.DaysInMonthType...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/Loan.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.846 IQR)
- **Top Global Matches:** file_cluster_0: 11.846, file_cluster_13: 12.009, file_cluster_8: 12.136
- **Magnitude:** 1470.94 | **LOC:** 1848 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 36.4%
- **Risk Profile:** Cognitive Load (19.2272%), Tech Debt (29.885%)
**Top Internal Functions/Classes:**
  * `Loan` (Impact: 73.3)
  * `findLastAssignmentHistoryRecord` (Impact: 20.4)
  * `getNextPossibleRepaymentDateForReschedul` (Impact: 18.9)
  * `hasMonetaryActivityAfter` (Impact: 17.8)
  * `getDisbursedAmount` (Impact: 16.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 309`, `args: 262`, `func_start: 214`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 98`, `state_mutation: 107`, `planned_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 353`, `import: 64`
* *Defense:* `safety: 7`, `doc: 18`, `immutability_locks: 193`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.329
  * `Choke Point (Betweenness):` 0.004479 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` jakarta.persistence.Column, org.apache.fineract.portfolio.rate.domain.Rate, lombok.Setter, java.util.Collection, org.apache.fineract.portfolio.group.domain.Group, jakarta.persistence.Convert, org.apache.fineract.portfolio.charge.domain.Charge, jakarta.persistence.Entity...
  * `Imported By (In-Degree: 315):` (Excluded from Brief to save tokens)

### `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/BatchHelper.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.383 IQR)
- **Top Global Matches:** file_cluster_13: 14.383, file_cluster_11: 14.602, file_cluster_7: 14.638
- **Magnitude:** 1333.44 | **LOC:** 1758 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.842%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `applyLoanRequest` (Impact: 62.3)
  * `applyLoanRequestWithClientIdAndExternalI` (Impact: 45.8)
  * `transitionLoanStateByExternalId` (Impact: 30.0)
    * *Intent:* /** * Creates and returns a Batch Request with given requestId and reference * * @param requestId * ...
  * `createActiveClientRequest` (Impact: 23.6)
    * *Intent:* /** * Returns a list of BatchResponse with query parameter enclosing transaction set to true by post...
  * `createClientRequest` (Impact: 21.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 166`, `args: 83`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 537`, `planned_debt: 7`, `duplicate_logic: 23`
* *Architecture:* `api: 123`, `import: 23`
* *Defense:* `doc: 330`, `test: 3`, `immutability_locks: 328`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.098
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` org.junit.jupiter.api.Assertions, java.security.SecureRandom, org.slf4j.Logger, java.util.HashMap, com.google.gson.Gson, org.apache.fineract.batch.command.internal.CreateTransactionLoanCommandStrategy, java.util.UUID, org.apache.fineract.integrationtests.common.savings.SavingsTransactionData...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculator.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.259 IQR)
- **Top Global Matches:** file_cluster_17: 13.259, file_cluster_11: 13.279, file_cluster_13: 13.316
- **Magnitude:** 1295.5 | **LOC:** 2137 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 37.9%
- **Risk Profile:** Cognitive Load (20.3132%), Tech Debt (99.7473%)
**Top Internal Functions/Classes:**
  * `calculateRateFactorPerPeriodForInterest` (Impact: 43.4)
  * `calculateRateFactorPerPeriod` (Impact: 31.8)
  * `calculatePeriodRatio` (Impact: 31.1)
  * `attachTemporaryScheduleModelReAgedPeriod` (Impact: 29.7)
  * `calculateEMIOnActualModelWithFlatInteres` (Impact: 29.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 213`, `args: 264`, `func_start: 175`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 207`, `dead_code: 5`, `planned_debt: 7`, `duplicate_logic: 35`
* *Architecture:* `api: 60`, `concurrency: 42`, `import: 48`
* *Defense:* `safety: 43`, `doc: 59`, `immutability_locks: 323`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` org.apache.fineract.portfolio.loanaccount.domain.LoanRepaymentScheduleInstallment, org.apache.fineract.portfolio.loanproduct.calc.data.PeriodDueDetails, org.apache.fineract.organisation.monetary.domain.MonetaryCurrency, org.apache.fineract.portfolio.common.domain.PeriodFrequencyType, org.apache.fineract.portfolio.loanproduct.calc.data.EqualAmortizationValues, org.apache.fineract.portfolio.common.domain.DaysInMonthType, org.apache.fineract.portfolio.loanaccount.loanschedule.domain.LoanScheduleModelRepaymentPeriod, org.springframework.util.CollectionUtils...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/helper/ErrorMessageHelper.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.642 IQR)
- **Top Global Matches:** file_cluster_8: 10.642, file_cluster_16: 11.013, file_cluster_13: 11.106
- **Magnitude:** 1281.98 | **LOC:** 1002 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (21.043%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wrongValueInLineInJournalEntries` (Impact: 13.8)
  * `wrongValueInLineInJournalEntry` (Impact: 13.7)
  * `wrongAmountInDeferredCapitalizedIncome` (Impact: 12.4)
  * `wrongValueInLineInRepaymentSchedule` (Impact: 11.5)
  * `wrongValueInLineInTransactionsTab` (Impact: 11.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 186`, `args: 192`, `func_start: 168`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 17`, `duplicate_logic: 19`
* *Architecture:* `api: 315`, `import: 12`
* *Defense:* `doc: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` java.util.Set, java.time.LocalDate, java.util.List, org.apache.fineract.client.models.BatchResponse, org.apache.fineract.client.models.LoanAccountLockResponseDTO, java.time.format.DateTimeFormatter, java.io.IOException, java.util.stream.Collectors...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanApplicationValidator.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.566 IQR)
- **Top Global Matches:** file_cluster_8: 10.566, file_cluster_13: 10.81, file_cluster_7: 11.128
- **Magnitude:** 1279.74 | **LOC:** 2267 | **CtrlFlow:** 59.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (15.8842%), Tech Debt (99.4531%)
**Top Internal Functions/Classes:**
  * `validateForCreate` (Impact: 250.9)
  * `validateForModify` (Impact: 218.1)
  * `validateClientOrGroup` (Impact: 171.8)
  * `validateApproval` (Impact: 46.9)
  * `validateLoanMultiDisbursementDate` (Impact: 42.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 369`, `structural_boundaries: 250`, `args: 51`, `func_start: 78`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 105`, `state_mutation: 30`, `dead_code: 3`, `planned_debt: 6`, `duplicate_logic: 39`
* *Architecture:* `api: 26`, `import: 113`
* *Defense:* `doc: 3`, `sync_locks: 1`, `immutability_locks: 295`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 95):` org.apache.fineract.portfolio.loanaccount.data.DisbursementData, java.util.Collection, org.apache.fineract.portfolio.group.domain.Group, org.apache.fineract.infrastructure.core.exception.UnsupportedParameterException, org.apache.fineract.infrastructure.entityaccess.exception.NotOfficeSpecificProductException, org.apache.fineract.organisation.monetary.domain.MoneyHelper, org.apache.fineract.portfolio.loanaccount.exception.LoanApplicationDateException, org.springframework.util.CollectionUtils...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepaymentScheduleInstallment.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.177 IQR)
- **Top Global Matches:** file_cluster_0: 13.177, file_cluster_13: 13.223, file_cluster_8: 13.276
- **Magnitude:** 1247.82 | **LOC:** 1303 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (92.455%), Tech Debt (99.9939%)
**Top Internal Functions/Classes:**
  * `getPaymentFunction` (Impact: 66.4)
  * `resetDerivedComponents` (Impact: 27.7)
  * `reduceAdvanceAndLateTotalsForRepaymentPe` (Impact: 17.1)
  * `compareToByFromDueDate` (Impact: 11.4)
  * `isOutstandingBalanceNotZero` (Impact: 10.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 186`, `args: 175`, `func_start: 201`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 375`, `planned_debt: 1`, `duplicate_logic: 34`
* *Architecture:* `api: 173`, `import: 27`
* *Defense:* `doc: 2`, `immutability_locks: 235`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.048
  * `Choke Point (Betweenness):` 0.000132 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` jakarta.persistence.Column, lombok.Setter, jakarta.persistence.Entity, org.apache.fineract.organisation.monetary.domain.MonetaryCurrency, org.apache.fineract.organisation.monetary.domain.MoneyHelper, org.apache.fineract.portfolio.repaymentwithpostdatedchecks.domain.PostDatedChecks, org.apache.fineract.infrastructure.core.service.MathUtil, org.apache.fineract.organisation.monetary.domain.Money...
  * `Imported By (In-Degree: 85):` (Excluded from Brief to save tokens)

### `fineract-core/src/main/java/org/apache/fineract/portfolio/savings/service/SavingsEnumerations.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.8 IQR)
- **Top Global Matches:** file_cluster_8: 9.8, file_cluster_13: 10.197, file_cluster_7: 10.399
- **Magnitude:** 1181.78 | **LOC:** 841 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (33.2229%), Tech Debt (99.9996%)
**Top Internal Functions/Classes:**
  * `transactionType` (Impact: 168.5)
  * `status` (Impact: 96.7)
  * `subStatus` (Impact: 63.4)
  * `compoundingInterestPeriodType` (Impact: 55.6)
  * `interestPostingPeriodType` (Impact: 54.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 359`, `structural_boundaries: 179`, `args: 58`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`, `duplicate_logic: 43`
* *Architecture:* `api: 58`, `import: 21`
* *Defense:* `doc: 1`, `immutability_locks: 94`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.271
  * `Choke Point (Betweenness):` 0.000177 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` org.apache.fineract.portfolio.savings.SavingsPeriodFrequencyType, org.apache.fineract.portfolio.savings.DepositAccountOnClosureType, org.apache.fineract.accounting.common.AccountingEnumerations, org.apache.fineract.portfolio.savings.RecurringDepositType, org.apache.fineract.portfolio.savings.PreClosurePenalInterestOnType, org.apache.fineract.portfolio.savings.data.SavingsAccountTransactionEnumData, org.apache.fineract.portfolio.savings.SavingsCompoundingInterestPeriodType, org.apache.fineract.portfolio.savings.DepositAccountType...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/impl/AdvancedPaymentScheduleTransactionProcessor.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.273 IQR)
- **Top Global Matches:** file_cluster_13: 13.273, file_cluster_17: 13.308, file_cluster_11: 13.353
- **Magnitude:** 1181.7 | **LOC:** 4170 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 23.9%
- **Risk Profile:** Cognitive Load (47.2368%), Tech Debt (88.8144%)
**Top Internal Functions/Classes:**
  * `reprocessProgressiveLoanTransactions` (Impact: 52.5)
  * `liftOutstandingBalances` (Impact: 48.8)
  * `handleCreditBalanceRefund` (Impact: 41.6)
  * `processLatestTransaction` (Impact: 37.9)
  * `updateRepaymentPeriodsAfterAccelerateMat` (Impact: 37.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 238`, `args: 214`, `func_start: 98`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 198`, `dead_code: 5`, `planned_debt: 9`, `duplicate_logic: 16`
* *Architecture:* `api: 46`, `concurrency: 120`, `import: 107`
* *Defense:* `safety: 25`, `doc: 9`, `immutability_locks: 199`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 62):` java.util.HashMap, org.apache.fineract.organisation.monetary.domain.MoneyHelper, org.apache.fineract.portfolio.loanproduct.calc.data.EqualAmortizationValues, org.apache.fineract.portfolio.loanaccount.domain.LoanTermVariations, org.apache.fineract.portfolio.loanaccount.domain.LoanInstallmentCharge, java.util.concurrent.atomic.AtomicInteger, org.apache.fineract.portfolio.loanproduct.domain.FutureInstallmentAllocationRule, org.apache.fineract.portfolio.loanaccount.service.schedule.LoanScheduleComponent...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `integration-tests/src/test/java/org/apache/fineract/integrationtests/ClientLoanIntegrationTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.299 IQR)
- **Top Global Matches:** file_cluster_8: 11.299, file_cluster_13: 11.671, file_cluster_16: 11.848
- **Magnitude:** 1176.88 | **LOC:** 8361 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (10.9278%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `verifyLoanRepaymentScheduleForEqualPrinc` (Impact: 152.3)
  * `verifyLoanRepaymentScheduleForEqualPrinc` (Impact: 137.2)
  * `verifyLoanRepaymentSchedule` (Impact: 62.4)
  * `verifyLoanRepaymentSchedule` (Impact: 26.8)
  * `chargeAdjustmentAccountingValidation` (Impact: 24.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 499`, `args: 128`, `func_start: 235`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 161`, `state_mutation: 151`, `duplicate_logic: 43`, `orphaned_logic: 32`
* *Architecture:* `api: 32`, `import: 100`
* *Defense:* `safety: 22`, `doc: 8`, `test: 874`, `immutability_locks: 454`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` org.apache.fineract.client.models.PostClientsResponse, org.apache.fineract.portfolio.charge.domain.ChargePaymentMode, org.apache.fineract.client.models.GetLoansLoanIdSummary, java.util.HashMap, org.apache.fineract.portfolio.charge.domain.ChargeTimeType, org.junit.jupiter.api.Assertions.assertEquals, org.junit.jupiter.api.Assertions.assertThrows, org.apache.fineract.integrationtests.common.accounting.AccountHelper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/service/DatatableWriteServiceImpl.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.41 IQR)
- **Top Global Matches:** file_cluster_13: 11.41, file_cluster_8: 11.642, file_cluster_0: 11.679
- **Magnitude:** 1130.72 | **LOC:** 1430 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (41.0102%), Tech Debt (99.9686%)
**Top Internal Functions/Classes:**
  * `parseDatatableColumnForUpdate` (Impact: 169.5)
  * `updateDatatable` (Impact: 100.3)
  * `createDatatable` (Impact: 76.3)
  * `createNewDatatableEntry` (Impact: 51.1)
  * `parseDatatableColumnForAdd` (Impact: 49.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 347`, `structural_boundaries: 246`, `args: 66`, `func_start: 89`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 98`, `state_mutation: 82`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 34`
* *Architecture:* `api: 24`, `concurrency: 18`, `import: 95`
* *Defense:* `safety: 38`, `doc: 5`, `test: 2`, `immutability_locks: 265`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` org.springframework.dao.EmptyResultDataAccessException, org.apache.fineract.infrastructure.security.service.PlatformSecurityContext, org.apache.fineract.infrastructure.dataqueries.api.DataTableApiConstant.API_PARAM_COLUMNS, java.util.HashMap, org.apache.fineract.infrastructure.dataqueries.api.DataTableApiConstant.API_PARAM_MULTIROW, org.apache.fineract.infrastructure.dataqueries.api.DataTableApiConstant.API_PARAM_DROPCOLUMNS, org.apache.fineract.portfolio.search.SearchConstants.API_PARAM_DATETIME_FORMAT, org.springframework.lang.NonNull...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/service/LoanScheduleAssembler.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.087 IQR)
- **Top Global Matches:** file_cluster_13: 12.087, file_cluster_8: 12.237, file_cluster_16: 12.617
- **Magnitude:** 1059.94 | **LOC:** 1607 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (61.9641%), Tech Debt (83.3354%)
**Top Internal Functions/Classes:**
  * `assembleLoanApplicationTermsFrom` (Impact: 119.4)
  * `assempleVariableScheduleFrom` (Impact: 117.8)
  * `adjustExistingVariations` (Impact: 108.0)
  * `updateLoanApplicationAttributes` (Impact: 77.8)
  * `deriveFirstRepaymentDate` (Impact: 40.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 188`, `args: 34`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 267`, `planned_debt: 1`, `duplicate_logic: 15`
* *Architecture:* `api: 21`, `import: 121`
* *Defense:* `safety: 3`, `doc: 2`, `immutability_locks: 285`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 97):` org.apache.fineract.portfolio.loanaccount.data.DisbursementData, java.util.Collection, org.apache.fineract.portfolio.loanaccount.domain.LoanOfficerAssignmentHistory, org.apache.fineract.portfolio.group.domain.Group, java.util.HashMap, org.apache.fineract.organisation.monetary.domain.MoneyHelper, org.apache.fineract.portfolio.loanaccount.exception.LoanApplicationDateException, org.apache.fineract.portfolio.loanaccount.domain.LoanTermVariations...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `fineract-charge/src/main/java/org/apache/fineract/portfolio/charge/api/ChargesApiResourceSwagger.java` (JAVA) | Magnitude: 133.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 225, api: 102, doc: 85, decorators: 83
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/organisation/StaffHelper.java` (JAVA) | Magnitude: 113.04 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 104, immutability_locks: 46, structural_boundaries: 32, state_mutation: 32
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/rates/RatesHelper.java` (JAVA) | Magnitude: 46.66 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 57, immutability_locks: 23, structural_boundaries: 21, api: 14
- `fineract-loan-origination/src/main/java/org/apache/fineract/portfolio/loanorigination/api/LoanOriginatorApiResourceSwagger.java` (JAVA) | Magnitude: 44.94 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 70, api: 29, doc: 27, decorators: 26
- `fineract-client/src/main/java/org/apache/fineract/client/services/ImagesApi.java` (JAVA) | Magnitude: 16.46 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, decorators: 10, structural_boundaries: 8, io: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `fineract-core/src/main/java/org/apache/fineract/portfolio/charge/data/ChargeData.java` (JAVA) | Magnitude: 25.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 82, immutability_locks: 46, encapsulation: 42, structural_boundaries: 23
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/domain/FineractEvent.java` (JAVA) | Magnitude: 8.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 7, api: 4, func_start: 3
- `fineract-accounting/src/main/java/org/apache/fineract/accounting/journalentry/domain/JournalEntry.java` (JAVA) | Magnitude: 29.5 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 88, immutability_locks: 33, decorators: 29, structural_boundaries: 23
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/domain/ShareAccountChargePaidBy.java` (JAVA) | Magnitude: 31.84 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 16, api: 14, args: 8
- `fineract-core/src/main/java/org/apache/fineract/portfolio/calendar/service/CalendarUtils.java` (JAVA) | Magnitude: 602.18 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 664, immutability_locks: 214, branch: 145, structural_boundaries: 135

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `fineract-command/src/test/java/org/apache/fineract/command/sample/service/DefaultDummyTenantService.java` (JAVA) | Magnitude: 8.74 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 6, api: 4, args: 2
- `fineract-accounting/src/main/java/org/apache/fineract/accounting/journalentry/domain/JournalEntryRepository.java` (JAVA) | Magnitude: 369.65 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, branch: 10, structural_boundaries: 9, args: 9
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/diagnostics/performance/MeasuringUtil.java` (JAVA) | Magnitude: 17.1 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 12, generics: 7, args: 6
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepositoryWrapper.java` (JAVA) | Magnitude: 122.54 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 212, structural_boundaries: 71, api: 57, args: 51
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/DepositAccountReadPlatformService.java` (JAVA) | Magnitude: 48.12 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, func_start: 12, args: 11, structural_boundaries: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculator.java` (JAVA) | Magnitude: 1295.5 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 1557, immutability_locks: 323, branch: 310, args: 264
- `fineract-core/src/main/java/org/apache/fineract/portfolio/savings/SavingsCompoundingInterestPeriodType.java` (JAVA) | Magnitude: 59.38 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 40, branch: 14, structural_boundaries: 13, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/LoanManualInterestRefundResponseStructureTest.java` (JAVA) | Magnitude: 119.06 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 117, concurrency: 66, structural_boundaries: 42, test: 23
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/LoanContractTerminationTest.java` (JAVA) | Magnitude: 72.82 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 83, concurrency: 42, structural_boundaries: 32, import: 15
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/LoanCapitalizedIncomeTest.java` (JAVA) | Magnitude: 705.0 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1002, concurrency: 414, structural_boundaries: 121, test: 91
- `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/mapper/AdvancedPaymentDataMapper.java` (JAVA) | Magnitude: 30.18 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 18, structural_boundaries: 15, indent_spaces: 11, import: 9
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/database/DatabaseTypeResolver.java` (JAVA) | Magnitude: 47.68 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 18, concurrency: 18, api: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `fineract-security/src/main/java/org/apache/fineract/infrastructure/security/package-info.java` (JAVA) | Magnitude: 10.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 1
- `fineract-provider/src/main/java/org/apache/fineract/infrastructure/gcm/GcmConstants.java` (JAVA) | Magnitude: 43.82 | Delta: **0.152 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 43, doc: 42, api: 41, immutability_locks: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `fineract-core/src/main/java/org/apache/fineract/interoperation/domain/InteropIdentifierType.java` (JAVA) | Magnitude: 31.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, branch: 11, structural_boundaries: 11, args: 8
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/data/LoanRepaymentPastDueData.java` (JAVA) | Magnitude: 16.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: scientific: 6, structural_boundaries: 5, immutability_locks: 5, encapsulation: 5
- `buildSrc/src/main/groovy/org/apache/fineract/gradle/service/EmailService.groovy` (GROOVY) | Magnitude: 32.3 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 12, import: 7, branch: 6
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

- `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/impl/AdvancedPaymentScheduleTransactionProcessor.java` -> Churn: **100.0%** | Cog Load: 47.2368% | Debt: 88.8144%
- `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculator.java` -> Churn: **88.34%** | Cog Load: 20.3132% | Debt: 99.7473%
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanReadPlatformServiceImpl.java` -> Churn: **76.08%** | Cog Load: 14.4858% | Debt: 68.1181%
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanWritePlatformServiceJpaRepositoryImpl.java` -> Churn: **63.73%** | Cog Load: 11.2655% | Debt: 97.4887%
- `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanReAgingStepDef.java` -> Churn: **63.05%** | Cog Load: 73.4351% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepository.java` -> **Adam Saghy** (100.0% isolated ownership) | Magnitude: 7305.13
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/BatchHelper.java` -> **Adam Saghy** (100.0% isolated ownership) | Magnitude: 1333.44
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service/SavingsAccountWritePlatformServiceJpaRepositoryImpl.java` -> **Juan-Pablo-Alvarez** (100.0% isolated ownership) | Magnitude: 841.6
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/LoanCapitalizedIncomeTest.java` -> **Jose Alberto Hernandez** (100.0% isolated ownership) | Magnitude: 705.0
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/shares/ShareAccountIntegrationTests.java` -> **Wilfred Kigenyi** (100.0% isolated ownership) | Magnitude: 647.56

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

- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/api/JsonCommand.java` -> **Severity: 1720.8** (Blast Radius: 17.208 * Doc Risk: 100.0%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/data/CommandProcessingResult.java` -> **Severity: 1457.796** (Blast Radius: 14.731 * Doc Risk: 98.9611%)
- `fineract-provider/src/main/java/org/apache/fineract/spm/domain/Component.java` -> **Severity: 1342.199** (Blast Radius: 13.424 * Doc Risk: 99.985%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/domain/ExternalId.java` -> **Severity: 950.665** (Blast Radius: 22.145 * Doc Risk: 42.9291%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/DateUtils.java` -> **Severity: 753.8** (Blast Radius: 7.538 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
