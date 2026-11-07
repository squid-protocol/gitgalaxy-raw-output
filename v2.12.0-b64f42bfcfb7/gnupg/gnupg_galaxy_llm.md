# ARCHITECTURAL_BRIEF: gnupg
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/gpg/gnupg.git` |
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
- **Scope:** 987 analyzed artifact(s), 299190 LOC.
- **Load-bearing artifact:** `doc/mkdefsinc.c` -- 256 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `g10/gpg.c` -- pulls in 42 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `dirmngr/dns.c` at magnitude 10228.3 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 987 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 378 |
| Total LOC | 299190 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 72.3% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4086 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1794 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 13.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5508 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 9 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 489 | 283458 | 49.5% |
| PLAINTEXT | 273 | 189 | 27.7% |
| SCHEME | 109 | 4962 | 11.0% |
| SHELL | 43 | 2773 | 4.4% |
| M4 | 41 | 4932 | 4.2% |
| MARKDOWN | 13 | 0 | 1.3% |
| XML | 5 | 0 | 0.5% |
| MAKEFILE | 4 | 1630 | 0.4% |
| CSS | 2 | 57 | 0.2% |
| PERL | 2 | 30 | 0.2% |
| HTML | 1 | 46 | 0.1% |
| RUBY | 1 | 25 | 0.1% |
| PHP | 1 | 26 | 0.1% |
| PYTHON | 1 | 17 | 0.1% |
| BATCH | 1 | 23 | 0.1% |
| LIVECODE | 1 | 1022 | 0.1% |

## 4.1 SOURCE ENCODINGS
> 1 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 797 |
| unknown | unknown | 189 |
| latin-1 | latin-1-fallback | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 34%, Declarative / Non-Code 24%, Many-Argument Workhorses Files 17%, Large Core Modules (3) 10%, Compute Cores Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 701 | 71.0% |
| Unknown | 189 | 19.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 97 | 9.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 378*

**Composition by Extension & Reason:**
- `.png`: 48x Excluded (Explicitly Denied Extension: '.png')
- `.asc`: 43x Excluded (Unsupported Extension: '.asc')
- `no_extension`: 19x Unsupported Format (.undeterminable), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 72 LOC)
- `.po`: 28x Excluded (Unsupported Extension: '.po')
- `.texi`: 24x Excluded (Unsupported Extension: '.texi')
- `.am`: 20x Excluded (Unsupported Extension: '.am'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 20x Excluded (Binary Format Detected), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pem`: 21x Excluded (Unsupported Extension: '.pem')
- `.rc`: 10x Excluded (Unsupported Extension: '.rc'), 6x Unsupported Format (.rc)
- `.h`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.scm`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 9x Excluded (Explicitly Denied Extension: '.jpg')
- `.c`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 47 LOC)
- `.der`: 5x Excluded (Explicitly Denied Extension: '.der')
- `.ico`: 4x Excluded (Explicitly Denied Extension: '.ico')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 37.9 | 21.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.1 | 43.4 | 59.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 22.6 | 11.1 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 29.9 | 2.3 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.1 | 2.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 49.6 | 31.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 55.3 | 0.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.1 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 64.6 | 2.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 59.3 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1744 | 252 | 5 | `g10/test-stubs.c` |
| cleanup | 342 | 70 | 0 | `dirmngr/dns.c` |
| guards | 17828 | 511 | 52 | `dirmngr/dns.c` |
| danger | 2582 | 308 | 7 | `autogen.sh` |
| concurrency | 32 | 15 | 0 | `build-aux/mkinstalldirs` |
| connectivity | 5918 | 513 | 16 | `dirmngr/dns.c` |
| io | 1200 | 206 | 2 | `build-aux/speedo.mk` |
| crypto | 0 | 0 | 0 | - |
| ipc | 351 | 60 | 0 | `agent/gpg-agent.c` |
| time | 225 | 60 | 0 | `common/gettime.c` |
| serialization | 15 | 2 | 0 | `build-aux/speedo.mk` |
| regex | 83 | 21 | 0 | `autogen.sh` |
| events | 6296 | 271 | 17 | `g10/gpg.c` |
| tests | 24 | 15 | 0 | `common/t-name-value.c` |
| docs | 156 | 64 | 0 | `g10/trustdb.c` |
| debt | 2434 | 342 | 6 | `dirmngr/dns.c` |
| mutation | 89071 | 469 | 259 | `scd/app-p15.c` |
| dead_code | 2366 | 381 | 8 | `g10/test-stubs.c` |
| credential | 76 | 11 | 0 | `tools/der-to-pem` |
| threat | 84 | 22 | 0 | `common/t-convert.c` |
| ml_ai | 329 | 62 | 0 | `dirmngr/dns.c` |
| ui | 7 | 4 | 0 | `build-aux/speedo/w32/g4wihelp.c` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.3333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `build-aux/speedo.mk` (Hits: 85)
- `autogen.sh` (Hits: 73)
- `build-aux/getswdb.sh` (Hits: 57)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **mkdefsinc.c** (`doc/mkdefsinc.c`) — 256 inbound connections
2. **util.h** (`common/util.h`) — 216 inbound connections
3. **i18n.h** (`common/i18n.h`) — 165 inbound connections
4. **stringhelp.c** (`common/stringhelp.c`) — 151 inbound connections
5. **logging.h** (`common/logging.h`) — 80 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **gpg.c** (`g10/gpg.c`) — 42 outbound dependencies
2. **dns.c** (`dirmngr/dns.c`) — 35 outbound dependencies
3. **dirmngr.c** (`dirmngr/dirmngr.c`) — 34 outbound dependencies
4. **http.c** (`dirmngr/http.c`) — 32 outbound dependencies
5. **sysutils.c** (`common/sysutils.c`) — 29 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `main` **(Many-Argument Workhorses)** (@ `g10/gpg.c`) -> Impact: **1966.4** | LOC: 3233
- `main` **(Many-Argument Workhorses)** (@ `sm/gpgsm.c`) -> Impact: **813.1** | LOC: 1471
- `keyedit_menu` **(Many-Argument Workhorses)** (@ `g10/keyedit.c`) -> Impact: **699.3** | LOC: 968
  * *Intent:* #endif /* HAVE_LIBREADLINE */
- `parse_key_parameter_part` **(Many-Argument Workhorses)** (@ `g10/keygen.c`) -> Impact: **612.9** | LOC: 411
  * *Intent:* /* Helper for parse_key_parameter_part_parameter_string for one part of the * specification string; i.e. ALGO/FLAGS. If STRING is NULL or empty * succ...
- `import_one_real` **(Many-Argument Workhorses)** (@ `g10/import.c`) -> Impact: **581.2** | LOC: 547
  * *Intent:* /* * Try to import one keyblock. Return an error only in serious cases, * but never for an invalid keyblock. It uses log_error to increase * the inter...
- `do_validate_chain` **(Many-Argument Workhorses)** (@ `sm/certchain.c`) -> Impact: **537.5** | LOC: 669
- `parse_key` **(Many-Argument Workhorses)** (@ `g10/parse-packet.c`) -> Impact: **505.8** | LOC: 592
- `main` **(Many-Argument Workhorses)** (@ `tools/gpg-connect-agent.c`) -> Impact: **504.8** | LOC: 812
- `ask_algo` **(Many-Argument Workhorses)** (@ `g10/keygen.c`) -> Impact: **454.7** | LOC: 382
  * *Intent:* /* Ask for an algorithm. The function returns the algorithm id to * create. If ADDMODE is false the function won't show an option to * create the prim...
- `sign_uids` **(Many-Argument Workhorses)** (@ `g10/keyedit.c`) -> Impact: **451.7** | LOC: 606
  * *Intent:* /* * Loop over all LOCUSR and sign the uids after asking. If no user id * is marked, all user ids will be signed; if some user_ids are marked * only t...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/openpgp/samplemsgs` | 52 | 255001.0 | 0.0% | 0.0% |
| `tests/openpgp/privkeys` | 47 | 235000.0 | 0.0% | 0.0% |
| `g10` | 105 | 110727.38 | 49.28% | 33.23% |
| `tests/openpgp/samplekeys` | 19 | 90001.0 | 0.0% | 0.0% |
| `tests/openpgp` | 93 | 86574.69 | 2.02% | 0.0% |
| `tests/cms/samplekeys` | 16 | 75001.0 | 0.0% | 0.0% |
| `tests/cms` | 29 | 65204.74 | 0.87% | 0.0% |
| `dirmngr` | 65 | 43675.16 | 42.26% | 24.05% |
| `scd` | 23 | 41037.62 | 53.64% | 16.71% |
| `tests/openpgp/tofu/cross-sigs` | 9 | 40001.6 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `common/t-support.c` -> **100.0%** Exposure
- `g10/test-stubs.c` -> **100.0%** Exposure
- `tools/no-libgcrypt.c` -> **99.9985%** Exposure
- `g10/gpgv.c` -> **99.9954%** Exposure
- `common/logging.h` -> **99.9881%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `agent/call-daemon.c` -> **100.0%** Exposure
- `agent/call-pinentry.c` -> **100.0%** Exposure
- `agent/call-scd.c` -> **100.0%** Exposure
- `agent/command-ssh.c` -> **100.0%** Exposure
- `agent/command.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `g10/test-stubs.c` -> **59** Orphaned Functions | **0** Duplicates
- `g10/gpgv.c` -> **55** Orphaned Functions | **0** Duplicates
- `common/stringhelp.c` -> **46** Orphaned Functions | **0** Duplicates
- `g10/misc.c` -> **42** Orphaned Functions | **0** Duplicates
- `g10/call-agent.c` -> **36** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/openpgp/ecc.scm` -> **100.0%** Exposure
- `tests/openpgp/signed-messages.scm` -> **100.0%** Exposure
- `tools/der-to-pem` -> **100.0%** Exposure
- `tools/gpg-card.c` -> **49.708%** Exposure
- `tests/openpgp/armor.scm` -> **39.7469%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `19` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3634` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `dirmngr/dns.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.145)
- **Top Global Matches:** file_cluster_4: 9.145, file_cluster_16: 10.985, file_cluster_15: 12.058
- **Magnitude:** 10228.3 | **LOC:** 11687 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **35**; blast radius 0.718; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.7%)
- **Documentation Coverage:** 99.6067% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dns_res_exec` **(Many-Argument Workhorses)** (Impact: 270.1)
  * `dns_so_check` **(Many-Argument Workhorses)** (Impact: 154.9)
    * *Intent:* } /* dns_so_tcp_recv() */ #if GPGRT_GCC_VERSION >= 80000 # pragma GCC diagnostic pop #elif __clang__...
  * `dns_resconf_loadfile` **(Many-Argument Workhorses)** (Impact: 129.4)
    * *Intent:* } /* dns_resconf_pton() */ #define dns_resconf_issep(ch) (dns_isspace(ch) || (ch) == ',') #define dn...
  * `dns_ai_nextent` **(Many-Argument Workhorses)** (Impact: 117.2)
    * *Intent:* }; /* enum dns_ai_state */ #define dns_ai_goto(which) do { ai->state = (which); goto exec; } while (...
  * `dns_p_push` **(Many-Argument Workhorses)** (Impact: 83.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 28 instances
* *Amplified Cascading Flux:* 1640 instances
* *Memory Alloc (weighted view):* 15
* *State Mutation (weighted view):* 5058
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1864`, `structural_boundaries: 2393`, `args: 924`, `func_start: 494`, `class_start: 350`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 1778`, `dead_code: 19`, `planned_debt: 18`, `fragile_debt: 22`, `unreferenced_by_name: 31`
* *Architecture:* `io: 21`, `api: 255`, `import: 41`
* *Defense:* `safety: 298`, `doc: 2`, `immutability_locks: 295`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.718
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.010462
  * `Imports (Out-Degree: 3):` inet.h, assert.h, cache.h, config.h, ctype.h, dns.h, err.h, errno.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `g10/keygen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.316)
- **Top Global Matches:** file_cluster_8: 9.316, file_cluster_3: 15.972, file_cluster_6: 21.17
- **Magnitude:** 8772.02 | **LOC:** 7360 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **25**; blast radius 0.617; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.6%), Complexity Load (formerly Cognitive Load) (78.8%)
- **Documentation Coverage:** 97.191% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_key_parameter_part` **(Many-Argument Workhorses)** (Impact: 612.9)
    * *Intent:* /* Helper for parse_key_parameter_part_parameter_string for one part of the * specification string; ...
  * `ask_algo` **(Many-Argument Workhorses)** (Impact: 454.7)
    * *Intent:* /* Ask for an algorithm. The function returns the algorithm id to * create. If ADDMODE is false the ...
  * `do_generate_keypair` **(Many-Argument Workhorses)** (Impact: 217.8)
  * `generate_keypair` **(Many-Argument Workhorses)** (Impact: 189.5)
    * *Intent:* /* * Generate a keypair (fname is only used in batch mode) If * CARD_SERIALNO is not NULL the functi...
  * `parse_key_parameter_string` **(Many-Argument Workhorses)** (Impact: 175.3)
    * *Intent:* * eddsa := Use algorithm EdDSA. * ecdh := Use algorithm ECDH. * v5 := Create version 5 key * * There...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1240 instances
* *State Mutation (weighted view):* 3856
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1710`, `structural_boundaries: 430`, `args: 267`, `func_start: 93`, `class_start: 58`
* *Risk/State:* `safety_bypasses: 67`, `state_mutation: 1376`, `fragile_debt: 34`, `unreferenced_by_name: 10`
* *Architecture:* `api: 30`, `import: 25`
* *Defense:* `safety: 27`, `doc: 7`, `immutability_locks: 127`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.617
  * `Choke Point (Betweenness):` 7.5e-05 | `Ripple Effect (Closeness):` 0.005134
  * `Imports (Out-Degree: 56):` host2net.h, i18n.h, mbox-util.h, shareddefs.h, status.h, ttyio.h, util.h, call-agent.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `scd/app-p15.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.517)
- **Top Global Matches:** file_cluster_3: 7.517, file_cluster_8: 18.196, file_cluster_6: 31.022
- **Magnitude:** 8189.82 | **LOC:** 6743 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.576; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.7%), Guard Balance (formerly Safety Score) (81.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_ef_aodf` **(Many-Argument Workhorses)** (Impact: 448.7)
  * `do_sign` **(Many-Argument Workhorses)** (Impact: 384.0)
  * `read_p15_info` **(Compute Cores)** (Impact: 233.2)
    * *Intent:* /* Get all the basic information from the pkcs#15 card, check the
  * `read_ef_pukdf` **(Many-Argument Workhorses)** (Impact: 206.4)
  * `read_ef_cdf` **(Many-Argument Workhorses)** (Impact: 203.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1328 instances
* *State Mutation (weighted view):* 4101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1680`, `structural_boundaries: 352`, `args: 217`, `func_start: 63`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1445`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 15`, `unreferenced_by_name: 1`
* *Architecture:* `api: 13`, `import: 13`
* *Defense:* `safety: 100`, `doc: 1`, `immutability_locks: 121`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` host2net.h, i18n.h, openpgpdefs.h, tlv.h, apdu.h, config.h, errno.h, iso7816.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scd/app-openpgp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.255)
- **Top Global Matches:** file_cluster_8: 10.255, file_cluster_3: 14.338, file_cluster_6: 22.592
- **Magnitude:** 7776.34 | **LOC:** 6791 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 0.6; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ecc_writekey` **(Many-Argument Workhorses)** (Impact: 290.6)
  * `do_decipher` **(Many-Argument Workhorses)** (Impact: 273.4)
  * `do_change_pin` **(Many-Argument Workhorses)** (Impact: 259.6)
  * `rsa_writekey` **(Many-Argument Workhorses)** (Impact: 246.6)
  * `do_setattr` **(Many-Argument Workhorses)** (Impact: 201.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1120 instances
* *State Mutation (weighted view):* 3437
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1494`, `structural_boundaries: 445`, `args: 253`, `func_start: 82`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 1`, `state_mutation: 1197`, `planned_debt: 2`, `fragile_debt: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 6`, `import: 14`
* *Defense:* `safety: 145`, `doc: 1`, `immutability_locks: 178`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.6
  * `Choke Point (Betweenness):` 4e-05 | `Ripple Effect (Closeness):` 0.005356
  * `Imports (Out-Degree: 23):` host2net.h, i18n.h, openpgpdefs.h, tlv.h, util.h, config.h, errno.h, iso7816.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `g10/keyedit.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.178)
- **Top Global Matches:** file_cluster_8: 11.178, file_cluster_3: 13.962, file_cluster_6: 23.416
- **Magnitude:** 7029.54 | **LOC:** 7228 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **28**; blast radius 0.623; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `keyedit_menu` **(Many-Argument Workhorses)** (Impact: 699.3)
    * *Intent:* #endif /* HAVE_LIBREADLINE */
  * `sign_uids` **(Many-Argument Workhorses)** (Impact: 451.7)
    * *Intent:* /* * Loop over all LOCUSR and sign the uids after asking. If no user id * is marked, all user ids wi...
  * `keyedit_print_one_sig` **(Many-Argument Workhorses)** (Impact: 210.4)
    * *Intent:* /* * Print information about a signature (rc is its status), check it * and return true if the signa...
  * `show_key_with_all_names` **(Many-Argument Workhorses)** (Impact: 208.1)
    * *Intent:* /*
  * `show_key_with_all_names_colon` **(Many-Argument Workhorses)** (Impact: 138.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 928 instances
* *State Mutation (weighted view):* 2862
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1554`, `structural_boundaries: 316`, `args: 170`, `func_start: 73`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1006`, `dead_code: 6`, `planned_debt: 8`, `fragile_debt: 11`, `unreferenced_by_name: 13`
* *Architecture:* `api: 18`, `import: 29`
* *Defense:* `safety: 13`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.623
  * `Choke Point (Betweenness):` 0.000133 | `Ripple Effect (Closeness):` 0.005477
  * `Imports (Out-Degree: 61):` host2net.h, i18n.h, iobuf.h, mbox-util.h, status.h, ttyio.h, util.h, call-agent.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `g10/gpg.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.614)
- **Top Global Matches:** file_cluster_8: 7.614, file_cluster_6: 10.81, file_cluster_4: 19.137
- **Magnitude:** 5481.34 | **LOC:** 6035 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **42**; blast radius 0.576; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.2%)
- **Documentation Coverage:** 97.8723% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 1966.4)
  * `check_permissions` **(Many-Argument Workhorses)** (Impact: 118.9)
    * *Intent:* Returns true if the item is unsafe. */
  * `print_mds` **(Many-Argument Workhorses)** (Impact: 71.1)
  * `list_config` **(Compute Cores)** (Impact: 67.2)
    * *Intent:* for frontends. */
  * `set_cmd` **(Compute Cores)** (Impact: 64.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 837 instances
* *State Mutation (weighted view):* 2577
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1471`, `structural_boundaries: 537`, `args: 147`, `func_start: 42`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 903`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 13`
* *Architecture:* `io: 1`, `api: 2`, `import: 42`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 95):` asshelp.h, comopt.h, compliance.h, gc-opt-flags.h, i18n.h, init.h, iobuf.h, mbox-util.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/import.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.548)
- **Top Global Matches:** file_cluster_8: 8.548, file_cluster_3: 16.447, file_cluster_6: 20.469
- **Magnitude:** 5025.6 | **LOC:** 4946 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **23**; blast radius 0.64; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `import_one_real` **(Many-Argument Workhorses)** (Impact: 581.2)
    * *Intent:* /* * Try to import one keyblock. Return an error only in serious cases, * but never for an invalid k...
  * `merge_blocks` **(Many-Argument Workhorses)** (Impact: 238.2)
    * *Intent:* /* * compare and merge the blocks * * o compare the signatures: If we already have this signature, c...
  * `impex_filter_getval` **(Many-Argument Workhorses)** (Impact: 197.9)
    * *Intent:* /* Helper for apply_*_filter in import.c and export.c and also used by
  * `read_block` **(Many-Argument Workhorses)** (Impact: 173.3)
    * *Intent:* /* Read the next keyblock from stream A. Meta data (ring trust * packets) are only considered if OPT...
  * `delete_inv_parts` **(Many-Argument Workhorses)** (Impact: 142.9)
    * *Intent:* /* Delete all parts which are invalid and those signatures whose * public key algorithm is not avail...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 630 instances
* *State Mutation (weighted view):* 1918
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1080`, `structural_boundaries: 236`, `args: 105`, `func_start: 57`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 658`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 22`, `unreferenced_by_name: 7`
* *Architecture:* `api: 18`, `import: 23`
* *Defense:* `safety: 40`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.64
  * `Choke Point (Betweenness):` 0.000159 | `Ripple Effect (Closeness):` 0.004832
  * `Imports (Out-Degree: 56):` i18n.h, init.h, mbox-util.h, membuf.h, recsel.h, status.h, ttyio.h, util.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `g10/distsigkey.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/t-keydb-get-keyblock.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/t-stutter-data.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/key_g10code_pete1.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/key_g10code_theo1.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/plain-1.cms.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/plain-2.cms.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/plain-3.cms.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/plain-large.cms.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/samplekeys/32100C27173EF6E9C4E9A25D3D69F86D37A4F939.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/samplekeys/68A638998DFABAC510EA645CE34F9686B2EDF7EA.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/samplekeys/8D6D17B4B94BBE8304926C016D2C5C7805EB6705.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/samplekeys/credential_private_encrypted_3DES.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/samplekeys/credential_private_encrypted_AES256.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/samplekeys/cryptlib-key.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/samplekeys/edward.tester@demo.gnupg.com.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/samplekeys/nistp256-openssl-self-signed.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/samplekeys/opensc-test.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/openpgp/shell.scm` (SCHEME) | Magnitude: 15.5 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 11, branch: 3, indent_tabs: 3, io: 2
- `tests/openpgp/verify.scm` (SCHEME) | Magnitude: 15.98 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, closures: 6, high_risk_execution: 4, io: 3
- `tests/openpgp/encrypt.scm` (SCHEME) | Magnitude: 16.86 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 57, closures: 12, branch: 3, io: 1
- `tests/openpgp/armdetachm.scm` (SCHEME) | Magnitude: 15.32 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4, closures: 2, io: 1, comprehensions: 1
- `tests/openpgp/detachm.scm` (SCHEME) | Magnitude: 15.32 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4, closures: 2, io: 1, comprehensions: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `tests/pkits/common.sh` (SHELL) | Magnitude: 220.7 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 153, indent_spaces: 136, branch: 53, core_var_decl: 43
- `tests/pkits/basic-certificate-revocation` (SHELL) | Magnitude: 9.62 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 2, io: 2, state_mutation: 2, core_var_decl: 2
- `tests/pkits/certificate-policies` (SHELL) | Magnitude: 9.62 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 2, io: 2, state_mutation: 2, core_var_decl: 2
- `tests/pkits/delta-crls` (SHELL) | Magnitude: 9.62 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 2, io: 2, state_mutation: 2, core_var_decl: 2
- `tests/pkits/distribution-points` (SHELL) | Magnitude: 9.62 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 2, io: 2, state_mutation: 2, core_var_decl: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `sm/passphrase.c` (C) | Magnitude: 56.1 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 35, branch: 14, state_mutation: 9, structural_boundaries: 7
- `m4/pkg.m4` (M4) | Magnitude: 30.62 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: args: 50, indent_spaces: 24, indent_tabs: 15, func_start: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `common/localename.c` (C) | Magnitude: 48.72 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 19, macros: 13, branch: 10, state_mutation: 9
- `common/t-w32-reg.c` (C) | Magnitude: 18.78 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 27, import: 9, branch: 6, pointers: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `dirmngr/t-support.c` (C) | Magnitude: 4.02 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: import: 7, indent_spaces: 5, structural_boundaries: 4, explicit_casts: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/cms/sign.scm` (SCHEME) | Magnitude: 15.32 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 9, closures: 2, io: 1
- `tests/gpgme/gpgme-defs.scm` (SCHEME) | Magnitude: 26.34 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 52, indent_tabs: 11, branch: 7, args: 5
- `m4/autobuild.m4` (M4) | Magnitude: 4.44 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 15, telemetry: 6, core_var_decl: 3, design_snake_case: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/asschk.c` (C) | Magnitude: 917.24 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 632, branch: 230, pointers: 178, state_mutation: 150

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `common/asshelp.c` (C) | Magnitude: 698.68 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 511, branch: 119, state_mutation: 95, pointers: 88
- `sm/server.c` (C) | Magnitude: 1420.3 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1217, branch: 296, pointers: 271, state_mutation: 260

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tools/der-to-pem` (SHELL) | Magnitude: 0.02 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: sec_hardcoded_secrets: 51, structural_boundaries: 8, indent_spaces: 4, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `kbx/keybox-util.c` (C) | Magnitude: 68.02 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 45, branch: 14, state_mutation: 11, pointers: 10
- `sm/fingerprint.c` (C) | Magnitude: 361.06 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 293, state_mutation: 69, branch: 58, core_var_decl: 52

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `g10/call-agent.c` -> Churn: **62.43%** | Cog Load: 79.1391% | Debt: 48.0079%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `dirmngr/dns.c` -> **NIIBE Yutaka** (100.0% isolated ownership) | Magnitude: 10228.3
- `scd/app-p15.c` -> **Mario Haustein** (100.0% isolated ownership) | Magnitude: 8189.82
- `scd/app-openpgp.c` -> **Werner Koch** (100.0% isolated ownership) | Magnitude: 7776.34
- `g10/gpg.c` -> **Werner Koch** (100.0% isolated ownership) | Magnitude: 5481.34
- `g10/import.c` -> **Werner Koch** (100.0% isolated ownership) | Magnitude: 5025.6

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `g10/getkey.c` -> **Severity: 0.345** (Bridge: 0.0035 * Flux: 100.0%)
- `g10/keyid.c` -> **Severity: 0.177** (Bridge: 0.0018 * Flux: 100.0%)
- `g10/misc.c` -> **Severity: 0.175** (Bridge: 0.0018 * Flux: 99.9997%)
- `sm/t-minip12.c` -> **Severity: 0.141** (Bridge: 0.0014 * Flux: 100.0%)
- `g10/mainproc.c` -> **Severity: 0.111** (Bridge: 0.0011 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `doc/mkdefsinc.c` -> **Severity: 18.594** (Embedded: 0.2571 * Error Risk: 72.3175%)
- `common/stringhelp.c` -> **Severity: 15.37** (Embedded: 0.1841 * Error Risk: 83.509%)
- `common/logging.h` -> **Severity: 11.343** (Embedded: 0.1862 * Error Risk: 60.9318%)
- `common/sysutils.c` -> **Severity: 9.618** (Embedded: 0.147 * Error Risk: 65.4381%)
- `common/utf8conv.c` -> **Severity: 9.33** (Embedded: 0.1161 * Error Risk: 80.374%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `common/util.h` -> **Severity: 3595.4** (Blast Radius: 35.954 * Doc Risk: 100.0%)
- `doc/mkdefsinc.c` -> **Severity: 1974.9** (Blast Radius: 19.749 * Doc Risk: 100.0%)
- `common/logging.h` -> **Severity: 1117.3** (Blast Radius: 11.173 * Doc Risk: 100.0%)
- `common/stringhelp.c` -> **Severity: 912.671** (Blast Radius: 10.312 * Doc Risk: 88.5057%)
- `tests/tpm2dtests/defs.scm` -> **Severity: 904.6** (Blast Radius: 9.046 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1338 literal sites + 24 sites through wrappers = 1362
- **`memory_alloc`:** 228 literal sites + 5489 sites through wrappers = 5717
- **`panics_and_aborts`:** 1006 literal sites + 125 sites through wrappers = 1131

- `xfree` (function, memory_alloc, primitive): 3966 call sites in 257 files -- `doc/mkdefsinc.c`
- `xtrymalloc` (macro, memory_alloc, primitive): 395 call sites in 132 files -- `common/dotlock.c`
- `xtrycalloc` (macro, memory_alloc, primitive): 224 call sites in 101 files -- `common/dotlock.c`
- `free_strlist` (function, memory_alloc, via xfree): 114 call sites in 32 files -- `common/strlist.c`
- `free_public_key` (function, memory_alloc, via xfree): 76 call sites in 15 files -- `g10/free-packet.c`
- `gpg_err_code_from_syserror` (function, panics_and_aborts, primitive): 69 call sites in 29 files -- `common/t-support.c`
- `FREEEXPR` (macro, memory_alloc, via recsel_release): 50 call sites in 1 files -- `common/t-recsel.c`
- `xtrymalloc_secure` (macro, memory_alloc, via gcry_malloc_secure): 36 call sites in 18 files -- `common/util.h`
- `release_progress_context` (function, memory_alloc, via xfree): 29 call sites in 6 files -- `g10/progress.c`
- `release_armor_context` (function, memory_alloc, via xfree): 24 call sites in 12 files -- `g10/armor.c`
- `dns_p_setptr` (function, memory_alloc, via dns_p_free): 22 call sites in 1 files -- `dirmngr/dns.c`
- `dirmngr_exit` (function, panics_and_aborts, primitive): 20 call sites in 3 files -- `dirmngr/dirmngr.c`
*(+163 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 43947 call pairs -- scoped 16.5%, unique 23.3%, ambiguous 5.3%, external 54.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 41986 | 16.8% | 24.3% | 5.5% | 53.4% |
| scheme | 793 | 6.1% | 4.3% | 0.4% | 89.3% |
| livecode | 459 | 0.0% | 0.0% | 0.0% | 100.0% |
| m4 | 356 | 3.1% | 2.0% | 0.0% | 94.9% |
| shell | 326 | 37.1% | 0.0% | 0.6% | 62.3% |
| ruby | 11 | 0.0% | 0.0% | 0.0% | 100.0% |
| makefile | 8 | 0.0% | 0.0% | 0.0% | 100.0% |
| python | 8 | 0.0% | 0.0% | 0.0% | 100.0% |

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
