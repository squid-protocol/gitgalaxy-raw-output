# ARCHITECTURAL_BRIEF: gnupg
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/gnupg` |
| **Timestamp** | `2026-08-07T04:59:20.242583+00:00` |
| **Scan Duration** | `4.32s` |
| **Git Branch** | `master` |
| **Git Commit** | `9673bbc47bc006f360da6ce938c6ea682116c7e2` |
| **Git Remote** | `https://github.com/gpg/gnupg.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 681 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
| Cognitive Load Exposure | 0.0 | 100.0 | 42.0 | 29.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 54.2 | 78.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 26.2 | 9.9 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 26.4 | 2.3 | 80.0 |
| API Exposure | 0.0 | 18.6 | 8.1 | 10.1 | 0.0 |
| Concurrency Exposure | 0.0 | 99.9 | 0.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 50.0 | 69.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 36.7 | 0.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 92.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.8 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 77.6 | 3.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 58.7 | 79.8 | 0.0 |
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

- `list_one_kinfo` (@ `tools/gpg-card.c`) -> Impact: **1438.6** | LOC: 1806
  * *Intent:* *p = ' ';
- `parse_list_options` (@ `g10/gpg.c`) -> Impact: **1108.3** | LOC: 1519
- `http_register_tls_ca` (@ `dirmngr/http.c`) -> Impact: **1007.5** | LOC: 1635
- `parse_import_options` (@ `g10/import.c`) -> Impact: **940.7** | LOC: 1494
- `http_raw_connect` (@ `dirmngr/http.c`) -> Impact: **884.2** | LOC: 1565
- `dns_d_cleave` (@ `dirmngr/dns.c`) -> Impact: **676.0** | LOC: 1221
- `read_block` (@ `g10/import.c`) -> Impact: **674.7** | LOC: 1161
- `set_debug` (@ `scd/scdaemon.c`) -> Impact: **620.7** | LOC: 921
- `keyring_search` (@ `g10/keyring.c`) -> Impact: **606.0** | LOC: 761
- `send_apdu_ccid` (@ `scd/apdu.c`) -> Impact: **598.8** | LOC: 811

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `tests/openpgp/samplemsgs` | 60 | 295001.0 | 0.0% | 0.0% |
| `tests/openpgp/privkeys` | 47 | 235000.0 | 0.0% | 0.0% |
| `tests/openpgp/samplekeys` | 37 | 180001.0 | 0.0% | 0.0% |
| `tests/openpgp` | 99 | 121266.03 | 4.69% | 0.0% |
| `tests/cms` | 38 | 115408.19 | 2.74% | 0.0% |
| `tests/cms/samplekeys` | 24 | 115001.0 | 0.0% | 0.0% |
| `g10` | 101 | 79364.8 | 54.36% | 37.92% |
| `tests/openpgp/trust-pgp` | 12 | 55039.76 | 0.32% | 0.0% |
| `scd` | 23 | 48980.7 | 56.19% | 21.27% |
| `dirmngr` | 66 | 44404.65 | 45.32% | 29.49% |

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
- `dirmngr/dns.c` -> **72** Orphaned Functions | **0** Duplicates
- `tests/gpgscm/ffi.c` -> **54** Orphaned Functions | **0** Duplicates
- `tests/gpgscm/scheme.c` -> **34** Orphaned Functions | **0** Duplicates
- `g10/misc.c` -> **33** Orphaned Functions | **0** Duplicates
- `scd/iso7816.c` -> **32** Orphaned Functions | **0** Duplicates

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

### Hardcoded Payload Artifacts
- `tools/gpg-card.c` -> **100.0%** Exposure
- `tests/openpgp/ecc.scm` -> **100.0%** Exposure
- `tests/openpgp/signed-messages.scm` -> **100.0%** Exposure
- `tools/der-to-pem` -> **100.0%** Exposure
- `tests/openpgp/armor.scm` -> **40.0688%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `20` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3628` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `dirmngr/dns.c` (C) -> Cumulative Risk: **689.79**
- **Archetype:** `file_cluster_11` (Distance: 15.496 IQR)
- **Magnitude:** 5245.46 | **LOC:** 11687 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (98.511%)
- **Heaviest Functions:** `dns_d_cleave` (Impact: 676.0), `dns_p_push` (Impact: 140.8), `dns_ai_open` (Impact: 74.8)

### 2. `common/stringhelp.c` (C) -> Cumulative Risk: **689.22**
- **Archetype:** `file_cluster_13` (Distance: 14.569 IQR)
- **Magnitude:** 1241.56 | **LOC:** 1889 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.5203%)
- **Heaviest Functions:** `do_make_filename` (Impact: 100.2), `hextobyte` (Impact: 43.7), `strsep` (Impact: 30.1)

### 3. `sm/keydb.c` (C) -> Cumulative Risk: **687.37**
- **Archetype:** `file_cluster_8` (Distance: 13.665 IQR)
- **Magnitude:** 1626.9 | **LOC:** 2239 | **CtrlFlow:** 81.2% | **Authorship Centralization:** 83.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (91.2508%)
- **Heaviest Functions:** `keydb_search_reset` (Impact: 170.4), `keydb_search` (Impact: 98.0), `keydb_add_resource` (Impact: 46.4)

### 4. `g10/getkey.c` (C) -> Cumulative Risk: **686.73**
- **Archetype:** `file_cluster_8` (Distance: 14.306 IQR)
- **Magnitude:** 3419.56 | **LOC:** 4772 | **CtrlFlow:** 85.5% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.1004%)
- **Heaviest Functions:** `get_best_pubkey_byname` (Impact: 279.6), `get_pubkey_bykid` (Impact: 238.4), `get_keyblock_byfpr_fast` (Impact: 202.6)

### 5. `g10/misc.c` (C) -> Cumulative Risk: **686.68**
- **Archetype:** `file_cluster_8` (Distance: 13.655 IQR)
- **Magnitude:** 2496.08 | **LOC:** 1967 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (93.8997%)
- **Heaviest Functions:** `is_secured_file` (Impact: 572.2), `openpgp_pk_test_algo2` (Impact: 120.1), `parse_options` (Impact: 90.1)

### 6. `common/tlv-parser.c` (C) -> Cumulative Risk: **683.19**
- **Archetype:** `file_cluster_8` (Distance: 14.079 IQR)
- **Magnitude:** 829.06 | **LOC:** 828 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (95.0275%)
- **Heaviest Functions:** `_tlv_parser_next` (Impact: 44.8), `cram_octet_string` (Impact: 35.1), `tlv_expect_object` (Impact: 16.2)

### 7. `common/sysutils.c` (C) -> Cumulative Risk: **683.07**
- **Archetype:** `file_cluster_13` (Distance: 12.902 IQR)
- **Magnitude:** 1200.54 | **LOC:** 2081 | **CtrlFlow:** 59.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `gnupg_stat` (Impact: 95.7), `map_w32_to_errno` (Impact: 81.2), `check_permissions` (Impact: 61.0)

### 8. `kbx/backend-kbx.c` (C) -> Cumulative Risk: **680.79**
- **Archetype:** `file_cluster_13` (Distance: 12.802 IQR)
- **Magnitude:** 465.72 | **LOC:** 459 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.6676%)
- **Heaviest Functions:** `check_kbx_file_magic` (Impact: 163.3), `be_kbx_add_resource` (Impact: 19.6), `be_kbx_search` (Impact: 14.4)

### 9. `g10/call-keyboxd.c` (C) -> Cumulative Risk: **680.75**
- **Archetype:** `file_cluster_13` (Distance: 13.853 IQR)
- **Magnitude:** 537.68 | **LOC:** 915 | **CtrlFlow:** 90.0% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (90.1941%)
- **Heaviest Functions:** `gpg_keyboxd_deinit_session_data` (Impact: 105.9), `keydb_search_reset` (Impact: 90.5), `keydb_search` (Impact: 84.5)

### 10. `g10/call-agent.c` (C) -> Cumulative Risk: **680.38**
- **Archetype:** `file_cluster_8` (Distance: 14.502 IQR)
- **Magnitude:** 2532.42 | **LOC:** 3467 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.3681%)
- **Heaviest Functions:** `agent_probe_secret_key` (Impact: 378.6), `learn_status_cb` (Impact: 289.2), `start_agent` (Impact: 44.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `scd/ccid-driver.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.015 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.982 IQR)
- **Top Global Matches:** file_cluster_8: 14.015, file_cluster_13: 14.208, file_cluster_11: 14.303
- **Magnitude:** 26831.32 | **LOC:** 4082 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.3737%), Tech Debt (9.9363%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 484`, `structural_boundaries: 154`, `args: 24`, `func_start: 35`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1381`, `fragile_debt: 3`
* *Architecture:* `io: 1`, `api: 321`, `import: 16`
* *Defense:* `safety: 24`, `test: 2`, `immutability_locks: 18`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` string.h, stat.h, npth.h, libusb.h, time.h, stdlib.h, scdaemon.h, unistd.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/gpgscm/init.scm` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.972 IQR)
- **Top Global Matches:** file_cluster_8: 9.972, file_cluster_7: 10.58, file_cluster_17: 10.791
- **Magnitude:** 13186.23 | **LOC:** 827 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.8294%), Tech Debt (0.0%)
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
- **Risk Profile:** Cognitive Load (6.7565%), Tech Debt (0.0%)
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

### `dirmngr/dns.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.496 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.641 IQR)
- **Top Global Matches:** file_cluster_11: 15.496, file_cluster_13: 15.597, file_cluster_0: 15.638
- **Magnitude:** 5245.46 | **LOC:** 11687 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (98.511%), Tech Debt (91.6809%)
**Top Internal Functions/Classes:**
  * `dns_d_cleave` (Impact: 676.0)
  * `dns_p_push` (Impact: 140.8)
  * `dns_ai_open` (Impact: 74.8)
  * `dns_ai_nextent` (Impact: 68.4)
    * *Intent:* } /* dns_soa_cmp() */
  * `dns_p_merge` (Impact: 56.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 848`, `structural_boundaries: 764`, `args: 170`, `func_start: 174`, `class_start: 110`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 2018`, `dead_code: 16`, `planned_debt: 8`, `fragile_debt: 12`, `orphaned_logic: 72`
* *Architecture:* `io: 16`, `api: 729`, `import: 33`
* *Defense:* `safety: 131`, `test: 5`, `immutability_locks: 130`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` winsock2.h, time.h, limits.h, strings.h, select.h, inet.h, stdio.h, dns.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dirmngr/sks-keyservers.netCA.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `tests/cms/cert_cci_user06.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `tests/cms/cert_cci_user07.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `tests/cms/cert_testpki_testpca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `tests/cms/crl_testpki_testpca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `tests/cms/key_g10code_pete1.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `tests/cms/key_g10code_theo1.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `tests/cms/plain-1.cms.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- `dirmngr/dns.c` (C) | Magnitude: 5245.46 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 2107, state_mutation: 2018, pointers: 1652, branch: 848

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `regexp/utf8.h` (C) | Magnitude: 25.54 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 15, api: 6, doc: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `agent/trustlist.c` (C) | Magnitude: 604.36 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 429, state_mutation: 394, branch: 165, pointers: 105
- `dirmngr/ocsp.c` (C) | Magnitude: 500.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 368, state_mutation: 272, branch: 113, api: 76
- `sm/fingerprint.c` (C) | Magnitude: 417.92 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 317, state_mutation: 216, api: 105, branch: 63
- `g10/export.c` (C) | Magnitude: 2362.04 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 1563, state_mutation: 1008, branch: 536, pointers: 462
- `dirmngr/workqueue.c` (C) | Magnitude: 206.38 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 117, indent_spaces: 100, pointers: 47, branch: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/tpm2dtests/start_sw_tpm.sh` (SHELL) | Magnitude: 39.38 | Delta: **0.35 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 24, branch: 20, state_mutation: 9, io: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `dirmngr/ks-action.c` (C) | Magnitude: 823.78 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 414, indent_spaces: 401, branch: 192, pointers: 156
- `g10/keylist.c` (C) | Magnitude: 1322.94 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 709, state_mutation: 563, branch: 370, pointers: 228
- `tests/pkits/validate-all-certs` (SHELL) | Magnitude: 5.36 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 39, indent_spaces: 29, safety_bypasses: 18, state_mutation: 9
- `common/asshelp.c` (C) | Magnitude: 623.28 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 416, state_mutation: 282, api: 125, branch: 99
- `g10/call-agent.c` (C) | Magnitude: 2532.42 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1201, state_mutation: 1085, branch: 451, pointers: 432

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `g13/create.h` (C) | Magnitude: 17.64 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 5, api: 4, structural_boundaries: 2, safety: 2
- `g10/objcache.h` (C) | Magnitude: 17.64 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 8, api: 4, structural_boundaries: 3, safety: 2
- `kbx/keybox-defs.h` (C) | Magnitude: 94.04 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 86, indent_spaces: 62, pointers: 51, structural_boundaries: 26
- `tests/pkits/inittests` (SHELL) | Magnitude: 5.66 | Delta: **0.149 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: branch: 35, io: 30, indent_spaces: 20, structural_boundaries: 9
- `scd/atr.h` (C) | Magnitude: 13.08 | Delta: **0.168 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 3, macros: 2, structural_boundaries: 1, args: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `agent/pkdecrypt.c` -> Churn: **57.97%** | Cog Load: 87.1177% | Debt: 15.5168%
- `g10/call-agent.c` -> Churn: **56.0%** | Cog Load: 94.8658% | Debt: 39.6224%
- `g10/keyedit.c` -> Churn: **52.11%** | Cog Load: 83.5685% | Debt: 22.5546%
- `g10/armor.c` -> Churn: **52.07%** | Cog Load: 72.7703% | Debt: 48.8917%
- `sm/gpgsm.c` -> Churn: **52.07%** | Cog Load: 76.1725% | Debt: 20.0186%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/gpgscm/tests.scm` -> **Joshua Frommholz** (100.0% isolated ownership) | Magnitude: 10354.38
- `dirmngr/dns.c` -> **NIIBE Yutaka** (100.0% isolated ownership) | Magnitude: 5245.46
- `scd/app-openpgp.c` -> **Werner Koch** (100.0% isolated ownership) | Magnitude: 4187.88
- `dirmngr/dirmngr_ldap.c` -> **Werner Koch** (100.0% isolated ownership) | Magnitude: 4138.14
- `scd/app-p15.c` -> **Mario Haustein** (100.0% isolated ownership) | Magnitude: 3708.76

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `common/tlv.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `g10/packet.h` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 12.0693%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `g10/options.h` -> **Severity: 2.96** (Embedded: 0.0568 * Error Risk: 52.0766%)
- `g10/packet.h` -> **Severity: 2.274** (Embedded: 0.0475 * Error Risk: 47.8347%)
- `g10/tofu.h` -> **Severity: 2.143** (Embedded: 0.0307 * Error Risk: 69.8251%)
- `dirmngr/http.h` -> **Severity: 1.087** (Embedded: 0.0184 * Error Risk: 59.0653%)
- `agent/agent.h` -> **Severity: 0.673** (Embedded: 0.0222 * Error Risk: 30.3559%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `agent/agent.h` -> **Severity: 1349.6** (Blast Radius: 13.496 * Doc Risk: 100.0%)
- `g10/gpg.h` -> **Severity: 1205.129** (Blast Radius: 12.052 * Doc Risk: 99.9941%)
- `sm/gpgsm.h` -> **Severity: 1161.1** (Blast Radius: 11.611 * Doc Risk: 100.0%)
- `g10/dek.h` -> **Severity: 1101.824** (Blast Radius: 11.813 * Doc Risk: 93.2722%)
- `g10/packet.h` -> **Severity: 1061.5** (Blast Radius: 10.615 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
