# ARCHITECTURAL_BRIEF: fineract
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/apache/fineract.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 6402 analyzed artifact(s), 585888 LOC.
- **Load-bearing artifact:** `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/api/JsonCommand.java` -- 865 in-repo importer(s) depend on it. Changes here propagate furthest.
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
| Analyzed Artifacts (Scanned) | 6402 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 456 |
| Total LOC | 585888 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 93.4% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6522 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1699 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.8444 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 335 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 5819 | 519802 | 90.9% |
| XML | 332 | 0 | 5.2% |
| GROOVY | 88 | 6034 | 1.4% |
| YAML | 45 | 2205 | 0.7% |
| PLAINTEXT | 38 | 1 | 0.6% |
| MARKDOWN | 33 | 0 | 0.5% |
| JSON | 19 | 607 | 0.3% |
| SQLITE | 15 | 2424 | 0.2% |
| SHELL | 8 | 403 | 0.1% |
| HTML | 3 | 53713 | 0.0% |
| CSS | 1 | 630 | 0.0% |
| BATCH | 1 | 69 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 6401 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 18%, State Mutators Files 18%, Data / Markup / Trivial 16%, Encapsulated Accessors Files 10%, Large Core Modules (3) 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 6330 | 98.9% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 70 | 1.1% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 456*

**Composition by Extension & Reason:**
- `.adoc`: 156x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 4 exceeds 500 chars), 1x Excluded (Saturation: Line 15 exceeds 500 chars)
- `.avsc`: 83x Unsupported Format (.avsc)
- `.feature`: 69x Unsupported Format (.feature)
- `.xml`: 7x Excluded (Saturation: Line 28 exceeds 500 chars), 2x Excluded (Saturation: Line 32 exceeds 500 chars), 2x Excluded (Massive Static Asset Blob: 3121 LOC)
- `no_extension`: 15x Unsupported Format (.undeterminable), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.env`: 19x Excluded (Unsupported Extension: '.env')
- `.png`: 17x Excluded (Explicitly Denied Extension: '.png')
- `.ftl`: 15x Unsupported Format (.ftl)
- `.sql`: 2x Excluded (Static Asset Blob without Intent: 1921 LOC), 2x Excluded (Static Asset Blob without Intent: 1895 LOC), 1x Excluded (Static Asset Blob without Intent: 1919 LOC)
- `.mustache`: 5x Unsupported Format (.mustache), 1x Excluded (Saturation: Line 47 exceeds 500 chars)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 2432 LOC), 1x Excluded (Static Asset Blob without Intent: 1073 LOC)
- `.imports`: 4x Unsupported Format (.imports)
- `.vm`: 4x Unsupported Format (.vm)
- `.properties`: 2x Excluded (Saturation: Line 68 exceeds 500 chars), 1x Excluded (Saturation: Line 67 exceeds 500 chars), 1x Excluded (Saturation: Line 19 exceeds 500 chars)
- `.puml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 7.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 94.7 | 30.1 | 45.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 11.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.3 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 21.0 | 9.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 14.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.8 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.2 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 72.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3094 | 479 | 0 | `integration-tests/src/test/java/org/apache/fineract/integrationtests/ClientLoanIntegrationTest.java` |
| cleanup | 179 | 82 | 0 | `fineract-db/old-schema-files/0001a-mifosplatform-core-ddl-latest.sql` |
| guards | 109698 | 4670 | 39 | `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanStepDef.java` |
| danger | 27935 | 2318 | 9 | `integration-tests/src/test/java/org/apache/fineract/integrationtests/AdvancedPaymentAllocationLoanRepaymentScheduleTest.java` |
| concurrency | 1229 | 346 | 0 | `integration-tests/src/test/java/org/apache/fineract/integrationtests/LoanCapitalizedIncomeTest.java` |
| connectivity | 47983 | 5766 | 13 | `fineract-provider/src/main/resources/static/legacy-docs/apiLive.htm` |
| io | 5492 | 471 | 0 | `fineract-provider/src/main/resources/static/legacy-docs/apiLive.htm` |
| crypto | 0 | 0 | 0 | - |
| ipc | 20 | 7 | 0 | `fineract-provider/src/main/java/org/apache/fineract/infrastructure/springbatch/messagehandler/kafka/KafkaManagerConfig.java` |
| time | 12043 | 1108 | 4 | `fineract-progressive-loan/src/test/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculatorTest.java` |
| serialization | 407 | 168 | 0 | `fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/sms/service/SmsCampaignWritePlatformServiceJpaImpl.java` |
| regex | 131 | 51 | 0 | `fineract-provider/src/test/java/org/apache/fineract/infrastructure/jobs/filter/LoanCOBApiFilterTest.java` |
| events | 2751 | 603 | 0 | `integration-tests/src/test/java/org/apache/fineract/integrationtests/LoanDisbursementDetailsIntegrationTest.java` |
| tests | 25915 | 649 | 1 | `integration-tests/src/test/java/org/apache/fineract/integrationtests/ClientLoanIntegrationTest.java` |
| docs | 16577 | 5933 | 2 | `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/api/LoansApiResourceSwagger.java` |
| debt | 2026 | 393 | 0 | `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/loans/LoanTransactionHelper.java` |
| mutation | 143733 | 3822 | 45 | `fineract-provider/src/main/resources/static/legacy-docs/apiLive.htm` |
| dead_code | 7080 | 2088 | 3 | `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanStepDef.java` |
| credential | 23 | 11 | 0 | `fineract-provider/src/main/resources/static/legacy-docs/apiLive.htm` |
| threat | 127 | 14 | 0 | `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/support/TestContextKey.java` |
| ml_ai | 12728 | 875 | 3 | `integration-tests/src/test/java/org/apache/fineract/integrationtests/investor/externalassetowner/InitiateExternalAssetOwnerTransferTest.java` |
| ui | 732 | 5 | 0 | `fineract-provider/src/main/resources/static/legacy-docs/apiLive.htm` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.2359**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `fineract-provider/src/main/resources/static/legacy-docs/apiLive.htm` (Hits: 3198)
- `scripts/split-tests.sh` (Hits: 48)
- `scripts/split-features.sh` (Hits: 35)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **JsonCommand.java** (`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/api/JsonCommand.java`) — 865 inbound connections
2. **CommandProcessingResult.java** (`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/data/CommandProcessingResult.java`) — 810 inbound connections
3. **NewCommandSourceHandler.java** (`fineract-core/src/main/java/org/apache/fineract/commands/handler/NewCommandSourceHandler.java`) — 459 inbound connections
4. **CommandType.java** (`fineract-core/src/main/java/org/apache/fineract/commands/annotation/CommandType.java`) — 436 inbound connections
5. **DateUtils.java** (`fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/DateUtils.java`) — 339 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **LoanWritePlatformServiceJpaRepositoryImpl.java** (`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanWritePlatformServiceJpaRepositoryImpl.java`) — 207 outbound dependencies
2. **LoanAccountConfiguration.java** (`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/starter/LoanAccountConfiguration.java`) — 170 outbound dependencies
3. **LoansApiResource.java** (`fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/api/LoansApiResource.java`) — 168 outbound dependencies
4. **FineractFeignClient.java** (`fineract-client-feign/src/main/java/org/apache/fineract/client/feign/FineractFeignClient.java`) — 156 outbound dependencies
5. **LoanStepDef.java** (`fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanStepDef.java`) — 154 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `validateForUpdate` **(Many-Argument Workhorses)** (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/serialization/LoanProductDataValidator.java`) -> Impact: **199.7** | LOC: 704
- `validateForModify` **(Many-Argument Workhorses)** (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanApplicationValidator.java`) -> Impact: **193.9** | LOC: 621
- `retrieveTransactionTemplate` **(Many-Argument Workhorses)** (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/api/LoanTransactionsApiResource.java`) -> Impact: **178.9** | LOC: 98
- `createJournalEntriesForRepaymentWhenLoanIsChargedOff` **(Many-Argument Workhorses)** (@ `fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/AccrualBasedAccountingProcessorForLoan.java`) -> Impact: **150.0** | LOC: 227
- `readSavings` **(Many-Argument Workhorses)** (@ `fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/recurringdeposit/RecurringDepositImportHandler.java`) -> Impact: **150.0** | LOC: 159
- `validateForCreate` **(Many-Argument Workhorses)** (@ `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/serialization/LoanProductDataValidator.java`) -> Impact: **144.4** | LOC: 682
- `readLoan` **(Many-Argument Workhorses)** (@ `fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/importhandler/loan/LoanImportHandler.java`) -> Impact: **144.0** | LOC: 234
- `LoanProduct` **(Many-Argument Workhorses)** (@ `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/domain/LoanProduct.java`) -> Impact: **137.4** | LOC: 149
- `testCreateShareAccountWithCharges` **(I/O & Config Routines)** (@ `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/shares/ShareAccountIntegrationTests.java`) -> Impact: **137.3** | LOC: 627
- `rescheduleNextInstallments` **(Many-Argument Workhorses)** (@ `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/AbstractCumulativeLoanScheduleGenerator.java`) -> Impact: **130.6** | LOC: 350

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `integration-tests/src/test/java/org/apache/fineract/integrationtests` | 227 | 21278.1 | 8.5% | 0.0% |
| `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service` | 46 | 8595.1 | 29.73% | 13.24% |
| `fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain` | 40 | 6781.26 | 28.59% | 31.27% |
| `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain` | 73 | 6070.56 | 12.59% | 8.28% |
| `fineract-provider/src/main/resources` | 9 | 5038.24 | 0.0% | 0.0% |
| `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain` | 26 | 4964.1 | 18.04% | 27.02% |
| `integration-tests/src/test/java/org/apache/fineract/integrationtests/common` | 44 | 4708.78 | 19.63% | 0.0% |
| `fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service` | 18 | 4269.9 | 19.92% | 11.67% |
| `fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/service` | 27 | 3869.22 | 15.54% | 5.91% |
| `fineract-core/src/main/java/org/apache/fineract/commands/service` | 8 | 3814.14 | 26.75% | 16.67% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/database/SqlOperator.java` -> **100.0%** Exposure
- `fineract-core/src/main/java/org/apache/fineract/portfolio/search/SearchConstants.java` -> **100.0%** Exposure
- `fineract-document/src/main/java/org/apache/fineract/infrastructure/documentmanagement/command/DocumentCommand.java` -> **100.0%** Exposure
- `fineract-document/src/main/java/org/apache/fineract/infrastructure/documentmanagement/data/ImageCreateRequest.java` -> **100.0%** Exposure
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/ScheduleCurrentPeriodParams.java` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `gradlew` -> **100.0%** Exposure
- `scripts/split-features.sh` -> **100.0%** Exposure
- `scripts/split-tests.sh` -> **100.0%** Exposure
- `fineract-accounting/src/main/java/org/apache/fineract/accounting/producttoaccountmapping/service/ProductToGLAccountMappingReadPlatformServiceImpl.java` -> **100.0%** Exposure
- `fineract-branch/src/main/java/org/apache/fineract/organisation/teller/util/DateRange.java` -> **100.0%** Exposure
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

### Credential Material (formerly Hardcoded Payload Artifacts)
- `fineract-war/setenv.sh` -> **99.9882%** Exposure
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/PasswordResetIntegrationTest.java` -> **98.3572%** Exposure
- `fineract-provider/src/main/resources/static/legacy-docs/apiLive.htm` -> **5.4652%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `64574` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `fineract-provider/src/main/resources/keystore.jks` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-core/src/main/java/org/apache/fineract/commands/service/CommandWrapperBuilder.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.907)
- **Top Global Matches:** file_cluster_12: 9.907, file_cluster_7: 11.542, file_cluster_15: 12.063
- **Magnitude:** 3365.86 | **LOC:** 3905 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **129** in-repo importer(s); it depends on **13**; blast radius 0.674; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.78% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `commonDatatableSettings` **(Stateful Encapsulated Methods)** (Impact: 6.5)
  * `payLoanCharge` **(Compute Cores)** (Impact: 5.8)
  * `deleteGuarantor` **(Parameter Forwarders)** (Impact: 2.5)
  * `createCalendar` **(Parameter Forwarders)** (Impact: 2.5)
  * `createMeeting` **(Parameter Forwarders)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 2016
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 478`, `args: 455`, `func_start: 455`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 108`, `state_mutation: 1994`, `planned_debt: 1`
* *Architecture:* `api: 455`, `import: 13`
* *Defense:* `doc: 2`, `immutability_locks: 462`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 6.6e-05 | `Ripple Effect (Closeness):` 0.020191
  * `Imports (Out-Degree: 8):` edu.umd.cs.findbugs.annotations.SuppressFBWarnings, java.util.Arrays, java.util.HashSet, java.util.Set, org.apache.fineract.commands.domain.CommandWrapper, org.apache.fineract.infrastructure.accountnumberformat.service.AccountNumberFormatConstants, org.apache.fineract.infrastructure.core.domain.ExternalId, org.apache.fineract.portfolio.client.api.ClientApiConstants...
  * `Imported By (In-Degree: 129):` (Excluded from Brief to save tokens)

### `fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain/SavingsAccount.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.562)
- **Top Global Matches:** file_cluster_5: 8.562, file_cluster_12: 9.579, file_cluster_7: 10.999
- **Magnitude:** 2658.28 | **LOC:** 3904 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **69** in-repo importer(s); it depends on **108**; blast radius 0.95; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Connectivity (formerly Api Exposure) (84.5%), Complexity Load (formerly Cognitive Load) (81.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.8662% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `postInterest` **(Many-Argument Workhorses)** (Impact: 108.8)
  * `modifyApplication` **(Many-Argument Workhorses)** (Impact: 85.7)
  * `recalculateDailyBalances` **(Many-Argument Workhorses)** (Impact: 64.9)
  * `payCharge` **(Many-Argument Workhorses)** (Impact: 60.1)
  * `calculateInterestUsing` **(Many-Argument Workhorses)** (Impact: 59.5)
    * *Intent:* * All interest calculation based on END-OF-DAY-BALANCE. * * Interest calculation is performed on-the...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 241 instances
* *State Mutation (weighted view):* 902
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 528`, `structural_boundaries: 559`, `args: 225`, `func_start: 234`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 177`, `state_mutation: 420`, `dead_code: 6`, `planned_debt: 4`, `fragile_debt: 2`
* *Architecture:* `api: 253`, `import: 108`
* *Defense:* `doc: 9`, `immutability_locks: 517`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.95
  * `Choke Point (Betweenness):` 0.000981 | `Ripple Effect (Closeness):` 0.017851
  * `Imports (Out-Degree: 64):` com.google.gson.JsonArray, jakarta.persistence.CascadeType, jakarta.persistence.Column, jakarta.persistence.DiscriminatorColumn, jakarta.persistence.DiscriminatorType, jakarta.persistence.DiscriminatorValue, jakarta.persistence.Embedded, jakarta.persistence.Entity...
  * `Imported By (In-Degree: 69):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/resources/static/legacy-docs/apiLive.htm` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.391)
- **Top Global Matches:** file_cluster_9: 8.391, file_cluster_15: 9.488, file_cluster_13: 9.831
- **Magnitude:** 2617.78 | **LOC:** 55066 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.07; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.9%), Connectivity (formerly Api Exposure) (13.4%), Mutation Surface (formerly State Flux) (8.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clickAPILink` **(Compute Cores)** (Impact: 12.1)
  * `clickAPILinkNotPretty` **(Compute Cores)** (Impact: 12.1)
  * `getBaseURL` **(Compute Cores)** (Impact: 8.2)
  * `getLocation` **(Callbacks & Closures)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 5971`, `args: 5869`, `func_start: 7`, `class_start: 389`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 16`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 3198`, `api: 1472`, `import: 1`
* *Defense:* `safety: 99`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` apidocs.css, jquery-1.7.min.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/impl/AdvancedPaymentScheduleTransactionProcessor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.179)
- **Top Global Matches:** file_cluster_5: 9.179, file_cluster_12: 10.656, file_cluster_4: 12.025
- **Magnitude:** 2350.68 | **LOC:** 4170 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 22.6%
- **Blast Radius:** changing it is visible to **38** in-repo importer(s); it depends on **107**; blast radius 0.253; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (98.9%), Guard Balance (formerly Safety Score) (66.9%), Complexity Load (formerly Cognitive Load) (38.6%)
- **Documentation Coverage:** 98.1595% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processAllocationsHorizontally` **(Many-Argument Workhorses)** (Impact: 99.9)
  * `processPeriodsVertically` **(Many-Argument Workhorses)** (Impact: 89.2)
  * `refundTransactionHorizontally` **(Many-Argument Workhorses)** (Impact: 44.2)
  * `liftOutstandingBalances` **(Many-Argument Workhorses)** (Impact: 39.8)
  * `refundTransactionVertically` **(Many-Argument Workhorses)** (Impact: 38.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 178 instances
* *State Mutation (weighted view):* 776
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 489`, `structural_boundaries: 412`, `args: 516`, `func_start: 139`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 182`, `state_mutation: 420`, `planned_debt: 9`
* *Architecture:* `api: 27`, `concurrency: 24`, `import: 107`
* *Defense:* `safety: 37`, `doc: 4`, `immutability_locks: 335`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 0.000761 | `Ripple Effect (Closeness):` 0.013158
  * `Imports (Out-Degree: 63):` jakarta.annotation.Nullable, jakarta.validation.constraints.NotNull, java.math.BigDecimal, java.math.BigDecimal.ZERO, java.math.MathContext, java.math.RoundingMode, java.time.LocalDate, java.time.temporal.ChronoUnit...
  * `Imported By (In-Degree: 38):` (Excluded from Brief to save tokens)

### `integration-tests/src/test/java/org/apache/fineract/integrationtests/ClientLoanIntegrationTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.731)
- **Top Global Matches:** file_cluster_5: 9.731, file_cluster_12: 9.878, file_cluster_7: 11.217
- **Magnitude:** 2285.52 | **LOC:** 8361 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **100**; blast radius 0.07; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (59.6%), Complexity Load (formerly Cognitive Load) (42.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (32.9%), Connectivity (formerly Api Exposure) (3.8%)
- **Documentation Coverage:** 86.802% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testLoanCharges_INSTALMENT_FEE` **(I/O & Config Routines)** (Impact: 44.0)
  * `chargeOff` **(Type Conversions)** (Impact: 14.4)
  * `createLoanProductWithInterestRecalculation` **(Many-Argument Workhorses)** (Impact: 14.4)
  * `chargeAdjustmentAccountingValidation` **(I/O & Config Routines)** (Impact: 13.5)
  * `createLoanProductWithInterestRecalculation` **(Many-Argument Workhorses)** (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 74 instances
* *State Mutation (weighted view):* 1462
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 854`, `args: 164`, `func_start: 130`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 295`, `state_mutation: 1314`, `unreferenced_by_name: 66`
* *Architecture:* `api: 68`, `import: 100`
* *Defense:* `safety: 26`, `doc: 31`, `test: 992`, `immutability_locks: 694`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` com.google.gson.Gson, com.google.gson.JsonObject, com.google.gson.JsonParser, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, io.restassured.builder.RequestSpecBuilder, io.restassured.builder.ResponseSpecBuilder, io.restassured.http.ContentType, io.restassured.path.json.JsonPath...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/AbstractCumulativeLoanScheduleGenerator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.344)
- **Top Global Matches:** file_cluster_4: 9.344, file_cluster_5: 11.945, file_cluster_12: 12.232
- **Magnitude:** 2249.44 | **LOC:** 2861 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **46**; blast radius 0.09; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.9%), Complexity Load (formerly Cognitive Load) (67.6%)
- **Documentation Coverage:** 75.9494% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rescheduleNextInstallments` **(Many-Argument Workhorses)** (Impact: 130.6)
  * `generate` **(Many-Argument Workhorses)** (Impact: 121.0)
  * `handleRecalculationForNonDueDateTransactions` **(Many-Argument Workhorses)** (Impact: 108.6)
  * `applyLoanTermVariations` **(Many-Argument Workhorses)** (Impact: 85.3)
    * *Intent:* /** * @param loanApplicationTerms * @param scheduleParams * @param previousRepaymentDate * @param sc...
  * `addInterestOnlyRepaymentScheduleForCurrentDate` **(Many-Argument Workhorses)** (Impact: 66.2)
    * *Intent:* /** * Method calculates interest on not paid outstanding principal and interest (if compounding is e...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 238 instances
* *State Mutation (weighted view):* 852
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 395`, `structural_boundaries: 219`, `args: 75`, `func_start: 71`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 77`, `state_mutation: 376`, `planned_debt: 4`, `unreferenced_by_name: 2`
* *Architecture:* `api: 9`, `import: 46`
* *Defense:* `safety: 2`, `doc: 18`, `immutability_locks: 317`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.09
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.000312
  * `Imports (Out-Degree: 41):` jakarta.validation.constraints.NotNull, java.math.BigDecimal, java.math.MathContext, java.time.LocalDate, java.util.ArrayList, java.util.Collection, java.util.HashMap, java.util.HashSet...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanStepDef.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.833)
- **Top Global Matches:** file_cluster_5: 8.833, file_cluster_12: 10.565, file_cluster_7: 11.78
- **Magnitude:** 1996.04 | **LOC:** 5999 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 27.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **154**; blast radius 0.07; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (90.5%), Guard Balance (formerly Safety Score) (58.4%), Complexity Load (formerly Cognitive Load) (17.7%), Connectivity (formerly Api Exposure) (11.0%)
- **Documentation Coverage:** 99.6296% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetchValuesOfRepaymentSchedule` **(Stateful Encapsulated Methods)** (Impact: 60.8)
  * `fetchValuesOfTransaction` **(Stateful Encapsulated Methods)** (Impact: 46.5)
  * `fetchValuesOfFilteredTransaction` **(Stateful Encapsulated Methods)** (Impact: 39.2)
  * `validateRepaymentScheduleTotal` **(Many-Argument Workhorses)** (Impact: 33.1)
  * `fetchValuesOfLoanTermVariations` **(Stateful Encapsulated Methods)** (Impact: 32.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 133 instances
* *State Mutation (weighted view):* 445
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 787`, `args: 691`, `func_start: 284`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 269`, `state_mutation: 179`, `dead_code: 12`, `planned_debt: 2`, `unreferenced_by_name: 207`
* *Architecture:* `api: 265`, `import: 154`
* *Defense:* `safety: 61`, `doc: 2`, `test: 281`, `immutability_locks: 868`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 55):` edu.umd.cs.findbugs.annotations.SuppressFBWarnings, io.cucumber.datatable.DataTable, io.cucumber.java.ParameterType, io.cucumber.java.en.And, io.cucumber.java.en.Then, io.cucumber.java.en.When, java.io.IOException, java.math.BigDecimal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanWritePlatformServiceJpaRepositoryImpl.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.317)
- **Top Global Matches:** file_cluster_5: 8.317, file_cluster_12: 9.331, file_cluster_7: 10.505
- **Magnitude:** 1615.76 | **LOC:** 3659 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 36.4%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **207**; blast radius 0.08; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.7%), Mutation Surface (formerly State Flux) (57.5%), Complexity Load (formerly Cognitive Load) (25.1%)
- **Documentation Coverage:** 97.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `disburseLoan` **(Many-Argument Workhorses)** (Impact: 64.5)
  * `close` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `applyMeetingDateChanges` **(Many-Argument Workhorses)** (Impact: 35.3)
  * `makeManualInterestRefund` **(Many-Argument Workhorses)** (Impact: 34.1)
  * `regenerateScheduleOnDisbursement` **(Many-Argument Workhorses)** (Impact: 31.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 127 instances
* *State Mutation (weighted view):* 504
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 361`, `structural_boundaries: 537`, `args: 113`, `func_start: 94`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 187`, `state_mutation: 250`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `api: 48`, `import: 207`
* *Defense:* `safety: 4`, `doc: 4`, `immutability_locks: 596`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 6.6e-05 | `Ripple Effect (Closeness):` 0.000803
  * `Imports (Out-Degree: 186):` com.google.common.collect.Lists, com.google.gson.JsonArray, com.google.gson.JsonElement, com.google.gson.JsonObject, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, io.github.resilience4j.retry.annotation.Retry, java.math.BigDecimal, java.time.LocalDate...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/LoanApplicationTerms.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.462)
- **Top Global Matches:** file_cluster_12: 7.462, file_cluster_5: 9.464, file_cluster_16: 10.015
- **Magnitude:** 1595.68 | **LOC:** 2272 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **48**; blast radius 0.256; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (84.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.1%)
- **Documentation Coverage:** 98.8406% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LoanApplicationTerms` **(Many-Argument Workhorses)** (Impact: 61.0)
  * `periodicInterestRate` **(Many-Argument Workhorses)** (Impact: 60.1)
  * `calculateTotalInterestForPeriod` **(Many-Argument Workhorses)** (Impact: 51.2)
  * `calculatePeriodsBetweenDates` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `calculateDecliningInterestDueForInstallmentAfterApplyingGrace` **(Many-Argument Workhorses)** (Impact: 24.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 131 instances
* *State Mutation (weighted view):* 602
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 314`, `args: 189`, `func_start: 189`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 340`, `dead_code: 1`, `planned_debt: 6`
* *Architecture:* `api: 158`, `import: 48`
* *Defense:* `safety: 1`, `doc: 9`, `immutability_locks: 351`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.000786 | `Ripple Effect (Closeness):` 0.050747
  * `Imports (Out-Degree: 41):` jakarta.validation.constraints.NotNull, java.math.BigDecimal, java.math.MathContext, java.time.LocalDate, java.time.temporal.ChronoUnit, java.util.ArrayList, java.util.HashSet, java.util.List...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/serialization/LoanProductDataValidator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 12.116)
- **Top Global Matches:** file_cluster_6: 12.116, file_cluster_8: 13.301, file_cluster_4: 18.524
- **Magnitude:** 1560.72 | **LOC:** 3019 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **60**; blast radius 0.074; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (80.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.6%), Connectivity (formerly Api Exposure) (36.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateForUpdate` **(Many-Argument Workhorses)** (Impact: 199.7)
  * `validateForCreate` **(Many-Argument Workhorses)** (Impact: 144.4)
  * `validateInterestRecalculationParams` **(Many-Argument Workhorses)** (Impact: 94.5)
  * `validateBorrowerCycleVariations` **(Many-Argument Workhorses)** (Impact: 70.2)
  * `validatePartialPeriodSupport` **(Many-Argument Workhorses)** (Impact: 62.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 137 instances
* *State Mutation (weighted view):* 421
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 429`, `structural_boundaries: 146`, `args: 38`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 178`, `state_mutation: 147`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 51`, `import: 60`
* *Defense:* `doc: 2`, `immutability_locks: 353`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.074
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.001201
  * `Imports (Out-Degree: 41):` com.google.gson.JsonArray, com.google.gson.JsonElement, com.google.gson.JsonObject, com.google.gson.reflect.TypeToken, java.lang.reflect.Type, java.math.BigDecimal, java.util.ArrayList, java.util.Arrays...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/loans/LoanTransactionHelper.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.355)
- **Top Global Matches:** file_cluster_5: 8.355, file_cluster_12: 9.716, file_cluster_7: 10.634
- **Magnitude:** 1558.16 | **LOC:** 3220 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **120** in-repo importer(s); it depends on **91**; blast radius 0.766; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (64.0%), Complexity Load (formerly Cognitive Load) (25.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.3%)
- **Documentation Coverage:** 99.4161% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkAccrualTransactionForRepayment` **(Many-Argument Workhorses)** (Impact: 11.2)
    * *Intent:* // TODO: Rewrite to use fineract-client instead! // Example: org.apache.fineract.integrationtests.co...
  * `getDisburseLoanAsJSON` **(Stateful Encapsulated Methods)** (Impact: 9.9)
    * *Intent:* // TODO: Rewrite to use fineract-client instead! // Example: org.apache.fineract.integrationtests.co...
  * `getApproveLoanAsJSON` **(Stateful Encapsulated Methods)** (Impact: 9.9)
    * *Intent:* // TODO: Rewrite to use fineract-client instead! // Example: org.apache.fineract.integrationtests.co...
  * `applyLoanCommand` **(Compute Cores)** (Impact: 7.6)
    * *Intent:* // TODO: Rewrite to use fineract-client instead! // Example: org.apache.fineract.integrationtests.co...
  * `getLoanChargeRefundBodyAsJSON` **(Stateful Encapsulated Methods)** (Impact: 7.6)
    * *Intent:* // TODO: Rewrite to use fineract-client instead! // Example: org.apache.fineract.integrationtests.co...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 339
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 561`, `args: 361`, `func_start: 365`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 113`, `state_mutation: 239`, `planned_debt: 180`
* *Architecture:* `io: 4`, `api: 323`, `import: 91`
* *Defense:* `doc: 3`, `test: 25`, `immutability_locks: 890`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.766
  * `Choke Point (Betweenness):` 6.1e-05 | `Ripple Effect (Closeness):` 0.020884
  * `Imports (Out-Degree: 15):` com.google.common.reflect.TypeToken, com.google.gson.Gson, io.restassured.specification.RequestSpecification, io.restassured.specification.ResponseSpecification, jakarta.ws.rs.core.HttpHeaders, jakarta.ws.rs.core.MediaType, java.io.ByteArrayInputStream, java.io.File...
  * `Imported By (In-Degree: 120):` (Excluded from Brief to save tokens)

### `fineract-progressive-loan/src/test/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculatorTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 11.432)
- **Top Global Matches:** file_cluster_12: 11.432, file_cluster_5: 11.584, file_cluster_9: 11.719
- **Magnitude:** 1488.46 | **LOC:** 5294 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 36.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **49**; blast radius 0.07; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.7%), Guard Balance (formerly Safety Score) (47.2%), Complexity Load (formerly Cognitive Load) (14.0%), Connectivity (formerly Api Exposure) (8.7%)
- **Documentation Coverage:** 94.8052% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_balance_correction_on0215_disbursedAmt100_dayInYears360_daysInMonth30_repayEvery1Month` **(I/O & Config Routines)** (Impact: 14.5)
    * *Intent:* /** * This test case tests a period early and late repayment with balance correction */
  * `test_emi_calculator_performance` **(Annotated & Test Methods)** (Impact: 13.6)
  * `test_two_reschedules_disbursedAmt100_dayInYears360_daysInMonth30_repayEvery1Month` **(I/O & Config Routines)** (Impact: 13.2)
  * `test_reschedule_disbursedAmt100_dayInYears360_daysInMonth30_repayEvery1Month` **(I/O & Config Routines)** (Impact: 13.1)
  * `test_reschedule_partial_period_disbursedAmt100_dayInYears360_daysInMonth30_repayEvery1Month` **(Annotated & Test Methods)** (Impact: 13.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 233
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 662`, `structural_boundaries: 278`, `args: 155`, `func_start: 133`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 138`, `state_mutation: 211`, `dead_code: 1`, `unreferenced_by_name: 108`
* *Architecture:* `api: 104`, `import: 49`
* *Defense:* `safety: 1`, `doc: 7`, `test: 878`, `immutability_locks: 594`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` java.math.BigDecimal, java.math.BigDecimal.ZERO, java.math.MathContext, java.math.RoundingMode, java.time.LocalDate, java.util.ArrayList, java.util.List, java.util.stream.IntStream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/AccrualBasedAccountingProcessorForLoan.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.806)
- **Top Global Matches:** file_cluster_6: 9.806, file_cluster_8: 9.99, file_cluster_4: 17.473
- **Magnitude:** 1472.16 | **LOC:** 2198 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **24**; blast radius 0.075; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.2%), Complexity Load (formerly Cognitive Load) (50.0%)
- **Documentation Coverage:** 88.3721% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createJournalEntriesForRepaymentWhenLoanIsChargedOff` **(Many-Argument Workhorses)** (Impact: 150.0)
  * `createJournalEntriesForLoanRepayments` **(Many-Argument Workhorses)** (Impact: 88.6)
  * `createJournalEntriesForLoanCapitalizedIncomeAmortization` **(Many-Argument Workhorses)** (Impact: 57.6)
  * `createJournalEntriesForLoanBuyDownFeeAmortization` **(Many-Argument Workhorses)** (Impact: 57.6)
  * `createJournalEntriesForLoan` **(Compute Cores)** (Impact: 52.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 145 instances
* *State Mutation (weighted view):* 436
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 403`, `structural_boundaries: 109`, `args: 48`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 146`, `planned_debt: 2`
* *Architecture:* `api: 3`, `import: 24`
* *Defense:* `doc: 11`, `immutability_locks: 378`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.000156
  * `Imports (Out-Degree: 15):` java.math.BigDecimal, java.time.LocalDate, java.util.ArrayList, java.util.LinkedHashMap, java.util.List, java.util.Map, java.util.Objects, lombok.RequiredArgsConstructor...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/service/LoanScheduleAssembler.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 11.213)
- **Top Global Matches:** file_cluster_6: 11.213, file_cluster_4: 11.877, file_cluster_5: 15.704
- **Magnitude:** 1128.74 | **LOC:** 1607 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **121**; blast radius 0.078; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assembleLoanApplicationTermsFrom` **(Many-Argument Workhorses)** (Impact: 106.0)
  * `assempleVariableScheduleFrom` **(Many-Argument Workhorses)** (Impact: 88.6)
  * `updateLoanApplicationAttributes` **(Many-Argument Workhorses)** (Impact: 75.8)
  * `adjustExistingVariations` **(Many-Argument Workhorses)** (Impact: 64.0)
  * `extractLoanTermVariations` **(Many-Argument Workhorses)** (Impact: 36.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 145 instances
* *State Mutation (weighted view):* 511
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 206`, `args: 34`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 221`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 13`, `import: 121`
* *Defense:* `safety: 3`, `doc: 2`, `immutability_locks: 285`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.078
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.000822
  * `Imports (Out-Degree: 95):` com.google.gson.JsonArray, com.google.gson.JsonElement, com.google.gson.JsonObject, java.math.BigDecimal, java.math.MathContext, java.time.LocalDate, java.time.temporal.ChronoField, java.util.ArrayList...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/calc/ProgressiveEMICalculator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.014)
- **Top Global Matches:** file_cluster_5: 9.014, file_cluster_12: 9.288, file_cluster_16: 11.149
- **Magnitude:** 1059.72 | **LOC:** 2137 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 39.1%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **48**; blast radius 0.085; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (91.7%), Guard Balance (formerly Safety Score) (60.5%), Mutation Surface (formerly State Flux) (60.5%), Complexity Load (formerly Cognitive Load) (23.8%)
- **Documentation Coverage:** 77.6119% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `calculateRateFactorPerPeriodForInterest` **(Many-Argument Workhorses)** (Impact: 34.5)
  * `calculatePeriodRatio` **(Many-Argument Workhorses)** (Impact: 28.9)
  * `calculateRateFactorPerPeriod` **(Many-Argument Workhorses)** (Impact: 25.1)
    * *Intent:* /** * Calculate Rate Factor for an exact Period */
  * `recalculateScheduleModelTillDate` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `attachTemporaryScheduleModelReAgedPeriodsToExistingModel` **(Many-Argument Workhorses)** (Impact: 22.3)
    * *Intent:* /** * * Attaching re-aged repayment periods of the new temporary model to existing model repayment p...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 282
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 202`, `structural_boundaries: 218`, `args: 266`, `func_start: 101`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 150`, `planned_debt: 7`
* *Architecture:* `api: 35`, `concurrency: 7`, `import: 48`
* *Defense:* `safety: 23`, `doc: 26`, `immutability_locks: 335`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.000562
  * `Imports (Out-Degree: 28):` jakarta.annotation.Nonnull, jakarta.validation.constraints.NotNull, java.math.BigDecimal, java.math.BigDecimal.ZERO, java.math.MathContext, java.time.LocalDate, java.time.Year, java.time.temporal.ChronoUnit...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/Loan.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.16)
- **Top Global Matches:** file_cluster_5: 8.16, file_cluster_12: 9.972, file_cluster_7: 10.635
- **Magnitude:** 1027.44 | **LOC:** 1848 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **329** in-repo importer(s); it depends on **64**; blast radius 6.558; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (99.8%), Mutation Surface (formerly State Flux) (95.2%), Guard Balance (formerly Safety Score) (68.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.9%)
- **Documentation Coverage:** 96.4824% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Loan` **(Many-Argument Workhorses)** (Impact: 62.9)
  * `findLastAssignmentHistoryRecord` **(Compute Cores)** (Impact: 9.3)
  * `getPrincipalAmountForRepaymentSchedule` **(I/O & Config Routines)** (Impact: 7.9)
  * `getDisbursedAmount` **(I/O & Config Routines)** (Impact: 7.8)
  * `hasMonetaryActivityAfter` **(Compute Cores)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 293
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 314`, `args: 262`, `func_start: 204`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 98`, `state_mutation: 147`, `planned_debt: 2`
* *Architecture:* `api: 215`, `import: 64`
* *Defense:* `safety: 4`, `doc: 7`, `immutability_locks: 193`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.558
  * `Choke Point (Betweenness):` 0.003399 | `Ripple Effect (Closeness):` 0.071789
  * `Imports (Out-Degree: 41):` jakarta.persistence.CascadeType, jakarta.persistence.Column, jakarta.persistence.Convert, jakarta.persistence.Embedded, jakarta.persistence.Entity, jakarta.persistence.Enumerated, jakarta.persistence.FetchType, jakarta.persistence.JoinColumn...
  * `Imported By (In-Degree: 329):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/serialization/LoanApplicationValidator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.318)
- **Top Global Matches:** file_cluster_4: 10.318, file_cluster_6: 12.427, file_cluster_12: 13.233
- **Magnitude:** 975.62 | **LOC:** 2267 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **113**; blast radius 0.09; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.6%), Complexity Load (formerly Cognitive Load) (33.1%), Mutation Surface (formerly State Flux) (30.9%)
- **Documentation Coverage:** 96.5517% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateForModify` **(Many-Argument Workhorses)** (Impact: 193.9)
  * `validateForCreate` **(Many-Argument Workhorses)** (Impact: 129.8)
  * `validateLoanMultiDisbursementDate` **(Many-Argument Workhorses)** (Impact: 42.8)
  * `validateApproval` **(Many-Argument Workhorses)** (Impact: 41.7)
  * `validateSubmittedOnDate` **(Many-Argument Workhorses)** (Impact: 30.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 224
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 248`, `args: 51`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 105`, `state_mutation: 88`, `dead_code: 1`, `planned_debt: 6`
* *Architecture:* `api: 21`, `import: 113`
* *Defense:* `doc: 3`, `immutability_locks: 295`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.09
  * `Choke Point (Betweenness):` 6.9e-05 | `Ripple Effect (Closeness):` 0.00141
  * `Imports (Out-Degree: 94):` com.google.gson.JsonArray, com.google.gson.JsonElement, com.google.gson.JsonObject, com.google.gson.reflect.TypeToken, java.lang.reflect.Type, java.math.BigDecimal, java.time.LocalDate, java.util.ArrayList...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanChargeService.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.857)
- **Top Global Matches:** file_cluster_5: 9.857, file_cluster_12: 10.924, file_cluster_7: 11.821
- **Magnitude:** 974.76 | **LOC:** 965 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **38**; blast radius 0.103; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.9%)
- **Documentation Coverage:** 92.7273% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Many-Argument Workhorses)** (Impact: 44.4)
  * `update` **(Many-Argument Workhorses)** (Impact: 41.6)
  * `calculateAmountPercentageAppliedTo` **(Compute Cores)** (Impact: 34.3)
  * `populateDerivedFields` **(Many-Argument Workhorses)** (Impact: 34.3)
  * `create` **(Many-Argument Workhorses)** (Impact: 29.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 128 instances
* *State Mutation (weighted view):* 426
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 127`, `args: 55`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 170`
* *Architecture:* `api: 21`, `import: 38`
* *Defense:* `doc: 3`, `immutability_locks: 166`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.103
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.011498
  * `Imports (Out-Degree: 28):` java.math.BigDecimal, java.time.LocalDate, java.util.ArrayList, java.util.Collection, java.util.HashMap, java.util.HashSet, java.util.LinkedHashMap, java.util.List...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/api/LoanProductsApiResourceSwagger.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.685)
- **Top Global Matches:** file_cluster_13: 7.685, file_cluster_0: 7.817, file_cluster_16: 8.727
- **Magnitude:** 924.38 | **LOC:** 1945 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (27.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.1%), Connectivity (formerly Api Exposure) (16.2%)
- **Documentation Coverage:** 78.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LoanProductsApiResourceSwagger` **(Encapsulated Accessors)** (Impact: 1.1)
  * `LoanProductChargeData` **(Encapsulated Accessors)** (Impact: 1.1)
  * `LoanProductChargeToGLAccountMapper` **(Encapsulated Accessors)** (Impact: 1.1)
  * `PostLoanProductsRequest` **(Encapsulated Accessors)** (Impact: 1.1)
  * `AllowAttributeOverrides` **(Encapsulated Accessors)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 90`, `args: 75`, `func_start: 75`, `class_start: 79`
* *Risk/State:* `duplicate_logic: 10`
* *Architecture:* `api: 809`, `import: 10`
* *Defense:* `doc: 614`, `immutability_locks: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000156
  * `Imports (Out-Degree: 5):` io.swagger.v3.oas.annotations.media.Schema, java.math.BigDecimal, java.time.LocalDate, java.util.List, java.util.Set, org.apache.fineract.accounting.glaccount.data.GLAccountData, org.apache.fineract.infrastructure.codes.api.CodeValuesApiResourceSwagger.GetCodeValuesDataResponse, org.apache.fineract.infrastructure.core.data.EnumOptionData...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanAccrualsProcessingServiceImpl.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.657)
- **Top Global Matches:** file_cluster_5: 8.657, file_cluster_12: 10.168, file_cluster_7: 11.352
- **Magnitude:** 898.34 | **LOC:** 1304 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **74**; blast radius 0.09; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.7%), Guard Balance (formerly Safety Score) (65.4%), Complexity Load (formerly Cognitive Load) (46.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.9%)
- **Documentation Coverage:** 73.7705% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addAccruals` **(Many-Argument Workhorses)** (Impact: 76.8)
    * *Intent:* // PeriodicAccruals
  * `reprocessPeriodicAccruals` **(Many-Argument Workhorses)** (Impact: 35.4)
    * *Intent:* // ReprocessAccruals
  * `addInterestAccrual` **(Many-Argument Workhorses)** (Impact: 32.1)
  * `reprocessNonPeriodicAccruals` **(Many-Argument Workhorses)** (Impact: 31.1)
  * `determineFeeDetails` **(Many-Argument Workhorses)** (Impact: 28.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 84 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 299
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 192`, `args: 83`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 131`, `planned_debt: 3`, `unreferenced_by_name: 5`
* *Architecture:* `api: 12`, `concurrency: 3`, `import: 74`
* *Defense:* `safety: 65`, `doc: 9`, `immutability_locks: 219`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.09
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.001181
  * `Imports (Out-Degree: 49):` java.math.BigDecimal, java.time.LocalDate, java.util.ArrayList, java.util.Collection, java.util.Comparator, java.util.HashMap, java.util.List, java.util.Map...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepaymentScheduleInstallment.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.238)
- **Top Global Matches:** file_cluster_5: 9.238, file_cluster_7: 9.802, file_cluster_12: 9.864
- **Magnitude:** 886.52 | **LOC:** 1303 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **92** in-repo importer(s); it depends on **27**; blast radius 1.317; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.6%), Connectivity (formerly Api Exposure) (93.2%), Guard Balance (formerly Safety Score) (75.7%), Complexity Load (formerly Cognitive Load) (71.9%)
- **Documentation Coverage:** 99.2509% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getPaymentFunction` **(Callbacks & Closures)** (Impact: 24.8)
  * `reduceAdvanceAndLateTotalsForRepaymentPeriod` **(Stateful Encapsulated Methods)** (Impact: 17.1)
  * `isOutstandingBalanceNotZero` **(Callbacks & Closures)** (Impact: 10.8)
  * `resetDerivedComponents` **(I/O & Config Routines)** (Impact: 10.7)
  * `trackAdvanceAndLateTotalsForRepaymentPeriod` **(Stateful Encapsulated Methods)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 293
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 186`, `args: 175`, `func_start: 139`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 157`, `planned_debt: 1`
* *Architecture:* `api: 131`, `import: 27`
* *Defense:* `doc: 2`, `immutability_locks: 235`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.317
  * `Choke Point (Betweenness):` 0.000218 | `Ripple Effect (Closeness):` 0.05387
  * `Imports (Out-Degree: 12):` jakarta.persistence.CascadeType, jakarta.persistence.Column, jakarta.persistence.Entity, jakarta.persistence.FetchType, jakarta.persistence.JoinColumn, jakarta.persistence.ManyToOne, jakarta.persistence.OneToMany, jakarta.persistence.Table...
  * `Imported By (In-Degree: 92):` (Excluded from Brief to save tokens)

### `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/api/LoansApiResourceSwagger.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.206)
- **Top Global Matches:** file_cluster_13: 7.206, file_cluster_16: 8.277, file_cluster_2: 8.715
- **Magnitude:** 868.7 | **LOC:** 1946 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 28.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.07; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (55.0%), Connectivity (formerly Api Exposure) (16.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.3%)
- **Documentation Coverage:** 71.0145% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LoansApiResourceSwagger` **(Encapsulated Accessors)** (Impact: 1.1)
  * `GetLoansApprovalTemplateResponse` **(Encapsulated Accessors)** (Impact: 1.1)
  * `GetLoanCurrency` **(Encapsulated Accessors)** (Impact: 1.1)
  * `GetLoansTemplateResponse` **(Encapsulated Accessors)** (Impact: 1.1)
  * `GetLoansTemplateTimeline` **(Encapsulated Accessors)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 81`, `args: 69`, `func_start: 69`, `class_start: 70`
* *Risk/State:* None
* *Architecture:* `api: 759`, `import: 9`
* *Defense:* `doc: 724`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` io.swagger.v3.oas.annotations.media.Schema, java.math.BigDecimal, java.time.LocalDate, java.util.List, java.util.Map, java.util.Set, org.apache.fineract.infrastructure.core.data.EnumOptionData, org.apache.fineract.infrastructure.core.data.StringEnumOptionData...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-tests/src/test/java/org/apache/fineract/integrationtests/AdvancedPaymentAllocationLoanRepaymentScheduleTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 9.945)
- **Top Global Matches:** file_cluster_7: 9.945, file_cluster_5: 10.961, file_cluster_12: 11.058
- **Magnitude:** 867.16 | **LOC:** 6583 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **85**; blast radius 0.07; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.0%), Concurrency Surface (formerly Concurrency) (20.2%), Complexity Load (formerly Cognitive Load) (10.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `uc124` **(I/O & Config Routines)** (Impact: 8.5)
    * *Intent:* // UC124: Advanced payment allocation, MIR, CBR and Chargeback on overpaid loan // ADVANCED_PAYMENT_...
  * `uc156` **(I/O & Config Routines)** (Impact: 7.0)
    * *Intent:* // UC156: Loan Transaction reprocess
  * `uc24` **(I/O & Config Routines)** (Impact: 6.3)
    * *Intent:* // UC24: Merchant issued credit reverse-replay // ADVANCED_PAYMENT_ALLOCATION_STRATEGY // 1. Disburs...
  * `createLoanForRoundingMethodValidation` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `uc144` **(Annotated & Test Methods)** (Impact: 5.7)
    * *Intent:* // UC144: Advanced payment allocation with Interest, // ADVANCED_PAYMENT_ALLOCATION_STRATEGY // 1. C...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 572`, `args: 237`, `func_start: 102`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 534`, `state_mutation: 259`, `unreferenced_by_name: 85`
* *Architecture:* `api: 88`, `concurrency: 40`, `import: 85`
* *Defense:* `doc: 1`, `test: 530`, `immutability_locks: 258`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` io.restassured.builder.RequestSpecBuilder, io.restassured.builder.ResponseSpecBuilder, io.restassured.http.ContentType, io.restassured.specification.RequestSpecification, io.restassured.specification.ResponseSpecification, java.math.BigDecimal, java.time.LocalDate, java.util.ArrayList...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-tests/src/test/java/org/apache/fineract/integrationtests/ClientSavingsIntegrationTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.934)
- **Top Global Matches:** file_cluster_5: 8.934, file_cluster_7: 8.938, file_cluster_12: 9.925
- **Magnitude:** 866.7 | **LOC:** 3614 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **48**; blast radius 0.07; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (75.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.9%), Complexity Load (formerly Cognitive Load) (25.3%), Dead Code Surface (formerly Dead Code) (13.7%)
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
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 534
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 285`, `args: 56`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 227`, `state_mutation: 488`, `dead_code: 31`, `unreferenced_by_name: 47`
* *Architecture:* `api: 55`, `import: 48`
* *Defense:* `safety: 4`, `doc: 95`, `test: 343`, `immutability_locks: 500`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` io.restassured.builder.RequestSpecBuilder, io.restassured.builder.ResponseSpecBuilder, io.restassured.http.ContentType, io.restassured.specification.RequestSpecification, io.restassured.specification.ResponseSpecification, java.math.BigDecimal, java.text.DateFormat, java.text.DecimalFormat...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/service/export/ResponseHolder.java` (JAVA) | Magnitude: 5.32 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 9, import: 6, encapsulation: 5
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/configuration/service/GlobalConfigurationValidationService.java` (JAVA) | Magnitude: 16.54 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 22, import: 12, encapsulation: 6
- `fineract-provider/src/main/java/org/apache/fineract/cob/service/InlineLoanCOBExecutionDataParser.java` (JAVA) | Magnitude: 8.58 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 14, import: 10, core_var_decl: 4
- `fineract-provider/src/test/java/org/apache/fineract/infrastructure/dataqueries/service/DatatableWriteServiceImplTest.java` (JAVA) | Magnitude: 26.86 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 144, test: 70, structural_boundaries: 69, import: 34
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/domain/AbstractAuditableWithUTCDateTimeCustom.java` (JAVA) | Magnitude: 10.94 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 25, decorators: 20, import: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/database/DatabasePasswordEncryptor.java` (JAVA) | Magnitude: 21.38 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 18, args: 14, core_var_decl: 10
- `fineract-war/build.gradle` (GROOVY) | Magnitude: 22.98 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 116, state_mutation: 16, core_var_decl: 16, design_camel_case: 11
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/shareproducts/domain/ShareProductDividentPayOutDetailsRepositoryWrapper.java` (JAVA) | Magnitude: 13.96 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 9, api: 6, args: 5
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/domain/ShareAccountRepositoryWrapper.java` (JAVA) | Magnitude: 13.82 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 9, api: 6, args: 5
- `fineract-provider/src/test/java/org/apache/fineract/infrastructure/classpath/ClasspathDuplicatesStepDefinitions.java` (JAVA) | Magnitude: 27.92 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 114, structural_boundaries: 32, import: 14, core_var_decl: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/domain/InterestCalculationPeriodMethod.java` (JAVA) | Magnitude: 22.42 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 7, args: 7, func_start: 6
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/domain/InterestMethod.java` (JAVA) | Magnitude: 22.42 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 7, args: 7, func_start: 6
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/reaging/LoanReAgeInterestHandlingType.java` (JAVA) | Magnitude: 5.7 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 11, import: 5, args: 3
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/error/ErrorResponse.java` (JAVA) | Magnitude: 11.12 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 18, decorators: 9, import: 8
- `fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/service/migration/TenantDatabaseStateVerifier.java` (JAVA) | Magnitude: 19.72 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 19, core_var_decl: 12, encapsulation: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/LoanProductWithRepaymentDueEventConfigurationTest.java` (JAVA) | Magnitude: 22.86 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 35, core_var_decl: 21, design_camel_case: 21
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/codes/domain/Code.java` (JAVA) | Magnitude: 19.82 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 29, indent_spaces: 29, import: 18, decorators: 9
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/BatchLoanIntegrationTest.java` (JAVA) | Magnitude: 15.56 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 85, core_var_decl: 28, structural_boundaries: 23, design_camel_case: 22
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/client/feign/modules/LoanTestData.java` (JAVA) | Magnitude: 122.82 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 149, api: 93, immutability_locks: 54, core_var_decl: 41
- `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/common/BusinessDateStepDef.java` (JAVA) | Magnitude: 26.12 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 28, import: 18, core_var_decl: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `fineract-provider/src/test/java/org/apache/fineract/batch/command/internal/GetReagePreviewByLoanExternalIdCommandStrategyTest.java` (JAVA) | Magnitude: 47.6 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 109, structural_boundaries: 47, immutability_locks: 31, test: 30
- `fineract-core/src/main/java/org/apache/fineract/organisation/monetary/serialization/MoneyDeserializer.java` (JAVA) | Magnitude: 4.62 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 14, import: 9, indent_spaces: 7, decorators: 3
- `fineract-provider/src/test/java/org/apache/fineract/batch/command/internal/GetReagePreviewByLoanIdCommandStrategyTest.java` (JAVA) | Magnitude: 47.62 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 106, structural_boundaries: 46, immutability_locks: 31, test: 30
- `fineract-investor/src/main/java/org/apache/fineract/investor/exception/ExternalAssetOwnerNotFoundException.java` (JAVA) | Magnitude: 6.44 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 5, api: 3, args: 2
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/bulkimport/service/BulkImportWorkbookPopulatorService.java` (JAVA) | Magnitude: 4.4 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/data/CommandProcessingResult.java` (JAVA) | Magnitude: 89.0 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 115, immutability_locks: 75, safety_bypasses: 34, structural_boundaries: 31
- `fineract-provider/src/main/java/org/apache/fineract/infrastructure/dataqueries/service/DatatableUtil.java` (JAVA) | Magnitude: 169.58 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 175, structural_boundaries: 56, safety_bypasses: 53, immutability_locks: 40
- `fineract-core/src/main/java/org/apache/fineract/portfolio/group/data/GroupRoleData.java` (JAVA) | Magnitude: 3.46 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 7, import: 5, immutability_locks: 5
- `fineract-provider/src/main/java/org/apache/fineract/useradministration/data/PasswordValidationPolicyData.java` (JAVA) | Magnitude: 8.86 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 14, immutability_locks: 8, structural_boundaries: 4, safety_bypasses: 4
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/self/registration/data/SelfServiceRegistrationData.java` (JAVA) | Magnitude: 21.6 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 40, immutability_locks: 21, safety_bypasses: 10, state_mutation: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `fineract-provider/src/main/java/org/apache/fineract/infrastructure/configuration/async/CustomAsyncExceptionHandler.java` (JAVA) | Magnitude: 6.8 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 7, telemetry: 4, import: 3
- `fineract-provider/src/main/java/org/apache/fineract/infrastructure/reportmailingjob/data/ReportMailingJobRunHistoryData.java` (JAVA) | Magnitude: 12.54 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, state_mutation: 7, encapsulation: 7
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/repaymentwithpostdatedchecks/data/PostDatedChecksData.java` (JAVA) | Magnitude: 17.26 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: immutability_locks: 25, indent_spaces: 23, encapsulation: 9, state_mutation: 8
- `fineract-provider/src/main/java/org/apache/fineract/organisation/office/starter/OrganisationOfficeConfiguration.java` (JAVA) | Magnitude: 12.24 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 27, import: 19, indent_spaces: 19, api: 5
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/address/data/ClientAddressData.java` (JAVA) | Magnitude: 12.8 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 17, immutability_locks: 16, encapsulation: 6, state_mutation: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `fineract-provider/src/main/java/org/apache/fineract/infrastructure/core/service/migration/TenantDatabaseUpgradeService.java` (JAVA) | Magnitude: 63.14 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 144, structural_boundaries: 52, import: 27, telemetry: 26
- `fineract-provider/src/main/java/org/apache/fineract/infrastructure/reportmailingjob/ReportMailingJobConstants.java` (JAVA) | Magnitude: 35.16 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 45, immutability_locks: 36, api: 33, globals: 32
- `fineract-investor/src/main/java/org/apache/fineract/investor/service/ExternalAssetOwnerLoanProductAttributesWriteServiceImpl.java` (JAVA) | Magnitude: 54.2 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 111, structural_boundaries: 62, import: 33, core_var_decl: 17
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/configuration/api/GlobalConfigurationConstants.java` (JAVA) | Magnitude: 65.42 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: api: 63, immutability_locks: 63, indent_spaces: 63, globals: 62
- `fineract-investor/src/main/java/org/apache/fineract/investor/api/ExternalAssetOwnerLoanProductAttributesApiConstants.java` (JAVA) | Magnitude: 2.4 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 7, immutability_locks: 6, globals: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `fineract-provider/src/main/java/org/apache/fineract/infrastructure/bulkimport/constants/TemplatePopulateImportConstants.java` (JAVA) | Magnitude: 97.06 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 95, api: 94, immutability_locks: 94, globals: 93
- `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/data/AccountTypeExpenseOptions.java` (JAVA) | Magnitude: 4.8 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 2, api: 2, args: 1
- `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/data/AccountTypeLiabilityOptions.java` (JAVA) | Magnitude: 4.8 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 2, api: 2, args: 1
- `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/data/ChargeOffBehaviour.java` (JAVA) | Magnitude: 4.8 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 2, api: 2, args: 1
- `fineract-core/src/main/java/org/apache/fineract/portfolio/search/data/SearchData.java` (JAVA) | Magnitude: 17.94 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 26, immutability_locks: 22, state_mutation: 11, encapsulation: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `.github/workflows/stale.yml` (YAML) | Magnitude: 15.42 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 17, args: 5, structural_boundaries: 2, events: 2
- `fineract-accounting/src/main/java/org/apache/fineract/accounting/journalentry/exception/JournalEntryRuntimeException.java` (JAVA) | Magnitude: 4.04 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, api: 2, args: 1
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/exception/LoanProductGeneralRuleException.java` (JAVA) | Magnitude: 4.04 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, api: 2, doc: 2
- `fineract-provider/src/main/java/org/apache/fineract/infrastructure/campaigns/sms/exception/SmsRuntimeException.java` (JAVA) | Magnitude: 4.04 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, api: 2, args: 1
- `fineract-provider/src/main/java/org/apache/fineract/interoperation/exception/InteropKycDataNotFoundException.java` (JAVA) | Magnitude: 4.04 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, api: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/shareproducts/serialization/ShareProductDataSerializer.java` (JAVA) | Magnitude: 284.12 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 391, core_var_decl: 98, structural_boundaries: 73, design_camel_case: 73
- `.github/workflows/verify-api-backward-compatibility.yml` (YAML) | Magnitude: 55.08 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 185, branch: 32, core_var_decl: 23, design_snake_case: 18
- `fineract-core/src/main/java/org/apache/fineract/commands/service/SynchronousCommandProcessingService.java` (JAVA) | Magnitude: 304.58 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 270, structural_boundaries: 99, branch: 73, core_var_decl: 61
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanproduct/service/LoanProductWritePlatformServiceJpaRepositoryImpl.java` (JAVA) | Magnitude: 182.82 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 285, structural_boundaries: 94, immutability_locks: 77, core_var_decl: 64
- `fineract-provider/src/test/java/org/apache/fineract/infrastructure/event/external/service/serialization/serializer/loan/LoanAccountDelinquencyRangeEventSerializerTest.java` (JAVA) | Magnitude: 0.19 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 311, structural_boundaries: 224, test: 142, import: 94

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `fineract-provider/src/main/java/org/apache/fineract/infrastructure/jobs/service/StuckJobListener.java` (JAVA) | Magnitude: 14.98 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 28, import: 22, immutability_locks: 13
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/fixeddeposit/FixedDepositAccountHelper.java` (JAVA) | Magnitude: 307.56 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 433, immutability_locks: 151, state_mutation: 110, core_var_decl: 92
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/ClientSavingsIntegrationTest.java` (JAVA) | Magnitude: 866.7 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 2446, core_var_decl: 1235, design_camel_case: 1028, immutability_locks: 500
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/ClientLoanMultipleDisbursementsIntegrationTest.java` (JAVA) | Magnitude: 140.82 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 268, core_var_decl: 107, design_camel_case: 89, state_mutation: 73
- `fineract-provider/src/test/java/org/apache/fineract/cob/common/InitialisationTaskletStepDefinitions.java` (JAVA) | Magnitude: 19.62 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 35, import: 22, core_var_decl: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `fineract-provider/src/main/java/org/apache/fineract/accounting/journalentry/service/AccrualBasedAccountingProcessorForLoan.java` (JAVA) | Magnitude: 1472.16 | Delta: **0.184** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1704, core_var_decl: 419, branch: 403, immutability_locks: 378
- `fineract-working-capital-loan/src/main/java/org/apache/fineract/portfolio/workingcapitalloanproduct/service/WorkingCapitalLoanProductWritePlatformServiceImpl.java` (JAVA) | Magnitude: 184.04 | Delta: **0.26** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 275, immutability_locks: 77, core_var_decl: 67, structural_boundaries: 65

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `fineract-core/src/main/java/org/apache/fineract/portfolio/search/data/AdvancedQueryRequest.java` (JAVA) | Magnitude: 5.78 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 9, args: 4, safety_bypasses: 4
- `fineract-validation/src/main/java/org/apache/fineract/validation/constraints/LocalDateValidator.java` (JAVA) | Magnitude: 20.04 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 26, import: 9, state_mutation: 7
- `fineract-provider/src/main/java/org/apache/fineract/cob/resolver/BusinessDateResolver.java` (JAVA) | Magnitude: 12.44 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 8, args: 6, branch: 5
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/ClientExternalIdTest.java` (JAVA) | Magnitude: 58.0 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 190, core_var_decl: 59, design_camel_case: 59, test: 49
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/loan/reamortization/LoanReAmortizationIntegrationTest.java` (JAVA) | Magnitude: 139.2 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 788, safety_bypasses: 150, args: 69, core_var_decl: 69

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/service/LoanProductInterestRecalculationDetailsAssembler.java` (JAVA) | Magnitude: 37.54 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 63, core_var_decl: 29, design_camel_case: 29, design_long_vars: 15
- `fineract-provider/src/test/java/org/apache/fineract/cob/loan/LoanItemReaderTest.java` (JAVA) | Magnitude: 63.3 | Delta: **0.21** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 95, structural_boundaries: 56, test: 36, import: 31

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/loan/LoanReAgingStepDef.java` -> Churn: **66.77%** | Cog Load: 69.0811% | Debt: 0.0%
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/LoanRepaymentScheduleInstallment.java` -> Churn: **66.44%** | Cog Load: 71.8521% | Debt: 7.9261%
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/LoanApplicationTerms.java` -> Churn: **63.4%** | Cog Load: 84.3253% | Debt: 8.8223%
- `fineract-core/src/main/java/org/apache/fineract/commands/service/CommandWrapperBuilder.java` -> Churn: **56.8%** | Cog Load: 89.4132% | Debt: 7.6892%
- `.github/workflows/verify-liquibase-backward-compatibility.yml` -> Churn: **56.15%** | Cog Load: 7.3588% | Debt: 79.35%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/loanschedule/domain/AbstractCumulativeLoanScheduleGenerator.java` -> **Attila Budai** (100.0% isolated ownership) | Magnitude: 2249.44
- `integration-tests/src/test/java/org/apache/fineract/integrationtests/common/BatchHelper.java` -> **Adam Saghy** (100.0% isolated ownership) | Magnitude: 667.74
- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/transactionprocessor/AbstractLoanRepaymentScheduleTransactionProcessor.java` -> **Jose Alberto Hernandez** (100.0% isolated ownership) | Magnitude: 661.66
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/savings/domain/RecurringDepositAccount.java` -> **Adam Saghy** (100.0% isolated ownership) | Magnitude: 657.18
- `fineract-core/src/main/java/org/apache/fineract/portfolio/calendar/service/CalendarUtils.java` -> **Aman-Mittal** (100.0% isolated ownership) | Magnitude: 655.38

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `fineract-loan/src/main/java/org/apache/fineract/portfolio/loanaccount/domain/Loan.java` -> **Severity: 0.324** (Bridge: 0.0034 * Flux: 95.2332%)
- `fineract-savings/src/main/java/org/apache/fineract/portfolio/savings/domain/SavingsAccount.java` -> **Severity: 0.098** (Bridge: 0.001 * Flux: 99.7021%)
- `fineract-core/src/main/java/org/apache/fineract/useradministration/domain/AppUser.java` -> **Severity: 0.085** (Bridge: 0.0009 * Flux: 98.9808%)
- `fineract-core/src/main/java/org/apache/fineract/portfolio/group/domain/Group.java` -> **Severity: 0.082** (Bridge: 0.0008 * Flux: 99.7275%)
- `fineract-provider/src/main/java/org/apache/fineract/portfolio/loanaccount/api/LoanTransactionsApiResource.java` -> **Severity: 0.081** (Bridge: 0.0008 * Flux: 98.2888%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/DateUtils.java` -> **Severity: 13.087** (Embedded: 0.1636 * Error Risk: 80.0%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/api/JsonCommand.java` -> **Severity: 12.351** (Embedded: 0.1544 * Error Risk: 80.0%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/MathUtil.java` -> **Severity: 12.121** (Embedded: 0.1437 * Error Risk: 84.3715%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/ThreadLocalContextUtil.java` -> **Severity: 11.494** (Embedded: 0.1437 * Error Risk: 80.0%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/data/DataValidatorBuilder.java` -> **Severity: 10.741** (Embedded: 0.1343 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/api/JsonCommand.java` -> **Severity: 1620.625** (Blast Radius: 16.676 * Doc Risk: 97.1831%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/data/CommandProcessingResult.java` -> **Severity: 1434.9** (Blast Radius: 14.349 * Doc Risk: 100.0%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/domain/AbstractPersistableCustom.java` -> **Severity: 1141.8** (Blast Radius: 11.418 * Doc Risk: 100.0%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/service/DateUtils.java` -> **Severity: 1076.885** (Blast Radius: 11.363 * Doc Risk: 94.7712%)
- `fineract-core/src/main/java/org/apache/fineract/infrastructure/core/data/ApiParameterError.java` -> **Severity: 905.464** (Blast Radius: 9.842 * Doc Risk: 92.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 2546 literal sites + 254 sites through wrappers = 2800

- `fail` (function, panics_and_aborts, primitive): 103 call sites in 21 files -- `fineract-client-feign/src/main/java/org/apache/fineract/client/feign/util/FeignCalls.java`
- `executeVoid` (function, panics_and_aborts, primitive): 28 call sites in 18 files -- `fineract-client-feign/src/main/java/org/apache/fineract/client/feign/util/FeignCalls.java`
- `toJson` (function, panics_and_aborts, primitive): 19 call sites in 1 files -- `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/common/BatchApiStepDef.java`
- `handleDataIntegrityIssues` (function, panics_and_aborts, primitive): 13 call sites in 1 files -- `fineract-provider/src/main/java/org/apache/fineract/portfolio/shareaccounts/service/ShareAccountWritePlatformServiceJpaRepositoryImpl.java`
- `raiseValidationError` (function, panics_and_aborts, primitive): 9 call sites in 1 files -- `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/domain/AdvancedPaymentAllocationsValidator.java`
- `failVoid` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `fineract-client-feign/src/main/java/org/apache/fineract/client/feign/util/FeignCalls.java`
- `fromJson` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `fineract-e2e-tests-core/src/test/java/org/apache/fineract/test/stepdef/common/BatchApiStepDef.java`
- `raiseValidationError` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `fineract-working-capital-loan/src/main/java/org/apache/fineract/portfolio/workingcapitalloanproduct/domain/WorkingCapitalAdvancedPaymentAllocationsValidator.java`
- `raiseValidationError` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `fineract-progressive-loan/src/main/java/org/apache/fineract/portfolio/loanproduct/domain/CreditAllocationsValidator.java`
- `write` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `fineract-document/src/test/java/org/apache/fineract/infrastructure/contentstore/processor/ContentProcessorTest.java`
- `handleAPIIntegrityIssues` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `fineract-provider/src/main/java/org/apache/fineract/infrastructure/creditbureau/service/ThitsaWorksCreditBureauIntegrationWritePlatformServiceImpl.java`
- `handleTokenDataIntegrityIssues` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `fineract-provider/src/main/java/org/apache/fineract/infrastructure/creditbureau/service/CreditReportWritePlatformServiceImpl.java`
*(+21 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 184911 call pairs -- scoped 40.7%, unique 0.2%, ambiguous 29.1%, external 29.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| java | 184501 | 40.8% | 0.2% | 29.1% | 29.9% |
| groovy | 354 | 2.0% | 0.0% | 38.1% | 59.9% |
| shell | 44 | 11.4% | 0.0% | 0.0% | 88.6% |
| html | 12 | 0.0% | 0.0% | 0.0% | 100.0% |

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
