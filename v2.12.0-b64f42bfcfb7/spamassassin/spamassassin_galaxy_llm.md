# ARCHITECTURAL_BRIEF: spamassassin
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/apache/spamassassin` |
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
- **Scope:** 681 analyzed artifact(s), 106671 LOC.
- **Load-bearing artifact:** `lib/Mail/SpamAssassin/Logger.pm` -- 97 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `lib/Mail/SpamAssassin.pm` -- pulls in 36 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/Mail/SpamAssassin/Conf.pm` at magnitude 22397.66 (structural weight, not risk).
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
| Total Artifacts | 1881 |
| Analyzed Artifacts (Scanned) | 681 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1200 |
| Total LOC | 106671 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 36.2% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4018 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3157 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.092 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 18 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 486 | 97221 | 71.4% |
| SHELL | 63 | 2480 | 9.3% |
| PLAINTEXT | 44 | 2 | 6.5% |
| MARKDOWN | 28 | 0 | 4.1% |
| POSTGRESQL | 18 | 335 | 2.6% |
| C | 15 | 5255 | 2.2% |
| YAML | 9 | 376 | 1.3% |
| MAKEFILE | 5 | 210 | 0.7% |
| SQLITE | 4 | 19 | 0.6% |
| PHP | 2 | 5 | 0.3% |
| M4 | 2 | 144 | 0.3% |
| CSS | 1 | 123 | 0.1% |
| JAVASCRIPT | 1 | 339 | 0.1% |
| XML | 1 | 0 | 0.1% |
| CSV | 1 | 3 | 0.1% |
| LIVECODE | 1 | 159 | 0.1% |

## 4.1 SOURCE ENCODINGS
> 10 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 669 |
| cp1252 | cp1252-fallback | 10 |
| unknown | unknown | 2 |

> 1 guessed file(s) read as double-byte text that decodes strictly as euc_jp / gbk / big5 / euc_kr: if that is the estate's code page, rescan with `--source-encoding euc_jp` (or the right one of those). E.g. `t/data/nice/cjk/iso-2022-jp.2`.

> 1 guessed file(s) read as double-byte text that decodes strictly as gbk: if that is the estate's code page, rescan with `--source-encoding gbk` (or the right one of those). E.g. `t/data/nice/cjk/gb2312.2`.

> 1 guessed file(s) read as double-byte text that decodes strictly as shift_jis / euc_jp / gbk / big5 / euc_kr: if that is the estate's code page, rescan with `--source-encoding shift_jis` (or the right one of those). E.g. `t/data/welcomelists/linuxplanet`.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 40%, Data / Markup / Trivial 17%, Compute Cores Files 15%, Large Core Modules (3) 14%, Many-Argument Workhorses Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 609 | 89.4% |
| Unknown | 2 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 70 | 10.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1200*

**Composition by Extension & Reason:**
- `no_extension`: 248x Unsupported Format (.undeterminable), 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Saturation: Line 2 exceeds 500 chars)
- `.cf`: 239x Excluded (Unsupported Extension: '.cf'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lm`: 172x Excluded (Unsupported Extension: '.lm')
- `.eml`: 44x Excluded (Unsupported Extension: '.eml')
- `.msg`: 44x Excluded (Unsupported Extension: '.msg')
- `.8`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.1`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.3`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pre`: 16x Excluded (Unsupported Extension: '.pre'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.2`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.5`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.4`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.7`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.9 | 41.6 | 39.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 54.9 | 56.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 18.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 20.9 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 74.6 | 99.6 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 72.0 | 1.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.5 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 43.8 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1656 | 212 | 7 | `lib/Mail/SpamAssassin/Plugin/NeuralNetwork.pm` |
| cleanup | 926 | 236 | 4 | `masses/mass-check` |
| guards | 1393 | 352 | 5 | `spamc/libspamc.c` |
| danger | 3122 | 292 | 11 | `masses/bayes-testing/bayes-10pcv-driver` |
| concurrency | 271 | 76 | 1 | `lib/Mail/SpamAssassin/AsyncLoop.pm` |
| connectivity | 2607 | 293 | 11 | `lib/Mail/SpamAssassin/Conf.pm` |
| io | 2335 | 306 | 9 | `masses/rule-update-score-gen/generate-new-scores.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 117 | 50 | 0 | `spamc/spamc.c` |
| time | 636 | 125 | 2 | `tools/sa-stats.pl` |
| serialization | 6 | 4 | 0 | `tools/github/apply_pr.sh` |
| regex | 5111 | 314 | 21 | `lib/Mail/SpamAssassin/Util.pm` |
| events | 64 | 34 | 0 | `masses/rule-qa/automc/sorttable.js` |
| tests | 1544 | 244 | 5 | `t/uri.t` |
| docs | 996 | 137 | 2 | `lib/Mail/SpamAssassin/Conf.pm` |
| debt | 2967 | 398 | 13 | `lib/Mail/SpamAssassin/Util.pm` |
| mutation | 20283 | 563 | 77 | `lib/Mail/SpamAssassin/Conf.pm` |
| dead_code | 686 | 185 | 3 | `lib/Mail/SpamAssassin/BayesStore/DBM.pm` |
| credential | 9 | 3 | 0 | `t/uri.t` |
| threat | 34 | 13 | 0 | `lib/Mail/SpamAssassin/Plugin/OLEVBMacro.pm` |
| ml_ai | 521 | 115 | 2 | `masses/mass-check` |
| ui | 122 | 21 | 0 | `masses/rule-qa/automc/ruleqa.cgi` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.05**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `masses/rule-update-score-gen/generate-new-scores.sh` (Hits: 120)
- `rulesrc/sandbox/dos/new-rule-score-gen/generate-new-scores` (Hits: 119)
- `masses/mass-check` (Hits: 80)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Logger.pm** (`lib/Mail/SpamAssassin/Logger.pm`) — 97 inbound connections
2. **Util.pm** (`lib/Mail/SpamAssassin/Util.pm`) — 74 inbound connections
3. **SpamAssassin.pm** (`lib/Mail/SpamAssassin.pm`) — 71 inbound connections
4. **Plugin.pm** (`lib/Mail/SpamAssassin/Plugin.pm`) — 71 inbound connections
5. **Constants.pm** (`lib/Mail/SpamAssassin/Constants.pm`) — 31 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **SpamAssassin.pm** (`lib/Mail/SpamAssassin.pm`) — 36 outbound dependencies
2. **mass-check** (`masses/mass-check`) — 33 outbound dependencies
3. **spamc.c** (`spamc/spamc.c`) — 28 outbound dependencies
4. **Util.pm** (`lib/Mail/SpamAssassin/Util.pm`) — 27 outbound dependencies
5. **Apache2.pm** (`spamd-apache2/lib/Mail/SpamAssassin/Spamd/Apache2.pm`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `set_default_commands` **(Many-Argument Workhorses)** (@ `lib/Mail/SpamAssassin/Conf.pm`) -> Impact: **20981.6** | LOC: 4896
  * *Intent:* # set to "1" by the test suite code, to record regression tests # $Mail::SpamAssassin::Conf::COLLECT_REGRESSION_TESTS = 1; # search for "sub new {" to...
- `begin_evalstr_chunk` **(Many-Argument Workhorses)** (@ `lib/Mail/SpamAssassin/Plugin/Check.pm`) -> Impact: **2832.3** | LOC: 932
- `scan` **(Many-Argument Workhorses)** (@ `lib/Mail/SpamAssassin/Plugin/Bayes.pm`) -> Impact: **2782.9** | LOC: 1057
  * *Intent:* ###########################################################################
- `set_config` **(Many-Argument Workhorses)** (@ `lib/Mail/SpamAssassin/Plugin/TxRep.pm`) -> Impact: **2226.0** | LOC: 972
  * *Intent:* ###########################################################################
- `set_config` **(Many-Argument Workhorses)** (@ `lib/Mail/SpamAssassin/Plugin/ASN.pm`) -> Impact: **1049.8** | LOC: 388
  * *Intent:* ###########################################################################
- `parse_css_background` **(Many-Argument Workhorses)** (@ `lib/Mail/SpamAssassin/HTML.pm`) -> Impact: **974.0** | LOC: 511
  * *Intent:* # Parses a CSS background property value. # Returns an arrayref of layers, each layer is an arrayref of values such as # [ # 'rgb(255, 192, 0)', # '35...
- `parse_received_line` **(Many-Argument Workhorses)** (@ `lib/Mail/SpamAssassin/Message/Metadata/Received.pm`) -> Impact: **880.1** | LOC: 1112
  * *Intent:* # returns undef if the header just couldn't be parsed # returns 0 if the header was specifically skipped # returns a hash of information if the header...
- `_opensocket` **(Many-Argument Workhorses)** (@ `spamc/libspamc.c`) -> Impact: **878.1** | LOC: 2243
  * *Intent:* /* * opensocket() * * Given a socket family (PF_INET or PF_INET6 or PF_UNIX), try to * create this socket and store the FD in the pointed-to place. * ...
- `html_tests` **(Many-Argument Workhorses)** (@ `lib/Mail/SpamAssassin/HTML.pm`) -> Impact: **658.9** | LOC: 347
- `set_config` **(Many-Argument Workhorses)** (@ `lib/Mail/SpamAssassin/Plugin/OLEVBMacro.pm`) -> Impact: **596.3** | LOC: 287

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib/Mail/SpamAssassin/Plugin` | 56 | 43124.98 | 68.84% | 42.87% |
| `lib/Mail/SpamAssassin` | 34 | 42769.24 | 56.38% | 54.05% |
| `t` | 232 | 9672.3 | 33.05% | 11.71% |
| `masses` | 36 | 8130.44 | 59.18% | 5.66% |
| `lib/Mail/SpamAssassin/BayesStore` | 7 | 7912.28 | 54.27% | 39.79% |
| `spamd-apache2/t/certs` | 2 | 5012.22 | 0.0% | 0.0% |
| `t/data/etc` | 2 | 5001.0 | 0.0% | 0.0% |
| `spamc` | 17 | 4863.28 | 32.35% | 21.6% |
| `masses/rule-qa/automc` | 6 | 2747.55 | 41.31% | 4.78% |
| `lib/Mail/SpamAssassin/Message/Metadata` | 1 | 2250.44 | 96.89% | 99.89% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lib/Mail/SpamAssassin/Logger/Stderr.pm` -> **100.0%** Exposure
- `lib/Mail/SpamAssassin/Reporter.pm` -> **100.0%** Exposure
- `lib/Mail/SpamAssassin/Logger/Syslog.pm` -> **99.999%** Exposure
- `lib/Mail/SpamAssassin/PerMsgLearner.pm` -> **99.9977%** Exposure
- `lib/Mail/SpamAssassin/Locales.pm` -> **99.9905%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `contrib/mbox-to-check` -> **100.0%** Exposure
- `lib/Mail/SpamAssassin/AICache.pm` -> **100.0%** Exposure
- `lib/Mail/SpamAssassin/AsyncLoop.pm` -> **100.0%** Exposure
- `lib/Mail/SpamAssassin/Bayes/CombineChi.pm` -> **100.0%** Exposure
- `lib/Mail/SpamAssassin/Conf/Parser.pm` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lib/Mail/SpamAssassin/BayesStore/DBM.pm` -> **27** Orphaned Functions | **0** Duplicates
- `lib/Mail/SpamAssassin/Plugin/HashBL.pm` -> **18** Orphaned Functions | **0** Duplicates
- `lib/Mail/SpamAssassin/Plugin/PDFInfo.pm` -> **18** Orphaned Functions | **0** Duplicates
- `lib/Mail/SpamAssassin/Dns.pm` -> **17** Orphaned Functions | **0** Duplicates
- `lib/Mail/SpamAssassin/Util.pm` -> **16** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `73` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2735` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/Mail/SpamAssassin/Conf.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.922)
- **Top Global Matches:** file_cluster_15: 8.922, file_cluster_4: 8.997, file_cluster_11: 9.919
- **Magnitude:** 22397.66 | **LOC:** 5717 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **10**; blast radius 4.427; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.7%), Complexity Load (formerly Cognitive Load) (56.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_default_commands` **(Many-Argument Workhorses)** (Impact: 20981.6)
    * *Intent:* # set to "1" by the test suite code, to record regression tests # $Mail::SpamAssassin::Conf::COLLECT...
  * `clone` **(Many-Argument Workhorses)** (Impact: 57.9)
    * *Intent:* ###########################################################################
  * `trim_rules` **(Compute Cores)** (Impact: 26.1)
    * *Intent:* # trim_rules ($regexp) # # Remove all rules that don't match the given regexp (or are sub-rules of #...
  * `is_rule_active` **(Many-Argument Workhorses)** (Impact: 23.8)
  * `set_ports_range` **(Compute Cores)** (Impact: 20.9)
    * *Intent:* ########################################################################### # treats a bitset argume...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 292 instances
* *Memory Alloc (weighted view):* 21
* *State Mutation (weighted view):* 971
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1367`, `structural_boundaries: 733`, `args: 101`, `func_start: 62`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 387`, `dead_code: 2`, `planned_debt: 5`, `fragile_debt: 12`
* *Architecture:* `io: 35`, `api: 65`, `import: 82`
* *Defense:* `safety: 9`, `doc: 136`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.427
  * `Choke Point (Betweenness):` 0.000775 | `Ripple Effect (Closeness):` 0.094655
  * `Imports (Out-Degree: 5):` File::Spec, HTML::Parser, Mail::SpamAssassin::Conf::Parser, Mail::SpamAssassin::Constants, Mail::SpamAssassin::Logger, Mail::SpamAssassin::NetSet, Mail::SpamAssassin::Util, re...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `spamd-apache2/t/certs/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/data/etc/testhost.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mail/SpamAssassin/Plugin/Check.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.692)
- **Top Global Matches:** file_cluster_8: 6.692, file_cluster_6: 12.888, file_cluster_4: 21.392
- **Magnitude:** 4578.02 | **LOC:** 1444 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.629; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `begin_evalstr_chunk` **(Many-Argument Workhorses)** (Impact: 2832.3)
  * `check_main` **(Many-Argument Workhorses)** (Impact: 189.3)
    * *Intent:* ###########################################################################
  * `do_head_tests` **(Many-Argument Workhorses)** (Impact: 179.7)
    * *Intent:* ###########################################################################
  * `run_eval_tests` **(Many-Argument Workhorses)** (Impact: 171.9)
  * `do_body_tests` **(Many-Argument Workhorses)** (Impact: 100.7)
    * *Intent:* ###########################################################################
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 155 instances
* *Concurrency (weighted view):* 12
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 486
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 408`, `structural_boundaries: 342`, `args: 47`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 176`, `planned_debt: 1`, `fragile_debt: 6`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 36`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 4`, `doc: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Mail::SpamAssassin::Constants, Mail::SpamAssassin::Logger, Mail::SpamAssassin::Plugin, Mail::SpamAssassin::Timeout, Mail::SpamAssassin::Util, Time::HiRes, eval, hit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mail/SpamAssassin/Plugin/Bayes.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.089)
- **Top Global Matches:** file_cluster_8: 7.089, file_cluster_6: 14.486, file_cluster_4: 22.992
- **Magnitude:** 4340.02 | **LOC:** 1853 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.763; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scan` **(Many-Argument Workhorses)** (Impact: 2782.9)
    * *Intent:* ###########################################################################
  * `new` **(Compute Cores)** (Impact: 122.2)
    * *Intent:* ###########################################################################
  * `_tokenize_headers` **(Compute Cores)** (Impact: 114.7)
  * `tokenize` **(Many-Argument Workhorses)** (Impact: 96.2)
    * *Intent:* ########################################################################### # The calling functions ...
  * `_tokenize_line` **(I/O & Config Routines)** (Impact: 84.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 137 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 421
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 668`, `structural_boundaries: 371`, `args: 43`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 147`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 6`
* *Architecture:* `api: 25`, `import: 35`
* *Defense:* `safety: 4`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.001471
  * `Imports (Out-Degree: 5):` Digest::SHA, Mail::SpamAssassin::Bayes::CombineChi, Mail::SpamAssassin::Logger, Mail::SpamAssassin::PerMsgStatus, Mail::SpamAssassin::Plugin, Mail::SpamAssassin::Util, bayes, constant...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/Mail/SpamAssassin/Plugin/TxRep.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.08)
- **Top Global Matches:** file_cluster_6: 7.08, file_cluster_8: 11.52, file_cluster_4: 14.116
- **Magnitude:** 3646.08 | **LOC:** 2193 | **CtrlFlow:** 43.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.629; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.4%), Guard Balance (formerly Safety Score) (66.1%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_config` **(Many-Argument Workhorses)** (Impact: 2226.0)
    * *Intent:* ###########################################################################
  * `check_reputation` **(Many-Argument Workhorses)** (Impact: 241.2)
    * *Intent:* ###########################################################################
  * `check_senders_reputation` **(Compute Cores)** (Impact: 240.8)
    * *Intent:* ###########################################################################
  * `_fn_envelope` **(Many-Argument Workhorses)** (Impact: 58.0)
    * *Intent:* ###########################################################################
  * `ip_to_awl_key` **(Compute Cores)** (Impact: 47.3)
    * *Intent:* ###########################################################################
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 13 instances
* *Amplified Cascading Flux:* 176 instances
* *Memory Alloc (weighted view):* 24
* *State Mutation (weighted view):* 536
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 685`, `structural_boundaries: 327`, `args: 47`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 184`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 15`, `unreferenced_by_name: 7`
* *Architecture:* `io: 5`, `api: 27`, `import: 37`
* *Defense:* `safety: 4`, `doc: 36`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Mail::SpamAssassin::Logger, Mail::SpamAssassin::Plugin, Mail::SpamAssassin::Plugin::Bayes, Mail::SpamAssassin::Util, NetAddr::IP, message, more, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mail/SpamAssassin/PerMsgStatus.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.371)
- **Top Global Matches:** file_cluster_6: 9.371, file_cluster_8: 9.493, file_cluster_4: 17.067
- **Magnitude:** 3103.06 | **LOC:** 3742 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **16**; blast radius 4.798; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (81.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.3%)
- **Documentation Coverage:** 45.8904% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get` **(Many-Argument Workhorses)** (Impact: 179.6)
    * *Intent:* # only uses two arguments, ignores $defval
  * `_process_text_uri_list` **(Compute Cores)** (Impact: 112.6)
  * `add_uri_detail_list` **(Many-Argument Workhorses)** (Impact: 103.1)
  * `rewrite_report_safe` **(Compute Cores)** (Impact: 102.0)
    * *Intent:* # rewrite the message in report_safe mode # should not be called directly, use rewrite_mail instead ...
  * `get_envelope_from` **(Compute Cores)** (Impact: 101.9)
    * *Intent:* ########################################################################### # helper for get()
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 397 instances
* *Memory Alloc (weighted view):* 29
* *State Mutation (weighted view):* 1206
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1162`, `structural_boundaries: 755`, `args: 116`, `func_start: 80`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 412`, `dead_code: 3`, `planned_debt: 8`, `fragile_debt: 33`, `unreferenced_by_name: 13`
* *Architecture:* `io: 6`, `api: 65`, `concurrency: 2`, `import: 28`
* *Defense:* `safety: 4`, `doc: 42`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.798
  * `Choke Point (Betweenness):` 0.001167 | `Ripple Effect (Closeness):` 0.091793
  * `Imports (Out-Degree: 7):` Encode, Errno, Mail::SpamAssassin::AsyncLoop, Mail::SpamAssassin::Conf, Mail::SpamAssassin::Constants, Mail::SpamAssassin::Logger, Mail::SpamAssassin::Timeout, Mail::SpamAssassin::Util...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `spamc/libspamc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.005)
- **Top Global Matches:** file_cluster_8: 9.005, file_cluster_6: 9.309, file_cluster_4: 17.375
- **Magnitude:** 2955.04 | **LOC:** 2465 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **24**; blast radius 0.696; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_opensocket` **(Many-Argument Workhorses)** (Impact: 878.1)
    * *Intent:* /* * opensocket() * * Given a socket family (PF_INET or PF_INET6 or PF_UNIX), try to * create this s...
  * `message_filter` **(Many-Argument Workhorses)** (Impact: 177.5)
  * `message_tell` **(Many-Argument Workhorses)** (Impact: 133.8)
  * `transport_setup` **(Many-Argument Workhorses)** (Impact: 102.6)
    * *Intent:* * transport_setup() * * Given a "transport" object that says how we're to connect to the * spam daem...
  * `_opensocket` **(Many-Argument Workhorses)** (Impact: 79.5)
    * *Intent:* #else
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 16 instances
* *Amplified Cascading Flux:* 331 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 1031
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 396`, `structural_boundaries: 208`, `args: 51`, `func_start: 37`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 1`, `state_mutation: 369`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 7`, `unreferenced_by_name: 10`
* *Architecture:* `io: 12`, `api: 18`, `import: 24`
* *Defense:* `safety: 42`, `immutability_locks: 18`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001471
  * `Imports (Out-Degree: 4):` inet.h, assert.h, config.h, errno.h, io.h, libspamc.h, in.h, tcp.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/Mail/SpamAssassin/HTML.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.991)
- **Top Global Matches:** file_cluster_8: 7.991, file_cluster_3: 17.568, file_cluster_6: 19.571
- **Magnitude:** 2910.26 | **LOC:** 1193 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 2.1; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_css_background` **(Many-Argument Workhorses)** (Impact: 974.0)
    * *Intent:* # Parses a CSS background property value. # Returns an arrayref of layers, each layer is an arrayref...
  * `html_tests` **(Many-Argument Workhorses)** (Impact: 658.9)
  * `text_style` **(Many-Argument Workhorses)** (Impact: 121.7)
  * `html_uri` **(Many-Argument Workhorses)** (Impact: 88.1)
  * `html_tag` **(Many-Argument Workhorses)** (Impact: 51.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 189 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 576
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 401`, `structural_boundaries: 203`, `args: 30`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `state_mutation: 198`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 6`, `unreferenced_by_name: 4`
* *Architecture:* `api: 26`, `import: 9`
* *Defense:* `safety: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.1
  * `Choke Point (Betweenness):` 0.000522 | `Ripple Effect (Closeness):` 0.053526
  * `Imports (Out-Degree: 4):` HTML::Parser, Mail::SpamAssassin::Constants, Mail::SpamAssassin::HTML::Color, Mail::SpamAssassin::Logger, Mail::SpamAssassin::Util, constant, re, strict...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/Mail/SpamAssassin/Util.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.72)
- **Top Global Matches:** file_cluster_8: 7.72, file_cluster_6: 15.177, file_cluster_3: 23.398
- **Magnitude:** 2897.76 | **LOC:** 2832 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **74** in-repo importer(s); it depends on **27**; blast radius 25.803; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.8%), Complexity Load (formerly Cognitive Load) (80.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 78.6885% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `uri_list_canonicalize` **(Many-Argument Workhorses)** (Impact: 519.3)
    * *Intent:* ########################################################################### ## ## DEPRECATED FUNCTIO...
  * `parse_rfc822_date` **(Compute Cores)** (Impact: 107.9)
  * `compile_regexp` **(Many-Argument Workhorses)** (Impact: 99.2)
    * *Intent:* # returns ($compiled_re, $error) # if any errors, $compiled_re = undef, $error has string # args: # ...
  * `_parse_header_addresses` **(Compute Cores)** (Impact: 97.4)
    * *Intent:* # # v0.1, improved internal parser, no support for comments in strange # places or nested comments, ...
  * `helper_app_pipe_open_unix` **(Many-Argument Workhorses)** (Impact: 72.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 326 instances
* *High Risk Execution (weighted view):* 4
* *Concurrency (weighted view):* 6
* *Memory Alloc (weighted view):* 31
* *State Mutation (weighted view):* 981
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1021`, `structural_boundaries: 576`, `args: 48`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 5`, `state_mutation: 329`, `dead_code: 11`, `planned_debt: 3`, `fragile_debt: 43`, `unreferenced_by_name: 16`
* *Architecture:* `io: 15`, `api: 64`, `concurrency: 1`, `import: 36`
* *Defense:* `safety: 15`, `doc: 18`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.803
  * `Choke Point (Betweenness):` 0.002825 | `Ripple Effect (Closeness):` 0.143098
  * `Imports (Out-Degree: 3):` Config, Email::Address::XS, Encode, Errno, Exporter, Fcntl, File::Basename, File::Spec...
  * `Imported By (In-Degree: 74):` (Excluded from Brief to save tokens)

### `masses/mass-check` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.001)
- **Top Global Matches:** file_cluster_8: 7.001, file_cluster_6: 13.711, file_cluster_4: 22.158
- **Magnitude:** 2349.06 | **LOC:** 2679 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.629; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_messages` **(Many-Argument Workhorses)** (Impact: 243.6)
    * *Intent:* # Input: # - Number of messages to generate (scalar) # - Hash of Arrays of outstanding requests (ref...
  * `wanted` **(Many-Argument Workhorses)** (Impact: 181.0)
  * `client_mode` **(I/O & Config Routines)** (Impact: 148.3)
    * *Intent:* # this is the function that implements client mode. generally, in a loop: # make a request of the se...
  * `usage` **(Compute Cores)** (Impact: 75.4)
  * `http_make_request` **(Many-Argument Workhorses)** (Impact: 59.6)
    * *Intent:* # the client needs to make a request to the server on a given socket.
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 22 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 323 instances
* *Concurrency (weighted view):* 36
* *Memory Alloc (weighted view):* 9
* *State Mutation (weighted view):* 1008
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 762`, `structural_boundaries: 434`, `args: 25`, `func_start: 38`
* *Risk/State:* `high_risk_execution: 15`, `state_mutation: 362`, `dead_code: 5`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `io: 80`, `api: 39`, `concurrency: 6`, `import: 39`
* *Defense:* `safety: 7`, `cleanup: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Config, Fcntl, File::Copy, File::Spec, FindBin, Getopt::Long, IO::Select, IO::Socket...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mail/SpamAssassin/Message/Metadata/Received.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.477)
- **Top Global Matches:** file_cluster_3: 7.477, file_cluster_8: 20.866, file_cluster_6: 33.644
- **Magnitude:** 2250.44 | **LOC:** 1466 | **CtrlFlow:** 78.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.807; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Complexity Load (formerly Cognitive Load) (96.9%), Guard Balance (formerly Safety Score) (95.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_received_line` **(Many-Argument Workhorses)** (Impact: 880.1)
    * *Intent:* # returns undef if the header just couldn't be parsed # returns 0 if the header was specifically ski...
  * `parse_received_headers` **(Many-Argument Workhorses)** (Impact: 186.2)
    * *Intent:* # ---------------------------------------------------------------------------
  * `found_pop_fetcher_sig` **(Compute Cores)** (Impact: 7.6)
    * *Intent:* # restart the parse if we find a fetchmail marker or similar. # spamcop does this, and it's a great ...
  * `make_relay_as_string` **(Compute Cores)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 378 instances
* *State Mutation (weighted view):* 1152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 568`, `structural_boundaries: 184`, `args: 5`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `state_mutation: 396`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 29`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 4`, `import: 8`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.807
  * `Choke Point (Betweenness):` 0.000371 | `Ripple Effect (Closeness):` 0.052534
  * `Imports (Out-Degree: 3):` Mail::SpamAssassin::Constants, Mail::SpamAssassin::Dns, Mail::SpamAssassin::PerMsgStatus, longer, re, strict, warnings
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `masses/rule-qa/automc/ruleqa.cgi` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.551)
- **Top Global Matches:** file_cluster_6: 6.551, file_cluster_4: 11.969, file_cluster_8: 13.909
- **Magnitude:** 1971.72 | **LOC:** 2189 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.629; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.1%), Guard Balance (formerly Safety Score) (71.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `show_default_view` **(Compute Cores)** (Impact: 124.6)
  * `read_freqs_file` **(Many-Argument Workhorses)** (Impact: 116.7)
  * `get_freqs_for_rule` **(Many-Argument Workhorses)** (Impact: 72.6)
  * `generate_scoremap_chart` **(Many-Argument Workhorses)** (Impact: 61.0)
  * `assemble_url` **(Compute Cores)** (Impact: 49.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 233 instances
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 733
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 529`, `structural_boundaries: 496`, `args: 64`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 267`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 25`, `api: 65`, `import: 18`
* *Defense:* `safety: 12`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CGI, CGI::Carp, Compress::LZ4, Date::Manip, POSIX, Storable, Time::Local, URI::Escape...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mail/SpamAssassin/BayesStore/SQL.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.333)
- **Top Global Matches:** file_cluster_8: 7.333, file_cluster_6: 12.989, file_cluster_4: 21.361
- **Magnitude:** 1947.76 | **LOC:** 2370 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 1.164; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.0%), Complexity Load (formerly Cognitive Load) (53.2%)
- **Documentation Coverage:** 2.5974% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_put_token` **(Many-Argument Workhorses)** (Impact: 222.3)
  * `_put_tokens` **(Many-Argument Workhorses)** (Impact: 219.8)
  * `restore_database` **(Many-Argument Workhorses)** (Impact: 186.2)
  * `token_expiration` **(Many-Argument Workhorses)** (Impact: 115.6)
  * `_initialize_db` **(Compute Cores)** (Impact: 59.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 135 instances
* *Memory Alloc (weighted view):* 29
* *State Mutation (weighted view):* 407
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 767`, `structural_boundaries: 571`, `args: 41`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `state_mutation: 137`, `dead_code: 1`, `fragile_debt: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 7`, `api: 35`, `import: 15`
* *Defense:* `safety: 3`, `doc: 43`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.164
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.002941
  * `Imports (Out-Degree: 2):` DBI, Digest::SHA, Errno, Mail::SpamAssassin::BayesStore, Mail::SpamAssassin::Logger, constant, delta, re...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Mail/SpamAssassin/Conf/Parser.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.659)
- **Top Global Matches:** file_cluster_6: 6.659, file_cluster_4: 10.732, file_cluster_8: 15.627
- **Magnitude:** 1915.26 | **LOC:** 1704 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 2.8; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.4%), Debt Markers (formerly Tech Debt) (83.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 252.8)
    * *Intent:* ###########################################################################
  * `add_test` **(Many-Argument Workhorses)** (Impact: 182.0)
    * *Intent:* ###########################################################################
  * `handle_conditional` **(Many-Argument Workhorses)** (Impact: 98.4)
  * `finish_parsing` **(Many-Argument Workhorses)** (Impact: 94.6)
    * *Intent:* ###########################################################################
  * `is_meta_valid` **(Compute Cores)** (Impact: 66.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 203 instances
* *State Mutation (weighted view):* 615
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 591`, `structural_boundaries: 355`, `args: 46`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 209`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 13`, `unreferenced_by_name: 14`
* *Architecture:* `io: 1`, `api: 50`, `import: 19`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.8
  * `Choke Point (Betweenness):` 0.000227 | `Ripple Effect (Closeness):` 0.069444
  * `Imports (Out-Degree: 5):` Mail::SpamAssassin::Conf, Mail::SpamAssassin::Constants, Mail::SpamAssassin::Logger, Mail::SpamAssassin::NetSet, Mail::SpamAssassin::Util, argument, compile_regexp, description...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Mail/SpamAssassin/Plugin/NeuralNetwork.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.454)
- **Top Global Matches:** file_cluster_8: 6.454, file_cluster_6: 16.341, file_cluster_3: 21.032
- **Magnitude:** 1854.1 | **LOC:** 1586 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.629; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_text_to_features` **(Many-Argument Workhorses)** (Impact: 349.8)
    * *Intent:* # Converts a list of raw text strings into a list of # numerical feature vectors (dense arrays), sui...
  * `set_config` **(Many-Argument Workhorses)** (Impact: 237.8)
  * `learn_message` **(Many-Argument Workhorses)** (Impact: 122.4)
  * `_retrain_from_vocabulary` **(Many-Argument Workhorses)** (Impact: 79.8)
    * *Intent:* # Create a baseline model from vocabulary statistics when vocab size has changed.
  * `_check_neuralnetwork` **(Many-Argument Workhorses)** (Impact: 75.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 166 instances
* *Memory Alloc (weighted view):* 20
* *State Mutation (weighted view):* 503
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 573`, `structural_boundaries: 412`, `args: 30`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `state_mutation: 171`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `io: 3`, `api: 12`, `import: 10`
* *Defense:* `safety: 31`, `doc: 2`, `sync_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` AI::FANN, DBI, File::Spec, Mail::SpamAssassin, Mail::SpamAssassin::Plugin, Mail::SpamAssassin::Util, Storable, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mail/SpamAssassin/Plugin/DKIM.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.157)
- **Top Global Matches:** file_cluster_8: 10.157, file_cluster_3: 15.354, file_cluster_6: 22.117
- **Magnitude:** 1658.58 | **LOC:** 1448 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.629; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_config` **(Many-Argument Workhorses)** (Impact: 449.1)
    * *Intent:* ###########################################################################
  * `_check_valid_signature` **(Many-Argument Workhorses)** (Impact: 143.3)
  * `_check_dkim_adsp` **(Many-Argument Workhorses)** (Impact: 122.2)
  * `_wlcheck_list` **(Many-Argument Workhorses)** (Impact: 109.1)
  * `_check_dkim_signed_by` **(Many-Argument Workhorses)** (Impact: 90.1)
    * *Intent:* # ---------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 112 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 349
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 520`, `structural_boundaries: 267`, `args: 30`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 125`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `api: 15`, `import: 35`
* *Defense:* `safety: 9`, `doc: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Mail::DKIM::AuthorDomainPolicy, Mail::DKIM::DkimPolicy, Mail::DKIM::Verifier, Mail::SpamAssassin::Logger, Mail::SpamAssassin::Plugin, Mail::SpamAssassin::Timeout, Mail::SpamAssassin::Util, author...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mail/SpamAssassin.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.407)
- **Top Global Matches:** file_cluster_6: 6.407, file_cluster_4: 11.766, file_cluster_8: 14.009
- **Magnitude:** 1608.28 | **LOC:** 2563 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **71** in-repo importer(s); it depends on **36**; blast radius 42.047; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.3%), Complexity Load (formerly Cognitive Load) (62.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 135.5)
    * *Intent:* ########################################################################### # non-public methods.
  * `create_default_prefs` **(Many-Argument Workhorses)** (Impact: 79.1)
  * `remove_spamassassin_markup` **(Compute Cores)** (Impact: 47.7)
  * `compile_now` **(Many-Argument Workhorses)** (Impact: 42.2)
  * `get_and_create_userstate_dir` **(Compute Cores)** (Impact: 42.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 13 instances
* *Amplified Cascading Flux:* 176 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 547
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 649`, `structural_boundaries: 465`, `args: 64`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 195`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 10`
* *Architecture:* `io: 18`, `api: 59`, `concurrency: 2`, `import: 60`
* *Defense:* `safety: 6`, `doc: 33`, `cleanup: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 42.047
  * `Choke Point (Betweenness):` 0.010828 | `Ripple Effect (Closeness):` 0.137097
  * `Imports (Out-Degree: 19):` Config, Cwd, Errno, File::Basename, File::Find, File::Path, File::Spec, Mail::SpamAssassin::Bayes...
  * `Imported By (In-Degree: 71):` (Excluded from Brief to save tokens)

### `lib/Mail/SpamAssassin/Plugin/DCC.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 12.324)
- **Top Global Matches:** file_cluster_8: 12.324, file_cluster_3: 12.775, file_cluster_6: 24.749
- **Magnitude:** 1588.62 | **LOC:** 1326 | **CtrlFlow:** 42.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.629; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.7%), Guard Balance (formerly Safety Score) (69.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_config` **(Many-Argument Workhorses)** (Impact: 436.8)
  * `ask_dcc` **(Many-Argument Workhorses)** (Impact: 141.6)
  * `_check_async` **(Many-Argument Workhorses)** (Impact: 79.7)
  * `dccsight_learn` **(Many-Argument Workhorses)** (Impact: 70.2)
  * `check_dcc_reputation_range` **(Many-Argument Workhorses)** (Impact: 60.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Cascading Flux:* 139 instances
* *Memory Alloc (weighted view):* 21
* *State Mutation (weighted view):* 418
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 416`, `structural_boundaries: 322`, `args: 28`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 140`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 5`, `unreferenced_by_name: 5`
* *Architecture:* `io: 20`, `api: 21`, `concurrency: 1`, `import: 25`
* *Defense:* `safety: 6`, `doc: 11`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Errno, IO::Select, IO::Socket, IO::Socket::INET, IO::Socket::INET6, IO::Socket::IP, Mail::SpamAssassin::Logger, Mail::SpamAssassin::Plugin...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/garescorer.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.4)
- **Top Global Matches:** file_cluster_8: 5.4, file_cluster_6: 13.252, file_cluster_4: 22.033
- **Magnitude:** 1574.26 | **LOC:** 1314 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.629; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.0%), Guard Balance (formerly Safety Score) (83.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 64.7059% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `adapt` **(Many-Argument Workhorses)** (Impact: 237.4)
    * *Intent:* #ifdef LAMARCK
  * `myMutation` **(Many-Argument Workhorses)** (Impact: 174.7)
    * *Intent:* * This mutation function tosses a weighted coin for each allele. * If the allele is to be mutated, t...
  * `Crossover` **(Many-Argument Workhorses)** (Impact: 110.9)
    * *Intent:* /***************************************************************************** * Crossover implement...
  * `main` **(Many-Argument Workhorses)** (Impact: 47.1)
  * `showSummary` **(Compute Cores)** (Impact: 40.6)
    * *Intent:* #endif
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 266 instances
* *State Mutation (weighted view):* 819
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 66`, `args: 42`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 3`, `state_mutation: 287`, `dead_code: 2`, `fragile_debt: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 34`, `import: 6`
* *Defense:* `doc: 6`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` math.h, pgapack.h, time.h, scores.h, tests.h, unistd.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mail/SpamAssassin/Plugin/ASN.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.302)
- **Top Global Matches:** file_cluster_8: 7.302, file_cluster_6: 14.787, file_cluster_4: 23.184
- **Magnitude:** 1565.58 | **LOC:** 630 | **CtrlFlow:** 48.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.629; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_config` **(Many-Argument Workhorses)** (Impact: 1049.8)
    * *Intent:* ###########################################################################
  * `process_dns_result` **(Many-Argument Workhorses)** (Impact: 177.0)
    * *Intent:* # # TXT-RR format of response: # The latter two fields are combined to create a CIDR. # <character-s...
  * `extract_metadata` **(Many-Argument Workhorses)** (Impact: 135.9)
    * *Intent:* # ---------------------------------------------------------------------------
  * `check_asn` **(Many-Argument Workhorses)** (Impact: 22.4)
  * `_check_asn` **(Many-Argument Workhorses)** (Impact: 10.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 120`, `args: 12`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 48`, `unreferenced_by_name: 6`
* *Architecture:* `io: 3`, `api: 10`, `concurrency: 1`, `import: 20`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Mail::SpamAssassin::Constants, Mail::SpamAssassin::Logger, Mail::SpamAssassin::Plugin, Mail::SpamAssassin::Util, first, re, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mail/SpamAssassin/BayesStore/DBM.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.462)
- **Top Global Matches:** file_cluster_6: 6.462, file_cluster_4: 12.069, file_cluster_8: 13.63
- **Magnitude:** 1555.98 | **LOC:** 1979 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 0.897; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.0%), Debt Markers (formerly Tech Debt) (88.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `restore_database` **(Many-Argument Workhorses)** (Impact: 178.7)
  * `_sync_journal_trapped` **(Many-Argument Workhorses)** (Impact: 97.6)
  * `_upgrade_db` **(Compute Cores)** (Impact: 84.6)
    * *Intent:* # Check to see if we need to upgrade the DB, and do so if necessary
  * `token_expiration` **(Many-Argument Workhorses)** (Impact: 67.1)
    * *Intent:* ###########################################################################
  * `tie_db_writable` **(Compute Cores)** (Impact: 55.2)
    * *Intent:* # tie() to the databases, read-write and locked. Any callers of # this should ensure they call untie...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 143 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 482
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 461`, `structural_boundaries: 470`, `args: 51`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 196`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 8`, `unreferenced_by_name: 27`
* *Architecture:* `io: 14`, `api: 46`, `import: 26`
* *Defense:* `safety: 6`, `sync_locks: 2`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.897
  * `Choke Point (Betweenness):` 7.6e-05 | `Ripple Effect (Closeness):` 0.001471
  * `Imports (Out-Degree: 4):` DB_File, Digest::SHA, Errno, Fcntl, File::Basename, File::Copy, File::Path, File::Spec...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/Mail/SpamAssassin/ArchiveIterator.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.57)
- **Top Global Matches:** file_cluster_3: 11.57, file_cluster_8: 15.034, file_cluster_6: 27.355
- **Magnitude:** 1411.58 | **LOC:** 1297 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 2.101; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.1%), Guard Balance (formerly Safety Score) (63.8%)
- **Documentation Coverage:** 74.0741% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_scan_mbx` **(Many-Argument Workhorses)** (Impact: 214.7)
  * `_scan_mailbox` **(Many-Argument Workhorses)** (Impact: 169.5)
  * `_mail_open` **(Many-Argument Workhorses)** (Impact: 165.8)
  * `_scan_directory` **(Many-Argument Workhorses)** (Impact: 95.4)
    * *Intent:* ############################################################################
  * `_scan_targets` **(Many-Argument Workhorses)** (Impact: 81.1)
    * *Intent:* ############################################################################ ## FUNCTIONS BELOW THIS...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 91 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 278
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 533`, `structural_boundaries: 267`, `args: 25`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `state_mutation: 96`, `fragile_debt: 10`
* *Architecture:* `io: 18`, `api: 5`, `import: 38`
* *Defense:* `safety: 4`, `doc: 5`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.101
  * `Choke Point (Betweenness):` 0.000176 | `Ripple Effect (Closeness):` 0.005882
  * `Imports (Out-Degree: 4):` Errno, IO::Zlib, Mail::SpamAssassin::AICache, Mail::SpamAssassin::Constants, Mail::SpamAssassin::Logger, Mail::SpamAssassin::Util, access, constant...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/Mail/SpamAssassin/Plugin/HashBL.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.059)
- **Top Global Matches:** file_cluster_6: 8.059, file_cluster_8: 10.785, file_cluster_4: 15.309
- **Magnitude:** 1408.34 | **LOC:** 1163 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.629; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.5%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (70.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_config` **(Many-Argument Workhorses)** (Impact: 183.7)
  * `check_hashbl_bodyre` **(Many-Argument Workhorses)** (Impact: 161.7)
  * `check_hashbl_emails` **(Many-Argument Workhorses)** (Impact: 155.4)
  * `check_hashbl_uris` **(Many-Argument Workhorses)** (Impact: 114.5)
  * `check_hashbl_attachments` **(Many-Argument Workhorses)** (Impact: 112.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 274
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 418`, `structural_boundaries: 269`, `args: 21`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 92`, `fragile_debt: 1`, `unreferenced_by_name: 18`
* *Architecture:* `io: 1`, `api: 26`, `concurrency: 1`, `import: 12`
* *Defense:* `safety: 2`, `doc: 1`, `test: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Digest::MD5, Digest::SHA, Mail::SpamAssassin::Constants, Mail::SpamAssassin::Plugin, Mail::SpamAssassin::Util, emails, matches, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mail/SpamAssassin/Plugin/BodyRuleBaseExtractor.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.475)
- **Top Global Matches:** file_cluster_8: 8.475, file_cluster_3: 17.861, file_cluster_6: 19.741
- **Magnitude:** 1318.14 | **LOC:** 1153 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.719; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.4%)
- **Documentation Coverage:** 93.5484% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extract_hints` **(Many-Argument Workhorses)** (Impact: 261.5)
  * `extract_set_pri` **(Many-Argument Workhorses)** (Impact: 196.2)
    * *Intent:* ###########################################################################
  * `unroll_branches` **(Many-Argument Workhorses)** (Impact: 153.1)
    * *Intent:* ###########################################################################
  * `simplify_and_qr_regexp` **(Compute Cores)** (Impact: 83.6)
    * *Intent:* ########################################################################### # TODO: # => should extr...
  * `test_split_alt` **(Compute Cores)** (Impact: 35.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 13 instances
* *Amplified Cascading Flux:* 162 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 490
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 382`, `structural_boundaries: 206`, `args: 16`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 166`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 5`, `unreferenced_by_name: 2`
* *Architecture:* `io: 6`, `api: 15`, `import: 24`
* *Defense:* `safety: 3`, `doc: 2`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.719
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.001471
  * `Imports (Out-Degree: 5):` Config, Data::Dumper, Errno, Mail::SpamAssassin::Logger, Mail::SpamAssassin::Plugin, Mail::SpamAssassin::Util, Mail::SpamAssassin::Util::Progress, bases...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `t/check_implemented.t` (PERL) | Magnitude: 24.8 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 13, import: 9, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `masses/rule-qa/get-rulemetadata-for-revision` (PERL) | Magnitude: 72.82 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 28, branch: 26, state_mutation: 12
- `t/line_endings.t` (PERL) | Magnitude: 103.3 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 48, indent_spaces: 39, state_mutation: 26, structural_boundaries: 23
- `t/bayesdbm.t` (PERL) | Magnitude: 96.12 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: test: 48, structural_boundaries: 43, indent_spaces: 40, state_mutation: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `t/bayesbdb.t` (PERL) | Magnitude: 95.0 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 44, test: 42, indent_spaces: 41, state_mutation: 35
- `spamd-apache2/t/30run.t` (PERL) | Magnitude: 19.74 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 13, import: 8, indent_tabs: 8, test: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/spamc_optL.t` (PERL) | Magnitude: 37.82 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 10, test: 10, bitwise_ops: 9, branch: 6
- `t/regexp_named_capture.t` (PERL) | Magnitude: 24.0 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 27, branch: 16, regex_execution: 8, decorators: 7
- `t/spamd_parallel.t` (PERL) | Magnitude: 18.54 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: test: 11, bitwise_ops: 10, indent_spaces: 5, branch: 4
- `t/spamd_allow_user_rules.t` (PERL) | Magnitude: 21.86 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 19, branch: 8, decorators: 5, structural_boundaries: 4
- `t/razor2.t` (PERL) | Magnitude: 25.72 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 9, import: 8, structural_boundaries: 7, core_var_decl: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `lib/Mail/SpamAssassin/Conf.pm` (PERL) | Magnitude: 22397.66 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 2061, branch: 1367, structural_boundaries: 733, core_var_decl: 515
- `t/sha1.t` (PERL) | Magnitude: 24.0 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 17, safety: 17, branch: 16, test: 16
- `t/cidrs.t` (PERL) | Magnitude: 22.52 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 131, indent_spaces: 30, structural_boundaries: 24, decorators: 17
- `t/ip_addrs.t` (PERL) | Magnitude: 19.22 | Delta: **0.162** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 270, decorators: 51, indent_spaces: 35, structural_boundaries: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `t/spamd_maxchildren.t` (PERL) | Magnitude: 18.58 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: test: 13, indent_spaces: 5, branch: 4, structural_boundaries: 4
- `t/basic_lint.t` (PERL) | Magnitude: 36.52 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, branch: 8, structural_boundaries: 7, state_mutation: 7
- `t/plugin.t` (PERL) | Magnitude: 17.48 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 4, import: 4, branch: 3
- `t/spamd_hup.t` (PERL) | Magnitude: 27.86 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 26, test: 10, branch: 8, structural_boundaries: 7
- `t/welcomelist_to.t` (PERL) | Magnitude: 18.3 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 4, import: 4, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `masses/rule-qa/reports-from-logs` (PERL) | Magnitude: 631.3 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 424, branch: 196, structural_boundaries: 179, state_mutation: 76
- `lib/Mail/SpamAssassin/PerMsgStatus.pm` (PERL) | Magnitude: 3103.06 | Delta: **0.122** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1821, branch: 1162, structural_boundaries: 755, state_mutation: 412

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `lib/Mail/SpamAssassin/Plugin/NeuralNetwork.pm` -> Churn: **100.0%** | Cog Load: 85.2325% | Debt: 13.6433%
- `lib/Mail/SpamAssassin/Plugin/DMARC.pm` -> Churn: **63.99%** | Cog Load: 88.4032% | Debt: 19.3921%
- `lib/Mail/SpamAssassin/Plugin/Redirectors.pm` -> Churn: **52.17%** | Cog Load: 72.2192% | Debt: 28.106%
- `lib/Mail/SpamAssassin/Conf.pm` -> Churn: **51.31%** | Cog Load: 56.7821% | Debt: 11.692%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/Mail/SpamAssassin/Plugin/Check.pm` -> **Giovanni Bechis** (100.0% isolated ownership) | Magnitude: 4578.02
- `lib/Mail/SpamAssassin/Plugin/TxRep.pm` -> **Giovanni Bechis** (100.0% isolated ownership) | Magnitude: 3646.08
- `lib/Mail/SpamAssassin/PerMsgStatus.pm` -> **Giovanni Bechis** (100.0% isolated ownership) | Magnitude: 3103.06
- `lib/Mail/SpamAssassin/Util.pm` -> **Giovanni Bechis** (100.0% isolated ownership) | Magnitude: 2897.76
- `lib/Mail/SpamAssassin/Message/Metadata/Received.pm` -> **Giovanni Bechis** (100.0% isolated ownership) | Magnitude: 2250.44

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/Mail/SpamAssassin.pm` -> **Severity: 1.083** (Bridge: 0.0108 * Flux: 99.997%)
- `lib/Mail/SpamAssassin/Util.pm` -> **Severity: 0.282** (Bridge: 0.0028 * Flux: 100.0%)
- `lib/Mail/SpamAssassin/Message.pm` -> **Severity: 0.24** (Bridge: 0.0024 * Flux: 100.0%)
- `lib/Mail/SpamAssassin/Locker/Win32.pm` -> **Severity: 0.147** (Bridge: 0.0019 * Flux: 77.493%)
- `lib/Mail/SpamAssassin/PerMsgStatus.pm` -> **Severity: 0.117** (Bridge: 0.0012 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/Mail/SpamAssassin/Logger.pm` -> **Severity: 12.174** (Embedded: 0.1864 * Error Risk: 65.3292%)
- `lib/Mail/SpamAssassin/Util.pm` -> **Severity: 10.78** (Embedded: 0.1431 * Error Risk: 75.3356%)
- `lib/Mail/SpamAssassin.pm` -> **Severity: 8.948** (Embedded: 0.1371 * Error Risk: 65.269%)
- `lib/Mail/SpamAssassin/Logger/Stderr.pm` -> **Severity: 7.253** (Embedded: 0.113 * Error Risk: 64.2129%)
- `lib/Mail/SpamAssassin/Message.pm` -> **Severity: 6.622** (Embedded: 0.0893 * Error Risk: 74.1684%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/Mail/SpamAssassin/Logger/Stderr.pm` -> **Severity: 18082.4** (Blast Radius: 180.824 * Doc Risk: 100.0%)
- `lib/Mail/SpamAssassin/Logger.pm` -> **Severity: 4235.04** (Blast Radius: 211.752 * Doc Risk: 20.0%)
- `lib/Mail/SpamAssassin.pm` -> **Severity: 2102.35** (Blast Radius: 42.047 * Doc Risk: 50.0%)
- `lib/Mail/SpamAssassin/Util.pm` -> **Severity: 2030.399** (Blast Radius: 25.803 * Doc Risk: 78.6885%)
- `lib/Mail/SpamAssassin/Locker/Win32.pm` -> **Severity: 794.1** (Blast Radius: 7.941 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 2222 literal sites + 78 sites through wrappers = 2300
- **`memory_alloc`:** 942 literal sites + 28 sites through wrappers = 970
- **`panics_and_aborts`:** 1366 literal sites + 24 sites through wrappers = 1390

- `usg` (function, debug_prints, primitive): 43 call sites in 1 files -- `spamc/spamc.c`
- `tstprefs` (function, debug_prints, primitive): 12 call sites in 2 files -- `t/SATest.pm`
- `tstprefs` (function, panics_and_aborts, primitive): 12 call sites in 2 files -- `t/SATest.pm`
- `_use_msg_for_out` (function, memory_alloc, primitive): 10 call sites in 1 files -- `spamc/libspamc.c`
- `die` (function, debug_prints, primitive): 10 call sites in 6 files -- `backend/root/backup/backup_zone`
- `die` (function, panics_and_aborts, primitive): 10 call sites in 6 files -- `backend/root/backup/backup_zone`
- `message_cleanup` (function, memory_alloc, primitive): 10 call sites in 2 files -- `spamc/libspamc.c`
- `runcmd` (function, debug_prints, primitive): 8 call sites in 1 files -- `masses/rule-qa/reports-from-logs`
- `_free_zlib_buffer` (function, memory_alloc, primitive): 5 call sites in 1 files -- `spamc/libspamc.c`
- `dbgprint` (function, debug_prints, primitive): 2 call sites in 1 files -- `t/SATest.pm`
- `print_version` (function, debug_prints, primitive): 2 call sites in 1 files -- `spamc/spamc.c`
- `destroy_weights` (function, memory_alloc, primitive): 1 call sites in 1 files -- `masses/perceptron.c`
*(+5 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 12992 call pairs -- scoped 13.9%, unique 0.2%, ambiguous 3.5%, external 82.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| perl | 11875 | 13.9% | 0.0% | 3.9% | 82.2% |
| c | 513 | 21.6% | 5.3% | 0.0% | 73.1% |
| shell | 425 | 7.5% | 0.0% | 0.0% | 92.5% |
| livecode | 123 | 0.0% | 0.0% | 0.0% | 100.0% |
| javascript | 45 | 8.9% | 0.0% | 0.0% | 91.1% |
| postgresql | 11 | 72.7% | 0.0% | 0.0% | 27.3% |

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
