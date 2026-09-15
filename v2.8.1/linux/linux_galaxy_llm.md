# ARCHITECTURAL_BRIEF: linux
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/torvalds/linux.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 93011 |
| Analyzed Artifacts (Scanned) | 81609 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 11402 |
| Total LOC | 24775448 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 87.7% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7466 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.063 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.6846 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5655 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 67718 | 23423179 | 83.0% |
| YAML | 4708 | 406180 | 5.8% |
| MAKEFILE | 3348 | 62460 | 4.1% |
| ASSEMBLY | 1339 | 244575 | 1.6% |
| SHELL | 1324 | 154153 | 1.6% |
| PLAINTEXT | 1136 | 3 | 1.4% |
| JSON | 963 | 298036 | 1.2% |
| PYTHON | 357 | 74823 | 0.4% |
| RUST | 335 | 68076 | 0.4% |
| XML | 198 | 6 | 0.2% |
| MARKDOWN | 68 | 0 | 0.1% |
| PERL | 64 | 33900 | 0.1% |
| YACC | 20 | 7106 | 0.0% |
| CSV | 10 | 286 | 0.0% |
| CPP | 9 | 2148 | 0.0% |
| CSS | 3 | 193 | 0.0% |
| M4 | 3 | 103 | 0.0% |
| HTML | 2 | 30 | 0.0% |
| PHP | 2 | 131 | 0.0% |
| RUBY | 1 | 25 | 0.0% |
| MATLAB | 1 | 35 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +3.08; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 29%, C Struct Operations Files 29%, Data / Markup / Trivial 16%, Interface Declarations Files 9%, Large Core Modules 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 80402 | 98.5% |
| Unknown | 3 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1201 | 1.5% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 11402*

**Composition by Extension & Reason:**
- `.rst`: 3864x Excluded (Unsupported Extension: '.rst'), 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 3001x Unsupported Format (.undeterminable), 567x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 207x Unresolved Ambiguity (No Retainable Structure)
- `.h`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 32x Excluded (Machine-Generated Source Code Signature: 62 LOC), 28x Excluded (Machine-Generated Source Code Signature: 835 LOC)
- `.yaml`: 39x Zero-Density Threshold (LOC: 51, Signals: 0), 34x Zero-Density Threshold (LOC: 52, Signals: 0), 32x Zero-Density Threshold (LOC: 56, Signals: 0)
- `.c`: 157x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Embedded Hex Payload: 3795 hex tokens in 603 LOC), 2x Excluded (Machine-Generated Source Code Signature: 328 LOC)
- `.dtso`: 268x Excluded (Unsupported Extension: '.dtso')
- `.pkt`: 158x Unsupported Format (.pkt)
- `.j2`: 149x Unsupported Format (.j2)
- `.cocci`: 76x Unsupported Format (.cocci)
- `.bconf`: 44x Unsupported Format (.bconf), 5x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.json`: 2x Excluded (Massive Static Asset Blob: 3447 LOC), 2x Excluded (Massive Static Asset Blob: 4954 LOC), 2x Excluded (Massive Static Asset Blob: 7627 LOC)
- `.litmus`: 35x Unsupported Format (.litmus), 12x Excluded (Unsupported Extension: '.litmus')
- `.s`: 29x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 639 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1130 LOC)
- `.boot`: 34x Unsupported Format (.boot)
- `.dot`: 23x Excluded (Unsupported Extension: '.dot'), 10x Unsupported Format (.dot)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 28.3 | 9.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 49.5 | 65.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 23.1 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 14.2 | 0.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 47.2 | 19.3 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 68.9 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 16.8 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 51.5 | 74.2 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 8058947 | 56803 | 265 | `drivers/gpu/drm/amd/display/dc/dml2_0/dml21/src/dml2_core/dml2_core_dcn4_calcs.c` |
| cleanup | 12402 | 2643 | 0 | `tools/testing/selftests/namespaces/ns_active_ref_test.c` |
| guards | 1337135 | 47829 | 43 | `lib/zstd/compress/zstd_compress.c` |
| danger | 137278 | 15506 | 2 | `tools/perf/arch/x86/tests/insn-x86-dat-src.c` |
| concurrency | 9353 | 2178 | 0 | `tools/testing/selftests/net/fcnal-test.sh` |
| connectivity | 518518 | 51278 | 15 | `drivers/gpu/drm/amd/include/vega10_enum.h` |
| io | 35687 | 3455 | 0 | `tools/testing/selftests/cgroup/test_cpuset_prs.sh` |
| crypto | 8 | 6 | 0 | `scripts/crypto/gen-fips-testvecs.py` |
| ipc | 33425 | 3990 | 0 | `drivers/staging/media/atomisp/pci/sh_css.c` |
| time | 1810 | 574 | 0 | `tools/testing/selftests/net/fcnal-test.sh` |
| serialization | 438 | 106 | 0 | `tools/testing/selftests/net/forwarding/devlink_lib.sh` |
| regex | 7754 | 982 | 0 | `scripts/checkpatch.pl` |
| events | 20071 | 4960 | 0 | `tools/testing/selftests/filesystems/epoll/epoll_wakeup_test.c` |
| tests | 26333 | 1266 | 0 | `tools/testing/selftests/landlock/fs_test.c` |
| docs | 152650 | 16378 | 3 | `drivers/gpu/drm/amd/display/dmub/inc/dmub_cmd.h` |
| debt | 55164 | 12163 | 1 | `arch/powerpc/xmon/xmon.c` |
| mutation | 5648760 | 56697 | 182 | `drivers/gpu/drm/amd/include/navi10_enum.h` |
| dead_code | 120413 | 22768 | 4 | `drivers/net/ethernet/sfc/mcdi_pcol.h` |
| credential | 157 | 52 | 0 | `Documentation/RCU/Design/Data-Structures/BigTreePreemptRCUBHdyntickCB.svg` |
| threat | 335366 | 30612 | 11 | `drivers/media/dvb-frontends/drxk_hard.c` |
| ml_ai | 20818 | 2850 | 0 | `drivers/comedi/drivers/ni_routing/ni_route_values/ni_mseries.c` |
| ui | 302 | 44 | 0 | `tools/net/sunrpc/xdrgen/generators/union.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.9583**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tools/testing/selftests/cgroup/test_cpuset_prs.sh` (Hits: 479)
- `tools/testing/selftests/net/openvswitch/openvswitch.sh` (Hits: 369)
- `tools/testing/selftests/net/fib_tests.sh` (Hits: 347)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **platform_device.h** (`include/linux/platform_device.h`) — 6402 inbound connections
2. **of.h** (`include/linux/of.h`) — 4628 inbound connections
3. **regmap.h** (`include/linux/regmap.h`) — 2759 inbound connections
4. **clk.h** (`include/linux/clk.h`) — 2630 inbound connections
5. **pm_runtime.h** (`include/linux/pm_runtime.h`) — 1623 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`rust/syn/lib.rs`) — 221 outbound dependencies
2. **gaudi2_regs.h** (`drivers/accel/habanalabs/include/gaudi2/asic_reg/gaudi2_regs.h`) — 158 outbound dependencies
3. **verifier.c** (`tools/testing/selftests/bpf/prog_tests/verifier.c`) — 113 outbound dependencies
4. **intel_display.c** (`drivers/gpu/drm/i915/display/intel_display.c`) — 108 outbound dependencies
5. **expr.rs** (`rust/syn/expr.rs`) — 107 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ctx_statement_block` **(Many-Argument Workhorses)** (@ `scripts/checkpatch.pl`) -> Impact: **8495.0** | LOC: 2091
- `CalculatePrefetchSchedule` **(Many-Argument Workhorses)** (@ `drivers/gpu/drm/amd/display/dc/dml/dcn314/display_mode_vba_314.c`) -> Impact: **2554.9** | LOC: 1335
- `CalculatePrefetchSchedule` **(Many-Argument Workhorses)** (@ `drivers/gpu/drm/amd/display/dc/dml/dcn31/display_mode_vba_31.c`) -> Impact: **2554.8** | LOC: 1332
- `wm5110_readable_register` **(Compute Cores)** (@ `drivers/mfd/wm5110-tables.c`) -> Impact: **2026.4** | LOC: 1142
- `wm5102_readable_register` **(Compute Cores)** (@ `drivers/mfd/wm5102-tables.c`) -> Impact: **1479.2** | LOC: 832
- `wm5100_readable_register` **(Compute Cores)** (@ `sound/soc/codecs/wm5100-tables.c`) -> Impact: **1372.0** | LOC: 767
- `cs47l24_readable_register` **(Compute Cores)** (@ `drivers/mfd/cs47l24-tables.c`) -> Impact: **1240.6** | LOC: 701
- `bpf_jit_build_body` **(Many-Argument Workhorses)** (@ `arch/powerpc/net/bpf_jit_comp64.c`) -> Impact: **1211.3** | LOC: 1033
  * *Intent:* /* Assemble the body code between the prologue & epilogue */
- `wm8998_readable_register` **(Compute Cores)** (@ `drivers/mfd/wm8998-tables.c`) -> Impact: **1208.5** | LOC: 683
- `bpf_jit_build_body` **(Many-Argument Workhorses)** (@ `arch/powerpc/net/bpf_jit_comp32.c`) -> Impact: **1200.6** | LOC: 1102
  * *Intent:* /* Assemble the body code between the prologue & epilogue */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `drivers/gpu/drm/amd/amdgpu` | 616 | 202977.36 | 30.25% | 13.44% |
| `sound/soc/codecs` | 683 | 198525.48 | 22.75% | 0.97% |
| `drivers/scsi` | 171 | 143597.06 | 47.31% | 11.17% |
| `mm` | 147 | 113245.96 | 54.14% | 27.5% |
| `fs/btrfs` | 128 | 108598.82 | 38.59% | 17.94% |
| `drivers/hwmon` | 240 | 105500.72 | 57.97% | 16.35% |
| `drivers/gpu/drm/radeon` | 190 | 103924.8 | 31.92% | 26.77% |
| `drivers/media/dvb-frontends` | 286 | 101339.26 | 34.0% | 4.93% |
| `drivers/gpu/drm/i915/display` | 336 | 100397.28 | 26.17% | 22.71% |
| `include/linux` | 1505 | 93032.48 | 10.79% | 4.77% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `scripts/gdb/linux/mm.py` -> **100.0%** Exposure
- `tools/perf/scripts/python/stat-cpi.py` -> **100.0%** Exposure
- `tools/verification/rvgen/rvgen/ltl2ba.py` -> **100.0%** Exposure
- `arch/arm/kernel/reboot.c` -> **100.0%** Exposure
- `arch/arm/mach-omap2/prm2xxx_3xxx.c` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `arch/arc/Makefile` -> **100.0%** Exposure
- `arch/arm/boot/compressed/Makefile` -> **100.0%** Exposure
- `arch/arm/boot/dts/Makefile` -> **100.0%** Exposure
- `arch/arm64/Makefile` -> **100.0%** Exposure
- `arch/arm64/boot/dts/Makefile` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `arch/m68k/ifpsp060/src/fpsp.S` -> **228** Orphaned Functions | **0** Duplicates
- `arch/m68k/ifpsp060/src/itest.S` -> **227** Orphaned Functions | **0** Duplicates
- `arch/sparc/kernel/ttable_64.S` -> **218** Orphaned Functions | **2** Duplicates
- `drivers/net/ethernet/aquantia/atlantic/hw_atl/hw_atl_llh.c` -> **219** Orphaned Functions | **0** Duplicates
- `sound/pci/asihpi/hpifunc.c` -> **194** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `181` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `417666` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `arch/powerpc/net/bpf_jit_comp.c` (C) -> Cumulative Risk: **709.87**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.11)
- **Magnitude:** 1040.52 | **LOC:** 1289 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.1971%)
- **Heaviest Functions:** `__arch_prepare_bpf_trampoline` (Many-Argument Workhorses, Impact: 187.8), `bpf_arch_text_poke` (Many-Argument Workhorses, Impact: 84.5), `bpf_int_jit_compile` (Compute Cores, Impact: 43.7)

### 2. `kernel/bpf/tnum.c` (C) -> Cumulative Risk: **699.71**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `C Struct Operations Files` (z -0.41)
- **Magnitude:** 239.0 | **LOC:** 328 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.5308%)
- **Heaviest Functions:** `tnum_sbin` (Defensive Guards, Impact: 14.9), `tnum_mul` (C Struct Operations, Impact: 11.6), `tnum_step` (Compute Cores, Impact: 10.7)

### 3. `drivers/gpu/drm/radeon/r600_dpm.c` (C) -> Cumulative Risk: **696.36**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.23)
- **Magnitude:** 1048.16 | **LOC:** 1369 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9995%), Tech Debt (94.8169%)
- **Heaviest Functions:** `r600_parse_extended_power_table` (Compute Cores, Impact: 100.3), `r600_dpm_print_class_info` (Compute Cores, Impact: 48.1), `r600_get_pcie_gen_support` (C Struct Operations, Impact: 27.9)

### 4. `drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd.c` (C) -> Cumulative Risk: **693.05**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.24)
- **Magnitude:** 750.2 | **LOC:** 917 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8996%), Documentation (98.9796%)
- **Heaviest Functions:** `amdgpu_amdkfd_get_dmabuf_info` (Many-Argument Workhorses, Impact: 40.7), `amdgpu_amdkfd_alloc_kernel_mem` (Many-Argument Workhorses, Impact: 34.7), `amdgpu_amdkfd_get_pcie_bandwidth_mbytes` (Compute Cores, Impact: 32.2)

### 5. `drivers/gpu/drm/amd/amdkfd/kfd_mqd_manager.c` (C) -> Cumulative Risk: **690.74**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `C Struct Operations Files` (z -1.07)
- **Magnitude:** 223.44 | **LOC:** 318 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.079%)
- **Heaviest Functions:** `mqd_symmetrically_map_cu_mask` (Many-Argument Workhorses, Impact: 47.1), `kfd_check_hiq_mqd_doorbell_id` (C Struct Operations, Impact: 14.8), `kfd_free_mqd_cp` (C Struct Operations, Impact: 6.5)

### 6. `drivers/gpu/drm/nouveau/nvif/outp.c` (C) -> Cumulative Risk: **689.86**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `C Struct Operations Files` (z -0.41)
- **Magnitude:** 421.46 | **LOC:** 557 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9166%)
- **Heaviest Functions:** `nvif_outp_ctor` (Many-Argument Workhorses, Impact: 34.4), `nvif_outp_detect` (C Struct Operations, Impact: 11.1), `nvif_outp_edid_get` (C Struct Operations, Impact: 8.3)

### 7. `drivers/gpu/drm/bridge/analogix/analogix_dp_reg.c` (C) -> Cumulative Risk: **689.39**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.47)
- **Magnitude:** 916.14 | **LOC:** 1108 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.6745%)
- **Heaviest Functions:** `analogix_dp_set_analog_power_down` (Many-Argument Workhorses, Impact: 73.2), `analogix_dp_transfer` (Many-Argument Workhorses, Impact: 55.1), `analogix_dp_send_psr_spd` (Many-Argument Workhorses, Impact: 19.6)

### 8. `arch/um/os-Linux/helper.c` (C) -> Cumulative Risk: **688.43**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `C Struct Operations Files` (z +1.27)
- **Magnitude:** 196.62 | **LOC:** 237 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.6873%)
- **Heaviest Functions:** `run_helper` (Many-Argument Workhorses, Impact: 25.7), `run_helper_thread` (Many-Argument Workhorses, Impact: 22.0), `os_run_helper_thread` (C Struct Operations, Impact: 15.6)

### 9. `drivers/gpu/drm/nouveau/nvif/vmm.c` (C) -> Cumulative Risk: **688.38**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `C Struct Operations Files` (z +0.96)
- **Magnitude:** 232.14 | **LOC:** 264 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (98.8362%)
- **Heaviest Functions:** `nvif_vmm_ctor` (Many-Argument Workhorses, Impact: 44.4), `nvif_vmm_get` (Many-Argument Workhorses, Impact: 21.3), `nvif_vmm_map` (Many-Argument Workhorses, Impact: 15.5)

### 10. `drivers/crypto/allwinner/sun4i-ss/sun4i-ss-hash.c` (C) -> Cumulative Risk: **685.65**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `C Struct Operations Files` (z +0.38)
- **Magnitude:** 4.91 | **LOC:** 546 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.9846%)
- **Heaviest Functions:** `sun4i_hash` (Compute Cores, Impact: 105.6), `sun4i_hash_export_sha1` (C Struct Operations, Impact: 8.1), `sun4i_hash_export_md5` (C Struct Operations, Impact: 8.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `kernel/bpf/verifier.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 23984.26 | **LOC:** 26244 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 18.2%
- **Risk Profile:** Cognitive Load (95.2875%), Tech Debt (8.8512%)
**Top Internal Functions/Classes:**
  * `check_kfunc_args` **(Many-Argument Workhorses)** (Impact: 395.3)
  * `check_mem_access` **(Many-Argument Workhorses)** (Impact: 392.8)
    * *Intent:* /* check whether memory at (regno + off) is accessible for t = (read | write) * if t==write, value_r...
  * `do_misc_fixups` **(Compute Cores)** (Impact: 339.3)
    * *Intent:* /* Do various post-verification rewrites in a single program pass. * These rewrites simplify JIT and...
  * `check_map_func_compatibility` **(Many-Argument Workhorses)** (Impact: 316.6)
  * `check_helper_call` **(Many-Argument Workhorses)** (Impact: 298.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3285 instances
* *State Mutation (weighted view):* 10285
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5419`, `structural_boundaries: 5594`, `args: 938`, `func_start: 670`, `class_start: 927`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 3715`, `dead_code: 36`, `planned_debt: 12`, `fragile_debt: 7`, `unreferenced_by_name: 4`
* *Architecture:* `api: 35`, `import: 29`
* *Defense:* `safety: 25`, `immutability_locks: 375`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` disasm.h, bpf-cgroup.h, bpf.h, bpf_lsm.h, bpf_mem_alloc.h, bpf_types.h, bpf_verifier.h, bsearch.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `net/wireless/nl80211.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 18542.5 | **LOC:** 22051 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (85.6968%), Tech Debt (9.6703%)
**Top Internal Functions/Classes:**
  * `nl80211_send_wiphy` **(Many-Argument Workhorses)** (Impact: 646.9)
  * `nl80211_send_station` **(Many-Argument Workhorses)** (Impact: 248.9)
  * `nl80211_parse_sched_scan` **(Many-Argument Workhorses)** (Impact: 184.7)
  * `nl80211_set_wiphy` **(Many-Argument Workhorses)** (Impact: 165.2)
  * `nl80211_msg_put_channel` **(Many-Argument Workhorses)** (Impact: 163.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2327 instances
* *State Mutation (weighted view):* 7139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4575`, `structural_boundaries: 4175`, `args: 907`, `func_start: 363`, `class_start: 1091`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 2485`, `dead_code: 9`, `planned_debt: 1`, `fragile_debt: 5`, `unreferenced_by_name: 23`
* *Architecture:* `api: 85`, `import: 22`
* *Defense:* `safety: 18`, `doc: 1`, `test: 2`, `immutability_locks: 202`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` core.h, err.h, etherdevice.h, ieee80211.h, if.h, if_ether.h, if_vlan.h, list.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/net/ethernet/broadcom/bnxt/bnxt.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 17221.86 | **LOC:** 17386 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (82.4809%), Tech Debt (9.1921%)
**Top Internal Functions/Classes:**
  * `bnxt_rx_pkt` **(Many-Argument Workhorses)** (Impact: 145.7)
    * *Intent:* /* returns the following: * 1 - 1 packet successfully received * 0 - successful TPA_START, packet no...
  * `bnxt_start_xmit` **(Many-Argument Workhorses)** (Impact: 115.6)
  * `bnxt_async_event_process` **(Many-Argument Workhorses)** (Impact: 101.3)
    * *Intent:* #define BNXT_PHC_BITS 48
  * `bnxt_init_one` **(Many-Argument Workhorses)** (Impact: 100.4)
  * `bnxt_tpa_end` **(Many-Argument Workhorses)** (Impact: 76.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3191 instances
* *State Mutation (weighted view):* 10150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2898`, `structural_boundaries: 3393`, `args: 918`, `func_start: 540`, `class_start: 811`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 3768`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 1`, `unreferenced_by_name: 16`
* *Architecture:* `api: 76`, `import: 64`
* *Defense:* `safety: 28`, `doc: 4`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 38):` byteorder.h, page.h, bnxt.h, bnxt_coredump.h, bnxt_dcb.h, bnxt_debugfs.h, bnxt_devlink.h, bnxt_ethtool.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/net/ethernet/broadcom/tg3.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 15834.26 | **LOC:** 18437 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (78.4062%), Tech Debt (9.1179%)
**Top Internal Functions/Classes:**
  * `tg3_get_invariants` **(Many-Argument Workhorses)** (Impact: 425.2)
  * `tg3_reset_hw` **(Many-Argument Workhorses)** (Impact: 400.7)
    * *Intent:* /* tp->lock is held. */
  * `tg3_setup_copper_phy` **(Many-Argument Workhorses)** (Impact: 190.5)
  * `tg3_init_one` **(Many-Argument Workhorses)** (Impact: 172.0)
  * `__tg3_start_xmit` **(Many-Argument Workhorses)** (Impact: 122.1)
    * *Intent:* /* hard_start_xmit for all devices */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2575 instances
* *State Mutation (weighted view):* 7966
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3688`, `structural_boundaries: 2054`, `args: 1162`, `func_start: 387`, `class_start: 249`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 2816`, `planned_debt: 1`, `fragile_debt: 18`
* *Architecture:* `api: 2`, `import: 43`
* *Defense:* `safety: 13`, `doc: 3`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` byteorder.h, brcmphy.h, compiler.h, crc32.h, delay.h, dma-mapping.h, dmi.h, etherdevice.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/gpu/drm/amd/display/dc/dml2_0/dml21/src/dml2_core/dml2_core_dcn4_calcs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 15546.94 | **LOC:** 13360 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.9847%), Tech Debt (9.1455%)
**Top Internal Functions/Classes:**
  * `CalculateOutputLink` **(Many-Argument Workhorses)** (Impact: 464.1)
  * `CalculateDCCConfiguration` **(Many-Argument Workhorses)** (Impact: 428.6)
  * `dml_core_mode_support` **(Compute Cores)** (Impact: 331.7)
  * `CalculateBytePerPixelAndBlockSizes` **(Many-Argument Workhorses)** (Impact: 292.8)
  * `CalculatePrefetchSchedule` **(Many-Argument Workhorses)** (Impact: 282.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2225 instances
* *State Mutation (weighted view):* 9012
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2270`, `structural_boundaries: 926`, `args: 237`, `func_start: 117`, `class_start: 137`
* *Risk/State:* `state_mutation: 4562`, `dead_code: 23`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 19`, `import: 5`
* *Defense:* `immutability_locks: 86`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` dml2_core_dcn4_calcs.h, dml2_debug.h, dml2_internal_shared_types.h, dml_top_types.h, lib_float_math.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/video/fbdev/sis/init301.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 15382.2 | **LOC:** 11380 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.9297%), Tech Debt (10.2618%)
**Top Internal Functions/Classes:**
  * `SiS_GetLCDResInfo` **(Many-Argument Workhorses)** (Impact: 485.9)
  * `SiS_SetGroup1_LVDS` **(Many-Argument Workhorses)** (Impact: 452.6)
    * *Intent:* /* Setup panel link * This is used for LVDS, LCDA and Chrontel TV output * 300/LVDS+TV, 300/301B-DH,...
  * `SiS_SetGroup2` **(Many-Argument Workhorses)** (Impact: 452.5)
  * `SiS_GetCRT2Data301` **(Many-Argument Workhorses)** (Impact: 329.1)
  * `SiS_SetGroup1` **(Many-Argument Workhorses)** (Impact: 275.8)
    * *Intent:* /* Set Part 1 */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2488 instances
* *State Mutation (weighted view):* 7609
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3393`, `structural_boundaries: 932`, `args: 1701`, `func_start: 163`
* *Risk/State:* `state_mutation: 2633`, `dead_code: 11`, `planned_debt: 1`, `fragile_debt: 7`, `unreferenced_by_name: 9`
* *Architecture:* `api: 33`, `import: 3`
* *Defense:* `doc: 64`, `immutability_locks: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` init301.h, oem300.h, oem310.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/scsi/lpfc/lpfc_sli.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 14851.14 | **LOC:** 22850 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (58.6951%), Tech Debt (14.182%)
**Top Internal Functions/Classes:**
  * `lpfc_sli4_hba_setup` **(Compute Cores)** (Impact: 168.6)
    * *Intent:* /** * lpfc_sli4_hba_setup - SLI4 device initialization PCI function * @phba: Pointer to HBA context ...
  * `lpfc_sli_issue_mbox_s3` **(Many-Argument Workhorses)** (Impact: 167.5)
    * *Intent:* * If the mailbox is submitted in no_wait mode (not polling) the * function will submit the command a...
  * `lpfc_rq_create` **(Many-Argument Workhorses)** (Impact: 125.9)
    * *Intent:* * to the HBA. * * The @phba struct is used to send mailbox command to HBA. The @drq and @hrq * struc...
  * `lpfc_sli_iocb_cmd_type` **(Compute Cores)** (Impact: 115.3)
    * *Intent:* * lpfc_sli_iocb_cmd_type - Get the iocb type * @iocb_cmnd: iocb command code. * * This function is c...
  * `lpfc_cq_create_set` **(Many-Argument Workhorses)** (Impact: 114.3)
    * *Intent:* * described by @phba by sending a CREATE_CQ_SET mailbox command to the HBA. * * The @phba struct is ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2353 instances
* *State Mutation (weighted view):* 7712
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2752`, `structural_boundaries: 2602`, `args: 495`, `func_start: 351`, `class_start: 688`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 3006`, `dead_code: 8`, `unreferenced_by_name: 105`
* *Architecture:* `api: 181`, `import: 31`
* *Defense:* `safety: 3`, `doc: 303`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` set_memory.h, blkdev.h, crash_dump.h, delay.h, dmi.h, interrupt.h, lockdep.h, of.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/checkpatch.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 13819.56 | **LOC:** 7931 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.5915%), Tech Debt (11.3758%)
**Top Internal Functions/Classes:**
  * `ctx_statement_block` **(Many-Argument Workhorses)** (Impact: 8495.0)
  * `process` **(Compute Cores)** (Impact: 910.3)
  * `annotate_values` **(Compute Cores)** (Impact: 200.5)
  * `build_types` **(Compute Cores)** (Impact: 87.4)
  * `ctx_block_get` **(Many-Argument Workhorses)** (Impact: 71.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 1023 instances
* *Memory Alloc (weighted view):* 5
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 3079
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4138`, `structural_boundaries: 1310`, `args: 68`, `func_start: 73`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 28`, `state_mutation: 1033`, `dead_code: 64`, `fragile_debt: 9`, `unreferenced_by_name: 4`
* *Architecture:* `io: 38`, `api: 73`, `import: 49`
* *Defense:* `safety: 2`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` BUG, C99, Cwd, Encode, File::Basename, Getopt::Long, KERN_, Kconfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/net/wireless/ath/ath12k/mac.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 13190.3 | **LOC:** 15217 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (80.8793%), Tech Debt (13.0483%)
**Top Internal Functions/Classes:**
  * `ath12k_mac_bss_info_changed` **(Many-Argument Workhorses)** (Impact: 243.4)
  * `ath12k_mac_op_sta_state` **(Many-Argument Workhorses)** (Impact: 117.6)
  * `ath12k_mac_bitrate_mask_get_single_nss` **(Many-Argument Workhorses)** (Impact: 109.2)
  * `ath12k_peer_assoc_h_phymode` **(Many-Argument Workhorses)** (Impact: 107.9)
  * `ath12k_peer_assoc_h_he` **(Many-Argument Workhorses)** (Impact: 103.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2138 instances
* *State Mutation (weighted view):* 6789
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2411`, `structural_boundaries: 2871`, `args: 445`, `func_start: 328`, `class_start: 979`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 2513`, `dead_code: 5`, `planned_debt: 37`, `fragile_debt: 5`, `unreferenced_by_name: 21`
* *Architecture:* `api: 88`, `import: 18`
* *Defense:* `safety: 3`, `immutability_locks: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` core.h, debug.h, debugfs.h, debugfs_sta.h, dp.h, dp_cmn.h, dp_rx.h, dp_tx.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/net/wireless/realtek/rtw89/coex.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 12883.9 | **LOC:** 11907 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.629%), Tech Debt (9.9764%)
**Top Internal Functions/Classes:**
  * `_chk_btc_report` **(Many-Argument Workhorses)** (Impact: 526.4)
  * `rtw89_btc_set_policy_v1` **(Many-Argument Workhorses)** (Impact: 226.8)
  * `rtw89_btc_set_policy` **(Compute Cores)** (Impact: 147.1)
    * *Intent:* #define BTC_B1_MAX 250 /* unit ms */
  * `_chk_btc_err` **(Many-Argument Workhorses)** (Impact: 146.4)
    * *Intent:* #define BTC_RPT_HDR_SIZE 3 #define BTC_CHK_WLSLOT_DRIFT_MAX 15 #define BTC_CHK_BTSLOT_DRIFT_MAX 15 #...
  * `rtw89_btc_fw_rpt_ver` **(Compute Cores)** (Impact: 142.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2171 instances
* *State Mutation (weighted view):* 6959
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2696`, `structural_boundaries: 2101`, `args: 460`, `func_start: 178`, `class_start: 687`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 2617`, `dead_code: 20`, `planned_debt: 2`, `unreferenced_by_name: 19`
* *Architecture:* `api: 80`, `import: 8`
* *Defense:* `safety: 31`, `immutability_locks: 82`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` chan.h, coex.h, debug.h, fw.h, mac.h, phy.h, ps.h, reg.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/gpu/drm/amd/display/dc/dml/dcn314/display_mode_vba_314.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 11594.66 | **LOC:** 7344 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.6068%), Tech Debt (8.5879%)
**Top Internal Functions/Classes:**
  * `CalculatePrefetchSchedule` **(Many-Argument Workhorses)** (Impact: 2554.9)
  * `dml314_ModeSupportAndSystemConfigurationFull` **(Compute Cores)** (Impact: 568.2)
  * `CalculateDCCConfiguration` **(Many-Argument Workhorses)** (Impact: 545.4)
  * `CalculateStutterEfficiency` **(Many-Argument Workhorses)** (Impact: 381.4)
  * `CalculateSwathAndDETConfiguration` **(Many-Argument Workhorses)** (Impact: 308.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1518 instances
* *State Mutation (weighted view):* 4801
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1427`, `structural_boundaries: 622`, `args: 151`, `func_start: 37`, `class_start: 89`
* *Risk/State:* `state_mutation: 1765`, `planned_debt: 7`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` display_mode_lib.h, dml_inline_defs.h, dc.h, display_mode_vba_314.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/gpu/drm/amd/display/dc/dml/dcn31/display_mode_vba_31.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 11281.62 | **LOC:** 7229 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.6427%), Tech Debt (8.6043%)
**Top Internal Functions/Classes:**
  * `CalculatePrefetchSchedule` **(Many-Argument Workhorses)** (Impact: 2554.8)
  * `dml31_ModeSupportAndSystemConfigurationFull` **(Compute Cores)** (Impact: 583.2)
  * `CalculateDCCConfiguration` **(Many-Argument Workhorses)** (Impact: 545.4)
  * `CalculateStutterEfficiency` **(Many-Argument Workhorses)** (Impact: 381.4)
  * `CalculateSwathAndDETConfiguration` **(Many-Argument Workhorses)** (Impact: 325.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1449 instances
* *State Mutation (weighted view):* 4590
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1383`, `structural_boundaries: 637`, `args: 146`, `func_start: 36`, `class_start: 84`
* *Risk/State:* `state_mutation: 1692`, `planned_debt: 7`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` display_mode_vba_30.h, display_mode_lib.h, dml_inline_defs.h, dc.h, display_mode_vba_31.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/net/ethernet/intel/i40e/i40e_main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 11008.4 | **LOC:** 16679 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (56.724%), Tech Debt (9.834%)
**Top Internal Functions/Classes:**
  * `i40e_probe` **(Many-Argument Workhorses)** (Impact: 191.2)
    * *Intent:* /** * i40e_probe - Device initialization routine * @pdev: PCI device information struct * @ent: entr...
  * `i40e_rebuild` **(Many-Argument Workhorses)** (Impact: 118.1)
    * *Intent:* /** * i40e_rebuild - rebuild using a saved config * @pf: board private structure * @reinit: if the M...
  * `i40e_vsi_setup_queue_map` **(Many-Argument Workhorses)** (Impact: 99.1)
    * *Intent:* /** * i40e_vsi_setup_queue_map - Setup a VSI queue map based on enabled_tc * @vsi: the VSI being set...
  * `i40e_parse_cls_flower` **(Many-Argument Workhorses)** (Impact: 98.2)
    * *Intent:* /** * i40e_parse_cls_flower - Parse tc flower filters provided by kernel * @vsi: Pointer to VSI * @f...
  * `i40e_vsi_setup` **(Many-Argument Workhorses)** (Impact: 95.8)
    * *Intent:* /** * i40e_vsi_setup - Set up a VSI by a given type * @pf: board private structure * @type: VSI type...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1793 instances
* *State Mutation (weighted view):* 5687
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2202`, `structural_boundaries: 2139`, `args: 1005`, `func_start: 345`, `class_start: 556`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 2101`, `dead_code: 19`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 18`
* *Architecture:* `api: 78`, `import: 15`
* *Defense:* `safety: 11`, `doc: 336`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` utsrelease.h, i40e.h, i40e_devids.h, i40e_diag.h, i40e_lan_hmc.h, i40e_trace.h, i40e_virtchnl_pf.h, i40e_xsk.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/x86/kvm/x86.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 10777.16 | **LOC:** 14497 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (94.674%), Tech Debt (21.0437%)
**Top Internal Functions/Classes:**
  * `kvm_set_msr_common` **(Compute Cores)** (Impact: 272.8)
  * `kvm_arch_vcpu_ioctl` **(Many-Argument Workhorses)** (Impact: 243.9)
  * `kvm_get_msr_common` **(Compute Cores)** (Impact: 217.7)
  * `kvm_vm_ioctl_check_extension` **(Compute Cores)** (Impact: 209.8)
  * `kvm_arch_vm_ioctl` **(Many-Argument Workhorses)** (Impact: 188.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1434 instances
* *State Mutation (weighted view):* 4544
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2427`, `structural_boundaries: 2799`, `args: 845`, `func_start: 511`, `class_start: 302`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1676`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 11`, `unreferenced_by_name: 61`
* *Architecture:* `api: 191`, `import: 67`
* *Defense:* `safety: 3`, `doc: 3`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 32):` debugreg.h, desc.h, div64.h, emulate_prefix.h, api.h, xcr.h, xstate.h, hypervisor.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/gpu/drm/amd/display/amdgpu_dm/amdgpu_dm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 10534.38 | **LOC:** 13613 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (81.497%), Tech Debt (14.4877%)
**Top Internal Functions/Classes:**
  * `amdgpu_dm_commit_planes` **(Many-Argument Workhorses)** (Impact: 188.6)
  * `amdgpu_dm_initialize_drm_device` **(Compute Cores)** (Impact: 186.1)
    * *Intent:* /* * In this architecture, the association * connector -> encoder -> crtc * id not really requried. ...
  * `amdgpu_dm_atomic_check` **(Many-Argument Workhorses)** (Impact: 162.4)
    * *Intent:* * * When validating the DC state, it's important that the right locks are * acquired. For full updat...
  * `dm_update_crtc_state` **(Many-Argument Workhorses)** (Impact: 152.3)
  * `amdgpu_dm_init` **(Compute Cores)** (Impact: 137.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1547 instances
* *State Mutation (weighted view):* 4946
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2389`, `structural_boundaries: 2636`, `args: 331`, `func_start: 250`, `class_start: 803`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1852`, `dead_code: 7`, `planned_debt: 46`, `fragile_debt: 9`, `unreferenced_by_name: 10`
* *Architecture:* `api: 29`, `import: 66`
* *Defense:* `safety: 10`, `doc: 39`, `immutability_locks: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 58):` video.h, amd_shared.h, amdgpu.h, amdgpu_atombios.h, amdgpu_display.h, amdgpu_dm.h, amdgpu_dm_crtc.h, amdgpu_dm_debugfs.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/net/ethernet/broadcom/bnx2x/bnx2x_main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 10127.14 | **LOC:** 15477 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (76.4727%), Tech Debt (15.5501%)
**Top Internal Functions/Classes:**
  * `bnx2x_get_hwinfo` **(Compute Cores)** (Impact: 103.1)
  * `bnx2x_check_blocks_with_parity1` **(Many-Argument Workhorses)** (Impact: 100.2)
  * `bnx2x_init_hw_common` **(Compute Cores)** (Impact: 92.7)
    * *Intent:* /** * bnx2x_init_hw_common - initialize the HW at the COMMON phase. * * @bp: driver handle */
  * `bnx2x_init_hw_port` **(Compute Cores)** (Impact: 84.9)
  * `bnx2x_panic_dump` **(Many-Argument Workhorses)** (Impact: 83.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1556 instances
* *State Mutation (weighted view):* 5060
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2091`, `structural_boundaries: 1779`, `args: 853`, `func_start: 365`, `class_start: 258`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 1948`, `dead_code: 20`, `planned_debt: 2`, `fragile_debt: 12`, `unreferenced_by_name: 40`
* *Architecture:* `io: 3`, `api: 92`, `import: 48`
* *Defense:* `safety: 9`, `doc: 29`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` byteorder.h, bnx2x.h, bnx2x_cmn.h, bnx2x_dcb.h, bnx2x_fw_file_hdr.h, bnx2x_init.h, bnx2x_init_ops.h, bnx2x_sp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/scsi/lpfc/lpfc_init.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 9910.38 | **LOC:** 15836 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (58.0296%), Tech Debt (9.6449%)
**Top Internal Functions/Classes:**
  * `lpfc_get_hba_model_desc` **(Many-Argument Workhorses)** (Impact: 187.8)
    * *Intent:* /** * lpfc_get_hba_model_desc - Retrieve HBA device model name and description * @phba: pointer to l...
  * `lpfc_sli4_driver_resource_setup` **(Compute Cores)** (Impact: 112.5)
    * *Intent:* /** * lpfc_sli4_driver_resource_setup - Setup drvr internal resources for SLI4 dev * @phba: pointer ...
  * `lpfc_sli4_read_config` **(Compute Cores)** (Impact: 94.1)
    * *Intent:* /** * lpfc_sli4_read_config - Get the config parameters. * @phba: pointer to lpfc hba data structure...
  * `lpfc_sli4_async_sli_evt` **(Many-Argument Workhorses)** (Impact: 93.9)
    * *Intent:* /** * lpfc_sli4_async_sli_evt - Process the asynchronous SLI link event * @phba: pointer to lpfc hba...
  * `lpfc_sli4_queue_setup` **(Compute Cores)** (Impact: 85.1)
    * *Intent:* /** * lpfc_sli4_queue_setup - Set up all the SLI4 queues * @phba: pointer to lpfc hba data structure...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1738 instances
* *State Mutation (weighted view):* 5686
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1782`, `structural_boundaries: 1633`, `args: 446`, `func_start: 254`, `class_start: 309`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 2210`, `dead_code: 5`, `unreferenced_by_name: 27`
* *Architecture:* `api: 88`, `import: 40`
* *Defense:* `safety: 9`, `doc: 218`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` bitops.h, blkdev.h, cpu.h, cpuhotplug.h, crash_dump.h, ctype.h, delay.h, dma-mapping.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/scsi/mpt3sas/mpt3sas_scsih.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 9817.72 | **LOC:** 14171 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (58.8981%), Tech Debt (8.9025%)
**Top Internal Functions/Classes:**
  * `_scsih_io_done` **(Many-Argument Workhorses)** (Impact: 197.4)
    * *Intent:* /** * _scsih_io_done - scsi request callback * @ioc: per adapter object * @smid: system request mess...
  * `_scsih_probe` **(Many-Argument Workhorses)** (Impact: 157.9)
    * *Intent:* /** * _scsih_probe - attach and add scsi host * @pdev: PCI device struct * @id: pci device id * * Re...
  * `_scsih_scsi_ioc_info` **(Many-Argument Workhorses)** (Impact: 130.7)
    * *Intent:* /** * _scsih_scsi_ioc_info - translated non-successful SCSI_IO request * @ioc: per adapter object * ...
  * `mpt3sas_scsih_event_callback` **(Many-Argument Workhorses)** (Impact: 106.2)
    * *Intent:* /** * mpt3sas_scsih_event_callback - firmware event handler (called at ISR time) * @ioc: per adapter...
  * `_scsih_determine_disposition` **(Compute Cores)** (Impact: 106.0)
    * *Intent:* /** * _scsih_determine_disposition - * @ioc: per adapter object * @transfer_packet: packet describin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1485 instances
* *State Mutation (weighted view):* 4670
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2155`, `structural_boundaries: 1782`, `args: 351`, `func_start: 239`, `class_start: 415`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 1700`, `dead_code: 6`, `planned_debt: 8`, `fragile_debt: 1`, `unreferenced_by_name: 6`
* *Architecture:* `api: 31`, `import: 13`
* *Defense:* `safety: 2`, `doc: 222`, `immutability_locks: 8`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` blkdev.h, delay.h, errno.h, init.h, interrupt.h, kernel.h, module.h, pci.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/net/wireless/ath/ath12k/wmi.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 9758.0 | **LOC:** 11251 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (72.8872%), Tech Debt (29.1126%)
**Top Internal Functions/Classes:**
  * `ath12k_wmi_op_rx` **(Compute Cores)** (Impact: 99.9)
  * `ath12k_pull_reg_chan_list_ext_update_ev` **(Many-Argument Workhorses)** (Impact: 93.3)
  * `ath12k_wmi_svc_rdy_ext_parse` **(Many-Argument Workhorses)** (Impact: 67.6)
  * `ath12k_wmi_svc_rdy_ext2_parse` **(Many-Argument Workhorses)** (Impact: 62.9)
  * `ath12k_wmi_copy_peer_flags` **(Many-Argument Workhorses)** (Impact: 58.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1681 instances
* *State Mutation (weighted view):* 5957
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1258`, `structural_boundaries: 2186`, `args: 590`, `func_start: 267`, `class_start: 648`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 2595`, `dead_code: 2`, `planned_debt: 9`, `unreferenced_by_name: 93`
* *Architecture:* `api: 110`, `import: 20`
* *Defense:* `safety: 21`, `doc: 1`, `immutability_locks: 200`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` core.h, debug.h, debugfs.h, hw.h, cleanup.h, completion.h, ctype.h, if_ether.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/net/ethernet/hisilicon/hns3/hns3pf/hclge_main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 9735.26 | **LOC:** 12944 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.6782%), Tech Debt (7.8301%)
**Top Internal Functions/Classes:**
  * `hclge_init_ae_dev` **(Compute Cores)** (Impact: 62.5)
  * `hclge_get_mac_vlan_cmd_status` **(Many-Argument Workhorses)** (Impact: 58.8)
  * `hclge_reset_ae_dev` **(Compute Cores)** (Impact: 39.6)
  * `hclge_fd_check_spec` **(Many-Argument Workhorses)** (Impact: 39.2)
  * `hclge_set_vlan_filter` **(Many-Argument Workhorses)** (Impact: 38.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1577 instances
* *State Mutation (weighted view):* 5054
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1721`, `structural_boundaries: 2893`, `args: 919`, `func_start: 466`, `class_start: 742`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 1900`, `dead_code: 22`, `unreferenced_by_name: 3`
* *Architecture:* `api: 37`, `import: 26`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` hclge_cmd.h, hclge_comm_cmd.h, hclge_dcb.h, hclge_devlink.h, hclge_err.h, hclge_main.h, hclge_mbx.h, hclge_mdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/net/wireless/ath/ath11k/mac.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 9410.34 | **LOC:** 10891 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.5314%), Tech Debt (14.8859%)
**Top Internal Functions/Classes:**
  * `ath11k_mac_op_bss_info_changed` **(Many-Argument Workhorses)** (Impact: 245.7)
  * `ath11k_mac_op_set_key` **(Many-Argument Workhorses)** (Impact: 135.9)
  * `ath11k_mac_op_sta_state` **(Many-Argument Workhorses)** (Impact: 122.0)
  * `ath11k_peer_assoc_h_he` **(Many-Argument Workhorses)** (Impact: 103.9)
  * `ath11k_peer_assoc_h_phymode` **(Many-Argument Workhorses)** (Impact: 86.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1557 instances
* *State Mutation (weighted view):* 4946
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1718`, `structural_boundaries: 1802`, `args: 375`, `func_start: 241`, `class_start: 566`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1832`, `dead_code: 3`, `planned_debt: 31`, `fragile_debt: 4`, `unreferenced_by_name: 21`
* *Architecture:* `api: 35`, `import: 19`
* *Defense:* `safety: 3`, `immutability_locks: 81`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` core.h, debug.h, debugfs_sta.h, dp_rx.h, dp_tx.h, hif.h, hw.h, bitfield.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/net/ethernet/sun/niu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 9395.04 | **LOC:** 10268 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.8211%), Tech Debt (10.4228%)
**Top Internal Functions/Classes:**
  * `mii_init_common` **(Compute Cores)** (Impact: 80.2)
  * `niu_add_ethtool_tcam_entry` **(Many-Argument Workhorses)** (Impact: 75.4)
  * `walk_phys` **(Compute Cores)** (Impact: 70.5)
  * `link_status_mii` **(Compute Cores)** (Impact: 69.7)
  * `niu_determine_phy_disposition` **(Compute Cores)** (Impact: 54.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1771 instances
* *State Mutation (weighted view):* 5595
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1543`, `structural_boundaries: 1572`, `args: 801`, `func_start: 343`, `class_start: 238`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 2053`, `dead_code: 2`, `fragile_debt: 19`
* *Architecture:* `io: 1`, `api: 2`, `import: 26`
* *Defense:* `safety: 13`, `immutability_locks: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` bitops.h, crc32.h, delay.h, dma-mapping.h, etherdevice.h, ethtool.h, if.h, if_ether.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `net/mac80211/mlme.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 9315.56 | **LOC:** 11229 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (77.0084%), Tech Debt (16.1823%)
**Top Internal Functions/Classes:**
  * `ieee80211_assoc_config_link` **(Many-Argument Workhorses)** (Impact: 310.4)
  * `ieee80211_determine_chan_mode` **(Many-Argument Workhorses)** (Impact: 159.8)
  * `ieee80211_mgd_assoc` **(Many-Argument Workhorses)** (Impact: 154.6)
  * `ieee80211_determine_ap_chan` **(Many-Argument Workhorses)** (Impact: 154.0)
  * `ieee80211_rx_mgmt_beacon` **(Many-Argument Workhorses)** (Impact: 148.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1405 instances
* *State Mutation (weighted view):* 4362
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1776`, `structural_boundaries: 2025`, `args: 330`, `func_start: 182`, `class_start: 541`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 1552`, `dead_code: 13`, `planned_debt: 9`, `fragile_debt: 10`, `unreferenced_by_name: 27`
* *Architecture:* `api: 57`, `import: 19`
* *Defense:* `safety: 54`, `immutability_locks: 156`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` driver-ops.h, fils_aead.h, ieee80211_i.h, static_stub.h, led.h, crc32.h, delay.h, etherdevice.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/gpu/drm/amd/display/dc/dml/dcn30/display_mode_vba_30.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 9302.16 | **LOC:** 6360 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.0728%), Tech Debt (8.3446%)
**Top Internal Functions/Classes:**
  * `CalculatePrefetchSchedule` **(Many-Argument Workhorses)** (Impact: 685.9)
  * `CalculateDCCConfiguration` **(Many-Argument Workhorses)** (Impact: 542.5)
  * `dml30_ModeSupportAndSystemConfigurationFull` **(Compute Cores)** (Impact: 533.5)
  * `CalculateSwathAndDETConfiguration` **(Many-Argument Workhorses)** (Impact: 309.3)
  * `CalculateVMAndRowBytes` **(Many-Argument Workhorses)** (Impact: 273.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1456 instances
* *State Mutation (weighted view):* 4580
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1295`, `structural_boundaries: 517`, `args: 126`, `func_start: 33`, `class_start: 77`
* *Risk/State:* `state_mutation: 1668`, `dead_code: 1`, `planned_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` display_mode_lib.h, dml_inline_defs.h, dc.h, display_mode_vba_30.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/gpu/drm/amd/display/dc/dml/dcn32/display_mode_vba_util_32.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 9252.74 | **LOC:** 6351 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.9901%), Tech Debt (16.0705%)
**Top Internal Functions/Classes:**
  * `dml32_CalculatePrefetchSchedule` **(Many-Argument Workhorses)** (Impact: 924.8)
  * `dml32_CalculateWatermarksMALLUseAndDRAMSpeedChangeSupport` **(Many-Argument Workhorses)** (Impact: 490.2)
  * `dml32_CalculateDCCConfiguration` **(Many-Argument Workhorses)** (Impact: 417.2)
  * `dml32_CalculateVMAndRowBytes` **(Many-Argument Workhorses)** (Impact: 376.5)
  * `dml32_CalculateOutputLink` **(Many-Argument Workhorses)** (Impact: 353.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1174 instances
* *State Mutation (weighted view):* 3737
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1139`, `structural_boundaries: 453`, `args: 269`, `func_start: 50`, `class_start: 71`
* *Risk/State:* `state_mutation: 1389`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 30`
* *Architecture:* `api: 50`, `import: 4`
* *Defense:* `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` display_mode_lib.h, dml_inline_defs.h, display_mode_vba_32.h, display_mode_vba_util_32.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `net/bluetooth/l2cap_core.c` -> Churn: **76.75%** | Cog Load: 76.772% | Debt: 11.1395%
- `kernel/bpf/verifier.c` -> Churn: **75.4%** | Cog Load: 95.2875% | Debt: 8.8512%
- `kernel/cgroup/cpuset.c` -> Churn: **75.4%** | Cog Load: 72.879% | Debt: 34.0307%
- `Makefile` -> Churn: **72.76%** | Cog Load: 56.5106% | Debt: 23.1715%
- `net/netfilter/nf_tables_api.c` -> Churn: **72.76%** | Cog Load: 73.4852% | Debt: 8.7213%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `drivers/scsi/lpfc/lpfc_sli.c` -> **Linus Torvalds** (100.0% isolated ownership) | Magnitude: 14851.14
- `drivers/net/ethernet/intel/i40e/i40e_main.c` -> **Larysa Zaremba** (100.0% isolated ownership) | Magnitude: 11008.4
- `drivers/net/ethernet/broadcom/bnx2x/bnx2x_main.c` -> **Linus Torvalds** (100.0% isolated ownership) | Magnitude: 10127.14
- `drivers/net/wireless/ath/ath12k/wmi.c` -> **Baochen Qiang** (100.0% isolated ownership) | Magnitude: 9758.0
- `net/mac80211/mlme.c` -> **Ariel Silver** (100.0% isolated ownership) | Magnitude: 9315.56

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `include/linux/memcontrol.h` -> **Severity: 0.003** (Bridge: 0.0001 * Flux: 58.8448%)
- `include/linux/rcuwait.h` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 96.4916%)
- `include/linux/sched/signal.h` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 80.8455%)
- `drivers/gpu/drm/nouveau/include/nvkm/core/os.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.9665%)
- `include/linux/alloc_tag.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 97.5236%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `include/linux/minmax.h` -> **Severity: 6.49** (Embedded: 0.0807 * Error Risk: 80.4327%)
- `include/linux/alloc_tag.h` -> **Severity: 5.592** (Embedded: 0.0867 * Error Risk: 64.5005%)
- `include/linux/util_macros.h` -> **Severity: 5.408** (Embedded: 0.0549 * Error Risk: 98.4863%)
- `include/linux/irqflags.h` -> **Severity: 5.392** (Embedded: 0.0718 * Error Risk: 75.074%)
- `include/linux/workqueue.h` -> **Severity: 5.17** (Embedded: 0.1028 * Error Risk: 50.274%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `include/linux/of.h` -> **Severity: 525.794** (Blast Radius: 6.699 * Doc Risk: 78.4884%)
- `include/linux/notifier.h` -> **Severity: 477.2** (Blast Radius: 4.772 * Doc Risk: 100.0%)
- `include/linux/platform_device.h` -> **Severity: 466.521** (Blast Radius: 7.257 * Doc Risk: 64.2857%)
- `include/linux/kobject.h` -> **Severity: 419.0** (Blast Radius: 4.19 * Doc Risk: 100.0%)
- `include/linux/ktime.h` -> **Severity: 372.641** (Blast Radius: 4.873 * Doc Risk: 76.4706%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
