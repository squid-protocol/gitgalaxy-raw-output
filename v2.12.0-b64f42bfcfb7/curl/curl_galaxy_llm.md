# ARCHITECTURAL_BRIEF: curl
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/curl/curl` |
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
- **Scope:** 1105 analyzed artifact(s), 237991 LOC.
- **Load-bearing artifact:** `lib/mprintf.c` -- 411 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `lib/url.c` -- pulls in 63 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/vtls/openssl.c` at magnitude 4669.94 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 1105 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3145 |
| Total LOC | 237991 |
| Volatility Index | 0.019 |
| % Scanned of codebase = | 26.0% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4495 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3316 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 9.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.066 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 20 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 833 | 184566 | 75.4% |
| PERL | 82 | 21954 | 7.4% |
| PYTHON | 47 | 10516 | 4.3% |
| SHELL | 33 | 2445 | 3.0% |
| YAML | 28 | 5783 | 2.5% |
| PLAINTEXT | 28 | 0 | 2.5% |
| M4 | 26 | 12123 | 2.4% |
| MARKDOWN | 20 | 0 | 1.8% |
| MAKEFILE | 2 | 193 | 0.2% |
| DOCKERFILE | 1 | 10 | 0.1% |
| REXX | 1 | 4 | 0.1% |
| BATCH | 1 | 246 | 0.1% |
| JSON | 1 | 111 | 0.1% |
| CPP | 1 | 22 | 0.1% |
| HTML | 1 | 18 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 1105 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 34%, Large Core Modules (3) 15%, Data / Markup / Trivial 11%, Many-Argument Workhorses Files 11%, Compute Cores Files 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1057 | 95.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 48 | 4.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3145*

**Composition by Extension & Reason:**
- `no_extension`: 1897x Unsupported Format (.undeterminable), 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Machine-Generated Source Code Signature: 89 LOC)
- `.md`: 899x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 129x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 391 LOC)
- `.cmake`: 30x Excluded (Unsupported Extension: '.cmake')
- `.am`: 14x Excluded (Unsupported Extension: '.am'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.com`: 19x Excluded (Unsupported Extension: '.com')
- `.txt`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.prm`: 8x Excluded (Unsupported Extension: '.prm')
- `.pl`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 163 LOC)
- `.inc`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sln`: 3x Excluded (Unsupported Extension: '.sln')
- `.words`: 2x Unsupported Format (.words)
- `.toml`: 1x Unsupported Format (.toml), 1x Excluded (Unsupported Extension: '.toml')
- `.rc`: 1x Excluded (Unsupported Extension: '.rc'), 1x Unsupported Format (.rc)
- `.vcxproj`: 2x Excluded (Unsupported Extension: '.vcxproj')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.5 | 25.2 | 15.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.1 | 44.8 | 56.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.5 | 8.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 14.4 | 2.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 92.2 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.1 | 0.4 | 0.3 | 1.1 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 98.5 | 21.7 | 14.8 | 5.6 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 51.5 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2718 | 375 | 6 | `lib/vquic/curl_ngtcp2.c` |
| cleanup | 447 | 103 | 0 | `tests/runtests.pl` |
| guards | 14487 | 935 | 36 | `lib/vtls/openssl.c` |
| danger | 1878 | 292 | 4 | `tests/ech_tests.sh` |
| concurrency | 178 | 65 | 0 | `tests/http/conftest.py` |
| connectivity | 5459 | 665 | 13 | `configure.ac` |
| io | 2287 | 226 | 4 | `tests/ech_tests.sh` |
| crypto | 9 | 1 | 0 | `tests/http/testenv/certs.py` |
| ipc | 537 | 130 | 1 | `tests/server/rtspd.c` |
| time | 405 | 90 | 0 | `tests/runtests.pl` |
| serialization | 2 | 1 | 0 | `.github/scripts/shellcheck-ci.sh` |
| regex | 1769 | 110 | 0 | `tests/runtests.pl` |
| events | 1586 | 133 | 1 | `m4/curl-functions.m4` |
| tests | 1060 | 46 | 0 | `tests/http/test_02_download.py` |
| docs | 1544 | 864 | 2 | `lib/cfilters.h` |
| debt | 1724 | 234 | 2 | `tests/ech_tests.sh` |
| mutation | 58569 | 793 | 138 | `tests/libtest/lib557.c` |
| dead_code | 1906 | 615 | 4 | `lib/cfilters.c` |
| credential | 133 | 22 | 0 | `scripts/mk-ca-bundle.pl` |
| threat | 154 | 20 | 0 | `tests/unit/unit1658.c` |
| ml_ai | 195 | 55 | 0 | `tests/runtests.pl` |
| ui | 9 | 4 | 0 | `scripts/managen` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **3.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/ech_tests.sh` (Hits: 128)
- `scripts/wcurl` (Hits: 68)
- `.github/workflows/distcheck.yml` (Hits: 58)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **mprintf.c** (`lib/mprintf.c`) — 411 inbound connections
2. **easy.c** (`lib/easy.c`) — 308 inbound connections
3. **curl_setup.h** (`lib/curl_setup.h`) — 298 inbound connections
4. **setopt.c** (`lib/setopt.c`) — 259 inbound connections
5. **first.h** (`tests/libtest/first.h`) — 251 inbound connections

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
- `ossl_connect_step2` **(Many-Argument Workhorses)** (@ `lib/vtls/openssl.c`) -> Impact: **509.9** | LOC: 1400
  * *Intent:* #endif
- `single` **(Many-Argument Workhorses)** (@ `scripts/managen`) -> Impact: **507.8** | LOC: 406
- `opt_string` **(Many-Argument Workhorses)** (@ `src/tool_getparam.c`) -> Impact: **416.8** | LOC: 536
  * *Intent:* /* opt_string handles string options */
- `startservers` **(Compute Cores)** (@ `tests/servers.pm`) -> Impact: **403.5** | LOC: 660
  * *Intent:* ####################################################################### # startservers() starts all the named servers # # 0 for success # 1 for an err...
- `setopt_cptr` **(Many-Argument Workhorses)** (@ `lib/setopt.c`) -> Impact: **368.8** | LOC: 695
  * *Intent:* #endif
- `parsefmt` **(Many-Argument Workhorses)** (@ `lib/mprintf.c`) -> Impact: **367.9** | LOC: 426
  * *Intent:* #define PFMT_OK 0 #define PFMT_DOLLAR 1 /* bad dollar for main param */ #define PFMT_DOLLARWIDTH 2 /* bad dollar use for width */ #define PFMT_DOLLARP...
- `opt_bool` **(Many-Argument Workhorses)** (@ `src/tool_getparam.c`) -> Impact: **325.2** | LOC: 385
  * *Intent:* /* opt_bool is the function that handles boolean options */
- `single` **(Compute Cores)** (@ `scripts/cd2nroff`) -> Impact: **319.9** | LOC: 374

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib` | 265 | 82904.56 | 30.69% | 15.81% |
| `lib/vtls` | 31 | 19152.56 | 34.09% | 9.11% |
| `tests` | 56 | 18715.64 | 32.67% | 0.0% |
| `src` | 91 | 18189.3 | 27.92% | 15.0% |
| `tests/libtest` | 262 | 16280.62 | 18.2% | 0.0% |
| `tests/server` | 14 | 9333.1 | 27.19% | 0.0% |
| `tests/http` | 32 | 7055.76 | 29.15% | 0.0% |
| `scripts` | 37 | 5717.56 | 54.37% | 7.57% |
| `lib/vssh` | 5 | 5443.02 | 40.82% | 7.68% |
| `tests/http/testenv` | 13 | 4841.28 | 33.26% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lib/curlx/warnless.c` -> **99.516%** Exposure
- `lib/uint-bset.c` -> **99.1865%** Exposure
- `lib/uint-table.c` -> **99.0893%** Exposure
- `lib/curlx/timeval.c` -> **98.5748%** Exposure
- `lib/bufref.c` -> **98.4733%** Exposure
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
- **Binary Anomalies (X-Ray):** `10` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4122` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/vtls/openssl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.964)
- **Top Global Matches:** file_cluster_6: 8.964, file_cluster_8: 10.123, file_cluster_4: 16.509
- **Magnitude:** 4669.94 | **LOC:** 5520 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 70.9%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **43**; blast radius 0.349; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (96.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.9%)
- **Documentation Coverage:** 99.5595% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ossl_connect_step2` **(Many-Argument Workhorses)** (Impact: 509.9)
    * *Intent:* #endif
  * `Curl_ossl_ctx_init` **(Many-Argument Workhorses)** (Impact: 180.7)
  * `client_cert` **(Many-Argument Workhorses)** (Impact: 157.2)
  * `ossl_verifyhost` **(Many-Argument Workhorses)** (Impact: 112.6)
    * *Intent:* */
  * `ossl_init_ech` **(Many-Argument Workhorses)** (Impact: 87.1)
    * *Intent:* #ifdef HAVE_SSL_SET1_ECH_CONFIG_LIST
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 528 instances
* *State Mutation (weighted view):* 1612
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 954`, `structural_boundaries: 759`, `args: 236`, `func_start: 95`, `class_start: 138`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 556`, `dead_code: 1`, `fragile_debt: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 18`, `import: 43`
* *Defense:* `safety: 51`, `doc: 2`, `immutability_locks: 138`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.349
  * `Choke Point (Betweenness):` 0.001354 | `Ripple Effect (Closeness):` 0.090082
  * `Imports (Out-Degree: 52):` connect.h, curl_setup.h, curl_trc.h, base64.h, inet_pton.h, strcopy.h, strdup.h, strerr.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/http.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.163)
- **Top Global Matches:** file_cluster_8: 6.163, file_cluster_6: 12.345, file_cluster_4: 20.994
- **Magnitude:** 4652.78 | **LOC:** 5020 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 47.3%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **45**; blast radius 0.58; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (92.0%), Complexity Load (formerly Cognitive Load) (81.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.3146% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `http_on_response` **(Many-Argument Workhorses)** (Impact: 210.2)
  * `Curl_http_follow` **(Many-Argument Workhorses)** (Impact: 148.2)
  * `http_add_hd` **(Many-Argument Workhorses)** (Impact: 142.4)
  * `http_rw_hd` **(Many-Argument Workhorses)** (Impact: 119.6)
  * `Curl_add_custom_headers` **(Many-Argument Workhorses)** (Impact: 111.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 604 instances
* *State Mutation (weighted view):* 1820
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1128`, `structural_boundaries: 642`, `args: 146`, `func_start: 96`, `class_start: 113`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 612`, `dead_code: 1`, `fragile_debt: 4`, `unreferenced_by_name: 6`
* *Architecture:* `api: 34`, `import: 45`
* *Defense:* `safety: 62`, `doc: 5`, `immutability_locks: 110`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.58
  * `Choke Point (Betweenness):` 0.011648 | `Ripple Effect (Closeness):` 0.131909
  * `Imports (Out-Degree: 84):` altsvc.h, inet.h, bufref.h, cfilters.h, connect.h, content_encoding.h, cookie.h, curl_setup.h...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `tests/ftpserver.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.307)
- **Top Global Matches:** file_cluster_4: 8.307, file_cluster_6: 8.378, file_cluster_15: 15.46
- **Magnitude:** 4074.24 | **LOC:** 3374 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.325; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (65.9%), Complexity Load (formerly Cognitive Load) (44.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.4%), Connectivity (formerly Api Exposure) (10.8%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.325
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Digest::MD5, File::Basename, IPC::Open2, NODATACONN, NODATACONN150, NODATACONN421, NODATACONN425, PASVBADIP...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/ftp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.165)
- **Top Global Matches:** file_cluster_6: 7.165, file_cluster_8: 10.522, file_cluster_4: 14.764
- **Magnitude:** 3740.22 | **LOC:** 4500 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 60.8%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **36**; blast radius 0.406; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (95.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.5%)
- **Documentation Coverage:** 86.4583% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ftp_pp_statemachine` **(Many-Argument Workhorses)** (Impact: 175.3)
  * `ftp_done` **(Many-Argument Workhorses)** (Impact: 169.9)
    * *Intent:* /*********************************************************************** * * ftp_done() * * The DONE...
  * `ftp_state_pasv_resp` **(Many-Argument Workhorses)** (Impact: 93.5)
  * `ftp_state_quote` **(Many-Argument Workhorses)** (Impact: 89.1)
  * `ftp_port_parse_string` **(Many-Argument Workhorses)** (Impact: 88.5)
    * *Intent:* /* * Parse the CURLOPT_FTPPORT string * "(ipv4|ipv6|domain|interface)?(:port(-range)?)?" * and extra...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 484 instances
* *State Mutation (weighted view):* 1479
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 867`, `structural_boundaries: 669`, `args: 103`, `func_start: 83`, `class_start: 177`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 511`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 6`, `import: 36`
* *Defense:* `safety: 33`, `doc: 13`, `immutability_locks: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.406
  * `Choke Point (Betweenness):` 0.001745 | `Ripple Effect (Closeness):` 0.127695
  * `Imports (Out-Degree: 64):` inet.h, cf-socket.h, cfilters.h, connect.h, curl_addrinfo.h, curl_ctype.h, curl_range.h, curl_setup.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/tool_getparam.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.915)
- **Top Global Matches:** file_cluster_8: 6.915, file_cluster_6: 17.836, file_cluster_3: 19.227
- **Magnitude:** 3732.46 | **LOC:** 3155 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 65.2%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **15**; blast radius 0.491; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.9%), Complexity Load (formerly Cognitive Load) (77.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `opt_string` **(Many-Argument Workhorses)** (Impact: 416.8)
    * *Intent:* /* opt_string handles string options */
  * `opt_bool` **(Many-Argument Workhorses)** (Impact: 325.2)
    * *Intent:* /* opt_bool is the function that handles boolean options */
  * `getparameter` **(Many-Argument Workhorses)** (Impact: 138.0)
    * *Intent:* /* the longest command line option, excluding the leading -- */ #define MAX_OPTION_LEN 26
  * `opt_file` **(Many-Argument Workhorses)** (Impact: 99.9)
    * *Intent:* /* opt_file handles file options */
  * `parse_args` **(Compute Cores)** (Impact: 62.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 624 instances
* *State Mutation (weighted view):* 1875
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 822`, `structural_boundaries: 523`, `args: 53`, `func_start: 44`, `class_start: 19`
* *Risk/State:* `state_mutation: 627`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 9`, `import: 15`
* *Defense:* `safety: 22`, `doc: 1`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.491
  * `Choke Point (Betweenness):` 0.000748 | `Ripple Effect (Closeness):` 0.005758
  * `Imports (Out-Degree: 34):` tool_cb_prg.h, tool_cfgable.h, tool_filetime.h, tool_formparse.h, tool_getparam.h, tool_help.h, tool_helpers.h, tool_libinfo.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `lib/multi.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.765)
- **Top Global Matches:** file_cluster_6: 6.765, file_cluster_4: 7.524, file_cluster_16: 15.087
- **Magnitude:** 3187.68 | **LOC:** 4169 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 39.6%
- **Blast Radius:** changing it is visible to **98** in-repo importer(s); it depends on **25**; blast radius 3.167; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (95.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `multi_runsingle` **(Many-Argument Workhorses)** (Impact: 174.1)
  * `curl_multi_setopt` **(Many-Argument Workhorses)** (Impact: 94.2)
    * *Intent:* #undef curl_multi_setopt
  * `multi_winsock_select` **(Many-Argument Workhorses)** (Impact: 89.3)
  * `multi_wait` **(Many-Argument Workhorses)** (Impact: 75.2)
    * *Intent:* #endif /* !USE_WINSOCK */ #define NUM_POLLS_ON_STACK 10
  * `Curl_multi_pollset` **(Many-Argument Workhorses)** (Impact: 73.3)
    * *Intent:* /* Initializes `poll_set` with the current socket poll actions needed * for transfer `data`. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 405 instances
* *State Mutation (weighted view):* 1248
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 737`, `structural_boundaries: 619`, `args: 131`, `func_start: 104`, `class_start: 141`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 438`, `fragile_debt: 1`, `unreferenced_by_name: 29`
* *Architecture:* `api: 50`, `import: 25`
* *Defense:* `safety: 13`, `doc: 1`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.167
  * `Choke Point (Betweenness):` 0.015393 | `Ripple Effect (Closeness):` 0.206583
  * `Imports (Out-Degree: 61):` bufref.h, cfilters.h, conncache.h, connect.h, curl_setup.h, curl_share.h, curl_trc.h, wait.h...
  * `Imported By (In-Degree: 98):` (Excluded from Brief to save tokens)

### `tests/servers.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.631)
- **Top Global Matches:** file_cluster_3: 11.631, file_cluster_8: 13.894, file_cluster_6: 26.341
- **Magnitude:** 3064.86 | **LOC:** 3220 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **16**; blast radius 0.528; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (71.4%), Connectivity (formerly Api Exposure) (62.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.1%), Complexity Load (formerly Cognitive Load) (40.6%)
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
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 382`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 22`, `api: 50`, `concurrency: 2`, `import: 21`
* *Defense:* `safety: 2`, `sync_locks: 3`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.528
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.002712
  * `Imports (Out-Degree: 5):` File::Temp, IO::Socket, POSIX, Time::HiRes, base, globalconfig, gnutls, pathhelp...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib/url.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.577)
- **Top Global Matches:** file_cluster_6: 6.577, file_cluster_8: 11.401, file_cluster_4: 13.812
- **Magnitude:** 2989.78 | **LOC:** 3788 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 45.8%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **63**; blast radius 1.266; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (98.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.5%)
- **Documentation Coverage:** 87.7698% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_proxy` **(Many-Argument Workhorses)** (Impact: 126.5)
    * *Intent:* #endif /* CURL_DISABLE_HTTP */ /* * If this is supposed to use a proxy, we need to figure out the pr...
  * `parseurlandfillconn` **(Many-Argument Workhorses)** (Impact: 121.7)
    * *Intent:* #else #define zonefrom_url(a, b, c) Curl_nop_stmt #endif /* * Parse URL and fill in the relevant mem...
  * `parse_connect_to_slist` **(Many-Argument Workhorses)** (Impact: 92.0)
    * *Intent:* /* * Processes all strings in the "connect to" slist, and uses the "connect * to host" and "connect ...
  * `create_conn_helper_init_proxy` **(Many-Argument Workhorses)** (Impact: 81.2)
    * *Intent:* /* create_conn helper to parse and init proxy values. to be called after Unix socket init but before...
  * `override_login` **(Many-Argument Workhorses)** (Impact: 73.6)
    * *Intent:* #endif /* * Override the login details from the URL with that in the CURLOPT_USERPWD * option or a ....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 416 instances
* *State Mutation (weighted view):* 1361
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 700`, `structural_boundaries: 453`, `args: 102`, `func_start: 69`, `class_start: 79`
* *Risk/State:* `state_mutation: 529`, `fragile_debt: 1`, `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 19`, `import: 63`
* *Defense:* `safety: 15`, `doc: 22`, `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.266
  * `Choke Point (Betweenness):` 0.013676 | `Ripple Effect (Closeness):` 0.188255
  * `Imports (Out-Degree: 95):` Iphlpapi.h, altsvc.h, inet.h, bufref.h, cfilters.h, conncache.h, connect.h, cookie.h...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `lib/vssh/libssh2.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.502)
- **Top Global Matches:** file_cluster_4: 7.502, file_cluster_6: 7.61, file_cluster_16: 14.354
- **Magnitude:** 2743.92 | **LOC:** 3867 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 71.9%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **23**; blast radius 0.333; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.0%), Guard Balance (formerly Safety Score) (65.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ssh_statemachine` **(Many-Argument Workhorses)** (Impact: 308.6)
    * *Intent:* /* * ssh_statemachine() runs the SSH state machine as far as it can without * blocking and without r...
  * `sftp_upload_init` **(Many-Argument Workhorses)** (Impact: 87.3)
  * `sftp_quote` **(Many-Argument Workhorses)** (Impact: 84.0)
  * `sftp_quote_stat` **(Many-Argument Workhorses)** (Impact: 63.6)
  * `ssh_knownhost` **(Many-Argument Workhorses)** (Impact: 63.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 321 instances
* *State Mutation (weighted view):* 993
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 688`, `structural_boundaries: 690`, `args: 85`, `func_start: 86`, `class_start: 138`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 351`
* *Architecture:* `api: 6`, `import: 23`
* *Defense:* `safety: 31`, `doc: 1`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.333
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000904
  * `Imports (Out-Degree: 39):` inet.h, cfilters.h, connect.h, curl_setup.h, curl_trc.h, base64.h, fopen.h, strparse.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/runtests.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.99)
- **Top Global Matches:** file_cluster_6: 6.99, file_cluster_4: 10.041, file_cluster_8: 16.511
- **Magnitude:** 2703.34 | **LOC:** 3372 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 0.325; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (76.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.7%), Complexity Load (formerly Cognitive Load) (48.0%), Connectivity (formerly Api Exposure) (9.1%)
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
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 18`, `state_mutation: 484`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `io: 27`, `api: 39`, `concurrency: 1`, `import: 33`
* *Defense:* `safety: 4`, `sync_locks: 2`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.325
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Digest::MD5, File::Basename, I18N::Langinfo, List::Util, POSIX, Time::HiRes, appveyor, azure...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/setopt.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.184)
- **Top Global Matches:** file_cluster_8: 6.184, file_cluster_6: 16.366, file_cluster_3: 20.746
- **Magnitude:** 2696.92 | **LOC:** 2933 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 40.6%
- **Blast Radius:** changing it is visible to **259** in-repo importer(s); it depends on **20**; blast radius 12.994; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.1%), Guard Balance (formerly Safety Score) (74.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setopt_cptr` **(Many-Argument Workhorses)** (Impact: 368.8)
    * *Intent:* #endif
  * `setopt_long_bool` **(Many-Argument Workhorses)** (Impact: 172.3)
    * *Intent:* #endif
  * `setopt_long_net` **(Many-Argument Workhorses)** (Impact: 118.4)
  * `setopt_long_proto` **(Many-Argument Workhorses)** (Impact: 91.0)
  * `setopt_func` **(Many-Argument Workhorses)** (Impact: 79.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 374 instances
* *State Mutation (weighted view):* 1134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 665`, `structural_boundaries: 545`, `args: 65`, `func_start: 34`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 386`
* *Architecture:* `api: 5`, `import: 20`
* *Defense:* `safety: 6`, `doc: 1`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.994
  * `Choke Point (Betweenness):` 0.016298 | `Ripple Effect (Closeness):` 0.2414
  * `Imports (Out-Degree: 37):` altsvc.h, bufref.h, content_encoding.h, curl_setup.h, curl_share.h, curl_trc.h, strdup.h, escape.h...
  * `Imported By (In-Degree: 259):` (Excluded from Brief to save tokens)

### `lib/vssh/libssh.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.315)
- **Top Global Matches:** file_cluster_4: 7.315, file_cluster_6: 7.458, file_cluster_16: 14.261
- **Magnitude:** 2405.72 | **LOC:** 3015 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 61.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.325; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (85.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `myssh_statemach_act` **(Many-Argument Workhorses)** (Impact: 288.7)
    * *Intent:* /* * ssh_statemach_act() runs the SSH state machine as far as it can without * blocking and without ...
  * `myssh_is_known` **(Many-Argument Workhorses)** (Impact: 97.7)
    * *Intent:* /* Multiple options: * 1. data->set.str[STRING_SSH_HOST_PUBLIC_KEY_MD5] is set with an MD5 * hash (9...
  * `myssh_in_SFTP_QUOTE` **(Many-Argument Workhorses)** (Impact: 95.7)
  * `myssh_in_UPLOAD_INIT` **(Many-Argument Workhorses)** (Impact: 71.4)
  * `myssh_connect` **(Many-Argument Workhorses)** (Impact: 43.8)
    * *Intent:* /* * Curl_ssh_connect() gets called from Curl_protocol_connect() to allow us to * do protocol-specif...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 337 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1044
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 538`, `structural_boundaries: 515`, `args: 72`, `func_start: 70`, `class_start: 98`
* *Risk/State:* `state_mutation: 370`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 23`
* *Defense:* `safety: 18`, `doc: 1`, `immutability_locks: 17`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.325
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` inet.h, cfilters.h, connect.h, curl_setup.h, curl_trc.h, strparse.h, fcntl.h, hostip.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server/sws.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.41)
- **Top Global Matches:** file_cluster_3: 9.41, file_cluster_8: 30.098, file_cluster_1: 40.272
- **Magnitude:** 2399.26 | **LOC:** 2484 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 84.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.325; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (76.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.3%), Complexity Load (formerly Cognitive Load) (40.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `http_connect` **(Many-Argument Workhorses)** (Impact: 296.2)
    * *Intent:* * This function needs to connect to the server, and then pass data between * the client and the serv...
  * `test_sws` **(Many-Argument Workhorses)** (Impact: 226.9)
  * `sws_ProcessRequest` **(Many-Argument Workhorses)** (Impact: 201.5)
  * `sws_send_doc` **(Many-Argument Workhorses)** (Impact: 126.4)
    * *Intent:* /* returns -1 on failure */
  * `sws_get_request` **(Many-Argument Workhorses)** (Impact: 72.7)
    * *Intent:* /* returns 1 if the connection should be serviced again immediately, 0 if there is no data waiting, ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 15 instances
* *Amplified Cascading Flux:* 386 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 1199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 571`, `structural_boundaries: 171`, `args: 44`, `func_start: 15`, `class_start: 7`
* *Risk/State:* `state_mutation: 427`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 20`, `api: 1`, `import: 2`
* *Defense:* `safety: 33`, `doc: 1`, `immutability_locks: 39`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.325
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` first.h, tcp.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/http2.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.199)
- **Top Global Matches:** file_cluster_4: 6.199, file_cluster_6: 8.431, file_cluster_16: 12.545
- **Magnitude:** 2376.32 | **LOC:** 3028 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 61.3%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **22**; blast radius 0.505; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `on_header` **(Many-Argument Workhorses)** (Impact: 113.7)
    * *Intent:* /* frame->hd.type is either NGHTTP2_HEADERS or NGHTTP2_PUSH_PROMISE */
  * `h2_submit` **(Many-Argument Workhorses)** (Impact: 83.0)
  * `on_stream_frame` **(Many-Argument Workhorses)** (Impact: 69.7)
  * `cf_h2_send` **(Many-Argument Workhorses)** (Impact: 54.7)
  * `h2_progress_ingress` **(Many-Argument Workhorses)** (Impact: 51.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 298 instances
* *State Mutation (weighted view):* 934
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 491`, `structural_boundaries: 572`, `args: 94`, `func_start: 82`, `class_start: 176`
* *Risk/State:* `state_mutation: 338`, `unreferenced_by_name: 7`
* *Architecture:* `api: 19`, `import: 22`
* *Defense:* `safety: 59`, `doc: 2`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.505
  * `Choke Point (Betweenness):` 0.00285 | `Ripple Effect (Closeness):` 0.139284
  * `Imports (Out-Degree: 48):` bufq.h, bufref.h, cfilters.h, connect.h, curl_setup.h, curl_trc.h, base64.h, dynbuf.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `tests/libtest/lib557.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.329)
- **Top Global Matches:** file_cluster_9: 7.329, file_cluster_16: 7.656, file_cluster_2: 8.669
- **Magnitude:** 2336.2 | **LOC:** 1560 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.325; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (97.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (33.3%), Complexity Load (formerly Cognitive Load) (27.6%), Dead Code Surface (formerly Dead Code) (5.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_unsigned_int_formatting` **(I/O & Config Routines)** (Impact: 10.5)
  * `test_signed_int_formatting` **(I/O & Config Routines)** (Impact: 10.5)
  * `test_unsigned_long_formatting` **(I/O & Config Routines)** (Impact: 10.5)
  * `test_signed_long_formatting` **(I/O & Config Routines)** (Impact: 10.5)
  * `test_curl_off_t_formatting` **(I/O & Config Routines)** (Impact: 10.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 119 instances
* *State Mutation (weighted view):* 2177
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 65`, `args: 38`, `func_start: 17`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1939`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.325
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` first.h, locale.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tool_operate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.022)
- **Top Global Matches:** file_cluster_8: 6.022, file_cluster_6: 15.121, file_cluster_3: 22.089
- **Magnitude:** 2238.04 | **LOC:** 2414 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 53.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **39**; blast radius 0.358; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (82.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `retrycheck` **(Many-Argument Workhorses)** (Impact: 185.3)
  * `create_single` **(Many-Argument Workhorses)** (Impact: 170.1)
    * *Intent:* /* create a transfer */
  * `operate` **(Many-Argument Workhorses)** (Impact: 86.6)
  * `setup_outfile` **(Many-Argument Workhorses)** (Impact: 73.2)
  * `post_per_transfer` **(Many-Argument Workhorses)** (Impact: 57.5)
    * *Intent:* /* * Call this after a transfer has completed. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 300 instances
* *State Mutation (weighted view):* 921
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 562`, `structural_boundaries: 308`, `args: 69`, `func_start: 45`, `class_start: 63`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 321`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 6`, `import: 39`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.358
  * `Choke Point (Betweenness):` 0.000395 | `Ripple Effect (Closeness):` 0.001808
  * `Imports (Out-Degree: 73):` config2setopts.h, nonblock.h, fabdef.h, locale.h, in.h, dos.h, select.h, tool_cb_hdr.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/mime.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.474)
- **Top Global Matches:** file_cluster_4: 5.474, file_cluster_6: 9.486, file_cluster_16: 11.847
- **Magnitude:** 2199.88 | **LOC:** 2229 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 87.0%
- **Blast Radius:** changing it is visible to **27** in-repo importer(s); it depends on **15**; blast radius 1.658; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.4%), Guard Balance (formerly Safety Score) (73.2%)
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
* *Structure:* `branch: 434`, `structural_boundaries: 362`, `args: 89`, `func_start: 83`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 339`, `unreferenced_by_name: 3`
* *Architecture:* `io: 2`, `api: 36`, `import: 15`
* *Defense:* `safety: 73`, `doc: 1`, `immutability_locks: 56`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.658
  * `Choke Point (Betweenness):` 0.002663 | `Ripple Effect (Closeness):` 0.173613
  * `Imports (Out-Degree: 28):` curl_setup.h, curl_trc.h, base64.h, basename.h, dynbuf.h, fopen.h, strcopy.h, strdup.h...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `lib/vquic/curl_ngtcp2.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.222)
- **Top Global Matches:** file_cluster_4: 6.222, file_cluster_16: 10.173, file_cluster_6: 10.971
- **Magnitude:** 2171.78 | **LOC:** 2951 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 62.5%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **34**; blast radius 0.342; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.4%)
- **Documentation Coverage:** 98.2456% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `h3_stream_open` **(Many-Argument Workhorses)** (Impact: 67.9)
  * `cf_ngtcp2_query` **(Many-Argument Workhorses)** (Impact: 67.6)
  * `cf_ngtcp2_connect` **(Many-Argument Workhorses)** (Impact: 63.2)
  * `cf_ngtcp2_send` **(Many-Argument Workhorses)** (Impact: 57.6)
  * `cf_progress_egress` **(Many-Argument Workhorses)** (Impact: 53.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 279 instances
* *State Mutation (weighted view):* 879
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 433`, `structural_boundaries: 609`, `args: 116`, `func_start: 74`, `class_start: 218`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 321`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 7`, `import: 34`
* *Defense:* `safety: 46`, `doc: 4`, `immutability_locks: 32`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.004166 | `Ripple Effect (Closeness):` 0.115976
  * `Imports (Out-Degree: 55):` bufref.h, cf-socket.h, cfilters.h, connect.h, curl_setup.h, curl_trc.h, dynbuf.h, fopen.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/urlapi.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.313)
- **Top Global Matches:** file_cluster_8: 6.313, file_cluster_6: 17.155, file_cluster_3: 19.742
- **Magnitude:** 2141.02 | **LOC:** 2001 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **31** in-repo importer(s); it depends on **12**; blast radius 1.276; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.7%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `curl_url_set` **(Many-Argument Workhorses)** (Impact: 166.2)
  * `urlget_url` **(Many-Argument Workhorses)** (Impact: 137.8)
  * `curl_url_get` **(Many-Argument Workhorses)** (Impact: 85.2)
  * `dedotdotify` **(Many-Argument Workhorses)** (Impact: 61.2)
  * `urlget_format` **(Many-Argument Workhorses)** (Impact: 58.9)
    * *Intent:* #endif
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 285 instances
* *State Mutation (weighted view):* 861
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 518`, `structural_boundaries: 266`, `args: 50`, `func_start: 38`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 291`, `unreferenced_by_name: 4`
* *Architecture:* `api: 13`, `import: 12`
* *Defense:* `safety: 53`, `doc: 1`, `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.276
  * `Choke Point (Betweenness):` 0.002007 | `Ripple Effect (Closeness):` 0.139737
  * `Imports (Out-Degree: 26):` curl_memrchr.h, curl_setup.h, inet_ntop.h, inet_pton.h, strdup.h, strparse.h, escape.h, idn.h...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `lib/vtls/schannel.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.629)
- **Top Global Matches:** file_cluster_8: 5.629, file_cluster_6: 12.906, file_cluster_4: 21.666
- **Magnitude:** 2138.06 | **LOC:** 2875 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 69.2%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 0.338; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `schannel_recv` **(Many-Argument Workhorses)** (Impact: 153.6)
  * `get_client_cert` **(Many-Argument Workhorses)** (Impact: 109.0)
  * `schannel_connect_step2` **(Many-Argument Workhorses)** (Impact: 100.0)
  * `schannel_recv_renegotiate` **(Many-Argument Workhorses)** (Impact: 97.1)
    * *Intent:* first to complete the renegotiation. */
  * `schannel_shutdown` **(Many-Argument Workhorses)** (Impact: 69.6)
    * *Intent:* if the SSL connection failed (eg connection made but failed handshake). */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 280 instances
* *State Mutation (weighted view):* 889
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 490`, `structural_boundaries: 329`, `args: 106`, `func_start: 38`, `class_start: 67`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 329`, `unreferenced_by_name: 2`
* *Architecture:* `io: 3`, `api: 6`, `import: 20`
* *Defense:* `safety: 37`, `doc: 2`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 6.5e-05 | `Ripple Effect (Closeness):` 0.000904
  * `Imports (Out-Degree: 39):` connect.h, curl_setup.h, curl_sha256.h, curl_trc.h, fopen.h, multibyte.h, strdup.h, strparse.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/vtls/gtls.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.326)
- **Top Global Matches:** file_cluster_6: 5.326, file_cluster_4: 10.284, file_cluster_8: 14.655
- **Magnitude:** 1966.76 | **LOC:** 2315 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **22**; blast radius 0.349; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.4%)
- **Documentation Coverage:** 99.0991% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Curl_gtls_verifyserver` **(Many-Argument Workhorses)** (Impact: 214.2)
    * *Intent:* #endif /* USE_APPLE_SECTRUST */
  * `gtls_client_init` **(Many-Argument Workhorses)** (Impact: 110.2)
  * `Curl_gtls_ctx_init` **(Many-Argument Workhorses)** (Impact: 97.3)
    * *Intent:* #endif
  * `gtls_populate_creds` **(Many-Argument Workhorses)** (Impact: 65.7)
  * `gtls_shutdown` **(Many-Argument Workhorses)** (Impact: 50.6)
    * *Intent:* /* * This function is called to shut down the SSL layer but keep the * socket open (CCC - Clear Comm...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 250 instances
* *State Mutation (weighted view):* 769
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 414`, `structural_boundaries: 368`, `args: 70`, `func_start: 53`, `class_start: 105`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 269`
* *Architecture:* `io: 3`, `api: 12`, `import: 22`
* *Defense:* `safety: 38`, `doc: 2`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.349
  * `Choke Point (Betweenness):` 0.000789 | `Ripple Effect (Closeness):` 0.09013
  * `Imports (Out-Degree: 32):` connect.h, curl_setup.h, curl_trc.h, fopen.h, strdup.h, abstract.h, crypto.h, gnutls.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scripts/managen` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.535)
- **Top Global Matches:** file_cluster_6: 8.535, file_cluster_8: 10.724, file_cluster_4: 15.78
- **Magnitude:** 1864.54 | **LOC:** 1384 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.325; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.5%), Guard Balance (formerly Safety Score) (77.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.8%)
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
* *Risk/State:* `high_risk_execution: 12`, `state_mutation: 218`, `dead_code: 1`
* *Architecture:* `io: 13`, `api: 27`, `import: 9`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.325
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` POSIX, extra, in, of, proper, several, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/vtls/wolfssl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.823)
- **Top Global Matches:** file_cluster_6: 7.823, file_cluster_8: 10.331, file_cluster_4: 15.415
- **Magnitude:** 1840.7 | **LOC:** 2293 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 64.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **19**; blast radius 0.626; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (85.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Curl_wssl_ctx_init` **(Many-Argument Workhorses)** (Impact: 271.4)
    * *Intent:* #define QUIC_GROUPS "P-256:P-384:P-521"
  * `wssl_handshake` **(Many-Argument Workhorses)** (Impact: 80.9)
    * *Intent:* #endif /* WOLFSSL_EARLY_DATA */
  * `wssl_populate_x509_store` **(Many-Argument Workhorses)** (Impact: 53.8)
  * `wssl_setup_session` **(Many-Argument Workhorses)** (Impact: 53.6)
  * `wssl_connect` **(Many-Argument Workhorses)** (Impact: 53.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 210 instances
* *State Mutation (weighted view):* 646
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 424`, `structural_boundaries: 350`, `args: 69`, `func_start: 45`, `class_start: 92`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 226`, `fragile_debt: 1`
* *Architecture:* `api: 8`, `import: 19`
* *Defense:* `safety: 26`, `doc: 1`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.626
  * `Choke Point (Betweenness):` 0.000703 | `Ripple Effect (Closeness):` 0.090414
  * `Imports (Out-Degree: 33):` connect.h, curl_setup.h, curl_trc.h, base64.h, strcopy.h, strdup.h, httpsrr.h, progress.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib/imap.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.976)
- **Top Global Matches:** file_cluster_6: 5.976, file_cluster_4: 11.986, file_cluster_8: 13.35
- **Magnitude:** 1783.52 | **LOC:** 2327 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 51.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.325; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.2%), Guard Balance (formerly Safety Score) (68.1%)
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
* *Amplified Cascading Flux:* 213 instances
* *State Mutation (weighted view):* 645
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 452`, `structural_boundaries: 354`, `args: 59`, `func_start: 54`, `class_start: 82`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 219`
* *Architecture:* `api: 4`, `import: 27`
* *Defense:* `safety: 27`, `doc: 31`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.325
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 43):` inet.h, bufref.h, cfilters.h, connect.h, curl_sasl.h, curl_setup.h, curl_trc.h, dynbuf.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/http/testenv/curl.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.991)
- **Top Global Matches:** file_cluster_5: 8.991, file_cluster_4: 10.078, file_cluster_12: 10.236
- **Magnitude:** 1708.64 | **LOC:** 1309 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **36** in-repo importer(s); it depends on **16**; blast radius 4.17; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (47.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.8%), Connectivity (formerly Api Exposure) (39.2%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.032574
  * `Imports (Out-Degree: 1):` .env, datetime, functools, json, logging, os, psutil, re...
  * `Imported By (In-Degree: 36):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/http/testenv/client.py` (PYTHON) | Magnitude: 115.82 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 35, state_mutation: 30, core_var_decl: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/libtest/lib558.c` (C) | Magnitude: 15.04 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 18, core_var_decl: 4, design_snake_case: 4, structural_boundaries: 3
- `tests/libtest/lib1308.c` (C) | Magnitude: 17.1 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 47, pointers: 19, core_var_decl: 11, design_snake_case: 11
- `src/tool_vms.c` (C) | Magnitude: 70.4 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 63, macros: 16, structural_boundaries: 14, state_mutation: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/http/test_40_socks.py` (PYTHON) | Magnitude: 59.64 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 20, state_mutation: 20, core_var_decl: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/libtest/lib1500.c` (C) | Magnitude: 26.04 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 37, pointers: 9, core_var_decl: 7, design_snake_case: 7
- `scripts/singleuse.pl` (PERL) | Magnitude: 45.64 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 175, branch: 29, structural_boundaries: 19, globals: 15
- `tests/libtest/lib560.c` (C) | Magnitude: 8.1 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 35, pointers: 16, structural_boundaries: 2, state_mutation: 2
- `.github/scripts/randcurl.pl` (PERL) | Magnitude: 151.54 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 133, structural_boundaries: 57, branch: 38, state_mutation: 32
- `tests/http/test_08_caddy.py` (PYTHON) | Magnitude: 187.46 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 151, core_var_decl: 58, design_snake_case: 58, state_mutation: 52

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/libtest/lib1526.c` (C) | Magnitude: 39.6 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 50, pointers: 12, core_var_decl: 9, design_snake_case: 9
- `tests/unit/unit3214.c` (C) | Magnitude: 13.56 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 18, macros: 15, pointers: 4
- `tests/libtest/lib1515.c` (C) | Magnitude: 46.72 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 75, pointers: 29, state_mutation: 10, branch: 9
- `tests/libtest/lib1594.c` (C) | Magnitude: 12.26 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 18, pointers: 4, core_var_decl: 3, design_snake_case: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/libtest/lib1545.c` (C) | Magnitude: 3.22 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 16, pointers: 6, structural_boundaries: 5, args: 2
- `tests/http/testenv/__init__.py` (PYTHON) | Magnitude: 15.28 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 21, import: 11, test: 2, indent_spaces: 1
- `lib/vauth/cram.c` (C) | Magnitude: 14.36 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 24, pointers: 7, structural_boundaries: 6, import: 4
- `src/toolx/tool_time.c` (C) | Magnitude: 20.38 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 13, macros: 9, pointers: 8, structural_boundaries: 7
- `tests/cmake/test.c` (C) | Magnitude: 3.42 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, debug_prints: 4, structural_boundaries: 2, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `.github/workflows/label.yml` (YAML) | Magnitude: 16.34 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 2, doc: 2, globals: 2
- `lib/macos.c` (C) | Magnitude: 4.14 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 4, import: 3, structural_boundaries: 2, args: 2
- `tests/libtest/lib3208.c` (C) | Magnitude: 26.56 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 43, pointers: 9, core_var_decl: 7, design_snake_case: 7
- `tests/unit/unit1654.c` (C) | Magnitude: 33.6 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 86, pointers: 24, state_mutation: 21, core_var_decl: 16
- `tests/libtest/lib1906.c` (C) | Magnitude: 25.78 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 39, pointers: 6, core_var_decl: 6, design_snake_case: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/ftpserver.pl` (PERL) | Magnitude: 4074.24 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 2231, branch: 714, structural_boundaries: 544, state_mutation: 282
- `lib/vssh/libssh2.c` (C) | Magnitude: 2743.92 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 2661, pointers: 1113, structural_boundaries: 690, branch: 688
- `lib/vssh/libssh.c` (C) | Magnitude: 2405.72 | Delta: **0.143** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 2069, pointers: 947, branch: 538, structural_boundaries: 515

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `scripts/contrithanks.sh` (SHELL) | Magnitude: 4.47 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: io: 44, structural_boundaries: 35, indent_spaces: 27, regex_execution: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tests/unit/unit3211.c` (C) | Magnitude: 137.72 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 91, pointers: 37, state_mutation: 33, branch: 14

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `lib/url.c` -> Churn: **98.45%** | Cog Load: 74.5127% | Debt: 12.6731%
- `lib/vtls/openssl.c` -> Churn: **96.79%** | Cog Load: 75.9348% | Debt: 9.8679%
- `lib/multi.c` -> Churn: **95.91%** | Cog Load: 76.0365% | Debt: 27.198%
- `lib/ftp.c` -> Churn: **95.01%** | Cog Load: 73.5283% | Debt: 7.8102%
- `lib/http.c` -> Churn: **92.04%** | Cog Load: 80.9537% | Debt: 11.7737%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/servers.pm` -> **Viktor Szakats** (83.3% isolated ownership) | Magnitude: 3064.86
- `tests/server/sws.c` -> **Viktor Szakats** (84.6% isolated ownership) | Magnitude: 2399.26
- `tests/libtest/lib557.c` -> **Viktor Szakats** (100.0% isolated ownership) | Magnitude: 2336.2
- `lib/mime.c` -> **Viktor Szakats** (87.0% isolated ownership) | Magnitude: 2199.88
- `scripts/managen` -> **Viktor Szakats** (100.0% isolated ownership) | Magnitude: 1864.54

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/easy.c` -> **Severity: 5.048** (Bridge: 0.0505 * Flux: 99.9998%)
- `lib/setopt.c` -> **Severity: 1.63** (Bridge: 0.0163 * Flux: 100.0%)
- `lib/multi.c` -> **Severity: 1.539** (Bridge: 0.0154 * Flux: 99.9999%)
- `lib/url.c` -> **Severity: 1.368** (Bridge: 0.0137 * Flux: 100.0%)
- `lib/http.c` -> **Severity: 1.165** (Bridge: 0.0116 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/mprintf.c` -> **Severity: 31.128** (Embedded: 0.3871 * Error Risk: 80.4055%)
- `lib/curl_setup.h` -> **Severity: 20.591** (Embedded: 0.4219 * Error Risk: 48.8006%)
- `lib/memdebug.c` -> **Severity: 18.928** (Embedded: 0.2976 * Error Risk: 63.6107%)
- `lib/setopt.c` -> **Severity: 17.979** (Embedded: 0.2414 * Error Risk: 74.4794%)
- `lib/easy.c` -> **Severity: 17.012** (Embedded: 0.252 * Error Risk: 67.5045%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/mprintf.c` -> **Severity: 2277.0** (Blast Radius: 22.77 * Doc Risk: 100.0%)
- `lib/memdebug.c` -> **Severity: 1354.6** (Blast Radius: 13.546 * Doc Risk: 100.0%)
- `lib/setopt.c` -> **Severity: 1299.4** (Blast Radius: 12.994 * Doc Risk: 100.0%)
- `lib/easy.c` -> **Severity: 1193.948** (Blast Radius: 14.653 * Doc Risk: 81.4815%)
- `lib/setup-vms.h` -> **Severity: 783.5** (Blast Radius: 7.835 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1533 literal sites + 2 sites through wrappers = 1535
- **`memory_alloc`:** 211 literal sites + 28 sites through wrappers = 239

- `CURLX_FREE` (macro, memory_alloc, primitive): 21 call sites in 1 files -- `lib/curlx/fopen.c`
- `CURLX_MALLOC` (macro, memory_alloc, primitive): 6 call sites in 1 files -- `lib/curlx/fopen.c`
- `prefixline` (function, debug_prints, primitive): 2 call sites in 1 files -- `scripts/managen`
- `Curl_formadd_release_local` (function, memory_alloc, primitive): 1 call sites in 1 files -- `projects/OS400/ccsidcurl.c`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 32007 call pairs -- scoped 19.7%, unique 34.8%, ambiguous 0.8%, external 44.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 25160 | 14.7% | 43.8% | 0.2% | 41.3% |
| python | 3476 | 52.8% | 0.0% | 3.2% | 44.1% |
| perl | 1884 | 35.1% | 0.0% | 5.1% | 59.8% |
| m4 | 1107 | 1.6% | 10.4% | 0.0% | 88.0% |
| shell | 373 | 22.5% | 0.0% | 0.0% | 77.5% |
| batch | 4 | 100.0% | 0.0% | 0.0% | 0.0% |
| cpp | 3 | 33.3% | 33.3% | 0.0% | 33.3% |

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
