# ARCHITECTURAL_BRIEF: pynacl
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 406 analyzed artifact(s), 53804 LOC.
- **Load-bearing artifact:** `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/common.h` -- 80 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium.h` -- pulls in 63 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_core/ed25519/ref10/ed25519_ref10.c` at magnitude 1738.78 (structural weight, not risk).
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
| Total Artifacts | 516 |
| Analyzed Artifacts (Scanned) | 406 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 110 |
| Total LOC | 53804 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 78.7% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5655 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2384 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.2327 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 31 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 283 | 30549 | 69.7% |
| PYTHON | 52 | 7880 | 12.8% |
| M4 | 20 | 8695 | 4.9% |
| XML | 17 | 0 | 4.2% |
| PLAINTEXT | 12 | 0 | 3.0% |
| ASSEMBLY | 7 | 2923 | 1.7% |
| MAKEFILE | 5 | 3097 | 1.2% |
| JSON | 4 | 388 | 1.0% |
| YAML | 3 | 160 | 0.7% |
| MARKDOWN | 1 | 0 | 0.2% |
| SHELL | 1 | 101 | 0.2% |
| BATCH | 1 | 11 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `2.991`
> **Composition Archetype:** `Hub-Coupled App` (z +2.99; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 35%, Data / Markup / Trivial 16%, Many-Argument Workhorses Files 13%, Large Core Modules (2) 13%, Large Core Modules (3) 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 391 | 96.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 15 | 3.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 110*

**Composition by Extension & Reason:**
- `.props`: 40x Excluded (Unsupported Extension: '.props'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.vcxproj`: 10x Excluded (Unsupported Extension: '.vcxproj')
- `.filters`: 10x Excluded (Unsupported Extension: '.filters')
- `.sln`: 9x Excluded (Unsupported Extension: '.sln')
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 25053 LOC)
- `.am`: 6x Excluded (Unsupported Extension: '.am')
- `.tpl`: 4x Excluded (Unsupported Extension: '.tpl')
- `.rst`: 3x Excluded (Unsupported Extension: '.rst')
- `.h`: 1x Excluded (Embedded Array/Matrix Payload: 7679 commas in 1345 LOC), 1x Zero-Density Threshold (LOC: 1344, Signals: 0)
- `.json`: 1x Excluded (Massive Static Asset Blob: 18435 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cff`: 1x Excluded (Unsupported Extension: '.cff')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 19.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 36.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 22.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 11.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 25.1 | 9.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 95.6 | 0.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 34.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 30.8 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 50.0 | 49.7 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 49.4 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 8097 | 249 | 54 | `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_core/ed25519/ref10/ed25519_ref10.c` |
| cleanup | 87 | 15 | 0 | `pynacl-1.6.2/src/libsodium/Makefile.in` |
| guards | 5407 | 295 | 33 | `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/armcrypto/aead_aes256gcm_armcrypto.c` |
| danger | 570 | 96 | 4 | `pynacl-1.6.2/src/libsodium/Makefile.in` |
| concurrency | 21 | 5 | 0 | `pynacl-1.6.2/src/libsodium/autogen.sh` |
| connectivity | 2621 | 324 | 17 | `pynacl-1.6.2/src/bindings/crypto_pwhash.h` |
| io | 151 | 17 | 0 | `pynacl-1.6.2/src/libsodium/Makefile.in` |
| crypto | 6 | 6 | 0 | `pynacl-1.6.2/src/nacl/pwhash/__init__.py` |
| ipc | 11 | 5 | 0 | `pynacl-1.6.2/setup.py` |
| time | 1 | 1 | 0 | `pynacl-1.6.2/src/libsodium/src/libsodium/randombytes/internal/randombytes_internal_random.c` |
| serialization | 18 | 5 | 0 | `pynacl-1.6.2/src/libsodium/Makefile.in` |
| regex | 18 | 6 | 0 | `pynacl-1.6.2/src/libsodium/Makefile.in` |
| events | 218 | 13 | 0 | `pynacl-1.6.2/src/libsodium/configure.ac` |
| tests | 485 | 19 | 0 | `pynacl-1.6.2/tests/test_bindings.py` |
| docs | 216 | 37 | 0 | `pynacl-1.6.2/src/nacl/hash.py` |
| debt | 155 | 19 | 0 | `pynacl-1.6.2/src/libsodium/m4/libtool.m4` |
| mutation | 17922 | 207 | 102 | `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_core/ed25519/ref10/ed25519_ref10.c` |
| dead_code | 834 | 140 | 7 | `pynacl-1.6.2/tests/test_pwhash.py` |
| credential | 21 | 3 | 0 | `pynacl-1.6.2/tests/data/modular_crypt_argon2i_hashes.json` |
| threat | 477 | 59 | 2 | `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/ref/blake2b-load-avx2.h` |
| ml_ai | 41 | 4 | 0 | `pynacl-1.6.2/src/libsodium/m4/libtool.m4` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **3.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pynacl-1.6.2/src/libsodium/Makefile.in` (Hits: 42)
- `pynacl-1.6.2/src/libsodium/autogen.sh` (Hits: 28)
- `pynacl-1.6.2/setup.py` (Hits: 15)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **common.h** (`pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/common.h`) — 80 inbound connections
2. **export.h** (`pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/export.h`) — 76 inbound connections
3. **core.h** (`pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/core.h`) — 32 inbound connections
4. **exceptions.py** (`pynacl-1.6.2/src/nacl/exceptions.py`) — 27 inbound connections
5. **sse2_64_32.h** (`pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/sse2_64_32.h`) — 18 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **sodium.h** (`pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium.h`) — 63 outbound dependencies
2. **randombytes_internal_random.c** (`pynacl-1.6.2/src/libsodium/src/libsodium/randombytes/internal/randombytes_internal_random.c`) — 27 outbound dependencies
3. **randombytes_sysrandom.c** (`pynacl-1.6.2/src/libsodium/src/libsodium/randombytes/sysrandom/randombytes_sysrandom.c`) — 21 outbound dependencies
4. **chacha20_dolbeau-avx2.c** (`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_stream/chacha20/dolbeau/chacha20_dolbeau-avx2.c`) — 18 outbound dependencies
5. **utils.c** (`pynacl-1.6.2/src/libsodium/src/libsodium/sodium/utils.c`) — 18 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_LT_FORMAT_COMMENT` **(Many-Argument Workhorses)** (@ `pynacl-1.6.2/src/libsodium/m4/libtool.m4`) -> Impact: **170.5** | LOC: 8146
  * *Intent:* # _LT_FORMAT_COMMENT([COMMENT]) # ----------------------------- # Add leading comment marks to the start of each line, and a trailing # full-stop to t...
- `_lt_decl_filter` **(Many-Argument Workhorses)** (@ `pynacl-1.6.2/src/libsodium/m4/libtool.m4`) -> Impact: **157.9** | LOC: 8102
  * *Intent:* # _lt_decl_filter(SUBKEY, VALUE, [SEPARATOR], [VARNAME1..]) # ---------------------------------------------------------
- `lt_decl_varnames_tagged` **(Many-Argument Workhorses)** (@ `pynacl-1.6.2/src/libsodium/m4/libtool.m4`) -> Impact: **154.7** | LOC: 8078
  * *Intent:* # lt_decl_varnames_tagged([SEPARATOR], [VARNAME1...]) # ---------------------------------------------------
- `LT_OUTPUT` **(Many-Argument Workhorses)** (@ `pynacl-1.6.2/src/libsodium/m4/libtool.m4`) -> Impact: **135.4** | LOC: 7868
  * *Intent:* # LT_OUTPUT # --------- # This macro allows early generation of the libtool script (before # AC_OUTPUT is called), in case it is used in configure for...
- `aes_gcm_encrypt_generic` **(Many-Argument Workhorses)** (@ `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/aesni/aead_aes256gcm_aesni.c`) -> Impact: **94.1** | LOC: 174
  * *Intent:* /* Generic AES-GCM encryption. "Generic" as it can handle arbitrary input sizes, unlike a length-limited version that would precompute all the require...
- `aes_gcm_encrypt_generic` **(Many-Argument Workhorses)** (@ `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/armcrypto/aead_aes256gcm_armcrypto.c`) -> Impact: **87.3** | LOC: 165
  * *Intent:* /* Generic AES-GCM encryption. "Generic" as it can handle arbitrary input sizes, unlike a length-limited version that would precompute all the require...
- `aes_gcm_decrypt_generic` **(Many-Argument Workhorses)** (@ `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/aesni/aead_aes256gcm_aesni.c`) -> Impact: **73.5** | LOC: 141
  * *Intent:* /* Generic AES-GCM decryption. "Generic" as it can handle arbitrary input sizes, unlike a length-limited version that would precompute all the require...
- `aes_gcm_decrypt_generic` **(Many-Argument Workhorses)** (@ `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/armcrypto/aead_aes256gcm_armcrypto.c`) -> Impact: **73.5** | LOC: 141
  * *Intent:* /* Generic AES-GCM decryption. "Generic" as it can handle arbitrary input sizes, unlike a length-limited version that would precompute all the require...
- `sodium_base642bin` **(Many-Argument Workhorses)** (@ `pynacl-1.6.2/src/libsodium/src/libsodium/sodium/codecs.c`) -> Impact: **72.5** | LOC: 69
- `._ladder_loop` **(Many-Argument Workhorses)** (@ `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_scalarmult/curve25519/sandy2x/ladder.S`) -> Impact: **71.7** | LOC: 1296

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2` | 18 | 2536.38 | 55.81% | 23.07% |
| `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium` | 66 | 1799.36 | 0.96% | 0.0% |
| `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_core/ed25519/ref10` | 1 | 1738.78 | 88.2% | 14.85% |
| `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/ref` | 13 | 1691.52 | 47.95% | 21.34% |
| `pynacl-1.6.2/src/nacl/bindings` | 16 | 1636.3 | 16.81% | 0.0% |
| `pynacl-1.6.2/tests` | 19 | 1634.3 | 13.44% | 0.0% |
| `pynacl-1.6.2/src/libsodium/m4` | 16 | 1474.58 | 3.91% | 12.94% |
| `pynacl-1.6.2/src/libsodium/src/libsodium/sodium` | 5 | 1164.5 | 54.81% | 64.21% |
| `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_stream/salsa20/xmm6int` | 8 | 1147.36 | 27.24% | 0.0% |
| `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private` | 10 | 1024.0 | 11.16% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_box/crypto_box.c` -> **100.0%** Exposure
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/generichash_blake2.c` -> **100.0%** Exposure
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_sign/crypto_sign.c` -> **100.0%** Exposure
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/crypto_generichash.c` -> **99.9999%** Exposure
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_secretbox/crypto_secretbox.c` -> **99.9999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `pynacl-1.6.2/src/libsodium/regen-msvc/regen-msvc.py` -> **100.0%** Exposure
- `pynacl-1.6.2/src/nacl/bindings/utils.py` -> **100.0%** Exposure
- `pynacl-1.6.2/src/nacl/pwhash/__init__.py` -> **100.0%** Exposure
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/aesni/aead_aes256gcm_aesni.c` -> **100.0%** Exposure
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/armcrypto/aead_aes256gcm_armcrypto.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pynacl-1.6.2/tests/test_pwhash.py` -> **33** Orphaned Functions | **0** Duplicates
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/crypto_pwhash.c` -> **25** Orphaned Functions | **0** Duplicates
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/pwhash_argon2i.c` -> **22** Orphaned Functions | **0** Duplicates
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/pwhash_argon2id.c` -> **20** Orphaned Functions | **0** Duplicates
- `pynacl-1.6.2/tests/test_secret.py` -> **18** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1541` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_core/ed25519/ref10/ed25519_ref10.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 1738.78 | **LOC:** 2877 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.5%), Complexity Load (formerly Cognitive Load) (88.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ge25519_double_scalarmult_vartime` **(Many-Argument Workhorses)** (Impact: 31.1)
    * *Intent:* */
  * `slide_vartime` **(Stateful Encapsulated Methods)** (Impact: 22.9)
  * `fe25519_invert` **(Many-Argument Workhorses)** (Impact: 18.3)
    * *Intent:* * and 10*25.5 bit limbs elsewhere. * * Functions used elsewhere that are candidates for inlining are...
  * `fe25519_pow22523` **(Many-Argument Workhorses)** (Impact: 16.5)
  * `ge25519_scalarmult` **(Many-Argument Workhorses)** (Impact: 12.0)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 128 instances
* *State Mutation (weighted view):* 1359
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 76`, `args: 71`, `func_start: 60`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1103`, `unreferenced_by_name: 18`
* *Architecture:* `api: 27`, `import: 16`
* *Defense:* `safety: 2`, `immutability_locks: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` crypto_verify_32.h, base.h, base2.h, constants.h, fe.h, base.h, base2.h, constants.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/m4/libtool.m4` (M4 | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1086.44 | **LOC:** 8489 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.478; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.7%), Connectivity (formerly Api Exposure) (41.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_LT_FORMAT_COMMENT` **(Many-Argument Workhorses)** (Impact: 170.5)
    * *Intent:* # _LT_FORMAT_COMMENT([COMMENT]) # ----------------------------- # Add leading comment marks to the s...
  * `_lt_decl_filter` **(Many-Argument Workhorses)** (Impact: 157.9)
    * *Intent:* # _lt_decl_filter(SUBKEY, VALUE, [SEPARATOR], [VARNAME1..]) # --------------------------------------...
  * `lt_decl_varnames_tagged` **(Many-Argument Workhorses)** (Impact: 154.7)
    * *Intent:* # lt_decl_varnames_tagged([SEPARATOR], [VARNAME1...]) # --------------------------------------------...
  * `LT_OUTPUT` **(Many-Argument Workhorses)** (Impact: 135.4)
    * *Intent:* # LT_OUTPUT # --------- # This macro allows early generation of the libtool script (before # AC_OUTP...
  * `_LT_COMPILER_PIC` **(I/O & Config Routines)** (Impact: 20.1)
    * *Intent:* # _LT_COMPILER_PIC([TAGNAME]) # ---------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 108`, `args: 1188`, `func_start: 112`
* *Risk/State:* `state_mutation: 5`, `dead_code: 31`, `planned_debt: 3`, `fragile_debt: 50`
* *Architecture:* `api: 26`
* *Defense:* `safety: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002463
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/aesni/aead_aes256gcm_aesni.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 969.78 | **LOC:** 1016 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `aes_gcm_encrypt_generic` **(Many-Argument Workhorses)** (Impact: 94.1)
    * *Intent:* /* Generic AES-GCM encryption. "Generic" as it can handle arbitrary input sizes, unlike a length-lim...
  * `aes_gcm_decrypt_generic` **(Many-Argument Workhorses)** (Impact: 73.5)
    * *Intent:* /* Generic AES-GCM decryption. "Generic" as it can handle arbitrary input sizes, unlike a length-lim...
  * `gh_ad_blocks` **(Many-Argument Workhorses)** (Impact: 24.7)
    * *Intent:* /* Absorb ad_len bytes of associated data. There has to be no partial block. */
  * `crypto_aead_aes256gcm_encrypt_detached_afternm` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `crypto_aead_aes256gcm_verify_mac` **(Many-Argument Workhorses)** (Impact: 21.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 178 instances
* *State Mutation (weighted view):* 561
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 51`, `args: 57`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 205`, `unreferenced_by_name: 5`
* *Architecture:* `api: 15`, `import: 16`
* *Defense:* `safety: 50`, `immutability_locks: 127`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` core.h, crypto_aead_aes256gcm.h, crypto_verify_16.h, errno.h, export.h, limits.h, common.h, sse2_64_32.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/armcrypto/aead_aes256gcm_armcrypto.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 966.6 | **LOC:** 1034 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `aes_gcm_encrypt_generic` **(Many-Argument Workhorses)** (Impact: 87.3)
    * *Intent:* /* Generic AES-GCM encryption. "Generic" as it can handle arbitrary input sizes, unlike a length-lim...
  * `aes_gcm_decrypt_generic` **(Many-Argument Workhorses)** (Impact: 73.5)
    * *Intent:* /* Generic AES-GCM decryption. "Generic" as it can handle arbitrary input sizes, unlike a length-lim...
  * `gh_ad_blocks` **(Many-Argument Workhorses)** (Impact: 24.7)
    * *Intent:* /* Absorb ad_len bytes of associated data. There has to be no partial block. */
  * `crypto_aead_aes256gcm_encrypt_detached_afternm` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `crypto_aead_aes256gcm_verify_mac` **(Many-Argument Workhorses)** (Impact: 21.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 178 instances
* *State Mutation (weighted view):* 562
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 54`, `args: 58`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 206`, `unreferenced_by_name: 5`
* *Architecture:* `api: 15`, `import: 14`
* *Defense:* `safety: 50`, `immutability_locks: 131`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` arm_neon.h, core.h, crypto_aead_aes256gcm.h, crypto_verify_16.h, errno.h, export.h, limits.h, common.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_onetimeauth/poly1305/sse2/poly1305_sse2.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 908.48 | **LOC:** 958 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poly1305_blocks` **(Many-Argument Workhorses)** (Impact: 51.0)
  * `poly1305_init_ext` **(Many-Argument Workhorses)** (Impact: 20.6)
  * `poly1305_finish_ext` **(Many-Argument Workhorses)** (Impact: 19.7)
  * `poly1305_update` **(Many-Argument Workhorses)** (Impact: 18.1)
  * `poly1305_block_copy31` **(Stateful Encapsulated Methods)** (Impact: 13.4)
    * *Intent:* # define _mm_loadl_epi64(X) _fakealign_mm_loadl_epi64(X) #endif /* copy 0-31 bytes */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 103 instances
* *State Mutation (weighted view):* 747
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 62`, `args: 229`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 541`
* *Architecture:* `api: 3`, `import: 9`
* *Defense:* `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` onetimeauth_poly1305.h, crypto_verify_16.h, emmintrin.h, poly1305_sse2.h, common.h, sse2_64_32.h, stdint.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/nacl/bindings/crypto_aead.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 542.54 | **LOC:** 1070 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 1.478; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (49.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `crypto_aead_aes256gcm_encrypt` **(Many-Argument Workhorses)** (Impact: 19.8)
  * `crypto_aead_aes256gcm_decrypt` **(Many-Argument Workhorses)** (Impact: 19.8)
  * `crypto_aead_chacha20poly1305_ietf_encrypt` **(Many-Argument Workhorses)** (Impact: 19.5)
  * `crypto_aead_chacha20poly1305_ietf_decrypt` **(Many-Argument Workhorses)** (Impact: 19.5)
  * `crypto_aead_chacha20poly1305_encrypt` **(Many-Argument Workhorses)** (Impact: 19.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 282
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 45`, `args: 12`, `func_start: 12`
* *Risk/State:* `state_mutation: 114`
* *Architecture:* `api: 12`, `import: 4`
* *Defense:* `safety: 48`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002463
  * `Imports (Out-Degree: 1):` nacl, nacl._sodium, nacl.exceptions, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/ref/blake2b-load-avx2.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 452.82 | **LOC:** 341 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 2.839; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (100.0%), Complexity Load (formerly Cognitive Load) (84.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 144 instances
* *State Mutation (weighted view):* 432
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`
* *Risk/State:* `state_mutation: 144`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.839
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003284
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pynacl-1.6.2/src/libsodium/src/libsodium/sodium/codecs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 421.76 | **LOC:** 336 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.2%), Complexity Load (formerly Cognitive Load) (83.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sodium_base642bin` **(Many-Argument Workhorses)** (Impact: 72.5)
  * `sodium_hex2bin` **(Many-Argument Workhorses)** (Impact: 45.5)
  * `sodium_bin2base64` **(Many-Argument Workhorses)** (Impact: 42.3)
  * `_sodium_base642bin_skip_padding` **(Stateful Encapsulated Methods)** (Impact: 18.3)
  * `sodium_bin2hex` **(Many-Argument Workhorses)** (Impact: 10.2)
    * *Intent:* #include <assert.h> #include <errno.h> #include <limits.h> #include <stddef.h> #include <stdint.h> #...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 19`, `args: 11`, `func_start: 11`
* *Risk/State:* `state_mutation: 73`, `unreferenced_by_name: 5`
* *Architecture:* `api: 5`, `import: 10`
* *Defense:* `safety: 40`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` assert.h, core.h, errno.h, limits.h, common.h, stddef.h, stdint.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/sodium/utils.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 412.0 | **LOC:** 810 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (70.4%), Guard Balance (formerly Safety Score) (68.4%), Complexity Load (formerly Cognitive Load) (50.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sodium_pad` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `sodium_memzero` **(Defensive Guards)** (Impact: 11.4)
    * *Intent:* #endif /* LCOV_EXCL_STOP */
  * `sodium_unpad` **(Defensive Guards)** (Impact: 10.4)
  * `sodium_compare` **(Many-Argument Workhorses)** (Impact: 9.5)
    * *Intent:* #endif
  * `sodium_memcmp` **(Many-Argument Workhorses)** (Impact: 9.2)
    * *Intent:* #endif
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 66 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 127`, `args: 96`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 78`, `fragile_debt: 2`, `unreferenced_by_name: 13`
* *Architecture:* `api: 20`, `import: 19`
* *Defense:* `safety: 73`, `immutability_locks: 61`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` alloca.h, assert.h, core.h, errno.h, limits.h, malloc.h, randombytes.h, signal.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/ref/blake2b-ref.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 360.5 | **LOC:** 439 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blake2b_salt_personal` **(Many-Argument Workhorses)** (Impact: 40.9)
  * `blake2b` **(Many-Argument Workhorses)** (Impact: 36.2)
    * *Intent:* /* inlen, at least, should be uint64_t. Others can be size_t. */
  * `blake2b_init_key_salt_personal` **(Many-Argument Workhorses)** (Impact: 31.4)
  * `blake2b_init_key` **(Many-Argument Workhorses)** (Impact: 17.5)
  * `blake2b_init_salt_personal` **(Many-Argument Workhorses)** (Impact: 17.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 35`, `args: 85`, `func_start: 17`
* *Risk/State:* `state_mutation: 50`, `unreferenced_by_name: 3`
* *Architecture:* `api: 10`, `import: 10`
* *Defense:* `safety: 5`, `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` assert.h, blake2.h, core.h, common.h, runtime.h, stddef.h, stdint.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_stream/salsa20/xmm6int/u4.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 357.64 | **LOC:** 548 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (46.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 333
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `args: 5`
* *Risk/State:* `state_mutation: 301`
* *Architecture:* None
* *Defense:* `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/ed25519_ref10_fe_25_5.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 341.16 | **LOC:** 1031 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 3.318; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (44.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fe25519_cmov` **(Many-Argument Workhorses)** (Impact: 4.0)
    * *Intent:* */
  * `fe25519_cswap` **(Many-Argument Workhorses)** (Impact: 4.0)
  * `fe25519_mul` **(Many-Argument Workhorses)** (Impact: 4.0)
    * *Intent:* */
  * `fe25519_mul32` **(Many-Argument Workhorses)** (Impact: 4.0)
  * `fe25519_add` **(State Mutators)** (Impact: 3.2)
    * *Intent:* */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 14`, `func_start: 14`
* *Risk/State:* `state_mutation: 270`
* *Architecture:* `api: 14`, `import: 3`
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.318
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.014192
  * `Imports (Out-Degree: 1):` common.h, string.h, utils.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pynacl-1.6.2/tests/test_bindings.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 332.7 | **LOC:** 1023 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 1.636; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (60.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (27.2%), Complexity Load (formerly Cognitive Load) (22.0%)
- **Documentation Coverage:** 90.5882% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_scalarmult_ed25519` **(I/O & Config Routines)** (Impact: 6.2)
  * `test_ed25519_from_uniform` **(Defensive Guards)** (Impact: 4.4)
    * *Intent:* """ Verify crypto_core_ed25519_from_uniform maps 32 byte inputs to valid points" """
  * `test_scalarmult_ed25519_noclamp` **(I/O & Config Routines)** (Impact: 3.5)
    * *Intent:* # An arbitrary scalar which is known to differ once clamped scalar = 32 * b"\x01" BASEPOINT = bytes(...
  * `test_ed25519_scalar_add_and_sub` **(I/O & Config Routines)** (Impact: 3.5)
  * `test_sign_ed25519ph_libsodium` **(I/O & Config Routines)** (Impact: 3.1)
    * *Intent:* # _hsk, _hpk, hmsg, _hsig, _hsigmsg = ed25519_known_answers()[-1] msg = unhexlify(hmsg) seed = unhex...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 234`, `args: 43`, `func_start: 43`
* *Risk/State:* `state_mutation: 161`
* *Architecture:* `api: 42`, `import: 11`
* *Defense:* `safety: 95`, `doc: 4`, `test: 126`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.636
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.002463
  * `Imports (Out-Degree: 4):` .test_signing, .utils, binascii, hashlib, hypothesis, hypothesis.strategies, nacl, nacl.exceptions...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-core.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 314.44 | **LOC:** 557 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (50.6%)
- **Documentation Coverage:** 84.2105% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `argon2_validate_inputs` **(Compute Cores)** (Impact: 51.5)
  * `allocate_memory` **(Many-Argument Workhorses)** (Impact: 27.0)
  * `argon2_initial_hash` **(Many-Argument Workhorses)** (Impact: 22.1)
  * `argon2_pick_best_implementation` **(Stateful Encapsulated Methods)** (Impact: 15.5)
  * `argon2_initialize` **(Compute Cores)** (Impact: 10.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 40 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 122
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 60`, `args: 35`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 42`, `unreferenced_by_name: 5`
* *Architecture:* `api: 5`, `import: 14`
* *Defense:* `safety: 1`, `doc: 8`, `immutability_locks: 10`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` argon2-core.h, blake2b-long.h, crypto_generichash_blake2b.h, errno.h, common.h, implementations.h, runtime.h, stdint.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_stream/salsa20/xmm6int/u8.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 313.26 | **LOC:** 478 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (47.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 290
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `args: 7`
* *Risk/State:* `state_mutation: 274`
* *Architecture:* None
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/ref/blake2b-load-sse41.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 307.86 | **LOC:** 308 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 2.839; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Complexity Load (formerly Cognitive Load) (84.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 96 instances
* *State Mutation (weighted view):* 288
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`
* *Risk/State:* `state_mutation: 96`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.839
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003284
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/ed25519_ref10_fe_51.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 306.66 | **LOC:** 509 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 3.318; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (46.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fe25519_cswap` **(Many-Argument Workhorses)** (Impact: 4.0)
    * *Intent:* */
  * `fe25519_mul` **(Type Conversions)** (Impact: 4.0)
    * *Intent:* */
  * `fe25519_sub` **(Many-Argument Workhorses)** (Impact: 3.8)
    * *Intent:* */
  * `fe25519_cmov` **(Many-Argument Workhorses)** (Impact: 3.5)
    * *Intent:* */
  * `fe25519_mul32` **(Type Conversions)** (Impact: 3.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 14`, `func_start: 14`
* *Risk/State:* `state_mutation: 248`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.318
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.014192
  * `Imports (Out-Degree: 1):` common.h, string.h, utils.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/crypto_scrypt-common.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 304.02 | **LOC:** 269 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `escrypt_r` **(Many-Argument Workhorses)** (Impact: 34.9)
  * `escrypt_gensalt_r` **(Many-Argument Workhorses)** (Impact: 30.3)
  * `crypto_pwhash_scryptsalsa208sha256_ll` **(Many-Argument Workhorses)** (Impact: 20.3)
  * `escrypt_parse_setting` **(Many-Argument Workhorses)** (Impact: 17.0)
  * `encode64` **(Stateful Encapsulated Methods)** (Impact: 14.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 27`, `args: 11`, `func_start: 8`
* *Risk/State:* `state_mutation: 54`, `unreferenced_by_name: 3`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 17`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` crypto_pwhash_scryptsalsa208sha256.h, crypto_scrypt.h, common.h, randombytes.h, runtime.h, stdint.h, string.h, utils.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/randombytes/internal/randombytes_internal_random.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 301.82 | **LOC:** 649 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (71.8%), Complexity Load (formerly Cognitive Load) (58.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `safe_read` **(Stateful Encapsulated Methods)** (Impact: 17.1)
    * *Intent:* /* LCOV_EXCL_STOP */
  * `randombytes_internal_random_stir` **(I/O & Config Routines)** (Impact: 14.4)
    * *Intent:* #endif /* _WIN32 */ /* * (Re)seed the generator using the entropy source */
  * `randombytes_internal_random_random_dev_open` **(Stateful Encapsulated Methods)** (Impact: 13.8)
    * *Intent:* # endif /* LCOV_EXCL_START */
  * `randombytes_internal_random_buf` **(Stateful Encapsulated Methods)** (Impact: 9.9)
    * *Intent:* /* * Put `size` random bytes into `buf` and overwrite the key */
  * `randombytes_getentropy` **(Stateful Encapsulated Methods)** (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 68`, `args: 59`, `func_start: 20`, `class_start: 7`
* *Risk/State:* `state_mutation: 56`
* *Architecture:* `io: 3`, `api: 4`, `import: 27`
* *Defense:* `safety: 34`, `immutability_locks: 18`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` assert.h, core.h, crypto_core_hchacha20.h, crypto_stream_chacha20.h, errno.h, fcntl.h, immintrin.h, limits.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/Makefile.in` (MAKEFILE | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 280.94 | **LOC:** 970 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (11.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `distcheck` **(I/O & Config Routines)** (Impact: 33.0)
    * *Intent:* # This target untars the dist file and tries a VPATH configuration. Then # it guarantees that the di...
  * `distdir-am` **(I/O & Config Routines)** (Impact: 28.2)
  * `else` **(I/O & Config Routines)** (Impact: 18.5)
  * `uninstall-pkgconfigDATA` **(I/O & Config Routines)** (Impact: 14.9)
  * `tags-am` **(I/O & Config Routines)** (Impact: 11.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 327`, `func_start: 97`
* *Risk/State:* `safety_bypasses: 19`, `unreferenced_by_name: 3`
* *Architecture:* `io: 42`, `api: 4`
* *Defense:* `safety: 1`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_stream/chacha20/ref/chacha20_ref.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 272.72 | **LOC:** 313 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `chacha20_encrypt_bytes` **(Many-Argument Workhorses)** (Impact: 29.5)
  * `stream_ref_xor_ic` **(C Struct Operations)** (Impact: 6.5)
  * `chacha_ivsetup` **(Stateful Encapsulated Methods)** (Impact: 6.4)
  * `stream_ietf_ext_ref_xor_ic` **(C Struct Operations)** (Impact: 6.2)
  * `stream_ref` **(C Struct Operations)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 22`, `args: 12`, `func_start: 8`, `class_start: 7`
* *Risk/State:* `state_mutation: 113`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` stream_chacha20.h, chacha20_ref.h, core.h, crypto_stream_chacha20.h, common.h, stdint.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/sse/pwhash_scryptsalsa208sha256_sse.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 271.46 | **LOC:** 407 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `escrypt_kdf_sse` **(Many-Argument Workhorses)** (Impact: 67.6)
    * *Intent:* /* * escrypt_kdf(local, passwd, passwdlen, salt, saltlen, * N, r, p, buf, buflen): * Compute scrypt(...
  * `smix` **(Many-Argument Workhorses)** (Impact: 20.5)
    * *Intent:* /* * smix(B, r, N, V, XY): * Compute B = SMix_r(B, N). The input B must be 128r bytes in length; * t...
  * `blockmix_salsa8_xor` **(Many-Argument Workhorses)** (Impact: 6.6)
  * `blockmix_salsa8` **(Stateful Encapsulated Methods)** (Impact: 5.9)
    * *Intent:* /* * blockmix_salsa8(Bin, Bout, r): * Compute Bout = BlockMix_{salsa20/8, r}(Bin). * The input Bin m...
  * `integerify` **(Encapsulated Accessors)** (Impact: 2.2)
    * *Intent:* # undef ARX # undef SALSA20_2ROUNDS # undef SALSA20_8_XOR # undef XOR4 # undef XOR4_2 /* * integerif...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 17`, `args: 48`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 69`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 17`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` crypto_scrypt.h, pbkdf2-sha256.h, emmintrin.h, errno.h, limits.h, common.h, sse2_64_32.h, stdint.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/nosse/pwhash_scryptsalsa208sha256_nosse.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 270.08 | **LOC:** 319 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `escrypt_kdf_nosse` **(Many-Argument Workhorses)** (Impact: 67.3)
    * *Intent:* /* * escrypt_kdf(local, passwd, passwdlen, salt, saltlen, * N, r, p, buf, buflen): * Compute scrypt(...
  * `smix` **(Many-Argument Workhorses)** (Impact: 14.7)
    * *Intent:* /* * smix(B, r, N, V, XY): * Compute B = SMix_r(B, N). The input B must be 128r bytes in length; * t...
  * `salsa20_8` **(Stateful Encapsulated Methods)** (Impact: 6.7)
    * *Intent:* /* * salsa20_8(B): * Apply the salsa20/8 core to the provided block. */
  * `blockmix_salsa8` **(Stateful Encapsulated Methods)** (Impact: 5.8)
    * *Intent:* /* * blockmix_salsa8(Bin, Bout, X, r): * Compute Bout = BlockMix_{salsa20/8, r}(Bin). * The input Bi...
  * `blkxor` **(Stateful Encapsulated Methods)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 17`, `args: 22`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 72`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* `safety: 19`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` crypto_scrypt.h, pbkdf2-sha256.h, errno.h, limits.h, common.h, stdint.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aegis128l/aegis128l_common.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 246.1 | **LOC:** 249 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 1.811; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decrypt_detached` **(Many-Argument Workhorses)** (Impact: 53.3)
  * `encrypt_detached` **(Many-Argument Workhorses)** (Impact: 20.8)
  * `aegis128l_mac` **(Stateful Encapsulated Methods)** (Impact: 16.1)
  * `aegis128l_init` **(Stateful Encapsulated Methods)** (Impact: 5.5)
    * *Intent:* #define RATE 32
  * `aegis128l_declast` **(Stateful Encapsulated Methods)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 130
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 9`, `args: 16`, `func_start: 9`
* *Risk/State:* `state_mutation: 70`
* *Architecture:* `api: 2`
* *Defense:* `safety: 11`, `immutability_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.811
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007389
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-fill-block-avx512f.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 229.72 | **LOC:** 252 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `argon2_fill_segment_avx512f` **(Many-Argument Workhorses)** (Impact: 36.0)
  * `generate_addresses` **(Many-Argument Workhorses)** (Impact: 12.1)
  * `fill_block_with_xor` **(Stateful Encapsulated Methods)** (Impact: 11.6)
  * `fill_block` **(Stateful Encapsulated Methods)** (Impact: 11.4)
    * *Intent:* # pragma GCC target("sse2,ssse3,sse4.1,avx2,avx512f") # endif # ifdef _MSC_VER # include <intrin.h> ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 154
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 5`, `args: 10`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 54`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` argon2-core.h, argon2.h, blamka-round-avx512f.h, emmintrin.h, immintrin.h, intrin.h, common.h, sse2_64_32.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pynacl-1.6.2/src/nacl/public.py` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.9896%)
- `pynacl-1.6.2/src/nacl/signing.py` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.8185%)
- `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/ed25519_ref10_fe_25_5.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.9976%)
- `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/ed25519_ref10_fe_51.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `pynacl-1.6.2/src/nacl/bindings/crypto_secretstream.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.7218%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/common.h` -> **Severity: 18.076** (Embedded: 0.1864 * Error Risk: 96.9598%)
- `pynacl-1.6.2/src/nacl/exceptions.py` -> **Severity: 6.315** (Embedded: 0.0668 * Error Risk: 94.5097%)
- `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/sse2_64_32.h` -> **Severity: 2.863** (Embedded: 0.0443 * Error Risk: 64.5656%)
- `pynacl-1.6.2/src/nacl/encoding.py` -> **Severity: 2.135** (Embedded: 0.0363 * Error Risk: 58.8663%)
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-core.h` -> **Severity: 1.869** (Embedded: 0.0222 * Error Risk: 84.3121%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/common.h` -> **Severity: 4468.6** (Blast Radius: 44.686 * Doc Risk: 100.0%)
- `pynacl-1.6.2/src/nacl/encoding.py` -> **Severity: 1028.907** (Blast Radius: 11.872 * Doc Risk: 86.6667%)
- `pynacl-1.6.2/src/nacl/utils.py` -> **Severity: 750.143** (Blast Radius: 10.502 * Doc Risk: 71.4286%)
- `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/sse2_64_32.h` -> **Severity: 692.9** (Blast Radius: 6.929 * Doc Risk: 100.0%)
- `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/ed25519_ref10_fe_25_5.h` -> **Severity: 331.8** (Blast Radius: 3.318 * Doc Risk: 100.0%)

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
