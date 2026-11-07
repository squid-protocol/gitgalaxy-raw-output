# ARCHITECTURAL_BRIEF: linux
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/torvalds/linux.git` |
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
- **Scope:** 72674 analyzed artifact(s), 21417757 LOC.
- **Load-bearing artifact:** `tools/testing/selftests/bpf/progs/lru_bug.c` -- 12670 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `rust/syn/lib.rs` -- pulls in 255 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `kernel/bpf/verifier.c` at magnitude 23810.46 (structural weight, not risk).
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
| Total Artifacts | 93011 |
| Analyzed Artifacts (Scanned) | 72674 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 20337 |
| Total LOC | 21417757 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 78.1% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6162 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0851 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 15.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3428 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 58763 | 20012509 | 80.9% |
| YAML | 4726 | 407342 | 6.5% |
| MAKEFILE | 2965 | 58618 | 4.1% |
| ASSEMBLY | 1341 | 245577 | 1.8% |
| SHELL | 1322 | 154161 | 1.8% |
| PLAINTEXT | 1142 | 3 | 1.6% |
| JSON | 963 | 298036 | 1.3% |
| CPP | 373 | 33033 | 0.5% |
| PYTHON | 358 | 75100 | 0.5% |
| RUST | 342 | 90514 | 0.5% |
| XML | 203 | 6 | 0.3% |
| PERL | 66 | 34375 | 0.1% |
| MARKDOWN | 65 | 0 | 0.1% |
| YACC | 20 | 7106 | 0.0% |
| CSV | 10 | 286 | 0.0% |
| BMS | 4 | 657 | 0.0% |
| CSS | 3 | 193 | 0.0% |
| HTML | 2 | 30 | 0.0% |
| M4 | 2 | 20 | 0.0% |
| PHP | 2 | 131 | 0.0% |
| RUBY | 1 | 25 | 0.0% |
| MATLAB | 1 | 35 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 2 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 72669 |
| unknown | unknown | 3 |
| cp1252 | cp1252-fallback | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 30%, Large Core Modules (3) 26%, Data / Markup / Trivial 17%, Encapsulated Accessors Files 12%, Compute Cores Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 71464 | 98.3% |
| Unknown | 3 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1204 | 1.7% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 20337*

**Composition by Extension & Reason:**
- `.h`: 5486x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 32x Excluded (Machine-Generated Source Code Signature: 62 LOC), 28x Excluded (Machine-Generated Source Code Signature: 835 LOC)
- `no_extension`: 2749x Unsupported Format (.undeterminable), 1211x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 209x Unresolved Ambiguity (No Retainable Structure)
- `.rst`: 3674x Excluded (Unsupported Extension: '.rst'), 208x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 3787x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 781 LOC), 1x Excluded (Machine-Generated Source Code Signature: 441 LOC)
- `.yaml`: 39x Zero-Density Threshold (LOC: 51, Signals: 0), 35x Zero-Density Threshold (LOC: 52, Signals: 0), 32x Zero-Density Threshold (LOC: 56, Signals: 0)
- `.dtso`: 268x Excluded (Unsupported Extension: '.dtso')
- `.pkt`: 158x Unsupported Format (.pkt)
- `.j2`: 149x Unsupported Format (.j2)
- `.cocci`: 76x Unsupported Format (.cocci)
- `.bconf`: 44x Unsupported Format (.bconf), 5x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.json`: 2x Excluded (Massive Static Asset Blob: 3447 LOC), 2x Excluded (Massive Static Asset Blob: 4954 LOC), 2x Excluded (Massive Static Asset Blob: 7627 LOC)
- `.litmus`: 35x Unsupported Format (.litmus), 12x Excluded (Unsupported Extension: '.litmus')
- `.s`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2063 LOC), 1x Excluded (Embedded Array/Matrix Payload: 2224 commas in 634 LOC)
- `.boot`: 34x Unsupported Format (.boot)
- `.dot`: 22x Excluded (Unsupported Extension: '.dot'), 10x Unsupported Format (.dot), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 26.0 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 38.8 | 53.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 22.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.0 | 0.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 47.4 | 22.7 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 16.8 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 51.4 | 71.4 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 90.8 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 32035 | 7869 | 1 | `drivers/gpu/drm/amd/display/dc/dml2_0/dml21/src/dml2_core/dml2_core_dcn4_calcs.c` |
| cleanup | 12314 | 2592 | 0 | `tools/testing/selftests/namespaces/ns_active_ref_test.c` |
| guards | 1171279 | 41604 | 42 | `drivers/pinctrl/pinctrl-ingenic.c` |
| danger | 130392 | 14132 | 3 | `tools/perf/arch/x86/tests/insn-x86-dat-src.c` |
| concurrency | 9077 | 2105 | 0 | `tools/testing/selftests/net/fcnal-test.sh` |
| connectivity | 394011 | 43427 | 13 | `drivers/gpu/drm/amd/include/vega10_enum.h` |
| io | 35086 | 3288 | 0 | `tools/testing/selftests/cgroup/test_cpuset_prs.sh` |
| crypto | 8 | 6 | 0 | `scripts/crypto/gen-fips-testvecs.py` |
| ipc | 31919 | 3758 | 0 | `drivers/staging/media/atomisp/pci/sh_css.c` |
| time | 1803 | 568 | 0 | `tools/testing/selftests/net/fcnal-test.sh` |
| serialization | 438 | 106 | 0 | `tools/testing/selftests/net/forwarding/devlink_lib.sh` |
| regex | 7803 | 984 | 0 | `scripts/checkpatch.pl` |
| events | 18579 | 4473 | 0 | `tools/testing/selftests/filesystems/epoll/epoll_wakeup_test.c` |
| tests | 26167 | 1183 | 0 | `tools/testing/selftests/landlock/fs_test.c` |
| docs | 129142 | 13977 | 2 | `drivers/gpu/drm/amd/display/dmub/inc/dmub_cmd.h` |
| debt | 52347 | 11007 | 1 | `arch/powerpc/xmon/xmon.c` |
| mutation | 4822754 | 51172 | 174 | `drivers/gpu/drm/amd/include/navi10_enum.h` |
| dead_code | 88967 | 18077 | 3 | `arch/m68k/ifpsp060/src/fpsp.S` |
| credential | 154 | 51 | 0 | `Documentation/RCU/Design/Data-Structures/BigTreePreemptRCUBHdyntickCB.svg` |
| threat | 354 | 65 | 0 | `crypto/hkdf.c` |
| ml_ai | 19826 | 2602 | 0 | `drivers/comedi/drivers/ni_routing/ni_route_values/ni_mseries.c` |
| ui | 303 | 45 | 0 | `tools/net/sunrpc/xdrgen/generators/union.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tools/testing/selftests/cgroup/test_cpuset_prs.sh` (Hits: 479)
- `tools/testing/selftests/net/openvswitch/openvswitch.sh` (Hits: 369)
- `tools/testing/selftests/net/fib_tests.sh` (Hits: 347)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lru_bug.c** (`tools/testing/selftests/bpf/progs/lru_bug.c`) — 12670 inbound connections
2. **platform_device.h** (`include/kunit/platform_device.h`) — 6045 inbound connections
3. **init.h** (`tools/include/linux/init.h`) — 5970 inbound connections
4. **overflow.h** (`tools/include/linux/overflow.h`) — 5769 inbound connections
5. **delay.h** (`tools/include/linux/delay.h`) — 5019 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`rust/syn/lib.rs`) — 255 outbound dependencies
2. **gaudi2_regs.h** (`drivers/accel/habanalabs/include/gaudi2/asic_reg/gaudi2_regs.h`) — 158 outbound dependencies
3. **verifier.c** (`tools/testing/selftests/bpf/prog_tests/verifier.c`) — 113 outbound dependencies
4. **intel_display.c** (`drivers/gpu/drm/i915/display/intel_display.c`) — 108 outbound dependencies
5. **fork.c** (`kernel/fork.c`) — 105 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ctx_statement_block` **(Many-Argument Workhorses)** (@ `scripts/checkpatch.pl`) -> Impact: **8495.1** | LOC: 2093
- `CalculatePrefetchSchedule` **(Many-Argument Workhorses)** (@ `drivers/gpu/drm/amd/display/dc/dml/dcn314/display_mode_vba_314.c`) -> Impact: **2460.4** | LOC: 1335
- `CalculatePrefetchSchedule` **(Many-Argument Workhorses)** (@ `drivers/gpu/drm/amd/display/dc/dml/dcn31/display_mode_vba_31.c`) -> Impact: **2460.3** | LOC: 1332
- `wm5110_readable_register` **(Many-Argument Workhorses)** (@ `drivers/mfd/wm5110-tables.c`) -> Impact: **2026.4** | LOC: 1142
- `cs47l85_16bit_readable_register` **(Many-Argument Workhorses)** (@ `drivers/mfd/cs47l85-tables.c`) -> Impact: **1796.6** | LOC: 1014
- `cs47l90_16bit_readable_register` **(Many-Argument Workhorses)** (@ `drivers/mfd/cs47l90-tables.c`) -> Impact: **1787.7** | LOC: 1009
- `calculate_bandwidth` **(Many-Argument Workhorses)** (@ `drivers/gpu/drm/amd/display/dc/basics/dce_calcs.c`) -> Impact: **1580.2** | LOC: 1964
- `wm5102_readable_register` **(Many-Argument Workhorses)** (@ `drivers/mfd/wm5102-tables.c`) -> Impact: **1479.2** | LOC: 832
- `wm5100_readable_register` **(Many-Argument Workhorses)** (@ `sound/soc/codecs/wm5100-tables.c`) -> Impact: **1372.0** | LOC: 767
- `cs47l92_16bit_readable_register` **(Many-Argument Workhorses)** (@ `drivers/mfd/cs47l92-tables.c`) -> Impact: **1283.4** | LOC: 726

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `sound/soc/codecs` | 698 | 219750.04 | 22.82% | 0.87% |
| `drivers/gpu/drm/amd/amdgpu` | 617 | 205016.76 | 29.44% | 12.17% |
| `drivers/scsi` | 172 | 142413.26 | 44.04% | 9.86% |
| `drivers/gpu/drm/radeon` | 197 | 120304.38 | 32.44% | 25.22% |
| `mm` | 147 | 113172.76 | 53.78% | 25.97% |
| `fs/btrfs` | 129 | 108038.24 | 37.4% | 16.78% |
| `drivers/hwmon` | 241 | 105477.44 | 57.59% | 14.96% |
| `drivers/gpu/drm/i915/display` | 343 | 103440.08 | 22.93% | 21.02% |
| `drivers/media/dvb-frontends` | 286 | 100851.26 | 31.68% | 4.27% |
| `drivers/media/i2c` | 185 | 89523.06 | 44.24% | 3.02% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `scripts/gdb/linux/mm.py` -> **100.0%** Exposure
- `tools/perf/scripts/python/stat-cpi.py` -> **100.0%** Exposure
- `arch/arm/kernel/reboot.c` -> **100.0%** Exposure
- `arch/arm/mach-omap2/prm2xxx_3xxx.c` -> **100.0%** Exposure
- `arch/m68k/include/asm/bug.h` -> **100.0%** Exposure
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
- `sound/pci/asihpi/hpifunc.c` -> **194** Orphaned Functions | **0** Duplicates
- `tools/testing/selftests/landlock/fs_test.c` -> **139** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tools/testing/selftests/net/mptcp/diag.sh` -> **90.8129%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `309` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `376248` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `kernel/bpf/verifier.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.729)
- **Top Global Matches:** file_cluster_4: 7.729, file_cluster_6: 9.141, file_cluster_16: 13.797
- **Magnitude:** 23810.46 | **LOC:** 26244 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 18.2%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **29**; blast radius 0.055; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.2%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (75.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_mem_access` **(Many-Argument Workhorses)** (Impact: 392.8)
    * *Intent:* /* check whether memory at (regno + off) is accessible for t = (read | write) * if t==write, value_r...
  * `check_kfunc_args` **(Many-Argument Workhorses)** (Impact: 385.3)
  * `do_misc_fixups` **(Many-Argument Workhorses)** (Impact: 332.3)
    * *Intent:* /* Do various post-verification rewrites in a single program pass. * These rewrites simplify JIT and...
  * `check_map_func_compatibility` **(Many-Argument Workhorses)** (Impact: 316.6)
  * `check_helper_call` **(Many-Argument Workhorses)** (Impact: 292.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3278 instances
* *State Mutation (weighted view):* 10271
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5332`, `structural_boundaries: 5594`, `args: 938`, `func_start: 670`, `class_start: 927`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 3715`, `dead_code: 5`, `planned_debt: 12`, `fragile_debt: 7`, `unreferenced_by_name: 4`
* *Architecture:* `api: 35`, `import: 29`
* *Defense:* `safety: 25`, `immutability_locks: 375`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 53):` disasm.h, bpf-cgroup.h, bpf.h, bpf_lsm.h, bpf_mem_alloc.h, bpf_types.h, bpf_verifier.h, bsearch.h...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `net/wireless/nl80211.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.975)
- **Top Global Matches:** file_cluster_8: 8.975, file_cluster_6: 11.816, file_cluster_4: 19.681
- **Magnitude:** 18424.9 | **LOC:** 22051 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **22**; blast radius 0.023; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.1%)
- **Documentation Coverage:** 99.9103% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nl80211_send_wiphy` **(Many-Argument Workhorses)** (Impact: 644.1)
  * `nl80211_send_station` **(Many-Argument Workhorses)** (Impact: 209.1)
  * `nl80211_parse_sched_scan` **(Many-Argument Workhorses)** (Impact: 184.7)
  * `nl80211_set_wiphy` **(Many-Argument Workhorses)** (Impact: 165.2)
  * `nl80211_msg_put_channel` **(Many-Argument Workhorses)** (Impact: 163.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2326 instances
* *State Mutation (weighted view):* 7137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4519`, `structural_boundaries: 4175`, `args: 907`, `func_start: 363`, `class_start: 1091`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 2485`, `planned_debt: 1`, `fragile_debt: 5`, `unreferenced_by_name: 23`
* *Architecture:* `api: 85`, `import: 22`
* *Defense:* `safety: 18`, `doc: 1`, `test: 2`, `immutability_locks: 202`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 46):` core.h, err.h, etherdevice.h, ieee80211.h, if.h, if_ether.h, if_vlan.h, list.h...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `drivers/gpu/drm/amd/display/dc/dml2_0/dml21/src/dml2_core/dml2_core_dcn4_calcs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.906)
- **Top Global Matches:** file_cluster_8: 6.906, file_cluster_6: 15.037, file_cluster_3: 22.817
- **Magnitude:** 15846.44 | **LOC:** 13360 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.006; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.2%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dml_core_mode_support` **(Many-Argument Workhorses)** (Impact: 617.1)
  * `CalculateOutputLink` **(Many-Argument Workhorses)** (Impact: 464.1)
  * `CalculateDCCConfiguration` **(Many-Argument Workhorses)** (Impact: 428.6)
  * `CalculateBytePerPixelAndBlockSizes` **(Many-Argument Workhorses)** (Impact: 292.8)
  * `CalculateDETBufferSize` **(Many-Argument Workhorses)** (Impact: 264.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2206 instances
* *State Mutation (weighted view):* 8974
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2224`, `structural_boundaries: 926`, `args: 237`, `func_start: 117`, `class_start: 137`
* *Risk/State:* `state_mutation: 4562`, `dead_code: 32`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 19`, `import: 5`
* *Defense:* `immutability_locks: 86`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 6):` dml2_core_dcn4_calcs.h, dml2_debug.h, dml2_internal_shared_types.h, dml_top_types.h, lib_float_math.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `drivers/video/fbdev/sis/init301.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.556)
- **Top Global Matches:** file_cluster_8: 7.556, file_cluster_6: 10.321, file_cluster_4: 18.678
- **Magnitude:** 15332.6 | **LOC:** 11380 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 0.009; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.9%), Guard Balance (formerly Safety Score) (83.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 79.0816% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SiS_GetLCDResInfo` **(Many-Argument Workhorses)** (Impact: 483.9)
  * `SiS_SetGroup1_LVDS` **(Many-Argument Workhorses)** (Impact: 452.6)
    * *Intent:* /* Setup panel link * This is used for LVDS, LCDA and Chrontel TV output * 300/LVDS+TV, 300/301B-DH,...
  * `SiS_SetGroup2` **(Many-Argument Workhorses)** (Impact: 452.5)
  * `SiS_GetCRT2Data301` **(Many-Argument Workhorses)** (Impact: 329.1)
  * `SiS_SetGroup1` **(Many-Argument Workhorses)** (Impact: 271.3)
    * *Intent:* /* Set Part 1 */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2481 instances
* *State Mutation (weighted view):* 7595
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3364`, `structural_boundaries: 932`, `args: 1701`, `func_start: 163`
* *Risk/State:* `state_mutation: 2633`, `dead_code: 20`, `planned_debt: 1`, `fragile_debt: 7`, `unreferenced_by_name: 9`
* *Architecture:* `api: 33`, `import: 3`
* *Defense:* `doc: 64`, `immutability_locks: 65`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 4):` init301.h, oem300.h, oem310.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `drivers/scsi/lpfc/lpfc_sli.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.84)
- **Top Global Matches:** file_cluster_6: 5.84, file_cluster_4: 9.625, file_cluster_8: 15.776
- **Magnitude:** 14767.74 | **LOC:** 22850 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **31**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.8%), Complexity Load (formerly Cognitive Load) (58.5%)
- **Documentation Coverage:** 10.4418% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lpfc_sli_issue_mbox_s3` **(Many-Argument Workhorses)** (Impact: 167.5)
    * *Intent:* * If the mailbox is submitted in no_wait mode (not polling) the * function will submit the command a...
  * `lpfc_sli4_hba_setup` **(Many-Argument Workhorses)** (Impact: 167.2)
    * *Intent:* /** * lpfc_sli4_hba_setup - SLI4 device initialization PCI function * @phba: Pointer to HBA context ...
  * `lpfc_rq_create` **(Many-Argument Workhorses)** (Impact: 125.9)
    * *Intent:* * to the HBA. * * The @phba struct is used to send mailbox command to HBA. The @drq and @hrq * struc...
  * `lpfc_sli_iocb_cmd_type` **(Compute Cores)** (Impact: 115.3)
    * *Intent:* * lpfc_sli_iocb_cmd_type - Get the iocb type * @iocb_cmnd: iocb command code. * * This function is c...
  * `lpfc_cq_create_set` **(Many-Argument Workhorses)** (Impact: 114.3)
    * *Intent:* * described by @phba by sending a CREATE_CQ_SET mailbox command to the HBA. * * The @phba struct is ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2347 instances
* *State Mutation (weighted view):* 7700
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2710`, `structural_boundaries: 2602`, `args: 495`, `func_start: 351`, `class_start: 688`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 3006`, `dead_code: 1`, `unreferenced_by_name: 105`
* *Architecture:* `api: 181`, `import: 31`
* *Defense:* `safety: 3`, `doc: 303`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 61):` set_memory.h, blkdev.h, crash_dump.h, delay.h, dmi.h, interrupt.h, lockdep.h, of.h...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `scripts/checkpatch.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.248)
- **Top Global Matches:** file_cluster_6: 8.248, file_cluster_4: 13.649, file_cluster_8: 13.89
- **Magnitude:** 13819.66 | **LOC:** 7931 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 0.005; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.6%), Guard Balance (formerly Safety Score) (74.6%), Debt Markers (formerly Tech Debt) (11.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ctx_statement_block` **(Many-Argument Workhorses)** (Impact: 8495.1)
  * `process` **(Compute Cores)** (Impact: 910.3)
  * `annotate_values` **(Many-Argument Workhorses)** (Impact: 200.5)
  * `build_types` **(Compute Cores)** (Impact: 87.4)
  * `ctx_block_get` **(Many-Argument Workhorses)** (Impact: 71.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 1023 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 3079
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4138`, `structural_boundaries: 1310`, `args: 68`, `func_start: 73`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 28`, `state_mutation: 1033`, `dead_code: 46`, `fragile_debt: 9`, `unreferenced_by_name: 4`
* *Architecture:* `io: 38`, `api: 73`, `import: 49`
* *Defense:* `safety: 2`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 3):` C99, Cwd, Encode, File::Basename, Getopt::Long, Kconfig, POSIX, Term::ANSIColor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/gpu/drm/amd/display/dc/dml2_0/display_mode_core.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.716)
- **Top Global Matches:** file_cluster_8: 8.716, file_cluster_3: 17.507, file_cluster_6: 20.035
- **Magnitude:** 12599.18 | **LOC:** 10346 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.005; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.8%), Guard Balance (formerly Safety Score) (80.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 67.0886% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dml_core_mode_support` **(Many-Argument Workhorses)** (Impact: 753.0)
    * *Intent:* /// @brief The Mode Support function.
  * `CalculateDCCConfiguration` **(Many-Argument Workhorses)** (Impact: 416.7)
  * `CalculateOutputLink` **(Many-Argument Workhorses)** (Impact: 351.1)
  * `CalculateVMAndRowBytes` **(Many-Argument Workhorses)** (Impact: 315.7)
  * `dml_core_mode_programming` **(Many-Argument Workhorses)** (Impact: 313.2)
    * *Intent:* /// @brief This is the mode programming function. It is assumed the display cfg is support at the gi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1750 instances
* *State Mutation (weighted view):* 6540
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1822`, `structural_boundaries: 710`, `args: 299`, `func_start: 69`, `class_start: 157`
* *Risk/State:* `state_mutation: 3040`, `dead_code: 14`, `planned_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 10`, `import: 4`
* *Defense:* `doc: 48`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 5):` display_mode_core.h, display_mode_lib_defines.h, display_mode_util.h, dml_assert.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `drivers/gpu/drm/amd/display/dc/dml/dcn314/display_mode_vba_314.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.062)
- **Top Global Matches:** file_cluster_3: 9.062, file_cluster_8: 16.733, file_cluster_6: 29.406
- **Magnitude:** 11766.56 | **LOC:** 7344 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.005; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (100.0%), Guard Balance (formerly Safety Score) (80.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CalculatePrefetchSchedule` **(Many-Argument Workhorses)** (Impact: 2460.4)
  * `dml314_ModeSupportAndSystemConfigurationFull` **(Many-Argument Workhorses)** (Impact: 836.0)
  * `CalculateDCCConfiguration` **(Many-Argument Workhorses)** (Impact: 545.4)
  * `CalculateStutterEfficiency` **(Many-Argument Workhorses)** (Impact: 381.4)
  * `CalculateSwathAndDETConfiguration` **(Many-Argument Workhorses)** (Impact: 308.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1518 instances
* *State Mutation (weighted view):* 4801
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1414`, `structural_boundaries: 622`, `args: 151`, `func_start: 37`, `class_start: 89`
* *Risk/State:* `state_mutation: 1765`, `dead_code: 2`, `planned_debt: 7`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 4):` display_mode_lib.h, dml_inline_defs.h, dc.h, display_mode_vba_314.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/gpu/drm/amd/display/dc/dml/dcn31/display_mode_vba_31.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 10.089)
- **Top Global Matches:** file_cluster_3: 10.089, file_cluster_8: 15.236, file_cluster_6: 27.854
- **Magnitude:** 11422.92 | **LOC:** 7229 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.005; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.9%), Guard Balance (formerly Safety Score) (80.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CalculatePrefetchSchedule` **(Many-Argument Workhorses)** (Impact: 2460.3)
  * `dml31_ModeSupportAndSystemConfigurationFull` **(Many-Argument Workhorses)** (Impact: 820.4)
  * `CalculateDCCConfiguration` **(Many-Argument Workhorses)** (Impact: 545.4)
  * `CalculateStutterEfficiency` **(Many-Argument Workhorses)** (Impact: 381.4)
  * `CalculateSwathAndDETConfiguration` **(Many-Argument Workhorses)** (Impact: 325.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1449 instances
* *State Mutation (weighted view):* 4590
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1370`, `structural_boundaries: 637`, `args: 146`, `func_start: 36`, `class_start: 84`
* *Risk/State:* `state_mutation: 1692`, `dead_code: 1`, `planned_debt: 7`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 6):` display_mode_vba_30.h, display_mode_lib.h, dml_inline_defs.h, dc.h, display_mode_vba_31.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/x86/kvm/x86.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.75)
- **Top Global Matches:** file_cluster_4: 6.75, file_cluster_16: 9.302, file_cluster_15: 10.593
- **Magnitude:** 10764.16 | **LOC:** 14497 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **66**; blast radius 0.017; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.8%)
- **Documentation Coverage:** 99.1982% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `kvm_set_msr_common` **(Many-Argument Workhorses)** (Impact: 272.8)
  * `kvm_arch_vcpu_ioctl` **(Many-Argument Workhorses)** (Impact: 243.9)
  * `kvm_get_msr_common` **(Many-Argument Workhorses)** (Impact: 217.7)
  * `kvm_vm_ioctl_check_extension` **(Compute Cores)** (Impact: 209.8)
  * `kvm_arch_vm_ioctl` **(Many-Argument Workhorses)** (Impact: 188.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1432 instances
* *State Mutation (weighted view):* 4540
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2419`, `structural_boundaries: 2799`, `args: 845`, `func_start: 511`, `class_start: 302`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1676`, `planned_debt: 5`, `fragile_debt: 11`, `unreferenced_by_name: 61`
* *Architecture:* `api: 191`, `import: 67`
* *Defense:* `safety: 3`, `doc: 3`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 108):` debugreg.h, desc.h, div64.h, emulate_prefix.h, api.h, xcr.h, xstate.h, hypervisor.h...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `drivers/accel/habanalabs/gaudi/gaudi_security.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.304)
- **Top Global Matches:** file_cluster_15: 7.304, file_cluster_2: 7.475, file_cluster_16: 8.139
- **Magnitude:** 10607.86 | **LOC:** 13080 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.005; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (50.0%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `gaudi_init_range_registers_hbw` **(Compute Cores)** (Impact: 10.2)
  * `gaudi_init_range_registers_lbw` **(I/O & Config Routines)** (Impact: 8.6)
  * `gaudi_init_dma_protection_bits` **(I/O & Config Routines)** (Impact: 5.3)
  * `gaudi_init_tpc_protection_bits` **(I/O & Config Routines)** (Impact: 5.3)
  * `gaudi_init_protection_bits` **(Stateful Encapsulated Methods)** (Impact: 5.1)
    * *Intent:* /** * gaudi_init_protection_bits - Initialize protection bits of specific registers * * @hdev: point...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 10319
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 22`, `args: 20`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 10293`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 2):` gaudi_regs.h, gaudiP.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `drivers/gpu/drm/amd/display/amdgpu_dm/amdgpu_dm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.52)
- **Top Global Matches:** file_cluster_6: 6.52, file_cluster_4: 12.41, file_cluster_8: 13.421
- **Magnitude:** 10442.08 | **LOC:** 13613 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **33** in-repo importer(s); it depends on **66**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.3%)
- **Documentation Coverage:** 84.949% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `amdgpu_dm_commit_planes` **(Many-Argument Workhorses)** (Impact: 186.1)
  * `amdgpu_dm_initialize_drm_device` **(Compute Cores)** (Impact: 183.2)
    * *Intent:* /* * In this architecture, the association * connector -> encoder -> crtc * id not really requried. ...
  * `amdgpu_dm_atomic_check` **(Many-Argument Workhorses)** (Impact: 157.2)
    * *Intent:* * * When validating the DC state, it's important that the right locks are * acquired. For full updat...
  * `dm_update_crtc_state` **(Many-Argument Workhorses)** (Impact: 146.6)
  * `amdgpu_dm_init` **(Compute Cores)** (Impact: 132.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1543 instances
* *State Mutation (weighted view):* 4938
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2335`, `structural_boundaries: 2636`, `args: 331`, `func_start: 250`, `class_start: 803`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1852`, `dead_code: 1`, `planned_debt: 46`, `fragile_debt: 9`, `unreferenced_by_name: 10`
* *Architecture:* `api: 29`, `import: 66`
* *Defense:* `safety: 10`, `doc: 39`, `immutability_locks: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 152):` video.h, amd_shared.h, amdgpu.h, amdgpu_atombios.h, amdgpu_display.h, amdgpu_dm.h, amdgpu_dm_crtc.h, amdgpu_dm_debugfs.h...
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `drivers/scsi/lpfc/lpfc_init.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.917)
- **Top Global Matches:** file_cluster_4: 6.917, file_cluster_6: 7.341, file_cluster_16: 14.388
- **Magnitude:** 9816.68 | **LOC:** 15836 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **40**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.8%), Complexity Load (formerly Cognitive Load) (57.7%)
- **Documentation Coverage:** 10.3718% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lpfc_get_hba_model_desc` **(Many-Argument Workhorses)** (Impact: 187.8)
    * *Intent:* /** * lpfc_get_hba_model_desc - Retrieve HBA device model name and description * @phba: pointer to l...
  * `lpfc_sli4_driver_resource_setup` **(Many-Argument Workhorses)** (Impact: 102.6)
    * *Intent:* /** * lpfc_sli4_driver_resource_setup - Setup drvr internal resources for SLI4 dev * @phba: pointer ...
  * `lpfc_sli4_read_config` **(Compute Cores)** (Impact: 91.3)
    * *Intent:* /** * lpfc_sli4_read_config - Get the config parameters. * @phba: pointer to lpfc hba data structure...
  * `lpfc_sli4_async_sli_evt` **(Many-Argument Workhorses)** (Impact: 86.9)
    * *Intent:* /** * lpfc_sli4_async_sli_evt - Process the asynchronous SLI link event * @phba: pointer to lpfc hba...
  * `lpfc_sli4_queue_setup` **(Many-Argument Workhorses)** (Impact: 83.7)
    * *Intent:* /** * lpfc_sli4_queue_setup - Set up all the SLI4 queues * @phba: pointer to lpfc hba data structure...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1726 instances
* *State Mutation (weighted view):* 5662
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1731`, `structural_boundaries: 1633`, `args: 446`, `func_start: 254`, `class_start: 309`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 2210`, `unreferenced_by_name: 27`
* *Architecture:* `api: 88`, `import: 40`
* *Defense:* `safety: 9`, `doc: 218`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 77):` bitops.h, blkdev.h, cpu.h, cpuhotplug.h, crash_dump.h, ctype.h, delay.h, dma-mapping.h...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `drivers/scsi/mpt3sas/mpt3sas_scsih.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.518)
- **Top Global Matches:** file_cluster_6: 5.518, file_cluster_4: 11.668, file_cluster_8: 13.365
- **Magnitude:** 9736.72 | **LOC:** 14171 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **13**; blast radius 0.006; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.4%), Complexity Load (formerly Cognitive Load) (58.6%)
- **Documentation Coverage:** 7.4627% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_scsih_io_done` **(Many-Argument Workhorses)** (Impact: 197.4)
    * *Intent:* /** * _scsih_io_done - scsi request callback * @ioc: per adapter object * @smid: system request mess...
  * `_scsih_probe` **(Many-Argument Workhorses)** (Impact: 152.7)
    * *Intent:* /** * _scsih_probe - attach and add scsi host * @pdev: PCI device struct * @id: pci device id * * Re...
  * `_scsih_scsi_ioc_info` **(Many-Argument Workhorses)** (Impact: 130.7)
    * *Intent:* /** * _scsih_scsi_ioc_info - translated non-successful SCSI_IO request * @ioc: per adapter object * ...
  * `_scsih_determine_disposition` **(Many-Argument Workhorses)** (Impact: 106.0)
    * *Intent:* /** * _scsih_determine_disposition - * @ioc: per adapter object * @transfer_packet: packet describin...
  * `mpt3sas_scsih_issue_tm` **(Many-Argument Workhorses)** (Impact: 103.5)
    * *Intent:* * @type: MPI2_SCSITASKMGMT_TASKTYPE__XXX (defined in mpi2_init.h) * @smid_task: smid assigned to the...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1475 instances
* *State Mutation (weighted view):* 4650
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2110`, `structural_boundaries: 1782`, `args: 351`, `func_start: 239`, `class_start: 415`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 1700`, `planned_debt: 8`, `fragile_debt: 1`, `unreferenced_by_name: 6`
* *Architecture:* `api: 31`, `import: 13`
* *Defense:* `safety: 2`, `doc: 222`, `immutability_locks: 8`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 43):` blkdev.h, delay.h, errno.h, init.h, interrupt.h, kernel.h, module.h, pci.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `drivers/media/dvb-frontends/drx39xyj/drxj.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.72)
- **Top Global Matches:** file_cluster_8: 7.72, file_cluster_3: 18.073, file_cluster_6: 19.052
- **Magnitude:** 9690.1 | **LOC:** 12392 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.005; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.7%), Complexity Load (formerly Cognitive Load) (64.2%)
- **Documentation Coverage:** 26.4033% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_qam` **(Many-Argument Workhorses)** (Impact: 374.0)
    * *Intent:* /*============================================================================*/ #define QAM_SET_OP_...
  * `ctrl_set_cfg_mpeg_output` **(Many-Argument Workhorses)** (Impact: 285.8)
    * *Intent:* /*----------------------------------------------------------------------------*/ /* MPEG Output Conf...
  * `ctrl_set_oob` **(Many-Argument Workhorses)** (Impact: 168.7)
    * *Intent:* * because START command causes COMM_EXEC transition * from 0 to 1 which causes all registers to be *...
  * `ctrl_set_channel` **(Many-Argument Workhorses)** (Impact: 161.5)
    * *Intent:* ===========================================================================*/ /* * \fn int ctrl_set_...
  * `set_vsb` **(Many-Argument Workhorses)** (Impact: 133.8)
    * *Intent:* /* * \fn int set_vsb() * \brief Set 8VSB demod. * \param demod instance of demodulator. * \return in...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1822 instances
* *State Mutation (weighted view):* 5645
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1784`, `structural_boundaries: 1113`, `args: 127`, `func_start: 99`, `class_start: 188`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 2001`, `dead_code: 16`, `planned_debt: 35`, `fragile_debt: 2`
* *Architecture:* `api: 10`, `import: 12`
* *Defense:* `doc: 293`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 12):` div64.h, drx39xxj.h, drx_driver_version.h, drxj.h, drxj_map.h, firmware.h, init.h, module.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/gpu/drm/amd/display/dc/dml/dcn30/display_mode_vba_30.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.374)
- **Top Global Matches:** file_cluster_3: 6.374, file_cluster_8: 21.994, file_cluster_6: 34.877
- **Magnitude:** 9412.06 | **LOC:** 6360 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 0.007; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dml30_ModeSupportAndSystemConfigurationFull` **(Many-Argument Workhorses)** (Impact: 705.6)
  * `CalculatePrefetchSchedule` **(Many-Argument Workhorses)** (Impact: 625.1)
  * `CalculateDCCConfiguration` **(Many-Argument Workhorses)** (Impact: 542.5)
  * `CalculateSwathAndDETConfiguration` **(Many-Argument Workhorses)** (Impact: 309.3)
  * `CalculateVMAndRowBytes` **(Many-Argument Workhorses)** (Impact: 273.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1456 instances
* *State Mutation (weighted view):* 4580
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1284`, `structural_boundaries: 517`, `args: 126`, `func_start: 33`, `class_start: 77`
* *Risk/State:* `state_mutation: 1668`, `dead_code: 1`, `planned_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 4):` display_mode_lib.h, dml_inline_defs.h, dc.h, display_mode_vba_30.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `net/mac80211/mlme.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.434)
- **Top Global Matches:** file_cluster_6: 5.434, file_cluster_4: 11.76, file_cluster_8: 13.144
- **Magnitude:** 9230.66 | **LOC:** 11229 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **19**; blast radius 0.01; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.7%), Guard Balance (formerly Safety Score) (74.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ieee80211_assoc_config_link` **(Many-Argument Workhorses)** (Impact: 310.4)
  * `ieee80211_determine_chan_mode` **(Many-Argument Workhorses)** (Impact: 157.0)
  * `ieee80211_determine_ap_chan` **(Many-Argument Workhorses)** (Impact: 154.0)
  * `ieee80211_mgd_assoc` **(Many-Argument Workhorses)** (Impact: 151.1)
  * `ieee80211_rx_mgmt_beacon` **(Many-Argument Workhorses)** (Impact: 146.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1400 instances
* *State Mutation (weighted view):* 4352
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1740`, `structural_boundaries: 2025`, `args: 330`, `func_start: 182`, `class_start: 541`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 1552`, `planned_debt: 9`, `fragile_debt: 10`, `unreferenced_by_name: 27`
* *Architecture:* `api: 57`, `import: 19`
* *Defense:* `safety: 54`, `immutability_locks: 156`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 58):` driver-ops.h, fils_aead.h, ieee80211_i.h, static_stub.h, led.h, crc32.h, delay.h, etherdevice.h...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `drivers/gpu/drm/amd/display/dc/dml/dcn32/display_mode_vba_util_32.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.272)
- **Top Global Matches:** file_cluster_8: 10.272, file_cluster_3: 14.058, file_cluster_6: 22.749
- **Magnitude:** 9187.74 | **LOC:** 6351 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.006; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.8%), Complexity Load (formerly Cognitive Load) (75.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dml32_CalculatePrefetchSchedule` **(Many-Argument Workhorses)** (Impact: 861.8)
  * `dml32_CalculateWatermarksMALLUseAndDRAMSpeedChangeSupport` **(Many-Argument Workhorses)** (Impact: 490.2)
  * `dml32_CalculateDCCConfiguration` **(Many-Argument Workhorses)** (Impact: 417.2)
  * `dml32_CalculateVMAndRowBytes` **(Many-Argument Workhorses)** (Impact: 376.5)
  * `dml32_CalculateOutputLink` **(Many-Argument Workhorses)** (Impact: 353.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1173 instances
* *State Mutation (weighted view):* 3735
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1125`, `structural_boundaries: 453`, `args: 269`, `func_start: 50`, `class_start: 71`
* *Risk/State:* `state_mutation: 1389`, `dead_code: 9`, `fragile_debt: 1`, `unreferenced_by_name: 30`
* *Architecture:* `api: 50`, `import: 4`
* *Defense:* `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 4):` display_mode_lib.h, dml_inline_defs.h, display_mode_vba_32.h, display_mode_vba_util_32.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `fs/smb/server/smb2pdu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.737)
- **Top Global Matches:** file_cluster_6: 6.737, file_cluster_4: 12.551, file_cluster_8: 13.613
- **Magnitude:** 8893.36 | **LOC:** 9271 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **35**; blast radius 0.006; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.4%)
- **Documentation Coverage:** 41.8259% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `smb2_open` **(Many-Argument Workhorses)** (Impact: 384.2)
    * *Intent:* /** * smb2_open() - handler for smb file open request * @work: smb work containing request buffer * ...
  * `smb2_lock` **(Compute Cores)** (Impact: 127.1)
    * *Intent:* /** * smb2_lock() - handler for smb2 file lock command * @work: smb work containing lock command buf...
  * `smb2_sess_setup` **(Compute Cores)** (Impact: 118.5)
    * *Intent:* #endif
  * `smb2_ioctl` **(Compute Cores)** (Impact: 116.3)
    * *Intent:* /** * smb2_ioctl() - handler for smb2 ioctl command * @work: smb work containing ioctl command buffe...
  * `smb2_populate_readdir_entry` **(Many-Argument Workhorses)** (Impact: 102.3)
    * *Intent:* /** * smb2_populate_readdir_entry() - encode directory entry in smb2 response * buffer * @conn: conn...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1631 instances
* *State Mutation (weighted view):* 5277
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1594`, `structural_boundaries: 1548`, `args: 413`, `func_start: 149`, `class_start: 406`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 2015`, `planned_debt: 8`, `fragile_debt: 1`, `unreferenced_by_name: 39`
* *Architecture:* `io: 2`, `api: 49`, `import: 35`
* *Defense:* `safety: 19`, `doc: 52`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 79):` smb2status.h, smbdirect.h, asn1.h, auth.h, connection.h, utils.h, glob.h, ksmbd_work.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `drivers/md/md.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.168)
- **Top Global Matches:** file_cluster_4: 6.168, file_cluster_6: 8.577, file_cluster_16: 12.949
- **Magnitude:** 8816.16 | **LOC:** 10871 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **30**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (80.0%), Guard Balance (formerly Safety Score) (72.4%)
- **Documentation Coverage:** 99.4163% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `state_store` **(Many-Argument Workhorses)** (Impact: 156.4)
  * `md_ioctl` **(Many-Argument Workhorses)** (Impact: 143.9)
  * `super_1_load` **(Many-Argument Workhorses)** (Impact: 125.1)
  * `array_state_store` **(Many-Argument Workhorses)** (Impact: 120.5)
  * `super_1_validate` **(Many-Argument Workhorses)** (Impact: 120.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 1185 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 3740
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2170`, `structural_boundaries: 1706`, `args: 834`, `func_start: 314`, `class_start: 207`
* *Risk/State:* `safety_bypasses: 93`, `state_mutation: 1370`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 11`
* *Architecture:* `api: 73`, `import: 30`
* *Defense:* `safety: 48`, `doc: 2`, `immutability_locks: 74`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 72):` badblocks.h, blk-integrity.h, blkdev.h, compat.h, ctype.h, delay.h, file.h, fs.h...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `net/netfilter/nf_tables_api.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.404)
- **Top Global Matches:** file_cluster_4: 7.404, file_cluster_16: 10.102, file_cluster_15: 11.435
- **Magnitude:** 8744.06 | **LOC:** 12192 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **61** in-repo importer(s); it depends on **18**; blast radius 0.032; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (72.8%)
- **Documentation Coverage:** 97.358% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nft_add_set_elem` **(Many-Argument Workhorses)** (Impact: 297.9)
  * `nf_tables_newset` **(Many-Argument Workhorses)** (Impact: 183.2)
  * `nf_tables_commit` **(Many-Argument Workhorses)** (Impact: 131.7)
  * `nf_tables_newrule` **(Many-Argument Workhorses)** (Impact: 125.8)
    * *Intent:* #define NFT_RULE_MAXEXPRS 128
  * `nf_tables_updchain` **(Many-Argument Workhorses)** (Impact: 120.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 1076 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 3315
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1887`, `structural_boundaries: 3019`, `args: 495`, `func_start: 390`, `class_start: 748`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 1`, `state_mutation: 1163`, `fragile_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `io: 1`, `api: 80`, `import: 18`
* *Defense:* `safety: 4`, `doc: 10`, `immutability_locks: 551`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 47):` audit.h, init.h, list.h, module.h, netfilter.h, nf_tables.h, nfnetlink.h, netfilter_ipv4.h...
  * `Imported By (In-Degree: 61):` (Excluded from Brief to save tokens)

### `net/core/filter.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.611)
- **Top Global Matches:** file_cluster_6: 6.611, file_cluster_4: 8.602, file_cluster_16: 16.185
- **Magnitude:** 8619.42 | **LOC:** 12589 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **112** in-repo importer(s); it depends on **69**; blast radius 0.318; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.0%), Guard Balance (formerly Safety Score) (66.9%)
- **Documentation Coverage:** 93.6842% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bpf_convert_filter` **(Many-Argument Workhorses)** (Impact: 242.5)
    * *Intent:* * @new_len: pointer to store length of converted program * @seen_ld_abs: bool whether we've seen ld_...
  * `bpf_convert_ctx_access` **(Many-Argument Workhorses)** (Impact: 150.5)
  * `sock_addr_is_valid_access` **(Many-Argument Workhorses)** (Impact: 140.7)
  * `sock_ops_convert_ctx_access` **(Many-Argument Workhorses)** (Impact: 132.4)
  * `tc_cls_act_func_proto` **(Compute Cores)** (Impact: 114.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1096 instances
* *State Mutation (weighted view):* 3496
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2278`, `structural_boundaries: 3851`, `args: 1145`, `func_start: 266`, `class_start: 362`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 1304`, `dead_code: 4`, `fragile_debt: 1`, `unreferenced_by_name: 23`
* *Architecture:* `api: 50`, `import: 69`
* *Defense:* `safety: 1`, `doc: 12`, `immutability_locks: 355`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.318
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 109):` dev.h, atomic.h, bpf.h, bpf_trace.h, bpf_verifier.h, btf.h, btf_ids.h, errno.h...
  * `Imported By (In-Degree: 112):` (Excluded from Brief to save tokens)

### `drivers/scsi/lpfc/lpfc_els.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.312)
- **Top Global Matches:** file_cluster_6: 6.312, file_cluster_4: 10.417, file_cluster_8: 15.624
- **Magnitude:** 8561.86 | **LOC:** 12562 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **23**; blast radius 0.006; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.0%), Complexity Load (formerly Cognitive Load) (64.8%)
- **Documentation Coverage:** 20.9845% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lpfc_els_retry` **(Many-Argument Workhorses)** (Impact: 308.6)
    * *Intent:* * failed. The following ELS IOCBs use this function for retrying the command * when previously issue...
  * `lpfc_els_unsol_buffer` **(Many-Argument Workhorses)** (Impact: 213.1)
    * *Intent:* /** * lpfc_els_unsol_buffer - Process an unsolicited event data buffer * @phba: pointer to lpfc hba ...
  * `lpfc_cmpl_els_flogi` **(Many-Argument Workhorses)** (Impact: 125.0)
    * *Intent:* * retry has been made (either immediately or delayed with lpfc_els_retry() * returning 1), the comma...
  * `lpfc_prep_els_iocb` **(Many-Argument Workhorses)** (Impact: 110.0)
    * *Intent:* * and preparation routine that is used by all the discovery state machine * routines and the ELS com...
  * `lpfc_plogi_confirm_nport` **(Many-Argument Workhorses)** (Impact: 93.3)
    * *Intent:* * into, a new node shall be allocated (or activated). In either case, the * parameters of the @ndlp ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1424 instances
* *State Mutation (weighted view):* 4669
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1484`, `structural_boundaries: 1438`, `args: 466`, `func_start: 154`, `class_start: 407`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 1821`, `planned_debt: 1`, `unreferenced_by_name: 24`
* *Architecture:* `api: 58`, `import: 23`
* *Defense:* `doc: 119`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 42):` blkdev.h, delay.h, interrupt.h, pci.h, slab.h, lpfc.h, lpfc_crtn.h, lpfc_debugfs.h...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `kernel/events/core.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.859)
- **Top Global Matches:** file_cluster_16: 6.859, file_cluster_4: 8.111, file_cluster_15: 8.815
- **Magnitude:** 8290.86 | **LOC:** 15373 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **140** in-repo importer(s); it depends on **52**; blast radius 0.109; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.2%), Guard Balance (formerly Safety Score) (66.4%)
- **Documentation Coverage:** 98.7212% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `perf_event_alloc` **(Many-Argument Workhorses)** (Impact: 155.9)
    * *Intent:* /* * Allocate and initialize an event structure */
  * `perf_output_sample` **(Many-Argument Workhorses)** (Impact: 108.0)
  * `perf_event_parse_addr_filter` **(Many-Argument Workhorses)** (Impact: 77.8)
    * *Intent:* /* * Address filter string parser */
  * `perf_copy_attr` **(Many-Argument Workhorses)** (Impact: 73.8)
  * `_perf_ioctl` **(Many-Argument Workhorses)** (Impact: 59.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1074 instances
* *State Mutation (weighted view):* 3381
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1746`, `structural_boundaries: 2999`, `args: 652`, `func_start: 559`, `class_start: 766`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1233`, `planned_debt: 2`, `fragile_debt: 9`, `unreferenced_by_name: 40`
* *Architecture:* `io: 3`, `api: 115`, `import: 52`
* *Defense:* `safety: 16`, `doc: 4`, `immutability_locks: 57`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.109
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 102):` irq_regs.h, internal.h, anon_inodes.h, bpf.h, buildid.h, cgroup.h, compat.h, cpu.h...
  * `Imported By (In-Degree: 140):` (Excluded from Brief to save tokens)

### `drivers/accel/habanalabs/gaudi2/gaudi2.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.894)
- **Top Global Matches:** file_cluster_4: 8.894, file_cluster_16: 9.772, file_cluster_15: 11.63
- **Magnitude:** 8277.48 | **LOC:** 12009 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 0.006; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.7%), Complexity Load (formerly Cognitive Load) (66.7%)
- **Documentation Coverage:** 98.9189% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `gaudi2_handle_eqe` **(Many-Argument Workhorses)** (Impact: 343.0)
  * `event_id_to_engine_id` **(Compute Cores)** (Impact: 169.3)
  * `gaudi2_ack_module_razwi_event_handler` **(Many-Argument Workhorses)** (Impact: 83.6)
    * *Intent:* /* * This function handles RR(Range register) hit events. * raised be initiators not PSOC RAZWI. */
  * `gaudi2_handle_qman_err` **(Many-Argument Workhorses)** (Impact: 58.0)
  * `get_hmmu_base` **(Compute Cores)** (Impact: 54.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1382 instances
* *State Mutation (weighted view):* 4669
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1329`, `structural_boundaries: 1675`, `args: 853`, `func_start: 306`, `class_start: 244`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 1905`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 19`, `import: 13`
* *Defense:* `safety: 16`, `doc: 4`, `immutability_locks: 90`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 40):` gaudi2_arc_common_packets.h, gaudi2_async_ids_map_extended.h, gaudi2_packets.h, gaudi2_reg_map.h, gaudi2_special_blocks.h, mmu_general.h, mmu_v2_0.h, gaudi2P.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `rust/syn/lib.rs` (RUST) | Magnitude: 81.92 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 619, indent_spaces: 130, decorators: 121, structural_boundaries: 91
- `drivers/android/binder/process.rs` (RUST) | Magnitude: 907.1 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1262, structural_boundaries: 398, branch: 246, core_var_decl: 179
- `rust/kernel/alloc/layout.rs` (RUST) | Magnitude: 27.16 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: doc: 42, indent_spaces: 41, generics: 14, api: 10
- `rust/kernel/print.rs` (RUST) | Magnitude: 48.52 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 253, indent_spaces: 160, decorators: 39, structural_boundaries: 20
- `drivers/scsi/aic7xxx/aicasm/aicasm_macro_scan.l` (YACC) | Magnitude: 67.8 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 50, state_mutation: 17, import: 11, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tools/testing/selftests/powerpc/dscr/dscr.h` (C) | Magnitude: 0.02 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 18, import: 13, args: 12, macros: 11
- `arch/m68k/hp300/time.c` (C) | Magnitude: 37.94 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 34, args: 16, import: 13, macros: 13
- `drivers/clk/ti/clockdomain.c` (C) | Magnitude: 63.04 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 68, pointers: 32, structural_boundaries: 25, state_mutation: 11
- `arch/x86/math-emu/reg_u_add.S` (ASSEMBLY) | Magnitude: 35.0 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 79, args: 45, structural_boundaries: 29, func_start: 13
- `drivers/scsi/megaraid/megaraid_sas_debugfs.c` (C) | Magnitude: 73.36 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 54, pointers: 51, structural_boundaries: 39, args: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tools/perf/ui/tui/progress.c` (C) | Magnitude: 0.04 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 44, pointers: 22, structural_boundaries: 16, state_mutation: 10
- `net/sunrpc/sysfs.c` (C) | Magnitude: 570.18 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 432, pointers: 352, structural_boundaries: 209, state_mutation: 103
- `tools/perf/util/parse-regs-options.c` (C) | Magnitude: 0.11 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 65, branch: 21, pointers: 20, structural_boundaries: 19
- `drivers/hwtracing/stm/console.c` (C) | Magnitude: 12.54 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 22, indent_tabs: 21, pointers: 20, args: 8
- `tools/testing/selftests/bpf/progs/test_core_reloc_kernel.c` (C) | Magnitude: 0.03 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 39, pointers: 25, structural_boundaries: 19, state_mutation: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `drivers/gpu/nova-core/gsp/fw/r570_144/bindings.rs` (RUST) | Magnitude: 748.34 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: api: 704, indent_spaces: 437, core_var_decl: 319, design_snake_case: 299
- `drivers/gpu/nova-core/nova_core.rs` (RUST) | Magnitude: 16.48 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 6, api: 1, doc: 1
- `rust/kernel/jump_label.rs` (RUST) | Magnitude: 14.46 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 26, doc: 21, decorators: 9, structural_boundaries: 5
- `rust/syn/custom_keyword.rs` (RUST) | Magnitude: 34.12 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 103, doc: 97, decorators: 30, structural_boundaries: 18
- `rust/proc-macro2/detection.rs` (RUST) | Magnitude: 19.7 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 12, core_var_decl: 9, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `tools/testing/selftests/drivers/net/bonding/bond-break-lacpdu-tx.sh` (SHELL) | Magnitude: 0.03 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: io: 17, indent_tabs: 10, branch: 6, safety_bypasses: 6
- `arch/um/Makefile` (MAKEFILE) | Magnitude: 37.92 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 27, indent_tabs: 20, safety_bypasses: 14, state_mutation: 14
- `arch/alpha/kernel/bugs.c` (C) | Magnitude: 30.44 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 16, indent_tabs: 13, pointers: 12, branch: 8
- `tools/testing/selftests/gpio/gpio-mockup-sysfs.sh` (SHELL) | Magnitude: 0.05 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 36, io: 27, structural_boundaries: 23, core_var_decl: 11
- `tools/testing/selftests/net/netfilter/nft_concat_range.sh` (SHELL) | Magnitude: 1.25 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 1147, structural_boundaries: 831, core_var_decl: 323, design_snake_case: 291

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `drivers/base/firmware_loader/builtin/main.c` (C) | Magnitude: 48.92 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 35, indent_tabs: 28, pointers: 24, branch: 8
- `net/openvswitch/dp_notify.c` (C) | Magnitude: 40.16 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 43, pointers: 25, structural_boundaries: 21, class_start: 10
- `kernel/bpf/offload.c` (C) | Magnitude: 566.3 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: pointers: 488, indent_tabs: 478, structural_boundaries: 236, state_mutation: 97
- `kernel/rcu/tiny.c` (C) | Magnitude: 94.32 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 85, structural_boundaries: 36, pointers: 32, args: 17
- `sound/core/seq/oss/seq_oss_synth.c` (C) | Magnitude: 456.68 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 325, pointers: 238, structural_boundaries: 123, state_mutation: 89

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `drivers/hwmon/pmbus/pmbus_core.c` (C) | Magnitude: 2688.34 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 2342, pointers: 1024, structural_boundaries: 836, state_mutation: 455
- `drivers/sh/intc/balancing.c` (C) | Magnitude: 72.1 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 43, pointers: 20, structural_boundaries: 17, state_mutation: 13
- `include/keys/request_key_auth-type.h` (C) | Magnitude: 3.96 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 9, indent_tabs: 9, pointers: 8, class_start: 4
- `arch/powerpc/include/asm/mediabay.h` (C) | Magnitude: 8.1 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 12, macros: 12, args: 6, pointers: 6
- `drivers/comedi/drivers/8255.c` (C) | Magnitude: 64.48 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 43, pointers: 16, state_mutation: 14, structural_boundaries: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `drivers/gpu/drm/nouveau/nvkm/subdev/therm/gf100.c` (C) | Magnitude: 17.12 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: pointers: 21, indent_tabs: 15, state_mutation: 7, structural_boundaries: 6
- `tools/testing/selftests/bpf/progs/test_pkt_md_access.c` (C) | Magnitude: 0.0 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 19, macros: 6, pointers: 6, import: 5
- `include/uapi/linux/gpib_ioctl.h` (C) | Magnitude: 72.64 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 92, args: 38, state_mutation: 38, core_var_decl: 38
- `drivers/gpu/drm/nouveau/nvkm/subdev/devinit/fbmem.h` (C) | Magnitude: 14.22 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: macros: 17, structural_boundaries: 12, indent_tabs: 12, pointers: 11
- `arch/x86/events/intel/pt.h` (C) | Magnitude: 9.9 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 44, structural_boundaries: 20, class_start: 13, api: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `include/uapi/linux/io_uring/mock_file.h` (C) | Magnitude: 17.74 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 19, structural_boundaries: 7, class_start: 7, core_var_decl: 3
- `drivers/pinctrl/intel/pinctrl-cedarfork.c` (C) | Magnitude: 8.56 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 269, structural_boundaries: 11, encapsulation: 9, globals: 7
- `arch/x86/include/asm/trap_pf.h` (C) | Magnitude: 25.3 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 9, indent_tabs: 9, core_var_decl: 9, design_upper_case: 9
- `drivers/block/drbd/drbd_protocol.h` (C) | Magnitude: 49.6 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 150, core_var_decl: 57, design_upper_case: 56, structural_boundaries: 32
- `drivers/gpu/drm/msm/disp/dpu1/catalog/dpu_3_0_msm8998.h` (C) | Magnitude: 20.88 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 267, pointers: 23, args: 18, structural_boundaries: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `drivers/gpu/drm/mediatek/mtk_disp_rdma.c` (C) | Magnitude: 169.62 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 172, pointers: 137, structural_boundaries: 96, macros: 36
- `sound/soc/codecs/arizona.c` (C) | Magnitude: 1834.2 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 1782, pointers: 654, structural_boundaries: 425, branch: 398
- `drivers/parport/parport_pc.c` (C) | Magnitude: 2395.42 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 1936, pointers: 574, branch: 475, state_mutation: 415
- `drivers/phy/broadcom/phy-brcm-usb.c` (C) | Magnitude: 384.38 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 437, pointers: 306, structural_boundaries: 138, branch: 88
- `Documentation/sphinx/kerneldoc.py` (PYTHON) | Magnitude: 218.14 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 147, state_mutation: 60, core_var_decl: 49, design_snake_case: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tools/testing/kunit/run_checks.py` (PYTHON) | Magnitude: 0.06 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 40, structural_boundaries: 15, branch: 12, state_mutation: 10
- `drivers/gpu/drm/nova/driver.rs` (RUST) | Magnitude: 11.84 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 15, generics: 9, core_var_decl: 7
- `rust/syn/attr.rs` (RUST) | Magnitude: 208.14 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 395, indent_spaces: 351, structural_boundaries: 85, branch: 63

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `drivers/pwm/pwm-stm32-lp.c` (C) | Magnitude: 389.52 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 253, pointers: 118, branch: 71, structural_boundaries: 70
- `drivers/usb/dwc2/drd.c` (C) | Magnitude: 223.86 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 141, branch: 67, pointers: 59, structural_boundaries: 37
- `drivers/scsi/gvp11.c` (C) | Magnitude: 370.86 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 263, pointers: 185, state_mutation: 86, structural_boundaries: 59
- `tools/testing/selftests/kvm/get-reg-list.c` (C) | Magnitude: 0.33 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 222, pointers: 79, structural_boundaries: 74, state_mutation: 71
- `drivers/video/fbdev/omap2/omapfb/omapfb-ioctl.c` (C) | Magnitude: 821.38 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 626, pointers: 311, structural_boundaries: 198, branch: 165

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tools/testing/selftests/damon/drgn_dump_damon_status.py` (PYTHON) | Magnitude: 0.16 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 163, structural_boundaries: 53, state_mutation: 28, args: 20
- `arch/x86/boot/bitops.h` (C) | Magnitude: 7.52 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 9, indent_tabs: 7, pointers: 6, macros: 4
- `arch/powerpc/kexec/core_32.c` (C) | Magnitude: 18.34 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 23, structural_boundaries: 8, pointers: 8, import: 7
- `drivers/scsi/lpfc/lpfc_compat.h` (C) | Magnitude: 54.5 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 25, structural_boundaries: 14, pointers: 14, state_mutation: 13
- `tools/testing/selftests/ftrace/test.d/ftrace/tracing-error-log.tc` (SHELL) | Magnitude: 0.01 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: io: 4, branch: 3, indent_spaces: 2, structural_boundaries: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `fs/hpfs/dnode.c` (C) | Magnitude: 1279.36 | Delta: **0.167** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 895, pointers: 589, branch: 233, state_mutation: 233

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `drivers/usb/serial/usb_wwan.c` (C) | Magnitude: 583.4 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 410, pointers: 281, state_mutation: 126, structural_boundaries: 116
- `drivers/gpu/drm/i915/selftests/i915_syncmap.c` (C) | Magnitude: 495.8 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 354, pointers: 145, state_mutation: 102, branch: 78
- `arch/arm64/kvm/hyp/vgic-v2-cpuif-proxy.c` (C) | Magnitude: 43.3 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 40, structural_boundaries: 13, pointers: 12, branch: 10
- `drivers/mfd/viperboard.c` (C) | Magnitude: 42.06 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 56, pointers: 35, structural_boundaries: 12, state_mutation: 9
- `tools/testing/selftests/bpf/prog_tests/pe_preserve_elems.c` (C) | Magnitude: 0.04 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 35, structural_boundaries: 17, pointers: 12, branch: 8

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `net/bluetooth/l2cap_core.c` -> Churn: **76.75%** | Cog Load: 76.7343% | Debt: 11.0092%
- `kernel/bpf/verifier.c` -> Churn: **75.4%** | Cog Load: 95.1797% | Debt: 8.819%
- `kernel/cgroup/cpuset.c` -> Churn: **75.4%** | Cog Load: 72.8557% | Debt: 33.2978%
- `Makefile` -> Churn: **72.76%** | Cog Load: 56.5106% | Debt: 21.7835%
- `net/netfilter/nf_tables_api.c` -> Churn: **72.76%** | Cog Load: 73.4469% | Debt: 8.6611%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `drivers/scsi/lpfc/lpfc_sli.c` -> **Linus Torvalds** (100.0% isolated ownership) | Magnitude: 14767.74
- `net/mac80211/mlme.c` -> **Ariel Silver** (100.0% isolated ownership) | Magnitude: 9230.66
- `drivers/scsi/lpfc/lpfc_els.c` -> **Linus Torvalds** (100.0% isolated ownership) | Magnitude: 8561.86
- `drivers/md/raid5.c` -> **Linus Torvalds** (100.0% isolated ownership) | Magnitude: 8166.54
- `drivers/scsi/scsi_debug.c` -> **Linus Torvalds** (100.0% isolated ownership) | Magnitude: 7971.52

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tools/include/linux/compiler.h` -> **Severity: 1157.8** (Blast Radius: 11.578 * Doc Risk: 100.0%)
- `tools/testing/selftests/bpf/progs/lru_bug.c` -> **Severity: 956.4** (Blast Radius: 9.564 * Doc Risk: 100.0%)
- `tools/lib/bpf/bpf_helpers.h` -> **Severity: 574.9** (Blast Radius: 5.749 * Doc Risk: 100.0%)
- `arch/powerpc/boot/io.h` -> **Severity: 428.7** (Blast Radius: 4.287 * Doc Risk: 100.0%)
- `tools/testing/selftests/drivers/net/hw/ncdevmem.c` -> **Severity: 262.5** (Blast Radius: 2.625 * Doc Risk: 100.0%)

- **Mainframe skeleton completeness:** n/a (no channel has facts) (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: none.

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 30572 literal sites + 785 sites through wrappers = 31357
- **`memory_alloc`:** 6256 literal sites + 17764 sites through wrappers = 24020
- **`panics_and_aborts`:** 28106 literal sites + 724 sites through wrappers = 28830

- `free` (macro, memory_alloc, via kvfree): 3014 call sites in 720 files -- `lib/inflate.c`
- `kmalloc_obj` (macro, memory_alloc, primitive): 1850 call sites in 1187 files -- `lib/decompress_unxz.c`
- `kvfree` (function, memory_alloc, via vfree): 1426 call sites in 540 files -- `mm/slub.c`
- `vfree` (macro, memory_alloc, primitive): 984 call sites in 415 files -- `lib/decompress_unxz.c`
- `strdup` (function, memory_alloc, primitive): 639 call sites in 190 files -- `tools/include/nolibc/string.h`
- `zfree` (macro, memory_alloc, primitive): 615 call sites in 122 files -- `tools/include/linux/zalloc.h`
- `release_firmware` (function, memory_alloc, via firmware_free_data): 603 call sites in 334 files -- `drivers/base/firmware_loader/main.c`
- `mempool_free` (function, memory_alloc, primitive): 465 call sites in 111 files -- `mm/mempool.c`
- `sock_put` (function, memory_alloc, via sk_free): 392 call sites in 118 files -- `include/net/sock.h`
- `vmalloc` (macro, memory_alloc, primitive): 297 call sites in 197 files -- `arch/um/include/shared/um_malloc.h`
- `vdo_free` (function, memory_alloc, via vfree): 175 call sites in 37 files -- `drivers/md/dm-vdo/memory-alloc.c`
- `bio_put` (function, memory_alloc, via bio_free): 169 call sites in 74 files -- `block/bio.c`
*(+1706 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2961483 call pairs -- scoped 23.1%, unique 23.5%, ambiguous 17.7%, external 35.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 2886746 | 22.8% | 23.9% | 17.9% | 35.4% |
| shell | 33049 | 34.1% | 16.5% | 6.9% | 42.5% |
| python | 19693 | 32.8% | 0.0% | 18.1% | 49.0% |
| rust | 18327 | 29.4% | 0.0% | 16.3% | 54.3% |
| perl | 1812 | 36.7% | 0.0% | 0.6% | 62.7% |
| cpp | 655 | 19.8% | 10.5% | 7.6% | 62.0% |
| yacc | 526 | 1.5% | 30.6% | 20.7% | 47.1% |
| makefile | 361 | 0.0% | 0.0% | 0.0% | 100.0% |
| assembly | 307 | 2.9% | 54.1% | 22.5% | 20.5% |
| ruby | 4 | 0.0% | 0.0% | 0.0% | 100.0% |

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
