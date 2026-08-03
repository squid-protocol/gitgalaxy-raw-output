# ARCHITECTURAL_BRIEF: gnupg
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/gnupg` |
| **Timestamp** | `2026-08-03T20:55:37.522810+00:00` |
| **Scan Duration** | `4.53s` |
| **Git Branch** | `master` |
| **Git Commit** | `9673bbc47bc006f360da6ce938c6ea682116c7e2` |
| **Git Remote** | `https://github.com/gpg/gnupg.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 681 malicious artifacts.

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
| Total Artifacts | 1365 |
| Analyzed Artifacts (Scanned) | 1039 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 326 |
| Total LOC | 194282 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 76.1% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7971 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.1799 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.3833 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 71 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 493 | 181448 | 47.4% |
| PLAINTEXT | 335 | 255 | 32.2% |
| SCHEME | 117 | 6651 | 11.3% |
| M4 | 32 | 3787 | 3.1% |
| SHELL | 32 | 1302 | 3.1% |
| MARKDOWN | 13 | 0 | 1.3% |
| XML | 5 | 0 | 0.5% |
| MAKEFILE | 4 | 635 | 0.4% |
| CSS | 2 | 57 | 0.2% |
| PERL | 2 | 30 | 0.2% |
| HTML | 1 | 46 | 0.1% |
| PHP | 1 | 26 | 0.1% |
| PYTHON | 1 | 17 | 0.1% |
| BATCH | 1 | 28 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.58`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 462 | 44.5% |
| Unknown | 255 | 24.5% |
| file_cluster_13 | 216 | 20.8% |
| file_cluster_9 | 8 | 0.8% |
| file_cluster_0 | 2 | 0.2% |
| file_cluster_11 | 1 | 0.1% |
| file_cluster_12 | 1 | 0.1% |
| file_cluster_4 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 93 | 9.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 326*

**Composition by Extension & Reason:**
- `.png`: 48x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 16x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 72 LOC)
- `.po`: 28x Excluded (Unsupported Extension: '.po')
- `.txt`: 20x Excluded (Binary Format Detected), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 874 LOC)
- `.texi`: 24x Excluded (Unsupported Extension: '.texi')
- `.am`: 22x Excluded (Unsupported Extension: '.am')
- `.rc`: 9x Excluded (Unsupported Extension: '.rc'), 6x Unsupported Format (.rc), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 47 LOC)
- `.jpg`: 9x Excluded (Explicitly Denied Extension: '.jpg')
- `.m4`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 105 LOC), 1x Excluded (Machine-Generated Source Code Signature: 70 LOC)
- `.der`: 5x Excluded (Explicitly Denied Extension: '.der')
- `.ico`: 4x Excluded (Explicitly Denied Extension: '.ico')
- `.sh`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.awk`: 4x Excluded (Unsupported Extension: '.awk')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 42.1 | 29.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 34.3 | 24.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 24.8 | 9.1 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 29.6 | 2.3 | 80.0 |
| API Exposure | 0.0 | 18.6 | 8.1 | 10.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 50.0 | 69.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 36.7 | 0.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 92.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.0 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 76.5 | 3.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 63.4 | 93.3 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 44.7 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 1.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `kbx/keyboxd.c` (Hits: 56)
- `tools/gpg-authcode-sign.sh` (Hits: 50)
- `artwork/icons/index.html` (Hits: 49)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **gpg.h** (`g10/gpg.h`) — 67 inbound connections
2. **options.h** (`g10/options.h`) — 59 inbound connections
3. **main.h** (`g10/main.h`) — 49 inbound connections
4. **packet.h** (`g10/packet.h`) — 45 inbound connections
5. **dirmngr.h** (`dirmngr/dirmngr.h`) — 25 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **gpg.c** (`g10/gpg.c`) — 42 outbound dependencies
2. **dns.c** (`dirmngr/dns.c`) — 35 outbound dependencies
3. **dirmngr.c** (`dirmngr/dirmngr.c`) — 34 outbound dependencies
4. **http.c** (`dirmngr/http.c`) — 32 outbound dependencies
5. **sysutils.c** (`common/sysutils.c`) — 29 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `list_one_kinfo` (@ `tools/gpg-card.c`) -> Impact: **4809.5** | LOC: 1806
  * *Intent:* *p = ' ';
- `set_debug` (@ `scd/scdaemon.c`) -> Impact: **4068.7** | LOC: 921
- `keyring_search` (@ `g10/keyring.c`) -> Impact: **4013.8** | LOC: 761
- `parse_list_options` (@ `g10/gpg.c`) -> Impact: **3689.0** | LOC: 1519
- `hash_and_copy_data` (@ `sm/sign.c`) -> Impact: **3465.5** | LOC: 928
- `http_register_tls_ca` (@ `dirmngr/http.c`) -> Impact: **3321.8** | LOC: 1635
- `gc_component_change_options` (@ `tools/gpgconf-comp.c`) -> Impact: **3132.8** | LOC: 672
- `parse_import_options` (@ `g10/import.c`) -> Impact: **3105.7** | LOC: 1494
- `encrypt_crypt` (@ `g10/encrypt.c`) -> Impact: **2045.0** | LOC: 435
- `direct_open` (@ `common/iobuf.c`) -> Impact: **2015.6** | LOC: 552

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `AC_DEFUN` (@ `m4/ksba.m4`) -> **O(2^N) [Recursive]**
  * *Intent:* # unlimited permission to copy and/or distribute it, with or without # modifications, as long as this notice is preserved. # # This file is distribute...
- `AC_DEFUN` (@ `m4/libassuan.m4`) -> **O(2^N) [Recursive]**
  * *Intent:* dnl unlimited permission to copy and/or distribute it, with or without dnl modifications, as long as this notice is preserved. dnl dnl This file is di...
- `AC_DEFUN` (@ `m4/libgcrypt.m4`) -> **O(2^N) [Recursive]**
  * *Intent:* # modifications, as long as this notice is preserved. # # This file is distributed in the hope that it will be useful, but # WITHOUT ANY WARRANTY, to ...
- `getpin_cb` (@ `agent/divert-scd.c`) -> **O(2^N) [Recursive]**
  * *Intent:* *r_val = frame; *r_len = asnlen+digestlen;
- `do_encode_raw_pkcs1` (@ `agent/pksign.c`) -> **O(2^N) [Recursive]**
  * *Intent:* processing to 512. */
- `send_pinentry_environment` (@ `common/asshelp.c`) -> **O(2^N) [Recursive]**
- `gnupg_exec_tool_stream` (@ `common/exectool.c`) -> **O(2^N) [Recursive]**
- `read_and_log_stderr` (@ `common/exectool.c`) -> **O(2^N) [Recursive]**
  * *Intent:* */ #include <config.h> #include <stdio.h> #include <stdlib.h> #include <string.h> #include <stdarg.h> #include <errno.h> #include <assert.h> #include ...
- `default_homedir` (@ `common/homedir.c`) -> **O(2^N) [Recursive]**
- `direct_open` (@ `common/iobuf.c`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `list_one_kinfo` (@ `tools/gpg-card.c`) -> DB Complexity: **443**
  * *Intent:* *p = ' ';
- `http_register_tls_ca` (@ `dirmngr/http.c`) -> DB Complexity: **366**
- `parse_list_options` (@ `g10/gpg.c`) -> DB Complexity: **359**
- `parse_import_options` (@ `g10/import.c`) -> DB Complexity: **286**
- `dns_d_cleave` (@ `dirmngr/dns.c`) -> DB Complexity: **230**
- `hash_and_copy_data` (@ `sm/sign.c`) -> DB Complexity: **229**
- `main` (@ `agent/gpg-agent.c`) -> DB Complexity: **227**
  * *Intent:* #endif /*!HAVE_W32_SYSTEM*/
- `gc_component_change_options` (@ `tools/gpgconf-comp.c`) -> DB Complexity: **216**
- `send_apdu_ccid` (@ `scd/apdu.c`) -> DB Complexity: **202**
- `get_best_pubkey_byname` (@ `g10/getkey.c`) -> DB Complexity: **195**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `tests/openpgp/samplemsgs` | 60 | 295001.0 | 0.0% | 0.0% |
| `tests/openpgp/privkeys` | 47 | 235000.0 | 0.0% | 0.0% |
| `tests/openpgp/samplekeys` | 37 | 180001.0 | 0.0% | 0.0% |
| `tests/openpgp` | 99 | 121434.73 | 5.08% | 0.0% |
| `g10` | 101 | 117569.5 | 54.54% | 35.54% |
| `tests/cms` | 38 | 115406.38 | 2.93% | 0.0% |
| `tests/cms/samplekeys` | 24 | 115001.0 | 0.0% | 0.0% |
| `scd` | 23 | 61993.6 | 55.49% | 16.78% |
| `tests/openpgp/trust-pgp` | 12 | 55039.76 | 0.32% | 0.0% |
| `dirmngr` | 66 | 54651.75 | 45.48% | 28.26% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `common/isascii.c` -> **100.0%** Exposure
- `common/logging.h` -> **100.0%** Exposure
- `common/t-support.c` -> **100.0%** Exposure
- `common/xasprintf.c` -> **100.0%** Exposure
- `dirmngr/t-support.c` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `agent/call-daemon.c` -> **100.0%** Exposure
- `agent/call-pinentry.c` -> **100.0%** Exposure
- `agent/call-scd.c` -> **100.0%** Exposure
- `agent/command-ssh.c` -> **100.0%** Exposure
- `agent/command.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/gpgscm/ffi.c` -> **54** Orphaned Functions | **0** Duplicates
- `dirmngr/dns.c` -> **47** Orphaned Functions | **0** Duplicates
- `scd/iso7816.c` -> **32** Orphaned Functions | **0** Duplicates
- `g10/gpgv.c` -> **31** Orphaned Functions | **0** Duplicates
- `common/stringhelp.c` -> **24** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`agent/command-ssh.c`** -> AI Confidence: **99.48%**
2. **`agent/command.c`** -> AI Confidence: **99.48%**
3. **`agent/cvt-openpgp.c`** -> AI Confidence: **99.48%**
4. **`agent/divert-scd.c`** -> AI Confidence: **99.48%**
5. **`agent/findkey.c`** -> AI Confidence: **99.48%**
6. **`agent/genkey.c`** -> AI Confidence: **99.48%**
7. **`agent/gpg-agent.c`** -> AI Confidence: **99.48%**
8. **`agent/pkdecrypt.c`** -> AI Confidence: **99.48%**
9. **`agent/pksign.c`** -> AI Confidence: **99.48%**
10. **`agent/preset-passphrase.c`** -> AI Confidence: **99.48%**
11. **`agent/trustlist.c`** -> AI Confidence: **99.48%**
12. **`common/asshelp.c`** -> AI Confidence: **99.48%**
13. **`common/audit.c`** -> AI Confidence: **99.48%**
14. **`common/comopt.c`** -> AI Confidence: **99.48%**
15. **`common/compliance.c`** -> AI Confidence: **99.48%**
16. **`common/mkdir_p.c`** -> AI Confidence: **99.48%**
17. **`common/recsel.c`** -> AI Confidence: **99.48%**
18. **`common/ssh-utils.c`** -> AI Confidence: **99.48%**
19. **`common/t-exechelp.c`** -> AI Confidence: **99.48%**
20. **`common/t-iobuf.c`** -> AI Confidence: **99.48%**
21. **`common/t-session-env.c`** -> AI Confidence: **99.48%**
22. **`common/t-ssh-utils.c`** -> AI Confidence: **99.48%**
23. **`common/t-stringhelp.c`** -> AI Confidence: **99.48%**
24. **`common/t-w32-cmdline.c`** -> AI Confidence: **99.48%**
25. **`common/zb32.c`** -> AI Confidence: **99.48%**
26. **`dirmngr/crlcache.c`** -> AI Confidence: **99.48%**
27. **`dirmngr/dirmngr-client.c`** -> AI Confidence: **99.48%**
28. **`dirmngr/dirmngr.c`** -> AI Confidence: **99.48%**
29. **`dirmngr/dirmngr_ldap.c`** -> AI Confidence: **99.48%**
30. **`dirmngr/ks-action.c`** -> AI Confidence: **99.48%**
31. **`dirmngr/ks-engine-hkp.c`** -> AI Confidence: **99.48%**
32. **`dirmngr/ks-engine-http.c`** -> AI Confidence: **99.48%**
33. **`dirmngr/ks-engine-ldap.c`** -> AI Confidence: **99.48%**
34. **`dirmngr/ldap-misc.c`** -> AI Confidence: **99.48%**
35. **`dirmngr/ldap.c`** -> AI Confidence: **99.48%**
36. **`dirmngr/loadswdb.c`** -> AI Confidence: **99.48%**
37. **`dirmngr/ocsp.c`** -> AI Confidence: **99.48%**
38. **`dirmngr/server.c`** -> AI Confidence: **99.48%**
39. **`dirmngr/t-http.c`** -> AI Confidence: **99.48%**
40. **`dirmngr/validate.c`** -> AI Confidence: **99.48%**
41. **`doc/mkdefsinc.c`** -> AI Confidence: **99.48%**
42. **`g10/armor.c`** -> AI Confidence: **99.48%**
43. **`g10/call-keyboxd.c`** -> AI Confidence: **99.48%**
44. **`g10/card-util.c`** -> AI Confidence: **99.48%**
45. **`g10/cipher-aead.c`** -> AI Confidence: **99.48%**
46. **`g10/cipher-cfb.c`** -> AI Confidence: **99.48%**
47. **`g10/compress-bz2.c`** -> AI Confidence: **99.48%**
48. **`g10/compress.c`** -> AI Confidence: **99.48%**
49. **`g10/dearmor.c`** -> AI Confidence: **99.48%**
50. **`g10/decrypt-data.c`** -> AI Confidence: **99.48%**
51. **`g10/delkey.c`** -> AI Confidence: **99.48%**
52. **`g10/encrypt.c`** -> AI Confidence: **99.48%**
53. **`g10/export.c`** -> AI Confidence: **99.48%**
54. **`g10/getkey.c`** -> AI Confidence: **99.48%**
55. **`g10/gpg.c`** -> AI Confidence: **99.48%**
56. **`g10/gpgsql.c`** -> AI Confidence: **99.48%**
57. **`g10/helptext.c`** -> AI Confidence: **99.48%**
58. **`g10/import.c`** -> AI Confidence: **99.48%**
59. **`g10/kbnode.c`** -> AI Confidence: **99.48%**
60. **`g10/key-check.c`** -> AI Confidence: **99.48%**
61. **`g10/key-clean.c`** -> AI Confidence: **99.48%**
62. **`g10/keydb.c`** -> AI Confidence: **99.48%**
63. **`g10/keyedit.c`** -> AI Confidence: **99.48%**
64. **`g10/keyid.c`** -> AI Confidence: **99.48%**
65. **`g10/keylist.c`** -> AI Confidence: **99.48%**
66. **`g10/keyring.c`** -> AI Confidence: **99.48%**
67. **`g10/keyserver.c`** -> AI Confidence: **99.48%**
68. **`g10/mainproc.c`** -> AI Confidence: **99.48%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `agent/t-protect.c` -> **100.0%** Exposure
- `common/t-convert.c` -> **100.0%** Exposure
- `g13/t-g13tuple.c` -> **0.9014%** Exposure
- `common/t-sexputil.c` -> **0.0003%** Exposure
- `scd/app-p15.c` -> **0.0001%** Exposure
### Exploit Generation Surface
- `tests/gpgscm/init.scm` -> **100.0%** Exposure
- `tests/gpgscm/repl.scm` -> **100.0%** Exposure
- `tests/gpgscm/tests.scm` -> **100.0%** Exposure
- `tests/openpgp/ecc.scm` -> **99.9999%** Exposure
- `tests/fake-pinentries/fake-pinentry.pl` -> **88.8729%** Exposure
### Weaponizable Injection Vectors
- `dirmngr/ks-engine-kdns.c` -> **100.0%** Exposure
- `tests/gpgscm/init.scm` -> **100.0%** Exposure
- `tests/gpgscm/repl.scm` -> **100.0%** Exposure
- `tests/gpgscm/tests.scm` -> **100.0%** Exposure
- `tests/openpgp/default-key.scm` -> **100.0%** Exposure
### Raw Memory Manipulation
- `agent/agent.h` -> **10.0%** Exposure
- `common/iobuf.c` -> **10.0%** Exposure
- `common/ksba-io-support.c` -> **10.0%** Exposure
- `common/tlv-parser.c` -> **10.0%** Exposure
- `dirmngr/dns.c` -> **10.0%** Exposure
### Hardcoded Payload Artifacts
- `tools/gpg-card.c` -> **100.0%** Exposure
- `tests/openpgp/ecc.scm` -> **100.0%** Exposure
- `tests/openpgp/signed-messages.scm` -> **100.0%** Exposure
- `tools/der-to-pem` -> **100.0%** Exposure
- `tests/openpgp/armor.scm` -> **40.0688%** Exposure
### Algorithmic DoS Exposure
- `agent/cache.c` -> **100.0%** Exposure
- `agent/call-daemon.c` -> **100.0%** Exposure
- `agent/call-pinentry.c` -> **100.0%** Exposure
- `agent/call-scd.c` -> **100.0%** Exposure
- `agent/call-tpm2d.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `20` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3628` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `common/percent.c` (C) -> Cumulative Risk: **808.4**
- **Archetype:** `file_cluster_13` (Distance: 14.836 IQR)
- **Magnitude:** 700.82 | **LOC:** 323 | **CtrlFlow:** 84.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `percent_data_escape` (Impact: 211.7), `percent_plus_escape` (Impact: 55.6), `do_unescape` (Impact: 46.0)

### 2. `common/stringhelp.c` (C) -> Cumulative Risk: **802.98**
- **Archetype:** `file_cluster_13` (Distance: 14.569 IQR)
- **Magnitude:** 1660.96 | **LOC:** 1889 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `do_make_filename` (Impact: 330.1), `strsep` (Impact: 69.1), `compare_filenames` (Impact: 56.5)

### 3. `dirmngr/ks-action.c` (C) -> Cumulative Risk: **791.81**
- **Archetype:** `file_cluster_13` (Distance: 13.721 IQR)
- **Magnitude:** 1292.78 | **LOC:** 685 | **CtrlFlow:** 86.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `ks_action_get` (Impact: 253.5), `ks_action_parse_uri` (Impact: 111.4), `ks_action_put` (Impact: 87.9)

### 4. `dirmngr/domaininfo.c` (C) -> Cumulative Risk: **790.13**
- **Archetype:** `file_cluster_8` (Distance: 13.55 IQR)
- **Magnitude:** 331.06 | **LOC:** 380 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (97.9826%)
- **Heaviest Functions:** `domaininfo_is_wkd_not_supported` (Impact: 27.6), `domaininfo_print_stats` (Impact: 23.9), `hash_domain` (Impact: 17.8)

### 5. `common/tlv-parser.c` (C) -> Cumulative Risk: **785.98**
- **Archetype:** `file_cluster_8` (Distance: 14.079 IQR)
- **Magnitude:** 1206.86 | **LOC:** 828 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_tlv_parser_next` (Impact: 144.8), `cram_octet_string` (Impact: 112.6), `_tlv_parser_dump_state` (Impact: 47.7)

### 6. `g10/armor.c` (C) -> Cumulative Risk: **778.82**
- **Archetype:** `file_cluster_13` (Distance: 14.181 IQR)
- **Magnitude:** 1268.66 | **LOC:** 1623 | **CtrlFlow:** 83.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `armor_filter` (Impact: 100.5), `check_input` (Impact: 95.0), `parse_hash_header` (Impact: 80.4)

### 7. `agent/cvt-openpgp.c` (C) -> Cumulative Risk: **778.51**
- **Archetype:** `file_cluster_8` (Distance: 14.035 IQR)
- **Magnitude:** 2367.3 | **LOC:** 1524 | **CtrlFlow:** 87.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `convert_from_openpgp_main` (Impact: 475.1), `get_keygrip` (Impact: 159.3), `extract_private_key` (Impact: 128.9)

### 8. `g10/free-packet.c` (C) -> Cumulative Risk: **778.21**
- **Archetype:** `file_cluster_8` (Distance: 13.469 IQR)
- **Magnitude:** 478.2 | **LOC:** 640 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `copy_public_key` (Impact: 36.3), `cmp_user_ids` (Impact: 14.7), `release_public_key_parts` (Impact: 13.5)

### 9. `sm/server.c` (C) -> Cumulative Risk: **778.01**
- **Archetype:** `file_cluster_8` (Distance: 13.351 IQR)
- **Magnitude:** 1926.32 | **LOC:** 1705 | **CtrlFlow:** 75.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (99.9949%)
- **Heaviest Functions:** `gpgsm_status2` (Impact: 156.2), `cmd_getinfo` (Impact: 122.4), `do_listkeys` (Impact: 101.3)

### 10. `common/sexputil.c` (C) -> Cumulative Risk: **774.97**
- **Archetype:** `file_cluster_13` (Distance: 13.496 IQR)
- **Magnitude:** 655.02 | **LOC:** 1240 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `pubkey_algo_string` (Impact: 42.0), `keygrip_from_canon_sexp` (Impact: 28.9), `get_pk_algo_from_key` (Impact: 28.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `scd/ccid-driver.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.015 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.982 IQR)
- **Top Global Matches:** file_cluster_8: 14.015, file_cluster_13: 14.208, file_cluster_11: 14.303
- **Magnitude:** 26831.32 | **LOC:** 4082 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (80.3737%), Tech Debt (9.9363%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 484`, `structural_boundaries: 154`, `args: 24`, `func_start: 35`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1381`, `fragile_debt: 3`
* *Architecture:* `io: 1`, `api: 321`, `import: 16`
* *Defense:* `safety: 24`, `test: 2`, `immutability_locks: 18`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` scdaemon.h, errno.h, libusb.h, time.h, stdio.h, npth.h, stat.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/gpgscm/init.scm` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.972 IQR)
- **Top Global Matches:** file_cluster_8: 9.972, file_cluster_7: 10.58, file_cluster_17: 10.791
- **Magnitude:** 13186.23 | **LOC:** 827 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.1617%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 66`, `args: 130`, `func_start: 129`
* *Risk/State:* `high_risk_execution: 8`, `state_mutation: 23`, `fragile_debt: 4`
* *Architecture:* `io: 24`
* *Defense:* `safety: 12`, `doc: 14`, `immutability_locks: 9`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/gpgscm/tests.scm` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.016 IQR)
- **Top Global Matches:** file_cluster_8: 10.016, file_cluster_17: 10.597, file_cluster_7: 10.743
- **Magnitude:** 10354.38 | **LOC:** 887 | **CtrlFlow:** 60.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.6137%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 63`, `args: 104`, `func_start: 102`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 5`, `state_mutation: 42`, `fragile_debt: 18`
* *Architecture:* `io: 19`
* *Defense:* `safety: 14`, `test: 6`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sm/minip12.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.679 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.965 IQR)
- **Top Global Matches:** file_cluster_8: 14.679, file_cluster_12: 14.731, file_cluster_11: 14.774
- **Magnitude:** 6933.04 | **LOC:** 3203 | **CtrlFlow:** 89.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 88
- **Risk Profile:** Cognitive Load (99.6934%), Tech Debt (11.7887%)
**Top Internal Functions/Classes:**
  * `parse_bag_encrypted_data` (Impact: 1724.2 | O(N^6) | DB: 88)
  * `parse_shrouded_key_bag` (Impact: 1455.1 | O(N^6) | DB: 86)
  * `parse_bag_data` (Impact: 244.6 | O(N^5) | DB: 18)
  * `string_to_key` (Impact: 183.0 | O(N^6) | DB: 34)
  * `parse_cert_bag` (Impact: 142.9 | O(N^3) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 879`, `structural_boundaries: 100`, `args: 18`, `func_start: 25`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1838`, `fragile_debt: 3`, `orphaned_logic: 3`
* *Architecture:* `io: 5`, `api: 547`, `import: 13`
* *Defense:* `safety: 79`, `immutability_locks: 79`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` gcrypt.h, minip12.h, errno.h, stdio.h, logging.h, utf8conv.h, openpgpdefs.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/gpg.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.807 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.315 IQR)
- **Top Global Matches:** file_cluster_8: 13.807, file_cluster_13: 13.989, file_cluster_7: 14.133
- **Magnitude:** 6395.44 | **LOC:** 6035 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 359
- **Risk Profile:** Cognitive Load (94.0875%), Tech Debt (21.403%)
**Top Internal Functions/Classes:**
  * `parse_list_options` (Impact: 3689.0 | O(N^6) | DB: 359)
  * `list_config` (Impact: 274.5 | O(N^6) | DB: 30)
  * `print_mds` (Impact: 169.8 | O(N^4) | DB: 4)
  * `open_info_file` (Impact: 147.8 | O(N^2) | DB: 13)
  * `g10_exit` (Impact: 40.0 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 881`, `structural_boundaries: 44`, `args: 16`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 1524`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 10`, `orphaned_logic: 8`
* *Architecture:* `io: 15`, `api: 292`, `import: 42`
* *Defense:* `safety: 6`, `doc: 1`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` zb32.h, gc-opt-flags.h, iobuf.h, objcache.h, status.h, assuan.h, filter.h, config.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scd/app-p15.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.742 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.42 IQR)
- **Top Global Matches:** file_cluster_8: 14.742, file_cluster_11: 14.885, file_cluster_13: 14.911
- **Magnitude:** 5967.96 | **LOC:** 6743 | **CtrlFlow:** 89.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 113
- **Risk Profile:** Cognitive Load (89.082%), Tech Debt (19.1893%)
**Top Internal Functions/Classes:**
  * `read_ef_pukdf` (Impact: 737.5 | O(N^6) | DB: 113)
    * *Intent:* ;
  * `read_ef_prkdf` (Impact: 675.8 | O(N^6) | DB: 106)
    * *Intent:* /* Info used for AUTH_TYPE_AUTHKEY: */
  * `parse_common_key_attr` (Impact: 553.8 | O(N^6) | DB: 54)
  * `do_getattr` (Impact: 341.1 | O(N^6) | DB: 35)
  * `app_select_p15` (Impact: 181.8 | O(N^6) | DB: 62)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1001`, `structural_boundaries: 120`, `args: 8`, `func_start: 14`, `class_start: 9`
* *Risk/State:* `state_mutation: 2382`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 9`, `orphaned_logic: 4`
* *Architecture:* `api: 490`, `import: 13`
* *Defense:* `safety: 47`, `immutability_locks: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` scdaemon.h, errno.h, time.h, host2net.h, stdio.h, openpgpdefs.h, string.h, iso7816.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/keyring.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.724 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.651 IQR)
- **Top Global Matches:** file_cluster_8: 13.724, file_cluster_13: 13.76, file_cluster_11: 13.879
- **Magnitude:** 5961.28 | **LOC:** 1761 | **CtrlFlow:** 81.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 175
- **Risk Profile:** Cognitive Load (96.5246%), Tech Debt (35.9286%)
**Top Internal Functions/Classes:**
  * `keyring_search` (Impact: 4013.8 | O(2^N) | DB: 175)
  * `keyring_get_keyblock` (Impact: 385.4 | O(2^N) | DB: 36)
  * `compare_name` (Impact: 269.3 | O(N^6) | DB: 19)
    * *Intent:* /* close this one otherwise we will lose the position for
  * `keyring_lock` (Impact: 90.5 | O(N^6) | DB: 12)
  * `prepare_search` (Impact: 70.0 | O(N^6) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 411`, `structural_boundaries: 93`, `args: 10`, `func_start: 25`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 776`, `dead_code: 2`, `fragile_debt: 7`, `orphaned_logic: 5`
* *Architecture:* `io: 11`, `api: 241`, `import: 17`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` keyring.h, keydb.h, errno.h, options.h, stdio.h, stat.h, string.h, gpg.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/parse-packet.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.37 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.678 IQR)
- **Top Global Matches:** file_cluster_8: 14.37, file_cluster_13: 14.564, file_cluster_11: 14.602
- **Magnitude:** 5889.28 | **LOC:** 3990 | **CtrlFlow:** 91.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 93
- **Risk Profile:** Cognitive Load (90.2728%), Tech Debt (12.5996%)
**Top Internal Functions/Classes:**
  * `dump_sig_subpkt` (Impact: 1221.5 | O(N^6) | DB: 54)
  * `parse_key` (Impact: 465.1 | O(N^6) | DB: 80)
    * *Intent:* nprinted = 1; /*(we use (nprinted-1) later.)*/
  * `parse_signature` (Impact: 393.9 | O(N^6) | DB: 93)
  * `set_packet_list_mode` (Impact: 336.4 | O(N^4) | DB: 40)
  * `enum_sig_subpkt` (Impact: 165.6 | O(N^5) | DB: 32)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 829`, `structural_boundaries: 82`, `args: 6`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1854`, `fragile_debt: 4`, `orphaned_logic: 2`
* *Architecture:* `api: 436`, `import: 15`
* *Defense:* `safety: 20`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` photoid.h, options.h, host2net.h, stdio.h, iobuf.h, gpg.h, string.h, i18n.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/keyedit.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.355 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.713 IQR)
- **Top Global Matches:** file_cluster_8: 14.355, file_cluster_13: 14.521, file_cluster_11: 14.605
- **Magnitude:** 5883.84 | **LOC:** 7228 | **CtrlFlow:** 89.2% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 118
- **Risk Profile:** Cognitive Load (83.5685%), Tech Debt (19.1486%)
**Top Internal Functions/Classes:**
  * `trustsig_prompt` (Impact: 1078.8 | O(2^N) | DB: 118)
  * `keyedit_print_one_sig` (Impact: 237.0 | O(N^6) | DB: 17)
  * `keyedit_quick_revsig` (Impact: 230.9 | O(N^6) | DB: 59)
  * `parse_trustsig_string` (Impact: 211.7 | O(N^5) | DB: 23)
  * `menu_revsig` (Impact: 195.2 | O(N^6) | DB: 44)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 903`, `structural_boundaries: 109`, `args: 2`, `func_start: 43`, `class_start: 12`
* *Risk/State:* `state_mutation: 1876`, `dead_code: 3`, `planned_debt: 6`, `fragile_debt: 6`, `orphaned_logic: 8`
* *Architecture:* `api: 461`, `import: 29`
* *Defense:* `safety: 3`, `immutability_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` iobuf.h, status.h, filter.h, config.h, ctype.h, key-clean.h, keyserver-internal.h, key-check.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/import.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.115 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.629 IQR)
- **Top Global Matches:** file_cluster_8: 14.115, file_cluster_13: 14.193, file_cluster_11: 14.334
- **Magnitude:** 5762.06 | **LOC:** 4946 | **CtrlFlow:** 87.9% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 286
- **Risk Profile:** Cognitive Load (95.3286%), Tech Debt (37.608%)
**Top Internal Functions/Classes:**
  * `parse_import_options` (Impact: 3105.7 | O(N^6) | DB: 286)
  * `import_secret_one` (Impact: 1107.7 | O(N^6) | DB: 73)
  * `import_matching_seckeys` (Impact: 73.5 | O(N^6) | DB: 21)
  * `do_transfer` (Impact: 37.4 | O(N^6) | DB: 11)
  * `cleanup_import_globals` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 569`, `structural_boundaries: 78`, `args: 6`, `func_start: 24`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1077`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 13`, `orphaned_logic: 2`
* *Architecture:* `io: 4`, `api: 322`, `import: 23`
* *Defense:* `safety: 25`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` status.h, config.h, recsel.h, key-clean.h, keyserver-internal.h, key-check.h, stdlib.h, packet.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dirmngr/http.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.388 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.351 IQR)
- **Top Global Matches:** file_cluster_8: 14.388, file_cluster_13: 14.397, file_cluster_11: 14.561
- **Magnitude:** 5082.16 | **LOC:** 4607 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 366
- **Risk Profile:** Cognitive Load (96.5774%), Tech Debt (13.2252%)
**Top Internal Functions/Classes:**
  * `http_register_tls_ca` (Impact: 3321.8 | O(N^6) | DB: 366)
  * `make_header_line` (Impact: 35.6 | O(N^4) | DB: 35)
  * `init_sockets` (Impact: 23.0 | O(N^4) | DB: 8)
  * `my_ntbtls_verify_cb` (Impact: 21.8 | O(N^6) | DB: 1)
  * `_my_socket_new` (Impact: 14.9 | O(N^3) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 469`, `structural_boundaries: 168`, `args: 27`, `func_start: 47`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1213`, `planned_debt: 1`, `fragile_debt: 3`, `orphaned_logic: 2`
* *Architecture:* `io: 8`, `api: 380`, `import: 32`
* *Defense:* `safety: 21`, `immutability_locks: 66`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` winhttp.h, http-common.h, stdarg.h, security.h, netdb.h, dns-stuff.h, assuan.h, config.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dirmngr/sks-keyservers.netCA.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dirmngr/tls-ca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/com-certs.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/samplekeys.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/distsigkey.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/pubring.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/t-keydb-get-keyblock.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `g10/t-stutter-data.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/cert_cci_sphinx_ca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/cert_cci_test_wzs.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/cert_cci_test_zs.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/cert_cci_user02.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/cert_cci_user03.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cms/cert_cci_user04.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `dirmngr/dns.h` (C) | Magnitude: 472.34 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 550, api: 392, indent_tabs: 273, args: 216
- `artwork/icons/index.html` (HTML) | Magnitude: 15.92 | Delta: **0.143 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 49, structural_boundaries: 35, decorators: 28, indent_tabs: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `dirmngr/dns.c` (C) | Magnitude: 4854.16 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 2107, state_mutation: 2018, pointers: 1652, branch: 848

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `regexp/utf8.h` (C) | Magnitude: 25.54 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 15, api: 6, doc: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `agent/trustlist.c` (C) | Magnitude: 762.96 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 429, state_mutation: 394, branch: 165, pointers: 105
- `dirmngr/ocsp.c` (C) | Magnitude: 783.9 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 368, state_mutation: 272, branch: 113, api: 76
- `sm/fingerprint.c` (C) | Magnitude: 464.02 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 317, state_mutation: 216, api: 105, branch: 63
- `tests/pkits/import-all-certs` (SHELL) | Magnitude: 5.65 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, branch: 21, safety_bypasses: 18, state_mutation: 9
- `g10/export.c` (C) | Magnitude: 4124.24 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 1563, state_mutation: 1010, branch: 536, pointers: 462

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/tpm2dtests/start_sw_tpm.sh` (SHELL) | Magnitude: 44.38 | Delta: **0.341 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 24, branch: 12, state_mutation: 9, io: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `dirmngr/ks-action.c` (C) | Magnitude: 1292.78 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 414, indent_spaces: 401, branch: 192, pointers: 156
- `g10/keylist.c` (C) | Magnitude: 2361.24 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 709, state_mutation: 563, branch: 370, pointers: 228
- `common/asshelp.c` (C) | Magnitude: 1472.48 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 416, state_mutation: 282, api: 125, branch: 99
- `g10/call-agent.c` (C) | Magnitude: 4040.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1201, state_mutation: 1085, branch: 451, pointers: 432
- `agent/cache.c` (C) | Magnitude: 424.06 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 185, indent_spaces: 171, pointers: 73, branch: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `g13/create.h` (C) | Magnitude: 17.64 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 5, api: 4, structural_boundaries: 2, safety: 2
- `g10/objcache.h` (C) | Magnitude: 17.64 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 8, api: 4, structural_boundaries: 3, safety: 2
- `kbx/keybox-defs.h` (C) | Magnitude: 94.04 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 86, indent_spaces: 62, pointers: 51, structural_boundaries: 26
- `scd/atr.h` (C) | Magnitude: 13.08 | Delta: **0.168 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 3, macros: 2, structural_boundaries: 1, args: 1
- `tests/pkits/inittests` (SHELL) | Magnitude: 5.3 | Delta: **0.195 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: io: 30, branch: 21, indent_spaces: 20, structural_boundaries: 12

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `agent/pkdecrypt.c` -> Churn: **57.14%** | Cog Load: 87.1177% | Debt: 15.5168%
- `g10/call-agent.c` -> Churn: **55.21%** | Cog Load: 95.0516% | Debt: 16.4554%
- `g10/keyedit.c` -> Churn: **51.37%** | Cog Load: 83.5685% | Debt: 19.1486%
- `g10/armor.c` -> Churn: **51.33%** | Cog Load: 72.7703% | Debt: 48.8917%
- `sm/gpgsm.c` -> Churn: **51.33%** | Cog Load: 76.6596% | Debt: 20.0186%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/gpgscm/tests.scm` -> **Joshua Frommholz** (100.0% isolated ownership) | Magnitude: 10354.38
- `scd/app-p15.c` -> **Mario Haustein** (100.0% isolated ownership) | Magnitude: 5967.96
- `g10/keyring.c` -> **NIIBE Yutaka** (100.0% isolated ownership) | Magnitude: 5961.28
- `g10/parse-packet.c` -> **Werner Koch** (100.0% isolated ownership) | Magnitude: 5889.28
- `dirmngr/dns-stuff.c` -> **NIIBE Yutaka** (100.0% isolated ownership) | Magnitude: 4933.6

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `common/tlv.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `g10/packet.h` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 12.0693%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `g10/tofu.h` -> **Severity: 0.406** (Embedded: 0.0307 * Error Risk: 13.2233%)
- `common/openpgpdefs.h` -> **Severity: 0.351** (Embedded: 0.0067 * Error Risk: 52.0821%)
- `g10/options.h` -> **Severity: 0.299** (Embedded: 0.0568 * Error Risk: 5.2691%)
- `g10/packet.h` -> **Severity: 0.223** (Embedded: 0.0475 * Error Risk: 4.6902%)
- `dirmngr/ldapserver.h` -> **Severity: 0.175** (Embedded: 0.0058 * Error Risk: 30.2364%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `agent/agent.h` -> **Severity: 1349.6** (Blast Radius: 13.496 * Doc Risk: 100.0%)
- `g10/gpg.h` -> **Severity: 1205.199** (Blast Radius: 12.052 * Doc Risk: 99.9999%)
- `sm/gpgsm.h` -> **Severity: 1161.1** (Blast Radius: 11.611 * Doc Risk: 100.0%)
- `g10/dek.h` -> **Severity: 1102.546** (Blast Radius: 11.813 * Doc Risk: 93.3333%)
- `g10/packet.h` -> **Severity: 1061.5** (Blast Radius: 10.615 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
