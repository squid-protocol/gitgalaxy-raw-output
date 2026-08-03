# ARCHITECTURAL_BRIEF: perl5
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/perl5` |
| **Timestamp** | `2026-08-03T19:30:19.140837+00:00` |
| **Scan Duration** | `21.12s` |
| **Git Branch** | `blead` |
| **Git Commit** | `8ef751faca0eea850cb6a8604bd4ae7e45a87031` |
| **Git Remote** | `https://github.com/Perl/perl5.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 340 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 6946 |
| Analyzed Artifacts (Scanned) | 4634 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2312 |
| Total LOC | 826978 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 66.7% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7772 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.172 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.7326 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 212 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 4045 | 706738 | 87.3% |
| C | 228 | 101877 | 4.9% |
| PLAINTEXT | 157 | 7 | 3.4% |
| SHELL | 102 | 12098 | 2.2% |
| YAML | 34 | 1188 | 0.7% |
| XML | 33 | 0 | 0.7% |
| MARKDOWN | 13 | 0 | 0.3% |
| JSON | 12 | 611 | 0.3% |
| MAKEFILE | 6 | 4333 | 0.1% |
| BATCH | 2 | 91 | 0.0% |
| M4 | 1 | 4 | 0.0% |
| OBJECTIVE-C | 1 | 31 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.655`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 1938 | 41.8% |
| file_cluster_8 | 1262 | 27.2% |
| file_cluster_13 | 1045 | 22.6% |
| file_cluster_4 | 82 | 1.8% |
| file_cluster_17 | 75 | 1.6% |
| file_cluster_11 | 44 | 0.9% |
| file_cluster_12 | 11 | 0.2% |
| Unknown | 7 | 0.2% |
| file_cluster_9 | 4 | 0.1% |
| file_cluster_1 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 163 | 3.5% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2312*

**Composition by Extension & Reason:**
- `no_extension`: 838x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 153x Unsupported Format (.undeterminable), 4x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)
- `.t`: 425x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Binary Format Detected), 1x Excluded (Machine-Generated Source Code Signature: 3662 LOC)
- `.pm`: 121x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected), 1x Excluded (Saturation: Line 82 exceeds 500 chars)
- `.ucm`: 103x Excluded (Unsupported Extension: '.ucm')
- `.pod`: 47x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Machine-Generated Source Code Signature: 126 LOC), 3x Excluded (Machine-Generated Source Code Signature: 110 LOC)
- `.pl`: 84x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 80211 commas in 20094 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1434 LOC)
- `.xs`: 59x Excluded (Unsupported Extension: '.xs'), 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 60x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected), 1x Excluded (Monolithic Amalgamation: 33097 LOC exceeds safe regex boundaries)
- `.tml`: 25x Excluded (Unsupported Extension: '.tml'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 3595 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1048 LOC)
- `.yml`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected)
- `.plx`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 37664 hex tokens in 9447 LOC), 1x Excluded (Embedded Hex Payload: 4096 hex tokens in 703 LOC)
- `.json`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.enc`: 8x Excluded (Unsupported Extension: '.enc')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 58.3 | 66.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 37.1 | 29.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 22.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 10.9 | 0.0 | 0.0 |
| API Exposure | 0.0 | 16.9 | 0.8 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 79.5 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 91.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.8 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 47.8 | 40.0 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 16.3 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 19.4 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 5.9 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.1 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `cpan/Win32API-File/File.pm` (Hits: 311)
- `config_h.SH` (Hits: 280)
- `pod/perlebcdic.pod` (Hits: 264)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **POSIX.pm** (`ext/POSIX/lib/POSIX.pm`) — 79 inbound connections
2. **Fcntl.pm** (`ext/Fcntl/Fcntl.pm`) — 68 inbound connections
3. **EXTERN.h** (`EXTERN.h`) — 67 inbound connections
4. **perl.h** (`perl.h`) — 63 inbound connections
5. **Errno.t** (`ext/Errno/t/Errno.t`) — 46 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **perl.h** (`perl.h`) — 110 outbound dependencies
2. **CPAN.pm** (`cpan/CPAN/lib/CPAN.pm`) — 105 outbound dependencies
3. **perl5db.pl** (`lib/perl5db.pl`) — 90 outbound dependencies
4. **epigraphs.pod** (`Porting/epigraphs.pod`) — 66 outbound dependencies
5. **Deparse.pm** (`lib/B/Deparse.pm`) — 62 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `shell` (@ `cpan/CPAN/lib/CPAN.pm`) -> Impact: **17212.8** | LOC: 1536
  * *Intent:* #-> sub CPAN::shell ;
- `_ftp_statistics` (@ `cpan/CPAN/lib/CPAN/FTP.pm`) -> Impact: **12249.4** | LOC: 1289
  * *Intent:* #-> sub CPAN::FTP::ftp_statistics # if they want to rewrite, they need to pass in a filehandle
- `_DB__at_end_of_every_command` (@ `lib/perl5db.pl`) -> Impact: **11215.9** | LOC: 2365
- `next_todo` (@ `lib/B/Deparse.pm`) -> Impact: **9014.4** | LOC: 2097
  * *Intent:* # Pop the next sub from the todo list and deparse it
- `canonicalName` (@ `cpan/IO-Compress/lib/IO/Compress/Zip.pm`) -> Impact: **8513.9** | LOC: 1789
- `find_perl` (@ `cpan/ExtUtils-MakeMaker/lib/ExtUtils/MM_Unix.pm`) -> Impact: **8097.7** | LOC: 1464
- `eval_in_subdirs` (@ `cpan/ExtUtils-MakeMaker/lib/ExtUtils/MakeMaker.pm`) -> Impact: **7968.9** | LOC: 1739
- `check_and_add_proto_defn` (@ `autodoc.pl`) -> Impact: **7818.4** | LOC: 1144
- `get_max_depth` (@ `cpan/JSON-PP/lib/JSON/PP.pm`) -> Impact: **7447.2** | LOC: 1837
- `Compress` (@ `cpan/IO-Compress/lib/Compress/Zlib.pm`) -> Impact: **7380.6** | LOC: 1297

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `generate_manifest` (@ `Porting/pod_rules.pl`) -> **O(2^N) [Recursive]**
- `watchdog` (@ `Porting/test-dist-modules.pl`) -> **O(2^N) [Recursive]**
  * *Intent:* # Set a watchdog to timeout the entire test file # NOTE: If the test file uses 'threads', then call the watchdog() function # _AFTER_ the 'threads' mo...
- `read_authors_file` (@ `Porting/updateAUTHORS.pm`) -> **O(2^N) [Recursive]**
- `check_and_add_proto_defn` (@ `autodoc.pl`) -> **O(2^N) [Recursive]**
- `write` (@ `cpan/Archive-Tar/lib/Archive/Tar.pm`) -> **O(2^N) [Recursive]**
- `effective_prereqs` (@ `cpan/CPAN-Meta/lib/CPAN/Meta.pm`) -> **O(2^N) [Recursive]**
  * *Intent:* #pod =method effective_prereqs #pod #pod my $prereqs = $meta->effective_prereqs; #pod #pod my $prereqs = $meta->effective_prereqs( \@feature_identifie...
- `shell` (@ `cpan/CPAN/lib/CPAN.pm`) -> **O(2^N) [Recursive]**
  * *Intent:* #-> sub CPAN::shell ;
- `tidyup` (@ `cpan/CPAN/lib/CPAN/CacheMgr.pm`) -> **O(2^N) [Recursive]**
  * *Intent:* #-> sub CPAN::CacheMgr::tidyup ;
- `new` (@ `cpan/CPAN/lib/CPAN/Distribution.pm`) -> **O(2^N) [Recursive]**
  * *Intent:* #-> sub CPAN::Distribution::new ;
- `test` (@ `cpan/CPAN/lib/CPAN/Distribution.pm`) -> **O(2^N) [Recursive]**
  * *Intent:* #-> sub CPAN::Distribution::test ;

### Highest Data Gravity (Database Complexity)
- `Anonymous_Block_[Truncated]` (@ `config_h.SH`) -> DB Complexity: **844**
  * *Intent:* #!/bin/sh # # THIS IS A GENERATED FILE # DO NOT HAND-EDIT # # See Porting/config_h.pl
- `tainted` (@ `t/op/taint.t`) -> DB Complexity: **738**
  * *Intent:* # How to identify taint when you see it
- `Anonymous_Block_[Truncated]` (@ `hints/aix.sh`) -> DB Complexity: **696**
  * *Intent:* # Take possible hint from the environment. If 32-bit is set in the # environment, we can override it later. If set for 64, the # 'sizeof' test sees a ...
- `set` (@ `cpan/Win32API-File/File.pm`) -> DB Complexity: **654**
- `new` (@ `lib/overload.t`) -> DB Complexity: **643**
- `Anonymous_Block_[Truncated]` (@ `Cross/Makefile-cross-SH`) -> DB Complexity: **634**
- `_db_system` (@ `lib/perl5db.pl`) -> DB Complexity: **634**
- `Perl_vmstrnenv` (@ `vms/vms.c`) -> DB Complexity: **588**
- `next_todo` (@ `lib/B/Deparse.pm`) -> DB Complexity: **562**
  * *Intent:* # Pop the next sub from the todo list and deparse it
- `Anonymous_Block_[Truncated]` (@ `hints/aix_4.sh`) -> DB Complexity: **561**
  * *Intent:* # Take possible hint from the environment. If 32-bit is set in the # environment, we can override it later. If set for 64, the # 'sizeof' test sees a ...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 152 | 163567.74 | 53.6% | 16.92% |
| `lib` | 79 | 142558.72 | 63.52% | 11.33% |
| `t/op` | 231 | 113451.47 | 78.69% | 26.72% |
| `pod` | 144 | 103030.54 | 22.1% | 43.48% |
| `cpan/CPAN/lib/CPAN` | 25 | 78222.86 | 76.25% | 30.44% |
| `t/re` | 77 | 62237.4 | 55.06% | 26.3% |
| `cpan/Unicode-Collate` | 3 | 50759.45 | 68.93% | 0.0% |
| `cpan/Math-BigInt/lib/Math` | 3 | 46125.68 | 70.18% | 18.98% |
| `Porting` | 72 | 37948.39 | 55.55% | 20.25% |
| `cpan/ExtUtils-MakeMaker/lib/ExtUtils` | 25 | 37895.77 | 46.19% | 12.29% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Cross/warp` -> **100.0%** Exposure
- `Policy_sh.SH` -> **100.0%** Exposure
- `Porting/bisect-example.sh` -> **100.0%** Exposure
- `Porting/git-make-p4-refs` -> **100.0%** Exposure
- `Porting/rt_list_patches` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `amigaos4/config.sh` -> **100.0%** Exposure
- `hints/aix.sh` -> **100.0%** Exposure
- `hints/aix_3.sh` -> **100.0%** Exposure
- `hints/aix_4.sh` -> **100.0%** Exposure
- `hints/amigaos.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `win32/win32sck.c` -> **45** Orphaned Functions | **0** Duplicates
- `util.c` -> **43** Orphaned Functions | **0** Duplicates
- `mg.c` -> **39** Orphaned Functions | **0** Duplicates
- `cpan/IO-Compress/lib/IO/Compress/Base/Common.pm` -> **20** Orphaned Functions | **17** Duplicates
- `cpan/Pod-Simple/lib/Pod/Simple/Text.pm` -> **29** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`cygwin/cygwin.c`** -> AI Confidence: **99.48%**
2. **`doio.c`** -> AI Confidence: **99.48%**
3. **`mg.c`** -> AI Confidence: **99.48%**
4. **`op.c`** -> AI Confidence: **99.48%**
5. **`perl.c`** -> AI Confidence: **99.48%**
6. **`pp_sys.c`** -> AI Confidence: **99.48%**
7. **`regcomp.c`** -> AI Confidence: **99.48%**
8. **`regcomp_debug.c`** -> AI Confidence: **99.48%**
9. **`regcomp_study.c`** -> AI Confidence: **99.48%**
10. **`regcomp_trie.c`** -> AI Confidence: **99.48%**
11. **`regexec.c`** -> AI Confidence: **99.48%**
12. **`vms/vms.c`** -> AI Confidence: **99.48%**
13. **`win32/perlglob.c`** -> AI Confidence: **99.48%**
14. **`cpan/Math-BigInt/t/upgrade.inc`** -> AI Confidence: **99.48%**
15. **`ext/SDBM_File/sdbm.h`** -> AI Confidence: **99.44%**
16. **`cpan/Compress-Raw-Zlib/zlib-src/zconf.h`** -> AI Confidence: **99.43%**
17. **`os2/os2.c`** -> AI Confidence: **99.39%**
18. **`regcomp_invlist.c`** -> AI Confidence: **99.39%**
19. **`util.c`** -> AI Confidence: **99.39%**
20. **`cpan/Compress-Raw-Zlib/zlib-src/zutil.h`** -> AI Confidence: **99.39%**
21. **`dump.c`** -> AI Confidence: **99.34%**
22. **`ext/SDBM_File/dbe.c`** -> AI Confidence: **99.34%**
23. **`ext/SDBM_File/dbu.c`** -> AI Confidence: **99.34%**
24. **`gv.c`** -> AI Confidence: **99.34%**
25. **`pp.c`** -> AI Confidence: **99.34%**
26. **`sv.c`** -> AI Confidence: **99.34%**
27. **`toke.c`** -> AI Confidence: **99.34%**
28. **`vms/munchconfig.c`** -> AI Confidence: **99.34%**
29. **`cflags.SH`** -> AI Confidence: **99.32%**
30. **`hints/cxux.sh`** -> AI Confidence: **99.32%**
31. **`cpan/Encode/encengine.c`** -> AI Confidence: **99.32%**
32. **`locale.c`** -> AI Confidence: **99.32%**
33. **`mro_core.c`** -> AI Confidence: **99.32%**
34. **`perl.h`** -> AI Confidence: **99.32%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `ext/XS-APItest/t/utf8.t` -> **100.0%** Exposure
- `ext/XS-APItest/t/utf8_warn_base.pl` -> **100.0%** Exposure
- `t/op/signatures.t` -> **100.0%** Exposure
- `pad.c` -> **16.1172%** Exposure
- `t/op/substr.t` -> **9.4226%** Exposure
### Exploit Generation Surface
- `Porting/add-pod-file` -> **100.0%** Exposure
- `Porting/bench.pl` -> **100.0%** Exposure
- `Porting/bisect-runner.pl` -> **100.0%** Exposure
- `Porting/bisect.pl` -> **100.0%** Exposure
- `Porting/checkURL.pl` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `Makefile.SH` -> **100.0%** Exposure
- `win32/pod.mak` -> **100.0%** Exposure
- `Cross/warp` -> **100.0%** Exposure
- `Porting/add-pod-file` -> **100.0%** Exposure
- `Porting/bisect.pl` -> **100.0%** Exposure
### Raw Memory Manipulation
- `op.c` -> **10.0%** Exposure
- `peep.c` -> **10.0%** Exposure
- `perlio.c` -> **10.0%** Exposure
- `class.c` -> **9.9999%** Exposure
- `ext/File-Glob/bsd_glob.c` -> **9.9999%** Exposure
### Algorithmic DoS Exposure
- `Cross/Makefile-cross-SH` -> **100.0%** Exposure
- `cflags.SH` -> **100.0%** Exposure
- `hints/aix.sh` -> **100.0%** Exposure
- `hints/aix_3.sh` -> **100.0%** Exposure
- `hints/aix_4.sh` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `47` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `24435` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `t/test.pl` (PERL) -> Cumulative Risk: **962.32**
- **Archetype:** `file_cluster_0` (Distance: 14.244 IQR)
- **Magnitude:** 4214.14 | **LOC:** 2092 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 69.2%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `display` (Impact: 1630.0), `warning_is` (Impact: 316.1), `_setup_one_file` (Impact: 288.7)

### 2. `os2/OS2/OS2-Process/t/os2_process_kid.t` (PERL) -> Cumulative Risk: **936.17**
- **Archetype:** `file_cluster_4` (Distance: 20.412 IQR)
- **Magnitude:** 44.64 | **LOC:** 65 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)

### 3. `cpan/CPAN/lib/CPAN/Tarzip.pm` (PERL) -> Cumulative Risk: **935.68**
- **Archetype:** `file_cluster_0` (Distance: 13.047 IQR)
- **Magnitude:** 5059.02 | **LOC:** 480 | **CtrlFlow:** 78.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `untar` (Impact: 3175.5), `gtest` (Impact: 926.7), `new` (Impact: 183.3)

### 4. `cpan/IO-Compress/lib/IO/Compress/Adapter/Deflate.pm` (PERL) -> Cumulative Risk: **911.52**
- **Archetype:** `file_cluster_0` (Distance: 15.371 IQR)
- **Magnitude:** 290.74 | **LOC:** 193 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `mkCompObject` (Impact: 45.6), `mkCompObject1` (Impact: 45.6), `flush` (Impact: 17.9)

### 5. `cpan/Test-Simple/lib/Test2/Workflow/Runner.pm` (PERL) -> Cumulative Risk: **908.2**
- **Archetype:** `file_cluster_0` (Distance: 13.83 IQR)
- **Magnitude:** 1831.66 | **LOC:** 497 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `run` (Impact: 1394.2), `init` (Impact: 69.5), `send_event` (Impact: 43.9)

### 6. `cpan/IO-Compress/lib/IO/Compress/Base/Common.pm` (PERL) -> Cumulative Risk: **902.61**
- **Archetype:** `file_cluster_0` (Distance: 15.702 IQR)
- **Magnitude:** 1579.84 | **LOC:** 1054 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `IO` (Impact: 179.6), `IO` (Impact: 149.5), `whatIs` (Impact: 122.7)

### 7. `cpan/Test-Simple/lib/Test2/Workflow/Task.pm` (PERL) -> Cumulative Risk: **902.39**
- **Archetype:** `file_cluster_0` (Distance: 13.555 IQR)
- **Magnitude:** 286.64 | **LOC:** 183 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `clone` (Impact: 133.7), `init` (Impact: 60.4)

### 8. `cpan/IO-Compress/private/MakeUtil.pm` (PERL) -> Cumulative Risk: **900.72**
- **Archetype:** `file_cluster_0` (Distance: 13.433 IQR)
- **Magnitude:** 1026.88 | **LOC:** 382 | **CtrlFlow:** 72.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `UpDowngrade` (Impact: 750.8), `getPerlFiles` (Impact: 29.7), `MY` (Impact: 14.8)

### 9. `cpan/Test-Harness/lib/TAP/Parser/Iterator/Process.pm` (PERL) -> Cumulative Risk: **890.69**
- **Archetype:** `file_cluster_0` (Distance: 13.546 IQR)
- **Magnitude:** 1157.48 | **LOC:** 381 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_get_unicode` (Impact: 869.7), `_finish` (Impact: 38.8), `_use_open3` (Impact: 13.9)

### 10. `cpan/CPAN/lib/CPAN/Distribution.pm` (PERL) -> Cumulative Risk: **888.44**
- **Archetype:** `file_cluster_0` (Distance: 14.059 IQR)
- **Magnitude:** 28274.74 | **LOC:** 4931 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `new` (Impact: 5275.4), `test` (Impact: 3839.6), `check_disabled` (Impact: 3709.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `cpan/Unicode-Collate/Collate.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.374 IQR)
- **Top Global Matches:** file_cluster_0: 14.374, file_cluster_13: 14.377, file_cluster_17: 14.424
- **Magnitude:** 50603.87 | **LOC:** 2157 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (56.6437%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 595`, `structural_boundaries: 325`, `args: 65`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1389`, `dead_code: 1`
* *Architecture:* `io: 33`, `import: 49`
* *Defense:* `safety: 17`, `doc: 82`, `cleanup: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` effect, Carp, Preprocess, Normalization, strict, parameters, no, constant...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/locale.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.434 IQR)
- **Top Global Matches:** file_cluster_0: 13.434, file_cluster_13: 13.672, file_cluster_8: 13.725
- **Magnitude:** 43709.29 | **LOC:** 2936 | **CtrlFlow:** 77.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (91.8767%), Tech Debt (16.8176%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1185`, `structural_boundaries: 352`, `args: 11`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 46`, `state_mutation: 1428`, `dead_code: 1`, `planned_debt: 18`, `fragile_debt: 7`
* *Architecture:* `import: 96`
* *Defense:* `safety: 7`, `test: 11`, `cleanup: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` eval, strict, bytes, charnames, all, warnings, Dumpvalue, tainting...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/re/anyof.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.661 IQR)
- **Top Global Matches:** file_cluster_0: 11.661, file_cluster_8: 11.945, file_cluster_13: 12.429
- **Magnitude:** 40574.14 | **LOC:** 900 | **CtrlFlow:** 97.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (67.5501%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1510`, `structural_boundaries: 45`, `args: 6`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 172`, `dead_code: 1`
* *Architecture:* `import: 9`
* *Defense:* `safety: 2`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ASCII, feature, Config, utf8, Unicode::UCD, re, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpan/CPAN/lib/CPAN/Distribution.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.059 IQR)
- **Top Global Matches:** file_cluster_0: 14.059, file_cluster_11: 14.604, file_cluster_8: 14.621
- **Magnitude:** 28274.74 | **LOC:** 4931 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 173
- **Risk Profile:** Cognitive Load (92.6494%), Tech Debt (19.0378%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 5275.4 | O(2^N) | DB: 132)
    * *Intent:* #-> sub CPAN::Distribution::new ;
  * `test` (Impact: 3839.6 | O(2^N) | DB: 53)
    * *Intent:* #-> sub CPAN::Distribution::test ;
  * `check_disabled` (Impact: 3709.5 | O(N^6) | DB: 173)
    * *Intent:* #-> sub CPAN::Distribution::check_disabled ;
  * `_getsave_url` (Impact: 3582.7 | O(2^N) | DB: 64)
    * *Intent:* #-> sub CPAN::Distribution::_getsave_url ;
  * `prereq_pm` (Impact: 2842.4 | O(2^N) | DB: 60)
    * *Intent:* #-> sub CPAN::Distribution::prereq_pm ;
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3470`, `structural_boundaries: 1118`, `args: 105`, `func_start: 100`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 79`, `state_mutation: 2501`, `dead_code: 7`, `planned_debt: 4`, `fragile_debt: 27`
* *Architecture:* `io: 60`, `api: 2`, `concurrency: 50`, `import: 27`
* *Defense:* `safety: 36`, `sync_locks: 1`, `cleanup: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` what, ExtUtils::MakeMaker, Cwd, anymore, Carp, build_dir, strict, need...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/perl5db.pl` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.949 IQR)
- **Top Global Matches:** file_cluster_0: 14.949, file_cluster_13: 15.023, file_cluster_17: 15.106
- **Magnitude:** 25315.22 | **LOC:** 10434 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 634
- **Risk Profile:** Cognitive Load (49.3026%), Tech Debt (19.1359%)
**Top Internal Functions/Classes:**
  * `_DB__at_end_of_every_command` (Impact: 11215.9 | O(2^N) | DB: 366)
  * `_db_system` (Impact: 5171.4 | O(2^N) | DB: 634)
  * `afterinit` (Impact: 2085.4 | O(2^N) | DB: 30)
  * `methods_via` (Impact: 1759.9 | O(2^N) | DB: 110)
  * `cmd_b` (Impact: 492.1 | O(N^4) | DB: 87)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2727`, `structural_boundaries: 1183`, `args: 212`, `func_start: 210`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 53`, `high_risk_execution: 21`, `state_mutation: 3456`, `dead_code: 21`, `planned_debt: 5`, `fragile_debt: 43`
* *Architecture:* `io: 259`, `api: 4`, `concurrency: 104`, `import: 153`
* *Defense:* `safety: 74`, `doc: 644`, `sync_locks: 9`, `cleanup: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` local, break, strict, generic, for, B, assumptions, value...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Unicode/UCD.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.69 IQR)
- **Top Global Matches:** file_cluster_0: 13.69, file_cluster_8: 13.734, file_cluster_13: 13.975
- **Magnitude:** 23850.17 | **LOC:** 2676 | **CtrlFlow:** 72.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (87.1839%), Tech Debt (9.983%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 891`, `structural_boundaries: 347`, `args: 5`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 1007`, `dead_code: 1`, `fragile_debt: 3`
* *Architecture:* `io: 11`, `import: 29`
* *Defense:* `safety: 3`, `test: 680`, `cleanup: 108`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` sense, strict, is, specials, Data::Dumper, Storable, charnames, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `perl.h` (C | Tier 0 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.181 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.773 IQR)
- **Top Global Matches:** file_cluster_8: 13.181, file_cluster_12: 13.43, file_cluster_13: 13.551
- **Magnitude:** 22844.92 | **LOC:** 9361 | **CtrlFlow:** 74.3% | **Authorship Centralization:** 83.6%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (61.4346%), Tech Debt (12.2747%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 574`, `structural_boundaries: 199`, `args: 12`, `func_start: 2`, `class_start: 56`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 318`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 10`
* *Architecture:* `io: 5`, `api: 235`, `import: 46`
* *Defense:* `safety: 11`, `doc: 3`, `test: 4`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 49):` gv.h, thread.h, perlstatic.h, crt_externs.h, math.h, zos.h, unistd.h, sv.h...
  * `Imported By (In-Degree: 63):` (Excluded from Brief to save tokens)

### `cpan/Math-BigInt/lib/Math/BigInt.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.142 IQR)
- **Top Global Matches:** file_cluster_0: 15.142, file_cluster_11: 15.373, file_cluster_13: 15.463
- **Magnitude:** 19448.14 | **LOC:** 10480 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 64
- **Risk Profile:** Cognitive Load (63.4353%), Tech Debt (13.6198%)
**Top Internal Functions/Classes:**
  * `bigint` (Impact: 1734.9 | O(2^N) | DB: 64)
  * `brsft` (Impact: 561.2 | O(2^N) | DB: 15)
  * `import` (Impact: 517.9 | O(2^N) | DB: 28)
  * `blsft` (Impact: 475.9 | O(2^N) | DB: 8)
  * `new` (Impact: 450.8 | O(2^N) | DB: 23)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3668`, `structural_boundaries: 1947`, `args: 138`, `func_start: 182`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 3276`, `dead_code: 53`, `planned_debt: 2`, `fragile_debt: 10`, `orphaned_logic: 9`
* *Architecture:* `io: 2`, `api: 2`, `import: 105`
* *Defense:* `safety: 177`, `doc: 291`, `test: 9`, `cleanup: 96`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` instance, non, modular, GCD, sense, Math::SomeClass, overflow, overload...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpan/CPAN/lib/CPAN.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.542 IQR)
- **Top Global Matches:** file_cluster_0: 13.542, file_cluster_13: 13.829, file_cluster_17: 14.021
- **Magnitude:** 18260.16 | **LOC:** 4164 | **CtrlFlow:** 84.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 255
- **Risk Profile:** Cognitive Load (48.0354%), Tech Debt (19.9345%)
**Top Internal Functions/Classes:**
  * `shell` (Impact: 17212.8 | O(2^N) | DB: 255)
    * *Intent:* #-> sub CPAN::shell ;
  * `soft_chdir_with_alternatives` (Impact: 106.7 | O(N^4) | DB: 8)
  * `_redirect` (Impact: 89.3 | O(N^5) | DB: 25)
  * `_uniq` (Impact: 5.3 | O(N^1))
  * `_unredirect` (Impact: 5.0 | O(N^2) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2463`, `structural_boundaries: 457`, `args: 52`, `func_start: 46`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 8`, `state_mutation: 771`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 10`, `duplicate_logic: 2`
* *Architecture:* `io: 52`, `api: 4`, `concurrency: 1`, `import: 125`
* *Defense:* `safety: 41`, `doc: 256`, `test: 1`, `sync_locks: 6`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.221
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` CPAN::Complete, CPAN::Distrostatus, YAML, Net::Config, CPAN::CacheMgr, strict, for, CPAN::Shell...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `cpan/Math-BigInt/lib/Math/BigFloat.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.705 IQR)
- **Top Global Matches:** file_cluster_0: 14.705, file_cluster_11: 14.903, file_cluster_13: 15.02
- **Magnitude:** 17665.78 | **LOC:** 8580 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 259
- **Risk Profile:** Cognitive Load (78.6807%), Tech Debt (27.8613%)
**Top Internal Functions/Classes:**
  * `bexp` (Impact: 6546.0 | O(2^N) | DB: 259)
  * `from_ieee754` (Impact: 493.5 | O(2^N) | DB: 60)
  * `bfdiv` (Impact: 486.2 | O(2^N) | DB: 24)
    * *Intent:* *bdiv = \&bfdiv; *bmod = \&bfmod;
  * `bmuladd` (Impact: 456.6 | O(2^N) | DB: 7)
  * `btdiv` (Impact: 452.3 | O(2^N) | DB: 23)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2615`, `structural_boundaries: 1866`, `args: 56`, `func_start: 116`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 3279`, `dead_code: 21`, `planned_debt: 2`, `fragile_debt: 30`, `orphaned_logic: 4`
* *Architecture:* `io: 2`, `api: 2`, `import: 40`
* *Defense:* `safety: 67`, `doc: 98`, `cleanup: 150`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` sense, overload, Carp, Math::BigRat, point, strict, need, it...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/B/Deparse.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.306 IQR)
- **Top Global Matches:** file_cluster_17: 15.306, file_cluster_0: 15.491, file_cluster_11: 15.553
- **Magnitude:** 17409.3 | **LOC:** 7691 | **CtrlFlow:** 57.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 562
- **Risk Profile:** Cognitive Load (92.262%), Tech Debt (25.4394%)
**Top Internal Functions/Classes:**
  * `next_todo` (Impact: 9014.4 | O(2^N) | DB: 562)
    * *Intent:* # Pop the next sub from the todo list and deparse it
  * `multideref_var_name` (Impact: 1428.6 | O(2^N) | DB: 149)
    * *Intent:* # a simplified version of elem_or_slice_array_name() # for the use of pp_multideref
  * `pp_argelem` (Impact: 539.3 | O(N^3) | DB: 93)
  * `dq_disambiguate` (Impact: 309.8 | O(2^N) | DB: 22)
    * *Intent:* # Join two components of a double-quoted string, disambiguating # "${foo}bar", "${foo}{bar}", "${foo...
  * `pp_null` (Impact: 272.5 | O(N^4) | DB: 65)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2511`, `structural_boundaries: 1879`, `args: 352`, `func_start: 539`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 7`, `state_mutation: 5113`, `dead_code: 23`, `planned_debt: 29`, `fragile_debt: 22`, `orphaned_logic: 8`
* *Architecture:* `io: 50`, `concurrency: 4`, `import: 58`
* *Defense:* `safety: 53`, `doc: 60`, `sync_locks: 2`, `cleanup: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` else, O, keyword, if, arguments, nextstate, prototype, Carp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpan/IO-Compress/lib/IO/Uncompress/AnyUncompress.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.683 IQR)
- **Top Global Matches:** file_cluster_0: 12.683, file_cluster_13: 12.945, file_cluster_17: 13.174
- **Magnitude:** 16007.57 | **LOC:** 1097 | **CtrlFlow:** 77.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (44.1104%), Tech Debt (11.4384%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 582`, `structural_boundaries: 170`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 205`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `api: 5`, `import: 48`
* *Defense:* `safety: 12`, `doc: 97`, `cleanup: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.332
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` effect, IO::Uncompress::Adapter::UnLzip, IO::Uncompress::RawInflate, IO::Uncompress::Gunzip, IO::Uncompress::Adapter::Bunzip2, IO::Uncompress::UnLzop, IO::Uncompress::AnyUncompress, IO::Uncompress::Bunzip2...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pod/perlebcdic.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.482 IQR)
- **Top Global Matches:** file_cluster_8: 12.482, file_cluster_13: 12.687, file_cluster_0: 12.697
- **Magnitude:** 15827.82 | **LOC:** 2021 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (36.8328%), Tech Debt (11.3747%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 88`, `args: 21`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 9`, `state_mutation: 491`, `fragile_debt: 4`
* *Architecture:* `io: 264`, `import: 34`
* *Defense:* `safety: 2`, `doc: 100`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` matter, different, example, it, use, Encode, one, octal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpan/ExtUtils-MakeMaker/lib/ExtUtils/MM_Unix.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.498 IQR)
- **Top Global Matches:** file_cluster_0: 14.498, file_cluster_8: 14.53, file_cluster_13: 14.576
- **Magnitude:** 14063.14 | **LOC:** 4166 | **CtrlFlow:** 65.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 244
- **Risk Profile:** Cognitive Load (56.9784%), Tech Debt (9.0801%)
**Top Internal Functions/Classes:**
  * `find_perl` (Impact: 8097.7 | O(2^N) | DB: 228)
  * `parse_version` (Impact: 3682.5 | O(2^N) | DB: 244)
  * `_xs_make_bs` (Impact: 286.0 | O(N^4) | DB: 51)
  * `c_o` (Impact: 50.1 | O(N^3) | DB: 17)
  * `dynamic_bs` (Impact: 6.7 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1214`, `structural_boundaries: 640`, `args: 98`, `func_start: 108`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 8`, `state_mutation: 1868`, `dead_code: 3`, `fragile_debt: 3`
* *Architecture:* `io: 28`, `api: 1`, `import: 35`
* *Defense:* `safety: 16`, `doc: 203`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ExtUtils::MakeMaker, VMS::Filespec, Cwd, depend, q, Carp, shar, when...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpan/Encode/Encode.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.424 IQR)
- **Top Global Matches:** file_cluster_0: 12.424, file_cluster_13: 12.615, file_cluster_11: 12.881
- **Magnitude:** 13875.84 | **LOC:** 977 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (46.8741%), Tech Debt (18.8266%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 354`, `structural_boundaries: 149`, `args: 13`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 221`, `fragile_debt: 4`
* *Architecture:* `io: 92`, `api: 9`, `import: 37`
* *Defense:* `safety: 7`, `doc: 62`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Carp, strict, it, bytes, constant, Encode, Storable, frivolously...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpan/CPAN/lib/CPAN/FTP.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.632 IQR)
- **Top Global Matches:** file_cluster_0: 13.632, file_cluster_11: 14.203, file_cluster_17: 14.243
- **Magnitude:** 13004.58 | **LOC:** 1324 | **CtrlFlow:** 79.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 321
- **Risk Profile:** Cognitive Load (90.5799%), Tech Debt (12.4415%)
**Top Internal Functions/Classes:**
  * `_ftp_statistics` (Impact: 12249.4 | O(2^N) | DB: 321)
    * *Intent:* #-> sub CPAN::FTP::ftp_statistics # if they want to rewrite, they need to pass in a filehandle
  * `_plus_append_open` (Impact: 34.4 | O(N^2) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1033`, `structural_boundaries: 265`, `args: 27`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 14`, `state_mutation: 698`, `dead_code: 9`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `io: 32`, `import: 13`
* *Defense:* `safety: 20`, `sync_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` eval, success, File::Basename, vars, Net::Ping, shared, Errno, Carp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/DB.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.905 IQR)
- **Top Global Matches:** file_cluster_0: 11.905, file_cluster_13: 12.481, file_cluster_8: 12.499
- **Magnitude:** 11798.48 | **LOC:** 527 | **CtrlFlow:** 79.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (87.8226%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 433`, `structural_boundaries: 115`, `args: 6`, `func_start: 7`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 123`
* *Architecture:* `import: 13`
* *Defense:* `safety: 7`, `test: 100`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` vars, _find_subline, Config, default, events, Scalar::Util, argument, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpan/Archive-Tar/t/02_methods.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.591 IQR)
- **Top Global Matches:** file_cluster_0: 12.591, file_cluster_8: 12.87, file_cluster_13: 12.904
- **Magnitude:** 11344.95 | **LOC:** 909 | **CtrlFlow:** 62.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.1001%), Tech Debt (28.0343%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 187`, `args: 11`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 332`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 5`
* *Architecture:* `io: 5`, `import: 19`
* *Defense:* `safety: 1`, `test: 115`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Cwd, Archive::Tar::Constant, IO::Uncompress::Bunzip2, strict, IO::Zlib, File::Spec::Unix, for, Data::Dumper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Benchmark.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.534 IQR)
- **Top Global Matches:** file_cluster_0: 13.534, file_cluster_17: 13.633, file_cluster_13: 13.7
- **Magnitude:** 11263.87 | **LOC:** 1123 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (55.066%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 139`, `args: 14`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 8`, `state_mutation: 526`, `dead_code: 2`
* *Architecture:* `io: 1`, `api: 7`, `import: 14`
* *Defense:* `safety: 7`, `doc: 45`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` the, other, time, Time::HiRes, Benchmark, subroutine, of, Exporter...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `toke.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.869 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.246 IQR)
- **Top Global Matches:** file_cluster_8: 14.869, file_cluster_11: 14.991, file_cluster_0: 15.047
- **Magnitude:** 11060.52 | **LOC:** 14900 | **CtrlFlow:** 85.9% | **Authorship Centralization:** 87.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 235
- **Risk Profile:** Cognitive Load (93.9452%), Tech Debt (23.9113%)
**Top Internal Functions/Classes:**
  * `yyl_just_a_word` (Impact: 6609.4 | O(2^N) | DB: 235)
  * `Perl_yyerror_pvn` (Impact: 497.1 | O(N^6) | DB: 58)
  * `yyl_fake_eof` (Impact: 300.5 | O(N^6) | DB: 82)
  * `S_new_constant` (Impact: 92.9 | O(N^6) | DB: 26)
  * `S_warn_expect_operator` (Impact: 91.2 | O(N^6) | DB: 21)
    * *Intent:* /* toke.c * * Copyright (C) 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, * 2001, 2002...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1201`, `structural_boundaries: 197`, `args: 2`, `func_start: 45`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 2426`, `dead_code: 7`, `planned_debt: 1`, `fragile_debt: 7`, `orphaned_logic: 15`
* *Architecture:* `io: 14`, `api: 496`
* *Defense:* `safety: 17`, `doc: 14`, `test: 17`, `immutability_locks: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` EXTERN.h, invlist_inline.h, keywords.h, perl.h, feature.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpan/DB_File/t/db-btree.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.054 IQR)
- **Top Global Matches:** file_cluster_0: 14.054, file_cluster_13: 14.07, file_cluster_11: 14.09
- **Magnitude:** 10724.02 | **LOC:** 1668 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (86.6242%), Tech Debt (12.202%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 262`, `args: 25`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 1`, `state_mutation: 668`, `dead_code: 13`, `fragile_debt: 3`
* *Architecture:* `io: 19`, `api: 4`, `import: 59`
* *Defense:* `safety: 43`, `test: 179`, `cleanup: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` File::Temp, seq, put, DB_File, Exporter, Config, Symbol, SubDB...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vms/vms.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.086 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.324 IQR)
- **Top Global Matches:** file_cluster_13: 15.086, file_cluster_8: 15.089, file_cluster_11: 15.184
- **Magnitude:** 10629.44 | **LOC:** 14086 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 588
- **Risk Profile:** Cognitive Load (96.3083%), Tech Debt (9.0327%)
**Top Internal Functions/Classes:**
  * `Perl_vmstrnenv` (Impact: 5248.8 | O(N^6) | DB: 588)
  * `Perl_flex_stat_int` (Impact: 1369.4 | O(N^6) | DB: 207)
    * *Intent:* /* Is vaxc$errno sane? */
  * `copy_expand_vms_filename_escape` (Impact: 118.0 | O(N^5) | DB: 45)
  * `mp_do_vms_realpath` (Impact: 96.3 | O(N^6) | DB: 30)
  * `vms_split_path` (Impact: 66.2 | O(N^3) | DB: 73)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 986`, `structural_boundaries: 198`, `args: 31`, `func_start: 62`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 2`, `state_mutation: 2871`, `dead_code: 9`, `planned_debt: 2`, `fragile_debt: 3`
* *Architecture:* `io: 12`, `api: 496`, `import: 40`
* *Defense:* `safety: 1`, `test: 1`, `immutability_locks: 76`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` rms.h, uaidef.h, devdef.h, kgbdef.h, descrip.h, dvidef.h, strdef.h, float.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `autodoc.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.26 IQR)
- **Top Global Matches:** file_cluster_8: 14.26, file_cluster_13: 14.457, file_cluster_0: 14.46
- **Magnitude:** 10610.78 | **LOC:** 3116 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 96.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 194
- **Risk Profile:** Cognitive Load (95.6079%), Tech Debt (9.249%)
**Top Internal Functions/Classes:**
  * `check_and_add_proto_defn` (Impact: 7818.4 | O(2^N) | DB: 194)
  * `docout` (Impact: 1087.3 | O(N^6) | DB: 142)
    * *Intent:* # output the docs for one function group
  * `output` (Impact: 190.2 | O(N^6) | DB: 23)
  * `format_pod_indexes` (Impact: 25.3 | O(N^3) | DB: 6)
  * `where_from_string` (Impact: 3.9 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 709`, `structural_boundaries: 378`, `args: 21`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 3`, `state_mutation: 1444`, `dead_code: 2`, `fragile_debt: 2`
* *Architecture:* `io: 22`, `import: 21`
* *Defense:* `safety: 3`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` MANIFEST, arguments, apidoc, its, strict, need, it, docs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpan/IO-Compress/bin/zipdetails` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.739 IQR)
- **Top Global Matches:** file_cluster_0: 14.739, file_cluster_13: 14.785, file_cluster_11: 14.824
- **Magnitude:** 10500.38 | **LOC:** 8209 | **CtrlFlow:** 44.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 522
- **Risk Profile:** Cognitive Load (86.9011%), Tech Debt (15.783%)
**Top Internal Functions/Classes:**
  * `OpenVMS_DateTime` (Impact: 2670.6 | O(2^N) | DB: 522)
  * `DecryptionHeader` (Impact: 2209.7 | O(N^6) | DB: 480)
  * `new` (Impact: 538.4 | O(N^6) | DB: 121)
  * `hexValue16` (Impact: 280.0 | O(2^N) | DB: 137)
  * `scanForSignature` (Impact: 79.6 | O(N^5) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1367`, `structural_boundaries: 1740`, `args: 401`, `func_start: 245`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 21`, `state_mutation: 4433`, `dead_code: 41`, `planned_debt: 45`, `fragile_debt: 2`, `orphaned_logic: 5`
* *Architecture:* `io: 10`, `api: 4`, `import: 125`
* *Defense:* `safety: 10`, `doc: 83`, `cleanup: 152`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` truncation, extensible, Devel::Peek, ZIP_GP_FLAG_ENCRYPTED_CD, Getopt::Long, strict, Time::Local, constant...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpan/IO-Compress/lib/IO/Compress/Zip.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.861 IQR)
- **Top Global Matches:** file_cluster_0: 13.861, file_cluster_13: 14.16, file_cluster_11: 14.402
- **Magnitude:** 9969.8 | **LOC:** 2292 | **CtrlFlow:** 82.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 285
- **Risk Profile:** Cognitive Load (53.9805%), Tech Debt (20.4969%)
**Top Internal Functions/Classes:**
  * `canonicalName` (Impact: 8513.9 | O(2^N) | DB: 285)
  * `mkComp` (Impact: 448.6 | O(N^6) | DB: 4)
  * `isMethodAvailable` (Impact: 169.1 | O(N^2) | DB: 2)
  * `beforePayload` (Impact: 57.6 | O(N^3) | DB: 5)
  * `reset` (Impact: 20.2 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1411`, `structural_boundaries: 299`, `args: 24`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 689`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 3`, `orphaned_logic: 4`
* *Architecture:* `io: 36`, `api: 5`, `import: 77`
* *Defense:* `safety: 22`, `doc: 154`, `cleanup: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` effect, filename, these, IO::Compress::Zstd, IO::Compress::Adapter::Zstd, strict, bytes, IO::Compress::Adapter::Lzma...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `cpan/Test-Harness/t/compat/inc-propagation.t` (PERL) | Magnitude: 21.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 20, structural_boundaries: 18, state_mutation: 18, indent_spaces: 15
- `cpan/Test-Simple/t/behavior/no_done_testing.t` (PERL) | Magnitude: 24.24 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 9, branch: 8, structural_boundaries: 6, indent_spaces: 6
- `cpan/Test-Simple/t/modules/Compare/Base.t` (PERL) | Magnitude: 26.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 25, indent_spaces: 19, test: 13, decorators: 12
- `cpan/Test-Simple/t/regression/684-nested_todo_diag.t` (PERL) | Magnitude: 24.34 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: branch: 13, state_mutation: 9, structural_boundaries: 7, indent_spaces: 7
- `lib/Class/Struct.t` (PERL) | Magnitude: 56.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 62, indent_spaces: 47, branch: 45, state_mutation: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `pod/perllexwarn.pod` (PERL) | Magnitude: 13.64 | Delta: **0.191 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, import: 1, events: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `hints/isc.sh` (SHELL) | Magnitude: 24.54 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 18, branch: 2, indent_tabs: 2, structural_boundaries: 1
- `hints/isc_2.sh` (SHELL) | Magnitude: 23.94 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 18, branch: 2, indent_tabs: 2, structural_boundaries: 1
- `cpan/Test-Simple/lib/Test2/Tools/Basic.pm` (PERL) | Magnitude: 0.17 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 108, state_mutation: 66, branch: 57, structural_boundaries: 53
- `t/op/tiearray.t` (PERL) | Magnitude: 222.34 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 180, state_mutation: 131, test: 61, branch: 52
- `cpan/Test-Simple/t/Test2/behavior/Subtest_todo.t` (PERL) | Magnitude: 21.48 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 14, test: 14, pointers: 10, indent_spaces: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `hints/haiku.sh` (SHELL) | Magnitude: 45.48 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 31, reflection_metaprogramming: 9, branch: 8, duplicate_logic: 4
- `pp.h` (C) | Magnitude: 137.02 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 162, state_mutation: 104, indent_spaces: 79, reflection_metaprogramming: 58
- `scope.h` (C) | Magnitude: 75.74 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 114, reflection_metaprogramming: 86, indent_spaces: 68, state_mutation: 54
- `sbox32_hash.h` (C) | Magnitude: 221.86 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 1602, branch: 539, reflection_metaprogramming: 538, indent_spaces: 330
- `hints/altos486.sh` (SHELL) | Magnitude: 2.66 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, safety: 1, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `cpan/ExtUtils-MakeMaker/t/postamble.t` (PERL) | Magnitude: 351.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 29, indent_spaces: 27, state_mutation: 21, structural_boundaries: 20
- `cpan/Test-Simple/lib/Test2/Event/Encoding.pm` (PERL) | Magnitude: 24.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 32, doc: 20, state_mutation: 17, structural_boundaries: 15
- `cpan/Test-Simple/lib/Test2/Tools/Mock.pm` (PERL) | Magnitude: 1.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 268, indent_spaces: 201, structural_boundaries: 158, branch: 147
- `cpan/Text-Tabs/lib/Text/Tabs.pm` (PERL) | Magnitude: 293.84 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 69, branch: 49, indent_tabs: 47, structural_boundaries: 36
- `ext/B/O.pm` (PERL) | Magnitude: 269.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 44, state_mutation: 27, structural_boundaries: 23, indent_tabs: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `cpan/ExtUtils-MakeMaker/t/00compile.t` (PERL) | Magnitude: 33.64 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 18, indent_spaces: 12, branch: 11, structural_boundaries: 10
- `cpan/Test-Harness/t/taint.t` (PERL) | Magnitude: 37.26 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, state_mutation: 18, branch: 17, structural_boundaries: 14
- `t/op/groups.t` (PERL) | Magnitude: 380.4 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 214, state_mutation: 119, structural_boundaries: 74, branch: 70
- `t/op/my.t` (PERL) | Magnitude: 294.74 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 81, indent_spaces: 54, structural_boundaries: 51, test: 44
- `regen/regcharclass_multi_char_folds.pl` (PERL) | Magnitude: 533.42 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 76, state_mutation: 63, branch: 55, structural_boundaries: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `cpan/Scalar-List-Utils/t/dualvar.t` (PERL) | Magnitude: 57.2 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 57, test: 42, state_mutation: 39, branch: 33
- `cpan/Test-Simple/t/Legacy/Regression/637.t` (PERL) | Magnitude: 40.82 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 26, indent_spaces: 20, state_mutation: 18, structural_boundaries: 10
- `os2/OS2/OS2-Process/t/os2_process_kid.t` (PERL) | Magnitude: 44.64 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 23, structural_boundaries: 11, panics_and_aborts: 11, bitwise_ops: 11
- `cpan/Test-Simple/lib/Test2/AsyncSubtest/Hub.pm` (PERL) | Magnitude: 261.32 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 61, branch: 52, indent_spaces: 34, structural_boundaries: 25
- `t/run/switchF2.t` (PERL) | Magnitude: 34.86 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, concurrency: 13, branch: 10, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `Porting/merge-deltas.pl` (PERL) | Magnitude: 473.8 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 162, state_mutation: 56, branch: 55, structural_boundaries: 44
- `cpan/Math-BigInt/t/Math/BigInt/Scalar.pm` (PERL) | Magnitude: 113.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 59, func_start: 46, state_mutation: 42
- `cpan/Socket/Makefile.PL` (PERL) | Magnitude: 64.68 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 171, branch: 53, state_mutation: 38, structural_boundaries: 31
- `cpan/Test-Simple/t/modules/Require/AuthorTesting.t` (PERL) | Magnitude: 14.16 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 8, decorators: 4, test_skip: 4, indent_spaces: 4
- `cpan/Test-Simple/t/modules/Require/AutomatedTesting.t` (PERL) | Magnitude: 14.16 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 8, decorators: 4, test_skip: 4, indent_spaces: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `cop.h` (C) | Magnitude: 119.46 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 132, macros: 76, api: 56, state_mutation: 44
- `perlsdio.h` (C) | Magnitude: 14.56 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 3, macros: 2, branch: 1, ownership: 1
- `cpan/Compress-Raw-Zlib/zlib-src/inflate.h` (C) | Magnitude: 54.48 | Delta: **0.227 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 67, api: 37, pointers: 4, structural_boundaries: 3
- `cpan/Compress-Raw-Zlib/zlib-src/inffast.h` (C) | Magnitude: 11.52 | Delta: **0.884 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: ownership: 2, structural_boundaries: 1, api: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `regen/embed.pl` -> Churn: **100.0%** | Cog Load: 55.774% | Debt: 8.558%
- `toke.c` -> Churn: **94.13%** | Cog Load: 93.9452% | Debt: 23.9113%
- `pod/perldelta.pod` -> Churn: **90.19%** | Cog Load: 4.5155% | Debt: 100.0%
- `perl.h` -> Churn: **84.71%** | Cog Load: 61.4346% | Debt: 12.2747%
- `regexec.c` -> Churn: **78.59%** | Cog Load: 94.512% | Debt: 21.083%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/locale.t` -> **Karl Williamson** (100.0% isolated ownership) | Magnitude: 43709.29
- `lib/Unicode/UCD.t` -> **Unicode Consortium** (100.0% isolated ownership) | Magnitude: 23850.17
- `perl.h` -> **Karl Williamson** (83.6% isolated ownership) | Magnitude: 22844.92
- `cpan/IO-Compress/lib/IO/Uncompress/AnyUncompress.pm` -> **Paul Marquess** (100.0% isolated ownership) | Magnitude: 16007.57
- `pod/perlebcdic.pod` -> **Karl Williamson** (100.0% isolated ownership) | Magnitude: 15827.82

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `cpan/CPAN/lib/CPAN.pm` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9553%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cpan/Test-Simple/t/Legacy/plan.t` -> **Severity: 658.141** (Blast Radius: 6.717 * Doc Risk: 97.9814%)
- `cpan/PerlIO-via-QuotedPrint/t/changes.t` -> **Severity: 444.093** (Blast Radius: 5.957 * Doc Risk: 74.5497%)
- `ext/POSIX/lib/POSIX.pm` -> **Severity: 377.076** (Blast Radius: 8.852 * Doc Risk: 42.5978%)
- `cpan/IO-Compress/t/compress/any.pl` -> **Severity: 337.305** (Blast Radius: 3.45 * Doc Risk: 97.7695%)
- `ext/Errno/t/Errno.t` -> **Severity: 331.076** (Blast Radius: 5.504 * Doc Risk: 60.1518%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
