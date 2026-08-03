# ARCHITECTURAL_BRIEF: pynacl
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/pynacl` |
| **Timestamp** | `2026-08-03T21:23:59.997370+00:00` |
| **Scan Duration** | `1.75s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 359 malicious artifacts.

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
| Total Artifacts | 509 |
| Analyzed Artifacts (Scanned) | 403 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 106 |
| Total LOC | 53998 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 79.2% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6663 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2562 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6345 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 48 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 283 | 31784 | 70.2% |
| PYTHON | 50 | 7580 | 12.4% |
| M4 | 20 | 8083 | 5.0% |
| XML | 17 | 0 | 4.2% |
| PLAINTEXT | 12 | 0 | 3.0% |
| ASSEMBLY | 7 | 2937 | 1.7% |
| MAKEFILE | 5 | 3071 | 1.2% |
| JSON | 4 | 388 | 1.0% |
| YAML | 3 | 142 | 0.7% |
| MARKDOWN | 1 | 0 | 0.2% |
| BATCH | 1 | 13 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.375`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 291 | 72.2% |
| file_cluster_13 | 82 | 20.3% |
| file_cluster_16 | 8 | 2.0% |
| file_cluster_9 | 6 | 1.5% |
| file_cluster_0 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 15 | 3.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 106*

**Composition by Extension & Reason:**
- `.props`: 38x Excluded (Unsupported Extension: '.props'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sln`: 9x Excluded (Unsupported Extension: '.sln')
- `.vcxproj`: 9x Excluded (Unsupported Extension: '.vcxproj')
- `.filters`: 9x Excluded (Unsupported Extension: '.filters')
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 25053 LOC)
- `.am`: 6x Excluded (Unsupported Extension: '.am')
- `.rst`: 3x Excluded (Unsupported Extension: '.rst')
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.in`: 1x Excluded (Machine-Generated Source Code Signature: 4083 LOC), 1x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)
- `.json`: 1x Excluded (Massive Static Asset Blob: 18435 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.cff`: 1x Excluded (Unsupported Extension: '.cff')
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 21.9 | 5.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 15.6 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 22.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 17.5 | 2.3 | 2.3 |
| API Exposure | 0.0 | 19.2 | 8.4 | 9.3 | 0.0 |
| Concurrency Exposure | 0.0 | 47.5 | 0.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 30.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 30.8 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 88.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 50.0 | 49.7 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 67.6 | 96.6 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 31.5 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 8.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.1 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pynacl-1.6.2/src/libsodium/Makefile.in` (Hits: 40)
- `pynacl-1.6.2/setup.py` (Hits: 22)
- `pynacl-1.6.2/tests/test_pwhash.py` (Hits: 13)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **export.h** (`pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/export.h`) — 76 inbound connections
2. **core.h** (`pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/core.h`) — 31 inbound connections
3. **exceptions.py** (`pynacl-1.6.2/src/nacl/exceptions.py`) — 27 inbound connections
4. **runtime.h** (`pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/runtime.h`) — 15 inbound connections
5. **crypto_stream_chacha20.h** (`pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/crypto_stream_chacha20.h`) — 15 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **sodium.h** (`pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium.h`) — 63 outbound dependencies
2. **randombytes_internal_random.c** (`pynacl-1.6.2/src/libsodium/src/libsodium/randombytes/internal/randombytes_internal_random.c`) — 27 outbound dependencies
3. **randombytes_sysrandom.c** (`pynacl-1.6.2/src/libsodium/src/libsodium/randombytes/sysrandom/randombytes_sysrandom.c`) — 21 outbound dependencies
4. **chacha20_dolbeau-avx2.c** (`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_stream/chacha20/dolbeau/chacha20_dolbeau-avx2.c`) — 18 outbound dependencies
5. **utils.c** (`pynacl-1.6.2/src/libsodium/src/libsodium/sodium/utils.c`) — 18 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `sodium_base642bin` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/sodium/codecs.c`) -> Impact: **276.4** | LOC: 69
- `m4_defun` (@ `pynacl-1.6.2/src/libsodium/m4/libtool.m4`) -> Impact: **260.6** | LOC: 2404
  * *Intent:* dnl aclocal-1.4 backwards compatibility: dnl AC_DEFUN([AC_PROG_LIBTOOL], []) dnl AC_DEFUN([AM_PROG_LIBTOOL], []) # _LT_PREPARE_CC_BASENAME # ---------...
- `crypto_pwhash_argon2i` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/pwhash_argon2i.c`) -> Impact: **149.2** | LOC: 45
- `crypto_pwhash_argon2id` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/pwhash_argon2id.c`) -> Impact: **149.2** | LOC: 45
- `decrypt_detached` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aegis128l/aegis128l_common.h`) -> Impact: **137.1** | LOC: 55
- `sodium_hex2bin` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/sodium/codecs.c`) -> Impact: **130.4** | LOC: 62
- `argon2_encode_string` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-encoding.c`) -> Impact: **128.6** | LOC: 67
- `run` (@ `pynacl-1.6.2/setup.py`) -> Impact: **126.6** | LOC: 107
- `crypto_shorthash_siphashx24` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_shorthash/siphash24/ref/shorthash_siphashx24_ref.c`) -> Impact: **105.4** | LOC: 73
  * *Intent:* #include "crypto_shorthash_siphash24.h" #include "private/common.h" #include "shorthash_siphash_ref.h"
- `crypto_shorthash_siphash24` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_shorthash/siphash24/ref/shorthash_siphash24_ref.c`) -> Impact: **105.1** | LOC: 67
  * *Intent:* #include "crypto_shorthash_siphash24.h" #include "private/common.h" #include "shorthash_siphash_ref.h"

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `m4_defun` (@ `pynacl-1.6.2/src/libsodium/m4/libtool.m4`) -> **O(2^N) [Recursive]**
  * *Intent:* dnl aclocal-1.4 backwards compatibility: dnl AC_DEFUN([AC_PROG_LIBTOOL], []) dnl AC_DEFUN([AM_PROG_LIBTOOL], []) # _LT_PREPARE_CC_BASENAME # ---------...
- `run` (@ `pynacl-1.6.2/setup.py`) -> **O(2^N) [Recursive]**
- `verify` (@ `pynacl-1.6.2/src/nacl/pwhash/__init__.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """ Takes a modular crypt encoded stored password hash derived using one of the algorithms supported by `libsodium` and checks if the user provided pa...
- `crypto_box_seal_open` (@ `pynacl-1.6.2/src/nacl/bindings/crypto_box.py`) -> **O(2^N) [Recursive]**
- `crypto_core_ed25519_add` (@ `pynacl-1.6.2/src/nacl/bindings/crypto_core.py`) -> **O(2^N) [Recursive]**
- `crypto_core_ed25519_sub` (@ `pynacl-1.6.2/src/nacl/bindings/crypto_core.py`) -> **O(2^N) [Recursive]**
- `crypto_core_ed25519_scalar_add` (@ `pynacl-1.6.2/src/nacl/bindings/crypto_core.py`) -> **O(2^N) [Recursive]**
- `crypto_core_ed25519_scalar_sub` (@ `pynacl-1.6.2/src/nacl/bindings/crypto_core.py`) -> **O(2^N) [Recursive]**
- `crypto_core_ed25519_scalar_mul` (@ `pynacl-1.6.2/src/nacl/bindings/crypto_core.py`) -> **O(2^N) [Recursive]**
- `crypto_core_ed25519_from_uniform` (@ `pynacl-1.6.2/src/nacl/bindings/crypto_core.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `poly1305_blocks` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_onetimeauth/poly1305/sse2/poly1305_sse2.c`) -> DB Complexity: **457**
- `fe25519_mul` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/ed25519_ref10_fe_25_5.h`) -> DB Complexity: **190**
- `fe25519_sq2` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/ed25519_ref10_fe_25_5.h`) -> DB Complexity: **144**
- `fe25519_sq` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/ed25519_ref10_fe_25_5.h`) -> DB Complexity: **134**
- `chacha20_encrypt_bytes` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_stream/chacha20/ref/chacha20_ref.c`) -> DB Complexity: **83**
- `crypto_core_salsa` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_core/salsa/ref/core_salsa_ref.c`) -> DB Complexity: **74**
  * *Intent:* #include <stdint.h> #include <stdlib.h> #include "crypto_core_salsa20.h" #include "crypto_core_salsa2012.h" #include "crypto_core_salsa208.h" #include...
- `aes_gcm_encrypt_generic` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/aesni/aead_aes256gcm_aesni.c`) -> DB Complexity: **66**
- `aes_gcm_encrypt_generic` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/armcrypto/aead_aes256gcm_armcrypto.c`) -> DB Complexity: **66**
- `fe25519_mul` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/ed25519_ref10_fe_51.h`) -> DB Complexity: **66**
- `poly1305_finish` (@ `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_onetimeauth/poly1305/donna/poly1305_donna32.h`) -> DB Complexity: **63**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `pynacl-1.6.2/src/libsodium` | 12 | 5010.52 | 3.94% | 2.96% |
| `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2` | 18 | 4091.68 | 58.97% | 23.07% |
| `pynacl-1.6.2/src/libsodium/m4` | 16 | 2691.96 | 10.08% | 35.58% |
| `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium` | 65 | 2519.38 | 3.95% | 0.0% |
| `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/ref` | 13 | 2016.42 | 53.19% | 22.53% |
| `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private` | 10 | 1975.5 | 14.95% | 0.0% |
| `pynacl-1.6.2/tests` | 19 | 1628.9 | 3.85% | 0.0% |
| `pynacl-1.6.2/src/libsodium/src/libsodium/sodium` | 5 | 1562.3 | 43.54% | 45.74% |
| `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/armcrypto` | 1 | 1522.7 | 100.0% | 17.0% |
| `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/aesni` | 1 | 1519.88 | 100.0% | 17.26% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `pynacl-1.6.2/src/nacl/encoding.py` -> **100.0%** Exposure
- `pynacl-1.6.2/src/nacl/public.py` -> **100.0%** Exposure
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_box/crypto_box.c` -> **100.0%** Exposure
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_box/curve25519xchacha20poly1305/box_curve25519xchacha20poly1305.c` -> **100.0%** Exposure
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_box/curve25519xsalsa20poly1305/box_curve25519xsalsa20poly1305.c` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `pynacl-1.6.2/src/bindings/minimal/crypto_pwhash.h` -> **100.0%** Exposure
- `pynacl-1.6.2/src/bindings/minimal/crypto_scalarmult.h` -> **100.0%** Exposure
- `pynacl-1.6.2/src/bindings/minimal/crypto_shorthash.h` -> **100.0%** Exposure
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/aesni/aead_aes256gcm_aesni.c` -> **100.0%** Exposure
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/armcrypto/aead_aes256gcm_armcrypto.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pynacl-1.6.2/tests/test_pwhash.py` -> **33** Orphaned Functions | **0** Duplicates
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/crypto_pwhash.c` -> **25** Orphaned Functions | **0** Duplicates
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/pwhash_argon2i.c` -> **22** Orphaned Functions | **0** Duplicates
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/chacha20poly1305/aead_chacha20poly1305.c` -> **16** Orphaned Functions | **4** Duplicates
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/pwhash_argon2id.c` -> **20** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/ref/blake2b-compress-avx2.c`** -> AI Confidence: **99.48%**
2. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-fill-block-avx2.c`** -> AI Confidence: **99.48%**
3. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-fill-block-avx512f.c`** -> AI Confidence: **99.48%**
4. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-fill-block-ref.c`** -> AI Confidence: **99.48%**
5. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-fill-block-ssse3.c`** -> AI Confidence: **99.48%**
6. **`pynacl-1.6.2/src/libsodium/src/libsodium/sodium/codecs.c`** -> AI Confidence: **99.48%**
7. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/ref/blake2b-compress-sse41.c`** -> AI Confidence: **99.39%**
8. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/pbkdf2-sha256.c`** -> AI Confidence: **99.39%**
9. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_secretbox/crypto_secretbox_easy.c`** -> AI Confidence: **99.39%**
10. **`pynacl-1.6.2/src/libsodium/src/libsodium/sodium/runtime.c`** -> AI Confidence: **99.39%**
11. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_core/ed25519/ref10/ed25519_ref10.c`** -> AI Confidence: **99.35%**
12. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/blake2b-long.c`** -> AI Confidence: **99.34%**
13. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_shorthash/siphash24/ref/shorthash_siphash24_ref.c`** -> AI Confidence: **99.32%**
14. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_shorthash/siphash24/ref/shorthash_siphashx24_ref.c`** -> AI Confidence: **99.32%**
15. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aegis128l/aead_aegis128l.c`** -> AI Confidence: **99.31%**
16. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aegis256/aead_aegis256.c`** -> AI Confidence: **99.31%**
17. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/aesni/aead_aes256gcm_aesni.c`** -> AI Confidence: **99.31%**
18. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/armcrypto/aead_aes256gcm_armcrypto.c`** -> AI Confidence: **99.31%**
19. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/ref/blake2b-compress-ssse3.c`** -> AI Confidence: **99.31%**
20. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/ref/blake2b-ref.c`** -> AI Confidence: **99.31%**
21. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/ref/generichash_blake2b.c`** -> AI Confidence: **99.31%**
22. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_hash/sha256/cp/hash_sha256_cp.c`** -> AI Confidence: **99.31%**
23. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_hash/sha512/cp/hash_sha512_cp.c`** -> AI Confidence: **99.31%**
24. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-core.c`** -> AI Confidence: **99.31%**
25. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-encoding.c`** -> AI Confidence: **99.31%**
26. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/crypto_scrypt-common.c`** -> AI Confidence: **99.31%**
27. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/nosse/pwhash_scryptsalsa208sha256_nosse.c`** -> AI Confidence: **99.31%**
28. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/sse/pwhash_scryptsalsa208sha256_sse.c`** -> AI Confidence: **99.31%**
29. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_scalarmult/curve25519/ref10/x25519_ref10.c`** -> AI Confidence: **99.31%**
30. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_secretbox/xchacha20poly1305/secretbox_xchacha20poly1305.c`** -> AI Confidence: **99.31%**
31. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_sign/ed25519/ref10/obsolete.c`** -> AI Confidence: **99.31%**
32. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_sign/ed25519/ref10/open.c`** -> AI Confidence: **99.31%**
33. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_sign/ed25519/ref10/sign.c`** -> AI Confidence: **99.31%**
34. **`pynacl-1.6.2/src/libsodium/src/libsodium/crypto_stream/salsa20/stream_salsa20.c`** -> AI Confidence: **99.31%**
35. **`pynacl-1.6.2/src/libsodium/src/libsodium/randombytes/internal/randombytes_internal_random.c`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `pynacl-1.6.2/tests/test_hash.py` -> **100.0%** Exposure
- `pynacl-1.6.2/tests/test_shorthash.py` -> **100.0%** Exposure
- `pynacl-1.6.2/tests/test_utils.py` -> **84.4774%** Exposure
- `pynacl-1.6.2/tests/test_encoding.py` -> **20.4281%** Exposure
- `pynacl-1.6.2/tests/test_public.py` -> **0.0007%** Exposure
### Exploit Generation Surface
- `pynacl-1.6.2/setup.py` -> **100.0%** Exposure
- `pynacl-1.6.2/src/nacl/bindings/crypto_box.py` -> **100.0%** Exposure
- `pynacl-1.6.2/src/nacl/public.py` -> **100.0%** Exposure
- `pynacl-1.6.2/tests/test_bindings.py` -> **100.0%** Exposure
- `pynacl-1.6.2/tests/test_pwhash.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `pynacl-1.6.2/src/libsodium/Makefile.in` -> **0.0091%** Exposure
### Raw Memory Manipulation
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/ref/blake2b-ref.c` -> **9.9999%** Exposure
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/crypto_scrypt.h` -> **9.7805%** Exposure
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_secretbox/crypto_secretbox_easy.c` -> **0.6079%** Exposure
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/nosse/pwhash_scryptsalsa208sha256_nosse.c` -> **0.3484%** Exposure
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_secretbox/xchacha20poly1305/secretbox_xchacha20poly1305.c` -> **0.3297%** Exposure
### Algorithmic DoS Exposure
- `pynacl-1.6.2/setup.py` -> **100.0%** Exposure
- `pynacl-1.6.2/src/nacl/public.py` -> **100.0%** Exposure
- `pynacl-1.6.2/tests/test_pwhash.py` -> **100.0%** Exposure
- `pynacl-1.6.2/tests/test_secretstream.py` -> **100.0%** Exposure
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aegis128l/aead_aegis128l.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1518` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_core/salsa/ref/core_salsa_ref.c` (C) -> Cumulative Risk: **817.81**
- **Archetype:** `file_cluster_13` (Distance: 13.746 IQR)
- **Magnitude:** 234.84 | **LOC:** 196 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9836%)
- **Heaviest Functions:** `crypto_core_salsa` (Impact: 22.7), `crypto_core_salsa20` (Impact: 7.1), `crypto_core_salsa2012` (Impact: 7.1)

### 2. `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_scalarmult/ed25519/ref10/scalarmult_ed25519_ref10.c` (C) -> Cumulative Risk: **787.43**
- **Archetype:** `file_cluster_8` (Distance: 12.445 IQR)
- **Magnitude:** 224.46 | **LOC:** 122 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `_crypto_scalarmult_ed25519` (Impact: 71.8), `_crypto_scalarmult_ed25519_base` (Impact: 36.1), `_crypto_scalarmult_ed25519_is_inf` (Impact: 7.4)

### 3. `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/argon2.c` (C) -> Cumulative Risk: **781.39**
- **Archetype:** `file_cluster_13` (Distance: 13.794 IQR)
- **Magnitude:** 307.1 | **LOC:** 284 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.9994%)
- **Heaviest Functions:** `argon2_verify` (Impact: 63.7), `argon2_hash` (Impact: 42.4), `argon2_ctx` (Impact: 13.3)

### 4. `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/scrypt_platform.c` (C) -> Cumulative Risk: **776.36**
- **Archetype:** `file_cluster_13` (Distance: 12.422 IQR)
- **Magnitude:** 109.84 | **LOC:** 113 | **CtrlFlow:** 68.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (96.7087%)
- **Heaviest Functions:** `escrypt_alloc_region` (Impact: 36.5), `escrypt_free_region` (Impact: 12.8), `escrypt_init_local` (Impact: 1.4)

### 5. `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_secretbox/xchacha20poly1305/secretbox_xchacha20poly1305.c` (C) -> Cumulative Risk: **773.45**
- **Archetype:** `file_cluster_13` (Distance: 12.163 IQR)
- **Magnitude:** 331.08 | **LOC:** 178 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9999%), State Flux (99.9937%)
- **Heaviest Functions:** `crypto_secretbox_xchacha20poly1305_open_` (Impact: 104.4), `crypto_secretbox_xchacha20poly1305_detac` (Impact: 86.1), `crypto_secretbox_xchacha20poly1305_easy` (Impact: 17.8)

### 6. `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/pwhash_argon2i.c` (C) -> Cumulative Risk: **772.15**
- **Archetype:** `file_cluster_13` (Distance: 13.334 IQR)
- **Magnitude:** 508.8 | **LOC:** 295 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.998%)
- **Heaviest Functions:** `crypto_pwhash_argon2i` (Impact: 149.2), `crypto_pwhash_argon2i_str` (Impact: 70.1), `_needs_rehash` (Impact: 46.6)

### 7. `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_shorthash/siphash24/ref/shorthash_siphashx24_ref.c` (C) -> Cumulative Risk: **770.3**
- **Archetype:** `file_cluster_13` (Distance: 13.376 IQR)
- **Magnitude:** 190.76 | **LOC:** 78 | **CtrlFlow:** 92.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.5502%)
- **Heaviest Functions:** `crypto_shorthash_siphashx24` (Impact: 105.4)

### 8. `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_scalarmult/ristretto255/ref10/scalarmult_ristretto255_ref10.c` (C) -> Cumulative Risk: **766.47**
- **Archetype:** `file_cluster_13` (Distance: 12.653 IQR)
- **Magnitude:** 97.7 | **LOC:** 64 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `crypto_scalarmult_ristretto255` (Impact: 29.1), `crypto_scalarmult_ristretto255_base` (Impact: 19.1), `crypto_scalarmult_ristretto255_bytes` (Impact: 1.7)

### 9. `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_stream/salsa2012/ref/stream_salsa2012_ref.c` (C) -> Cumulative Risk: **765.32**
- **Archetype:** `file_cluster_13` (Distance: 13.484 IQR)
- **Magnitude:** 303.66 | **LOC:** 107 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9834%)
- **Heaviest Functions:** `crypto_stream_salsa2012_xor` (Impact: 88.2), `crypto_stream_salsa2012` (Impact: 72.6)

### 10. `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_stream/salsa208/ref/stream_salsa208_ref.c` (C) -> Cumulative Risk: **765.32**
- **Archetype:** `file_cluster_13` (Distance: 13.484 IQR)
- **Magnitude:** 293.66 | **LOC:** 107 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9834%)
- **Heaviest Functions:** `crypto_stream_salsa208_xor` (Impact: 88.2), `crypto_stream_salsa208` (Impact: 62.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pynacl-1.6.2/src/libsodium/aclocal.m4` (M4 | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.162 IQR)
- **Top Global Matches:** file_cluster_8: 8.162, file_cluster_7: 9.071, file_cluster_1: 9.279
- **Magnitude:** 2727.36 | **LOC:** 1389 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.8182%), Tech Debt (35.4755%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 29`, `args: 85`, `func_start: 40`
* *Risk/State:* `planned_debt: 1`, `fragile_debt: 8`
* *Architecture:* `api: 33`, `import: 15`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/Makefile.in` (MAKEFILE | Tier 1 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.907 IQR)
- **Top Global Matches:** file_cluster_8: 7.907, file_cluster_7: 8.929, file_cluster_1: 9.132
- **Magnitude:** 2101.72 | **LOC:** 970 | **CtrlFlow:** 33.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.9677%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 327`, `func_start: 92`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 7`
* *Architecture:* `io: 40`, `api: 4`
* *Defense:* `safety: 1`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/armcrypto/aead_aes256gcm_armcrypto.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.591 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.19 IQR)
- **Top Global Matches:** file_cluster_8: 14.591, file_cluster_13: 14.612, file_cluster_11: 14.769
- **Magnitude:** 1522.7 | **LOC:** 1034 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 66
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (17.0037%)
**Top Internal Functions/Classes:**
  * `aes_gcm_encrypt_generic` (Impact: 95.7 | O(N^6) | DB: 66)
  * `aes_gcm_decrypt_generic` (Impact: 80.5 | O(N^6) | DB: 50)
  * `crypto_aead_aes256gcm_encrypt_detached_a` (Impact: 71.7 | O(N^6) | DB: 6)
  * `crypto_aead_aes256gcm_decrypt_detached_a` (Impact: 68.6 | O(N^6) | DB: 5)
  * `crypto_aead_aes256gcm_verify_mac` (Impact: 66.2 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 54`, `args: 11`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 679`, `orphaned_logic: 7`
* *Architecture:* `api: 181`, `import: 14`
* *Defense:* `safety: 50`, `immutability_locks: 131`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` common.h, errno.h, stdlib.h, stdint.h, limits.h, export.h, randombytes.h, utils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/aesni/aead_aes256gcm_aesni.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.658 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.17 IQR)
- **Top Global Matches:** file_cluster_13: 14.658, file_cluster_8: 14.669, file_cluster_11: 14.828
- **Magnitude:** 1519.88 | **LOC:** 1016 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 66
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (17.2621%)
**Top Internal Functions/Classes:**
  * `aes_gcm_encrypt_generic` (Impact: 103.2 | O(N^6) | DB: 66)
  * `aes_gcm_decrypt_generic` (Impact: 80.5 | O(N^6) | DB: 50)
  * `crypto_aead_aes256gcm_encrypt_detached_a` (Impact: 71.7 | O(N^6) | DB: 6)
  * `crypto_aead_aes256gcm_decrypt_detached_a` (Impact: 68.6 | O(N^6) | DB: 5)
  * `crypto_aead_aes256gcm_verify_mac` (Impact: 66.2 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 51`, `args: 11`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 675`, `orphaned_logic: 7`
* *Architecture:* `api: 177`, `import: 16`
* *Defense:* `safety: 50`, `immutability_locks: 127`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` wmmintrin.h, common.h, errno.h, stdlib.h, stdint.h, limits.h, export.h, randombytes.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/include/Makefile.in` (MAKEFILE | Tier 1 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.394 IQR)
- **Top Global Matches:** file_cluster_8: 7.394, file_cluster_7: 8.51, file_cluster_1: 8.696
- **Magnitude:** 1289.92 | **LOC:** 735 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.2347%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 263`, `func_start: 71`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`
* *Architecture:* `io: 6`, `api: 4`
* *Defense:* `safety: 1`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/Makefile.in` (MAKEFILE | Tier 1 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.342 IQR)
- **Top Global Matches:** file_cluster_8: 7.342, file_cluster_7: 8.449, file_cluster_1: 8.643
- **Magnitude:** 1236.52 | **LOC:** 692 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.4105%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 285`, `func_start: 68`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`
* *Architecture:* `io: 7`, `api: 4`
* *Defense:* `safety: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/ed25519_ref10_fe_25_5.h` (C | Tier 4 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.101 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.077 IQR)
- **Top Global Matches:** file_cluster_8: 12.101, file_cluster_7: 12.53, file_cluster_13: 12.611
- **Magnitude:** 1208.16 | **LOC:** 1031 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 190
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fe25519_mul` (Impact: 3.5 | O(N^4) | DB: 190)
  * `fe25519_mul32` (Impact: 3.0 | O(N^3) | DB: 61)
  * `fe25519_add` (Impact: 2.0 | O(N^1) | DB: 20)
  * `fe25519_sub` (Impact: 2.0 | O(N^1) | DB: 20)
  * `fe25519_neg` (Impact: 2.0 | O(N^1) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 14`, `func_start: 14`
* *Risk/State:* `state_mutation: 693`
* *Architecture:* `api: 472`, `import: 3`
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002481
  * `Imports (Out-Degree: 0):` string.h, common.h, utils.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_onetimeauth/poly1305/sse2/poly1305_sse2.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.452 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.93 IQR)
- **Top Global Matches:** file_cluster_8: 13.452, file_cluster_13: 13.736, file_cluster_7: 13.871
- **Magnitude:** 1084.78 | **LOC:** 958 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 457
- **Risk Profile:** Cognitive Load (62.256%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `poly1305_blocks` (Impact: 72.0 | O(N^6) | DB: 457)
  * `poly1305_block_copy31` (Impact: 43.5 | O(N^6) | DB: 9)
  * `poly1305_init_ext` (Impact: 29.6 | O(N^4) | DB: 44)
  * `poly1305_finish_ext` (Impact: 25.8 | O(N^5) | DB: 10)
  * `poly1305_update` (Impact: 22.1 | O(N^4) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 60`, `args: 4`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 770`
* *Architecture:* `api: 67`, `import: 9`
* *Defense:* `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` common.h, utils.h, onetimeauth_poly1305.h, stdint.h, sse2_64_32.h, poly1305_sse2.h, crypto_verify_16.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/m4/ltsugar.m4` (M4 | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.646 IQR)
- **Top Global Matches:** file_cluster_8: 9.646, file_cluster_7: 10.497, file_cluster_17: 10.544
- **Magnitude:** 1031.95 | **LOC:** 125 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (23.7458%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `args: 69`, `func_start: 14`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/sodium/codecs.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.903 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 4.882 IQR)
- **Top Global Matches:** file_cluster_13: 14.903, file_cluster_8: 15.037, file_cluster_11: 15.131
- **Magnitude:** 932.06 | **LOC:** 336 | **CtrlFlow:** 83.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (85.3297%), Tech Debt (33.5187%)
**Top Internal Functions/Classes:**
  * `sodium_base642bin` (Impact: 276.4 | O(N^6) | DB: 26)
  * `sodium_hex2bin` (Impact: 130.4 | O(N^4) | DB: 27)
  * `sodium_bin2base64` (Impact: 101.1 | O(N^4) | DB: 30)
  * `_sodium_base642bin_skip_padding` (Impact: 61.2 | O(N^6) | DB: 6)
  * `sodium_bin2hex` (Impact: 19.2 | O(N^3) | DB: 8)
    * *Intent:* #include <assert.h> #include <errno.h> #include <limits.h> #include <stddef.h> #include <stdint.h> #...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 13`, `args: 10`, `func_start: 11`
* *Risk/State:* `state_mutation: 263`, `orphaned_logic: 5`
* *Architecture:* `api: 54`, `import: 10`
* *Defense:* `safety: 40`, `test: 1`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` common.h, errno.h, stdlib.h, stdint.h, limits.h, stddef.h, utils.h, assert.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_core/ed25519/ref10/ed25519_ref10.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.821 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.865 IQR)
- **Top Global Matches:** file_cluster_8: 11.821, file_cluster_7: 12.342, file_cluster_13: 12.524
- **Magnitude:** 850.78 | **LOC:** 2877 | **CtrlFlow:** 69.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (32.8805%), Tech Debt (10.0257%)
**Top Internal Functions/Classes:**
  * `slide_vartime` (Impact: 99.1 | O(N^6) | DB: 17)
  * `fe25519_invert` (Impact: 16.2 | O(N^2) | DB: 16)
    * *Intent:* /* * Field arithmetic: * Use 5*51 bit limbs on 64-bit systems with support for 128 bit arithmetic, *...
  * `fe25519_pow22523` (Impact: 14.6 | O(N^2) | DB: 14)
  * `sc25519_is_canonical` (Impact: 11.1 | O(N^2) | DB: 7)
  * `ge25519_frombytes_negate_vartime` (Impact: 10.2 | O(N^3))
    * *Intent:* fe25519_mul(x_sqrtm1, h->X, sqrtm1); /* x*sqrt(-1) */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 43`, `args: 17`, `func_start: 39`
* *Risk/State:* `state_mutation: 413`, `orphaned_logic: 7`
* *Architecture:* `api: 140`, `import: 12`
* *Defense:* `safety: 1`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` common.h, utils.h, stdlib.h, stdint.h, stddef.h, fe.h, fe.h, base.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/builds/Makefile.in` (MAKEFILE | Tier 1 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.97 IQR)
- **Top Global Matches:** file_cluster_8: 6.97, file_cluster_7: 8.132, file_cluster_1: 8.324
- **Magnitude:** 749.48 | **LOC:** 599 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.2172%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 237`, `func_start: 59`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 2`
* *Architecture:* `io: 5`, `api: 4`
* *Defense:* `safety: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/chacha20poly1305/aead_chacha20poly1305.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.764 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.174 IQR)
- **Top Global Matches:** file_cluster_8: 11.764, file_cluster_13: 11.851, file_cluster_0: 12.23
- **Magnitude:** 530.48 | **LOC:** 401 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (26.1977%), Tech Debt (99.4533%)
**Top Internal Functions/Classes:**
  * `crypto_aead_chacha20poly1305_encrypt` (Impact: 45.8 | O(N^6) | DB: 4)
  * `crypto_aead_chacha20poly1305_ietf_encryp` (Impact: 45.8 | O(N^6) | DB: 4)
  * `crypto_aead_chacha20poly1305_decrypt` (Impact: 45.7 | O(N^6) | DB: 5)
  * `crypto_aead_chacha20poly1305_ietf_decryp` (Impact: 45.7 | O(N^6) | DB: 5)
  * `crypto_aead_chacha20poly1305_ietf_decryp` (Impact: 35.9 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 38`, `args: 20`, `func_start: 20`
* *Risk/State:* `state_mutation: 69`, `duplicate_logic: 4`, `orphaned_logic: 16`
* *Architecture:* `api: 128`, `import: 13`
* *Defense:* `safety: 10`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` common.h, crypto_stream_chacha20.h, utils.h, stdlib.h, stdint.h, limits.h, randombytes.h, crypto_onetimeauth_poly1305.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/m4/ax_pthread.m4` (M4 | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.044 IQR)
- **Top Global Matches:** file_cluster_8: 7.044, file_cluster_7: 8.14, file_cluster_1: 8.373
- **Magnitude:** 525.68 | **LOC:** 523 | **CtrlFlow:** 86.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.9801%), Tech Debt (28.9578%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 3`, `args: 3`, `func_start: 1`
* *Risk/State:* `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 6`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/pwhash_argon2i.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.334 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 4.461 IQR)
- **Top Global Matches:** file_cluster_13: 13.334, file_cluster_8: 13.516, file_cluster_0: 13.724
- **Magnitude:** 508.8 | **LOC:** 295 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (95.4235%), Tech Debt (99.7879%)
**Top Internal Functions/Classes:**
  * `crypto_pwhash_argon2i` (Impact: 149.2 | O(N^6) | DB: 6)
  * `crypto_pwhash_argon2i_str` (Impact: 70.1 | O(N^6) | DB: 2)
  * `_needs_rehash` (Impact: 46.6 | O(N^3) | DB: 19)
  * `crypto_pwhash_argon2i_str_verify` (Impact: 36.4 | O(N^6) | DB: 4)
  * `crypto_pwhash_argon2i_str_needs_rehash` (Impact: 7.3 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 59`, `args: 24`, `func_start: 24`
* *Risk/State:* `state_mutation: 93`, `orphaned_logic: 22`
* *Architecture:* `api: 63`, `import: 15`
* *Defense:* `safety: 28`, `immutability_locks: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` crypto_pwhash.h, common.h, errno.h, stdlib.h, stdint.h, limits.h, stddef.h, argon2.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-core.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.246 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.913 IQR)
- **Top Global Matches:** file_cluster_13: 12.246, file_cluster_8: 12.258, file_cluster_7: 12.559
- **Magnitude:** 488.04 | **LOC:** 557 | **CtrlFlow:** 60.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (62.8978%), Tech Debt (24.0736%)
**Top Internal Functions/Classes:**
  * `argon2_validate_inputs` (Impact: 70.2 | O(N^3))
  * `allocate_memory` (Impact: 44.8 | O(N^5) | DB: 22)
  * `argon2_initial_hash` (Impact: 35.6 | O(N^6) | DB: 2)
  * `argon2_pick_best_implementation` (Impact: 31.2 | O(N^2) | DB: 4)
  * `argon2_finalize` (Impact: 15.7 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 60`, `args: 3`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 146`, `orphaned_logic: 5`
* *Architecture:* `api: 62`, `import: 14`
* *Defense:* `safety: 1`, `doc: 8`, `immutability_locks: 10`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` common.h, stdio.h, errno.h, stdlib.h, stdint.h, utils.h, types.h, blake2b-long.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/tests/test_bindings.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.563 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.648 IQR)
- **Top Global Matches:** file_cluster_8: 10.563, file_cluster_0: 11.032, file_cluster_7: 11.16
- **Magnitude:** 485.3 | **LOC:** 1023 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.6857%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_box_easy_wrong_lengths` (Impact: 47.0 | O(N^3))
  * `test_box_wrong_lengths` (Impact: 46.7 | O(N^3))
  * `test_ed25519_unavailable` (Impact: 29.8 | O(N^2))
  * `test_secretbox_easy_wrong_length` (Impact: 18.0 | O(N^3))
  * `test_secretbox_wrong_length` (Impact: 17.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 162`, `args: 43`, `func_start: 43`
* *Risk/State:* None
* *Architecture:* `api: 82`, `import: 11`
* *Defense:* `safety: 95`, `doc: 8`, `test: 221`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.657
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.002481
  * `Imports (Out-Degree: 3):` hypothesis, nacl.exceptions, nacl.utils, .test_signing, .utils, pytest, nacl, typing...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-encoding.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.214 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.183 IQR)
- **Top Global Matches:** file_cluster_13: 13.214, file_cluster_8: 13.348, file_cluster_11: 13.466
- **Magnitude:** 465.84 | **LOC:** 307 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (94.5474%), Tech Debt (21.0693%)
**Top Internal Functions/Classes:**
  * `argon2_encode_string` (Impact: 128.6 | O(N^6) | DB: 12)
  * `argon2_decode_string` (Impact: 103.8 | O(N^6) | DB: 23)
  * `decode_decimal` (Impact: 36.1 | O(N^3) | DB: 9)
    * *Intent:* #include "argon2-encoding.h" #include "argon2-core.h" #include "utils.h" #include <limits.h> #includ...
  * `u32_to_string` (Impact: 11.1 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 30`, `args: 3`, `func_start: 4`
* *Risk/State:* `state_mutation: 137`, `orphaned_logic: 2`
* *Architecture:* `api: 45`, `import: 7`
* *Defense:* `safety: 9`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` stdio.h, utils.h, stdlib.h, limits.h, argon2-core.h, argon2-encoding.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/ref/blake2b-load-avx2.h` (C | Tier 4 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.17 IQR)
- **Top Global Matches:** file_cluster_8: 14.17, file_cluster_7: 14.698, file_cluster_13: 14.811
- **Magnitude:** 452.82 | **LOC:** 341 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (68.0275%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `args: 144`
* *Risk/State:* `state_mutation: 432`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.132
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003309
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/pwhash_scryptsalsa208sha256.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.912 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 4.754 IQR)
- **Top Global Matches:** file_cluster_13: 12.912, file_cluster_8: 12.987, file_cluster_0: 13.222
- **Magnitude:** 447.78 | **LOC:** 302 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (79.3369%), Tech Debt (99.9988%)
**Top Internal Functions/Classes:**
  * `pickparams` (Impact: 69.2 | O(N^4) | DB: 12)
  * `crypto_pwhash_scryptsalsa208sha256_str` (Impact: 62.7 | O(N^6) | DB: 4)
  * `crypto_pwhash_scryptsalsa208sha256` (Impact: 61.0 | O(N^6) | DB: 3)
  * `crypto_pwhash_scryptsalsa208sha256_str_n` (Impact: 50.4 | O(N^6) | DB: 3)
  * `crypto_pwhash_scryptsalsa208sha256_str_v` (Impact: 21.4 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 53`, `args: 21`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 74`, `duplicate_logic: 12`, `orphaned_logic: 6`
* *Architecture:* `api: 70`, `import: 10`
* *Defense:* `safety: 26`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` common.h, errno.h, utils.h, stdint.h, limits.h, stddef.h, randombytes.h, crypto_pwhash_scryptsalsa208sha256.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/ref/blake2b-ref.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.143 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.294 IQR)
- **Top Global Matches:** file_cluster_8: 12.143, file_cluster_13: 12.286, file_cluster_7: 12.636
- **Magnitude:** 423.5 | **LOC:** 439 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (75.3864%), Tech Debt (17.4502%)
**Top Internal Functions/Classes:**
  * `blake2b_salt_personal` (Impact: 47.4 | O(N^6))
  * `blake2b_init_key_salt_personal` (Impact: 40.8 | O(N^6) | DB: 6)
  * `blake2b` (Impact: 27.8 | O(N^3))
  * `blake2b_pick_best_implementation` (Impact: 26.9 | O(N^2) | DB: 4)
  * `blake2b_init_salt_personal` (Impact: 26.0 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 35`, `args: 1`, `func_start: 17`
* *Risk/State:* `state_mutation: 146`, `orphaned_logic: 3`
* *Architecture:* `api: 34`, `import: 10`
* *Defense:* `safety: 5`, `test: 1`, `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` common.h, utils.h, stdlib.h, stdint.h, stddef.h, assert.h, core.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_stream/salsa20/xmm6int/u4.h` (C | Tier 4 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.395 IQR)
- **Top Global Matches:** file_cluster_8: 13.395, file_cluster_7: 13.92, file_cluster_1: 14.133
- **Magnitude:** 416.64 | **LOC:** 548 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (43.9103%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `args: 263`
* *Risk/State:* `state_mutation: 392`
* *Architecture:* None
* *Defense:* `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/m4/libtool.m4` (M4 | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.734 IQR)
- **Top Global Matches:** file_cluster_8: 9.734, file_cluster_7: 10.447, file_cluster_1: 10.64
- **Magnitude:** 403.18 | **LOC:** 8489 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (5.0709%), Tech Debt (45.2558%)
**Top Internal Functions/Classes:**
  * `m4_defun` (Impact: 260.6 | O(2^N) | DB: 7)
    * *Intent:* dnl aclocal-1.4 backwards compatibility: dnl AC_DEFUN([AC_PROG_LIBTOOL], []) dnl AC_DEFUN([AM_PROG_L...
  * `m4_defun` (Impact: 4.8 | O(2^N))
    * *Intent:* # _LT_LANG_GO_CONFIG([TAG]) # -------------------------- # Ensure that the configuration variables f...
  * `AC_DEFUN` (Impact: 2.4 | O(N^1))
    * *Intent:* # LT_INIT([OPTIONS]) # ------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 108`, `args: 1187`, `func_start: 112`
* *Risk/State:* `state_mutation: 15`, `dead_code: 33`, `planned_debt: 3`, `fragile_debt: 52`, `duplicate_logic: 2`
* *Architecture:* `api: 9`
* *Defense:* `safety: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_stream/salsa20/xmm6int/u8.h` (C | Tier 4 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.355 IQR)
- **Top Global Matches:** file_cluster_8: 13.355, file_cluster_7: 13.88, file_cluster_1: 14.095
- **Magnitude:** 388.26 | **LOC:** 478 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (44.1457%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `args: 254`
* *Risk/State:* `state_mutation: 365`
* *Architecture:* None
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/private/ed25519_ref10_fe_51.h` (C | Tier 4 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.591 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.896 IQR)
- **Top Global Matches:** file_cluster_8: 11.591, file_cluster_7: 12.102, file_cluster_13: 12.109
- **Magnitude:** 383.16 | **LOC:** 509 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 66
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fe25519_sub` (Impact: 2.0 | O(N^1) | DB: 26)
  * `fe25519_cmov` (Impact: 2.0 | O(N^1) | DB: 21)
    * *Intent:* */
  * `fe25519_cswap` (Impact: 2.0 | O(N^1) | DB: 31)
  * `fe25519_mul` (Impact: 2.0 | O(N^1) | DB: 66)
  * `fe25519_sq` (Impact: 2.0 | O(N^1) | DB: 54)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 14`, `func_start: 14`
* *Risk/State:* `state_mutation: 281`
* *Architecture:* `api: 71`, `import: 3`
* *Defense:* `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002481
  * `Imports (Out-Degree: 0):` string.h, common.h, utils.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `pynacl-1.6.2/tests/test_kx.py` (PYTHON) | Magnitude: 52.34 | Delta: **0.125 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 21, test: 21, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pynacl-1.6.2/src/nacl/bindings/sodium_core.py` (PYTHON) | Magnitude: 6.02 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 6, import: 3, encapsulation: 3
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/aesni/aead_aes256gcm_aesni.c` (C) | Magnitude: 1519.88 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 675, indent_spaces: 624, pointers: 256, api: 177
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-core.c` (C) | Magnitude: 488.04 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 305, pointers: 162, state_mutation: 146, branch: 91
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_sign/ed25519/ref10/keypair.c` (C) | Magnitude: 65.84 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 43, api: 15, pointers: 13, import: 8
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_core/salsa/ref/core_salsa_ref.c` (C) | Magnitude: 234.84 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 132, indent_spaces: 100, api: 35, bitwise_ops: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `pynacl-1.6.2/src/nacl/hash.py` (PYTHON) | Magnitude: 15.08 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 72, indent_spaces: 24, structural_boundaries: 12, api: 8
- `pynacl-1.6.2/tests/utils.py` (PYTHON) | Magnitude: 28.06 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 24, branch: 16, generics: 13
- `pynacl-1.6.2/src/nacl/bindings/randombytes.py` (PYTHON) | Magnitude: 21.0 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 10, doc: 7, args: 2
- `pynacl-1.6.2/src/nacl/public.py` (PYTHON) | Magnitude: 138.34 | Delta: **0.118 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 185, structural_boundaries: 63, encapsulation: 51, doc: 45
- `pynacl-1.6.2/src/nacl/bindings/crypto_hash.py` (PYTHON) | Magnitude: 16.32 | Delta: **0.138 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 12, doc: 9, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pynacl-1.6.2/src/bindings/minimal/crypto_core.h` (C) | Magnitude: 40.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 22, pointers: 19, immutability_locks: 18, structural_boundaries: 8
- `pynacl-1.6.2/tests/test_generichash.py` (PYTHON) | Magnitude: 66.96 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 135, structural_boundaries: 47, test: 41, args: 15
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_scalarmult/ed25519/ref10/scalarmult_ed25519_ref10.c` (C) | Magnitude: 224.46 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, state_mutation: 47, api: 27, pointers: 26
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_hash/sha512/cp/hash_sha512_cp.c` (C) | Magnitude: 222.28 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 169, state_mutation: 124, pointers: 55, api: 18
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aes256gcm/armcrypto/aead_aes256gcm_armcrypto.c` (C) | Magnitude: 1522.7 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 679, indent_spaces: 637, pointers: 259, api: 181

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `pynacl-1.6.2/src/bindings/minimal/crypto_pwhash.h` (C) | Magnitude: 46.68 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 36, state_mutation: 24, safety: 18, structural_boundaries: 15
- `pynacl-1.6.2/src/bindings/minimal/crypto_scalarmult.h` (C) | Magnitude: 30.24 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 14, pointers: 8, immutability_locks: 8, safety: 2
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_scalarmult/curve25519/sandy2x/ladder_namespace.h` (C) | Magnitude: 12.6 | Delta: **0.117 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: macros: 5, dead_code: 1
- `pynacl-1.6.2/src/bindings/utils.h` (C) | Magnitude: 25.2 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 25, safety: 13, immutability_locks: 13, api: 10
- `pynacl-1.6.2/src/bindings/minimal/crypto_shorthash.h` (C) | Magnitude: 24.68 | Delta: **0.198 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 9, pointers: 5, immutability_locks: 4, safety: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pynacl-1.6.2/src/nacl/public.py` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 91.6065%)
- `pynacl-1.6.2/src/nacl/signing.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 27.9556%)
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/ref/blake2b-compress-avx2.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/ref/blake2b-compress-sse41.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_generichash/blake2b/ref/blake2b-compress-ssse3.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pynacl-1.6.2/src/nacl/exceptions.py` -> **Severity: 5.385** (Embedded: 0.0673 * Error Risk: 80.0%)
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-core.h` -> **Severity: 0.62** (Embedded: 0.0223 * Error Risk: 27.7614%)
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_shorthash/siphash24/ref/shorthash_siphash_ref.h` -> **Severity: 0.45** (Embedded: 0.005 * Error Risk: 90.6217%)
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aegis128l/aegis128l_common.h` -> **Severity: 0.394** (Embedded: 0.0074 * Error Risk: 52.8692%)
- `pynacl-1.6.2/src/libsodium/src/libsodium/crypto_aead/aegis256/aegis256_common.h` -> **Severity: 0.392** (Embedded: 0.0074 * Error Risk: 52.6004%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/export.h` -> **Severity: 14004.524** (Blast Radius: 182.226 * Doc Risk: 76.8525%)
- `pynacl-1.6.2/src/nacl/exceptions.py` -> **Severity: 2865.811** (Blast Radius: 28.661 * Doc Risk: 99.9899%)
- `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/core.h` -> **Severity: 1439.914** (Blast Radius: 14.401 * Doc Risk: 99.9871%)
- `pynacl-1.6.2/src/nacl/encoding.py` -> **Severity: 1237.795** (Blast Radius: 12.378 * Doc Risk: 99.9996%)
- `pynacl-1.6.2/src/libsodium/src/libsodium/include/sodium/crypto_stream_salsa20.h` -> **Severity: 1156.892** (Blast Radius: 11.569 * Doc Risk: 99.9993%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
