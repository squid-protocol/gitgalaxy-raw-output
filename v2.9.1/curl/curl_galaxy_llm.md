# ARCHITECTURAL_BRIEF: curl
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/curl/curl` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1060 analyzed artifact(s), 229002 LOC.
- **Load-bearing artifact:** `lib/curl_setup.h` -- 296 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `lib/url.c` -- pulls in 63 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/vtls/openssl.c` at magnitude 4894.24 (structural weight, not risk).
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
| Total Artifacts | 4250 |
| Analyzed Artifacts (Scanned) | 1060 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3190 |
| Total LOC | 229002 |
| Volatility Index | 0.015 |
| % Scanned of codebase = | 24.9% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4451 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2316 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4668 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 25 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 818 | 181591 | 77.2% |
| PERL | 79 | 21599 | 7.5% |
| PYTHON | 47 | 10516 | 4.4% |
| SHELL | 33 | 2445 | 3.1% |
| PLAINTEXT | 27 | 0 | 2.5% |
| M4 | 26 | 12123 | 2.5% |
| MARKDOWN | 19 | 0 | 1.8% |
| YAML | 3 | 124 | 0.3% |
| MAKEFILE | 2 | 193 | 0.2% |
| DOCKERFILE | 1 | 10 | 0.1% |
| REXX | 1 | 4 | 0.1% |
| BATCH | 1 | 246 | 0.1% |
| JSON | 1 | 111 | 0.1% |
| CPP | 1 | 22 | 0.1% |
| HTML | 1 | 18 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `2.817`
> **Composition Archetype:** `Hub-Coupled App` (z +2.82; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 36%, Large Core Modules (3) 16%, Compute Cores Files 11%, Many-Argument Workhorses Files 10%, Data / Markup / Trivial 9%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1014 | 95.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 46 | 4.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3190*

**Composition by Extension & Reason:**
- `no_extension`: 1896x Unsupported Format (.undeterminable), 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Machine-Generated Source Code Signature: 89 LOC)
- `.md`: 900x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 129x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Machine-Generated Source Code Signature: 47 LOC), 2x Excluded (Machine-Generated Source Code Signature: 49 LOC)
- `.cmake`: 30x Excluded (Unsupported Extension: '.cmake')
- `.yml`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.am`: 14x Excluded (Unsupported Extension: '.am'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.com`: 19x Excluded (Unsupported Extension: '.com')
- `.txt`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pl`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 163 LOC), 1x Excluded (Machine-Generated Source Code Signature: 250 LOC)
- `.prm`: 8x Excluded (Unsupported Extension: '.prm')
- `.inc`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sln`: 3x Excluded (Unsupported Extension: '.sln')
- `.words`: 2x Unsupported Format (.words)
- `.toml`: 1x Unsupported Format (.toml), 1x Excluded (Unsupported Extension: '.toml')
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 306 LOC), 1x Excluded (Machine-Generated Source Code Signature: 144 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.5 | 27.6 | 18.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 58.5 | 75.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.6 | 10.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 14.9 | 2.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 26.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.5 | 3.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.1 | 0.4 | 0.3 | 1.1 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 98.5 | 21.4 | 14.8 | 5.6 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 51.8 | 50.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 63816 | 811 | 137 | `lib/multi.c` |
| cleanup | 432 | 99 | 0 | `tests/runtests.pl` |
| guards | 14227 | 916 | 37 | `lib/vtls/openssl.c` |
| danger | 1851 | 290 | 4 | `tests/ech_tests.sh` |
| concurrency | 138 | 49 | 0 | `tests/http/conftest.py` |
| connectivity | 5427 | 649 | 14 | `configure.ac` |
| io | 1957 | 202 | 4 | `tests/ech_tests.sh` |
| crypto | 2 | 1 | 0 | `tests/http/testenv/certs.py` |
| ipc | 536 | 129 | 1 | `tests/server/rtspd.c` |
| time | 405 | 90 | 0 | `tests/runtests.pl` |
| serialization | 2 | 1 | 0 | `.github/scripts/shellcheck-ci.sh` |
| regex | 1745 | 107 | 1 | `tests/runtests.pl` |
| events | 1568 | 122 | 1 | `m4/curl-functions.m4` |
| tests | 923 | 38 | 0 | `tests/http/test_02_download.py` |
| docs | 1436 | 831 | 1 | `lib/cfilters.h` |
| debt | 1665 | 208 | 2 | `tests/ech_tests.sh` |
| mutation | 57529 | 764 | 143 | `tests/libtest/lib557.c` |
| dead_code | 2457 | 667 | 6 | `lib/cfilters.c` |
| credential | 101 | 15 | 0 | `scripts/mk-ca-bundle.pl` |
| threat | 2869 | 403 | 7 | `tests/http/testenv/env.py` |
| ml_ai | 196 | 56 | 0 | `tests/runtests.pl` |
| ui | 9 | 4 | 0 | `scripts/managen` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **3.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/ech_tests.sh` (Hits: 128)
- `scripts/wcurl` (Hits: 68)
- `tests/http/test_07_upload.py` (Hits: 54)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **curl_setup.h** (`lib/curl_setup.h`) — 296 inbound connections
2. **urldata.h** (`lib/urldata.h`) — 141 inbound connections
3. **curl_trc.h** (`lib/curl_trc.h`) — 103 inbound connections
4. **tool_setup.h** (`src/tool_setup.h`) — 80 inbound connections
5. **unitcheck.h** (`tests/libtest/unitcheck.h`) — 73 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **url.c** (`lib/url.c`) — 63 outbound dependencies
2. **curl_setup.h** (`lib/curl_setup.h`) — 50 outbound dependencies
3. **http.c** (`lib/http.c`) — 45 outbound dependencies
4. **openssl.c** (`lib/vtls/openssl.c`) — 43 outbound dependencies
5. **easy.c** (`lib/easy.c`) — 39 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `APPEND_imap` **(Many-Argument Workhorses)** (@ `tests/ftpserver.pl`) -> Impact: **2135.3** | LOC: 1672
- `singletest_check` **(Many-Argument Workhorses)** (@ `tests/runtests.pl`) -> Impact: **605.4** | LOC: 679
  * *Intent:* ####################################################################### # Verify test succeeded
- `ossl_connect_step2` **(Many-Argument Workhorses)** (@ `lib/vtls/openssl.c`) -> Impact: **548.0** | LOC: 1400
  * *Intent:* #endif
- `single` **(Many-Argument Workhorses)** (@ `scripts/managen`) -> Impact: **507.8** | LOC: 406
- `opt_string` **(Many-Argument Workhorses)** (@ `src/tool_getparam.c`) -> Impact: **418.8** | LOC: 536
  * *Intent:* /* opt_string handles string options */
- `startservers` **(Compute Cores)** (@ `tests/servers.pm`) -> Impact: **403.5** | LOC: 660
  * *Intent:* ####################################################################### # startservers() starts all the named servers # # 0 for success # 1 for an err...
- `parsefmt` **(Many-Argument Workhorses)** (@ `lib/mprintf.c`) -> Impact: **383.8** | LOC: 426
  * *Intent:* #define PFMT_OK 0 #define PFMT_DOLLAR 1 /* bad dollar for main param */ #define PFMT_DOLLARWIDTH 2 /* bad dollar use for width */ #define PFMT_DOLLARP...
- `setopt_cptr` **(Many-Argument Workhorses)** (@ `lib/setopt.c`) -> Impact: **376.8** | LOC: 695
  * *Intent:* #endif
- `opt_bool` **(Many-Argument Workhorses)** (@ `src/tool_getparam.c`) -> Impact: **325.2** | LOC: 385
  * *Intent:* /* opt_bool is the function that handles boolean options */
- `single` **(Compute Cores)** (@ `scripts/cd2nroff`) -> Impact: **319.9** | LOC: 374

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib` | 264 | 84081.78 | 33.92% | 17.86% |
| `src` | 91 | 18649.1 | 31.02% | 17.8% |
| `tests` | 53 | 18466.94 | 32.45% | 0.0% |
| `lib/vtls` | 29 | 17537.08 | 35.07% | 10.41% |
| `tests/libtest` | 262 | 16546.92 | 18.98% | 0.0% |
| `tests/server` | 14 | 9516.9 | 28.47% | 0.0% |
| `tests/http` | 32 | 7046.86 | 29.15% | 0.0% |
| `scripts` | 37 | 5725.56 | 54.42% | 8.27% |
| `lib/vssh` | 5 | 5541.32 | 42.77% | 8.56% |
| `tests/http/testenv` | 13 | 4840.68 | 33.26% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lib/curlx/warnless.c` -> **99.6102%** Exposure
- `lib/uint-bset.c` -> **99.3845%** Exposure
- `lib/uint-table.c` -> **99.3415%** Exposure
- `.github/scripts/cmp-pkg-config.sh` -> **99.3307%** Exposure
- `m4/curl-override.m4` -> **99.3307%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.github/scripts/cleancmd.pl` -> **100.0%** Exposure
- `.github/scripts/randcurl.pl` -> **100.0%** Exposure
- `scripts/badwords` -> **100.0%** Exposure
- `scripts/cd2cd` -> **100.0%** Exposure
- `scripts/cd2nroff` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lib/cfilters.c` -> **48** Orphaned Functions | **0** Duplicates
- `tests/http/test_07_upload.py` -> **39** Orphaned Functions | **0** Duplicates
- `tests/http/test_02_download.py` -> **38** Orphaned Functions | **0** Duplicates
- `m4/curl-functions.m4` -> **37** Orphaned Functions | **0** Duplicates
- `lib/vtls/vtls.c` -> **32** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `scripts/mk-ca-bundle.pl` -> **100.0%** Exposure
- `lib/vtls/x509asn1.c` -> **73.8141%** Exposure
- `lib/vtls/schannel_verify.c` -> **16.3812%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4131` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/vtls/openssl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 4894.24 | **LOC:** 5520 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 70.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **43**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (96.8%), Guard Balance (formerly Safety Score) (88.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.5595% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ossl_connect_step2` **(Many-Argument Workhorses)** (Impact: 548.0)
    * *Intent:* #endif
  * `Curl_ossl_ctx_init` **(Many-Argument Workhorses)** (Impact: 197.3)
  * `client_cert` **(Many-Argument Workhorses)** (Impact: 179.4)
  * `ossl_verifyhost` **(Many-Argument Workhorses)** (Impact: 117.1)
    * *Intent:* */
  * `ossl_init_ech` **(Many-Argument Workhorses)** (Impact: 93.9)
    * *Intent:* #ifdef HAVE_SSL_SET1_ECH_CONFIG_LIST
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 535 instances
* *State Mutation (weighted view):* 1626
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1071`, `structural_boundaries: 759`, `args: 236`, `func_start: 95`, `class_start: 138`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 556`, `dead_code: 7`, `fragile_debt: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 18`, `import: 43`
* *Defense:* `safety: 51`, `doc: 2`, `immutability_locks: 138`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` connect.h, curl_setup.h, curl_trc.h, base64.h, inet_pton.h, strcopy.h, strdup.h, strerr.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/http.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 4752.48 | **LOC:** 5020 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 47.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **45**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (92.0%), Complexity Load (formerly Cognitive Load) (81.9%)
- **Documentation Coverage:** 98.3146% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `http_on_response` **(Many-Argument Workhorses)** (Impact: 231.4)
  * `http_add_hd` **(Many-Argument Workhorses)** (Impact: 150.3)
  * `Curl_http_follow` **(Many-Argument Workhorses)** (Impact: 150.2)
  * `http_rw_hd` **(Many-Argument Workhorses)** (Impact: 119.6)
  * `Curl_add_custom_headers` **(Many-Argument Workhorses)** (Impact: 113.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 604 instances
* *State Mutation (weighted view):* 1820
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1189`, `structural_boundaries: 642`, `args: 146`, `func_start: 96`, `class_start: 113`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 612`, `dead_code: 14`, `fragile_debt: 4`, `unreferenced_by_name: 6`
* *Architecture:* `api: 34`, `import: 45`
* *Defense:* `safety: 62`, `doc: 5`, `immutability_locks: 110`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 39):` altsvc.h, inet.h, bufref.h, cfilters.h, connect.h, content_encoding.h, cookie.h, curl_setup.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ftpserver.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4074.24 | **LOC:** 3374 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (87.9%), Complexity Load (formerly Cognitive Load) (44.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.4%), Connectivity (formerly Api Exposure) (10.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `APPEND_imap` **(Many-Argument Workhorses)** (Impact: 2135.3)
  * `customize` **(Compute Cores)** (Impact: 91.7)
    * *Intent:* #********************************************************************** # customize configures test ...
  * `eXsysread` **(Many-Argument Workhorses)** (Impact: 86.7)
    * *Intent:* #********************************************************************** # eXsysread is a wrapper aro...
  * `PASV_ftp` **(Many-Argument Workhorses)** (Impact: 70.9)
  * `PORT_ftp` **(Compute Cores)** (Impact: 57.0)
    * *Intent:* # # Support both PORT and EPRT here. #
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 259 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 800
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 714`, `structural_boundaries: 544`, `args: 55`, `func_start: 79`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 4`, `state_mutation: 282`, `dead_code: 3`, `planned_debt: 2`
* *Architecture:* `io: 34`, `api: 79`, `import: 25`
* *Defense:* `safety: 4`, `sync_locks: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Digest::MD5, File::Basename, IPC::Open2, NODATACONN, NODATACONN150, NODATACONN421, NODATACONN425, PASVBADIP...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/ftp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3772.62 | **LOC:** 4500 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 60.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **36**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (95.0%), Guard Balance (formerly Safety Score) (93.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 86.4583% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ftp_pp_statemachine` **(Many-Argument Workhorses)** (Impact: 175.3)
  * `ftp_done` **(Many-Argument Workhorses)** (Impact: 169.9)
    * *Intent:* /*********************************************************************** * * ftp_done() * * The DONE...
  * `ftp_state_pasv_resp` **(Many-Argument Workhorses)** (Impact: 95.5)
  * `ftp_state_quote` **(Many-Argument Workhorses)** (Impact: 89.1)
  * `ftp_port_parse_string` **(Many-Argument Workhorses)** (Impact: 88.5)
    * *Intent:* /* * Parse the CURLOPT_FTPPORT string * "(ipv4|ipv6|domain|interface)?(:port(-range)?)?" * and extra...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 485 instances
* *State Mutation (weighted view):* 1481
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 890`, `structural_boundaries: 669`, `args: 103`, `func_start: 83`, `class_start: 177`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 511`, `dead_code: 21`, `unreferenced_by_name: 1`
* *Architecture:* `api: 6`, `import: 36`
* *Defense:* `safety: 33`, `doc: 13`, `immutability_locks: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` inet.h, cf-socket.h, cfilters.h, connect.h, curl_addrinfo.h, curl_ctype.h, curl_range.h, curl_setup.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tool_getparam.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3745.86 | **LOC:** 3155 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 65.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `opt_string` **(Many-Argument Workhorses)** (Impact: 418.8)
    * *Intent:* /* opt_string handles string options */
  * `opt_bool` **(Many-Argument Workhorses)** (Impact: 325.2)
    * *Intent:* /* opt_bool is the function that handles boolean options */
  * `getparameter` **(Many-Argument Workhorses)** (Impact: 140.4)
    * *Intent:* /* the longest command line option, excluding the leading -- */ #define MAX_OPTION_LEN 26
  * `opt_file` **(Many-Argument Workhorses)** (Impact: 99.9)
    * *Intent:* /* opt_file handles file options */
  * `parse_args` **(Compute Cores)** (Impact: 62.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 624 instances
* *State Mutation (weighted view):* 1875
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 831`, `structural_boundaries: 523`, `args: 53`, `func_start: 44`, `class_start: 19`
* *Risk/State:* `state_mutation: 627`, `dead_code: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 9`, `import: 15`
* *Defense:* `safety: 22`, `doc: 1`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` tool_cb_prg.h, tool_cfgable.h, tool_filetime.h, tool_formparse.h, tool_getparam.h, tool_help.h, tool_helpers.h, tool_libinfo.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/multi.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3217.18 | **LOC:** 4169 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 39.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (95.9%), Guard Balance (formerly Safety Score) (91.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `multi_runsingle` **(Many-Argument Workhorses)** (Impact: 174.1)
  * `curl_multi_setopt` **(Many-Argument Workhorses)** (Impact: 94.2)
    * *Intent:* #undef curl_multi_setopt
  * `multi_winsock_select` **(Many-Argument Workhorses)** (Impact: 89.3)
  * `multi_wait` **(Many-Argument Workhorses)** (Impact: 77.8)
    * *Intent:* #endif /* !USE_WINSOCK */ #define NUM_POLLS_ON_STACK 10
  * `Curl_multi_pollset` **(Many-Argument Workhorses)** (Impact: 73.3)
    * *Intent:* /* Initializes `poll_set` with the current socket poll actions needed * for transfer `data`. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 407 instances
* *State Mutation (weighted view):* 1252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 761`, `structural_boundaries: 619`, `args: 131`, `func_start: 104`, `class_start: 141`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 438`, `dead_code: 15`, `fragile_debt: 1`, `unreferenced_by_name: 29`
* *Architecture:* `api: 50`, `import: 25`
* *Defense:* `safety: 13`, `doc: 1`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` bufref.h, cfilters.h, conncache.h, connect.h, curl_setup.h, curl_share.h, curl_trc.h, wait.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/url.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3082.88 | **LOC:** 3788 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 45.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **63**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (98.5%), Guard Balance (formerly Safety Score) (95.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 87.7698% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_proxy` **(Many-Argument Workhorses)** (Impact: 128.8)
    * *Intent:* #endif /* CURL_DISABLE_HTTP */ /* * If this is supposed to use a proxy, we need to figure out the pr...
  * `parseurlandfillconn` **(Many-Argument Workhorses)** (Impact: 121.7)
    * *Intent:* #else #define zonefrom_url(a, b, c) Curl_nop_stmt #endif /* * Parse URL and fill in the relevant mem...
  * `parse_connect_to_slist` **(Many-Argument Workhorses)** (Impact: 96.0)
    * *Intent:* /* * Processes all strings in the "connect to" slist, and uses the "connect * to host" and "connect ...
  * `create_conn_helper_init_proxy` **(Many-Argument Workhorses)** (Impact: 83.0)
    * *Intent:* /* create_conn helper to parse and init proxy values. to be called after Unix socket init but before...
  * `override_login` **(Many-Argument Workhorses)** (Impact: 73.6)
    * *Intent:* #endif /* * Override the login details from the URL with that in the CURLOPT_USERPWD * option or a ....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 436 instances
* *State Mutation (weighted view):* 1401
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 746`, `structural_boundaries: 453`, `args: 102`, `func_start: 69`, `class_start: 79`
* *Risk/State:* `state_mutation: 529`, `dead_code: 9`, `fragile_debt: 1`, `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 19`, `import: 63`
* *Defense:* `safety: 15`, `doc: 22`, `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 51):` Iphlpapi.h, altsvc.h, inet.h, bufref.h, cfilters.h, conncache.h, connect.h, cookie.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/servers.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 3064.86 | **LOC:** 3220 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **24**; blast radius 0.766; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (94.0%), Connectivity (formerly Api Exposure) (62.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.1%), Complexity Load (formerly Cognitive Load) (40.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `startservers` **(Compute Cores)** (Impact: 403.5)
    * *Intent:* ####################################################################### # startservers() starts all ...
  * `verifyhttp` **(Many-Argument Workhorses)** (Impact: 115.1)
    * *Intent:* ####################################################################### # Verify that the server tha...
  * `verifyhttptls` **(Many-Argument Workhorses)** (Impact: 89.5)
    * *Intent:* ####################################################################### # Verify that the non-stunne...
  * `verifyrtsp` **(Many-Argument Workhorses)** (Impact: 84.3)
    * *Intent:* ####################################################################### # Verify that the server tha...
  * `runsshserver` **(Many-Argument Workhorses)** (Impact: 75.9)
    * *Intent:* ####################################################################### # Start the ssh (scp/sftp) s...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 347 instances
* *State Mutation (weighted view):* 1076
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 878`, `structural_boundaries: 757`, `args: 41`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 382`, `dead_code: 9`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 22`, `api: 50`, `concurrency: 2`, `import: 21`
* *Defense:* `safety: 2`, `sync_locks: 3`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.766
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.002828
  * `Imports (Out-Degree: 5):` File::Temp, IO::Socket, POSIX, Time::HiRes, a, an, base, by...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib/vssh/libssh2.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2779.22 | **LOC:** 3867 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 71.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.6%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ssh_statemachine` **(Many-Argument Workhorses)** (Impact: 310.8)
    * *Intent:* /* * ssh_statemachine() runs the SSH state machine as far as it can without * blocking and without r...
  * `sftp_upload_init` **(Many-Argument Workhorses)** (Impact: 87.3)
  * `sftp_quote` **(Many-Argument Workhorses)** (Impact: 84.0)
  * `sftp_quote_stat` **(Many-Argument Workhorses)** (Impact: 68.1)
  * `ssh_knownhost` **(Many-Argument Workhorses)** (Impact: 63.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 321 instances
* *State Mutation (weighted view):* 993
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 706`, `structural_boundaries: 690`, `args: 85`, `func_start: 86`, `class_start: 138`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 351`, `dead_code: 7`
* *Architecture:* `api: 6`, `import: 23`
* *Defense:* `safety: 31`, `doc: 1`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` inet.h, cfilters.h, connect.h, curl_setup.h, curl_trc.h, base64.h, fopen.h, strparse.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/setopt.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2772.52 | **LOC:** 2933 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 40.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setopt_cptr` **(Many-Argument Workhorses)** (Impact: 376.8)
    * *Intent:* #endif
  * `setopt_long_bool` **(Many-Argument Workhorses)** (Impact: 184.3)
    * *Intent:* #endif
  * `setopt_long_net` **(Many-Argument Workhorses)** (Impact: 120.4)
  * `setopt_func` **(Many-Argument Workhorses)** (Impact: 95.4)
  * `setopt_long_proto` **(Many-Argument Workhorses)** (Impact: 95.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 375 instances
* *State Mutation (weighted view):* 1136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 709`, `structural_boundaries: 545`, `args: 65`, `func_start: 34`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 386`, `dead_code: 1`
* *Architecture:* `api: 5`, `import: 20`
* *Defense:* `safety: 6`, `doc: 1`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` altsvc.h, bufref.h, content_encoding.h, curl_setup.h, curl_share.h, curl_trc.h, strdup.h, escape.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/runtests.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2703.34 | **LOC:** 3372 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (97.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.7%), Complexity Load (formerly Cognitive Load) (48.0%), Connectivity (formerly Api Exposure) (9.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `singletest_check` **(Many-Argument Workhorses)** (Impact: 605.4)
    * *Intent:* ####################################################################### # Verify test succeeded
  * `checksystemfeatures` **(I/O & Config Routines)** (Impact: 130.2)
    * *Intent:* ####################################################################### # Check & display informatio...
  * `displaylogs` **(Compute Cores)** (Impact: 82.5)
  * `singletest_shouldrun` **(I/O & Config Routines)** (Impact: 69.0)
    * *Intent:* ####################################################################### # Verify that this test case...
  * `singletest` **(Many-Argument Workhorses)** (Impact: 66.9)
    * *Intent:* ####################################################################### # Run a single specified tes...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 426 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 1336
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 911`, `structural_boundaries: 530`, `args: 21`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 18`, `state_mutation: 484`, `dead_code: 5`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `io: 27`, `api: 39`, `concurrency: 1`, `import: 33`
* *Defense:* `safety: 4`, `sync_locks: 2`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Digest::MD5, File::Basename, I18N::Langinfo, List::Util, POSIX, Time::HiRes, a, additional...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/vssh/libssh.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2464.72 | **LOC:** 3015 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 61.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (85.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `myssh_statemach_act` **(Many-Argument Workhorses)** (Impact: 288.7)
    * *Intent:* /* * ssh_statemach_act() runs the SSH state machine as far as it can without * blocking and without ...
  * `myssh_is_known` **(Many-Argument Workhorses)** (Impact: 97.7)
    * *Intent:* /* Multiple options: * 1. data->set.str[STRING_SSH_HOST_PUBLIC_KEY_MD5] is set with an MD5 * hash (9...
  * `myssh_in_SFTP_QUOTE` **(Many-Argument Workhorses)** (Impact: 95.7)
  * `myssh_in_UPLOAD_INIT` **(Many-Argument Workhorses)** (Impact: 73.4)
  * `myssh_in_SFTP_QUOTE_STAT` **(Many-Argument Workhorses)** (Impact: 46.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 345 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1060
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 561`, `structural_boundaries: 515`, `args: 72`, `func_start: 70`, `class_start: 98`
* *Risk/State:* `state_mutation: 370`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 23`
* *Defense:* `safety: 18`, `doc: 1`, `immutability_locks: 17`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` inet.h, cfilters.h, connect.h, curl_setup.h, curl_trc.h, strparse.h, fcntl.h, hostip.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server/sws.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 2440.86 | **LOC:** 2484 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 84.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.471; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (97.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.3%), Complexity Load (formerly Cognitive Load) (40.9%), Dead Code Surface (formerly Dead Code) (6.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `http_connect` **(Many-Argument Workhorses)** (Impact: 303.6)
    * *Intent:* * This function needs to connect to the server, and then pass data between * the client and the serv...
  * `test_sws` **(Many-Argument Workhorses)** (Impact: 237.3)
  * `sws_ProcessRequest` **(Many-Argument Workhorses)** (Impact: 202.9)
  * `sws_send_doc` **(Many-Argument Workhorses)** (Impact: 128.2)
    * *Intent:* /* returns -1 on failure */
  * `sws_get_request` **(Many-Argument Workhorses)** (Impact: 76.1)
    * *Intent:* /* returns 1 if the connection should be serviced again immediately, 0 if there is no data waiting, ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 15 instances
* *Amplified Cascading Flux:* 386 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 1199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 598`, `structural_boundaries: 171`, `args: 44`, `func_start: 15`, `class_start: 7`
* *Risk/State:* `state_mutation: 427`, `dead_code: 7`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 20`, `api: 1`, `import: 2`
* *Defense:* `safety: 33`, `doc: 1`, `immutability_locks: 39`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` first.h, tcp.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/libtest/lib557.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 2405.2 | **LOC:** 1560 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.471; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (33.3%), Complexity Load (formerly Cognitive Load) (28.1%), Dead Code Surface (formerly Dead Code) (5.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_unsigned_int_formatting` **(I/O & Config Routines)** (Impact: 12.0)
  * `test_signed_int_formatting` **(I/O & Config Routines)** (Impact: 12.0)
  * `test_unsigned_long_formatting` **(I/O & Config Routines)** (Impact: 12.0)
  * `test_signed_long_formatting` **(I/O & Config Routines)** (Impact: 12.0)
  * `test_weird_arguments` **(I/O & Config Routines)** (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 148 instances
* *State Mutation (weighted view):* 2235
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 65`, `args: 38`, `func_start: 17`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1939`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` first.h, locale.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/http2.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2395.72 | **LOC:** 3028 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 61.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `on_header` **(Many-Argument Workhorses)** (Impact: 113.7)
    * *Intent:* /* frame->hd.type is either NGHTTP2_HEADERS or NGHTTP2_PUSH_PROMISE */
  * `h2_submit` **(Many-Argument Workhorses)** (Impact: 85.8)
  * `on_stream_frame` **(Many-Argument Workhorses)** (Impact: 69.7)
  * `cf_h2_send` **(Many-Argument Workhorses)** (Impact: 57.4)
  * `h2_progress_ingress` **(Many-Argument Workhorses)** (Impact: 51.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 299 instances
* *State Mutation (weighted view):* 936
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 508`, `structural_boundaries: 572`, `args: 94`, `func_start: 82`, `class_start: 176`
* *Risk/State:* `state_mutation: 338`, `dead_code: 3`, `unreferenced_by_name: 7`
* *Architecture:* `api: 19`, `import: 22`
* *Defense:* `safety: 59`, `doc: 2`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` bufq.h, bufref.h, cfilters.h, connect.h, curl_setup.h, curl_trc.h, base64.h, dynbuf.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tool_operate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2274.04 | **LOC:** 2414 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 53.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **39**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (82.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `retrycheck` **(Many-Argument Workhorses)** (Impact: 187.7)
  * `create_single` **(Many-Argument Workhorses)** (Impact: 170.1)
    * *Intent:* /* create a transfer */
  * `operate` **(Many-Argument Workhorses)** (Impact: 88.4)
  * `setup_outfile` **(Many-Argument Workhorses)** (Impact: 77.7)
  * `post_per_transfer` **(Many-Argument Workhorses)** (Impact: 59.7)
    * *Intent:* /* * Call this after a transfer has completed. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 301 instances
* *State Mutation (weighted view):* 923
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 583`, `structural_boundaries: 308`, `args: 69`, `func_start: 45`, `class_start: 63`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 321`, `dead_code: 7`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 6`, `import: 39`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` config2setopts.h, nonblock.h, fabdef.h, locale.h, in.h, dos.h, select.h, tool_cb_hdr.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/vquic/curl_ngtcp2.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2228.98 | **LOC:** 2951 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 62.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.2456% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `h3_stream_open` **(Many-Argument Workhorses)** (Impact: 70.3)
  * `cf_ngtcp2_query` **(Many-Argument Workhorses)** (Impact: 67.6)
  * `cf_ngtcp2_connect` **(Many-Argument Workhorses)** (Impact: 63.2)
  * `cf_ngtcp2_send` **(Many-Argument Workhorses)** (Impact: 57.6)
  * `cf_progress_egress` **(Many-Argument Workhorses)** (Impact: 53.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 287 instances
* *State Mutation (weighted view):* 895
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 465`, `structural_boundaries: 609`, `args: 116`, `func_start: 74`, `class_start: 218`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 321`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 7`, `import: 34`
* *Defense:* `safety: 46`, `doc: 4`, `immutability_locks: 32`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` bufref.h, cf-socket.h, cfilters.h, connect.h, curl_setup.h, curl_trc.h, dynbuf.h, fopen.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/mime.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2199.88 | **LOC:** 2229 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 87.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Curl_mime_prepare_headers` **(Many-Argument Workhorses)** (Impact: 154.0)
  * `cr_mime_read` **(Many-Argument Workhorses)** (Impact: 75.5)
    * *Intent:* /* Real client reader to installed client callbacks. */
  * `readback_part` **(Many-Argument Workhorses)** (Impact: 68.9)
    * *Intent:* /* Readback a mime part. */
  * `read_part_content` **(Many-Argument Workhorses)** (Impact: 61.3)
    * *Intent:* /* Read a non-encoded part content. */
  * `encoder_qp_read` **(Many-Argument Workhorses)** (Impact: 60.9)
    * *Intent:* /* Quoted-printable encoder. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 313 instances
* *State Mutation (weighted view):* 965
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 440`, `structural_boundaries: 362`, `args: 89`, `func_start: 83`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 339`, `dead_code: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 2`, `api: 36`, `import: 15`
* *Defense:* `safety: 73`, `doc: 1`, `immutability_locks: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` curl_setup.h, curl_trc.h, base64.h, basename.h, dynbuf.h, fopen.h, strcopy.h, strdup.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/urlapi.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2175.12 | **LOC:** 2001 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 57.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.0%), Complexity Load (formerly Cognitive Load) (83.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `curl_url_set` **(Many-Argument Workhorses)** (Impact: 166.2)
  * `urlget_url` **(Many-Argument Workhorses)** (Impact: 141.8)
  * `curl_url_get` **(Many-Argument Workhorses)** (Impact: 85.2)
  * `parse_file` **(Many-Argument Workhorses)** (Impact: 74.3)
  * `dedotdotify` **(Many-Argument Workhorses)** (Impact: 61.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 285 instances
* *State Mutation (weighted view):* 861
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 553`, `structural_boundaries: 266`, `args: 50`, `func_start: 38`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 291`, `dead_code: 10`, `unreferenced_by_name: 4`
* *Architecture:* `api: 13`, `import: 12`
* *Defense:* `safety: 53`, `doc: 1`, `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` curl_memrchr.h, curl_setup.h, inet_ntop.h, inet_pton.h, strdup.h, strparse.h, escape.h, idn.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/vtls/schannel.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2162.46 | **LOC:** 2875 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 69.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `schannel_recv` **(Many-Argument Workhorses)** (Impact: 153.6)
  * `get_client_cert` **(Many-Argument Workhorses)** (Impact: 115.0)
  * `schannel_connect_step2` **(Many-Argument Workhorses)** (Impact: 103.4)
  * `schannel_recv_renegotiate` **(Many-Argument Workhorses)** (Impact: 99.1)
    * *Intent:* first to complete the renegotiation. */
  * `schannel_shutdown` **(Many-Argument Workhorses)** (Impact: 69.6)
    * *Intent:* if the SSL connection failed (eg connection made but failed handshake). */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 281 instances
* *State Mutation (weighted view):* 891
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 515`, `structural_boundaries: 329`, `args: 106`, `func_start: 38`, `class_start: 67`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 329`, `dead_code: 3`, `unreferenced_by_name: 2`
* *Architecture:* `io: 3`, `api: 6`, `import: 20`
* *Defense:* `safety: 37`, `doc: 2`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` connect.h, curl_setup.h, curl_sha256.h, curl_trc.h, fopen.h, multibyte.h, strdup.h, strparse.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/vtls/gtls.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1978.66 | **LOC:** 2315 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.6%)
- **Documentation Coverage:** 99.0991% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Curl_gtls_verifyserver` **(Many-Argument Workhorses)** (Impact: 217.0)
    * *Intent:* #endif /* USE_APPLE_SECTRUST */
  * `gtls_client_init` **(Many-Argument Workhorses)** (Impact: 110.2)
  * `Curl_gtls_ctx_init` **(Many-Argument Workhorses)** (Impact: 97.3)
    * *Intent:* #endif
  * `gtls_populate_creds` **(Many-Argument Workhorses)** (Impact: 67.7)
  * `gtls_shutdown` **(Many-Argument Workhorses)** (Impact: 50.6)
    * *Intent:* /* * This function is called to shut down the SSL layer but keep the * socket open (CCC - Clear Comm...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 250 instances
* *State Mutation (weighted view):* 769
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 424`, `structural_boundaries: 368`, `args: 70`, `func_start: 53`, `class_start: 105`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 269`, `dead_code: 2`
* *Architecture:* `io: 3`, `api: 12`, `import: 22`
* *Defense:* `safety: 38`, `doc: 2`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` connect.h, curl_setup.h, curl_trc.h, fopen.h, strdup.h, abstract.h, crypto.h, gnutls.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/managen` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1864.54 | **LOC:** 1384 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.471; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.6%), Complexity Load (formerly Cognitive Load) (96.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `single` **(Many-Argument Workhorses)** (Impact: 507.8)
  * `render` **(Many-Argument Workhorses)** (Impact: 302.3)
  * `getshortlong` **(Compute Cores)** (Impact: 55.0)
  * `printdesc` **(Many-Argument Workhorses)** (Impact: 36.7)
  * `listglobals` **(Compute Cores)** (Impact: 36.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 216 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 650
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 526`, `structural_boundaries: 289`, `args: 23`, `func_start: 27`
* *Risk/State:* `high_risk_execution: 12`, `state_mutation: 218`, `dead_code: 3`
* *Architecture:* `io: 13`, `api: 27`, `import: 9`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` POSIX, commas, extra, in, of, proper, several, spaces...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/imap.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1795.82 | **LOC:** 2327 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 51.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.2%)
- **Documentation Coverage:** 41.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `imap_endofresp` **(Many-Argument Workhorses)** (Impact: 120.3)
    * *Intent:* /*********************************************************************** * * imap_endofresp() * * Ch...
  * `imap_state_capability_resp` **(Many-Argument Workhorses)** (Impact: 77.5)
    * *Intent:* /* For CAPABILITY responses */
  * `imap_parse_url_path` **(Many-Argument Workhorses)** (Impact: 73.4)
    * *Intent:* /*********************************************************************** * * imap_parse_url_path() *...
  * `imap_perform` **(Many-Argument Workhorses)** (Impact: 73.2)
    * *Intent:* /*********************************************************************** * * imap_perform() * * This...
  * `imap_state_listsearch_resp` **(Many-Argument Workhorses)** (Impact: 68.9)
    * *Intent:* /* For LIST and SEARCH responses */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 214 instances
* *State Mutation (weighted view):* 647
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 457`, `structural_boundaries: 354`, `args: 59`, `func_start: 54`, `class_start: 82`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 219`, `dead_code: 2`
* *Architecture:* `api: 4`, `import: 27`
* *Defense:* `safety: 27`, `doc: 31`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` inet.h, bufref.h, cfilters.h, connect.h, curl_sasl.h, curl_setup.h, curl_trc.h, dynbuf.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/cf-socket.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1737.18 | **LOC:** 2256 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 57.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **31**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (88.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 95.9459% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bindlocal` **(Many-Argument Workhorses)** (Impact: 142.0)
    * *Intent:* #ifndef CURL_DISABLE_BINDLOCAL
  * `cf_socket_open` **(Many-Argument Workhorses)** (Impact: 60.7)
  * `cf_socket_send` **(Many-Argument Workhorses)** (Impact: 54.4)
    * *Intent:* #endif /* USE_WINSOCK */
  * `cf_socket_query` **(Many-Argument Workhorses)** (Impact: 52.1)
  * `tcpkeepalive` **(Many-Argument Workhorses)** (Impact: 47.6)
    * *Intent:* /* Solaris < 11.4, DragonFlyBSD < 500702 and Windows < 10.0.16299 * use millisecond units. */ #defin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 243 instances
* *State Mutation (weighted view):* 756
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 370`, `structural_boundaries: 346`, `args: 107`, `func_start: 45`, `class_start: 87`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 270`, `dead_code: 4`, `fragile_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `io: 6`, `api: 11`, `import: 31`
* *Defense:* `safety: 8`, `doc: 5`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` inet.h, cf-socket.h, cfilters.h, conncache.h, connect.h, curl_addrinfo.h, curl_setup.h, curl_trc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/http/testenv/curl.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1708.64 | **LOC:** 1309 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.5%), Complexity Load (formerly Cognitive Load) (47.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.8%), Connectivity (formerly Api Exposure) (39.2%)
- **Documentation Coverage:** 98.7261% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_complete_args` **(Many-Argument Workhorses)** (Impact: 114.0)
  * `check_response` **(Many-Argument Workhorses)** (Impact: 63.8)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 56.2)
  * `_run` **(Many-Argument Workhorses)** (Impact: 54.1)
  * `_parse_headerfile` **(Many-Argument Workhorses)** (Impact: 38.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 230 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 744
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 243`, `args: 88`, `func_start: 88`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 9`, `state_mutation: 284`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 52`, `api: 75`, `concurrency: 1`, `import: 16`
* *Defense:* `safety: 48`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .env, datetime, functools, json, logging, os, psutil, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `lib/url.c` -> Churn: **98.45%** | Cog Load: 75.4379% | Debt: 12.9765%
- `lib/vtls/openssl.c` -> Churn: **96.79%** | Cog Load: 78.213% | Debt: 10.0196%
- `lib/multi.c` -> Churn: **95.91%** | Cog Load: 76.605% | Debt: 27.6927%
- `lib/ftp.c` -> Churn: **95.01%** | Cog Load: 74.0227% | Debt: 7.9247%
- `lib/http.c` -> Churn: **92.04%** | Cog Load: 81.8902% | Debt: 11.9856%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/servers.pm` -> **Viktor Szakats** (83.3% isolated ownership) | Magnitude: 3064.86
- `tests/server/sws.c` -> **Viktor Szakats** (84.6% isolated ownership) | Magnitude: 2440.86
- `tests/libtest/lib557.c` -> **Viktor Szakats** (100.0% isolated ownership) | Magnitude: 2405.2
- `lib/mime.c` -> **Viktor Szakats** (87.0% isolated ownership) | Magnitude: 2199.88
- `scripts/managen` -> **Viktor Szakats** (100.0% isolated ownership) | Magnitude: 1864.54

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/doh.h` -> **Severity: 0.001** (Bridge: 0.0002 * Flux: 9.9229%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/curl_setup.h` -> **Severity: 14.701** (Embedded: 0.3113 * Error Risk: 47.2281%)
- `lib/setup-vms.h` -> **Severity: 12.423** (Embedded: 0.1833 * Error Risk: 67.7854%)
- `include/curl/curl.h` -> **Severity: 8.685** (Embedded: 0.189 * Error Risk: 45.9558%)
- `tests/libtest/unitcheck.h` -> **Severity: 5.302** (Embedded: 0.0688 * Error Risk: 77.0591%)
- `lib/ftp.h` -> **Severity: 4.637** (Embedded: 0.0771 * Error Risk: 60.143%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/setup-vms.h` -> **Severity: 854.5** (Blast Radius: 8.545 * Doc Risk: 100.0%)
- `tests/pathhelp.pm` -> **Severity: 523.5** (Blast Radius: 5.235 * Doc Risk: 100.0%)
- `tests/http/testenv/certs.py` -> **Severity: 312.7** (Blast Radius: 3.127 * Doc Risk: 100.0%)
- `tests/http/testenv/env.py` -> **Severity: 307.0** (Blast Radius: 3.07 * Doc Risk: 100.0%)
- `projects/OS400/initscript.sh` -> **Severity: 287.4** (Blast Radius: 2.874 * Doc Risk: 100.0%)

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
