# ARCHITECTURAL_BRIEF: workers-sdk
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/cloudflare/workers-sdk.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 4310 analyzed artifact(s), 406338 LOC.
- **Load-bearing artifact:** `packages/wrangler/src/logger.ts` -- 284 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/wrangler/src/index.ts` -- pulls in 224 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `packages/wrangler/e2e/dev.test.ts` at magnitude 22633.11 (structural weight, not risk).
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
| Total Artifacts | 4635 |
| Analyzed Artifacts (Scanned) | 4310 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 325 |
| Total LOC | 406338 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 93.0% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7768 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1976 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.458 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 262 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2805 | 388375 | 65.1% |
| JSON | 749 | 9120 | 17.4% |
| PLAINTEXT | 227 | 7 | 5.3% |
| JAVASCRIPT | 201 | 6266 | 4.7% |
| MARKDOWN | 151 | 0 | 3.5% |
| HTML | 105 | 1494 | 2.4% |
| XML | 26 | 97 | 0.6% |
| CSS | 14 | 622 | 0.3% |
| PYTHON | 9 | 58 | 0.2% |
| SQLITE | 7 | 28 | 0.2% |
| DOCKERFILE | 6 | 56 | 0.1% |
| BINARY_THREAT | 4 | 4 | 0.1% |
| PHP | 3 | 146 | 0.1% |
| SHELL | 2 | 36 | 0.0% |
| MAKEFILE | 1 | 29 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `6.519`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +6.52; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 43%, Declarative / Non-Code 20%, Large Core Modules (2) 8%, Large Core Modules (3) 5%, Compute Cores Files 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3917 | 90.9% |
| Unknown | 11 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 371 | 8.6% |
| Static: Minified & Vendor Opaque Mass | 11 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 325*

**Composition by Extension & Reason:**
- `no_extension`: 95x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 24x Unsupported Format (.undeterminable)
- `.yml`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 3x Excluded (Machine-Generated Source Code Signature: 8 LOC), 3x Excluded (Machine-Generated Source Code Signature: 5 LOC), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 64 LOC), 1x Excluded (Machine-Generated Source Code Signature: 161 LOC)
- `.patch`: 15x Excluded (Unsupported Extension: '.patch')
- `.wasm`: 7x Excluded (Unsupported Extension: '.wasm'), 4x Excluded (Binary Format Detected)
- `.json`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3161 LOC)
- `.vars`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1765 LOC), 1x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.png`: 8x Excluded (Explicitly Denied Extension: '.png')
- `.toml`: 6x Excluded (Unsupported Extension: '.toml')
- `.gif`: 6x Excluded (Explicitly Denied Extension: '.gif')
- `.snap`: 4x Unsupported Format (.snap), 2x Excluded (Unsupported Extension: '.snap')
- `.staging`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 16.4 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 19.0 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 19.8 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 33.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 17.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 64.6 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 7.5 | 1.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 70.9 | 9.1 | 4.4 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 35.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1863 | 515 | 1 | `packages/workers-utils/tests/config/validation/normalize-and-validate-config.test.ts` |
| cleanup | 416 | 170 | 0 | `packages/wrangler/src/__tests__/middleware.test.ts` |
| guards | 11940 | 1386 | 7 | `packages/quick-edit-extension/vscode.d.ts` |
| danger | 3638 | 798 | 2 | `packages/workers-utils/tests/config/validation/normalize-and-validate-config.test.ts` |
| concurrency | 32173 | 1668 | 16 | `packages/miniflare/test/index.spec.ts` |
| connectivity | 9884 | 2411 | 5 | `packages/quick-edit-extension/vscode.d.ts` |
| io | 14504 | 1458 | 8 | `packages/miniflare/test/index.spec.ts` |
| crypto | 3 | 3 | 0 | `fixtures/isomorphic-random-example/src/node.js` |
| ipc | 1778 | 360 | 0 | `packages/wrangler/src/__tests__/versions/versions.deploy.test.ts` |
| time | 815 | 265 | 0 | `packages/wrangler/src/__tests__/metrics.test.ts` |
| serialization | 1582 | 473 | 1 | `packages/workers-utils/src/config/validation.ts` |
| regex | 965 | 346 | 0 | `packages/local-explorer-ui/src/drivers/sqlite/parsers.ts` |
| events | 3215 | 655 | 2 | `packages/wrangler/src/pipelines/cli/setup.ts` |
| tests | 25448 | 904 | 10 | `packages/workers-utils/tests/config/validation/normalize-and-validate-config.test.ts` |
| docs | 6733 | 929 | 2 | `packages/quick-edit-extension/vscode.d.ts` |
| debt | 1559 | 475 | 1 | `packages/quick-edit-extension/vscode.d.ts` |
| mutation | 51323 | 2403 | 30 | `packages/workers-utils/src/config/validation.ts` |
| dead_code | 1005 | 349 | 0 | `packages/quick-edit-extension/vscode.d.ts` |
| credential | 41 | 17 | 0 | `packages/wrangler/src/__tests__/containers/deploy.test.ts` |
| threat | 435 | 147 | 0 | `packages/wrangler/src/__tests__/core/handle-errors.test.ts` |
| ml_ai | 407 | 122 | 0 | `packages/miniflare/test/plugins/email/index.spec.ts` |
| ui | 2710 | 230 | 0 | `packages/local-explorer-ui/src/routes/workflows/$workflowName/$instanceId.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/miniflare/test/index.spec.ts` (Hits: 403)
- `packages/wrangler/src/__tests__/dev.test.ts` (Hits: 254)
- `packages/wrangler/src/__tests__/pages/deploy.test.ts` (Hits: 246)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **logger.ts** (`packages/wrangler/src/logger.ts`) — 284 inbound connections
2. **create-command.ts** (`packages/wrangler/src/core/create-command.ts`) — 218 inbound connections
3. **run-wrangler.ts** (`packages/wrangler/src/__tests__/helpers/run-wrangler.ts`) — 131 inbound connections
4. **vite-plugin.ts** (`packages/wrangler/src/autoconfig/frameworks/utils/vite-plugin.ts`) — 117 inbound connections
5. **mock-account-id.ts** (`packages/wrangler/src/__tests__/helpers/mock-account-id.ts`) — 111 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`packages/wrangler/src/index.ts`) — 224 outbound dependencies
2. **deploy.ts** (`packages/wrangler/src/deploy/deploy.ts`) — 54 outbound dependencies
3. **templates.ts** (`packages/create-cloudflare/src/templates.ts`) — 48 outbound dependencies
4. **upload.ts** (`packages/wrangler/src/versions/upload.ts`) — 47 outbound dependencies
5. **index.ts** (`packages/miniflare/src/index.ts`) — 43 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `printBindings` **(Many-Argument Workhorses)** (@ `packages/wrangler/src/utils/print-bindings.ts`) -> Impact: **504.3** | LOC: 875
  * *Intent:* /** * Print all the bindings a worker would have access to. * Accepts StartDevWorkerInput["bindings"] format */
- `generatePerEnvironmentTypes` **(Many-Argument Workhorses)** (@ `packages/wrangler/src/type-generation/index.ts`) -> Impact: **432.0** | LOC: 418
  * *Intent:* * Used when named environments exist and no `--env` flag is specified. * * */
- `truncate` **(Many-Argument Workhorses)** (@ `packages/wrangler/src/utils/print-bindings.ts`) -> Impact: **361.7** | LOC: 860
- `createWorkerUploadForm` **(Many-Argument Workhorses)** (@ `packages/wrangler/src/deployment-bundle/create-worker-upload-form.ts`) -> Impact: **328.1** | LOC: 762
  * *Intent:* /** * Creates a `FormData` upload from Worker data and bindings */
- `deploy` **(Many-Argument Workhorses)** (@ `packages/wrangler/src/deploy/deploy.ts`) -> Impact: **297.8** | LOC: 894
- `unescapeIdentity` **(Many-Argument Workhorses)** (@ `packages/local-explorer-ui/src/drivers/sqlite/parsers.ts`) -> Impact: **262.8** | LOC: 900
  * *Intent:* /** * Strips surrounding quote characters (`"`, `` ` ``, `[`/`]`) from a SQL * identifier and un-doubles any escaped double-quotes within. * * */
- `generateSimpleEnvTypes` **(Many-Argument Workhorses)** (@ `packages/wrangler/src/type-generation/index.ts`) -> Impact: **221.6** | LOC: 291
  * *Intent:* * * Used when no named environments exist or when `--env` is specified. * * */
- `validateContainerApp` **(Many-Argument Workhorses)** (@ `packages/workers-utils/src/config/validation.ts`) -> Impact: **212.7** | LOC: 493
- `executeGetInstanceDetails` **(Defensive Guards)** (@ `packages/miniflare/src/workers/local-explorer/resources/workflows.ts`) -> Impact: **207.3** | LOC: 187
  * *Intent:* /** * Get instance details via the Engine DO directly. * * Accepts either a real instance ID or a hex DO ID: * - Real instance ID (e.g. "my-instance")...
- `convertConfigToBindings` **(Many-Argument Workhorses)** (@ `packages/wrangler/src/api/startDevWorker/utils.ts`) -> Impact: **196.4** | LOC: 290
  * *Intent:* /** * Convert Config to the StartDevWorkerInput["bindings"] format for consistent internal use. */

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/wrangler/src/__tests__` | 74 | 41513.25 | 22.12% | 2.01% |
| `packages/wrangler/e2e` | 24 | 34768.29 | 35.21% | 2.08% |
| `packages/wrangler/src/__tests__/pages` | 21 | 14556.67 | 55.34% | 0.0% |
| `packages/wrangler/src/__tests__/r2` | 12 | 9693.86 | 74.85% | 0.0% |
| `packages/miniflare/test/plugins/local-explorer` | 8 | 9026.96 | 72.12% | 0.0% |
| `packages/wrangler/src/__tests__/versions` | 6 | 8149.69 | 71.27% | 0.0% |
| `packages/workflows-shared/tests` | 8 | 7560.21 | 19.26% | 0.0% |
| `packages/workers-playground` | 12 | 5208.14 | 8.73% | 0.0% |
| `packages/vite-plugin-cloudflare/playground/bindings` | 8 | 5083.52 | 0.64% | 0.0% |
| `packages/vite-plugin-cloudflare/playground/dot-env` | 8 | 5080.68 | 1.28% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/miniflare/src/workers/assets/rpc-proxy.worker.ts` -> **100.0%** Exposure
- `packages/miniflare/src/workers/node.d.ts` -> **100.0%** Exposure
- `packages/miniflare/src/workers/stream/binding.worker.ts` -> **100.0%** Exposure
- `packages/miniflare/types/streams.d.ts` -> **100.0%** Exposure
- `packages/quick-edit-extension/vscode.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/create-cloudflare/templates/common/js/src/proxy.js` -> **100.0%** Exposure
- `fixtures/shared/src/mock-postgres-server.ts` -> **100.0%** Exposure
- `fixtures/shared/src/run-wrangler-long-lived.ts` -> **100.0%** Exposure
- `packages/create-cloudflare/e2e/helpers/workers-helpers.ts` -> **100.0%** Exposure
- `packages/create-cloudflare/src/helpers/__tests__/args.test.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/quick-edit-extension/vscode.d.ts` -> **306** Orphaned Functions | **69** Duplicates
- `packages/miniflare/src/workers/node.d.ts` -> **60** Orphaned Functions | **0** Duplicates
- `packages/workers-shared/router-worker/tests/index.test.ts` -> **0** Orphaned Functions | **51** Duplicates
- `packages/vitest-pool-workers/types/cloudflare-test.d.ts` -> **43** Orphaned Functions | **4** Duplicates
- `packages/vitest-pool-workers/src/worker/node/console.ts` -> **21** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `packages/vite-plugin-cloudflare/playground/node-compat/__tests__/worker-crypto/crypto.spec.ts` -> **99.9973%** Exposure
- `packages/vite-plugin-cloudflare/playground/node-compat/worker-crypto/index.ts` -> **99.9946%** Exposure
- `packages/miniflare/src/http/cert.ts` -> **99.9898%** Exposure
- `packages/wrangler/src/cloudchamber/ssh/validate.ts` -> **99.9257%** Exposure
- `packages/pages-shared/__tests__/metadata-generator/createMetadataObject.test.ts` -> **99.5623%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### 📡 API Network Audit (Set Theory)
- **Shadow APIs (Critical):** `37` undocumented endpoints actively listening.
- **Ghost APIs (Bloat):** `27` endpoints documented but missing from code.
- **Known Shadow Routes:** `DELETE /api/r2/buckets/{var}/objects`, `DELETE /api/storage/kv/namespaces/{var}/values/{var}`, `DELETE /api/workflows/{var}`, `DELETE /api/workflows/{var}/instances/{var}`, `GET /`

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `17` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5830` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `packages/wrangler/e2e/dev.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 22633.11 | **LOC:** 2919 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 44.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (64.0%), Complexity Load (formerly Cognitive Load) (49.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 295 instances
* *Amplified Cascading Flux:* 91 instances
* *Concurrency (weighted view):* 1997
* *State Mutation (weighted view):* 517
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 680`, `args: 174`, `func_start: 117`
* *Risk/State:* `state_mutation: 335`, `planned_debt: 3`, `fragile_debt: 4`
* *Architecture:* `io: 111`, `api: 40`, `concurrency: 522`, `import: 36`
* *Defense:* `safety: 28`, `doc: 1`, `test: 223`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` account-id, e2e-wrangler-test, fetch-text, fetch-with-etag, generate-resource-name, mysql-echo-handler, postgres-echo-handler, retry...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/type-generation.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 16287.36 | **LOC:** 3994 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.8%), Guard Balance (formerly Safety Score) (44.6%), Mutation Surface (formerly State Flux) (27.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 71 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 514
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 809`, `args: 149`, `func_start: 75`, `class_start: 155`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 94`
* *Architecture:* `io: 177`, `api: 42`, `concurrency: 159`, `import: 65`
* *Defense:* `safety: 20`, `doc: 2`, `test: 254`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` index, index, index, type-generation, helpers, runtime, dedent, durable-2.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/workflows-shared/tests/engine.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 6715.89 | **LOC:** 1063 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 41.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.5%), Complexity Load (formerly Cognitive Load) (44.6%), Guard Balance (formerly Safety Score) (36.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 357
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 424`, `args: 162`, `func_start: 73`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 8`, `planned_debt: 1`
* *Architecture:* `concurrency: 267`, `import: 11`
* *Defense:* `safety: 44`, `test: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` src, engine, errors, test-entry, utils, cloudflare:test, cloudflare:workers, cloudflare:workflows...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/versions/versions.deploy.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 6486.57 | **LOC:** 1351 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (87.0%), Guard Balance (formerly Safety Score) (43.6%), Mutation Surface (formerly State Flux) (43.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 52 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 380
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 105`, `args: 62`, `func_start: 25`
* *Risk/State:* `state_mutation: 40`, `planned_debt: 1`
* *Architecture:* `io: 3`, `concurrency: 120`, `import: 16`
* *Defense:* `safety: 2`, `test: 118`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` normalize, deploy, collect-cli-output, mock-account-id, mock-console, mock-istty, mock-upload-worker, mock-workers-subdomain...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fixtures/nodejs-hybrid-app/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fixtures/pages-workerjs-app/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fixtures/worker-app/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vite-plugin-cloudflare/playground/bindings/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vite-plugin-cloudflare/playground/dot-env/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vite-plugin-cloudflare/playground/sensitive-files/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/workers-playground/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/pages/functions-build.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 4055.5 | **LOC:** 1263 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 64 instances
* *Concurrency (weighted view):* 180
* *State Mutation (weighted view):* 363
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 153`, `args: 42`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 235`
* *Architecture:* `io: 20`, `api: 37`, `concurrency: 75`, `import: 36`
* *Defense:* `safety: 4`, `test: 87`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` end-event-loop, mock-console, run-in-tmp, run-wrangler, string-dynamic-values-matcher, meaning-of-life.js, greeting.wasm, name.wasm...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/core/handle-errors.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3730.26 | **LOC:** 697 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.0%), Complexity Load (formerly Cognitive Load) (43.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (3.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 112`, `args: 58`, `func_start: 25`
* *Risk/State:* None
* *Architecture:* `io: 31`, `concurrency: 50`, `import: 3`
* *Defense:* `safety: 6`, `test: 125`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` handle-errors, mock-console, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/e2e/pages-dev.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3673.75 | **LOC:** 904 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (71.0%), Complexity Load (formerly Cognitive Load) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 81 instances
* *Amplified Cascading Flux:* 36 instances
* *Concurrency (weighted view):* 566
* *State Mutation (weighted view):* 193
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 213`, `args: 59`, `func_start: 47`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 121`
* *Architecture:* `io: 36`, `api: 32`, `concurrency: 161`, `import: 16`
* *Defense:* `safety: 7`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` greetings, my-html.html, greetings, graham.html, e2e-wrangler-test, fetch-text, normalize, wait-for...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/workers-utils/src/config/validation.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3166.52 | **LOC:** 5390 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 22.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **15**; blast radius 0.326; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (65.4%), Connectivity (formerly Api Exposure) (37.2%)
- **Documentation Coverage:** 32.5843% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateContainerApp` **(Many-Argument Workhorses)** (Impact: 212.7)
  * `normalizeAndValidateConfig` **(Many-Argument Workhorses)** (Impact: 99.2)
    * *Intent:* * Validate the given `rawConfig` object that was loaded from `configPath`. * * The configuration is ...
  * `validateObservability` **(Many-Argument Workhorses)** (Impact: 67.2)
  * `normalizeAndValidateEnvironment` **(Many-Argument Workhorses)** (Impact: 52.6)
  * `validateMigrations` **(Many-Argument Workhorses)** (Impact: 52.0)
    * *Intent:* /** * Validate the `migrations` configuration and return the normalized values. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 397 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 1216
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 755`, `structural_boundaries: 367`, `args: 122`, `func_start: 84`
* *Risk/State:* `state_mutation: 422`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 60`, `api: 9`, `concurrency: 7`, `import: 16`
* *Defense:* `safety: 85`, `doc: 36`, `test: 7`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.326
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000696
  * `Imports (Out-Degree: 5):` , misc-variables, errors, fs-helpers, types, config, config-helpers, diagnostics...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/wrangler/src/__tests__/r2/catalog-force.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3078.36 | **LOC:** 718 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (97.7%), Complexity Load (formerly Cognitive Load) (96.8%), Guard Balance (formerly Safety Score) (50.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 28 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 181
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 103`, `args: 44`, `func_start: 16`
* *Risk/State:* `state_mutation: 69`
* *Architecture:* `io: 37`, `concurrency: 41`, `import: 10`
* *Defense:* `safety: 20`, `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` mock-account-id, mock-console, mock-dialogs, mock-istty, msw, run-in-tmp, run-wrangler, msw...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/e2e/multiworker-dev.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3062.46 | **LOC:** 653 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.6%), Guard Balance (formerly Safety Score) (65.1%), Complexity Load (formerly Cognitive Load) (49.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 41 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 329
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 174`, `args: 67`, `func_start: 36`, `class_start: 3`
* *Risk/State:* `state_mutation: 83`, `planned_debt: 6`
* *Architecture:* `io: 31`, `api: 12`, `concurrency: 124`, `import: 14`
* *Defense:* `test: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` e2e-wrangler-test, fetch-json, fetch-text, generate-resource-name, setup, wait-for, cloudflare:workers, node:crypto...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/miniflare/test/plugins/local-explorer/do.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2983.09 | **LOC:** 880 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.6%), Guard Balance (formerly Safety Score) (35.4%), Complexity Load (formerly Cognitive Load) (33.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 121
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 155`, `args: 38`, `func_start: 27`, `class_start: 17`
* *Risk/State:* `state_mutation: 5`, `planned_debt: 5`
* *Architecture:* `io: 37`, `api: 17`, `concurrency: 86`, `import: 8`
* *Defense:* `safety: 8`, `test: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` constants, test-shared, workers-utils, cloudflare:workers, miniflare, promises, node:path, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/queues/queues-subscription.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2914.52 | **LOC:** 803 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (85.0%), Guard Balance (formerly Safety Score) (65.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 39 instances
* *Amplified Cascading Flux:* 40 instances
* *Concurrency (weighted view):* 256
* *State Mutation (weighted view):* 168
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 88`, `args: 29`, `func_start: 23`
* *Risk/State:* `state_mutation: 88`
* *Architecture:* `io: 1`, `concurrency: 61`, `import: 10`
* *Defense:* `safety: 3`, `test: 84`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` subscription-types, mock-account-id, mock-console, mock-dialogs, mock-istty, run-in-tmp, run-wrangler, mock-utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/index.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2767.31 | **LOC:** 437 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 23.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (72.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 33 instances
* *Concurrency (weighted view):* 172
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 89`, `args: 27`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 60`, `fragile_debt: 3`
* *Architecture:* `io: 9`, `concurrency: 67`, `import: 12`
* *Defense:* `safety: 8`, `test: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` package-manager, update-check, logPossibleBugMessage, end-event-loop, mock-console, run-in-tmp, run-wrangler, write-worker-source...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/type-generation/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2760.38 | **LOC:** 3520 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.8%), Connectivity (formerly Api Exposure) (56.8%), Guard Balance (formerly Safety Score) (55.4%)
- **Documentation Coverage:** 42.623% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generatePerEnvironmentTypes` **(Many-Argument Workhorses)** (Impact: 432.0)
    * *Intent:* * Used when named environments exist and no `--env` flag is specified. * * */
  * `generateSimpleEnvTypes` **(Many-Argument Workhorses)** (Impact: 221.6)
    * *Intent:* * * Used when no named environments exist or when `--env` is specified. * * */
  * `collectEnvironmentBindings` **(Many-Argument Workhorses)** (Impact: 193.9)
  * `collectEnvironmentBindings` **(Many-Argument Workhorses)** (Impact: 190.3)
  * `collectCoreBindingsPerEnvironment` **(Many-Argument Workhorses)** (Impact: 180.1)
    * *Intent:* /** * Collects core bindings per environment, returning a map from environment name to bindings. * *...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 130 instances
* *Concurrency (weighted view):* 65
* *State Mutation (weighted view):* 398
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 694`, `structural_boundaries: 327`, `args: 82`, `func_start: 53`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 138`, `dead_code: 2`
* *Architecture:* `io: 23`, `api: 12`, `concurrency: 20`, `import: 30`
* *Defense:* `safety: 155`, `doc: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` $entrypointModule, $importPath, config, create-command, entry, class-names-sqlite, dev-vars, logger...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/autoconfig/details/get-details-for-auto-config.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2516.27 | **LOC:** 558 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.5%), Complexity Load (formerly Cognitive Load) (36.2%), Guard Balance (formerly Safety Score) (18.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 116`, `args: 38`, `func_start: 29`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 2`, `api: 3`, `concurrency: 78`, `import: 17`
* *Defense:* `safety: 30`, `test: 67`, `sync_locks: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` details, config-cache, is-interactive, output, package-manager, constants, mock-console, mock-dialogs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/miniflare/test/index.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2185.34 | **LOC:** 3696 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **30**; blast radius 0.14; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (39.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `STORE` **(Defensive Guards)** (Impact: 15.0)
  * `handleRuntimeStdio` **(I/O & Config Routines)** (Impact: 6.6)
  * `unsafeModuleFallbackService` **(Compute Cores)** (Impact: 4.8)
  * `CUSTOM` **(Defensive Guards)** (Impact: 4.7)
  * `testEncoding` **(Callbacks & Closures)** (Impact: 2.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 243 instances
* *Amplified Cascading Flux:* 33 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 1776
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 911`, `args: 253`, `func_start: 203`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 117`, `planned_debt: 2`, `duplicate_logic: 4`, `unreferenced_by_name: 3`
* *Architecture:* `io: 403`, `api: 103`, `concurrency: 561`, `import: 41`
* *Defense:* `safety: 39`, `test: 363`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` a.mjs, c.cjs, b.mjs, d.cjs, index.js, index.js, test-shared, experimental...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/r2/local-uploads.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2086.52 | **LOC:** 352 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (72.6%), Complexity Load (formerly Cognitive Load) (69.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (33.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 63
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 69`, `args: 30`, `func_start: 22`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `io: 9`, `concurrency: 43`, `import: 10`
* *Defense:* `safety: 10`, `test: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` end-event-loop, mock-account-id, mock-console, mock-dialogs, mock-istty, msw, run-in-tmp, run-wrangler...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/versions/secrets/bulk.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2033.49 | **LOC:** 380 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 42.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (97.4%), Mutation Surface (formerly State Flux) (85.1%), Guard Balance (formerly Safety Score) (47.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 108
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 84`, `args: 26`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 15`
* *Architecture:* `io: 1`, `concurrency: 38`, `import: 11`
* *Defense:* `safety: 4`, `test: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` mock-account-id, mock-console, mock-dialogs, run-in-tmp, run-wrangler, utils, test-helpers, promises...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/wrangler/src/__tests__/autoconfig/run.test.ts` -> Churn: **67.12%** | Cog Load: 74.3585% | Debt: 0.0%
- `packages/create-cloudflare/src/templates.ts` -> Churn: **64.45%** | Cog Load: 55.1773% | Debt: 0.0%
- `packages/miniflare/src/index.ts` -> Churn: **62.47%** | Cog Load: 64.3995% | Debt: 8.2763%
- `packages/wrangler/src/deploy/deploy.ts` -> Churn: **62.47%** | Cog Load: 82.2263% | Debt: 8.5683%
- `packages/create-cloudflare/e2e/tests/cli/cli.test.ts` -> Churn: **59.96%** | Cog Load: 100.0% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/wrangler/src/__tests__/r2/catalog-force.test.ts` -> **Carol Xu** (100.0% isolated ownership) | Magnitude: 3078.36
- `packages/wrangler/src/__tests__/email-routing.test.ts` -> **Thomas Gauvin** (100.0% isolated ownership) | Magnitude: 1082.56
- `packages/local-explorer-ui/src/__e2e__/r2/r2-bucket.spec.ts` -> **Ben** (100.0% isolated ownership) | Magnitude: 1010.23
- `packages/wrangler/src/__tests__/autoconfig/frameworks/utils/vite-plugin.test.ts` -> **Dario Piotrowicz** (100.0% isolated ownership) | Magnitude: 621.31
- `packages/workers-utils/tests/config/findWranglerConfig.test.ts` -> **Victor Berchet** (100.0% isolated ownership) | Magnitude: 617.04

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/create-cloudflare/src/templates.ts` -> **Severity: 0.035** (Bridge: 0.0004 * Flux: 99.5575%)
- `packages/wrangler/e2e/helpers/e2e-wrangler-test.ts` -> **Severity: 0.021** (Bridge: 0.0002 * Flux: 100.0%)
- `packages/wrangler/src/deploy/deploy.ts` -> **Severity: 0.011** (Bridge: 0.0001 * Flux: 91.7929%)
- `packages/wrangler/src/utils/print-bindings.ts` -> **Severity: 0.011** (Bridge: 0.0001 * Flux: 100.0%)
- `packages/wrangler/src/triggers/deploy.ts` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 92.9391%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/wrangler/src/logger.ts` -> **Severity: 3.566** (Embedded: 0.0777 * Error Risk: 45.8631%)
- `packages/wrangler/src/utils/log-file.ts` -> **Severity: 3.308** (Embedded: 0.0508 * Error Risk: 65.1476%)
- `packages/wrangler/src/utils/format-message.ts` -> **Severity: 2.41** (Embedded: 0.0508 * Error Risk: 47.4308%)
- `packages/cli/select-list.ts` -> **Severity: 2.067** (Embedded: 0.0245 * Error Risk: 84.3617%)
- `packages/cli/interactive.ts` -> **Severity: 2.062** (Embedded: 0.0329 * Error Risk: 62.6712%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/wrangler/src/logger.ts` -> **Severity: 5096.104** (Blast Radius: 59.225 * Doc Risk: 86.0465%)
- `packages/wrangler/src/utils/log-file.ts` -> **Severity: 1535.28** (Blast Radius: 25.588 * Doc Risk: 60.0%)
- `packages/wrangler/src/core/create-command.ts` -> **Severity: 1154.8** (Blast Radius: 11.548 * Doc Risk: 100.0%)
- `packages/wrangler/src/utils/filesystem.ts` -> **Severity: 1099.9** (Blast Radius: 10.999 * Doc Risk: 100.0%)
- `packages/create-cloudflare/src/templates.ts` -> **Severity: 804.267** (Blast Radius: 10.556 * Doc Risk: 76.1905%)

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
