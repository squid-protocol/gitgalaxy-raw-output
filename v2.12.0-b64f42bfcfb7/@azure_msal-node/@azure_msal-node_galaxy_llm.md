# ARCHITECTURAL_BRIEF: @azure_msal-node
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
- **Scope:** 153 analyzed artifact(s), 16049 LOC.
- **Load-bearing artifact:** `package/src/utils/Constants.ts` -- 29 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/src/index.ts` -- pulls in 30 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/lib/msal-node.cjs` at magnitude 5887.14 (structural weight, not risk).
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
| Total Artifacts | 231 |
| Analyzed Artifacts (Scanned) | 153 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 78 |
| Total LOC | 16049 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.2% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4209 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2147 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2762 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 149 | 7812 | 97.4% |
| PLAINTEXT | 2 | 0 | 1.3% |
| MARKDOWN | 1 | 0 | 0.7% |
| JAVASCRIPT | 1 | 8237 | 0.7% |

## 4.1 SOURCE ENCODINGS
All 153 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 31%, State Mutators Files 17%, Declarative / Non-Code 15%, Generic / Templated Code Files 10%, Large Core Modules (3) 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 150 | 98.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 2.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 78*

**Composition by Extension & Reason:**
- `.map`: 44x Excluded (Saturation: Line 1 exceeds 500 chars), 32x Unresolved Ambiguity (No Retainable Structure)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 1x Excluded (Saturation: Line 52 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 92.5 | 6.5 | 2.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 65.3 | 12.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 38.8 | 21.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 8.6 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.2 | 89.7 | 11.0 | 3.5 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 27.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 13.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 8.4 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 14.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 93.0 | 0.9 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 59 | 20 | 1 | `package/src/cache/NodeStorage.ts` |
| cleanup | 12 | 4 | 0 | `package/lib/msal-node.cjs` |
| guards | 882 | 72 | 10 | `package/lib/msal-node.cjs` |
| danger | 247 | 19 | 1 | `package/lib/msal-node.cjs` |
| concurrency | 622 | 61 | 8 | `package/lib/msal-node.cjs` |
| connectivity | 554 | 150 | 8 | `package/lib/msal-node.cjs` |
| io | 40 | 16 | 1 | `package/lib/msal-node.cjs` |
| crypto | 5 | 4 | 0 | `package/lib/msal-node.cjs` |
| ipc | 4 | 2 | 0 | `package/lib/msal-node.cjs` |
| time | 47 | 9 | 0 | `package/lib/msal-node.cjs` |
| serialization | 29 | 4 | 0 | `package/lib/msal-node.cjs` |
| regex | 40 | 6 | 0 | `package/lib/msal-node.cjs` |
| events | 158 | 19 | 2 | `package/lib/msal-node.cjs` |
| tests | 0 | 0 | 0 | - |
| docs | 1366 | 132 | 13 | `package/lib/msal-node.cjs` |
| debt | 25 | 4 | 0 | `package/lib/msal-node.cjs` |
| mutation | 2520 | 93 | 17 | `package/lib/msal-node.cjs` |
| dead_code | 381 | 78 | 6 | `package/lib/msal-node.cjs` |
| credential | 6 | 4 | 0 | `package/lib/msal-node.cjs` |
| threat | 7 | 1 | 0 | `package/lib/msal-node.cjs` |
| ml_ai | 4 | 2 | 0 | `package/src/retry/ExponentialRetryStrategy.ts` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/lib/msal-node.cjs` (Hits: 12)
- `package/src/network/LoopbackClient.ts` (Hits: 6)
- `package/src/client/ManagedIdentitySources/AzureArc.ts` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Constants.ts** (`package/src/utils/Constants.ts`) — 29 inbound connections
2. **CryptoProvider.ts** (`package/src/crypto/CryptoProvider.ts`) — 13 inbound connections
3. **NodeStorage.ts** (`package/src/cache/NodeStorage.ts`) — 11 inbound connections
4. **ManagedIdentityId.ts** (`package/src/config/ManagedIdentityId.ts`) — 10 inbound connections
5. **msal-node.cjs** (`package/lib/msal-node.cjs`) — 9 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`package/src/index.ts`) — 30 outbound dependencies
2. **PublicClientApplication.ts** (`package/src/client/PublicClientApplication.ts`) — 18 outbound dependencies
3. **ClientApplication.ts** (`package/src/client/ClientApplication.ts`) — 17 outbound dependencies
4. **ManagedIdentityClient.ts** (`package/src/client/ManagedIdentityClient.ts`) — 14 outbound dependencies
5. **ConfidentialClientApplication.ts** (`package/src/client/ConfidentialClientApplication.ts`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `generateAuthenticationResult` **(Many-Argument Workhorses)** (@ `package/lib/msal-node.cjs`) -> Impact: **116.5** | LOC: 74
  * *Intent:* /** * * Optionally takes a state string that is set as-is in the response. * */
- `handleServerTokenResponse` **(Many-Argument Workhorses)** (@ `package/lib/msal-node.cjs`) -> Impact: **86.5** | LOC: 71
  * *Intent:* /** * Returns a constructed token response based on given string. Also manages the cache updates and cleanups. */
- `getStandardAuthorizeRequestParameters` **(Many-Argument Workhorses)** (@ `package/lib/msal-node.cjs`) -> Impact: **86.4** | LOC: 118
  * *Intent:* /* * Copyright (c) Microsoft Corporation. All rights reserved. * Licensed under the MIT License. */ /** * Returns map of parameters that are applicabl...
- `generateCacheRecord` **(Many-Argument Workhorses)** (@ `package/lib/msal-node.cjs`) -> Impact: **74.6** | LOC: 78
  * *Intent:* /** * Generates CacheRecord */
- `createAccountEntity` **(Defensive Guards)** (@ `package/lib/msal-node.cjs`) -> Impact: **69.5** | LOC: 71
  * *Intent:* /** * Build Account cache from IdToken, clientInfo and authority/policy. Associated with AAD. */
- `getCachedAuthenticationResult` **(Many-Argument Workhorses)** (@ `package/src/client/ClientCredentialClient.ts`) -> Impact: **55.3** | LOC: 100
  * *Intent:* /** * looks up cache if the tokens are cached already */
- `buildAccountToCache` **(Many-Argument Workhorses)** (@ `package/lib/msal-node.cjs`) -> Impact: **54.4** | LOC: 40
- `createTokenRequestBody` **(Compute Cores)** (@ `package/lib/msal-node.cjs`) -> Impact: **54.1** | LOC: 121
  * *Intent:* /** * Generates a map for all the params to be sent to the service */
- `sendPostRequest` **(Many-Argument Workhorses)** (@ `package/lib/msal-node.cjs`) -> Impact: **50.0** | LOC: 39
  * *Intent:* /** * Wraps sendPostRequestAsync with necessary preflight and postflight logic */
- `getCachedAuthenticationResult` **(Many-Argument Workhorses)** (@ `package/lib/msal-node.cjs`) -> Impact: **49.9** | LOC: 46
  * *Intent:* /** * looks up cache if the tokens are cached already */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/lib` | 2 | 5888.14 | 15.85% | 14.48% |
| `package/src/client` | 13 | 1232.58 | 14.51% | 8.15% |
| `package/src/client/ManagedIdentitySources` | 7 | 411.84 | 6.95% | 41.56% |
| `package/src/cache` | 4 | 406.86 | 11.04% | 0.0% |
| `package/src/request` | 16 | 236.18 | 1.91% | 0.0% |
| `package/src/network` | 4 | 210.38 | 37.61% | 20.02% |
| `package/src/config` | 3 | 150.64 | 34.0% | 35.4% |
| `package/src/retry` | 5 | 97.26 | 16.91% | 17.37% |
| `package/src/cache/serializer` | 3 | 96.52 | 4.38% | 15.96% |
| `package/src/utils` | 4 | 88.94 | 7.24% | 50.32% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/lib/types/cache/NodeStorage.d.ts` -> **100.0%** Exposure
- `package/lib/types/cache/TokenCache.d.ts` -> **100.0%** Exposure
- `package/lib/types/client/ClientApplication.d.ts` -> **100.0%** Exposure
- `package/lib/types/client/IConfidentialClientApplication.d.ts` -> **100.0%** Exposure
- `package/lib/types/client/IPublicClientApplication.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/src/config/ManagedIdentityId.ts` -> **100.0%** Exposure
- `package/src/config/ManagedIdentityRequestParameters.ts` -> **100.0%** Exposure
- `package/src/utils/NetworkUtils.ts` -> **100.0%** Exposure
- `package/src/client/ClientAssertion.ts` -> **99.9997%** Exposure
- `package/lib/msal-node.cjs` -> **96.0342%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/lib/msal-node.cjs` -> **45** Orphaned Functions | **16** Duplicates
- `package/lib/types/cache/NodeStorage.d.ts` -> **40** Orphaned Functions | **0** Duplicates
- `package/lib/types/client/ClientApplication.d.ts` -> **15** Orphaned Functions | **0** Duplicates
- `package/lib/types/client/IPublicClientApplication.d.ts` -> **13** Orphaned Functions | **0** Duplicates
- `package/lib/types/client/IConfidentialClientApplication.d.ts` -> **12** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `package/src/client/ClientAssertion.ts` -> **92.9994%** Exposure
- `package/lib/msal-node.cjs` -> **41.4537%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `135` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/lib/msal-node.cjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.669)
- **Top Global Matches:** file_cluster_15: 7.669, file_cluster_4: 8.631, file_cluster_11: 9.134
- **Magnitude:** 5887.14 | **LOC:** 12392 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **6**; blast radius 14.652; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.0%), Concurrency Surface (formerly Concurrency) (90.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.8%)
- **Documentation Coverage:** 19.1489% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generateAuthenticationResult` **(Many-Argument Workhorses)** (Impact: 116.5)
    * *Intent:* /** * * Optionally takes a state string that is set as-is in the response. * */
  * `handleServerTokenResponse` **(Many-Argument Workhorses)** (Impact: 86.5)
    * *Intent:* /** * Returns a constructed token response based on given string. Also manages the cache updates and...
  * `getStandardAuthorizeRequestParameters` **(Many-Argument Workhorses)** (Impact: 86.4)
    * *Intent:* /* * Copyright (c) Microsoft Corporation. All rights reserved. * Licensed under the MIT License. */ ...
  * `generateCacheRecord` **(Many-Argument Workhorses)** (Impact: 74.6)
    * *Intent:* /** * Generates CacheRecord */
  * `createAccountEntity` **(Defensive Guards)** (Impact: 69.5)
    * *Intent:* /** * Build Account cache from IdToken, clientInfo and authority/policy. Associated with AAD. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 35 instances
* *Amplified Cascading Flux:* 283 instances
* *Concurrency (weighted view):* 436
* *State Mutation (weighted view):* 1153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1471`, `structural_boundaries: 1115`, `args: 740`, `func_start: 651`, `class_start: 63`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 587`, `dead_code: 3`, `planned_debt: 6`, `duplicate_logic: 16`, `unreferenced_by_name: 45`
* *Architecture:* `io: 12`, `api: 44`, `concurrency: 261`, `import: 6`
* *Defense:* `safety: 464`, `doc: 610`, `immutability_locks: 5`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.652
  * `Choke Point (Betweenness):` 0.003465 | `Ripple Effect (Closeness):` 0.077199
  * `Imports (Out-Degree: 1):` crypto, fs, http, jsonwebtoken, path, uuid
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `package/src/client/ClientApplication.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.791)
- **Top Global Matches:** file_cluster_15: 6.791, file_cluster_16: 7.12, file_cluster_11: 7.575
- **Magnitude:** 214.3 | **LOC:** 684 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **17**; blast radius 4.111; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.8%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.1%)
- **Documentation Coverage:** 8.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `acquireTokenByCode` **(Many-Argument Workhorses)** (Impact: 16.9)
    * *Intent:* /** * Acquires a token by exchanging the Authorization Code received from the first step of OAuth2.0...
  * `buildOauthClientConfiguration` **(Many-Argument Workhorses)** (Impact: 14.1)
    * *Intent:* /** * Builds the common configuration to be passed to the common component based on the platform con...
  * `acquireTokenSilent` **(Defensive Guards)** (Impact: 12.0)
    * *Intent:* /** * Acquires a token silently when a user specifies the account the token is requested for. * * Th...
  * `initializeBaseRequest` **(Stateful Encapsulated Methods)** (Impact: 11.4)
    * *Intent:* /** * Generates a request with the default scopes & generates a correlationId. */
  * `createAuthority` **(Stateful Encapsulated Methods)** (Impact: 10.5)
    * *Intent:* /** * Create authority instance. If authority not passed in request, default to authority set on the...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 58
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 59`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 9`, `concurrency: 43`, `import: 17`
* *Defense:* `safety: 15`, `doc: 21`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.111
  * `Choke Point (Betweenness):` 0.000876 | `Ripple Effect (Closeness):` 0.012228
  * `Imports (Out-Degree: 17):` NodeStorage.js, TokenCache.js, Configuration.js, CryptoProvider.js, NodeAuthError.js, packageMetadata.js, Authorize.js, AuthorizationCodeRequest.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/cache/TokenCache.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.655)
- **Top Global Matches:** file_cluster_16: 7.655, file_cluster_0: 7.664, file_cluster_15: 8.621
- **Magnitude:** 189.98 | **LOC:** 399 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **8**; blast radius 18.304; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.8%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (77.2%), Guard Balance (formerly Safety Score) (53.8%)
- **Documentation Coverage:** 11.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mergeUpdates` **(Stateful Encapsulated Methods)** (Impact: 19.0)
    * *Intent:* /** * Deep update of oldState based on newState values */
  * `removeAccount` **(Defensive Guards)** (Impact: 13.2)
    * *Intent:* /** * API to remove a specific account and the relevant data from cache */
  * `mergeRemovals` **(Stateful Encapsulated Methods)** (Impact: 12.5)
    * *Intent:* /** * Removes entities in oldState that the were removed from newState. If there are any unknown val...
  * `getAccountByHomeId` **(Generic / Templated Code)** (Impact: 9.2)
    * *Intent:* /** * Returns the signed in account matching homeAccountId. * (the account object is created at the ...
  * `getAccountByLocalId` **(Generic / Templated Code)** (Impact: 9.2)
    * *Intent:* /** * Returns the signed in account matching localAccountId. * (the account object is created at the...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 41`, `args: 21`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `api: 11`, `concurrency: 18`, `import: 8`
* *Defense:* `safety: 4`, `doc: 17`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.304
  * `Choke Point (Betweenness):` 0.005405 | `Ripple Effect (Closeness):` 0.062903
  * `Imports (Out-Degree: 7):` CryptoProvider.js, GuidGenerator.js, ITokenCache.js, NodeStorage.js, Deserializer.js, Serializer.js, SerializerTypes.js, node
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `package/src/cache/NodeStorage.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.993)
- **Top Global Matches:** file_cluster_15: 5.993, file_cluster_11: 6.899, file_cluster_10: 7.787
- **Magnitude:** 183.7 | **LOC:** 566 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **5**; blast radius 10.274; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (59.3%), Guard Balance (formerly Safety Score) (52.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 11.5942% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cacheToInMemoryCache` **(Type Conversions)** (Impact: 19.9)
    * *Intent:* /** * Converts cacheKVStore to InMemoryCache */
  * `updateCredentialCacheKey` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* /** * Updates a credential's cache key if the current cache key is outdated */
  * `constructor` **(State Mutators)** (Impact: 5.2)
  * `removeItem` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* /** * Removes the cache item from memory with the given key. */
  * `getServerTelemetry` **(Type Conversions)** (Impact: 5.1)
    * *Intent:* /** * fetch server telemetry entity from the platform cache */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 63`, `args: 43`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `api: 29`, `concurrency: 8`, `import: 5`
* *Defense:* `doc: 36`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.274
  * `Choke Point (Betweenness):` 0.002561 | `Ripple Effect (Closeness):` 0.072271
  * `Imports (Out-Degree: 5):` CacheHelpers.js, Deserializer.js, Serializer.js, SerializerTypes.js, node
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `package/src/client/ClientCredentialClient.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.856)
- **Top Global Matches:** file_cluster_6: 5.856, file_cluster_4: 10.569, file_cluster_8: 14.901
- **Magnitude:** 163.72 | **LOC:** 432 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 4.225; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getCachedAuthenticationResult` **(Many-Argument Workhorses)** (Impact: 55.3)
    * *Intent:* /** * looks up cache if the tokens are cached already */
  * `createTokenRequestBody` **(I/O & Config Routines)** (Impact: 16.8)
    * *Intent:* /** * generate the request to the server in the acceptable format */
  * `executeTokenRequest` **(Many-Argument Workhorses)** (Impact: 12.9)
    * *Intent:* /** * Makes a network call to request the token from the service */
  * `readAccessTokenFromCache` **(Stateful Encapsulated Methods)** (Impact: 11.3)
    * *Intent:* /** * Reads access token from the cache */
  * `acquireToken` **(Compute Cores)** (Impact: 10.6)
    * *Intent:* /** * Public API to acquire a token with ClientCredential Flow for Confidential clients */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 28`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 4`, `concurrency: 18`, `import: 5`
* *Defense:* `safety: 5`, `doc: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.225
  * `Choke Point (Betweenness):` 0.000129 | `Ripple Effect (Closeness):` 0.012228
  * `Imports (Out-Degree: 5):` Configuration.js, CommonClientCredentialRequest.js, Constants.js, BaseClient.js, node
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/client/PublicClientApplication.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.892)
- **Top Global Matches:** file_cluster_4: 7.892, file_cluster_6: 9.806, file_cluster_15: 13.542
- **Magnitude:** 138.96 | **LOC:** 406 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 3.773; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `acquireTokenInteractive` **(Compute Cores)** (Impact: 28.0)
    * *Intent:* /** * Acquires a token interactively via the browser by requesting an authorization code then exchan...
  * `acquireTokenSilent` **(Compute Cores)** (Impact: 14.6)
    * *Intent:* /** * Returns a token retrieved either from the cache or by exchanging the refresh token for a fresh...
  * `waitForRedirectUri` **(Stateful Encapsulated Methods)** (Impact: 7.6)
    * *Intent:* /** * Attempts to retrieve the redirectUri from the loopback server. If the loopback server does not...
  * `constructor` **(I/O & Config Routines)** (Impact: 6.7)
    * *Intent:* * - authority: the authority URL for your application. * * AAD authorities are of the form https://l...
  * `signOut` **(Compute Cores)** (Impact: 6.5)
    * *Intent:* /** * Removes cache artifacts associated with the given account */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 40
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 53`, `args: 13`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 7`
* *Architecture:* `api: 2`, `concurrency: 30`, `import: 18`
* *Defense:* `safety: 9`, `doc: 10`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.773
  * `Choke Point (Betweenness):` 0.000171 | `Ripple Effect (Closeness):` 0.005435
  * `Imports (Out-Degree: 18):` Configuration.js, NodeAuthError.js, ILoopbackClient.js, LoopbackClient.js, packageMetadata.js, AuthorizationCodeRequest.js, AuthorizationUrlRequest.js, CommonDeviceCodeRequest.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/client/ManagedIdentitySources/BaseManagedIdentitySource.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.855)
- **Top Global Matches:** file_cluster_9: 7.855, file_cluster_0: 8.159, file_cluster_15: 8.472
- **Magnitude:** 137.68 | **LOC:** 416 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **11**; blast radius 6.963; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (93.3%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (74.9%), Guard Balance (formerly Safety Score) (50.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `acquireTokenWithManagedIdentity` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* * Acquires an access token using the managed identity endpoint for the specified resource. * This is...
  * `getManagedIdentityUserAssignedIdQueryParameterKey` **(Many-Argument Workhorses)** (Impact: 21.9)
    * *Intent:* /** * Determines the appropriate query parameter name for user-assigned managed identity * based on ...
  * `getServerTokenResponse` **(Compute Cores)** (Impact: 16.5)
    * *Intent:* /** * Converts a managed identity token response to a standardized server authorization token respon...
  * `getValidatedEnvVariableUrlString` **(Defensive Guards)** (Impact: 3.3)
    * *Intent:* /** * Validates and normalizes an environment variable containing a URL string. * This static utilit...
  * `constructor` **(State Mutators)** (Impact: 3.1)
    * *Intent:* /** * Creates an instance of BaseManagedIdentitySource. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 17
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 27`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `dead_code: 1`
* *Architecture:* `api: 9`, `concurrency: 7`, `import: 11`
* *Defense:* `safety: 9`, `doc: 13`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.963
  * `Choke Point (Betweenness):` 0.001438 | `Ripple Effect (Closeness):` 0.036685
  * `Imports (Out-Degree: 10):` NodeStorage.js, ManagedIdentityId.js, ManagedIdentityRequestParameters.js, CryptoProvider.js, ManagedIdentityError.js, HttpClientWithRetries.js, ManagedIdentityRequest.js, ManagedIdentityTokenResponse.js...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `package/src/client/OnBehalfOfClient.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.846)
- **Top Global Matches:** file_cluster_9: 7.846, file_cluster_16: 7.938, file_cluster_15: 8.363
- **Magnitude:** 118.38 | **LOC:** 416 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 3.933; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getCachedAuthenticationResult` **(I/O & Config Routines)** (Impact: 18.5)
    * *Intent:* /** * look up cache for tokens * Find idtoken in the cache * Find accessToken based on user assertio...
  * `createTokenRequestBody` **(I/O & Config Routines)** (Impact: 15.8)
    * *Intent:* /** * generate a server request in accepable format */
  * `readAccessTokenFromCacheForOBO` **(Stateful Encapsulated Methods)** (Impact: 14.3)
    * *Intent:* /** * Fetches the cached access token based on incoming assertion */
  * `acquireToken` **(Defensive Guards)** (Impact: 7.1)
    * *Intent:* /** * Public API to acquire tokens with on behalf of flow */
  * `executeTokenRequest` **(Many-Argument Workhorses)** (Impact: 5.0)
    * *Intent:* /** * Make a network call to the server requesting credentials */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 25`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 1`
* *Architecture:* `api: 3`, `concurrency: 15`, `import: 5`
* *Defense:* `safety: 5`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.933
  * `Choke Point (Betweenness):` 4.7e-05 | `Ripple Effect (Closeness):` 0.007246
  * `Imports (Out-Degree: 5):` CommonOnBehalfOfRequest.js, Constants.js, EncodingUtils.js, BaseClient.js, node
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/client/ClientAssertion.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.133)
- **Top Global Matches:** file_cluster_15: 6.133, file_cluster_16: 6.549, file_cluster_0: 8.142
- **Magnitude:** 106.78 | **LOC:** 203 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 4.246; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Credential Material (formerly Secrets Risk) (93.0%), Guard Balance (formerly Safety Score) (65.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getJwt` **(Many-Argument Workhorses)** (Impact: 17.4)
    * *Intent:* /** * Update JWT for certificate based clientAssertion, if passed by the user, uses it as is */
  * `createJwt` **(Many-Argument Workhorses)** (Impact: 10.2)
    * *Intent:* /** * JWT format and required claims specified: https://tools.ietf.org/html/rfc7523#section-3 */
  * `fromCertificate` **(Compute Cores)** (Impact: 6.8)
    * *Intent:* /** * Initialize the ClientAssertion class from the certificate passed by the user */
  * `fromCertificateWithSha256Thumbprint` **(Compute Cores)** (Impact: 6.8)
    * *Intent:* /** * Initialize the ClientAssertion class from the certificate passed by the user */
  * `parseCertificate` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* /** * Extracts the raw certs from a given certificate string and returns them in an array. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 17`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.246
  * `Choke Point (Betweenness):` 0.000156 | `Ripple Effect (Closeness):` 0.017391
  * `Imports (Out-Degree: 4):` CryptoProvider.js, ClientAuthErrorCodes.js, Constants.js, EncodingUtils.js, node, jsonwebtoken
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/client/DeviceCodeClient.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.561)
- **Top Global Matches:** file_cluster_16: 7.561, file_cluster_15: 7.895, file_cluster_9: 8.411
- **Magnitude:** 102.96 | **LOC:** 415 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 3.844; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (72.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (12.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `continuePolling` **(Many-Argument Workhorses)** (Impact: 24.1)
    * *Intent:* /** * Breaks the polling with specific conditions */
  * `acquireTokenWithDeviceCode` **(Many-Argument Workhorses)** (Impact: 18.5)
    * *Intent:* /** * Creates token request with device code response and polls token endpoint at interval set by th...
  * `createTokenRequestBody` **(Many-Argument Workhorses)** (Impact: 13.0)
    * *Intent:* /** * Creates query parameters and converts to string. */
  * `createQueryString` **(Stateful Encapsulated Methods)** (Impact: 8.6)
    * *Intent:* /** * Create device code endpoint query parameters and returns string */
  * `executePostRequestToDeviceCodeEndpoint` **(Stateful Encapsulated Methods)** (Impact: 4.2)
    * *Intent:* /** * Executes POST request to device code endpoint */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 22`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 4`, `concurrency: 13`, `import: 5`
* *Defense:* `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.844
  * `Choke Point (Betweenness):` 6.7e-05 | `Ripple Effect (Closeness):` 0.007246
  * `Imports (Out-Degree: 5):` ClientAuthErrorCodes.js, CommonDeviceCodeRequest.js, Constants.js, BaseClient.js, node
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/client/ManagedIdentitySources/AzureArc.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.713)
- **Top Global Matches:** file_cluster_9: 7.713, file_cluster_15: 8.126, file_cluster_16: 8.443
- **Magnitude:** 100.36 | **LOC:** 416 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 3.925; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (86.9%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getServerTokenResponseAsync` **(Many-Argument Workhorses)** (Impact: 30.4)
    * *Intent:* * * * - WWW-Authenticate header is missing or has unsupported format * - Platform is not supported (...
  * `tryCreate` **(Many-Argument Workhorses)** (Impact: 22.1)
    * *Intent:* * are supported for Azure Arc scenarios. The method performs comprehensive validation of * endpoint ...
  * `getEnvironmentVariables` **(I/O & Config Routines)** (Impact: 4.8)
    * *Intent:* /** * Retrieves and validates Azure Arc environment variables for managed identity configuration. * ...
  * `constructor` **(Many-Argument Workhorses)** (Impact: 3.5)
    * *Intent:* /** * Creates a new instance of the AzureArc managed identity source. * */
  * `createRequest` **(I/O & Config Routines)** (Impact: 2.3)
    * *Intent:* /** * Creates a properly formatted HTTP request for acquiring tokens from the Azure Arc identity end...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 27`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `io: 5`, `api: 9`, `concurrency: 4`, `import: 11`
* *Defense:* `safety: 11`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.925
  * `Choke Point (Betweenness):` 5.7e-05 | `Ripple Effect (Closeness):` 0.008152
  * `Imports (Out-Degree: 8):` NodeStorage.js, ManagedIdentityId.js, ManagedIdentityRequestParameters.js, CryptoProvider.js, ManagedIdentityError.js, ManagedIdentityTokenResponse.js, Constants.js, BaseManagedIdentitySource.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/client/ConfidentialClientApplication.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.56)
- **Top Global Matches:** file_cluster_8: 8.56, file_cluster_6: 10.273, file_cluster_4: 18.218
- **Magnitude:** 99.8 | **LOC:** 304 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 3.773; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.2%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.9%), Guard Balance (formerly Safety Score) (51.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Compute Cores)** (Impact: 28.5)
    * *Intent:* * - authority: the authority URL for your application. * - client credential: Must set either client...
  * `acquireTokenByClientCredential` **(Compute Cores)** (Impact: 18.3)
    * *Intent:* /** * Acquires tokens from the authority for the application (not for an end user). */
  * `acquireTokenOnBehalfOf` **(Defensive Guards)** (Impact: 6.1)
    * *Intent:* /** * Acquires tokens from the authority for the application. * * Used in scenarios where the curren...
  * `SetAppTokenProvider` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** * This extensibility point only works for the client_credential flow, i.e. acquireTokenByClientC...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 33`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`, `unreferenced_by_name: 4`
* *Architecture:* `api: 3`, `concurrency: 13`, `import: 13`
* *Defense:* `safety: 7`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.773
  * `Choke Point (Betweenness):` 0.000148 | `Ripple Effect (Closeness):` 0.005435
  * `Imports (Out-Degree: 12):` Configuration.js, ClientAuthErrorCodes.js, ClientCredentialRequest.js, CommonClientCredentialRequest.js, CommonOnBehalfOfRequest.js, OnBehalfOfRequest.js, Constants.js, ClientApplication.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/network/HttpClient.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.542)
- **Top Global Matches:** file_cluster_0: 6.542, file_cluster_10: 8.891, file_cluster_15: 9.755
- **Magnitude:** 81.44 | **LOC:** 222 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 6.362; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (79.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sendRequest` **(Many-Argument Workhorses)** (Impact: 31.0)
    * *Intent:* * * Error handling priority: * 1. Timeout errors (AbortError) are converted to "Request timeout" mes...
  * `sendGetRequestAsync` **(Generic / Templated Code)** (Impact: 6.3)
    * *Intent:* * Sends an HTTP GET request to the specified URL. * * This method handles GET requests with optional...
  * `getFetchHeaders` **(Callbacks & Closures)** (Impact: 6.3)
    * *Intent:* /** * Converts NetworkRequestOptions headers to a fetch-compatible Headers object. * * The MSAL libr...
  * `sendPostRequestAsync` **(Generic / Templated Code)** (Impact: 3.8)
    * *Intent:* /** * Sends an HTTP POST request to the specified URL. * * This method handles POST requests with re...
  * `getHeaderDict` **(Generic / Templated Code)** (Impact: 1.9)
    * *Intent:* /** * Converts a fetch Headers object to a plain JavaScript object. * * The fetch API returns header...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 18`, `args: 8`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 9`, `import: 2`
* *Defense:* `safety: 5`, `doc: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.362
  * `Choke Point (Betweenness):` 8.9e-05 | `Ripple Effect (Closeness):` 0.038309
  * `Imports (Out-Degree: 1):` Constants.js, node
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/network/HttpClientWithRetries.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.671)
- **Top Global Matches:** file_cluster_0: 5.671, file_cluster_13: 9.247, file_cluster_16: 9.274
- **Magnitude:** 66.78 | **LOC:** 90 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 4.258; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (92.5%), Mutation Surface (formerly State Flux) (87.3%), Guard Balance (formerly Safety Score) (54.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sendNetworkRequestAsync` **(Stateful Encapsulated Methods)** (Impact: 9.6)
  * `sendNetworkRequestAsyncHelper` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `sendGetRequestAsync` **(Generic / Templated Code)** (Impact: 3.8)
  * `sendPostRequestAsync` **(Generic / Templated Code)** (Impact: 3.8)
  * `constructor` **(State Mutators)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 14`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `concurrency: 11`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.258
  * `Choke Point (Betweenness):` 7.4e-05 | `Ripple Effect (Closeness):` 0.024704
  * `Imports (Out-Degree: 2):` IHttpRetryPolicy.js, Constants.js, node
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/client/ManagedIdentityClient.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.468)
- **Top Global Matches:** file_cluster_16: 7.468, file_cluster_15: 8.29, file_cluster_9: 8.346
- **Magnitude:** 66.16 | **LOC:** 190 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 3.957; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (72.7%), Guard Balance (formerly Safety Score) (52.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (45.2%)
- **Documentation Coverage:** 62.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `selectManagedIdentitySource` **(Many-Argument Workhorses)** (Impact: 21.6)
    * *Intent:* /** * Tries to create a managed identity source for all sources */
  * `sendManagedIdentityTokenRequest` **(Many-Argument Workhorses)** (Impact: 8.0)
  * `getManagedIdentitySource` **(I/O & Config Routines)** (Impact: 7.3)
    * *Intent:* /** * Determine the Managed Identity Source based on available environment variables. This API is co...
  * `constructor` **(State Mutators)** (Impact: 3.1)
  * `allEnvironmentVariablesAreDefined` **(Encapsulated Accessors)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 22`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 5`, `concurrency: 2`, `import: 14`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.957
  * `Choke Point (Betweenness):` 0.000703 | `Ripple Effect (Closeness):` 0.007246
  * `Imports (Out-Degree: 13):` NodeStorage.js, ManagedIdentityId.js, CryptoProvider.js, ManagedIdentityError.js, ManagedIdentityRequest.js, Constants.js, AppService.js, AzureArc.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/config/ManagedIdentityId.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.406)
- **Top Global Matches:** file_cluster_6: 8.406, file_cluster_8: 13.383, file_cluster_4: 13.985
- **Magnitude:** 62.62 | **LOC:** 74 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **3**; blast radius 10.543; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (65.5%), Guard Balance (formerly Safety Score) (62.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 26.0)
  * `id` **(Encapsulated Accessors)** (Impact: 1.6)
  * `idType` **(Encapsulated Accessors)** (Impact: 1.6)
  * `id` **(Interface Declarations)** (Impact: 1.1)
  * `idType` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 8`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.543
  * `Choke Point (Betweenness):` 0.001346 | `Ripple Effect (Closeness):` 0.063241
  * `Imports (Out-Degree: 3):` ManagedIdentityError.js, Constants.js, Configuration.js
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `package/src/client/ManagedIdentityApplication.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.088)
- **Top Global Matches:** file_cluster_11: 7.088, file_cluster_16: 7.162, file_cluster_15: 7.741
- **Magnitude:** 62.48 | **LOC:** 270 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 3.773; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.3%), Concurrency Surface (formerly Concurrency) (53.6%), Guard Balance (formerly Safety Score) (53.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 16.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `acquireToken` **(I/O & Config Routines)** (Impact: 17.8)
    * *Intent:* /** * Acquire an access token from the cache or the managed identity */
  * `constructor` **(I/O & Config Routines)** (Impact: 8.2)
  * `acquireTokenFromManagedIdentity` **(Stateful Encapsulated Methods)** (Impact: 5.2)
    * *Intent:* /** * Acquires a token from a managed identity endpoint. * */
  * `getManagedIdentitySource` **(Interface Declarations)** (Impact: 2.3)
    * *Intent:* /** * Determine the Managed Identity Source based on available environment variables. This API is co...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 22`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `unreferenced_by_name: 2`
* *Architecture:* `api: 3`, `concurrency: 6`, `import: 12`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.773
  * `Choke Point (Betweenness):` 0.000507 | `Ripple Effect (Closeness):` 0.005435
  * `Imports (Out-Degree: 11):` NodeStorage.js, Configuration.js, ManagedIdentityId.js, CryptoProvider.js, HashUtils.js, packageMetadata.js, ManagedIdentityRequest.js, ManagedIdentityRequestParams.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/config/Configuration.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.507)
- **Top Global Matches:** file_cluster_9: 7.507, file_cluster_0: 9.677, file_cluster_15: 10.835
- **Magnitude:** 50.78 | **LOC:** 268 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **4**; blast radius 9.518; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (57.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.3%), Mutation Surface (formerly State Flux) (33.1%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildManagedIdentityConfiguration` **(Defensive Guards)** (Impact: 14.3)
  * `buildAppConfiguration` **(Defensive Guards)** (Impact: 12.9)
    * *Intent:* /** * Sets the default options when not explicitly configured from app developer * * */
  * `loggerCallback` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 30`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 2`, `planned_debt: 1`
* *Architecture:* `api: 13`, `import: 4`
* *Defense:* `safety: 5`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.518
  * `Choke Point (Betweenness):` 0.001341 | `Ripple Effect (Closeness):` 0.057971
  * `Imports (Out-Degree: 3):` NodeAuthError.js, HttpClient.js, ManagedIdentityId.js, node
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `package/src/cache/distributed/DistributedCachePlugin.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.731)
- **Top Global Matches:** file_cluster_15: 6.731, file_cluster_13: 7.605, file_cluster_11: 8.052
- **Magnitude:** 49.68 | **LOC:** 73 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 3.773; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (97.1%), Mutation Surface (formerly State Flux) (84.9%), Guard Balance (formerly Safety Score) (57.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `afterCacheAccess` **(Type Conversions)** (Impact: 7.0)
    * *Intent:* /** * Serializes the cache after accessing it */
  * `constructor` **(State Mutators)** (Impact: 1.9)
  * `beforeCacheAccess` **(Parameter Forwarders)** (Impact: 1.8)
    * *Intent:* /** * Deserializes the cache before accessing it */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 15`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `concurrency: 9`, `import: 4`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.773
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005435
  * `Imports (Out-Degree: 3):` TokenCache.js, ICacheClient.js, IPartitionManager.js, node
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/network/LoopbackClient.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.463)
- **Top Global Matches:** file_cluster_9: 6.463, file_cluster_15: 9.889, file_cluster_16: 10.244
- **Magnitude:** 49.38 | **LOC:** 117 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 3.844; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.0%), Guard Balance (formerly Safety Score) (50.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (21.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `listenForAuthCode` **(Compute Cores)** (Impact: 25.1)
    * *Intent:* /** * Spins up a loopback server which returns the server response when the localhost redirectUri is...
  * `getRedirectUri` **(I/O & Config Routines)** (Impact: 7.8)
    * *Intent:* /** * Get the port that the loopback server is running on */
  * `closeServer` **(I/O & Config Routines)** (Impact: 3.8)
    * *Intent:* /** * Close the loopback server */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Concurrency (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 15`, `args: 5`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 3`, `import: 5`
* *Defense:* `doc: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.844
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007246
  * `Imports (Out-Degree: 3):` NodeAuthError.js, Constants.js, ILoopbackClient.js, node, http
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 13.632)
- **Top Global Matches:** file_cluster_13: 13.632, file_cluster_17: 13.827, file_cluster_15: 14.116
- **Magnitude:** 47.7 | **LOC:** 124 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **30**; blast radius 3.666; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (14.4%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 44`
* *Risk/State:* None
* *Architecture:* `api: 31`, `import: 31`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.666
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` ITokenCache.js, TokenCache.js, DistributedCachePlugin.js, ICacheClient.js, IPartitionManager.js, SerializerTypes.js, ClientAssertion.js, ConfidentialClientApplication.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/retry/ImdsRetryPolicy.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.655)
- **Top Global Matches:** file_cluster_11: 5.655, file_cluster_15: 6.901, file_cluster_13: 7.345
- **Magnitude:** 47.4 | **LOC:** 123 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 25.269; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.6%), Mutation Surface (formerly State Flux) (75.0%), Guard Balance (formerly Safety Score) (53.3%), Debt Markers (formerly Tech Debt) (50.0%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pauseForRetry` **(Many-Argument Workhorses)** (Impact: 20.8)
    * *Intent:* /** * Pauses execution for a calculated delay before retrying a request. * */
  * `isNewRequest` **(State Mutators)** (Impact: 1.6)
  * `MIN_EXPONENTIAL_BACKOFF_MS` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* /* * these are defined here as static variables despite being defined as constants outside of the * ...
  * `MAX_EXPONENTIAL_BACKOFF_MS` **(Interface Declarations)** (Impact: 1.1)
  * `EXPONENTIAL_DELTA_BACKOFF_MS` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 10
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 15`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `concurrency: 5`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.269
  * `Choke Point (Betweenness):` 0.001715 | `Ripple Effect (Closeness):` 0.083612
  * `Imports (Out-Degree: 2):` ExponentialRetryStrategy.js, IHttpRetryPolicy.js, node
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/cache/serializer/Deserializer.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.903)
- **Top Global Matches:** file_cluster_10: 6.903, file_cluster_15: 7.032, file_cluster_0: 8.025
- **Magnitude:** 45.96 | **LOC:** 222 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 9.238; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (26.7%), Debt Markers (formerly Tech Debt) (20.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserializeAllCache` **(Compute Cores)** (Impact: 9.4)
    * *Intent:* /** * Deserialize an inMemory Cache */
  * `deserializeAccounts` **(Callbacks & Closures)** (Impact: 5.9)
    * *Intent:* /** * Deserializes accounts to AccountEntity objects */
  * `deserializeAccessTokens` **(Type Conversions)** (Impact: 4.5)
    * *Intent:* /** * Deserializes access tokens to AccessTokenEntity objects */
  * `deserializeRefreshTokens` **(Callbacks & Closures)** (Impact: 4.1)
    * *Intent:* /** * Deserializes refresh tokens to RefreshTokenEntity objects */
  * `deserializeIdTokens` **(Callbacks & Closures)** (Impact: 3.9)
    * *Intent:* /** * Deserializes id tokens to IdTokenEntity objects */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 13`, `args: 13`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 1`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.238
  * `Choke Point (Betweenness):` 0.000549 | `Ripple Effect (Closeness):` 0.062903
  * `Imports (Out-Degree: 2):` SerializerTypes.js, node
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/utils/Constants.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.425)
- **Top Global Matches:** file_cluster_0: 5.425, file_cluster_2: 6.192, file_cluster_17: 6.492
- **Magnitude:** 45.22 | **LOC:** 187 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **2**; blast radius 49.723; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (12.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 39`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 28`, `import: 2`
* *Defense:* `doc: 15`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 49.723
  * `Choke Point (Betweenness):` 0.005227 | `Ripple Effect (Closeness):` 0.127174
  * `Imports (Out-Degree: 2):` DefaultManagedIdentityRetryPolicy.js, ImdsRetryPolicy.js
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `package/src/client/UsernamePasswordClient.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.439)
- **Top Global Matches:** file_cluster_16: 7.439, file_cluster_2: 7.701, file_cluster_15: 7.811
- **Magnitude:** 42.66 | **LOC:** 222 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 3.871; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (83.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (17.5%), Complexity Load (formerly Cognitive Load) (10.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createTokenRequestBody` **(I/O & Config Routines)** (Impact: 18.8)
    * *Intent:* /** * Generates a map for all the params to be sent to the service */
  * `acquireToken` **(I/O & Config Routines)** (Impact: 3.4)
    * *Intent:* /** * API to acquire a token by passing the username and password to the service in exchage of crede...
  * `executeTokenRequest` **(Stateful Encapsulated Methods)** (Impact: 3.4)
    * *Intent:* /** * Executes POST request to token endpoint */
  * `constructor` **(State Mutators)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 14`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 3`, `concurrency: 9`, `import: 4`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.871
  * `Choke Point (Betweenness):` 3e-05 | `Ripple Effect (Closeness):` 0.01087
  * `Imports (Out-Degree: 4):` CommonUsernamePasswordRequest.js, Constants.js, BaseClient.js, node
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `package/src/cache/serializer/Deserializer.ts` (TYPESCRIPT) | Magnitude: 45.96 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 167, core_var_decl: 16, structural_boundaries: 13, args: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `package/src/client/ManagedIdentitySources/AppService.ts` (TYPESCRIPT) | Magnitude: 33.14 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 14, import: 7, state_mutation: 5
- `package/src/client/ManagedIdentityApplication.ts` (TYPESCRIPT) | Magnitude: 62.48 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 181, structural_boundaries: 22, branch: 14, import: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/src/cache/distributed/ICacheClient.ts` (TYPESCRIPT) | Magnitude: 8.38 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 3, doc: 3, structural_boundaries: 2, args: 2
- `package/src/index.ts` (TYPESCRIPT) | Magnitude: 47.7 | Delta: **0.195** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 44, api: 31, import: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `package/src/client/ManagedIdentitySources/Imds.ts` (TYPESCRIPT) | Magnitude: 33.04 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 103, structural_boundaries: 14, import: 8, state_mutation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `package/src/cache/TokenCache.ts` (TYPESCRIPT) | Magnitude: 189.98 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 280, branch: 43, structural_boundaries: 41, core_var_decl: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `package/src/client/OnBehalfOfClient.ts` (TYPESCRIPT) | Magnitude: 118.38 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 316, branch: 26, structural_boundaries: 25, core_var_decl: 24

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/src/cache/TokenCache.ts` -> **Severity: 0.417** (Bridge: 0.0054 * Flux: 77.2113%)
- `package/lib/msal-node.cjs` -> **Severity: 0.333** (Bridge: 0.0035 * Flux: 96.0342%)
- `package/src/crypto/CryptoProvider.ts` -> **Severity: 0.159** (Bridge: 0.0034 * Flux: 46.609%)
- `package/src/config/ManagedIdentityId.ts` -> **Severity: 0.135** (Bridge: 0.0013 * Flux: 100.0%)
- `package/src/retry/ImdsRetryPolicy.ts` -> **Severity: 0.129** (Bridge: 0.0017 * Flux: 75.026%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/retry/ImdsRetryPolicy.ts` -> **Severity: 4.456** (Embedded: 0.0836 * Error Risk: 53.2952%)
- `package/src/crypto/CryptoProvider.ts` -> **Severity: 3.962** (Embedded: 0.0792 * Error Risk: 50.0%)
- `package/src/config/ManagedIdentityId.ts` -> **Severity: 3.927** (Embedded: 0.0632 * Error Risk: 62.1008%)
- `package/lib/msal-node.cjs` -> **Severity: 3.919** (Embedded: 0.0772 * Error Risk: 50.769%)
- `package/src/cache/NodeStorage.ts` -> **Severity: 3.772** (Embedded: 0.0723 * Error Risk: 52.193%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/retry/DefaultManagedIdentityRetryPolicy.ts` -> **Severity: 2686.0** (Blast Radius: 26.86 * Doc Risk: 100.0%)
- `package/src/retry/ImdsRetryPolicy.ts` -> **Severity: 2105.749** (Blast Radius: 25.269 * Doc Risk: 83.3333%)
- `package/src/config/ManagedIdentityId.ts` -> **Severity: 1054.3** (Blast Radius: 10.543 * Doc Risk: 100.0%)
- `package/src/error/ManagedIdentityError.ts` -> **Severity: 839.7** (Blast Radius: 8.397 * Doc Risk: 100.0%)
- `package/src/config/ManagedIdentityRequestParameters.ts` -> **Severity: 729.6** (Blast Radius: 7.296 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2583 call pairs -- scoped 57.9%, unique 0.0%, ambiguous 11.3%, external 30.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 1784 | 66.1% | 0.0% | 5.4% | 28.4% |
| typescript | 799 | 39.5% | 0.1% | 24.3% | 36.0% |

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
