# ARCHITECTURAL_BRIEF: gnupg
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/gpg/gnupg.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1047 analyzed artifact(s), 301956 LOC.
- **Load-bearing artifact:** `common/i18n.h` -- 164 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `g10/gpg.c` -- pulls in 42 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `dirmngr/dns.c` at magnitude 10367.4 (structural weight, not risk).
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
| Total Artifacts | 1365 |
| Analyzed Artifacts (Scanned) | 1047 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 318 |
| Total LOC | 301956 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 76.7% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5381 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0089 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7367 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 46 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 497 | 288631 | 47.5% |
| PLAINTEXT | 335 | 255 | 32.0% |
| SCHEME | 118 | 6593 | 11.3% |
| SHELL | 35 | 1816 | 3.3% |
| M4 | 33 | 3880 | 3.2% |
| MARKDOWN | 13 | 0 | 1.2% |
| XML | 5 | 0 | 0.5% |
| MAKEFILE | 3 | 582 | 0.3% |
| CSS | 2 | 57 | 0.2% |
| PERL | 2 | 30 | 0.2% |
| HTML | 1 | 46 | 0.1% |
| PHP | 1 | 26 | 0.1% |
| PYTHON | 1 | 17 | 0.1% |
| BATCH | 1 | 23 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `4.349`
> **Composition Archetype:** `Hub-Coupled App` (z +4.35; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 38%, Declarative / Non-Code 23%, Many-Argument Workhorses Files 16%, Large Core Modules (3) 9%, Compute Cores Files 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 699 | 66.8% |
| Unknown | 255 | 24.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 93 | 8.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 318*

**Composition by Extension & Reason:**
- `.png`: 48x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 17x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 72 LOC)
- `.po`: 28x Excluded (Unsupported Extension: '.po')
- `.txt`: 20x Excluded (Binary Format Detected), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 874 LOC)
- `.texi`: 24x Excluded (Unsupported Extension: '.texi')
- `.am`: 22x Excluded (Unsupported Extension: '.am')
- `.rc`: 10x Excluded (Unsupported Extension: '.rc'), 6x Unsupported Format (.rc)
- `.jpg`: 9x Excluded (Explicitly Denied Extension: '.jpg')
- `.m4`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 38 LOC), 1x Excluded (Machine-Generated Source Code Signature: 105 LOC)
- `.c`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 47 LOC)
- `.der`: 5x Excluded (Explicitly Denied Extension: '.der')
- `.ico`: 4x Excluded (Explicitly Denied Extension: '.ico')
- `.patch`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.awk`: 4x Excluded (Unsupported Extension: '.awk')
- `.pdf`: 4x Excluded (Explicitly Denied Extension: '.pdf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 38.2 | 21.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 54.3 | 78.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 24.3 | 11.4 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 29.3 | 2.3 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.3 | 2.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 48.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 36.7 | 0.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.5 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 78.2 | 3.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 58.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 74761 | 500 | 203 | `dirmngr/dns.c` |
| cleanup | 360 | 72 | 0 | `dirmngr/dns.c` |
| guards | 18154 | 519 | 51 | `dirmngr/dns.c` |
| danger | 2269 | 298 | 6 | `autogen.sh` |
| concurrency | 22 | 13 | 0 | `tests/gpgscm/ffi.c` |
| connectivity | 5825 | 510 | 14 | `dirmngr/dns.c` |
| io | 995 | 204 | 2 | `autogen.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 302 | 60 | 0 | `agent/gpg-agent.c` |
| time | 223 | 57 | 0 | `common/gettime.c` |
| serialization | 3 | 1 | 0 | `po/Makefile.in.in` |
| regex | 72 | 17 | 0 | `autogen.sh` |
| events | 6234 | 263 | 16 | `g10/gpg.c` |
| tests | 23 | 12 | 0 | `tests/gpgscm/tests.scm` |
| docs | 184 | 68 | 0 | `tests/gpgscm/init.scm` |
| debt | 2305 | 338 | 5 | `dirmngr/dns.c` |
| mutation | 89487 | 455 | 248 | `scd/app-p15.c` |
| dead_code | 2356 | 384 | 7 | `dirmngr/dns.c` |
| credential | 76 | 11 | 0 | `tools/der-to-pem` |
| threat | 5385 | 295 | 11 | `dirmngr/dns.c` |
| ml_ai | 289 | 62 | 0 | `dirmngr/dns.c` |
| ui | 2 | 2 | 0 | `agent/w32main.c` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `autogen.sh` (Hits: 73)
- `tools/gpg-authcode-sign.sh` (Hits: 51)
- `artwork/icons/index.html` (Hits: 49)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **i18n.h** (`common/i18n.h`) — 164 inbound connections
2. **sysutils.h** (`common/sysutils.h`) — 73 inbound connections
3. **gpg.h** (`g10/gpg.h`) — 68 inbound connections
4. **types.h** (`common/types.h`) — 61 inbound connections
5. **options.h** (`g10/options.h`) — 60 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **gpg.c** (`g10/gpg.c`) — 42 outbound dependencies
2. **dns.c** (`dirmngr/dns.c`) — 35 outbound dependencies
3. **dirmngr.c** (`dirmngr/dirmngr.c`) — 34 outbound dependencies
4. **http.c** (`dirmngr/http.c`) — 32 outbound dependencies
5. **sysutils.c** (`common/sysutils.c`) — 29 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `main` **(Many-Argument Workhorses)** (@ `g10/gpg.c`) -> Impact: **1025.2** | LOC: 1625
- `main` **(Many-Argument Workhorses)** (@ `sm/gpgsm.c`) -> Impact: **820.1** | LOC: 1471
- `keyedit_menu` **(Many-Argument Workhorses)** (@ `g10/keyedit.c`) -> Impact: **770.7** | LOC: 968
  * *Intent:* #endif /* HAVE_LIBREADLINE */
- `Eval_Cycle` **(Many-Argument Workhorses)** (@ `tests/gpgscm/scheme.c`) -> Impact: **644.6** | LOC: 1668
  * *Intent:* /* Safe because we would have already returned if `fast' encountered a non-pair. */
- `parse_key_parameter_part` **(Many-Argument Workhorses)** (@ `g10/keygen.c`) -> Impact: **612.9** | LOC: 411
  * *Intent:* /* Helper for parse_key_parameter_part_parameter_string for one part of the * specification string; i.e. ALGO/FLAGS. If STRING is NULL or empty * succ...
- `import_one_real` **(Many-Argument Workhorses)** (@ `g10/import.c`) -> Impact: **585.1** | LOC: 547
  * *Intent:* /* * Try to import one keyblock. Return an error only in serious cases, * but never for an invalid keyblock. It uses log_error to increase * the inter...
- `do_validate_chain` **(Many-Argument Workhorses)** (@ `sm/certchain.c`) -> Impact: **537.5** | LOC: 669
- `main` **(Many-Argument Workhorses)** (@ `tools/gpg-connect-agent.c`) -> Impact: **518.6** | LOC: 812
- `parse_key` **(Many-Argument Workhorses)** (@ `g10/parse-packet.c`) -> Impact: **511.1** | LOC: 592
- `sign_uids` **(Many-Argument Workhorses)** (@ `g10/keyedit.c`) -> Impact: **505.5** | LOC: 606
  * *Intent:* /* * Loop over all LOCUSR and sign the uids after asking. If no user id * is marked, all user ids will be signed; if some user_ids are marked * only t...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/openpgp/samplemsgs` | 60 | 295001.0 | 0.0% | 0.0% |
| `tests/openpgp/privkeys` | 47 | 235000.0 | 0.0% | 0.0% |
| `tests/openpgp/samplekeys` | 37 | 180001.0 | 0.0% | 0.0% |
| `tests/openpgp` | 99 | 116573.19 | 1.9% | 0.0% |
| `tests/cms` | 39 | 115204.74 | 0.65% | 0.0% |
| `tests/cms/samplekeys` | 24 | 115001.0 | 0.0% | 0.0% |
| `g10` | 103 | 113739.26 | 49.96% | 35.7% |
| `tests/openpgp/trust-pgp` | 12 | 55002.58 | 0.0% | 0.0% |
| `dirmngr` | 67 | 54461.76 | 42.35% | 26.22% |
| `scd` | 23 | 41578.42 | 54.17% | 17.66% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `common/t-support.c` -> **100.0%** Exposure
- `tools/no-libgcrypt.c` -> **99.9991%** Exposure
- `g10/gpgv.c` -> **99.9958%** Exposure
- `common/logging.h` -> **99.9955%** Exposure
- `common/xasprintf.c` -> **99.9925%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `agent/call-daemon.c` -> **100.0%** Exposure
- `agent/call-pinentry.c` -> **100.0%** Exposure
- `agent/call-scd.c` -> **100.0%** Exposure
- `agent/command-ssh.c` -> **100.0%** Exposure
- `agent/command.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `g10/gpgv.c` -> **55** Orphaned Functions | **0** Duplicates
- `tests/gpgscm/ffi.c` -> **53** Orphaned Functions | **0** Duplicates
- `common/stringhelp.c` -> **46** Orphaned Functions | **0** Duplicates
- `g10/misc.c` -> **42** Orphaned Functions | **0** Duplicates
- `tests/gpgscm/init.scm` -> **37** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/openpgp/ecc.scm` -> **100.0%** Exposure
- `tests/openpgp/signed-messages.scm` -> **100.0%** Exposure
- `tools/der-to-pem` -> **100.0%** Exposure
- `tools/gpg-card.c` -> **42.9633%** Exposure
- `tests/openpgp/armor.scm` -> **39.7469%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `20` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3677` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `dirmngr/dns.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 10367.4 | **LOC:** 11687 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.635; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.3%), Guard Balance (formerly Safety Score) (96.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.6067% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dns_res_exec` **(Many-Argument Workhorses)** (Impact: 270.1)
  * `dns_so_check` **(Many-Argument Workhorses)** (Impact: 157.7)
    * *Intent:* } /* dns_so_tcp_recv() */ #if GPGRT_GCC_VERSION >= 80000 # pragma GCC diagnostic pop #elif __clang__...
  * `dns_resconf_loadfile` **(Many-Argument Workhorses)** (Impact: 129.4)
    * *Intent:* } /* dns_resconf_pton() */ #define dns_resconf_issep(ch) (dns_isspace(ch) || (ch) == ',') #define dn...
  * `dns_ai_nextent` **(Many-Argument Workhorses)** (Impact: 117.2)
    * *Intent:* }; /* enum dns_ai_state */ #define dns_ai_goto(which) do { ai->state = (which); goto exec; } while (...
  * `dns_trace_dump` **(Many-Argument Workhorses)** (Impact: 84.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 28 instances
* *Amplified Cascading Flux:* 1664 instances
* *Memory Alloc (weighted view):* 15
* *State Mutation (weighted view):* 5106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2041`, `structural_boundaries: 2393`, `args: 924`, `func_start: 494`, `class_start: 350`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 1778`, `dead_code: 44`, `planned_debt: 18`, `fragile_debt: 22`, `unreferenced_by_name: 31`
* *Architecture:* `io: 21`, `api: 255`, `import: 41`
* *Defense:* `safety: 298`, `doc: 2`, `immutability_locks: 295`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` inet.h, assert.h, cache.h, config.h, ctype.h, dns.h, err.h, errno.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/keygen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 8939.52 | **LOC:** 7360 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.635; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.5%)
- **Documentation Coverage:** 97.191% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_key_parameter_part` **(Many-Argument Workhorses)** (Impact: 612.9)
    * *Intent:* /* Helper for parse_key_parameter_part_parameter_string for one part of the * specification string; ...
  * `ask_algo` **(Many-Argument Workhorses)** (Impact: 485.8)
    * *Intent:* /* Ask for an algorithm. The function returns the algorithm id to * create. If ADDMODE is false the ...
  * `do_generate_keypair` **(Many-Argument Workhorses)** (Impact: 222.2)
  * `generate_keypair` **(Many-Argument Workhorses)** (Impact: 194.4)
    * *Intent:* /* * Generate a keypair (fname is only used in batch mode) If * CARD_SERIALNO is not NULL the functi...
  * `parse_key_parameter_string` **(Many-Argument Workhorses)** (Impact: 184.1)
    * *Intent:* * eddsa := Use algorithm EdDSA. * ecdh := Use algorithm ECDH. * v5 := Create version 5 key * * There...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1244 instances
* *State Mutation (weighted view):* 3864
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1777`, `structural_boundaries: 430`, `args: 267`, `func_start: 93`, `class_start: 58`
* *Risk/State:* `safety_bypasses: 67`, `state_mutation: 1376`, `fragile_debt: 34`, `unreferenced_by_name: 10`
* *Architecture:* `api: 30`, `import: 25`
* *Defense:* `safety: 27`, `doc: 7`, `immutability_locks: 127`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` host2net.h, i18n.h, mbox-util.h, shareddefs.h, status.h, ttyio.h, util.h, call-agent.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scd/app-p15.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 8276.52 | **LOC:** 6743 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.635; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.9%), Complexity Load (formerly Cognitive Load) (87.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_ef_aodf` **(Many-Argument Workhorses)** (Impact: 450.7)
  * `do_sign` **(Many-Argument Workhorses)** (Impact: 417.2)
  * `read_p15_info` **(Compute Cores)** (Impact: 233.2)
    * *Intent:* /* Get all the basic information from the pkcs#15 card, check the
  * `read_ef_pukdf` **(Many-Argument Workhorses)** (Impact: 206.4)
  * `verify_pin` **(Many-Argument Workhorses)** (Impact: 205.0)
    * *Intent:* /* Given the private key object PRKDF and its authentication object
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1331 instances
* *State Mutation (weighted view):* 4107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1712`, `structural_boundaries: 352`, `args: 217`, `func_start: 63`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1445`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 15`, `unreferenced_by_name: 1`
* *Architecture:* `api: 13`, `import: 13`
* *Defense:* `safety: 100`, `doc: 1`, `immutability_locks: 121`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` host2net.h, i18n.h, openpgpdefs.h, tlv.h, apdu.h, config.h, errno.h, iso7816.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scd/app-openpgp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 7865.24 | **LOC:** 6791 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.635; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.4%), Complexity Load (formerly Cognitive Load) (82.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ecc_writekey` **(Many-Argument Workhorses)** (Impact: 293.6)
  * `do_change_pin` **(Many-Argument Workhorses)** (Impact: 278.1)
  * `do_decipher` **(Many-Argument Workhorses)** (Impact: 276.7)
  * `rsa_writekey` **(Many-Argument Workhorses)** (Impact: 246.6)
  * `do_setattr` **(Many-Argument Workhorses)** (Impact: 201.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1127 instances
* *State Mutation (weighted view):* 3451
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1526`, `structural_boundaries: 445`, `args: 253`, `func_start: 82`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 1`, `state_mutation: 1197`, `planned_debt: 2`, `fragile_debt: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 6`, `import: 14`
* *Defense:* `safety: 145`, `doc: 1`, `immutability_locks: 178`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` host2net.h, i18n.h, openpgpdefs.h, tlv.h, util.h, config.h, errno.h, iso7816.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/keyedit.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 7241.14 | **LOC:** 7228 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.635; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.1%), Complexity Load (formerly Cognitive Load) (81.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `keyedit_menu` **(Many-Argument Workhorses)** (Impact: 770.7)
    * *Intent:* #endif /* HAVE_LIBREADLINE */
  * `sign_uids` **(Many-Argument Workhorses)** (Impact: 505.5)
    * *Intent:* /* * Loop over all LOCUSR and sign the uids after asking. If no user id * is marked, all user ids wi...
  * `keyedit_print_one_sig` **(Many-Argument Workhorses)** (Impact: 220.8)
    * *Intent:* /* * Print information about a signature (rc is its status), check it * and return true if the signa...
  * `show_key_with_all_names` **(Many-Argument Workhorses)** (Impact: 208.1)
    * *Intent:* /*
  * `show_key_with_all_names_colon` **(Many-Argument Workhorses)** (Impact: 140.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 931 instances
* *State Mutation (weighted view):* 2868
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1643`, `structural_boundaries: 316`, `args: 170`, `func_start: 73`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1006`, `dead_code: 5`, `planned_debt: 8`, `fragile_debt: 11`, `unreferenced_by_name: 13`
* *Architecture:* `api: 18`, `import: 29`
* *Defense:* `safety: 13`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` host2net.h, i18n.h, iobuf.h, mbox-util.h, status.h, ttyio.h, util.h, call-agent.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/gpgscm/scheme.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5153.24 | **LOC:** 6046 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.635; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (94.6%), Complexity Load (formerly Cognitive Load) (47.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (29.4%), Dead Code Surface (formerly Dead Code) (5.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Eval_Cycle` **(Many-Argument Workhorses)** (Impact: 644.6)
    * *Intent:* /* Safe because we would have already returned if `fast' encountered a non-pair. */
  * `atom2str` **(Many-Argument Workhorses)** (Impact: 175.2)
    * *Intent:* /* print atoms */
  * `readstrexp` **(Compute Cores)** (Impact: 71.0)
  * `MacTS_main` **(Compute Cores)** (Impact: 61.7)
  * `mk_sharp_const` **(Compute Cores)** (Impact: 61.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 14 instances
* *Amplified Cascading Flux:* 779 instances
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 2479
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1117`, `structural_boundaries: 541`, `args: 527`, `func_start: 231`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 2`, `state_mutation: 921`, `dead_code: 4`, `fragile_debt: 6`, `unreferenced_by_name: 9`
* *Architecture:* `io: 9`, `api: 95`, `import: 16`
* *Defense:* `safety: 84`, `doc: 1`, `immutability_locks: 56`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` assert.h, config.h, ctype.h, dynload.h, float.h, limits.h, math.h, opdefines.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/import.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 5073.2 | **LOC:** 4946 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.635; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.1%), Complexity Load (formerly Cognitive Load) (80.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `import_one_real` **(Many-Argument Workhorses)** (Impact: 585.1)
    * *Intent:* /* * Try to import one keyblock. Return an error only in serious cases, * but never for an invalid k...
  * `merge_blocks` **(Many-Argument Workhorses)** (Impact: 238.2)
    * *Intent:* /* * compare and merge the blocks * * o compare the signatures: If we already have this signature, c...
  * `impex_filter_getval` **(Many-Argument Workhorses)** (Impact: 199.6)
    * *Intent:* /* Helper for apply_*_filter in import.c and export.c and also used by
  * `read_block` **(Many-Argument Workhorses)** (Impact: 173.3)
    * *Intent:* /* Read the next keyblock from stream A. Meta data (ring trust * packets) are only considered if OPT...
  * `delete_inv_parts` **(Many-Argument Workhorses)** (Impact: 142.9)
    * *Intent:* /* Delete all parts which are invalid and those signatures whose * public key algorithm is not avail...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 630 instances
* *State Mutation (weighted view):* 1918
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1105`, `structural_boundaries: 236`, `args: 105`, `func_start: 57`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 658`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 22`, `unreferenced_by_name: 7`
* *Architecture:* `api: 18`, `import: 23`
* *Defense:* `safety: 40`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` i18n.h, init.h, mbox-util.h, membuf.h, recsel.h, status.h, ttyio.h, util.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dirmngr/sks-keyservers.netCA.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dirmngr/tls-ca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/com-certs.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/samplekeys.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/distsigkey.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/pubring.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/t-keydb-get-keyblock.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/t-stutter-data.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/cert_cci_sphinx_ca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/cert_cci_test_wzs.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/cert_cci_test_zs.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/cert_cci_user02.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/cert_cci_user03.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/cert_cci_user04.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/cert_cci_user06.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/cert_cci_user07.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/cert_testpki_testpca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/crl_testpki_testpca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `agent/pkdecrypt.c` -> Churn: **60.85%** | Cog Load: 84.7193% | Debt: 15.5168%
- `g10/keygen.c` -> Churn: **60.85%** | Cog Load: 79.4811% | Debt: 28.4551%
- `g10/call-agent.c` -> Churn: **58.79%** | Cog Load: 79.1391% | Debt: 48.719%
- `g10/armor.c` -> Churn: **54.66%** | Cog Load: 73.6186% | Debt: 35.5088%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `dirmngr/dns.c` -> **NIIBE Yutaka** (100.0% isolated ownership) | Magnitude: 10367.4
- `scd/app-p15.c` -> **Mario Haustein** (100.0% isolated ownership) | Magnitude: 8276.52
- `scd/app-openpgp.c` -> **Werner Koch** (100.0% isolated ownership) | Magnitude: 7865.24
- `g10/parse-packet.c` -> **Werner Koch** (100.0% isolated ownership) | Magnitude: 4932.44
- `g10/gpg.c` -> **Werner Koch** (100.0% isolated ownership) | Magnitude: 4571.44

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `common/iobuf.h` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 12.58%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `common/openpgpdefs.h` -> **Severity: 2.868** (Embedded: 0.0483 * Error Risk: 59.3991%)
- `common/host2net.h` -> **Severity: 2.428** (Embedded: 0.0308 * Error Risk: 78.8694%)
- `g10/packet.h` -> **Severity: 2.113** (Embedded: 0.048 * Error Risk: 43.9749%)
- `kbx/keybox-search-desc.h` -> **Severity: 1.932** (Embedded: 0.0345 * Error Risk: 56.0513%)
- `g10/tofu.h` -> **Severity: 1.871** (Embedded: 0.0309 * Error Risk: 60.5532%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/pkits/common.sh` -> **Severity: 980.4** (Blast Radius: 9.804 * Doc Risk: 100.0%)
- `common/openpgpdefs.h` -> **Severity: 783.6** (Blast Radius: 7.836 * Doc Risk: 100.0%)
- `agent/agent.h` -> **Severity: 595.7** (Blast Radius: 5.957 * Doc Risk: 100.0%)
- `common/host2net.h` -> **Severity: 436.3** (Blast Radius: 4.363 * Doc Risk: 100.0%)
- `kbx/keybox-defs.h` -> **Severity: 327.8** (Blast Radius: 3.278 * Doc Risk: 100.0%)

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
