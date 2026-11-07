# ARCHITECTURAL_BRIEF: perl5
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Perl/perl5.git` |
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
- **Scope:** 4837 analyzed artifact(s), 1041076 LOC.
- **Load-bearing artifact:** `cpan/Test-Simple/lib/Test/More.pm` -- 1282 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `perl.h` -- pulls in 110 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `pod/perlfunc.pod` at magnitude 158989.11 (structural weight, not risk).
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
| Total Artifacts | 6946 |
| Analyzed Artifacts (Scanned) | 4837 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2109 |
| Total LOC | 1041076 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 69.6% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.715 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2688 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.8418 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 230 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 4158 | 780001 | 86.0% |
| C | 232 | 213281 | 4.8% |
| PLAINTEXT | 199 | 0 | 4.1% |
| SHELL | 110 | 35222 | 2.3% |
| YAML | 46 | 1925 | 1.0% |
| XML | 33 | 0 | 0.7% |
| JSON | 20 | 1308 | 0.4% |
| MARKDOWN | 17 | 0 | 0.4% |
| MAKEFILE | 5 | 3088 | 0.1% |
| CPP | 5 | 3921 | 0.1% |
| BATCH | 3 | 53 | 0.1% |
| LIVECODE | 3 | 398 | 0.1% |
| M4 | 2 | 10 | 0.0% |
| REXX | 1 | 50 | 0.0% |
| YACC | 1 | 1616 | 0.0% |
| OBJECTIVE-C | 1 | 87 | 0.0% |
| POWERSHELL | 1 | 116 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 39 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 4789 |
| cp1252 | cp1252-fallback | 36 |
| utf-8 | bom | 4 |
| latin-1 | latin-1-fallback | 3 |
| utf-16-le | bom | 3 |
| utf-16-be | bom | 2 |

> 2 guessed file(s) read as double-byte text that decodes strictly as gbk: if that is the estate's code page, rescan with `--source-encoding gbk` (or the right one of those). E.g. `cpan/Encode/t/at-cn.t`, `t/op/utfhash.t`.

> 1 guessed file(s) read as double-byte text that decodes strictly as euc_jp / gbk / big5: if that is the estate's code page, rescan with `--source-encoding euc_jp` (or the right one of those). E.g. `cpan/Encode/t/enc_data.t`.

> 1 guessed file(s) read as double-byte text that decodes strictly as euc_jp / gbk / big5 / euc_kr: if that is the estate's code page, rescan with `--source-encoding euc_jp` (or the right one of those). E.g. `cpan/Encode/t/enc_module.t`.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 43%, Data / Markup / Trivial 14%, Interface Declarations Files 13%, Large Core Modules (3) 10%, Compute Cores Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4619 | 95.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 216 | 4.5% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2109*

**Composition by Extension & Reason:**
- `no_extension`: 646x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 287x Unsupported Format (.undeterminable), 6x Unresolved Ambiguity (No Retainable Structure)
- `.t`: 425x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected), 1x Packed Payload Guard (Impossible Density: 3.75 hits/line)
- `.pm`: 123x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1004 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1005 LOC)
- `.pl`: 81x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Zero-Density Threshold (LOC: 51, Signals: 0), 2x Zero-Density Threshold (LOC: 62, Signals: 0)
- `.ucm`: 103x Excluded (Unsupported Extension: '.ucm')
- `.xs`: 65x Excluded (Unsupported Extension: '.xs'), 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tml`: 28x Excluded (Unsupported Extension: '.tml')
- `.pod`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3811 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2922 LOC)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 33097 LOC), 1x Excluded (Machine-Generated Source Code Signature: 865 LOC)
- `.c`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 3595 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1048 LOC)
- `.h`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 37664 hex tokens in 9447 LOC), 1x Excluded (Embedded Hex Payload: 4096 hex tokens in 703 LOC)
- `.yml`: 5x Zero-Density Threshold (LOC: 132, Signals: 0), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Zero-Density Threshold (LOC: 128, Signals: 0)
- `.enc`: 8x Excluded (Unsupported Extension: '.enc')
- `.typemap`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.utf`: 7x Excluded (Unsupported Extension: '.utf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 30.5 | 17.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.7 | 41.2 | 49.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 16.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 6.8 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 52.9 | 50.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.8 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 42.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 21922 | 1984 | 10 | `cpan/Math-BigInt/lib/Math/BigInt.pm` |
| cleanup | 4887 | 1068 | 3 | `Configure` |
| guards | 28099 | 3501 | 8 | `sv.c` |
| danger | 32551 | 2321 | 11 | `Configure` |
| concurrency | 2386 | 392 | 0 | `pod/perlthrtut.pod` |
| connectivity | 20916 | 2296 | 10 | `lib/B/Deparse.pm` |
| io | 23678 | 1544 | 7 | `Configure` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1875 | 476 | 0 | `cpan/perlfaq/lib/perlfaq8.pod` |
| time | 3447 | 644 | 1 | `pod/perlfunc.pod` |
| serialization | 11 | 7 | 0 | `cpan/CPAN-Meta-YAML/t/21_yamlpm_compat.t` |
| regex | 29848 | 2013 | 12 | `t/re/pat_advanced.t` |
| events | 1979 | 531 | 1 | `cpan/CPAN/lib/CPAN/Distribution.pm` |
| tests | 55532 | 2511 | 26 | `cpan/Unicode-Collate/t/loc_cjkc.t` |
| docs | 2543 | 1146 | 1 | `lib/perl5db.pl` |
| debt | 26879 | 2326 | 12 | `Configure` |
| mutation | 170831 | 3793 | 61 | `Configure` |
| dead_code | 6009 | 1059 | 2 | `lib/B/Deparse.pm` |
| credential | 37 | 17 | 0 | `cpan/ExtUtils-MakeMaker/lib/ExtUtils/MM_Unix.pm` |
| threat | 642 | 63 | 0 | `ext/XS-APItest/t/utf8.t` |
| ml_ai | 5661 | 606 | 1 | `cpan/Math-BigInt/lib/Math/BigInt.pm` |
| ui | 477 | 149 | 0 | `pod/perlfunc.pod` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.871**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Configure` (Hits: 5612)
- `pod/perlfunc.pod` (Hits: 677)
- `Makefile.SH` (Hits: 433)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **More.pm** (`cpan/Test-Simple/lib/Test/More.pm`) — 1282 inbound connections
2. **API.pm** (`cpan/Test-Simple/lib/Test2/API.pm`) — 127 inbound connections
3. **Temp.pm** (`cpan/File-Temp/lib/File/Temp.pm`) — 126 inbound connections
4. **MakeMaker.pm** (`cpan/ExtUtils-MakeMaker/lib/ExtUtils/MakeMaker.pm`) — 116 inbound connections
5. **Util.pm** (`cpan/Scalar-List-Utils/lib/Scalar/Util.pm`) — 102 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **perl.h** (`perl.h`) — 110 outbound dependencies
2. **CPAN.pm** (`cpan/CPAN/lib/CPAN.pm`) — 67 outbound dependencies
3. **vms.c** (`vms/vms.c`) — 42 outbound dependencies
4. **Compare.pm** (`cpan/Test-Simple/lib/Test2/Tools/Compare.pm`) — 31 outbound dependencies
5. **Configure** (`Configure`) — 31 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `pp_nextstate` **(Many-Argument Workhorses)** (@ `lib/B/Deparse.pm`) -> Impact: **15971.1** | LOC: 3363
  * *Intent:* # Notice how subs and formats are inserted between statements here; # also $[ assignments and pragmas.
- `gv_name` **(Many-Argument Workhorses)** (@ `lib/B/Deparse.pm`) -> Impact: **6226.9** | LOC: 1867
- `stash_variable_name` **(Many-Argument Workhorses)** (@ `lib/B/Deparse.pm`) -> Impact: **5932.9** | LOC: 1897
  * *Intent:* # Return just the name, without the prefix. It may be returned as a quoted # string. The second return value is a boolean indicating that.
- `opt_o_with` **(Many-Argument Workhorses)** (@ `cpan/Pod-Perldoc/lib/Pod/Perldoc.pm`) -> Impact: **5692.5** | LOC: 1963
- `_read_tar` **(Many-Argument Workhorses)** (@ `cpan/Archive-Tar/lib/Archive/Tar.pm`) -> Impact: **3707.7** | LOC: 1910
- `makeaperl` **(Many-Argument Workhorses)** (@ `cpan/ExtUtils-MakeMaker/lib/ExtUtils/MM_Unix.pm`) -> Impact: **3577.9** | LOC: 1577
- `setupFormat` **(Many-Argument Workhorses)** (@ `cpan/IO-Compress/bin/zipdetails`) -> Impact: **3014.8** | LOC: 2145
- `cmd_wrapper` **(Many-Argument Workhorses)** (@ `lib/perl5db.pl`) -> Impact: **2737.0** | LOC: 1800
- `init` **(Many-Argument Workhorses)** (@ `cpan/CPAN/lib/CPAN/FirstTime.pm`) -> Impact: **2654.5** | LOC: 1386
- `re_dq_disambiguate` **(Many-Argument Workhorses)** (@ `lib/B/Deparse.pm`) -> Impact: **2610.8** | LOC: 1177
  * *Intent:* # Join two components of a double-quoted re, disambiguating # "${foo}bar", "${foo}{bar}", "${foo}[1]".

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pod` | 180 | 568230.6 | 19.95% | 45.69% |
| `__monolith__` | 153 | 183887.06 | 37.88% | 17.15% |
| `cpan/perlfaq/lib` | 11 | 66813.1 | 31.75% | 15.92% |
| `lib/B` | 4 | 41134.74 | 63.01% | 40.92% |
| `t/op` | 230 | 28348.92 | 58.55% | 24.47% |
| `lib` | 81 | 23747.44 | 48.8% | 11.41% |
| `cpan/CPAN/lib/CPAN` | 25 | 17635.76 | 63.8% | 37.25% |
| `Porting` | 73 | 16951.5 | 45.66% | 16.81% |
| `vms` | 5 | 15733.32 | 67.87% | 14.36% |
| `cpan/ExtUtils-MakeMaker/lib/ExtUtils` | 25 | 14447.64 | 26.11% | 17.9% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Porting/perldelta_template.pod` -> **100.0%** Exposure
- `Porting/security_template.pod` -> **100.0%** Exposure
- `cpan/Math-BigInt/t/Math/BigInt/Scalar.pm` -> **100.0%** Exposure
- `cpan/Math-BigInt/t/rt-16221.t` -> **100.0%** Exposure
- `cpan/NEXT/t/next.t` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Cross/generate_config_sh` -> **100.0%** Exposure
- `Porting/bisect.pl` -> **100.0%** Exposure
- `Porting/check-cpan-pollution` -> **100.0%** Exposure
- `Porting/config_h.pl` -> **100.0%** Exposure
- `Porting/corelist.pl` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lib/B/Deparse.pm` -> **362** Orphaned Functions | **0** Duplicates
- `op.c` -> **240** Orphaned Functions | **0** Duplicates
- `sv.c` -> **220** Orphaned Functions | **0** Duplicates
- `win32/win32.c` -> **118** Orphaned Functions | **0** Duplicates
- `util.c` -> **110** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `36` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `18096` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pod/perlfunc.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.774)
- **Top Global Matches:** file_cluster_2: 6.774, file_cluster_13: 7.039, file_cluster_17: 7.628
- **Magnitude:** 158989.11 | **LOC:** 11179 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 20.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.7%), Mutation Surface (formerly State Flux) (39.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.4%), Complexity Load (formerly Cognitive Load) (26.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 16 instances
* *Mitigated Memory Allocs:* 38 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 123 instances
* *High Risk Execution (weighted view):* 63
* *Concurrency (weighted view):* 62
* *Memory Alloc (weighted view):* 118
* *State Mutation (weighted view):* 408
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2534`, `structural_boundaries: 1852`, `args: 36`, `func_start: 28`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 79`, `state_mutation: 162`, `dead_code: 2`, `planned_debt: 12`, `fragile_debt: 2`
* *Architecture:* `io: 677`, `api: 29`, `concurrency: 52`, `import: 488`
* *Defense:* `safety: 97`, `doc: 1`, `test: 2`, `sync_locks: 22`, `cleanup: 61`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pod/perlop.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.743)
- **Top Global Matches:** file_cluster_2: 5.743, file_cluster_13: 6.506, file_cluster_17: 6.947
- **Magnitude:** 56173.58 | **LOC:** 4374 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.9%), Guard Balance (formerly Safety Score) (60.7%), Complexity Load (formerly Cognitive Load) (37.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 162 instances
* *State Mutation (weighted view):* 531
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1017`, `structural_boundaries: 331`, `args: 27`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 31`, `state_mutation: 207`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 6`
* *Architecture:* `io: 171`, `api: 4`, `concurrency: 1`, `import: 163`
* *Defense:* `safety: 30`, `doc: 1`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pod/perlsub.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.893)
- **Top Global Matches:** file_cluster_13: 5.893, file_cluster_2: 6.231, file_cluster_17: 6.737
- **Magnitude:** 44417.32 | **LOC:** 2210 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.7%), Guard Balance (formerly Safety Score) (56.4%), Complexity Load (formerly Cognitive Load) (39.8%), Connectivity (formerly Api Exposure) (12.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 66 instances
* *Memory Alloc (weighted view):* 10
* *State Mutation (weighted view):* 209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 440`, `structural_boundaries: 635`, `args: 95`, `func_start: 113`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 3`, `state_mutation: 77`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `io: 125`, `api: 120`, `import: 80`
* *Defense:* `safety: 19`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/B/Deparse.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.39)
- **Top Global Matches:** file_cluster_4: 10.39, file_cluster_6: 14.172, file_cluster_15: 14.509
- **Magnitude:** 39646.96 | **LOC:** 7691 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 87.5%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.098; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Complexity Load (formerly Cognitive Load) (97.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pp_nextstate` **(Many-Argument Workhorses)** (Impact: 15971.1)
    * *Intent:* # Notice how subs and formats are inserted between statements here; # also $[ assignments and pragma...
  * `gv_name` **(Many-Argument Workhorses)** (Impact: 6226.9)
  * `stash_variable_name` **(Many-Argument Workhorses)** (Impact: 5932.9)
    * *Intent:* # Return just the name, without the prefix. It may be returned as a quoted # string. The second retu...
  * `re_dq_disambiguate` **(Many-Argument Workhorses)** (Impact: 2610.8)
    * *Intent:* # Join two components of a double-quoted re, disambiguating # "${foo}bar", "${foo}{bar}", "${foo}[1]...
  * `ambient_pragmas` **(Many-Argument Workhorses)** (Impact: 528.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 954 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 2891
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2183`, `structural_boundaries: 2466`, `args: 323`, `func_start: 539`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 4`, `state_mutation: 983`, `dead_code: 12`, `planned_debt: 28`, `fragile_debt: 22`, `unreferenced_by_name: 362`
* *Architecture:* `io: 41`, `api: 534`, `concurrency: 4`, `import: 58`
* *Defense:* `safety: 53`, `doc: 1`, `sync_locks: 2`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.098
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000205
  * `Imports (Out-Degree: 1):` B, B::Op_private, Carp, Config, Data::Dumper, builtin, feature, if...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cpan/perlfaq/lib/perlfaq4.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.227)
- **Top Global Matches:** file_cluster_13: 6.227, file_cluster_2: 6.231, file_cluster_17: 7.168
- **Magnitude:** 33399.77 | **LOC:** 2771 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Guard Balance (formerly Safety Score) (59.4%), Complexity Load (formerly Cognitive Load) (53.1%), Debt Markers (formerly Tech Debt) (8.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 130 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 9
* *State Mutation (weighted view):* 391
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 714`, `structural_boundaries: 577`, `args: 19`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 131`, `planned_debt: 2`
* *Architecture:* `io: 18`, `api: 18`, `concurrency: 1`, `import: 139`
* *Defense:* `safety: 15`, `doc: 1`, `sync_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Configure` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 5.079)
- **Top Global Matches:** file_cluster_14: 5.079, file_cluster_7: 9.469, file_cluster_5: 13.259
- **Magnitude:** 25432.2 | **LOC:** 26272 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **31**; blast radius 0.098; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.3%), Complexity Load (formerly Cognitive Load) (85.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 2253 instances
* *Concurrency (weighted view):* 93
* *State Mutation (weighted view):* 9392
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4796`, `structural_boundaries: 5238`, `args: 395`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 8366`, `high_risk_execution: 1`, `state_mutation: 4886`, `dead_code: 28`, `planned_debt: 1`, `fragile_debt: 303`
* *Architecture:* `io: 5612`, `api: 2`, `concurrency: 23`, `import: 203`
* *Defense:* `safety: 1`, `test: 43`, `sync_locks: 51`, `cleanup: 105`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.098
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000205
  * `Imports (Out-Degree: 1):` $config_sh, config_h.SH, $file.sh, myread, $file, $file), checkcc, extract...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pod/perltie.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.945)
- **Top Global Matches:** file_cluster_13: 5.945, file_cluster_2: 6.213, file_cluster_17: 6.68
- **Magnitude:** 22048.51 | **LOC:** 1258 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.8%), Complexity Load (formerly Cognitive Load) (71.5%), Guard Balance (formerly Safety Score) (54.0%), Connectivity (formerly Api Exposure) (10.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 38 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 9
* *State Mutation (weighted view):* 122
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 378`, `args: 71`, `func_start: 47`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 46`, `planned_debt: 5`
* *Architecture:* `io: 68`, `api: 47`, `import: 46`
* *Defense:* `safety: 26`, `doc: 1`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pod/perlre.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.637)
- **Top Global Matches:** file_cluster_2: 5.637, file_cluster_13: 6.387, file_cluster_17: 6.93
- **Magnitude:** 21504.82 | **LOC:** 3524 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.3%), Guard Balance (formerly Safety Score) (53.6%), Complexity Load (formerly Cognitive Load) (36.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 212
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1149`, `structural_boundaries: 215`, `args: 2`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 74`, `fragile_debt: 2`
* *Architecture:* `io: 127`, `api: 3`, `import: 129`
* *Defense:* `safety: 15`, `doc: 1`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pod/perl5160delta.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.824)
- **Top Global Matches:** file_cluster_2: 4.824, file_cluster_13: 5.943, file_cluster_17: 5.978
- **Magnitude:** 19875.2 | **LOC:** 4315 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.6%), Debt Markers (formerly Tech Debt) (41.8%), Mutation Surface (formerly State Flux) (18.6%), Complexity Load (formerly Cognitive Load) (17.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Cascading Flux:* 20 instances
* *Memory Alloc (weighted view):* 12
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 609`, `structural_boundaries: 264`, `args: 8`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 4`, `state_mutation: 26`, `planned_debt: 4`, `fragile_debt: 40`
* *Architecture:* `io: 90`, `api: 11`, `concurrency: 11`, `import: 184`
* *Defense:* `safety: 20`, `doc: 1`, `sync_locks: 5`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pod/perlipc.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.387)
- **Top Global Matches:** file_cluster_2: 7.387, file_cluster_13: 7.596, file_cluster_10: 7.926
- **Magnitude:** 18255.88 | **LOC:** 1841 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Mutation Surface (formerly State Flux) (80.9%), Complexity Load (formerly Cognitive Load) (69.9%), Guard Balance (formerly Safety Score) (60.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 17 instances
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 43 instances
* *High Risk Execution (weighted view):* 30
* *Concurrency (weighted view):* 164
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 573`, `structural_boundaries: 368`, `args: 8`, `func_start: 11`
* *Risk/State:* `high_risk_execution: 47`, `state_mutation: 48`, `planned_debt: 3`, `fragile_debt: 3`
* *Architecture:* `io: 146`, `api: 13`, `concurrency: 59`, `import: 104`
* *Defense:* `safety: 38`, `doc: 1`, `sync_locks: 2`, `cleanup: 57`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pod/perlperf.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.582)
- **Top Global Matches:** file_cluster_2: 5.582, file_cluster_13: 5.829, file_cluster_10: 6.359
- **Magnitude:** 17051.78 | **LOC:** 1187 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (68.6%), Guard Balance (formerly Safety Score) (54.2%), Complexity Load (formerly Cognitive Load) (38.9%), Concurrency Surface (formerly Concurrency) (14.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 399`, `structural_boundaries: 166`, `args: 16`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 25`
* *Architecture:* `io: 17`, `api: 6`, `concurrency: 3`, `import: 48`
* *Defense:* `safety: 13`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pod/perlsyn.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.381)
- **Top Global Matches:** file_cluster_2: 6.381, file_cluster_13: 6.735, file_cluster_17: 7.361
- **Magnitude:** 15811.14 | **LOC:** 1507 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.8%), Complexity Load (formerly Cognitive Load) (61.7%), Guard Balance (formerly Safety Score) (51.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 66 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 7
* *State Mutation (weighted view):* 198
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 670`, `structural_boundaries: 218`, `args: 4`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 66`, `fragile_debt: 2`
* *Architecture:* `io: 49`, `api: 7`, `concurrency: 1`, `import: 72`
* *Defense:* `safety: 89`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vms/vms.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.051)
- **Top Global Matches:** file_cluster_8: 8.051, file_cluster_6: 10.876, file_cluster_4: 19.114
- **Magnitude:** 14829.94 | **LOC:** 14086 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **42**; blast radius 0.465; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.7%), Guard Balance (formerly Safety Score) (81.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.4413% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `store_pipelocs` **(Many-Argument Workhorses)** (Impact: 534.7)
  * `int_tovmsspec` **(Many-Argument Workhorses)** (Impact: 474.2)
    * *Intent:* /*{{{ char *tovmsspec[_ts](char *path, char *buf, int * utf8_flag)*/
  * `posix_to_vmsspec_hardway` **(Many-Argument Workhorses)** (Impact: 443.5)
    * *Intent:* */
  * `int_fileify_dirspec` **(Many-Argument Workhorses)** (Impact: 335.0)
    * *Intent:* ** tounixpath() - convert a directory spec into a Unix-style path. ** tovmspath() - convert a direct...
  * `int_rmsexpand` **(Many-Argument Workhorses)** (Impact: 322.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2349 instances
* *State Mutation (weighted view):* 7291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2979`, `structural_boundaries: 1022`, `args: 754`, `func_start: 188`, `class_start: 140`
* *Risk/State:* `safety_bypasses: 168`, `high_risk_execution: 14`, `state_mutation: 2593`, `dead_code: 1`, `planned_debt: 9`, `fragile_debt: 16`, `unreferenced_by_name: 95`
* *Architecture:* `io: 29`, `api: 150`, `import: 42`
* *Defense:* `safety: 8`, `doc: 2`, `immutability_locks: 197`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.465
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.010869
  * `Imports (Out-Degree: 18):` EXTERN.h, XSUB.h, acedef.h, acldef.h, armdef.h, chpdef.h, clidef.h, climsgdef.h...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `sv.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.401)
- **Top Global Matches:** file_cluster_6: 7.401, file_cluster_4: 13.234, file_cluster_8: 13.6
- **Magnitude:** 14564.86 | **LOC:** 18761 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 46.2%
- **Blast Radius:** changing it is visible to **56** in-repo importer(s); it depends on **5**; blast radius 1.318; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.7%), Debt Markers (formerly Tech Debt) (81.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Perl_sv_vcatpvfn_flags` **(Many-Argument Workhorses)** (Impact: 1369.1)
  * `Perl_sv_setsv_flags` **(Many-Argument Workhorses)** (Impact: 960.3)
  * `S_find_uninit_var` **(Many-Argument Workhorses)** (Impact: 781.0)
    * *Intent:* */
  * `Perl_sv_clear` **(Many-Argument Workhorses)** (Impact: 767.9)
    * *Intent:* */
  * `S_format_hexfp` **(Many-Argument Workhorses)** (Impact: 238.6)
    * *Intent:* * built-in snprintf()s which are used for most of the f/p formats, don't * universally handle %a/%A....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1488 instances
* *State Mutation (weighted view):* 4912
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3242`, `structural_boundaries: 1115`, `args: 904`, `func_start: 254`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 246`, `high_risk_execution: 3`, `state_mutation: 1936`, `dead_code: 7`, `planned_debt: 10`, `fragile_debt: 59`, `unreferenced_by_name: 220`
* *Architecture:* `api: 207`, `import: 5`
* *Defense:* `safety: 225`, `doc: 3`, `immutability_locks: 930`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.318
  * `Choke Point (Betweenness):` 6.9e-05 | `Ripple Effect (Closeness):` 0.013601
  * `Imports (Out-Degree: 34):` EXTERN.h, perl.h, regcomp.h, rms.h, mman.h
  * `Imported By (In-Degree: 56):` (Excluded from Brief to save tokens)

### `pod/perlebcdic.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.908)
- **Top Global Matches:** file_cluster_2: 4.908, file_cluster_13: 6.047, file_cluster_17: 6.311
- **Magnitude:** 14380.2 | **LOC:** 2021 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (77.1%), Guard Balance (formerly Safety Score) (55.2%), Complexity Load (formerly Cognitive Load) (17.5%), Debt Markers (formerly Tech Debt) (10.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 48 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 284`, `structural_boundaries: 111`, `args: 21`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 5`, `state_mutation: 51`, `fragile_debt: 4`
* *Architecture:* `io: 263`, `api: 20`, `import: 34`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `op.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.115)
- **Top Global Matches:** file_cluster_6: 7.115, file_cluster_8: 11.769, file_cluster_4: 14.193
- **Magnitude:** 13998.94 | **LOC:** 17650 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 30.0%
- **Blast Radius:** changing it is visible to **33** in-repo importer(s); it depends on **8**; blast radius 0.836; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.5%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (73.6%)
- **Documentation Coverage:** 49.8469% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Perl_newATTRSUB_x` **(Many-Argument Workhorses)** (Impact: 480.2)
    * *Intent:* */ /* _x = extended */
  * `Perl_op_lvalue_flags` **(Many-Argument Workhorses)** (Impact: 454.2)
    * *Intent:* */
  * `S_pmtrans` **(Many-Argument Workhorses)** (Impact: 365.8)
    * *Intent:* * a translation table attached as o->op_pv. * Free expr and repl. * It expects the toker to have alr...
  * `Perl_scalarvoid` **(Compute Cores)** (Impact: 308.3)
    * *Intent:* /* apply void context to the optree arg */
  * `Perl_newMYSUB` **(Many-Argument Workhorses)** (Impact: 236.0)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 1658 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 5206
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3861`, `structural_boundaries: 989`, `args: 1066`, `func_start: 288`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 203`, `high_risk_execution: 2`, `state_mutation: 1890`, `dead_code: 5`, `planned_debt: 11`, `fragile_debt: 18`, `unreferenced_by_name: 240`
* *Architecture:* `api: 215`, `import: 8`
* *Defense:* `safety: 243`, `doc: 16`, `immutability_locks: 405`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.836
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.012053
  * `Imports (Out-Degree: 39):` EXTERN.h, XSUB.h, feature.h, invlist_inline.h, keywords.h, perl.h, regcomp.h, mman.h
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `regcomp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.65)
- **Top Global Matches:** file_cluster_8: 5.65, file_cluster_6: 15.135, file_cluster_3: 21.767
- **Magnitude:** 13271.66 | **LOC:** 16628 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 94.1%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **10**; blast radius 0.446; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `S_regclass` **(Many-Argument Workhorses)** (Impact: 1334.0)
  * `S_regatom` **(Many-Argument Workhorses)** (Impact: 958.1)
    * *Intent:* */
  * `S_reg` **(Many-Argument Workhorses)** (Impact: 908.4)
    * *Intent:* * has to add them to its *flagp. This means that it takes extra steps to keep * passing a flag upwar...
  * `S_parse_uniprop_string` **(Many-Argument Workhorses)** (Impact: 807.7)
  * `Perl_re_op_compile` **(Many-Argument Workhorses)** (Impact: 709.5)
    * *Intent:* * by node. This design is to minimize, to the extent possible, memory churn * when doing the realloc...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1527 instances
* *State Mutation (weighted view):* 4882
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2860`, `structural_boundaries: 877`, `args: 607`, `func_start: 88`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 118`, `state_mutation: 1828`, `dead_code: 9`, `planned_debt: 4`, `fragile_debt: 32`, `unreferenced_by_name: 70`
* *Architecture:* `api: 37`, `import: 10`
* *Defense:* `safety: 107`, `immutability_locks: 302`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.446
  * `Choke Point (Betweenness):` 3.8e-05 | `Ripple Effect (Closeness):` 0.010144
  * `Imports (Out-Degree: 32):` EXTERN.h, feature.h, invlist_inline.h, perl.h, re_comp.h, re_top.h, regcomp.h, regcomp_internal.h...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `toke.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.646)
- **Top Global Matches:** file_cluster_8: 6.646, file_cluster_6: 16.272, file_cluster_3: 21.118
- **Magnitude:** 13129.98 | **LOC:** 14900 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 87.1%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **5**; blast radius 0.293; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.4%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.6%)
- **Documentation Coverage:** 49.6711% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `yyl_word_or_keyword` **(Many-Argument Workhorses)** (Impact: 861.0)
  * `S_scan_const` **(Many-Argument Workhorses)** (Impact: 450.1)
    * *Intent:* */
  * `yyl_try` **(Compute Cores)** (Impact: 385.7)
  * `S_intuit_more` **(Many-Argument Workhorses)** (Impact: 282.8)
    * *Intent:* * { and [ outside a pattern are always subscripts, so return TRUE * if we're outside a pattern and i...
  * `yyl_just_a_word` **(Many-Argument Workhorses)** (Impact: 209.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1872 instances
* *State Mutation (weighted view):* 5853
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3597`, `structural_boundaries: 746`, `args: 1436`, `func_start: 164`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 114`, `state_mutation: 2109`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 26`, `unreferenced_by_name: 97`
* *Architecture:* `io: 1`, `api: 63`, `import: 5`
* *Defense:* `safety: 52`, `doc: 15`, `immutability_locks: 350`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.293
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.009051
  * `Imports (Out-Degree: 29):` EXTERN.h, feature.h, invlist_inline.h, keywords.h, perl.h
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `pod/perl5140delta.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.604)
- **Top Global Matches:** file_cluster_2: 4.604, file_cluster_17: 5.939, file_cluster_13: 5.964
- **Magnitude:** 13043.21 | **LOC:** 4591 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.0%), Debt Markers (formerly Tech Debt) (34.0%), Mutation Surface (formerly State Flux) (20.6%), Complexity Load (formerly Cognitive Load) (17.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 22 instances
* *High Risk Execution (weighted view):* 5
* *Memory Alloc (weighted view):* 9
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 657`, `structural_boundaries: 272`, `args: 2`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 6`, `state_mutation: 34`, `planned_debt: 1`, `fragile_debt: 36`
* *Architecture:* `io: 122`, `api: 9`, `concurrency: 17`, `import: 208`
* *Defense:* `safety: 8`, `doc: 1`, `test: 1`, `sync_locks: 2`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pod/perl5004delta.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.319)
- **Top Global Matches:** file_cluster_2: 5.319, file_cluster_13: 5.858, file_cluster_17: 6.363
- **Magnitude:** 12818.92 | **LOC:** 1613 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.8%), Mutation Surface (formerly State Flux) (43.6%), Debt Markers (formerly Tech Debt) (35.8%), Complexity Load (formerly Cognitive Load) (26.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 19 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 350`, `structural_boundaries: 205`, `args: 11`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 8`, `state_mutation: 22`, `planned_debt: 1`, `fragile_debt: 14`
* *Architecture:* `io: 30`, `api: 14`, `concurrency: 3`, `import: 77`
* *Defense:* `safety: 11`, `doc: 1`, `test: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/unicore/mktables` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.067)
- **Top Global Matches:** file_cluster_6: 7.067, file_cluster_4: 12.947, file_cluster_8: 13.191
- **Magnitude:** 11759.14 | **LOC:** 20935 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.088; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_pod` **(Many-Argument Workhorses)** (Impact: 660.0)
  * `_add_delete` **(Many-Argument Workhorses)** (Impact: 514.6)
  * `write` **(Many-Argument Workhorses)** (Impact: 335.2)
  * `compile_perl` **(I/O & Config Routines)** (Impact: 266.4)
  * `new` **(Many-Argument Workhorses)** (Impact: 209.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 19 instances
* *Amplified Cascading Flux:* 1642 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 37
* *State Mutation (weighted view):* 5155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3642`, `structural_boundaries: 3104`, `args: 307`, `func_start: 261`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 33`, `high_risk_execution: 5`, `state_mutation: 1871`, `dead_code: 9`, `planned_debt: 8`, `fragile_debt: 24`, `duplicate_logic: 11`, `unreferenced_by_name: 3`
* *Architecture:* `io: 13`, `api: 241`, `concurrency: 1`, `import: 101`
* *Defense:* `safety: 40`, `doc: 1`, `test: 23`, `sync_locks: 5`, `immutability_locks: 1`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Carp, Config, File::Find, File::Path, File::Spec, Text::Tabs, builtin, by...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpan/perlfaq/lib/perlfaq5.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.609)
- **Top Global Matches:** file_cluster_13: 6.609, file_cluster_2: 6.621, file_cluster_17: 7.508
- **Magnitude:** 11723.79 | **LOC:** 1605 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.5%), Guard Balance (formerly Safety Score) (57.2%), Complexity Load (formerly Cognitive Load) (37.6%), Debt Markers (formerly Tech Debt) (12.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 44 instances
* *High Risk Execution (weighted view):* 5
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 414`, `structural_boundaries: 320`, `args: 6`, `func_start: 11`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 49`, `planned_debt: 4`, `fragile_debt: 3`
* *Architecture:* `io: 120`, `api: 11`, `import: 94`
* *Defense:* `safety: 4`, `doc: 1`, `sync_locks: 12`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pod/perlunicode.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.559)
- **Top Global Matches:** file_cluster_2: 4.559, file_cluster_13: 5.553, file_cluster_17: 5.984
- **Magnitude:** 11479.72 | **LOC:** 2417 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.3%), Mutation Surface (formerly State Flux) (15.4%), Complexity Load (formerly Cognitive Load) (15.0%), Debt Markers (formerly Tech Debt) (13.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 468`, `structural_boundaries: 168`, `args: 4`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 4`, `state_mutation: 14`, `planned_debt: 2`, `fragile_debt: 7`
* *Architecture:* `io: 49`, `api: 10`, `import: 108`
* *Defense:* `safety: 11`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `regexec.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.537)
- **Top Global Matches:** file_cluster_8: 8.537, file_cluster_6: 16.714, file_cluster_3: 22.333
- **Magnitude:** 10430.0 | **LOC:** 12653 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 62.5%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.096; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `S_regmatch` **(Many-Argument Workhorses)** (Impact: 1630.0)
    * *Intent:* */ /* returns -1 on failure, $+[0] on success */
  * `S_find_byclass` **(Many-Argument Workhorses)** (Impact: 876.0)
    * *Intent:* /* We know what class REx starts with. Try to find this position... */ /* if reginfo->intuit, its a ...
  * `S_regrepeat` **(Many-Argument Workhorses)** (Impact: 594.0)
    * *Intent:* * * What 'simple' means is a node which can be the operand of a quantifier like * '+', or {1,3} * * ...
  * `Perl_regexec_flags` **(Many-Argument Workhorses)** (Impact: 505.5)
    * *Intent:* */
  * `Perl_re_intuit_start` **(Many-Argument Workhorses)** (Impact: 427.1)
    * *Intent:* * stclass = [ax] * * Be aware that during the course of this function, sometimes 'anchored' * refers...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1267 instances
* *State Mutation (weighted view):* 4000
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2451`, `structural_boundaries: 672`, `args: 458`, `func_start: 60`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 295`, `state_mutation: 1466`, `dead_code: 7`, `planned_debt: 2`, `fragile_debt: 18`, `unreferenced_by_name: 49`
* *Architecture:* `api: 22`, `import: 7`
* *Defense:* `safety: 80`, `doc: 3`, `immutability_locks: 270`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.096
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006475
  * `Imports (Out-Degree: 25):` EXTERN.h, invlist_inline.h, perl.h, re_comp.h, re_top.h, regcomp.h, unicode_constants.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/perl5db.pl` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.337)
- **Top Global Matches:** file_cluster_4: 8.337, file_cluster_6: 8.66, file_cluster_12: 15.608
- **Magnitude:** 9359.32 | **LOC:** 10434 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.088; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.6%), Complexity Load (formerly Cognitive Load) (61.3%)
- **Documentation Coverage:** 39.0671% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cmd_wrapper` **(Many-Argument Workhorses)** (Impact: 2737.0)
  * `sethelp` **(Many-Argument Workhorses)** (Impact: 1662.5)
  * `runman` **(Many-Argument Workhorses)** (Impact: 446.4)
  * `db_complete` **(Many-Argument Workhorses)** (Impact: 154.2)
  * `DB` **(I/O & Config Routines)** (Impact: 110.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Mitigated Memory Allocs:* 17 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 550 instances
* *High Risk Execution (weighted view):* 20
* *Concurrency (weighted view):* 39
* *Memory Alloc (weighted view):* 22
* *State Mutation (weighted view):* 1699
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1933`, `structural_boundaries: 1526`, `args: 208`, `func_start: 210`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 46`, `high_risk_execution: 23`, `state_mutation: 599`, `dead_code: 7`, `planned_debt: 5`, `fragile_debt: 43`, `unreferenced_by_name: 9`
* *Architecture:* `io: 246`, `api: 120`, `concurrency: 24`, `import: 156`
* *Defense:* `safety: 76`, `doc: 183`, `sync_locks: 9`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` B, Carp, Config, Cwd, Devel::Peek, File::Basename, File::Path, IO::Handle...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `lib/B/Deparse-subclass.t` (PERL) | Magnitude: 3.44 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 12, branch: 6, indent_spaces: 6, import: 4
- `cpan/ExtUtils-MakeMaker/t/problems.t` (PERL) | Magnitude: 19.84 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 15, reflection_metaprogramming: 9, globals: 8
- `cpan/autodie/lib/autodie/skip.pm` (PERL) | Magnitude: 16.6 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 13, safety: 6, branch: 5, import: 3
- `ext/PerlIO-encoding/t/threads.t` (PERL) | Magnitude: 18.56 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 10, branch: 7, import: 7
- `cpan/Test-Simple/lib/Test2/Tools/Subtest.pm` (PERL) | Magnitude: 0.04 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 38, indent_spaces: 35, branch: 21, test: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `ext/mro/mro.pm` (PERL) | Magnitude: 19.08 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 120, branch: 84, indent_spaces: 25, io: 23
- `cpan/JSON-PP/t/113_overloaded_eq.t` (PERL) | Magnitude: 10.3 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 30, import: 11, indent_spaces: 10, reflection_metaprogramming: 8
- `lib/DB.t` (PERL) | Magnitude: 69.64 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 294, structural_boundaries: 151, test: 100, branch: 45
- `ext/XS-APItest/t/arrayexpr.t` (PERL) | Magnitude: 393.62 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 288, state_mutation: 152, branch: 65, structural_boundaries: 36
- `cpan/CPAN/lib/CPAN/Distrostatus.pm` (PERL) | Magnitude: 30.48 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 16, args: 6, func_start: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `cpan/Test-Harness/lib/App/Prove/State/Result/Test.pm` (PERL) | Magnitude: 20.52 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 42, indent_spaces: 32, branch: 30, core_var_decl: 13
- `lib/DBM_Filter/t/null.t` (PERL) | Magnitude: 19.44 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 20, indent_tabs: 20, indent_spaces: 20, reflection_metaprogramming: 12
- `ext/XS-APItest/t/gv_fetchmeth.t` (PERL) | Magnitude: 9.4 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 28, import: 8, branch: 6
- `lib/meta_notation.t` (PERL) | Magnitude: 21.76 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: bitwise_ops: 45, indent_spaces: 27, branch: 16, test: 9
- `t/op/leaky-magic.t` (PERL) | Magnitude: 34.86 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 29, globals: 18, import: 15, branch: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `cpan/perlfaq/lib/perlfaq4.pod` (PERL) | Magnitude: 33399.77 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 812, branch: 714, structural_boundaries: 577, decorators: 157
- `cpan/Encode/t/at-cn.t` (PERL) | Magnitude: 13.9 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 45, branch: 20, bitwise_ops: 19, structural_boundaries: 11
- `cpan/Config-Perl-V/t/27_plv5202.t` (PERL) | Magnitude: 23.32 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 79, core_var_decl: 44, design_snake_case: 44, structural_boundaries: 30
- `cpan/Config-Perl-V/t/28_plv5220.t` (PERL) | Magnitude: 23.32 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 79, core_var_decl: 44, design_snake_case: 44, structural_boundaries: 30
- `lib/Net/netent.pm` (PERL) | Magnitude: 89.66 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 44, structural_boundaries: 35, indent_spaces: 33, state_mutation: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `t/mro/method_caching_utf8.t` (PERL) | Magnitude: 4.16 | Delta: **0.222** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 80, indent_spaces: 38, closures: 34, test: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `.github/workflows/testsuite.yml` (YAML) | Magnitude: 179.52 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 601, func_start: 83, branch: 82, structural_boundaries: 70
- `t/op/concat2.t` (PERL) | Magnitude: 13.0 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 21, indent_spaces: 21, reflection_metaprogramming: 7, state_mutation: 6
- `lib/charnames.pm` (PERL) | Magnitude: 27.46 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 113, structural_boundaries: 71, indent_spaces: 60, decorators: 39
- `lib/h2ph.t` (PERL) | Magnitude: 22.2 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 20, branch: 11, structural_boundaries: 8, core_var_decl: 8
- `ext/B/t/terse.t` (PERL) | Magnitude: 48.62 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 33, structural_boundaries: 31, branch: 16, globals: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `win32/fcrypt.c` (C) | Magnitude: 244.16 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 182, bitwise_ops: 99, state_mutation: 92, core_var_decl: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `t/porting/pod_rules.t` (PERL) | Magnitude: 18.38 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, branch: 3, core_var_decl: 3
- `t/re/regexp_notrie.t` (PERL) | Magnitude: 18.24 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 4, panics_and_aborts: 3, indent_spaces: 3, decorators: 2
- `t/re/regexp_trielist.t` (PERL) | Magnitude: 18.24 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 4, indent_spaces: 4, panics_and_aborts: 3, decorators: 2
- `t/comp/final_line_num.t` (PERL) | Magnitude: 18.68 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 4, reflection_metaprogramming: 3, macros: 3, debug_prints: 3
- `t/bigmem/pos.t` (PERL) | Magnitude: 24.36 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 5, branch: 3, structural_boundaries: 3, state_mutation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `t/io/getcwd.t` (PERL) | Magnitude: 15.28 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 6, test: 4, branch: 2, structural_boundaries: 2
- `ext/File-Glob/t/rt114984.t` (PERL) | Magnitude: 21.68 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 12, branch: 8, import: 6
- `Porting/perlgov-team-update` (PERL) | Magnitude: 24.42 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 8, branch: 5, globals: 4
- `cpan/Test-Simple/t/Legacy/require_ok.t` (PERL) | Magnitude: 21.4 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 7, branch: 3, test: 3, globals: 3
- `cpan/Test-Simple/t/Legacy/eq_set.t` (PERL) | Magnitude: 21.48 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 11, explicit_casts: 9, test: 5, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `cpan/Test-Simple/lib/Test2/Util/Stash.pm` (PERL) | Magnitude: 137.32 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 105, indent_spaces: 88, branch: 55, state_mutation: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `ext/B/t/OptreeCheck.pm` (PERL) | Magnitude: 538.64 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 242, indent_spaces: 204, structural_boundaries: 155, indent_tabs: 86
- `install_lib.pl` (PERL) | Magnitude: 220.04 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: branch: 70, indent_tabs: 61, indent_spaces: 57, structural_boundaries: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `ext/XS-APItest/t/delimcpy.t` (PERL) | Magnitude: 42.72 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 134, test: 47, structural_boundaries: 34, state_mutation: 30
- `t/op/getpid.t` (PERL) | Magnitude: 19.76 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 19, branch: 11, structural_boundaries: 10, import: 6
- `t/op/yadayada.t` (PERL) | Magnitude: 40.4 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 19, globals: 16, indent_spaces: 14, state_mutation: 12
- `cpan/Test-Simple/lib/Test2/Require/Perl.pm` (PERL) | Magnitude: 8.52 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 19, branch: 9, import: 8, indent_spaces: 8
- `ext/SDBM_File/dba.c` (C) | Magnitude: 69.3 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 52, branch: 13, state_mutation: 12, debug_prints: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pp.c` (C) | Magnitude: 3786.16 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 5799, branch: 1958, pointers: 1223, state_mutation: 1052

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `cpan/Digest/lib/Digest.pm` (PERL) | Magnitude: 60.26 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 61, branch: 47, state_mutation: 15
- `t/re/regexp.t` (PERL) | Magnitude: 436.92 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 319, branch: 273, state_mutation: 135, regex_execution: 80

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pod/perldelta.pod` -> Churn: **82.38%** | Cog Load: 8.1707% | Debt: 100.0%
- `numeric.c` -> Churn: **81.38%** | Cog Load: 96.1625% | Debt: 75.8141%
- `toke.c` -> Churn: **79.62%** | Cog Load: 83.3631% | Debt: 38.4339%
- `op.c` -> Churn: **67.68%** | Cog Load: 82.4554% | Debt: 73.5576%
- `sv.c` -> Churn: **62.52%** | Cog Load: 95.6614% | Debt: 81.647%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/B/Deparse.pm` -> **David Mitchell** (87.5% isolated ownership) | Magnitude: 39646.96
- `pod/perlre.pod` -> **Karl Williamson** (100.0% isolated ownership) | Magnitude: 21504.82
- `vms/vms.c` -> **Karl Williamson** (100.0% isolated ownership) | Magnitude: 14829.94
- `pod/perlebcdic.pod` -> **Karl Williamson** (100.0% isolated ownership) | Magnitude: 14380.2
- `regcomp.c` -> **Karl Williamson** (94.1% isolated ownership) | Magnitude: 13271.66

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `cpan/Test-Simple/lib/Test2/API.pm` -> **Severity: 0.256** (Bridge: 0.0026 * Flux: 98.6677%)
- `cpan/Test-Simple/lib/Test2/IPC/Driver/Files.pm` -> **Severity: 0.098** (Bridge: 0.001 * Flux: 98.8029%)
- `cpan/Test-Simple/lib/Test2/Event.pm` -> **Severity: 0.088** (Bridge: 0.0009 * Flux: 99.9983%)
- `cpan/Test-Simple/lib/Test2/V0.pm` -> **Severity: 0.081** (Bridge: 0.0008 * Flux: 99.9575%)
- `cpan/Test-Simple/lib/Test2/Bundle/Extended.pm` -> **Severity: 0.065** (Bridge: 0.0006 * Flux: 99.8071%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `cpan/Scalar-List-Utils/lib/Scalar/Util.pm` -> **Severity: 13.557** (Embedded: 0.1942 * Error Risk: 69.8172%)
- `cpan/Test-Simple/lib/Test/More.pm` -> **Severity: 10.036** (Embedded: 0.1937 * Error Risk: 51.8194%)
- `cpan/Digest-SHA/t/methods.t` -> **Severity: 9.953** (Embedded: 0.1309 * Error Risk: 76.0048%)
- `cpan/Scalar-List-Utils/lib/List/Util.pm` -> **Severity: 8.181** (Embedded: 0.1401 * Error Risk: 58.4059%)
- `cpan/Test-Simple/lib/Test/Builder/Module.pm` -> **Severity: 6.947** (Embedded: 0.1328 * Error Risk: 52.3291%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cpan/Scalar-List-Utils/lib/Scalar/Util.pm` -> **Severity: 3671.0** (Blast Radius: 36.71 * Doc Risk: 100.0%)
- `cpan/Scalar-List-Utils/lib/List/Util.pm` -> **Severity: 3453.4** (Blast Radius: 34.534 * Doc Risk: 100.0%)
- `cpan/Test-Simple/lib/Test/More.pm` -> **Severity: 2354.845** (Blast Radius: 73.717 * Doc Risk: 31.9444%)
- `cpan/Test-Simple/lib/Test/Builder.pm` -> **Severity: 2233.8** (Blast Radius: 22.338 * Doc Risk: 100.0%)
- `cpan/Digest-SHA/lib/Digest/SHA.pm` -> **Severity: 1977.6** (Blast Radius: 19.776 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 19834 literal sites + 389 sites through wrappers = 20223
- **`memory_alloc`:** 9965 literal sites + 505 sites through wrappers = 10470
- **`panics_and_aborts`:** 10311 literal sites + 186 sites through wrappers = 10497

- `PerlMem_free` (macro, memory_alloc, primitive): 298 call sites in 3 files -- `iperlsys.h`
- `shift` (function, debug_prints, primitive): 187 call sites in 77 files -- `t/japh/abigail.t`
- `split` (function, debug_prints, primitive): 175 call sites in 84 files -- `cpan/ExtUtils-Install/t/lib/MakeMaker/Test/Setup/BFD.pm`
- `PerlMem_malloc` (macro, memory_alloc, primitive): 99 call sites in 3 files -- `iperlsys.h`
- `_new` (function, panics_and_aborts, primitive): 53 call sites in 1 files -- `cpan/Math-BigInt/lib/Math/BigInt/Lib.pm`
- `_str` (function, panics_and_aborts, primitive): 33 call sites in 1 files -- `cpan/Math-BigInt/lib/Math/BigInt/Lib.pm`
- `PerlMemShared_free` (macro, memory_alloc, primitive): 31 call sites in 5 files -- `iperlsys.h`
- `_add` (function, panics_and_aborts, primitive): 28 call sites in 1 files -- `cpan/Math-BigInt/lib/Math/BigInt/Lib.pm`
- `PerlMemShared_malloc` (macro, memory_alloc, primitive): 16 call sites in 7 files -- `iperlsys.h`
- `PerlMemShared_calloc` (macro, memory_alloc, primitive): 15 call sites in 2 files -- `iperlsys.h`
- `_sub` (function, panics_and_aborts, primitive): 15 call sites in 1 files -- `cpan/Math-BigInt/lib/Math/BigInt/Lib.pm`
- `_croak` (function, panics_and_aborts, primitive): 14 call sites in 1 files -- `cpan/HTTP-Tiny/lib/HTTP/Tiny.pm`
*(+47 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 88706 call pairs -- scoped 11.9%, unique 7.6%, ambiguous 6.1%, external 74.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| perl | 49891 | 12.8% | 0.0% | 10.8% | 76.4% |
| c | 36890 | 10.7% | 17.9% | 0.0% | 71.4% |
| cpp | 798 | 19.3% | 23.6% | 4.3% | 52.9% |
| shell | 797 | 0.3% | 0.0% | 0.0% | 99.7% |
| yacc | 252 | 4.4% | 0.0% | 0.0% | 95.6% |
| livecode | 75 | 0.0% | 0.0% | 0.0% | 100.0% |
| rexx | 3 | 33.3% | 0.0% | 0.0% | 66.7% |

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
