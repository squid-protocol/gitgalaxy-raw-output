# ARCHITECTURAL_BRIEF: fineract
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/apache/fineract.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 6336 analyzed artifact(s), 527114 LOC.
- **Load-bearing artifact:** `fineract-validation/src/main/java/org/apache/fineract/validation/constraints/LocalDate.java` -- 994 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanWritePlatformServiceJpaRepositoryImpl.java` -- pulls in 207 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `fineract-provider/src/main/resources/keystore.jks` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 6858 |
| Analyzed Artifacts (Scanned) | 6336 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 522 |
| Total LOC | 527114 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 92.4% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5936 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.189 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.114 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 305 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 5814 | 519014 | 91.8% |
| XML | 332 | 0 | 5.2% |
| GROOVY | 48 | 2931 | 0.8% |
| PLAINTEXT | 38 | 1 | 0.6% |
| MARKDOWN | 32 | 0 | 0.5% |
| YAML | 27 | 911 | 0.4% |
| JSON | 19 | 607 | 0.3% |
| SQLITE | 15 | 2424 | 0.2% |
| SHELL | 7 | 298 | 0.1% |
| HTML | 2 | 229 | 0.0% |
| CSS | 1 | 630 | 0.0% |
| BATCH | 1 | 69 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `3.659`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +3.66; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 18%, State Mutators Files 18%, Data / Markup / Trivial 16%, Encapsulated Accessors Files 10%, Large Core Modules (3) 9%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 6265 | 98.9% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 69 | 1.1% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 522*

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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 8.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 33.9 | 33.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 11.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.8 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 21.2 | 10.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 72.9 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.1 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 72.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3091 | 477 | 0 | `integration-tests/src/test/java/org/apache/fineract/integrationtests/ClientLoanIntegrationTest.java` |
| cleanup | 177 | 81 | 0 | `fineract-db/old-schema-files/0001a-mifosplatform-core-ddl-latest.sql` |
| guards | 109301 | 4644 | 39 | `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanStepDef.java` |
| danger | 27845 | 2299 | 9 | `integration-tests/src/test/java/org/apache/fineract/integrationtests/AdvancedPaymentAllocationLoanRepaymentScheduleTest.java` |
| concurrency | 1198 | 332 | 0 | `integration-tests/src/test/java/org/apache/fineract/integrationtests/LoanCapitalizedIncomeTest.java` |
| connectivity | 46396 | 5754 | 13 | `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/api/LoanProductsApiResourceSwagger.java` |
| io | 2138 | 430 | 0 | `scripts/split-tests.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 17 | 6 | 0 | `fineract-provider/src/main/java/org/apache/fineract/infrastructure/springbatch/messagehandler/kafka/KafkaManagerConfig.java` |
| time | 12043 | 1108 | 4 | `fineract-progressive-loan/src/test/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculatorTest.java` |
| serialization | 407 | 168 | 0 | `fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/sms/service/SmsCampaignWritePlatformServiceJpaImpl.java` |
| regex | 74 | 39 | 0 | `scripts/split-features.sh` |
| events | 2695 | 594 | 0 | `integration-tests/src/test/java/org/apache/fineract/integrationtests/LoanDisbursementDetailsIntegrationTest.java` |
| tests | 25913 | 648 | 1 | `integration-tests/src/test/java/org/apache/fineract/integrationtests/ClientLoanIntegrationTest.java` |
| docs | 16379 | 5869 | 2 | `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/api/LoansApiResourceSwagger.java` |
| debt | 1932 | 375 | 0 | `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/loans/LoanTransactionHelper.java` |
| mutation | 133487 | 3759 | 45 | `integration-tests/src/test/java/org/apache/fineract/integrationtests/ClientLoanIntegrationTest.java` |
| dead_code | 7016 | 2082 | 3 | `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanStepDef.java` |
| credential | 13 | 7 | 0 | `fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/data/ReportParameters.java` |
| threat | 368 | 202 | 0 | `fineract-provider/src/test/resources/results/loan.html` |
| ml_ai | 12727 | 874 | 3 | `integration-tests/src/test/java/org/apache/fineract/integrationtests/investor/externalassetowner/InitiateExternalAssetOwnerTransferTest.java` |
| ui | 24 | 4 | 0 | `fineract-provider/src/main/resources/static/legacy-docs/apidocs.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.25**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/split-tests.sh` (Hits: 48)
- `scripts/split-features.sh` (Hits: 35)
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/api/LoansApiResource.java` (Hits: 34)

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

- `validateForUpdate` **(Many-Argument Workhorses)** (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/serialization/LoanProductDataValidator.java`) -> Impact: **258.6** | LOC: 704
- `validateForModify` **(Many-Argument Workhorses)** (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanApplicationValidator.java`) -> Impact: **214.6** | LOC: 621
- `validateForCreate` **(Many-Argument Workhorses)** (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/serialization/LoanProductDataValidator.java`) -> Impact: **188.2** | LOC: 682
- `retrieveTransactionTemplate` **(Many-Argument Workhorses)** (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/api/LoanTransactionsApiResource.java`) -> Impact: **181.9** | LOC: 98
- `parseDatatableColumnForUpdate` **(Many-Argument Workhorses)** (@ `fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/service/DatatableWriteServiceImpl.java`) -> Impact: **169.5** | LOC: 102
- `LoanProduct` **(Many-Argument Workhorses)** (@ `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/domain/LoanProduct.java`) -> Impact: **167.4** | LOC: 149
- `extractLoanScheduleData` **(Many-Argument Workhorses)** (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanRepaymentScheduleService.java`) -> Impact: **155.6** | LOC: 201
- `createJournalEntriesForRepaymentWhenLoanIsChargedOff` **(Many-Argument Workhorses)** (@ `fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/AccrualBasedAccountingProcessorForLoan.java`) -> Impact: **154.5** | LOC: 227
- `rescheduleNextInstallments` **(Many-Argument Workhorses)** (@ `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/AbstractCumulativeLoanScheduleGenerator.java`) -> Impact: **153.3** | LOC: 350
- `readSavings` **(Many-Argument Workhorses)** (@ `fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/recurringdeposit/RecurringDepositImportHandler.java`) -> Impact: **150.0** | LOC: 159

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `integration-tests/src/test/java/org/apache/fineract/integrationtests` | 227 | 23759.1 | 13.21% | 0.0% |
| `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service` | 46 | 9386.2 | 30.96% | 13.24% |
| `fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain` | 40 | 7086.16 | 30.42% | 31.27% |
| `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain` | 73 | 6366.36 | 14.47% | 8.28% |
| `integration-tests/src/test/java/org/apache/fineract/integrationtests/common` | 44 | 6313.28 | 33.87% | 0.0% |
| `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain` | 26 | 5417.6 | 19.42% | 27.02% |
| `fineract-provider/src/main/resources` | 9 | 5038.24 | 0.0% | 0.0% |
| `fineract-core/src/main/java/org/apache/fineract/commands/service` | 8 | 4830.04 | 26.41% | 16.67% |
| `fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service` | 18 | 4696.3 | 21.65% | 11.67% |
| `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan` | 17 | 4260.72 | 18.84% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `buildSrc/src/main/groovy/org/apache/fineract/gradle/service/SubversionService.groovy` -> **100.0%** Exposure
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/database/SqlOperator.java` -> **100.0%** Exposure
- `fineract-core/src/main/java/org/apache/fineract/portfolio/search/SearchConstants.java` -> **100.0%** Exposure
- `fineract-document/src/main/java/org/apache/fineract/infrastructure/documentmanagement/command/DocumentCommand.java` -> **100.0%** Exposure
- `fineract-document/src/main/java/org/apache/fineract/infrastructure/documentmanagement/data/ImageCreateRequest.java` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `scripts/split-features.sh` -> **100.0%** Exposure
- `scripts/split-tests.sh` -> **100.0%** Exposure
- `fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/service/ProductToGLAccountMappingReadPlatformServiceImpl.java` -> **100.0%** Exposure
- `fineract-branch/src/main/java/org/apache/fineract/organisation/teller/util/DateRange.java` -> **100.0%** Exposure
- `fineract-charge/src/main/java/org/apache/fineract/portfolio/charge/service/ChargeEnumerations.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanStepDef.java` -> **207** Orphaned Functions | **0** Duplicates
- `fineract-progressive-loan/src/test/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculatorTest.java` -> **108** Orphaned Functions | **0** Duplicates
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/AdvancedPaymentAllocationLoanRepaymentScheduleTest.java` -> **85** Orphaned Functions | **0** Duplicates
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/ClientLoanIntegrationTest.java` -> **66** Orphaned Functions | **0** Duplicates
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/ClientSavingsIntegrationTest.java` -> **47** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `64309` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `fineract-provider/src/main/resources/keystore.jks` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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

### `fineract-core/src/main/java/org/apache/fineract/commands/service/CommandWrapperBuilder.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 4355.96 | **LOC:** 3905 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **126** in-repo importer(s); it depends on **13**; blast radius 0.612; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Complexity Load (formerly Cognitive Load) (85.6%)
- **Documentation Coverage:** 99.78% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `commonDatatableSettings` **(Stateful Encapsulated Methods)** (Impact: 6.5)
  * `payLoanCharge` **(Compute Cores)** (Impact: 5.8)
  * `saveOrUpdateAttendance` **(Parameter Forwarders)** (Impact: 4.4)
  * `createProductCommand` **(Parameter Forwarders)** (Impact: 4.3)
  * `createAccountCommand` **(Parameter Forwarders)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 412 instances
* *State Mutation (weighted view):* 2818
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 478`, `args: 455`, `func_start: 455`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 108`, `state_mutation: 1994`, `planned_debt: 1`
* *Architecture:* `api: 455`, `import: 13`
* *Defense:* `doc: 2`, `immutability_locks: 462`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.612
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.021161
  * `Imports (Out-Degree: 7):` edu.umd.cs.findbugs.annotations.SuppressFBWarnings, java.util.Arrays, java.util.HashSet, java.util.Set, org.apache.fineract.commands.domain.CommandWrapper, org.apache.fineract.infrastructure.accountnumberformat.service.AccountNumberFormatConstants, org.apache.fineract.infrastructure.core.domain.ExternalId, org.apache.fineract.portfolio.client.api.ClientApiConstants...
  * `Imported By (In-Degree: 126):` (Excluded from Brief to save tokens)

### `fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain/SavingsAccount.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2753.68 | **LOC:** 3904 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **58** in-repo importer(s); it depends on **108**; blast radius 0.981; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (93.8%), Connectivity (formerly Api Exposure) (84.5%), Complexity Load (formerly Cognitive Load) (82.9%)
- **Documentation Coverage:** 98.8662% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `postInterest` **(Many-Argument Workhorses)** (Impact: 111.8)
  * `modifyApplication` **(Many-Argument Workhorses)** (Impact: 97.7)
  * `recalculateDailyBalances` **(Many-Argument Workhorses)** (Impact: 67.1)
  * `calculateInterestUsing` **(Many-Argument Workhorses)** (Impact: 65.5)
    * *Intent:* * All interest calculation based on END-OF-DAY-BALANCE. * * Interest calculation is performed on-the...
  * `payCharge` **(Many-Argument Workhorses)** (Impact: 60.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 241 instances
* *State Mutation (weighted view):* 902
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 591`, `structural_boundaries: 559`, `args: 225`, `func_start: 234`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 177`, `state_mutation: 420`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 2`
* *Architecture:* `api: 253`, `import: 108`
* *Defense:* `doc: 9`, `immutability_locks: 517`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.981
  * `Choke Point (Betweenness):` 0.000467 | `Ripple Effect (Closeness):` 0.015766
  * `Imports (Out-Degree: 54):` com.google.gson.JsonArray, jakarta.persistence.CascadeType, jakarta.persistence.Column, jakarta.persistence.DiscriminatorColumn, jakarta.persistence.DiscriminatorType, jakarta.persistence.DiscriminatorValue, jakarta.persistence.Embedded, jakarta.persistence.Entity...
  * `Imported By (In-Degree: 58):` (Excluded from Brief to save tokens)

### `integration-tests/src/test/java/org/apache/fineract/integrationtests/ClientLoanIntegrationTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2579.02 | **LOC:** 8361 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **100**; blast radius 0.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (76.9%), Complexity Load (formerly Cognitive Load) (48.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.7%), Connectivity (formerly Api Exposure) (3.8%)
- **Documentation Coverage:** 86.802% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `verifyLoanRepaymentScheduleForEqualPrincipalWithGrace` **(Compute Cores)** (Impact: 89.1)
  * `verifyLoanRepaymentScheduleForEqualPrincipal` **(Compute Cores)** (Impact: 80.2)
  * `testLoanCharges_INSTALMENT_FEE` **(I/O & Config Routines)** (Impact: 59.9)
  * `verifyLoanRepaymentSchedule` **(Stateful Encapsulated Methods)** (Impact: 36.6)
  * `verifyLoanRepaymentSchedule` **(Stateful Encapsulated Methods)** (Impact: 26.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 1502
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 854`, `args: 164`, `func_start: 130`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 295`, `state_mutation: 1314`, `unreferenced_by_name: 66`
* *Architecture:* `api: 68`, `import: 100`
* *Defense:* `safety: 26`, `doc: 31`, `test: 992`, `immutability_locks: 694`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` com.google.gson.Gson, com.google.gson.JsonObject, com.google.gson.JsonParser, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, io.restassured.builder.RequestSpecBuilder, io.restassured.builder.ResponseSpecBuilder, io.restassured.http.ContentType, io.restassured.path.json.JsonPath...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/impl/AdvancedPaymentScheduleTransactionProcessor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2464.48 | **LOC:** 4170 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 22.5%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **107**; blast radius 0.203; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (99.0%), Guard Balance (formerly Safety Score) (89.3%), Complexity Load (formerly Cognitive Load) (40.5%)
- **Documentation Coverage:** 98.1595% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processAllocationsHorizontally` **(Many-Argument Workhorses)** (Impact: 105.5)
  * `processPeriodsVertically` **(Many-Argument Workhorses)** (Impact: 94.5)
  * `refundTransactionHorizontally` **(Many-Argument Workhorses)** (Impact: 49.9)
  * `liftOutstandingBalances` **(Many-Argument Workhorses)** (Impact: 42.8)
  * `refundTransactionVertically` **(Many-Argument Workhorses)** (Impact: 41.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 180 instances
* *State Mutation (weighted view):* 780
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 547`, `structural_boundaries: 412`, `args: 516`, `func_start: 139`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 182`, `state_mutation: 420`, `dead_code: 13`, `planned_debt: 9`
* *Architecture:* `api: 27`, `concurrency: 24`, `import: 107`
* *Defense:* `safety: 37`, `doc: 4`, `immutability_locks: 335`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.000173 | `Ripple Effect (Closeness):` 0.005414
  * `Imports (Out-Degree: 62):` jakarta.annotation.Nullable, jakarta.validation.constraints.NotNull, java.math.BigDecimal, java.math.BigDecimal.ZERO, java.math.MathContext, java.math.RoundingMode, java.time.LocalDate, java.time.temporal.ChronoUnit...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/AbstractCumulativeLoanScheduleGenerator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2458.84 | **LOC:** 2861 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **46**; blast radius 0.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.7%)
- **Documentation Coverage:** 75.9494% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rescheduleNextInstallments` **(Many-Argument Workhorses)** (Impact: 153.3)
  * `generate` **(Many-Argument Workhorses)** (Impact: 128.4)
  * `handleRecalculationForNonDueDateTransactions` **(Many-Argument Workhorses)** (Impact: 116.4)
  * `applyLoanTermVariations` **(Many-Argument Workhorses)** (Impact: 110.8)
    * *Intent:* /** * @param loanApplicationTerms * @param scheduleParams * @param previousRepaymentDate * @param sc...
  * `addInterestOnlyRepaymentScheduleForCurrentDate` **(Many-Argument Workhorses)** (Impact: 72.8)
    * *Intent:* /** * Method calculates interest on not paid outstanding principal and interest (if compounding is e...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 238 instances
* *State Mutation (weighted view):* 852
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 477`, `structural_boundaries: 219`, `args: 75`, `func_start: 71`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 77`, `state_mutation: 376`, `dead_code: 9`, `planned_debt: 4`, `unreferenced_by_name: 2`
* *Architecture:* `api: 9`, `import: 46`
* *Defense:* `safety: 2`, `doc: 18`, `immutability_locks: 317`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` jakarta.validation.constraints.NotNull, java.math.BigDecimal, java.math.MathContext, java.time.LocalDate, java.util.ArrayList, java.util.Collection, java.util.HashMap, java.util.HashSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanStepDef.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2445.54 | **LOC:** 5999 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 24.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **154**; blast radius 0.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (91.6%), Guard Balance (formerly Safety Score) (73.5%), Complexity Load (formerly Cognitive Load) (21.6%), Connectivity (formerly Api Exposure) (11.0%)
- **Documentation Coverage:** 99.6296% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetchValuesOfRepaymentSchedule` **(Compute Cores)** (Impact: 88.5)
  * `fetchValuesOfTransaction` **(Stateful Encapsulated Methods)** (Impact: 67.3)
  * `fetchValuesOfFilteredTransaction` **(Stateful Encapsulated Methods)** (Impact: 56.5)
  * `fetchValuesOfLoanTermVariations` **(Stateful Encapsulated Methods)** (Impact: 46.3)
  * `getActualValuesList` **(Stateful Encapsulated Methods)** (Impact: 43.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 133 instances
* *State Mutation (weighted view):* 445
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 521`, `structural_boundaries: 787`, `args: 691`, `func_start: 284`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 269`, `state_mutation: 179`, `dead_code: 2`, `planned_debt: 2`, `unreferenced_by_name: 207`
* *Architecture:* `api: 265`, `import: 154`
* *Defense:* `safety: 61`, `doc: 2`, `test: 281`, `immutability_locks: 868`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 61):` edu.umd.cs.findbugs.annotations.SuppressFBWarnings, io.cucumber.datatable.DataTable, io.cucumber.java.ParameterType, io.cucumber.java.en.And, io.cucumber.java.en.Then, io.cucumber.java.en.When, java.io.IOException, java.math.BigDecimal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/loans/LoanTransactionHelper.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1817.86 | **LOC:** 3220 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **119** in-repo importer(s); it depends on **91**; blast radius 0.791; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (86.8%), Complexity Load (formerly Cognitive Load) (35.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.4%)
- **Documentation Coverage:** 99.4161% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getDisburseLoanAsJSON` **(Stateful Encapsulated Methods)** (Impact: 12.2)
    * *Intent:* // TODO: Rewrite to use fineract-client instead! // Example: org.apache.fineract.integrationtests.co...
  * `checkAccrualTransactionForRepayment` **(Many-Argument Workhorses)** (Impact: 11.2)
    * *Intent:* // TODO: Rewrite to use fineract-client instead! // Example: org.apache.fineract.integrationtests.co...
  * `applyLoanCommand` **(Compute Cores)** (Impact: 11.1)
    * *Intent:* // TODO: Rewrite to use fineract-client instead! // Example: org.apache.fineract.integrationtests.co...
  * `getApproveLoanAsJSON` **(Stateful Encapsulated Methods)** (Impact: 9.9)
    * *Intent:* // TODO: Rewrite to use fineract-client instead! // Example: org.apache.fineract.integrationtests.co...
  * `evaluateLastLoanTransactionData` **(Many-Argument Workhorses)** (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 399
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 561`, `args: 361`, `func_start: 365`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 113`, `state_mutation: 239`, `planned_debt: 180`
* *Architecture:* `io: 4`, `api: 323`, `import: 91`
* *Defense:* `doc: 3`, `test: 25`, `immutability_locks: 890`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.791
  * `Choke Point (Betweenness):` 0.000271 | `Ripple Effect (Closeness):` 0.018878
  * `Imports (Out-Degree: 21):` com.google.common.reflect.TypeToken, com.google.gson.Gson, io.restassured.specification.RequestSpecification, io.restassured.specification.ResponseSpecification, jakarta.ws.rs.core.HttpHeaders, jakarta.ws.rs.core.MediaType, java.io.ByteArrayInputStream, java.io.File...
  * `Imported By (In-Degree: 119):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanWritePlatformServiceJpaRepositoryImpl.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1758.56 | **LOC:** 3659 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **207**; blast radius 0.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (88.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.6%), Mutation Surface (formerly State Flux) (58.2%), Complexity Load (formerly Cognitive Load) (27.2%)
- **Documentation Coverage:** 97.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `disburseLoan` **(Many-Argument Workhorses)** (Impact: 69.0)
  * `applyMeetingDateChanges` **(Many-Argument Workhorses)** (Impact: 45.1)
  * `makeManualInterestRefund` **(Many-Argument Workhorses)** (Impact: 40.1)
  * `close` **(Many-Argument Workhorses)** (Impact: 39.7)
  * `chargebackLoanTransaction` **(Many-Argument Workhorses)** (Impact: 34.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 128 instances
* *State Mutation (weighted view):* 506
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 440`, `structural_boundaries: 537`, `args: 113`, `func_start: 94`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 187`, `state_mutation: 250`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `api: 48`, `import: 207`
* *Defense:* `safety: 4`, `doc: 4`, `immutability_locks: 596`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000158
  * `Imports (Out-Degree: 174):` com.google.common.collect.Lists, com.google.gson.JsonArray, com.google.gson.JsonElement, com.google.gson.JsonObject, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, io.github.resilience4j.retry.annotation.Retry, java.math.BigDecimal, java.time.LocalDate...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/serialization/LoanProductDataValidator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1757.72 | **LOC:** 3019 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **60**; blast radius 0.077; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (90.1%), Mutation Surface (formerly State Flux) (80.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (36.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateForUpdate` **(Many-Argument Workhorses)** (Impact: 258.6)
  * `validateForCreate` **(Many-Argument Workhorses)** (Impact: 188.2)
  * `validateInterestRecalculationParams` **(Many-Argument Workhorses)** (Impact: 108.5)
  * `validatePartialPeriodSupport` **(Many-Argument Workhorses)** (Impact: 73.3)
  * `validateBorrowerCycleVariations` **(Many-Argument Workhorses)** (Impact: 70.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 137 instances
* *State Mutation (weighted view):* 421
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 539`, `structural_boundaries: 146`, `args: 38`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 178`, `state_mutation: 147`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 51`, `import: 60`
* *Defense:* `doc: 2`, `immutability_locks: 353`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.077
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.000777
  * `Imports (Out-Degree: 42):` com.google.gson.JsonArray, com.google.gson.JsonElement, com.google.gson.JsonObject, com.google.gson.reflect.TypeToken, java.lang.reflect.Type, java.math.BigDecimal, java.util.ArrayList, java.util.Arrays...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/LoanApplicationTerms.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1748.78 | **LOC:** 2272 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 22.2%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **48**; blast radius 0.313; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (91.8%), Complexity Load (formerly Cognitive Load) (88.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.8406% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `periodicInterestRate` **(Many-Argument Workhorses)** (Impact: 96.8)
  * `LoanApplicationTerms` **(Many-Argument Workhorses)** (Impact: 69.9)
  * `calculateTotalInterestForPeriod` **(Many-Argument Workhorses)** (Impact: 69.2)
  * `calculateTotalPrincipalForPeriod` **(Many-Argument Workhorses)** (Impact: 38.2)
  * `calculatePeriodsBetweenDates` **(Many-Argument Workhorses)** (Impact: 34.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 132 instances
* *State Mutation (weighted view):* 604
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 314`, `args: 189`, `func_start: 189`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 340`, `planned_debt: 6`
* *Architecture:* `api: 158`, `import: 48`
* *Defense:* `safety: 1`, `doc: 9`, `immutability_locks: 351`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.313
  * `Choke Point (Betweenness):` 0.000889 | `Ripple Effect (Closeness):` 0.041093
  * `Imports (Out-Degree: 39):` jakarta.validation.constraints.NotNull, java.math.BigDecimal, java.math.MathContext, java.time.LocalDate, java.time.temporal.ChronoUnit, java.util.ArrayList, java.util.HashSet, java.util.List...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/AccrualBasedAccountingProcessorForLoan.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1574.66 | **LOC:** 2198 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **24**; blast radius 0.079; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.4%), Guard Balance (formerly Safety Score) (85.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (53.1%)
- **Documentation Coverage:** 88.3721% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createJournalEntriesForRepaymentWhenLoanIsChargedOff` **(Many-Argument Workhorses)** (Impact: 154.5)
  * `createJournalEntriesForLoanRepayments` **(Many-Argument Workhorses)** (Impact: 93.1)
  * `createJournalEntriesForLoanCapitalizedIncomeAmortization` **(Many-Argument Workhorses)** (Impact: 63.6)
  * `createJournalEntriesForLoanBuyDownFeeAmortization` **(Many-Argument Workhorses)** (Impact: 63.6)
  * `createJournalEntriesForChargeback` **(Many-Argument Workhorses)** (Impact: 55.0)
    * *Intent:* /** * Handle chargeback journal entry creation * * @param loanDTO * @param loanTransactionDTO * @par...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 145 instances
* *State Mutation (weighted view):* 436
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 454`, `structural_boundaries: 109`, `args: 48`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 146`, `planned_debt: 2`
* *Architecture:* `api: 3`, `import: 24`
* *Defense:* `doc: 11`, `immutability_locks: 378`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000158
  * `Imports (Out-Degree: 14):` java.math.BigDecimal, java.time.LocalDate, java.util.ArrayList, java.util.LinkedHashMap, java.util.List, java.util.Map, java.util.Objects, lombok.RequiredArgsConstructor...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `fineract-progressive-loan/src/test/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculatorTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1497.26 | **LOC:** 5294 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **49**; blast radius 0.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.2%), Guard Balance (formerly Safety Score) (41.6%), Complexity Load (formerly Cognitive Load) (14.2%), Connectivity (formerly Api Exposure) (8.7%)
- **Documentation Coverage:** 94.8052% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_balance_correction_on0215_disbursedAmt100_dayInYears360_daysInMonth30_repayEvery1Month` **(I/O & Config Routines)** (Impact: 14.5)
    * *Intent:* /** * This test case tests a period early and late repayment with balance correction */
  * `test_emi_calculator_performance` **(Annotated & Test Methods)** (Impact: 13.6)
  * `test_two_reschedules_disbursedAmt100_dayInYears360_daysInMonth30_repayEvery1Month` **(I/O & Config Routines)** (Impact: 13.2)
  * `test_reschedule_disbursedAmt100_dayInYears360_daysInMonth30_repayEvery1Month` **(I/O & Config Routines)** (Impact: 13.1)
  * `test_reschedule_partial_period_disbursedAmt100_dayInYears360_daysInMonth30_repayEvery1Month` **(Annotated & Test Methods)** (Impact: 13.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 235
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 668`, `structural_boundaries: 278`, `args: 155`, `func_start: 133`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 138`, `state_mutation: 211`, `unreferenced_by_name: 108`
* *Architecture:* `api: 104`, `import: 49`
* *Defense:* `safety: 1`, `doc: 7`, `test: 878`, `immutability_locks: 594`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` java.math.BigDecimal, java.math.BigDecimal.ZERO, java.math.MathContext, java.math.RoundingMode, java.time.LocalDate, java.util.ArrayList, java.util.List, java.util.stream.IntStream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/BatchHelper.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1344.64 | **LOC:** 1758 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **23**; blast radius 0.098; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Connectivity (formerly Api Exposure) (71.6%), Complexity Load (formerly Cognitive Load) (39.8%)
- **Documentation Coverage:** 13.7255% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `applyLoanRequest` **(Many-Argument Workhorses)** (Impact: 62.3)
    * *Intent:* * given requestId and reference. * * @param requestId * the request ID * @param reference * the refe...
  * `applyLoanRequestWithClientIdAndExternalId` **(Compute Cores)** (Impact: 45.8)
    * *Intent:* /** * Creates and returns a {@link org.apache.fineract.batch.command.internal.ApplyLoanCommandStrate...
  * `transitionLoanStateByExternalId` **(Compute Cores)** (Impact: 30.0)
    * *Intent:* * {@link org.apache.fineract.batch.command.internal.LoanStateTransistionsByExternalIdCommandStrategy...
  * `createActiveClientRequest` **(Compute Cores)** (Impact: 23.6)
    * *Intent:* /** * Creates and returns a {@link org.apache.fineract.batch.command.internal.CreateClientCommandStr...
  * `createClientRequest` **(Compute Cores)** (Impact: 21.9)
    * *Intent:* /** * Creates and returns a {@link org.apache.fineract.batch.command.internal.CreateClientCommandStr...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 178 instances
* *State Mutation (weighted view):* 600
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 166`, `args: 83`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 244`, `planned_debt: 7`
* *Architecture:* `api: 75`, `import: 23`
* *Defense:* `doc: 68`, `test: 3`, `immutability_locks: 328`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.098
  * `Choke Point (Betweenness):` 9.4e-05 | `Ripple Effect (Closeness):` 0.001913
  * `Imports (Out-Degree: 7):` com.google.gson.Gson, com.google.gson.reflect.TypeToken, io.restassured.specification.RequestSpecification, io.restassured.specification.ResponseSpecification, jakarta.ws.rs.HttpMethod, java.security.SecureRandom, java.time.LocalDate, java.time.format.DateTimeFormatter...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/service/LoanScheduleAssembler.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1218.54 | **LOC:** 1607 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 14.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **121**; blast radius 0.075; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.2%), Guard Balance (formerly Safety Score) (95.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assembleLoanApplicationTermsFrom` **(Many-Argument Workhorses)** (Impact: 116.4)
  * `assempleVariableScheduleFrom` **(Many-Argument Workhorses)** (Impact: 109.4)
  * `adjustExistingVariations` **(Many-Argument Workhorses)** (Impact: 90.0)
  * `updateLoanApplicationAttributes` **(Many-Argument Workhorses)** (Impact: 77.8)
  * `deriveFirstRepaymentDate` **(Many-Argument Workhorses)** (Impact: 40.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 145 instances
* *State Mutation (weighted view):* 511
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 206`, `args: 34`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 221`, `planned_debt: 1`
* *Architecture:* `api: 13`, `import: 121`
* *Defense:* `safety: 3`, `doc: 2`, `immutability_locks: 285`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.000474
  * `Imports (Out-Degree: 97):` com.google.gson.JsonArray, com.google.gson.JsonElement, com.google.gson.JsonObject, java.math.BigDecimal, java.math.MathContext, java.time.LocalDate, java.time.temporal.ChronoField, java.util.ArrayList...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1144.42 | **LOC:** 2137 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 40.7%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **48**; blast radius 0.085; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (89.7%), Guard Balance (formerly Safety Score) (78.7%), Mutation Surface (formerly State Flux) (64.0%), Complexity Load (formerly Cognitive Load) (26.1%)
- **Documentation Coverage:** 77.6119% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `calculateRateFactorPerPeriodForInterest` **(Many-Argument Workhorses)** (Impact: 43.4)
  * `calculateRateFactorPerPeriod` **(Many-Argument Workhorses)** (Impact: 31.8)
    * *Intent:* /** * Calculate Rate Factor for an exact Period */
  * `calculatePeriodRatio` **(Many-Argument Workhorses)** (Impact: 31.1)
  * `attachTemporaryScheduleModelReAgedPeriodsToExistingModel` **(Many-Argument Workhorses)** (Impact: 29.7)
    * *Intent:* /** * * Attaching re-aged repayment periods of the new temporary model to existing model repayment p...
  * `payPrincipal` **(Many-Argument Workhorses)** (Impact: 23.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 288
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 218`, `args: 266`, `func_start: 101`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 150`, `dead_code: 5`, `planned_debt: 7`
* *Architecture:* `api: 35`, `concurrency: 7`, `import: 48`
* *Defense:* `safety: 23`, `doc: 26`, `immutability_locks: 335`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.000361
  * `Imports (Out-Degree: 29):` jakarta.annotation.Nonnull, jakarta.validation.constraints.NotNull, java.math.BigDecimal, java.math.BigDecimal.ZERO, java.math.MathContext, java.time.LocalDate, java.time.Year, java.time.temporal.ChronoUnit...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanChargeService.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1094.26 | **LOC:** 965 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **38**; blast radius 0.089; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.7%), Complexity Load (formerly Cognitive Load) (82.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 92.7273% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Many-Argument Workhorses)** (Impact: 61.3)
  * `update` **(Many-Argument Workhorses)** (Impact: 57.5)
  * `populateDerivedFields` **(Many-Argument Workhorses)** (Impact: 49.0)
  * `update` **(Many-Argument Workhorses)** (Impact: 41.9)
  * `create` **(Many-Argument Workhorses)** (Impact: 40.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 131 instances
* *State Mutation (weighted view):* 432
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 127`, `args: 55`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 170`, `dead_code: 1`
* *Architecture:* `api: 21`, `import: 38`
* *Defense:* `doc: 3`, `immutability_locks: 166`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.089
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.004058
  * `Imports (Out-Degree: 28):` java.math.BigDecimal, java.time.LocalDate, java.util.ArrayList, java.util.Collection, java.util.HashMap, java.util.HashSet, java.util.LinkedHashMap, java.util.List...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/Loan.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1087.74 | **LOC:** 1848 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **315** in-repo importer(s); it depends on **64**; blast radius 6.327; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (99.8%), Mutation Surface (formerly State Flux) (95.5%), Guard Balance (formerly Safety Score) (91.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.3%)
- **Documentation Coverage:** 96.4824% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Loan` **(Many-Argument Workhorses)** (Impact: 73.5)
  * `findLastAssignmentHistoryRecord` **(Compute Cores)** (Impact: 10.7)
  * `hasMonetaryActivityAfter` **(Compute Cores)** (Impact: 10.6)
  * `getPrincipalAmountForRepaymentSchedule` **(I/O & Config Routines)** (Impact: 8.9)
  * `getDisbursedAmount` **(Compute Cores)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 74 instances
* *State Mutation (weighted view):* 295
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 314`, `args: 262`, `func_start: 204`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 98`, `state_mutation: 147`, `planned_debt: 2`
* *Architecture:* `api: 215`, `import: 64`
* *Defense:* `safety: 4`, `doc: 7`, `immutability_locks: 193`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.327
  * `Choke Point (Betweenness):` 0.003238 | `Ripple Effect (Closeness):` 0.053744
  * `Imports (Out-Degree: 27):` jakarta.persistence.CascadeType, jakarta.persistence.Column, jakarta.persistence.Convert, jakarta.persistence.Embedded, jakarta.persistence.Entity, jakarta.persistence.Enumerated, jakarta.persistence.FetchType, jakarta.persistence.JoinColumn...
  * `Imported By (In-Degree: 315):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanApplicationValidator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1065.82 | **LOC:** 2267 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **113**; blast radius 0.079; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (84.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (36.5%), Mutation Surface (formerly State Flux) (30.9%)
- **Documentation Coverage:** 96.5517% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateForModify` **(Many-Argument Workhorses)** (Impact: 214.6)
  * `validateForCreate` **(Many-Argument Workhorses)** (Impact: 149.6)
  * `validateApproval` **(Many-Argument Workhorses)** (Impact: 46.9)
  * `validateLoanMultiDisbursementDate` **(Many-Argument Workhorses)** (Impact: 42.8)
  * `validatePartialPeriodSupport` **(Many-Argument Workhorses)** (Impact: 42.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 224
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 248`, `args: 51`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 105`, `state_mutation: 88`, `dead_code: 3`, `planned_debt: 6`
* *Architecture:* `api: 21`, `import: 113`
* *Defense:* `doc: 3`, `immutability_locks: 295`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.079
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.000789
  * `Imports (Out-Degree: 95):` com.google.gson.JsonArray, com.google.gson.JsonElement, com.google.gson.JsonObject, com.google.gson.reflect.TypeToken, java.lang.reflect.Type, java.math.BigDecimal, java.time.LocalDate, java.util.ArrayList...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/service/DatatableWriteServiceImpl.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1057.32 | **LOC:** 1430 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **95**; blast radius 0.076; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (87.8%), Complexity Load (formerly Cognitive Load) (56.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (29.3%), Concurrency Surface (formerly Concurrency) (23.8%)
- **Documentation Coverage:** 98.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseDatatableColumnForUpdate` **(Many-Argument Workhorses)** (Impact: 169.5)
  * `updateDatatable` **(Many-Argument Workhorses)** (Impact: 91.7)
  * `updateDatatableEntry` **(Many-Argument Workhorses)** (Impact: 60.5)
  * `parseDatatableColumnForAdd` **(Many-Argument Workhorses)** (Impact: 49.6)
  * `parseDatatableColumnObjectForCreate` **(Many-Argument Workhorses)** (Impact: 44.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 52 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 164
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 311`, `structural_boundaries: 251`, `args: 66`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 98`, `state_mutation: 60`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `api: 15`, `concurrency: 3`, `import: 95`
* *Defense:* `safety: 24`, `doc: 2`, `test: 2`, `immutability_locks: 265`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000158
  * `Imports (Out-Degree: 35):` com.google.gson.JsonArray, com.google.gson.JsonElement, com.google.gson.JsonObject, com.google.gson.reflect.TypeToken, jakarta.persistence.PersistenceException, java.lang.reflect.Type, java.math.BigDecimal, java.sql.PreparedStatement...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanAccrualsProcessingServiceImpl.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1026.04 | **LOC:** 1304 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **74**; blast radius 0.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Guard Balance (formerly Safety Score) (87.3%), Complexity Load (formerly Cognitive Load) (52.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.9%)
- **Documentation Coverage:** 73.7705% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addAccruals` **(Many-Argument Workhorses)** (Impact: 98.0)
    * *Intent:* // PeriodicAccruals
  * `reprocessPeriodicAccruals` **(Many-Argument Workhorses)** (Impact: 41.4)
    * *Intent:* // ReprocessAccruals
  * `addInterestAccrual` **(Many-Argument Workhorses)** (Impact: 37.0)
  * `determineFeeDetails` **(Many-Argument Workhorses)** (Impact: 35.5)
  * `reprocessNonPeriodicAccruals` **(Many-Argument Workhorses)** (Impact: 35.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 86 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 303
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 192`, `args: 83`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 131`, `dead_code: 2`, `planned_debt: 3`, `unreferenced_by_name: 5`
* *Architecture:* `api: 12`, `concurrency: 3`, `import: 74`
* *Defense:* `safety: 65`, `doc: 9`, `immutability_locks: 219`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 46):` java.math.BigDecimal, java.time.LocalDate, java.util.ArrayList, java.util.Collection, java.util.Comparator, java.util.HashMap, java.util.List, java.util.Map...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/helper/ErrorMessageHelper.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 961.38 | **LOC:** 1002 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 22.2%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **12**; blast radius 0.176; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (56.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.1%), Complexity Load (formerly Cognitive Load) (16.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrongAmountInDeferredCapitalizedIncome` **(Compute Cores)** (Impact: 12.4)
  * `wrongValueInExternalAssetDetails` **(Generic / Templated Code)** (Impact: 10.7)
  * `wrongValueInLineInAssetExternalizationJournalEntry` **(Generic / Templated Code)** (Impact: 10.7)
  * `wrongValueInLineInDelinquencyPausePeriodData` **(Generic / Templated Code)** (Impact: 10.7)
  * `wrongValueInLineInLoanTermVariations` **(Generic / Templated Code)** (Impact: 10.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 272`, `structural_boundaries: 186`, `args: 192`, `func_start: 168`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`
* *Architecture:* `api: 168`, `import: 12`
* *Defense:* `doc: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.003027
  * `Imports (Out-Degree: 4):` java.io.IOException, java.math.BigDecimal, java.time.LocalDate, java.time.format.DateTimeFormatter, java.util.List, java.util.Set, java.util.stream.Collectors, org.apache.commons.lang3.StringUtils...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/api/LoanProductsApiResourceSwagger.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 924.38 | **LOC:** 1945 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 28.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.3%), Debt Markers (formerly Tech Debt) (27.3%), Connectivity (formerly Api Exposure) (16.2%)
- **Documentation Coverage:** 78.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LoanProductsApiResourceSwagger` **(Encapsulated Accessors)** (Impact: 1.1)
  * `LoanProductChargeData` **(Encapsulated Accessors)** (Impact: 1.1)
  * `LoanProductChargeToGLAccountMapper` **(Encapsulated Accessors)** (Impact: 1.1)
  * `PostLoanProductsRequest` **(Encapsulated Accessors)** (Impact: 1.1)
  * `AllowAttributeOverrides` **(Encapsulated Accessors)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 90`, `args: 75`, `func_start: 75`, `class_start: 79`
* *Risk/State:* `duplicate_logic: 10`
* *Architecture:* `api: 809`, `import: 10`
* *Defense:* `doc: 614`, `immutability_locks: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` io.swagger.v3.oas.annotations.media.Schema, java.math.BigDecimal, java.time.LocalDate, java.util.List, java.util.Set, org.apache.fineract.accounting.glaccount.data.GLAccountData, org.apache.fineract.infrastructure.codes.api.CodeValuesApiResourceSwagger.GetCodeValuesDataResponse, org.apache.fineract.infrastructure.core.data.EnumOptionData...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepaymentScheduleInstallment.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 904.42 | **LOC:** 1303 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 30.0%
- **Blast Radius:** changing it is visible to **85** in-repo importer(s); it depends on **27**; blast radius 1.047; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.6%), Guard Balance (formerly Safety Score) (96.3%), Connectivity (formerly Api Exposure) (93.2%), Complexity Load (formerly Cognitive Load) (74.0%)
- **Documentation Coverage:** 99.2509% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getPaymentFunction` **(Compute Cores)** (Impact: 38.7)
  * `reduceAdvanceAndLateTotalsForRepaymentPeriod` **(Stateful Encapsulated Methods)** (Impact: 17.1)
  * `resetDerivedComponents` **(I/O & Config Routines)** (Impact: 14.7)
  * `isOutstandingBalanceNotZero` **(Callbacks & Closures)** (Impact: 10.8)
  * `trackAdvanceAndLateTotalsForRepaymentPeriod` **(Stateful Encapsulated Methods)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 293
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 186`, `args: 175`, `func_start: 139`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 157`, `planned_debt: 1`
* *Architecture:* `api: 131`, `import: 27`
* *Defense:* `doc: 2`, `immutability_locks: 235`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.047
  * `Choke Point (Betweenness):` 0.000198 | `Ripple Effect (Closeness):` 0.035558
  * `Imports (Out-Degree: 11):` jakarta.persistence.CascadeType, jakarta.persistence.Column, jakarta.persistence.Entity, jakarta.persistence.FetchType, jakarta.persistence.JoinColumn, jakarta.persistence.ManyToOne, jakarta.persistence.OneToMany, jakarta.persistence.Table...
  * `Imported By (In-Degree: 85):` (Excluded from Brief to save tokens)

### `integration-tests/src/test/java/org/apache/fineract/integrationtests/ClientSavingsIntegrationTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 885.2 | **LOC:** 3614 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **48**; blast radius 0.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (88.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (32.2%), Complexity Load (formerly Cognitive Load) (25.2%), Connectivity (formerly Api Exposure) (7.6%)
- **Documentation Coverage:** 94.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createSavingsProduct` **(Many-Argument Workhorses)** (Impact: 14.0)
    * *Intent:* // LienAtProductlevel with Overdraft Limit > Lien Limit
  * `createSavingsProduct` **(Many-Argument Workhorses)** (Impact: 12.9)
    * *Intent:* // LienAtProductLevel
  * `testSavingsAccountPostInterestOnLastDayWithOverdraft` **(I/O & Config Routines)** (Impact: 11.5)
  * `testSavingsAccountPostInterestOnLastDayWithdrawalWithOverdraft` **(I/O & Config Routines)** (Impact: 11.5)
  * `createSavingsProduct` **(Many-Argument Workhorses)** (Impact: 10.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 540
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 285`, `args: 56`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 227`, `state_mutation: 488`, `unreferenced_by_name: 47`
* *Architecture:* `api: 55`, `import: 48`
* *Defense:* `safety: 4`, `doc: 95`, `test: 343`, `immutability_locks: 500`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` io.restassured.builder.RequestSpecBuilder, io.restassured.builder.ResponseSpecBuilder, io.restassured.http.ContentType, io.restassured.specification.RequestSpecification, io.restassured.specification.ResponseSpecification, java.math.BigDecimal, java.text.DateFormat, java.text.DecimalFormat...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanReAgingStepDef.java` -> Churn: **65.37%** | Cog Load: 78.8015% | Debt: 0.0%
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepaymentScheduleInstallment.java` -> Churn: **64.57%** | Cog Load: 73.9578% | Debt: 7.9261%
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/LoanApplicationTerms.java` -> Churn: **62.0%** | Cog Load: 88.2692% | Debt: 8.8223%
- `fineract-core/src/main/java/org/apache/fineract/commands/service/CommandWrapperBuilder.java` -> Churn: **53.01%** | Cog Load: 85.6461% | Debt: 7.6892%
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/Loan.java` -> Churn: **50.28%** | Cog Load: 50.1031% | Debt: 8.0812%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/AbstractCumulativeLoanScheduleGenerator.java` -> **Attila Budai** (100.0% isolated ownership) | Magnitude: 2458.84
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/BatchHelper.java` -> **Adam Saghy** (100.0% isolated ownership) | Magnitude: 1344.64
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/FixedDepositTest.java` -> **sayhaed** (100.0% isolated ownership) | Magnitude: 822.02
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/savings/SavingsAccountHelper.java` -> **Adam Saghy** (100.0% isolated ownership) | Magnitude: 731.96
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/ClientHelper.java` -> **Adam Saghy** (100.0% isolated ownership) | Magnitude: 694.96

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/Loan.java` -> **Severity: 0.309** (Bridge: 0.0032 * Flux: 95.4763%)
- `fineract-client/src/main/java/org/apache/fineract/client/util/FineractClient.java` -> **Severity: 0.091** (Bridge: 0.0009 * Flux: 100.0%)
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/LoanApplicationTerms.java` -> **Severity: 0.089** (Bridge: 0.0009 * Flux: 99.9086%)
- `fineract-core/src/main/java/org/apache/fineract/portfolio/group/domain/Group.java` -> **Severity: 0.072** (Bridge: 0.0007 * Flux: 99.7275%)
- `fineract-charge/src/main/java/org/apache/fineract/portfolio/charge/domain/Charge.java` -> **Severity: 0.061** (Bridge: 0.0006 * Flux: 99.984%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/api/JsonCommand.java` -> **Severity: 15.803** (Embedded: 0.1617 * Error Risk: 97.7439%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/DateUtils.java` -> **Severity: 15.076** (Embedded: 0.1554 * Error Risk: 97.0026%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/MathUtil.java` -> **Severity: 14.329** (Embedded: 0.1442 * Error Risk: 99.3684%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/data/CommandProcessingResult.java` -> **Severity: 13.557** (Embedded: 0.1372 * Error Risk: 98.8052%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/data/ApiParameterError.java` -> **Severity: 12.871** (Embedded: 0.1578 * Error Risk: 81.5703%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `fineract-validation/src/main/java/org/apache/fineract/validation/constraints/LocalDate.java` -> **Severity: 3721.1** (Blast Radius: 37.211 * Doc Risk: 100.0%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/api/JsonCommand.java` -> **Severity: 1671.744** (Blast Radius: 17.202 * Doc Risk: 97.1831%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/domain/AbstractPersistableCustom.java` -> **Severity: 1646.3** (Blast Radius: 16.463 * Doc Risk: 100.0%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/data/CommandProcessingResult.java` -> **Severity: 1472.6** (Blast Radius: 14.726 * Doc Risk: 100.0%)
- `fineract-provider/src/main/java/org/apache/fineract/spm/domain/Component.java` -> **Severity: 1341.9** (Blast Radius: 13.419 * Doc Risk: 100.0%)

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
