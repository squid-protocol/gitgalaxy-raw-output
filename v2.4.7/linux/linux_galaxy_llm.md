# ARCHITECTURAL_BRIEF: linux
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/OS/linux` |
| **Timestamp** | `2026-08-07T03:41:41.102439+00:00` |
| **Scan Duration** | `387.42s` |
| **Git Branch** | `master` |
| **Git Commit** | `3aae9383f42f687221c011d7ee87529398e826b3` |
| **Git Remote** | `https://github.com/torvalds/linux.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 71397 malicious artifacts.

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
| Total Artifacts | 93011 |
| Analyzed Artifacts (Scanned) | 80153 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 12858 |
| Total LOC | 20333319 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 86.2% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.035 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 5505 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 66137 | 18980562 | 82.5% |
| YAML | 5400 | 459244 | 6.7% |
| MAKEFILE | 3239 | 63188 | 4.0% |
| SHELL | 1311 | 151557 | 1.6% |
| PLAINTEXT | 1126 | 3 | 1.4% |
| JSON | 963 | 298036 | 1.2% |
| ASSEMBLY | 931 | 228382 | 1.2% |
| PYTHON | 357 | 74236 | 0.4% |
| RUST | 325 | 51349 | 0.4% |
| XML | 198 | 6 | 0.2% |
| MARKDOWN | 68 | 0 | 0.1% |
| PERL | 55 | 22219 | 0.1% |
| CSV | 10 | 286 | 0.0% |
| YACC | 10 | 1834 | 0.0% |
| CPP | 9 | 1757 | 0.0% |
| M4 | 5 | 324 | 0.0% |
| CSS | 3 | 125 | 0.0% |
| HTML | 2 | 24 | 0.0% |
| PHP | 2 | 128 | 0.0% |
| RUBY | 1 | 24 | 0.0% |
| MATLAB | 1 | 35 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.203`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 55351 | 69.1% |
| file_cluster_13 | 20074 | 25.0% |
| file_cluster_9 | 2445 | 3.1% |
| file_cluster_17 | 371 | 0.5% |
| file_cluster_12 | 220 | 0.3% |
| file_cluster_4 | 158 | 0.2% |
| file_cluster_0 | 130 | 0.2% |
| file_cluster_16 | 98 | 0.1% |
| file_cluster_11 | 83 | 0.1% |
| file_cluster_6 | 14 | 0.0% |
| file_cluster_2 | 6 | 0.0% |
| file_cluster_7 | 5 | 0.0% |
| Unknown | 3 | 0.0% |
| file_cluster_1 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1191 | 1.5% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 12858*

**Composition by Extension & Reason:**
- `no_extension`: 2987x Unsupported Format (.undeterminable), 727x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 198x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)
- `.rst`: 3807x Excluded (Unsupported Extension: '.rst'), 75x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 1328x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Embedded Hex Payload: 3795 hex tokens in 603 LOC), 2x Excluded (Machine-Generated Source Code Signature: 328 LOC)
- `.h`: 530x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 32x Excluded (Machine-Generated Source Code Signature: 62 LOC), 28x Excluded (Machine-Generated Source Code Signature: 835 LOC)
- `.s`: 443x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1130 LOC)
- `.dtso`: 229x Excluded (Unsupported Extension: '.dtso'), 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pkt`: 158x Unsupported Format (.pkt)
- `.j2`: 149x Unsupported Format (.j2)
- `.cocci`: 76x Unsupported Format (.cocci)
- `.yaml`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Machine-Generated Source Code Signature: 42 LOC), 2x Excluded (Machine-Generated Source Code Signature: 78 LOC)
- `.bconf`: 44x Unsupported Format (.bconf), 5x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.json`: 2x Excluded (Massive Static Asset Blob: 3447 LOC), 2x Excluded (Massive Static Asset Blob: 4954 LOC), 2x Excluded (Massive Static Asset Blob: 7627 LOC)
- `.litmus`: 35x Unsupported Format (.litmus), 12x Excluded (Unsupported Extension: '.litmus')
- `.txt`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 77 LOC), 1x Excluded (Machine-Generated Source Code Signature: 46 LOC)
- `.boot`: 34x Unsupported Format (.boot)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 37.3 | 28.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 55.3 | 76.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 12.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 23.0 | 2.3 | 2.3 |
| API Exposure | 0.0 | 19.9 | 7.2 | 8.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 55.5 | 98.2 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 93.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 16.8 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 59.7 | 73.4 | 100.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tools/testing/selftests/cgroup/test_cpuset_prs.sh` (Hits: 477)
- `tools/testing/selftests/net/openvswitch/openvswitch.sh` (Hits: 363)
- `tools/testing/selftests/net/fib_tests.sh` (Hits: 345)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **stdlib.h** (`tools/include/nolibc/stdlib.h`) — 1253 inbound connections
2. **test_progs.h** (`tools/testing/selftests/bpf/test_progs.h`) — 421 inbound connections
3. **amdgpu.h** (`drivers/gpu/drm/amd/amdgpu/amdgpu.h`) — 387 inbound connections
4. **bpf_misc.h** (`tools/testing/selftests/bpf/progs/bpf_misc.h`) — 304 inbound connections
5. **inttypes.h** (`tools/include/nolibc/inttypes.h`) — 238 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **gaudi2_regs.h** (`drivers/accel/habanalabs/include/gaudi2/asic_reg/gaudi2_regs.h`) — 158 outbound dependencies
2. **verifier.c** (`tools/testing/selftests/bpf/prog_tests/verifier.c`) — 113 outbound dependencies
3. **intel_display.c** (`drivers/gpu/drm/i915/display/intel_display.c`) — 108 outbound dependencies
4. **expr.rs** (`rust/syn/expr.rs`) — 107 outbound dependencies
5. **fork.c** (`kernel/fork.c`) — 105 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `wm5110_readable_register` (@ `drivers/mfd/wm5110-tables.c`) -> Impact: **2026.4** | LOC: 1142
- `check_func_arg` (@ `kernel/bpf/verifier.c`) -> Impact: **1791.3** | LOC: 1779
- `hidinput_configure_usage` (@ `drivers/hid/hid-input.c`) -> Impact: **1750.5** | LOC: 798
- `xfs_bmap_add_extent_unwritten_real` (@ `fs/xfs/libxfs/xfs_bmap.c`) -> Impact: **1711.2** | LOC: 2150
- `Anonymous_Block_[Truncated]` (@ `tools/testing/selftests/net/mptcp/mptcp_join.sh`) -> Impact: **1686.6** | LOC: 3354
- `SiS_GetVCLK2Ptr` (@ `drivers/video/fbdev/sis/init301.c`) -> Impact: **1640.2** | LOC: 1722
- `read_log_page` (@ `fs/ntfs3/fslog.c`) -> Impact: **1636.8** | LOC: 2326
- `ethtool_virtdev_set_link_ksettings` (@ `net/ethtool/ioctl.c`) -> Impact: **1580.5** | LOC: 2093
- `ieee80211_put_preq_ies_band` (@ `net/mac80211/util.c`) -> Impact: **1554.9** | LOC: 2069
- `process_iter_arg` (@ `kernel/bpf/verifier.c`) -> Impact: **1549.3** | LOC: 1873

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `sound/soc/codecs` | 673 | 294569.27 | 38.93% | 1.93% |
| `drivers/gpu/drm/amd/amdgpu` | 616 | 247077.88 | 38.32% | 16.35% |
| `drivers/clk/qcom` | 217 | 238107.33 | 41.75% | 0.57% |
| `include/linux` | 1495 | 158980.68 | 16.14% | 4.41% |
| `drivers/hwmon` | 240 | 143830.62 | 71.16% | 17.34% |
| `drivers/media/dvb-frontends` | 286 | 137254.4 | 39.95% | 5.61% |
| `drivers/scsi` | 167 | 136285.54 | 55.25% | 15.14% |
| `arch/arm64/boot/dts/qcom` | 529 | 129764.36 | 39.56% | 0.92% |
| `drivers/net/wireless/realtek/rtw89` | 89 | 126476.28 | 36.66% | 4.9% |
| `mm` | 142 | 122630.52 | 63.65% | 37.98% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `arch/um/kernel/skas/Makefile` -> **100.0%** Exposure
- `arch/xtensa/kernel/Makefile` -> **100.0%** Exposure
- `Documentation/admin-guide/aoe/autoload.sh` -> **100.0%** Exposure
- `Documentation/firmware_class/hotplug-script` -> **100.0%** Exposure
- `arch/arm/boot/install.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `arch/arc/Makefile` -> **100.0%** Exposure
- `arch/arc/plat-tb10x/Makefile` -> **100.0%** Exposure
- `arch/arm/boot/compressed/Makefile` -> **100.0%** Exposure
- `arch/arm/boot/dts/Makefile` -> **100.0%** Exposure
- `arch/arm/boot/dts/intel/Makefile` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `arch/m68k/ifpsp060/src/fpsp.S` -> **235** Orphaned Functions | **0** Duplicates
- `arch/m68k/ifpsp060/src/itest.S` -> **227** Orphaned Functions | **0** Duplicates
- `drivers/net/ethernet/aquantia/atlantic/hw_atl/hw_atl_llh.c` -> **219** Orphaned Functions | **0** Duplicates
- `sound/pci/asihpi/hpifunc.c` -> **194** Orphaned Functions | **0** Duplicates
- `drivers/gpu/drm/amd/display/dc/core/dc_hw_sequencer.c` -> **170** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`Documentation/usb/usbdevfs-drop-permissions.c`** -> AI Confidence: **99.48%**
2. **`arch/alpha/boot/tools/objstrip.c`** -> AI Confidence: **99.48%**
3. **`arch/alpha/kernel/irq_alpha.c`** -> AI Confidence: **99.48%**
4. **`arch/alpha/math-emu/math.c`** -> AI Confidence: **99.48%**
5. **`arch/arc/include/asm/atomic.h`** -> AI Confidence: **99.48%**
6. **`arch/arc/kernel/signal.c`** -> AI Confidence: **99.48%**
7. **`arch/arc/kernel/unwind.c`** -> AI Confidence: **99.48%**
8. **`arch/arc/mm/fault.c`** -> AI Confidence: **99.48%**
9. **`arch/arm/boot/dts/allwinner/sun4i-a10-dserve-dsrv9703c.dts`** -> AI Confidence: **99.48%**
10. **`arch/arm/boot/dts/allwinner/sun4i-a10-inet1.dts`** -> AI Confidence: **99.48%**
11. **`arch/arm/boot/dts/allwinner/sun4i-a10-pov-protab2-ips9.dts`** -> AI Confidence: **99.48%**
12. **`arch/arm/boot/dts/allwinner/sun4i-a10-topwise-a721.dts`** -> AI Confidence: **99.48%**
13. **`arch/arm/boot/dts/allwinner/sun5i-a13-empire-electronix-d709.dts`** -> AI Confidence: **99.48%**
14. **`arch/arm/boot/dts/allwinner/sun5i-a13-pocketbook-614-plus.dts`** -> AI Confidence: **99.48%**
15. **`arch/arm/boot/dts/allwinner/sun5i-a13-pocketbook-touch-lux-3.dts`** -> AI Confidence: **99.48%**
16. **`arch/arm/boot/dts/allwinner/sun7i-a20-wexler-tab7200.dts`** -> AI Confidence: **99.48%**
17. **`arch/arm/boot/dts/aspeed/aspeed-bmc-asrock-e3c256d4i.dts`** -> AI Confidence: **99.48%**
18. **`arch/arm/boot/dts/aspeed/aspeed-bmc-facebook-bletchley.dts`** -> AI Confidence: **99.48%**
19. **`arch/arm/boot/dts/aspeed/aspeed-bmc-facebook-catalina.dts`** -> AI Confidence: **99.48%**
20. **`arch/arm/boot/dts/aspeed/aspeed-bmc-facebook-clemente.dts`** -> AI Confidence: **99.48%**
21. **`arch/arm/boot/dts/aspeed/aspeed-bmc-ibm-sbp1.dts`** -> AI Confidence: **99.48%**
22. **`arch/arm/boot/dts/mediatek/mt7629.dtsi`** -> AI Confidence: **99.48%**
23. **`arch/arm/boot/dts/microchip/at91-sama5d2_xplained.dts`** -> AI Confidence: **99.48%**
24. **`arch/arm/boot/dts/microchip/at91-sama7g5ek.dts`** -> AI Confidence: **99.48%**
25. **`arch/arm/boot/dts/nvidia/tegra20-acer-a500-picasso.dts`** -> AI Confidence: **99.48%**
26. **`arch/arm/boot/dts/nvidia/tegra30-pegatron-chagall.dts`** -> AI Confidence: **99.48%**
27. **`arch/arm/boot/dts/nxp/imx/imx6dl-prtmvt.dts`** -> AI Confidence: **99.48%**
28. **`arch/arm/boot/dts/qcom/qcom-apq8060-dragonboard.dts`** -> AI Confidence: **99.48%**
29. **`arch/arm/boot/dts/qcom/qcom-apq8064-asus-nexus7-flo.dts`** -> AI Confidence: **99.48%**
30. **`arch/arm/boot/dts/qcom/qcom-apq8064-ifc6410.dts`** -> AI Confidence: **99.48%**
31. **`arch/arm/boot/dts/qcom/qcom-apq8064-lg-nexus4-mako.dts`** -> AI Confidence: **99.48%**
32. **`arch/arm/boot/dts/qcom/qcom-apq8064-sony-xperia-lagan-yuga.dts`** -> AI Confidence: **99.48%**
33. **`arch/arm/boot/dts/qcom/qcom-apq8074-dragonboard.dts`** -> AI Confidence: **99.48%**
34. **`arch/arm/boot/dts/qcom/qcom-msm8960-samsung-expressatt.dts`** -> AI Confidence: **99.48%**
35. **`arch/arm/boot/dts/qcom/qcom-msm8960-sony-huashan.dts`** -> AI Confidence: **99.48%**
36. **`arch/arm/boot/dts/qcom/qcom-msm8974-lge-nexus5-hammerhead.dts`** -> AI Confidence: **99.48%**
37. **`arch/arm/boot/dts/qcom/qcom-msm8974-samsung-hlte.dts`** -> AI Confidence: **99.48%**
38. **`arch/arm/boot/dts/qcom/qcom-msm8974pro-fairphone-fp2.dts`** -> AI Confidence: **99.48%**
39. **`arch/arm/boot/dts/samsung/exynos4412-itop-scp-core.dtsi`** -> AI Confidence: **99.48%**
40. **`arch/arm/boot/dts/samsung/exynos4412-p4note.dtsi`** -> AI Confidence: **99.48%**
41. **`arch/arm/boot/dts/samsung/exynos5250-arndale.dts`** -> AI Confidence: **99.48%**
42. **`arch/arm/boot/dts/samsung/exynos5250-spring.dts`** -> AI Confidence: **99.48%**
43. **`arch/arm/boot/dts/samsung/exynos5410-odroidxu.dts`** -> AI Confidence: **99.48%**
44. **`arch/arm/boot/dts/samsung/exynos5420-arndale-octa.dts`** -> AI Confidence: **99.48%**
45. **`arch/arm/boot/dts/samsung/exynos5420-peach-pit.dts`** -> AI Confidence: **99.48%**
46. **`arch/arm/boot/dts/samsung/exynos5800-peach-pi.dts`** -> AI Confidence: **99.48%**
47. **`arch/arm/boot/dts/st/ste-ux500-samsung-codina-tmo.dts`** -> AI Confidence: **99.48%**
48. **`arch/arm/boot/dts/st/ste-ux500-samsung-codina.dts`** -> AI Confidence: **99.48%**
49. **`arch/arm/boot/dts/st/ste-ux500-samsung-gavini.dts`** -> AI Confidence: **99.48%**
50. **`arch/arm/boot/dts/st/ste-ux500-samsung-golden.dts`** -> AI Confidence: **99.48%**
51. **`arch/arm/boot/dts/st/ste-ux500-samsung-janice.dts`** -> AI Confidence: **99.48%**
52. **`arch/arm/boot/dts/st/ste-ux500-samsung-kyle.dts`** -> AI Confidence: **99.48%**
53. **`arch/arm/boot/dts/st/ste-ux500-samsung-skomer.dts`** -> AI Confidence: **99.48%**
54. **`arch/arm/boot/dts/st/stm32mp133c-prihmb.dts`** -> AI Confidence: **99.48%**
55. **`arch/arm/boot/dts/st/stm32mp135f-dk.dts`** -> AI Confidence: **99.48%**
56. **`arch/arm/boot/dts/st/stm32mp13xx-dhcor-som.dtsi`** -> AI Confidence: **99.48%**
57. **`arch/arm/boot/dts/st/stm32mp151c-mecio1r0.dts`** -> AI Confidence: **99.48%**
58. **`arch/arm/boot/dts/st/stm32mp151c-mect1s.dts`** -> AI Confidence: **99.48%**
59. **`arch/arm/boot/dts/st/stm32mp151c-plyaqm.dts`** -> AI Confidence: **99.48%**
60. **`arch/arm/boot/dts/st/stm32mp153c-mecio1r1.dts`** -> AI Confidence: **99.48%**
61. **`arch/arm/boot/dts/st/stm32mp157c-emstamp-argon.dtsi`** -> AI Confidence: **99.48%**
62. **`arch/arm/boot/dts/st/stm32mp157c-odyssey-som.dtsi`** -> AI Confidence: **99.48%**
63. **`arch/arm/boot/dts/st/stm32mp157c-phycore-stm32mp15-som.dtsi`** -> AI Confidence: **99.48%**
64. **`arch/arm/boot/dts/st/stm32mp157c-ultra-fly-sbc.dts`** -> AI Confidence: **99.48%**
65. **`arch/arm/boot/dts/ti/omap/am571x-idk.dts`** -> AI Confidence: **99.48%**
66. **`arch/arm/boot/dts/ti/omap/am5729-beagleboneai.dts`** -> AI Confidence: **99.48%**
67. **`arch/arm/include/asm/assembler.h`** -> AI Confidence: **99.48%**
68. **`arch/arm/mach-footbridge/isa-irq.c`** -> AI Confidence: **99.48%**
69. **`arch/arm/mach-imx/hardware.h`** -> AI Confidence: **99.48%**
70. **`arch/arm/mm/pgd.c`** -> AI Confidence: **99.48%**
71. **`arch/arm64/boot/dts/allwinner/sun50i-a64-pinebook.dts`** -> AI Confidence: **99.48%**
72. **`arch/arm64/boot/dts/exynos/exynosautov9.dtsi`** -> AI Confidence: **99.48%**
73. **`arch/arm64/boot/dts/freescale/imx8mp-hummingboard-pro.dts`** -> AI Confidence: **99.48%**
74. **`arch/arm64/boot/dts/freescale/imx8mp-hummingboard-pulse.dts`** -> AI Confidence: **99.48%**
75. **`arch/arm64/boot/dts/hisilicon/hi6220.dtsi`** -> AI Confidence: **99.48%**
76. **`arch/arm64/boot/dts/mediatek/mt8195-demo.dts`** -> AI Confidence: **99.48%**
77. **`arch/arm64/boot/dts/mediatek/mt8395-kontron-3-5-sbc-i1200.dts`** -> AI Confidence: **99.48%**
78. **`arch/arm64/boot/dts/mediatek/mt8395-radxa-nio-12l.dts`** -> AI Confidence: **99.48%**
79. **`arch/arm64/boot/dts/qcom/apq8016-sbc.dts`** -> AI Confidence: **99.48%**
80. **`arch/arm64/boot/dts/qcom/apq8016-schneider-hmibsc.dts`** -> AI Confidence: **99.48%**
81. **`arch/arm64/boot/dts/qcom/apq8039-t2.dts`** -> AI Confidence: **99.48%**
82. **`arch/arm64/boot/dts/qcom/apq8096-db820c.dts`** -> AI Confidence: **99.48%**
83. **`arch/arm64/boot/dts/qcom/apq8096-ifc6640.dts`** -> AI Confidence: **99.48%**
84. **`arch/arm64/boot/dts/qcom/lemans-evk.dts`** -> AI Confidence: **99.48%**
85. **`arch/arm64/boot/dts/qcom/milos-fairphone-fp6.dts`** -> AI Confidence: **99.48%**
86. **`arch/arm64/boot/dts/qcom/milos.dtsi`** -> AI Confidence: **99.48%**
87. **`arch/arm64/boot/dts/qcom/monaco-evk.dts`** -> AI Confidence: **99.48%**
88. **`arch/arm64/boot/dts/qcom/msm8916-longcheer-l8910.dts`** -> AI Confidence: **99.48%**
89. **`arch/arm64/boot/dts/qcom/msm8917.dtsi`** -> AI Confidence: **99.48%**
90. **`arch/arm64/boot/dts/qcom/msm8937-xiaomi-land.dts`** -> AI Confidence: **99.48%**
91. **`arch/arm64/boot/dts/qcom/msm8937.dtsi`** -> AI Confidence: **99.48%**
92. **`arch/arm64/boot/dts/qcom/msm8939-longcheer-l9100.dts`** -> AI Confidence: **99.48%**
93. **`arch/arm64/boot/dts/qcom/msm8939-sony-xperia-kanuti-tulip.dts`** -> AI Confidence: **99.48%**
94. **`arch/arm64/boot/dts/qcom/msm8996-xiaomi-gemini.dts`** -> AI Confidence: **99.48%**
95. **`arch/arm64/boot/dts/qcom/msm8996pro-xiaomi-scorpio.dts`** -> AI Confidence: **99.48%**
96. **`arch/arm64/boot/dts/qcom/msm8998-fxtec-pro1.dts`** -> AI Confidence: **99.48%**
97. **`arch/arm64/boot/dts/qcom/msm8998-xiaomi-sagit.dts`** -> AI Confidence: **99.48%**
98. **`arch/arm64/boot/dts/qcom/qcm6490-fairphone-fp5.dts`** -> AI Confidence: **99.48%**
99. **`arch/arm64/boot/dts/qcom/qcm6490-idp.dts`** -> AI Confidence: **99.48%**
100. **`arch/arm64/boot/dts/qcom/qcm6490-particle-tachyon.dts`** -> AI Confidence: **99.48%**
101. **`arch/arm64/boot/dts/qcom/qcm6490-shift-otter.dts`** -> AI Confidence: **99.48%**
102. **`arch/arm64/boot/dts/qcom/qcs6490-radxa-dragon-q6a.dts`** -> AI Confidence: **99.48%**
103. **`arch/arm64/boot/dts/qcom/qcs6490-rb3gen2.dts`** -> AI Confidence: **99.48%**
104. **`arch/arm64/boot/dts/qcom/qcs6490-thundercomm-rubikpi3.dts`** -> AI Confidence: **99.48%**
105. **`arch/arm64/boot/dts/qcom/qcs8550-aim300.dtsi`** -> AI Confidence: **99.48%**
106. **`arch/arm64/boot/dts/qcom/qrb4210-rb2.dts`** -> AI Confidence: **99.48%**
107. **`arch/arm64/boot/dts/qcom/qrb5165-rb5.dts`** -> AI Confidence: **99.48%**
108. **`arch/arm64/boot/dts/qcom/sa8295p-adp.dts`** -> AI Confidence: **99.48%**
109. **`arch/arm64/boot/dts/qcom/sar2130p.dtsi`** -> AI Confidence: **99.48%**
110. **`arch/arm64/boot/dts/qcom/sc7180-acer-aspire1.dts`** -> AI Confidence: **99.48%**
111. **`arch/arm64/boot/dts/qcom/sc7180-idp.dts`** -> AI Confidence: **99.48%**
112. **`arch/arm64/boot/dts/qcom/sc8180x-lenovo-flex-5g.dts`** -> AI Confidence: **99.48%**
113. **`arch/arm64/boot/dts/qcom/sc8180x-primus.dts`** -> AI Confidence: **99.48%**
114. **`arch/arm64/boot/dts/qcom/sc8280xp-huawei-gaokun3.dts`** -> AI Confidence: **99.48%**
115. **`arch/arm64/boot/dts/qcom/sc8280xp-lenovo-thinkpad-x13s.dts`** -> AI Confidence: **99.48%**
116. **`arch/arm64/boot/dts/qcom/sc8280xp-microsoft-blackrock.dts`** -> AI Confidence: **99.48%**
117. **`arch/arm64/boot/dts/qcom/sdm670-google-sargo.dts`** -> AI Confidence: **99.48%**
118. **`arch/arm64/boot/dts/qcom/sdm670.dtsi`** -> AI Confidence: **99.48%**
119. **`arch/arm64/boot/dts/qcom/sdm845-db845c.dts`** -> AI Confidence: **99.48%**
120. **`arch/arm64/boot/dts/qcom/sdm845-samsung-starqltechn.dts`** -> AI Confidence: **99.48%**
121. **`arch/arm64/boot/dts/qcom/sdm845-shift-axolotl.dts`** -> AI Confidence: **99.48%**
122. **`arch/arm64/boot/dts/qcom/sdm845-xiaomi-polaris.dts`** -> AI Confidence: **99.48%**
123. **`arch/arm64/boot/dts/qcom/sdm850-huawei-matebook-e-2019.dts`** -> AI Confidence: **99.48%**
124. **`arch/arm64/boot/dts/qcom/sdm850-lenovo-yoga-c630.dts`** -> AI Confidence: **99.48%**
125. **`arch/arm64/boot/dts/qcom/sdm850-samsung-w737.dts`** -> AI Confidence: **99.48%**
126. **`arch/arm64/boot/dts/qcom/sdx75.dtsi`** -> AI Confidence: **99.48%**
127. **`arch/arm64/boot/dts/qcom/sm4450.dtsi`** -> AI Confidence: **99.48%**
128. **`arch/arm64/boot/dts/qcom/sm6115-fxtec-pro1x.dts`** -> AI Confidence: **99.48%**
129. **`arch/arm64/boot/dts/qcom/sm6125-xiaomi-ginkgo.dts`** -> AI Confidence: **99.48%**
130. **`arch/arm64/boot/dts/qcom/sm6375.dtsi`** -> AI Confidence: **99.48%**
131. **`arch/arm64/boot/dts/qcom/sm7225-fairphone-fp4.dts`** -> AI Confidence: **99.48%**
132. **`arch/arm64/boot/dts/qcom/sm7325-nothing-spacewar.dts`** -> AI Confidence: **99.48%**
133. **`arch/arm64/boot/dts/qcom/sm8150-hdk.dts`** -> AI Confidence: **99.48%**
134. **`arch/arm64/boot/dts/qcom/sm8150-microsoft-surface-duo.dts`** -> AI Confidence: **99.48%**
135. **`arch/arm64/boot/dts/qcom/sm8250-mtp.dts`** -> AI Confidence: **99.48%**
136. **`arch/arm64/boot/dts/qcom/sm8250-xiaomi-pipa.dts`** -> AI Confidence: **99.48%**
137. **`arch/arm64/boot/dts/qcom/sm8350-hdk.dts`** -> AI Confidence: **99.48%**
138. **`arch/arm64/boot/dts/qcom/sm8450-hdk.dts`** -> AI Confidence: **99.48%**
139. **`arch/arm64/boot/dts/qcom/sm8450-qrd.dts`** -> AI Confidence: **99.48%**
140. **`arch/arm64/boot/dts/qcom/sm8550-hdk.dts`** -> AI Confidence: **99.48%**
141. **`arch/arm64/boot/dts/qcom/sm8550-mtp.dts`** -> AI Confidence: **99.48%**
142. **`arch/arm64/boot/dts/qcom/sm8550-qrd.dts`** -> AI Confidence: **99.48%**
143. **`arch/arm64/boot/dts/qcom/sm8550-samsung-q5q.dts`** -> AI Confidence: **99.48%**
144. **`arch/arm64/boot/dts/qcom/sm8550-sony-xperia-yodo-pdx234.dts`** -> AI Confidence: **99.48%**
145. **`arch/arm64/boot/dts/qcom/sm8650-hdk.dts`** -> AI Confidence: **99.48%**
146. **`arch/arm64/boot/dts/qcom/sm8650-mtp.dts`** -> AI Confidence: **99.48%**
147. **`arch/arm64/boot/dts/qcom/sm8650-qrd.dts`** -> AI Confidence: **99.48%**
148. **`arch/arm64/boot/dts/qcom/sm8750-mtp.dts`** -> AI Confidence: **99.48%**
149. **`arch/arm64/boot/dts/qcom/sm8750-qrd.dts`** -> AI Confidence: **99.48%**
150. **`arch/arm64/boot/dts/qcom/talos.dtsi`** -> AI Confidence: **99.48%**
151. **`arch/arm64/boot/dts/qcom/x1e80100-asus-vivobook-s15.dts`** -> AI Confidence: **99.48%**
152. **`arch/arm64/boot/dts/qcom/x1e80100-dell-xps13-9345.dts`** -> AI Confidence: **99.48%**
153. **`arch/arm64/boot/dts/qcom/x1p42100-lenovo-thinkbook-16.dts`** -> AI Confidence: **99.48%**
154. **`arch/arm64/boot/dts/renesas/r9a09g047e57-smarc.dts`** -> AI Confidence: **99.48%**
155. **`arch/arm64/boot/dts/rockchip/rk3562.dtsi`** -> AI Confidence: **99.48%**
156. **`arch/arm64/boot/dts/rockchip/rk3566-lckfb-tspi.dts`** -> AI Confidence: **99.48%**
157. **`arch/arm64/boot/dts/rockchip/rk3566-nanopi-r3s.dts`** -> AI Confidence: **99.48%**
158. **`arch/arm64/boot/dts/rockchip/rk3566-powkiddy-x55.dts`** -> AI Confidence: **99.48%**
159. **`arch/arm64/boot/dts/rockchip/rk3568-9tripod-x3568-v4.dts`** -> AI Confidence: **99.48%**
160. **`arch/arm64/boot/dts/rockchip/rk3568-anbernic-rg-ds.dts`** -> AI Confidence: **99.48%**
161. **`arch/arm64/boot/dts/rockchip/rk3568-easepi-r1.dts`** -> AI Confidence: **99.48%**
162. **`arch/arm64/boot/dts/rockchip/rk3568-wolfvision-pf5.dts`** -> AI Confidence: **99.48%**
163. **`arch/arm64/boot/dts/rockchip/rk3576-100ask-dshanpi-a1.dts`** -> AI Confidence: **99.48%**
164. **`arch/arm64/boot/dts/rockchip/rk3576-armsom-sige5.dts`** -> AI Confidence: **99.48%**
165. **`arch/arm64/boot/dts/rockchip/rk3576-evb1-v10.dts`** -> AI Confidence: **99.48%**
166. **`arch/arm64/boot/dts/rockchip/rk3576-nanopi-m5.dts`** -> AI Confidence: **99.48%**
167. **`arch/arm64/boot/dts/rockchip/rk3576-nanopi-r76s.dts`** -> AI Confidence: **99.48%**
168. **`arch/arm64/boot/dts/rockchip/rk3576-roc-pc.dts`** -> AI Confidence: **99.48%**
169. **`arch/arm64/boot/dts/rockchip/rk3576-rock-4d.dts`** -> AI Confidence: **99.48%**
170. **`arch/arm64/boot/dts/rockchip/rk3588-evb1-v10.dts`** -> AI Confidence: **99.48%**
171. **`arch/arm64/boot/dts/rockchip/rk3588-evb2-v10.dts`** -> AI Confidence: **99.48%**
172. **`arch/arm64/boot/dts/rockchip/rk3588-firefly-itx-3588j.dts`** -> AI Confidence: **99.48%**
173. **`arch/arm64/boot/dts/rockchip/rk3588-friendlyelec-cm3588-nas.dts`** -> AI Confidence: **99.48%**
174. **`arch/arm64/boot/dts/rockchip/rk3588-jaguar.dts`** -> AI Confidence: **99.48%**
175. **`arch/arm64/boot/dts/rockchip/rk3588-mnt-reform2.dts`** -> AI Confidence: **99.48%**
176. **`arch/arm64/boot/dts/rockchip/rk3588-roc-rt.dts`** -> AI Confidence: **99.48%**
177. **`arch/arm64/boot/dts/rockchip/rk3588-rock-5-itx.dts`** -> AI Confidence: **99.48%**
178. **`arch/arm64/boot/dts/rockchip/rk3588s-evb1-v10.dts`** -> AI Confidence: **99.48%**
179. **`arch/arm64/boot/dts/rockchip/rk3588s-gameforce-ace.dts`** -> AI Confidence: **99.48%**
180. **`arch/arm64/boot/dts/rockchip/rk3588s-indiedroid-nova.dts`** -> AI Confidence: **99.48%**
181. **`arch/arm64/boot/dts/rockchip/rk3588s-khadas-edge2.dts`** -> AI Confidence: **99.48%**
182. **`arch/arm64/boot/dts/rockchip/rk3588s-odroid-m2.dts`** -> AI Confidence: **99.48%**
183. **`arch/arm64/boot/dts/rockchip/rk3588s-orangepi-cm5-base.dts`** -> AI Confidence: **99.48%**
184. **`arch/arm64/boot/dts/rockchip/rk3588s-roc-pc.dts`** -> AI Confidence: **99.48%**
185. **`arch/arm64/boot/dts/st/stm32mp235f-dk.dts`** -> AI Confidence: **99.48%**
186. **`arch/arm64/boot/dts/st/stm32mp257f-dk.dts`** -> AI Confidence: **99.48%**
187. **`arch/arm64/boot/dts/st/stm32mp257f-ev1.dts`** -> AI Confidence: **99.48%**
188. **`arch/arm64/boot/dts/ti/k3-am62l3-evm.dts`** -> AI Confidence: **99.48%**
189. **`arch/arm64/boot/dts/ti/k3-am62p5-var-som.dtsi`** -> AI Confidence: **99.48%**
190. **`arch/arm64/boot/dts/ti/k3-am642-evm.dts`** -> AI Confidence: **99.48%**
191. **`arch/arm64/boot/dts/ti/k3-am642-phyboard-electra-rdk.dts`** -> AI Confidence: **99.48%**
192. **`arch/arm64/boot/dts/ti/k3-am642-sk.dts`** -> AI Confidence: **99.48%**
193. **`arch/arm64/boot/dts/ti/k3-am642-tqma64xxl-mbax4xxl.dts`** -> AI Confidence: **99.48%**
194. **`arch/arm64/boot/dts/ti/k3-j721e-beagleboneai64.dts`** -> AI Confidence: **99.48%**
195. **`arch/arm64/boot/dts/xilinx/zynqmp-zcu100-revC.dts`** -> AI Confidence: **99.48%**
196. **`arch/arm64/include/asm/assembler.h`** -> AI Confidence: **99.48%**
197. **`arch/arm64/include/asm/lse.h`** -> AI Confidence: **99.48%**
198. **`arch/arm64/include/asm/sysreg.h`** -> AI Confidence: **99.48%**
199. **`arch/loongarch/include/asm/bitops.h`** -> AI Confidence: **99.48%**
200. **`arch/loongarch/include/asm/stackframe.h`** -> AI Confidence: **99.48%**
201. **`arch/loongarch/include/asm/uaccess.h`** -> AI Confidence: **99.48%**
202. **`arch/m68k/include/asm/mcfsim.h`** -> AI Confidence: **99.48%**
203. **`arch/m68k/include/asm/pgtable_mm.h`** -> AI Confidence: **99.48%**
204. **`arch/m68k/kernel/sys_m68k.c`** -> AI Confidence: **99.48%**
205. **`arch/m68k/kernel/uboot.c`** -> AI Confidence: **99.48%**
206. **`arch/m68k/sun3/mmu_emu.c`** -> AI Confidence: **99.48%**
207. **`arch/m68k/sun3x/dvma.c`** -> AI Confidence: **99.48%**
208. **`arch/mips/alchemy/common/time.c`** -> AI Confidence: **99.48%**
209. **`arch/mips/bcm63xx/prom.c`** -> AI Confidence: **99.48%**
210. **`arch/mips/boot/dts/ingenic/ci20.dts`** -> AI Confidence: **99.48%**
211. **`arch/mips/boot/dts/ingenic/gcw0.dts`** -> AI Confidence: **99.48%**
212. **`arch/mips/boot/dts/ingenic/qi_lb60.dts`** -> AI Confidence: **99.48%**
213. **`arch/mips/boot/elf2ecoff.c`** -> AI Confidence: **99.48%**
214. **`arch/mips/boot/tools/relocs_main.c`** -> AI Confidence: **99.48%**
215. **`arch/mips/cavium-octeon/executive/cvmx-helper-rgmii.c`** -> AI Confidence: **99.48%**
216. **`arch/mips/cobalt/irq.c`** -> AI Confidence: **99.48%**
217. **`arch/mips/kernel/branch.c`** -> AI Confidence: **99.48%**
218. **`arch/mips/kernel/cpu-probe.c`** -> AI Confidence: **99.48%**
219. **`arch/mips/kernel/proc.c`** -> AI Confidence: **99.48%**
220. **`arch/mips/kernel/ptrace32.c`** -> AI Confidence: **99.48%**
221. **`arch/mips/kernel/unaligned.c`** -> AI Confidence: **99.48%**
222. **`arch/mips/kvm/emulate.c`** -> AI Confidence: **99.48%**
223. **`arch/mips/loongson64/cop2-ex.c`** -> AI Confidence: **99.48%**
224. **`arch/mips/math-emu/cp1emu.c`** -> AI Confidence: **99.48%**
225. **`arch/mips/mm/page.c`** -> AI Confidence: **99.48%**
226. **`arch/mips/mm/uasm-micromips.c`** -> AI Confidence: **99.48%**
227. **`arch/mips/mti-malta/malta-init.c`** -> AI Confidence: **99.48%**
228. **`arch/mips/net/bpf_jit_comp32.c`** -> AI Confidence: **99.48%**
229. **`arch/mips/net/bpf_jit_comp64.c`** -> AI Confidence: **99.48%**
230. **`arch/mips/sgi-ip22/ip22-setup.c`** -> AI Confidence: **99.48%**
231. **`arch/mips/sibyte/bcm1480/setup.c`** -> AI Confidence: **99.48%**
232. **`arch/mips/sibyte/common/cfe.c`** -> AI Confidence: **99.48%**
233. **`arch/mips/sibyte/sb1250/setup.c`** -> AI Confidence: **99.48%**
234. **`arch/mips/sni/setup.c`** -> AI Confidence: **99.48%**
235. **`arch/mips/tools/elf-entry.c`** -> AI Confidence: **99.48%**
236. **`arch/mips/tools/loongson3-llsc-check.c`** -> AI Confidence: **99.48%**
237. **`arch/openrisc/kernel/sync-timer.c`** -> AI Confidence: **99.48%**
238. **`arch/parisc/include/asm/uaccess.h`** -> AI Confidence: **99.48%**
239. **`arch/parisc/kernel/setup.c`** -> AI Confidence: **99.48%**
240. **`arch/parisc/kernel/unaligned.c`** -> AI Confidence: **99.48%**
241. **`arch/powerpc/boot/4xx.c`** -> AI Confidence: **99.48%**
242. **`arch/powerpc/boot/mktree.c`** -> AI Confidence: **99.48%**
243. **`arch/powerpc/include/asm/ppc_asm.h`** -> AI Confidence: **99.48%**
244. **`arch/powerpc/kexec/ranges.c`** -> AI Confidence: **99.48%**
245. **`arch/powerpc/kvm/book3s_emulate.c`** -> AI Confidence: **99.48%**
246. **`arch/powerpc/kvm/book3s_hv_nestedv2.c`** -> AI Confidence: **99.48%**
247. **`arch/powerpc/kvm/book3s_paired_singles.c`** -> AI Confidence: **99.48%**
248. **`arch/powerpc/kvm/emulate.c`** -> AI Confidence: **99.48%**
249. **`arch/powerpc/math-emu/math.c`** -> AI Confidence: **99.48%**
250. **`arch/powerpc/math-emu/math_efp.c`** -> AI Confidence: **99.48%**
251. **`arch/powerpc/mm/numa.c`** -> AI Confidence: **99.48%**
252. **`arch/powerpc/platforms/52xx/mpc52xx_pic.c`** -> AI Confidence: **99.48%**
253. **`arch/powerpc/platforms/pseries/kexec.c`** -> AI Confidence: **99.48%**
254. **`arch/powerpc/sysdev/cpm2.c`** -> AI Confidence: **99.48%**
255. **`arch/riscv/include/asm/cmpxchg.h`** -> AI Confidence: **99.48%**
256. **`arch/s390/kernel/module.c`** -> AI Confidence: **99.48%**
257. **`arch/sh/include/asm/atomic.h`** -> AI Confidence: **99.48%**
258. **`arch/sparc/math-emu/math_32.c`** -> AI Confidence: **99.48%**
259. **`arch/sparc/math-emu/math_64.c`** -> AI Confidence: **99.48%**
260. **`arch/sparc/mm/fault_64.c`** -> AI Confidence: **99.48%**
261. **`arch/sparc/net/bpf_jit_comp_32.c`** -> AI Confidence: **99.48%**
262. **`arch/sparc/vdso/vclock_gettime.c`** -> AI Confidence: **99.48%**
263. **`arch/x86/entry/calling.h`** -> AI Confidence: **99.48%**
264. **`arch/x86/kernel/cpu/cyrix.c`** -> AI Confidence: **99.48%**
265. **`arch/x86/kernel/cpu/mtrr/cyrix.c`** -> AI Confidence: **99.48%**
266. **`arch/x86/math-emu/fpu_entry.c`** -> AI Confidence: **99.48%**
267. **`arch/x86/math-emu/poly_atan.c`** -> AI Confidence: **99.48%**
268. **`arch/x86/math-emu/reg_ld_str.c`** -> AI Confidence: **99.48%**
269. **`arch/xtensa/kernel/module.c`** -> AI Confidence: **99.48%**
270. **`arch/xtensa/mm/fault.c`** -> AI Confidence: **99.48%**
271. **`block/ioprio.c`** -> AI Confidence: **99.48%**
272. **`drivers/accessibility/speakup/genmap.c`** -> AI Confidence: **99.48%**
273. **`drivers/accessibility/speakup/main.c`** -> AI Confidence: **99.48%**
274. **`drivers/acpi/acpica/dsobject.c`** -> AI Confidence: **99.48%**
275. **`drivers/acpi/acpica/dsutils.c`** -> AI Confidence: **99.48%**
276. **`drivers/acpi/acpica/dswexec.c`** -> AI Confidence: **99.48%**
277. **`drivers/acpi/acpica/dswload.c`** -> AI Confidence: **99.48%**
278. **`drivers/acpi/acpica/dswload2.c`** -> AI Confidence: **99.48%**
279. **`drivers/acpi/acpica/exoparg1.c`** -> AI Confidence: **99.48%**
280. **`drivers/acpi/acpica/psargs.c`** -> AI Confidence: **99.48%**
281. **`drivers/acpi/acpica/psloop.c`** -> AI Confidence: **99.48%**
282. **`drivers/acpi/acpica/psparse.c`** -> AI Confidence: **99.48%**
283. **`drivers/block/drbd/drbd_proc.c`** -> AI Confidence: **99.48%**
284. **`drivers/crypto/intel/qat/qat_common/adf_gen2_config.c`** -> AI Confidence: **99.48%**
285. **`drivers/crypto/intel/qat/qat_common/adf_gen4_config.c`** -> AI Confidence: **99.48%**
286. **`drivers/edac/edac_mc.c`** -> AI Confidence: **99.48%**
287. **`drivers/firmware/xilinx/zynqmp-debug.c`** -> AI Confidence: **99.48%**
288. **`drivers/gpu/drm/amd/display/dc/basics/dce_calcs.c`** -> AI Confidence: **99.48%**
289. **`drivers/gpu/drm/amd/display/dc/dml/calcs/dcn_calcs.c`** -> AI Confidence: **99.48%**
290. **`drivers/gpu/drm/i915/i915_getparam.c`** -> AI Confidence: **99.48%**
291. **`drivers/gpu/drm/nouveau/include/nvif/os.h`** -> AI Confidence: **99.48%**
292. **`drivers/gpu/drm/radeon/r200.c`** -> AI Confidence: **99.48%**
293. **`drivers/gpu/drm/radeon/radeon_combios.c`** -> AI Confidence: **99.48%**
294. **`drivers/gpu/drm/ttm/ttm_module.c`** -> AI Confidence: **99.48%**
295. **`drivers/hid/hid-input.c`** -> AI Confidence: **99.48%**
296. **`drivers/hid/hid-lg.c`** -> AI Confidence: **99.48%**
297. **`drivers/hid/hid-picolcd_debugfs.c`** -> AI Confidence: **99.48%**
298. **`drivers/hwmon/pmbus/tps25990.c`** -> AI Confidence: **99.48%**
299. **`drivers/i2c/busses/i2c-ali1535.c`** -> AI Confidence: **99.48%**
300. **`drivers/i2c/i2c-boardinfo.c`** -> AI Confidence: **99.48%**
301. **`drivers/iio/proximity/sx9310.c`** -> AI Confidence: **99.48%**
302. **`drivers/iio/proximity/sx9324.c`** -> AI Confidence: **99.48%**
303. **`drivers/iio/proximity/sx9360.c`** -> AI Confidence: **99.48%**
304. **`drivers/input/serio/hp_sdc.c`** -> AI Confidence: **99.48%**
305. **`drivers/input/serio/libps2.c`** -> AI Confidence: **99.48%**
306. **`drivers/isdn/hardware/mISDN/hfcmulti.c`** -> AI Confidence: **99.48%**
307. **`drivers/isdn/mISDN/dsp_audio.c`** -> AI Confidence: **99.48%**
308. **`drivers/isdn/mISDN/dsp_core.c`** -> AI Confidence: **99.48%**
309. **`drivers/macintosh/adbhid.c`** -> AI Confidence: **99.48%**
310. **`drivers/media/common/tveeprom.c`** -> AI Confidence: **99.48%**
311. **`drivers/media/dvb-frontends/dib8000.c`** -> AI Confidence: **99.48%**
312. **`drivers/media/dvb-frontends/drxk_hard.c`** -> AI Confidence: **99.48%**
313. **`drivers/media/dvb-frontends/stv090x.c`** -> AI Confidence: **99.48%**
314. **`drivers/media/i2c/msp3400-kthreads.c`** -> AI Confidence: **99.48%**
315. **`drivers/media/pci/cx23885/cx23885-cards.c`** -> AI Confidence: **99.48%**
316. **`drivers/media/pci/cx88/cx88-cards.c`** -> AI Confidence: **99.48%**
317. **`drivers/media/pci/cx88/cx88-dsp.c`** -> AI Confidence: **99.48%**
318. **`drivers/media/pci/cx88/cx88-input.c`** -> AI Confidence: **99.48%**
319. **`drivers/media/pci/cx88/cx88-tvaudio.c`** -> AI Confidence: **99.48%**
320. **`drivers/media/pci/ivtv/ivtv-routing.c`** -> AI Confidence: **99.48%**
321. **`drivers/media/pci/saa7134/saa7134-input.c`** -> AI Confidence: **99.48%**
322. **`drivers/media/pci/saa7134/saa7134-tvaudio.c`** -> AI Confidence: **99.48%**
323. **`drivers/media/pci/ttpci/budget.c`** -> AI Confidence: **99.48%**
324. **`drivers/media/usb/as102/as102_fw.c`** -> AI Confidence: **99.48%**
325. **`drivers/media/usb/go7007/go7007-fw.c`** -> AI Confidence: **99.48%**
326. **`drivers/memory/tegra/tegra210-emc-cc-r21021.c`** -> AI Confidence: **99.48%**
327. **`drivers/message/fusion/mptbase.c`** -> AI Confidence: **99.48%**
328. **`drivers/mfd/arizona-core.c`** -> AI Confidence: **99.48%**
329. **`drivers/mfd/da9052-core.c`** -> AI Confidence: **99.48%**
330. **`drivers/mfd/da9055-core.c`** -> AI Confidence: **99.48%**
331. **`drivers/mfd/wm831x-core.c`** -> AI Confidence: **99.48%**
332. **`drivers/misc/altera-stapl/altera.c`** -> AI Confidence: **99.48%**
333. **`drivers/mtd/maps/sc520cdp.c`** -> AI Confidence: **99.48%**
334. **`drivers/mtd/tests/nandbiterrs.c`** -> AI Confidence: **99.48%**
335. **`drivers/net/ethernet/qlogic/qed/qed_mng_tlv.c`** -> AI Confidence: **99.48%**
336. **`drivers/net/wireless/ath/ath9k/ar9003_hw.c`** -> AI Confidence: **99.48%**
337. **`drivers/net/wireless/broadcom/brcm80211/brcmfmac/proto.c`** -> AI Confidence: **99.48%**
338. **`drivers/net/wireless/intel/ipw2x00/libipw_tx.c`** -> AI Confidence: **99.48%**
339. **`drivers/net/wireless/st/cw1200/fwio.c`** -> AI Confidence: **99.48%**
340. **`drivers/scsi/aic7xxx/aicasm/aicasm_symbol.c`** -> AI Confidence: **99.48%**
341. **`drivers/scsi/arm/acornscsi.c`** -> AI Confidence: **99.48%**
342. **`drivers/scsi/atp870u.c`** -> AI Confidence: **99.48%**
343. **`drivers/scsi/ppa.h`** -> AI Confidence: **99.48%**
344. **`drivers/soc/fsl/qe/ucc.c`** -> AI Confidence: **99.48%**
345. **`drivers/soc/imx/soc-imx.c`** -> AI Confidence: **99.48%**
346. **`drivers/ssb/main.c`** -> AI Confidence: **99.48%**
347. **`drivers/staging/fbtft/fb_uc1611.c`** -> AI Confidence: **99.48%**
348. **`drivers/tc/tc.c`** -> AI Confidence: **99.48%**
349. **`drivers/thermal/intel/therm_throt.c`** -> AI Confidence: **99.48%**
350. **`drivers/usb/common/usb-otg-fsm.c`** -> AI Confidence: **99.48%**
351. **`drivers/usb/storage/debug.c`** -> AI Confidence: **99.48%**
352. **`drivers/video/fbdev/core/fbcon_rotate.c`** -> AI Confidence: **99.48%**
353. **`fs/btrfs/tests/inode-tests.c`** -> AI Confidence: **99.48%**
354. **`fs/ext4/page-io.c`** -> AI Confidence: **99.48%**
355. **`fs/jbd2/commit.c`** -> AI Confidence: **99.48%**
356. **`fs/jffs2/read.c`** -> AI Confidence: **99.48%**
357. **`fs/udf/unicode.c`** -> AI Confidence: **99.48%**
358. **`include/acpi/platform/acenv.h`** -> AI Confidence: **99.48%**
359. **`include/math-emu/soft-fp.h`** -> AI Confidence: **99.48%**
360. **`include/ras/ras_event.h`** -> AI Confidence: **99.48%**
361. **`kernel/kcmp.c`** -> AI Confidence: **99.48%**
362. **`net/ax25/ax25_ds_in.c`** -> AI Confidence: **99.48%**
363. **`net/ax25/ax25_std_in.c`** -> AI Confidence: **99.48%**
364. **`net/ax25/ax25_std_timer.c`** -> AI Confidence: **99.48%**
365. **`net/ceph/crush/mapper.c`** -> AI Confidence: **99.48%**
366. **`net/core/net-traces.c`** -> AI Confidence: **99.48%**
367. **`net/lapb/lapb_in.c`** -> AI Confidence: **99.48%**
368. **`net/netrom/nr_in.c`** -> AI Confidence: **99.48%**
369. **`samples/binderfs/binderfs_example.c`** -> AI Confidence: **99.48%**
370. **`samples/bpf/lwt_len_hist_user.c`** -> AI Confidence: **99.48%**
371. **`samples/bpf/tc_l2_redirect_user.c`** -> AI Confidence: **99.48%**
372. **`samples/bpf/tcp_basertt_kern.c`** -> AI Confidence: **99.48%**
373. **`samples/bpf/tcp_bufs_kern.c`** -> AI Confidence: **99.48%**
374. **`samples/bpf/tcp_clamp_kern.c`** -> AI Confidence: **99.48%**
375. **`samples/bpf/tcp_cong_kern.c`** -> AI Confidence: **99.48%**
376. **`samples/bpf/tcp_iw_kern.c`** -> AI Confidence: **99.48%**
377. **`samples/cgroup/cgroup_event_listener.c`** -> AI Confidence: **99.48%**
378. **`samples/hidraw/hid-example.c`** -> AI Confidence: **99.48%**
379. **`scripts/asn1_compiler.c`** -> AI Confidence: **99.48%**
380. **`scripts/dtc/fdtoverlay.c`** -> AI Confidence: **99.48%**
381. **`scripts/gendwarfksyms/gendwarfksyms.c`** -> AI Confidence: **99.48%**
382. **`scripts/kconfig/conf.c`** -> AI Confidence: **99.48%**
383. **`scripts/selinux/mdp/mdp.c`** -> AI Confidence: **99.48%**
384. **`security/apparmor/path.c`** -> AI Confidence: **99.48%**
385. **`sound/soc/amd/acp/acp-i2s.c`** -> AI Confidence: **99.48%**
386. **`sound/soc/amd/vangogh/acp5x-i2s.c`** -> AI Confidence: **99.48%**
387. **`sound/soc/codecs/wcd937x-sdw.c`** -> AI Confidence: **99.48%**
388. **`sound/soc/codecs/wcd938x-sdw.c`** -> AI Confidence: **99.48%**
389. **`sound/soc/codecs/wcd939x-sdw.c`** -> AI Confidence: **99.48%**
390. **`sound/soc/codecs/wm2200.c`** -> AI Confidence: **99.48%**
391. **`sound/usb/caiaq/input.c`** -> AI Confidence: **99.48%**
392. **`tools/arch/arm64/include/asm/sysreg.h`** -> AI Confidence: **99.48%**
393. **`tools/arch/x86/dell-uart-backlight-emulator/dell-uart-backlight-emulator.c`** -> AI Confidence: **99.48%**
394. **`tools/bpf/bpftool/perf.c`** -> AI Confidence: **99.48%**
395. **`tools/bpf/bpftool/sign.c`** -> AI Confidence: **99.48%**
396. **`tools/counter/counter_watch_events.c`** -> AI Confidence: **99.48%**
397. **`tools/dma/dma_map_benchmark.c`** -> AI Confidence: **99.48%**
398. **`tools/gpio/gpio-event-mon.c`** -> AI Confidence: **99.48%**
399. **`tools/gpio/gpio-hammer.c`** -> AI Confidence: **99.48%**
400. **`tools/iio/iio_event_monitor.c`** -> AI Confidence: **99.48%**
401. **`tools/iio/iio_generic_buffer.c`** -> AI Confidence: **99.48%**
402. **`tools/iio/iio_utils.c`** -> AI Confidence: **99.48%**
403. **`tools/include/asm/barrier.h`** -> AI Confidence: **99.48%**
404. **`tools/include/linux/kernel.h`** -> AI Confidence: **99.48%**
405. **`tools/include/nolibc/arch.h`** -> AI Confidence: **99.48%**
406. **`tools/include/uapi/asm/bitsperlong.h`** -> AI Confidence: **99.48%**
407. **`tools/net/ynl/ynltool/qstats.c`** -> AI Confidence: **99.48%**
408. **`tools/perf/arch/s390/util/header.c`** -> AI Confidence: **99.48%**
409. **`tools/perf/util/arm-spe-decoder/arm-spe-decoder.c`** -> AI Confidence: **99.48%**
410. **`tools/perf/util/demangle-java.c`** -> AI Confidence: **99.48%**
411. **`tools/perf/util/genelf.c`** -> AI Confidence: **99.48%**
412. **`tools/power/acpi/tools/ec/ec_access.c`** -> AI Confidence: **99.48%**
413. **`tools/power/cpupower/bench/main.c`** -> AI Confidence: **99.48%**
414. **`tools/power/cpupower/utils/cpuidle-info.c`** -> AI Confidence: **99.48%**
415. **`tools/power/cpupower/utils/cpuidle-set.c`** -> AI Confidence: **99.48%**
416. **`tools/power/cpupower/utils/cpupower-set.c`** -> AI Confidence: **99.48%**
417. **`tools/power/cpupower/utils/helpers/cpuid.c`** -> AI Confidence: **99.48%**
418. **`tools/power/cpupower/utils/idle_monitor/cpupower-monitor.c`** -> AI Confidence: **99.48%**
419. **`tools/spi/spidev_test.c`** -> AI Confidence: **99.48%**
420. **`tools/testing/selftests/arm64/fp/sve-probe-vls.c`** -> AI Confidence: **99.48%**
421. **`tools/testing/selftests/arm64/fp/vlset.c`** -> AI Confidence: **99.48%**
422. **`tools/testing/selftests/arm64/fp/zt-ptrace.c`** -> AI Confidence: **99.48%**
423. **`tools/testing/selftests/bpf/prog_tests/linked_list.c`** -> AI Confidence: **99.48%**
424. **`tools/testing/selftests/bpf/prog_tests/xdp_bonding.c`** -> AI Confidence: **99.48%**
425. **`tools/testing/selftests/bpf/test_maps.c`** -> AI Confidence: **99.48%**
426. **`tools/testing/selftests/bpf/xdp_synproxy.c`** -> AI Confidence: **99.48%**
427. **`tools/testing/selftests/breakpoints/breakpoint_test.c`** -> AI Confidence: **99.48%**
428. **`tools/testing/selftests/breakpoints/breakpoint_test_arm64.c`** -> AI Confidence: **99.48%**
429. **`tools/testing/selftests/cgroup/test_core.c`** -> AI Confidence: **99.48%**
430. **`tools/testing/selftests/cgroup/test_freezer.c`** -> AI Confidence: **99.48%**
431. **`tools/testing/selftests/cgroup/test_kill.c`** -> AI Confidence: **99.48%**
432. **`tools/testing/selftests/cgroup/test_memcontrol.c`** -> AI Confidence: **99.48%**
433. **`tools/testing/selftests/cgroup/test_pids.c`** -> AI Confidence: **99.48%**
434. **`tools/testing/selftests/clone3/clone3_set_tid.c`** -> AI Confidence: **99.48%**
435. **`tools/testing/selftests/coredump/stackdump_test.c`** -> AI Confidence: **99.48%**
436. **`tools/testing/selftests/exec/recursion-depth.c`** -> AI Confidence: **99.48%**
437. **`tools/testing/selftests/filesystems/fclog.c`** -> AI Confidence: **99.48%**
438. **`tools/testing/selftests/filesystems/file_stressor.c`** -> AI Confidence: **99.48%**
439. **`tools/testing/selftests/filesystems/statmount/listmount_test.c`** -> AI Confidence: **99.48%**
440. **`tools/testing/selftests/futex/functional/futex_requeue_pi_mismatched_ops.c`** -> AI Confidence: **99.48%**
441. **`tools/testing/selftests/futex/functional/futex_wait_wouldblock.c`** -> AI Confidence: **99.48%**
442. **`tools/testing/selftests/futex/functional/futex_waitv.c`** -> AI Confidence: **99.48%**
443. **`tools/testing/selftests/ir/ir_loopback.c`** -> AI Confidence: **99.48%**
444. **`tools/testing/selftests/kvm/kvm_binary_stats_test.c`** -> AI Confidence: **99.48%**
445. **`tools/testing/selftests/kvm/x86/vmx_preemption_timer_test.c`** -> AI Confidence: **99.48%**
446. **`tools/testing/selftests/lsm/lsm_list_modules_test.c`** -> AI Confidence: **99.48%**
447. **`tools/testing/selftests/media_tests/media_device_open.c`** -> AI Confidence: **99.48%**
448. **`tools/testing/selftests/media_tests/media_device_test.c`** -> AI Confidence: **99.48%**
449. **`tools/testing/selftests/mincore/mincore_selftest.c`** -> AI Confidence: **99.48%**
450. **`tools/testing/selftests/mm/gup_test.c`** -> AI Confidence: **99.48%**
451. **`tools/testing/selftests/mm/mrelease_test.c`** -> AI Confidence: **99.48%**
452. **`tools/testing/selftests/mm/transhuge-stress.c`** -> AI Confidence: **99.48%**
453. **`tools/testing/selftests/mm/write_to_hugetlbfs.c`** -> AI Confidence: **99.48%**
454. **`tools/testing/selftests/namespaces/listns_pagination_bug.c`** -> AI Confidence: **99.48%**
455. **`tools/testing/selftests/namespaces/nsid_test.c`** -> AI Confidence: **99.48%**
456. **`tools/testing/selftests/namespaces/regression_pidfd_setns_test.c`** -> AI Confidence: **99.48%**
457. **`tools/testing/selftests/namespaces/stress_test.c`** -> AI Confidence: **99.48%**
458. **`tools/testing/selftests/net/sk_so_peek_off.c`** -> AI Confidence: **99.48%**
459. **`tools/testing/selftests/perf_events/watermark_signal.c`** -> AI Confidence: **99.48%**
460. **`tools/testing/selftests/pid_namespace/regression_enomem.c`** -> AI Confidence: **99.48%**
461. **`tools/testing/selftests/pidfd/pidfd_open_test.c`** -> AI Confidence: **99.48%**
462. **`tools/testing/selftests/pidfd/pidfd_poll_test.c`** -> AI Confidence: **99.48%**
463. **`tools/testing/selftests/pidfd/pidfd_setattr_test.c`** -> AI Confidence: **99.48%**
464. **`tools/testing/selftests/pidfd/pidfd_setns_test.c`** -> AI Confidence: **99.48%**
465. **`tools/testing/selftests/powerpc/mm/tlbie_test.c`** -> AI Confidence: **99.48%**
466. **`tools/testing/selftests/powerpc/nx-gzip/gunz_test.c`** -> AI Confidence: **99.48%**
467. **`tools/testing/selftests/powerpc/primitives/asm/ppc_asm.h`** -> AI Confidence: **99.48%**
468. **`tools/testing/selftests/powerpc/ptrace/ptrace-syscall.c`** -> AI Confidence: **99.48%**
469. **`tools/testing/selftests/powerpc/signal/signal.c`** -> AI Confidence: **99.48%**
470. **`tools/testing/selftests/ptp/testptp.c`** -> AI Confidence: **99.48%**
471. **`tools/testing/selftests/rlimits/rlimits-per-userns.c`** -> AI Confidence: **99.48%**
472. **`tools/testing/selftests/thermal/intel/power_floor/power_floor_test.c`** -> AI Confidence: **99.48%**
473. **`tools/testing/selftests/thermal/intel/workload_hint/workload_hint_test.c`** -> AI Confidence: **99.48%**
474. **`tools/testing/selftests/timers/clocksource-switch.c`** -> AI Confidence: **99.48%**
475. **`tools/testing/selftests/timers/nanosleep.c`** -> AI Confidence: **99.48%**
476. **`tools/testing/selftests/timers/rtcpie.c`** -> AI Confidence: **99.48%**
477. **`tools/testing/selftests/watchdog/watchdog-test.c`** -> AI Confidence: **99.48%**
478. **`tools/testing/selftests/x86/mov_ss_trap.c`** -> AI Confidence: **99.48%**
479. **`tools/tracing/rtla/src/timerlat_u.c`** -> AI Confidence: **99.48%**
480. **`rust/syn/op.rs`** -> AI Confidence: **99.48%**
481. **`arch/arm/boot/dts/qcom/qcom-apq8064.dtsi`** -> AI Confidence: **99.44%**
482. **`arch/arm/boot/dts/qcom/qcom-msm8974.dtsi`** -> AI Confidence: **99.44%**
483. **`arch/arm/boot/dts/rockchip/rv1126.dtsi`** -> AI Confidence: **99.44%**
484. **`arch/arm/boot/dts/samsung/exynos4212-tab3.dtsi`** -> AI Confidence: **99.44%**
485. **`arch/arm64/boot/dts/allwinner/sun55i-a523.dtsi`** -> AI Confidence: **99.44%**
486. **`arch/arm64/boot/dts/amlogic/meson-axg.dtsi`** -> AI Confidence: **99.44%**
487. **`arch/arm64/boot/dts/mediatek/mt6795.dtsi`** -> AI Confidence: **99.44%**
488. **`arch/arm64/boot/dts/qcom/agatti.dtsi`** -> AI Confidence: **99.44%**
489. **`arch/arm64/boot/dts/qcom/hamoa.dtsi`** -> AI Confidence: **99.44%**
490. **`arch/arm64/boot/dts/qcom/kaanapali.dtsi`** -> AI Confidence: **99.44%**
491. **`arch/arm64/boot/dts/qcom/lemans.dtsi`** -> AI Confidence: **99.44%**
492. **`arch/arm64/boot/dts/qcom/monaco.dtsi`** -> AI Confidence: **99.44%**
493. **`arch/arm64/boot/dts/qcom/msm8939.dtsi`** -> AI Confidence: **99.44%**
494. **`arch/arm64/boot/dts/qcom/msm8953.dtsi`** -> AI Confidence: **99.44%**
495. **`arch/arm64/boot/dts/qcom/msm8996-oneplus-common.dtsi`** -> AI Confidence: **99.44%**
496. **`arch/arm64/boot/dts/qcom/msm8996.dtsi`** -> AI Confidence: **99.44%**
497. **`arch/arm64/boot/dts/qcom/msm8998.dtsi`** -> AI Confidence: **99.44%**
498. **`arch/arm64/boot/dts/qcom/qdu1000.dtsi`** -> AI Confidence: **99.44%**
499. **`arch/arm64/boot/dts/qcom/sc7280-qcard.dtsi`** -> AI Confidence: **99.44%**
500. **`arch/arm64/boot/dts/qcom/sc8280xp.dtsi`** -> AI Confidence: **99.44%**
501. **`arch/arm64/boot/dts/qcom/sdm630.dtsi`** -> AI Confidence: **99.44%**
502. **`arch/arm64/boot/dts/qcom/sdm845-oneplus-common.dtsi`** -> AI Confidence: **99.44%**
503. **`arch/arm64/boot/dts/qcom/sdm845-sony-xperia-tama.dtsi`** -> AI Confidence: **99.44%**
504. **`arch/arm64/boot/dts/qcom/sdm845-xiaomi-beryllium-common.dtsi`** -> AI Confidence: **99.44%**
505. **`arch/arm64/boot/dts/qcom/sdm845.dtsi`** -> AI Confidence: **99.44%**
506. **`arch/arm64/boot/dts/qcom/sm6115.dtsi`** -> AI Confidence: **99.44%**
507. **`arch/arm64/boot/dts/qcom/sm6350.dtsi`** -> AI Confidence: **99.44%**
508. **`arch/arm64/boot/dts/qcom/sm8150.dtsi`** -> AI Confidence: **99.44%**
509. **`arch/arm64/boot/dts/qcom/sm8250-xiaomi-elish-common.dtsi`** -> AI Confidence: **99.44%**
510. **`arch/arm64/boot/dts/qcom/sm8250.dtsi`** -> AI Confidence: **99.44%**
511. **`arch/arm64/boot/dts/qcom/sm8350-sony-xperia-sagami.dtsi`** -> AI Confidence: **99.44%**
512. **`arch/arm64/boot/dts/qcom/sm8350.dtsi`** -> AI Confidence: **99.44%**
513. **`arch/arm64/boot/dts/qcom/sm8450-sony-xperia-nagara.dtsi`** -> AI Confidence: **99.44%**
514. **`arch/arm64/boot/dts/qcom/sm8450.dtsi`** -> AI Confidence: **99.44%**
515. **`arch/arm64/boot/dts/qcom/sm8550.dtsi`** -> AI Confidence: **99.44%**
516. **`arch/arm64/boot/dts/qcom/sm8650.dtsi`** -> AI Confidence: **99.44%**
517. **`arch/arm64/boot/dts/qcom/sm8750.dtsi`** -> AI Confidence: **99.44%**
518. **`arch/arm64/boot/dts/rockchip/rk3528.dtsi`** -> AI Confidence: **99.44%**
519. **`arch/arm64/boot/dts/rockchip/rk3576.dtsi`** -> AI Confidence: **99.44%**
520. **`arch/arm/boot/dts/allwinner/sun8i-a83t.dtsi`** -> AI Confidence: **99.43%**
521. **`arch/arm/boot/dts/allwinner/sun8i-r40.dtsi`** -> AI Confidence: **99.43%**
522. **`arch/arm/boot/dts/allwinner/sun9i-a80.dtsi`** -> AI Confidence: **99.43%**
523. **`arch/arm/boot/dts/allwinner/sunxi-h3-h5.dtsi`** -> AI Confidence: **99.43%**
524. **`arch/arm/boot/dts/mediatek/mt7623.dtsi`** -> AI Confidence: **99.43%**
525. **`arch/arm/boot/dts/microchip/lan966x.dtsi`** -> AI Confidence: **99.43%**
526. **`arch/arm/boot/dts/nvidia/tegra20-asus-transformer-common.dtsi`** -> AI Confidence: **99.43%**
527. **`arch/arm/boot/dts/nvidia/tegra30-asus-nexus7-grouper-common.dtsi`** -> AI Confidence: **99.43%**
528. **`arch/arm/boot/dts/nvidia/tegra30-lg-x3.dtsi`** -> AI Confidence: **99.43%**
529. **`arch/arm/boot/dts/nxp/imx/imx6ull-dhcor-som.dtsi`** -> AI Confidence: **99.43%**
530. **`arch/arm/boot/dts/qcom/qcom-ipq8064.dtsi`** -> AI Confidence: **99.43%**
531. **`arch/arm/boot/dts/qcom/qcom-msm8226.dtsi`** -> AI Confidence: **99.43%**
532. **`arch/arm/boot/dts/qcom/qcom-msm8960.dtsi`** -> AI Confidence: **99.43%**
533. **`arch/arm/boot/dts/qcom/qcom-msm8974-sony-xperia-rhine.dtsi`** -> AI Confidence: **99.43%**
534. **`arch/arm/boot/dts/qcom/qcom-msm8974pro-sony-xperia-shinano-common.dtsi`** -> AI Confidence: **99.43%**
535. **`arch/arm/boot/dts/rockchip/rk3036.dtsi`** -> AI Confidence: **99.43%**
536. **`arch/arm/boot/dts/rockchip/rk322x.dtsi`** -> AI Confidence: **99.43%**
537. **`arch/arm/boot/dts/rockchip/rk3288-veyron-chromebook.dtsi`** -> AI Confidence: **99.43%**
538. **`arch/arm/boot/dts/samsung/exynos4412-midas.dtsi`** -> AI Confidence: **99.43%**
539. **`arch/arm/boot/dts/samsung/exynos4412-odroid-common.dtsi`** -> AI Confidence: **99.43%**
540. **`arch/arm/boot/dts/samsung/exynos5250-snow-common.dtsi`** -> AI Confidence: **99.43%**
541. **`arch/arm/boot/dts/samsung/exynos5410.dtsi`** -> AI Confidence: **99.43%**
542. **`arch/arm/boot/dts/samsung/exynos5420.dtsi`** -> AI Confidence: **99.43%**
543. **`arch/arm/boot/dts/st/stm32mp153c-lxa-fairytux2.dtsi`** -> AI Confidence: **99.43%**
544. **`arch/arm/boot/dts/st/stm32mp157c-ed1.dts`** -> AI Confidence: **99.43%**
545. **`arch/arm/boot/dts/st/stm32mp15xc-lxa-tac.dtsi`** -> AI Confidence: **99.43%**
546. **`arch/arm/boot/dts/sunplus/sunplus-sp7021.dtsi`** -> AI Confidence: **99.43%**
547. **`arch/arm64/boot/dts/allwinner/sun50i-a64-pinephone.dtsi`** -> AI Confidence: **99.43%**
548. **`arch/arm64/boot/dts/allwinner/sun50i-a64.dtsi`** -> AI Confidence: **99.43%**
549. **`arch/arm64/boot/dts/allwinner/sun50i-h6.dtsi`** -> AI Confidence: **99.43%**
550. **`arch/arm64/boot/dts/allwinner/sun50i-h616.dtsi`** -> AI Confidence: **99.43%**
551. **`arch/arm64/boot/dts/amlogic/meson-a1.dtsi`** -> AI Confidence: **99.43%**
552. **`arch/arm64/boot/dts/amlogic/meson-libretech-cottonwood.dtsi`** -> AI Confidence: **99.43%**
553. **`arch/arm64/boot/dts/apple/t8103.dtsi`** -> AI Confidence: **99.43%**
554. **`arch/arm64/boot/dts/apple/t8112.dtsi`** -> AI Confidence: **99.43%**
555. **`arch/arm64/boot/dts/exynos/exynos5433-tm2-common.dtsi`** -> AI Confidence: **99.43%**
556. **`arch/arm64/boot/dts/exynos/google/gs101.dtsi`** -> AI Confidence: **99.43%**
557. **`arch/arm64/boot/dts/mediatek/mt7622.dtsi`** -> AI Confidence: **99.43%**
558. **`arch/arm64/boot/dts/mediatek/mt7988a.dtsi`** -> AI Confidence: **99.43%**
559. **`arch/arm64/boot/dts/mediatek/mt8173-elm.dtsi`** -> AI Confidence: **99.43%**
560. **`arch/arm64/boot/dts/mediatek/mt8173.dtsi`** -> AI Confidence: **99.43%**
561. **`arch/arm64/boot/dts/mediatek/mt8186-corsola.dtsi`** -> AI Confidence: **99.43%**
562. **`arch/arm64/boot/dts/mediatek/mt8390-genio-common.dtsi`** -> AI Confidence: **99.43%**
563. **`arch/arm64/boot/dts/mediatek/mt8390-tungsten-smarc.dtsi`** -> AI Confidence: **99.43%**
564. **`arch/arm64/boot/dts/mediatek/mt8395-genio-common.dtsi`** -> AI Confidence: **99.43%**
565. **`arch/arm64/boot/dts/nvidia/tegra186.dtsi`** -> AI Confidence: **99.43%**
566. **`arch/arm64/boot/dts/nvidia/tegra194.dtsi`** -> AI Confidence: **99.43%**
567. **`arch/arm64/boot/dts/nvidia/tegra210.dtsi`** -> AI Confidence: **99.43%**
568. **`arch/arm64/boot/dts/nvidia/tegra234.dtsi`** -> AI Confidence: **99.43%**
569. **`arch/arm64/boot/dts/qcom/msm8916-samsung-a2015-common.dtsi`** -> AI Confidence: **99.43%**
570. **`arch/arm64/boot/dts/qcom/msm8916-samsung-fortuna-common.dtsi`** -> AI Confidence: **99.43%**
571. **`arch/arm64/boot/dts/qcom/msm8976.dtsi`** -> AI Confidence: **99.43%**
572. **`arch/arm64/boot/dts/qcom/msm8994.dtsi`** -> AI Confidence: **99.43%**
573. **`arch/arm64/boot/dts/qcom/msm8996-sony-xperia-tone.dtsi`** -> AI Confidence: **99.43%**
574. **`arch/arm64/boot/dts/qcom/msm8996-xiaomi-common.dtsi`** -> AI Confidence: **99.43%**
575. **`arch/arm64/boot/dts/qcom/msm8998-oneplus-common.dtsi`** -> AI Confidence: **99.43%**
576. **`arch/arm64/boot/dts/qcom/msm8998-sony-xperia-yoshino.dtsi`** -> AI Confidence: **99.43%**
577. **`arch/arm64/boot/dts/qcom/qcs404.dtsi`** -> AI Confidence: **99.43%**
578. **`arch/arm64/boot/dts/qcom/qcs6490-audioreach.dtsi`** -> AI Confidence: **99.43%**
579. **`arch/arm64/boot/dts/qcom/sc7280-herobrine.dtsi`** -> AI Confidence: **99.43%**
580. **`arch/arm64/boot/dts/qcom/sc7280-idp.dtsi`** -> AI Confidence: **99.43%**
581. **`arch/arm64/boot/dts/qcom/sdm845-google-common.dtsi`** -> AI Confidence: **99.43%**
582. **`arch/arm64/boot/dts/qcom/sdm845-lg-common.dtsi`** -> AI Confidence: **99.43%**
583. **`arch/arm64/boot/dts/qcom/sm6125.dtsi`** -> AI Confidence: **99.43%**
584. **`arch/arm64/boot/dts/qcom/sm7125-xiaomi-common.dtsi`** -> AI Confidence: **99.43%**
585. **`arch/arm64/boot/dts/qcom/sm8150-sony-xperia-kumano.dtsi`** -> AI Confidence: **99.43%**
586. **`arch/arm64/boot/dts/qcom/sm8250-sony-xperia-edo.dtsi`** -> AI Confidence: **99.43%**
587. **`arch/arm64/boot/dts/qcom/x1-asus-zenbook-a14.dtsi`** -> AI Confidence: **99.43%**
588. **`arch/arm64/boot/dts/qcom/x1-crd.dtsi`** -> AI Confidence: **99.43%**
589. **`arch/arm64/boot/dts/qcom/x1-dell-thena.dtsi`** -> AI Confidence: **99.43%**
590. **`arch/arm64/boot/dts/qcom/x1-hp-omnibook-x14.dtsi`** -> AI Confidence: **99.43%**
591. **`arch/arm64/boot/dts/qcom/x1e78100-lenovo-thinkpad-t14s.dtsi`** -> AI Confidence: **99.43%**
592. **`arch/arm64/boot/dts/qcom/x1e80100-microsoft-romulus.dtsi`** -> AI Confidence: **99.43%**
593. **`arch/arm64/boot/dts/renesas/rzt2h-n2h-evk-common.dtsi`** -> AI Confidence: **99.43%**
594. **`arch/arm64/boot/dts/rockchip/px30.dtsi`** -> AI Confidence: **99.43%**
595. **`arch/arm64/boot/dts/rockchip/rk3308.dtsi`** -> AI Confidence: **99.43%**
596. **`arch/arm64/boot/dts/rockchip/rk3328.dtsi`** -> AI Confidence: **99.43%**
597. **`arch/arm64/boot/dts/rockchip/rk3368.dtsi`** -> AI Confidence: **99.43%**
598. **`arch/arm64/boot/dts/rockchip/rk3566-anbernic-rgxx3.dtsi`** -> AI Confidence: **99.43%**
599. **`arch/arm64/boot/dts/rockchip/rk3566-bigtreetech-cb2.dtsi`** -> AI Confidence: **99.43%**
600. **`arch/arm64/boot/dts/rockchip/rk3566-pinetab2.dtsi`** -> AI Confidence: **99.43%**
601. **`arch/arm64/boot/dts/rockchip/rk3566-powkiddy-rk2023.dtsi`** -> AI Confidence: **99.43%**
602. **`arch/arm64/boot/dts/rockchip/rk3568-fastrhino-r66s.dtsi`** -> AI Confidence: **99.43%**
603. **`arch/arm64/boot/dts/rockchip/rk3568-hinlink-opc.dtsi`** -> AI Confidence: **99.43%**
604. **`arch/arm64/boot/dts/rockchip/rk3568-nanopi-r5s.dtsi`** -> AI Confidence: **99.43%**
605. **`arch/arm64/boot/dts/rockchip/rk3588-nanopc-t6.dtsi`** -> AI Confidence: **99.43%**
606. **`arch/arm64/boot/dts/rockchip/rk3588s-orangepi-5.dtsi`** -> AI Confidence: **99.43%**
607. **`arch/arm64/boot/dts/ti/k3-am69-aquila.dtsi`** -> AI Confidence: **99.43%**
608. **`arch/riscv/boot/dts/allwinner/sunxi-d1s-t113.dtsi`** -> AI Confidence: **99.43%**
609. **`drivers/iommu/generic_pt/fmt/iommu_template.h`** -> AI Confidence: **99.43%**
610. **`drivers/net/ethernet/brocade/bna/cna.h`** -> AI Confidence: **99.43%**
611. **`arch/arm/boot/dts/rockchip/rk3288.dtsi`** -> AI Confidence: **99.42%**
612. **`arch/arm64/boot/dts/amlogic/meson-g12-common.dtsi`** -> AI Confidence: **99.42%**
613. **`arch/arm64/boot/dts/qcom/kodiak.dtsi`** -> AI Confidence: **99.42%**
614. **`arch/arm64/boot/dts/qcom/msm8916.dtsi`** -> AI Confidence: **99.42%**
615. **`arch/arm64/boot/dts/qcom/sc7180-trogdor.dtsi`** -> AI Confidence: **99.42%**
616. **`arch/arm64/boot/dts/qcom/sc7180.dtsi`** -> AI Confidence: **99.42%**
617. **`arch/arm64/boot/dts/rockchip/rk3399-base.dtsi`** -> AI Confidence: **99.42%**
618. **`arch/arm64/boot/dts/rockchip/rk356x-base.dtsi`** -> AI Confidence: **99.42%**
619. **`arch/arm64/boot/dts/rockchip/rk3588-base.dtsi`** -> AI Confidence: **99.42%**
620. **`drivers/gpu/drm/amd/display/dc/os_types.h`** -> AI Confidence: **99.42%**
621. **`tools/include/nolibc/stdio.h`** -> AI Confidence: **99.42%**
622. **`tools/include/uapi/asm/errno.h`** -> AI Confidence: **99.42%**
623. **`tools/lib/python/abi/abi_parser.py`** -> AI Confidence: **99.39%**
624. **`tools/power/pm-graph/bootgraph.py`** -> AI Confidence: **99.39%**
625. **`tools/power/pm-graph/sleepgraph.py`** -> AI Confidence: **99.39%**
626. **`arch/alpha/kernel/err_marvel.c`** -> AI Confidence: **99.39%**
627. **`arch/alpha/kernel/module.c`** -> AI Confidence: **99.39%**
628. **`arch/alpha/mm/fault.c`** -> AI Confidence: **99.39%**
629. **`arch/arm/kernel/module.c`** -> AI Confidence: **99.39%**
630. **`arch/arm/mach-omap1/id.c`** -> AI Confidence: **99.39%**
631. **`arch/arm/mach-omap1/mux.c`** -> AI Confidence: **99.39%**
632. **`arch/arm/mach-omap1/timer.c`** -> AI Confidence: **99.39%**
633. **`arch/arm/mach-omap1/usb.c`** -> AI Confidence: **99.39%**
634. **`arch/arm/mach-omap2/clock.c`** -> AI Confidence: **99.39%**
635. **`arch/arm/mach-pxa/mfp-pxa2xx.c`** -> AI Confidence: **99.39%**
636. **`arch/arm/mm/cache-tauros2.c`** -> AI Confidence: **99.39%**
637. **`arch/arm64/include/asm/hardirq.h`** -> AI Confidence: **99.39%**
638. **`arch/csky/kernel/module.c`** -> AI Confidence: **99.39%**
639. **`arch/loongarch/kernel/cpu-probe.c`** -> AI Confidence: **99.39%**
640. **`arch/loongarch/kvm/exit.c`** -> AI Confidence: **99.39%**
641. **`arch/loongarch/mm/fault.c`** -> AI Confidence: **99.39%**
642. **`arch/m68k/amiga/config.c`** -> AI Confidence: **99.39%**
643. **`arch/m68k/atari/atasound.c`** -> AI Confidence: **99.39%**
644. **`arch/m68k/atari/time.c`** -> AI Confidence: **99.39%**
645. **`arch/m68k/coldfire/intc-simr.c`** -> AI Confidence: **99.39%**
646. **`arch/m68k/kernel/traps.c`** -> AI Confidence: **99.39%**
647. **`arch/m68k/mac/via.c`** -> AI Confidence: **99.39%**
648. **`arch/m68k/mm/fault.c`** -> AI Confidence: **99.39%**
649. **`arch/m68k/mm/kmap.c`** -> AI Confidence: **99.39%**
650. **`arch/m68k/mm/mcfmmu.c`** -> AI Confidence: **99.39%**
651. **`arch/m68k/mm/memory.c`** -> AI Confidence: **99.39%**
652. **`arch/mips/ath79/clock.c`** -> AI Confidence: **99.39%**
653. **`arch/mips/ath79/common.c`** -> AI Confidence: **99.39%**
654. **`arch/mips/ath79/setup.c`** -> AI Confidence: **99.39%**
655. **`arch/mips/bcm63xx/cpu.c`** -> AI Confidence: **99.39%**
656. **`arch/mips/bcm63xx/reset.c`** -> AI Confidence: **99.39%**
657. **`arch/mips/cavium-octeon/octeon-platform.c`** -> AI Confidence: **99.39%**
658. **`arch/mips/dec/tc.c`** -> AI Confidence: **99.39%**
659. **`arch/mips/generic/irq.c`** -> AI Confidence: **99.39%**
660. **`arch/mips/include/asm/mmu_context.h`** -> AI Confidence: **99.39%**
661. **`arch/mips/kernel/spram.c`** -> AI Confidence: **99.39%**
662. **`arch/mips/kernel/sync-r4k.c`** -> AI Confidence: **99.39%**
663. **`arch/mips/kvm/vz.c`** -> AI Confidence: **99.39%**
664. **`arch/mips/lantiq/xway/clk.c`** -> AI Confidence: **99.39%**
665. **`arch/mips/mm/fault.c`** -> AI Confidence: **99.39%**
666. **`arch/mips/mm/uasm-mips.c`** -> AI Confidence: **99.39%**
667. **`arch/mips/mti-malta/malta-dtshim.c`** -> AI Confidence: **99.39%**
668. **`arch/mips/mti-malta/malta-int.c`** -> AI Confidence: **99.39%**
669. **`arch/mips/net/bpf_jit_comp.c`** -> AI Confidence: **99.39%**
670. **`arch/mips/txx9/generic/setup_tx4927.c`** -> AI Confidence: **99.39%**
671. **`arch/mips/txx9/generic/setup_tx4938.c`** -> AI Confidence: **99.39%**
672. **`arch/nios2/mm/fault.c`** -> AI Confidence: **99.39%**
673. **`arch/openrisc/mm/fault.c`** -> AI Confidence: **99.39%**
674. **`arch/parisc/kernel/pdc_chassis.c`** -> AI Confidence: **99.39%**
675. **`arch/parisc/math-emu/decode_exc.c`** -> AI Confidence: **99.39%**
676. **`arch/parisc/mm/fault.c`** -> AI Confidence: **99.39%**
677. **`arch/powerpc/boot/treeboot-akebono.c`** -> AI Confidence: **99.39%**
678. **`arch/powerpc/kernel/mce.c`** -> AI Confidence: **99.39%**
679. **`arch/powerpc/kernel/smp-tbsync.c`** -> AI Confidence: **99.39%**
680. **`arch/powerpc/kernel/vecemu.c`** -> AI Confidence: **99.39%**
681. **`arch/powerpc/kvm/emulate_loadstore.c`** -> AI Confidence: **99.39%**
682. **`arch/powerpc/mm/pageattr.c`** -> AI Confidence: **99.39%**
683. **`arch/powerpc/net/bpf_jit_comp64.c`** -> AI Confidence: **99.39%**
684. **`arch/powerpc/platforms/83xx/usb_831x.c`** -> AI Confidence: **99.39%**
685. **`arch/powerpc/platforms/83xx/usb_834x.c`** -> AI Confidence: **99.39%**
686. **`arch/powerpc/platforms/cell/spufs/run.c`** -> AI Confidence: **99.39%**
687. **`arch/powerpc/platforms/powernv/opal-sysparam.c`** -> AI Confidence: **99.39%**
688. **`arch/powerpc/platforms/powernv/pci.c`** -> AI Confidence: **99.39%**
689. **`arch/s390/boot/ipl_parm.c`** -> AI Confidence: **99.39%**
690. **`arch/s390/kernel/dis.c`** -> AI Confidence: **99.39%**
691. **`arch/s390/mm/pageattr.c`** -> AI Confidence: **99.39%**
692. **`arch/sh/kernel/traps_32.c`** -> AI Confidence: **99.39%**
693. **`arch/sh/mm/fault.c`** -> AI Confidence: **99.39%**
694. **`arch/sparc/boot/piggyback.c`** -> AI Confidence: **99.39%**
695. **`arch/sparc/include/asm/uaccess_64.h`** -> AI Confidence: **99.39%**
696. **`arch/sparc/kernel/module.c`** -> AI Confidence: **99.39%**
697. **`arch/sparc/kernel/psycho_common.c`** -> AI Confidence: **99.39%**
698. **`arch/sparc/kernel/setup_64.c`** -> AI Confidence: **99.39%**
699. **`arch/sparc/kernel/signal_64.c`** -> AI Confidence: **99.39%**
700. **`arch/sparc/kernel/sys_sparc_64.c`** -> AI Confidence: **99.39%**
701. **`arch/sparc/kernel/visemul.c`** -> AI Confidence: **99.39%**
702. **`arch/sparc/mm/tsb.c`** -> AI Confidence: **99.39%**
703. **`arch/sparc/net/bpf_jit_comp_64.c`** -> AI Confidence: **99.39%**
704. **`arch/um/kernel/skas/syscall.c`** -> AI Confidence: **99.39%**
705. **`arch/um/os-Linux/elf_aux.c`** -> AI Confidence: **99.39%**
706. **`arch/um/os-Linux/execvp.c`** -> AI Confidence: **99.39%**
707. **`arch/x86/boot/cpucheck.c`** -> AI Confidence: **99.39%**
708. **`arch/x86/kernel/cpu/centaur.c`** -> AI Confidence: **99.39%**
709. **`arch/x86/kernel/cpu/feat_ctl.c`** -> AI Confidence: **99.39%**
710. **`arch/x86/kernel/cpu/intel.c`** -> AI Confidence: **99.39%**
711. **`arch/x86/kernel/early_printk.c`** -> AI Confidence: **99.39%**
712. **`arch/x86/math-emu/errors.c`** -> AI Confidence: **99.39%**
713. **`arch/x86/mm/amdtopology.c`** -> AI Confidence: **99.39%**
714. **`arch/x86/pci/pcbios.c`** -> AI Confidence: **99.39%**
715. **`arch/x86/tools/insn_sanity.c`** -> AI Confidence: **99.39%**
716. **`arch/x86/um/ptrace_64.c`** -> AI Confidence: **99.39%**
717. **`arch/x86/xen/suspend_hvm.c`** -> AI Confidence: **99.39%**
718. **`block/partitions/efi.c`** -> AI Confidence: **99.39%**
719. **`certs/extract-cert.c`** -> AI Confidence: **99.39%**
720. **`drivers/accessibility/braille/braille_console.c`** -> AI Confidence: **99.39%**
721. **`drivers/ata/libata-eh.c`** -> AI Confidence: **99.39%**
722. **`drivers/ata/pata_parport/bpck.c`** -> AI Confidence: **99.39%**
723. **`drivers/ata/pata_parport/dstr.c`** -> AI Confidence: **99.39%**
724. **`drivers/ata/pata_parport/epat.c`** -> AI Confidence: **99.39%**
725. **`drivers/ata/pata_parport/epia.c`** -> AI Confidence: **99.39%**
726. **`drivers/ata/pata_parport/on26.c`** -> AI Confidence: **99.39%**
727. **`drivers/char/pc8736x_gpio.c`** -> AI Confidence: **99.39%**
728. **`drivers/clk/berlin/bg2.c`** -> AI Confidence: **99.39%**
729. **`drivers/clk/ti/clkt_dpll.c`** -> AI Confidence: **99.39%**
730. **`drivers/dma/qcom/hidma_mgmt.c`** -> AI Confidence: **99.39%**
731. **`drivers/firmware/efi/cper-arm.c`** -> AI Confidence: **99.39%**
732. **`drivers/firmware/efi/libstub/printk.c`** -> AI Confidence: **99.39%**
733. **`drivers/firmware/efi/libstub/vsprintf.c`** -> AI Confidence: **99.39%**
734. **`drivers/gpu/drm/amd/amdgpu/atom.c`** -> AI Confidence: **99.39%**
735. **`drivers/gpu/drm/amd/amdgpu/atombios_encoders.c`** -> AI Confidence: **99.39%**
736. **`drivers/gpu/drm/amd/amdgpu/nbio_v7_4.c`** -> AI Confidence: **99.39%**
737. **`drivers/gpu/drm/amd/amdkfd/kfd_flat_memory.c`** -> AI Confidence: **99.39%**
738. **`drivers/gpu/drm/amd/display/amdgpu_dm/amdgpu_dm_colorop.c`** -> AI Confidence: **99.39%**
739. **`drivers/gpu/drm/amd/display/dc/dio/dcn401/dcn401_dio_stream_encoder.c`** -> AI Confidence: **99.39%**
740. **`drivers/gpu/drm/amd/display/dc/dpp/dcn401/dcn401_dpp.c`** -> AI Confidence: **99.39%**
741. **`drivers/gpu/drm/amd/pm/swsmu/smu13/smu_v13_0_4_ppt.c`** -> AI Confidence: **99.39%**
742. **`drivers/gpu/drm/amd/pm/swsmu/smu14/smu_v14_0_0_ppt.c`** -> AI Confidence: **99.39%**
743. **`drivers/gpu/drm/ast/ast_2300.c`** -> AI Confidence: **99.39%**
744. **`drivers/gpu/drm/bridge/adv7511/adv7511_audio.c`** -> AI Confidence: **99.39%**
745. **`drivers/gpu/drm/nouveau/nouveau_connector.c`** -> AI Confidence: **99.39%**
746. **`drivers/gpu/drm/nouveau/nvkm/subdev/gsp/rm/r570/fifo.c`** -> AI Confidence: **99.39%**
747. **`drivers/gpu/drm/radeon/atom.c`** -> AI Confidence: **99.39%**
748. **`drivers/gpu/drm/radeon/r300.c`** -> AI Confidence: **99.39%**
749. **`drivers/gpu/drm/radeon/radeon_asic.c`** -> AI Confidence: **99.39%**
750. **`drivers/gpu/drm/radeon/radeon_clocks.c`** -> AI Confidence: **99.39%**
751. **`drivers/gpu/drm/radeon/radeon_i2c.c`** -> AI Confidence: **99.39%**
752. **`drivers/gpu/drm/radeon/radeon_kms.c`** -> AI Confidence: **99.39%**
753. **`drivers/gpu/drm/radeon/si.c`** -> AI Confidence: **99.39%**
754. **`drivers/gpu/drm/rockchip/cdn-dp-reg.c`** -> AI Confidence: **99.39%**
755. **`drivers/gpu/drm/xe/xe_exec.c`** -> AI Confidence: **99.39%**
756. **`drivers/hid/hid-uclogic-params.c`** -> AI Confidence: **99.39%**
757. **`drivers/hwmon/aquacomputer_d5next.c`** -> AI Confidence: **99.39%**
758. **`drivers/hwmon/k10temp.c`** -> AI Confidence: **99.39%**
759. **`drivers/hwmon/pmbus/lm25066.c`** -> AI Confidence: **99.39%**
760. **`drivers/hwmon/pmbus/ltc3815.c`** -> AI Confidence: **99.39%**
761. **`drivers/hwmon/pmbus/max34440.c`** -> AI Confidence: **99.39%**
762. **`drivers/hwmon/pmbus/max8688.c`** -> AI Confidence: **99.39%**
763. **`drivers/i2c/algos/i2c-algo-pca.c`** -> AI Confidence: **99.39%**
764. **`drivers/i2c/busses/i2c-viapro.c`** -> AI Confidence: **99.39%**
765. **`drivers/iio/common/cros_ec_sensors/cros_ec_sensors.c`** -> AI Confidence: **99.39%**
766. **`drivers/infiniband/hw/hfi1/rc.c`** -> AI Confidence: **99.39%**
767. **`drivers/input/joystick/sidewinder.c`** -> AI Confidence: **99.39%**
768. **`drivers/input/joystick/xpad.c`** -> AI Confidence: **99.39%**
769. **`drivers/input/keyboard/hil_kbd.c`** -> AI Confidence: **99.39%**
770. **`drivers/input/serio/hp_sdc_mlc.c`** -> AI Confidence: **99.39%**
771. **`drivers/input/serio/ps2-gpio.c`** -> AI Confidence: **99.39%**
772. **`drivers/macintosh/windfarm_pm91.c`** -> AI Confidence: **99.39%**
773. **`drivers/md/md-autodetect.c`** -> AI Confidence: **99.39%**
774. **`drivers/media/common/cx2341x.c`** -> AI Confidence: **99.39%**
775. **`drivers/media/dvb-core/dvb_frontend.c`** -> AI Confidence: **99.39%**
776. **`drivers/media/dvb-frontends/dib9000.c`** -> AI Confidence: **99.39%**
777. **`drivers/media/dvb-frontends/drxd_hard.c`** -> AI Confidence: **99.39%**
778. **`drivers/media/dvb-frontends/mb86a16.c`** -> AI Confidence: **99.39%**
779. **`drivers/media/dvb-frontends/tda18271c2dd.c`** -> AI Confidence: **99.39%**
780. **`drivers/media/i2c/cx25840/cx25840-core.c`** -> AI Confidence: **99.39%**
781. **`drivers/media/pci/bt8xx/bttv-input.c`** -> AI Confidence: **99.39%**
782. **`drivers/media/pci/cx18/cx18-driver.c`** -> AI Confidence: **99.39%**
783. **`drivers/media/pci/ivtv/ivtv-driver.c`** -> AI Confidence: **99.39%**
784. **`drivers/media/pci/ivtv/ivtv-streams.c`** -> AI Confidence: **99.39%**
785. **`drivers/media/rc/lirc_dev.c`** -> AI Confidence: **99.39%**
786. **`drivers/media/tuners/mxl5005s.c`** -> AI Confidence: **99.39%**
787. **`drivers/media/tuners/xc2028.c`** -> AI Confidence: **99.39%**
788. **`drivers/media/tuners/xc4000.c`** -> AI Confidence: **99.39%**
789. **`drivers/media/usb/go7007/go7007-driver.c`** -> AI Confidence: **99.39%**
790. **`drivers/media/usb/hdpvr/hdpvr-core.c`** -> AI Confidence: **99.39%**
791. **`drivers/media/usb/pvrusb2/pvrusb2-encoder.c`** -> AI Confidence: **99.39%**
792. **`drivers/media/usb/pvrusb2/pvrusb2-i2c-core.c`** -> AI Confidence: **99.39%**
793. **`drivers/media/v4l2-core/v4l2-cci.c`** -> AI Confidence: **99.39%**
794. **`drivers/message/fusion/mptscsih.c`** -> AI Confidence: **99.39%**
795. **`drivers/mfd/axp20x.c`** -> AI Confidence: **99.39%**
796. **`drivers/misc/lis3lv02d/lis3lv02d.c`** -> AI Confidence: **99.39%**
797. **`drivers/mmc/core/mmc.c`** -> AI Confidence: **99.39%**
798. **`drivers/mmc/host/sdhci-pci-o2micro.c`** -> AI Confidence: **99.39%**
799. **`drivers/mtd/inftlmount.c`** -> AI Confidence: **99.39%**
800. **`drivers/mtd/nftlmount.c`** -> AI Confidence: **99.39%**
801. **`drivers/mtd/parsers/bcm47xxpart.c`** -> AI Confidence: **99.39%**
802. **`drivers/mtd/parsers/redboot.c`** -> AI Confidence: **99.39%**
803. **`drivers/net/ethernet/3com/3c515.c`** -> AI Confidence: **99.39%**
804. **`drivers/net/ethernet/cisco/enic/enic_res.c`** -> AI Confidence: **99.39%**
805. **`drivers/net/ethernet/microchip/sparx5/sparx5_vcap_debugfs.c`** -> AI Confidence: **99.39%**
806. **`drivers/net/ethernet/sunplus/spl2sw_int.c`** -> AI Confidence: **99.39%**
807. **`drivers/net/ethernet/xircom/xirc2ps_cs.c`** -> AI Confidence: **99.39%**
808. **`drivers/net/ovpn/pktid.c`** -> AI Confidence: **99.39%**
809. **`drivers/net/wireguard/main.c`** -> AI Confidence: **99.39%**
810. **`drivers/net/wireless/ath/ath5k/reset.c`** -> AI Confidence: **99.39%**
811. **`drivers/net/wireless/broadcom/b43legacy/phy.c`** -> AI Confidence: **99.39%**
812. **`drivers/net/wireless/intel/ipw2x00/libipw_wx.c`** -> AI Confidence: **99.39%**
813. **`drivers/net/wireless/mediatek/mt76/mt76x0/phy.c`** -> AI Confidence: **99.39%**
814. **`drivers/net/wireless/realtek/rtw88/rtw88xxa.c`** -> AI Confidence: **99.39%**
815. **`drivers/parisc/asp.c`** -> AI Confidence: **99.39%**
816. **`drivers/pci/hotplug/ibmphp_core.c`** -> AI Confidence: **99.39%**
817. **`drivers/pcmcia/i82365.c`** -> AI Confidence: **99.39%**
818. **`drivers/pcmcia/pxa2xx_sharpsl.c`** -> AI Confidence: **99.39%**
819. **`drivers/platform/x86/asus-armoury.c`** -> AI Confidence: **99.39%**
820. **`drivers/platform/x86/dell/dell-wmi-sysman/sysman.c`** -> AI Confidence: **99.39%**
821. **`drivers/platform/x86/hp/hp-bioscfg/bioscfg.c`** -> AI Confidence: **99.39%**
822. **`drivers/pnp/interface.c`** -> AI Confidence: **99.39%**
823. **`drivers/regulator/axp20x-regulator.c`** -> AI Confidence: **99.39%**
824. **`drivers/regulator/s2mpa01.c`** -> AI Confidence: **99.39%**
825. **`drivers/scsi/3w-xxxx.c`** -> AI Confidence: **99.39%**
826. **`drivers/scsi/aacraid/commsup.c`** -> AI Confidence: **99.39%**
827. **`drivers/scsi/aacraid/src.c`** -> AI Confidence: **99.39%**
828. **`drivers/scsi/arm/fas216.c`** -> AI Confidence: **99.39%**
829. **`drivers/scsi/fnic/fnic_res.c`** -> AI Confidence: **99.39%**
830. **`drivers/scsi/g_NCR5380.c`** -> AI Confidence: **99.39%**
831. **`drivers/scsi/lpfc/lpfc_vport.c`** -> AI Confidence: **99.39%**
832. **`drivers/scsi/qla2xxx/qla_init.c`** -> AI Confidence: **99.39%**
833. **`drivers/scsi/qla2xxx/qla_isr.c`** -> AI Confidence: **99.39%**
834. **`drivers/scsi/qla4xxx/ql4_os.c`** -> AI Confidence: **99.39%**
835. **`drivers/scsi/wd33c93.c`** -> AI Confidence: **99.39%**
836. **`drivers/spi/spi-falcon.c`** -> AI Confidence: **99.39%**
837. **`drivers/ssb/scan.c`** -> AI Confidence: **99.39%**
838. **`drivers/staging/media/atomisp/pci/hive_isp_css_common/host/fifo_monitor.c`** -> AI Confidence: **99.39%**
839. **`drivers/staging/media/atomisp/pci/runtime/binary/src/binary.c`** -> AI Confidence: **99.39%**
840. **`drivers/staging/media/atomisp/pci/runtime/event/src/event.c`** -> AI Confidence: **99.39%**
841. **`drivers/staging/media/atomisp/pci/runtime/ifmtr/src/ifmtr.c`** -> AI Confidence: **99.39%**
842. **`drivers/staging/media/atomisp/pci/sh_css_mipi.c`** -> AI Confidence: **99.39%**
843. **`drivers/staging/media/sunxi/cedrus/cedrus_dec.c`** -> AI Confidence: **99.39%**
844. **`drivers/tty/serial/suncore.c`** -> AI Confidence: **99.39%**
845. **`drivers/usb/chipidea/otg_fsm.c`** -> AI Confidence: **99.39%**
846. **`drivers/usb/core/hub.c`** -> AI Confidence: **99.39%**
847. **`drivers/usb/dwc2/core_intr.c`** -> AI Confidence: **99.39%**
848. **`drivers/usb/gadget/udc/omap_udc.c`** -> AI Confidence: **99.39%**
849. **`drivers/usb/host/fhci-sched.c`** -> AI Confidence: **99.39%**
850. **`drivers/usb/host/isp116x-hcd.c`** -> AI Confidence: **99.39%**
851. **`drivers/usb/image/microtek.c`** -> AI Confidence: **99.39%**
852. **`drivers/usb/musb/musb_virthub.c`** -> AI Confidence: **99.39%**
853. **`drivers/usb/serial/qcserial.c`** -> AI Confidence: **99.39%**
854. **`drivers/usb/storage/cypress_atacb.c`** -> AI Confidence: **99.39%**
855. **`drivers/video/fbdev/acornfb.c`** -> AI Confidence: **99.39%**
856. **`drivers/video/fbdev/amifb.c`** -> AI Confidence: **99.39%**
857. **`drivers/video/fbdev/aty/atyfb_base.c`** -> AI Confidence: **99.39%**
858. **`drivers/video/fbdev/aty/radeon_base.c`** -> AI Confidence: **99.39%**
859. **`drivers/video/fbdev/core/fbmon.c`** -> AI Confidence: **99.39%**
860. **`drivers/video/fbdev/geode/lxfb_ops.c`** -> AI Confidence: **99.39%**
861. **`drivers/video/fbdev/geode/video_gx.c`** -> AI Confidence: **99.39%**
862. **`drivers/video/fbdev/macfb.c`** -> AI Confidence: **99.39%**
863. **`drivers/video/fbdev/nvidia/nv_of.c`** -> AI Confidence: **99.39%**
864. **`drivers/video/fbdev/nvidia/nv_setup.c`** -> AI Confidence: **99.39%**
865. **`drivers/video/fbdev/nvidia/nvidia.c`** -> AI Confidence: **99.39%**
866. **`drivers/video/logo/pnmtologo.c`** -> AI Confidence: **99.39%**
867. **`drivers/watchdog/w83627hf_wdt.c`** -> AI Confidence: **99.39%**
868. **`fs/binfmt_flat.c`** -> AI Confidence: **99.39%**
869. **`fs/btrfs/tests/raid-stripe-tree-tests.c`** -> AI Confidence: **99.39%**
870. **`fs/ecryptfs/keystore.c`** -> AI Confidence: **99.39%**
871. **`fs/jffs2/nodemgmt.c`** -> AI Confidence: **99.39%**
872. **`fs/netfs/buffered_write.c`** -> AI Confidence: **99.39%**
873. **`fs/ntfs3/fslog.c`** -> AI Confidence: **99.39%**
874. **`fs/smb/client/fs_context.c`** -> AI Confidence: **99.39%**
875. **`fs/smb/client/ioctl.c`** -> AI Confidence: **99.39%**
876. **`fs/squashfs/dir.c`** -> AI Confidence: **99.39%**
877. **`fs/squashfs/inode.c`** -> AI Confidence: **99.39%**
878. **`fs/unicode/mkutf8data.c`** -> AI Confidence: **99.39%**
879. **`include/acpi/platform/aclinux.h`** -> AI Confidence: **99.39%**
880. **`kernel/auditfilter.c`** -> AI Confidence: **99.39%**
881. **`kernel/trace/ring_buffer_benchmark.c`** -> AI Confidence: **99.39%**
882. **`mm/mprotect.c`** -> AI Confidence: **99.39%**
883. **`net/9p/trans_rdma.c`** -> AI Confidence: **99.39%**
884. **`net/atm/resources.c`** -> AI Confidence: **99.39%**
885. **`net/ax25/ax25_ds_subr.c`** -> AI Confidence: **99.39%**
886. **`net/ax25/ax25_ds_timer.c`** -> AI Confidence: **99.39%**
887. **`net/ax25/ax25_in.c`** -> AI Confidence: **99.39%**
888. **`net/ax25/ax25_subr.c`** -> AI Confidence: **99.39%**
889. **`net/core/lock_debug.c`** -> AI Confidence: **99.39%**
890. **`net/ipv4/ip_options.c`** -> AI Confidence: **99.39%**
891. **`net/ipv4/ipconfig.c`** -> AI Confidence: **99.39%**
892. **`net/llc/af_llc.c`** -> AI Confidence: **99.39%**
893. **`net/mac80211/parse.c`** -> AI Confidence: **99.39%**
894. **`net/rds/send.c`** -> AI Confidence: **99.39%**
895. **`net/rose/rose_in.c`** -> AI Confidence: **99.39%**
896. **`net/rose/rose_subr.c`** -> AI Confidence: **99.39%**
897. **`net/rxrpc/recvmsg.c`** -> AI Confidence: **99.39%**
898. **`net/smc/smc_close.c`** -> AI Confidence: **99.39%**
899. **`net/smc/smc_stats.c`** -> AI Confidence: **99.39%**
900. **`net/sunrpc/auth_gss/gss_krb5_keys.c`** -> AI Confidence: **99.39%**
901. **`net/x25/af_x25.c`** -> AI Confidence: **99.39%**
902. **`net/x25/x25_in.c`** -> AI Confidence: **99.39%**
903. **`samples/bpf/fds_example.c`** -> AI Confidence: **99.39%**
904. **`samples/bpf/spintest_user.c`** -> AI Confidence: **99.39%**
905. **`samples/bpf/xdp_adjust_tail_user.c`** -> AI Confidence: **99.39%**
906. **`samples/nitro_enclaves/ne_ioctl_sample.c`** -> AI Confidence: **99.39%**
907. **`samples/uhid/uhid-example.c`** -> AI Confidence: **99.39%**
908. **`scripts/dtc/fdtput.c`** -> AI Confidence: **99.39%**
909. **`scripts/dtc/util.c`** -> AI Confidence: **99.39%**
910. **`scripts/kconfig/mconf.c`** -> AI Confidence: **99.39%**
911. **`scripts/mod/sumversion.c`** -> AI Confidence: **99.39%**
912. **`scripts/sign-file.c`** -> AI Confidence: **99.39%**
913. **`security/keys/process_keys.c`** -> AI Confidence: **99.39%**
914. **`security/landlock/errata.h`** -> AI Confidence: **99.39%**
915. **`sound/core/seq/seq.c`** -> AI Confidence: **99.39%**
916. **`sound/core/seq/seq_midi_emul.c`** -> AI Confidence: **99.39%**
917. **`sound/isa/wavefront/wavefront_synth.c`** -> AI Confidence: **99.39%**
918. **`sound/pci/ac97/ac97_pcm.c`** -> AI Confidence: **99.39%**
919. **`sound/pci/ca0106/ca0106_proc.c`** -> AI Confidence: **99.39%**
920. **`sound/pci/emu10k1/emu10k1_main.c`** -> AI Confidence: **99.39%**
921. **`sound/pci/ymfpci/ymfpci.c`** -> AI Confidence: **99.39%**
922. **`sound/soc/amd/raven/acp3x-i2s.c`** -> AI Confidence: **99.39%**
923. **`sound/soc/codecs/cs35l36.c`** -> AI Confidence: **99.39%**
924. **`sound/soc/codecs/rt1015.c`** -> AI Confidence: **99.39%**
925. **`sound/soc/codecs/wm8995.c`** -> AI Confidence: **99.39%**
926. **`sound/soc/mediatek/mt8192/mt8192-afe-pcm.c`** -> AI Confidence: **99.39%**
927. **`tools/accounting/getdelays.c`** -> AI Confidence: **99.39%**
928. **`tools/bpf/bpf_jit_disasm.c`** -> AI Confidence: **99.39%**
929. **`tools/gpio/lsgpio.c`** -> AI Confidence: **99.39%**
930. **`tools/hv/hv_fcopy_uio_daemon.c`** -> AI Confidence: **99.39%**
931. **`tools/hv/hv_kvp_daemon.c`** -> AI Confidence: **99.39%**
932. **`tools/hv/hv_vss_daemon.c`** -> AI Confidence: **99.39%**
933. **`tools/laptop/dslm/dslm.c`** -> AI Confidence: **99.39%**
934. **`tools/lib/api/fs/cgroup.c`** -> AI Confidence: **99.39%**
935. **`tools/lib/bpf/libbpf_probes.c`** -> AI Confidence: **99.39%**
936. **`tools/lib/subcmd/parse-options.c`** -> AI Confidence: **99.39%**
937. **`tools/lib/subcmd/run-command.c`** -> AI Confidence: **99.39%**
938. **`tools/mm/page-types.c`** -> AI Confidence: **99.39%**
939. **`tools/mm/slabinfo.c`** -> AI Confidence: **99.39%**
940. **`tools/objtool/arch/x86/decode.c`** -> AI Confidence: **99.39%**
941. **`tools/objtool/include/objtool/warn.h`** -> AI Confidence: **99.39%**
942. **`tools/perf/bench/futex-hash.c`** -> AI Confidence: **99.39%**
943. **`tools/perf/bench/futex-wake.c`** -> AI Confidence: **99.39%**
944. **`tools/perf/bench/syscall.c`** -> AI Confidence: **99.39%**
945. **`tools/perf/perf.c`** -> AI Confidence: **99.39%**
946. **`tools/perf/util/arm-spe-decoder/arm-spe-pkt-decoder.c`** -> AI Confidence: **99.39%**
947. **`tools/perf/util/bpf_off_cpu.c`** -> AI Confidence: **99.39%**
948. **`tools/perf/util/cloexec.c`** -> AI Confidence: **99.39%**
949. **`tools/perf/util/dwarf-regs.c`** -> AI Confidence: **99.39%**
950. **`tools/perf/util/intel-pt-decoder/intel-pt-insn-decoder.c`** -> AI Confidence: **99.39%**
951. **`tools/perf/util/perf_regs.c`** -> AI Confidence: **99.39%**
952. **`tools/perf/util/sample-raw.c`** -> AI Confidence: **99.39%**
953. **`tools/perf/util/target.c`** -> AI Confidence: **99.39%**
954. **`tools/perf/util/top.c`** -> AI Confidence: **99.39%**
955. **`tools/power/acpi/tools/acpidbg/acpidbg.c`** -> AI Confidence: **99.39%**
956. **`tools/power/cpupower/bench/parse.c`** -> AI Confidence: **99.39%**
957. **`tools/power/cpupower/utils/cpufreq-info.c`** -> AI Confidence: **99.39%**
958. **`tools/power/cpupower/utils/cpufreq-set.c`** -> AI Confidence: **99.39%**
959. **`tools/power/cpupower/utils/cpupower-info.c`** -> AI Confidence: **99.39%**
960. **`tools/power/cpupower/utils/idle_monitor/cpuidle_sysfs.c`** -> AI Confidence: **99.39%**
961. **`tools/power/x86/x86_energy_perf_policy/x86_energy_perf_policy.c`** -> AI Confidence: **99.39%**
962. **`tools/sched_ext/scx_qmap.c`** -> AI Confidence: **99.39%**
963. **`tools/spi/spidev_fdx.c`** -> AI Confidence: **99.39%**
964. **`tools/testing/crypto/chacha20-s390/test-cipher.c`** -> AI Confidence: **99.39%**
965. **`tools/testing/selftests/alsa/pcm-test.c`** -> AI Confidence: **99.39%**
966. **`tools/testing/selftests/arm64/abi/ptrace.c`** -> AI Confidence: **99.39%**
967. **`tools/testing/selftests/arm64/mte/check_user_mem.c`** -> AI Confidence: **99.39%**
968. **`tools/testing/selftests/bpf/prog_tests/bpf_obj_pinning.c`** -> AI Confidence: **99.39%**
969. **`tools/testing/selftests/bpf/prog_tests/cgroup_getset_retval.c`** -> AI Confidence: **99.39%**
970. **`tools/testing/selftests/bpf/prog_tests/lsm_cgroup.c`** -> AI Confidence: **99.39%**
971. **`tools/testing/selftests/bpf/prog_tests/sock_fields.c`** -> AI Confidence: **99.39%**
972. **`tools/testing/selftests/bpf/prog_tests/sockmap_basic.c`** -> AI Confidence: **99.39%**
973. **`tools/testing/selftests/bpf/prog_tests/sockmap_ktls.c`** -> AI Confidence: **99.39%**
974. **`tools/testing/selftests/bpf/prog_tests/tailcalls.c`** -> AI Confidence: **99.39%**
975. **`tools/testing/selftests/cgroup/test_cpu.c`** -> AI Confidence: **99.39%**
976. **`tools/testing/selftests/cgroup/test_kmem.c`** -> AI Confidence: **99.39%**
977. **`tools/testing/selftests/cgroup/test_zswap.c`** -> AI Confidence: **99.39%**
978. **`tools/testing/selftests/cgroup/wait_inotify.c`** -> AI Confidence: **99.39%**
979. **`tools/testing/selftests/core/close_range_test.c`** -> AI Confidence: **99.39%**
980. **`tools/testing/selftests/firmware/fw_namespace.c`** -> AI Confidence: **99.39%**
981. **`tools/testing/selftests/ftrace/poll.c`** -> AI Confidence: **99.39%**
982. **`tools/testing/selftests/ia64/aliasing-test.c`** -> AI Confidence: **99.39%**
983. **`tools/testing/selftests/kcmp/kcmp_test.c`** -> AI Confidence: **99.39%**
984. **`tools/testing/selftests/kvm/get-reg-list.c`** -> AI Confidence: **99.39%**
985. **`tools/testing/selftests/kvm/x86/monitor_mwait_test.c`** -> AI Confidence: **99.39%**
986. **`tools/testing/selftests/kvm/x86/nested_dirty_log_test.c`** -> AI Confidence: **99.39%**
987. **`tools/testing/selftests/landlock/fs_bench.c`** -> AI Confidence: **99.39%**
988. **`tools/testing/selftests/landlock/scoped_abstract_unix_test.c`** -> AI Confidence: **99.39%**
989. **`tools/testing/selftests/lsm/lsm_get_self_attr_test.c`** -> AI Confidence: **99.39%**
990. **`tools/testing/selftests/media_tests/video_device_test.c`** -> AI Confidence: **99.39%**
991. **`tools/testing/selftests/mm/hugetlb-madvise.c`** -> AI Confidence: **99.39%**
992. **`tools/testing/selftests/mm/hugetlb_dio.c`** -> AI Confidence: **99.39%**
993. **`tools/testing/selftests/mm/map_hugetlb.c`** -> AI Confidence: **99.39%**
994. **`tools/testing/selftests/mm/migration.c`** -> AI Confidence: **99.39%**
995. **`tools/testing/selftests/mm/mlock-random-test.c`** -> AI Confidence: **99.39%**
996. **`tools/testing/selftests/mm/pagemap_ioctl.c`** -> AI Confidence: **99.39%**
997. **`tools/testing/selftests/mm/pfnmap.c`** -> AI Confidence: **99.39%**
998. **`tools/testing/selftests/mm/soft-dirty.c`** -> AI Confidence: **99.39%**
999. **`tools/testing/selftests/mm/split_huge_page_test.c`** -> AI Confidence: **99.39%**
1000. **`tools/testing/selftests/mount/unprivileged-remount-test.c`** -> AI Confidence: **99.39%**
1001. **`tools/testing/selftests/mqueue/mq_open_tests.c`** -> AI Confidence: **99.39%**
1002. **`tools/testing/selftests/net/af_unix/unix_connreset.c`** -> AI Confidence: **99.39%**
1003. **`tools/testing/selftests/net/io_uring_zerocopy_tx.c`** -> AI Confidence: **99.39%**
1004. **`tools/testing/selftests/net/ipv6_flowlabel_mgr.c`** -> AI Confidence: **99.39%**
1005. **`tools/testing/selftests/net/so_rcv_listener.c`** -> AI Confidence: **99.39%**
1006. **`tools/testing/selftests/net/tcp_mmap.c`** -> AI Confidence: **99.39%**
1007. **`tools/testing/selftests/net/udpgso_bench_rx.c`** -> AI Confidence: **99.39%**
1008. **`tools/testing/selftests/nolibc/nolibc-test.c`** -> AI Confidence: **99.39%**
1009. **`tools/testing/selftests/openat2/rename_attack_test.c`** -> AI Confidence: **99.39%**
1010. **`tools/testing/selftests/pidfd/pidfd_xattr_test.c`** -> AI Confidence: **99.39%**
1011. **`tools/testing/selftests/powerpc/benchmarks/fork.c`** -> AI Confidence: **99.39%**
1012. **`tools/testing/selftests/powerpc/security/entry_flush.c`** -> AI Confidence: **99.39%**
1013. **`tools/testing/selftests/powerpc/security/rfi_flush.c`** -> AI Confidence: **99.39%**
1014. **`tools/testing/selftests/powerpc/security/uaccess_flush.c`** -> AI Confidence: **99.39%**
1015. **`tools/testing/selftests/powerpc/signal/sigfuz.c`** -> AI Confidence: **99.39%**
1016. **`tools/testing/selftests/powerpc/tm/tm-unavailable.c`** -> AI Confidence: **99.39%**
1017. **`tools/testing/selftests/ptrace/peeksiginfo.c`** -> AI Confidence: **99.39%**
1018. **`tools/testing/selftests/riscv/vector/validate_v_ptrace.c`** -> AI Confidence: **99.39%**
1019. **`tools/testing/selftests/timers/leap-a-day.c`** -> AI Confidence: **99.39%**
1020. **`tools/testing/selftests/timers/set-2038.c`** -> AI Confidence: **99.39%**
1021. **`tools/testing/selftests/tmpfs/bug-link-o-tmpfile.c`** -> AI Confidence: **99.39%**
1022. **`tools/testing/selftests/x86/ptrace_syscall.c`** -> AI Confidence: **99.39%**
1023. **`tools/testing/vsock/vsock_perf.c`** -> AI Confidence: **99.39%**
1024. **`tools/thermal/tmon/tmon.c`** -> AI Confidence: **99.39%**
1025. **`tools/tracing/rtla/src/common.c`** -> AI Confidence: **99.39%**
1026. **`tools/tracing/rtla/src/timerlat_hist.c`** -> AI Confidence: **99.39%**
1027. **`tools/usb/usbip/src/usbip_detach.c`** -> AI Confidence: **99.39%**
1028. **`tools/usb/usbip/src/usbip_unbind.c`** -> AI Confidence: **99.39%**
1029. **`usr/gen_init_cpio.c`** -> AI Confidence: **99.39%**
1030. **`scripts/kconfig/qconf.cc`** -> AI Confidence: **99.39%**
1031. **`tools/testing/selftests/net/netfilter/nft_concat_range.sh`** -> AI Confidence: **99.35%**
1032. **`arch/alpha/kernel/setup.c`** -> AI Confidence: **99.35%**
1033. **`arch/mips/bcm63xx/irq.c`** -> AI Confidence: **99.35%**
1034. **`arch/powerpc/kvm/book3s_pr.c`** -> AI Confidence: **99.35%**
1035. **`arch/powerpc/perf/8xx-pmu.c`** -> AI Confidence: **99.35%**
1036. **`arch/s390/net/bpf_jit_comp.c`** -> AI Confidence: **99.35%**
1037. **`arch/sparc/kernel/unaligned_64.c`** -> AI Confidence: **99.35%**
1038. **`arch/x86/kernel/cpu/amd.c`** -> AI Confidence: **99.35%**
1039. **`arch/x86/kernel/cpu/mtrr/cleanup.c`** -> AI Confidence: **99.35%**
1040. **`drivers/extcon/extcon-max77693.c`** -> AI Confidence: **99.35%**
1041. **`drivers/gpu/drm/radeon/ni.c`** -> AI Confidence: **99.35%**
1042. **`drivers/hwmon/dme1737.c`** -> AI Confidence: **99.35%**
1043. **`drivers/infiniband/hw/hfi1/sdma.c`** -> AI Confidence: **99.35%**
1044. **`drivers/md/dm-integrity.c`** -> AI Confidence: **99.35%**
1045. **`drivers/media/firewire/firedtv-dvb.c`** -> AI Confidence: **99.35%**
1046. **`drivers/mfd/wm8350-core.c`** -> AI Confidence: **99.35%**
1047. **`drivers/net/can/cc770/cc770_isa.c`** -> AI Confidence: **99.35%**
1048. **`drivers/net/ethernet/broadcom/tg3.c`** -> AI Confidence: **99.35%**
1049. **`drivers/net/ethernet/fujitsu/fmvj18x_cs.c`** -> AI Confidence: **99.35%**
1050. **`drivers/net/wireless/admtek/adm8211.c`** -> AI Confidence: **99.35%**
1051. **`drivers/net/wireless/broadcom/b43/phy_n.c`** -> AI Confidence: **99.35%**
1052. **`drivers/net/wireless/intel/iwlwifi/iwl-drv.c`** -> AI Confidence: **99.35%**
1053. **`drivers/pci/hotplug/ibmphp_hpc.c`** -> AI Confidence: **99.35%**
1054. **`drivers/pcmcia/tcic.c`** -> AI Confidence: **99.35%**
1055. **`drivers/pinctrl/cirrus/pinctrl-madera-core.c`** -> AI Confidence: **99.35%**
1056. **`drivers/regulator/s2mps11.c`** -> AI Confidence: **99.35%**
1057. **`drivers/scsi/advansys.c`** -> AI Confidence: **99.35%**
1058. **`drivers/scsi/ips.c`** -> AI Confidence: **99.35%**
1059. **`drivers/video/fbdev/matrox/matroxfb_base.c`** -> AI Confidence: **99.35%**
1060. **`drivers/video/fbdev/offb.c`** -> AI Confidence: **99.35%**
1061. **`io_uring/register.c`** -> AI Confidence: **99.35%**
1062. **`samples/bpf/xdp_tx_iptunnel_user.c`** -> AI Confidence: **99.35%**
1063. **`tools/bpf/bpf_dbg.c`** -> AI Confidence: **99.35%**
1064. **`tools/bpf/bpftool/cgroup.c`** -> AI Confidence: **99.35%**
1065. **`tools/bpf/bpftool/link.c`** -> AI Confidence: **99.35%**
1066. **`tools/bpf/bpftool/map.c`** -> AI Confidence: **99.35%**
1067. **`tools/perf/util/annotate-arch/annotate-x86.c`** -> AI Confidence: **99.35%**
1068. **`tools/perf/util/copyfile.c`** -> AI Confidence: **99.35%**
1069. **`tools/power/acpi/tools/pfrut/pfrut.c`** -> AI Confidence: **99.35%**
1070. **`tools/testing/selftests/bpf/progs/test_tcpnotify_kern.c`** -> AI Confidence: **99.35%**
1071. **`tools/testing/selftests/bpf/xdping.c`** -> AI Confidence: **99.35%**
1072. **`tools/testing/selftests/kvm/rseq_test.c`** -> AI Confidence: **99.35%**
1073. **`tools/testing/selftests/mm/thuge-gen.c`** -> AI Confidence: **99.35%**
1074. **`tools/testing/selftests/namespaces/cred_change_test.c`** -> AI Confidence: **99.35%**
1075. **`tools/testing/selftests/net/mptcp/mptcp_inq.c`** -> AI Confidence: **99.35%**
1076. **`tools/testing/selftests/net/tfo.c`** -> AI Confidence: **99.35%**
1077. **`tools/testing/selftests/proc/read.c`** -> AI Confidence: **99.35%**
1078. **`tools/testing/selftests/x86/syscall_numbering.c`** -> AI Confidence: **99.35%**
1079. **`tools/tracing/rtla/src/timerlat.c`** -> AI Confidence: **99.35%**
1080. **`tools/testing/selftests/net/ipv6_route_update_soft_lockup.sh`** -> AI Confidence: **99.34%**
1081. **`arch/alpha/kernel/gct.c`** -> AI Confidence: **99.34%**
1082. **`arch/alpha/math-emu/sfp-util.h`** -> AI Confidence: **99.34%**
1083. **`arch/arc/include/asm/cmpxchg.h`** -> AI Confidence: **99.34%**
1084. **`arch/arc/kernel/disasm.c`** -> AI Confidence: **99.34%**
1085. **`arch/arm/boot/dts/allwinner/sun4i-a10-chuwi-v7-cw0825.dts`** -> AI Confidence: **99.34%**
1086. **`arch/arm/boot/dts/allwinner/sun4i-a10-gemei-g9.dts`** -> AI Confidence: **99.34%**
1087. **`arch/arm/boot/dts/allwinner/sun4i-a10-inet97fv2.dts`** -> AI Confidence: **99.34%**
1088. **`arch/arm/boot/dts/allwinner/sun4i-a10-inet9f-rev03.dts`** -> AI Confidence: **99.34%**
1089. **`arch/arm/boot/dts/allwinner/sun4i-a10-pcduino.dts`** -> AI Confidence: **99.34%**
1090. **`arch/arm/boot/dts/allwinner/sun5i-a10s-olinuxino-micro.dts`** -> AI Confidence: **99.34%**
1091. **`arch/arm/boot/dts/allwinner/sun5i-a10s-wobo-i5.dts`** -> AI Confidence: **99.34%**
1092. **`arch/arm/boot/dts/allwinner/sun5i-a13-hsg-h702.dts`** -> AI Confidence: **99.34%**
1093. **`arch/arm/boot/dts/allwinner/sun5i-a13-licheepi-one.dts`** -> AI Confidence: **99.34%**
1094. **`arch/arm/boot/dts/allwinner/sun5i-gr8-chip-pro.dts`** -> AI Confidence: **99.34%**
1095. **`arch/arm/boot/dts/allwinner/sun5i-gr8-evb.dts`** -> AI Confidence: **99.34%**
1096. **`arch/arm/boot/dts/allwinner/sun5i-r8-chip.dts`** -> AI Confidence: **99.34%**
1097. **`arch/arm/boot/dts/allwinner/sun6i-a31s-primo81.dts`** -> AI Confidence: **99.34%**
1098. **`arch/arm/boot/dts/allwinner/sun7i-a20-bananapi-m1-plus.dts`** -> AI Confidence: **99.34%**
1099. **`arch/arm/boot/dts/allwinner/sun7i-a20-bananapi.dts`** -> AI Confidence: **99.34%**
1100. **`arch/arm/boot/dts/allwinner/sun7i-a20-cubieboard2.dts`** -> AI Confidence: **99.34%**
1101. **`arch/arm/boot/dts/allwinner/sun7i-a20-cubietruck.dts`** -> AI Confidence: **99.34%**
1102. **`arch/arm/boot/dts/allwinner/sun7i-a20-haoyu-marsboard.dts`** -> AI Confidence: **99.34%**
1103. **`arch/arm/boot/dts/allwinner/sun7i-a20-icnova-swac.dts`** -> AI Confidence: **99.34%**
1104. **`arch/arm/boot/dts/allwinner/sun7i-a20-lamobo-r1.dts`** -> AI Confidence: **99.34%**
1105. **`arch/arm/boot/dts/allwinner/sun7i-a20-olimex-som-evb.dts`** -> AI Confidence: **99.34%**
1106. **`arch/arm/boot/dts/allwinner/sun7i-a20-olimex-som204-evb.dts`** -> AI Confidence: **99.34%**
1107. **`arch/arm/boot/dts/allwinner/sun7i-a20-olinuxino-lime2.dts`** -> AI Confidence: **99.34%**
1108. **`arch/arm/boot/dts/allwinner/sun7i-a20-olinuxino-micro.dts`** -> AI Confidence: **99.34%**
1109. **`arch/arm/boot/dts/allwinner/sun7i-a20-orangepi-mini.dts`** -> AI Confidence: **99.34%**
1110. **`arch/arm/boot/dts/allwinner/sun7i-a20-orangepi.dts`** -> AI Confidence: **99.34%**
1111. **`arch/arm/boot/dts/allwinner/sun7i-a20-pcduino3-nano.dts`** -> AI Confidence: **99.34%**
1112. **`arch/arm/boot/dts/allwinner/sun7i-a20-pcduino3.dts`** -> AI Confidence: **99.34%**
1113. **`arch/arm/boot/dts/allwinner/sun7i-a20-wits-pro-a20-dkt.dts`** -> AI Confidence: **99.34%**
1114. **`arch/arm/boot/dts/allwinner/sun8i-a33-sinlinx-sina33.dts`** -> AI Confidence: **99.34%**
1115. **`arch/arm/boot/dts/allwinner/sun8i-a83t-tbs-a711.dts`** -> AI Confidence: **99.34%**
1116. **`arch/arm/boot/dts/allwinner/sun8i-r16-parrot.dts`** -> AI Confidence: **99.34%**
1117. **`arch/arm/boot/dts/aspeed/aspeed-bmc-ampere-mtjefferson.dts`** -> AI Confidence: **99.34%**
1118. **`arch/arm/boot/dts/aspeed/aspeed-bmc-ampere-mtmitchell.dts`** -> AI Confidence: **99.34%**
1119. **`arch/arm/boot/dts/aspeed/aspeed-bmc-asrock-altrad8.dts`** -> AI Confidence: **99.34%**
1120. **`arch/arm/boot/dts/aspeed/aspeed-bmc-asrock-e3c246d4i.dts`** -> AI Confidence: **99.34%**
1121. **`arch/arm/boot/dts/aspeed/aspeed-bmc-asrock-spc621d8hm3.dts`** -> AI Confidence: **99.34%**
1122. **`arch/arm/boot/dts/aspeed/aspeed-bmc-asus-x4tf.dts`** -> AI Confidence: **99.34%**
1123. **`arch/arm/boot/dts/aspeed/aspeed-bmc-bytedance-g220a.dts`** -> AI Confidence: **99.34%**
1124. **`arch/arm/boot/dts/aspeed/aspeed-bmc-facebook-greatlakes.dts`** -> AI Confidence: **99.34%**
1125. **`arch/arm/boot/dts/aspeed/aspeed-bmc-facebook-yosemite4.dts`** -> AI Confidence: **99.34%**
1126. **`arch/arm/boot/dts/aspeed/aspeed-bmc-ibm-balcones.dts`** -> AI Confidence: **99.34%**
1127. **`arch/arm/boot/dts/aspeed/aspeed-bmc-ibm-blueridge.dts`** -> AI Confidence: **99.34%**
1128. **`arch/arm/boot/dts/aspeed/aspeed-bmc-ibm-bonnell.dts`** -> AI Confidence: **99.34%**
1129. **`arch/arm/boot/dts/aspeed/aspeed-bmc-ibm-everest.dts`** -> AI Confidence: **99.34%**
1130. **`arch/arm/boot/dts/aspeed/aspeed-bmc-ibm-fuji.dts`** -> AI Confidence: **99.34%**
1131. **`arch/arm/boot/dts/aspeed/aspeed-bmc-inspur-fp5280g2.dts`** -> AI Confidence: **99.34%**
1132. **`arch/arm/boot/dts/aspeed/aspeed-bmc-inspur-nf5280m6.dts`** -> AI Confidence: **99.34%**
1133. **`arch/arm/boot/dts/aspeed/aspeed-bmc-inventec-starscream.dts`** -> AI Confidence: **99.34%**
1134. **`arch/arm/boot/dts/aspeed/aspeed-bmc-inventec-transformers.dts`** -> AI Confidence: **99.34%**
1135. **`arch/arm/boot/dts/aspeed/aspeed-bmc-opp-tacoma.dts`** -> AI Confidence: **99.34%**
1136. **`arch/arm/boot/dts/aspeed/aspeed-bmc-ufispace-ncplite.dts`** -> AI Confidence: **99.34%**
1137. **`arch/arm/boot/dts/broadcom/bcm2711-rpi-4-b.dts`** -> AI Confidence: **99.34%**
1138. **`arch/arm/boot/dts/broadcom/bcm2835-rpi-a-plus.dts`** -> AI Confidence: **99.34%**
1139. **`arch/arm/boot/dts/broadcom/bcm2835-rpi-a.dts`** -> AI Confidence: **99.34%**
1140. **`arch/arm/boot/dts/broadcom/bcm2835-rpi-b-plus.dts`** -> AI Confidence: **99.34%**
1141. **`arch/arm/boot/dts/broadcom/bcm2835-rpi-b-rev2.dts`** -> AI Confidence: **99.34%**
1142. **`arch/arm/boot/dts/broadcom/bcm2835-rpi-b.dts`** -> AI Confidence: **99.34%**
1143. **`arch/arm/boot/dts/broadcom/bcm2835-rpi-zero-w.dts`** -> AI Confidence: **99.34%**
1144. **`arch/arm/boot/dts/broadcom/bcm2835-rpi-zero.dts`** -> AI Confidence: **99.34%**
1145. **`arch/arm/boot/dts/broadcom/bcm2836-rpi-2-b.dts`** -> AI Confidence: **99.34%**
1146. **`arch/arm/boot/dts/broadcom/bcm2837-rpi-2-b.dts`** -> AI Confidence: **99.34%**
1147. **`arch/arm/boot/dts/broadcom/bcm2837-rpi-3-a-plus.dts`** -> AI Confidence: **99.34%**
1148. **`arch/arm/boot/dts/broadcom/bcm2837-rpi-3-b-plus.dts`** -> AI Confidence: **99.34%**
1149. **`arch/arm/boot/dts/broadcom/bcm2837-rpi-3-b.dts`** -> AI Confidence: **99.34%**
1150. **`arch/arm/boot/dts/broadcom/bcm2837-rpi-zero-2-w.dts`** -> AI Confidence: **99.34%**
1151. **`arch/arm/boot/dts/marvell/armada-370-c200-v2.dts`** -> AI Confidence: **99.34%**
1152. **`arch/arm/boot/dts/marvell/armada-370-rd.dts`** -> AI Confidence: **99.34%**
1153. **`arch/arm/boot/dts/microchip/at91-kizbox3_common.dtsi`** -> AI Confidence: **99.34%**
1154. **`arch/arm/boot/dts/microchip/at91-sama5d27_wlsom1.dtsi`** -> AI Confidence: **99.34%**
1155. **`arch/arm/boot/dts/microchip/at91-sama5d29_curiosity.dts`** -> AI Confidence: **99.34%**
1156. **`arch/arm/boot/dts/microchip/at91-sama5d2_icp.dts`** -> AI Confidence: **99.34%**
1157. **`arch/arm/boot/dts/microchip/at91-sama5d2_ptc_ek.dts`** -> AI Confidence: **99.34%**
1158. **`arch/arm/boot/dts/microchip/at91-sama7d65_curiosity.dts`** -> AI Confidence: **99.34%**
1159. **`arch/arm/boot/dts/microchip/at91-sama7g54_curiosity.dts`** -> AI Confidence: **99.34%**
1160. **`arch/arm/boot/dts/microchip/at91sam9261.dtsi`** -> AI Confidence: **99.34%**
1161. **`arch/arm/boot/dts/microchip/at91sam9n12.dtsi`** -> AI Confidence: **99.34%**
1162. **`arch/arm/boot/dts/microchip/at91sam9rl.dtsi`** -> AI Confidence: **99.34%**
1163. **`arch/arm/boot/dts/nvidia/tegra20-paz00.dts`** -> AI Confidence: **99.34%**
1164. **`arch/arm/boot/dts/nvidia/tegra20-ventana.dts`** -> AI Confidence: **99.34%**
1165. **`arch/arm/boot/dts/nvidia/tegra30-asus-transformer-common.dtsi`** -> AI Confidence: **99.34%**
1166. **`arch/arm/boot/dts/nxp/imx/imx6dl-prtvt7.dts`** -> AI Confidence: **99.34%**
1167. **`arch/arm/boot/dts/nxp/imx/imx6q-apalis-ixora.dts`** -> AI Confidence: **99.34%**
1168. **`arch/arm/boot/dts/nxp/imx/imx6ull-uti260b.dts`** -> AI Confidence: **99.34%**
1169. **`arch/arm/boot/dts/nxp/ls/ls1021a-tqmls1021a-mbls1021a.dts`** -> AI Confidence: **99.34%**
1170. **`arch/arm/boot/dts/qcom/qcom-apq8026-samsung-milletwifi.dts`** -> AI Confidence: **99.34%**
1171. **`arch/arm/boot/dts/qcom/qcom-apq8064-cm-qs600.dts`** -> AI Confidence: **99.34%**
1172. **`arch/arm/boot/dts/qcom/qcom-msm8974pro-oneplus-bacon.dts`** -> AI Confidence: **99.34%**
1173. **`arch/arm/boot/dts/qcom/qcom-sdx55-t55.dts`** -> AI Confidence: **99.34%**
1174. **`arch/arm/boot/dts/qcom/qcom-sdx55-telit-fn980-tlb.dts`** -> AI Confidence: **99.34%**
1175. **`arch/arm/boot/dts/qcom/qcom-sdx65-mtp.dts`** -> AI Confidence: **99.34%**
1176. **`arch/arm/boot/dts/renesas/r8a7740-armadillo800eva.dts`** -> AI Confidence: **99.34%**
1177. **`arch/arm/boot/dts/renesas/r9a06g032-rzn1d400-db.dts`** -> AI Confidence: **99.34%**
1178. **`arch/arm/boot/dts/samsung/exynos3250-artik5.dtsi`** -> AI Confidence: **99.34%**
1179. **`arch/arm/boot/dts/samsung/exynos3250-monk.dts`** -> AI Confidence: **99.34%**
1180. **`arch/arm/boot/dts/samsung/exynos3250-rinato.dts`** -> AI Confidence: **99.34%**
1181. **`arch/arm/boot/dts/samsung/exynos5250-smdk5250.dts`** -> AI Confidence: **99.34%**
1182. **`arch/arm/boot/dts/samsung/exynos5420-smdk5420.dts`** -> AI Confidence: **99.34%**
1183. **`arch/arm/boot/dts/samsung/exynos5422-samsung-k3g.dts`** -> AI Confidence: **99.34%**
1184. **`arch/arm/boot/dts/st/stm32429i-eval.dts`** -> AI Confidence: **99.34%**
1185. **`arch/arm/boot/dts/st/stm32746g-eval.dts`** -> AI Confidence: **99.34%**
1186. **`arch/arm/boot/dts/st/stm32f429-disco.dts`** -> AI Confidence: **99.34%**
1187. **`arch/arm/boot/dts/st/stm32f469-disco.dts`** -> AI Confidence: **99.34%**
1188. **`arch/arm/boot/dts/st/stm32f746-disco.dts`** -> AI Confidence: **99.34%**
1189. **`arch/arm/boot/dts/st/stm32f769-disco.dts`** -> AI Confidence: **99.34%**
1190. **`arch/arm/boot/dts/st/stm32h747i-disco.dts`** -> AI Confidence: **99.34%**
1191. **`arch/arm/boot/dts/st/stm32mp135f-dhcor-dhsbc.dts`** -> AI Confidence: **99.34%**
1192. **`arch/arm/boot/dts/st/stm32mp157a-icore-stm32mp1-ctouch2-of10.dts`** -> AI Confidence: **99.34%**
1193. **`arch/arm/boot/dts/st/stm32mp157a-icore-stm32mp1-ctouch2.dts`** -> AI Confidence: **99.34%**
1194. **`arch/arm/boot/dts/st/stm32mp157a-icore-stm32mp1-edimm2.2.dts`** -> AI Confidence: **99.34%**
1195. **`arch/arm/boot/dts/st/stm32mp157a-microgea-stm32mp1-microdev2.0-of7.dts`** -> AI Confidence: **99.34%**
1196. **`arch/arm/boot/dts/st/stm32mp157a-microgea-stm32mp1-microdev2.0.dts`** -> AI Confidence: **99.34%**
1197. **`arch/arm/boot/dts/st/stm32mp157c-dk2.dts`** -> AI Confidence: **99.34%**
1198. **`arch/arm/boot/dts/st/stm32mp157c-lxa-mc1.dts`** -> AI Confidence: **99.34%**
1199. **`arch/arm/boot/dts/st/stm32mp157c-osd32mp1-red.dts`** -> AI Confidence: **99.34%**
1200. **`arch/arm/boot/dts/ti/omap/am335x-boneblack-wireless.dts`** -> AI Confidence: **99.34%**
1201. **`arch/arm/boot/dts/ti/omap/am335x-sancloud-bbe-extended-wifi.dts`** -> AI Confidence: **99.34%**
1202. **`arch/arm/boot/dts/ti/omap/am335x-sancloud-bbe.dts`** -> AI Confidence: **99.34%**
1203. **`arch/arm/boot/dts/ti/omap/am437x-idk-evm.dts`** -> AI Confidence: **99.34%**
1204. **`arch/arm/boot/dts/ti/omap/am437x-sk-evm.dts`** -> AI Confidence: **99.34%**
1205. **`arch/arm/boot/dts/ti/omap/am43x-epos-evm.dts`** -> AI Confidence: **99.34%**
1206. **`arch/arm/boot/dts/ti/omap/omap3-ldp.dts`** -> AI Confidence: **99.34%**
1207. **`arch/arm/boot/dts/ti/omap/omap3-n900.dts`** -> AI Confidence: **99.34%**
1208. **`arch/arm/boot/dts/ti/omap/omap4-sdp.dts`** -> AI Confidence: **99.34%**
1209. **`arch/arm/include/asm/cmpxchg.h`** -> AI Confidence: **99.34%**
1210. **`arch/arm/mm/proc-syms.c`** -> AI Confidence: **99.34%**
1211. **`arch/arm/nwfpe/fpa11_cpdt.c`** -> AI Confidence: **99.34%**
1212. **`arch/arm/nwfpe/fpa11_cprt.c`** -> AI Confidence: **99.34%**
1213. **`arch/arm64/boot/dts/allwinner/sun50i-a133-liontron-h-a133l.dts`** -> AI Confidence: **99.34%**
1214. **`arch/arm64/boot/dts/allwinner/sun50i-a64-pinetab.dts`** -> AI Confidence: **99.34%**
1215. **`arch/arm64/boot/dts/allwinner/sun50i-a64-teres-i.dts`** -> AI Confidence: **99.34%**
1216. **`arch/arm64/boot/dts/allwinner/sun50i-h313-tanix-tx1.dts`** -> AI Confidence: **99.34%**
1217. **`arch/arm64/boot/dts/allwinner/sun50i-h313-x96q.dts`** -> AI Confidence: **99.34%**
1218. **`arch/arm64/boot/dts/allwinner/sun50i-h5-nanopi-r1s-h5.dts`** -> AI Confidence: **99.34%**
1219. **`arch/arm64/boot/dts/allwinner/sun50i-h5-orangepi-pc2.dts`** -> AI Confidence: **99.34%**
1220. **`arch/arm64/boot/dts/allwinner/sun50i-h618-orangepi-zero2w.dts`** -> AI Confidence: **99.34%**
1221. **`arch/arm64/boot/dts/amlogic/meson-g12a-fbx8am.dts`** -> AI Confidence: **99.34%**
1222. **`arch/arm64/boot/dts/amlogic/meson-g12a-sei510.dts`** -> AI Confidence: **99.34%**
1223. **`arch/arm64/boot/dts/amlogic/meson-g12a-u200.dts`** -> AI Confidence: **99.34%**
1224. **`arch/arm64/boot/dts/amlogic/meson-g12b-odroid-go-ultra.dts`** -> AI Confidence: **99.34%**
1225. **`arch/arm64/boot/dts/amlogic/meson-g12b-radxa-zero2.dts`** -> AI Confidence: **99.34%**
1226. **`arch/arm64/boot/dts/amlogic/meson-gxbb-kii-pro.dts`** -> AI Confidence: **99.34%**
1227. **`arch/arm64/boot/dts/amlogic/meson-gxm-ugoos-am3.dts`** -> AI Confidence: **99.34%**
1228. **`arch/arm64/boot/dts/amlogic/meson-sm1-sei610.dts`** -> AI Confidence: **99.34%**
1229. **`arch/arm64/boot/dts/exynos/exynos2200.dtsi`** -> AI Confidence: **99.34%**
1230. **`arch/arm64/boot/dts/exynos/exynos7-espresso.dts`** -> AI Confidence: **99.34%**
1231. **`arch/arm64/boot/dts/exynos/exynos7.dtsi`** -> AI Confidence: **99.34%**
1232. **`arch/arm64/boot/dts/exynos/exynos850.dtsi`** -> AI Confidence: **99.34%**
1233. **`arch/arm64/boot/dts/exynos/exynos8895-dreamlte.dts`** -> AI Confidence: **99.34%**
1234. **`arch/arm64/boot/dts/exynos/exynos8895.dtsi`** -> AI Confidence: **99.34%**
1235. **`arch/arm64/boot/dts/exynos/exynosautov920.dtsi`** -> AI Confidence: **99.34%**
1236. **`arch/arm64/boot/dts/freescale/fsl-ls1012a-tqmls1012al-mbls1012al.dts`** -> AI Confidence: **99.34%**
1237. **`arch/arm64/boot/dts/freescale/imx8mm-venice-gw7901.dts`** -> AI Confidence: **99.34%**
1238. **`arch/arm64/boot/dts/freescale/imx8mm-venice-gw7902.dts`** -> AI Confidence: **99.34%**
1239. **`arch/arm64/boot/dts/freescale/imx8mm-venice-gw7903.dts`** -> AI Confidence: **99.34%**
1240. **`arch/arm64/boot/dts/freescale/imx8mm-venice-gw7904.dts`** -> AI Confidence: **99.34%**
1241. **`arch/arm64/boot/dts/freescale/imx8mn-venice-gw7902.dts`** -> AI Confidence: **99.34%**
1242. **`arch/arm64/boot/dts/freescale/imx8mp-tqma8mpql-mba8mp-ras314.dts`** -> AI Confidence: **99.34%**
1243. **`arch/arm64/boot/dts/freescale/imx8mp-tqma8mpql-mba8mpxl.dts`** -> AI Confidence: **99.34%**
1244. **`arch/arm64/boot/dts/freescale/imx8mp-venice-gw74xx.dts`** -> AI Confidence: **99.34%**
1245. **`arch/arm64/boot/dts/freescale/imx8mq-librem5-devkit.dts`** -> AI Confidence: **99.34%**
1246. **`arch/arm64/boot/dts/freescale/imx91-tqma9131-mba91xxca.dts`** -> AI Confidence: **99.34%**
1247. **`arch/arm64/boot/dts/freescale/imx93-tqma9352-mba91xxca.dts`** -> AI Confidence: **99.34%**
1248. **`arch/arm64/boot/dts/freescale/imx93-tqma9352-mba93xxca.dts`** -> AI Confidence: **99.34%**
1249. **`arch/arm64/boot/dts/freescale/imx93-tqma9352-mba93xxla.dts`** -> AI Confidence: **99.34%**
1250. **`arch/arm64/boot/dts/freescale/imx95-15x15-evk.dts`** -> AI Confidence: **99.34%**
1251. **`arch/arm64/boot/dts/freescale/imx95-15x15-frdm.dts`** -> AI Confidence: **99.34%**
1252. **`arch/arm64/boot/dts/hisilicon/hi3660-hikey960.dts`** -> AI Confidence: **99.34%**
1253. **`arch/arm64/boot/dts/marvell/cn9130-cf-base.dts`** -> AI Confidence: **99.34%**
1254. **`arch/arm64/boot/dts/marvell/cn9130-cf-pro.dts`** -> AI Confidence: **99.34%**
1255. **`arch/arm64/boot/dts/marvell/cn9131-cf-solidwan.dts`** -> AI Confidence: **99.34%**
1256. **`arch/arm64/boot/dts/mediatek/mt7622-bananapi-bpi-r64.dts`** -> AI Confidence: **99.34%**
1257. **`arch/arm64/boot/dts/mediatek/mt7986a-bananapi-bpi-r3-mini.dts`** -> AI Confidence: **99.34%**
1258. **`arch/arm64/boot/dts/mediatek/mt7986a-bananapi-bpi-r3.dts`** -> AI Confidence: **99.34%**
1259. **`arch/arm64/boot/dts/mediatek/mt8365-evk.dts`** -> AI Confidence: **99.34%**
1260. **`arch/arm64/boot/dts/nvidia/tegra210-p2894.dtsi`** -> AI Confidence: **99.34%**
1261. **`arch/arm64/boot/dts/qcom/hamoa-iot-som.dtsi`** -> AI Confidence: **99.34%**
1262. **`arch/arm64/boot/dts/qcom/msm8916-acer-a1-724.dts`** -> AI Confidence: **99.34%**
1263. **`arch/arm64/boot/dts/qcom/msm8916-alcatel-idol347.dts`** -> AI Confidence: **99.34%**
1264. **`arch/arm64/boot/dts/qcom/msm8916-asus-z00l.dts`** -> AI Confidence: **99.34%**
1265. **`arch/arm64/boot/dts/qcom/msm8916-gplus-fl8005a.dts`** -> AI Confidence: **99.34%**
1266. **`arch/arm64/boot/dts/qcom/msm8916-huawei-g7.dts`** -> AI Confidence: **99.34%**
1267. **`arch/arm64/boot/dts/qcom/msm8916-longcheer-l8150.dts`** -> AI Confidence: **99.34%**
1268. **`arch/arm64/boot/dts/qcom/msm8916-samsung-serranove.dts`** -> AI Confidence: **99.34%**
1269. **`arch/arm64/boot/dts/qcom/msm8916-wingtech-wt88047.dts`** -> AI Confidence: **99.34%**
1270. **`arch/arm64/boot/dts/qcom/msm8917-xiaomi-riva.dts`** -> AI Confidence: **99.34%**
1271. **`arch/arm64/boot/dts/qcom/msm8939-asus-z00t.dts`** -> AI Confidence: **99.34%**
1272. **`arch/arm64/boot/dts/qcom/msm8939-samsung-a7.dts`** -> AI Confidence: **99.34%**
1273. **`arch/arm64/boot/dts/qcom/msm8996pro-xiaomi-natrium.dts`** -> AI Confidence: **99.34%**
1274. **`arch/arm64/boot/dts/qcom/qcs615-ride.dts`** -> AI Confidence: **99.34%**
1275. **`arch/arm64/boot/dts/qcom/qcs8300-ride.dts`** -> AI Confidence: **99.34%**
1276. **`arch/arm64/boot/dts/qcom/qcs8550-aim300-aiot.dts`** -> AI Confidence: **99.34%**
1277. **`arch/arm64/boot/dts/qcom/sa8155p-adp.dts`** -> AI Confidence: **99.34%**
1278. **`arch/arm64/boot/dts/qcom/sa8540p-ride.dts`** -> AI Confidence: **99.34%**
1279. **`arch/arm64/boot/dts/qcom/sar2130p-qar2130p.dts`** -> AI Confidence: **99.34%**
1280. **`arch/arm64/boot/dts/qcom/sc7180-trogdor-kingoftown.dts`** -> AI Confidence: **99.34%**
1281. **`arch/arm64/boot/dts/qcom/sc7180-trogdor-lazor-limozeen-r10.dts`** -> AI Confidence: **99.34%**
1282. **`arch/arm64/boot/dts/qcom/sc7180-trogdor-lazor-limozeen-r4.dts`** -> AI Confidence: **99.34%**
1283. **`arch/arm64/boot/dts/qcom/sc7180-trogdor-lazor-limozeen-r9.dts`** -> AI Confidence: **99.34%**
1284. **`arch/arm64/boot/dts/qcom/sc8280xp-crd.dts`** -> AI Confidence: **99.34%**
1285. **`arch/arm64/boot/dts/qcom/sc8280xp-microsoft-arcata.dts`** -> AI Confidence: **99.34%**
1286. **`arch/arm64/boot/dts/qcom/sdm845-mtp.dts`** -> AI Confidence: **99.34%**
1287. **`arch/arm64/boot/dts/qcom/sdx75-idp.dts`** -> AI Confidence: **99.34%**
1288. **`arch/arm64/boot/dts/qcom/sm6125-sony-xperia-seine-pdx201.dts`** -> AI Confidence: **99.34%**
1289. **`arch/arm64/boot/dts/qcom/sm6350-sony-xperia-lena-pdx213.dts`** -> AI Confidence: **99.34%**
1290. **`arch/arm64/boot/dts/qcom/sm6375-sony-xperia-murray-pdx225.dts`** -> AI Confidence: **99.34%**
1291. **`arch/arm64/boot/dts/qcom/x1e001de-devkit.dts`** -> AI Confidence: **99.34%**
1292. **`arch/arm64/boot/dts/qcom/x1e80100-lenovo-yoga-slim7x.dts`** -> AI Confidence: **99.34%**
1293. **`arch/arm64/boot/dts/qcom/x1e80100-medion-sprchrgd-14-s1.dts`** -> AI Confidence: **99.34%**
1294. **`arch/arm64/boot/dts/qcom/x1e80100-qcp.dts`** -> AI Confidence: **99.34%**
1295. **`arch/arm64/boot/dts/renesas/r9a07g044l2-smarc.dts`** -> AI Confidence: **99.34%**
1296. **`arch/arm64/boot/dts/renesas/r9a07g054l2-smarc.dts`** -> AI Confidence: **99.34%**
1297. **`arch/arm64/boot/dts/renesas/r9a09g057h44-rzv2h-evk.dts`** -> AI Confidence: **99.34%**
1298. **`arch/arm64/boot/dts/renesas/rzg3s-smarc-som.dtsi`** -> AI Confidence: **99.34%**
1299. **`arch/arm64/boot/dts/rockchip/rk3326-gameforce-chi.dts`** -> AI Confidence: **99.34%**
1300. **`arch/arm64/boot/dts/rockchip/rk3328-rock-pi-e.dts`** -> AI Confidence: **99.34%**
1301. **`arch/arm64/boot/dts/rockchip/rk3368-lba3368.dts`** -> AI Confidence: **99.34%**
1302. **`arch/arm64/boot/dts/rockchip/rk3399-firefly.dts`** -> AI Confidence: **99.34%**
1303. **`arch/arm64/boot/dts/rockchip/rk3399-orangepi.dts`** -> AI Confidence: **99.34%**
1304. **`arch/arm64/boot/dts/rockchip/rk3399-pinebook-pro.dts`** -> AI Confidence: **99.34%**
1305. **`arch/arm64/boot/dts/rockchip/rk3562-evb2-v10.dts`** -> AI Confidence: **99.34%**
1306. **`arch/arm64/boot/dts/rockchip/rk3566-box-demo.dts`** -> AI Confidence: **99.34%**
1307. **`arch/arm64/boot/dts/rockchip/rk3566-lubancat-1.dts`** -> AI Confidence: **99.34%**
1308. **`arch/arm64/boot/dts/rockchip/rk3566-odroid-m1s.dts`** -> AI Confidence: **99.34%**
1309. **`arch/arm64/boot/dts/rockchip/rk3566-quartz64-a.dts`** -> AI Confidence: **99.34%**
1310. **`arch/arm64/boot/dts/rockchip/rk3566-quartz64-b.dts`** -> AI Confidence: **99.34%**
1311. **`arch/arm64/boot/dts/rockchip/rk3566-roc-pc.dts`** -> AI Confidence: **99.34%**
1312. **`arch/arm64/boot/dts/rockchip/rk3566-rock-3c.dts`** -> AI Confidence: **99.34%**
1313. **`arch/arm64/boot/dts/rockchip/rk3566-soquartz-blade.dts`** -> AI Confidence: **99.34%**
1314. **`arch/arm64/boot/dts/rockchip/rk3568-bpi-r2-pro.dts`** -> AI Confidence: **99.34%**
1315. **`arch/arm64/boot/dts/rockchip/rk3568-evb1-v10.dts`** -> AI Confidence: **99.34%**
1316. **`arch/arm64/boot/dts/rockchip/rk3568-lubancat-2.dts`** -> AI Confidence: **99.34%**
1317. **`arch/arm64/boot/dts/rockchip/rk3568-mecsbc.dts`** -> AI Confidence: **99.34%**
1318. **`arch/arm64/boot/dts/rockchip/rk3568-odroid-m1.dts`** -> AI Confidence: **99.34%**
1319. **`arch/arm64/boot/dts/rockchip/rk3568-photonicat.dts`** -> AI Confidence: **99.34%**
1320. **`arch/arm64/boot/dts/rockchip/rk3568-radxa-cm3j.dtsi`** -> AI Confidence: **99.34%**
1321. **`arch/arm64/boot/dts/rockchip/rk3568-roc-pc.dts`** -> AI Confidence: **99.34%**
1322. **`arch/arm64/boot/dts/rockchip/rk3568-rock-3a.dts`** -> AI Confidence: **99.34%**
1323. **`arch/arm64/boot/dts/rockchip/rk3568-rock-3b.dts`** -> AI Confidence: **99.34%**
1324. **`arch/arm64/boot/dts/rockchip/rk3568-wolfvision-pf5-display.dtsi`** -> AI Confidence: **99.34%**
1325. **`arch/arm64/boot/dts/rockchip/rk3576-luckfox-core3576.dtsi`** -> AI Confidence: **99.34%**
1326. **`arch/arm64/boot/dts/rockchip/rk3582-radxa-e52c.dts`** -> AI Confidence: **99.34%**
1327. **`arch/arm64/boot/dts/rockchip/rk3588-armsom-sige7.dts`** -> AI Confidence: **99.34%**
1328. **`arch/arm64/boot/dts/rockchip/rk3588-armsom-w3.dts`** -> AI Confidence: **99.34%**
1329. **`arch/arm64/boot/dts/rockchip/rk3588-h96-max-v58.dts`** -> AI Confidence: **99.34%**
1330. **`arch/arm64/boot/dts/rockchip/rk3588-orangepi-5-max.dts`** -> AI Confidence: **99.34%**
1331. **`arch/arm64/boot/dts/rockchip/rk3588-orangepi-5-plus.dts`** -> AI Confidence: **99.34%**
1332. **`arch/arm64/boot/dts/rockchip/rk3588-orangepi-5-ultra.dts`** -> AI Confidence: **99.34%**
1333. **`arch/arm64/boot/dts/rockchip/rk3588-quartzpro64.dts`** -> AI Confidence: **99.34%**
1334. **`arch/arm64/boot/dts/rockchip/rk3588-tiger.dtsi`** -> AI Confidence: **99.34%**
1335. **`arch/arm64/boot/dts/rockchip/rk3588s-coolpi-4b.dts`** -> AI Confidence: **99.34%**
1336. **`arch/arm64/boot/dts/rockchip/rk3588s-orangepi-cm5.dtsi`** -> AI Confidence: **99.34%**
1337. **`arch/arm64/boot/dts/rockchip/rk3588s-radxa-cm5.dtsi`** -> AI Confidence: **99.34%**
1338. **`arch/arm64/boot/dts/rockchip/rk3588s-rock-5a.dts`** -> AI Confidence: **99.34%**
1339. **`arch/arm64/boot/dts/rockchip/rk3588s-rock-5c.dts`** -> AI Confidence: **99.34%**
1340. **`arch/arm64/boot/dts/ti/k3-am62-pocketbeagle2.dts`** -> AI Confidence: **99.34%**
1341. **`arch/arm64/boot/dts/ti/k3-am62a7-sk.dts`** -> AI Confidence: **99.34%**
1342. **`arch/arm64/boot/dts/ti/k3-am62d2-evm.dts`** -> AI Confidence: **99.34%**
1343. **`arch/arm64/boot/dts/ti/k3-am62p5-sk.dts`** -> AI Confidence: **99.34%**
1344. **`arch/arm64/boot/dts/ti/k3-am67a-kontron-sa67-base.dts`** -> AI Confidence: **99.34%**
1345. **`arch/arm64/boot/dts/ti/k3-am68-phyboard-izar.dts`** -> AI Confidence: **99.34%**
1346. **`arch/arm64/boot/dts/ti/k3-am68-sk-base-board.dts`** -> AI Confidence: **99.34%**
1347. **`arch/arm64/boot/dts/ti/k3-am69-sk.dts`** -> AI Confidence: **99.34%**
1348. **`arch/arm64/boot/dts/ti/k3-j7200-common-proc-board.dts`** -> AI Confidence: **99.34%**
1349. **`arch/arm64/boot/dts/ti/k3-j721e-common-proc-board.dts`** -> AI Confidence: **99.34%**
1350. **`arch/arm64/boot/dts/ti/k3-j721e-sk.dts`** -> AI Confidence: **99.34%**
1351. **`arch/arm64/boot/dts/ti/k3-j721s2-common-proc-board.dts`** -> AI Confidence: **99.34%**
1352. **`arch/arm64/boot/dts/ti/k3-j722s-evm.dts`** -> AI Confidence: **99.34%**
1353. **`arch/arm64/boot/dts/xilinx/zynqmp-zc1751-xm015-dc1.dts`** -> AI Confidence: **99.34%**
1354. **`arch/arm64/boot/dts/xilinx/zynqmp-zcu104-revA.dts`** -> AI Confidence: **99.34%**
1355. **`arch/arm64/boot/dts/xilinx/zynqmp-zcu104-revC.dts`** -> AI Confidence: **99.34%**
1356. **`arch/arm64/boot/dts/xilinx/zynqmp-zcu106-revA.dts`** -> AI Confidence: **99.34%**
1357. **`arch/arm64/boot/dts/xilinx/zynqmp-zcu111-revA.dts`** -> AI Confidence: **99.34%**
1358. **`arch/arm64/include/asm/asm-uaccess.h`** -> AI Confidence: **99.34%**
1359. **`arch/arm64/include/asm/pgtable-prot.h`** -> AI Confidence: **99.34%**
1360. **`arch/hexagon/kernel/module.c`** -> AI Confidence: **99.34%**
1361. **`arch/loongarch/include/asm/asmmacro.h`** -> AI Confidence: **99.34%**
1362. **`arch/loongarch/include/asm/futex.h`** -> AI Confidence: **99.34%**
1363. **`arch/loongarch/kernel/mem.c`** -> AI Confidence: **99.34%**
1364. **`arch/m68k/atari/debug.c`** -> AI Confidence: **99.34%**
1365. **`arch/m68k/include/asm/io_mm.h`** -> AI Confidence: **99.34%**
1366. **`arch/m68k/include/asm/uaccess.h`** -> AI Confidence: **99.34%**
1367. **`arch/microblaze/include/asm/uaccess.h`** -> AI Confidence: **99.34%**
1368. **`arch/microblaze/kernel/cpu/cpuinfo-static.c`** -> AI Confidence: **99.34%**
1369. **`arch/mips/bcm47xx/time.c`** -> AI Confidence: **99.34%**
1370. **`arch/mips/boot/dts/img/pistachio.dtsi`** -> AI Confidence: **99.34%**
1371. **`arch/mips/boot/dts/ingenic/cu1000-neo.dts`** -> AI Confidence: **99.34%**
1372. **`arch/mips/boot/dts/ingenic/cu1830-neo.dts`** -> AI Confidence: **99.34%**
1373. **`arch/mips/boot/dts/ingenic/rs90.dts`** -> AI Confidence: **99.34%**
1374. **`arch/mips/fw/arc/cmdline.c`** -> AI Confidence: **99.34%**
1375. **`arch/mips/include/asm/asmmacro.h`** -> AI Confidence: **99.34%**
1376. **`arch/mips/include/asm/sn/addrs.h`** -> AI Confidence: **99.34%**
1377. **`arch/mips/include/asm/stackframe.h`** -> AI Confidence: **99.34%**
1378. **`arch/mips/include/asm/uaccess.h`** -> AI Confidence: **99.34%**
1379. **`arch/mips/lantiq/xway/prom.c`** -> AI Confidence: **99.34%**
1380. **`arch/mips/loongson64/env.c`** -> AI Confidence: **99.34%**
1381. **`arch/mips/math-emu/ieee754d.c`** -> AI Confidence: **99.34%**
1382. **`arch/mips/sgi-ip27/ip27-xtalk.c`** -> AI Confidence: **99.34%**
1383. **`arch/parisc/include/asm/assembly.h`** -> AI Confidence: **99.34%**
1384. **`arch/parisc/math-emu/denormal.c`** -> AI Confidence: **99.34%**
1385. **`arch/powerpc/boot/addnote.c`** -> AI Confidence: **99.34%**
1386. **`arch/powerpc/boot/hack-coff.c`** -> AI Confidence: **99.34%**
1387. **`arch/powerpc/boot/simpleboot.c`** -> AI Confidence: **99.34%**
1388. **`arch/powerpc/boot/stdio.c`** -> AI Confidence: **99.34%**
1389. **`arch/powerpc/kernel/ptrace/ptrace32.c`** -> AI Confidence: **99.34%**
1390. **`arch/powerpc/kvm/e500_emulate.c`** -> AI Confidence: **99.34%**
1391. **`arch/powerpc/math-emu/mtfsf.c`** -> AI Confidence: **99.34%**
1392. **`arch/powerpc/perf/power5+-pmu.c`** -> AI Confidence: **99.34%**
1393. **`arch/powerpc/perf/power5-pmu.c`** -> AI Confidence: **99.34%**
1394. **`arch/powerpc/perf/power6-pmu.c`** -> AI Confidence: **99.34%**
1395. **`arch/powerpc/perf/ppc970-pmu.c`** -> AI Confidence: **99.34%**
1396. **`arch/powerpc/xmon/ppc-dis.c`** -> AI Confidence: **99.34%**
1397. **`arch/riscv/boot/dts/allwinner/sun20i-d1-nezha.dts`** -> AI Confidence: **99.34%**
1398. **`arch/riscv/include/asm/errata_list.h`** -> AI Confidence: **99.34%**
1399. **`arch/riscv/include/asm/futex.h`** -> AI Confidence: **99.34%**
1400. **`arch/s390/kvm/trace.h`** -> AI Confidence: **99.34%**
1401. **`arch/sh/drivers/pci/fixups-snapgear.c`** -> AI Confidence: **99.34%**
1402. **`arch/sh/include/asm/futex.h`** -> AI Confidence: **99.34%**
1403. **`arch/sparc/kernel/adi_64.c`** -> AI Confidence: **99.34%**
1404. **`arch/x86/boot/compressed/mkpiggy.c`** -> AI Confidence: **99.34%**
1405. **`arch/x86/include/asm/cmpxchg.h`** -> AI Confidence: **99.34%**
1406. **`arch/x86/include/asm/futex.h`** -> AI Confidence: **99.34%**
1407. **`arch/x86/include/asm/highmem.h`** -> AI Confidence: **99.34%**
1408. **`arch/x86/include/asm/unistd.h`** -> AI Confidence: **99.34%**
1409. **`arch/x86/math-emu/fpu_etc.c`** -> AI Confidence: **99.34%**
1410. **`arch/x86/math-emu/load_store.c`** -> AI Confidence: **99.34%**
1411. **`arch/x86/math-emu/poly_2xm1.c`** -> AI Confidence: **99.34%**
1412. **`arch/x86/math-emu/poly_l2.c`** -> AI Confidence: **99.34%**
1413. **`arch/x86/math-emu/poly_sin.c`** -> AI Confidence: **99.34%**
1414. **`arch/x86/math-emu/poly_tan.c`** -> AI Confidence: **99.34%**
1415. **`arch/x86/math-emu/reg_add_sub.c`** -> AI Confidence: **99.34%**
1416. **`arch/x86/net/bpf_jit_comp32.c`** -> AI Confidence: **99.34%**
1417. **`arch/x86/pci/olpc.c`** -> AI Confidence: **99.34%**
1418. **`block/partitions/amiga.c`** -> AI Confidence: **99.34%**
1419. **`drivers/accessibility/speakup/makemapdata.c`** -> AI Confidence: **99.34%**
1420. **`drivers/accessibility/speakup/thread.c`** -> AI Confidence: **99.34%**
1421. **`drivers/acpi/acpica/dscontrol.c`** -> AI Confidence: **99.34%**
1422. **`drivers/acpi/acpica/exfield.c`** -> AI Confidence: **99.34%**
1423. **`drivers/acpi/acpica/exfldio.c`** -> AI Confidence: **99.34%**
1424. **`drivers/acpi/acpica/exoparg2.c`** -> AI Confidence: **99.34%**
1425. **`drivers/acpi/acpica/exoparg3.c`** -> AI Confidence: **99.34%**
1426. **`drivers/acpi/acpica/exprep.c`** -> AI Confidence: **99.34%**
1427. **`drivers/acpi/acpica/exresnte.c`** -> AI Confidence: **99.34%**
1428. **`drivers/acpi/acpica/exresolv.c`** -> AI Confidence: **99.34%**
1429. **`drivers/acpi/acpica/exresop.c`** -> AI Confidence: **99.34%**
1430. **`drivers/acpi/acpica/nsaccess.c`** -> AI Confidence: **99.34%**
1431. **`drivers/acpi/acpica/nseval.c`** -> AI Confidence: **99.34%**
1432. **`drivers/acpi/acpica/nsload.c`** -> AI Confidence: **99.34%**
1433. **`drivers/acpi/acpica/psobject.c`** -> AI Confidence: **99.34%**
1434. **`drivers/acpi/acpica/psopinfo.c`** -> AI Confidence: **99.34%**
1435. **`drivers/acpi/acpica/psxface.c`** -> AI Confidence: **99.34%**
1436. **`drivers/acpi/acpica/utxfinit.c`** -> AI Confidence: **99.34%**
1437. **`drivers/clk/mvebu/ap806-system-controller.c`** -> AI Confidence: **99.34%**
1438. **`drivers/gpu/drm/amd/display/dc/bios/dce60/command_table_helper_dce60.c`** -> AI Confidence: **99.34%**
1439. **`drivers/gpu/drm/amd/display/dc/bios/dce80/command_table_helper_dce80.c`** -> AI Confidence: **99.34%**
1440. **`drivers/gpu/drm/amd/display/dc/dml/dcn302/dcn302_fpu.c`** -> AI Confidence: **99.34%**
1441. **`drivers/gpu/drm/amd/display/dc/dml/dcn303/dcn303_fpu.c`** -> AI Confidence: **99.34%**
1442. **`drivers/gpu/drm/amd/display/dc/dml/dcn321/dcn321_fpu.c`** -> AI Confidence: **99.34%**
1443. **`drivers/gpu/drm/i915/display/i9xx_display_sr.c`** -> AI Confidence: **99.34%**
1444. **`drivers/gpu/drm/radeon/atombios_crtc.c`** -> AI Confidence: **99.34%**
1445. **`drivers/hid/hid-samsung.c`** -> AI Confidence: **99.34%**
1446. **`drivers/hid/hid-twinhan.c`** -> AI Confidence: **99.34%**
1447. **`drivers/hwmon/pmbus/ltc2978.c`** -> AI Confidence: **99.34%**
1448. **`drivers/infiniband/hw/hfi1/pcie.c`** -> AI Confidence: **99.34%**
1449. **`drivers/infiniband/hw/mthca/mthca_reset.c`** -> AI Confidence: **99.34%**
1450. **`drivers/input/joystick/db9.c`** -> AI Confidence: **99.34%**
1451. **`drivers/input/serio/hil_mlc.c`** -> AI Confidence: **99.34%**
1452. **`drivers/input/serio/i8042.h`** -> AI Confidence: **99.34%**
1453. **`drivers/input/touchscreen/elo.c`** -> AI Confidence: **99.34%**
1454. **`drivers/isdn/hardware/mISDN/isdnhdlc.c`** -> AI Confidence: **99.34%**
1455. **`drivers/isdn/hardware/mISDN/mISDNisar.c`** -> AI Confidence: **99.34%**
1456. **`drivers/isdn/mISDN/dsp_cmx.c`** -> AI Confidence: **99.34%**
1457. **`drivers/media/platform/qcom/venus/venc_ctrls.c`** -> AI Confidence: **99.34%**
1458. **`drivers/media/usb/pvrusb2/pvrusb2-dvb.c`** -> AI Confidence: **99.34%**
1459. **`drivers/media/usb/pwc/pwc-dec23.c`** -> AI Confidence: **99.34%**
1460. **`drivers/mfd/cs47l24-tables.c`** -> AI Confidence: **99.34%**
1461. **`drivers/mfd/wm5102-tables.c`** -> AI Confidence: **99.34%**
1462. **`drivers/mfd/wm5110-tables.c`** -> AI Confidence: **99.34%**
1463. **`drivers/mfd/wm8998-tables.c`** -> AI Confidence: **99.34%**
1464. **`drivers/misc/altera-stapl/altera-jtag.c`** -> AI Confidence: **99.34%**
1465. **`drivers/net/can/softing/softing_fw.c`** -> AI Confidence: **99.34%**
1466. **`drivers/net/ethernet/dec/tulip/media.c`** -> AI Confidence: **99.34%**
1467. **`drivers/net/ethernet/intel/i40e/i40e_debugfs.c`** -> AI Confidence: **99.34%**
1468. **`drivers/net/ethernet/mellanox/mlx4/reset.c`** -> AI Confidence: **99.34%**
1469. **`drivers/net/ethernet/qualcomm/ppe/ppe_debugfs.c`** -> AI Confidence: **99.34%**
1470. **`drivers/net/fddi/skfp/pcmplc.c`** -> AI Confidence: **99.34%**
1471. **`drivers/net/fddi/skfp/pmf.c`** -> AI Confidence: **99.34%**
1472. **`drivers/net/wireless/intersil/p54/fwio.c`** -> AI Confidence: **99.34%**
1473. **`drivers/pci/syscall.c`** -> AI Confidence: **99.34%**
1474. **`drivers/s390/crypto/pkey_pckmo.c`** -> AI Confidence: **99.34%**
1475. **`drivers/soc/amlogic/meson-mx-socinfo.c`** -> AI Confidence: **99.34%**
1476. **`drivers/soc/fsl/qe/usb.c`** -> AI Confidence: **99.34%**
1477. **`drivers/soc/tegra/fuse/speedo-tegra124.c`** -> AI Confidence: **99.34%**
1478. **`drivers/soc/tegra/fuse/speedo-tegra20.c`** -> AI Confidence: **99.34%**
1479. **`drivers/soc/tegra/fuse/speedo-tegra210.c`** -> AI Confidence: **99.34%**
1480. **`drivers/soc/tegra/fuse/speedo-tegra30.c`** -> AI Confidence: **99.34%**
1481. **`drivers/staging/media/ipu3/ipu3-css-fw.c`** -> AI Confidence: **99.34%**
1482. **`drivers/tty/vt/conmakehash.c`** -> AI Confidence: **99.34%**
1483. **`drivers/usb/host/uhci-debug.c`** -> AI Confidence: **99.34%**
1484. **`drivers/usb/misc/ldusb.c`** -> AI Confidence: **99.34%**
1485. **`drivers/usb/typec/tipd/trace.h`** -> AI Confidence: **99.34%**
1486. **`drivers/video/fbdev/atafb_iplan2p2.c`** -> AI Confidence: **99.34%**
1487. **`drivers/video/fbdev/atafb_iplan2p4.c`** -> AI Confidence: **99.34%**
1488. **`drivers/video/fbdev/atafb_iplan2p8.c`** -> AI Confidence: **99.34%**
1489. **`drivers/video/fbdev/aty/radeon_pm.c`** -> AI Confidence: **99.34%**
1490. **`drivers/video/fbdev/core/fb_ddc.c`** -> AI Confidence: **99.34%**
1491. **`drivers/video/fbdev/kyro/STG4000InitDevice.c`** -> AI Confidence: **99.34%**
1492. **`drivers/video/fbdev/riva/nv_driver.c`** -> AI Confidence: **99.34%**
1493. **`drivers/video/fbdev/riva/riva_hw.c`** -> AI Confidence: **99.34%**
1494. **`drivers/video/fbdev/via/viafbdev.c`** -> AI Confidence: **99.34%**
1495. **`drivers/xen/xen-pciback/xenbus.c`** -> AI Confidence: **99.34%**
1496. **`fs/btrfs/tests/extent-buffer-tests.c`** -> AI Confidence: **99.34%**
1497. **`fs/jbd2/checkpoint.c`** -> AI Confidence: **99.34%**
1498. **`fs/jbd2/recovery.c`** -> AI Confidence: **99.34%**
1499. **`fs/jfs/jfs_extent.c`** -> AI Confidence: **99.34%**
1500. **`fs/orangefs/orangefs-utils.c`** -> AI Confidence: **99.34%**
1501. **`fs/proc/bootconfig.c`** -> AI Confidence: **99.34%**
1502. **`fs/smb/server/unicode.c`** -> AI Confidence: **99.34%**
1503. **`include/acpi/platform/acenvex.h`** -> AI Confidence: **99.34%**
1504. **`include/linux/bits.h`** -> AI Confidence: **99.34%**
1505. **`include/linux/compiler_types.h`** -> AI Confidence: **99.34%**
1506. **`include/linux/iopoll.h`** -> AI Confidence: **99.34%**
1507. **`include/linux/packing.h`** -> AI Confidence: **99.34%**
1508. **`kernel/kstack_erase.c`** -> AI Confidence: **99.34%**
1509. **`mm/msync.c`** -> AI Confidence: **99.34%**
1510. **`mm/pagewalk.c`** -> AI Confidence: **99.34%**
1511. **`net/core/stream.c`** -> AI Confidence: **99.34%**
1512. **`samples/pfsm/pfsm-wakeup.c`** -> AI Confidence: **99.34%**
1513. **`scripts/ipe/polgen/polgen.c`** -> AI Confidence: **99.34%**
1514. **`sound/isa/wavefront/wavefront_midi.c`** -> AI Confidence: **99.34%**
1515. **`sound/pci/ac97/ac97_proc.c`** -> AI Confidence: **99.34%**
1516. **`sound/soc/qcom/qdsp6/q6dsp-common.c`** -> AI Confidence: **99.34%**
1517. **`tools/include/linux/bits.h`** -> AI Confidence: **99.34%**
1518. **`tools/include/uapi/asm/bpf_perf_event.h`** -> AI Confidence: **99.34%**
1519. **`tools/perf/arch/x86/util/unwind-libunwind.c`** -> AI Confidence: **99.34%**
1520. **`tools/perf/util/zlib.c`** -> AI Confidence: **99.34%**
1521. **`tools/testing/selftests/bpf/prog_tests/btf_sysfs.c`** -> AI Confidence: **99.34%**
1522. **`tools/testing/selftests/bpf/prog_tests/connect_ping.c`** -> AI Confidence: **99.34%**
1523. **`tools/testing/selftests/bpf/prog_tests/sock_destroy.c`** -> AI Confidence: **99.34%**
1524. **`tools/testing/selftests/bpf/prog_tests/sockopt_sk.c`** -> AI Confidence: **99.34%**
1525. **`tools/testing/selftests/bpf/prog_tests/test_bpffs.c`** -> AI Confidence: **99.34%**
1526. **`tools/testing/selftests/coredump/coredump_socket_protocol_test.c`** -> AI Confidence: **99.34%**
1527. **`tools/testing/selftests/coredump/coredump_socket_test.c`** -> AI Confidence: **99.34%**
1528. **`tools/testing/selftests/kvm/x86/xcr0_cpuid_test.c`** -> AI Confidence: **99.34%**
1529. **`tools/testing/selftests/net/proc_net_pktgen.c`** -> AI Confidence: **99.34%**
1530. **`tools/testing/selftests/powerpc/nx-gzip/include/nx_dbg.h`** -> AI Confidence: **99.34%**
1531. **`tools/testing/selftests/powerpc/signal/sig_sc_double_restart.c`** -> AI Confidence: **99.34%**
1532. **`tools/testing/selftests/rseq/syscall_errors_test.c`** -> AI Confidence: **99.34%**
1533. **`tools/testing/selftests/sync/sync_stress_merge.c`** -> AI Confidence: **99.34%**
1534. **`tools/tracing/rtla/src/rtla.c`** -> AI Confidence: **99.34%**
1535. **`tools/verification/rv/src/rv.c`** -> AI Confidence: **99.34%**
1536. **`tools/arch/x86/lib/insn.c`** -> AI Confidence: **99.33%**
1537. **`scripts/patch-kernel`** -> AI Confidence: **99.32%**
1538. **`tools/testing/selftests/cpufreq/module.sh`** -> AI Confidence: **99.32%**
1539. **`arch/alpha/include/asm/bug.h`** -> AI Confidence: **99.32%**
1540. **`arch/alpha/kernel/es1888.c`** -> AI Confidence: **99.32%**
1541. **`arch/arc/include/asm/elf.h`** -> AI Confidence: **99.32%**
1542. **`arch/arc/include/asm/pgtable-levels.h`** -> AI Confidence: **99.32%**
1543. **`arch/arm/boot/dts/allwinner/sun4i-a10-ba10-tvbox.dts`** -> AI Confidence: **99.32%**
1544. **`arch/arm/boot/dts/allwinner/sun4i-a10-hackberry.dts`** -> AI Confidence: **99.32%**
1545. **`arch/arm/boot/dts/allwinner/sun4i-a10-hyundai-a7hd.dts`** -> AI Confidence: **99.32%**
1546. **`arch/arm/boot/dts/allwinner/sun4i-a10-jesurun-q5.dts`** -> AI Confidence: **99.32%**
1547. **`arch/arm/boot/dts/allwinner/sun4i-a10-marsboard.dts`** -> AI Confidence: **99.32%**
1548. **`arch/arm/boot/dts/allwinner/sun4i-a10-mini-xplus.dts`** -> AI Confidence: **99.32%**
1549. **`arch/arm/boot/dts/allwinner/sun4i-a10-mk802.dts`** -> AI Confidence: **99.32%**
1550. **`arch/arm/boot/dts/allwinner/sun4i-a10-mk802ii.dts`** -> AI Confidence: **99.32%**
1551. **`arch/arm/boot/dts/allwinner/sun4i-a10-olinuxino-lime.dts`** -> AI Confidence: **99.32%**
1552. **`arch/arm/boot/dts/allwinner/sun5i-a10s-auxtek-t003.dts`** -> AI Confidence: **99.32%**
1553. **`arch/arm/boot/dts/allwinner/sun5i-a10s-auxtek-t004.dts`** -> AI Confidence: **99.32%**
1554. **`arch/arm/boot/dts/allwinner/sun5i-a10s-mk802.dts`** -> AI Confidence: **99.32%**
1555. **`arch/arm/boot/dts/allwinner/sun5i-a10s-r7-tv-dongle.dts`** -> AI Confidence: **99.32%**
1556. **`arch/arm/boot/dts/allwinner/sun5i-a13-olinuxino-micro.dts`** -> AI Confidence: **99.32%**
1557. **`arch/arm/boot/dts/allwinner/sun5i-a13-utoo-p66.dts`** -> AI Confidence: **99.32%**
1558. **`arch/arm/boot/dts/allwinner/sun6i-a31-app4-evb1.dts`** -> AI Confidence: **99.32%**
1559. **`arch/arm/boot/dts/allwinner/sun6i-a31-colombus.dts`** -> AI Confidence: **99.32%**
1560. **`arch/arm/boot/dts/allwinner/sun6i-a31-i7.dts`** -> AI Confidence: **99.32%**
1561. **`arch/arm/boot/dts/allwinner/sun6i-a31s-sinovoip-bpi-m2.dts`** -> AI Confidence: **99.32%**
1562. **`arch/arm/boot/dts/allwinner/sun7i-a20-icnova-a20-adb4006.dts`** -> AI Confidence: **99.32%**
1563. **`arch/arm/boot/dts/allwinner/sun8i-a33-vstar.dts`** -> AI Confidence: **99.32%**
1564. **`arch/arm/boot/dts/allwinner/sun8i-a83t-allwinner-h8homlet-v2.dts`** -> AI Confidence: **99.32%**
1565. **`arch/arm/boot/dts/allwinner/sun8i-a83t-bananapi-m3.dts`** -> AI Confidence: **99.32%**
1566. **`arch/arm/boot/dts/allwinner/sun8i-a83t-cubietruck-plus.dts`** -> AI Confidence: **99.32%**
1567. **`arch/arm/boot/dts/allwinner/sun8i-h3-nanopi-neo-air.dts`** -> AI Confidence: **99.32%**
1568. **`arch/arm/boot/dts/allwinner/sun8i-r16-bananapi-m2m.dts`** -> AI Confidence: **99.32%**
1569. **`arch/arm/boot/dts/allwinner/sun8i-r40-feta40i.dtsi`** -> AI Confidence: **99.32%**
1570. **`arch/arm/boot/dts/allwinner/sun8i-r40-oka40i-c.dts`** -> AI Confidence: **99.32%**
1571. **`arch/arm/boot/dts/allwinner/sun9i-a80-cubieboard4.dts`** -> AI Confidence: **99.32%**
1572. **`arch/arm/boot/dts/allwinner/sun9i-a80-optimus.dts`** -> AI Confidence: **99.32%**
1573. **`arch/arm/boot/dts/allwinner/suniv-f1c200s-popstick-v1.1.dts`** -> AI Confidence: **99.32%**
1574. **`arch/arm/boot/dts/amlogic/meson8b-ec100.dts`** -> AI Confidence: **99.32%**
1575. **`arch/arm/boot/dts/amlogic/meson8m2-mxiii-plus.dts`** -> AI Confidence: **99.32%**
1576. **`arch/arm/boot/dts/aspeed/aspeed-ast2600-evb.dts`** -> AI Confidence: **99.32%**
1577. **`arch/arm/boot/dts/aspeed/aspeed-bmc-arm-stardragon4800-rep2.dts`** -> AI Confidence: **99.32%**
1578. **`arch/arm/boot/dts/aspeed/aspeed-bmc-delta-ahe50dc.dts`** -> AI Confidence: **99.32%**
1579. **`arch/arm/boot/dts/aspeed/aspeed-bmc-facebook-fuji-data64.dts`** -> AI Confidence: **99.32%**
1580. **`arch/arm/boot/dts/aspeed/aspeed-bmc-facebook-wedge400-data64.dts`** -> AI Confidence: **99.32%**
1581. **`arch/arm/boot/dts/aspeed/aspeed-bmc-facebook-yosemitev2.dts`** -> AI Confidence: **99.32%**
1582. **`arch/arm/boot/dts/aspeed/aspeed-bmc-inspur-on5263m5.dts`** -> AI Confidence: **99.32%**
1583. **`arch/arm/boot/dts/aspeed/aspeed-bmc-lenovo-hr630.dts`** -> AI Confidence: **99.32%**
1584. **`arch/arm/boot/dts/aspeed/aspeed-bmc-lenovo-hr855xg2.dts`** -> AI Confidence: **99.32%**
1585. **`arch/arm/boot/dts/aspeed/aspeed-bmc-microsoft-olympus.dts`** -> AI Confidence: **99.32%**
1586. **`arch/arm/boot/dts/aspeed/aspeed-bmc-opp-palmetto.dts`** -> AI Confidence: **99.32%**
1587. **`arch/arm/boot/dts/aspeed/aspeed-bmc-opp-vesnin.dts`** -> AI Confidence: **99.32%**
1588. **`arch/arm/boot/dts/aspeed/aspeed-bmc-portwell-neptune.dts`** -> AI Confidence: **99.32%**
1589. **`arch/arm/boot/dts/aspeed/aspeed-bmc-qcom-dc-scm-v1.dts`** -> AI Confidence: **99.32%**
1590. **`arch/arm/boot/dts/aspeed/aspeed-bmc-quanta-q71l.dts`** -> AI Confidence: **99.32%**
1591. **`arch/arm/boot/dts/broadcom/bcm2711-rpi-cm4.dtsi`** -> AI Confidence: **99.32%**
1592. **`arch/arm/boot/dts/broadcom/bcm4708-buffalo-wxr-1750dhp.dts`** -> AI Confidence: **99.32%**
1593. **`arch/arm/boot/dts/broadcom/bcm4709-asus-rt-ac3200.dts`** -> AI Confidence: **99.32%**
1594. **`arch/arm/boot/dts/broadcom/bcm47094-asus-rt-ac5300.dts`** -> AI Confidence: **99.32%**
1595. **`arch/arm/boot/dts/broadcom/bcm53015-meraki-mr26.dts`** -> AI Confidence: **99.32%**
1596. **`arch/arm/boot/dts/broadcom/bcm53016-meraki-mr32.dts`** -> AI Confidence: **99.32%**
1597. **`arch/arm/boot/dts/gemini/gemini-dlink-dns-313.dts`** -> AI Confidence: **99.32%**
1598. **`arch/arm/boot/dts/marvell/armada-370-dlink-dns327l.dts`** -> AI Confidence: **99.32%**
1599. **`arch/arm/boot/dts/marvell/armada-370-netgear-rn102.dts`** -> AI Confidence: **99.32%**
1600. **`arch/arm/boot/dts/marvell/armada-370-netgear-rn104.dts`** -> AI Confidence: **99.32%**
1601. **`arch/arm/boot/dts/marvell/armada-370-synology-ds213j.dts`** -> AI Confidence: **99.32%**
1602. **`arch/arm/boot/dts/marvell/armada-381-netgear-gs110emx.dts`** -> AI Confidence: **99.32%**
1603. **`arch/arm/boot/dts/marvell/armada-385-linksys-rango.dts`** -> AI Confidence: **99.32%**
1604. **`arch/arm/boot/dts/marvell/armada-xp-axpwifiap.dts`** -> AI Confidence: **99.32%**
1605. **`arch/arm/boot/dts/marvell/armada-xp-lenovo-ix4-300d.dts`** -> AI Confidence: **99.32%**
1606. **`arch/arm/boot/dts/marvell/armada-xp-linksys-mamba.dts`** -> AI Confidence: **99.32%**
1607. **`arch/arm/boot/dts/marvell/armada-xp-netgear-rn2120.dts`** -> AI Confidence: **99.32%**
1608. **`arch/arm/boot/dts/marvell/armada-xp-openblocks-ax3-4.dts`** -> AI Confidence: **99.32%**
1609. **`arch/arm/boot/dts/marvell/kirkwood-4i-edge-200.dts`** -> AI Confidence: **99.32%**
1610. **`arch/arm/boot/dts/marvell/kirkwood-c200-v1.dts`** -> AI Confidence: **99.32%**
1611. **`arch/arm/boot/dts/marvell/kirkwood-nsa310s.dts`** -> AI Confidence: **99.32%**
1612. **`arch/arm/boot/dts/marvell/kirkwood-pogoplug-series-4.dts`** -> AI Confidence: **99.32%**
1613. **`arch/arm/boot/dts/marvell/kirkwood-ts219-6281.dts`** -> AI Confidence: **99.32%**
1614. **`arch/arm/boot/dts/marvell/kirkwood-ts219-6282.dts`** -> AI Confidence: **99.32%**
1615. **`arch/arm/boot/dts/marvell/orion5x-netgear-wnr854t.dts`** -> AI Confidence: **99.32%**
1616. **`arch/arm/boot/dts/mediatek/mt7623a-rfb-emmc.dts`** -> AI Confidence: **99.32%**
1617. **`arch/arm/boot/dts/mediatek/mt7623a-rfb-nand.dts`** -> AI Confidence: **99.32%**
1618. **`arch/arm/boot/dts/mediatek/mt7623n-bananapi-bpi-r2.dts`** -> AI Confidence: **99.32%**
1619. **`arch/arm/boot/dts/mediatek/mt7623n-rfb-emmc.dts`** -> AI Confidence: **99.32%**
1620. **`arch/arm/boot/dts/microchip/at91-sama5d27_som1.dtsi`** -> AI Confidence: **99.32%**
1621. **`arch/arm/boot/dts/microchip/at91sam9g25-gardena-smart-gateway.dts`** -> AI Confidence: **99.32%**
1622. **`arch/arm/boot/dts/nuvoton/nuvoton-npcm730-gsj.dts`** -> AI Confidence: **99.32%**
1623. **`arch/arm/boot/dts/nuvoton/nuvoton-npcm750-evb.dts`** -> AI Confidence: **99.32%**
1624. **`arch/arm/boot/dts/nuvoton/nuvoton-wpcm450-supermicro-x9sci-ln4f.dts`** -> AI Confidence: **99.32%**
1625. **`arch/arm/boot/dts/nvidia/tegra114-asus-tf701t.dts`** -> AI Confidence: **99.32%**
1626. **`arch/arm/boot/dts/nvidia/tegra124-jetson-tk1.dts`** -> AI Confidence: **99.32%**
1627. **`arch/arm/boot/dts/nvidia/tegra124-venice2.dts`** -> AI Confidence: **99.32%**
1628. **`arch/arm/boot/dts/nvidia/tegra30-beaver.dts`** -> AI Confidence: **99.32%**
1629. **`arch/arm/boot/dts/nxp/imx/imx25-pdk.dts`** -> AI Confidence: **99.32%**
1630. **`arch/arm/boot/dts/nxp/imx/imx35-eukrea-mbimxsd35-baseboard.dts`** -> AI Confidence: **99.32%**
1631. **`arch/arm/boot/dts/nxp/imx/imx50-kobo-aura.dts`** -> AI Confidence: **99.32%**
1632. **`arch/arm/boot/dts/nxp/imx/imx6dl-lanmcu.dts`** -> AI Confidence: **99.32%**
1633. **`arch/arm/boot/dts/nxp/imx/imx6dl-plybas.dts`** -> AI Confidence: **99.32%**
1634. **`arch/arm/boot/dts/nxp/imx/imx6dl-plym2m.dts`** -> AI Confidence: **99.32%**
1635. **`arch/arm/boot/dts/nxp/imx/imx6dl-prtrvt.dts`** -> AI Confidence: **99.32%**
1636. **`arch/arm/boot/dts/nxp/imx/imx6dl-skov-revc-lt6.dts`** -> AI Confidence: **99.32%**
1637. **`arch/arm/boot/dts/nxp/imx/imx6dl-tx6s-8035.dts`** -> AI Confidence: **99.32%**
1638. **`arch/arm/boot/dts/nxp/imx/imx6dl-tx6u-8033.dts`** -> AI Confidence: **99.32%**
1639. **`arch/arm/boot/dts/nxp/imx/imx6q-bosch-acc.dts`** -> AI Confidence: **99.32%**
1640. **`arch/arm/boot/dts/nxp/imx/imx6q-cm-fx6.dts`** -> AI Confidence: **99.32%**
1641. **`arch/arm/boot/dts/nxp/imx/imx6q-evi.dts`** -> AI Confidence: **99.32%**
1642. **`arch/arm/boot/dts/nxp/imx/imx6q-gk802.dts`** -> AI Confidence: **99.32%**
1643. **`arch/arm/boot/dts/nxp/imx/imx6q-gw54xx.dts`** -> AI Confidence: **99.32%**
1644. **`arch/arm/boot/dts/nxp/imx/imx6q-h100.dts`** -> AI Confidence: **99.32%**
1645. **`arch/arm/boot/dts/nxp/imx/imx6q-logicpd.dts`** -> AI Confidence: **99.32%**
1646. **`arch/arm/boot/dts/nxp/imx/imx6q-mccmon6.dts`** -> AI Confidence: **99.32%**
1647. **`arch/arm/boot/dts/nxp/imx/imx6q-novena.dts`** -> AI Confidence: **99.32%**
1648. **`arch/arm/boot/dts/nxp/imx/imx6q-pistachio.dts`** -> AI Confidence: **99.32%**
1649. **`arch/arm/boot/dts/nxp/imx/imx6q-prtwd2.dts`** -> AI Confidence: **99.32%**
1650. **`arch/arm/boot/dts/nxp/imx/imx6q-skov-revc-lt6.dts`** -> AI Confidence: **99.32%**
1651. **`arch/arm/boot/dts/nxp/imx/imx6q-tbs2910.dts`** -> AI Confidence: **99.32%**
1652. **`arch/arm/boot/dts/nxp/imx/imx6q-tx6q-1020-comtft.dts`** -> AI Confidence: **99.32%**
1653. **`arch/arm/boot/dts/nxp/imx/imx6q-tx6q-1020.dts`** -> AI Confidence: **99.32%**
1654. **`arch/arm/boot/dts/nxp/imx/imx6q-tx6q-1036.dts`** -> AI Confidence: **99.32%**
1655. **`arch/arm/boot/dts/nxp/imx/imx6q-var-dt6customboard.dts`** -> AI Confidence: **99.32%**
1656. **`arch/arm/boot/dts/nxp/imx/imx6q-var-mx6customboard.dts`** -> AI Confidence: **99.32%**
1657. **`arch/arm/boot/dts/nxp/imx/imx6qdl-ds.dtsi`** -> AI Confidence: **99.32%**
1658. **`arch/arm/boot/dts/nxp/imx/imx6qdl-var-som.dtsi`** -> AI Confidence: **99.32%**
1659. **`arch/arm/boot/dts/nxp/imx/imx6qp-tx6qp-8037.dts`** -> AI Confidence: **99.32%**
1660. **`arch/arm/boot/dts/nxp/imx/imx6qp-tx6qp-8137.dts`** -> AI Confidence: **99.32%**
1661. **`arch/arm/boot/dts/nxp/imx/imx6sl-evk.dts`** -> AI Confidence: **99.32%**
1662. **`arch/arm/boot/dts/nxp/imx/imx6sl-tolino-shine2hd.dts`** -> AI Confidence: **99.32%**
1663. **`arch/arm/boot/dts/nxp/imx/imx6sll-evk.dts`** -> AI Confidence: **99.32%**
1664. **`arch/arm/boot/dts/nxp/imx/imx6sx-softing-vining-2000.dts`** -> AI Confidence: **99.32%**
1665. **`arch/arm/boot/dts/nxp/imx/imx6ul-geam.dts`** -> AI Confidence: **99.32%**
1666. **`arch/arm/boot/dts/nxp/imx/imx6ul-tqma6ul1-mba6ulx.dts`** -> AI Confidence: **99.32%**
1667. **`arch/arm/boot/dts/nxp/imx/imx6ul-var-som.dtsi`** -> AI Confidence: **99.32%**
1668. **`arch/arm/boot/dts/nxp/imx/imx6ull-jozacp.dts`** -> AI Confidence: **99.32%**
1669. **`arch/arm/boot/dts/nxp/imx/imx6ull-myir-mys-6ulx.dtsi`** -> AI Confidence: **99.32%**
1670. **`arch/arm/boot/dts/nxp/lpc/lpc4337-ciaa.dts`** -> AI Confidence: **99.32%**
1671. **`arch/arm/boot/dts/nxp/lpc/lpc4357-myd-lpc4357.dts`** -> AI Confidence: **99.32%**
1672. **`arch/arm/boot/dts/nxp/ls/ls1021a-moxa-uc-8410a.dts`** -> AI Confidence: **99.32%**
1673. **`arch/arm/boot/dts/nxp/mxs/imx28-amarula-rmm.dts`** -> AI Confidence: **99.32%**
1674. **`arch/arm/boot/dts/nxp/mxs/imx28-tx28.dts`** -> AI Confidence: **99.32%**
1675. **`arch/arm/boot/dts/qcom/qcom-apq8026-huawei-sturgeon.dts`** -> AI Confidence: **99.32%**
1676. **`arch/arm/boot/dts/qcom/qcom-ipq4018-jalapeno.dts`** -> AI Confidence: **99.32%**
1677. **`arch/arm/boot/dts/qcom/qcom-ipq8064-rb3011.dts`** -> AI Confidence: **99.32%**
1678. **`arch/arm/boot/dts/qcom/qcom-ipq8064-v1.0.dtsi`** -> AI Confidence: **99.32%**
1679. **`arch/arm/boot/dts/qcom/qcom-msm8960-cdp.dts`** -> AI Confidence: **99.32%**
1680. **`arch/arm/boot/dts/renesas/r7s72100-gr-peach.dts`** -> AI Confidence: **99.32%**
1681. **`arch/arm/boot/dts/renesas/r8a73a4-ape6evm.dts`** -> AI Confidence: **99.32%**
1682. **`arch/arm/boot/dts/renesas/r8a7742-iwg21d-q7-dbcm-ca.dts`** -> AI Confidence: **99.32%**
1683. **`arch/arm/boot/dts/renesas/r8a7778-bockw.dts`** -> AI Confidence: **99.32%**
1684. **`arch/arm/boot/dts/renesas/r8a7790-lager.dts`** -> AI Confidence: **99.32%**
1685. **`arch/arm/boot/dts/renesas/r8a7791-koelsch.dts`** -> AI Confidence: **99.32%**
1686. **`arch/arm/boot/dts/renesas/r8a7792-blanche.dts`** -> AI Confidence: **99.32%**
1687. **`arch/arm/boot/dts/renesas/r8a7792-wheat.dts`** -> AI Confidence: **99.32%**
1688. **`arch/arm/boot/dts/renesas/r8a7793-gose.dts`** -> AI Confidence: **99.32%**
1689. **`arch/arm/boot/dts/renesas/r8a7794-alt.dts`** -> AI Confidence: **99.32%**
1690. **`arch/arm/boot/dts/renesas/r8a7794-silk.dts`** -> AI Confidence: **99.32%**
1691. **`arch/arm/boot/dts/rockchip/rk3128-xpi-3128.dts`** -> AI Confidence: **99.32%**
1692. **`arch/arm/boot/dts/rockchip/rk3288-phycore-rdk.dts`** -> AI Confidence: **99.32%**
1693. **`arch/arm/boot/dts/rockchip/rk3288-r89.dts`** -> AI Confidence: **99.32%**
1694. **`arch/arm/boot/dts/rockchip/rk3288-veyron-speedy.dts`** -> AI Confidence: **99.32%**
1695. **`arch/arm/boot/dts/rockchip/rv1109-relfor-saib.dts`** -> AI Confidence: **99.32%**
1696. **`arch/arm/boot/dts/samsung/exynos4210-smdkv310.dts`** -> AI Confidence: **99.32%**
1697. **`arch/arm/boot/dts/samsung/exynos4412-odroidu3.dts`** -> AI Confidence: **99.32%**
1698. **`arch/arm/boot/dts/samsung/exynos4412-tiny4412.dts`** -> AI Confidence: **99.32%**
1699. **`arch/arm/boot/dts/samsung/exynos5422-odroidxu3-lite.dts`** -> AI Confidence: **99.32%**
1700. **`arch/arm/boot/dts/samsung/exynos5422-odroidxu3.dts`** -> AI Confidence: **99.32%**
1701. **`arch/arm/boot/dts/samsung/exynos5422-odroidxu4.dts`** -> AI Confidence: **99.32%**
1702. **`arch/arm/boot/dts/samsung/s3c6410-mini6410.dts`** -> AI Confidence: **99.32%**
1703. **`arch/arm/boot/dts/samsung/s3c6410-smdk6410.dts`** -> AI Confidence: **99.32%**
1704. **`arch/arm/boot/dts/samsung/s5pv210-aquila.dts`** -> AI Confidence: **99.32%**
1705. **`arch/arm/boot/dts/samsung/s5pv210-fascinate4g.dts`** -> AI Confidence: **99.32%**
1706. **`arch/arm/boot/dts/samsung/s5pv210-galaxys.dts`** -> AI Confidence: **99.32%**
1707. **`arch/arm/boot/dts/samsung/s5pv210-smdkv210.dts`** -> AI Confidence: **99.32%**
1708. **`arch/arm/boot/dts/socionext/uniphier-ld4.dtsi`** -> AI Confidence: **99.32%**
1709. **`arch/arm/boot/dts/socionext/uniphier-sld8.dtsi`** -> AI Confidence: **99.32%**
1710. **`arch/arm/boot/dts/st/ste-nomadik-nhk15.dts`** -> AI Confidence: **99.32%**
1711. **`arch/arm/boot/dts/st/ste-snowball.dts`** -> AI Confidence: **99.32%**
1712. **`arch/arm/boot/dts/st/stm32mp157a-dhcor-avenger96.dts`** -> AI Confidence: **99.32%**
1713. **`arch/arm/boot/dts/ti/davinci/da850-lcdk.dts`** -> AI Confidence: **99.32%**
1714. **`arch/arm/boot/dts/ti/omap/am335x-boneblue.dts`** -> AI Confidence: **99.32%**
1715. **`arch/arm/boot/dts/ti/omap/am335x-evm.dts`** -> AI Confidence: **99.32%**
1716. **`arch/arm/boot/dts/ti/omap/am335x-igep0033.dtsi`** -> AI Confidence: **99.32%**
1717. **`arch/arm/boot/dts/ti/omap/am335x-mba335x.dts`** -> AI Confidence: **99.32%**
1718. **`arch/arm/boot/dts/ti/omap/am335x-myirtech-myc.dtsi`** -> AI Confidence: **99.32%**
1719. **`arch/arm/boot/dts/ti/omap/am335x-myirtech-myd.dts`** -> AI Confidence: **99.32%**
1720. **`arch/arm/boot/dts/ti/omap/am335x-pocketbeagle.dts`** -> AI Confidence: **99.32%**
1721. **`arch/arm/boot/dts/ti/omap/am335x-tqma335x.dtsi`** -> AI Confidence: **99.32%**
1722. **`arch/arm/boot/dts/ti/omap/am57xx-cl-som-am57x.dts`** -> AI Confidence: **99.32%**
1723. **`arch/arm/boot/dts/ti/omap/dra7-evm.dts`** -> AI Confidence: **99.32%**
1724. **`arch/arm/boot/dts/ti/omap/dra72-evm.dts`** -> AI Confidence: **99.32%**
1725. **`arch/arm/boot/dts/ti/omap/omap3-beagle-xm.dts`** -> AI Confidence: **99.32%**
1726. **`arch/arm/boot/dts/ti/omap/omap3-beagle.dts`** -> AI Confidence: **99.32%**
1727. **`arch/arm/boot/dts/ti/omap/omap3-evm-37xx.dts`** -> AI Confidence: **99.32%**
1728. **`arch/arm/boot/dts/ti/omap/omap3-evm.dts`** -> AI Confidence: **99.32%**
1729. **`arch/arm/boot/dts/ti/omap/omap3-lilly-a83x.dtsi`** -> AI Confidence: **99.32%**
1730. **`arch/arm/boot/dts/ti/omap/omap3-zoom3.dts`** -> AI Confidence: **99.32%**
1731. **`arch/arm/boot/dts/ti/omap/omap4-duovero-parlor.dts`** -> AI Confidence: **99.32%**
1732. **`arch/arm/boot/dts/ti/omap/omap4-kc1.dts`** -> AI Confidence: **99.32%**
1733. **`arch/arm/boot/dts/ti/omap/omap4-var-dvk-om44.dts`** -> AI Confidence: **99.32%**
1734. **`arch/arm/boot/dts/ti/omap/omap5-cm-t54.dts`** -> AI Confidence: **99.32%**
1735. **`arch/arm64/boot/dts/allwinner/sun50i-h5-orangepi-prime.dts`** -> AI Confidence: **99.32%**
1736. **`arch/arm64/boot/dts/allwinner/sun50i-h6-orangepi-3.dts`** -> AI Confidence: **99.32%**
1737. **`arch/arm64/boot/dts/allwinner/sun50i-h6-pine-h64.dts`** -> AI Confidence: **99.32%**
1738. **`arch/arm64/boot/dts/allwinner/sun55i-a527-cubie-a5e.dts`** -> AI Confidence: **99.32%**
1739. **`arch/arm64/boot/dts/allwinner/sun55i-t527-orangepi-4a.dts`** -> AI Confidence: **99.32%**
1740. **`arch/arm64/boot/dts/amlogic/meson-g12a-radxa-zero.dts`** -> AI Confidence: **99.32%**
1741. **`arch/arm64/boot/dts/amlogic/meson-g12b-gsking-x.dts`** -> AI Confidence: **99.32%**
1742. **`arch/arm64/boot/dts/amlogic/meson-gxbb-nanopi-k2.dts`** -> AI Confidence: **99.32%**
1743. **`arch/arm64/boot/dts/amlogic/meson-gxbb-odroidc2.dts`** -> AI Confidence: **99.32%**
1744. **`arch/arm64/boot/dts/amlogic/meson-gxbb-p200.dts`** -> AI Confidence: **99.32%**
1745. **`arch/arm64/boot/dts/amlogic/meson-gxbb-wetek-play2.dts`** -> AI Confidence: **99.32%**
1746. **`arch/arm64/boot/dts/amlogic/meson-gxl-s805x-libretech-ac.dts`** -> AI Confidence: **99.32%**
1747. **`arch/arm64/boot/dts/amlogic/meson-gxl-s805x-p241.dts`** -> AI Confidence: **99.32%**
1748. **`arch/arm64/boot/dts/amlogic/meson-gxl-s905d-p230.dts`** -> AI Confidence: **99.32%**
1749. **`arch/arm64/boot/dts/amlogic/meson-gxl-s905d-sml5442tw.dts`** -> AI Confidence: **99.32%**
1750. **`arch/arm64/boot/dts/amlogic/meson-gxl-s905x-khadas-vim.dts`** -> AI Confidence: **99.32%**
1751. **`arch/arm64/boot/dts/amlogic/meson-gxl-s905x-libretech-cc.dts`** -> AI Confidence: **99.32%**
1752. **`arch/arm64/boot/dts/amlogic/meson-gxm-khadas-vim2.dts`** -> AI Confidence: **99.32%**
1753. **`arch/arm64/boot/dts/amlogic/meson-gxm-q200.dts`** -> AI Confidence: **99.32%**
1754. **`arch/arm64/boot/dts/amlogic/meson-gxm-tx9-pro.dts`** -> AI Confidence: **99.32%**
1755. **`arch/arm64/boot/dts/amlogic/meson-sm1-khadas-vim3l.dts`** -> AI Confidence: **99.32%**
1756. **`arch/arm64/boot/dts/apple/t8103-j293.dts`** -> AI Confidence: **99.32%**
1757. **`arch/arm64/boot/dts/apple/t8103-j313.dts`** -> AI Confidence: **99.32%**
1758. **`arch/arm64/boot/dts/apple/t8112-j413.dts`** -> AI Confidence: **99.32%**
1759. **`arch/arm64/boot/dts/apple/t8112-j415.dts`** -> AI Confidence: **99.32%**
1760. **`arch/arm64/boot/dts/apple/t8112-j493.dts`** -> AI Confidence: **99.32%**
1761. **`arch/arm64/boot/dts/exynos/axis/artpec8.dtsi`** -> AI Confidence: **99.32%**
1762. **`arch/arm64/boot/dts/exynos/exynos9810-starlte.dts`** -> AI Confidence: **99.32%**
1763. **`arch/arm64/boot/dts/exynos/exynosautov9-sadk.dts`** -> AI Confidence: **99.32%**
1764. **`arch/arm64/boot/dts/freescale/fsl-ls1028a-tqmls1028a-mbls1028a.dts`** -> AI Confidence: **99.32%**
1765. **`arch/arm64/boot/dts/freescale/imx8mm-beacon-kit.dts`** -> AI Confidence: **99.32%**
1766. **`arch/arm64/boot/dts/freescale/imx8mm-data-modul-edm-sbc.dts`** -> AI Confidence: **99.32%**
1767. **`arch/arm64/boot/dts/freescale/imx8mm-kontron-osm-s.dtsi`** -> AI Confidence: **99.32%**
1768. **`arch/arm64/boot/dts/freescale/imx8mm-phyboard-polis-peb-av-10.dtsi`** -> AI Confidence: **99.32%**
1769. **`arch/arm64/boot/dts/freescale/imx8mm-tqma8mqml-mba8mx.dts`** -> AI Confidence: **99.32%**
1770. **`arch/arm64/boot/dts/freescale/imx8mm-venice-gw71xx.dtsi`** -> AI Confidence: **99.32%**
1771. **`arch/arm64/boot/dts/freescale/imx8mm-venice-gw72xx.dtsi`** -> AI Confidence: **99.32%**
1772. **`arch/arm64/boot/dts/freescale/imx8mm-venice-gw73xx.dtsi`** -> AI Confidence: **99.32%**
1773. **`arch/arm64/boot/dts/freescale/imx8mm-venice-gw75xx.dtsi`** -> AI Confidence: **99.32%**
1774. **`arch/arm64/boot/dts/freescale/imx8mn-beacon-kit.dts`** -> AI Confidence: **99.32%**
1775. **`arch/arm64/boot/dts/freescale/imx8mn-ddr3l-evk.dts`** -> AI Confidence: **99.32%**
1776. **`arch/arm64/boot/dts/freescale/imx8mn-evk.dts`** -> AI Confidence: **99.32%**
1777. **`arch/arm64/boot/dts/freescale/imx8mp-aristainetos3-helios.dts`** -> AI Confidence: **99.32%**
1778. **`arch/arm64/boot/dts/freescale/imx8mp-aristainetos3-proton2s.dts`** -> AI Confidence: **99.32%**
1779. **`arch/arm64/boot/dts/freescale/imx8mp-data-modul-edm-sbc.dts`** -> AI Confidence: **99.32%**
1780. **`arch/arm64/boot/dts/freescale/imx8mp-dhcom-drc02.dts`** -> AI Confidence: **99.32%**
1781. **`arch/arm64/boot/dts/freescale/imx8mp-dhcom-pdk2.dts`** -> AI Confidence: **99.32%**
1782. **`arch/arm64/boot/dts/freescale/imx8mp-dhcom-pdk3.dts`** -> AI Confidence: **99.32%**
1783. **`arch/arm64/boot/dts/freescale/imx8mp-hummingboard-mate.dts`** -> AI Confidence: **99.32%**
1784. **`arch/arm64/boot/dts/freescale/imx8mp-hummingboard-ripple.dts`** -> AI Confidence: **99.32%**
1785. **`arch/arm64/boot/dts/freescale/imx8mp-icore-mx8mp-edimm2.2.dts`** -> AI Confidence: **99.32%**
1786. **`arch/arm64/boot/dts/freescale/imx8mp-libra-rdk-fpsc-lvds-peb-av-10.dtsi`** -> AI Confidence: **99.32%**
1787. **`arch/arm64/boot/dts/freescale/imx8mp-msc-sm2s-ep1.dts`** -> AI Confidence: **99.32%**
1788. **`arch/arm64/boot/dts/freescale/imx8mp-navqp.dts`** -> AI Confidence: **99.32%**
1789. **`arch/arm64/boot/dts/freescale/imx8mp-phyboard-pollux-peb-av-10.dtsi`** -> AI Confidence: **99.32%**
1790. **`arch/arm64/boot/dts/freescale/imx8mp-toradex-smarc.dtsi`** -> AI Confidence: **99.32%**
1791. **`arch/arm64/boot/dts/freescale/imx8mp-venice-gw71xx.dtsi`** -> AI Confidence: **99.32%**
1792. **`arch/arm64/boot/dts/freescale/imx8mp-venice-gw72xx.dtsi`** -> AI Confidence: **99.32%**
1793. **`arch/arm64/boot/dts/freescale/imx8mp-venice-gw73xx.dtsi`** -> AI Confidence: **99.32%**
1794. **`arch/arm64/boot/dts/freescale/imx8mp-venice-gw75xx.dtsi`** -> AI Confidence: **99.32%**
1795. **`arch/arm64/boot/dts/freescale/imx8mp-venice-gw82xx.dtsi`** -> AI Confidence: **99.32%**
1796. **`arch/arm64/boot/dts/freescale/imx95-19x19-evk.dts`** -> AI Confidence: **99.32%**
1797. **`arch/arm64/boot/dts/freescale/imx95-libra-rdk-fpsc.dts`** -> AI Confidence: **99.32%**
1798. **`arch/arm64/boot/dts/freescale/imx95-toradex-smarc.dtsi`** -> AI Confidence: **99.32%**
1799. **`arch/arm64/boot/dts/freescale/imx952-evk.dts`** -> AI Confidence: **99.32%**
1800. **`arch/arm64/boot/dts/hisilicon/hi3798cv200-poplar.dts`** -> AI Confidence: **99.32%**
1801. **`arch/arm64/boot/dts/hisilicon/hi6220-hikey.dts`** -> AI Confidence: **99.32%**
1802. **`arch/arm64/boot/dts/marvell/armada-3720-gl-mv1000.dts`** -> AI Confidence: **99.32%**
1803. **`arch/arm64/boot/dts/marvell/armada-8040-clearfog-gt-8k.dts`** -> AI Confidence: **99.32%**
1804. **`arch/arm64/boot/dts/marvell/armada-8040-puzzle-m801.dts`** -> AI Confidence: **99.32%**
1805. **`arch/arm64/boot/dts/marvell/mmp/pxa1908-samsung-coreprimevelte.dts`** -> AI Confidence: **99.32%**
1806. **`arch/arm64/boot/dts/mediatek/mt6795-sony-xperia-m5.dts`** -> AI Confidence: **99.32%**
1807. **`arch/arm64/boot/dts/nvidia/tegra186-p2771-0000.dts`** -> AI Confidence: **99.32%**
1808. **`arch/arm64/boot/dts/nvidia/tegra194-p2972-0000.dts`** -> AI Confidence: **99.32%**
1809. **`arch/arm64/boot/dts/nvidia/tegra210-p2597.dtsi`** -> AI Confidence: **99.32%**
1810. **`arch/arm64/boot/dts/qcom/ipq5424-rdp466.dts`** -> AI Confidence: **99.32%**
1811. **`arch/arm64/boot/dts/qcom/kaanapali-mtp.dts`** -> AI Confidence: **99.32%**
1812. **`arch/arm64/boot/dts/qcom/kaanapali-qrd.dts`** -> AI Confidence: **99.32%**
1813. **`arch/arm64/boot/dts/qcom/msm8916-lg-m216.dts`** -> AI Confidence: **99.32%**
1814. **`arch/arm64/boot/dts/qcom/msm8953-flipkart-rimob.dts`** -> AI Confidence: **99.32%**
1815. **`arch/arm64/boot/dts/qcom/msm8953-motorola-potter.dts`** -> AI Confidence: **99.32%**
1816. **`arch/arm64/boot/dts/qcom/msm8953-xiaomi-daisy.dts`** -> AI Confidence: **99.32%**
1817. **`arch/arm64/boot/dts/qcom/msm8998-lenovo-miix-630.dts`** -> AI Confidence: **99.32%**
1818. **`arch/arm64/boot/dts/qcom/qrb2210-arduino-imola.dts`** -> AI Confidence: **99.32%**
1819. **`arch/arm64/boot/dts/qcom/sc7280-herobrine-crd.dts`** -> AI Confidence: **99.32%**
1820. **`arch/arm64/boot/dts/qcom/sc7280-herobrine-herobrine-r1.dts`** -> AI Confidence: **99.32%**
1821. **`arch/arm64/boot/dts/qcom/sdm450-lenovo-tbx605f.dts`** -> AI Confidence: **99.32%**
1822. **`arch/arm64/boot/dts/qcom/sdm450-motorola-ali.dts`** -> AI Confidence: **99.32%**
1823. **`arch/arm64/boot/dts/qcom/sdm632-motorola-ocean.dts`** -> AI Confidence: **99.32%**
1824. **`arch/arm64/boot/dts/renesas/r8a774a1-beacon-rzg2m-kit.dts`** -> AI Confidence: **99.32%**
1825. **`arch/arm64/boot/dts/renesas/r8a774a1-hihope-rzg2m-ex-idk-1110wr.dts`** -> AI Confidence: **99.32%**
1826. **`arch/arm64/boot/dts/renesas/r8a774a1-hihope-rzg2m-rev2-ex-idk-1110wr.dts`** -> AI Confidence: **99.32%**
1827. **`arch/arm64/boot/dts/renesas/r8a774b1-beacon-rzg2n-kit.dts`** -> AI Confidence: **99.32%**
1828. **`arch/arm64/boot/dts/renesas/r8a774b1-hihope-rzg2n-ex-idk-1110wr.dts`** -> AI Confidence: **99.32%**
1829. **`arch/arm64/boot/dts/renesas/r8a774b1-hihope-rzg2n-rev2-ex-idk-1110wr.dts`** -> AI Confidence: **99.32%**
1830. **`arch/arm64/boot/dts/renesas/r8a774e1-beacon-rzg2h-kit.dts`** -> AI Confidence: **99.32%**
1831. **`arch/arm64/boot/dts/renesas/r8a774e1-hihope-rzg2h-ex-idk-1110wr.dts`** -> AI Confidence: **99.32%**
1832. **`arch/arm64/boot/dts/renesas/r8a77990.dtsi`** -> AI Confidence: **99.32%**
1833. **`arch/arm64/boot/dts/renesas/r8a77995.dtsi`** -> AI Confidence: **99.32%**
1834. **`arch/arm64/boot/dts/renesas/r8a779a0-falcon.dts`** -> AI Confidence: **99.32%**
1835. **`arch/arm64/boot/dts/renesas/r8a779f0-spider-cpu.dtsi`** -> AI Confidence: **99.32%**
1836. **`arch/arm64/boot/dts/renesas/r8a779g3-sparrow-hawk.dts`** -> AI Confidence: **99.32%**
1837. **`arch/arm64/boot/dts/renesas/r9a07g043u11-smarc.dts`** -> AI Confidence: **99.32%**
1838. **`arch/arm64/boot/dts/renesas/r9a07g044c2-smarc.dts`** -> AI Confidence: **99.32%**
1839. **`arch/arm64/boot/dts/renesas/r9a07g044l2-remi-pi.dts`** -> AI Confidence: **99.32%**
1840. **`arch/arm64/boot/dts/renesas/r9a09g011-v2mevk2.dts`** -> AI Confidence: **99.32%**
1841. **`arch/arm64/boot/dts/renesas/r9a09g056n48-rzv2n-evk.dts`** -> AI Confidence: **99.32%**
1842. **`arch/arm64/boot/dts/renesas/r9a09g077m44-rzt2h-evk.dts`** -> AI Confidence: **99.32%**
1843. **`arch/arm64/boot/dts/renesas/r9a09g087m44-rzn2h-evk.dts`** -> AI Confidence: **99.32%**
1844. **`arch/arm64/boot/dts/renesas/rzg2lc-smarc-som.dtsi`** -> AI Confidence: **99.32%**
1845. **`arch/arm64/boot/dts/renesas/rzg2ul-smarc-som.dtsi`** -> AI Confidence: **99.32%**
1846. **`arch/arm64/boot/dts/renesas/rzg2ul-smarc.dtsi`** -> AI Confidence: **99.32%**
1847. **`arch/arm64/boot/dts/renesas/rzg3s-smarc.dtsi`** -> AI Confidence: **99.32%**
1848. **`arch/arm64/boot/dts/rockchip/px30-firefly-jd4-core-mb.dts`** -> AI Confidence: **99.32%**
1849. **`arch/arm64/boot/dts/rockchip/px30-firefly-jd4-core.dtsi`** -> AI Confidence: **99.32%**
1850. **`arch/arm64/boot/dts/rockchip/px30-ringneck-haikou.dts`** -> AI Confidence: **99.32%**
1851. **`arch/arm64/boot/dts/rockchip/rk3308-bpi-p2-pro.dts`** -> AI Confidence: **99.32%**
1852. **`arch/arm64/boot/dts/rockchip/rk3368-evb.dtsi`** -> AI Confidence: **99.32%**
1853. **`arch/arm64/boot/dts/rockchip/rk3399pro-vmarc-som.dtsi`** -> AI Confidence: **99.32%**
1854. **`arch/arm64/boot/dts/rockchip/rk3588-armsom-lm7.dtsi`** -> AI Confidence: **99.32%**
1855. **`arch/arm64/boot/dts/rockchip/rk3588-firefly-core-3588j.dtsi`** -> AI Confidence: **99.32%**
1856. **`arch/arm64/boot/dts/rockchip/rk3588-firefly-icore-3588q.dtsi`** -> AI Confidence: **99.32%**
1857. **`arch/arm64/boot/dts/rockchip/rk3588-turing-rk1.dtsi`** -> AI Confidence: **99.32%**
1858. **`arch/arm64/boot/dts/tesla/fsd.dtsi`** -> AI Confidence: **99.32%**
1859. **`arch/arm64/boot/dts/ti/k3-am68-sk-som.dtsi`** -> AI Confidence: **99.32%**
1860. **`arch/arm64/boot/dts/ti/k3-j7200-som-p0.dtsi`** -> AI Confidence: **99.32%**
1861. **`arch/arm64/boot/dts/ti/k3-j721s2-som-p0.dtsi`** -> AI Confidence: **99.32%**
1862. **`arch/arm64/include/asm/asm-extable.h`** -> AI Confidence: **99.32%**
1863. **`arch/arm64/include/asm/barrier.h`** -> AI Confidence: **99.32%**
1864. **`arch/arm64/include/asm/bug.h`** -> AI Confidence: **99.32%**
1865. **`arch/arm64/include/asm/futex.h`** -> AI Confidence: **99.32%**
1866. **`arch/arm64/include/asm/kernel-pgtable.h`** -> AI Confidence: **99.32%**
1867. **`arch/arm64/include/asm/rwonce.h`** -> AI Confidence: **99.32%**
1868. **`arch/csky/include/asm/io.h`** -> AI Confidence: **99.32%**
1869. **`arch/hexagon/include/asm/futex.h`** -> AI Confidence: **99.32%**
1870. **`arch/loongarch/include/asm/addrspace.h`** -> AI Confidence: **99.32%**
1871. **`arch/loongarch/include/asm/asm-extable.h`** -> AI Confidence: **99.32%**
1872. **`arch/loongarch/include/asm/percpu.h`** -> AI Confidence: **99.32%**
1873. **`arch/loongarch/include/asm/xor.h`** -> AI Confidence: **99.32%**
1874. **`arch/loongarch/include/uapi/asm/unistd.h`** -> AI Confidence: **99.32%**
1875. **`arch/m68k/include/asm/entry.h`** -> AI Confidence: **99.32%**
1876. **`arch/m68k/include/asm/io.h`** -> AI Confidence: **99.32%**
1877. **`arch/m68k/include/asm/q40_master.h`** -> AI Confidence: **99.32%**
1878. **`arch/microblaze/include/asm/futex.h`** -> AI Confidence: **99.32%**
1879. **`arch/mips/boot/dts/pic32/pic32mzda_sk.dts`** -> AI Confidence: **99.32%**
1880. **`arch/mips/boot/dts/qca/ar9132_tl_wr1043nd_v1.dts`** -> AI Confidence: **99.32%**
1881. **`arch/mips/boot/dts/qca/ar9331_dragino_ms14.dts`** -> AI Confidence: **99.32%**
1882. **`arch/mips/boot/dts/qca/ar9331_omega.dts`** -> AI Confidence: **99.32%**
1883. **`arch/mips/boot/dts/qca/ar9331_tl_mr3020.dts`** -> AI Confidence: **99.32%**
1884. **`arch/mips/boot/dts/ralink/gardena_smart_gateway_mt7688.dts`** -> AI Confidence: **99.32%**
1885. **`arch/mips/boot/dts/ralink/mt7621-gnubee-gb-pc1.dts`** -> AI Confidence: **99.32%**
1886. **`arch/mips/boot/dts/ralink/mt7621-gnubee-gb-pc2.dts`** -> AI Confidence: **99.32%**
1887. **`arch/mips/cavium-octeon/executive/cvmx-interrupt-rsl.c`** -> AI Confidence: **99.32%**
1888. **`arch/mips/lantiq/early_printk.c`** -> AI Confidence: **99.32%**
1889. **`arch/mips/loongson2ef/common/cs5536/cs5536_isa.c`** -> AI Confidence: **99.32%**
1890. **`arch/mips/pci/fixup-rbtx4927.c`** -> AI Confidence: **99.32%**
1891. **`arch/parisc/include/asm/io.h`** -> AI Confidence: **99.32%**
1892. **`arch/parisc/math-emu/fmpyfadd.c`** -> AI Confidence: **99.32%**
1893. **`arch/powerpc/boot/dts/turris1x.dts`** -> AI Confidence: **99.32%**
1894. **`arch/powerpc/include/asm/asm-compat.h`** -> AI Confidence: **99.32%**
1895. **`arch/powerpc/include/asm/barrier.h`** -> AI Confidence: **99.32%**
1896. **`arch/powerpc/include/asm/cputable.h`** -> AI Confidence: **99.32%**
1897. **`arch/powerpc/include/asm/nohash/mmu.h`** -> AI Confidence: **99.32%**
1898. **`arch/powerpc/include/asm/spinlock_types.h`** -> AI Confidence: **99.32%**
1899. **`arch/powerpc/kernel/static_call.c`** -> AI Confidence: **99.32%**
1900. **`arch/powerpc/kvm/booke_emulate.c`** -> AI Confidence: **99.32%**
1901. **`arch/riscv/boot/dts/allwinner/sun20i-d1-clockworkpi-v3.14.dts`** -> AI Confidence: **99.32%**
1902. **`arch/riscv/boot/dts/canaan/canaan_kd233.dts`** -> AI Confidence: **99.32%**
1903. **`arch/riscv/boot/dts/canaan/k210_generic.dts`** -> AI Confidence: **99.32%**
1904. **`arch/riscv/boot/dts/canaan/sipeed_maixduino.dts`** -> AI Confidence: **99.32%**
1905. **`arch/riscv/boot/dts/sophgo/sg2042-evb-v1.dts`** -> AI Confidence: **99.32%**
1906. **`arch/riscv/boot/dts/sophgo/sg2042-evb-v2.dts`** -> AI Confidence: **99.32%**
1907. **`arch/riscv/boot/dts/sophgo/sg2042-milkv-pioneer.dts`** -> AI Confidence: **99.32%**
1908. **`arch/riscv/boot/dts/thead/th1520-beaglev-ahead.dts`** -> AI Confidence: **99.32%**
1909. **`arch/riscv/include/asm/asm-extable.h`** -> AI Confidence: **99.32%**
1910. **`arch/riscv/include/asm/assembler.h`** -> AI Confidence: **99.32%**
1911. **`arch/riscv/include/asm/barrier.h`** -> AI Confidence: **99.32%**
1912. **`arch/riscv/include/asm/insn-def.h`** -> AI Confidence: **99.32%**
1913. **`arch/riscv/include/asm/syscall_table.h`** -> AI Confidence: **99.32%**
1914. **`arch/riscv/include/uapi/asm/unistd.h`** -> AI Confidence: **99.32%**
1915. **`arch/riscv/net/bpf_jit_comp32.c`** -> AI Confidence: **99.32%**
1916. **`arch/sparc/include/asm/io.h`** -> AI Confidence: **99.32%**
1917. **`arch/sparc/include/asm/mc146818rtc.h`** -> AI Confidence: **99.32%**
1918. **`arch/sparc/include/asm/percpu_64.h`** -> AI Confidence: **99.32%**
1919. **`arch/sparc/include/asm/ttable.h`** -> AI Confidence: **99.32%**
1920. **`arch/sparc/include/asm/uaccess.h`** -> AI Confidence: **99.32%**
1921. **`arch/sparc/prom/bootstr_32.c`** -> AI Confidence: **99.32%**
1922. **`arch/um/include/asm/xor.h`** -> AI Confidence: **99.32%**
1923. **`arch/um/kernel/config.c.in`** -> AI Confidence: **99.32%**
1924. **`arch/x86/coco/tdx/debug.c`** -> AI Confidence: **99.32%**
1925. **`arch/x86/include/asm/barrier.h`** -> AI Confidence: **99.32%**
1926. **`arch/x86/include/asm/checksum.h`** -> AI Confidence: **99.32%**
1927. **`arch/x86/include/asm/seccomp.h`** -> AI Confidence: **99.32%**
1928. **`arch/x86/include/asm/vdso/sys_call.h`** -> AI Confidence: **99.32%**
1929. **`arch/x86/include/uapi/asm/posix_types.h`** -> AI Confidence: **99.32%**
1930. **`arch/x86/include/uapi/asm/unistd.h`** -> AI Confidence: **99.32%**
1931. **`arch/x86/um/asm/barrier.h`** -> AI Confidence: **99.32%**
1932. **`arch/xtensa/include/asm/cacheasm.h`** -> AI Confidence: **99.32%**
1933. **`arch/xtensa/include/asm/initialize_mmu.h`** -> AI Confidence: **99.32%**
1934. **`arch/xtensa/include/asm/pgtable.h`** -> AI Confidence: **99.32%**
1935. **`block/partitions/atari.c`** -> AI Confidence: **99.32%**
1936. **`drivers/accessibility/speakup/keyhelp.c`** -> AI Confidence: **99.32%**
1937. **`drivers/acpi/acpica/evxfevnt.c`** -> AI Confidence: **99.32%**
1938. **`drivers/acpi/acpica/exdebug.c`** -> AI Confidence: **99.32%**
1939. **`drivers/acpi/acpica/rsmisc.c`** -> AI Confidence: **99.32%**
1940. **`drivers/acpi/acpica/tbfind.c`** -> AI Confidence: **99.32%**
1941. **`drivers/acpi/acpica/utownerid.c`** -> AI Confidence: **99.32%**
1942. **`drivers/acpi/acpica/utresdecode.c`** -> AI Confidence: **99.32%**
1943. **`drivers/acpi/acpica/utstring.c`** -> AI Confidence: **99.32%**
1944. **`drivers/ata/libata-trace.c`** -> AI Confidence: **99.32%**
1945. **`drivers/gpu/drm/amd/display/dc/dcn30/dcn30_vpg.c`** -> AI Confidence: **99.32%**
1946. **`drivers/gpu/drm/amd/display/dc/dml/calcs/dcn_calc_auto.c`** -> AI Confidence: **99.32%**
1947. **`drivers/gpu/drm/amd/display/dc/dml/dsc/rc_calc_fpu.c`** -> AI Confidence: **99.32%**
1948. **`drivers/gpu/drm/nouveau/nvkm/subdev/bios/therm.c`** -> AI Confidence: **99.32%**
1949. **`drivers/gpu/drm/nouveau/nvkm/subdev/clk/pllnv04.c`** -> AI Confidence: **99.32%**
1950. **`drivers/gpu/drm/tegra/hda.c`** -> AI Confidence: **99.32%**
1951. **`drivers/media/pci/saa7164/saa7164-fw.c`** -> AI Confidence: **99.32%**
1952. **`drivers/media/usb/dvb-usb-v2/mxl111sf-gpio.c`** -> AI Confidence: **99.32%**
1953. **`drivers/net/ethernet/mellanox/mlx5/core/diag/cmd_tracepoint.h`** -> AI Confidence: **99.32%**
1954. **`drivers/staging/media/atomisp/pci/hive_isp_css_include/tag.h`** -> AI Confidence: **99.32%**
1955. **`drivers/staging/rtl8723bs/hal/hal_com_phycfg.c`** -> AI Confidence: **99.32%**
1956. **`drivers/staging/sm750fb/ddk750_mode.c`** -> AI Confidence: **99.32%**
1957. **`drivers/video/fbdev/sis/init.c`** -> AI Confidence: **99.32%**
1958. **`drivers/video/fbdev/sis/init301.c`** -> AI Confidence: **99.32%**
1959. **`fs/hfsplus/bitmap.c`** -> AI Confidence: **99.32%**
1960. **`fs/orangefs/orangefs-debug.h`** -> AI Confidence: **99.32%**
1961. **`fs/smb/server/glob.h`** -> AI Confidence: **99.32%**
1962. **`include/asm-generic/barrier.h`** -> AI Confidence: **99.32%**
1963. **`include/asm-generic/futex.h`** -> AI Confidence: **99.32%**
1964. **`include/asm-generic/percpu.h`** -> AI Confidence: **99.32%**
1965. **`include/linux/compiler-version.h`** -> AI Confidence: **99.32%**
1966. **`include/linux/export.h`** -> AI Confidence: **99.32%**
1967. **`include/linux/overflow.h`** -> AI Confidence: **99.32%**
1968. **`include/linux/randomize_kstack.h`** -> AI Confidence: **99.32%**
1969. **`include/sound/asequencer.h`** -> AI Confidence: **99.32%**
1970. **`include/trace/events/kyber.h`** -> AI Confidence: **99.32%**
1971. **`include/trace/events/mmflags.h`** -> AI Confidence: **99.32%**
1972. **`include/trace/events/qrtr.h`** -> AI Confidence: **99.32%**
1973. **`include/trace/events/regulator.h`** -> AI Confidence: **99.32%**
1974. **`include/trace/events/smbus.h`** -> AI Confidence: **99.32%**
1975. **`include/trace/events/spmi.h`** -> AI Confidence: **99.32%**
1976. **`include/trace/events/thp.h`** -> AI Confidence: **99.32%**
1977. **`include/trace/events/tlb.h`** -> AI Confidence: **99.32%**
1978. **`include/uapi/linux/atmbr2684.h`** -> AI Confidence: **99.32%**
1979. **`include/uapi/linux/vm_sockets.h`** -> AI Confidence: **99.32%**
1980. **`scripts/dtc/dtc.c`** -> AI Confidence: **99.32%**
1981. **`scripts/kconfig/nconf.gui.c`** -> AI Confidence: **99.32%**
1982. **`security/keys/permission.c`** -> AI Confidence: **99.32%**
1983. **`sound/pci/emu10k1/irq.c`** -> AI Confidence: **99.32%**
1984. **`sound/soc/amd/acp/acp-sdw-mach-common.c`** -> AI Confidence: **99.32%**
1985. **`sound/soc/codecs/cs35l45-tables.c`** -> AI Confidence: **99.32%**
1986. **`tools/arch/x86/include/uapi/asm/unistd.h`** -> AI Confidence: **99.32%**
1987. **`tools/include/nolibc/stdlib.h`** -> AI Confidence: **99.32%**
1988. **`tools/perf/arch/riscv/include/perf_regs.h`** -> AI Confidence: **99.32%**
1989. **`tools/perf/ui/keysyms.c`** -> AI Confidence: **99.32%**
1990. **`tools/perf/util/spark.c`** -> AI Confidence: **99.32%**
1991. **`tools/testing/selftests/bpf/prog_tests/hashmap.c`** -> AI Confidence: **99.32%**
1992. **`tools/testing/selftests/bpf/prog_tests/mmap.c`** -> AI Confidence: **99.32%**
1993. **`tools/testing/selftests/bpf/prog_tests/netns_cookie.c`** -> AI Confidence: **99.32%**
1994. **`tools/testing/selftests/bpf/prog_tests/sockopt_multi.c`** -> AI Confidence: **99.32%**
1995. **`tools/testing/selftests/bpf/prog_tests/xdp_link.c`** -> AI Confidence: **99.32%**
1996. **`tools/testing/selftests/bpf/prog_tests/xdp_synproxy.c`** -> AI Confidence: **99.32%**
1997. **`tools/testing/selftests/bpf/progs/dev_cgroup.c`** -> AI Confidence: **99.32%**
1998. **`tools/testing/selftests/bpf/progs/verifier_jit_convergence.c`** -> AI Confidence: **99.32%**
1999. **`tools/testing/selftests/kvm/lib/guest_sprintf.c`** -> AI Confidence: **99.32%**
2000. **`tools/testing/selftests/pidfd/pidfd_exec_helper.c`** -> AI Confidence: **99.32%**
2001. **`tools/testing/selftests/powerpc/primitives/asm/asm-compat.h`** -> AI Confidence: **99.32%**
2002. **`Makefile`** -> AI Confidence: **99.31%**
2003. **`tools/testing/selftests/net/netfilter/nft_fib.sh`** -> AI Confidence: **99.31%**
2004. **`tools/testing/selftests/net/netfilter/nft_nat_zones.sh`** -> AI Confidence: **99.31%**
2005. **`Documentation/conf.py`** -> AI Confidence: **99.31%**
2006. **`Documentation/sphinx/kfigure.py`** -> AI Confidence: **99.31%**
2007. **`drivers/gpu/drm/msm/registers/gen_header.py`** -> AI Confidence: **99.31%**
2008. **`drivers/tty/vt/gen_ucs_fallback_table.py`** -> AI Confidence: **99.31%**
2009. **`scripts/bpf_doc.py`** -> AI Confidence: **99.31%**
2010. **`scripts/checkkconfigsymbols.py`** -> AI Confidence: **99.31%**
2011. **`scripts/clang-tools/gen_compile_commands.py`** -> AI Confidence: **99.31%**
2012. **`scripts/gdb/linux/symbols.py`** -> AI Confidence: **99.31%**
2013. **`scripts/make_fit.py`** -> AI Confidence: **99.31%**
2014. **`scripts/spdxcheck.py`** -> AI Confidence: **99.31%**
2015. **`tools/cgroup/iocost_monitor.py`** -> AI Confidence: **99.31%**
2016. **`tools/kvm/kvm_stat/kvm_stat`** -> AI Confidence: **99.31%**
2017. **`tools/lib/python/abi/system_symbols.py`** -> AI Confidence: **99.31%**
2018. **`tools/lib/python/kdoc/python_version.py`** -> AI Confidence: **99.31%**
2019. **`tools/mm/thpmaps`** -> AI Confidence: **99.31%**
2020. **`tools/net/ynl/pyynl/cli.py`** -> AI Confidence: **99.31%**
2021. **`tools/net/ynl/pyynl/ethtool.py`** -> AI Confidence: **99.31%**
2022. **`tools/net/ynl/pyynl/lib/ynl.py`** -> AI Confidence: **99.31%**
2023. **`tools/net/ynl/pyynl/ynl_gen_c.py`** -> AI Confidence: **99.31%**
2024. **`tools/perf/pmu-events/intel_metrics.py`** -> AI Confidence: **99.31%**
2025. **`tools/perf/pmu-events/jevents.py`** -> AI Confidence: **99.31%**
2026. **`tools/perf/scripts/python/arm-cs-trace-disasm.py`** -> AI Confidence: **99.31%**
2027. **`tools/perf/scripts/python/export-to-postgresql.py`** -> AI Confidence: **99.31%**
2028. **`tools/perf/scripts/python/export-to-sqlite.py`** -> AI Confidence: **99.31%**
2029. **`tools/perf/scripts/python/flamegraph.py`** -> AI Confidence: **99.31%**
2030. **`tools/perf/scripts/python/intel-pt-events.py`** -> AI Confidence: **99.31%**
2031. **`tools/perf/scripts/python/netdev-times.py`** -> AI Confidence: **99.31%**
2032. **`tools/perf/scripts/python/parallel-perf.py`** -> AI Confidence: **99.31%**
2033. **`tools/perf/scripts/python/stackcollapse.py`** -> AI Confidence: **99.31%**
2034. **`tools/perf/scripts/python/task-analyzer.py`** -> AI Confidence: **99.31%**
2035. **`tools/perf/tests/shell/lib/attr.py`** -> AI Confidence: **99.31%**
2036. **`tools/perf/tests/shell/lib/perf_metric_validation.py`** -> AI Confidence: **99.31%**
2037. **`tools/power/x86/amd_pstate_tracer/amd_pstate_trace.py`** -> AI Confidence: **99.31%**
2038. **`tools/power/x86/intel_pstate_tracer/intel_pstate_tracer.py`** -> AI Confidence: **99.31%**
2039. **`tools/testing/kunit/kunit.py`** -> AI Confidence: **99.31%**
2040. **`tools/testing/selftests/devices/probe/test_discoverable_devices.py`** -> AI Confidence: **99.31%**
2041. **`tools/testing/selftests/net/bpf_offload.py`** -> AI Confidence: **99.31%**
2042. **`tools/testing/selftests/net/lib/py/utils.py`** -> AI Confidence: **99.31%**
2043. **`tools/testing/selftests/net/openvswitch/ovs-dpctl.py`** -> AI Confidence: **99.31%**
2044. **`tools/testing/selftests/tc-testing/plugin-lib/valgrindPlugin.py`** -> AI Confidence: **99.31%**
2045. **`tools/testing/selftests/tc-testing/tdc.py`** -> AI Confidence: **99.31%**
2046. **`tools/testing/selftests/x86/bugs/its_indirect_alignment.py`** -> AI Confidence: **99.31%**
2047. **`tools/testing/selftests/x86/bugs/its_permutations.py`** -> AI Confidence: **99.31%**
2048. **`tools/testing/selftests/x86/bugs/its_ret_alignment.py`** -> AI Confidence: **99.31%**
2049. **`tools/usb/p9_fwd.py`** -> AI Confidence: **99.31%**
2050. **`tools/workqueue/wq_dump.py`** -> AI Confidence: **99.31%**
2051. **`tools/workqueue/wq_monitor.py`** -> AI Confidence: **99.31%**
2052. **`tools/writeback/wb_monitor.py`** -> AI Confidence: **99.31%**
2053. **`arch/alpha/boot/bootpz.c`** -> AI Confidence: **99.31%**
2054. **`arch/alpha/kernel/core_cia.c`** -> AI Confidence: **99.31%**
2055. **`arch/alpha/kernel/core_irongate.c`** -> AI Confidence: **99.31%**
2056. **`arch/alpha/kernel/core_marvel.c`** -> AI Confidence: **99.31%**
2057. **`arch/alpha/kernel/core_mcpcia.c`** -> AI Confidence: **99.31%**
2058. **`arch/alpha/kernel/core_polaris.c`** -> AI Confidence: **99.31%**
2059. **`arch/alpha/kernel/core_t2.c`** -> AI Confidence: **99.31%**
2060. **`arch/alpha/kernel/core_titan.c`** -> AI Confidence: **99.31%**
2061. **`arch/alpha/kernel/core_tsunami.c`** -> AI Confidence: **99.31%**
2062. **`arch/alpha/kernel/core_wildfire.c`** -> AI Confidence: **99.31%**
2063. **`arch/alpha/kernel/err_common.c`** -> AI Confidence: **99.31%**
2064. **`arch/alpha/kernel/err_ev6.c`** -> AI Confidence: **99.31%**
2065. **`arch/alpha/kernel/err_ev7.c`** -> AI Confidence: **99.31%**
2066. **`arch/alpha/kernel/err_titan.c`** -> AI Confidence: **99.31%**
2067. **`arch/alpha/kernel/pci.c`** -> AI Confidence: **99.31%**
2068. **`arch/alpha/kernel/pci_iommu.c`** -> AI Confidence: **99.31%**
2069. **`arch/alpha/kernel/perf_event.c`** -> AI Confidence: **99.31%**
2070. **`arch/alpha/kernel/signal.c`** -> AI Confidence: **99.31%**
2071. **`arch/alpha/kernel/smc37c669.c`** -> AI Confidence: **99.31%**
2072. **`arch/alpha/kernel/smc37c93x.c`** -> AI Confidence: **99.31%**
2073. **`arch/alpha/kernel/smp.c`** -> AI Confidence: **99.31%**
2074. **`arch/alpha/kernel/srm_env.c`** -> AI Confidence: **99.31%**
2075. **`arch/alpha/kernel/sys_alcor.c`** -> AI Confidence: **99.31%**
2076. **`arch/alpha/kernel/sys_eiger.c`** -> AI Confidence: **99.31%**
2077. **`arch/alpha/kernel/sys_miata.c`** -> AI Confidence: **99.31%**
2078. **`arch/alpha/kernel/sys_nautilus.c`** -> AI Confidence: **99.31%**
2079. **`arch/alpha/kernel/sys_noritake.c`** -> AI Confidence: **99.31%**
2080. **`arch/alpha/kernel/sys_ruffian.c`** -> AI Confidence: **99.31%**
2081. **`arch/alpha/kernel/sys_takara.c`** -> AI Confidence: **99.31%**
2082. **`arch/alpha/kernel/sys_wildfire.c`** -> AI Confidence: **99.31%**
2083. **`arch/alpha/kernel/time.c`** -> AI Confidence: **99.31%**
2084. **`arch/alpha/kernel/traps.c`** -> AI Confidence: **99.31%**
2085. **`arch/arc/kernel/module.c`** -> AI Confidence: **99.31%**
2086. **`arch/arc/kernel/smp.c`** -> AI Confidence: **99.31%**
2087. **`arch/arc/kernel/troubleshoot.c`** -> AI Confidence: **99.31%**
2088. **`arch/arc/mm/cache.c`** -> AI Confidence: **99.31%**
2089. **`arch/arc/mm/tlb.c`** -> AI Confidence: **99.31%**
2090. **`arch/arm/boot/compressed/decompress.c`** -> AI Confidence: **99.31%**
2091. **`arch/arm/common/mcpm_entry.c`** -> AI Confidence: **99.31%**
2092. **`arch/arm/include/asm/arch_timer.h`** -> AI Confidence: **99.31%**
2093. **`arch/arm/kernel/dma.c`** -> AI Confidence: **99.31%**
2094. **`arch/arm/kernel/elf.c`** -> AI Confidence: **99.31%**
2095. **`arch/arm/kernel/hw_breakpoint.c`** -> AI Confidence: **99.31%**
2096. **`arch/arm/kernel/irq.c`** -> AI Confidence: **99.31%**
2097. **`arch/arm/kernel/module-plts.c`** -> AI Confidence: **99.31%**
2098. **`arch/arm/kernel/patch.c`** -> AI Confidence: **99.31%**
2099. **`arch/arm/kernel/setup.c`** -> AI Confidence: **99.31%**
2100. **`arch/arm/kernel/signal.c`** -> AI Confidence: **99.31%**
2101. **`arch/arm/kernel/stacktrace.c`** -> AI Confidence: **99.31%**
2102. **`arch/arm/kernel/swp_emulate.c`** -> AI Confidence: **99.31%**
2103. **`arch/arm/kernel/tcm.c`** -> AI Confidence: **99.31%**
2104. **`arch/arm/kernel/time.c`** -> AI Confidence: **99.31%**
2105. **`arch/arm/kernel/topology.c`** -> AI Confidence: **99.31%**
2106. **`arch/arm/kernel/traps.c`** -> AI Confidence: **99.31%**
2107. **`arch/arm/kernel/unwind.c`** -> AI Confidence: **99.31%**
2108. **`arch/arm/mach-at91/pm.c`** -> AI Confidence: **99.31%**
2109. **`arch/arm/mach-bcm/bcm63xx_pmb.c`** -> AI Confidence: **99.31%**
2110. **`arch/arm/mach-bcm/platsmp-brcmstb.c`** -> AI Confidence: **99.31%**
2111. **`arch/arm/mach-davinci/pm.c`** -> AI Confidence: **99.31%**
2112. **`arch/arm/mach-dove/mpp.c`** -> AI Confidence: **99.31%**
2113. **`arch/arm/mach-exynos/exynos.c`** -> AI Confidence: **99.31%**
2114. **`arch/arm/mach-exynos/firmware.c`** -> AI Confidence: **99.31%**
2115. **`arch/arm/mach-exynos/platsmp.c`** -> AI Confidence: **99.31%**
2116. **`arch/arm/mach-exynos/pm.c`** -> AI Confidence: **99.31%**
2117. **`arch/arm/mach-footbridge/dma-isa.c`** -> AI Confidence: **99.31%**
2118. **`arch/arm/mach-hisi/platmcpm.c`** -> AI Confidence: **99.31%**
2119. **`arch/arm/mach-imx/mach-imx6q.c`** -> AI Confidence: **99.31%**
2120. **`arch/arm/mach-imx/mach-imx6sl.c`** -> AI Confidence: **99.31%**
2121. **`arch/arm/mach-imx/mach-imx7ulp.c`** -> AI Confidence: **99.31%**
2122. **`arch/arm/mach-imx/pm-imx5.c`** -> AI Confidence: **99.31%**
2123. **`arch/arm/mach-imx/pm-imx6.c`** -> AI Confidence: **99.31%**
2124. **`arch/arm/mach-lpc32xx/serial.c`** -> AI Confidence: **99.31%**
2125. **`arch/arm/mach-meson/platsmp.c`** -> AI Confidence: **99.31%**
2126. **`arch/arm/mach-mvebu/pm-board.c`** -> AI Confidence: **99.31%**
2127. **`arch/arm/mach-mxs/mach-mxs.c`** -> AI Confidence: **99.31%**
2128. **`arch/arm/mach-omap1/clock.c`** -> AI Confidence: **99.31%**
2129. **`arch/arm/mach-omap1/devices.c`** -> AI Confidence: **99.31%**
2130. **`arch/arm/mach-omap1/dma.c`** -> AI Confidence: **99.31%**
2131. **`arch/arm/mach-omap1/irq.c`** -> AI Confidence: **99.31%**
2132. **`arch/arm/mach-omap1/mcbsp.c`** -> AI Confidence: **99.31%**
2133. **`arch/arm/mach-omap1/omap-dma.c`** -> AI Confidence: **99.31%**
2134. **`arch/arm/mach-omap1/pm.c`** -> AI Confidence: **99.31%**
2135. **`arch/arm/mach-omap1/serial.c`** -> AI Confidence: **99.31%**
2136. **`arch/arm/mach-omap2/board-n8x0.c`** -> AI Confidence: **99.31%**
2137. **`arch/arm/mach-omap2/clkt2xxx_dpllcore.c`** -> AI Confidence: **99.31%**
2138. **`arch/arm/mach-omap2/clkt2xxx_virt_prcm_set.c`** -> AI Confidence: **99.31%**
2139. **`arch/arm/mach-omap2/cpuidle34xx.c`** -> AI Confidence: **99.31%**
2140. **`arch/arm/mach-omap2/cpuidle44xx.c`** -> AI Confidence: **99.31%**
2141. **`arch/arm/mach-omap2/display.c`** -> AI Confidence: **99.31%**
2142. **`arch/arm/mach-omap2/hdq1w.c`** -> AI Confidence: **99.31%**
2143. **`arch/arm/mach-omap2/id.c`** -> AI Confidence: **99.31%**
2144. **`arch/arm/mach-omap2/msdi.c`** -> AI Confidence: **99.31%**
2145. **`arch/arm/mach-omap2/omap-mpuss-lowpower.c`** -> AI Confidence: **99.31%**
2146. **`arch/arm/mach-omap2/omap-smp.c`** -> AI Confidence: **99.31%**
2147. **`arch/arm/mach-omap2/pm34xx.c`** -> AI Confidence: **99.31%**
2148. **`arch/arm/mach-omap2/pm44xx.c`** -> AI Confidence: **99.31%**
2149. **`arch/arm/mach-omap2/pmic-cpcap.c`** -> AI Confidence: **99.31%**
2150. **`arch/arm/mach-omap2/powerdomain-common.c`** -> AI Confidence: **99.31%**
2151. **`arch/arm/mach-omap2/powerdomain.c`** -> AI Confidence: **99.31%**
2152. **`arch/arm/mach-omap2/sdrc2xxx.c`** -> AI Confidence: **99.31%**
2153. **`arch/arm/mach-omap2/sr_device.c`** -> AI Confidence: **99.31%**
2154. **`arch/arm/mach-omap2/vc.c`** -> AI Confidence: **99.31%**
2155. **`arch/arm/mach-omap2/vp.c`** -> AI Confidence: **99.31%**
2156. **`arch/arm/mach-omap2/wd_timer.c`** -> AI Confidence: **99.31%**
2157. **`arch/arm/mach-orion5x/board-rd88f5182.c`** -> AI Confidence: **99.31%**
2158. **`arch/arm/mach-orion5x/common.c`** -> AI Confidence: **99.31%**
2159. **`arch/arm/mach-orion5x/dns323-setup.c`** -> AI Confidence: **99.31%**
2160. **`arch/arm/mach-orion5x/kurobox_pro-setup.c`** -> AI Confidence: **99.31%**
2161. **`arch/arm/mach-orion5x/net2big-setup.c`** -> AI Confidence: **99.31%**
2162. **`arch/arm/mach-orion5x/terastation_pro2-setup.c`** -> AI Confidence: **99.31%**
2163. **`arch/arm/mach-orion5x/ts78xx-setup.c`** -> AI Confidence: **99.31%**
2164. **`arch/arm/mach-orion5x/tsx09-common.c`** -> AI Confidence: **99.31%**
2165. **`arch/arm/mach-pxa/generic.c`** -> AI Confidence: **99.31%**
2166. **`arch/arm/mach-pxa/pxa3xx.c`** -> AI Confidence: **99.31%**
2167. **`arch/arm/mach-pxa/reset.c`** -> AI Confidence: **99.31%**
2168. **`arch/arm/mach-pxa/sharpsl_pm.c`** -> AI Confidence: **99.31%**
2169. **`arch/arm/mach-pxa/spitz_pm.c`** -> AI Confidence: **99.31%**
2170. **`arch/arm/mach-rpc/dma.c`** -> AI Confidence: **99.31%**
2171. **`arch/arm/mach-rpc/ecard.c`** -> AI Confidence: **99.31%**
2172. **`arch/arm/mach-s3c/pm-gpio.c`** -> AI Confidence: **99.31%**
2173. **`arch/arm/mach-s3c/setup-usb-phy-s3c64xx.c`** -> AI Confidence: **99.31%**
2174. **`arch/arm/mach-s3c/wakeup-mask.c`** -> AI Confidence: **99.31%**
2175. **`arch/arm/mach-sa1100/h3600.c`** -> AI Confidence: **99.31%**
2176. **`arch/arm/mach-shmobile/regulator-quirk-rcar-gen2.c`** -> AI Confidence: **99.31%**
2177. **`arch/arm/mach-shmobile/setup-rcar-gen2.c`** -> AI Confidence: **99.31%**
2178. **`arch/arm/mach-socfpga/pm.c`** -> AI Confidence: **99.31%**
2179. **`arch/arm/mach-sti/platsmp.c`** -> AI Confidence: **99.31%**
2180. **`arch/arm/mach-sunxi/mc_smp.c`** -> AI Confidence: **99.31%**
2181. **`arch/arm/mach-tegra/hotplug.c`** -> AI Confidence: **99.31%**
2182. **`arch/arm/mach-tegra/platsmp.c`** -> AI Confidence: **99.31%**
2183. **`arch/arm/mach-tegra/pm.c`** -> AI Confidence: **99.31%**
2184. **`arch/arm/mach-tegra/tegra.c`** -> AI Confidence: **99.31%**
2185. **`arch/arm/mach-versatile/platsmp.c`** -> AI Confidence: **99.31%**
2186. **`arch/arm/mach-vt8500/vt8500.c`** -> AI Confidence: **99.31%**
2187. **`arch/arm/mm/cache-b15-rac.c`** -> AI Confidence: **99.31%**
2188. **`arch/arm/mm/fault-armv.c`** -> AI Confidence: **99.31%**
2189. **`arch/arm/mm/fault.c`** -> AI Confidence: **99.31%**
2190. **`arch/arm/mm/flush.c`** -> AI Confidence: **99.31%**
2191. **`arch/arm/mm/idmap.c`** -> AI Confidence: **99.31%**
2192. **`arch/arm/mm/mmap.c`** -> AI Confidence: **99.31%**
2193. **`arch/arm/mm/mmu.c`** -> AI Confidence: **99.31%**
2194. **`arch/arm/mm/proc-v7-bugs.c`** -> AI Confidence: **99.31%**
2195. **`arch/arm/net/bpf_jit_32.c`** -> AI Confidence: **99.31%**
2196. **`arch/arm/plat-orion/mpp.c`** -> AI Confidence: **99.31%**
2197. **`arch/arm/vdso/vdsomunge.c`** -> AI Confidence: **99.31%**
2198. **`arch/arm/vfp/vfpmodule.c`** -> AI Confidence: **99.31%**
2199. **`arch/arm64/include/asm/simd.h`** -> AI Confidence: **99.31%**
2200. **`arch/arm64/include/asm/uaccess.h`** -> AI Confidence: **99.31%**
2201. **`arch/arm64/kernel/acpi.c`** -> AI Confidence: **99.31%**
2202. **`arch/arm64/kernel/armv8_deprecated.c`** -> AI Confidence: **99.31%**
2203. **`arch/arm64/kernel/compat_alignment.c`** -> AI Confidence: **99.31%**
2204. **`arch/arm64/kernel/entry-common.c`** -> AI Confidence: **99.31%**
2205. **`arch/arm64/kernel/hw_breakpoint.c`** -> AI Confidence: **99.31%**
2206. **`arch/arm64/kernel/machine_kexec_file.c`** -> AI Confidence: **99.31%**
2207. **`arch/arm64/kernel/module.c`** -> AI Confidence: **99.31%**
2208. **`arch/arm64/kernel/pi/idreg-override.c`** -> AI Confidence: **99.31%**
2209. **`arch/arm64/kernel/pi/kaslr_early.c`** -> AI Confidence: **99.31%**
2210. **`arch/arm64/kernel/pi/relacheck.c`** -> AI Confidence: **99.31%**
2211. **`arch/arm64/kernel/pointer_auth.c`** -> AI Confidence: **99.31%**
2212. **`arch/arm64/kernel/process.c`** -> AI Confidence: **99.31%**
2213. **`arch/arm64/kernel/sdei.c`** -> AI Confidence: **99.31%**
2214. **`arch/arm64/kernel/signal.c`** -> AI Confidence: **99.31%**
2215. **`arch/arm64/kernel/smp.c`** -> AI Confidence: **99.31%**
2216. **`arch/arm64/kernel/sys_compat.c`** -> AI Confidence: **99.31%**
2217. **`arch/arm64/kvm/arch_timer.c`** -> AI Confidence: **99.31%**
2218. **`arch/arm64/kvm/arm.c`** -> AI Confidence: **99.31%**
2219. **`arch/arm64/kvm/guest.c`** -> AI Confidence: **99.31%**
2220. **`arch/arm64/kvm/handle_exit.c`** -> AI Confidence: **99.31%**
2221. **`arch/arm64/kvm/hyp/include/hyp/switch.h`** -> AI Confidence: **99.31%**
2222. **`arch/arm64/kvm/hyp/nvhe/ffa.c`** -> AI Confidence: **99.31%**
2223. **`arch/arm64/kvm/hyp/vgic-v3-sr.c`** -> AI Confidence: **99.31%**
2224. **`arch/arm64/kvm/nested.c`** -> AI Confidence: **99.31%**
2225. **`arch/arm64/kvm/psci.c`** -> AI Confidence: **99.31%**
2226. **`arch/arm64/kvm/reset.c`** -> AI Confidence: **99.31%**
2227. **`arch/arm64/kvm/vgic/vgic-init.c`** -> AI Confidence: **99.31%**
2228. **`arch/arm64/kvm/vgic/vgic-kvm-device.c`** -> AI Confidence: **99.31%**
2229. **`arch/arm64/kvm/vgic/vgic-mmio-v2.c`** -> AI Confidence: **99.31%**
2230. **`arch/arm64/mm/context.c`** -> AI Confidence: **99.31%**
2231. **`arch/arm64/mm/fixmap.c`** -> AI Confidence: **99.31%**
2232. **`arch/arm64/mm/gcs.c`** -> AI Confidence: **99.31%**
2233. **`arch/arm64/mm/hugetlbpage.c`** -> AI Confidence: **99.31%**
2234. **`arch/arm64/mm/init.c`** -> AI Confidence: **99.31%**
2235. **`arch/arm64/net/bpf_jit_comp.c`** -> AI Confidence: **99.31%**
2236. **`arch/csky/abiv1/mmap.c`** -> AI Confidence: **99.31%**
2237. **`arch/csky/mm/dma-mapping.c`** -> AI Confidence: **99.31%**
2238. **`arch/csky/mm/init.c`** -> AI Confidence: **99.31%**
2239. **`arch/hexagon/kernel/traps.c`** -> AI Confidence: **99.31%**
2240. **`arch/hexagon/mm/vm_fault.c`** -> AI Confidence: **99.31%**
2241. **`arch/loongarch/kernel/alternative.c`** -> AI Confidence: **99.31%**
2242. **`arch/loongarch/kernel/ftrace.c`** -> AI Confidence: **99.31%**
2243. **`arch/loongarch/kernel/kgdb.c`** -> AI Confidence: **99.31%**
2244. **`arch/loongarch/kernel/module.c`** -> AI Confidence: **99.31%**
2245. **`arch/loongarch/kernel/proc.c`** -> AI Confidence: **99.31%**
2246. **`arch/loongarch/kernel/signal.c`** -> AI Confidence: **99.31%**
2247. **`arch/loongarch/kernel/traps.c`** -> AI Confidence: **99.31%**
2248. **`arch/loongarch/kernel/unwind_orc.c`** -> AI Confidence: **99.31%**
2249. **`arch/loongarch/mm/cache.c`** -> AI Confidence: **99.31%**
2250. **`arch/loongarch/mm/hugetlbpage.c`** -> AI Confidence: **99.31%**
2251. **`arch/loongarch/mm/mmap.c`** -> AI Confidence: **99.31%**
2252. **`arch/loongarch/mm/tlb.c`** -> AI Confidence: **99.31%**
2253. **`arch/m68k/68000/m68328.c`** -> AI Confidence: **99.31%**
2254. **`arch/m68k/amiga/cia.c`** -> AI Confidence: **99.31%**
2255. **`arch/m68k/amiga/platform.c`** -> AI Confidence: **99.31%**
2256. **`arch/m68k/apollo/config.c`** -> AI Confidence: **99.31%**
2257. **`arch/m68k/atari/config.c`** -> AI Confidence: **99.31%**
2258. **`arch/m68k/bvme6000/rtc.c`** -> AI Confidence: **99.31%**
2259. **`arch/m68k/coldfire/device.c`** -> AI Confidence: **99.31%**
2260. **`arch/m68k/coldfire/intc-2.c`** -> AI Confidence: **99.31%**
2261. **`arch/m68k/coldfire/intc-5272.c`** -> AI Confidence: **99.31%**
2262. **`arch/m68k/coldfire/m5307.c`** -> AI Confidence: **99.31%**
2263. **`arch/m68k/coldfire/pci.c`** -> AI Confidence: **99.31%**
2264. **`arch/m68k/hp300/config.c`** -> AI Confidence: **99.31%**
2265. **`arch/m68k/include/asm/bitops.h`** -> AI Confidence: **99.31%**
2266. **`arch/m68k/include/asm/pgalloc.h`** -> AI Confidence: **99.31%**
2267. **`arch/m68k/kernel/early_printk.c`** -> AI Confidence: **99.31%**
2268. **`arch/m68k/kernel/ptrace.c`** -> AI Confidence: **99.31%**
2269. **`arch/m68k/kernel/setup_mm.c`** -> AI Confidence: **99.31%**
2270. **`arch/m68k/mac/config.c`** -> AI Confidence: **99.31%**
2271. **`arch/m68k/mac/misc.c`** -> AI Confidence: **99.31%**
2272. **`arch/m68k/mac/oss.c`** -> AI Confidence: **99.31%**
2273. **`arch/m68k/mm/init.c`** -> AI Confidence: **99.31%**
2274. **`arch/m68k/mm/motorola.c`** -> AI Confidence: **99.31%**
2275. **`arch/m68k/mm/sun3mmu.c`** -> AI Confidence: **99.31%**
2276. **`arch/m68k/mvme16x/config.c`** -> AI Confidence: **99.31%**
2277. **`arch/m68k/q40/q40ints.c`** -> AI Confidence: **99.31%**
2278. **`arch/m68k/sun3/idprom.c`** -> AI Confidence: **99.31%**
2279. **`arch/m68k/sun3x/config.c`** -> AI Confidence: **99.31%**
2280. **`arch/microblaze/kernel/cpu/mb.c`** -> AI Confidence: **99.31%**
2281. **`arch/microblaze/kernel/exceptions.c`** -> AI Confidence: **99.31%**
2282. **`arch/microblaze/kernel/module.c`** -> AI Confidence: **99.31%**
2283. **`arch/microblaze/kernel/ptrace.c`** -> AI Confidence: **99.31%**
2284. **`arch/microblaze/kernel/setup.c`** -> AI Confidence: **99.31%**
2285. **`arch/microblaze/kernel/signal.c`** -> AI Confidence: **99.31%**
2286. **`arch/microblaze/kernel/traps.c`** -> AI Confidence: **99.31%**
2287. **`arch/microblaze/kernel/unwind.c`** -> AI Confidence: **99.31%**
2288. **`arch/microblaze/mm/fault.c`** -> AI Confidence: **99.31%**
2289. **`arch/microblaze/mm/pgtable.c`** -> AI Confidence: **99.31%**
2290. **`arch/mips/alchemy/common/clock.c`** -> AI Confidence: **99.31%**
2291. **`arch/mips/alchemy/common/dbdma.c`** -> AI Confidence: **99.31%**
2292. **`arch/mips/alchemy/common/dma.c`** -> AI Confidence: **99.31%**
2293. **`arch/mips/alchemy/common/prom.c`** -> AI Confidence: **99.31%**
2294. **`arch/mips/alchemy/common/usb.c`** -> AI Confidence: **99.31%**
2295. **`arch/mips/alchemy/devboards/db1200.c`** -> AI Confidence: **99.31%**
2296. **`arch/mips/alchemy/devboards/platform.c`** -> AI Confidence: **99.31%**
2297. **`arch/mips/alchemy/devboards/pm.c`** -> AI Confidence: **99.31%**
2298. **`arch/mips/ath79/early_printk.c`** -> AI Confidence: **99.31%**
2299. **`arch/mips/bcm47xx/irq.c`** -> AI Confidence: **99.31%**
2300. **`arch/mips/bcm47xx/setup.c`** -> AI Confidence: **99.31%**
2301. **`arch/mips/bcm63xx/boards/board_bcm963xx.c`** -> AI Confidence: **99.31%**
2302. **`arch/mips/bcm63xx/clk.c`** -> AI Confidence: **99.31%**
2303. **`arch/mips/bcm63xx/cs.c`** -> AI Confidence: **99.31%**
2304. **`arch/mips/bcm63xx/dev-enet.c`** -> AI Confidence: **99.31%**
2305. **`arch/mips/bcm63xx/dev-flash.c`** -> AI Confidence: **99.31%**
2306. **`arch/mips/bcm63xx/dev-pcmcia.c`** -> AI Confidence: **99.31%**
2307. **`arch/mips/bcm63xx/dev-spi.c`** -> AI Confidence: **99.31%**
2308. **`arch/mips/bcm63xx/gpio.c`** -> AI Confidence: **99.31%**
2309. **`arch/mips/bcm63xx/nvram.c`** -> AI Confidence: **99.31%**
2310. **`arch/mips/bcm63xx/setup.c`** -> AI Confidence: **99.31%**
2311. **`arch/mips/boot/compressed/calc_vmlinuz_load_addr.c`** -> AI Confidence: **99.31%**
2312. **`arch/mips/cavium-octeon/dma-octeon.c`** -> AI Confidence: **99.31%**
2313. **`arch/mips/cavium-octeon/executive/cvmx-cmd-queue.c`** -> AI Confidence: **99.31%**
2314. **`arch/mips/cavium-octeon/executive/cvmx-helper-board.c`** -> AI Confidence: **99.31%**
2315. **`arch/mips/cavium-octeon/executive/cvmx-helper-spi.c`** -> AI Confidence: **99.31%**
2316. **`arch/mips/cavium-octeon/executive/cvmx-helper-util.c`** -> AI Confidence: **99.31%**
2317. **`arch/mips/cavium-octeon/executive/cvmx-helper.c`** -> AI Confidence: **99.31%**
2318. **`arch/mips/cavium-octeon/setup.c`** -> AI Confidence: **99.31%**
2319. **`arch/mips/dec/ecc-berr.c`** -> AI Confidence: **99.31%**
2320. **`arch/mips/dec/prom/identify.c`** -> AI Confidence: **99.31%**
2321. **`arch/mips/dec/prom/memory.c`** -> AI Confidence: **99.31%**
2322. **`arch/mips/dec/setup.c`** -> AI Confidence: **99.31%**
2323. **`arch/mips/dec/time.c`** -> AI Confidence: **99.31%**
2324. **`arch/mips/fw/arc/memory.c`** -> AI Confidence: **99.31%**
2325. **`arch/mips/generic/yamon-dt.c`** -> AI Confidence: **99.31%**
2326. **`arch/mips/include/asm/bitops.h`** -> AI Confidence: **99.31%**
2327. **`arch/mips/include/asm/futex.h`** -> AI Confidence: **99.31%**
2328. **`arch/mips/include/asm/io.h`** -> AI Confidence: **99.31%**
2329. **`arch/mips/include/asm/mips-cps.h`** -> AI Confidence: **99.31%**
2330. **`arch/mips/include/asm/pgtable-32.h`** -> AI Confidence: **99.31%**
2331. **`arch/mips/kernel/cevt-r4k.c`** -> AI Confidence: **99.31%**
2332. **`arch/mips/kernel/cpu-r3k-probe.c`** -> AI Confidence: **99.31%**
2333. **`arch/mips/kernel/fpu-probe.c`** -> AI Confidence: **99.31%**
2334. **`arch/mips/kernel/ftrace.c`** -> AI Confidence: **99.31%**
2335. **`arch/mips/kernel/irq-msc01.c`** -> AI Confidence: **99.31%**
2336. **`arch/mips/kernel/kprobes.c`** -> AI Confidence: **99.31%**
2337. **`arch/mips/kernel/mips-cm.c`** -> AI Confidence: **99.31%**
2338. **`arch/mips/kernel/mips-mt-fpaff.c`** -> AI Confidence: **99.31%**
2339. **`arch/mips/kernel/mips-r2-to-r6-emul.c`** -> AI Confidence: **99.31%**
2340. **`arch/mips/kernel/perf_event_mipsxx.c`** -> AI Confidence: **99.31%**
2341. **`arch/mips/kernel/pm-cps.c`** -> AI Confidence: **99.31%**
2342. **`arch/mips/kernel/process.c`** -> AI Confidence: **99.31%**
2343. **`arch/mips/kernel/rtlx-mt.c`** -> AI Confidence: **99.31%**
2344. **`arch/mips/kernel/setup.c`** -> AI Confidence: **99.31%**
2345. **`arch/mips/kernel/smp-bmips.c`** -> AI Confidence: **99.31%**
2346. **`arch/mips/kernel/smp-cps.c`** -> AI Confidence: **99.31%**
2347. **`arch/mips/kernel/traps.c`** -> AI Confidence: **99.31%**
2348. **`arch/mips/kernel/vdso.c`** -> AI Confidence: **99.31%**
2349. **`arch/mips/kvm/mips.c`** -> AI Confidence: **99.31%**
2350. **`arch/mips/lantiq/falcon/sysctrl.c`** -> AI Confidence: **99.31%**
2351. **`arch/mips/lantiq/xway/dma.c`** -> AI Confidence: **99.31%**
2352. **`arch/mips/lantiq/xway/sysctrl.c`** -> AI Confidence: **99.31%**
2353. **`arch/mips/loongson2ef/common/mem.c`** -> AI Confidence: **99.31%**
2354. **`arch/mips/loongson2ef/lemote-2f/irq.c`** -> AI Confidence: **99.31%**
2355. **`arch/mips/loongson2ef/lemote-2f/reset.c`** -> AI Confidence: **99.31%**
2356. **`arch/mips/loongson64/cpucfg-emul.c`** -> AI Confidence: **99.31%**
2357. **`arch/mips/loongson64/init.c`** -> AI Confidence: **99.31%**
2358. **`arch/mips/loongson64/numa.c`** -> AI Confidence: **99.31%**
2359. **`arch/mips/mm/c-octeon.c`** -> AI Confidence: **99.31%**
2360. **`arch/mips/mm/init.c`** -> AI Confidence: **99.31%**
2361. **`arch/mips/mm/sc-mips.c`** -> AI Confidence: **99.31%**
2362. **`arch/mips/mm/tlb-r3k.c`** -> AI Confidence: **99.31%**
2363. **`arch/mips/mm/tlb-r4k.c`** -> AI Confidence: **99.31%**
2364. **`arch/mips/mm/tlbex.c`** -> AI Confidence: **99.31%**
2365. **`arch/mips/mti-malta/malta-setup.c`** -> AI Confidence: **99.31%**
2366. **`arch/mips/mti-malta/malta-time.c`** -> AI Confidence: **99.31%**
2367. **`arch/mips/pci/msi-octeon.c`** -> AI Confidence: **99.31%**
2368. **`arch/mips/pci/ops-lantiq.c`** -> AI Confidence: **99.31%**
2369. **`arch/mips/pci/ops-loongson2.c`** -> AI Confidence: **99.31%**
2370. **`arch/mips/pci/ops-rc32434.c`** -> AI Confidence: **99.31%**
2371. **`arch/mips/pci/pci-bcm1480.c`** -> AI Confidence: **99.31%**
2372. **`arch/mips/pci/pci-bcm63xx.c`** -> AI Confidence: **99.31%**
2373. **`arch/mips/pci/pci-malta.c`** -> AI Confidence: **99.31%**
2374. **`arch/mips/pci/pci-mt7620.c`** -> AI Confidence: **99.31%**
2375. **`arch/mips/pci/pci-octeon.c`** -> AI Confidence: **99.31%**
2376. **`arch/mips/pci/pcie-octeon.c`** -> AI Confidence: **99.31%**
2377. **`arch/mips/ralink/clk.c`** -> AI Confidence: **99.31%**
2378. **`arch/mips/ralink/mt7620.c`** -> AI Confidence: **99.31%**
2379. **`arch/mips/ralink/rt305x.c`** -> AI Confidence: **99.31%**
2380. **`arch/mips/rb532/irq.c`** -> AI Confidence: **99.31%**
2381. **`arch/mips/rb532/prom.c`** -> AI Confidence: **99.31%**
2382. **`arch/mips/sgi-ip22/ip22-berr.c`** -> AI Confidence: **99.31%**
2383. **`arch/mips/sgi-ip22/ip22-eisa.c`** -> AI Confidence: **99.31%**
2384. **`arch/mips/sgi-ip22/ip22-gio.c`** -> AI Confidence: **99.31%**
2385. **`arch/mips/sgi-ip22/ip22-int.c`** -> AI Confidence: **99.31%**
2386. **`arch/mips/sgi-ip22/ip22-mc.c`** -> AI Confidence: **99.31%**
2387. **`arch/mips/sgi-ip22/ip22-time.c`** -> AI Confidence: **99.31%**
2388. **`arch/mips/sgi-ip22/ip28-berr.c`** -> AI Confidence: **99.31%**
2389. **`arch/mips/sgi-ip27/ip27-berr.c`** -> AI Confidence: **99.31%**
2390. **`arch/mips/sgi-ip27/ip27-init.c`** -> AI Confidence: **99.31%**
2391. **`arch/mips/sgi-ip27/ip27-klconfig.c`** -> AI Confidence: **99.31%**
2392. **`arch/mips/sgi-ip27/ip27-memory.c`** -> AI Confidence: **99.31%**
2393. **`arch/mips/sgi-ip27/ip27-nmi.c`** -> AI Confidence: **99.31%**
2394. **`arch/mips/sgi-ip30/ip30-setup.c`** -> AI Confidence: **99.31%**
2395. **`arch/mips/sgi-ip30/ip30-xtalk.c`** -> AI Confidence: **99.31%**
2396. **`arch/mips/sgi-ip32/crime.c`** -> AI Confidence: **99.31%**
2397. **`arch/mips/sgi-ip32/ip32-irq.c`** -> AI Confidence: **99.31%**
2398. **`arch/mips/sgi-ip32/ip32-memory.c`** -> AI Confidence: **99.31%**
2399. **`arch/mips/sgi-ip32/ip32-setup.c`** -> AI Confidence: **99.31%**
2400. **`arch/mips/sibyte/bcm1480/irq.c`** -> AI Confidence: **99.31%**
2401. **`arch/mips/sibyte/common/sb_tbprof.c`** -> AI Confidence: **99.31%**
2402. **`arch/mips/sibyte/swarm/platform.c`** -> AI Confidence: **99.31%**
2403. **`arch/mips/sibyte/swarm/rtc_m41t81.c`** -> AI Confidence: **99.31%**
2404. **`arch/mips/sibyte/swarm/rtc_xicor1241.c`** -> AI Confidence: **99.31%**
2405. **`arch/mips/sibyte/swarm/setup.c`** -> AI Confidence: **99.31%**
2406. **`arch/mips/sni/irq.c`** -> AI Confidence: **99.31%**
2407. **`arch/mips/sni/pcimt.c`** -> AI Confidence: **99.31%**
2408. **`arch/mips/sni/time.c`** -> AI Confidence: **99.31%**
2409. **`arch/mips/txx9/generic/pci.c`** -> AI Confidence: **99.31%**
2410. **`arch/mips/txx9/generic/setup.c`** -> AI Confidence: **99.31%**
2411. **`arch/mips/txx9/rbtx4927/irq.c`** -> AI Confidence: **99.31%**
2412. **`arch/mips/vdso/genvdso.c`** -> AI Confidence: **99.31%**
2413. **`arch/nios2/kernel/cpuinfo.c`** -> AI Confidence: **99.31%**
2414. **`arch/nios2/kernel/misaligned.c`** -> AI Confidence: **99.31%**
2415. **`arch/nios2/kernel/module.c`** -> AI Confidence: **99.31%**
2416. **`arch/nios2/mm/cacheflush.c`** -> AI Confidence: **99.31%**
2417. **`arch/nios2/mm/dma-mapping.c`** -> AI Confidence: **99.31%**
2418. **`arch/nios2/mm/ioremap.c`** -> AI Confidence: **99.31%**
2419. **`arch/nios2/mm/tlb.c`** -> AI Confidence: **99.31%**
2420. **`arch/openrisc/kernel/signal.c`** -> AI Confidence: **99.31%**
2421. **`arch/openrisc/kernel/traps.c`** -> AI Confidence: **99.31%**
2422. **`arch/openrisc/mm/ioremap.c`** -> AI Confidence: **99.31%**
2423. **`arch/parisc/boot/compressed/misc.c`** -> AI Confidence: **99.31%**
2424. **`arch/parisc/include/asm/bitops.h`** -> AI Confidence: **99.31%**
2425. **`arch/parisc/include/asm/pgtable.h`** -> AI Confidence: **99.31%**
2426. **`arch/parisc/kernel/cache.c`** -> AI Confidence: **99.31%**
2427. **`arch/parisc/kernel/inventory.c`** -> AI Confidence: **99.31%**
2428. **`arch/parisc/kernel/irq.c`** -> AI Confidence: **99.31%**
2429. **`arch/parisc/kernel/kexec_file.c`** -> AI Confidence: **99.31%**
2430. **`arch/parisc/kernel/module.c`** -> AI Confidence: **99.31%**
2431. **`arch/parisc/kernel/pci-dma.c`** -> AI Confidence: **99.31%**
2432. **`arch/parisc/kernel/pci.c`** -> AI Confidence: **99.31%**
2433. **`arch/parisc/kernel/pdt.c`** -> AI Confidence: **99.31%**
2434. **`arch/parisc/kernel/perf.c`** -> AI Confidence: **99.31%**
2435. **`arch/parisc/kernel/process.c`** -> AI Confidence: **99.31%**
2436. **`arch/parisc/kernel/processor.c`** -> AI Confidence: **99.31%**
2437. **`arch/parisc/kernel/ptrace.c`** -> AI Confidence: **99.31%**
2438. **`arch/parisc/kernel/signal.c`** -> AI Confidence: **99.31%**
2439. **`arch/parisc/kernel/sys_parisc.c`** -> AI Confidence: **99.31%**
2440. **`arch/parisc/kernel/toc.c`** -> AI Confidence: **99.31%**
2441. **`arch/parisc/kernel/traps.c`** -> AI Confidence: **99.31%**
2442. **`arch/parisc/mm/init.c`** -> AI Confidence: **99.31%**
2443. **`arch/powerpc/boot/devtree.c`** -> AI Confidence: **99.31%**
2444. **`arch/powerpc/boot/main.c`** -> AI Confidence: **99.31%**
2445. **`arch/powerpc/boot/of.c`** -> AI Confidence: **99.31%**
2446. **`arch/powerpc/boot/serial.c`** -> AI Confidence: **99.31%**
2447. **`arch/powerpc/boot/treeboot-currituck.c`** -> AI Confidence: **99.31%**
2448. **`arch/powerpc/crypto/vmx.c`** -> AI Confidence: **99.31%**
2449. **`arch/powerpc/include/asm/nohash/32/pgtable.h`** -> AI Confidence: **99.31%**
2450. **`arch/powerpc/include/asm/plpar_wrappers.h`** -> AI Confidence: **99.31%**
2451. **`arch/powerpc/include/asm/reg.h`** -> AI Confidence: **99.31%**
2452. **`arch/powerpc/include/asm/uaccess.h`** -> AI Confidence: **99.31%**
2453. **`arch/powerpc/kernel/align.c`** -> AI Confidence: **99.31%**
2454. **`arch/powerpc/kernel/asm-offsets.c`** -> AI Confidence: **99.31%**
2455. **`arch/powerpc/kernel/btext.c`** -> AI Confidence: **99.31%**
2456. **`arch/powerpc/kernel/compat_audit.c`** -> AI Confidence: **99.31%**
2457. **`arch/powerpc/kernel/crash_dump.c`** -> AI Confidence: **99.31%**
2458. **`arch/powerpc/kernel/dbell.c`** -> AI Confidence: **99.31%**
2459. **`arch/powerpc/kernel/dexcr.c`** -> AI Confidence: **99.31%**
2460. **`arch/powerpc/kernel/eeh.c`** -> AI Confidence: **99.31%**
2461. **`arch/powerpc/kernel/eeh_event.c`** -> AI Confidence: **99.31%**
2462. **`arch/powerpc/kernel/epapr_paravirt.c`** -> AI Confidence: **99.31%**
2463. **`arch/powerpc/kernel/fadump.c`** -> AI Confidence: **99.31%**
2464. **`arch/powerpc/kernel/hw_breakpoint.c`** -> AI Confidence: **99.31%**
2465. **`arch/powerpc/kernel/interrupt.c`** -> AI Confidence: **99.31%**
2466. **`arch/powerpc/kernel/io.c`** -> AI Confidence: **99.31%**
2467. **`arch/powerpc/kernel/isa-bridge.c`** -> AI Confidence: **99.31%**
2468. **`arch/powerpc/kernel/kprobes.c`** -> AI Confidence: **99.31%**
2469. **`arch/powerpc/kernel/kvm.c`** -> AI Confidence: **99.31%**
2470. **`arch/powerpc/kernel/legacy_serial.c`** -> AI Confidence: **99.31%**
2471. **`arch/powerpc/kernel/module_64.c`** -> AI Confidence: **99.31%**
2472. **`arch/powerpc/kernel/nvram_64.c`** -> AI Confidence: **99.31%**
2473. **`arch/powerpc/kernel/pci-common.c`** -> AI Confidence: **99.31%**
2474. **`arch/powerpc/kernel/pci_32.c`** -> AI Confidence: **99.31%**
2475. **`arch/powerpc/kernel/pmc.c`** -> AI Confidence: **99.31%**
2476. **`arch/powerpc/kernel/process.c`** -> AI Confidence: **99.31%**
2477. **`arch/powerpc/kernel/prom.c`** -> AI Confidence: **99.31%**
2478. **`arch/powerpc/kernel/prom_init.c`** -> AI Confidence: **99.31%**
2479. **`arch/powerpc/kernel/ptrace/ptrace.c`** -> AI Confidence: **99.31%**
2480. **`arch/powerpc/kernel/rtas-proc.c`** -> AI Confidence: **99.31%**
2481. **`arch/powerpc/kernel/rtas-rtc.c`** -> AI Confidence: **99.31%**
2482. **`arch/powerpc/kernel/rtas.c`** -> AI Confidence: **99.31%**
2483. **`arch/powerpc/kernel/rtas_flash.c`** -> AI Confidence: **99.31%**
2484. **`arch/powerpc/kernel/security.c`** -> AI Confidence: **99.31%**
2485. **`arch/powerpc/kernel/setup-common.c`** -> AI Confidence: **99.31%**
2486. **`arch/powerpc/kernel/setup_64.c`** -> AI Confidence: **99.31%**
2487. **`arch/powerpc/kernel/signal.c`** -> AI Confidence: **99.31%**
2488. **`arch/powerpc/kernel/signal_32.c`** -> AI Confidence: **99.31%**
2489. **`arch/powerpc/kernel/signal_64.c`** -> AI Confidence: **99.31%**
2490. **`arch/powerpc/kernel/stacktrace.c`** -> AI Confidence: **99.31%**
2491. **`arch/powerpc/kernel/syscall.c`** -> AI Confidence: **99.31%**
2492. **`arch/powerpc/kernel/tau_6xx.c`** -> AI Confidence: **99.31%**
2493. **`arch/powerpc/kernel/trace/ftrace.c`** -> AI Confidence: **99.31%**
2494. **`arch/powerpc/kernel/traps.c`** -> AI Confidence: **99.31%**
2495. **`arch/powerpc/kernel/udbg.c`** -> AI Confidence: **99.31%**
2496. **`arch/powerpc/kexec/core_64.c`** -> AI Confidence: **99.31%**
2497. **`arch/powerpc/kexec/crash.c`** -> AI Confidence: **99.31%**
2498. **`arch/powerpc/kexec/elf_64.c`** -> AI Confidence: **99.31%**
2499. **`arch/powerpc/kexec/file_load_64.c`** -> AI Confidence: **99.31%**
2500. **`arch/powerpc/kvm/book3s_32_mmu.c`** -> AI Confidence: **99.31%**
2501. **`arch/powerpc/kvm/book3s_32_mmu_host.c`** -> AI Confidence: **99.31%**
2502. **`arch/powerpc/kvm/book3s_64_mmu.c`** -> AI Confidence: **99.31%**
2503. **`arch/powerpc/kvm/book3s_64_mmu_host.c`** -> AI Confidence: **99.31%**
2504. **`arch/powerpc/kvm/book3s_64_mmu_hv.c`** -> AI Confidence: **99.31%**
2505. **`arch/powerpc/kvm/book3s_64_mmu_radix.c`** -> AI Confidence: **99.31%**
2506. **`arch/powerpc/kvm/book3s_hv.c`** -> AI Confidence: **99.31%**
2507. **`arch/powerpc/kvm/book3s_hv_ras.c`** -> AI Confidence: **99.31%**
2508. **`arch/powerpc/kvm/book3s_hv_rm_mmu.c`** -> AI Confidence: **99.31%**
2509. **`arch/powerpc/kvm/book3s_rtas.c`** -> AI Confidence: **99.31%**
2510. **`arch/powerpc/kvm/booke.c`** -> AI Confidence: **99.31%**
2511. **`arch/powerpc/kvm/e500_mmu.c`** -> AI Confidence: **99.31%**
2512. **`arch/powerpc/kvm/powerpc.c`** -> AI Confidence: **99.31%**
2513. **`arch/powerpc/math-emu/fdivs.c`** -> AI Confidence: **99.31%**
2514. **`arch/powerpc/math-emu/fmadds.c`** -> AI Confidence: **99.31%**
2515. **`arch/powerpc/math-emu/fmsubs.c`** -> AI Confidence: **99.31%**
2516. **`arch/powerpc/math-emu/fmuls.c`** -> AI Confidence: **99.31%**
2517. **`arch/powerpc/math-emu/fnmadds.c`** -> AI Confidence: **99.31%**
2518. **`arch/powerpc/math-emu/fnmsubs.c`** -> AI Confidence: **99.31%**
2519. **`arch/powerpc/math-emu/fsqrts.c`** -> AI Confidence: **99.31%**
2520. **`arch/powerpc/math-emu/fsubs.c`** -> AI Confidence: **99.31%**
2521. **`arch/powerpc/mm/book3s32/mmu.c`** -> AI Confidence: **99.31%**
2522. **`arch/powerpc/mm/book3s32/tlb.c`** -> AI Confidence: **99.31%**
2523. **`arch/powerpc/mm/book3s64/hash_native.c`** -> AI Confidence: **99.31%**
2524. **`arch/powerpc/mm/book3s64/hash_tlb.c`** -> AI Confidence: **99.31%**
2525. **`arch/powerpc/mm/book3s64/hash_utils.c`** -> AI Confidence: **99.31%**
2526. **`arch/powerpc/mm/book3s64/radix_pgtable.c`** -> AI Confidence: **99.31%**
2527. **`arch/powerpc/mm/book3s64/radix_tlb.c`** -> AI Confidence: **99.31%**
2528. **`arch/powerpc/mm/book3s64/slb.c`** -> AI Confidence: **99.31%**
2529. **`arch/powerpc/mm/book3s64/slice.c`** -> AI Confidence: **99.31%**
2530. **`arch/powerpc/mm/book3s64/subpage_prot.c`** -> AI Confidence: **99.31%**
2531. **`arch/powerpc/mm/fault.c`** -> AI Confidence: **99.31%**
2532. **`arch/powerpc/mm/init_32.c`** -> AI Confidence: **99.31%**
2533. **`arch/powerpc/mm/init_64.c`** -> AI Confidence: **99.31%**
2534. **`arch/powerpc/mm/nohash/44x.c`** -> AI Confidence: **99.31%**
2535. **`arch/powerpc/mm/nohash/book3e_pgtable.c`** -> AI Confidence: **99.31%**
2536. **`arch/powerpc/mm/nohash/e500.c`** -> AI Confidence: **99.31%**
2537. **`arch/powerpc/mm/nohash/mmu_context.c`** -> AI Confidence: **99.31%**
2538. **`arch/powerpc/mm/pgtable.c`** -> AI Confidence: **99.31%**
2539. **`arch/powerpc/net/bpf_jit_comp.c`** -> AI Confidence: **99.31%**
2540. **`arch/powerpc/net/bpf_jit_comp32.c`** -> AI Confidence: **99.31%**
2541. **`arch/powerpc/perf/callchain.c`** -> AI Confidence: **99.31%**
2542. **`arch/powerpc/perf/callchain_64.c`** -> AI Confidence: **99.31%**
2543. **`arch/powerpc/perf/core-book3s.c`** -> AI Confidence: **99.31%**
2544. **`arch/powerpc/perf/core-fsl-emb.c`** -> AI Confidence: **99.31%**
2545. **`arch/powerpc/perf/hv-gpci.c`** -> AI Confidence: **99.31%**
2546. **`arch/powerpc/perf/imc-pmu.c`** -> AI Confidence: **99.31%**
2547. **`arch/powerpc/perf/kvm-hv-pmu.c`** -> AI Confidence: **99.31%**
2548. **`arch/powerpc/perf/perf_regs.c`** -> AI Confidence: **99.31%**
2549. **`arch/powerpc/perf/power7-pmu.c`** -> AI Confidence: **99.31%**
2550. **`arch/powerpc/platforms/44x/cpm.c`** -> AI Confidence: **99.31%**
2551. **`arch/powerpc/platforms/44x/pci.c`** -> AI Confidence: **99.31%**
2552. **`arch/powerpc/platforms/44x/soc.c`** -> AI Confidence: **99.31%**
2553. **`arch/powerpc/platforms/83xx/km83xx.c`** -> AI Confidence: **99.31%**
2554. **`arch/powerpc/platforms/83xx/mpc832x_rdb.c`** -> AI Confidence: **99.31%**
2555. **`arch/powerpc/platforms/85xx/mpc85xx_mds.c`** -> AI Confidence: **99.31%**
2556. **`arch/powerpc/platforms/85xx/mpc85xx_rdb.c`** -> AI Confidence: **99.31%**
2557. **`arch/powerpc/platforms/85xx/p1022_ds.c`** -> AI Confidence: **99.31%**
2558. **`arch/powerpc/platforms/85xx/t1042rdb_diu.c`** -> AI Confidence: **99.31%**
2559. **`arch/powerpc/platforms/85xx/twr_p102x.c`** -> AI Confidence: **99.31%**
2560. **`arch/powerpc/platforms/cell/spufs/context.c`** -> AI Confidence: **99.31%**
2561. **`arch/powerpc/platforms/cell/spufs/sched.c`** -> AI Confidence: **99.31%**
2562. **`arch/powerpc/platforms/cell/spufs/syscalls.c`** -> AI Confidence: **99.31%**
2563. **`arch/powerpc/platforms/chrp/pci.c`** -> AI Confidence: **99.31%**
2564. **`arch/powerpc/platforms/chrp/setup.c`** -> AI Confidence: **99.31%**
2565. **`arch/powerpc/platforms/microwatt/smp.c`** -> AI Confidence: **99.31%**
2566. **`arch/powerpc/platforms/pasemi/idle.c`** -> AI Confidence: **99.31%**
2567. **`arch/powerpc/platforms/pasemi/pci.c`** -> AI Confidence: **99.31%**
2568. **`arch/powerpc/platforms/pasemi/setup.c`** -> AI Confidence: **99.31%**
2569. **`arch/powerpc/platforms/powermac/bootx_init.c`** -> AI Confidence: **99.31%**
2570. **`arch/powerpc/platforms/powermac/feature.c`** -> AI Confidence: **99.31%**
2571. **`arch/powerpc/platforms/powermac/nvram.c`** -> AI Confidence: **99.31%**
2572. **`arch/powerpc/platforms/powermac/pci.c`** -> AI Confidence: **99.31%**
2573. **`arch/powerpc/platforms/powermac/pfunc_base.c`** -> AI Confidence: **99.31%**
2574. **`arch/powerpc/platforms/powermac/pic.c`** -> AI Confidence: **99.31%**
2575. **`arch/powerpc/platforms/powermac/setup.c`** -> AI Confidence: **99.31%**
2576. **`arch/powerpc/platforms/powermac/smp.c`** -> AI Confidence: **99.31%**
2577. **`arch/powerpc/platforms/powermac/time.c`** -> AI Confidence: **99.31%**
2578. **`arch/powerpc/platforms/powermac/udbg_adb.c`** -> AI Confidence: **99.31%**
2579. **`arch/powerpc/platforms/powernv/eeh-powernv.c`** -> AI Confidence: **99.31%**
2580. **`arch/powerpc/platforms/powernv/idle.c`** -> AI Confidence: **99.31%**
2581. **`arch/powerpc/platforms/powernv/opal-async.c`** -> AI Confidence: **99.31%**
2582. **`arch/powerpc/platforms/powernv/opal-core.c`** -> AI Confidence: **99.31%**
2583. **`arch/powerpc/platforms/powernv/opal-imc.c`** -> AI Confidence: **99.31%**
2584. **`arch/powerpc/platforms/powernv/opal-lpc.c`** -> AI Confidence: **99.31%**
2585. **`arch/powerpc/platforms/powernv/opal-nvram.c`** -> AI Confidence: **99.31%**
2586. **`arch/powerpc/platforms/powernv/opal-rtc.c`** -> AI Confidence: **99.31%**
2587. **`arch/powerpc/platforms/powernv/opal.c`** -> AI Confidence: **99.31%**
2588. **`arch/powerpc/platforms/powernv/setup.c`** -> AI Confidence: **99.31%**
2589. **`arch/powerpc/platforms/powernv/smp.c`** -> AI Confidence: **99.31%**
2590. **`arch/powerpc/platforms/powernv/subcore.c`** -> AI Confidence: **99.31%**
2591. **`arch/powerpc/platforms/powernv/vas.h`** -> AI Confidence: **99.31%**
2592. **`arch/powerpc/platforms/ps3/device-init.c`** -> AI Confidence: **99.31%**
2593. **`arch/powerpc/platforms/ps3/htab.c`** -> AI Confidence: **99.31%**
2594. **`arch/powerpc/platforms/ps3/mm.c`** -> AI Confidence: **99.31%**
2595. **`arch/powerpc/platforms/pseries/cmm.c`** -> AI Confidence: **99.31%**
2596. **`arch/powerpc/platforms/pseries/dlpar.c`** -> AI Confidence: **99.31%**
2597. **`arch/powerpc/platforms/pseries/eeh_pseries.c`** -> AI Confidence: **99.31%**
2598. **`arch/powerpc/platforms/pseries/hotplug-cpu.c`** -> AI Confidence: **99.31%**
2599. **`arch/powerpc/platforms/pseries/hotplug-memory.c`** -> AI Confidence: **99.31%**
2600. **`arch/powerpc/platforms/pseries/hvcserver.c`** -> AI Confidence: **99.31%**
2601. **`arch/powerpc/platforms/pseries/iommu.c`** -> AI Confidence: **99.31%**
2602. **`arch/powerpc/platforms/pseries/lpar.c`** -> AI Confidence: **99.31%**
2603. **`arch/powerpc/platforms/pseries/lparcfg.c`** -> AI Confidence: **99.31%**
2604. **`arch/powerpc/platforms/pseries/mobility.c`** -> AI Confidence: **99.31%**
2605. **`arch/powerpc/platforms/pseries/nvram.c`** -> AI Confidence: **99.31%**
2606. **`arch/powerpc/platforms/pseries/papr-hvpipe.c`** -> AI Confidence: **99.31%**
2607. **`arch/powerpc/platforms/pseries/papr-indices.c`** -> AI Confidence: **99.31%**
2608. **`arch/powerpc/platforms/pseries/papr-platform-dump.c`** -> AI Confidence: **99.31%**
2609. **`arch/powerpc/platforms/pseries/papr-sysparm.c`** -> AI Confidence: **99.31%**
2610. **`arch/powerpc/platforms/pseries/papr_scm.c`** -> AI Confidence: **99.31%**
2611. **`arch/powerpc/platforms/pseries/pci_dlpar.c`** -> AI Confidence: **99.31%**
2612. **`arch/powerpc/platforms/pseries/plpks.c`** -> AI Confidence: **99.31%**
2613. **`arch/powerpc/platforms/pseries/pmem.c`** -> AI Confidence: **99.31%**
2614. **`arch/powerpc/platforms/pseries/pseries_energy.c`** -> AI Confidence: **99.31%**
2615. **`arch/powerpc/platforms/pseries/ras.c`** -> AI Confidence: **99.31%**
2616. **`arch/powerpc/platforms/pseries/reconfig.c`** -> AI Confidence: **99.31%**
2617. **`arch/powerpc/platforms/pseries/rtas-fadump.c`** -> AI Confidence: **99.31%**
2618. **`arch/powerpc/platforms/pseries/setup.c`** -> AI Confidence: **99.31%**
2619. **`arch/powerpc/platforms/pseries/smp.c`** -> AI Confidence: **99.31%**
2620. **`arch/powerpc/platforms/pseries/vas.c`** -> AI Confidence: **99.31%**
2621. **`arch/powerpc/platforms/pseries/vio.c`** -> AI Confidence: **99.31%**
2622. **`arch/powerpc/sysdev/cpm2_pic.c`** -> AI Confidence: **99.31%**
2623. **`arch/powerpc/sysdev/fsl_lbc.c`** -> AI Confidence: **99.31%**
2624. **`arch/powerpc/sysdev/fsl_pci.c`** -> AI Confidence: **99.31%**
2625. **`arch/powerpc/sysdev/fsl_rcpm.c`** -> AI Confidence: **99.31%**
2626. **`arch/powerpc/sysdev/fsl_rio.c`** -> AI Confidence: **99.31%**
2627. **`arch/powerpc/sysdev/fsl_soc.c`** -> AI Confidence: **99.31%**
2628. **`arch/powerpc/sysdev/indirect_pci.c`** -> AI Confidence: **99.31%**
2629. **`arch/powerpc/sysdev/mmio_nvram.c`** -> AI Confidence: **99.31%**
2630. **`arch/powerpc/sysdev/mpic.c`** -> AI Confidence: **99.31%**
2631. **`arch/powerpc/sysdev/mpic_msi.c`** -> AI Confidence: **99.31%**
2632. **`arch/powerpc/sysdev/of_rtc.c`** -> AI Confidence: **99.31%**
2633. **`arch/powerpc/sysdev/tsi108_dev.c`** -> AI Confidence: **99.31%**
2634. **`arch/powerpc/sysdev/xive/native.c`** -> AI Confidence: **99.31%**
2635. **`arch/powerpc/sysdev/xive/spapr.c`** -> AI Confidence: **99.31%**
2636. **`arch/powerpc/xmon/xmon.c`** -> AI Confidence: **99.31%**
2637. **`arch/riscv/include/asm/bitops.h`** -> AI Confidence: **99.31%**
2638. **`arch/riscv/include/asm/elf.h`** -> AI Confidence: **99.31%**
2639. **`arch/riscv/include/asm/runtime-const.h`** -> AI Confidence: **99.31%**
2640. **`arch/riscv/kernel/acpi.c`** -> AI Confidence: **99.31%**
2641. **`arch/riscv/kernel/cpu.c`** -> AI Confidence: **99.31%**
2642. **`arch/riscv/kernel/hibernate.c`** -> AI Confidence: **99.31%**
2643. **`arch/riscv/kernel/machine_kexec.c`** -> AI Confidence: **99.31%**
2644. **`arch/riscv/kernel/machine_kexec_file.c`** -> AI Confidence: **99.31%**
2645. **`arch/riscv/kernel/sbi.c`** -> AI Confidence: **99.31%**
2646. **`arch/riscv/kernel/setup.c`** -> AI Confidence: **99.31%**
2647. **`arch/riscv/kernel/sys_hwprobe.c`** -> AI Confidence: **99.31%**
2648. **`arch/riscv/kernel/traps_misaligned.c`** -> AI Confidence: **99.31%**
2649. **`arch/riscv/kernel/unaligned_access_speed.c`** -> AI Confidence: **99.31%**
2650. **`arch/riscv/kernel/vendor_extensions.c`** -> AI Confidence: **99.31%**
2651. **`arch/riscv/kvm/aia.c`** -> AI Confidence: **99.31%**
2652. **`arch/riscv/kvm/aia_aplic.c`** -> AI Confidence: **99.31%**
2653. **`arch/riscv/kvm/main.c`** -> AI Confidence: **99.31%**
2654. **`arch/riscv/kvm/tlb.c`** -> AI Confidence: **99.31%**
2655. **`arch/riscv/kvm/vcpu_onereg.c`** -> AI Confidence: **99.31%**
2656. **`arch/riscv/kvm/vcpu_pmu.c`** -> AI Confidence: **99.31%**
2657. **`arch/riscv/kvm/vcpu_sbi_replace.c`** -> AI Confidence: **99.31%**
2658. **`arch/riscv/kvm/vcpu_sbi_sta.c`** -> AI Confidence: **99.31%**
2659. **`arch/riscv/mm/fault.c`** -> AI Confidence: **99.31%**
2660. **`arch/riscv/mm/init.c`** -> AI Confidence: **99.31%**
2661. **`arch/riscv/mm/kasan_init.c`** -> AI Confidence: **99.31%**
2662. **`arch/riscv/net/bpf_jit_comp64.c`** -> AI Confidence: **99.31%**
2663. **`arch/s390/boot/kaslr.c`** -> AI Confidence: **99.31%**
2664. **`arch/s390/boot/printk.c`** -> AI Confidence: **99.31%**
2665. **`arch/s390/boot/startup.c`** -> AI Confidence: **99.31%**
2666. **`arch/s390/crypto/aes_s390.c`** -> AI Confidence: **99.31%**
2667. **`arch/s390/crypto/paes_s390.c`** -> AI Confidence: **99.31%**
2668. **`arch/s390/crypto/phmac_s390.c`** -> AI Confidence: **99.31%**
2669. **`arch/s390/crypto/prng.c`** -> AI Confidence: **99.31%**
2670. **`arch/s390/hypfs/hypfs_vm_fs.c`** -> AI Confidence: **99.31%**
2671. **`arch/s390/include/asm/mmu_context.h`** -> AI Confidence: **99.31%**
2672. **`arch/s390/include/asm/uaccess.h`** -> AI Confidence: **99.31%**
2673. **`arch/s390/kernel/alternative.c`** -> AI Confidence: **99.31%**
2674. **`arch/s390/kernel/cpcmd.c`** -> AI Confidence: **99.31%**
2675. **`arch/s390/kernel/debug.c`** -> AI Confidence: **99.31%**
2676. **`arch/s390/kernel/diag/diag_misc.c`** -> AI Confidence: **99.31%**
2677. **`arch/s390/kernel/machine_kexec_file.c`** -> AI Confidence: **99.31%**
2678. **`arch/s390/kernel/os_info.c`** -> AI Confidence: **99.31%**
2679. **`arch/s390/kernel/processor.c`** -> AI Confidence: **99.31%**
2680. **`arch/s390/kernel/setup.c`** -> AI Confidence: **99.31%**
2681. **`arch/s390/kernel/signal.c`** -> AI Confidence: **99.31%**
2682. **`arch/s390/kernel/syscall.c`** -> AI Confidence: **99.31%**
2683. **`arch/s390/kernel/traps.c`** -> AI Confidence: **99.31%**
2684. **`arch/s390/kernel/uprobes.c`** -> AI Confidence: **99.31%**
2685. **`arch/s390/kvm/diag.c`** -> AI Confidence: **99.31%**
2686. **`arch/s390/kvm/gaccess.c`** -> AI Confidence: **99.31%**
2687. **`arch/s390/kvm/intercept.c`** -> AI Confidence: **99.31%**
2688. **`arch/s390/kvm/interrupt.c`** -> AI Confidence: **99.31%**
2689. **`arch/s390/kvm/kvm-s390.c`** -> AI Confidence: **99.31%**
2690. **`arch/s390/kvm/pci.c`** -> AI Confidence: **99.31%**
2691. **`arch/s390/kvm/priv.c`** -> AI Confidence: **99.31%**
2692. **`arch/s390/kvm/pv.c`** -> AI Confidence: **99.31%**
2693. **`arch/s390/kvm/sigp.c`** -> AI Confidence: **99.31%**
2694. **`arch/s390/kvm/vsie.c`** -> AI Confidence: **99.31%**
2695. **`arch/s390/mm/cmm.c`** -> AI Confidence: **99.31%**
2696. **`arch/s390/mm/extmem.c`** -> AI Confidence: **99.31%**
2697. **`arch/s390/mm/fault.c`** -> AI Confidence: **99.31%**
2698. **`arch/s390/mm/gmap_helpers.c`** -> AI Confidence: **99.31%**
2699. **`arch/s390/mm/hugetlbpage.c`** -> AI Confidence: **99.31%**
2700. **`arch/s390/mm/mmap.c`** -> AI Confidence: **99.31%**
2701. **`arch/s390/mm/pfault.c`** -> AI Confidence: **99.31%**
2702. **`arch/s390/mm/pgalloc.c`** -> AI Confidence: **99.31%**
2703. **`arch/s390/mm/vmem.c`** -> AI Confidence: **99.31%**
2704. **`arch/s390/pci/pci_event.c`** -> AI Confidence: **99.31%**
2705. **`arch/s390/pci/pci_mmio.c`** -> AI Confidence: **99.31%**
2706. **`arch/s390/tools/relocs.c`** -> AI Confidence: **99.31%**
2707. **`arch/sh/boards/mach-hp6xx/hp6xx_apm.c`** -> AI Confidence: **99.31%**
2708. **`arch/sh/boards/mach-landisk/gio.c`** -> AI Confidence: **99.31%**
2709. **`arch/sh/boards/mach-se/7724/irq.c`** -> AI Confidence: **99.31%**
2710. **`arch/sh/boards/mach-sh03/rtc.c`** -> AI Confidence: **99.31%**
2711. **`arch/sh/drivers/dma/dma-sh.c`** -> AI Confidence: **99.31%**
2712. **`arch/sh/drivers/heartbeat.c`** -> AI Confidence: **99.31%**
2713. **`arch/sh/drivers/pci/fixups-se7751.c`** -> AI Confidence: **99.31%**
2714. **`arch/sh/drivers/pci/ops-dreamcast.c`** -> AI Confidence: **99.31%**
2715. **`arch/sh/drivers/pci/pci-sh7751.c`** -> AI Confidence: **99.31%**
2716. **`arch/sh/drivers/pci/pci-sh7780.c`** -> AI Confidence: **99.31%**
2717. **`arch/sh/drivers/pci/pci.c`** -> AI Confidence: **99.31%**
2718. **`arch/sh/include/asm/mmu_context.h`** -> AI Confidence: **99.31%**
2719. **`arch/sh/kernel/cpu/init.c`** -> AI Confidence: **99.31%**
2720. **`arch/sh/kernel/cpu/sh3/setup-sh770x.c`** -> AI Confidence: **99.31%**
2721. **`arch/sh/kernel/cpu/sh4/setup-sh7750.c`** -> AI Confidence: **99.31%**
2722. **`arch/sh/kernel/dwarf.c`** -> AI Confidence: **99.31%**
2723. **`arch/sh/kernel/hw_breakpoint.c`** -> AI Confidence: **99.31%**
2724. **`arch/sh/kernel/io_trapped.c`** -> AI Confidence: **99.31%**
2725. **`arch/sh/kernel/kgdb.c`** -> AI Confidence: **99.31%**
2726. **`arch/sh/kernel/kprobes.c`** -> AI Confidence: **99.31%**
2727. **`arch/sh/kernel/machine_kexec.c`** -> AI Confidence: **99.31%**
2728. **`arch/sh/kernel/machvec.c`** -> AI Confidence: **99.31%**
2729. **`arch/sh/kernel/module.c`** -> AI Confidence: **99.31%**
2730. **`arch/sh/kernel/setup.c`** -> AI Confidence: **99.31%**
2731. **`arch/sh/kernel/sys_sh.c`** -> AI Confidence: **99.31%**
2732. **`arch/sh/kernel/traps.c`** -> AI Confidence: **99.31%**
2733. **`arch/sh/mm/cache-debugfs.c`** -> AI Confidence: **99.31%**
2734. **`arch/sh/mm/cache-sh2a.c`** -> AI Confidence: **99.31%**
2735. **`arch/sh/mm/hugetlbpage.c`** -> AI Confidence: **99.31%**
2736. **`arch/sh/mm/mmap.c`** -> AI Confidence: **99.31%**
2737. **`arch/sh/mm/pmb.c`** -> AI Confidence: **99.31%**
2738. **`arch/sh/mm/tlb-debugfs.c`** -> AI Confidence: **99.31%**
2739. **`arch/sh/mm/tlbex_32.c`** -> AI Confidence: **99.31%**
2740. **`arch/sparc/include/asm/floppy_32.h`** -> AI Confidence: **99.31%**
2741. **`arch/sparc/include/asm/floppy_64.h`** -> AI Confidence: **99.31%**
2742. **`arch/sparc/kernel/auxio_32.c`** -> AI Confidence: **99.31%**
2743. **`arch/sparc/kernel/auxio_64.c`** -> AI Confidence: **99.31%**
2744. **`arch/sparc/kernel/btext.c`** -> AI Confidence: **99.31%**
2745. **`arch/sparc/kernel/central.c`** -> AI Confidence: **99.31%**
2746. **`arch/sparc/kernel/chmc.c`** -> AI Confidence: **99.31%**
2747. **`arch/sparc/kernel/compat_audit.c`** -> AI Confidence: **99.31%**
2748. **`arch/sparc/kernel/cpu.c`** -> AI Confidence: **99.31%**
2749. **`arch/sparc/kernel/cpumap.c`** -> AI Confidence: **99.31%**
2750. **`arch/sparc/kernel/ebus.c`** -> AI Confidence: **99.31%**
2751. **`arch/sparc/kernel/iommu-common.c`** -> AI Confidence: **99.31%**
2752. **`arch/sparc/kernel/iommu.c`** -> AI Confidence: **99.31%**
2753. **`arch/sparc/kernel/jump_label.c`** -> AI Confidence: **99.31%**
2754. **`arch/sparc/kernel/ldc.c`** -> AI Confidence: **99.31%**
2755. **`arch/sparc/kernel/led.c`** -> AI Confidence: **99.31%**
2756. **`arch/sparc/kernel/leon_kernel.c`** -> AI Confidence: **99.31%**
2757. **`arch/sparc/kernel/leon_pci_grpci2.c`** -> AI Confidence: **99.31%**
2758. **`arch/sparc/kernel/nmi.c`** -> AI Confidence: **99.31%**
2759. **`arch/sparc/kernel/of_device_32.c`** -> AI Confidence: **99.31%**
2760. **`arch/sparc/kernel/of_device_64.c`** -> AI Confidence: **99.31%**
2761. **`arch/sparc/kernel/pci_common.c`** -> AI Confidence: **99.31%**
2762. **`arch/sparc/kernel/pci_msi.c`** -> AI Confidence: **99.31%**
2763. **`arch/sparc/kernel/pci_psycho.c`** -> AI Confidence: **99.31%**
2764. **`arch/sparc/kernel/pci_sabre.c`** -> AI Confidence: **99.31%**
2765. **`arch/sparc/kernel/pci_schizo.c`** -> AI Confidence: **99.31%**
2766. **`arch/sparc/kernel/pci_sun4v.c`** -> AI Confidence: **99.31%**
2767. **`arch/sparc/kernel/pcic.c`** -> AI Confidence: **99.31%**
2768. **`arch/sparc/kernel/prom_32.c`** -> AI Confidence: **99.31%**
2769. **`arch/sparc/kernel/ptrace_64.c`** -> AI Confidence: **99.31%**
2770. **`arch/sparc/kernel/sbus.c`** -> AI Confidence: **99.31%**
2771. **`arch/sparc/kernel/signal32.c`** -> AI Confidence: **99.31%**
2772. **`arch/sparc/kernel/signal_32.c`** -> AI Confidence: **99.31%**
2773. **`arch/sparc/kernel/sigutil_32.c`** -> AI Confidence: **99.31%**
2774. **`arch/sparc/kernel/smp_32.c`** -> AI Confidence: **99.31%**
2775. **`arch/sparc/kernel/smp_64.c`** -> AI Confidence: **99.31%**
2776. **`arch/sparc/kernel/starfire.c`** -> AI Confidence: **99.31%**
2777. **`arch/sparc/kernel/sun4m_smp.c`** -> AI Confidence: **99.31%**
2778. **`arch/sparc/kernel/sys_sparc_32.c`** -> AI Confidence: **99.31%**
2779. **`arch/sparc/kernel/traps_32.c`** -> AI Confidence: **99.31%**
2780. **`arch/sparc/kernel/traps_64.c`** -> AI Confidence: **99.31%**
2781. **`arch/sparc/kernel/unaligned_32.c`** -> AI Confidence: **99.31%**
2782. **`arch/sparc/kernel/viohs.c`** -> AI Confidence: **99.31%**
2783. **`arch/sparc/mm/fault_32.c`** -> AI Confidence: **99.31%**
2784. **`arch/sparc/mm/hugetlbpage.c`** -> AI Confidence: **99.31%**
2785. **`arch/sparc/mm/init_32.c`** -> AI Confidence: **99.31%**
2786. **`arch/sparc/mm/init_64.c`** -> AI Confidence: **99.31%**
2787. **`arch/sparc/mm/tlb.c`** -> AI Confidence: **99.31%**
2788. **`arch/sparc/prom/tree_32.c`** -> AI Confidence: **99.31%**
2789. **`arch/sparc/vdso/vdso2c.c`** -> AI Confidence: **99.31%**
2790. **`arch/um/drivers/chan_user.c`** -> AI Confidence: **99.31%**
2791. **`arch/um/drivers/cow_user.c`** -> AI Confidence: **99.31%**
2792. **`arch/um/drivers/random.c`** -> AI Confidence: **99.31%**
2793. **`arch/um/drivers/rtc_user.c`** -> AI Confidence: **99.31%**
2794. **`arch/um/drivers/ubd_kern.c`** -> AI Confidence: **99.31%**
2795. **`arch/um/drivers/ubd_user.c`** -> AI Confidence: **99.31%**
2796. **`arch/um/drivers/vector_user.c`** -> AI Confidence: **99.31%**
2797. **`arch/um/drivers/xterm.c`** -> AI Confidence: **99.31%**
2798. **`arch/um/kernel/physmem.c`** -> AI Confidence: **99.31%**
2799. **`arch/um/kernel/skas/stub_exe.c`** -> AI Confidence: **99.31%**
2800. **`arch/um/kernel/skas/uaccess.c`** -> AI Confidence: **99.31%**
2801. **`arch/um/kernel/sysrq.c`** -> AI Confidence: **99.31%**
2802. **`arch/um/kernel/tlb.c`** -> AI Confidence: **99.31%**
2803. **`arch/um/kernel/trap.c`** -> AI Confidence: **99.31%**
2804. **`arch/um/os-Linux/helper.c`** -> AI Confidence: **99.31%**
2805. **`arch/um/os-Linux/main.c`** -> AI Confidence: **99.31%**
2806. **`arch/um/os-Linux/mem.c`** -> AI Confidence: **99.31%**
2807. **`arch/um/os-Linux/skas/process.c`** -> AI Confidence: **99.31%**
2808. **`arch/um/os-Linux/start_up.c`** -> AI Confidence: **99.31%**
2809. **`arch/um/os-Linux/umid.c`** -> AI Confidence: **99.31%**
2810. **`arch/x86/boot/compressed/misc.c`** -> AI Confidence: **99.31%**
2811. **`arch/x86/boot/compressed/pgtable_64.c`** -> AI Confidence: **99.31%**
2812. **`arch/x86/boot/compressed/sev-handle-vc.c`** -> AI Confidence: **99.31%**
2813. **`arch/x86/boot/startup/map_kernel.c`** -> AI Confidence: **99.31%**
2814. **`arch/x86/boot/string.c`** -> AI Confidence: **99.31%**
2815. **`arch/x86/coco/sev/vc-handle.c`** -> AI Confidence: **99.31%**
2816. **`arch/x86/entry/entry_fred.c`** -> AI Confidence: **99.31%**
2817. **`arch/x86/entry/vdso/vdso32-setup.c`** -> AI Confidence: **99.31%**
2818. **`arch/x86/entry/vsyscall/vsyscall_64.c`** -> AI Confidence: **99.31%**
2819. **`arch/x86/events/core.c`** -> AI Confidence: **99.31%**
2820. **`arch/x86/events/intel/core.c`** -> AI Confidence: **99.31%**
2821. **`arch/x86/events/intel/lbr.c`** -> AI Confidence: **99.31%**
2822. **`arch/x86/events/intel/p4.c`** -> AI Confidence: **99.31%**
2823. **`arch/x86/hyperv/mmu.c`** -> AI Confidence: **99.31%**
2824. **`arch/x86/ia32/audit.c`** -> AI Confidence: **99.31%**
2825. **`arch/x86/include/asm/elf.h`** -> AI Confidence: **99.31%**
2826. **`arch/x86/include/asm/thread_info.h`** -> AI Confidence: **99.31%**
2827. **`arch/x86/include/asm/uaccess.h`** -> AI Confidence: **99.31%**
2828. **`arch/x86/kernel/acpi/boot.c`** -> AI Confidence: **99.31%**
2829. **`arch/x86/kernel/acpi/cstate.c`** -> AI Confidence: **99.31%**
2830. **`arch/x86/kernel/acpi/sleep.c`** -> AI Confidence: **99.31%**
2831. **`arch/x86/kernel/amd_gart_64.c`** -> AI Confidence: **99.31%**
2832. **`arch/x86/kernel/amd_nb.c`** -> AI Confidence: **99.31%**
2833. **`arch/x86/kernel/aperture_64.c`** -> AI Confidence: **99.31%**
2834. **`arch/x86/kernel/apic/apic.c`** -> AI Confidence: **99.31%**
2835. **`arch/x86/kernel/apic/x2apic_uv_x.c`** -> AI Confidence: **99.31%**
2836. **`arch/x86/kernel/apm_32.c`** -> AI Confidence: **99.31%**
2837. **`arch/x86/kernel/audit_64.c`** -> AI Confidence: **99.31%**
2838. **`arch/x86/kernel/check.c`** -> AI Confidence: **99.31%**
2839. **`arch/x86/kernel/cpu/bugs.c`** -> AI Confidence: **99.31%**
2840. **`arch/x86/kernel/cpu/bus_lock.c`** -> AI Confidence: **99.31%**
2841. **`arch/x86/kernel/cpu/common.c`** -> AI Confidence: **99.31%**
2842. **`arch/x86/kernel/cpu/hygon.c`** -> AI Confidence: **99.31%**
2843. **`arch/x86/kernel/cpu/mce/apei.c`** -> AI Confidence: **99.31%**
2844. **`arch/x86/kernel/cpu/mce/core.c`** -> AI Confidence: **99.31%**
2845. **`arch/x86/kernel/cpu/mce/severity.c`** -> AI Confidence: **99.31%**
2846. **`arch/x86/kernel/cpu/microcode/core.c`** -> AI Confidence: **99.31%**
2847. **`arch/x86/kernel/cpu/mtrr/if.c`** -> AI Confidence: **99.31%**
2848. **`arch/x86/kernel/cpu/mtrr/legacy.c`** -> AI Confidence: **99.31%**
2849. **`arch/x86/kernel/cpu/perfctr-watchdog.c`** -> AI Confidence: **99.31%**
2850. **`arch/x86/kernel/cpu/proc.c`** -> AI Confidence: **99.31%**
2851. **`arch/x86/kernel/cpu/resctrl/pseudo_lock.c`** -> AI Confidence: **99.31%**
2852. **`arch/x86/kernel/cpu/sgx/ioctl.c`** -> AI Confidence: **99.31%**
2853. **`arch/x86/kernel/cpu/sgx/main.c`** -> AI Confidence: **99.31%**
2854. **`arch/x86/kernel/cpu/topology_common.c`** -> AI Confidence: **99.31%**
2855. **`arch/x86/kernel/e820.c`** -> AI Confidence: **99.31%**
2856. **`arch/x86/kernel/espfix_64.c`** -> AI Confidence: **99.31%**
2857. **`arch/x86/kernel/fpu/init.c`** -> AI Confidence: **99.31%**
2858. **`arch/x86/kernel/head32.c`** -> AI Confidence: **99.31%**
2859. **`arch/x86/kernel/head64.c`** -> AI Confidence: **99.31%**
2860. **`arch/x86/kernel/hw_breakpoint.c`** -> AI Confidence: **99.31%**
2861. **`arch/x86/kernel/ioport.c`** -> AI Confidence: **99.31%**
2862. **`arch/x86/kernel/irqinit.c`** -> AI Confidence: **99.31%**
2863. **`arch/x86/kernel/kprobes/core.c`** -> AI Confidence: **99.31%**
2864. **`arch/x86/kernel/kprobes/ftrace.c`** -> AI Confidence: **99.31%**
2865. **`arch/x86/kernel/kprobes/opt.c`** -> AI Confidence: **99.31%**
2866. **`arch/x86/kernel/ldt.c`** -> AI Confidence: **99.31%**
2867. **`arch/x86/kernel/machine_kexec_64.c`** -> AI Confidence: **99.31%**
2868. **`arch/x86/kernel/mmconf-fam10h_64.c`** -> AI Confidence: **99.31%**
2869. **`arch/x86/kernel/module.c`** -> AI Confidence: **99.31%**
2870. **`arch/x86/kernel/mpparse.c`** -> AI Confidence: **99.31%**
2871. **`arch/x86/kernel/msr.c`** -> AI Confidence: **99.31%**
2872. **`arch/x86/kernel/nmi.c`** -> AI Confidence: **99.31%**
2873. **`arch/x86/kernel/probe_roms.c`** -> AI Confidence: **99.31%**
2874. **`arch/x86/kernel/process.c`** -> AI Confidence: **99.31%**
2875. **`arch/x86/kernel/process_64.c`** -> AI Confidence: **99.31%**
2876. **`arch/x86/kernel/reboot.c`** -> AI Confidence: **99.31%**
2877. **`arch/x86/kernel/signal_32.c`** -> AI Confidence: **99.31%**
2878. **`arch/x86/kernel/smp.c`** -> AI Confidence: **99.31%**
2879. **`arch/x86/kernel/stacktrace.c`** -> AI Confidence: **99.31%**
2880. **`arch/x86/kernel/sys_x86_64.c`** -> AI Confidence: **99.31%**
2881. **`arch/x86/kernel/tsc.c`** -> AI Confidence: **99.31%**
2882. **`arch/x86/kernel/unwind_frame.c`** -> AI Confidence: **99.31%**
2883. **`arch/x86/kernel/vm86_32.c`** -> AI Confidence: **99.31%**
2884. **`arch/x86/kvm/cpuid.c`** -> AI Confidence: **99.31%**
2885. **`arch/x86/kvm/emulate.c`** -> AI Confidence: **99.31%**
2886. **`arch/x86/kvm/hyperv.c`** -> AI Confidence: **99.31%**
2887. **`arch/x86/kvm/ioapic.c`** -> AI Confidence: **99.31%**
2888. **`arch/x86/kvm/irq.c`** -> AI Confidence: **99.31%**
2889. **`arch/x86/kvm/svm/sev.c`** -> AI Confidence: **99.31%**
2890. **`arch/x86/kvm/svm/svm.c`** -> AI Confidence: **99.31%**
2891. **`arch/x86/kvm/svm/svm_onhyperv.c`** -> AI Confidence: **99.31%**
2892. **`arch/x86/kvm/vmx/nested.c`** -> AI Confidence: **99.31%**
2893. **`arch/x86/kvm/vmx/pmu_intel.c`** -> AI Confidence: **99.31%**
2894. **`arch/x86/kvm/vmx/sgx.c`** -> AI Confidence: **99.31%**
2895. **`arch/x86/kvm/vmx/vmx.c`** -> AI Confidence: **99.31%**
2896. **`arch/x86/kvm/x86.c`** -> AI Confidence: **99.31%**
2897. **`arch/x86/kvm/xen.c`** -> AI Confidence: **99.31%**
2898. **`arch/x86/mm/fault.c`** -> AI Confidence: **99.31%**
2899. **`arch/x86/mm/init.c`** -> AI Confidence: **99.31%**
2900. **`arch/x86/mm/init_32.c`** -> AI Confidence: **99.31%**
2901. **`arch/x86/mm/init_64.c`** -> AI Confidence: **99.31%**
2902. **`arch/x86/mm/kasan_init_64.c`** -> AI Confidence: **99.31%**
2903. **`arch/x86/mm/kaslr.c`** -> AI Confidence: **99.31%**
2904. **`arch/x86/mm/mem_encrypt.c`** -> AI Confidence: **99.31%**
2905. **`arch/x86/mm/mmio-mod.c`** -> AI Confidence: **99.31%**
2906. **`arch/x86/mm/numa.c`** -> AI Confidence: **99.31%**
2907. **`arch/x86/mm/pat/set_memory.c`** -> AI Confidence: **99.31%**
2908. **`arch/x86/mm/pgtable_32.c`** -> AI Confidence: **99.31%**
2909. **`arch/x86/net/bpf_jit_comp.c`** -> AI Confidence: **99.31%**
2910. **`arch/x86/pci/amd_bus.c`** -> AI Confidence: **99.31%**
2911. **`arch/x86/pci/broadcom_bus.c`** -> AI Confidence: **99.31%**
2912. **`arch/x86/pci/common.c`** -> AI Confidence: **99.31%**
2913. **`arch/x86/pci/i386.c`** -> AI Confidence: **99.31%**
2914. **`arch/x86/pci/mmconfig_64.c`** -> AI Confidence: **99.31%**
2915. **`arch/x86/pci/xen.c`** -> AI Confidence: **99.31%**
2916. **`arch/x86/platform/efi/memmap.c`** -> AI Confidence: **99.31%**
2917. **`arch/x86/platform/efi/quirks.c`** -> AI Confidence: **99.31%**
2918. **`arch/x86/platform/intel-quark/imr.c`** -> AI Confidence: **99.31%**
2919. **`arch/x86/platform/olpc/olpc.c`** -> AI Confidence: **99.31%**
2920. **`arch/x86/power/hibernate_32.c`** -> AI Confidence: **99.31%**
2921. **`arch/x86/tools/insn_decoder_test.c`** -> AI Confidence: **99.31%**
2922. **`arch/x86/um/os-Linux/registers.c`** -> AI Confidence: **99.31%**
2923. **`arch/x86/um/os-Linux/tls.c`** -> AI Confidence: **99.31%**
2924. **`arch/x86/um/ptrace_32.c`** -> AI Confidence: **99.31%**
2925. **`arch/x86/um/syscalls_64.c`** -> AI Confidence: **99.31%**
2926. **`arch/x86/um/tls_32.c`** -> AI Confidence: **99.31%**
2927. **`arch/x86/xen/efi.c`** -> AI Confidence: **99.31%**
2928. **`arch/x86/xen/enlighten.c`** -> AI Confidence: **99.31%**
2929. **`arch/x86/xen/enlighten_pvh.c`** -> AI Confidence: **99.31%**
2930. **`arch/x86/xen/p2m.c`** -> AI Confidence: **99.31%**
2931. **`arch/x86/xen/pmu.c`** -> AI Confidence: **99.31%**
2932. **`arch/x86/xen/setup.c`** -> AI Confidence: **99.31%**
2933. **`arch/x86/xen/smp.c`** -> AI Confidence: **99.31%**
2934. **`arch/x86/xen/spinlock.c`** -> AI Confidence: **99.31%**
2935. **`arch/xtensa/include/asm/bitops.h`** -> AI Confidence: **99.31%**
2936. **`arch/xtensa/include/asm/processor.h`** -> AI Confidence: **99.31%**
2937. **`arch/xtensa/kernel/irq.c`** -> AI Confidence: **99.31%**
2938. **`arch/xtensa/kernel/pci-dma.c`** -> AI Confidence: **99.31%**
2939. **`arch/xtensa/kernel/ptrace.c`** -> AI Confidence: **99.31%**
2940. **`arch/xtensa/kernel/setup.c`** -> AI Confidence: **99.31%**
2941. **`arch/xtensa/kernel/signal.c`** -> AI Confidence: **99.31%**
2942. **`arch/xtensa/kernel/syscall.c`** -> AI Confidence: **99.31%**
2943. **`arch/xtensa/mm/cache.c`** -> AI Confidence: **99.31%**
2944. **`arch/xtensa/mm/init.c`** -> AI Confidence: **99.31%**
2945. **`arch/xtensa/mm/mmu.c`** -> AI Confidence: **99.31%**
2946. **`arch/xtensa/platforms/iss/simdisk.c`** -> AI Confidence: **99.31%**
2947. **`block/badblocks.c`** -> AI Confidence: **99.31%**
2948. **`block/bfq-iosched.c`** -> AI Confidence: **99.31%**
2949. **`block/blk-crypto.c`** -> AI Confidence: **99.31%**
2950. **`block/blk-map.c`** -> AI Confidence: **99.31%**
2951. **`block/blk-settings.c`** -> AI Confidence: **99.31%**
2952. **`block/genhd.c`** -> AI Confidence: **99.31%**
2953. **`block/partitions/ibm.c`** -> AI Confidence: **99.31%**
2954. **`block/partitions/ldm.c`** -> AI Confidence: **99.31%**
2955. **`crypto/af_alg.c`** -> AI Confidence: **99.31%**
2956. **`crypto/algboss.c`** -> AI Confidence: **99.31%**
2957. **`crypto/api.c`** -> AI Confidence: **99.31%**
2958. **`crypto/asymmetric_keys/mscode_parser.c`** -> AI Confidence: **99.31%**
2959. **`crypto/asymmetric_keys/pkcs7_parser.c`** -> AI Confidence: **99.31%**
2960. **`crypto/asymmetric_keys/pkcs7_trust.c`** -> AI Confidence: **99.31%**
2961. **`crypto/asymmetric_keys/pkcs7_verify.c`** -> AI Confidence: **99.31%**
2962. **`crypto/asymmetric_keys/public_key.c`** -> AI Confidence: **99.31%**
2963. **`crypto/asymmetric_keys/verify_pefile.c`** -> AI Confidence: **99.31%**
2964. **`crypto/asymmetric_keys/x509_cert_parser.c`** -> AI Confidence: **99.31%**
2965. **`crypto/async_tx/async_pq.c`** -> AI Confidence: **99.31%**
2966. **`crypto/blowfish_common.c`** -> AI Confidence: **99.31%**
2967. **`crypto/camellia_generic.c`** -> AI Confidence: **99.31%**
2968. **`crypto/ecc.c`** -> AI Confidence: **99.31%**
2969. **`crypto/krb5/rfc3961_simplified.c`** -> AI Confidence: **99.31%**
2970. **`crypto/rsa.c`** -> AI Confidence: **99.31%**
2971. **`crypto/tcrypt.c`** -> AI Confidence: **99.31%**
2972. **`crypto/testmgr.c`** -> AI Confidence: **99.31%**
2973. **`crypto/zstd.c`** -> AI Confidence: **99.31%**
2974. **`drivers/accel/amdxdna/aie2_pm.c`** -> AI Confidence: **99.31%**
2975. **`drivers/accel/habanalabs/common/memory.c`** -> AI Confidence: **99.31%**
2976. **`drivers/accel/habanalabs/gaudi/gaudi.c`** -> AI Confidence: **99.31%**
2977. **`drivers/accel/habanalabs/gaudi2/gaudi2.c`** -> AI Confidence: **99.31%**
2978. **`drivers/accel/ivpu/ivpu_drv.c`** -> AI Confidence: **99.31%**
2979. **`drivers/accel/ivpu/ivpu_fw.c`** -> AI Confidence: **99.31%**
2980. **`drivers/accel/ivpu/ivpu_fw_log.c`** -> AI Confidence: **99.31%**
2981. **`drivers/accel/ivpu/ivpu_hw.c`** -> AI Confidence: **99.31%**
2982. **`drivers/accel/qaic/qaic_data.c`** -> AI Confidence: **99.31%**
2983. **`drivers/accessibility/speakup/kobjects.c`** -> AI Confidence: **99.31%**
2984. **`drivers/accessibility/speakup/speakup_dectlk.c`** -> AI Confidence: **99.31%**
2985. **`drivers/accessibility/speakup/speakup_dtlk.c`** -> AI Confidence: **99.31%**
2986. **`drivers/accessibility/speakup/speakup_keypc.c`** -> AI Confidence: **99.31%**
2987. **`drivers/acpi/acpi_processor.c`** -> AI Confidence: **99.31%**
2988. **`drivers/acpi/acpi_video.c`** -> AI Confidence: **99.31%**
2989. **`drivers/acpi/acpica/dbcmds.c`** -> AI Confidence: **99.31%**
2990. **`drivers/acpi/acpica/dbdisply.c`** -> AI Confidence: **99.31%**
2991. **`drivers/acpi/acpica/dsmethod.c`** -> AI Confidence: **99.31%**
2992. **`drivers/acpi/acpica/dsopcode.c`** -> AI Confidence: **99.31%**
2993. **`drivers/acpi/acpica/dspkginit.c`** -> AI Confidence: **99.31%**
2994. **`drivers/acpi/acpica/exconfig.c`** -> AI Confidence: **99.31%**
2995. **`drivers/acpi/acpica/nsparse.c`** -> AI Confidence: **99.31%**
2996. **`drivers/acpi/apei/bert.c`** -> AI Confidence: **99.31%**
2997. **`drivers/acpi/apei/einj-core.c`** -> AI Confidence: **99.31%**
2998. **`drivers/acpi/apei/erst.c`** -> AI Confidence: **99.31%**
2999. **`drivers/acpi/apei/ghes.c`** -> AI Confidence: **99.31%**
3000. **`drivers/acpi/cppc_acpi.c`** -> AI Confidence: **99.31%**
3001. **`drivers/acpi/device_pm.c`** -> AI Confidence: **99.31%**
3002. **`drivers/acpi/numa/hmat.c`** -> AI Confidence: **99.31%**
3003. **`drivers/acpi/numa/srat.c`** -> AI Confidence: **99.31%**
3004. **`drivers/acpi/osl.c`** -> AI Confidence: **99.31%**
3005. **`drivers/acpi/pci_irq.c`** -> AI Confidence: **99.31%**
3006. **`drivers/acpi/pci_link.c`** -> AI Confidence: **99.31%**
3007. **`drivers/acpi/pci_root.c`** -> AI Confidence: **99.31%**
3008. **`drivers/acpi/proc.c`** -> AI Confidence: **99.31%**
3009. **`drivers/acpi/processor_idle.c`** -> AI Confidence: **99.31%**
3010. **`drivers/acpi/processor_throttling.c`** -> AI Confidence: **99.31%**
3011. **`drivers/acpi/sbs.c`** -> AI Confidence: **99.31%**
3012. **`drivers/acpi/sysfs.c`** -> AI Confidence: **99.31%**
3013. **`drivers/acpi/utils.c`** -> AI Confidence: **99.31%**
3014. **`drivers/android/binder.c`** -> AI Confidence: **99.31%**
3015. **`drivers/ata/ahci.c`** -> AI Confidence: **99.31%**
3016. **`drivers/ata/ahci_ceva.c`** -> AI Confidence: **99.31%**
3017. **`drivers/ata/ahci_qoriq.c`** -> AI Confidence: **99.31%**
3018. **`drivers/ata/libahci_platform.c`** -> AI Confidence: **99.31%**
3019. **`drivers/ata/libata-acpi.c`** -> AI Confidence: **99.31%**
3020. **`drivers/ata/libata-core.c`** -> AI Confidence: **99.31%**
3021. **`drivers/ata/libata-scsi.c`** -> AI Confidence: **99.31%**
3022. **`drivers/ata/libata-sff.c`** -> AI Confidence: **99.31%**
3023. **`drivers/ata/pata_ali.c`** -> AI Confidence: **99.31%**
3024. **`drivers/ata/pata_atp867x.c`** -> AI Confidence: **99.31%**
3025. **`drivers/ata/pata_cs5530.c`** -> AI Confidence: **99.31%**
3026. **`drivers/ata/pata_falcon.c`** -> AI Confidence: **99.31%**
3027. **`drivers/ata/pata_it821x.c`** -> AI Confidence: **99.31%**
3028. **`drivers/ata/pata_ixp4xx_cf.c`** -> AI Confidence: **99.31%**
3029. **`drivers/ata/pata_jmicron.c`** -> AI Confidence: **99.31%**
3030. **`drivers/ata/pata_parport/comm.c`** -> AI Confidence: **99.31%**
3031. **`drivers/ata/pata_parport/fit3.c`** -> AI Confidence: **99.31%**
3032. **`drivers/ata/pata_parport/friq.c`** -> AI Confidence: **99.31%**
3033. **`drivers/ata/pata_parport/frpw.c`** -> AI Confidence: **99.31%**
3034. **`drivers/ata/pata_parport/kbic.c`** -> AI Confidence: **99.31%**
3035. **`drivers/ata/pata_pcmcia.c`** -> AI Confidence: **99.31%**
3036. **`drivers/ata/pata_sil680.c`** -> AI Confidence: **99.31%**
3037. **`drivers/ata/pata_triflex.c`** -> AI Confidence: **99.31%**
3038. **`drivers/ata/pata_via.c`** -> AI Confidence: **99.31%**
3039. **`drivers/ata/sata_mv.c`** -> AI Confidence: **99.31%**
3040. **`drivers/ata/sata_sil24.c`** -> AI Confidence: **99.31%**
3041. **`drivers/ata/sata_sis.c`** -> AI Confidence: **99.31%**
3042. **`drivers/atm/eni.c`** -> AI Confidence: **99.31%**
3043. **`drivers/atm/fore200e.c`** -> AI Confidence: **99.31%**
3044. **`drivers/atm/he.c`** -> AI Confidence: **99.31%**
3045. **`drivers/atm/idt77105.c`** -> AI Confidence: **99.31%**
3046. **`drivers/atm/idt77252.c`** -> AI Confidence: **99.31%**
3047. **`drivers/atm/iphase.c`** -> AI Confidence: **99.31%**
3048. **`drivers/atm/lanai.c`** -> AI Confidence: **99.31%**
3049. **`drivers/atm/nicstar.c`** -> AI Confidence: **99.31%**
3050. **`drivers/atm/suni.c`** -> AI Confidence: **99.31%**
3051. **`drivers/auxdisplay/charlcd.c`** -> AI Confidence: **99.31%**
3052. **`drivers/auxdisplay/panel.c`** -> AI Confidence: **99.31%**
3053. **`drivers/base/dd.c`** -> AI Confidence: **99.31%**
3054. **`drivers/base/power/main.c`** -> AI Confidence: **99.31%**
3055. **`drivers/base/power/qos.c`** -> AI Confidence: **99.31%**
3056. **`drivers/base/power/runtime.c`** -> AI Confidence: **99.31%**
3057. **`drivers/base/power/trace.c`** -> AI Confidence: **99.31%**
3058. **`drivers/base/regmap/regcache.c`** -> AI Confidence: **99.31%**
3059. **`drivers/base/regmap/regmap-irq.c`** -> AI Confidence: **99.31%**
3060. **`drivers/base/regmap/regmap-mmio.c`** -> AI Confidence: **99.31%**
3061. **`drivers/base/regmap/regmap.c`** -> AI Confidence: **99.31%**
3062. **`drivers/bcma/driver_mips.c`** -> AI Confidence: **99.31%**
3063. **`drivers/bcma/scan.c`** -> AI Confidence: **99.31%**
3064. **`drivers/bcma/sprom.c`** -> AI Confidence: **99.31%**
3065. **`drivers/block/amiflop.c`** -> AI Confidence: **99.31%**
3066. **`drivers/block/aoe/aoeblk.c`** -> AI Confidence: **99.31%**
3067. **`drivers/block/aoe/aoedev.c`** -> AI Confidence: **99.31%**
3068. **`drivers/block/ataflop.c`** -> AI Confidence: **99.31%**
3069. **`drivers/block/drbd/drbd_main.c`** -> AI Confidence: **99.31%**
3070. **`drivers/block/drbd/drbd_nl.c`** -> AI Confidence: **99.31%**
3071. **`drivers/block/drbd/drbd_receiver.c`** -> AI Confidence: **99.31%**
3072. **`drivers/block/drbd/drbd_worker.c`** -> AI Confidence: **99.31%**
3073. **`drivers/block/floppy.c`** -> AI Confidence: **99.31%**
3074. **`drivers/block/loop.c`** -> AI Confidence: **99.31%**
3075. **`drivers/block/mtip32xx/mtip32xx.c`** -> AI Confidence: **99.31%**
3076. **`drivers/block/nbd.c`** -> AI Confidence: **99.31%**
3077. **`drivers/block/rnbd/rnbd-clt-sysfs.c`** -> AI Confidence: **99.31%**
3078. **`drivers/block/swim3.c`** -> AI Confidence: **99.31%**
3079. **`drivers/block/xen-blkback/blkback.c`** -> AI Confidence: **99.31%**
3080. **`drivers/block/xen-blkfront.c`** -> AI Confidence: **99.31%**
3081. **`drivers/block/z2ram.c`** -> AI Confidence: **99.31%**
3082. **`drivers/block/zloop.c`** -> AI Confidence: **99.31%**
3083. **`drivers/bluetooth/bcm203x.c`** -> AI Confidence: **99.31%**
3084. **`drivers/bluetooth/bluecard_cs.c`** -> AI Confidence: **99.31%**
3085. **`drivers/bluetooth/bt3c_cs.c`** -> AI Confidence: **99.31%**
3086. **`drivers/bluetooth/btintel.c`** -> AI Confidence: **99.31%**
3087. **`drivers/bluetooth/btmrvl_main.c`** -> AI Confidence: **99.31%**
3088. **`drivers/bluetooth/btmrvl_sdio.c`** -> AI Confidence: **99.31%**
3089. **`drivers/bluetooth/btmtk.c`** -> AI Confidence: **99.31%**
3090. **`drivers/bluetooth/btmtksdio.c`** -> AI Confidence: **99.31%**
3091. **`drivers/bluetooth/btmtkuart.c`** -> AI Confidence: **99.31%**
3092. **`drivers/bluetooth/btnxpuart.c`** -> AI Confidence: **99.31%**
3093. **`drivers/bluetooth/btusb.c`** -> AI Confidence: **99.31%**
3094. **`drivers/bluetooth/dtl1_cs.c`** -> AI Confidence: **99.31%**
3095. **`drivers/bluetooth/hci_bcm.c`** -> AI Confidence: **99.31%**
3096. **`drivers/bluetooth/hci_bcsp.c`** -> AI Confidence: **99.31%**
3097. **`drivers/bluetooth/hci_h5.c`** -> AI Confidence: **99.31%**
3098. **`drivers/bluetooth/hci_intel.c`** -> AI Confidence: **99.31%**
3099. **`drivers/bluetooth/hci_ldisc.c`** -> AI Confidence: **99.31%**
3100. **`drivers/bluetooth/hci_qca.c`** -> AI Confidence: **99.31%**
3101. **`drivers/bluetooth/hci_serdev.c`** -> AI Confidence: **99.31%**
3102. **`drivers/bus/imx-weim.c`** -> AI Confidence: **99.31%**
3103. **`drivers/bus/intel-ixp4xx-eb.c`** -> AI Confidence: **99.31%**
3104. **`drivers/bus/mhi/host/boot.c`** -> AI Confidence: **99.31%**
3105. **`drivers/bus/mhi/host/init.c`** -> AI Confidence: **99.31%**
3106. **`drivers/bus/mhi/host/pm.c`** -> AI Confidence: **99.31%**
3107. **`drivers/bus/omap_l3_noc.c`** -> AI Confidence: **99.31%**
3108. **`drivers/bus/omap_l3_smx.c`** -> AI Confidence: **99.31%**
3109. **`drivers/bus/tegra-gmi.c`** -> AI Confidence: **99.31%**
3110. **`drivers/bus/ti-sysc.c`** -> AI Confidence: **99.31%**
3111. **`drivers/cdrom/cdrom.c`** -> AI Confidence: **99.31%**
3112. **`drivers/cdx/controller/cdx_controller.c`** -> AI Confidence: **99.31%**
3113. **`drivers/char/adi.c`** -> AI Confidence: **99.31%**
3114. **`drivers/char/agp/ali-agp.c`** -> AI Confidence: **99.31%**
3115. **`drivers/char/agp/amd64-agp.c`** -> AI Confidence: **99.31%**
3116. **`drivers/char/agp/backend.c`** -> AI Confidence: **99.31%**
3117. **`drivers/char/agp/efficeon-agp.c`** -> AI Confidence: **99.31%**
3118. **`drivers/char/agp/generic.c`** -> AI Confidence: **99.31%**
3119. **`drivers/char/agp/intel-gtt.c`** -> AI Confidence: **99.31%**
3120. **`drivers/char/agp/uninorth-agp.c`** -> AI Confidence: **99.31%**
3121. **`drivers/char/apm-emulation.c`** -> AI Confidence: **99.31%**
3122. **`drivers/char/applicom.c`** -> AI Confidence: **99.31%**
3123. **`drivers/char/bsr.c`** -> AI Confidence: **99.31%**
3124. **`drivers/char/dsp56k.c`** -> AI Confidence: **99.31%**
3125. **`drivers/char/dtlk.c`** -> AI Confidence: **99.31%**
3126. **`drivers/char/hangcheck-timer.c`** -> AI Confidence: **99.31%**
3127. **`drivers/char/hpet.c`** -> AI Confidence: **99.31%**
3128. **`drivers/char/hw_random/intel-rng.c`** -> AI Confidence: **99.31%**
3129. **`drivers/char/hw_random/n2-drv.c`** -> AI Confidence: **99.31%**
3130. **`drivers/char/hw_random/omap-rng.c`** -> AI Confidence: **99.31%**
3131. **`drivers/char/hw_random/via-rng.c`** -> AI Confidence: **99.31%**
3132. **`drivers/char/ipmi/ipmb_dev_int.c`** -> AI Confidence: **99.31%**
3133. **`drivers/char/ipmi/ipmi_devintf.c`** -> AI Confidence: **99.31%**
3134. **`drivers/char/ipmi/ipmi_dmi.c`** -> AI Confidence: **99.31%**
3135. **`drivers/char/ipmi/ipmi_kcs_sm.c`** -> AI Confidence: **99.31%**
3136. **`drivers/char/ipmi/ipmi_msghandler.c`** -> AI Confidence: **99.31%**
3137. **`drivers/char/ipmi/ipmi_si_intf.c`** -> AI Confidence: **99.31%**
3138. **`drivers/char/ipmi/ipmi_ssif.c`** -> AI Confidence: **99.31%**
3139. **`drivers/char/ipmi/ipmi_watchdog.c`** -> AI Confidence: **99.31%**
3140. **`drivers/char/ipmi/kcs_bmc_aspeed.c`** -> AI Confidence: **99.31%**
3141. **`drivers/char/ipmi/kcs_bmc_cdev_ipmi.c`** -> AI Confidence: **99.31%**
3142. **`drivers/char/ipmi/ssif_bmc.c`** -> AI Confidence: **99.31%**
3143. **`drivers/char/lp.c`** -> AI Confidence: **99.31%**
3144. **`drivers/char/misc.c`** -> AI Confidence: **99.31%**
3145. **`drivers/char/nsc_gpio.c`** -> AI Confidence: **99.31%**
3146. **`drivers/char/nvram.c`** -> AI Confidence: **99.31%**
3147. **`drivers/char/nwflash.c`** -> AI Confidence: **99.31%**
3148. **`drivers/char/ppdev.c`** -> AI Confidence: **99.31%**
3149. **`drivers/char/sonypi.c`** -> AI Confidence: **99.31%**
3150. **`drivers/char/toshiba.c`** -> AI Confidence: **99.31%**
3151. **`drivers/char/tpm/eventlog/of.c`** -> AI Confidence: **99.31%**
3152. **`drivers/char/tpm/tpm-interface.c`** -> AI Confidence: **99.31%**
3153. **`drivers/char/tpm/tpm1-cmd.c`** -> AI Confidence: **99.31%**
3154. **`drivers/char/tpm/tpm2-sessions.c`** -> AI Confidence: **99.31%**
3155. **`drivers/char/tpm/tpm_i2c_nuvoton.c`** -> AI Confidence: **99.31%**
3156. **`drivers/char/tpm/tpm_tis_core.c`** -> AI Confidence: **99.31%**
3157. **`drivers/char/tpm/tpm_tis_i2c_cr50.c`** -> AI Confidence: **99.31%**
3158. **`drivers/char/xilinx_hwicap/xilinx_hwicap.c`** -> AI Confidence: **99.31%**
3159. **`drivers/char/xillybus/xillybus_class.c`** -> AI Confidence: **99.31%**
3160. **`drivers/char/xillybus/xillybus_core.c`** -> AI Confidence: **99.31%**
3161. **`drivers/char/xillybus/xillyusb.c`** -> AI Confidence: **99.31%**
3162. **`drivers/clk/analogbits/wrpll-cln28hpc.c`** -> AI Confidence: **99.31%**
3163. **`drivers/clk/axis/clk-artpec6.c`** -> AI Confidence: **99.31%**
3164. **`drivers/clk/bcm/clk-iproc-armpll.c`** -> AI Confidence: **99.31%**
3165. **`drivers/clk/clk-cdce925.c`** -> AI Confidence: **99.31%**
3166. **`drivers/clk/clk-clps711x.c`** -> AI Confidence: **99.31%**
3167. **`drivers/clk/clk-conf.c`** -> AI Confidence: **99.31%**
3168. **`drivers/clk/clk-si5351.c`** -> AI Confidence: **99.31%**
3169. **`drivers/clk/clk-sp7021.c`** -> AI Confidence: **99.31%**
3170. **`drivers/clk/clk-vt8500.c`** -> AI Confidence: **99.31%**
3171. **`drivers/clk/imgtec/clk-boston.c`** -> AI Confidence: **99.31%**
3172. **`drivers/clk/imx/clk-imx27.c`** -> AI Confidence: **99.31%**
3173. **`drivers/clk/imx/clk-imx6q.c`** -> AI Confidence: **99.31%**
3174. **`drivers/clk/imx/clk-imx6ul.c`** -> AI Confidence: **99.31%**
3175. **`drivers/clk/ingenic/cgu.c`** -> AI Confidence: **99.31%**
3176. **`drivers/clk/mvebu/common.c`** -> AI Confidence: **99.31%**
3177. **`drivers/clk/mvebu/cp110-system-controller.c`** -> AI Confidence: **99.31%**
3178. **`drivers/clk/mxs/clk-ssp.c`** -> AI Confidence: **99.31%**
3179. **`drivers/clk/nuvoton/clk-ma35d1-pll.c`** -> AI Confidence: **99.31%**
3180. **`drivers/clk/pxa/clk-pxa3xx.c`** -> AI Confidence: **99.31%**
3181. **`drivers/clk/qcom/gdsc.c`** -> AI Confidence: **99.31%**
3182. **`drivers/clk/renesas/clk-r8a73a4.c`** -> AI Confidence: **99.31%**
3183. **`drivers/clk/renesas/clk-r8a7740.c`** -> AI Confidence: **99.31%**
3184. **`drivers/clk/renesas/clk-r8a7779.c`** -> AI Confidence: **99.31%**
3185. **`drivers/clk/renesas/clk-sh73a0.c`** -> AI Confidence: **99.31%**
3186. **`drivers/clk/renesas/renesas-cpg-mssr.c`** -> AI Confidence: **99.31%**
3187. **`drivers/clk/samsung/clk-exynos-audss.c`** -> AI Confidence: **99.31%**
3188. **`drivers/clk/samsung/clk-pll.c`** -> AI Confidence: **99.31%**
3189. **`drivers/clk/socfpga/clk-gate-a10.c`** -> AI Confidence: **99.31%**
3190. **`drivers/clk/socfpga/clk-gate.c`** -> AI Confidence: **99.31%**
3191. **`drivers/clk/starfive/clk-starfive-jh7100-audio.c`** -> AI Confidence: **99.31%**
3192. **`drivers/clk/starfive/clk-starfive-jh7100.c`** -> AI Confidence: **99.31%**
3193. **`drivers/clk/starfive/clk-starfive-jh7110-sys.c`** -> AI Confidence: **99.31%**
3194. **`drivers/clk/sunxi/clk-sun9i-cpus.c`** -> AI Confidence: **99.31%**
3195. **`drivers/clk/sunxi/clk-sunxi.c`** -> AI Confidence: **99.31%**
3196. **`drivers/clk/tegra/clk-dfll.c`** -> AI Confidence: **99.31%**
3197. **`drivers/clk/tegra/clk-pll.c`** -> AI Confidence: **99.31%**
3198. **`drivers/clk/ti/clkt_dflt.c`** -> AI Confidence: **99.31%**
3199. **`drivers/clk/ti/divider.c`** -> AI Confidence: **99.31%**
3200. **`drivers/clk/ti/dpll.c`** -> AI Confidence: **99.31%**
3201. **`drivers/clk/ti/dpll3xxx.c`** -> AI Confidence: **99.31%**
3202. **`drivers/clk/ti/mux.c`** -> AI Confidence: **99.31%**
3203. **`drivers/clk/ux500/u8500_of_clk.c`** -> AI Confidence: **99.31%**
3204. **`drivers/clk/versatile/clk-icst.c`** -> AI Confidence: **99.31%**
3205. **`drivers/clk/zynq/clkc.c`** -> AI Confidence: **99.31%**
3206. **`drivers/clocksource/armv7m_systick.c`** -> AI Confidence: **99.31%**
3207. **`drivers/clocksource/hyperv_timer.c`** -> AI Confidence: **99.31%**
3208. **`drivers/clocksource/mps2-timer.c`** -> AI Confidence: **99.31%**
3209. **`drivers/clocksource/timer-atmel-tcb.c`** -> AI Confidence: **99.31%**
3210. **`drivers/clocksource/timer-clint.c`** -> AI Confidence: **99.31%**
3211. **`drivers/clocksource/timer-of.c`** -> AI Confidence: **99.31%**
3212. **`drivers/comedi/comedi_fops.c`** -> AI Confidence: **99.31%**
3213. **`drivers/comedi/drivers.c`** -> AI Confidence: **99.31%**
3214. **`drivers/comedi/drivers/adl_pci9118.c`** -> AI Confidence: **99.31%**
3215. **`drivers/comedi/drivers/comedi_isadma.c`** -> AI Confidence: **99.31%**
3216. **`drivers/comedi/drivers/das1800.c`** -> AI Confidence: **99.31%**
3217. **`drivers/comedi/drivers/jr3_pci.c`** -> AI Confidence: **99.31%**
3218. **`drivers/comedi/drivers/ni_at_a2150.c`** -> AI Confidence: **99.31%**
3219. **`drivers/comedi/drivers/ni_atmio.c`** -> AI Confidence: **99.31%**
3220. **`drivers/comedi/drivers/ni_routes.c`** -> AI Confidence: **99.31%**
3221. **`drivers/comedi/drivers/ni_routing/tools/convert_c_to_py.c`** -> AI Confidence: **99.31%**
3222. **`drivers/comedi/drivers/pcl812.c`** -> AI Confidence: **99.31%**
3223. **`drivers/comedi/drivers/usbdux.c`** -> AI Confidence: **99.31%**
3224. **`drivers/comedi/drivers/usbduxfast.c`** -> AI Confidence: **99.31%**
3225. **`drivers/counter/counter-chrdev.c`** -> AI Confidence: **99.31%**
3226. **`drivers/cpufreq/amd-pstate-ut.c`** -> AI Confidence: **99.31%**
3227. **`drivers/cpufreq/amd_freq_sensitivity.c`** -> AI Confidence: **99.31%**
3228. **`drivers/cpufreq/armada-8k-cpufreq.c`** -> AI Confidence: **99.31%**
3229. **`drivers/cpufreq/cpufreq-nforce2.c`** -> AI Confidence: **99.31%**
3230. **`drivers/cpufreq/e_powersaver.c`** -> AI Confidence: **99.31%**
3231. **`drivers/cpufreq/gx-suspmod.c`** -> AI Confidence: **99.31%**
3232. **`drivers/cpufreq/highbank-cpufreq.c`** -> AI Confidence: **99.31%**
3233. **`drivers/cpufreq/imx-cpufreq-dt.c`** -> AI Confidence: **99.31%**
3234. **`drivers/cpufreq/imx6q-cpufreq.c`** -> AI Confidence: **99.31%**
3235. **`drivers/cpufreq/kirkwood-cpufreq.c`** -> AI Confidence: **99.31%**
3236. **`drivers/cpufreq/longhaul.c`** -> AI Confidence: **99.31%**
3237. **`drivers/cpufreq/longrun.c`** -> AI Confidence: **99.31%**
3238. **`drivers/cpufreq/mediatek-cpufreq.c`** -> AI Confidence: **99.31%**
3239. **`drivers/cpufreq/p4-clockmod.c`** -> AI Confidence: **99.31%**
3240. **`drivers/cpufreq/pasemi-cpufreq.c`** -> AI Confidence: **99.31%**
3241. **`drivers/cpufreq/pcc-cpufreq.c`** -> AI Confidence: **99.31%**
3242. **`drivers/cpufreq/pmac32-cpufreq.c`** -> AI Confidence: **99.31%**
3243. **`drivers/cpufreq/pmac64-cpufreq.c`** -> AI Confidence: **99.31%**
3244. **`drivers/cpufreq/powernow-k6.c`** -> AI Confidence: **99.31%**
3245. **`drivers/cpufreq/powernow-k7.c`** -> AI Confidence: **99.31%**
3246. **`drivers/cpufreq/powernow-k8.c`** -> AI Confidence: **99.31%**
3247. **`drivers/cpufreq/powernv-cpufreq.c`** -> AI Confidence: **99.31%**
3248. **`drivers/cpufreq/qcom-cpufreq-nvmem.c`** -> AI Confidence: **99.31%**
3249. **`drivers/cpufreq/s3c64xx-cpufreq.c`** -> AI Confidence: **99.31%**
3250. **`drivers/cpufreq/s5pv210-cpufreq.c`** -> AI Confidence: **99.31%**
3251. **`drivers/cpufreq/sparc-us2e-cpufreq.c`** -> AI Confidence: **99.31%**
3252. **`drivers/cpufreq/sparc-us3-cpufreq.c`** -> AI Confidence: **99.31%**
3253. **`drivers/cpufreq/spear-cpufreq.c`** -> AI Confidence: **99.31%**
3254. **`drivers/cpufreq/speedstep-centrino.c`** -> AI Confidence: **99.31%**
3255. **`drivers/cpufreq/speedstep-smi.c`** -> AI Confidence: **99.31%**
3256. **`drivers/cpufreq/sun50i-cpufreq-nvmem.c`** -> AI Confidence: **99.31%**
3257. **`drivers/cpufreq/vexpress-spc-cpufreq.c`** -> AI Confidence: **99.31%**
3258. **`drivers/cpuidle/cpuidle-powernv.c`** -> AI Confidence: **99.31%**
3259. **`drivers/cpuidle/cpuidle-tegra.c`** -> AI Confidence: **99.31%**
3260. **`drivers/cpuidle/cpuidle.c`** -> AI Confidence: **99.31%**
3261. **`drivers/cpuidle/driver.c`** -> AI Confidence: **99.31%**
3262. **`drivers/cpuidle/dt_idle_states.c`** -> AI Confidence: **99.31%**
3263. **`drivers/crypto/allwinner/sun4i-ss/sun4i-ss-core.c`** -> AI Confidence: **99.31%**
3264. **`drivers/crypto/allwinner/sun8i-ce/sun8i-ce-cipher.c`** -> AI Confidence: **99.31%**
3265. **`drivers/crypto/allwinner/sun8i-ce/sun8i-ce-core.c`** -> AI Confidence: **99.31%**
3266. **`drivers/crypto/allwinner/sun8i-ss/sun8i-ss-core.c`** -> AI Confidence: **99.31%**
3267. **`drivers/crypto/amlogic/amlogic-gxl-core.c`** -> AI Confidence: **99.31%**
3268. **`drivers/crypto/bcm/cipher.c`** -> AI Confidence: **99.31%**
3269. **`drivers/crypto/caam/ctrl.c`** -> AI Confidence: **99.31%**
3270. **`drivers/crypto/cavium/nitrox/nitrox_sriov.c`** -> AI Confidence: **99.31%**
3271. **`drivers/crypto/ccp/ccp-dev.c`** -> AI Confidence: **99.31%**
3272. **`drivers/crypto/ccp/ccp-ops.c`** -> AI Confidence: **99.31%**
3273. **`drivers/crypto/ccree/cc_buffer_mgr.c`** -> AI Confidence: **99.31%**
3274. **`drivers/crypto/ccree/cc_cipher.c`** -> AI Confidence: **99.31%**
3275. **`drivers/crypto/ccree/cc_driver.c`** -> AI Confidence: **99.31%**
3276. **`drivers/crypto/chelsio/chcr_algo.c`** -> AI Confidence: **99.31%**
3277. **`drivers/crypto/inside-secure/eip93/eip93-common.c`** -> AI Confidence: **99.31%**
3278. **`drivers/crypto/inside-secure/eip93/eip93-main.c`** -> AI Confidence: **99.31%**
3279. **`drivers/crypto/inside-secure/safexcel.c`** -> AI Confidence: **99.31%**
3280. **`drivers/crypto/intel/keembay/ocs-aes.c`** -> AI Confidence: **99.31%**
3281. **`drivers/crypto/intel/qat/qat_420xx/adf_drv.c`** -> AI Confidence: **99.31%**
3282. **`drivers/crypto/intel/qat/qat_4xxx/adf_drv.c`** -> AI Confidence: **99.31%**
3283. **`drivers/crypto/intel/qat/qat_c3xxx/adf_drv.c`** -> AI Confidence: **99.31%**
3284. **`drivers/crypto/intel/qat/qat_c62x/adf_drv.c`** -> AI Confidence: **99.31%**
3285. **`drivers/crypto/intel/qat/qat_common/adf_ctl_drv.c`** -> AI Confidence: **99.31%**
3286. **`drivers/crypto/intel/qat/qat_common/adf_init.c`** -> AI Confidence: **99.31%**
3287. **`drivers/crypto/intel/qat/qat_common/adf_pfvf_pf_proto.c`** -> AI Confidence: **99.31%**
3288. **`drivers/crypto/intel/qat/qat_common/adf_rl.c`** -> AI Confidence: **99.31%**
3289. **`drivers/crypto/intel/qat/qat_common/qat_bl.c`** -> AI Confidence: **99.31%**
3290. **`drivers/crypto/intel/qat/qat_common/qat_crypto.c`** -> AI Confidence: **99.31%**
3291. **`drivers/crypto/intel/qat/qat_common/qat_hal.c`** -> AI Confidence: **99.31%**
3292. **`drivers/crypto/intel/qat/qat_dh895xcc/adf_drv.c`** -> AI Confidence: **99.31%**
3293. **`drivers/crypto/marvell/octeontx2/otx2_cptpf_main.c`** -> AI Confidence: **99.31%**
3294. **`drivers/crypto/marvell/octeontx2/otx2_cptpf_ucode.c`** -> AI Confidence: **99.31%**
3295. **`drivers/crypto/nx/nx-aes-cbc.c`** -> AI Confidence: **99.31%**
3296. **`drivers/crypto/nx/nx-aes-ccm.c`** -> AI Confidence: **99.31%**
3297. **`drivers/crypto/nx/nx-aes-ctr.c`** -> AI Confidence: **99.31%**
3298. **`drivers/crypto/nx/nx-aes-ecb.c`** -> AI Confidence: **99.31%**
3299. **`drivers/crypto/nx/nx-aes-gcm.c`** -> AI Confidence: **99.31%**
3300. **`drivers/crypto/nx/nx-common-powernv.c`** -> AI Confidence: **99.31%**
3301. **`drivers/crypto/nx/nx.c`** -> AI Confidence: **99.31%**
3302. **`drivers/crypto/qce/aead.c`** -> AI Confidence: **99.31%**
3303. **`drivers/crypto/qce/common.c`** -> AI Confidence: **99.31%**
3304. **`drivers/crypto/qce/skcipher.c`** -> AI Confidence: **99.31%**
3305. **`drivers/crypto/rockchip/rk3288_crypto.c`** -> AI Confidence: **99.31%**
3306. **`drivers/cxl/core/trace.h`** -> AI Confidence: **99.31%**
3307. **`drivers/dax/kmem.c`** -> AI Confidence: **99.31%**
3308. **`drivers/devfreq/event/exynos-nocp.c`** -> AI Confidence: **99.31%**
3309. **`drivers/devfreq/mtk-cci-devfreq.c`** -> AI Confidence: **99.31%**
3310. **`drivers/dio/dio.c`** -> AI Confidence: **99.31%**
3311. **`drivers/dma-buf/st-dma-fence-chain.c`** -> AI Confidence: **99.31%**
3312. **`drivers/dma/amba-pl08x.c`** -> AI Confidence: **99.31%**
3313. **`drivers/dma/dw-edma/dw-edma-core.c`** -> AI Confidence: **99.31%**
3314. **`drivers/dma/dw-edma/dw-edma-v0-core.c`** -> AI Confidence: **99.31%**
3315. **`drivers/dma/ioat/init.c`** -> AI Confidence: **99.31%**
3316. **`drivers/dma/ppc4xx/adma.c`** -> AI Confidence: **99.31%**
3317. **`drivers/dma/tegra210-adma.c`** -> AI Confidence: **99.31%**
3318. **`drivers/dma/ti/k3-psil.c`** -> AI Confidence: **99.31%**
3319. **`drivers/dma/ti/k3-udma.c`** -> AI Confidence: **99.31%**
3320. **`drivers/dma/ti/omap-dma.c`** -> AI Confidence: **99.31%**
3321. **`drivers/dpll/zl3073x/prop.c`** -> AI Confidence: **99.31%**
3322. **`drivers/dpll/zl3073x/ref.c`** -> AI Confidence: **99.31%**
3323. **`drivers/edac/armada_xp_edac.c`** -> AI Confidence: **99.31%**
3324. **`drivers/edac/bluefield_edac.c`** -> AI Confidence: **99.31%**
3325. **`drivers/edac/cpc925_edac.c`** -> AI Confidence: **99.31%**
3326. **`drivers/edac/edac_device.c`** -> AI Confidence: **99.31%**
3327. **`drivers/edac/fsl_ddr_edac.c`** -> AI Confidence: **99.31%**
3328. **`drivers/edac/ghes_edac.c`** -> AI Confidence: **99.31%**
3329. **`drivers/edac/highbank_l2_edac.c`** -> AI Confidence: **99.31%**
3330. **`drivers/edac/i10nm_base.c`** -> AI Confidence: **99.31%**
3331. **`drivers/edac/i5000_edac.c`** -> AI Confidence: **99.31%**
3332. **`drivers/edac/i5400_edac.c`** -> AI Confidence: **99.31%**
3333. **`drivers/edac/i7core_edac.c`** -> AI Confidence: **99.31%**
3334. **`drivers/edac/octeon_edac-l2c.c`** -> AI Confidence: **99.31%**
3335. **`drivers/edac/pnd2_edac.c`** -> AI Confidence: **99.31%**
3336. **`drivers/edac/qcom_edac.c`** -> AI Confidence: **99.31%**
3337. **`drivers/edac/sb_edac.c`** -> AI Confidence: **99.31%**
3338. **`drivers/edac/skx_base.c`** -> AI Confidence: **99.31%**
3339. **`drivers/edac/skx_common.c`** -> AI Confidence: **99.31%**
3340. **`drivers/edac/synopsys_edac.c`** -> AI Confidence: **99.31%**
3341. **`drivers/edac/versalnet_edac.c`** -> AI Confidence: **99.31%**
3342. **`drivers/edac/xgene_edac.c`** -> AI Confidence: **99.31%**
3343. **`drivers/eisa/eisa-bus.c`** -> AI Confidence: **99.31%**
3344. **`drivers/extcon/extcon-intel-cht-wc.c`** -> AI Confidence: **99.31%**
3345. **`drivers/extcon/extcon-lc824206xa.c`** -> AI Confidence: **99.31%**
3346. **`drivers/extcon/extcon-max14577.c`** -> AI Confidence: **99.31%**
3347. **`drivers/extcon/extcon-max77843.c`** -> AI Confidence: **99.31%**
3348. **`drivers/extcon/extcon-max8997.c`** -> AI Confidence: **99.31%**
3349. **`drivers/extcon/extcon-palmas.c`** -> AI Confidence: **99.31%**
3350. **`drivers/extcon/extcon-rt8973a.c`** -> AI Confidence: **99.31%**
3351. **`drivers/extcon/extcon-rtk-type-c.c`** -> AI Confidence: **99.31%**
3352. **`drivers/extcon/extcon-sm5502.c`** -> AI Confidence: **99.31%**
3353. **`drivers/firmware/arm_scmi/quirks.c`** -> AI Confidence: **99.31%**
3354. **`drivers/firmware/arm_scpi.c`** -> AI Confidence: **99.31%**
3355. **`drivers/firmware/broadcom/bcm47xx_nvram.c`** -> AI Confidence: **99.31%**
3356. **`drivers/firmware/broadcom/bcm47xx_sprom.c`** -> AI Confidence: **99.31%**
3357. **`drivers/firmware/cirrus/cs_dsp.c`** -> AI Confidence: **99.31%**
3358. **`drivers/firmware/efi/apple-properties.c`** -> AI Confidence: **99.31%**
3359. **`drivers/firmware/efi/capsule.c`** -> AI Confidence: **99.31%**
3360. **`drivers/firmware/efi/cper.c`** -> AI Confidence: **99.31%**
3361. **`drivers/firmware/efi/earlycon.c`** -> AI Confidence: **99.31%**
3362. **`drivers/firmware/efi/efi-init.c`** -> AI Confidence: **99.31%**
3363. **`drivers/firmware/efi/efi.c`** -> AI Confidence: **99.31%**
3364. **`drivers/firmware/efi/embedded-firmware.c`** -> AI Confidence: **99.31%**
3365. **`drivers/firmware/efi/libstub/efi-stub-helper.c`** -> AI Confidence: **99.31%**
3366. **`drivers/firmware/efi/libstub/gop.c`** -> AI Confidence: **99.31%**
3367. **`drivers/firmware/efi/mokvar-table.c`** -> AI Confidence: **99.31%**
3368. **`drivers/firmware/efi/ovmf-debug-log.c`** -> AI Confidence: **99.31%**
3369. **`drivers/firmware/google/framebuffer-coreboot.c`** -> AI Confidence: **99.31%**
3370. **`drivers/firmware/google/gsmi.c`** -> AI Confidence: **99.31%**
3371. **`drivers/firmware/iscsi_ibft.c`** -> AI Confidence: **99.31%**
3372. **`drivers/firmware/iscsi_ibft_find.c`** -> AI Confidence: **99.31%**
3373. **`drivers/firmware/psci/psci_checker.c`** -> AI Confidence: **99.31%**
3374. **`drivers/firmware/sysfb_simplefb.c`** -> AI Confidence: **99.31%**
3375. **`drivers/firmware/trusted_foundations.c`** -> AI Confidence: **99.31%**
3376. **`drivers/fpga/dfl-pci.c`** -> AI Confidence: **99.31%**
3377. **`drivers/fpga/zynq-fpga.c`** -> AI Confidence: **99.31%**
3378. **`drivers/fsi/fsi-master-ast-cf.c`** -> AI Confidence: **99.31%**
3379. **`drivers/fsi/fsi-occ.c`** -> AI Confidence: **99.31%**
3380. **`drivers/gnss/sirf.c`** -> AI Confidence: **99.31%**
3381. **`drivers/gpib/nec7210/nec7210.c`** -> AI Confidence: **99.31%**
3382. **`drivers/gpib/ni_usb/ni_usb_gpib.c`** -> AI Confidence: **99.31%**
3383. **`drivers/gpib/tms9914/tms9914.c`** -> AI Confidence: **99.31%**
3384. **`drivers/gpio/gpio-eic-sprd.c`** -> AI Confidence: **99.31%**
3385. **`drivers/gpio/gpio-max3191x.c`** -> AI Confidence: **99.31%**
3386. **`drivers/gpio/gpio-regmap.c`** -> AI Confidence: **99.31%**
3387. **`drivers/gpio/gpio-stp-xway.c`** -> AI Confidence: **99.31%**
3388. **`drivers/gpio/gpio-twl4030.c`** -> AI Confidence: **99.31%**
3389. **`drivers/gpio/gpio-wm831x.c`** -> AI Confidence: **99.31%**
3390. **`drivers/gpu/drm/amd/amdgpu/aldebaran.c`** -> AI Confidence: **99.31%**
3391. **`drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd_arcturus.c`** -> AI Confidence: **99.31%**
3392. **`drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd_gpuvm.c`** -> AI Confidence: **99.31%**
3393. **`drivers/gpu/drm/amd/amdgpu/amdgpu_atombios.c`** -> AI Confidence: **99.31%**
3394. **`drivers/gpu/drm/amd/amdgpu/amdgpu_atomfirmware.c`** -> AI Confidence: **99.31%**
3395. **`drivers/gpu/drm/amd/amdgpu/amdgpu_cgs.c`** -> AI Confidence: **99.31%**
3396. **`drivers/gpu/drm/amd/amdgpu/amdgpu_connectors.c`** -> AI Confidence: **99.31%**
3397. **`drivers/gpu/drm/amd/amdgpu/amdgpu_cs.c`** -> AI Confidence: **99.31%**
3398. **`drivers/gpu/drm/amd/amdgpu/amdgpu_debugfs.c`** -> AI Confidence: **99.31%**
3399. **`drivers/gpu/drm/amd/amdgpu/amdgpu_device.c`** -> AI Confidence: **99.31%**
3400. **`drivers/gpu/drm/amd/amdgpu/amdgpu_discovery.c`** -> AI Confidence: **99.31%**
3401. **`drivers/gpu/drm/amd/amdgpu/amdgpu_drv.c`** -> AI Confidence: **99.31%**
3402. **`drivers/gpu/drm/amd/amdgpu/amdgpu_fdinfo.c`** -> AI Confidence: **99.31%**
3403. **`drivers/gpu/drm/amd/amdgpu/amdgpu_fru_eeprom.c`** -> AI Confidence: **99.31%**
3404. **`drivers/gpu/drm/amd/amdgpu/amdgpu_gem.c`** -> AI Confidence: **99.31%**
3405. **`drivers/gpu/drm/amd/amdgpu/amdgpu_gfx.c`** -> AI Confidence: **99.31%**
3406. **`drivers/gpu/drm/amd/amdgpu/amdgpu_gmc.c`** -> AI Confidence: **99.31%**
3407. **`drivers/gpu/drm/amd/amdgpu/amdgpu_kms.c`** -> AI Confidence: **99.31%**
3408. **`drivers/gpu/drm/amd/amdgpu/amdgpu_object.c`** -> AI Confidence: **99.31%**
3409. **`drivers/gpu/drm/amd/amdgpu/amdgpu_pll.c`** -> AI Confidence: **99.31%**
3410. **`drivers/gpu/drm/amd/amdgpu/amdgpu_psp.c`** -> AI Confidence: **99.31%**
3411. **`drivers/gpu/drm/amd/amdgpu/amdgpu_ras.c`** -> AI Confidence: **99.31%**
3412. **`drivers/gpu/drm/amd/amdgpu/amdgpu_ras_eeprom.c`** -> AI Confidence: **99.31%**
3413. **`drivers/gpu/drm/amd/amdgpu/amdgpu_sdma.c`** -> AI Confidence: **99.31%**
3414. **`drivers/gpu/drm/amd/amdgpu/amdgpu_uvd.c`** -> AI Confidence: **99.31%**
3415. **`drivers/gpu/drm/amd/amdgpu/amdgpu_vce.c`** -> AI Confidence: **99.31%**
3416. **`drivers/gpu/drm/amd/amdgpu/amdgpu_vcn.c`** -> AI Confidence: **99.31%**
3417. **`drivers/gpu/drm/amd/amdgpu/amdgpu_virt.c`** -> AI Confidence: **99.31%**
3418. **`drivers/gpu/drm/amd/amdgpu/amdgpu_xgmi.c`** -> AI Confidence: **99.31%**
3419. **`drivers/gpu/drm/amd/amdgpu/aqua_vanjaram.c`** -> AI Confidence: **99.31%**
3420. **`drivers/gpu/drm/amd/amdgpu/atombios_crtc.c`** -> AI Confidence: **99.31%**
3421. **`drivers/gpu/drm/amd/amdgpu/atombios_dp.c`** -> AI Confidence: **99.31%**
3422. **`drivers/gpu/drm/amd/amdgpu/cik.c`** -> AI Confidence: **99.31%**
3423. **`drivers/gpu/drm/amd/amdgpu/dce_v10_0.c`** -> AI Confidence: **99.31%**
3424. **`drivers/gpu/drm/amd/amdgpu/dce_v8_0.c`** -> AI Confidence: **99.31%**
3425. **`drivers/gpu/drm/amd/amdgpu/gfx_v10_0.c`** -> AI Confidence: **99.31%**
3426. **`drivers/gpu/drm/amd/amdgpu/gfx_v11_0.c`** -> AI Confidence: **99.31%**
3427. **`drivers/gpu/drm/amd/amdgpu/gfx_v11_0_3.c`** -> AI Confidence: **99.31%**
3428. **`drivers/gpu/drm/amd/amdgpu/gfx_v6_0.c`** -> AI Confidence: **99.31%**
3429. **`drivers/gpu/drm/amd/amdgpu/gfx_v8_0.c`** -> AI Confidence: **99.31%**
3430. **`drivers/gpu/drm/amd/amdgpu/gfx_v9_0.c`** -> AI Confidence: **99.31%**
3431. **`drivers/gpu/drm/amd/amdgpu/gfx_v9_4.c`** -> AI Confidence: **99.31%**
3432. **`drivers/gpu/drm/amd/amdgpu/gfx_v9_4_2.c`** -> AI Confidence: **99.31%**
3433. **`drivers/gpu/drm/amd/amdgpu/gmc_v10_0.c`** -> AI Confidence: **99.31%**
3434. **`drivers/gpu/drm/amd/amdgpu/gmc_v11_0.c`** -> AI Confidence: **99.31%**
3435. **`drivers/gpu/drm/amd/amdgpu/gmc_v12_0.c`** -> AI Confidence: **99.31%**
3436. **`drivers/gpu/drm/amd/amdgpu/gmc_v12_1.c`** -> AI Confidence: **99.31%**
3437. **`drivers/gpu/drm/amd/amdgpu/gmc_v6_0.c`** -> AI Confidence: **99.31%**
3438. **`drivers/gpu/drm/amd/amdgpu/gmc_v7_0.c`** -> AI Confidence: **99.31%**
3439. **`drivers/gpu/drm/amd/amdgpu/gmc_v8_0.c`** -> AI Confidence: **99.31%**
3440. **`drivers/gpu/drm/amd/amdgpu/gmc_v9_0.c`** -> AI Confidence: **99.31%**
3441. **`drivers/gpu/drm/amd/amdgpu/imu_v11_0.c`** -> AI Confidence: **99.31%**
3442. **`drivers/gpu/drm/amd/amdgpu/imu_v12_0.c`** -> AI Confidence: **99.31%**
3443. **`drivers/gpu/drm/amd/amdgpu/jpeg_v4_0_5.c`** -> AI Confidence: **99.31%**
3444. **`drivers/gpu/drm/amd/amdgpu/mes_v12_0.c`** -> AI Confidence: **99.31%**
3445. **`drivers/gpu/drm/amd/amdgpu/mes_v12_1.c`** -> AI Confidence: **99.31%**
3446. **`drivers/gpu/drm/amd/amdgpu/mmhub_v2_0.c`** -> AI Confidence: **99.31%**
3447. **`drivers/gpu/drm/amd/amdgpu/nbio_v2_3.c`** -> AI Confidence: **99.31%**
3448. **`drivers/gpu/drm/amd/amdgpu/nv.c`** -> AI Confidence: **99.31%**
3449. **`drivers/gpu/drm/amd/amdgpu/psp_v11_0.c`** -> AI Confidence: **99.31%**
3450. **`drivers/gpu/drm/amd/amdgpu/psp_v15_0_8.c`** -> AI Confidence: **99.31%**
3451. **`drivers/gpu/drm/amd/amdgpu/si.c`** -> AI Confidence: **99.31%**
3452. **`drivers/gpu/drm/amd/amdgpu/soc15.c`** -> AI Confidence: **99.31%**
3453. **`drivers/gpu/drm/amd/amdgpu/soc21.c`** -> AI Confidence: **99.31%**
3454. **`drivers/gpu/drm/amd/amdgpu/soc_v1_0.c`** -> AI Confidence: **99.31%**
3455. **`drivers/gpu/drm/amd/amdgpu/umc_v12_0.c`** -> AI Confidence: **99.31%**
3456. **`drivers/gpu/drm/amd/amdgpu/umc_v6_1.c`** -> AI Confidence: **99.31%**
3457. **`drivers/gpu/drm/amd/amdgpu/vcn_v2_5.c`** -> AI Confidence: **99.31%**
3458. **`drivers/gpu/drm/amd/amdgpu/vcn_v3_0.c`** -> AI Confidence: **99.31%**
3459. **`drivers/gpu/drm/amd/amdgpu/vcn_v4_0_5.c`** -> AI Confidence: **99.31%**
3460. **`drivers/gpu/drm/amd/amdgpu/vi.c`** -> AI Confidence: **99.31%**
3461. **`drivers/gpu/drm/amd/amdkfd/kfd_chardev.c`** -> AI Confidence: **99.31%**
3462. **`drivers/gpu/drm/amd/amdkfd/kfd_crat.c`** -> AI Confidence: **99.31%**
3463. **`drivers/gpu/drm/amd/amdkfd/kfd_device.c`** -> AI Confidence: **99.31%**
3464. **`drivers/gpu/drm/amd/amdkfd/kfd_kernel_queue.c`** -> AI Confidence: **99.31%**
3465. **`drivers/gpu/drm/amd/amdkfd/kfd_migrate.c`** -> AI Confidence: **99.31%**
3466. **`drivers/gpu/drm/amd/amdkfd/kfd_process_queue_manager.c`** -> AI Confidence: **99.31%**
3467. **`drivers/gpu/drm/amd/amdkfd/kfd_svm.c`** -> AI Confidence: **99.31%**
3468. **`drivers/gpu/drm/amd/amdkfd/kfd_topology.c`** -> AI Confidence: **99.31%**
3469. **`drivers/gpu/drm/amd/display/amdgpu_dm/amdgpu_dm.c`** -> AI Confidence: **99.31%**
3470. **`drivers/gpu/drm/amd/display/amdgpu_dm/amdgpu_dm_crc.c`** -> AI Confidence: **99.31%**
3471. **`drivers/gpu/drm/amd/display/amdgpu_dm/amdgpu_dm_debugfs.c`** -> AI Confidence: **99.31%**
3472. **`drivers/gpu/drm/amd/display/amdgpu_dm/amdgpu_dm_mst_types.c`** -> AI Confidence: **99.31%**
3473. **`drivers/gpu/drm/amd/display/amdgpu_dm/amdgpu_dm_plane.c`** -> AI Confidence: **99.31%**
3474. **`drivers/gpu/drm/amd/display/dc/bios/bios_parser.c`** -> AI Confidence: **99.31%**
3475. **`drivers/gpu/drm/amd/display/dc/bios/command_table.c`** -> AI Confidence: **99.31%**
3476. **`drivers/gpu/drm/amd/display/dc/clk_mgr/clk_mgr.c`** -> AI Confidence: **99.31%**
3477. **`drivers/gpu/drm/amd/display/dc/clk_mgr/dce100/dce_clk_mgr.c`** -> AI Confidence: **99.31%**
3478. **`drivers/gpu/drm/amd/display/dc/clk_mgr/dcn20/dcn20_clk_mgr.c`** -> AI Confidence: **99.31%**
3479. **`drivers/gpu/drm/amd/display/dc/clk_mgr/dcn21/rn_clk_mgr.c`** -> AI Confidence: **99.31%**
3480. **`drivers/gpu/drm/amd/display/dc/clk_mgr/dcn314/dcn314_clk_mgr.c`** -> AI Confidence: **99.31%**
3481. **`drivers/gpu/drm/amd/display/dc/clk_mgr/dcn315/dcn315_clk_mgr.c`** -> AI Confidence: **99.31%**
3482. **`drivers/gpu/drm/amd/display/dc/clk_mgr/dcn316/dcn316_clk_mgr.c`** -> AI Confidence: **99.31%**
3483. **`drivers/gpu/drm/amd/display/dc/clk_mgr/dcn32/dcn32_clk_mgr.c`** -> AI Confidence: **99.31%**
3484. **`drivers/gpu/drm/amd/display/dc/clk_mgr/dcn35/dcn35_clk_mgr.c`** -> AI Confidence: **99.31%**
3485. **`drivers/gpu/drm/amd/display/dc/clk_mgr/dcn401/dcn401_clk_mgr.c`** -> AI Confidence: **99.31%**
3486. **`drivers/gpu/drm/amd/display/dc/core/dc.c`** -> AI Confidence: **99.31%**
3487. **`drivers/gpu/drm/amd/display/dc/core/dc_resource.c`** -> AI Confidence: **99.31%**
3488. **`drivers/gpu/drm/amd/display/dc/dccg/dcn401/dcn401_dccg.c`** -> AI Confidence: **99.31%**
3489. **`drivers/gpu/drm/amd/display/dc/dce/dce_aux.c`** -> AI Confidence: **99.31%**
3490. **`drivers/gpu/drm/amd/display/dc/dce/dce_link_encoder.c`** -> AI Confidence: **99.31%**
3491. **`drivers/gpu/drm/amd/display/dc/dce112/dce112_compressor.c`** -> AI Confidence: **99.31%**
3492. **`drivers/gpu/drm/amd/display/dc/dcn10/dcn10_hw_sequencer_debug.c`** -> AI Confidence: **99.31%**
3493. **`drivers/gpu/drm/amd/display/dc/dio/dcn10/dcn10_stream_encoder.c`** -> AI Confidence: **99.31%**
3494. **`drivers/gpu/drm/amd/display/dc/dio/dcn301/dcn301_dio_link_encoder.c`** -> AI Confidence: **99.31%**
3495. **`drivers/gpu/drm/amd/display/dc/dio/dcn31/dcn31_dio_link_encoder.c`** -> AI Confidence: **99.31%**
3496. **`drivers/gpu/drm/amd/display/dc/dio/dcn32/dcn32_dio_link_encoder.c`** -> AI Confidence: **99.31%**
3497. **`drivers/gpu/drm/amd/display/dc/dio/dcn321/dcn321_dio_link_encoder.c`** -> AI Confidence: **99.31%**
3498. **`drivers/gpu/drm/amd/display/dc/dio/dcn35/dcn35_dio_stream_encoder.c`** -> AI Confidence: **99.31%**
3499. **`drivers/gpu/drm/amd/display/dc/dio/dcn401/dcn401_dio_link_encoder.c`** -> AI Confidence: **99.31%**
3500. **`drivers/gpu/drm/amd/display/dc/dml/dcn20/dcn20_fpu.c`** -> AI Confidence: **99.31%**
3501. **`drivers/gpu/drm/amd/display/dc/dml/dcn30/dcn30_fpu.c`** -> AI Confidence: **99.31%**
3502. **`drivers/gpu/drm/amd/display/dc/dml/dcn314/dcn314_fpu.c`** -> AI Confidence: **99.31%**
3503. **`drivers/gpu/drm/amd/display/dc/dml/dcn32/dcn32_fpu.c`** -> AI Confidence: **99.31%**
3504. **`drivers/gpu/drm/amd/display/dc/dml/dcn35/dcn35_fpu.c`** -> AI Confidence: **99.31%**
3505. **`drivers/gpu/drm/amd/display/dc/dml/dcn351/dcn351_fpu.c`** -> AI Confidence: **99.31%**
3506. **`drivers/gpu/drm/amd/display/dc/dml2_0/dml21/dml21_translation_helper.c`** -> AI Confidence: **99.31%**
3507. **`drivers/gpu/drm/amd/display/dc/dsc/dc_dsc.c`** -> AI Confidence: **99.31%**
3508. **`drivers/gpu/drm/amd/display/dc/gpio/dce120/hw_translate_dce120.c`** -> AI Confidence: **99.31%**
3509. **`drivers/gpu/drm/amd/display/dc/gpio/dce60/hw_translate_dce60.c`** -> AI Confidence: **99.31%**
3510. **`drivers/gpu/drm/amd/display/dc/gpio/dce80/hw_translate_dce80.c`** -> AI Confidence: **99.31%**
3511. **`drivers/gpu/drm/amd/display/dc/gpio/dcn10/hw_translate_dcn10.c`** -> AI Confidence: **99.31%**
3512. **`drivers/gpu/drm/amd/display/dc/gpio/dcn20/hw_translate_dcn20.c`** -> AI Confidence: **99.31%**
3513. **`drivers/gpu/drm/amd/display/dc/gpio/dcn21/hw_translate_dcn21.c`** -> AI Confidence: **99.31%**
3514. **`drivers/gpu/drm/amd/display/dc/gpio/dcn30/hw_translate_dcn30.c`** -> AI Confidence: **99.31%**
3515. **`drivers/gpu/drm/amd/display/dc/gpio/hw_ddc.c`** -> AI Confidence: **99.31%**
3516. **`drivers/gpu/drm/amd/display/dc/gpio/hw_factory.c`** -> AI Confidence: **99.31%**
3517. **`drivers/gpu/drm/amd/display/dc/gpio/hw_translate.c`** -> AI Confidence: **99.31%**
3518. **`drivers/gpu/drm/amd/display/dc/hwss/dce110/dce110_hwseq.c`** -> AI Confidence: **99.31%**
3519. **`drivers/gpu/drm/amd/display/dc/hwss/dcn10/dcn10_hwseq.c`** -> AI Confidence: **99.31%**
3520. **`drivers/gpu/drm/amd/display/dc/hwss/dcn20/dcn20_hwseq.c`** -> AI Confidence: **99.31%**
3521. **`drivers/gpu/drm/amd/display/dc/hwss/dcn30/dcn30_hwseq.c`** -> AI Confidence: **99.31%**
3522. **`drivers/gpu/drm/amd/display/dc/hwss/dcn31/dcn31_hwseq.c`** -> AI Confidence: **99.31%**
3523. **`drivers/gpu/drm/amd/display/dc/hwss/dcn314/dcn314_hwseq.c`** -> AI Confidence: **99.31%**
3524. **`drivers/gpu/drm/amd/display/dc/hwss/dcn32/dcn32_hwseq.c`** -> AI Confidence: **99.31%**
3525. **`drivers/gpu/drm/amd/display/dc/hwss/dcn35/dcn35_hwseq.c`** -> AI Confidence: **99.31%**
3526. **`drivers/gpu/drm/amd/display/dc/hwss/dcn401/dcn401_hwseq.c`** -> AI Confidence: **99.31%**
3527. **`drivers/gpu/drm/amd/display/dc/link/accessories/link_dp_cts.c`** -> AI Confidence: **99.31%**
3528. **`drivers/gpu/drm/amd/display/dc/link/link_detection.c`** -> AI Confidence: **99.31%**
3529. **`drivers/gpu/drm/amd/display/dc/link/protocols/link_dp_capability.c`** -> AI Confidence: **99.31%**
3530. **`drivers/gpu/drm/amd/display/dc/link/protocols/link_dp_dpia.c`** -> AI Confidence: **99.31%**
3531. **`drivers/gpu/drm/amd/display/dc/link/protocols/link_dp_training.c`** -> AI Confidence: **99.31%**
3532. **`drivers/gpu/drm/amd/display/dc/link/protocols/link_dp_training_dpia.c`** -> AI Confidence: **99.31%**
3533. **`drivers/gpu/drm/amd/display/dc/optc/dcn35/dcn35_optc.c`** -> AI Confidence: **99.31%**
3534. **`drivers/gpu/drm/amd/pm/legacy-dpm/legacy_dpm.c`** -> AI Confidence: **99.31%**
3535. **`drivers/gpu/drm/amd/pm/legacy-dpm/si_smc.c`** -> AI Confidence: **99.31%**
3536. **`drivers/gpu/drm/amd/pm/powerplay/hwmgr/hwmgr.c`** -> AI Confidence: **99.31%**
3537. **`drivers/gpu/drm/amd/pm/powerplay/hwmgr/vega10_processpptables.c`** -> AI Confidence: **99.31%**
3538. **`drivers/gpu/drm/amd/pm/powerplay/hwmgr/vega20_hwmgr.c`** -> AI Confidence: **99.31%**
3539. **`drivers/gpu/drm/amd/pm/powerplay/smumgr/ci_smumgr.c`** -> AI Confidence: **99.31%**
3540. **`drivers/gpu/drm/amd/pm/powerplay/smumgr/smu7_smumgr.c`** -> AI Confidence: **99.31%**
3541. **`drivers/gpu/drm/amd/pm/swsmu/smu11/arcturus_ppt.c`** -> AI Confidence: **99.31%**
3542. **`drivers/gpu/drm/amd/pm/swsmu/smu11/cyan_skillfish_ppt.c`** -> AI Confidence: **99.31%**
3543. **`drivers/gpu/drm/amd/pm/swsmu/smu11/navi10_ppt.c`** -> AI Confidence: **99.31%**
3544. **`drivers/gpu/drm/amd/pm/swsmu/smu11/sienna_cichlid_ppt.c`** -> AI Confidence: **99.31%**
3545. **`drivers/gpu/drm/amd/pm/swsmu/smu11/smu_v11_0.c`** -> AI Confidence: **99.31%**
3546. **`drivers/gpu/drm/amd/pm/swsmu/smu11/vangogh_ppt.c`** -> AI Confidence: **99.31%**
3547. **`drivers/gpu/drm/amd/pm/swsmu/smu13/aldebaran_ppt.c`** -> AI Confidence: **99.31%**
3548. **`drivers/gpu/drm/amd/pm/swsmu/smu13/smu_v13_0.c`** -> AI Confidence: **99.31%**
3549. **`drivers/gpu/drm/amd/pm/swsmu/smu13/smu_v13_0_0_ppt.c`** -> AI Confidence: **99.31%**
3550. **`drivers/gpu/drm/amd/pm/swsmu/smu13/smu_v13_0_12_ppt.c`** -> AI Confidence: **99.31%**
3551. **`drivers/gpu/drm/amd/pm/swsmu/smu13/smu_v13_0_5_ppt.c`** -> AI Confidence: **99.31%**
3552. **`drivers/gpu/drm/amd/pm/swsmu/smu13/smu_v13_0_6_ppt.c`** -> AI Confidence: **99.31%**
3553. **`drivers/gpu/drm/amd/pm/swsmu/smu13/smu_v13_0_7_ppt.c`** -> AI Confidence: **99.31%**
3554. **`drivers/gpu/drm/amd/pm/swsmu/smu13/yellow_carp_ppt.c`** -> AI Confidence: **99.31%**
3555. **`drivers/gpu/drm/amd/pm/swsmu/smu14/smu_v14_0.c`** -> AI Confidence: **99.31%**
3556. **`drivers/gpu/drm/amd/pm/swsmu/smu14/smu_v14_0_2_ppt.c`** -> AI Confidence: **99.31%**
3557. **`drivers/gpu/drm/amd/pm/swsmu/smu15/smu_v15_0.c`** -> AI Confidence: **99.31%**
3558. **`drivers/gpu/drm/amd/pm/swsmu/smu15/smu_v15_0_0_ppt.c`** -> AI Confidence: **99.31%**
3559. **`drivers/gpu/drm/arm/display/komeda/komeda_dev.c`** -> AI Confidence: **99.31%**
3560. **`drivers/gpu/drm/arm/malidp_hw.c`** -> AI Confidence: **99.31%**
3561. **`drivers/gpu/drm/armada/armada_fb.c`** -> AI Confidence: **99.31%**
3562. **`drivers/gpu/drm/armada/armada_overlay.c`** -> AI Confidence: **99.31%**
3563. **`drivers/gpu/drm/armada/armada_plane.c`** -> AI Confidence: **99.31%**
3564. **`drivers/gpu/drm/atmel-hlcdc/atmel_hlcdc_crtc.c`** -> AI Confidence: **99.31%**
3565. **`drivers/gpu/drm/atmel-hlcdc/atmel_hlcdc_plane.c`** -> AI Confidence: **99.31%**
3566. **`drivers/gpu/drm/bridge/adv7511/adv7511_cec.c`** -> AI Confidence: **99.31%**
3567. **`drivers/gpu/drm/bridge/adv7511/adv7511_drv.c`** -> AI Confidence: **99.31%**
3568. **`drivers/gpu/drm/bridge/analogix/analogix_dp_core.c`** -> AI Confidence: **99.31%**
3569. **`drivers/gpu/drm/bridge/analogix/analogix_dp_reg.c`** -> AI Confidence: **99.31%**
3570. **`drivers/gpu/drm/bridge/cadence/cdns-mhdp8546-core.c`** -> AI Confidence: **99.31%**
3571. **`drivers/gpu/drm/bridge/display-connector.c`** -> AI Confidence: **99.31%**
3572. **`drivers/gpu/drm/bridge/ite-it66121.c`** -> AI Confidence: **99.31%**
3573. **`drivers/gpu/drm/bridge/parade-ps8622.c`** -> AI Confidence: **99.31%**
3574. **`drivers/gpu/drm/bridge/synopsys/dw-dp.c`** -> AI Confidence: **99.31%**
3575. **`drivers/gpu/drm/bridge/tc358767.c`** -> AI Confidence: **99.31%**
3576. **`drivers/gpu/drm/bridge/ti-sn65dsi86.c`** -> AI Confidence: **99.31%**
3577. **`drivers/gpu/drm/display/drm_dp_dual_mode_helper.c`** -> AI Confidence: **99.31%**
3578. **`drivers/gpu/drm/display/drm_dp_helper.c`** -> AI Confidence: **99.31%**
3579. **`drivers/gpu/drm/display/drm_dsc_helper.c`** -> AI Confidence: **99.31%**
3580. **`drivers/gpu/drm/display/drm_hdmi_helper.c`** -> AI Confidence: **99.31%**
3581. **`drivers/gpu/drm/drm_atomic_helper.c`** -> AI Confidence: **99.31%**
3582. **`drivers/gpu/drm/drm_atomic_uapi.c`** -> AI Confidence: **99.31%**
3583. **`drivers/gpu/drm/drm_client_modeset.c`** -> AI Confidence: **99.31%**
3584. **`drivers/gpu/drm/drm_color_mgmt.c`** -> AI Confidence: **99.31%**
3585. **`drivers/gpu/drm/drm_crtc.c`** -> AI Confidence: **99.31%**
3586. **`drivers/gpu/drm/drm_crtc_helper.c`** -> AI Confidence: **99.31%**
3587. **`drivers/gpu/drm/drm_draw.c`** -> AI Confidence: **99.31%**
3588. **`drivers/gpu/drm/drm_drv.c`** -> AI Confidence: **99.31%**
3589. **`drivers/gpu/drm/drm_edid.c`** -> AI Confidence: **99.31%**
3590. **`drivers/gpu/drm/drm_edid_load.c`** -> AI Confidence: **99.31%**
3591. **`drivers/gpu/drm/drm_fb_helper.c`** -> AI Confidence: **99.31%**
3592. **`drivers/gpu/drm/drm_framebuffer.c`** -> AI Confidence: **99.31%**
3593. **`drivers/gpu/drm/drm_lease.c`** -> AI Confidence: **99.31%**
3594. **`drivers/gpu/drm/drm_modes.c`** -> AI Confidence: **99.31%**
3595. **`drivers/gpu/drm/drm_pagemap.c`** -> AI Confidence: **99.31%**
3596. **`drivers/gpu/drm/drm_print.c`** -> AI Confidence: **99.31%**
3597. **`drivers/gpu/drm/drm_probe_helper.c`** -> AI Confidence: **99.31%**
3598. **`drivers/gpu/drm/drm_suballoc.c`** -> AI Confidence: **99.31%**
3599. **`drivers/gpu/drm/drm_vma_manager.c`** -> AI Confidence: **99.31%**
3600. **`drivers/gpu/drm/etnaviv/etnaviv_buffer.c`** -> AI Confidence: **99.31%**
3601. **`drivers/gpu/drm/etnaviv/etnaviv_gem_submit.c`** -> AI Confidence: **99.31%**
3602. **`drivers/gpu/drm/etnaviv/etnaviv_gpu.c`** -> AI Confidence: **99.31%**
3603. **`drivers/gpu/drm/exynos/exynos_drm_fimc.c`** -> AI Confidence: **99.31%**
3604. **`drivers/gpu/drm/exynos/exynos_drm_gsc.c`** -> AI Confidence: **99.31%**
3605. **`drivers/gpu/drm/fsl-dcu/fsl_dcu_drm_plane.c`** -> AI Confidence: **99.31%**
3606. **`drivers/gpu/drm/gma500/gma_display.c`** -> AI Confidence: **99.31%**
3607. **`drivers/gpu/drm/gma500/intel_bios.c`** -> AI Confidence: **99.31%**
3608. **`drivers/gpu/drm/gma500/oaktrail_crtc.c`** -> AI Confidence: **99.31%**
3609. **`drivers/gpu/drm/gma500/oaktrail_lvds.c`** -> AI Confidence: **99.31%**
3610. **`drivers/gpu/drm/gma500/psb_drv.c`** -> AI Confidence: **99.31%**
3611. **`drivers/gpu/drm/gma500/psb_irq.c`** -> AI Confidence: **99.31%**
3612. **`drivers/gpu/drm/gud/gud_connector.c`** -> AI Confidence: **99.31%**
3613. **`drivers/gpu/drm/gud/gud_drv.c`** -> AI Confidence: **99.31%**
3614. **`drivers/gpu/drm/i915/display/i9xx_plane.c`** -> AI Confidence: **99.31%**
3615. **`drivers/gpu/drm/i915/display/intel_acpi.c`** -> AI Confidence: **99.31%**
3616. **`drivers/gpu/drm/i915/display/intel_combo_phy.c`** -> AI Confidence: **99.31%**
3617. **`drivers/gpu/drm/i915/display/intel_crtc_state_dump.c`** -> AI Confidence: **99.31%**
3618. **`drivers/gpu/drm/i915/display/intel_cursor.c`** -> AI Confidence: **99.31%**
3619. **`drivers/gpu/drm/i915/display/intel_display.c`** -> AI Confidence: **99.31%**
3620. **`drivers/gpu/drm/i915/display/intel_display_device.c`** -> AI Confidence: **99.31%**
3621. **`drivers/gpu/drm/i915/display/intel_dp_aux.c`** -> AI Confidence: **99.31%**
3622. **`drivers/gpu/drm/i915/display/intel_dram.c`** -> AI Confidence: **99.31%**
3623. **`drivers/gpu/drm/i915/display/intel_dsi_vbt.c`** -> AI Confidence: **99.31%**
3624. **`drivers/gpu/drm/i915/display/intel_fb_pin.c`** -> AI Confidence: **99.31%**
3625. **`drivers/gpu/drm/i915/display/intel_hotplug_irq.c`** -> AI Confidence: **99.31%**
3626. **`drivers/gpu/drm/i915/display/intel_load_detect.c`** -> AI Confidence: **99.31%**
3627. **`drivers/gpu/drm/i915/display/intel_pch_refclk.c`** -> AI Confidence: **99.31%**
3628. **`drivers/gpu/drm/i915/display/intel_pipe_crc.c`** -> AI Confidence: **99.31%**
3629. **`drivers/gpu/drm/i915/display/intel_sprite.c`** -> AI Confidence: **99.31%**
3630. **`drivers/gpu/drm/i915/display/skl_universal_plane.c`** -> AI Confidence: **99.31%**
3631. **`drivers/gpu/drm/i915/gem/i915_gem_context.c`** -> AI Confidence: **99.31%**
3632. **`drivers/gpu/drm/i915/gem/i915_gem_domain.c`** -> AI Confidence: **99.31%**
3633. **`drivers/gpu/drm/i915/gem/i915_gem_execbuffer.c`** -> AI Confidence: **99.31%**
3634. **`drivers/gpu/drm/i915/gem/i915_gem_mman.c`** -> AI Confidence: **99.31%**
3635. **`drivers/gpu/drm/i915/gem/i915_gem_pm.c`** -> AI Confidence: **99.31%**
3636. **`drivers/gpu/drm/i915/gem/i915_gem_shrinker.c`** -> AI Confidence: **99.31%**
3637. **`drivers/gpu/drm/i915/gem/i915_gem_stolen.c`** -> AI Confidence: **99.31%**
3638. **`drivers/gpu/drm/i915/gem/i915_gem_throttle.c`** -> AI Confidence: **99.31%**
3639. **`drivers/gpu/drm/i915/gem/i915_gem_tiling.c`** -> AI Confidence: **99.31%**
3640. **`drivers/gpu/drm/i915/gem/selftests/i915_gem_coherency.c`** -> AI Confidence: **99.31%**
3641. **`drivers/gpu/drm/i915/gem/selftests/i915_gem_context.c`** -> AI Confidence: **99.31%**
3642. **`drivers/gpu/drm/i915/gem/selftests/i915_gem_dmabuf.c`** -> AI Confidence: **99.31%**
3643. **`drivers/gpu/drm/i915/gem/selftests/i915_gem_mman.c`** -> AI Confidence: **99.31%**
3644. **`drivers/gpu/drm/i915/gem/selftests/igt_gem_utils.c`** -> AI Confidence: **99.31%**
3645. **`drivers/gpu/drm/i915/gt/gen8_engine_cs.c`** -> AI Confidence: **99.31%**
3646. **`drivers/gpu/drm/i915/gt/gen8_ppgtt.c`** -> AI Confidence: **99.31%**
3647. **`drivers/gpu/drm/i915/gt/intel_context.c`** -> AI Confidence: **99.31%**
3648. **`drivers/gpu/drm/i915/gt/intel_engine_cs.c`** -> AI Confidence: **99.31%**
3649. **`drivers/gpu/drm/i915/gt/intel_engine_heartbeat.c`** -> AI Confidence: **99.31%**
3650. **`drivers/gpu/drm/i915/gt/intel_engine_user.c`** -> AI Confidence: **99.31%**
3651. **`drivers/gpu/drm/i915/gt/intel_ggtt_fencing.c`** -> AI Confidence: **99.31%**
3652. **`drivers/gpu/drm/i915/gt/intel_gt_irq.c`** -> AI Confidence: **99.31%**
3653. **`drivers/gpu/drm/i915/gt/intel_gt_pm_debugfs.c`** -> AI Confidence: **99.31%**
3654. **`drivers/gpu/drm/i915/gt/intel_migrate.c`** -> AI Confidence: **99.31%**
3655. **`drivers/gpu/drm/i915/gt/intel_renderstate.c`** -> AI Confidence: **99.31%**
3656. **`drivers/gpu/drm/i915/gt/intel_ring_submission.c`** -> AI Confidence: **99.31%**
3657. **`drivers/gpu/drm/i915/gt/intel_sseu.c`** -> AI Confidence: **99.31%**
3658. **`drivers/gpu/drm/i915/gt/intel_tlb.c`** -> AI Confidence: **99.31%**
3659. **`drivers/gpu/drm/i915/gt/intel_workarounds.c`** -> AI Confidence: **99.31%**
3660. **`drivers/gpu/drm/i915/gt/selftest_context.c`** -> AI Confidence: **99.31%**
3661. **`drivers/gpu/drm/i915/gt/selftest_engine_pm.c`** -> AI Confidence: **99.31%**
3662. **`drivers/gpu/drm/i915/gt/selftest_execlists.c`** -> AI Confidence: **99.31%**
3663. **`drivers/gpu/drm/i915/gt/selftest_hangcheck.c`** -> AI Confidence: **99.31%**
3664. **`drivers/gpu/drm/i915/gt/selftest_lrc.c`** -> AI Confidence: **99.31%**
3665. **`drivers/gpu/drm/i915/gt/selftest_rc6.c`** -> AI Confidence: **99.31%**
3666. **`drivers/gpu/drm/i915/gt/selftest_reset.c`** -> AI Confidence: **99.31%**
3667. **`drivers/gpu/drm/i915/gt/selftest_rps.c`** -> AI Confidence: **99.31%**
3668. **`drivers/gpu/drm/i915/gt/selftest_timeline.c`** -> AI Confidence: **99.31%**
3669. **`drivers/gpu/drm/i915/gt/selftest_tlb.c`** -> AI Confidence: **99.31%**
3670. **`drivers/gpu/drm/i915/gt/selftest_workarounds.c`** -> AI Confidence: **99.31%**
3671. **`drivers/gpu/drm/i915/gt/uc/intel_gsc_fw.c`** -> AI Confidence: **99.31%**
3672. **`drivers/gpu/drm/i915/gt/uc/intel_gsc_uc.c`** -> AI Confidence: **99.31%**
3673. **`drivers/gpu/drm/i915/gt/uc/intel_gsc_uc_heci_cmd_submit.c`** -> AI Confidence: **99.31%**
3674. **`drivers/gpu/drm/i915/gt/uc/intel_guc_fw.c`** -> AI Confidence: **99.31%**
3675. **`drivers/gpu/drm/i915/gt/uc/intel_huc_fw.c`** -> AI Confidence: **99.31%**
3676. **`drivers/gpu/drm/i915/gvt/display.c`** -> AI Confidence: **99.31%**
3677. **`drivers/gpu/drm/i915/gvt/edid.c`** -> AI Confidence: **99.31%**
3678. **`drivers/gpu/drm/i915/gvt/fb_decoder.c`** -> AI Confidence: **99.31%**
3679. **`drivers/gpu/drm/i915/gvt/gtt.c`** -> AI Confidence: **99.31%**
3680. **`drivers/gpu/drm/i915/gvt/mmio.c`** -> AI Confidence: **99.31%**
3681. **`drivers/gpu/drm/i915/i915_cmd_parser.c`** -> AI Confidence: **99.31%**
3682. **`drivers/gpu/drm/i915/i915_gem.c`** -> AI Confidence: **99.31%**
3683. **`drivers/gpu/drm/i915/i915_gem_evict.c`** -> AI Confidence: **99.31%**
3684. **`drivers/gpu/drm/i915/i915_gem_gtt.c`** -> AI Confidence: **99.31%**
3685. **`drivers/gpu/drm/i915/i915_ioctl.c`** -> AI Confidence: **99.31%**
3686. **`drivers/gpu/drm/i915/i915_mitigations.c`** -> AI Confidence: **99.31%**
3687. **`drivers/gpu/drm/i915/i915_module.c`** -> AI Confidence: **99.31%**
3688. **`drivers/gpu/drm/i915/i915_perf.c`** -> AI Confidence: **99.31%**
3689. **`drivers/gpu/drm/i915/intel_device_info.c`** -> AI Confidence: **99.31%**
3690. **`drivers/gpu/drm/i915/intel_gvt_mmio_table.c`** -> AI Confidence: **99.31%**
3691. **`drivers/gpu/drm/i915/intel_memory_region.c`** -> AI Confidence: **99.31%**
3692. **`drivers/gpu/drm/i915/intel_uncore.c`** -> AI Confidence: **99.31%**
3693. **`drivers/gpu/drm/i915/pxp/intel_pxp_gsccs.c`** -> AI Confidence: **99.31%**
3694. **`drivers/gpu/drm/i915/selftests/i915_gem_evict.c`** -> AI Confidence: **99.31%**
3695. **`drivers/gpu/drm/i915/selftests/i915_gem_gtt.c`** -> AI Confidence: **99.31%**
3696. **`drivers/gpu/drm/i915/selftests/i915_request.c`** -> AI Confidence: **99.31%**
3697. **`drivers/gpu/drm/i915/selftests/i915_vma.c`** -> AI Confidence: **99.31%**
3698. **`drivers/gpu/drm/imagination/pvr_device_info.c`** -> AI Confidence: **99.31%**
3699. **`drivers/gpu/drm/imagination/pvr_fw_startstop.c`** -> AI Confidence: **99.31%**
3700. **`drivers/gpu/drm/imagination/pvr_stream.c`** -> AI Confidence: **99.31%**
3701. **`drivers/gpu/drm/imagination/pvr_vm_mips.c`** -> AI Confidence: **99.31%**
3702. **`drivers/gpu/drm/imx/dcss/dcss-plane.c`** -> AI Confidence: **99.31%**
3703. **`drivers/gpu/drm/imx/ipuv3/imx-ldb.c`** -> AI Confidence: **99.31%**
3704. **`drivers/gpu/drm/imx/ipuv3/ipuv3-plane.c`** -> AI Confidence: **99.31%**
3705. **`drivers/gpu/drm/kmb/kmb_plane.c`** -> AI Confidence: **99.31%**
3706. **`drivers/gpu/drm/logicvc/logicvc_drm.c`** -> AI Confidence: **99.31%**
3707. **`drivers/gpu/drm/mediatek/mtk_hdmi_ddc_v2.c`** -> AI Confidence: **99.31%**
3708. **`drivers/gpu/drm/meson/meson_drv.c`** -> AI Confidence: **99.31%**
3709. **`drivers/gpu/drm/meson/meson_overlay.c`** -> AI Confidence: **99.31%**
3710. **`drivers/gpu/drm/meson/meson_plane.c`** -> AI Confidence: **99.31%**
3711. **`drivers/gpu/drm/mgag200/mgag200_drv.c`** -> AI Confidence: **99.31%**
3712. **`drivers/gpu/drm/mgag200/mgag200_g200.c`** -> AI Confidence: **99.31%**
3713. **`drivers/gpu/drm/msm/adreno/a6xx_gmu.c`** -> AI Confidence: **99.31%**
3714. **`drivers/gpu/drm/msm/adreno/a6xx_gpu.c`** -> AI Confidence: **99.31%**
3715. **`drivers/gpu/drm/msm/disp/dpu1/dpu_hw_cdm.c`** -> AI Confidence: **99.31%**
3716. **`drivers/gpu/drm/msm/disp/dpu1/dpu_rm.c`** -> AI Confidence: **99.31%**
3717. **`drivers/gpu/drm/msm/dp/dp_ctrl.c`** -> AI Confidence: **99.31%**
3718. **`drivers/gpu/drm/msm/dsi/phy/dsi_phy_7nm.c`** -> AI Confidence: **99.31%**
3719. **`drivers/gpu/drm/msm/msm_gem_submit.c`** -> AI Confidence: **99.31%**
3720. **`drivers/gpu/drm/nouveau/dispnv04/dfp.c`** -> AI Confidence: **99.31%**
3721. **`drivers/gpu/drm/nouveau/dispnv04/disp.c`** -> AI Confidence: **99.31%**
3722. **`drivers/gpu/drm/nouveau/dispnv50/crc907d.c`** -> AI Confidence: **99.31%**
3723. **`drivers/gpu/drm/nouveau/dispnv50/crcc37d.c`** -> AI Confidence: **99.31%**
3724. **`drivers/gpu/drm/nouveau/dispnv50/crcc57d.c`** -> AI Confidence: **99.31%**
3725. **`drivers/gpu/drm/nouveau/dispnv50/head.c`** -> AI Confidence: **99.31%**
3726. **`drivers/gpu/drm/nouveau/dispnv50/wndw.c`** -> AI Confidence: **99.31%**
3727. **`drivers/gpu/drm/nouveau/nouveau_abi16.c`** -> AI Confidence: **99.31%**
3728. **`drivers/gpu/drm/nouveau/nouveau_backlight.c`** -> AI Confidence: **99.31%**
3729. **`drivers/gpu/drm/nouveau/nouveau_bios.c`** -> AI Confidence: **99.31%**
3730. **`drivers/gpu/drm/nouveau/nouveau_chan.c`** -> AI Confidence: **99.31%**
3731. **`drivers/gpu/drm/nouveau/nouveau_gem.c`** -> AI Confidence: **99.31%**
3732. **`drivers/gpu/drm/nouveau/nvkm/engine/device/user.c`** -> AI Confidence: **99.31%**
3733. **`drivers/gpu/drm/nouveau/nvkm/engine/disp/dp.c`** -> AI Confidence: **99.31%**
3734. **`drivers/gpu/drm/nouveau/nvkm/engine/disp/ga102.c`** -> AI Confidence: **99.31%**
3735. **`drivers/gpu/drm/nouveau/nvkm/engine/disp/tu102.c`** -> AI Confidence: **99.31%**
3736. **`drivers/gpu/drm/nouveau/nvkm/engine/disp/uconn.c`** -> AI Confidence: **99.31%**
3737. **`drivers/gpu/drm/nouveau/nvkm/engine/fifo/chan.c`** -> AI Confidence: **99.31%**
3738. **`drivers/gpu/drm/nouveau/nvkm/engine/gr/nv04.c`** -> AI Confidence: **99.31%**
3739. **`drivers/gpu/drm/nouveau/nvkm/engine/gr/nv40.c`** -> AI Confidence: **99.31%**
3740. **`drivers/gpu/drm/nouveau/nvkm/subdev/devinit/nv04.c`** -> AI Confidence: **99.31%**
3741. **`drivers/gpu/drm/nouveau/nvkm/subdev/fb/ramgk104.c`** -> AI Confidence: **99.31%**
3742. **`drivers/gpu/drm/nouveau/nvkm/subdev/fb/ramgt215.c`** -> AI Confidence: **99.31%**
3743. **`drivers/gpu/drm/nouveau/nvkm/subdev/fb/ramnv40.c`** -> AI Confidence: **99.31%**
3744. **`drivers/gpu/drm/nouveau/nvkm/subdev/fb/ramnv50.c`** -> AI Confidence: **99.31%**
3745. **`drivers/gpu/drm/nouveau/nvkm/subdev/gsp/rm/r535/fifo.c`** -> AI Confidence: **99.31%**
3746. **`drivers/gpu/drm/nouveau/nvkm/subdev/gsp/rm/r570/gr.c`** -> AI Confidence: **99.31%**
3747. **`drivers/gpu/drm/nouveau/nvkm/subdev/i2c/base.c`** -> AI Confidence: **99.31%**
3748. **`drivers/gpu/drm/omapdrm/dss/dss.c`** -> AI Confidence: **99.31%**
3749. **`drivers/gpu/drm/omapdrm/dss/hdmi_phy.c`** -> AI Confidence: **99.31%**
3750. **`drivers/gpu/drm/omapdrm/dss/pll.c`** -> AI Confidence: **99.31%**
3751. **`drivers/gpu/drm/omapdrm/omap_dmm_tiler.c`** -> AI Confidence: **99.31%**
3752. **`drivers/gpu/drm/omapdrm/omap_fb.c`** -> AI Confidence: **99.31%**
3753. **`drivers/gpu/drm/omapdrm/tcm-sita.c`** -> AI Confidence: **99.31%**
3754. **`drivers/gpu/drm/panel/panel-edp.c`** -> AI Confidence: **99.31%**
3755. **`drivers/gpu/drm/panfrost/panfrost_device.c`** -> AI Confidence: **99.31%**
3756. **`drivers/gpu/drm/panfrost/panfrost_gpu.c`** -> AI Confidence: **99.31%**
3757. **`drivers/gpu/drm/panfrost/panfrost_perfcnt.c`** -> AI Confidence: **99.31%**
3758. **`drivers/gpu/drm/panthor/panthor_hw.c`** -> AI Confidence: **99.31%**
3759. **`drivers/gpu/drm/pl111/pl111_display.c`** -> AI Confidence: **99.31%**
3760. **`drivers/gpu/drm/qxl/qxl_kms.c`** -> AI Confidence: **99.31%**
3761. **`drivers/gpu/drm/radeon/atombios_encoders.c`** -> AI Confidence: **99.31%**
3762. **`drivers/gpu/drm/radeon/ci_dpm.c`** -> AI Confidence: **99.31%**
3763. **`drivers/gpu/drm/radeon/cik.c`** -> AI Confidence: **99.31%**
3764. **`drivers/gpu/drm/radeon/cypress_dpm.c`** -> AI Confidence: **99.31%**
3765. **`drivers/gpu/drm/radeon/evergreen_hdmi.c`** -> AI Confidence: **99.31%**
3766. **`drivers/gpu/drm/radeon/r100.c`** -> AI Confidence: **99.31%**
3767. **`drivers/gpu/drm/radeon/r420.c`** -> AI Confidence: **99.31%**
3768. **`drivers/gpu/drm/radeon/r600.c`** -> AI Confidence: **99.31%**
3769. **`drivers/gpu/drm/radeon/r600_hdmi.c`** -> AI Confidence: **99.31%**
3770. **`drivers/gpu/drm/radeon/radeon_atombios.c`** -> AI Confidence: **99.31%**
3771. **`drivers/gpu/drm/radeon/radeon_bios.c`** -> AI Confidence: **99.31%**
3772. **`drivers/gpu/drm/radeon/radeon_connectors.c`** -> AI Confidence: **99.31%**
3773. **`drivers/gpu/drm/radeon/radeon_cs.c`** -> AI Confidence: **99.31%**
3774. **`drivers/gpu/drm/radeon/radeon_device.c`** -> AI Confidence: **99.31%**
3775. **`drivers/gpu/drm/radeon/radeon_display.c`** -> AI Confidence: **99.31%**
3776. **`drivers/gpu/drm/radeon/radeon_encoders.c`** -> AI Confidence: **99.31%**
3777. **`drivers/gpu/drm/radeon/radeon_legacy_crtc.c`** -> AI Confidence: **99.31%**
3778. **`drivers/gpu/drm/radeon/radeon_legacy_encoders.c`** -> AI Confidence: **99.31%**
3779. **`drivers/gpu/drm/radeon/radeon_pm.c`** -> AI Confidence: **99.31%**
3780. **`drivers/gpu/drm/radeon/rs400.c`** -> AI Confidence: **99.31%**
3781. **`drivers/gpu/drm/radeon/rs600.c`** -> AI Confidence: **99.31%**
3782. **`drivers/gpu/drm/radeon/rv515.c`** -> AI Confidence: **99.31%**
3783. **`drivers/gpu/drm/renesas/rcar-du/rcar_du_encoder.c`** -> AI Confidence: **99.31%**
3784. **`drivers/gpu/drm/rockchip/rockchip_rgb.c`** -> AI Confidence: **99.31%**
3785. **`drivers/gpu/drm/rockchip/rockchip_vop2_reg.c`** -> AI Confidence: **99.31%**
3786. **`drivers/gpu/drm/sprd/megacores_pll.c`** -> AI Confidence: **99.31%**
3787. **`drivers/gpu/drm/sti/sti_compositor.c`** -> AI Confidence: **99.31%**
3788. **`drivers/gpu/drm/sti/sti_plane.c`** -> AI Confidence: **99.31%**
3789. **`drivers/gpu/drm/stm/ltdc.c`** -> AI Confidence: **99.31%**
3790. **`drivers/gpu/drm/sun4i/sun4i_crtc.c`** -> AI Confidence: **99.31%**
3791. **`drivers/gpu/drm/sysfb/vesadrm.c`** -> AI Confidence: **99.31%**
3792. **`drivers/gpu/drm/tegra/fb.c`** -> AI Confidence: **99.31%**
3793. **`drivers/gpu/drm/tegra/output.c`** -> AI Confidence: **99.31%**
3794. **`drivers/gpu/drm/tegra/plane.c`** -> AI Confidence: **99.31%**
3795. **`drivers/gpu/drm/tegra/sor.c`** -> AI Confidence: **99.31%**
3796. **`drivers/gpu/drm/tegra/submit.c`** -> AI Confidence: **99.31%**
3797. **`drivers/gpu/drm/tiny/repaper.c`** -> AI Confidence: **99.31%**
3798. **`drivers/gpu/drm/ttm/ttm_pool.c`** -> AI Confidence: **99.31%**
3799. **`drivers/gpu/drm/tve200/tve200_drv.c`** -> AI Confidence: **99.31%**
3800. **`drivers/gpu/drm/vc4/vc4_kms.c`** -> AI Confidence: **99.31%**
3801. **`drivers/gpu/drm/vmwgfx/vmwgfx_msg.c`** -> AI Confidence: **99.31%**
3802. **`drivers/gpu/drm/xe/xe_drm_client.c`** -> AI Confidence: **99.31%**
3803. **`drivers/gpu/drm/xe/xe_gt_ccs_mode.c`** -> AI Confidence: **99.31%**
3804. **`drivers/gpu/drm/xe/xe_gt_mcr.c`** -> AI Confidence: **99.31%**
3805. **`drivers/gpu/drm/xe/xe_guc_capture.c`** -> AI Confidence: **99.31%**
3806. **`drivers/gpu/drm/xe/xe_hwmon.c`** -> AI Confidence: **99.31%**
3807. **`drivers/gpu/drm/xe/xe_module.c`** -> AI Confidence: **99.31%**
3808. **`drivers/gpu/drm/xe/xe_pci_rebar.c`** -> AI Confidence: **99.31%**
3809. **`drivers/gpu/drm/xe/xe_wait_user_fence.c`** -> AI Confidence: **99.31%**
3810. **`drivers/gpu/drm/xen/xen_drm_front_evtchnl.c`** -> AI Confidence: **99.31%**
3811. **`drivers/gpu/drm/xlnx/zynqmp_dpsub.c`** -> AI Confidence: **99.31%**
3812. **`drivers/gpu/host1x/job.c`** -> AI Confidence: **99.31%**
3813. **`drivers/gpu/ipu-v3/ipu-common.c`** -> AI Confidence: **99.31%**
3814. **`drivers/gpu/ipu-v3/ipu-csi.c`** -> AI Confidence: **99.31%**
3815. **`drivers/hid/amd-sfh-hid/amd_sfh_client.c`** -> AI Confidence: **99.31%**
3816. **`drivers/hid/amd-sfh-hid/hid_descriptor/amd_sfh_hid_desc.c`** -> AI Confidence: **99.31%**
3817. **`drivers/hid/hid-alps.c`** -> AI Confidence: **99.31%**
3818. **`drivers/hid/hid-apple.c`** -> AI Confidence: **99.31%**
3819. **`drivers/hid/hid-asus.c`** -> AI Confidence: **99.31%**
3820. **`drivers/hid/hid-core.c`** -> AI Confidence: **99.31%**
3821. **`drivers/hid/hid-cp2112.c`** -> AI Confidence: **99.31%**
3822. **`drivers/hid/hid-lenovo.c`** -> AI Confidence: **99.31%**
3823. **`drivers/hid/hid-lg-g15.c`** -> AI Confidence: **99.31%**
3824. **`drivers/hid/hid-lg4ff.c`** -> AI Confidence: **99.31%**
3825. **`drivers/hid/hid-logitech-dj.c`** -> AI Confidence: **99.31%**
3826. **`drivers/hid/hid-logitech-hidpp.c`** -> AI Confidence: **99.31%**
3827. **`drivers/hid/hid-magicmouse.c`** -> AI Confidence: **99.31%**
3828. **`drivers/hid/hid-mcp2221.c`** -> AI Confidence: **99.31%**
3829. **`drivers/hid/hid-multitouch.c`** -> AI Confidence: **99.31%**
3830. **`drivers/hid/hid-nintendo.c`** -> AI Confidence: **99.31%**
3831. **`drivers/hid/hid-picolcd_core.c`** -> AI Confidence: **99.31%**
3832. **`drivers/hid/hid-picolcd_leds.c`** -> AI Confidence: **99.31%**
3833. **`drivers/hid/hid-prodikeys.c`** -> AI Confidence: **99.31%**
3834. **`drivers/hid/hid-sensor-hub.c`** -> AI Confidence: **99.31%**
3835. **`drivers/hid/hid-sony.c`** -> AI Confidence: **99.31%**
3836. **`drivers/hid/hid-steam.c`** -> AI Confidence: **99.31%**
3837. **`drivers/hid/hid-uclogic-core.c`** -> AI Confidence: **99.31%**
3838. **`drivers/hid/hidraw.c`** -> AI Confidence: **99.31%**
3839. **`drivers/hid/intel-ish-hid/ishtp/dma-if.c`** -> AI Confidence: **99.31%**
3840. **`drivers/hid/intel-ish-hid/ishtp/loader.c`** -> AI Confidence: **99.31%**
3841. **`drivers/hid/intel-thc-hid/intel-quickspi/quickspi-protocol.c`** -> AI Confidence: **99.31%**
3842. **`drivers/hv/connection.c`** -> AI Confidence: **99.31%**
3843. **`drivers/hv/hv_proc.c`** -> AI Confidence: **99.31%**
3844. **`drivers/hv/mshv_root_main.c`** -> AI Confidence: **99.31%**
3845. **`drivers/hwmon/abituguru.c`** -> AI Confidence: **99.31%**
3846. **`drivers/hwmon/abituguru3.c`** -> AI Confidence: **99.31%**
3847. **`drivers/hwmon/acpi_power_meter.c`** -> AI Confidence: **99.31%**
3848. **`drivers/hwmon/adm1177.c`** -> AI Confidence: **99.31%**
3849. **`drivers/hwmon/adm9240.c`** -> AI Confidence: **99.31%**
3850. **`drivers/hwmon/adt7411.c`** -> AI Confidence: **99.31%**
3851. **`drivers/hwmon/adt7462.c`** -> AI Confidence: **99.31%**
3852. **`drivers/hwmon/adt7470.c`** -> AI Confidence: **99.31%**
3853. **`drivers/hwmon/adt7475.c`** -> AI Confidence: **99.31%**
3854. **`drivers/hwmon/amc6821.c`** -> AI Confidence: **99.31%**
3855. **`drivers/hwmon/asb100.c`** -> AI Confidence: **99.31%**
3856. **`drivers/hwmon/asus_rog_ryujin.c`** -> AI Confidence: **99.31%**
3857. **`drivers/hwmon/coretemp.c`** -> AI Confidence: **99.31%**
3858. **`drivers/hwmon/corsair-cpro.c`** -> AI Confidence: **99.31%**
3859. **`drivers/hwmon/corsair-psu.c`** -> AI Confidence: **99.31%**
3860. **`drivers/hwmon/cros_ec_hwmon.c`** -> AI Confidence: **99.31%**
3861. **`drivers/hwmon/dell-smm-hwmon.c`** -> AI Confidence: **99.31%**
3862. **`drivers/hwmon/drivetemp.c`** -> AI Confidence: **99.31%**
3863. **`drivers/hwmon/emc1403.c`** -> AI Confidence: **99.31%**
3864. **`drivers/hwmon/emc2305.c`** -> AI Confidence: **99.31%**
3865. **`drivers/hwmon/f71882fg.c`** -> AI Confidence: **99.31%**
3866. **`drivers/hwmon/fschmd.c`** -> AI Confidence: **99.31%**
3867. **`drivers/hwmon/ftsteutates.c`** -> AI Confidence: **99.31%**
3868. **`drivers/hwmon/gigabyte_waterforce.c`** -> AI Confidence: **99.31%**
3869. **`drivers/hwmon/hp-wmi-sensors.c`** -> AI Confidence: **99.31%**
3870. **`drivers/hwmon/ina238.c`** -> AI Confidence: **99.31%**
3871. **`drivers/hwmon/ina3221.c`** -> AI Confidence: **99.31%**
3872. **`drivers/hwmon/it87.c`** -> AI Confidence: **99.31%**
3873. **`drivers/hwmon/jc42.c`** -> AI Confidence: **99.31%**
3874. **`drivers/hwmon/k8temp.c`** -> AI Confidence: **99.31%**
3875. **`drivers/hwmon/lineage-pem.c`** -> AI Confidence: **99.31%**
3876. **`drivers/hwmon/lm78.c`** -> AI Confidence: **99.31%**
3877. **`drivers/hwmon/lm83.c`** -> AI Confidence: **99.31%**
3878. **`drivers/hwmon/lm90.c`** -> AI Confidence: **99.31%**
3879. **`drivers/hwmon/lm92.c`** -> AI Confidence: **99.31%**
3880. **`drivers/hwmon/lm95234.c`** -> AI Confidence: **99.31%**
3881. **`drivers/hwmon/lm95241.c`** -> AI Confidence: **99.31%**
3882. **`drivers/hwmon/lm95245.c`** -> AI Confidence: **99.31%**
3883. **`drivers/hwmon/ltc2945.c`** -> AI Confidence: **99.31%**
3884. **`drivers/hwmon/ltc2947-core.c`** -> AI Confidence: **99.31%**
3885. **`drivers/hwmon/ltc2990.c`** -> AI Confidence: **99.31%**
3886. **`drivers/hwmon/ltc2991.c`** -> AI Confidence: **99.31%**
3887. **`drivers/hwmon/ltc2992.c`** -> AI Confidence: **99.31%**
3888. **`drivers/hwmon/ltc4245.c`** -> AI Confidence: **99.31%**
3889. **`drivers/hwmon/macsmc-hwmon.c`** -> AI Confidence: **99.31%**
3890. **`drivers/hwmon/max1619.c`** -> AI Confidence: **99.31%**
3891. **`drivers/hwmon/max31760.c`** -> AI Confidence: **99.31%**
3892. **`drivers/hwmon/max31790.c`** -> AI Confidence: **99.31%**
3893. **`drivers/hwmon/max31827.c`** -> AI Confidence: **99.31%**
3894. **`drivers/hwmon/max6620.c`** -> AI Confidence: **99.31%**
3895. **`drivers/hwmon/max6621.c`** -> AI Confidence: **99.31%**
3896. **`drivers/hwmon/max6650.c`** -> AI Confidence: **99.31%**
3897. **`drivers/hwmon/max6697.c`** -> AI Confidence: **99.31%**
3898. **`drivers/hwmon/max77705-hwmon.c`** -> AI Confidence: **99.31%**
3899. **`drivers/hwmon/mlxreg-fan.c`** -> AI Confidence: **99.31%**
3900. **`drivers/hwmon/nct6775-core.c`** -> AI Confidence: **99.31%**
3901. **`drivers/hwmon/nct6775-platform.c`** -> AI Confidence: **99.31%**
3902. **`drivers/hwmon/nzxt-kraken3.c`** -> AI Confidence: **99.31%**
3903. **`drivers/hwmon/nzxt-smart2.c`** -> AI Confidence: **99.31%**
3904. **`drivers/hwmon/occ/common.c`** -> AI Confidence: **99.31%**
3905. **`drivers/hwmon/occ/p8_i2c.c`** -> AI Confidence: **99.31%**
3906. **`drivers/hwmon/occ/p9_sbe.c`** -> AI Confidence: **99.31%**
3907. **`drivers/hwmon/occ/sysfs.c`** -> AI Confidence: **99.31%**
3908. **`drivers/hwmon/pc87427.c`** -> AI Confidence: **99.31%**
3909. **`drivers/hwmon/pmbus/adm1275.c`** -> AI Confidence: **99.31%**
3910. **`drivers/hwmon/pmbus/ibm-cffps.c`** -> AI Confidence: **99.31%**
3911. **`drivers/hwmon/pmbus/lt7182s.c`** -> AI Confidence: **99.31%**
3912. **`drivers/hwmon/pmbus/ltc4286.c`** -> AI Confidence: **99.31%**
3913. **`drivers/hwmon/pmbus/max20730.c`** -> AI Confidence: **99.31%**
3914. **`drivers/hwmon/pmbus/mp2856.c`** -> AI Confidence: **99.31%**
3915. **`drivers/hwmon/pmbus/mp2975.c`** -> AI Confidence: **99.31%**
3916. **`drivers/hwmon/pmbus/pim4328.c`** -> AI Confidence: **99.31%**
3917. **`drivers/hwmon/pmbus/pmbus.c`** -> AI Confidence: **99.31%**
3918. **`drivers/hwmon/pmbus/q54sj108a2.c`** -> AI Confidence: **99.31%**
3919. **`drivers/hwmon/pmbus/stpddc60.c`** -> AI Confidence: **99.31%**
3920. **`drivers/hwmon/pmbus/tps53679.c`** -> AI Confidence: **99.31%**
3921. **`drivers/hwmon/pmbus/ucd9000.c`** -> AI Confidence: **99.31%**
3922. **`drivers/hwmon/pmbus/ucd9200.c`** -> AI Confidence: **99.31%**
3923. **`drivers/hwmon/pmbus/xdpe12284.c`** -> AI Confidence: **99.31%**
3924. **`drivers/hwmon/pmbus/zl6100.c`** -> AI Confidence: **99.31%**
3925. **`drivers/hwmon/powerz.c`** -> AI Confidence: **99.31%**
3926. **`drivers/hwmon/powr1220.c`** -> AI Confidence: **99.31%**
3927. **`drivers/hwmon/sch5627.c`** -> AI Confidence: **99.31%**
3928. **`drivers/hwmon/sch5636.c`** -> AI Confidence: **99.31%**
3929. **`drivers/hwmon/sch56xx-common.c`** -> AI Confidence: **99.31%**
3930. **`drivers/hwmon/sht15.c`** -> AI Confidence: **99.31%**
3931. **`drivers/hwmon/sht3x.c`** -> AI Confidence: **99.31%**
3932. **`drivers/hwmon/sis5595.c`** -> AI Confidence: **99.31%**
3933. **`drivers/hwmon/smpro-hwmon.c`** -> AI Confidence: **99.31%**
3934. **`drivers/hwmon/spd5118.c`** -> AI Confidence: **99.31%**
3935. **`drivers/hwmon/tmp401.c`** -> AI Confidence: **99.31%**
3936. **`drivers/hwmon/tmp464.c`** -> AI Confidence: **99.31%**
3937. **`drivers/hwmon/tmp513.c`** -> AI Confidence: **99.31%**
3938. **`drivers/hwmon/tps23861.c`** -> AI Confidence: **99.31%**
3939. **`drivers/hwmon/tsc1641.c`** -> AI Confidence: **99.31%**
3940. **`drivers/hwmon/w83627ehf.c`** -> AI Confidence: **99.31%**
3941. **`drivers/hwmon/w83627hf.c`** -> AI Confidence: **99.31%**
3942. **`drivers/hwmon/w83781d.c`** -> AI Confidence: **99.31%**
3943. **`drivers/hwmon/w83793.c`** -> AI Confidence: **99.31%**
3944. **`drivers/hwtracing/coresight/coresight-tmc-etf.c`** -> AI Confidence: **99.31%**
3945. **`drivers/hwtracing/coresight/coresight-tpda.c`** -> AI Confidence: **99.31%**
3946. **`drivers/hwtracing/intel_th/sth.c`** -> AI Confidence: **99.31%**
3947. **`drivers/i2c/algos/i2c-algo-bit.c`** -> AI Confidence: **99.31%**
3948. **`drivers/i2c/algos/i2c-algo-pcf.c`** -> AI Confidence: **99.31%**
3949. **`drivers/i2c/busses/i2c-ali15x3.c`** -> AI Confidence: **99.31%**
3950. **`drivers/i2c/busses/i2c-amd756.c`** -> AI Confidence: **99.31%**
3951. **`drivers/i2c/busses/i2c-amd8111.c`** -> AI Confidence: **99.31%**
3952. **`drivers/i2c/busses/i2c-aspeed.c`** -> AI Confidence: **99.31%**
3953. **`drivers/i2c/busses/i2c-axxia.c`** -> AI Confidence: **99.31%**
3954. **`drivers/i2c/busses/i2c-bcm-kona.c`** -> AI Confidence: **99.31%**
3955. **`drivers/i2c/busses/i2c-brcmstb.c`** -> AI Confidence: **99.31%**
3956. **`drivers/i2c/busses/i2c-cadence.c`** -> AI Confidence: **99.31%**
3957. **`drivers/i2c/busses/i2c-davinci.c`** -> AI Confidence: **99.31%**
3958. **`drivers/i2c/busses/i2c-designware-master.c`** -> AI Confidence: **99.31%**
3959. **`drivers/i2c/busses/i2c-designware-slave.c`** -> AI Confidence: **99.31%**
3960. **`drivers/i2c/busses/i2c-diolan-u2c.c`** -> AI Confidence: **99.31%**
3961. **`drivers/i2c/busses/i2c-elektor.c`** -> AI Confidence: **99.31%**
3962. **`drivers/i2c/busses/i2c-exynos5.c`** -> AI Confidence: **99.31%**
3963. **`drivers/i2c/busses/i2c-i801.c`** -> AI Confidence: **99.31%**
3964. **`drivers/i2c/busses/i2c-ibm_iic.c`** -> AI Confidence: **99.31%**
3965. **`drivers/i2c/busses/i2c-img-scb.c`** -> AI Confidence: **99.31%**
3966. **`drivers/i2c/busses/i2c-isch.c`** -> AI Confidence: **99.31%**
3967. **`drivers/i2c/busses/i2c-ismt.c`** -> AI Confidence: **99.31%**
3968. **`drivers/i2c/busses/i2c-jz4780.c`** -> AI Confidence: **99.31%**
3969. **`drivers/i2c/busses/i2c-k1.c`** -> AI Confidence: **99.31%**
3970. **`drivers/i2c/busses/i2c-lpc2k.c`** -> AI Confidence: **99.31%**
3971. **`drivers/i2c/busses/i2c-mlxcpld.c`** -> AI Confidence: **99.31%**
3972. **`drivers/i2c/busses/i2c-mpc.c`** -> AI Confidence: **99.31%**
3973. **`drivers/i2c/busses/i2c-mt65xx.c`** -> AI Confidence: **99.31%**
3974. **`drivers/i2c/busses/i2c-mv64xxx.c`** -> AI Confidence: **99.31%**
3975. **`drivers/i2c/busses/i2c-mxs.c`** -> AI Confidence: **99.31%**
3976. **`drivers/i2c/busses/i2c-nforce2.c`** -> AI Confidence: **99.31%**
3977. **`drivers/i2c/busses/i2c-nomadik.c`** -> AI Confidence: **99.31%**
3978. **`drivers/i2c/busses/i2c-ocores.c`** -> AI Confidence: **99.31%**
3979. **`drivers/i2c/busses/i2c-octeon-core.c`** -> AI Confidence: **99.31%**
3980. **`drivers/i2c/busses/i2c-octeon-platdrv.c`** -> AI Confidence: **99.31%**
3981. **`drivers/i2c/busses/i2c-omap.c`** -> AI Confidence: **99.31%**
3982. **`drivers/i2c/busses/i2c-opal.c`** -> AI Confidence: **99.31%**
3983. **`drivers/i2c/busses/i2c-pasemi-core.c`** -> AI Confidence: **99.31%**
3984. **`drivers/i2c/busses/i2c-pca-isa.c`** -> AI Confidence: **99.31%**
3985. **`drivers/i2c/busses/i2c-powermac.c`** -> AI Confidence: **99.31%**
3986. **`drivers/i2c/busses/i2c-pxa.c`** -> AI Confidence: **99.31%**
3987. **`drivers/i2c/busses/i2c-qcom-geni.c`** -> AI Confidence: **99.31%**
3988. **`drivers/i2c/busses/i2c-qup.c`** -> AI Confidence: **99.31%**
3989. **`drivers/i2c/busses/i2c-s3c2410.c`** -> AI Confidence: **99.31%**
3990. **`drivers/i2c/busses/i2c-scmi.c`** -> AI Confidence: **99.31%**
3991. **`drivers/i2c/busses/i2c-sh7760.c`** -> AI Confidence: **99.31%**
3992. **`drivers/i2c/busses/i2c-sibyte.c`** -> AI Confidence: **99.31%**
3993. **`drivers/i2c/busses/i2c-sis5595.c`** -> AI Confidence: **99.31%**
3994. **`drivers/i2c/busses/i2c-sis630.c`** -> AI Confidence: **99.31%**
3995. **`drivers/i2c/busses/i2c-stm32f7.c`** -> AI Confidence: **99.31%**
3996. **`drivers/i2c/busses/i2c-sun6i-p2wi.c`** -> AI Confidence: **99.31%**
3997. **`drivers/i2c/busses/i2c-synquacer.c`** -> AI Confidence: **99.31%**
3998. **`drivers/i2c/busses/i2c-viperboard.c`** -> AI Confidence: **99.31%**
3999. **`drivers/i2c/busses/i2c-xiic.c`** -> AI Confidence: **99.31%**
4000. **`drivers/i2c/busses/i2c-xlp9xx.c`** -> AI Confidence: **99.31%**
4001. **`drivers/i2c/busses/scx200_acb.c`** -> AI Confidence: **99.31%**
4002. **`drivers/i2c/i2c-core-smbus.c`** -> AI Confidence: **99.31%**
4003. **`drivers/i2c/i2c-slave-testunit.c`** -> AI Confidence: **99.31%**
4004. **`drivers/i2c/i2c-smbus.c`** -> AI Confidence: **99.31%**
4005. **`drivers/i2c/i2c-stub.c`** -> AI Confidence: **99.31%**
4006. **`drivers/i2c/muxes/i2c-mux-reg.c`** -> AI Confidence: **99.31%**
4007. **`drivers/i3c/device.c`** -> AI Confidence: **99.31%**
4008. **`drivers/i3c/master/mipi-i3c-hci/dma.c`** -> AI Confidence: **99.31%**
4009. **`drivers/iio/accel/bma400_core.c`** -> AI Confidence: **99.31%**
4010. **`drivers/iio/accel/cros_ec_accel_legacy.c`** -> AI Confidence: **99.31%**
4011. **`drivers/iio/accel/sca3000.c`** -> AI Confidence: **99.31%**
4012. **`drivers/iio/accel/st_accel_core.c`** -> AI Confidence: **99.31%**
4013. **`drivers/iio/accel/stk8ba50.c`** -> AI Confidence: **99.31%**
4014. **`drivers/iio/adc/ab8500-gpadc.c`** -> AI Confidence: **99.31%**
4015. **`drivers/iio/adc/ad7280a.c`** -> AI Confidence: **99.31%**
4016. **`drivers/iio/adc/ad7291.c`** -> AI Confidence: **99.31%**
4017. **`drivers/iio/adc/ad799x.c`** -> AI Confidence: **99.31%**
4018. **`drivers/iio/adc/ad_sigma_delta.c`** -> AI Confidence: **99.31%**
4019. **`drivers/iio/adc/ade9000.c`** -> AI Confidence: **99.31%**
4020. **`drivers/iio/adc/cpcap-adc.c`** -> AI Confidence: **99.31%**
4021. **`drivers/iio/adc/ltc2497-core.c`** -> AI Confidence: **99.31%**
4022. **`drivers/iio/adc/mcp320x.c`** -> AI Confidence: **99.31%**
4023. **`drivers/iio/adc/mt6360-adc.c`** -> AI Confidence: **99.31%**
4024. **`drivers/iio/adc/mt6370-adc.c`** -> AI Confidence: **99.31%**
4025. **`drivers/iio/adc/nau7802.c`** -> AI Confidence: **99.31%**
4026. **`drivers/iio/adc/pac1934.c`** -> AI Confidence: **99.31%**
4027. **`drivers/iio/adc/qcom-pm8xxx-xoadc.c`** -> AI Confidence: **99.31%**
4028. **`drivers/iio/adc/qcom-spmi-rradc.c`** -> AI Confidence: **99.31%**
4029. **`drivers/iio/adc/sc27xx_adc.c`** -> AI Confidence: **99.31%**
4030. **`drivers/iio/adc/twl4030-madc.c`** -> AI Confidence: **99.31%**
4031. **`drivers/iio/adc/twl6030-gpadc.c`** -> AI Confidence: **99.31%**
4032. **`drivers/iio/adc/vf610_adc.c`** -> AI Confidence: **99.31%**
4033. **`drivers/iio/adc/xilinx-ams.c`** -> AI Confidence: **99.31%**
4034. **`drivers/iio/amplifiers/ad8366.c`** -> AI Confidence: **99.31%**
4035. **`drivers/iio/cdc/ad7150.c`** -> AI Confidence: **99.31%**
4036. **`drivers/iio/cdc/ad7746.c`** -> AI Confidence: **99.31%**
4037. **`drivers/iio/common/st_sensors/st_sensors_core.c`** -> AI Confidence: **99.31%**
4038. **`drivers/iio/common/st_sensors/st_sensors_trigger.c`** -> AI Confidence: **99.31%**
4039. **`drivers/iio/dac/ad5592r-base.c`** -> AI Confidence: **99.31%**
4040. **`drivers/iio/dac/ad7293.c`** -> AI Confidence: **99.31%**
4041. **`drivers/iio/dac/max517.c`** -> AI Confidence: **99.31%**
4042. **`drivers/iio/dummy/iio_simple_dummy.c`** -> AI Confidence: **99.31%**
4043. **`drivers/iio/frequency/ad9523.c`** -> AI Confidence: **99.31%**
4044. **`drivers/iio/frequency/adf4350.c`** -> AI Confidence: **99.31%**
4045. **`drivers/iio/frequency/adf4371.c`** -> AI Confidence: **99.31%**
4046. **`drivers/iio/gyro/adxrs450.c`** -> AI Confidence: **99.31%**
4047. **`drivers/iio/gyro/mpu3050-core.c`** -> AI Confidence: **99.31%**
4048. **`drivers/iio/humidity/dht11.c`** -> AI Confidence: **99.31%**
4049. **`drivers/iio/humidity/si7005.c`** -> AI Confidence: **99.31%**
4050. **`drivers/iio/imu/adis.c`** -> AI Confidence: **99.31%**
4051. **`drivers/iio/imu/adis_buffer.c`** -> AI Confidence: **99.31%**
4052. **`drivers/iio/imu/adis_trigger.c`** -> AI Confidence: **99.31%**
4053. **`drivers/iio/imu/bno055/bno055.c`** -> AI Confidence: **99.31%**
4054. **`drivers/iio/imu/bno055/bno055_ser_core.c`** -> AI Confidence: **99.31%**
4055. **`drivers/iio/imu/inv_icm42600/inv_icm42600_accel.c`** -> AI Confidence: **99.31%**
4056. **`drivers/iio/imu/inv_icm42600/inv_icm42600_buffer.c`** -> AI Confidence: **99.31%**
4057. **`drivers/iio/imu/inv_icm42600/inv_icm42600_core.c`** -> AI Confidence: **99.31%**
4058. **`drivers/iio/imu/inv_icm42600/inv_icm42600_gyro.c`** -> AI Confidence: **99.31%**
4059. **`drivers/iio/imu/inv_icm42600/inv_icm42600_temp.c`** -> AI Confidence: **99.31%**
4060. **`drivers/iio/imu/inv_mpu6050/inv_mpu_core.c`** -> AI Confidence: **99.31%**
4061. **`drivers/iio/imu/inv_mpu6050/inv_mpu_ring.c`** -> AI Confidence: **99.31%**
4062. **`drivers/iio/imu/st_lsm6dsx/st_lsm6dsx_buffer.c`** -> AI Confidence: **99.31%**
4063. **`drivers/iio/light/adux1020.c`** -> AI Confidence: **99.31%**
4064. **`drivers/iio/light/cm36651.c`** -> AI Confidence: **99.31%**
4065. **`drivers/iio/light/cros_ec_light_prox.c`** -> AI Confidence: **99.31%**
4066. **`drivers/iio/light/gp2ap020a00f.c`** -> AI Confidence: **99.31%**
4067. **`drivers/iio/light/hid-sensor-als.c`** -> AI Confidence: **99.31%**
4068. **`drivers/iio/light/iqs621-als.c`** -> AI Confidence: **99.31%**
4069. **`drivers/iio/light/lv0104cs.c`** -> AI Confidence: **99.31%**
4070. **`drivers/iio/light/tcs3472.c`** -> AI Confidence: **99.31%**
4071. **`drivers/iio/light/tsl2563.c`** -> AI Confidence: **99.31%**
4072. **`drivers/iio/light/tsl2583.c`** -> AI Confidence: **99.31%**
4073. **`drivers/iio/light/tsl2591.c`** -> AI Confidence: **99.31%**
4074. **`drivers/iio/light/tsl2772.c`** -> AI Confidence: **99.31%**
4075. **`drivers/iio/light/vcnl4000.c`** -> AI Confidence: **99.31%**
4076. **`drivers/iio/magnetometer/ak8974.c`** -> AI Confidence: **99.31%**
4077. **`drivers/iio/magnetometer/hid-sensor-magn-3d.c`** -> AI Confidence: **99.31%**
4078. **`drivers/iio/magnetometer/yamaha-yas530.c`** -> AI Confidence: **99.31%**
4079. **`drivers/iio/pressure/cros_ec_baro.c`** -> AI Confidence: **99.31%**
4080. **`drivers/iio/pressure/ms5611_core.c`** -> AI Confidence: **99.31%**
4081. **`drivers/iio/temperature/ltc2983.c`** -> AI Confidence: **99.31%**
4082. **`drivers/iio/temperature/mlx90632.c`** -> AI Confidence: **99.31%**
4083. **`drivers/infiniband/core/cm.c`** -> AI Confidence: **99.31%**
4084. **`drivers/infiniband/core/device.c`** -> AI Confidence: **99.31%**
4085. **`drivers/infiniband/core/mad.c`** -> AI Confidence: **99.31%**
4086. **`drivers/infiniband/core/nldev.c`** -> AI Confidence: **99.31%**
4087. **`drivers/infiniband/core/umem.c`** -> AI Confidence: **99.31%**
4088. **`drivers/infiniband/core/umem_odp.c`** -> AI Confidence: **99.31%**
4089. **`drivers/infiniband/hw/bnxt_re/debugfs.c`** -> AI Confidence: **99.31%**
4090. **`drivers/infiniband/hw/bnxt_re/ib_verbs.c`** -> AI Confidence: **99.31%**
4091. **`drivers/infiniband/hw/bnxt_re/qplib_res.c`** -> AI Confidence: **99.31%**
4092. **`drivers/infiniband/hw/cxgb4/cm.c`** -> AI Confidence: **99.31%**
4093. **`drivers/infiniband/hw/hfi1/affinity.c`** -> AI Confidence: **99.31%**
4094. **`drivers/infiniband/hw/hfi1/driver.c`** -> AI Confidence: **99.31%**
4095. **`drivers/infiniband/hw/hfi1/init.c`** -> AI Confidence: **99.31%**
4096. **`drivers/infiniband/hw/hfi1/mad.c`** -> AI Confidence: **99.31%**
4097. **`drivers/infiniband/hw/hfi1/ud.c`** -> AI Confidence: **99.31%**
4098. **`drivers/infiniband/hw/hfi1/user_sdma.c`** -> AI Confidence: **99.31%**
4099. **`drivers/infiniband/hw/hns/hns_roce_main.c`** -> AI Confidence: **99.31%**
4100. **`drivers/infiniband/hw/hns/hns_roce_mr.c`** -> AI Confidence: **99.31%**
4101. **`drivers/infiniband/hw/ionic/ionic_controlpath.c`** -> AI Confidence: **99.31%**
4102. **`drivers/infiniband/hw/irdma/ctrl.c`** -> AI Confidence: **99.31%**
4103. **`drivers/infiniband/hw/mlx4/alias_GUID.c`** -> AI Confidence: **99.31%**
4104. **`drivers/infiniband/hw/mlx4/cq.c`** -> AI Confidence: **99.31%**
4105. **`drivers/infiniband/hw/mlx4/mad.c`** -> AI Confidence: **99.31%**
4106. **`drivers/infiniband/hw/mlx4/main.c`** -> AI Confidence: **99.31%**
4107. **`drivers/infiniband/hw/mlx4/qp.c`** -> AI Confidence: **99.31%**
4108. **`drivers/infiniband/hw/mlx5/cq.c`** -> AI Confidence: **99.31%**
4109. **`drivers/infiniband/hw/mlx5/devx.c`** -> AI Confidence: **99.31%**
4110. **`drivers/infiniband/hw/mlx5/fs.c`** -> AI Confidence: **99.31%**
4111. **`drivers/infiniband/hw/mlx5/qp.c`** -> AI Confidence: **99.31%**
4112. **`drivers/infiniband/hw/mthca/mthca_cmd.c`** -> AI Confidence: **99.31%**
4113. **`drivers/infiniband/hw/mthca/mthca_cq.c`** -> AI Confidence: **99.31%**
4114. **`drivers/infiniband/hw/mthca/mthca_eq.c`** -> AI Confidence: **99.31%**
4115. **`drivers/infiniband/hw/mthca/mthca_mad.c`** -> AI Confidence: **99.31%**
4116. **`drivers/infiniband/hw/mthca/mthca_main.c`** -> AI Confidence: **99.31%**
4117. **`drivers/infiniband/hw/mthca/mthca_memfree.c`** -> AI Confidence: **99.31%**
4118. **`drivers/infiniband/hw/mthca/mthca_qp.c`** -> AI Confidence: **99.31%**
4119. **`drivers/infiniband/hw/qedr/main.c`** -> AI Confidence: **99.31%**
4120. **`drivers/infiniband/hw/usnic/usnic_ib_qp_grp.c`** -> AI Confidence: **99.31%**
4121. **`drivers/infiniband/hw/vmw_pvrdma/pvrdma_main.c`** -> AI Confidence: **99.31%**
4122. **`drivers/infiniband/sw/rdmavt/qp.c`** -> AI Confidence: **99.31%**
4123. **`drivers/infiniband/sw/rdmavt/srq.c`** -> AI Confidence: **99.31%**
4124. **`drivers/infiniband/sw/rxe/rxe_qp.c`** -> AI Confidence: **99.31%**
4125. **`drivers/infiniband/sw/siw/siw_cm.c`** -> AI Confidence: **99.31%**
4126. **`drivers/infiniband/sw/siw/siw_mem.c`** -> AI Confidence: **99.31%**
4127. **`drivers/infiniband/sw/siw/siw_qp.c`** -> AI Confidence: **99.31%**
4128. **`drivers/infiniband/sw/siw/siw_qp_rx.c`** -> AI Confidence: **99.31%**
4129. **`drivers/infiniband/sw/siw/siw_qp_tx.c`** -> AI Confidence: **99.31%**
4130. **`drivers/infiniband/sw/siw/siw_verbs.c`** -> AI Confidence: **99.31%**
4131. **`drivers/infiniband/ulp/iser/iscsi_iser.c`** -> AI Confidence: **99.31%**
4132. **`drivers/infiniband/ulp/srpt/ib_srpt.c`** -> AI Confidence: **99.31%**
4133. **`drivers/input/ff-core.c`** -> AI Confidence: **99.31%**
4134. **`drivers/input/ff-memless.c`** -> AI Confidence: **99.31%**
4135. **`drivers/input/gameport/lightning.c`** -> AI Confidence: **99.31%**
4136. **`drivers/input/input.c`** -> AI Confidence: **99.31%**
4137. **`drivers/input/joystick/adi.c`** -> AI Confidence: **99.31%**
4138. **`drivers/input/joystick/amijoy.c`** -> AI Confidence: **99.31%**
4139. **`drivers/input/joystick/analog.c`** -> AI Confidence: **99.31%**
4140. **`drivers/input/joystick/fsia6b.c`** -> AI Confidence: **99.31%**
4141. **`drivers/input/joystick/gamecon.c`** -> AI Confidence: **99.31%**
4142. **`drivers/input/joystick/gf2k.c`** -> AI Confidence: **99.31%**
4143. **`drivers/input/joystick/grip_mp.c`** -> AI Confidence: **99.31%**
4144. **`drivers/input/joystick/guillemot.c`** -> AI Confidence: **99.31%**
4145. **`drivers/input/joystick/interact.c`** -> AI Confidence: **99.31%**
4146. **`drivers/input/joystick/tmdc.c`** -> AI Confidence: **99.31%**
4147. **`drivers/input/joystick/turbografx.c`** -> AI Confidence: **99.31%**
4148. **`drivers/input/keyboard/amikbd.c`** -> AI Confidence: **99.31%**
4149. **`drivers/input/keyboard/gpio_keys_polled.c`** -> AI Confidence: **99.31%**
4150. **`drivers/input/keyboard/hilkbd.c`** -> AI Confidence: **99.31%**
4151. **`drivers/input/keyboard/iqs62x-keys.c`** -> AI Confidence: **99.31%**
4152. **`drivers/input/keyboard/lkkbd.c`** -> AI Confidence: **99.31%**
4153. **`drivers/input/keyboard/lm8333.c`** -> AI Confidence: **99.31%**
4154. **`drivers/input/keyboard/omap-keypad.c`** -> AI Confidence: **99.31%**
4155. **`drivers/input/keyboard/pmic8xxx-keypad.c`** -> AI Confidence: **99.31%**
4156. **`drivers/input/keyboard/sh_keysc.c`** -> AI Confidence: **99.31%**
4157. **`drivers/input/keyboard/sunkbd.c`** -> AI Confidence: **99.31%**
4158. **`drivers/input/keyboard/twl4030_keypad.c`** -> AI Confidence: **99.31%**
4159. **`drivers/input/matrix-keymap.c`** -> AI Confidence: **99.31%**
4160. **`drivers/input/misc/ad714x.c`** -> AI Confidence: **99.31%**
4161. **`drivers/input/misc/cm109.c`** -> AI Confidence: **99.31%**
4162. **`drivers/input/misc/da7280.c`** -> AI Confidence: **99.31%**
4163. **`drivers/input/misc/ibm-panel.c`** -> AI Confidence: **99.31%**
4164. **`drivers/input/misc/iqs269a.c`** -> AI Confidence: **99.31%**
4165. **`drivers/input/misc/iqs626a.c`** -> AI Confidence: **99.31%**
4166. **`drivers/input/misc/iqs7222.c`** -> AI Confidence: **99.31%**
4167. **`drivers/input/misc/max8997_haptic.c`** -> AI Confidence: **99.31%**
4168. **`drivers/input/misc/mc13783-pwrbutton.c`** -> AI Confidence: **99.31%**
4169. **`drivers/input/misc/pf1550-onkey.c`** -> AI Confidence: **99.31%**
4170. **`drivers/input/misc/rotary_encoder.c`** -> AI Confidence: **99.31%**
4171. **`drivers/input/misc/uinput.c`** -> AI Confidence: **99.31%**
4172. **`drivers/input/misc/wistron_btns.c`** -> AI Confidence: **99.31%**
4173. **`drivers/input/misc/xen-kbdfront.c`** -> AI Confidence: **99.31%**
4174. **`drivers/input/misc/yealink.c`** -> AI Confidence: **99.31%**
4175. **`drivers/input/mouse/alps.c`** -> AI Confidence: **99.31%**
4176. **`drivers/input/mouse/cyapa.c`** -> AI Confidence: **99.31%**
4177. **`drivers/input/mouse/cyapa_gen5.c`** -> AI Confidence: **99.31%**
4178. **`drivers/input/mouse/cyapa_gen6.c`** -> AI Confidence: **99.31%**
4179. **`drivers/input/mouse/cypress_ps2.c`** -> AI Confidence: **99.31%**
4180. **`drivers/input/mouse/elantech.c`** -> AI Confidence: **99.31%**
4181. **`drivers/input/mouse/hgpk.c`** -> AI Confidence: **99.31%**
4182. **`drivers/input/mouse/logips2pp.c`** -> AI Confidence: **99.31%**
4183. **`drivers/input/mouse/pc110pad.c`** -> AI Confidence: **99.31%**
4184. **`drivers/input/mouse/psmouse-base.c`** -> AI Confidence: **99.31%**
4185. **`drivers/input/mouse/sentelic.c`** -> AI Confidence: **99.31%**
4186. **`drivers/input/mouse/synaptics.c`** -> AI Confidence: **99.31%**
4187. **`drivers/input/mouse/synaptics_usb.c`** -> AI Confidence: **99.31%**
4188. **`drivers/input/mousedev.c`** -> AI Confidence: **99.31%**
4189. **`drivers/input/rmi4/rmi_2d_sensor.c`** -> AI Confidence: **99.31%**
4190. **`drivers/input/rmi4/rmi_f34v7.c`** -> AI Confidence: **99.31%**
4191. **`drivers/input/serio/pcips2.c`** -> AI Confidence: **99.31%**
4192. **`drivers/input/tablet/wacom_serial4.c`** -> AI Confidence: **99.31%**
4193. **`drivers/input/touchscreen/88pm860x-ts.c`** -> AI Confidence: **99.31%**
4194. **`drivers/input/touchscreen/atmel_mxt_ts.c`** -> AI Confidence: **99.31%**
4195. **`drivers/input/touchscreen/goodix.c`** -> AI Confidence: **99.31%**
4196. **`drivers/input/touchscreen/hycon-hy46xx.c`** -> AI Confidence: **99.31%**
4197. **`drivers/input/touchscreen/iqs5xx.c`** -> AI Confidence: **99.31%**
4198. **`drivers/input/touchscreen/iqs7211.c`** -> AI Confidence: **99.31%**
4199. **`drivers/input/touchscreen/mainstone-wm97xx.c`** -> AI Confidence: **99.31%**
4200. **`drivers/input/touchscreen/melfas_mip4.c`** -> AI Confidence: **99.31%**
4201. **`drivers/input/touchscreen/mk712.c`** -> AI Confidence: **99.31%**
4202. **`drivers/input/touchscreen/rohm_bu21023.c`** -> AI Confidence: **99.31%**
4203. **`drivers/input/touchscreen/sis_i2c.c`** -> AI Confidence: **99.31%**
4204. **`drivers/input/touchscreen/ti_am335x_tsc.c`** -> AI Confidence: **99.31%**
4205. **`drivers/input/touchscreen/tps6507x-ts.c`** -> AI Confidence: **99.31%**
4206. **`drivers/input/touchscreen/wacom_w8001.c`** -> AI Confidence: **99.31%**
4207. **`drivers/input/touchscreen/wm831x-ts.c`** -> AI Confidence: **99.31%**
4208. **`drivers/input/touchscreen/wm9705.c`** -> AI Confidence: **99.31%**
4209. **`drivers/input/touchscreen/wm9712.c`** -> AI Confidence: **99.31%**
4210. **`drivers/input/touchscreen/wm9713.c`** -> AI Confidence: **99.31%**
4211. **`drivers/input/touchscreen/wm97xx-core.c`** -> AI Confidence: **99.31%**
4212. **`drivers/input/touchscreen/zforce_ts.c`** -> AI Confidence: **99.31%**
4213. **`drivers/interconnect/qcom/icc-rpm.c`** -> AI Confidence: **99.31%**
4214. **`drivers/interconnect/qcom/icc-rpmh.c`** -> AI Confidence: **99.31%**
4215. **`drivers/iommu/arm/arm-smmu/arm-smmu-qcom-debug.c`** -> AI Confidence: **99.31%**
4216. **`drivers/iommu/arm/arm-smmu/arm-smmu.c`** -> AI Confidence: **99.31%**
4217. **`drivers/iommu/fsl_pamu.c`** -> AI Confidence: **99.31%**
4218. **`drivers/iommu/intel/dmar.c`** -> AI Confidence: **99.31%**
4219. **`drivers/iommu/io-pgtable-arm-v7s.c`** -> AI Confidence: **99.31%**
4220. **`drivers/iommu/io-pgtable-arm.c`** -> AI Confidence: **99.31%**
4221. **`drivers/iommu/iommufd/io_pagetable.c`** -> AI Confidence: **99.31%**
4222. **`drivers/iommu/iommufd/pages.c`** -> AI Confidence: **99.31%**
4223. **`drivers/iommu/irq_remapping.c`** -> AI Confidence: **99.31%**
4224. **`drivers/iommu/mtk_iommu.c`** -> AI Confidence: **99.31%**
4225. **`drivers/iommu/riscv/iommu-platform.c`** -> AI Confidence: **99.31%**
4226. **`drivers/ipack/devices/ipoctal.c`** -> AI Confidence: **99.31%**
4227. **`drivers/irqchip/irq-apple-aic.c`** -> AI Confidence: **99.31%**
4228. **`drivers/irqchip/irq-crossbar.c`** -> AI Confidence: **99.31%**
4229. **`drivers/irqchip/irq-econet-en751221.c`** -> AI Confidence: **99.31%**
4230. **`drivers/irqchip/irq-gic-v5-irs.c`** -> AI Confidence: **99.31%**
4231. **`drivers/irqchip/irq-gic.c`** -> AI Confidence: **99.31%**
4232. **`drivers/irqchip/irq-mchp-eic.c`** -> AI Confidence: **99.31%**
4233. **`drivers/irqchip/irq-mips-gic.c`** -> AI Confidence: **99.31%**
4234. **`drivers/irqchip/irq-mtk-sysirq.c`** -> AI Confidence: **99.31%**
4235. **`drivers/irqchip/irq-qcom-mpm.c`** -> AI Confidence: **99.31%**
4236. **`drivers/irqchip/irq-sifive-plic.c`** -> AI Confidence: **99.31%**
4237. **`drivers/irqchip/irq-tb10x.c`** -> AI Confidence: **99.31%**
4238. **`drivers/irqchip/qcom-pdc.c`** -> AI Confidence: **99.31%**
4239. **`drivers/isdn/capi/capiutil.c`** -> AI Confidence: **99.31%**
4240. **`drivers/isdn/capi/kcapi.c`** -> AI Confidence: **99.31%**
4241. **`drivers/isdn/hardware/mISDN/avmfritz.c`** -> AI Confidence: **99.31%**
4242. **`drivers/isdn/hardware/mISDN/hfcpci.c`** -> AI Confidence: **99.31%**
4243. **`drivers/isdn/hardware/mISDN/mISDNinfineon.c`** -> AI Confidence: **99.31%**
4244. **`drivers/isdn/hardware/mISDN/netjet.c`** -> AI Confidence: **99.31%**
4245. **`drivers/isdn/hardware/mISDN/speedfax.c`** -> AI Confidence: **99.31%**
4246. **`drivers/isdn/hardware/mISDN/w6692.c`** -> AI Confidence: **99.31%**
4247. **`drivers/isdn/mISDN/clock.c`** -> AI Confidence: **99.31%**
4248. **`drivers/isdn/mISDN/dsp_hwec.c`** -> AI Confidence: **99.31%**
4249. **`drivers/isdn/mISDN/l1oip_core.c`** -> AI Confidence: **99.31%**
4250. **`drivers/isdn/mISDN/stack.c`** -> AI Confidence: **99.31%**
4251. **`drivers/leds/flash/leds-mt6360.c`** -> AI Confidence: **99.31%**
4252. **`drivers/leds/flash/leds-qcom-flash.c`** -> AI Confidence: **99.31%**
4253. **`drivers/leds/led-core.c`** -> AI Confidence: **99.31%**
4254. **`drivers/leds/leds-88pm860x.c`** -> AI Confidence: **99.31%**
4255. **`drivers/leds/leds-aw2013.c`** -> AI Confidence: **99.31%**
4256. **`drivers/leds/leds-bcm6358.c`** -> AI Confidence: **99.31%**
4257. **`drivers/leds/leds-cht-wcove.c`** -> AI Confidence: **99.31%**
4258. **`drivers/leds/leds-clevo-mail.c`** -> AI Confidence: **99.31%**
4259. **`drivers/leds/leds-is31fl319x.c`** -> AI Confidence: **99.31%**
4260. **`drivers/leds/leds-lm3532.c`** -> AI Confidence: **99.31%**
4261. **`drivers/leds/leds-lm355x.c`** -> AI Confidence: **99.31%**
4262. **`drivers/leds/leds-lm3692x.c`** -> AI Confidence: **99.31%**
4263. **`drivers/leds/leds-lp5569.c`** -> AI Confidence: **99.31%**
4264. **`drivers/leds/leds-max8997.c`** -> AI Confidence: **99.31%**
4265. **`drivers/leds/leds-mc13783.c`** -> AI Confidence: **99.31%**
4266. **`drivers/leds/leds-netxbig.c`** -> AI Confidence: **99.31%**
4267. **`drivers/leds/leds-tca6507.c`** -> AI Confidence: **99.31%**
4268. **`drivers/leds/leds-wm831x-status.c`** -> AI Confidence: **99.31%**
4269. **`drivers/leds/rgb/leds-mt6370-rgb.c`** -> AI Confidence: **99.31%**
4270. **`drivers/leds/simatic/simatic-ipc-leds-gpio-core.c`** -> AI Confidence: **99.31%**
4271. **`drivers/leds/trigger/ledtrig-netdev.c`** -> AI Confidence: **99.31%**
4272. **`drivers/leds/trigger/ledtrig-tty.c`** -> AI Confidence: **99.31%**
4273. **`drivers/macintosh/adb.c`** -> AI Confidence: **99.31%**
4274. **`drivers/macintosh/ans-lcd.c`** -> AI Confidence: **99.31%**
4275. **`drivers/macintosh/therm_windtunnel.c`** -> AI Confidence: **99.31%**
4276. **`drivers/macintosh/via-macii.c`** -> AI Confidence: **99.31%**
4277. **`drivers/macintosh/via-pmu-backlight.c`** -> AI Confidence: **99.31%**
4278. **`drivers/macintosh/via-pmu-led.c`** -> AI Confidence: **99.31%**
4279. **`drivers/macintosh/windfarm_fcu_controls.c`** -> AI Confidence: **99.31%**
4280. **`drivers/macintosh/windfarm_lm75_sensor.c`** -> AI Confidence: **99.31%**
4281. **`drivers/macintosh/windfarm_pm112.c`** -> AI Confidence: **99.31%**
4282. **`drivers/macintosh/windfarm_pm121.c`** -> AI Confidence: **99.31%**
4283. **`drivers/macintosh/windfarm_pm72.c`** -> AI Confidence: **99.31%**
4284. **`drivers/macintosh/windfarm_pm81.c`** -> AI Confidence: **99.31%**
4285. **`drivers/macintosh/windfarm_rm31.c`** -> AI Confidence: **99.31%**
4286. **`drivers/macintosh/windfarm_smu_controls.c`** -> AI Confidence: **99.31%**
4287. **`drivers/macintosh/windfarm_smu_sat.c`** -> AI Confidence: **99.31%**
4288. **`drivers/macintosh/windfarm_smu_sensors.c`** -> AI Confidence: **99.31%**
4289. **`drivers/mailbox/bcm-flexrm-mailbox.c`** -> AI Confidence: **99.31%**
4290. **`drivers/mailbox/cix-mailbox.c`** -> AI Confidence: **99.31%**
4291. **`drivers/mcb/mcb-parse.c`** -> AI Confidence: **99.31%**
4292. **`drivers/md/bcache/super.c`** -> AI Confidence: **99.31%**
4293. **`drivers/md/bcache/sysfs.c`** -> AI Confidence: **99.31%**
4294. **`drivers/md/bcache/util.c`** -> AI Confidence: **99.31%**
4295. **`drivers/md/bcache/util.h`** -> AI Confidence: **99.31%**
4296. **`drivers/md/bcache/writeback.c`** -> AI Confidence: **99.31%**
4297. **`drivers/md/dm-exception-store.c`** -> AI Confidence: **99.31%**
4298. **`drivers/md/dm-ima.c`** -> AI Confidence: **99.31%**
4299. **`drivers/md/dm-init.c`** -> AI Confidence: **99.31%**
4300. **`drivers/md/dm-log-userspace-base.c`** -> AI Confidence: **99.31%**
4301. **`drivers/md/dm-mpath.c`** -> AI Confidence: **99.31%**
4302. **`drivers/md/dm-raid.c`** -> AI Confidence: **99.31%**
4303. **`drivers/md/dm-snap-persistent.c`** -> AI Confidence: **99.31%**
4304. **`drivers/md/dm-snap.c`** -> AI Confidence: **99.31%**
4305. **`drivers/md/dm-stats.c`** -> AI Confidence: **99.31%**
4306. **`drivers/md/dm-vdo/dm-vdo-target.c`** -> AI Confidence: **99.31%**
4307. **`drivers/md/dm-vdo/dump.c`** -> AI Confidence: **99.31%**
4308. **`drivers/md/dm-vdo/indexer/sparse-cache.c`** -> AI Confidence: **99.31%**
4309. **`drivers/md/dm-vdo/logger.c`** -> AI Confidence: **99.31%**
4310. **`drivers/md/dm-verity-target.c`** -> AI Confidence: **99.31%**
4311. **`drivers/md/dm-writecache.c`** -> AI Confidence: **99.31%**
4312. **`drivers/md/md-bitmap.c`** -> AI Confidence: **99.31%**
4313. **`drivers/md/md.c`** -> AI Confidence: **99.31%**
4314. **`drivers/md/raid1.c`** -> AI Confidence: **99.31%**
4315. **`drivers/md/raid10.c`** -> AI Confidence: **99.31%**
4316. **`drivers/md/raid5-ppl.c`** -> AI Confidence: **99.31%**
4317. **`drivers/md/raid5.c`** -> AI Confidence: **99.31%**
4318. **`drivers/media/cec/core/cec-adap.c`** -> AI Confidence: **99.31%**
4319. **`drivers/media/cec/core/cec-api.c`** -> AI Confidence: **99.31%**
4320. **`drivers/media/cec/i2c/ch7322.c`** -> AI Confidence: **99.31%**
4321. **`drivers/media/cec/platform/meson/ao-cec.c`** -> AI Confidence: **99.31%**
4322. **`drivers/media/cec/platform/s5p/s5p_cec.c`** -> AI Confidence: **99.31%**
4323. **`drivers/media/cec/platform/seco/seco-cec.c`** -> AI Confidence: **99.31%**
4324. **`drivers/media/cec/usb/extron-da-hd-4k-plus/extron-da-hd-4k-plus.c`** -> AI Confidence: **99.31%**
4325. **`drivers/media/cec/usb/pulse8/pulse8-cec.c`** -> AI Confidence: **99.31%**
4326. **`drivers/media/cec/usb/rainshadow/rainshadow-cec.c`** -> AI Confidence: **99.31%**
4327. **`drivers/media/common/b2c2/flexcop-fe-tuner.c`** -> AI Confidence: **99.31%**
4328. **`drivers/media/common/siano/smscoreapi.c`** -> AI Confidence: **99.31%**
4329. **`drivers/media/common/siano/smsdvb-main.c`** -> AI Confidence: **99.31%**
4330. **`drivers/media/common/ttpci-eeprom.c`** -> AI Confidence: **99.31%**
4331. **`drivers/media/common/videobuf2/videobuf2-core.c`** -> AI Confidence: **99.31%**
4332. **`drivers/media/common/videobuf2/videobuf2-v4l2.c`** -> AI Confidence: **99.31%**
4333. **`drivers/media/dvb-core/dmxdev.c`** -> AI Confidence: **99.31%**
4334. **`drivers/media/dvb-core/dvb_ca_en50221.c`** -> AI Confidence: **99.31%**
4335. **`drivers/media/dvb-core/dvb_net.c`** -> AI Confidence: **99.31%**
4336. **`drivers/media/dvb-core/dvbdev.c`** -> AI Confidence: **99.31%**
4337. **`drivers/media/dvb-frontends/au8522_decoder.c`** -> AI Confidence: **99.31%**
4338. **`drivers/media/dvb-frontends/au8522_dig.c`** -> AI Confidence: **99.31%**
4339. **`drivers/media/dvb-frontends/bcm3510.c`** -> AI Confidence: **99.31%**
4340. **`drivers/media/dvb-frontends/cx22702.c`** -> AI Confidence: **99.31%**
4341. **`drivers/media/dvb-frontends/cx24116.c`** -> AI Confidence: **99.31%**
4342. **`drivers/media/dvb-frontends/cx24123.c`** -> AI Confidence: **99.31%**
4343. **`drivers/media/dvb-frontends/cxd2099.c`** -> AI Confidence: **99.31%**
4344. **`drivers/media/dvb-frontends/cxd2841er.c`** -> AI Confidence: **99.31%**
4345. **`drivers/media/dvb-frontends/cxd2880/cxd2880_top.c`** -> AI Confidence: **99.31%**
4346. **`drivers/media/dvb-frontends/dib0070.c`** -> AI Confidence: **99.31%**
4347. **`drivers/media/dvb-frontends/dib3000mb.c`** -> AI Confidence: **99.31%**
4348. **`drivers/media/dvb-frontends/dib7000p.c`** -> AI Confidence: **99.31%**
4349. **`drivers/media/dvb-frontends/ds3000.c`** -> AI Confidence: **99.31%**
4350. **`drivers/media/dvb-frontends/isl6405.c`** -> AI Confidence: **99.31%**
4351. **`drivers/media/dvb-frontends/isl6421.c`** -> AI Confidence: **99.31%**
4352. **`drivers/media/dvb-frontends/isl6423.c`** -> AI Confidence: **99.31%**
4353. **`drivers/media/dvb-frontends/l64781.c`** -> AI Confidence: **99.31%**
4354. **`drivers/media/dvb-frontends/lgdt330x.c`** -> AI Confidence: **99.31%**
4355. **`drivers/media/dvb-frontends/m88rs2000.c`** -> AI Confidence: **99.31%**
4356. **`drivers/media/dvb-frontends/mt352.c`** -> AI Confidence: **99.31%**
4357. **`drivers/media/dvb-frontends/mxl5xx.c`** -> AI Confidence: **99.31%**
4358. **`drivers/media/dvb-frontends/nxt200x.c`** -> AI Confidence: **99.31%**
4359. **`drivers/media/dvb-frontends/nxt6000.c`** -> AI Confidence: **99.31%**
4360. **`drivers/media/dvb-frontends/or51132.c`** -> AI Confidence: **99.31%**
4361. **`drivers/media/dvb-frontends/rtl2832_sdr.c`** -> AI Confidence: **99.31%**
4362. **`drivers/media/dvb-frontends/s5h1409.c`** -> AI Confidence: **99.31%**
4363. **`drivers/media/dvb-frontends/s5h1411.c`** -> AI Confidence: **99.31%**
4364. **`drivers/media/dvb-frontends/s5h1420.c`** -> AI Confidence: **99.31%**
4365. **`drivers/media/dvb-frontends/si2165.c`** -> AI Confidence: **99.31%**
4366. **`drivers/media/dvb-frontends/sp887x.c`** -> AI Confidence: **99.31%**
4367. **`drivers/media/dvb-frontends/stb0899_drv.c`** -> AI Confidence: **99.31%**
4368. **`drivers/media/dvb-frontends/stv0297.c`** -> AI Confidence: **99.31%**
4369. **`drivers/media/dvb-frontends/stv0367.c`** -> AI Confidence: **99.31%**
4370. **`drivers/media/dvb-frontends/stv0900_core.c`** -> AI Confidence: **99.31%**
4371. **`drivers/media/dvb-frontends/stv0910.c`** -> AI Confidence: **99.31%**
4372. **`drivers/media/dvb-frontends/stv6111.c`** -> AI Confidence: **99.31%**
4373. **`drivers/media/dvb-frontends/tda10021.c`** -> AI Confidence: **99.31%**
4374. **`drivers/media/dvb-frontends/tda10023.c`** -> AI Confidence: **99.31%**
4375. **`drivers/media/dvb-frontends/tda1004x.c`** -> AI Confidence: **99.31%**
4376. **`drivers/media/dvb-frontends/tda10086.c`** -> AI Confidence: **99.31%**
4377. **`drivers/media/dvb-frontends/zl10353.c`** -> AI Confidence: **99.31%**
4378. **`drivers/media/firewire/firedtv-avc.c`** -> AI Confidence: **99.31%**
4379. **`drivers/media/firewire/firedtv-rc.c`** -> AI Confidence: **99.31%**
4380. **`drivers/media/i2c/adv7175.c`** -> AI Confidence: **99.31%**
4381. **`drivers/media/i2c/adv7183.c`** -> AI Confidence: **99.31%**
4382. **`drivers/media/i2c/adv7343.c`** -> AI Confidence: **99.31%**
4383. **`drivers/media/i2c/ccs/ccs-core.c`** -> AI Confidence: **99.31%**
4384. **`drivers/media/i2c/ds90ub960.c`** -> AI Confidence: **99.31%**
4385. **`drivers/media/i2c/gc0308.c`** -> AI Confidence: **99.31%**
4386. **`drivers/media/i2c/imx219.c`** -> AI Confidence: **99.31%**
4387. **`drivers/media/i2c/imx415.c`** -> AI Confidence: **99.31%**
4388. **`drivers/media/i2c/ir-kbd-i2c.c`** -> AI Confidence: **99.31%**
4389. **`drivers/media/i2c/ks0127.c`** -> AI Confidence: **99.31%**
4390. **`drivers/media/i2c/msp3400-driver.c`** -> AI Confidence: **99.31%**
4391. **`drivers/media/i2c/ov5647.c`** -> AI Confidence: **99.31%**
4392. **`drivers/media/i2c/ov772x.c`** -> AI Confidence: **99.31%**
4393. **`drivers/media/i2c/ov9640.c`** -> AI Confidence: **99.31%**
4394. **`drivers/media/i2c/rj54n1cb0c.c`** -> AI Confidence: **99.31%**
4395. **`drivers/media/i2c/s5c73m3/s5c73m3-ctrls.c`** -> AI Confidence: **99.31%**
4396. **`drivers/media/i2c/saa6588.c`** -> AI Confidence: **99.31%**
4397. **`drivers/media/i2c/saa6752hs.c`** -> AI Confidence: **99.31%**
4398. **`drivers/media/i2c/saa7115.c`** -> AI Confidence: **99.31%**
4399. **`drivers/media/i2c/saa717x.c`** -> AI Confidence: **99.31%**
4400. **`drivers/media/i2c/tda1997x.c`** -> AI Confidence: **99.31%**
4401. **`drivers/media/i2c/tvaudio.c`** -> AI Confidence: **99.31%**
4402. **`drivers/media/i2c/tvp5150.c`** -> AI Confidence: **99.31%**
4403. **`drivers/media/i2c/vd56g3.c`** -> AI Confidence: **99.31%**
4404. **`drivers/media/mmc/siano/smssdio.c`** -> AI Confidence: **99.31%**
4405. **`drivers/media/pci/bt8xx/bt878.c`** -> AI Confidence: **99.31%**
4406. **`drivers/media/pci/bt8xx/btcx-risc.c`** -> AI Confidence: **99.31%**
4407. **`drivers/media/pci/bt8xx/bttv-driver.c`** -> AI Confidence: **99.31%**
4408. **`drivers/media/pci/bt8xx/bttv-i2c.c`** -> AI Confidence: **99.31%**
4409. **`drivers/media/pci/bt8xx/bttv-risc.c`** -> AI Confidence: **99.31%**
4410. **`drivers/media/pci/bt8xx/dst.c`** -> AI Confidence: **99.31%**
4411. **`drivers/media/pci/bt8xx/dst_ca.c`** -> AI Confidence: **99.31%**
4412. **`drivers/media/pci/bt8xx/dvb-bt8xx.c`** -> AI Confidence: **99.31%**
4413. **`drivers/media/pci/cobalt/cobalt-driver.c`** -> AI Confidence: **99.31%**
4414. **`drivers/media/pci/cx18/cx18-dvb.c`** -> AI Confidence: **99.31%**
4415. **`drivers/media/pci/cx18/cx18-fileops.c`** -> AI Confidence: **99.31%**
4416. **`drivers/media/pci/cx18/cx18-firmware.c`** -> AI Confidence: **99.31%**
4417. **`drivers/media/pci/cx18/cx18-mailbox.c`** -> AI Confidence: **99.31%**
4418. **`drivers/media/pci/cx18/cx18-streams.c`** -> AI Confidence: **99.31%**
4419. **`drivers/media/pci/cx23885/cx23885-core.c`** -> AI Confidence: **99.31%**
4420. **`drivers/media/pci/cx23885/cx23885-dvb.c`** -> AI Confidence: **99.31%**
4421. **`drivers/media/pci/cx23885/cx23885-video.c`** -> AI Confidence: **99.31%**
4422. **`drivers/media/pci/cx88/cx88-core.c`** -> AI Confidence: **99.31%**
4423. **`drivers/media/pci/cx88/cx88-dvb.c`** -> AI Confidence: **99.31%**
4424. **`drivers/media/pci/cx88/cx88-mpeg.c`** -> AI Confidence: **99.31%**
4425. **`drivers/media/pci/ddbridge/ddbridge-core.c`** -> AI Confidence: **99.31%**
4426. **`drivers/media/pci/ddbridge/ddbridge-i2c.c`** -> AI Confidence: **99.31%**
4427. **`drivers/media/pci/ddbridge/ddbridge-main.c`** -> AI Confidence: **99.31%**
4428. **`drivers/media/pci/ddbridge/ddbridge-max.c`** -> AI Confidence: **99.31%**
4429. **`drivers/media/pci/dm1105/dm1105.c`** -> AI Confidence: **99.31%**
4430. **`drivers/media/pci/intel/ipu6/ipu6-buttress.c`** -> AI Confidence: **99.31%**
4431. **`drivers/media/pci/intel/ipu6/ipu6-isys-subdev.c`** -> AI Confidence: **99.31%**
4432. **`drivers/media/pci/intel/ipu6/ipu6-isys.c`** -> AI Confidence: **99.31%**
4433. **`drivers/media/pci/intel/ivsc/mei_csi.c`** -> AI Confidence: **99.31%**
4434. **`drivers/media/pci/ivtv/ivtv-fileops.c`** -> AI Confidence: **99.31%**
4435. **`drivers/media/pci/ivtv/ivtv-firmware.c`** -> AI Confidence: **99.31%**
4436. **`drivers/media/pci/ivtv/ivtv-irq.c`** -> AI Confidence: **99.31%**
4437. **`drivers/media/pci/ivtv/ivtvfb.c`** -> AI Confidence: **99.31%**
4438. **`drivers/media/pci/mantis/hopper_cards.c`** -> AI Confidence: **99.31%**
4439. **`drivers/media/pci/mantis/mantis_cards.c`** -> AI Confidence: **99.31%**
4440. **`drivers/media/pci/mantis/mantis_dma.c`** -> AI Confidence: **99.31%**
4441. **`drivers/media/pci/mantis/mantis_dvb.c`** -> AI Confidence: **99.31%**
4442. **`drivers/media/pci/mantis/mantis_evm.c`** -> AI Confidence: **99.31%**
4443. **`drivers/media/pci/mantis/mantis_i2c.c`** -> AI Confidence: **99.31%**
4444. **`drivers/media/pci/mantis/mantis_pci.c`** -> AI Confidence: **99.31%**
4445. **`drivers/media/pci/mantis/mantis_uart.c`** -> AI Confidence: **99.31%**
4446. **`drivers/media/pci/mantis/mantis_vp1033.c`** -> AI Confidence: **99.31%**
4447. **`drivers/media/pci/mantis/mantis_vp1034.c`** -> AI Confidence: **99.31%**
4448. **`drivers/media/pci/mantis/mantis_vp2033.c`** -> AI Confidence: **99.31%**
4449. **`drivers/media/pci/mantis/mantis_vp2040.c`** -> AI Confidence: **99.31%**
4450. **`drivers/media/pci/netup_unidvb/netup_unidvb_core.c`** -> AI Confidence: **99.31%**
4451. **`drivers/media/pci/ngene/ngene-core.c`** -> AI Confidence: **99.31%**
4452. **`drivers/media/pci/ngene/ngene-i2c.c`** -> AI Confidence: **99.31%**
4453. **`drivers/media/pci/pt3/pt3.c`** -> AI Confidence: **99.31%**
4454. **`drivers/media/pci/saa7134/saa7134-alsa.c`** -> AI Confidence: **99.31%**
4455. **`drivers/media/pci/saa7134/saa7134-core.c`** -> AI Confidence: **99.31%**
4456. **`drivers/media/pci/saa7134/saa7134-dvb.c`** -> AI Confidence: **99.31%**
4457. **`drivers/media/pci/saa7134/saa7134-i2c.c`** -> AI Confidence: **99.31%**
4458. **`drivers/media/pci/saa7134/saa7134-video.c`** -> AI Confidence: **99.31%**
4459. **`drivers/media/pci/saa7164/saa7164-core.c`** -> AI Confidence: **99.31%**
4460. **`drivers/media/pci/saa7164/saa7164-dvb.c`** -> AI Confidence: **99.31%**
4461. **`drivers/media/pci/solo6x10/solo6x10-core.c`** -> AI Confidence: **99.31%**
4462. **`drivers/media/pci/ttpci/budget-av.c`** -> AI Confidence: **99.31%**
4463. **`drivers/media/pci/ttpci/budget-ci.c`** -> AI Confidence: **99.31%**
4464. **`drivers/media/pci/tw5864/tw5864-core.c`** -> AI Confidence: **99.31%**
4465. **`drivers/media/pci/tw68/tw68-core.c`** -> AI Confidence: **99.31%**
4466. **`drivers/media/pci/tw686x/tw686x-core.c`** -> AI Confidence: **99.31%**
4467. **`drivers/media/pci/zoran/zoran_card.c`** -> AI Confidence: **99.31%**
4468. **`drivers/media/pci/zoran/zoran_driver.c`** -> AI Confidence: **99.31%**
4469. **`drivers/media/platform/allegro-dvt/nal-h264.c`** -> AI Confidence: **99.31%**
4470. **`drivers/media/platform/allegro-dvt/nal-hevc.c`** -> AI Confidence: **99.31%**
4471. **`drivers/media/platform/amphion/vpu_helpers.c`** -> AI Confidence: **99.31%**
4472. **`drivers/media/platform/broadcom/bcm2835-unicam.c`** -> AI Confidence: **99.31%**
4473. **`drivers/media/platform/chips-media/coda/coda-bit.c`** -> AI Confidence: **99.31%**
4474. **`drivers/media/platform/chips-media/coda/coda-common.c`** -> AI Confidence: **99.31%**
4475. **`drivers/media/platform/chips-media/coda/coda-jpeg.c`** -> AI Confidence: **99.31%**
4476. **`drivers/media/platform/chips-media/wave5/wave5-vpu.c`** -> AI Confidence: **99.31%**
4477. **`drivers/media/platform/mediatek/mdp3/mtk-mdp3-cmdq.c`** -> AI Confidence: **99.31%**
4478. **`drivers/media/platform/mediatek/mdp3/mtk-mdp3-comp.c`** -> AI Confidence: **99.31%**
4479. **`drivers/media/platform/mediatek/mdp3/mtk-mdp3-core.c`** -> AI Confidence: **99.31%**
4480. **`drivers/media/platform/mediatek/vcodec/decoder/mtk_vcodec_dec_drv.c`** -> AI Confidence: **99.31%**
4481. **`drivers/media/platform/mediatek/vcodec/decoder/mtk_vcodec_dec_stateless.c`** -> AI Confidence: **99.31%**
4482. **`drivers/media/platform/mediatek/vcodec/decoder/vdec/vdec_vp9_req_lat_if.c`** -> AI Confidence: **99.31%**
4483. **`drivers/media/platform/mediatek/vcodec/decoder/vdec_drv_if.c`** -> AI Confidence: **99.31%**
4484. **`drivers/media/platform/nvidia/tegra-vde/dmabuf-cache.c`** -> AI Confidence: **99.31%**
4485. **`drivers/media/platform/qcom/camss/camss-csid-gen2.c`** -> AI Confidence: **99.31%**
4486. **`drivers/media/platform/qcom/camss/camss-csid-gen3.c`** -> AI Confidence: **99.31%**
4487. **`drivers/media/platform/qcom/camss/camss-ispif.c`** -> AI Confidence: **99.31%**
4488. **`drivers/media/platform/qcom/camss/camss-vfe-4-7.c`** -> AI Confidence: **99.31%**
4489. **`drivers/media/platform/qcom/camss/camss-vfe-4-8.c`** -> AI Confidence: **99.31%**
4490. **`drivers/media/platform/qcom/iris/iris_hfi_gen1_response.c`** -> AI Confidence: **99.31%**
4491. **`drivers/media/platform/qcom/iris/iris_hfi_gen2_response.c`** -> AI Confidence: **99.31%**
4492. **`drivers/media/platform/qcom/iris/iris_vb2.c`** -> AI Confidence: **99.31%**
4493. **`drivers/media/platform/qcom/iris/iris_vdec.c`** -> AI Confidence: **99.31%**
4494. **`drivers/media/platform/qcom/iris/iris_venc.c`** -> AI Confidence: **99.31%**
4495. **`drivers/media/platform/qcom/iris/iris_vpu_common.c`** -> AI Confidence: **99.31%**
4496. **`drivers/media/platform/qcom/venus/core.c`** -> AI Confidence: **99.31%**
4497. **`drivers/media/platform/qcom/venus/firmware.c`** -> AI Confidence: **99.31%**
4498. **`drivers/media/platform/qcom/venus/helpers.c`** -> AI Confidence: **99.31%**
4499. **`drivers/media/platform/qcom/venus/pm_helpers.c`** -> AI Confidence: **99.31%**
4500. **`drivers/media/platform/qcom/venus/venc.c`** -> AI Confidence: **99.31%**
4501. **`drivers/media/platform/renesas/rcar-vin/rcar-core.c`** -> AI Confidence: **99.31%**
4502. **`drivers/media/platform/renesas/rcar_fdp1.c`** -> AI Confidence: **99.31%**
4503. **`drivers/media/platform/renesas/vsp1/vsp1_drv.c`** -> AI Confidence: **99.31%**
4504. **`drivers/media/platform/renesas/vsp1/vsp1_rpf.c`** -> AI Confidence: **99.31%**
4505. **`drivers/media/platform/renesas/vsp1/vsp1_wpf.c`** -> AI Confidence: **99.31%**
4506. **`drivers/media/platform/rockchip/rkisp1/rkisp1-dev.c`** -> AI Confidence: **99.31%**
4507. **`drivers/media/platform/samsung/exynos-gsc/gsc-core.c`** -> AI Confidence: **99.31%**
4508. **`drivers/media/platform/samsung/exynos4-is/fimc-core.c`** -> AI Confidence: **99.31%**
4509. **`drivers/media/platform/samsung/exynos4-is/fimc-is-param.c`** -> AI Confidence: **99.31%**
4510. **`drivers/media/platform/samsung/exynos4-is/fimc-is.c`** -> AI Confidence: **99.31%**
4511. **`drivers/media/platform/samsung/exynos4-is/fimc-isp.c`** -> AI Confidence: **99.31%**
4512. **`drivers/media/platform/samsung/exynos4-is/fimc-reg.c`** -> AI Confidence: **99.31%**
4513. **`drivers/media/platform/samsung/exynos4-is/media-dev.c`** -> AI Confidence: **99.31%**
4514. **`drivers/media/platform/samsung/s5p-jpeg/jpeg-core.c`** -> AI Confidence: **99.31%**
4515. **`drivers/media/platform/samsung/s5p-mfc/s5p_mfc.c`** -> AI Confidence: **99.31%**
4516. **`drivers/media/platform/samsung/s5p-mfc/s5p_mfc_ctrl.c`** -> AI Confidence: **99.31%**
4517. **`drivers/media/platform/samsung/s5p-mfc/s5p_mfc_dec.c`** -> AI Confidence: **99.31%**
4518. **`drivers/media/platform/samsung/s5p-mfc/s5p_mfc_enc.c`** -> AI Confidence: **99.31%**
4519. **`drivers/media/platform/samsung/s5p-mfc/s5p_mfc_intr.c`** -> AI Confidence: **99.31%**
4520. **`drivers/media/platform/samsung/s5p-mfc/s5p_mfc_opr_v5.c`** -> AI Confidence: **99.31%**
4521. **`drivers/media/platform/samsung/s5p-mfc/s5p_mfc_opr_v6.c`** -> AI Confidence: **99.31%**
4522. **`drivers/media/platform/st/sti/hva/hva-hw.c`** -> AI Confidence: **99.31%**
4523. **`drivers/media/platform/ti/davinci/vpif_capture.c`** -> AI Confidence: **99.31%**
4524. **`drivers/media/platform/ti/omap/omap_vout_vrfb.c`** -> AI Confidence: **99.31%**
4525. **`drivers/media/platform/ti/omap3isp/isp.c`** -> AI Confidence: **99.31%**
4526. **`drivers/media/platform/ti/omap3isp/ispcsiphy.c`** -> AI Confidence: **99.31%**
4527. **`drivers/media/platform/ti/omap3isp/isphist.c`** -> AI Confidence: **99.31%**
4528. **`drivers/media/platform/ti/vpe/csc.c`** -> AI Confidence: **99.31%**
4529. **`drivers/media/platform/ti/vpe/sc.c`** -> AI Confidence: **99.31%**
4530. **`drivers/media/platform/video-mux.c`** -> AI Confidence: **99.31%**
4531. **`drivers/media/radio/radio-si476x.c`** -> AI Confidence: **99.31%**
4532. **`drivers/media/radio/radio-tea5777.c`** -> AI Confidence: **99.31%**
4533. **`drivers/media/radio/si4713/si4713.c`** -> AI Confidence: **99.31%**
4534. **`drivers/media/radio/tea575x.c`** -> AI Confidence: **99.31%**
4535. **`drivers/media/rc/ati_remote.c`** -> AI Confidence: **99.31%**
4536. **`drivers/media/rc/ene_ir.c`** -> AI Confidence: **99.31%**
4537. **`drivers/media/rc/iguanair.c`** -> AI Confidence: **99.31%**
4538. **`drivers/media/rc/img-ir/img-ir-core.c`** -> AI Confidence: **99.31%**
4539. **`drivers/media/rc/imon.c`** -> AI Confidence: **99.31%**
4540. **`drivers/media/rc/ir_toy.c`** -> AI Confidence: **99.31%**
4541. **`drivers/media/rc/mceusb.c`** -> AI Confidence: **99.31%**
4542. **`drivers/media/rc/rc-main.c`** -> AI Confidence: **99.31%**
4543. **`drivers/media/rc/redrat3.c`** -> AI Confidence: **99.31%**
4544. **`drivers/media/rc/serial_ir.c`** -> AI Confidence: **99.31%**
4545. **`drivers/media/rc/st_rc.c`** -> AI Confidence: **99.31%**
4546. **`drivers/media/rc/winbond-cir.c`** -> AI Confidence: **99.31%**
4547. **`drivers/media/spi/cxd2880-spi.c`** -> AI Confidence: **99.31%**
4548. **`drivers/media/tuners/mc44s803.c`** -> AI Confidence: **99.31%**
4549. **`drivers/media/tuners/mt2060.c`** -> AI Confidence: **99.31%**
4550. **`drivers/media/tuners/mt2063.c`** -> AI Confidence: **99.31%**
4551. **`drivers/media/tuners/mt2131.c`** -> AI Confidence: **99.31%**
4552. **`drivers/media/tuners/mt2266.c`** -> AI Confidence: **99.31%**
4553. **`drivers/media/tuners/tda8290.c`** -> AI Confidence: **99.31%**
4554. **`drivers/media/tuners/tda9887.c`** -> AI Confidence: **99.31%**
4555. **`drivers/media/tuners/tuner-simple.c`** -> AI Confidence: **99.31%**
4556. **`drivers/media/tuners/xc5000.c`** -> AI Confidence: **99.31%**
4557. **`drivers/media/usb/as102/as102_drv.c`** -> AI Confidence: **99.31%**
4558. **`drivers/media/usb/au0828/au0828-core.c`** -> AI Confidence: **99.31%**
4559. **`drivers/media/usb/au0828/au0828-i2c.c`** -> AI Confidence: **99.31%**
4560. **`drivers/media/usb/cx231xx/cx231xx-audio.c`** -> AI Confidence: **99.31%**
4561. **`drivers/media/usb/cx231xx/cx231xx-avcore.c`** -> AI Confidence: **99.31%**
4562. **`drivers/media/usb/cx231xx/cx231xx-cards.c`** -> AI Confidence: **99.31%**
4563. **`drivers/media/usb/cx231xx/cx231xx-core.c`** -> AI Confidence: **99.31%**
4564. **`drivers/media/usb/cx231xx/cx231xx-dvb.c`** -> AI Confidence: **99.31%**
4565. **`drivers/media/usb/cx231xx/cx231xx-i2c.c`** -> AI Confidence: **99.31%**
4566. **`drivers/media/usb/cx231xx/cx231xx-vbi.c`** -> AI Confidence: **99.31%**
4567. **`drivers/media/usb/cx231xx/cx231xx-video.c`** -> AI Confidence: **99.31%**
4568. **`drivers/media/usb/dvb-usb-v2/anysee.c`** -> AI Confidence: **99.31%**
4569. **`drivers/media/usb/dvb-usb-v2/lmedm04.c`** -> AI Confidence: **99.31%**
4570. **`drivers/media/usb/dvb-usb-v2/mxl111sf.c`** -> AI Confidence: **99.31%**
4571. **`drivers/media/usb/dvb-usb/cxusb.c`** -> AI Confidence: **99.31%**
4572. **`drivers/media/usb/dvb-usb/dw2102.c`** -> AI Confidence: **99.31%**
4573. **`drivers/media/usb/dvb-usb/m920x.c`** -> AI Confidence: **99.31%**
4574. **`drivers/media/usb/em28xx/em28xx-audio.c`** -> AI Confidence: **99.31%**
4575. **`drivers/media/usb/em28xx/em28xx-cards.c`** -> AI Confidence: **99.31%**
4576. **`drivers/media/usb/em28xx/em28xx-core.c`** -> AI Confidence: **99.31%**
4577. **`drivers/media/usb/em28xx/em28xx-dvb.c`** -> AI Confidence: **99.31%**
4578. **`drivers/media/usb/em28xx/em28xx-i2c.c`** -> AI Confidence: **99.31%**
4579. **`drivers/media/usb/em28xx/em28xx-input.c`** -> AI Confidence: **99.31%**
4580. **`drivers/media/usb/em28xx/em28xx-video.c`** -> AI Confidence: **99.31%**
4581. **`drivers/media/usb/go7007/go7007-i2c.c`** -> AI Confidence: **99.31%**
4582. **`drivers/media/usb/go7007/go7007-usb.c`** -> AI Confidence: **99.31%**
4583. **`drivers/media/usb/gspca/gspca.c`** -> AI Confidence: **99.31%**
4584. **`drivers/media/usb/hackrf/hackrf.c`** -> AI Confidence: **99.31%**
4585. **`drivers/media/usb/hdpvr/hdpvr-control.c`** -> AI Confidence: **99.31%**
4586. **`drivers/media/usb/msi2500/msi2500.c`** -> AI Confidence: **99.31%**
4587. **`drivers/media/usb/pvrusb2/pvrusb2-context.c`** -> AI Confidence: **99.31%**
4588. **`drivers/media/usb/pvrusb2/pvrusb2-hdw.c`** -> AI Confidence: **99.31%**
4589. **`drivers/media/usb/pvrusb2/pvrusb2-ioread.c`** -> AI Confidence: **99.31%**
4590. **`drivers/media/usb/pwc/pwc-ctrl.c`** -> AI Confidence: **99.31%**
4591. **`drivers/media/usb/pwc/pwc-if.c`** -> AI Confidence: **99.31%**
4592. **`drivers/media/usb/pwc/pwc-v4l.c`** -> AI Confidence: **99.31%**
4593. **`drivers/media/usb/s2255/s2255drv.c`** -> AI Confidence: **99.31%**
4594. **`drivers/media/usb/ttusb-budget/dvb-ttusb-budget.c`** -> AI Confidence: **99.31%**
4595. **`drivers/media/usb/ttusb-dec/ttusb_dec.c`** -> AI Confidence: **99.31%**
4596. **`drivers/media/usb/uvc/uvc_ctrl.c`** -> AI Confidence: **99.31%**
4597. **`drivers/media/usb/uvc/uvc_driver.c`** -> AI Confidence: **99.31%**
4598. **`drivers/media/usb/uvc/uvc_video.c`** -> AI Confidence: **99.31%**
4599. **`drivers/media/v4l2-core/tuner-core.c`** -> AI Confidence: **99.31%**
4600. **`drivers/media/v4l2-core/v4l2-common.c`** -> AI Confidence: **99.31%**
4601. **`drivers/media/v4l2-core/v4l2-compat-ioctl32.c`** -> AI Confidence: **99.31%**
4602. **`drivers/media/v4l2-core/v4l2-ctrls-core.c`** -> AI Confidence: **99.31%**
4603. **`drivers/media/v4l2-core/v4l2-dev.c`** -> AI Confidence: **99.31%**
4604. **`drivers/media/v4l2-core/v4l2-device.c`** -> AI Confidence: **99.31%**
4605. **`drivers/media/v4l2-core/v4l2-dv-timings.c`** -> AI Confidence: **99.31%**
4606. **`drivers/media/v4l2-core/v4l2-fwnode.c`** -> AI Confidence: **99.31%**
4607. **`drivers/media/v4l2-core/v4l2-ioctl.c`** -> AI Confidence: **99.31%**
4608. **`drivers/media/v4l2-core/v4l2-mc.c`** -> AI Confidence: **99.31%**
4609. **`drivers/memory/emif.c`** -> AI Confidence: **99.31%**
4610. **`drivers/memory/fsl-corenet-cf.c`** -> AI Confidence: **99.31%**
4611. **`drivers/memory/fsl_ifc.c`** -> AI Confidence: **99.31%**
4612. **`drivers/memory/pl172.c`** -> AI Confidence: **99.31%**
4613. **`drivers/memory/renesas-rpc-if.c`** -> AI Confidence: **99.31%**
4614. **`drivers/memory/tegra/mc.c`** -> AI Confidence: **99.31%**
4615. **`drivers/memory/tegra/tegra186.c`** -> AI Confidence: **99.31%**
4616. **`drivers/memory/tegra/tegra210-emc-core.c`** -> AI Confidence: **99.31%**
4617. **`drivers/memstick/core/ms_block.c`** -> AI Confidence: **99.31%**
4618. **`drivers/memstick/host/jmb38x_ms.c`** -> AI Confidence: **99.31%**
4619. **`drivers/memstick/host/rtsx_usb_ms.c`** -> AI Confidence: **99.31%**
4620. **`drivers/memstick/host/tifm_ms.c`** -> AI Confidence: **99.31%**
4621. **`drivers/message/fusion/mptctl.c`** -> AI Confidence: **99.31%**
4622. **`drivers/message/fusion/mptfc.c`** -> AI Confidence: **99.31%**
4623. **`drivers/message/fusion/mptlan.h`** -> AI Confidence: **99.31%**
4624. **`drivers/message/fusion/mptsas.c`** -> AI Confidence: **99.31%**
4625. **`drivers/message/fusion/mptspi.c`** -> AI Confidence: **99.31%**
4626. **`drivers/mfd/88pm800.c`** -> AI Confidence: **99.31%**
4627. **`drivers/mfd/ab8500-core.c`** -> AI Confidence: **99.31%**
4628. **`drivers/mfd/adp5585.c`** -> AI Confidence: **99.31%**
4629. **`drivers/mfd/arizona-i2c.c`** -> AI Confidence: **99.31%**
4630. **`drivers/mfd/arizona-irq.c`** -> AI Confidence: **99.31%**
4631. **`drivers/mfd/as3711.c`** -> AI Confidence: **99.31%**
4632. **`drivers/mfd/cs42l43.c`** -> AI Confidence: **99.31%**
4633. **`drivers/mfd/da9052-i2c.c`** -> AI Confidence: **99.31%**
4634. **`drivers/mfd/da9063-core.c`** -> AI Confidence: **99.31%**
4635. **`drivers/mfd/da9150-core.c`** -> AI Confidence: **99.31%**
4636. **`drivers/mfd/db8500-prcmu.c`** -> AI Confidence: **99.31%**
4637. **`drivers/mfd/ipaq-micro.c`** -> AI Confidence: **99.31%**
4638. **`drivers/mfd/lochnagar-i2c.c`** -> AI Confidence: **99.31%**
4639. **`drivers/mfd/madera-core.c`** -> AI Confidence: **99.31%**
4640. **`drivers/mfd/madera-i2c.c`** -> AI Confidence: **99.31%**
4641. **`drivers/mfd/madera-spi.c`** -> AI Confidence: **99.31%**
4642. **`drivers/mfd/max77620.c`** -> AI Confidence: **99.31%**
4643. **`drivers/mfd/menelaus.c`** -> AI Confidence: **99.31%**
4644. **`drivers/mfd/mxs-lradc.c`** -> AI Confidence: **99.31%**
4645. **`drivers/mfd/omap-usb-host.c`** -> AI Confidence: **99.31%**
4646. **`drivers/mfd/omap-usb-tll.c`** -> AI Confidence: **99.31%**
4647. **`drivers/mfd/palmas.c`** -> AI Confidence: **99.31%**
4648. **`drivers/mfd/rave-sp.c`** -> AI Confidence: **99.31%**
4649. **`drivers/mfd/rc5t583.c`** -> AI Confidence: **99.31%**
4650. **`drivers/mfd/rk8xx-core.c`** -> AI Confidence: **99.31%**
4651. **`drivers/mfd/rn5t618.c`** -> AI Confidence: **99.31%**
4652. **`drivers/mfd/rsmu_core.c`** -> AI Confidence: **99.31%**
4653. **`drivers/mfd/sec-common.c`** -> AI Confidence: **99.31%**
4654. **`drivers/mfd/si476x-i2c.c`** -> AI Confidence: **99.31%**
4655. **`drivers/mfd/ssbi.c`** -> AI Confidence: **99.31%**
4656. **`drivers/mfd/stmpe.c`** -> AI Confidence: **99.31%**
4657. **`drivers/mfd/stw481x.c`** -> AI Confidence: **99.31%**
4658. **`drivers/mfd/tps6105x.c`** -> AI Confidence: **99.31%**
4659. **`drivers/mfd/tps65010.c`** -> AI Confidence: **99.31%**
4660. **`drivers/mfd/tqmx86.c`** -> AI Confidence: **99.31%**
4661. **`drivers/mfd/twl4030-power.c`** -> AI Confidence: **99.31%**
4662. **`drivers/mfd/twl6040.c`** -> AI Confidence: **99.31%**
4663. **`drivers/mfd/wm831x-auxadc.c`** -> AI Confidence: **99.31%**
4664. **`drivers/misc/ad525x_dpot.c`** -> AI Confidence: **99.31%**
4665. **`drivers/misc/amd-sbi/rmi-core.c`** -> AI Confidence: **99.31%**
4666. **`drivers/misc/bcm-vk/bcm_vk_dev.c`** -> AI Confidence: **99.31%**
4667. **`drivers/misc/bcm-vk/bcm_vk_sg.c`** -> AI Confidence: **99.31%**
4668. **`drivers/misc/cardreader/rtsx_pcr.c`** -> AI Confidence: **99.31%**
4669. **`drivers/misc/cs5535-mfgpt.c`** -> AI Confidence: **99.31%**
4670. **`drivers/misc/eeprom/at24.c`** -> AI Confidence: **99.31%**
4671. **`drivers/misc/eeprom/at25.c`** -> AI Confidence: **99.31%**
4672. **`drivers/misc/eeprom/idt_89hpesx.c`** -> AI Confidence: **99.31%**
4673. **`drivers/misc/genwqe/card_base.c`** -> AI Confidence: **99.31%**
4674. **`drivers/misc/ibmvmc.c`** -> AI Confidence: **99.31%**
4675. **`drivers/misc/kgdbts.c`** -> AI Confidence: **99.31%**
4676. **`drivers/misc/lattice-ecp3-config.c`** -> AI Confidence: **99.31%**
4677. **`drivers/misc/lkdtm/bugs.c`** -> AI Confidence: **99.31%**
4678. **`drivers/misc/mchp_pci1xxxx/mchp_pci1xxxx_gp.c`** -> AI Confidence: **99.31%**
4679. **`drivers/misc/mei/interrupt.c`** -> AI Confidence: **99.31%**
4680. **`drivers/misc/mei/main.c`** -> AI Confidence: **99.31%**
4681. **`drivers/misc/pch_phub.c`** -> AI Confidence: **99.31%**
4682. **`drivers/misc/phantom.c`** -> AI Confidence: **99.31%**
4683. **`drivers/misc/sgi-gru/grufault.c`** -> AI Confidence: **99.31%**
4684. **`drivers/misc/sgi-gru/grufile.c`** -> AI Confidence: **99.31%**
4685. **`drivers/misc/sgi-gru/grukdump.c`** -> AI Confidence: **99.31%**
4686. **`drivers/misc/sgi-gru/grukservices.c`** -> AI Confidence: **99.31%**
4687. **`drivers/misc/sgi-gru/grumain.c`** -> AI Confidence: **99.31%**
4688. **`drivers/misc/sgi-xp/xpc_main.c`** -> AI Confidence: **99.31%**
4689. **`drivers/misc/sram.c`** -> AI Confidence: **99.31%**
4690. **`drivers/misc/tps6594-pfsm.c`** -> AI Confidence: **99.31%**
4691. **`drivers/misc/vmw_vmci/vmci_context.c`** -> AI Confidence: **99.31%**
4692. **`drivers/misc/vmw_vmci/vmci_driver.c`** -> AI Confidence: **99.31%**
4693. **`drivers/misc/vmw_vmci/vmci_queue_pair.c`** -> AI Confidence: **99.31%**
4694. **`drivers/misc/xilinx_sdfec.c`** -> AI Confidence: **99.31%**
4695. **`drivers/mmc/core/bus.c`** -> AI Confidence: **99.31%**
4696. **`drivers/mmc/core/core.c`** -> AI Confidence: **99.31%**
4697. **`drivers/mmc/core/debugfs.c`** -> AI Confidence: **99.31%**
4698. **`drivers/mmc/core/host.c`** -> AI Confidence: **99.31%**
4699. **`drivers/mmc/core/sd.c`** -> AI Confidence: **99.31%**
4700. **`drivers/mmc/core/sd_uhs2.c`** -> AI Confidence: **99.31%**
4701. **`drivers/mmc/core/sdio.c`** -> AI Confidence: **99.31%**
4702. **`drivers/mmc/core/sdio_cis.c`** -> AI Confidence: **99.31%**
4703. **`drivers/mmc/core/sdio_io.c`** -> AI Confidence: **99.31%**
4704. **`drivers/mmc/core/sdio_irq.c`** -> AI Confidence: **99.31%**
4705. **`drivers/mmc/core/sdio_ops.c`** -> AI Confidence: **99.31%**
4706. **`drivers/mmc/host/atmel-mci.c`** -> AI Confidence: **99.31%**
4707. **`drivers/mmc/host/au1xmmc.c`** -> AI Confidence: **99.31%**
4708. **`drivers/mmc/host/bcm2835.c`** -> AI Confidence: **99.31%**
4709. **`drivers/mmc/host/cavium.c`** -> AI Confidence: **99.31%**
4710. **`drivers/mmc/host/davinci_mmc.c`** -> AI Confidence: **99.31%**
4711. **`drivers/mmc/host/dw_mmc-exynos.c`** -> AI Confidence: **99.31%**
4712. **`drivers/mmc/host/dw_mmc-hi3798cv200.c`** -> AI Confidence: **99.31%**
4713. **`drivers/mmc/host/dw_mmc-hi3798mv200.c`** -> AI Confidence: **99.31%**
4714. **`drivers/mmc/host/dw_mmc-starfive.c`** -> AI Confidence: **99.31%**
4715. **`drivers/mmc/host/dw_mmc.c`** -> AI Confidence: **99.31%**
4716. **`drivers/mmc/host/jz4740_mmc.c`** -> AI Confidence: **99.31%**
4717. **`drivers/mmc/host/meson-mx-sdio.c`** -> AI Confidence: **99.31%**
4718. **`drivers/mmc/host/mmc_spi.c`** -> AI Confidence: **99.31%**
4719. **`drivers/mmc/host/moxart-mmc.c`** -> AI Confidence: **99.31%**
4720. **`drivers/mmc/host/mvsdio.c`** -> AI Confidence: **99.31%**
4721. **`drivers/mmc/host/mxcmmc.c`** -> AI Confidence: **99.31%**
4722. **`drivers/mmc/host/omap.c`** -> AI Confidence: **99.31%**
4723. **`drivers/mmc/host/omap_hsmmc.c`** -> AI Confidence: **99.31%**
4724. **`drivers/mmc/host/owl-mmc.c`** -> AI Confidence: **99.31%**
4725. **`drivers/mmc/host/pxamci.c`** -> AI Confidence: **99.31%**
4726. **`drivers/mmc/host/renesas_sdhi_core.c`** -> AI Confidence: **99.31%**
4727. **`drivers/mmc/host/renesas_sdhi_sys_dmac.c`** -> AI Confidence: **99.31%**
4728. **`drivers/mmc/host/rtsx_usb_sdmmc.c`** -> AI Confidence: **99.31%**
4729. **`drivers/mmc/host/sdhci-bcm-kona.c`** -> AI Confidence: **99.31%**
4730. **`drivers/mmc/host/sdhci-brcmstb.c`** -> AI Confidence: **99.31%**
4731. **`drivers/mmc/host/sdhci-esdhc-imx.c`** -> AI Confidence: **99.31%**
4732. **`drivers/mmc/host/sdhci-of-esdhc.c`** -> AI Confidence: **99.31%**
4733. **`drivers/mmc/host/sdhci-omap.c`** -> AI Confidence: **99.31%**
4734. **`drivers/mmc/host/sdhci-sprd.c`** -> AI Confidence: **99.31%**
4735. **`drivers/mmc/host/sdhci-uhs2.c`** -> AI Confidence: **99.31%**
4736. **`drivers/mmc/host/sdhci.c`** -> AI Confidence: **99.31%**
4737. **`drivers/mmc/host/sunplus-mmc.c`** -> AI Confidence: **99.31%**
4738. **`drivers/mmc/host/sunxi-mmc.c`** -> AI Confidence: **99.31%**
4739. **`drivers/mmc/host/tifm_sd.c`** -> AI Confidence: **99.31%**
4740. **`drivers/mmc/host/tmio_mmc_core.c`** -> AI Confidence: **99.31%**
4741. **`drivers/mmc/host/toshsd.c`** -> AI Confidence: **99.31%**
4742. **`drivers/mmc/host/vub300.c`** -> AI Confidence: **99.31%**
4743. **`drivers/mmc/host/wbsd.c`** -> AI Confidence: **99.31%**
4744. **`drivers/mmc/host/wmt-sdmmc.c`** -> AI Confidence: **99.31%**
4745. **`drivers/mtd/chips/cfi_cmdset_0001.c`** -> AI Confidence: **99.31%**
4746. **`drivers/mtd/chips/cfi_cmdset_0002.c`** -> AI Confidence: **99.31%**
4747. **`drivers/mtd/chips/cfi_cmdset_0020.c`** -> AI Confidence: **99.31%**
4748. **`drivers/mtd/chips/cfi_probe.c`** -> AI Confidence: **99.31%**
4749. **`drivers/mtd/chips/cfi_util.c`** -> AI Confidence: **99.31%**
4750. **`drivers/mtd/devices/bcm47xxsflash.c`** -> AI Confidence: **99.31%**
4751. **`drivers/mtd/devices/docg3.c`** -> AI Confidence: **99.31%**
4752. **`drivers/mtd/devices/ms02-nv.c`** -> AI Confidence: **99.31%**
4753. **`drivers/mtd/devices/mtd_intel_dg.c`** -> AI Confidence: **99.31%**
4754. **`drivers/mtd/devices/phram.c`** -> AI Confidence: **99.31%**
4755. **`drivers/mtd/devices/pmc551.c`** -> AI Confidence: **99.31%**
4756. **`drivers/mtd/ftl.c`** -> AI Confidence: **99.31%**
4757. **`drivers/mtd/inftlcore.c`** -> AI Confidence: **99.31%**
4758. **`drivers/mtd/maps/amd76xrom.c`** -> AI Confidence: **99.31%**
4759. **`drivers/mtd/maps/ck804xrom.c`** -> AI Confidence: **99.31%**
4760. **`drivers/mtd/maps/esb2rom.c`** -> AI Confidence: **99.31%**
4761. **`drivers/mtd/maps/ichxrom.c`** -> AI Confidence: **99.31%**
4762. **`drivers/mtd/maps/impa7.c`** -> AI Confidence: **99.31%**
4763. **`drivers/mtd/maps/l440gx.c`** -> AI Confidence: **99.31%**
4764. **`drivers/mtd/maps/nettel.c`** -> AI Confidence: **99.31%**
4765. **`drivers/mtd/maps/physmap-core.c`** -> AI Confidence: **99.31%**
4766. **`drivers/mtd/maps/plat-ram.c`** -> AI Confidence: **99.31%**
4767. **`drivers/mtd/maps/sa1100-flash.c`** -> AI Confidence: **99.31%**
4768. **`drivers/mtd/maps/scb2_flash.c`** -> AI Confidence: **99.31%**
4769. **`drivers/mtd/maps/scx200_docflash.c`** -> AI Confidence: **99.31%**
4770. **`drivers/mtd/maps/ts5500_flash.c`** -> AI Confidence: **99.31%**
4771. **`drivers/mtd/maps/vmu-flash.c`** -> AI Confidence: **99.31%**
4772. **`drivers/mtd/mtd_blkdevs.c`** -> AI Confidence: **99.31%**
4773. **`drivers/mtd/mtdchar.c`** -> AI Confidence: **99.31%**
4774. **`drivers/mtd/mtdconcat.c`** -> AI Confidence: **99.31%**
4775. **`drivers/mtd/mtdoops.c`** -> AI Confidence: **99.31%**
4776. **`drivers/mtd/mtdswap.c`** -> AI Confidence: **99.31%**
4777. **`drivers/mtd/nand/ecc-sw-bch.c`** -> AI Confidence: **99.31%**
4778. **`drivers/mtd/nand/ecc-sw-hamming.c`** -> AI Confidence: **99.31%**
4779. **`drivers/mtd/nand/onenand/generic.c`** -> AI Confidence: **99.31%**
4780. **`drivers/mtd/nand/onenand/onenand_base.c`** -> AI Confidence: **99.31%**
4781. **`drivers/mtd/nand/onenand/onenand_omap2.c`** -> AI Confidence: **99.31%**
4782. **`drivers/mtd/nand/onenand/onenand_samsung.c`** -> AI Confidence: **99.31%**
4783. **`drivers/mtd/nand/qpic_common.c`** -> AI Confidence: **99.31%**
4784. **`drivers/mtd/nand/raw/brcmnand/brcmnand.c`** -> AI Confidence: **99.31%**
4785. **`drivers/mtd/nand/raw/cadence-nand-controller.c`** -> AI Confidence: **99.31%**
4786. **`drivers/mtd/nand/raw/cafe_nand.c`** -> AI Confidence: **99.31%**
4787. **`drivers/mtd/nand/raw/cs553x_nand.c`** -> AI Confidence: **99.31%**
4788. **`drivers/mtd/nand/raw/diskonchip.c`** -> AI Confidence: **99.31%**
4789. **`drivers/mtd/nand/raw/fsl_elbc_nand.c`** -> AI Confidence: **99.31%**
4790. **`drivers/mtd/nand/raw/gpmi-nand/gpmi-nand.c`** -> AI Confidence: **99.31%**
4791. **`drivers/mtd/nand/raw/ingenic/jz4725b_bch.c`** -> AI Confidence: **99.31%**
4792. **`drivers/mtd/nand/raw/mpc5121_nfc.c`** -> AI Confidence: **99.31%**
4793. **`drivers/mtd/nand/raw/nand_base.c`** -> AI Confidence: **99.31%**
4794. **`drivers/mtd/nand/raw/nand_bbt.c`** -> AI Confidence: **99.31%**
4795. **`drivers/mtd/nand/raw/nandsim.c`** -> AI Confidence: **99.31%**
4796. **`drivers/mtd/nand/raw/omap2.c`** -> AI Confidence: **99.31%**
4797. **`drivers/mtd/nand/raw/orion_nand.c`** -> AI Confidence: **99.31%**
4798. **`drivers/mtd/nand/raw/r852.c`** -> AI Confidence: **99.31%**
4799. **`drivers/mtd/nand/raw/renesas-nand-controller.c`** -> AI Confidence: **99.31%**
4800. **`drivers/mtd/nand/raw/sh_flctl.c`** -> AI Confidence: **99.31%**
4801. **`drivers/mtd/nand/raw/sharpsl.c`** -> AI Confidence: **99.31%**
4802. **`drivers/mtd/nand/raw/stm32_fmc2_nand.c`** -> AI Confidence: **99.31%**
4803. **`drivers/mtd/nftlcore.c`** -> AI Confidence: **99.31%**
4804. **`drivers/mtd/parsers/afs.c`** -> AI Confidence: **99.31%**
4805. **`drivers/mtd/parsers/ofpart_bcm4908.c`** -> AI Confidence: **99.31%**
4806. **`drivers/mtd/parsers/ofpart_core.c`** -> AI Confidence: **99.31%**
4807. **`drivers/mtd/parsers/parser_imagetag.c`** -> AI Confidence: **99.31%**
4808. **`drivers/mtd/parsers/sharpslpart.c`** -> AI Confidence: **99.31%**
4809. **`drivers/mtd/rfd_ftl.c`** -> AI Confidence: **99.31%**
4810. **`drivers/mtd/sm_ftl.c`** -> AI Confidence: **99.31%**
4811. **`drivers/mtd/spi-nor/core.c`** -> AI Confidence: **99.31%**
4812. **`drivers/mtd/ssfdc.c`** -> AI Confidence: **99.31%**
4813. **`drivers/mtd/ubi/cdev.c`** -> AI Confidence: **99.31%**
4814. **`drivers/mtd/ubi/kapi.c`** -> AI Confidence: **99.31%**
4815. **`drivers/mtd/ubi/wl.c`** -> AI Confidence: **99.31%**
4816. **`drivers/net/arcnet/arcnet.c`** -> AI Confidence: **99.31%**
4817. **`drivers/net/arcnet/com20020-isa.c`** -> AI Confidence: **99.31%**
4818. **`drivers/net/arcnet/com90xx.c`** -> AI Confidence: **99.31%**
4819. **`drivers/net/bonding/bond_3ad.c`** -> AI Confidence: **99.31%**
4820. **`drivers/net/bonding/bond_main.c`** -> AI Confidence: **99.31%**
4821. **`drivers/net/bonding/bond_netlink.c`** -> AI Confidence: **99.31%**
4822. **`drivers/net/bonding/bond_procfs.c`** -> AI Confidence: **99.31%**
4823. **`drivers/net/bonding/bond_sysfs.c`** -> AI Confidence: **99.31%**
4824. **`drivers/net/can/cc770/cc770.c`** -> AI Confidence: **99.31%**
4825. **`drivers/net/can/cc770/cc770_platform.c`** -> AI Confidence: **99.31%**
4826. **`drivers/net/can/ctucanfd/ctucanfd_base.c`** -> AI Confidence: **99.31%**
4827. **`drivers/net/can/flexcan/flexcan-core.c`** -> AI Confidence: **99.31%**
4828. **`drivers/net/can/ifi_canfd/ifi_canfd.c`** -> AI Confidence: **99.31%**
4829. **`drivers/net/can/kvaser_pciefd/kvaser_pciefd_core.c`** -> AI Confidence: **99.31%**
4830. **`drivers/net/can/m_can/m_can.c`** -> AI Confidence: **99.31%**
4831. **`drivers/net/can/mscan/mpc5xxx_can.c`** -> AI Confidence: **99.31%**
4832. **`drivers/net/can/mscan/mscan.c`** -> AI Confidence: **99.31%**
4833. **`drivers/net/can/rcar/rcar_can.c`** -> AI Confidence: **99.31%**
4834. **`drivers/net/can/rockchip/rockchip_canfd-core.c`** -> AI Confidence: **99.31%**
4835. **`drivers/net/can/sja1000/ems_pcmcia.c`** -> AI Confidence: **99.31%**
4836. **`drivers/net/can/sja1000/peak_pcmcia.c`** -> AI Confidence: **99.31%**
4837. **`drivers/net/can/sja1000/sja1000.c`** -> AI Confidence: **99.31%**
4838. **`drivers/net/can/sja1000/sja1000_isa.c`** -> AI Confidence: **99.31%**
4839. **`drivers/net/can/sja1000/sja1000_platform.c`** -> AI Confidence: **99.31%**
4840. **`drivers/net/can/sja1000/tscan1.c`** -> AI Confidence: **99.31%**
4841. **`drivers/net/can/slcan/slcan-core.c`** -> AI Confidence: **99.31%**
4842. **`drivers/net/can/sun4i_can.c`** -> AI Confidence: **99.31%**
4843. **`drivers/net/can/usb/ems_usb.c`** -> AI Confidence: **99.31%**
4844. **`drivers/net/can/usb/etas_es58x/es58x_core.c`** -> AI Confidence: **99.31%**
4845. **`drivers/net/can/usb/f81604.c`** -> AI Confidence: **99.31%**
4846. **`drivers/net/can/usb/gs_usb.c`** -> AI Confidence: **99.31%**
4847. **`drivers/net/can/usb/kvaser_usb/kvaser_usb_core.c`** -> AI Confidence: **99.31%**
4848. **`drivers/net/can/usb/kvaser_usb/kvaser_usb_leaf.c`** -> AI Confidence: **99.31%**
4849. **`drivers/net/can/usb/peak_usb/pcan_usb.c`** -> AI Confidence: **99.31%**
4850. **`drivers/net/can/usb/peak_usb/pcan_usb_pro.c`** -> AI Confidence: **99.31%**
4851. **`drivers/net/can/usb/ucan.c`** -> AI Confidence: **99.31%**
4852. **`drivers/net/can/usb/usb_8dev.c`** -> AI Confidence: **99.31%**
4853. **`drivers/net/can/xilinx_can.c`** -> AI Confidence: **99.31%**
4854. **`drivers/net/dsa/b53/b53_common.c`** -> AI Confidence: **99.31%**
4855. **`drivers/net/dsa/bcm_sf2.c`** -> AI Confidence: **99.31%**
4856. **`drivers/net/dsa/bcm_sf2_cfp.c`** -> AI Confidence: **99.31%**
4857. **`drivers/net/dsa/lantiq/lantiq_gswip.c`** -> AI Confidence: **99.31%**
4858. **`drivers/net/dsa/microchip/ksz8.c`** -> AI Confidence: **99.31%**
4859. **`drivers/net/dsa/microchip/ksz9477.c`** -> AI Confidence: **99.31%**
4860. **`drivers/net/dsa/microchip/ksz_dcb.c`** -> AI Confidence: **99.31%**
4861. **`drivers/net/dsa/microchip/ksz_spi.c`** -> AI Confidence: **99.31%**
4862. **`drivers/net/dsa/mt7530.c`** -> AI Confidence: **99.31%**
4863. **`drivers/net/dsa/mv88e6xxx/chip.c`** -> AI Confidence: **99.31%**
4864. **`drivers/net/dsa/mv88e6xxx/port.c`** -> AI Confidence: **99.31%**
4865. **`drivers/net/dsa/mv88e6xxx/serdes.c`** -> AI Confidence: **99.31%**
4866. **`drivers/net/dsa/qca/qca8k-8xxx.c`** -> AI Confidence: **99.31%**
4867. **`drivers/net/dsa/realtek/rtl8365mb.c`** -> AI Confidence: **99.31%**
4868. **`drivers/net/dsa/realtek/rtl8366rb.c`** -> AI Confidence: **99.31%**
4869. **`drivers/net/dsa/sja1105/sja1105_main.c`** -> AI Confidence: **99.31%**
4870. **`drivers/net/ethernet/3com/3c509.c`** -> AI Confidence: **99.31%**
4871. **`drivers/net/ethernet/3com/3c574_cs.c`** -> AI Confidence: **99.31%**
4872. **`drivers/net/ethernet/3com/3c589_cs.c`** -> AI Confidence: **99.31%**
4873. **`drivers/net/ethernet/3com/3c59x.c`** -> AI Confidence: **99.31%**
4874. **`drivers/net/ethernet/8390/apne.c`** -> AI Confidence: **99.31%**
4875. **`drivers/net/ethernet/8390/axnet_cs.c`** -> AI Confidence: **99.31%**
4876. **`drivers/net/ethernet/8390/ne.c`** -> AI Confidence: **99.31%**
4877. **`drivers/net/ethernet/8390/pcnet_cs.c`** -> AI Confidence: **99.31%**
4878. **`drivers/net/ethernet/8390/wd.c`** -> AI Confidence: **99.31%**
4879. **`drivers/net/ethernet/adaptec/starfire.c`** -> AI Confidence: **99.31%**
4880. **`drivers/net/ethernet/aeroflex/greth.c`** -> AI Confidence: **99.31%**
4881. **`drivers/net/ethernet/agere/et131x.c`** -> AI Confidence: **99.31%**
4882. **`drivers/net/ethernet/airoha/airoha_eth.c`** -> AI Confidence: **99.31%**
4883. **`drivers/net/ethernet/alteon/acenic.c`** -> AI Confidence: **99.31%**
4884. **`drivers/net/ethernet/altera/altera_tse_main.c`** -> AI Confidence: **99.31%**
4885. **`drivers/net/ethernet/amazon/ena/ena_netdev.c`** -> AI Confidence: **99.31%**
4886. **`drivers/net/ethernet/amd/amd8111e.c`** -> AI Confidence: **99.31%**
4887. **`drivers/net/ethernet/amd/au1000_eth.c`** -> AI Confidence: **99.31%**
4888. **`drivers/net/ethernet/amd/declance.c`** -> AI Confidence: **99.31%**
4889. **`drivers/net/ethernet/amd/lance.c`** -> AI Confidence: **99.31%**
4890. **`drivers/net/ethernet/amd/nmclan_cs.c`** -> AI Confidence: **99.31%**
4891. **`drivers/net/ethernet/amd/pcnet32.c`** -> AI Confidence: **99.31%**
4892. **`drivers/net/ethernet/amd/sunlance.c`** -> AI Confidence: **99.31%**
4893. **`drivers/net/ethernet/amd/xgbe/xgbe-dev.c`** -> AI Confidence: **99.31%**
4894. **`drivers/net/ethernet/amd/xgbe/xgbe-drv.c`** -> AI Confidence: **99.31%**
4895. **`drivers/net/ethernet/amd/xgbe/xgbe-mdio.c`** -> AI Confidence: **99.31%**
4896. **`drivers/net/ethernet/amd/xgbe/xgbe-pci.c`** -> AI Confidence: **99.31%**
4897. **`drivers/net/ethernet/amd/xgbe/xgbe-phy-v2.c`** -> AI Confidence: **99.31%**
4898. **`drivers/net/ethernet/amd/xgbe/xgbe-platform.c`** -> AI Confidence: **99.31%**
4899. **`drivers/net/ethernet/apple/mace.c`** -> AI Confidence: **99.31%**
4900. **`drivers/net/ethernet/aquantia/atlantic/aq_drvinfo.c`** -> AI Confidence: **99.31%**
4901. **`drivers/net/ethernet/aquantia/atlantic/aq_main.c`** -> AI Confidence: **99.31%**
4902. **`drivers/net/ethernet/aquantia/atlantic/aq_nic.c`** -> AI Confidence: **99.31%**
4903. **`drivers/net/ethernet/aquantia/atlantic/aq_pci_func.c`** -> AI Confidence: **99.31%**
4904. **`drivers/net/ethernet/aquantia/atlantic/aq_ring.c`** -> AI Confidence: **99.31%**
4905. **`drivers/net/ethernet/arc/emac_main.c`** -> AI Confidence: **99.31%**
4906. **`drivers/net/ethernet/arc/emac_rockchip.c`** -> AI Confidence: **99.31%**
4907. **`drivers/net/ethernet/asix/ax88796c_main.c`** -> AI Confidence: **99.31%**
4908. **`drivers/net/ethernet/atheros/atlx/atl1.c`** -> AI Confidence: **99.31%**
4909. **`drivers/net/ethernet/atheros/atlx/atl2.c`** -> AI Confidence: **99.31%**
4910. **`drivers/net/ethernet/broadcom/asp2/bcmasp.c`** -> AI Confidence: **99.31%**
4911. **`drivers/net/ethernet/broadcom/asp2/bcmasp_intf.c`** -> AI Confidence: **99.31%**
4912. **`drivers/net/ethernet/broadcom/bcm63xx_enet.c`** -> AI Confidence: **99.31%**
4913. **`drivers/net/ethernet/broadcom/bcmsysport.c`** -> AI Confidence: **99.31%**
4914. **`drivers/net/ethernet/broadcom/bgmac.c`** -> AI Confidence: **99.31%**
4915. **`drivers/net/ethernet/broadcom/bnge/bnge_rmem.c`** -> AI Confidence: **99.31%**
4916. **`drivers/net/ethernet/broadcom/bnx2.c`** -> AI Confidence: **99.31%**
4917. **`drivers/net/ethernet/broadcom/bnx2x/bnx2x_cmn.c`** -> AI Confidence: **99.31%**
4918. **`drivers/net/ethernet/broadcom/bnx2x/bnx2x_dcb.c`** -> AI Confidence: **99.31%**
4919. **`drivers/net/ethernet/broadcom/bnx2x/bnx2x_ethtool.c`** -> AI Confidence: **99.31%**
4920. **`drivers/net/ethernet/broadcom/bnx2x/bnx2x_link.c`** -> AI Confidence: **99.31%**
4921. **`drivers/net/ethernet/broadcom/bnx2x/bnx2x_main.c`** -> AI Confidence: **99.31%**
4922. **`drivers/net/ethernet/broadcom/bnxt/bnxt.c`** -> AI Confidence: **99.31%**
4923. **`drivers/net/ethernet/broadcom/bnxt/bnxt_coredump.c`** -> AI Confidence: **99.31%**
4924. **`drivers/net/ethernet/broadcom/bnxt/bnxt_dcb.c`** -> AI Confidence: **99.31%**
4925. **`drivers/net/ethernet/broadcom/bnxt/bnxt_devlink.c`** -> AI Confidence: **99.31%**
4926. **`drivers/net/ethernet/broadcom/bnxt/bnxt_ethtool.c`** -> AI Confidence: **99.31%**
4927. **`drivers/net/ethernet/broadcom/bnxt/bnxt_hwmon.c`** -> AI Confidence: **99.31%**
4928. **`drivers/net/ethernet/broadcom/bnxt/bnxt_hwrm.c`** -> AI Confidence: **99.31%**
4929. **`drivers/net/ethernet/broadcom/bnxt/bnxt_sriov.c`** -> AI Confidence: **99.31%**
4930. **`drivers/net/ethernet/broadcom/genet/bcmgenet.c`** -> AI Confidence: **99.31%**
4931. **`drivers/net/ethernet/broadcom/genet/bcmmii.c`** -> AI Confidence: **99.31%**
4932. **`drivers/net/ethernet/brocade/bna/bnad_ethtool.c`** -> AI Confidence: **99.31%**
4933. **`drivers/net/ethernet/cavium/liquidio/cn23xx_vf_device.c`** -> AI Confidence: **99.31%**
4934. **`drivers/net/ethernet/cavium/liquidio/lio_core.c`** -> AI Confidence: **99.31%**
4935. **`drivers/net/ethernet/cavium/liquidio/lio_ethtool.c`** -> AI Confidence: **99.31%**
4936. **`drivers/net/ethernet/cavium/liquidio/octeon_device.c`** -> AI Confidence: **99.31%**
4937. **`drivers/net/ethernet/cavium/liquidio/octeon_mailbox.c`** -> AI Confidence: **99.31%**
4938. **`drivers/net/ethernet/cavium/liquidio/octeon_mem_ops.c`** -> AI Confidence: **99.31%**
4939. **`drivers/net/ethernet/cavium/liquidio/response_manager.c`** -> AI Confidence: **99.31%**
4940. **`drivers/net/ethernet/cavium/octeon/octeon_mgmt.c`** -> AI Confidence: **99.31%**
4941. **`drivers/net/ethernet/cavium/thunder/nic_main.c`** -> AI Confidence: **99.31%**
4942. **`drivers/net/ethernet/cavium/thunder/nicvf_ethtool.c`** -> AI Confidence: **99.31%**
4943. **`drivers/net/ethernet/cavium/thunder/nicvf_queues.c`** -> AI Confidence: **99.31%**
4944. **`drivers/net/ethernet/chelsio/cxgb/subr.c`** -> AI Confidence: **99.31%**
4945. **`drivers/net/ethernet/chelsio/cxgb3/cxgb3_main.c`** -> AI Confidence: **99.31%**
4946. **`drivers/net/ethernet/chelsio/cxgb3/l2t.c`** -> AI Confidence: **99.31%**
4947. **`drivers/net/ethernet/chelsio/cxgb4/cxgb4_debugfs.c`** -> AI Confidence: **99.31%**
4948. **`drivers/net/ethernet/chelsio/cxgb4/cxgb4_ethtool.c`** -> AI Confidence: **99.31%**
4949. **`drivers/net/ethernet/chelsio/cxgb4/cxgb4_filter.c`** -> AI Confidence: **99.31%**
4950. **`drivers/net/ethernet/chelsio/cxgb4/cxgb4_main.c`** -> AI Confidence: **99.31%**
4951. **`drivers/net/ethernet/chelsio/cxgb4/cxgb4_tc_flower.c`** -> AI Confidence: **99.31%**
4952. **`drivers/net/ethernet/chelsio/cxgb4/cxgb4_uld.c`** -> AI Confidence: **99.31%**
4953. **`drivers/net/ethernet/chelsio/cxgb4vf/sge.c`** -> AI Confidence: **99.31%**
4954. **`drivers/net/ethernet/chelsio/cxgb4vf/t4vf_hw.c`** -> AI Confidence: **99.31%**
4955. **`drivers/net/ethernet/chelsio/inline_crypto/chtls/chtls_io.c`** -> AI Confidence: **99.31%**
4956. **`drivers/net/ethernet/cirrus/cs89x0.c`** -> AI Confidence: **99.31%**
4957. **`drivers/net/ethernet/cirrus/mac89x0.c`** -> AI Confidence: **99.31%**
4958. **`drivers/net/ethernet/cisco/enic/enic_clsf.c`** -> AI Confidence: **99.31%**
4959. **`drivers/net/ethernet/cisco/enic/enic_main.c`** -> AI Confidence: **99.31%**
4960. **`drivers/net/ethernet/cisco/enic/enic_pp.c`** -> AI Confidence: **99.31%**
4961. **`drivers/net/ethernet/cisco/enic/enic_rq.c`** -> AI Confidence: **99.31%**
4962. **`drivers/net/ethernet/dec/tulip/de2104x.c`** -> AI Confidence: **99.31%**
4963. **`drivers/net/ethernet/dec/tulip/dmfe.c`** -> AI Confidence: **99.31%**
4964. **`drivers/net/ethernet/dec/tulip/tulip_core.c`** -> AI Confidence: **99.31%**
4965. **`drivers/net/ethernet/dlink/sundance.c`** -> AI Confidence: **99.31%**
4966. **`drivers/net/ethernet/emulex/benet/be_main.c`** -> AI Confidence: **99.31%**
4967. **`drivers/net/ethernet/fealnx.c`** -> AI Confidence: **99.31%**
4968. **`drivers/net/ethernet/freescale/dpaa2/dpaa2-eth.c`** -> AI Confidence: **99.31%**
4969. **`drivers/net/ethernet/freescale/fman/fman.c`** -> AI Confidence: **99.31%**
4970. **`drivers/net/ethernet/freescale/fman/fman_port.c`** -> AI Confidence: **99.31%**
4971. **`drivers/net/ethernet/freescale/fs_enet/mii-fec.c`** -> AI Confidence: **99.31%**
4972. **`drivers/net/ethernet/freescale/gianfar.c`** -> AI Confidence: **99.31%**
4973. **`drivers/net/ethernet/freescale/gianfar_ethtool.c`** -> AI Confidence: **99.31%**
4974. **`drivers/net/ethernet/freescale/ucc_geth.c`** -> AI Confidence: **99.31%**
4975. **`drivers/net/ethernet/fungible/funeth/funeth_ethtool.c`** -> AI Confidence: **99.31%**
4976. **`drivers/net/ethernet/fungible/funeth/funeth_tx.c`** -> AI Confidence: **99.31%**
4977. **`drivers/net/ethernet/google/gve/gve_rx_dqo.c`** -> AI Confidence: **99.31%**
4978. **`drivers/net/ethernet/hisilicon/hns/hns_dsaf_rcb.c`** -> AI Confidence: **99.31%**
4979. **`drivers/net/ethernet/huawei/hinic/hinic_ethtool.c`** -> AI Confidence: **99.31%**
4980. **`drivers/net/ethernet/huawei/hinic/hinic_main.c`** -> AI Confidence: **99.31%**
4981. **`drivers/net/ethernet/huawei/hinic3/hinic3_cmdq.c`** -> AI Confidence: **99.31%**
4982. **`drivers/net/ethernet/i825xx/ether1.c`** -> AI Confidence: **99.31%**
4983. **`drivers/net/ethernet/i825xx/sun3_82586.c`** -> AI Confidence: **99.31%**
4984. **`drivers/net/ethernet/ibm/ehea/ehea_main.c`** -> AI Confidence: **99.31%**
4985. **`drivers/net/ethernet/ibm/emac/core.c`** -> AI Confidence: **99.31%**
4986. **`drivers/net/ethernet/ibm/emac/mal.c`** -> AI Confidence: **99.31%**
4987. **`drivers/net/ethernet/ibm/emac/phy.c`** -> AI Confidence: **99.31%**
4988. **`drivers/net/ethernet/ibm/ibmveth.c`** -> AI Confidence: **99.31%**
4989. **`drivers/net/ethernet/ibm/ibmvnic.c`** -> AI Confidence: **99.31%**
4990. **`drivers/net/ethernet/intel/e100.c`** -> AI Confidence: **99.31%**
4991. **`drivers/net/ethernet/intel/e1000e/ethtool.c`** -> AI Confidence: **99.31%**
4992. **`drivers/net/ethernet/intel/e1000e/netdev.c`** -> AI Confidence: **99.31%**
4993. **`drivers/net/ethernet/intel/i40e/i40e_common.c`** -> AI Confidence: **99.31%**
4994. **`drivers/net/ethernet/intel/i40e/i40e_main.c`** -> AI Confidence: **99.31%**
4995. **`drivers/net/ethernet/intel/i40e/i40e_txrx.c`** -> AI Confidence: **99.31%**
4996. **`drivers/net/ethernet/intel/iavf/iavf_txrx.c`** -> AI Confidence: **99.31%**
4997. **`drivers/net/ethernet/intel/ice/ice_ethtool.c`** -> AI Confidence: **99.31%**
4998. **`drivers/net/ethernet/intel/ice/ice_fw_update.c`** -> AI Confidence: **99.31%**
4999. **`drivers/net/ethernet/intel/ice/ice_main.c`** -> AI Confidence: **99.31%**
5000. **`drivers/net/ethernet/intel/ice/ice_sriov.c`** -> AI Confidence: **99.31%**
5001. **`drivers/net/ethernet/intel/ice/ice_txrx.c`** -> AI Confidence: **99.31%**
5002. **`drivers/net/ethernet/intel/ice/ice_xsk.c`** -> AI Confidence: **99.31%**
5003. **`drivers/net/ethernet/intel/ice/virt/virtchnl.c`** -> AI Confidence: **99.31%**
5004. **`drivers/net/ethernet/intel/igb/e1000_82575.c`** -> AI Confidence: **99.31%**
5005. **`drivers/net/ethernet/intel/igb/e1000_mac.c`** -> AI Confidence: **99.31%**
5006. **`drivers/net/ethernet/intel/igb/igb_ethtool.c`** -> AI Confidence: **99.31%**
5007. **`drivers/net/ethernet/intel/igb/igb_hwmon.c`** -> AI Confidence: **99.31%**
5008. **`drivers/net/ethernet/intel/igb/igb_main.c`** -> AI Confidence: **99.31%**
5009. **`drivers/net/ethernet/intel/igc/igc_ptp.c`** -> AI Confidence: **99.31%**
5010. **`drivers/net/ethernet/intel/ixgbe/ixgbe_common.c`** -> AI Confidence: **99.31%**
5011. **`drivers/net/ethernet/intel/ixgbe/ixgbe_ethtool.c`** -> AI Confidence: **99.31%**
5012. **`drivers/net/ethernet/intel/ixgbe/ixgbe_fcoe.c`** -> AI Confidence: **99.31%**
5013. **`drivers/net/ethernet/intel/ixgbe/ixgbe_main.c`** -> AI Confidence: **99.31%**
5014. **`drivers/net/ethernet/intel/ixgbe/ixgbe_sriov.c`** -> AI Confidence: **99.31%**
5015. **`drivers/net/ethernet/jme.c`** -> AI Confidence: **99.31%**
5016. **`drivers/net/ethernet/marvell/mv643xx_eth.c`** -> AI Confidence: **99.31%**
5017. **`drivers/net/ethernet/marvell/mvpp2/mvpp2_main.c`** -> AI Confidence: **99.31%**
5018. **`drivers/net/ethernet/marvell/octeontx2/af/mbox.c`** -> AI Confidence: **99.31%**
5019. **`drivers/net/ethernet/marvell/octeontx2/af/mcs.c`** -> AI Confidence: **99.31%**
5020. **`drivers/net/ethernet/marvell/octeontx2/af/ptp.c`** -> AI Confidence: **99.31%**
5021. **`drivers/net/ethernet/marvell/octeontx2/af/rvu.c`** -> AI Confidence: **99.31%**
5022. **`drivers/net/ethernet/marvell/octeontx2/af/rvu_debugfs.c`** -> AI Confidence: **99.31%**
5023. **`drivers/net/ethernet/marvell/octeontx2/af/rvu_nix.c`** -> AI Confidence: **99.31%**
5024. **`drivers/net/ethernet/marvell/octeontx2/af/rvu_npc.c`** -> AI Confidence: **99.31%**
5025. **`drivers/net/ethernet/marvell/octeontx2/nic/otx2_ethtool.c`** -> AI Confidence: **99.31%**
5026. **`drivers/net/ethernet/marvell/octeontx2/nic/otx2_pf.c`** -> AI Confidence: **99.31%**
5027. **`drivers/net/ethernet/marvell/octeontx2/nic/otx2_vf.c`** -> AI Confidence: **99.31%**
5028. **`drivers/net/ethernet/marvell/octeontx2/nic/qos.c`** -> AI Confidence: **99.31%**
5029. **`drivers/net/ethernet/marvell/skge.c`** -> AI Confidence: **99.31%**
5030. **`drivers/net/ethernet/marvell/sky2.c`** -> AI Confidence: **99.31%**
5031. **`drivers/net/ethernet/mediatek/mtk_eth_soc.c`** -> AI Confidence: **99.31%**
5032. **`drivers/net/ethernet/mediatek/mtk_ppe_offload.c`** -> AI Confidence: **99.31%**
5033. **`drivers/net/ethernet/mediatek/mtk_wed.c`** -> AI Confidence: **99.31%**
5034. **`drivers/net/ethernet/mellanox/mlx4/en_ethtool.c`** -> AI Confidence: **99.31%**
5035. **`drivers/net/ethernet/mellanox/mlx4/en_main.c`** -> AI Confidence: **99.31%**
5036. **`drivers/net/ethernet/mellanox/mlx4/en_netdev.c`** -> AI Confidence: **99.31%**
5037. **`drivers/net/ethernet/mellanox/mlx4/eq.c`** -> AI Confidence: **99.31%**
5038. **`drivers/net/ethernet/mellanox/mlx4/fw.c`** -> AI Confidence: **99.31%**
5039. **`drivers/net/ethernet/mellanox/mlx4/icm.c`** -> AI Confidence: **99.31%**
5040. **`drivers/net/ethernet/mellanox/mlx4/main.c`** -> AI Confidence: **99.31%**
5041. **`drivers/net/ethernet/mellanox/mlx4/port.c`** -> AI Confidence: **99.31%**
5042. **`drivers/net/ethernet/mellanox/mlx4/resource_tracker.c`** -> AI Confidence: **99.31%**
5043. **`drivers/net/ethernet/mellanox/mlx5/core/cmd.c`** -> AI Confidence: **99.31%**
5044. **`drivers/net/ethernet/mellanox/mlx5/core/en_accel/ipsec.c`** -> AI Confidence: **99.31%**
5045. **`drivers/net/ethernet/mellanox/mlx5/core/esw/legacy.c`** -> AI Confidence: **99.31%**
5046. **`drivers/net/ethernet/mellanox/mlx5/core/steering/sws/fs_dr.c`** -> AI Confidence: **99.31%**
5047. **`drivers/net/ethernet/meta/fbnic/fbnic_devlink.c`** -> AI Confidence: **99.31%**
5048. **`drivers/net/ethernet/meta/fbnic/fbnic_fw.c`** -> AI Confidence: **99.31%**
5049. **`drivers/net/ethernet/meta/fbnic/fbnic_rpc.c`** -> AI Confidence: **99.31%**
5050. **`drivers/net/ethernet/microchip/enc28j60.c`** -> AI Confidence: **99.31%**
5051. **`drivers/net/ethernet/microchip/encx24j600-regmap.c`** -> AI Confidence: **99.31%**
5052. **`drivers/net/ethernet/microchip/lan743x_main.c`** -> AI Confidence: **99.31%**
5053. **`drivers/net/ethernet/microchip/lan743x_ptp.c`** -> AI Confidence: **99.31%**
5054. **`drivers/net/ethernet/microchip/sparx5/sparx5_main.c`** -> AI Confidence: **99.31%**
5055. **`drivers/net/ethernet/microchip/sparx5/sparx5_tc_flower.c`** -> AI Confidence: **99.31%**
5056. **`drivers/net/ethernet/microsoft/mana/gdma_main.c`** -> AI Confidence: **99.31%**
5057. **`drivers/net/ethernet/mscc/ocelot_ptp.c`** -> AI Confidence: **99.31%**
5058. **`drivers/net/ethernet/mscc/ocelot_vsc7514.c`** -> AI Confidence: **99.31%**
5059. **`drivers/net/ethernet/myricom/myri10ge/myri10ge.c`** -> AI Confidence: **99.31%**
5060. **`drivers/net/ethernet/natsemi/macsonic.c`** -> AI Confidence: **99.31%**
5061. **`drivers/net/ethernet/natsemi/natsemi.c`** -> AI Confidence: **99.31%**
5062. **`drivers/net/ethernet/natsemi/ns83820.c`** -> AI Confidence: **99.31%**
5063. **`drivers/net/ethernet/netronome/nfp/bpf/verifier.c`** -> AI Confidence: **99.31%**
5064. **`drivers/net/ethernet/netronome/nfp/crypto/ipsec.c`** -> AI Confidence: **99.31%**
5065. **`drivers/net/ethernet/netronome/nfp/nfd3/dp.c`** -> AI Confidence: **99.31%**
5066. **`drivers/net/ethernet/netronome/nfp/nfdk/dp.c`** -> AI Confidence: **99.31%**
5067. **`drivers/net/ethernet/netronome/nfp/nfp_main.c`** -> AI Confidence: **99.31%**
5068. **`drivers/net/ethernet/netronome/nfp/nfp_net_common.c`** -> AI Confidence: **99.31%**
5069. **`drivers/net/ethernet/netronome/nfp/nfp_net_main.c`** -> AI Confidence: **99.31%**
5070. **`drivers/net/ethernet/netronome/nfp/nfp_netvf_main.c`** -> AI Confidence: **99.31%**
5071. **`drivers/net/ethernet/nvidia/forcedeth.c`** -> AI Confidence: **99.31%**
5072. **`drivers/net/ethernet/packetengines/yellowfin.c`** -> AI Confidence: **99.31%**
5073. **`drivers/net/ethernet/pasemi/pasemi_mac.c`** -> AI Confidence: **99.31%**
5074. **`drivers/net/ethernet/pensando/ionic/ionic_bus_pci.c`** -> AI Confidence: **99.31%**
5075. **`drivers/net/ethernet/pensando/ionic/ionic_ethtool.c`** -> AI Confidence: **99.31%**
5076. **`drivers/net/ethernet/pensando/ionic/ionic_fw.c`** -> AI Confidence: **99.31%**
5077. **`drivers/net/ethernet/pensando/ionic/ionic_lif.c`** -> AI Confidence: **99.31%**
5078. **`drivers/net/ethernet/pensando/ionic/ionic_rx_filter.c`** -> AI Confidence: **99.31%**
5079. **`drivers/net/ethernet/qlogic/netxen/netxen_nic_ethtool.c`** -> AI Confidence: **99.31%**
5080. **`drivers/net/ethernet/qlogic/netxen/netxen_nic_init.c`** -> AI Confidence: **99.31%**
5081. **`drivers/net/ethernet/qlogic/netxen/netxen_nic_main.c`** -> AI Confidence: **99.31%**
5082. **`drivers/net/ethernet/qlogic/qed/qed_dev.c`** -> AI Confidence: **99.31%**
5083. **`drivers/net/ethernet/qlogic/qed/qed_int.c`** -> AI Confidence: **99.31%**
5084. **`drivers/net/ethernet/qlogic/qed/qed_iwarp.c`** -> AI Confidence: **99.31%**
5085. **`drivers/net/ethernet/qlogic/qed/qed_mcp.c`** -> AI Confidence: **99.31%**
5086. **`drivers/net/ethernet/qlogic/qede/qede_ethtool.c`** -> AI Confidence: **99.31%**
5087. **`drivers/net/ethernet/qlogic/qla3xxx.c`** -> AI Confidence: **99.31%**
5088. **`drivers/net/ethernet/qlogic/qlcnic/qlcnic_ethtool.c`** -> AI Confidence: **99.31%**
5089. **`drivers/net/ethernet/qlogic/qlcnic/qlcnic_io.c`** -> AI Confidence: **99.31%**
5090. **`drivers/net/ethernet/qlogic/qlcnic/qlcnic_main.c`** -> AI Confidence: **99.31%**
5091. **`drivers/net/ethernet/qualcomm/rmnet/rmnet_handlers.c`** -> AI Confidence: **99.31%**
5092. **`drivers/net/ethernet/renesas/ravb_main.c`** -> AI Confidence: **99.31%**
5093. **`drivers/net/ethernet/samsung/sxgbe/sxgbe_desc.c`** -> AI Confidence: **99.31%**
5094. **`drivers/net/ethernet/samsung/sxgbe/sxgbe_ethtool.c`** -> AI Confidence: **99.31%**
5095. **`drivers/net/ethernet/samsung/sxgbe/sxgbe_main.c`** -> AI Confidence: **99.31%**
5096. **`drivers/net/ethernet/seeq/ether3.c`** -> AI Confidence: **99.31%**
5097. **`drivers/net/ethernet/sfc/ef100.c`** -> AI Confidence: **99.31%**
5098. **`drivers/net/ethernet/sfc/ef100_netdev.c`** -> AI Confidence: **99.31%**
5099. **`drivers/net/ethernet/sfc/ef100_rx.c`** -> AI Confidence: **99.31%**
5100. **`drivers/net/ethernet/sfc/ef10_sriov.c`** -> AI Confidence: **99.31%**
5101. **`drivers/net/ethernet/sfc/efx_reflash.c`** -> AI Confidence: **99.31%**
5102. **`drivers/net/ethernet/sfc/falcon/ethtool.c`** -> AI Confidence: **99.31%**
5103. **`drivers/net/ethernet/sfc/falcon/farch.c`** -> AI Confidence: **99.31%**
5104. **`drivers/net/ethernet/sfc/falcon/nic.c`** -> AI Confidence: **99.31%**
5105. **`drivers/net/ethernet/sfc/falcon/qt202x_phy.c`** -> AI Confidence: **99.31%**
5106. **`drivers/net/ethernet/sfc/mae.c`** -> AI Confidence: **99.31%**
5107. **`drivers/net/ethernet/sfc/mcdi.c`** -> AI Confidence: **99.31%**
5108. **`drivers/net/ethernet/sfc/mcdi_mon.c`** -> AI Confidence: **99.31%**
5109. **`drivers/net/ethernet/sfc/nic.c`** -> AI Confidence: **99.31%**
5110. **`drivers/net/ethernet/sfc/rx.c`** -> AI Confidence: **99.31%**
5111. **`drivers/net/ethernet/sfc/siena/ethtool_common.c`** -> AI Confidence: **99.31%**
5112. **`drivers/net/ethernet/sfc/siena/mcdi.c`** -> AI Confidence: **99.31%**
5113. **`drivers/net/ethernet/sfc/siena/mcdi_mon.c`** -> AI Confidence: **99.31%**
5114. **`drivers/net/ethernet/sfc/siena/nic.c`** -> AI Confidence: **99.31%**
5115. **`drivers/net/ethernet/sfc/siena/rx.c`** -> AI Confidence: **99.31%**
5116. **`drivers/net/ethernet/sfc/tc.c`** -> AI Confidence: **99.31%**
5117. **`drivers/net/ethernet/sfc/tx.c`** -> AI Confidence: **99.31%**
5118. **`drivers/net/ethernet/sfc/tx_tso.c`** -> AI Confidence: **99.31%**
5119. **`drivers/net/ethernet/sgi/meth.c`** -> AI Confidence: **99.31%**
5120. **`drivers/net/ethernet/silan/sc92031.c`** -> AI Confidence: **99.31%**
5121. **`drivers/net/ethernet/sis/sis900.c`** -> AI Confidence: **99.31%**
5122. **`drivers/net/ethernet/smsc/smc9194.c`** -> AI Confidence: **99.31%**
5123. **`drivers/net/ethernet/smsc/smc91c92_cs.c`** -> AI Confidence: **99.31%**
5124. **`drivers/net/ethernet/smsc/smc91x.c`** -> AI Confidence: **99.31%**
5125. **`drivers/net/ethernet/smsc/smsc911x.c`** -> AI Confidence: **99.31%**
5126. **`drivers/net/ethernet/stmicro/stmmac/dwmac-ipq806x.c`** -> AI Confidence: **99.31%**
5127. **`drivers/net/ethernet/stmicro/stmmac/dwmac-loongson.c`** -> AI Confidence: **99.31%**
5128. **`drivers/net/ethernet/stmicro/stmmac/dwmac-mediatek.c`** -> AI Confidence: **99.31%**
5129. **`drivers/net/ethernet/stmicro/stmmac/dwmac-socfpga.c`** -> AI Confidence: **99.31%**
5130. **`drivers/net/ethernet/stmicro/stmmac/dwmac-stm32.c`** -> AI Confidence: **99.31%**
5131. **`drivers/net/ethernet/stmicro/stmmac/dwmac-sun55i.c`** -> AI Confidence: **99.31%**
5132. **`drivers/net/ethernet/stmicro/stmmac/dwmac-thead.c`** -> AI Confidence: **99.31%**
5133. **`drivers/net/ethernet/stmicro/stmmac/dwmac1000_core.c`** -> AI Confidence: **99.31%**
5134. **`drivers/net/ethernet/stmicro/stmmac/dwmac4_core.c`** -> AI Confidence: **99.31%**
5135. **`drivers/net/ethernet/stmicro/stmmac/stmmac_main.c`** -> AI Confidence: **99.31%**
5136. **`drivers/net/ethernet/stmicro/stmmac/stmmac_platform.c`** -> AI Confidence: **99.31%**
5137. **`drivers/net/ethernet/stmicro/stmmac/stmmac_selftests.c`** -> AI Confidence: **99.31%**
5138. **`drivers/net/ethernet/sun/cassini.c`** -> AI Confidence: **99.31%**
5139. **`drivers/net/ethernet/sun/niu.c`** -> AI Confidence: **99.31%**
5140. **`drivers/net/ethernet/sun/sunbmac.c`** -> AI Confidence: **99.31%**
5141. **`drivers/net/ethernet/sun/sungem.c`** -> AI Confidence: **99.31%**
5142. **`drivers/net/ethernet/sun/sunhme.c`** -> AI Confidence: **99.31%**
5143. **`drivers/net/ethernet/sun/sunqe.c`** -> AI Confidence: **99.31%**
5144. **`drivers/net/ethernet/sun/sunvnet_common.c`** -> AI Confidence: **99.31%**
5145. **`drivers/net/ethernet/sunplus/spl2sw_driver.c`** -> AI Confidence: **99.31%**
5146. **`drivers/net/ethernet/synopsys/dwc-xlgmac-hw.c`** -> AI Confidence: **99.31%**
5147. **`drivers/net/ethernet/ti/cpsw.c`** -> AI Confidence: **99.31%**
5148. **`drivers/net/ethernet/ti/cpsw_priv.c`** -> AI Confidence: **99.31%**
5149. **`drivers/net/ethernet/ti/davinci_emac.c`** -> AI Confidence: **99.31%**
5150. **`drivers/net/ethernet/ti/icssg/icssg_common.c`** -> AI Confidence: **99.31%**
5151. **`drivers/net/ethernet/ti/icssg/icssg_config.c`** -> AI Confidence: **99.31%**
5152. **`drivers/net/ethernet/ti/icssg/icssg_prueth.c`** -> AI Confidence: **99.31%**
5153. **`drivers/net/ethernet/ti/icssg/icssg_prueth_sr1.c`** -> AI Confidence: **99.31%**
5154. **`drivers/net/ethernet/ti/icssm/icssm_prueth.c`** -> AI Confidence: **99.31%**
5155. **`drivers/net/ethernet/ti/tlan.c`** -> AI Confidence: **99.31%**
5156. **`drivers/net/ethernet/toshiba/ps3_gelic_net.c`** -> AI Confidence: **99.31%**
5157. **`drivers/net/ethernet/toshiba/ps3_gelic_wireless.c`** -> AI Confidence: **99.31%**
5158. **`drivers/net/ethernet/tundra/tsi108_eth.c`** -> AI Confidence: **99.31%**
5159. **`drivers/net/ethernet/via/via-velocity.c`** -> AI Confidence: **99.31%**
5160. **`drivers/net/ethernet/wangxun/ngbe/ngbe_main.c`** -> AI Confidence: **99.31%**
5161. **`drivers/net/ethernet/wangxun/ngbevf/ngbevf_main.c`** -> AI Confidence: **99.31%**
5162. **`drivers/net/ethernet/wangxun/txgbe/txgbe_aml.c`** -> AI Confidence: **99.31%**
5163. **`drivers/net/ethernet/wangxun/txgbe/txgbe_ethtool.c`** -> AI Confidence: **99.31%**
5164. **`drivers/net/ethernet/wangxun/txgbe/txgbe_fdir.c`** -> AI Confidence: **99.31%**
5165. **`drivers/net/ethernet/wangxun/txgbe/txgbe_main.c`** -> AI Confidence: **99.31%**
5166. **`drivers/net/ethernet/wangxun/txgbevf/txgbevf_main.c`** -> AI Confidence: **99.31%**
5167. **`drivers/net/ethernet/xilinx/ll_temac_main.c`** -> AI Confidence: **99.31%**
5168. **`drivers/net/ethernet/xilinx/xilinx_axienet_main.c`** -> AI Confidence: **99.31%**
5169. **`drivers/net/ethernet/xscale/ixp4xx_eth.c`** -> AI Confidence: **99.31%**
5170. **`drivers/net/fddi/defxx.c`** -> AI Confidence: **99.31%**
5171. **`drivers/net/fddi/defza.c`** -> AI Confidence: **99.31%**
5172. **`drivers/net/fddi/skfp/drvfbi.c`** -> AI Confidence: **99.31%**
5173. **`drivers/net/fddi/skfp/skfddi.c`** -> AI Confidence: **99.31%**
5174. **`drivers/net/fddi/skfp/smt.c`** -> AI Confidence: **99.31%**
5175. **`drivers/net/fjes/fjes_main.c`** -> AI Confidence: **99.31%**
5176. **`drivers/net/hamradio/6pack.c`** -> AI Confidence: **99.31%**
5177. **`drivers/net/hamradio/baycom_ser_fdx.c`** -> AI Confidence: **99.31%**
5178. **`drivers/net/hamradio/baycom_ser_hdx.c`** -> AI Confidence: **99.31%**
5179. **`drivers/net/hamradio/hdlcdrv.c`** -> AI Confidence: **99.31%**
5180. **`drivers/net/hamradio/mkiss.c`** -> AI Confidence: **99.31%**
5181. **`drivers/net/hamradio/scc.c`** -> AI Confidence: **99.31%**
5182. **`drivers/net/hamradio/yam.c`** -> AI Confidence: **99.31%**
5183. **`drivers/net/hyperv/netvsc_bpf.c`** -> AI Confidence: **99.31%**
5184. **`drivers/net/hyperv/rndis_filter.c`** -> AI Confidence: **99.31%**
5185. **`drivers/net/ieee802154/adf7242.c`** -> AI Confidence: **99.31%**
5186. **`drivers/net/ieee802154/ca8210.c`** -> AI Confidence: **99.31%**
5187. **`drivers/net/ieee802154/cc2520.c`** -> AI Confidence: **99.31%**
5188. **`drivers/net/ieee802154/mcr20a.c`** -> AI Confidence: **99.31%**
5189. **`drivers/net/ieee802154/mrf24j40.c`** -> AI Confidence: **99.31%**
5190. **`drivers/net/mctp/mctp-serial.c`** -> AI Confidence: **99.31%**
5191. **`drivers/net/mdio/mdio-mux-mmioreg.c`** -> AI Confidence: **99.31%**
5192. **`drivers/net/mdio/mdio-realtek-rtl9300.c`** -> AI Confidence: **99.31%**
5193. **`drivers/net/mdio/mdio-thunder.c`** -> AI Confidence: **99.31%**
5194. **`drivers/net/ovpn/io.c`** -> AI Confidence: **99.31%**
5195. **`drivers/net/ovpn/netlink.c`** -> AI Confidence: **99.31%**
5196. **`drivers/net/pcs/pcs-xpcs.c`** -> AI Confidence: **99.31%**
5197. **`drivers/net/phy/aquantia/aquantia_main.c`** -> AI Confidence: **99.31%**
5198. **`drivers/net/phy/bcm54140.c`** -> AI Confidence: **99.31%**
5199. **`drivers/net/phy/bcm7xxx.c`** -> AI Confidence: **99.31%**
5200. **`drivers/net/phy/broadcom.c`** -> AI Confidence: **99.31%**
5201. **`drivers/net/phy/dp83822.c`** -> AI Confidence: **99.31%**
5202. **`drivers/net/phy/dp83867.c`** -> AI Confidence: **99.31%**
5203. **`drivers/net/phy/dp83869.c`** -> AI Confidence: **99.31%**
5204. **`drivers/net/phy/lxt.c`** -> AI Confidence: **99.31%**
5205. **`drivers/net/phy/marvell.c`** -> AI Confidence: **99.31%**
5206. **`drivers/net/phy/mdio_bus_provider.c`** -> AI Confidence: **99.31%**
5207. **`drivers/net/phy/mediatek/mtk-ge-soc.c`** -> AI Confidence: **99.31%**
5208. **`drivers/net/phy/meson-gxl.c`** -> AI Confidence: **99.31%**
5209. **`drivers/net/phy/microchip.c`** -> AI Confidence: **99.31%**
5210. **`drivers/net/phy/microchip_t1.c`** -> AI Confidence: **99.31%**
5211. **`drivers/net/phy/mscc/mscc_main.c`** -> AI Confidence: **99.31%**
5212. **`drivers/net/phy/mxl-gpy.c`** -> AI Confidence: **99.31%**
5213. **`drivers/net/phy/ncn26000.c`** -> AI Confidence: **99.31%**
5214. **`drivers/net/phy/phy-c45.c`** -> AI Confidence: **99.31%**
5215. **`drivers/net/phy/phy-core.c`** -> AI Confidence: **99.31%**
5216. **`drivers/net/phy/phylink.c`** -> AI Confidence: **99.31%**
5217. **`drivers/net/phy/qcom/qca807x.c`** -> AI Confidence: **99.31%**
5218. **`drivers/net/phy/sfp-bus.c`** -> AI Confidence: **99.31%**
5219. **`drivers/net/phy/sfp.c`** -> AI Confidence: **99.31%**
5220. **`drivers/net/phy/smsc.c`** -> AI Confidence: **99.31%**
5221. **`drivers/net/ppp/bsd_comp.c`** -> AI Confidence: **99.31%**
5222. **`drivers/net/ppp/ppp_async.c`** -> AI Confidence: **99.31%**
5223. **`drivers/net/ppp/ppp_deflate.c`** -> AI Confidence: **99.31%**
5224. **`drivers/net/ppp/ppp_synctty.c`** -> AI Confidence: **99.31%**
5225. **`drivers/net/ppp/pppox.c`** -> AI Confidence: **99.31%**
5226. **`drivers/net/ppp/pptp.c`** -> AI Confidence: **99.31%**
5227. **`drivers/net/pse-pd/pse_core.c`** -> AI Confidence: **99.31%**
5228. **`drivers/net/slip/slhc.c`** -> AI Confidence: **99.31%**
5229. **`drivers/net/slip/slip.c`** -> AI Confidence: **99.31%**
5230. **`drivers/net/tun.c`** -> AI Confidence: **99.31%**
5231. **`drivers/net/usb/aqc111.c`** -> AI Confidence: **99.31%**
5232. **`drivers/net/usb/catc.c`** -> AI Confidence: **99.31%**
5233. **`drivers/net/usb/cdc_eem.c`** -> AI Confidence: **99.31%**
5234. **`drivers/net/usb/cdc_ether.c`** -> AI Confidence: **99.31%**
5235. **`drivers/net/usb/cdc_mbim.c`** -> AI Confidence: **99.31%**
5236. **`drivers/net/usb/cdc_ncm.c`** -> AI Confidence: **99.31%**
5237. **`drivers/net/usb/hso.c`** -> AI Confidence: **99.31%**
5238. **`drivers/net/usb/kalmia.c`** -> AI Confidence: **99.31%**
5239. **`drivers/net/usb/lan78xx.c`** -> AI Confidence: **99.31%**
5240. **`drivers/net/usb/lg-vl600.c`** -> AI Confidence: **99.31%**
5241. **`drivers/net/usb/pegasus.c`** -> AI Confidence: **99.31%**
5242. **`drivers/net/usb/rndis_host.c`** -> AI Confidence: **99.31%**
5243. **`drivers/net/usb/rtl8150.c`** -> AI Confidence: **99.31%**
5244. **`drivers/net/usb/smsc75xx.c`** -> AI Confidence: **99.31%**
5245. **`drivers/net/usb/smsc95xx.c`** -> AI Confidence: **99.31%**
5246. **`drivers/net/usb/sr9800.c`** -> AI Confidence: **99.31%**
5247. **`drivers/net/usb/usbnet.c`** -> AI Confidence: **99.31%**
5248. **`drivers/net/usb/zaurus.c`** -> AI Confidence: **99.31%**
5249. **`drivers/net/vxlan/vxlan_core.c`** -> AI Confidence: **99.31%**
5250. **`drivers/net/wan/c101.c`** -> AI Confidence: **99.31%**
5251. **`drivers/net/wan/farsync.c`** -> AI Confidence: **99.31%**
5252. **`drivers/net/wan/framer/pef2256/pef2256.c`** -> AI Confidence: **99.31%**
5253. **`drivers/net/wan/fsl_ucc_hdlc.c`** -> AI Confidence: **99.31%**
5254. **`drivers/net/wan/hdlc_fr.c`** -> AI Confidence: **99.31%**
5255. **`drivers/net/wan/hdlc_ppp.c`** -> AI Confidence: **99.31%**
5256. **`drivers/net/wan/ixp4xx_hss.c`** -> AI Confidence: **99.31%**
5257. **`drivers/net/wan/n2.c`** -> AI Confidence: **99.31%**
5258. **`drivers/net/wan/pc300too.c`** -> AI Confidence: **99.31%**
5259. **`drivers/net/wan/pci200syn.c`** -> AI Confidence: **99.31%**
5260. **`drivers/net/wan/wanxl.c`** -> AI Confidence: **99.31%**
5261. **`drivers/net/wireguard/netlink.c`** -> AI Confidence: **99.31%**
5262. **`drivers/net/wireguard/receive.c`** -> AI Confidence: **99.31%**
5263. **`drivers/net/wireguard/socket.c`** -> AI Confidence: **99.31%**
5264. **`drivers/net/wireless/ath/ar5523/ar5523.c`** -> AI Confidence: **99.31%**
5265. **`drivers/net/wireless/ath/ath10k/core.c`** -> AI Confidence: **99.31%**
5266. **`drivers/net/wireless/ath/ath10k/hw.c`** -> AI Confidence: **99.31%**
5267. **`drivers/net/wireless/ath/ath10k/mac.c`** -> AI Confidence: **99.31%**
5268. **`drivers/net/wireless/ath/ath10k/qmi.c`** -> AI Confidence: **99.31%**
5269. **`drivers/net/wireless/ath/ath10k/wow.c`** -> AI Confidence: **99.31%**
5270. **`drivers/net/wireless/ath/ath11k/dp.c`** -> AI Confidence: **99.31%**
5271. **`drivers/net/wireless/ath/ath11k/dp_tx.c`** -> AI Confidence: **99.31%**
5272. **`drivers/net/wireless/ath/ath11k/mac.c`** -> AI Confidence: **99.31%**
5273. **`drivers/net/wireless/ath/ath11k/pci.c`** -> AI Confidence: **99.31%**
5274. **`drivers/net/wireless/ath/ath11k/testmode.c`** -> AI Confidence: **99.31%**
5275. **`drivers/net/wireless/ath/ath11k/wow.c`** -> AI Confidence: **99.31%**
5276. **`drivers/net/wireless/ath/ath12k/core.c`** -> AI Confidence: **99.31%**
5277. **`drivers/net/wireless/ath/ath12k/debugfs_sta.c`** -> AI Confidence: **99.31%**
5278. **`drivers/net/wireless/ath/ath12k/dp.c`** -> AI Confidence: **99.31%**
5279. **`drivers/net/wireless/ath/ath12k/mac.c`** -> AI Confidence: **99.31%**
5280. **`drivers/net/wireless/ath/ath12k/mhi.c`** -> AI Confidence: **99.31%**
5281. **`drivers/net/wireless/ath/ath12k/wifi7/dp.c`** -> AI Confidence: **99.31%**
5282. **`drivers/net/wireless/ath/ath12k/wifi7/dp_mon.c`** -> AI Confidence: **99.31%**
5283. **`drivers/net/wireless/ath/ath12k/wifi7/dp_tx.c`** -> AI Confidence: **99.31%**
5284. **`drivers/net/wireless/ath/ath12k/wow.c`** -> AI Confidence: **99.31%**
5285. **`drivers/net/wireless/ath/ath5k/base.c`** -> AI Confidence: **99.31%**
5286. **`drivers/net/wireless/ath/ath5k/debug.c`** -> AI Confidence: **99.31%**
5287. **`drivers/net/wireless/ath/ath5k/phy.c`** -> AI Confidence: **99.31%**
5288. **`drivers/net/wireless/ath/ath6kl/cfg80211.c`** -> AI Confidence: **99.31%**
5289. **`drivers/net/wireless/ath/ath6kl/core.c`** -> AI Confidence: **99.31%**
5290. **`drivers/net/wireless/ath/ath6kl/hif.c`** -> AI Confidence: **99.31%**
5291. **`drivers/net/wireless/ath/ath6kl/init.c`** -> AI Confidence: **99.31%**
5292. **`drivers/net/wireless/ath/ath9k/hw.c`** -> AI Confidence: **99.31%**
5293. **`drivers/net/wireless/ath/carl9170/rx.c`** -> AI Confidence: **99.31%**
5294. **`drivers/net/wireless/ath/carl9170/usb.c`** -> AI Confidence: **99.31%**
5295. **`drivers/net/wireless/ath/wcn36xx/smd.c`** -> AI Confidence: **99.31%**
5296. **`drivers/net/wireless/ath/wil6210/main.c`** -> AI Confidence: **99.31%**
5297. **`drivers/net/wireless/ath/wil6210/pcie_bus.c`** -> AI Confidence: **99.31%**
5298. **`drivers/net/wireless/ath/wil6210/pmc.c`** -> AI Confidence: **99.31%**
5299. **`drivers/net/wireless/ath/wil6210/txrx.c`** -> AI Confidence: **99.31%**
5300. **`drivers/net/wireless/atmel/at76c50x-usb.c`** -> AI Confidence: **99.31%**
5301. **`drivers/net/wireless/broadcom/b43/dma.c`** -> AI Confidence: **99.31%**
5302. **`drivers/net/wireless/broadcom/b43/lo.c`** -> AI Confidence: **99.31%**
5303. **`drivers/net/wireless/broadcom/b43/main.c`** -> AI Confidence: **99.31%**
5304. **`drivers/net/wireless/broadcom/b43/phy_g.c`** -> AI Confidence: **99.31%**
5305. **`drivers/net/wireless/broadcom/b43/phy_lp.c`** -> AI Confidence: **99.31%**
5306. **`drivers/net/wireless/broadcom/b43/pio.c`** -> AI Confidence: **99.31%**
5307. **`drivers/net/wireless/broadcom/b43legacy/dma.c`** -> AI Confidence: **99.31%**
5308. **`drivers/net/wireless/broadcom/b43legacy/main.c`** -> AI Confidence: **99.31%**
5309. **`drivers/net/wireless/broadcom/brcm80211/brcmfmac/bcmsdh.c`** -> AI Confidence: **99.31%**
5310. **`drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c`** -> AI Confidence: **99.31%**
5311. **`drivers/net/wireless/broadcom/brcm80211/brcmfmac/common.c`** -> AI Confidence: **99.31%**
5312. **`drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.c`** -> AI Confidence: **99.31%**
5313. **`drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwsignal.c`** -> AI Confidence: **99.31%**
5314. **`drivers/net/wireless/broadcom/brcm80211/brcmfmac/pno.c`** -> AI Confidence: **99.31%**
5315. **`drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.c`** -> AI Confidence: **99.31%**
5316. **`drivers/net/wireless/broadcom/brcm80211/brcmsmac/antsel.c`** -> AI Confidence: **99.31%**
5317. **`drivers/net/wireless/broadcom/brcm80211/brcmsmac/channel.c`** -> AI Confidence: **99.31%**
5318. **`drivers/net/wireless/broadcom/brcm80211/brcmsmac/main.c`** -> AI Confidence: **99.31%**
5319. **`drivers/net/wireless/broadcom/brcm80211/brcmsmac/phy/phy_cmn.c`** -> AI Confidence: **99.31%**
5320. **`drivers/net/wireless/broadcom/brcm80211/brcmsmac/phy/phy_lcn.c`** -> AI Confidence: **99.31%**
5321. **`drivers/net/wireless/broadcom/brcm80211/brcmsmac/pmu.c`** -> AI Confidence: **99.31%**
5322. **`drivers/net/wireless/broadcom/brcm80211/brcmsmac/stf.c`** -> AI Confidence: **99.31%**
5323. **`drivers/net/wireless/intel/ipw2x00/ipw2100.c`** -> AI Confidence: **99.31%**
5324. **`drivers/net/wireless/intel/ipw2x00/libipw_geo.c`** -> AI Confidence: **99.31%**
5325. **`drivers/net/wireless/intel/ipw2x00/libipw_rx.c`** -> AI Confidence: **99.31%**
5326. **`drivers/net/wireless/intel/iwlegacy/3945-mac.c`** -> AI Confidence: **99.31%**
5327. **`drivers/net/wireless/intel/iwlegacy/3945-rs.c`** -> AI Confidence: **99.31%**
5328. **`drivers/net/wireless/intel/iwlegacy/4965-rs.c`** -> AI Confidence: **99.31%**
5329. **`drivers/net/wireless/intel/iwlegacy/common.c`** -> AI Confidence: **99.31%**
5330. **`drivers/net/wireless/intel/iwlwifi/dvm/eeprom.c`** -> AI Confidence: **99.31%**
5331. **`drivers/net/wireless/intel/iwlwifi/dvm/mac80211.c`** -> AI Confidence: **99.31%**
5332. **`drivers/net/wireless/intel/iwlwifi/dvm/main.c`** -> AI Confidence: **99.31%**
5333. **`drivers/net/wireless/intel/iwlwifi/dvm/power.c`** -> AI Confidence: **99.31%**
5334. **`drivers/net/wireless/intel/iwlwifi/dvm/rs.c`** -> AI Confidence: **99.31%**
5335. **`drivers/net/wireless/intel/iwlwifi/dvm/tx.c`** -> AI Confidence: **99.31%**
5336. **`drivers/net/wireless/intel/iwlwifi/fw/dump.c`** -> AI Confidence: **99.31%**
5337. **`drivers/net/wireless/intel/iwlwifi/fw/pnvm.c`** -> AI Confidence: **99.31%**
5338. **`drivers/net/wireless/intel/iwlwifi/iwl-nvm-parse.c`** -> AI Confidence: **99.31%**
5339. **`drivers/net/wireless/intel/iwlwifi/mld/ftm-initiator.c`** -> AI Confidence: **99.31%**
5340. **`drivers/net/wireless/intel/iwlwifi/mld/regulatory.c`** -> AI Confidence: **99.31%**
5341. **`drivers/net/wireless/intel/iwlwifi/mld/rx.c`** -> AI Confidence: **99.31%**
5342. **`drivers/net/wireless/intel/iwlwifi/mld/tlc.c`** -> AI Confidence: **99.31%**
5343. **`drivers/net/wireless/intel/iwlwifi/mld/tx.c`** -> AI Confidence: **99.31%**
5344. **`drivers/net/wireless/intel/iwlwifi/mvm/d3.c`** -> AI Confidence: **99.31%**
5345. **`drivers/net/wireless/intel/iwlwifi/mvm/fw.c`** -> AI Confidence: **99.31%**
5346. **`drivers/net/wireless/intel/iwlwifi/mvm/mac80211.c`** -> AI Confidence: **99.31%**
5347. **`drivers/net/wireless/intel/iwlwifi/mvm/nvm.c`** -> AI Confidence: **99.31%**
5348. **`drivers/net/wireless/intel/iwlwifi/mvm/power.c`** -> AI Confidence: **99.31%**
5349. **`drivers/net/wireless/intel/iwlwifi/mvm/rs.c`** -> AI Confidence: **99.31%**
5350. **`drivers/net/wireless/intel/iwlwifi/mvm/tx.c`** -> AI Confidence: **99.31%**
5351. **`drivers/net/wireless/intel/iwlwifi/pcie/drv.c`** -> AI Confidence: **99.31%**
5352. **`drivers/net/wireless/intel/iwlwifi/pcie/gen1_2/rx.c`** -> AI Confidence: **99.31%**
5353. **`drivers/net/wireless/intel/iwlwifi/pcie/gen1_2/tx-gen2.c`** -> AI Confidence: **99.31%**
5354. **`drivers/net/wireless/intel/iwlwifi/pcie/gen1_2/tx.c`** -> AI Confidence: **99.31%**
5355. **`drivers/net/wireless/intersil/p54/eeprom.c`** -> AI Confidence: **99.31%**
5356. **`drivers/net/wireless/intersil/p54/main.c`** -> AI Confidence: **99.31%**
5357. **`drivers/net/wireless/intersil/p54/p54usb.c`** -> AI Confidence: **99.31%**
5358. **`drivers/net/wireless/intersil/p54/txrx.c`** -> AI Confidence: **99.31%**
5359. **`drivers/net/wireless/marvell/libertas/cfg.c`** -> AI Confidence: **99.31%**
5360. **`drivers/net/wireless/marvell/libertas/cmd.c`** -> AI Confidence: **99.31%**
5361. **`drivers/net/wireless/marvell/libertas/if_sdio.c`** -> AI Confidence: **99.31%**
5362. **`drivers/net/wireless/marvell/libertas/if_spi.c`** -> AI Confidence: **99.31%**
5363. **`drivers/net/wireless/marvell/libertas/if_usb.c`** -> AI Confidence: **99.31%**
5364. **`drivers/net/wireless/marvell/libertas/main.c`** -> AI Confidence: **99.31%**
5365. **`drivers/net/wireless/marvell/libertas/tx.c`** -> AI Confidence: **99.31%**
5366. **`drivers/net/wireless/marvell/libertas_tf/if_usb.c`** -> AI Confidence: **99.31%**
5367. **`drivers/net/wireless/marvell/mwifiex/11n_aggr.c`** -> AI Confidence: **99.31%**
5368. **`drivers/net/wireless/marvell/mwifiex/cmdevt.c`** -> AI Confidence: **99.31%**
5369. **`drivers/net/wireless/marvell/mwifiex/join.c`** -> AI Confidence: **99.31%**
5370. **`drivers/net/wireless/marvell/mwifiex/pcie.c`** -> AI Confidence: **99.31%**
5371. **`drivers/net/wireless/marvell/mwifiex/sta_cmd.c`** -> AI Confidence: **99.31%**
5372. **`drivers/net/wireless/marvell/mwifiex/sta_cmdresp.c`** -> AI Confidence: **99.31%**
5373. **`drivers/net/wireless/marvell/mwifiex/sta_event.c`** -> AI Confidence: **99.31%**
5374. **`drivers/net/wireless/marvell/mwifiex/sta_ioctl.c`** -> AI Confidence: **99.31%**
5375. **`drivers/net/wireless/marvell/mwifiex/sta_rx.c`** -> AI Confidence: **99.31%**
5376. **`drivers/net/wireless/marvell/mwifiex/wmm.c`** -> AI Confidence: **99.31%**
5377. **`drivers/net/wireless/mediatek/mt76/eeprom.c`** -> AI Confidence: **99.31%**
5378. **`drivers/net/wireless/mediatek/mt76/mt7615/mac.c`** -> AI Confidence: **99.31%**
5379. **`drivers/net/wireless/mediatek/mt76/mt76x0/eeprom.c`** -> AI Confidence: **99.31%**
5380. **`drivers/net/wireless/mediatek/mt76/mt7915/init.c`** -> AI Confidence: **99.31%**
5381. **`drivers/net/wireless/mediatek/mt76/mt7915/mac.c`** -> AI Confidence: **99.31%**
5382. **`drivers/net/wireless/mediatek/mt76/mt7915/soc.c`** -> AI Confidence: **99.31%**
5383. **`drivers/net/wireless/mediatek/mt76/mt7996/init.c`** -> AI Confidence: **99.31%**
5384. **`drivers/net/wireless/mediatek/mt76/mt7996/mac.c`** -> AI Confidence: **99.31%**
5385. **`drivers/net/wireless/mediatek/mt76/mt7996/mmio.c`** -> AI Confidence: **99.31%**
5386. **`drivers/net/wireless/mediatek/mt76/sdio.c`** -> AI Confidence: **99.31%**
5387. **`drivers/net/wireless/mediatek/mt76/sdio_txrx.c`** -> AI Confidence: **99.31%**
5388. **`drivers/net/wireless/mediatek/mt7601u/eeprom.c`** -> AI Confidence: **99.31%**
5389. **`drivers/net/wireless/microchip/wilc1000/netdev.c`** -> AI Confidence: **99.31%**
5390. **`drivers/net/wireless/purelifi/plfxlc/usb.c`** -> AI Confidence: **99.31%**
5391. **`drivers/net/wireless/quantenna/qtnfmac/commands.c`** -> AI Confidence: **99.31%**
5392. **`drivers/net/wireless/quantenna/qtnfmac/event.c`** -> AI Confidence: **99.31%**
5393. **`drivers/net/wireless/ralink/rt2x00/rt2400pci.c`** -> AI Confidence: **99.31%**
5394. **`drivers/net/wireless/ralink/rt2x00/rt2500pci.c`** -> AI Confidence: **99.31%**
5395. **`drivers/net/wireless/ralink/rt2x00/rt2500usb.c`** -> AI Confidence: **99.31%**
5396. **`drivers/net/wireless/ralink/rt2x00/rt2800mmio.c`** -> AI Confidence: **99.31%**
5397. **`drivers/net/wireless/ralink/rt2x00/rt2x00dev.c`** -> AI Confidence: **99.31%**
5398. **`drivers/net/wireless/ralink/rt2x00/rt61pci.c`** -> AI Confidence: **99.31%**
5399. **`drivers/net/wireless/ralink/rt2x00/rt73usb.c`** -> AI Confidence: **99.31%**
5400. **`drivers/net/wireless/realtek/rtl818x/rtl8180/dev.c`** -> AI Confidence: **99.31%**
5401. **`drivers/net/wireless/realtek/rtl818x/rtl8187/dev.c`** -> AI Confidence: **99.31%**
5402. **`drivers/net/wireless/realtek/rtlwifi/base.c`** -> AI Confidence: **99.31%**
5403. **`drivers/net/wireless/realtek/rtlwifi/core.c`** -> AI Confidence: **99.31%**
5404. **`drivers/net/wireless/realtek/rtlwifi/rtl8188ee/dm.c`** -> AI Confidence: **99.31%**
5405. **`drivers/net/wireless/realtek/rtlwifi/rtl8188ee/hw.c`** -> AI Confidence: **99.31%**
5406. **`drivers/net/wireless/realtek/rtlwifi/rtl8188ee/phy.c`** -> AI Confidence: **99.31%**
5407. **`drivers/net/wireless/realtek/rtlwifi/rtl8188ee/trx.c`** -> AI Confidence: **99.31%**
5408. **`drivers/net/wireless/realtek/rtlwifi/rtl8192c/phy_common.c`** -> AI Confidence: **99.31%**
5409. **`drivers/net/wireless/realtek/rtlwifi/rtl8192ce/dm.c`** -> AI Confidence: **99.31%**
5410. **`drivers/net/wireless/realtek/rtlwifi/rtl8192ce/hw.c`** -> AI Confidence: **99.31%**
5411. **`drivers/net/wireless/realtek/rtlwifi/rtl8192ce/phy.c`** -> AI Confidence: **99.31%**
5412. **`drivers/net/wireless/realtek/rtlwifi/rtl8192ce/trx.c`** -> AI Confidence: **99.31%**
5413. **`drivers/net/wireless/realtek/rtlwifi/rtl8192cu/hw.c`** -> AI Confidence: **99.31%**
5414. **`drivers/net/wireless/realtek/rtlwifi/rtl8192cu/mac.c`** -> AI Confidence: **99.31%**
5415. **`drivers/net/wireless/realtek/rtlwifi/rtl8192cu/phy.c`** -> AI Confidence: **99.31%**
5416. **`drivers/net/wireless/realtek/rtlwifi/rtl8192cu/trx.c`** -> AI Confidence: **99.31%**
5417. **`drivers/net/wireless/realtek/rtlwifi/rtl8192d/dm_common.c`** -> AI Confidence: **99.31%**
5418. **`drivers/net/wireless/realtek/rtlwifi/rtl8192d/fw_common.c`** -> AI Confidence: **99.31%**
5419. **`drivers/net/wireless/realtek/rtlwifi/rtl8192d/hw_common.c`** -> AI Confidence: **99.31%**
5420. **`drivers/net/wireless/realtek/rtlwifi/rtl8192d/phy_common.c`** -> AI Confidence: **99.31%**
5421. **`drivers/net/wireless/realtek/rtlwifi/rtl8192de/dm.c`** -> AI Confidence: **99.31%**
5422. **`drivers/net/wireless/realtek/rtlwifi/rtl8192de/hw.c`** -> AI Confidence: **99.31%**
5423. **`drivers/net/wireless/realtek/rtlwifi/rtl8192de/phy.c`** -> AI Confidence: **99.31%**
5424. **`drivers/net/wireless/realtek/rtlwifi/rtl8192de/rf.c`** -> AI Confidence: **99.31%**
5425. **`drivers/net/wireless/realtek/rtlwifi/rtl8192de/trx.c`** -> AI Confidence: **99.31%**
5426. **`drivers/net/wireless/realtek/rtlwifi/rtl8192du/hw.c`** -> AI Confidence: **99.31%**
5427. **`drivers/net/wireless/realtek/rtlwifi/rtl8192du/phy.c`** -> AI Confidence: **99.31%**
5428. **`drivers/net/wireless/realtek/rtlwifi/rtl8192du/trx.c`** -> AI Confidence: **99.31%**
5429. **`drivers/net/wireless/realtek/rtlwifi/rtl8192ee/dm.c`** -> AI Confidence: **99.31%**
5430. **`drivers/net/wireless/realtek/rtlwifi/rtl8192ee/hw.c`** -> AI Confidence: **99.31%**
5431. **`drivers/net/wireless/realtek/rtlwifi/rtl8192ee/phy.c`** -> AI Confidence: **99.31%**
5432. **`drivers/net/wireless/realtek/rtlwifi/rtl8192ee/trx.c`** -> AI Confidence: **99.31%**
5433. **`drivers/net/wireless/realtek/rtlwifi/rtl8192se/dm.c`** -> AI Confidence: **99.31%**
5434. **`drivers/net/wireless/realtek/rtlwifi/rtl8192se/hw.c`** -> AI Confidence: **99.31%**
5435. **`drivers/net/wireless/realtek/rtlwifi/rtl8192se/phy.c`** -> AI Confidence: **99.31%**
5436. **`drivers/net/wireless/realtek/rtlwifi/rtl8192se/trx.c`** -> AI Confidence: **99.31%**
5437. **`drivers/net/wireless/realtek/rtlwifi/rtl8723ae/dm.c`** -> AI Confidence: **99.31%**
5438. **`drivers/net/wireless/realtek/rtlwifi/rtl8723ae/hal_bt_coexist.c`** -> AI Confidence: **99.31%**
5439. **`drivers/net/wireless/realtek/rtlwifi/rtl8723ae/hw.c`** -> AI Confidence: **99.31%**
5440. **`drivers/net/wireless/realtek/rtlwifi/rtl8723ae/phy.c`** -> AI Confidence: **99.31%**
5441. **`drivers/net/wireless/realtek/rtlwifi/rtl8723ae/trx.c`** -> AI Confidence: **99.31%**
5442. **`drivers/net/wireless/realtek/rtlwifi/rtl8723be/dm.c`** -> AI Confidence: **99.31%**
5443. **`drivers/net/wireless/realtek/rtlwifi/rtl8723be/hw.c`** -> AI Confidence: **99.31%**
5444. **`drivers/net/wireless/realtek/rtlwifi/rtl8723be/trx.c`** -> AI Confidence: **99.31%**
5445. **`drivers/net/wireless/realtek/rtlwifi/rtl8821ae/dm.c`** -> AI Confidence: **99.31%**
5446. **`drivers/net/wireless/realtek/rtlwifi/rtl8821ae/hw.c`** -> AI Confidence: **99.31%**
5447. **`drivers/net/wireless/realtek/rtlwifi/rtl8821ae/phy.c`** -> AI Confidence: **99.31%**
5448. **`drivers/net/wireless/realtek/rtlwifi/rtl8821ae/trx.c`** -> AI Confidence: **99.31%**
5449. **`drivers/net/wireless/realtek/rtw88/coex.c`** -> AI Confidence: **99.31%**
5450. **`drivers/net/wireless/realtek/rtw88/main.c`** -> AI Confidence: **99.31%**
5451. **`drivers/net/wireless/realtek/rtw88/phy.c`** -> AI Confidence: **99.31%**
5452. **`drivers/net/wireless/realtek/rtw88/rtw8812a.c`** -> AI Confidence: **99.31%**
5453. **`drivers/net/wireless/realtek/rtw88/rtw8814a.c`** -> AI Confidence: **99.31%**
5454. **`drivers/net/wireless/realtek/rtw88/rtw8821c.c`** -> AI Confidence: **99.31%**
5455. **`drivers/net/wireless/realtek/rtw88/rtw8822b.c`** -> AI Confidence: **99.31%**
5456. **`drivers/net/wireless/realtek/rtw88/rtw8822c.c`** -> AI Confidence: **99.31%**
5457. **`drivers/net/wireless/realtek/rtw88/wow.c`** -> AI Confidence: **99.31%**
5458. **`drivers/net/wireless/realtek/rtw89/coex.c`** -> AI Confidence: **99.31%**
5459. **`drivers/net/wireless/realtek/rtw89/debug.c`** -> AI Confidence: **99.31%**
5460. **`drivers/net/wireless/realtek/rtw89/rtw8852b_common.c`** -> AI Confidence: **99.31%**
5461. **`drivers/net/wireless/realtek/rtw89/rtw8852b_rfk.c`** -> AI Confidence: **99.31%**
5462. **`drivers/net/wireless/realtek/rtw89/rtw8852c.c`** -> AI Confidence: **99.31%**
5463. **`drivers/net/wireless/realtek/rtw89/rtw8852c_rfk.c`** -> AI Confidence: **99.31%**
5464. **`drivers/net/wireless/realtek/rtw89/rtw8922a_rfk.c`** -> AI Confidence: **99.31%**
5465. **`drivers/net/wireless/rsi/rsi_91x_main.c`** -> AI Confidence: **99.31%**
5466. **`drivers/net/wireless/silabs/wfx/bh.c`** -> AI Confidence: **99.31%**
5467. **`drivers/net/wireless/silabs/wfx/fwio.c`** -> AI Confidence: **99.31%**
5468. **`drivers/net/wireless/silabs/wfx/main.c`** -> AI Confidence: **99.31%**
5469. **`drivers/net/wireless/st/cw1200/main.c`** -> AI Confidence: **99.31%**
5470. **`drivers/net/wireless/st/cw1200/txrx.c`** -> AI Confidence: **99.31%**
5471. **`drivers/net/wireless/ti/wl1251/boot.c`** -> AI Confidence: **99.31%**
5472. **`drivers/net/wireless/ti/wl1251/cmd.c`** -> AI Confidence: **99.31%**
5473. **`drivers/net/wireless/ti/wl1251/init.c`** -> AI Confidence: **99.31%**
5474. **`drivers/net/wireless/ti/wl1251/tx.c`** -> AI Confidence: **99.31%**
5475. **`drivers/net/wireless/ti/wl12xx/main.c`** -> AI Confidence: **99.31%**
5476. **`drivers/net/wireless/ti/wl18xx/event.c`** -> AI Confidence: **99.31%**
5477. **`drivers/net/wireless/ti/wl18xx/tx.c`** -> AI Confidence: **99.31%**
5478. **`drivers/net/wireless/ti/wlcore/acx.c`** -> AI Confidence: **99.31%**
5479. **`drivers/net/wireless/ti/wlcore/boot.c`** -> AI Confidence: **99.31%**
5480. **`drivers/net/wireless/ti/wlcore/cmd.c`** -> AI Confidence: **99.31%**
5481. **`drivers/net/wireless/ti/wlcore/io.c`** -> AI Confidence: **99.31%**
5482. **`drivers/net/wireless/ti/wlcore/main.c`** -> AI Confidence: **99.31%**
5483. **`drivers/net/wireless/ti/wlcore/rx.c`** -> AI Confidence: **99.31%**
5484. **`drivers/net/wireless/ti/wlcore/scan.c`** -> AI Confidence: **99.31%**
5485. **`drivers/net/wireless/ti/wlcore/testmode.c`** -> AI Confidence: **99.31%**
5486. **`drivers/net/wireless/virtual/mac80211_hwsim.c`** -> AI Confidence: **99.31%**
5487. **`drivers/net/wireless/zydas/zd1211rw/zd_mac.c`** -> AI Confidence: **99.31%**
5488. **`drivers/net/wwan/iosm/iosm_ipc_imem.c`** -> AI Confidence: **99.31%**
5489. **`drivers/net/wwan/iosm/iosm_ipc_imem_ops.c`** -> AI Confidence: **99.31%**
5490. **`drivers/net/wwan/t7xx/t7xx_modem_ops.c`** -> AI Confidence: **99.31%**
5491. **`drivers/net/wwan/t7xx/t7xx_port_ctrl_msg.c`** -> AI Confidence: **99.31%**
5492. **`drivers/net/xen-netback/netback.c`** -> AI Confidence: **99.31%**
5493. **`drivers/net/xen-netfront.c`** -> AI Confidence: **99.31%**
5494. **`drivers/nfc/fdp/i2c.c`** -> AI Confidence: **99.31%**
5495. **`drivers/nfc/microread/microread.c`** -> AI Confidence: **99.31%**
5496. **`drivers/nfc/nfcmrvl/fw_dnld.c`** -> AI Confidence: **99.31%**
5497. **`drivers/nfc/nxp-nci/i2c.c`** -> AI Confidence: **99.31%**
5498. **`drivers/nfc/pn544/i2c.c`** -> AI Confidence: **99.31%**
5499. **`drivers/nfc/st21nfca/i2c.c`** -> AI Confidence: **99.31%**
5500. **`drivers/nfc/trf7970a.c`** -> AI Confidence: **99.31%**
5501. **`drivers/ntb/hw/intel/ntb_hw_gen1.c`** -> AI Confidence: **99.31%**
5502. **`drivers/nubus/nubus.c`** -> AI Confidence: **99.31%**
5503. **`drivers/nvdimm/badrange.c`** -> AI Confidence: **99.31%**
5504. **`drivers/nvdimm/claim.c`** -> AI Confidence: **99.31%**
5505. **`drivers/nvdimm/dimm.c`** -> AI Confidence: **99.31%**
5506. **`drivers/nvdimm/security.c`** -> AI Confidence: **99.31%**
5507. **`drivers/nvme/common/auth.c`** -> AI Confidence: **99.31%**
5508. **`drivers/nvme/host/auth.c`** -> AI Confidence: **99.31%**
5509. **`drivers/nvme/host/core.c`** -> AI Confidence: **99.31%**
5510. **`drivers/nvme/host/fabrics.c`** -> AI Confidence: **99.31%**
5511. **`drivers/of/device.c`** -> AI Confidence: **99.31%**
5512. **`drivers/of/irq.c`** -> AI Confidence: **99.31%**
5513. **`drivers/of/kexec.c`** -> AI Confidence: **99.31%**
5514. **`drivers/of/resolver.c`** -> AI Confidence: **99.31%**
5515. **`drivers/parisc/eisa.c`** -> AI Confidence: **99.31%**
5516. **`drivers/parisc/eisa_enumerator.c`** -> AI Confidence: **99.31%**
5517. **`drivers/parisc/lasi.c`** -> AI Confidence: **99.31%**
5518. **`drivers/parisc/lba_pci.c`** -> AI Confidence: **99.31%**
5519. **`drivers/parisc/led.c`** -> AI Confidence: **99.31%**
5520. **`drivers/parisc/power.c`** -> AI Confidence: **99.31%**
5521. **`drivers/parisc/superio.c`** -> AI Confidence: **99.31%**
5522. **`drivers/parisc/wax.c`** -> AI Confidence: **99.31%**
5523. **`drivers/parport/ieee1284.c`** -> AI Confidence: **99.31%**
5524. **`drivers/parport/parport_gsc.c`** -> AI Confidence: **99.31%**
5525. **`drivers/parport/parport_ip32.c`** -> AI Confidence: **99.31%**
5526. **`drivers/parport/parport_pc.c`** -> AI Confidence: **99.31%**
5527. **`drivers/parport/share.c`** -> AI Confidence: **99.31%**
5528. **`drivers/pci/controller/dwc/pcie-designware.c`** -> AI Confidence: **99.31%**
5529. **`drivers/pci/controller/pci-aardvark.c`** -> AI Confidence: **99.31%**
5530. **`drivers/pci/controller/pci-ftpci100.c`** -> AI Confidence: **99.31%**
5531. **`drivers/pci/controller/pci-thunder-ecam.c`** -> AI Confidence: **99.31%**
5532. **`drivers/pci/controller/pci-thunder-pem.c`** -> AI Confidence: **99.31%**
5533. **`drivers/pci/controller/pci-v3-semi.c`** -> AI Confidence: **99.31%**
5534. **`drivers/pci/controller/pcie-rockchip-host.c`** -> AI Confidence: **99.31%**
5535. **`drivers/pci/controller/pcie-rockchip.c`** -> AI Confidence: **99.31%**
5536. **`drivers/pci/ecam.c`** -> AI Confidence: **99.31%**
5537. **`drivers/pci/hotplug/cpci_hotplug_core.c`** -> AI Confidence: **99.31%**
5538. **`drivers/pci/hotplug/cpci_hotplug_pci.c`** -> AI Confidence: **99.31%**
5539. **`drivers/pci/hotplug/cpqphp_core.c`** -> AI Confidence: **99.31%**
5540. **`drivers/pci/hotplug/cpqphp_ctrl.c`** -> AI Confidence: **99.31%**
5541. **`drivers/pci/hotplug/cpqphp_pci.c`** -> AI Confidence: **99.31%**
5542. **`drivers/pci/hotplug/ibmphp_ebda.c`** -> AI Confidence: **99.31%**
5543. **`drivers/pci/hotplug/pciehp_ctrl.c`** -> AI Confidence: **99.31%**
5544. **`drivers/pci/hotplug/rpaphp_core.c`** -> AI Confidence: **99.31%**
5545. **`drivers/pci/hotplug/rpaphp_pci.c`** -> AI Confidence: **99.31%**
5546. **`drivers/pci/hotplug/shpchp_ctrl.c`** -> AI Confidence: **99.31%**
5547. **`drivers/pci/of.c`** -> AI Confidence: **99.31%**
5548. **`drivers/pci/pcie/aer_inject.c`** -> AI Confidence: **99.31%**
5549. **`drivers/pci/pcie/err.c`** -> AI Confidence: **99.31%**
5550. **`drivers/pci/probe.c`** -> AI Confidence: **99.31%**
5551. **`drivers/pci/proc.c`** -> AI Confidence: **99.31%**
5552. **`drivers/pci/quirks.c`** -> AI Confidence: **99.31%**
5553. **`drivers/pci/setup-cardbus.c`** -> AI Confidence: **99.31%**
5554. **`drivers/pci/setup-res.c`** -> AI Confidence: **99.31%**
5555. **`drivers/pci/switch/switchtec.c`** -> AI Confidence: **99.31%**
5556. **`drivers/pci/vc.c`** -> AI Confidence: **99.31%**
5557. **`drivers/pci/vgaarb.c`** -> AI Confidence: **99.31%**
5558. **`drivers/pcmcia/cistpl.c`** -> AI Confidence: **99.31%**
5559. **`drivers/pcmcia/cs.c`** -> AI Confidence: **99.31%**
5560. **`drivers/pcmcia/db1xxx_ss.c`** -> AI Confidence: **99.31%**
5561. **`drivers/pcmcia/i82092.c`** -> AI Confidence: **99.31%**
5562. **`drivers/pcmcia/pcmcia_resource.c`** -> AI Confidence: **99.31%**
5563. **`drivers/pcmcia/pd6729.c`** -> AI Confidence: **99.31%**
5564. **`drivers/pcmcia/rsrc_nonstatic.c`** -> AI Confidence: **99.31%**
5565. **`drivers/pcmcia/sa1100_h3600.c`** -> AI Confidence: **99.31%**
5566. **`drivers/pcmcia/sa1111_generic.c`** -> AI Confidence: **99.31%**
5567. **`drivers/pcmcia/sa1111_jornada720.c`** -> AI Confidence: **99.31%**
5568. **`drivers/pcmcia/soc_common.c`** -> AI Confidence: **99.31%**
5569. **`drivers/pcmcia/xxs1500_ss.c`** -> AI Confidence: **99.31%**
5570. **`drivers/pcmcia/yenta_socket.c`** -> AI Confidence: **99.31%**
5571. **`drivers/perf/arm_pmu_acpi.c`** -> AI Confidence: **99.31%**
5572. **`drivers/perf/arm_pmu_platform.c`** -> AI Confidence: **99.31%**
5573. **`drivers/perf/riscv_pmu_sbi.c`** -> AI Confidence: **99.31%**
5574. **`drivers/phy/broadcom/phy-brcm-sata.c`** -> AI Confidence: **99.31%**
5575. **`drivers/phy/hisilicon/phy-hi3660-usb3.c`** -> AI Confidence: **99.31%**
5576. **`drivers/phy/hisilicon/phy-hi3670-usb3.c`** -> AI Confidence: **99.31%**
5577. **`drivers/phy/marvell/phy-mvebu-a3700-comphy.c`** -> AI Confidence: **99.31%**
5578. **`drivers/phy/marvell/phy-mvebu-cp110-comphy.c`** -> AI Confidence: **99.31%**
5579. **`drivers/phy/mediatek/phy-mtk-tphy.c`** -> AI Confidence: **99.31%**
5580. **`drivers/phy/mediatek/phy-mtk-xfi-tphy.c`** -> AI Confidence: **99.31%**
5581. **`drivers/phy/phy-xgene.c`** -> AI Confidence: **99.31%**
5582. **`drivers/phy/qualcomm/phy-qcom-ipq806x-usb.c`** -> AI Confidence: **99.31%**
5583. **`drivers/phy/qualcomm/phy-qcom-usb-hs.c`** -> AI Confidence: **99.31%**
5584. **`drivers/phy/rockchip/phy-rockchip-samsung-hdptx.c`** -> AI Confidence: **99.31%**
5585. **`drivers/phy/rockchip/phy-rockchip-typec.c`** -> AI Confidence: **99.31%**
5586. **`drivers/phy/samsung/phy-samsung-ufs.c`** -> AI Confidence: **99.31%**
5587. **`drivers/phy/st/phy-stm32-combophy.c`** -> AI Confidence: **99.31%**
5588. **`drivers/phy/st/phy-stm32-usbphyc.c`** -> AI Confidence: **99.31%**
5589. **`drivers/phy/ti/phy-omap-control.c`** -> AI Confidence: **99.31%**
5590. **`drivers/pinctrl/bcm/pinctrl-bcm281xx.c`** -> AI Confidence: **99.31%**
5591. **`drivers/pinctrl/intel/pinctrl-tangier.c`** -> AI Confidence: **99.31%**
5592. **`drivers/pinctrl/mediatek/mtk-eint.c`** -> AI Confidence: **99.31%**
5593. **`drivers/pinctrl/mediatek/pinctrl-mt8135.c`** -> AI Confidence: **99.31%**
5594. **`drivers/pinctrl/mediatek/pinctrl-mtk-common-v2.c`** -> AI Confidence: **99.31%**
5595. **`drivers/pinctrl/mediatek/pinctrl-mtk-common.c`** -> AI Confidence: **99.31%**
5596. **`drivers/pinctrl/microchip/pinctrl-mpfs-mssio.c`** -> AI Confidence: **99.31%**
5597. **`drivers/pinctrl/mvebu/pinctrl-dove.c`** -> AI Confidence: **99.31%**
5598. **`drivers/pinctrl/pinconf-generic.c`** -> AI Confidence: **99.31%**
5599. **`drivers/pinctrl/pinconf.c`** -> AI Confidence: **99.31%**
5600. **`drivers/pinctrl/pinctrl-amd.c`** -> AI Confidence: **99.31%**
5601. **`drivers/pinctrl/pinctrl-at91-pio4.c`** -> AI Confidence: **99.31%**
5602. **`drivers/pinctrl/pinctrl-aw9523.c`** -> AI Confidence: **99.31%**
5603. **`drivers/pinctrl/pinctrl-bm1880.c`** -> AI Confidence: **99.31%**
5604. **`drivers/pinctrl/pinctrl-k210.c`** -> AI Confidence: **99.31%**
5605. **`drivers/pinctrl/pinctrl-lpc18xx.c`** -> AI Confidence: **99.31%**
5606. **`drivers/pinctrl/pinctrl-max77620.c`** -> AI Confidence: **99.31%**
5607. **`drivers/pinctrl/pinctrl-single.c`** -> AI Confidence: **99.31%**
5608. **`drivers/pinctrl/qcom/pinctrl-msm.c`** -> AI Confidence: **99.31%**
5609. **`drivers/pinctrl/qcom/pinctrl-spmi-mpp.c`** -> AI Confidence: **99.31%**
5610. **`drivers/pinctrl/qcom/pinctrl-ssbi-mpp.c`** -> AI Confidence: **99.31%**
5611. **`drivers/pinctrl/realtek/pinctrl-rtd.c`** -> AI Confidence: **99.31%**
5612. **`drivers/pinctrl/renesas/core.c`** -> AI Confidence: **99.31%**
5613. **`drivers/pinctrl/renesas/pinctrl-rzn1.c`** -> AI Confidence: **99.31%**
5614. **`drivers/pinctrl/renesas/pinctrl-rzv2m.c`** -> AI Confidence: **99.31%**
5615. **`drivers/pinctrl/renesas/pinctrl.c`** -> AI Confidence: **99.31%**
5616. **`drivers/pinctrl/sophgo/pinctrl-sg2042-ops.c`** -> AI Confidence: **99.31%**
5617. **`drivers/pinctrl/spear/pinctrl-plgpio.c`** -> AI Confidence: **99.31%**
5618. **`drivers/pinctrl/sprd/pinctrl-sprd.c`** -> AI Confidence: **99.31%**
5619. **`drivers/pinctrl/starfive/pinctrl-starfive-jh7100.c`** -> AI Confidence: **99.31%**
5620. **`drivers/pinctrl/sunxi/pinctrl-sunxi-dt.c`** -> AI Confidence: **99.31%**
5621. **`drivers/pinctrl/sunxi/pinctrl-sunxi.c`** -> AI Confidence: **99.31%**
5622. **`drivers/pinctrl/tegra/pinctrl-tegra.c`** -> AI Confidence: **99.31%**
5623. **`drivers/pinctrl/uniphier/pinctrl-uniphier-core.c`** -> AI Confidence: **99.31%**
5624. **`drivers/platform/arm64/acer-aspire1-ec.c`** -> AI Confidence: **99.31%**
5625. **`drivers/platform/chrome/cros_ec_i2c.c`** -> AI Confidence: **99.31%**
5626. **`drivers/platform/chrome/cros_ec_lpc.c`** -> AI Confidence: **99.31%**
5627. **`drivers/platform/chrome/cros_ec_proto.c`** -> AI Confidence: **99.31%**
5628. **`drivers/platform/chrome/cros_ec_sensorhub.c`** -> AI Confidence: **99.31%**
5629. **`drivers/platform/chrome/cros_ec_sensorhub_ring.c`** -> AI Confidence: **99.31%**
5630. **`drivers/platform/chrome/cros_ec_typec.c`** -> AI Confidence: **99.31%**
5631. **`drivers/platform/loongarch/loongson-laptop.c`** -> AI Confidence: **99.31%**
5632. **`drivers/platform/mellanox/mlx-platform.c`** -> AI Confidence: **99.31%**
5633. **`drivers/platform/mellanox/mlxbf-pmc.c`** -> AI Confidence: **99.31%**
5634. **`drivers/platform/mellanox/mlxreg-dpu.c`** -> AI Confidence: **99.31%**
5635. **`drivers/platform/mellanox/mlxreg-hotplug.c`** -> AI Confidence: **99.31%**
5636. **`drivers/platform/mellanox/mlxreg-lc.c`** -> AI Confidence: **99.31%**
5637. **`drivers/platform/mellanox/nvsw-sn2201.c`** -> AI Confidence: **99.31%**
5638. **`drivers/platform/olpc/olpc-xo175-ec.c`** -> AI Confidence: **99.31%**
5639. **`drivers/platform/raspberrypi/vchiq-interface/vchiq_core.c`** -> AI Confidence: **99.31%**
5640. **`drivers/platform/raspberrypi/vchiq-interface/vchiq_dev.c`** -> AI Confidence: **99.31%**
5641. **`drivers/platform/wmi/marshalling.c`** -> AI Confidence: **99.31%**
5642. **`drivers/platform/x86/acer-wmi.c`** -> AI Confidence: **99.31%**
5643. **`drivers/platform/x86/amd/pmc/pmc.c`** -> AI Confidence: **99.31%**
5644. **`drivers/platform/x86/apple-gmux.c`** -> AI Confidence: **99.31%**
5645. **`drivers/platform/x86/asus-wmi.c`** -> AI Confidence: **99.31%**
5646. **`drivers/platform/x86/dell/dell-smbios-base.c`** -> AI Confidence: **99.31%**
5647. **`drivers/platform/x86/dell/dell_rbu.c`** -> AI Confidence: **99.31%**
5648. **`drivers/platform/x86/hp/hp-wmi.c`** -> AI Confidence: **99.31%**
5649. **`drivers/platform/x86/ibm_rtl.c`** -> AI Confidence: **99.31%**
5650. **`drivers/platform/x86/intel/int3472/discrete.c`** -> AI Confidence: **99.31%**
5651. **`drivers/platform/x86/intel/punit_ipc.c`** -> AI Confidence: **99.31%**
5652. **`drivers/platform/x86/intel/speed_select_if/isst_if_common.c`** -> AI Confidence: **99.31%**
5653. **`drivers/platform/x86/intel/speed_select_if/isst_if_mbox_msr.c`** -> AI Confidence: **99.31%**
5654. **`drivers/platform/x86/intel/speed_select_if/isst_tpmi_core.c`** -> AI Confidence: **99.31%**
5655. **`drivers/platform/x86/intel/telemetry/pltdrv.c`** -> AI Confidence: **99.31%**
5656. **`drivers/platform/x86/intel/turbo_max_3.c`** -> AI Confidence: **99.31%**
5657. **`drivers/platform/x86/intel/uncore-frequency/uncore-frequency-tpmi.c`** -> AI Confidence: **99.31%**
5658. **`drivers/platform/x86/intel/uncore-frequency/uncore-frequency.c`** -> AI Confidence: **99.31%**
5659. **`drivers/platform/x86/intel_ips.c`** -> AI Confidence: **99.31%**
5660. **`drivers/platform/x86/lenovo/think-lmi.c`** -> AI Confidence: **99.31%**
5661. **`drivers/platform/x86/lenovo/thinkpad_acpi.c`** -> AI Confidence: **99.31%**
5662. **`drivers/platform/x86/msi-wmi.c`** -> AI Confidence: **99.31%**
5663. **`drivers/platform/x86/oxpec.c`** -> AI Confidence: **99.31%**
5664. **`drivers/platform/x86/siemens/simatic-ipc-batt.c`** -> AI Confidence: **99.31%**
5665. **`drivers/platform/x86/sony-laptop.c`** -> AI Confidence: **99.31%**
5666. **`drivers/platform/x86/toshiba_acpi.c`** -> AI Confidence: **99.31%**
5667. **`drivers/platform/x86/x86-android-tablets/vexia_atla10_ec.c`** -> AI Confidence: **99.31%**
5668. **`drivers/pmdomain/mediatek/mtk-pm-domains.c`** -> AI Confidence: **99.31%**
5669. **`drivers/pmdomain/qcom/rpmhpd.c`** -> AI Confidence: **99.31%**
5670. **`drivers/pmdomain/renesas/rcar-gen4-sysc.c`** -> AI Confidence: **99.31%**
5671. **`drivers/pnp/isapnp/core.c`** -> AI Confidence: **99.31%**
5672. **`drivers/pnp/manager.c`** -> AI Confidence: **99.31%**
5673. **`drivers/pnp/pnpacpi/core.c`** -> AI Confidence: **99.31%**
5674. **`drivers/pnp/pnpacpi/rsparser.c`** -> AI Confidence: **99.31%**
5675. **`drivers/pnp/pnpbios/bioscalls.c`** -> AI Confidence: **99.31%**
5676. **`drivers/pnp/pnpbios/core.c`** -> AI Confidence: **99.31%**
5677. **`drivers/pnp/resource.c`** -> AI Confidence: **99.31%**
5678. **`drivers/power/reset/atc260x-poweroff.c`** -> AI Confidence: **99.31%**
5679. **`drivers/power/supply/88pm860x_battery.c`** -> AI Confidence: **99.31%**
5680. **`drivers/power/supply/88pm860x_charger.c`** -> AI Confidence: **99.31%**
5681. **`drivers/power/supply/ab8500_chargalg.c`** -> AI Confidence: **99.31%**
5682. **`drivers/power/supply/ab8500_charger.c`** -> AI Confidence: **99.31%**
5683. **`drivers/power/supply/ab8500_fg.c`** -> AI Confidence: **99.31%**
5684. **`drivers/power/supply/act8945a_charger.c`** -> AI Confidence: **99.31%**
5685. **`drivers/power/supply/adc-battery-helper.c`** -> AI Confidence: **99.31%**
5686. **`drivers/power/supply/axp20x_battery.c`** -> AI Confidence: **99.31%**
5687. **`drivers/power/supply/axp288_charger.c`** -> AI Confidence: **99.31%**
5688. **`drivers/power/supply/axp288_fuel_gauge.c`** -> AI Confidence: **99.31%**
5689. **`drivers/power/supply/bd99954-charger.c`** -> AI Confidence: **99.31%**
5690. **`drivers/power/supply/bq2415x_charger.c`** -> AI Confidence: **99.31%**
5691. **`drivers/power/supply/bq24190_charger.c`** -> AI Confidence: **99.31%**
5692. **`drivers/power/supply/bq256xx_charger.c`** -> AI Confidence: **99.31%**
5693. **`drivers/power/supply/bq25890_charger.c`** -> AI Confidence: **99.31%**
5694. **`drivers/power/supply/bq25980_charger.c`** -> AI Confidence: **99.31%**
5695. **`drivers/power/supply/bq27xxx_battery.c`** -> AI Confidence: **99.31%**
5696. **`drivers/power/supply/charger-manager.c`** -> AI Confidence: **99.31%**
5697. **`drivers/power/supply/collie_battery.c`** -> AI Confidence: **99.31%**
5698. **`drivers/power/supply/cpcap-battery.c`** -> AI Confidence: **99.31%**
5699. **`drivers/power/supply/cpcap-charger.c`** -> AI Confidence: **99.31%**
5700. **`drivers/power/supply/cros_usbpd-charger.c`** -> AI Confidence: **99.31%**
5701. **`drivers/power/supply/cw2015_battery.c`** -> AI Confidence: **99.31%**
5702. **`drivers/power/supply/da9052-battery.c`** -> AI Confidence: **99.31%**
5703. **`drivers/power/supply/da9150-charger.c`** -> AI Confidence: **99.31%**
5704. **`drivers/power/supply/ds2760_battery.c`** -> AI Confidence: **99.31%**
5705. **`drivers/power/supply/goldfish_battery.c`** -> AI Confidence: **99.31%**
5706. **`drivers/power/supply/intel_dc_ti_battery.c`** -> AI Confidence: **99.31%**
5707. **`drivers/power/supply/isp1704_charger.c`** -> AI Confidence: **99.31%**
5708. **`drivers/power/supply/lenovo_yoga_c630_battery.c`** -> AI Confidence: **99.31%**
5709. **`drivers/power/supply/lt3651-charger.c`** -> AI Confidence: **99.31%**
5710. **`drivers/power/supply/max17042_battery.c`** -> AI Confidence: **99.31%**
5711. **`drivers/power/supply/max77650-charger.c`** -> AI Confidence: **99.31%**
5712. **`drivers/power/supply/max77693_charger.c`** -> AI Confidence: **99.31%**
5713. **`drivers/power/supply/max77705_charger.c`** -> AI Confidence: **99.31%**
5714. **`drivers/power/supply/max8903_charger.c`** -> AI Confidence: **99.31%**
5715. **`drivers/power/supply/max8925_power.c`** -> AI Confidence: **99.31%**
5716. **`drivers/power/supply/max8971_charger.c`** -> AI Confidence: **99.31%**
5717. **`drivers/power/supply/max8997_charger.c`** -> AI Confidence: **99.31%**
5718. **`drivers/power/supply/max8998_charger.c`** -> AI Confidence: **99.31%**
5719. **`drivers/power/supply/mp2629_charger.c`** -> AI Confidence: **99.31%**
5720. **`drivers/power/supply/mt6360_charger.c`** -> AI Confidence: **99.31%**
5721. **`drivers/power/supply/olpc_battery.c`** -> AI Confidence: **99.31%**
5722. **`drivers/power/supply/pm8916_bms_vm.c`** -> AI Confidence: **99.31%**
5723. **`drivers/power/supply/pm8916_lbc.c`** -> AI Confidence: **99.31%**
5724. **`drivers/power/supply/pmu_battery.c`** -> AI Confidence: **99.31%**
5725. **`drivers/power/supply/qcom_battmgr.c`** -> AI Confidence: **99.31%**
5726. **`drivers/power/supply/rn5t618_power.c`** -> AI Confidence: **99.31%**
5727. **`drivers/power/supply/rt5033_charger.c`** -> AI Confidence: **99.31%**
5728. **`drivers/power/supply/sbs-battery.c`** -> AI Confidence: **99.31%**
5729. **`drivers/power/supply/sc2731_charger.c`** -> AI Confidence: **99.31%**
5730. **`drivers/power/supply/sc27xx_fuel_gauge.c`** -> AI Confidence: **99.31%**
5731. **`drivers/power/supply/smb347-charger.c`** -> AI Confidence: **99.31%**
5732. **`drivers/power/supply/twl4030_charger.c`** -> AI Confidence: **99.31%**
5733. **`drivers/power/supply/twl4030_madc_battery.c`** -> AI Confidence: **99.31%**
5734. **`drivers/power/supply/twl6030_charger.c`** -> AI Confidence: **99.31%**
5735. **`drivers/power/supply/wm831x_backup.c`** -> AI Confidence: **99.31%**
5736. **`drivers/power/supply/wm831x_power.c`** -> AI Confidence: **99.31%**
5737. **`drivers/power/supply/wm8350_power.c`** -> AI Confidence: **99.31%**
5738. **`drivers/power/supply/wm97xx_battery.c`** -> AI Confidence: **99.31%**
5739. **`drivers/powercap/intel_rapl_tpmi.c`** -> AI Confidence: **99.31%**
5740. **`drivers/pps/clients/pps_parport.c`** -> AI Confidence: **99.31%**
5741. **`drivers/pps/kapi.c`** -> AI Confidence: **99.31%**
5742. **`drivers/pps/kc.c`** -> AI Confidence: **99.31%**
5743. **`drivers/ps3/ps3-lpm.c`** -> AI Confidence: **99.31%**
5744. **`drivers/ps3/ps3av.c`** -> AI Confidence: **99.31%**
5745. **`drivers/ps3/ps3av_cmd.c`** -> AI Confidence: **99.31%**
5746. **`drivers/ptp/ptp_chardev.c`** -> AI Confidence: **99.31%**
5747. **`drivers/ptp/ptp_clockmatrix.c`** -> AI Confidence: **99.31%**
5748. **`drivers/pwm/pwm-imx27.c`** -> AI Confidence: **99.31%**
5749. **`drivers/pwm/pwm-sifive.c`** -> AI Confidence: **99.31%**
5750. **`drivers/pwm/pwm-stm32-lp.c`** -> AI Confidence: **99.31%**
5751. **`drivers/pwm/pwm-stmpe.c`** -> AI Confidence: **99.31%**
5752. **`drivers/rapidio/devices/tsi721.c`** -> AI Confidence: **99.31%**
5753. **`drivers/rapidio/rio-scan.c`** -> AI Confidence: **99.31%**
5754. **`drivers/rapidio/rio.c`** -> AI Confidence: **99.31%**
5755. **`drivers/rapidio/switches/idt_gen3.c`** -> AI Confidence: **99.31%**
5756. **`drivers/regulator/act8865-regulator.c`** -> AI Confidence: **99.31%**
5757. **`drivers/regulator/act8945a-regulator.c`** -> AI Confidence: **99.31%**
5758. **`drivers/regulator/as3722-regulator.c`** -> AI Confidence: **99.31%**
5759. **`drivers/regulator/core.c`** -> AI Confidence: **99.31%**
5760. **`drivers/regulator/da9052-regulator.c`** -> AI Confidence: **99.31%**
5761. **`drivers/regulator/da9063-regulator.c`** -> AI Confidence: **99.31%**
5762. **`drivers/regulator/da9121-regulator.c`** -> AI Confidence: **99.31%**
5763. **`drivers/regulator/da9211-regulator.c`** -> AI Confidence: **99.31%**
5764. **`drivers/regulator/fan53555.c`** -> AI Confidence: **99.31%**
5765. **`drivers/regulator/gpio-regulator.c`** -> AI Confidence: **99.31%**
5766. **`drivers/regulator/helpers.c`** -> AI Confidence: **99.31%**
5767. **`drivers/regulator/irq_helpers.c`** -> AI Confidence: **99.31%**
5768. **`drivers/regulator/lm363x-regulator.c`** -> AI Confidence: **99.31%**
5769. **`drivers/regulator/lp8755.c`** -> AI Confidence: **99.31%**
5770. **`drivers/regulator/lp8788-buck.c`** -> AI Confidence: **99.31%**
5771. **`drivers/regulator/max5970-regulator.c`** -> AI Confidence: **99.31%**
5772. **`drivers/regulator/max77620-regulator.c`** -> AI Confidence: **99.31%**
5773. **`drivers/regulator/max77675-regulator.c`** -> AI Confidence: **99.31%**
5774. **`drivers/regulator/max77686-regulator.c`** -> AI Confidence: **99.31%**
5775. **`drivers/regulator/max77857-regulator.c`** -> AI Confidence: **99.31%**
5776. **`drivers/regulator/max8973-regulator.c`** -> AI Confidence: **99.31%**
5777. **`drivers/regulator/max8997-regulator.c`** -> AI Confidence: **99.31%**
5778. **`drivers/regulator/max8998.c`** -> AI Confidence: **99.31%**
5779. **`drivers/regulator/mt6359-regulator.c`** -> AI Confidence: **99.31%**
5780. **`drivers/regulator/of_regulator.c`** -> AI Confidence: **99.31%**
5781. **`drivers/regulator/palmas-regulator.c`** -> AI Confidence: **99.31%**
5782. **`drivers/regulator/pca9450-regulator.c`** -> AI Confidence: **99.31%**
5783. **`drivers/regulator/pfuze100-regulator.c`** -> AI Confidence: **99.31%**
5784. **`drivers/regulator/pv88060-regulator.c`** -> AI Confidence: **99.31%**
5785. **`drivers/regulator/pv88090-regulator.c`** -> AI Confidence: **99.31%**
5786. **`drivers/regulator/rt5190a-regulator.c`** -> AI Confidence: **99.31%**
5787. **`drivers/regulator/s5m8767.c`** -> AI Confidence: **99.31%**
5788. **`drivers/regulator/slg51000-regulator.c`** -> AI Confidence: **99.31%**
5789. **`drivers/regulator/ti-abb-regulator.c`** -> AI Confidence: **99.31%**
5790. **`drivers/regulator/tps6507x-regulator.c`** -> AI Confidence: **99.31%**
5791. **`drivers/regulator/tps65910-regulator.c`** -> AI Confidence: **99.31%**
5792. **`drivers/regulator/twl6030-regulator.c`** -> AI Confidence: **99.31%**
5793. **`drivers/regulator/wm8350-regulator.c`** -> AI Confidence: **99.31%**
5794. **`drivers/remoteproc/remoteproc_cdev.c`** -> AI Confidence: **99.31%**
5795. **`drivers/remoteproc/remoteproc_core.c`** -> AI Confidence: **99.31%**
5796. **`drivers/remoteproc/st_slim_rproc.c`** -> AI Confidence: **99.31%**
5797. **`drivers/remoteproc/ti_k3_r5_remoteproc.c`** -> AI Confidence: **99.31%**
5798. **`drivers/resctrl/mpam_devices.c`** -> AI Confidence: **99.31%**
5799. **`drivers/reset/core.c`** -> AI Confidence: **99.31%**
5800. **`drivers/reset/reset-pistachio.c`** -> AI Confidence: **99.31%**
5801. **`drivers/rtc/rtc-at91sam9.c`** -> AI Confidence: **99.31%**
5802. **`drivers/rtc/rtc-ds1286.c`** -> AI Confidence: **99.31%**
5803. **`drivers/rtc/rtc-ds1307.c`** -> AI Confidence: **99.31%**
5804. **`drivers/rtc/rtc-ds1685.c`** -> AI Confidence: **99.31%**
5805. **`drivers/rtc/rtc-imxdi.c`** -> AI Confidence: **99.31%**
5806. **`drivers/rtc/rtc-isl12026.c`** -> AI Confidence: **99.31%**
5807. **`drivers/rtc/rtc-mc13xxx.c`** -> AI Confidence: **99.31%**
5808. **`drivers/rtc/rtc-opal.c`** -> AI Confidence: **99.31%**
5809. **`drivers/rtc/rtc-rv8803.c`** -> AI Confidence: **99.31%**
5810. **`drivers/rtc/rtc-rx8025.c`** -> AI Confidence: **99.31%**
5811. **`drivers/rtc/rtc-s5m.c`** -> AI Confidence: **99.31%**
5812. **`drivers/rtc/rtc-wm8350.c`** -> AI Confidence: **99.31%**
5813. **`drivers/s390/block/dasd.c`** -> AI Confidence: **99.31%**
5814. **`drivers/s390/block/dasd_devmap.c`** -> AI Confidence: **99.31%**
5815. **`drivers/s390/block/dasd_eckd.c`** -> AI Confidence: **99.31%**
5816. **`drivers/s390/block/dasd_eer.c`** -> AI Confidence: **99.31%**
5817. **`drivers/s390/block/dasd_fba.c`** -> AI Confidence: **99.31%**
5818. **`drivers/s390/block/dasd_ioctl.c`** -> AI Confidence: **99.31%**
5819. **`drivers/s390/block/dasd_proc.c`** -> AI Confidence: **99.31%**
5820. **`drivers/s390/block/dcssblk.c`** -> AI Confidence: **99.31%**
5821. **`drivers/s390/char/diag_ftp.c`** -> AI Confidence: **99.31%**
5822. **`drivers/s390/char/hmcdrv_dev.c`** -> AI Confidence: **99.31%**
5823. **`drivers/s390/char/hmcdrv_ftp.c`** -> AI Confidence: **99.31%**
5824. **`drivers/s390/char/keyboard.c`** -> AI Confidence: **99.31%**
5825. **`drivers/s390/char/monwriter.c`** -> AI Confidence: **99.31%**
5826. **`drivers/s390/char/sclp_cmd.c`** -> AI Confidence: **99.31%**
5827. **`drivers/s390/char/sclp_early.c`** -> AI Confidence: **99.31%**
5828. **`drivers/s390/char/sclp_ftp.c`** -> AI Confidence: **99.31%**
5829. **`drivers/s390/char/sclp_mem.c`** -> AI Confidence: **99.31%**
5830. **`drivers/s390/char/sclp_pci.c`** -> AI Confidence: **99.31%**
5831. **`drivers/s390/char/sclp_sdias.c`** -> AI Confidence: **99.31%**
5832. **`drivers/s390/char/tape_3490.c`** -> AI Confidence: **99.31%**
5833. **`drivers/s390/char/tape_char.c`** -> AI Confidence: **99.31%**
5834. **`drivers/s390/char/tape_core.c`** -> AI Confidence: **99.31%**
5835. **`drivers/s390/char/uvdevice.c`** -> AI Confidence: **99.31%**
5836. **`drivers/s390/char/vmlogrdr.c`** -> AI Confidence: **99.31%**
5837. **`drivers/s390/char/vmur.c`** -> AI Confidence: **99.31%**
5838. **`drivers/s390/char/zcore.c`** -> AI Confidence: **99.31%**
5839. **`drivers/s390/cio/airq.c`** -> AI Confidence: **99.31%**
5840. **`drivers/s390/cio/ccwgroup.c`** -> AI Confidence: **99.31%**
5841. **`drivers/s390/cio/ccwreq.c`** -> AI Confidence: **99.31%**
5842. **`drivers/s390/cio/chsc.c`** -> AI Confidence: **99.31%**
5843. **`drivers/s390/cio/chsc_sch.c`** -> AI Confidence: **99.31%**
5844. **`drivers/s390/cio/crw.c`** -> AI Confidence: **99.31%**
5845. **`drivers/s390/cio/device.c`** -> AI Confidence: **99.31%**
5846. **`drivers/s390/cio/device_status.c`** -> AI Confidence: **99.31%**
5847. **`drivers/s390/cio/qdio_main.c`** -> AI Confidence: **99.31%**
5848. **`drivers/s390/crypto/vfio_ap_ops.c`** -> AI Confidence: **99.31%**
5849. **`drivers/s390/crypto/zcrypt_api.c`** -> AI Confidence: **99.31%**
5850. **`drivers/s390/crypto/zcrypt_ccamisc.c`** -> AI Confidence: **99.31%**
5851. **`drivers/s390/crypto/zcrypt_cex4.c`** -> AI Confidence: **99.31%**
5852. **`drivers/s390/crypto/zcrypt_ep11misc.c`** -> AI Confidence: **99.31%**
5853. **`drivers/s390/crypto/zcrypt_msgtype50.c`** -> AI Confidence: **99.31%**
5854. **`drivers/s390/crypto/zcrypt_msgtype6.c`** -> AI Confidence: **99.31%**
5855. **`drivers/s390/net/ctcm_fsms.c`** -> AI Confidence: **99.31%**
5856. **`drivers/s390/net/ctcm_main.c`** -> AI Confidence: **99.31%**
5857. **`drivers/s390/net/ctcm_mpc.c`** -> AI Confidence: **99.31%**
5858. **`drivers/s390/net/qeth_core_main.c`** -> AI Confidence: **99.31%**
5859. **`drivers/s390/net/qeth_l2_main.c`** -> AI Confidence: **99.31%**
5860. **`drivers/s390/net/qeth_l3_main.c`** -> AI Confidence: **99.31%**
5861. **`drivers/s390/scsi/zfcp_fsf.c`** -> AI Confidence: **99.31%**
5862. **`drivers/sbus/char/bbc_i2c.c`** -> AI Confidence: **99.31%**
5863. **`drivers/sbus/char/display7seg.c`** -> AI Confidence: **99.31%**
5864. **`drivers/sbus/char/envctrl.c`** -> AI Confidence: **99.31%**
5865. **`drivers/sbus/char/flash.c`** -> AI Confidence: **99.31%**
5866. **`drivers/sbus/char/openprom.c`** -> AI Confidence: **99.31%**
5867. **`drivers/sbus/char/oradax.c`** -> AI Confidence: **99.31%**
5868. **`drivers/scsi/53c700.c`** -> AI Confidence: **99.31%**
5869. **`drivers/scsi/BusLogic.c`** -> AI Confidence: **99.31%**
5870. **`drivers/scsi/aacraid/aachba.c`** -> AI Confidence: **99.31%**
5871. **`drivers/scsi/aacraid/commctrl.c`** -> AI Confidence: **99.31%**
5872. **`drivers/scsi/aacraid/comminit.c`** -> AI Confidence: **99.31%**
5873. **`drivers/scsi/aacraid/dpcsup.c`** -> AI Confidence: **99.31%**
5874. **`drivers/scsi/aacraid/rx.c`** -> AI Confidence: **99.31%**
5875. **`drivers/scsi/aha1542.c`** -> AI Confidence: **99.31%**
5876. **`drivers/scsi/aha1740.c`** -> AI Confidence: **99.31%**
5877. **`drivers/scsi/aic7xxx/aic7xxx_osm.c`** -> AI Confidence: **99.31%**
5878. **`drivers/scsi/aic7xxx/aicasm/aicasm.c`** -> AI Confidence: **99.31%**
5879. **`drivers/scsi/aic94xx/aic94xx_hwi.c`** -> AI Confidence: **99.31%**
5880. **`drivers/scsi/aic94xx/aic94xx_init.c`** -> AI Confidence: **99.31%**
5881. **`drivers/scsi/aic94xx/aic94xx_scb.c`** -> AI Confidence: **99.31%**
5882. **`drivers/scsi/aic94xx/aic94xx_seq.c`** -> AI Confidence: **99.31%**
5883. **`drivers/scsi/arcmsr/arcmsr_hba.c`** -> AI Confidence: **99.31%**
5884. **`drivers/scsi/arm/cumana_1.c`** -> AI Confidence: **99.31%**
5885. **`drivers/scsi/arm/cumana_2.c`** -> AI Confidence: **99.31%**
5886. **`drivers/scsi/arm/oak.c`** -> AI Confidence: **99.31%**
5887. **`drivers/scsi/atari_scsi.c`** -> AI Confidence: **99.31%**
5888. **`drivers/scsi/be2iscsi/be_iscsi.c`** -> AI Confidence: **99.31%**
5889. **`drivers/scsi/bfa/bfad.c`** -> AI Confidence: **99.31%**
5890. **`drivers/scsi/ch.c`** -> AI Confidence: **99.31%**
5891. **`drivers/scsi/csiostor/csio_hw.c`** -> AI Confidence: **99.31%**
5892. **`drivers/scsi/csiostor/csio_isr.c`** -> AI Confidence: **99.31%**
5893. **`drivers/scsi/csiostor/csio_rnode.c`** -> AI Confidence: **99.31%**
5894. **`drivers/scsi/cxgbi/libcxgbi.c`** -> AI Confidence: **99.31%**
5895. **`drivers/scsi/device_handler/scsi_dh_alua.c`** -> AI Confidence: **99.31%**
5896. **`drivers/scsi/esp_scsi.c`** -> AI Confidence: **99.31%**
5897. **`drivers/scsi/fcoe/fcoe_ctlr.c`** -> AI Confidence: **99.31%**
5898. **`drivers/scsi/fdomain.c`** -> AI Confidence: **99.31%**
5899. **`drivers/scsi/fnic/fdls_disc.c`** -> AI Confidence: **99.31%**
5900. **`drivers/scsi/fnic/fnic_isr.c`** -> AI Confidence: **99.31%**
5901. **`drivers/scsi/fnic/fnic_main.c`** -> AI Confidence: **99.31%**
5902. **`drivers/scsi/fnic/fnic_scsi.c`** -> AI Confidence: **99.31%**
5903. **`drivers/scsi/fnic/fnic_trace.c`** -> AI Confidence: **99.31%**
5904. **`drivers/scsi/hosts.c`** -> AI Confidence: **99.31%**
5905. **`drivers/scsi/hpsa.c`** -> AI Confidence: **99.31%**
5906. **`drivers/scsi/ibmvscsi/ibmvfc.c`** -> AI Confidence: **99.31%**
5907. **`drivers/scsi/ibmvscsi_tgt/ibmvscsi_tgt.c`** -> AI Confidence: **99.31%**
5908. **`drivers/scsi/ibmvscsi_tgt/libsrp.c`** -> AI Confidence: **99.31%**
5909. **`drivers/scsi/imm.c`** -> AI Confidence: **99.31%**
5910. **`drivers/scsi/imm.h`** -> AI Confidence: **99.31%**
5911. **`drivers/scsi/initio.c`** -> AI Confidence: **99.31%**
5912. **`drivers/scsi/isci/host.c`** -> AI Confidence: **99.31%**
5913. **`drivers/scsi/isci/probe_roms.c`** -> AI Confidence: **99.31%**
5914. **`drivers/scsi/isci/remote_node_context.c`** -> AI Confidence: **99.31%**
5915. **`drivers/scsi/isci/request.c`** -> AI Confidence: **99.31%**
5916. **`drivers/scsi/isci/task.c`** -> AI Confidence: **99.31%**
5917. **`drivers/scsi/libfc/fc_disc.c`** -> AI Confidence: **99.31%**
5918. **`drivers/scsi/libfc/fc_elsct.c`** -> AI Confidence: **99.31%**
5919. **`drivers/scsi/libfc/fc_fcp.c`** -> AI Confidence: **99.31%**
5920. **`drivers/scsi/libfc/fc_lport.c`** -> AI Confidence: **99.31%**
5921. **`drivers/scsi/libfc/fc_rport.c`** -> AI Confidence: **99.31%**
5922. **`drivers/scsi/libiscsi.c`** -> AI Confidence: **99.31%**
5923. **`drivers/scsi/libsas/sas_expander.c`** -> AI Confidence: **99.31%**
5924. **`drivers/scsi/libsas/sas_host_smp.c`** -> AI Confidence: **99.31%**
5925. **`drivers/scsi/lpfc/lpfc_attr.c`** -> AI Confidence: **99.31%**
5926. **`drivers/scsi/lpfc/lpfc_bsg.c`** -> AI Confidence: **99.31%**
5927. **`drivers/scsi/lpfc/lpfc_ct.c`** -> AI Confidence: **99.31%**
5928. **`drivers/scsi/lpfc/lpfc_debugfs.c`** -> AI Confidence: **99.31%**
5929. **`drivers/scsi/lpfc/lpfc_els.c`** -> AI Confidence: **99.31%**
5930. **`drivers/scsi/lpfc/lpfc_hbadisc.c`** -> AI Confidence: **99.31%**
5931. **`drivers/scsi/lpfc/lpfc_init.c`** -> AI Confidence: **99.31%**
5932. **`drivers/scsi/lpfc/lpfc_nvmet.c`** -> AI Confidence: **99.31%**
5933. **`drivers/scsi/lpfc/lpfc_scsi.c`** -> AI Confidence: **99.31%**
5934. **`drivers/scsi/lpfc/lpfc_sli.c`** -> AI Confidence: **99.31%**
5935. **`drivers/scsi/lpfc/lpfc_vmid.c`** -> AI Confidence: **99.31%**
5936. **`drivers/scsi/mac_esp.c`** -> AI Confidence: **99.31%**
5937. **`drivers/scsi/mac_scsi.c`** -> AI Confidence: **99.31%**
5938. **`drivers/scsi/megaraid.c`** -> AI Confidence: **99.31%**
5939. **`drivers/scsi/megaraid/megaraid_mm.h`** -> AI Confidence: **99.31%**
5940. **`drivers/scsi/megaraid/megaraid_sas_base.c`** -> AI Confidence: **99.31%**
5941. **`drivers/scsi/megaraid/megaraid_sas_fp.c`** -> AI Confidence: **99.31%**
5942. **`drivers/scsi/megaraid/megaraid_sas_fusion.c`** -> AI Confidence: **99.31%**
5943. **`drivers/scsi/mesh.c`** -> AI Confidence: **99.31%**
5944. **`drivers/scsi/mpt3sas/mpt3sas_base.c`** -> AI Confidence: **99.31%**
5945. **`drivers/scsi/mpt3sas/mpt3sas_config.c`** -> AI Confidence: **99.31%**
5946. **`drivers/scsi/mpt3sas/mpt3sas_ctl.c`** -> AI Confidence: **99.31%**
5947. **`drivers/scsi/mpt3sas/mpt3sas_scsih.c`** -> AI Confidence: **99.31%**
5948. **`drivers/scsi/mpt3sas/mpt3sas_transport.c`** -> AI Confidence: **99.31%**
5949. **`drivers/scsi/mpt3sas/mpt3sas_trigger_diag.c`** -> AI Confidence: **99.31%**
5950. **`drivers/scsi/mvumi.c`** -> AI Confidence: **99.31%**
5951. **`drivers/scsi/myrb.c`** -> AI Confidence: **99.31%**
5952. **`drivers/scsi/ncr53c8xx.c`** -> AI Confidence: **99.31%**
5953. **`drivers/scsi/nsp32.c`** -> AI Confidence: **99.31%**
5954. **`drivers/scsi/pcmcia/nsp_cs.c`** -> AI Confidence: **99.31%**
5955. **`drivers/scsi/pcmcia/sym53c500_cs.c`** -> AI Confidence: **99.31%**
5956. **`drivers/scsi/ppa.c`** -> AI Confidence: **99.31%**
5957. **`drivers/scsi/qedf/qedf_main.c`** -> AI Confidence: **99.31%**
5958. **`drivers/scsi/qedi/qedi_iscsi.c`** -> AI Confidence: **99.31%**
5959. **`drivers/scsi/qedi/qedi_main.c`** -> AI Confidence: **99.31%**
5960. **`drivers/scsi/qla1280.c`** -> AI Confidence: **99.31%**
5961. **`drivers/scsi/qla2xxx/qla_mid.c`** -> AI Confidence: **99.31%**
5962. **`drivers/scsi/qla2xxx/qla_mr.c`** -> AI Confidence: **99.31%**
5963. **`drivers/scsi/qla2xxx/qla_nx.c`** -> AI Confidence: **99.31%**
5964. **`drivers/scsi/qla2xxx/qla_os.c`** -> AI Confidence: **99.31%**
5965. **`drivers/scsi/qla2xxx/qla_target.c`** -> AI Confidence: **99.31%**
5966. **`drivers/scsi/qla4xxx/ql4_nx.c`** -> AI Confidence: **99.31%**
5967. **`drivers/scsi/qlogicfas.c`** -> AI Confidence: **99.31%**
5968. **`drivers/scsi/qlogicfas408.c`** -> AI Confidence: **99.31%**
5969. **`drivers/scsi/qlogicpti.c`** -> AI Confidence: **99.31%**
5970. **`drivers/scsi/scsi.c`** -> AI Confidence: **99.31%**
5971. **`drivers/scsi/scsi_bsg.c`** -> AI Confidence: **99.31%**
5972. **`drivers/scsi/scsi_common.c`** -> AI Confidence: **99.31%**
5973. **`drivers/scsi/scsi_debug.c`** -> AI Confidence: **99.31%**
5974. **`drivers/scsi/scsi_error.c`** -> AI Confidence: **99.31%**
5975. **`drivers/scsi/scsi_ioctl.c`** -> AI Confidence: **99.31%**
5976. **`drivers/scsi/scsi_logging.c`** -> AI Confidence: **99.31%**
5977. **`drivers/scsi/scsi_netlink.c`** -> AI Confidence: **99.31%**
5978. **`drivers/scsi/scsi_scan.c`** -> AI Confidence: **99.31%**
5979. **`drivers/scsi/scsi_transport_iscsi.c`** -> AI Confidence: **99.31%**
5980. **`drivers/scsi/scsi_transport_spi.c`** -> AI Confidence: **99.31%**
5981. **`drivers/scsi/scsicam.c`** -> AI Confidence: **99.31%**
5982. **`drivers/scsi/sd.c`** -> AI Confidence: **99.31%**
5983. **`drivers/scsi/sd_dif.c`** -> AI Confidence: **99.31%**
5984. **`drivers/scsi/sd_zbc.c`** -> AI Confidence: **99.31%**
5985. **`drivers/scsi/ses.c`** -> AI Confidence: **99.31%**
5986. **`drivers/scsi/sg.c`** -> AI Confidence: **99.31%**
5987. **`drivers/scsi/sim710.c`** -> AI Confidence: **99.31%**
5988. **`drivers/scsi/snic/snic_ctl.c`** -> AI Confidence: **99.31%**
5989. **`drivers/scsi/snic/snic_main.c`** -> AI Confidence: **99.31%**
5990. **`drivers/scsi/snic/snic_res.c`** -> AI Confidence: **99.31%**
5991. **`drivers/scsi/snic/snic_scsi.c`** -> AI Confidence: **99.31%**
5992. **`drivers/scsi/sr.c`** -> AI Confidence: **99.31%**
5993. **`drivers/scsi/sr_ioctl.c`** -> AI Confidence: **99.31%**
5994. **`drivers/scsi/st.c`** -> AI Confidence: **99.31%**
5995. **`drivers/scsi/sun3_scsi.c`** -> AI Confidence: **99.31%**
5996. **`drivers/scsi/sun3x_esp.c`** -> AI Confidence: **99.31%**
5997. **`drivers/scsi/sun_esp.c`** -> AI Confidence: **99.31%**
5998. **`drivers/scsi/sym53c8xx_2/sym_glue.c`** -> AI Confidence: **99.31%**
5999. **`drivers/scsi/vmw_pvscsi.c`** -> AI Confidence: **99.31%**
6000. **`drivers/scsi/wd719x.c`** -> AI Confidence: **99.31%**
6001. **`drivers/sh/clk/core.c`** -> AI Confidence: **99.31%**
6002. **`drivers/sh/intc/core.c`** -> AI Confidence: **99.31%**
6003. **`drivers/sh/maple/maple.c`** -> AI Confidence: **99.31%**
6004. **`drivers/soc/aspeed/aspeed-socinfo.c`** -> AI Confidence: **99.31%**
6005. **`drivers/soc/fsl/dpio/dpio-driver.c`** -> AI Confidence: **99.31%**
6006. **`drivers/soc/fsl/guts.c`** -> AI Confidence: **99.31%**
6007. **`drivers/soc/fsl/qe/qe_io.c`** -> AI Confidence: **99.31%**
6008. **`drivers/soc/fsl/qe/tsa.c`** -> AI Confidence: **99.31%**
6009. **`drivers/soc/fsl/qe/ucc_fast.c`** -> AI Confidence: **99.31%**
6010. **`drivers/soc/fsl/qe/ucc_slow.c`** -> AI Confidence: **99.31%**
6011. **`drivers/soc/ixp4xx/ixp4xx-npe.c`** -> AI Confidence: **99.31%**
6012. **`drivers/soc/ixp4xx/ixp4xx-qmgr.c`** -> AI Confidence: **99.31%**
6013. **`drivers/soc/mediatek/mtk-svs.c`** -> AI Confidence: **99.31%**
6014. **`drivers/soc/qcom/qcom-geni-se.c`** -> AI Confidence: **99.31%**
6015. **`drivers/soc/qcom/qcom-pbs.c`** -> AI Confidence: **99.31%**
6016. **`drivers/soc/qcom/qmi_encdec.c`** -> AI Confidence: **99.31%**
6017. **`drivers/soc/qcom/smsm.c`** -> AI Confidence: **99.31%**
6018. **`drivers/soc/rockchip/io-domain.c`** -> AI Confidence: **99.31%**
6019. **`drivers/soc/samsung/exynos-asv.c`** -> AI Confidence: **99.31%**
6020. **`drivers/soc/tegra/fuse/tegra-apbmisc.c`** -> AI Confidence: **99.31%**
6021. **`drivers/soc/ti/k3-socinfo.c`** -> AI Confidence: **99.31%**
6022. **`drivers/soc/ti/pm33xx.c`** -> AI Confidence: **99.31%**
6023. **`drivers/soc/ti/smartreflex.c`** -> AI Confidence: **99.31%**
6024. **`drivers/soc/ti/ti_sci_inta_msi.c`** -> AI Confidence: **99.31%**
6025. **`drivers/soc/xilinx/xlnx_event_manager.c`** -> AI Confidence: **99.31%**
6026. **`drivers/soundwire/amd_init.c`** -> AI Confidence: **99.31%**
6027. **`drivers/soundwire/cadence_master.c`** -> AI Confidence: **99.31%**
6028. **`drivers/soundwire/debugfs.c`** -> AI Confidence: **99.31%**
6029. **`drivers/spi/spi-airoha-snfi.c`** -> AI Confidence: **99.31%**
6030. **`drivers/spi/spi-altera-core.c`** -> AI Confidence: **99.31%**
6031. **`drivers/spi/spi-altera-platform.c`** -> AI Confidence: **99.31%**
6032. **`drivers/spi/spi-apple.c`** -> AI Confidence: **99.31%**
6033. **`drivers/spi/spi-ar934x.c`** -> AI Confidence: **99.31%**
6034. **`drivers/spi/spi-atmel.c`** -> AI Confidence: **99.31%**
6035. **`drivers/spi/spi-au1550.c`** -> AI Confidence: **99.31%**
6036. **`drivers/spi/spi-bcm-qspi.c`** -> AI Confidence: **99.31%**
6037. **`drivers/spi/spi-bcm63xx-hsspi.c`** -> AI Confidence: **99.31%**
6038. **`drivers/spi/spi-bcm63xx.c`** -> AI Confidence: **99.31%**
6039. **`drivers/spi/spi-bcmbca-hsspi.c`** -> AI Confidence: **99.31%**
6040. **`drivers/spi/spi-bitbang.c`** -> AI Confidence: **99.31%**
6041. **`drivers/spi/spi-cadence.c`** -> AI Confidence: **99.31%**
6042. **`drivers/spi/spi-dw-core.c`** -> AI Confidence: **99.31%**
6043. **`drivers/spi/spi-dw-dma.c`** -> AI Confidence: **99.31%**
6044. **`drivers/spi/spi-fsi.c`** -> AI Confidence: **99.31%**
6045. **`drivers/spi/spi-fsl-cpm.c`** -> AI Confidence: **99.31%**
6046. **`drivers/spi/spi-fsl-dspi.c`** -> AI Confidence: **99.31%**
6047. **`drivers/spi/spi-microchip-core-qspi.c`** -> AI Confidence: **99.31%**
6048. **`drivers/spi/spi-mpc52xx.c`** -> AI Confidence: **99.31%**
6049. **`drivers/spi/spi-mtk-snfi.c`** -> AI Confidence: **99.31%**
6050. **`drivers/spi/spi-mxs.c`** -> AI Confidence: **99.31%**
6051. **`drivers/spi/spi-npcm-pspi.c`** -> AI Confidence: **99.31%**
6052. **`drivers/spi/spi-omap-uwire.c`** -> AI Confidence: **99.31%**
6053. **`drivers/spi/spi-omap2-mcspi.c`** -> AI Confidence: **99.31%**
6054. **`drivers/spi/spi-pl022.c`** -> AI Confidence: **99.31%**
6055. **`drivers/spi/spi-ppc4xx.c`** -> AI Confidence: **99.31%**
6056. **`drivers/spi/spi-pxa2xx.c`** -> AI Confidence: **99.31%**
6057. **`drivers/spi/spi-qup.c`** -> AI Confidence: **99.31%**
6058. **`drivers/spi/spi-realtek-rtl-snand.c`** -> AI Confidence: **99.31%**
6059. **`drivers/spi/spi-rockchip.c`** -> AI Confidence: **99.31%**
6060. **`drivers/spi/spi-s3c64xx.c`** -> AI Confidence: **99.31%**
6061. **`drivers/spi/spi-sc18is602.c`** -> AI Confidence: **99.31%**
6062. **`drivers/spi/spi-sh-msiof.c`** -> AI Confidence: **99.31%**
6063. **`drivers/spi/spi-sh.c`** -> AI Confidence: **99.31%**
6064. **`drivers/spi/spi-sn-f-ospi.c`** -> AI Confidence: **99.31%**
6065. **`drivers/spi/spi-sprd-adi.c`** -> AI Confidence: **99.31%**
6066. **`drivers/spi/spi-stm32.c`** -> AI Confidence: **99.31%**
6067. **`drivers/spi/spi-sun4i.c`** -> AI Confidence: **99.31%**
6068. **`drivers/spi/spi-synquacer.c`** -> AI Confidence: **99.31%**
6069. **`drivers/spi/spi-tegra114.c`** -> AI Confidence: **99.31%**
6070. **`drivers/spi/spi-tegra20-slink.c`** -> AI Confidence: **99.31%**
6071. **`drivers/spi/spi-tegra210-quad.c`** -> AI Confidence: **99.31%**
6072. **`drivers/spi/spi-ti-qspi.c`** -> AI Confidence: **99.31%**
6073. **`drivers/spi/spi-uniphier.c`** -> AI Confidence: **99.31%**
6074. **`drivers/spi/spi-xcomm.c`** -> AI Confidence: **99.31%**
6075. **`drivers/spi/spi-xlp.c`** -> AI Confidence: **99.31%**
6076. **`drivers/spi/spi-zynq-qspi.c`** -> AI Confidence: **99.31%**
6077. **`drivers/spi/spi-zynqmp-gqspi.c`** -> AI Confidence: **99.31%**
6078. **`drivers/spmi/hisi-spmi-controller.c`** -> AI Confidence: **99.31%**
6079. **`drivers/ssb/driver_chipcommon_pmu.c`** -> AI Confidence: **99.31%**
6080. **`drivers/ssb/driver_mipscore.c`** -> AI Confidence: **99.31%**
6081. **`drivers/ssb/driver_pcicore.c`** -> AI Confidence: **99.31%**
6082. **`drivers/ssb/embedded.c`** -> AI Confidence: **99.31%**
6083. **`drivers/ssb/pcmcia.c`** -> AI Confidence: **99.31%**
6084. **`drivers/staging/axis-fifo/axis-fifo.c`** -> AI Confidence: **99.31%**
6085. **`drivers/staging/fbtft/fb_agm1264k-fl.c`** -> AI Confidence: **99.31%**
6086. **`drivers/staging/fbtft/fb_hx8340bn.c`** -> AI Confidence: **99.31%**
6087. **`drivers/staging/fbtft/fb_hx8357d.c`** -> AI Confidence: **99.31%**
6088. **`drivers/staging/fbtft/fb_pcd8544.c`** -> AI Confidence: **99.31%**
6089. **`drivers/staging/fbtft/fb_ssd1331.c`** -> AI Confidence: **99.31%**
6090. **`drivers/staging/fbtft/fb_st7789v.c`** -> AI Confidence: **99.31%**
6091. **`drivers/staging/fbtft/fb_tls8204.c`** -> AI Confidence: **99.31%**
6092. **`drivers/staging/fbtft/fbtft-core.c`** -> AI Confidence: **99.31%**
6093. **`drivers/staging/greybus/Documentation/firmware/authenticate.c`** -> AI Confidence: **99.31%**
6094. **`drivers/staging/greybus/Documentation/firmware/firmware.c`** -> AI Confidence: **99.31%**
6095. **`drivers/staging/greybus/audio_module.c`** -> AI Confidence: **99.31%**
6096. **`drivers/staging/greybus/sdio.c`** -> AI Confidence: **99.31%**
6097. **`drivers/staging/iio/frequency/ad9832.c`** -> AI Confidence: **99.31%**
6098. **`drivers/staging/iio/frequency/ad9834.c`** -> AI Confidence: **99.31%**
6099. **`drivers/staging/iio/impedance-analyzer/ad5933.c`** -> AI Confidence: **99.31%**
6100. **`drivers/staging/media/atomisp/pci/atomisp_cmd.c`** -> AI Confidence: **99.31%**
6101. **`drivers/staging/media/atomisp/pci/atomisp_gmin_platform.c`** -> AI Confidence: **99.31%**
6102. **`drivers/staging/media/atomisp/pci/atomisp_ioctl.c`** -> AI Confidence: **99.31%**
6103. **`drivers/staging/media/atomisp/pci/atomisp_v4l2.c`** -> AI Confidence: **99.31%**
6104. **`drivers/staging/media/atomisp/pci/isp/kernels/raw/raw_1.0/ia_css_raw.host.c`** -> AI Confidence: **99.31%**
6105. **`drivers/staging/media/atomisp/pci/runtime/bufq/src/bufq.c`** -> AI Confidence: **99.31%**
6106. **`drivers/staging/media/atomisp/pci/runtime/isys/src/csi_rx_rmgr.c`** -> AI Confidence: **99.31%**
6107. **`drivers/staging/media/atomisp/pci/sh_css.c`** -> AI Confidence: **99.31%**
6108. **`drivers/staging/media/atomisp/pci/sh_css_param_shading.c`** -> AI Confidence: **99.31%**
6109. **`drivers/staging/media/av7110/av7110.c`** -> AI Confidence: **99.31%**
6110. **`drivers/staging/media/av7110/av7110_ca.c`** -> AI Confidence: **99.31%**
6111. **`drivers/staging/media/av7110/sp8870.c`** -> AI Confidence: **99.31%**
6112. **`drivers/staging/media/imx/imx-ic-prp.c`** -> AI Confidence: **99.31%**
6113. **`drivers/staging/media/imx/imx-media-csi.c`** -> AI Confidence: **99.31%**
6114. **`drivers/staging/media/imx/imx-media-of.c`** -> AI Confidence: **99.31%**
6115. **`drivers/staging/media/imx/imx-media-vdic.c`** -> AI Confidence: **99.31%**
6116. **`drivers/staging/media/ipu3/ipu3-css.c`** -> AI Confidence: **99.31%**
6117. **`drivers/staging/media/ipu7/ipu7-buttress.c`** -> AI Confidence: **99.31%**
6118. **`drivers/staging/media/ipu7/ipu7-isys-csi-phy.c`** -> AI Confidence: **99.31%**
6119. **`drivers/staging/media/ipu7/ipu7-isys-subdev.c`** -> AI Confidence: **99.31%**
6120. **`drivers/staging/media/ipu7/ipu7-mmu.c`** -> AI Confidence: **99.31%**
6121. **`drivers/staging/media/meson/vdec/vdec_hevc.c`** -> AI Confidence: **99.31%**
6122. **`drivers/staging/media/sunxi/cedrus/cedrus_hw.c`** -> AI Confidence: **99.31%**
6123. **`drivers/staging/media/tegra-video/tegra20.c`** -> AI Confidence: **99.31%**
6124. **`drivers/staging/most/net/net.c`** -> AI Confidence: **99.31%**
6125. **`drivers/staging/nvec/nvec_power.c`** -> AI Confidence: **99.31%**
6126. **`drivers/staging/octeon/ethernet-rx.c`** -> AI Confidence: **99.31%**
6127. **`drivers/staging/octeon/ethernet-spi.c`** -> AI Confidence: **99.31%**
6128. **`drivers/staging/octeon/ethernet-tx.c`** -> AI Confidence: **99.31%**
6129. **`drivers/staging/octeon/ethernet.c`** -> AI Confidence: **99.31%**
6130. **`drivers/staging/sm750fb/sm750_cursor.c`** -> AI Confidence: **99.31%**
6131. **`drivers/staging/sm750fb/sm750_hw.c`** -> AI Confidence: **99.31%**
6132. **`drivers/staging/vme_user/vme_fake.c`** -> AI Confidence: **99.31%**
6133. **`drivers/staging/vme_user/vme_tsi148.c`** -> AI Confidence: **99.31%**
6134. **`drivers/staging/vme_user/vme_user.c`** -> AI Confidence: **99.31%**
6135. **`drivers/tee/amdtee/call.c`** -> AI Confidence: **99.31%**
6136. **`drivers/tee/optee/protmem.c`** -> AI Confidence: **99.31%**
6137. **`drivers/tee/optee/rpc.c`** -> AI Confidence: **99.31%**
6138. **`drivers/thermal/intel/int340x_thermal/acpi_thermal_rel.c`** -> AI Confidence: **99.31%**
6139. **`drivers/thermal/intel/int340x_thermal/int340x_thermal_zone.c`** -> AI Confidence: **99.31%**
6140. **`drivers/thermal/intel/int340x_thermal/processor_thermal_device.c`** -> AI Confidence: **99.31%**
6141. **`drivers/thermal/intel/intel_pch_thermal.c`** -> AI Confidence: **99.31%**
6142. **`drivers/thermal/intel/intel_soc_dts_iosf.c`** -> AI Confidence: **99.31%**
6143. **`drivers/thermal/k3_j72xx_bandgap.c`** -> AI Confidence: **99.31%**
6144. **`drivers/thermal/qcom/tsens.c`** -> AI Confidence: **99.31%**
6145. **`drivers/thermal/ti-soc-thermal/ti-bandgap.c`** -> AI Confidence: **99.31%**
6146. **`drivers/thunderbolt/switch.c`** -> AI Confidence: **99.31%**
6147. **`drivers/thunderbolt/tunnel.c`** -> AI Confidence: **99.31%**
6148. **`drivers/tty/amiserial.c`** -> AI Confidence: **99.31%**
6149. **`drivers/tty/hvc/hvc_dcc.c`** -> AI Confidence: **99.31%**
6150. **`drivers/tty/hvc/hvc_iucv.c`** -> AI Confidence: **99.31%**
6151. **`drivers/tty/hvc/hvc_opal.c`** -> AI Confidence: **99.31%**
6152. **`drivers/tty/hvc/hvc_riscv_sbi.c`** -> AI Confidence: **99.31%**
6153. **`drivers/tty/hvc/hvc_rtas.c`** -> AI Confidence: **99.31%**
6154. **`drivers/tty/hvc/hvc_xen.c`** -> AI Confidence: **99.31%**
6155. **`drivers/tty/ipwireless/main.c`** -> AI Confidence: **99.31%**
6156. **`drivers/tty/moxa.c`** -> AI Confidence: **99.31%**
6157. **`drivers/tty/mxser.c`** -> AI Confidence: **99.31%**
6158. **`drivers/tty/n_gsm.c`** -> AI Confidence: **99.31%**
6159. **`drivers/tty/n_tty.c`** -> AI Confidence: **99.31%**
6160. **`drivers/tty/nozomi.c`** -> AI Confidence: **99.31%**
6161. **`drivers/tty/serial/21285.c`** -> AI Confidence: **99.31%**
6162. **`drivers/tty/serial/8250/8250_core.c`** -> AI Confidence: **99.31%**
6163. **`drivers/tty/serial/8250/8250_early.c`** -> AI Confidence: **99.31%**
6164. **`drivers/tty/serial/8250/8250_em.c`** -> AI Confidence: **99.31%**
6165. **`drivers/tty/serial/8250/8250_fintek.c`** -> AI Confidence: **99.31%**
6166. **`drivers/tty/serial/8250/8250_men_mcb.c`** -> AI Confidence: **99.31%**
6167. **`drivers/tty/serial/8250/8250_parisc.c`** -> AI Confidence: **99.31%**
6168. **`drivers/tty/serial/8250/8250_pci.c`** -> AI Confidence: **99.31%**
6169. **`drivers/tty/serial/8250/8250_pci1xxxx.c`** -> AI Confidence: **99.31%**
6170. **`drivers/tty/serial/8250/8250_platform.c`** -> AI Confidence: **99.31%**
6171. **`drivers/tty/serial/8250/8250_port.c`** -> AI Confidence: **99.31%**
6172. **`drivers/tty/serial/8250/8250_rsa.c`** -> AI Confidence: **99.31%**
6173. **`drivers/tty/serial/8250/serial_cs.c`** -> AI Confidence: **99.31%**
6174. **`drivers/tty/serial/atmel_serial.c`** -> AI Confidence: **99.31%**
6175. **`drivers/tty/serial/clps711x.c`** -> AI Confidence: **99.31%**
6176. **`drivers/tty/serial/cpm_uart.c`** -> AI Confidence: **99.31%**
6177. **`drivers/tty/serial/dz.c`** -> AI Confidence: **99.31%**
6178. **`drivers/tty/serial/earlycon.c`** -> AI Confidence: **99.31%**
6179. **`drivers/tty/serial/icom.c`** -> AI Confidence: **99.31%**
6180. **`drivers/tty/serial/imx.c`** -> AI Confidence: **99.31%**
6181. **`drivers/tty/serial/ip22zilog.c`** -> AI Confidence: **99.31%**
6182. **`drivers/tty/serial/jsm/jsm_cls.c`** -> AI Confidence: **99.31%**
6183. **`drivers/tty/serial/max310x.c`** -> AI Confidence: **99.31%**
6184. **`drivers/tty/serial/mcf.c`** -> AI Confidence: **99.31%**
6185. **`drivers/tty/serial/meson_uart.c`** -> AI Confidence: **99.31%**
6186. **`drivers/tty/serial/mvebu-uart.c`** -> AI Confidence: **99.31%**
6187. **`drivers/tty/serial/mxs-auart.c`** -> AI Confidence: **99.31%**
6188. **`drivers/tty/serial/pmac_zilog.c`** -> AI Confidence: **99.31%**
6189. **`drivers/tty/serial/sb1250-duart.c`** -> AI Confidence: **99.31%**
6190. **`drivers/tty/serial/sccnxp.c`** -> AI Confidence: **99.31%**
6191. **`drivers/tty/serial/serial_txx9.c`** -> AI Confidence: **99.31%**
6192. **`drivers/tty/serial/sh-sci.c`** -> AI Confidence: **99.31%**
6193. **`drivers/tty/serial/sunhv.c`** -> AI Confidence: **99.31%**
6194. **`drivers/tty/serial/sunsu.c`** -> AI Confidence: **99.31%**
6195. **`drivers/tty/serial/sunzilog.c`** -> AI Confidence: **99.31%**
6196. **`drivers/tty/serial/ucc_uart.c`** -> AI Confidence: **99.31%**
6197. **`drivers/tty/serial/xilinx_uartps.c`** -> AI Confidence: **99.31%**
6198. **`drivers/tty/synclink_gt.c`** -> AI Confidence: **99.31%**
6199. **`drivers/tty/tty_jobctrl.c`** -> AI Confidence: **99.31%**
6200. **`drivers/tty/tty_ldsem.c`** -> AI Confidence: **99.31%**
6201. **`drivers/tty/vt/keyboard.c`** -> AI Confidence: **99.31%**
6202. **`drivers/tty/vt/selection.c`** -> AI Confidence: **99.31%**
6203. **`drivers/tty/vt/vc_screen.c`** -> AI Confidence: **99.31%**
6204. **`drivers/tty/vt/vt.c`** -> AI Confidence: **99.31%**
6205. **`drivers/tty/vt/vt_ioctl.c`** -> AI Confidence: **99.31%**
6206. **`drivers/ufs/core/ufs_bsg.c`** -> AI Confidence: **99.31%**
6207. **`drivers/ufs/host/ufs-amd-versal2.c`** -> AI Confidence: **99.31%**
6208. **`drivers/ufs/host/ufs-mediatek.c`** -> AI Confidence: **99.31%**
6209. **`drivers/ufs/host/ufshcd-pltfrm.c`** -> AI Confidence: **99.31%**
6210. **`drivers/uio/uio_dmem_genirq.c`** -> AI Confidence: **99.31%**
6211. **`drivers/uio/uio_mf624.c`** -> AI Confidence: **99.31%**
6212. **`drivers/usb/atm/cxacru.c`** -> AI Confidence: **99.31%**
6213. **`drivers/usb/atm/speedtch.c`** -> AI Confidence: **99.31%**
6214. **`drivers/usb/atm/ueagle-atm.c`** -> AI Confidence: **99.31%**
6215. **`drivers/usb/atm/usbatm.c`** -> AI Confidence: **99.31%**
6216. **`drivers/usb/c67x00/c67x00-drv.c`** -> AI Confidence: **99.31%**
6217. **`drivers/usb/cdns3/cdns3-gadget.c`** -> AI Confidence: **99.31%**
6218. **`drivers/usb/cdns3/cdnsp-pci.c`** -> AI Confidence: **99.31%**
6219. **`drivers/usb/cdns3/cdnsp-ring.c`** -> AI Confidence: **99.31%**
6220. **`drivers/usb/cdns3/core.c`** -> AI Confidence: **99.31%**
6221. **`drivers/usb/chipidea/ci_hdrc_imx.c`** -> AI Confidence: **99.31%**
6222. **`drivers/usb/chipidea/core.c`** -> AI Confidence: **99.31%**
6223. **`drivers/usb/chipidea/host.c`** -> AI Confidence: **99.31%**
6224. **`drivers/usb/chipidea/otg.c`** -> AI Confidence: **99.31%**
6225. **`drivers/usb/chipidea/udc.c`** -> AI Confidence: **99.31%**
6226. **`drivers/usb/class/cdc-acm.c`** -> AI Confidence: **99.31%**
6227. **`drivers/usb/class/usblp.c`** -> AI Confidence: **99.31%**
6228. **`drivers/usb/class/usbtmc.c`** -> AI Confidence: **99.31%**
6229. **`drivers/usb/common/common.c`** -> AI Confidence: **99.31%**
6230. **`drivers/usb/common/usb-conn-gpio.c`** -> AI Confidence: **99.31%**
6231. **`drivers/usb/core/config.c`** -> AI Confidence: **99.31%**
6232. **`drivers/usb/core/devices.c`** -> AI Confidence: **99.31%**
6233. **`drivers/usb/core/devio.c`** -> AI Confidence: **99.31%**
6234. **`drivers/usb/core/driver.c`** -> AI Confidence: **99.31%**
6235. **`drivers/usb/core/hcd-pci.c`** -> AI Confidence: **99.31%**
6236. **`drivers/usb/core/hcd.c`** -> AI Confidence: **99.31%**
6237. **`drivers/usb/core/message.c`** -> AI Confidence: **99.31%**
6238. **`drivers/usb/dwc2/core.c`** -> AI Confidence: **99.31%**
6239. **`drivers/usb/dwc2/gadget.c`** -> AI Confidence: **99.31%**
6240. **`drivers/usb/dwc2/hcd.c`** -> AI Confidence: **99.31%**
6241. **`drivers/usb/dwc2/hcd_ddma.c`** -> AI Confidence: **99.31%**
6242. **`drivers/usb/dwc2/hcd_intr.c`** -> AI Confidence: **99.31%**
6243. **`drivers/usb/dwc2/hcd_queue.c`** -> AI Confidence: **99.31%**
6244. **`drivers/usb/dwc2/platform.c`** -> AI Confidence: **99.31%**
6245. **`drivers/usb/dwc3/core.c`** -> AI Confidence: **99.31%**
6246. **`drivers/usb/dwc3/drd.c`** -> AI Confidence: **99.31%**
6247. **`drivers/usb/dwc3/dwc3-octeon.c`** -> AI Confidence: **99.31%**
6248. **`drivers/usb/dwc3/ep0.c`** -> AI Confidence: **99.31%**
6249. **`drivers/usb/dwc3/gadget.c`** -> AI Confidence: **99.31%**
6250. **`drivers/usb/dwc3/host.c`** -> AI Confidence: **99.31%**
6251. **`drivers/usb/early/xhci-dbc.c`** -> AI Confidence: **99.31%**
6252. **`drivers/usb/fotg210/fotg210-core.c`** -> AI Confidence: **99.31%**
6253. **`drivers/usb/fotg210/fotg210-hcd.c`** -> AI Confidence: **99.31%**
6254. **`drivers/usb/fotg210/fotg210-udc.c`** -> AI Confidence: **99.31%**
6255. **`drivers/usb/gadget/composite.c`** -> AI Confidence: **99.31%**
6256. **`drivers/usb/gadget/config.c`** -> AI Confidence: **99.31%**
6257. **`drivers/usb/gadget/function/f_fs.c`** -> AI Confidence: **99.31%**
6258. **`drivers/usb/gadget/function/f_ncm.c`** -> AI Confidence: **99.31%**
6259. **`drivers/usb/gadget/function/rndis.c`** -> AI Confidence: **99.31%**
6260. **`drivers/usb/gadget/function/uvc_video.c`** -> AI Confidence: **99.31%**
6261. **`drivers/usb/gadget/legacy/ether.c`** -> AI Confidence: **99.31%**
6262. **`drivers/usb/gadget/legacy/g_ffs.c`** -> AI Confidence: **99.31%**
6263. **`drivers/usb/gadget/legacy/inode.c`** -> AI Confidence: **99.31%**
6264. **`drivers/usb/gadget/legacy/multi.c`** -> AI Confidence: **99.31%**
6265. **`drivers/usb/gadget/legacy/nokia.c`** -> AI Confidence: **99.31%**
6266. **`drivers/usb/gadget/legacy/printer.c`** -> AI Confidence: **99.31%**
6267. **`drivers/usb/gadget/legacy/raw_gadget.c`** -> AI Confidence: **99.31%**
6268. **`drivers/usb/gadget/legacy/serial.c`** -> AI Confidence: **99.31%**
6269. **`drivers/usb/gadget/legacy/zero.c`** -> AI Confidence: **99.31%**
6270. **`drivers/usb/gadget/udc/amd5536udc_pci.c`** -> AI Confidence: **99.31%**
6271. **`drivers/usb/gadget/udc/aspeed-vhub/core.c`** -> AI Confidence: **99.31%**
6272. **`drivers/usb/gadget/udc/aspeed-vhub/ep0.c`** -> AI Confidence: **99.31%**
6273. **`drivers/usb/gadget/udc/aspeed-vhub/epn.c`** -> AI Confidence: **99.31%**
6274. **`drivers/usb/gadget/udc/aspeed_udc.c`** -> AI Confidence: **99.31%**
6275. **`drivers/usb/gadget/udc/at91_udc.c`** -> AI Confidence: **99.31%**
6276. **`drivers/usb/gadget/udc/bcm63xx_udc.c`** -> AI Confidence: **99.31%**
6277. **`drivers/usb/gadget/udc/bdc/bdc_ep.c`** -> AI Confidence: **99.31%**
6278. **`drivers/usb/gadget/udc/bdc/bdc_udc.c`** -> AI Confidence: **99.31%**
6279. **`drivers/usb/gadget/udc/cdns2/cdns2-gadget.c`** -> AI Confidence: **99.31%**
6280. **`drivers/usb/gadget/udc/dummy_hcd.c`** -> AI Confidence: **99.31%**
6281. **`drivers/usb/gadget/udc/fsl_qe_udc.c`** -> AI Confidence: **99.31%**
6282. **`drivers/usb/gadget/udc/fsl_udc_core.c`** -> AI Confidence: **99.31%**
6283. **`drivers/usb/gadget/udc/goku_udc.c`** -> AI Confidence: **99.31%**
6284. **`drivers/usb/gadget/udc/lpc32xx_udc.c`** -> AI Confidence: **99.31%**
6285. **`drivers/usb/gadget/udc/m66592-udc.c`** -> AI Confidence: **99.31%**
6286. **`drivers/usb/gadget/udc/net2280.c`** -> AI Confidence: **99.31%**
6287. **`drivers/usb/gadget/udc/pch_udc.c`** -> AI Confidence: **99.31%**
6288. **`drivers/usb/gadget/udc/pxa25x_udc.c`** -> AI Confidence: **99.31%**
6289. **`drivers/usb/gadget/udc/pxa27x_udc.c`** -> AI Confidence: **99.31%**
6290. **`drivers/usb/gadget/udc/r8a66597-udc.c`** -> AI Confidence: **99.31%**
6291. **`drivers/usb/gadget/udc/renesas_usbf.c`** -> AI Confidence: **99.31%**
6292. **`drivers/usb/gadget/udc/snps_udc_core.c`** -> AI Confidence: **99.31%**
6293. **`drivers/usb/gadget/udc/snps_udc_plat.c`** -> AI Confidence: **99.31%**
6294. **`drivers/usb/gadget/udc/tegra-xudc.c`** -> AI Confidence: **99.31%**
6295. **`drivers/usb/gadget/udc/udc-xilinx.c`** -> AI Confidence: **99.31%**
6296. **`drivers/usb/gadget/usbstring.c`** -> AI Confidence: **99.31%**
6297. **`drivers/usb/host/ehci-hcd.c`** -> AI Confidence: **99.31%**
6298. **`drivers/usb/host/ehci-omap.c`** -> AI Confidence: **99.31%**
6299. **`drivers/usb/host/ehci-orion.c`** -> AI Confidence: **99.31%**
6300. **`drivers/usb/host/ehci-pci.c`** -> AI Confidence: **99.31%**
6301. **`drivers/usb/host/ehci-platform.c`** -> AI Confidence: **99.31%**
6302. **`drivers/usb/host/fhci-hcd.c`** -> AI Confidence: **99.31%**
6303. **`drivers/usb/host/fhci-hub.c`** -> AI Confidence: **99.31%**
6304. **`drivers/usb/host/fhci-q.c`** -> AI Confidence: **99.31%**
6305. **`drivers/usb/host/fhci-tds.c`** -> AI Confidence: **99.31%**
6306. **`drivers/usb/host/fsl-mph-dr-of.c`** -> AI Confidence: **99.31%**
6307. **`drivers/usb/host/max3421-hcd.c`** -> AI Confidence: **99.31%**
6308. **`drivers/usb/host/octeon-hcd.c`** -> AI Confidence: **99.31%**
6309. **`drivers/usb/host/ohci-hcd.c`** -> AI Confidence: **99.31%**
6310. **`drivers/usb/host/ohci-omap.c`** -> AI Confidence: **99.31%**
6311. **`drivers/usb/host/ohci-s3c2410.c`** -> AI Confidence: **99.31%**
6312. **`drivers/usb/host/oxu210hp-hcd.c`** -> AI Confidence: **99.31%**
6313. **`drivers/usb/host/pci-quirks.c`** -> AI Confidence: **99.31%**
6314. **`drivers/usb/host/r8a66597-hcd.c`** -> AI Confidence: **99.31%**
6315. **`drivers/usb/host/sl811-hcd.c`** -> AI Confidence: **99.31%**
6316. **`drivers/usb/host/uhci-hcd.c`** -> AI Confidence: **99.31%**
6317. **`drivers/usb/host/xen-hcd.c`** -> AI Confidence: **99.31%**
6318. **`drivers/usb/host/xhci-mem.c`** -> AI Confidence: **99.31%**
6319. **`drivers/usb/host/xhci-pci-renesas.c`** -> AI Confidence: **99.31%**
6320. **`drivers/usb/host/xhci-pci.c`** -> AI Confidence: **99.31%**
6321. **`drivers/usb/host/xhci-tegra.c`** -> AI Confidence: **99.31%**
6322. **`drivers/usb/host/xhci.c`** -> AI Confidence: **99.31%**
6323. **`drivers/usb/image/mdc800.c`** -> AI Confidence: **99.31%**
6324. **`drivers/usb/isp1760/isp1760-hcd.c`** -> AI Confidence: **99.31%**
6325. **`drivers/usb/isp1760/isp1760-if.c`** -> AI Confidence: **99.31%**
6326. **`drivers/usb/misc/appledisplay.c`** -> AI Confidence: **99.31%**
6327. **`drivers/usb/misc/emi26.c`** -> AI Confidence: **99.31%**
6328. **`drivers/usb/misc/emi62.c`** -> AI Confidence: **99.31%**
6329. **`drivers/usb/misc/iowarrior.c`** -> AI Confidence: **99.31%**
6330. **`drivers/usb/misc/legousbtower.c`** -> AI Confidence: **99.31%**
6331. **`drivers/usb/misc/onboard_usb_dev_pdevs.c`** -> AI Confidence: **99.31%**
6332. **`drivers/usb/misc/sisusbvga/sisusbvga.c`** -> AI Confidence: **99.31%**
6333. **`drivers/usb/misc/yurex.c`** -> AI Confidence: **99.31%**
6334. **`drivers/usb/mon/mon_bin.c`** -> AI Confidence: **99.31%**
6335. **`drivers/usb/mtu3/mtu3_host.c`** -> AI Confidence: **99.31%**
6336. **`drivers/usb/mtu3/mtu3_plat.c`** -> AI Confidence: **99.31%**
6337. **`drivers/usb/musb/jz4740.c`** -> AI Confidence: **99.31%**
6338. **`drivers/usb/musb/musb_core.c`** -> AI Confidence: **99.31%**
6339. **`drivers/usb/musb/musb_debugfs.c`** -> AI Confidence: **99.31%**
6340. **`drivers/usb/musb/musb_gadget.c`** -> AI Confidence: **99.31%**
6341. **`drivers/usb/musb/musb_gadget_ep0.c`** -> AI Confidence: **99.31%**
6342. **`drivers/usb/musb/tusb6010.c`** -> AI Confidence: **99.31%**
6343. **`drivers/usb/musb/tusb6010_omap.c`** -> AI Confidence: **99.31%**
6344. **`drivers/usb/musb/ux500.c`** -> AI Confidence: **99.31%**
6345. **`drivers/usb/phy/phy-ab8500-usb.c`** -> AI Confidence: **99.31%**
6346. **`drivers/usb/phy/phy-fsl-usb.c`** -> AI Confidence: **99.31%**
6347. **`drivers/usb/phy/phy-tahvo.c`** -> AI Confidence: **99.31%**
6348. **`drivers/usb/phy/phy-tegra-usb.c`** -> AI Confidence: **99.31%**
6349. **`drivers/usb/serial/ark3116.c`** -> AI Confidence: **99.31%**
6350. **`drivers/usb/serial/belkin_sa.c`** -> AI Confidence: **99.31%**
6351. **`drivers/usb/serial/ch341.c`** -> AI Confidence: **99.31%**
6352. **`drivers/usb/serial/console.c`** -> AI Confidence: **99.31%**
6353. **`drivers/usb/serial/digi_acceleport.c`** -> AI Confidence: **99.31%**
6354. **`drivers/usb/serial/f81534.c`** -> AI Confidence: **99.31%**
6355. **`drivers/usb/serial/garmin_gps.c`** -> AI Confidence: **99.31%**
6356. **`drivers/usb/serial/generic.c`** -> AI Confidence: **99.31%**
6357. **`drivers/usb/serial/io_edgeport.c`** -> AI Confidence: **99.31%**
6358. **`drivers/usb/serial/ir-usb.c`** -> AI Confidence: **99.31%**
6359. **`drivers/usb/serial/iuu_phoenix.c`** -> AI Confidence: **99.31%**
6360. **`drivers/usb/serial/keyspan.c`** -> AI Confidence: **99.31%**
6361. **`drivers/usb/serial/keyspan_pda.c`** -> AI Confidence: **99.31%**
6362. **`drivers/usb/serial/kl5kusb105.c`** -> AI Confidence: **99.31%**
6363. **`drivers/usb/serial/mct_u232.c`** -> AI Confidence: **99.31%**
6364. **`drivers/usb/serial/mos7720.c`** -> AI Confidence: **99.31%**
6365. **`drivers/usb/serial/mos7840.c`** -> AI Confidence: **99.31%**
6366. **`drivers/usb/serial/mxuport.c`** -> AI Confidence: **99.31%**
6367. **`drivers/usb/serial/oti6858.c`** -> AI Confidence: **99.31%**
6368. **`drivers/usb/serial/pl2303.c`** -> AI Confidence: **99.31%**
6369. **`drivers/usb/serial/spcp8x5.c`** -> AI Confidence: **99.31%**
6370. **`drivers/usb/serial/ssu100.c`** -> AI Confidence: **99.31%**
6371. **`drivers/usb/serial/ti_usb_3410_5052.c`** -> AI Confidence: **99.31%**
6372. **`drivers/usb/serial/usb_wwan.c`** -> AI Confidence: **99.31%**
6373. **`drivers/usb/serial/visor.c`** -> AI Confidence: **99.31%**
6374. **`drivers/usb/storage/datafab.c`** -> AI Confidence: **99.31%**
6375. **`drivers/usb/storage/ene_ub6250.c`** -> AI Confidence: **99.31%**
6376. **`drivers/usb/storage/freecom.c`** -> AI Confidence: **99.31%**
6377. **`drivers/usb/storage/isd200.c`** -> AI Confidence: **99.31%**
6378. **`drivers/usb/storage/jumpshot.c`** -> AI Confidence: **99.31%**
6379. **`drivers/usb/storage/option_ms.c`** -> AI Confidence: **99.31%**
6380. **`drivers/usb/storage/realtek_cr.c`** -> AI Confidence: **99.31%**
6381. **`drivers/usb/storage/sddr09.c`** -> AI Confidence: **99.31%**
6382. **`drivers/usb/storage/sddr55.c`** -> AI Confidence: **99.31%**
6383. **`drivers/usb/storage/shuttle_usbat.c`** -> AI Confidence: **99.31%**
6384. **`drivers/usb/storage/transport.c`** -> AI Confidence: **99.31%**
6385. **`drivers/usb/storage/usb.c`** -> AI Confidence: **99.31%**
6386. **`drivers/usb/typec/altmodes/displayport.c`** -> AI Confidence: **99.31%**
6387. **`drivers/usb/typec/altmodes/thunderbolt.c`** -> AI Confidence: **99.31%**
6388. **`drivers/usb/typec/anx7411.c`** -> AI Confidence: **99.31%**
6389. **`drivers/usb/typec/hd3ss3220.c`** -> AI Confidence: **99.31%**
6390. **`drivers/usb/typec/mux/fsa4480.c`** -> AI Confidence: **99.31%**
6391. **`drivers/usb/typec/mux/nb7vpq904m.c`** -> AI Confidence: **99.31%**
6392. **`drivers/usb/typec/mux/ps883x.c`** -> AI Confidence: **99.31%**
6393. **`drivers/usb/typec/mux/tusb1046.c`** -> AI Confidence: **99.31%**
6394. **`drivers/usb/typec/mux/wcd939x-usbss.c`** -> AI Confidence: **99.31%**
6395. **`drivers/usb/typec/rt1719.c`** -> AI Confidence: **99.31%**
6396. **`drivers/usb/typec/stusb160x.c`** -> AI Confidence: **99.31%**
6397. **`drivers/usb/typec/tcpm/fusb302.c`** -> AI Confidence: **99.31%**
6398. **`drivers/usb/typec/tcpm/maxim_contaminant.c`** -> AI Confidence: **99.31%**
6399. **`drivers/usb/typec/tcpm/qcom/qcom_pmic_typec_pdphy.c`** -> AI Confidence: **99.31%**
6400. **`drivers/usb/typec/tcpm/qcom/qcom_pmic_typec_port.c`** -> AI Confidence: **99.31%**
6401. **`drivers/usb/typec/tcpm/tcpci.c`** -> AI Confidence: **99.31%**
6402. **`drivers/usb/typec/tcpm/tcpm.c`** -> AI Confidence: **99.31%**
6403. **`drivers/usb/typec/tipd/core.c`** -> AI Confidence: **99.31%**
6404. **`drivers/usb/typec/ucsi/debugfs.c`** -> AI Confidence: **99.31%**
6405. **`drivers/usb/typec/ucsi/ucsi.c`** -> AI Confidence: **99.31%**
6406. **`drivers/usb/typec/ucsi/ucsi_ccg.c`** -> AI Confidence: **99.31%**
6407. **`drivers/usb/usb-skeleton.c`** -> AI Confidence: **99.31%**
6408. **`drivers/usb/usbip/stub_rx.c`** -> AI Confidence: **99.31%**
6409. **`drivers/usb/usbip/usbip_common.c`** -> AI Confidence: **99.31%**
6410. **`drivers/vdpa/pds/debugfs.c`** -> AI Confidence: **99.31%**
6411. **`drivers/vdpa/vdpa_sim/vdpa_sim_blk.c`** -> AI Confidence: **99.31%**
6412. **`drivers/vdpa/vdpa_sim/vdpa_sim_net.c`** -> AI Confidence: **99.31%**
6413. **`drivers/vfio/pci/mlx5/main.c`** -> AI Confidence: **99.31%**
6414. **`drivers/vfio/pci/pds/lm.c`** -> AI Confidence: **99.31%**
6415. **`drivers/vfio/pci/vfio_pci_intrs.c`** -> AI Confidence: **99.31%**
6416. **`drivers/vfio/pci/vfio_pci_rdwr.c`** -> AI Confidence: **99.31%**
6417. **`drivers/vfio/platform/reset/vfio_platform_amdxgbe.c`** -> AI Confidence: **99.31%**
6418. **`drivers/vfio/platform/reset/vfio_platform_bcmflexrm.c`** -> AI Confidence: **99.31%**
6419. **`drivers/vfio/platform/vfio_platform_common.c`** -> AI Confidence: **99.31%**
6420. **`drivers/vfio/platform/vfio_platform_irq.c`** -> AI Confidence: **99.31%**
6421. **`drivers/video/backlight/88pm860x_bl.c`** -> AI Confidence: **99.31%**
6422. **`drivers/video/backlight/as3711_bl.c`** -> AI Confidence: **99.31%**
6423. **`drivers/video/backlight/da903x_bl.c`** -> AI Confidence: **99.31%**
6424. **`drivers/video/backlight/ktd253-backlight.c`** -> AI Confidence: **99.31%**
6425. **`drivers/video/backlight/lm3639_bl.c`** -> AI Confidence: **99.31%**
6426. **`drivers/video/backlight/lp855x_bl.c`** -> AI Confidence: **99.31%**
6427. **`drivers/video/backlight/mp3309c.c`** -> AI Confidence: **99.31%**
6428. **`drivers/video/backlight/pandora_bl.c`** -> AI Confidence: **99.31%**
6429. **`drivers/video/backlight/pwm_bl.c`** -> AI Confidence: **99.31%**
6430. **`drivers/video/backlight/qcom-wled.c`** -> AI Confidence: **99.31%**
6431. **`drivers/video/backlight/tdo24m.c`** -> AI Confidence: **99.31%**
6432. **`drivers/video/backlight/tps65217_bl.c`** -> AI Confidence: **99.31%**
6433. **`drivers/video/backlight/wm831x_bl.c`** -> AI Confidence: **99.31%**
6434. **`drivers/video/console/newport_con.c`** -> AI Confidence: **99.31%**
6435. **`drivers/video/console/vgacon.c`** -> AI Confidence: **99.31%**
6436. **`drivers/video/fbdev/68328fb.c`** -> AI Confidence: **99.31%**
6437. **`drivers/video/fbdev/asiliantfb.c`** -> AI Confidence: **99.31%**
6438. **`drivers/video/fbdev/atafb.c`** -> AI Confidence: **99.31%**
6439. **`drivers/video/fbdev/aty/aty128fb.c`** -> AI Confidence: **99.31%**
6440. **`drivers/video/fbdev/aty/mach64_cursor.c`** -> AI Confidence: **99.31%**
6441. **`drivers/video/fbdev/au1200fb.c`** -> AI Confidence: **99.31%**
6442. **`drivers/video/fbdev/broadsheetfb.c`** -> AI Confidence: **99.31%**
6443. **`drivers/video/fbdev/cirrusfb.c`** -> AI Confidence: **99.31%**
6444. **`drivers/video/fbdev/clps711x-fb.c`** -> AI Confidence: **99.31%**
6445. **`drivers/video/fbdev/cobalt_lcdfb.c`** -> AI Confidence: **99.31%**
6446. **`drivers/video/fbdev/controlfb.c`** -> AI Confidence: **99.31%**
6447. **`drivers/video/fbdev/core/bitblit.c`** -> AI Confidence: **99.31%**
6448. **`drivers/video/fbdev/core/fbcon.c`** -> AI Confidence: **99.31%**
6449. **`drivers/video/fbdev/core/fbcon_ccw.c`** -> AI Confidence: **99.31%**
6450. **`drivers/video/fbdev/core/fbcon_cw.c`** -> AI Confidence: **99.31%**
6451. **`drivers/video/fbdev/core/fbcon_ud.c`** -> AI Confidence: **99.31%**
6452. **`drivers/video/fbdev/core/fbmem.c`** -> AI Confidence: **99.31%**
6453. **`drivers/video/fbdev/core/tileblit.c`** -> AI Confidence: **99.31%**
6454. **`drivers/video/fbdev/cyber2000fb.c`** -> AI Confidence: **99.31%**
6455. **`drivers/video/fbdev/dnfb.c`** -> AI Confidence: **99.31%**
6456. **`drivers/video/fbdev/efifb.c`** -> AI Confidence: **99.31%**
6457. **`drivers/video/fbdev/ep93xx-fb.c`** -> AI Confidence: **99.31%**
6458. **`drivers/video/fbdev/fsl-diu-fb.c`** -> AI Confidence: **99.31%**
6459. **`drivers/video/fbdev/gbefb.c`** -> AI Confidence: **99.31%**
6460. **`drivers/video/fbdev/goldfishfb.c`** -> AI Confidence: **99.31%**
6461. **`drivers/video/fbdev/grvga.c`** -> AI Confidence: **99.31%**
6462. **`drivers/video/fbdev/gxt4500.c`** -> AI Confidence: **99.31%**
6463. **`drivers/video/fbdev/hecubafb.c`** -> AI Confidence: **99.31%**
6464. **`drivers/video/fbdev/hgafb.c`** -> AI Confidence: **99.31%**
6465. **`drivers/video/fbdev/hitfb.c`** -> AI Confidence: **99.31%**
6466. **`drivers/video/fbdev/hpfb.c`** -> AI Confidence: **99.31%**
6467. **`drivers/video/fbdev/i740fb.c`** -> AI Confidence: **99.31%**
6468. **`drivers/video/fbdev/i810/i810_main.c`** -> AI Confidence: **99.31%**
6469. **`drivers/video/fbdev/imsttfb.c`** -> AI Confidence: **99.31%**
6470. **`drivers/video/fbdev/kyro/fbdev.c`** -> AI Confidence: **99.31%**
6471. **`drivers/video/fbdev/matrox/matroxfb_crtc2.c`** -> AI Confidence: **99.31%**
6472. **`drivers/video/fbdev/matrox/matroxfb_maven.c`** -> AI Confidence: **99.31%**
6473. **`drivers/video/fbdev/mb862xx/mb862xxfb_accel.c`** -> AI Confidence: **99.31%**
6474. **`drivers/video/fbdev/mb862xx/mb862xxfbdrv.c`** -> AI Confidence: **99.31%**
6475. **`drivers/video/fbdev/metronomefb.c`** -> AI Confidence: **99.31%**
6476. **`drivers/video/fbdev/mmp/hw/mmp_ctrl.c`** -> AI Confidence: **99.31%**
6477. **`drivers/video/fbdev/n411.c`** -> AI Confidence: **99.31%**
6478. **`drivers/video/fbdev/neofb.c`** -> AI Confidence: **99.31%**
6479. **`drivers/video/fbdev/ocfb.c`** -> AI Confidence: **99.31%**
6480. **`drivers/video/fbdev/omap/lcd_dma.c`** -> AI Confidence: **99.31%**
6481. **`drivers/video/fbdev/omap/lcdc.c`** -> AI Confidence: **99.31%**
6482. **`drivers/video/fbdev/omap/omapfb_main.c`** -> AI Confidence: **99.31%**
6483. **`drivers/video/fbdev/omap2/omapfb/dss/dispc-compat.c`** -> AI Confidence: **99.31%**
6484. **`drivers/video/fbdev/omap2/omapfb/dss/dispc.c`** -> AI Confidence: **99.31%**
6485. **`drivers/video/fbdev/omap2/omapfb/dss/display.c`** -> AI Confidence: **99.31%**
6486. **`drivers/video/fbdev/omap2/omapfb/dss/dss.c`** -> AI Confidence: **99.31%**
6487. **`drivers/video/fbdev/omap2/omapfb/dss/hdmi4_core.c`** -> AI Confidence: **99.31%**
6488. **`drivers/video/fbdev/omap2/omapfb/dss/hdmi_phy.c`** -> AI Confidence: **99.31%**
6489. **`drivers/video/fbdev/omap2/omapfb/dss/overlay.c`** -> AI Confidence: **99.31%**
6490. **`drivers/video/fbdev/omap2/omapfb/dss/pll.c`** -> AI Confidence: **99.31%**
6491. **`drivers/video/fbdev/omap2/omapfb/omapfb-ioctl.c`** -> AI Confidence: **99.31%**
6492. **`drivers/video/fbdev/omap2/omapfb/omapfb-main.c`** -> AI Confidence: **99.31%**
6493. **`drivers/video/fbdev/pm2fb.c`** -> AI Confidence: **99.31%**
6494. **`drivers/video/fbdev/pm3fb.c`** -> AI Confidence: **99.31%**
6495. **`drivers/video/fbdev/ps3fb.c`** -> AI Confidence: **99.31%**
6496. **`drivers/video/fbdev/pvr2fb.c`** -> AI Confidence: **99.31%**
6497. **`drivers/video/fbdev/pxa168fb.c`** -> AI Confidence: **99.31%**
6498. **`drivers/video/fbdev/pxafb.c`** -> AI Confidence: **99.31%**
6499. **`drivers/video/fbdev/riva/fbdev.c`** -> AI Confidence: **99.31%**
6500. **`drivers/video/fbdev/s1d13xxxfb.c`** -> AI Confidence: **99.31%**
6501. **`drivers/video/fbdev/s3c-fb.c`** -> AI Confidence: **99.31%**
6502. **`drivers/video/fbdev/s3fb.c`** -> AI Confidence: **99.31%**
6503. **`drivers/video/fbdev/sa1100fb.c`** -> AI Confidence: **99.31%**
6504. **`drivers/video/fbdev/savage/savagefb-i2c.c`** -> AI Confidence: **99.31%**
6505. **`drivers/video/fbdev/savage/savagefb_driver.c`** -> AI Confidence: **99.31%**
6506. **`drivers/video/fbdev/sh7760fb.c`** -> AI Confidence: **99.31%**
6507. **`drivers/video/fbdev/sh_mobile_lcdcfb.c`** -> AI Confidence: **99.31%**
6508. **`drivers/video/fbdev/sis/sis_accel.c`** -> AI Confidence: **99.31%**
6509. **`drivers/video/fbdev/sm501fb.c`** -> AI Confidence: **99.31%**
6510. **`drivers/video/fbdev/sstfb.c`** -> AI Confidence: **99.31%**
6511. **`drivers/video/fbdev/stifb.c`** -> AI Confidence: **99.31%**
6512. **`drivers/video/fbdev/sunxvr2500.c`** -> AI Confidence: **99.31%**
6513. **`drivers/video/fbdev/tdfxfb.c`** -> AI Confidence: **99.31%**
6514. **`drivers/video/fbdev/tgafb.c`** -> AI Confidence: **99.31%**
6515. **`drivers/video/fbdev/tridentfb.c`** -> AI Confidence: **99.31%**
6516. **`drivers/video/fbdev/udlfb.c`** -> AI Confidence: **99.31%**
6517. **`drivers/video/fbdev/uvesafb.c`** -> AI Confidence: **99.31%**
6518. **`drivers/video/fbdev/vfb.c`** -> AI Confidence: **99.31%**
6519. **`drivers/video/fbdev/vga16fb.c`** -> AI Confidence: **99.31%**
6520. **`drivers/video/fbdev/vt8500lcdfb.c`** -> AI Confidence: **99.31%**
6521. **`drivers/video/fbdev/xilinxfb.c`** -> AI Confidence: **99.31%**
6522. **`drivers/video/hdmi.c`** -> AI Confidence: **99.31%**
6523. **`drivers/video/sticore.c`** -> AI Confidence: **99.31%**
6524. **`drivers/virt/acrn/hsm.c`** -> AI Confidence: **99.31%**
6525. **`drivers/virt/acrn/ioreq.c`** -> AI Confidence: **99.31%**
6526. **`drivers/virt/fsl_hypervisor.c`** -> AI Confidence: **99.31%**
6527. **`drivers/virt/nitro_enclaves/ne_misc_dev.c`** -> AI Confidence: **99.31%**
6528. **`drivers/virt/vboxguest/vboxguest_core.c`** -> AI Confidence: **99.31%**
6529. **`drivers/virt/vboxguest/vboxguest_utils.c`** -> AI Confidence: **99.31%**
6530. **`drivers/virtio/virtio_mem.c`** -> AI Confidence: **99.31%**
6531. **`drivers/w1/masters/omap_hdq.c`** -> AI Confidence: **99.31%**
6532. **`drivers/w1/slaves/w1_ds2413.c`** -> AI Confidence: **99.31%**
6533. **`drivers/w1/slaves/w1_ds2423.c`** -> AI Confidence: **99.31%**
6534. **`drivers/w1/slaves/w1_ds2430.c`** -> AI Confidence: **99.31%**
6535. **`drivers/w1/slaves/w1_ds2431.c`** -> AI Confidence: **99.31%**
6536. **`drivers/w1/slaves/w1_ds250x.c`** -> AI Confidence: **99.31%**
6537. **`drivers/w1/slaves/w1_ds2805.c`** -> AI Confidence: **99.31%**
6538. **`drivers/w1/slaves/w1_ds28e17.c`** -> AI Confidence: **99.31%**
6539. **`drivers/w1/w1_int.c`** -> AI Confidence: **99.31%**
6540. **`drivers/watchdog/advantechwdt.c`** -> AI Confidence: **99.31%**
6541. **`drivers/watchdog/alim7101_wdt.c`** -> AI Confidence: **99.31%**
6542. **`drivers/watchdog/at91sam9_wdt.c`** -> AI Confidence: **99.31%**
6543. **`drivers/watchdog/ath79_wdt.c`** -> AI Confidence: **99.31%**
6544. **`drivers/watchdog/cpwd.c`** -> AI Confidence: **99.31%**
6545. **`drivers/watchdog/eurotechwdt.c`** -> AI Confidence: **99.31%**
6546. **`drivers/watchdog/f71808e_wdt.c`** -> AI Confidence: **99.31%**
6547. **`drivers/watchdog/iTCO_wdt.c`** -> AI Confidence: **99.31%**
6548. **`drivers/watchdog/ib700wdt.c`** -> AI Confidence: **99.31%**
6549. **`drivers/watchdog/ibmasr.c`** -> AI Confidence: **99.31%**
6550. **`drivers/watchdog/it87_wdt.c`** -> AI Confidence: **99.31%**
6551. **`drivers/watchdog/m54xx_wdt.c`** -> AI Confidence: **99.31%**
6552. **`drivers/watchdog/mixcomwd.c`** -> AI Confidence: **99.31%**
6553. **`drivers/watchdog/mlx_wdt.c`** -> AI Confidence: **99.31%**
6554. **`drivers/watchdog/npcm_wdt.c`** -> AI Confidence: **99.31%**
6555. **`drivers/watchdog/octeon-wdt-main.c`** -> AI Confidence: **99.31%**
6556. **`drivers/watchdog/pcwd.c`** -> AI Confidence: **99.31%**
6557. **`drivers/watchdog/pcwd_pci.c`** -> AI Confidence: **99.31%**
6558. **`drivers/watchdog/pcwd_usb.c`** -> AI Confidence: **99.31%**
6559. **`drivers/watchdog/rti_wdt.c`** -> AI Confidence: **99.31%**
6560. **`drivers/watchdog/sa1100_wdt.c`** -> AI Confidence: **99.31%**
6561. **`drivers/watchdog/sbc60xxwdt.c`** -> AI Confidence: **99.31%**
6562. **`drivers/watchdog/sbc7240_wdt.c`** -> AI Confidence: **99.31%**
6563. **`drivers/watchdog/sbc8360.c`** -> AI Confidence: **99.31%**
6564. **`drivers/watchdog/sbc_fitpc2_wdt.c`** -> AI Confidence: **99.31%**
6565. **`drivers/watchdog/sbsa_gwdt.c`** -> AI Confidence: **99.31%**
6566. **`drivers/watchdog/sc1200wdt.c`** -> AI Confidence: **99.31%**
6567. **`drivers/watchdog/sc520_wdt.c`** -> AI Confidence: **99.31%**
6568. **`drivers/watchdog/sch311x_wdt.c`** -> AI Confidence: **99.31%**
6569. **`drivers/watchdog/smsc37b787_wdt.c`** -> AI Confidence: **99.31%**
6570. **`drivers/watchdog/sun4v_wdt.c`** -> AI Confidence: **99.31%**
6571. **`drivers/watchdog/w83877f_wdt.c`** -> AI Confidence: **99.31%**
6572. **`drivers/watchdog/w83977f_wdt.c`** -> AI Confidence: **99.31%**
6573. **`drivers/watchdog/wafer5823wdt.c`** -> AI Confidence: **99.31%**
6574. **`drivers/watchdog/watchdog_core.c`** -> AI Confidence: **99.31%**
6575. **`drivers/watchdog/wdt.c`** -> AI Confidence: **99.31%**
6576. **`drivers/watchdog/wdt285.c`** -> AI Confidence: **99.31%**
6577. **`drivers/watchdog/wdt977.c`** -> AI Confidence: **99.31%**
6578. **`drivers/watchdog/wdt_pci.c`** -> AI Confidence: **99.31%**
6579. **`drivers/xen/arm-device.c`** -> AI Confidence: **99.31%**
6580. **`drivers/xen/balloon.c`** -> AI Confidence: **99.31%**
6581. **`drivers/xen/events/events_2l.c`** -> AI Confidence: **99.31%**
6582. **`drivers/xen/evtchn.c`** -> AI Confidence: **99.31%**
6583. **`drivers/xen/features.c`** -> AI Confidence: **99.31%**
6584. **`drivers/xen/gntdev.c`** -> AI Confidence: **99.31%**
6585. **`drivers/xen/manage.c`** -> AI Confidence: **99.31%**
6586. **`drivers/xen/mcelog.c`** -> AI Confidence: **99.31%**
6587. **`drivers/xen/pci.c`** -> AI Confidence: **99.31%**
6588. **`drivers/xen/platform-pci.c`** -> AI Confidence: **99.31%**
6589. **`drivers/xen/pvcalls-back.c`** -> AI Confidence: **99.31%**
6590. **`drivers/xen/time.c`** -> AI Confidence: **99.31%**
6591. **`drivers/xen/unpopulated-alloc.c`** -> AI Confidence: **99.31%**
6592. **`drivers/xen/xen-acpi-processor.c`** -> AI Confidence: **99.31%**
6593. **`drivers/xen/xen-pciback/pci_stub.c`** -> AI Confidence: **99.31%**
6594. **`drivers/zorro/zorro.c`** -> AI Confidence: **99.31%**
6595. **`fs/9p/v9fs.c`** -> AI Confidence: **99.31%**
6596. **`fs/9p/vfs_addr.c`** -> AI Confidence: **99.31%**
6597. **`fs/9p/vfs_file.c`** -> AI Confidence: **99.31%**
6598. **`fs/9p/vfs_inode.c`** -> AI Confidence: **99.31%**
6599. **`fs/affs/super.c`** -> AI Confidence: **99.31%**
6600. **`fs/afs/addr_list.c`** -> AI Confidence: **99.31%**
6601. **`fs/afs/cell.c`** -> AI Confidence: **99.31%**
6602. **`fs/afs/cm_security.c`** -> AI Confidence: **99.31%**
6603. **`fs/afs/dir_search.c`** -> AI Confidence: **99.31%**
6604. **`fs/afs/main.c`** -> AI Confidence: **99.31%**
6605. **`fs/afs/misc.c`** -> AI Confidence: **99.31%**
6606. **`fs/afs/rotate.c`** -> AI Confidence: **99.31%**
6607. **`fs/afs/security.c`** -> AI Confidence: **99.31%**
6608. **`fs/afs/write.c`** -> AI Confidence: **99.31%**
6609. **`fs/attr.c`** -> AI Confidence: **99.31%**
6610. **`fs/autofs/dev-ioctl.c`** -> AI Confidence: **99.31%**
6611. **`fs/binfmt_elf.c`** -> AI Confidence: **99.31%**
6612. **`fs/binfmt_elf_fdpic.c`** -> AI Confidence: **99.31%**
6613. **`fs/binfmt_misc.c`** -> AI Confidence: **99.31%**
6614. **`fs/btrfs/acl.c`** -> AI Confidence: **99.31%**
6615. **`fs/btrfs/backref.c`** -> AI Confidence: **99.31%**
6616. **`fs/btrfs/block-group.c`** -> AI Confidence: **99.31%**
6617. **`fs/btrfs/block-rsv.c`** -> AI Confidence: **99.31%**
6618. **`fs/btrfs/compression.c`** -> AI Confidence: **99.31%**
6619. **`fs/btrfs/ctree.c`** -> AI Confidence: **99.31%**
6620. **`fs/btrfs/defrag.c`** -> AI Confidence: **99.31%**
6621. **`fs/btrfs/dev-replace.c`** -> AI Confidence: **99.31%**
6622. **`fs/btrfs/direct-io.c`** -> AI Confidence: **99.31%**
6623. **`fs/btrfs/disk-io.c`** -> AI Confidence: **99.31%**
6624. **`fs/btrfs/extent-io-tree.c`** -> AI Confidence: **99.31%**
6625. **`fs/btrfs/extent-tree.c`** -> AI Confidence: **99.31%**
6626. **`fs/btrfs/file-item.c`** -> AI Confidence: **99.31%**
6627. **`fs/btrfs/file.c`** -> AI Confidence: **99.31%**
6628. **`fs/btrfs/free-space-cache.c`** -> AI Confidence: **99.31%**
6629. **`fs/btrfs/inode-item.c`** -> AI Confidence: **99.31%**
6630. **`fs/btrfs/inode.c`** -> AI Confidence: **99.31%**
6631. **`fs/btrfs/ioctl.c`** -> AI Confidence: **99.31%**
6632. **`fs/btrfs/ordered-data.c`** -> AI Confidence: **99.31%**
6633. **`fs/btrfs/print-tree.c`** -> AI Confidence: **99.31%**
6634. **`fs/btrfs/qgroup.c`** -> AI Confidence: **99.31%**
6635. **`fs/btrfs/raid-stripe-tree.c`** -> AI Confidence: **99.31%**
6636. **`fs/btrfs/ref-verify.c`** -> AI Confidence: **99.31%**
6637. **`fs/btrfs/reflink.c`** -> AI Confidence: **99.31%**
6638. **`fs/btrfs/relocation.c`** -> AI Confidence: **99.31%**
6639. **`fs/btrfs/scrub.c`** -> AI Confidence: **99.31%**
6640. **`fs/btrfs/send.c`** -> AI Confidence: **99.31%**
6641. **`fs/btrfs/space-info.c`** -> AI Confidence: **99.31%**
6642. **`fs/btrfs/super.c`** -> AI Confidence: **99.31%**
6643. **`fs/btrfs/tests/extent-io-tests.c`** -> AI Confidence: **99.31%**
6644. **`fs/btrfs/tests/extent-map-tests.c`** -> AI Confidence: **99.31%**
6645. **`fs/btrfs/tree-checker.c`** -> AI Confidence: **99.31%**
6646. **`fs/btrfs/tree-log.c`** -> AI Confidence: **99.31%**
6647. **`fs/btrfs/uuid-tree.c`** -> AI Confidence: **99.31%**
6648. **`fs/btrfs/verity.c`** -> AI Confidence: **99.31%**
6649. **`fs/btrfs/volumes.c`** -> AI Confidence: **99.31%**
6650. **`fs/btrfs/xattr.c`** -> AI Confidence: **99.31%**
6651. **`fs/btrfs/zoned.c`** -> AI Confidence: **99.31%**
6652. **`fs/btrfs/zstd.c`** -> AI Confidence: **99.31%**
6653. **`fs/buffer.c`** -> AI Confidence: **99.31%**
6654. **`fs/cachefiles/xattr.c`** -> AI Confidence: **99.31%**
6655. **`fs/ceph/acl.c`** -> AI Confidence: **99.31%**
6656. **`fs/ceph/addr.c`** -> AI Confidence: **99.31%**
6657. **`fs/ceph/caps.c`** -> AI Confidence: **99.31%**
6658. **`fs/ceph/crypto.c`** -> AI Confidence: **99.31%**
6659. **`fs/ceph/dir.c`** -> AI Confidence: **99.31%**
6660. **`fs/ceph/file.c`** -> AI Confidence: **99.31%**
6661. **`fs/ceph/inode.c`** -> AI Confidence: **99.31%**
6662. **`fs/ceph/locks.c`** -> AI Confidence: **99.31%**
6663. **`fs/ceph/mds_client.c`** -> AI Confidence: **99.31%**
6664. **`fs/ceph/mdsmap.c`** -> AI Confidence: **99.31%**
6665. **`fs/ceph/xattr.c`** -> AI Confidence: **99.31%**
6666. **`fs/coda/coda_linux.c`** -> AI Confidence: **99.31%**
6667. **`fs/coda/psdev.c`** -> AI Confidence: **99.31%**
6668. **`fs/coredump.c`** -> AI Confidence: **99.31%**
6669. **`fs/cramfs/inode.c`** -> AI Confidence: **99.31%**
6670. **`fs/crypto/crypto.c`** -> AI Confidence: **99.31%**
6671. **`fs/d_path.c`** -> AI Confidence: **99.31%**
6672. **`fs/direct-io.c`** -> AI Confidence: **99.31%**
6673. **`fs/dlm/ast.c`** -> AI Confidence: **99.31%**
6674. **`fs/dlm/debug_fs.c`** -> AI Confidence: **99.31%**
6675. **`fs/dlm/dir.c`** -> AI Confidence: **99.31%**
6676. **`fs/dlm/lock.c`** -> AI Confidence: **99.31%**
6677. **`fs/dlm/lowcomms.c`** -> AI Confidence: **99.31%**
6678. **`fs/dlm/main.c`** -> AI Confidence: **99.31%**
6679. **`fs/dlm/midcomms.c`** -> AI Confidence: **99.31%**
6680. **`fs/dlm/plock.c`** -> AI Confidence: **99.31%**
6681. **`fs/dlm/recover.c`** -> AI Confidence: **99.31%**
6682. **`fs/dlm/recoverd.c`** -> AI Confidence: **99.31%**
6683. **`fs/dlm/user.c`** -> AI Confidence: **99.31%**
6684. **`fs/ecryptfs/crypto.c`** -> AI Confidence: **99.31%**
6685. **`fs/ecryptfs/main.c`** -> AI Confidence: **99.31%**
6686. **`fs/ecryptfs/miscdev.c`** -> AI Confidence: **99.31%**
6687. **`fs/ecryptfs/mmap.c`** -> AI Confidence: **99.31%**
6688. **`fs/erofs/super.c`** -> AI Confidence: **99.31%**
6689. **`fs/eventpoll.c`** -> AI Confidence: **99.31%**
6690. **`fs/exfat/balloc.c`** -> AI Confidence: **99.31%**
6691. **`fs/exfat/dir.c`** -> AI Confidence: **99.31%**
6692. **`fs/exfat/file.c`** -> AI Confidence: **99.31%**
6693. **`fs/exfat/misc.c`** -> AI Confidence: **99.31%**
6694. **`fs/exfat/namei.c`** -> AI Confidence: **99.31%**
6695. **`fs/exfat/super.c`** -> AI Confidence: **99.31%**
6696. **`fs/ext2/acl.c`** -> AI Confidence: **99.31%**
6697. **`fs/ext2/balloc.c`** -> AI Confidence: **99.31%**
6698. **`fs/ext2/ialloc.c`** -> AI Confidence: **99.31%**
6699. **`fs/ext2/inode.c`** -> AI Confidence: **99.31%**
6700. **`fs/ext2/ioctl.c`** -> AI Confidence: **99.31%**
6701. **`fs/ext2/super.c`** -> AI Confidence: **99.31%**
6702. **`fs/ext2/xattr.c`** -> AI Confidence: **99.31%**
6703. **`fs/ext4/balloc.c`** -> AI Confidence: **99.31%**
6704. **`fs/ext4/block_validity.c`** -> AI Confidence: **99.31%**
6705. **`fs/ext4/dir.c`** -> AI Confidence: **99.31%**
6706. **`fs/ext4/extents.c`** -> AI Confidence: **99.31%**
6707. **`fs/ext4/extents_status.c`** -> AI Confidence: **99.31%**
6708. **`fs/ext4/file.c`** -> AI Confidence: **99.31%**
6709. **`fs/ext4/fsync.c`** -> AI Confidence: **99.31%**
6710. **`fs/ext4/ialloc.c`** -> AI Confidence: **99.31%**
6711. **`fs/ext4/inline.c`** -> AI Confidence: **99.31%**
6712. **`fs/ext4/inode.c`** -> AI Confidence: **99.31%**
6713. **`fs/ext4/ioctl.c`** -> AI Confidence: **99.31%**
6714. **`fs/ext4/move_extent.c`** -> AI Confidence: **99.31%**
6715. **`fs/ext4/namei.c`** -> AI Confidence: **99.31%**
6716. **`fs/ext4/readpage.c`** -> AI Confidence: **99.31%**
6717. **`fs/ext4/super.c`** -> AI Confidence: **99.31%**
6718. **`fs/ext4/xattr.c`** -> AI Confidence: **99.31%**
6719. **`fs/f2fs/checkpoint.c`** -> AI Confidence: **99.31%**
6720. **`fs/f2fs/data.c`** -> AI Confidence: **99.31%**
6721. **`fs/f2fs/debug.c`** -> AI Confidence: **99.31%**
6722. **`fs/f2fs/file.c`** -> AI Confidence: **99.31%**
6723. **`fs/f2fs/gc.c`** -> AI Confidence: **99.31%**
6724. **`fs/f2fs/inode.c`** -> AI Confidence: **99.31%**
6725. **`fs/f2fs/namei.c`** -> AI Confidence: **99.31%**
6726. **`fs/f2fs/recovery.c`** -> AI Confidence: **99.31%**
6727. **`fs/f2fs/super.c`** -> AI Confidence: **99.31%**
6728. **`fs/fat/dir.c`** -> AI Confidence: **99.31%**
6729. **`fs/fat/file.c`** -> AI Confidence: **99.31%**
6730. **`fs/fat/inode.c`** -> AI Confidence: **99.31%**
6731. **`fs/fat/namei_vfat.c`** -> AI Confidence: **99.31%**
6732. **`fs/fhandle.c`** -> AI Confidence: **99.31%**
6733. **`fs/filesystems.c`** -> AI Confidence: **99.31%**
6734. **`fs/freevxfs/vxfs_fshead.c`** -> AI Confidence: **99.31%**
6735. **`fs/freevxfs/vxfs_lookup.c`** -> AI Confidence: **99.31%**
6736. **`fs/fs_context.c`** -> AI Confidence: **99.31%**
6737. **`fs/fsopen.c`** -> AI Confidence: **99.31%**
6738. **`fs/gfs2/aops.c`** -> AI Confidence: **99.31%**
6739. **`fs/gfs2/bmap.c`** -> AI Confidence: **99.31%**
6740. **`fs/gfs2/dir.c`** -> AI Confidence: **99.31%**
6741. **`fs/gfs2/file.c`** -> AI Confidence: **99.31%**
6742. **`fs/gfs2/inode.c`** -> AI Confidence: **99.31%**
6743. **`fs/gfs2/log.c`** -> AI Confidence: **99.31%**
6744. **`fs/gfs2/main.c`** -> AI Confidence: **99.31%**
6745. **`fs/gfs2/ops_fstype.c`** -> AI Confidence: **99.31%**
6746. **`fs/gfs2/quota.c`** -> AI Confidence: **99.31%**
6747. **`fs/gfs2/trans.c`** -> AI Confidence: **99.31%**
6748. **`fs/hfs/inode.c`** -> AI Confidence: **99.31%**
6749. **`fs/hfsplus/bnode.c`** -> AI Confidence: **99.31%**
6750. **`fs/hfsplus/dir.c`** -> AI Confidence: **99.31%**
6751. **`fs/hfsplus/inode.c`** -> AI Confidence: **99.31%**
6752. **`fs/hfsplus/options.c`** -> AI Confidence: **99.31%**
6753. **`fs/hfsplus/super.c`** -> AI Confidence: **99.31%**
6754. **`fs/hostfs/hostfs_user.c`** -> AI Confidence: **99.31%**
6755. **`fs/hpfs/super.c`** -> AI Confidence: **99.31%**
6756. **`fs/ioctl.c`** -> AI Confidence: **99.31%**
6757. **`fs/iomap/direct-io.c`** -> AI Confidence: **99.31%**
6758. **`fs/isofs/compress.c`** -> AI Confidence: **99.31%**
6759. **`fs/jbd2/journal.c`** -> AI Confidence: **99.31%**
6760. **`fs/jbd2/transaction.c`** -> AI Confidence: **99.31%**
6761. **`fs/jffs2/acl.c`** -> AI Confidence: **99.31%**
6762. **`fs/jffs2/background.c`** -> AI Confidence: **99.31%**
6763. **`fs/jffs2/fs.c`** -> AI Confidence: **99.31%**
6764. **`fs/jffs2/gc.c`** -> AI Confidence: **99.31%**
6765. **`fs/jffs2/readinode.c`** -> AI Confidence: **99.31%**
6766. **`fs/jffs2/scan.c`** -> AI Confidence: **99.31%**
6767. **`fs/jffs2/summary.c`** -> AI Confidence: **99.31%**
6768. **`fs/jffs2/wbuf.c`** -> AI Confidence: **99.31%**
6769. **`fs/jffs2/write.c`** -> AI Confidence: **99.31%**
6770. **`fs/jffs2/xattr.c`** -> AI Confidence: **99.31%**
6771. **`fs/jfs/acl.c`** -> AI Confidence: **99.31%**
6772. **`fs/jfs/file.c`** -> AI Confidence: **99.31%**
6773. **`fs/jfs/inode.c`** -> AI Confidence: **99.31%**
6774. **`fs/jfs/jfs_dmap.c`** -> AI Confidence: **99.31%**
6775. **`fs/jfs/jfs_dtree.c`** -> AI Confidence: **99.31%**
6776. **`fs/jfs/jfs_imap.c`** -> AI Confidence: **99.31%**
6777. **`fs/jfs/jfs_inode.c`** -> AI Confidence: **99.31%**
6778. **`fs/jfs/jfs_logmgr.c`** -> AI Confidence: **99.31%**
6779. **`fs/jfs/jfs_mount.c`** -> AI Confidence: **99.31%**
6780. **`fs/jfs/jfs_txnmgr.c`** -> AI Confidence: **99.31%**
6781. **`fs/jfs/jfs_xtree.c`** -> AI Confidence: **99.31%**
6782. **`fs/jfs/namei.c`** -> AI Confidence: **99.31%**
6783. **`fs/jfs/xattr.c`** -> AI Confidence: **99.31%**
6784. **`fs/lockd/host.c`** -> AI Confidence: **99.31%**
6785. **`fs/mpage.c`** -> AI Confidence: **99.31%**
6786. **`fs/netfs/direct_read.c`** -> AI Confidence: **99.31%**
6787. **`fs/netfs/iterator.c`** -> AI Confidence: **99.31%**
6788. **`fs/netfs/read_collect.c`** -> AI Confidence: **99.31%**
6789. **`fs/netfs/read_pgpriv2.c`** -> AI Confidence: **99.31%**
6790. **`fs/nfs/client.c`** -> AI Confidence: **99.31%**
6791. **`fs/nfs/dir.c`** -> AI Confidence: **99.31%**
6792. **`fs/nfs/direct.c`** -> AI Confidence: **99.31%**
6793. **`fs/nfs/file.c`** -> AI Confidence: **99.31%**
6794. **`fs/nfs/getroot.c`** -> AI Confidence: **99.31%**
6795. **`fs/nfs/inode.c`** -> AI Confidence: **99.31%**
6796. **`fs/nfs/namespace.c`** -> AI Confidence: **99.31%**
6797. **`fs/nfs/nfs3acl.c`** -> AI Confidence: **99.31%**
6798. **`fs/nfs/nfs40client.c`** -> AI Confidence: **99.31%**
6799. **`fs/nfs/nfs42proc.c`** -> AI Confidence: **99.31%**
6800. **`fs/nfs/nfs4file.c`** -> AI Confidence: **99.31%**
6801. **`fs/nfs/nfs4namespace.c`** -> AI Confidence: **99.31%**
6802. **`fs/nfs/nfs4renewd.c`** -> AI Confidence: **99.31%**
6803. **`fs/nfs/nfs4state.c`** -> AI Confidence: **99.31%**
6804. **`fs/nfs/nfsroot.c`** -> AI Confidence: **99.31%**
6805. **`fs/nfs/super.c`** -> AI Confidence: **99.31%**
6806. **`fs/nfsd/blocklayoutxdr.c`** -> AI Confidence: **99.31%**
6807. **`fs/nfsd/nfs4acl.c`** -> AI Confidence: **99.31%**
6808. **`fs/nfsd/nfscache.c`** -> AI Confidence: **99.31%**
6809. **`fs/nfsd/vfs.c`** -> AI Confidence: **99.31%**
6810. **`fs/nilfs2/ioctl.c`** -> AI Confidence: **99.31%**
6811. **`fs/nilfs2/page.c`** -> AI Confidence: **99.31%**
6812. **`fs/nilfs2/recovery.c`** -> AI Confidence: **99.31%**
6813. **`fs/nilfs2/segment.c`** -> AI Confidence: **99.31%**
6814. **`fs/nilfs2/sufile.c`** -> AI Confidence: **99.31%**
6815. **`fs/nilfs2/super.c`** -> AI Confidence: **99.31%**
6816. **`fs/notify/fanotify/fanotify_user.c`** -> AI Confidence: **99.31%**
6817. **`fs/ntfs3/file.c`** -> AI Confidence: **99.31%**
6818. **`fs/ntfs3/frecord.c`** -> AI Confidence: **99.31%**
6819. **`fs/ntfs3/fsntfs.c`** -> AI Confidence: **99.31%**
6820. **`fs/ntfs3/index.c`** -> AI Confidence: **99.31%**
6821. **`fs/ntfs3/inode.c`** -> AI Confidence: **99.31%**
6822. **`fs/ntfs3/lznt.c`** -> AI Confidence: **99.31%**
6823. **`fs/ntfs3/run.c`** -> AI Confidence: **99.31%**
6824. **`fs/ntfs3/super.c`** -> AI Confidence: **99.31%**
6825. **`fs/ntfs3/xattr.c`** -> AI Confidence: **99.31%**
6826. **`fs/ocfs2/acl.c`** -> AI Confidence: **99.31%**
6827. **`fs/ocfs2/alloc.c`** -> AI Confidence: **99.31%**
6828. **`fs/ocfs2/aops.c`** -> AI Confidence: **99.31%**
6829. **`fs/ocfs2/buffer_head_io.c`** -> AI Confidence: **99.31%**
6830. **`fs/ocfs2/cluster/heartbeat.c`** -> AI Confidence: **99.31%**
6831. **`fs/ocfs2/cluster/quorum.c`** -> AI Confidence: **99.31%**
6832. **`fs/ocfs2/cluster/tcp.c`** -> AI Confidence: **99.31%**
6833. **`fs/ocfs2/dcache.c`** -> AI Confidence: **99.31%**
6834. **`fs/ocfs2/dir.c`** -> AI Confidence: **99.31%**
6835. **`fs/ocfs2/dlm/dlmast.c`** -> AI Confidence: **99.31%**
6836. **`fs/ocfs2/dlm/dlmconvert.c`** -> AI Confidence: **99.31%**
6837. **`fs/ocfs2/dlm/dlmdomain.c`** -> AI Confidence: **99.31%**
6838. **`fs/ocfs2/dlm/dlmlock.c`** -> AI Confidence: **99.31%**
6839. **`fs/ocfs2/dlm/dlmrecovery.c`** -> AI Confidence: **99.31%**
6840. **`fs/ocfs2/dlm/dlmthread.c`** -> AI Confidence: **99.31%**
6841. **`fs/ocfs2/dlm/dlmunlock.c`** -> AI Confidence: **99.31%**
6842. **`fs/ocfs2/export.c`** -> AI Confidence: **99.31%**
6843. **`fs/ocfs2/extent_map.c`** -> AI Confidence: **99.31%**
6844. **`fs/ocfs2/file.c`** -> AI Confidence: **99.31%**
6845. **`fs/ocfs2/inode.c`** -> AI Confidence: **99.31%**
6846. **`fs/ocfs2/ioctl.c`** -> AI Confidence: **99.31%**
6847. **`fs/ocfs2/journal.c`** -> AI Confidence: **99.31%**
6848. **`fs/ocfs2/localalloc.c`** -> AI Confidence: **99.31%**
6849. **`fs/ocfs2/move_extents.c`** -> AI Confidence: **99.31%**
6850. **`fs/ocfs2/namei.c`** -> AI Confidence: **99.31%**
6851. **`fs/ocfs2/quota_local.c`** -> AI Confidence: **99.31%**
6852. **`fs/ocfs2/refcounttree.c`** -> AI Confidence: **99.31%**
6853. **`fs/ocfs2/resize.c`** -> AI Confidence: **99.31%**
6854. **`fs/ocfs2/suballoc.c`** -> AI Confidence: **99.31%**
6855. **`fs/ocfs2/super.c`** -> AI Confidence: **99.31%**
6856. **`fs/ocfs2/sysfile.c`** -> AI Confidence: **99.31%**
6857. **`fs/omfs/inode.c`** -> AI Confidence: **99.31%**
6858. **`fs/orangefs/devorangefs-req.c`** -> AI Confidence: **99.31%**
6859. **`fs/orangefs/orangefs-sysfs.c`** -> AI Confidence: **99.31%**
6860. **`fs/overlayfs/dir.c`** -> AI Confidence: **99.31%**
6861. **`fs/overlayfs/namei.c`** -> AI Confidence: **99.31%**
6862. **`fs/overlayfs/params.c`** -> AI Confidence: **99.31%**
6863. **`fs/pipe.c`** -> AI Confidence: **99.31%**
6864. **`fs/proc/kcore.c`** -> AI Confidence: **99.31%**
6865. **`fs/proc/page.c`** -> AI Confidence: **99.31%**
6866. **`fs/proc/task_mmu.c`** -> AI Confidence: **99.31%**
6867. **`fs/proc/vmcore.c`** -> AI Confidence: **99.31%**
6868. **`fs/pstore/blk.c`** -> AI Confidence: **99.31%**
6869. **`fs/pstore/platform.c`** -> AI Confidence: **99.31%**
6870. **`fs/pstore/ram_core.c`** -> AI Confidence: **99.31%**
6871. **`fs/pstore/zone.c`** -> AI Confidence: **99.31%**
6872. **`fs/quota/dquot.c`** -> AI Confidence: **99.31%**
6873. **`fs/quota/netlink.c`** -> AI Confidence: **99.31%**
6874. **`fs/quota/quota.c`** -> AI Confidence: **99.31%**
6875. **`fs/quota/quota_tree.c`** -> AI Confidence: **99.31%**
6876. **`fs/read_write.c`** -> AI Confidence: **99.31%**
6877. **`fs/remap_range.c`** -> AI Confidence: **99.31%**
6878. **`fs/resctrl/ctrlmondata.c`** -> AI Confidence: **99.31%**
6879. **`fs/resctrl/pseudo_lock.c`** -> AI Confidence: **99.31%**
6880. **`fs/romfs/super.c`** -> AI Confidence: **99.31%**
6881. **`fs/select.c`** -> AI Confidence: **99.31%**
6882. **`fs/signalfd.c`** -> AI Confidence: **99.31%**
6883. **`fs/smb/client/cifs_debug.c`** -> AI Confidence: **99.31%**
6884. **`fs/smb/client/cifs_spnego.c`** -> AI Confidence: **99.31%**
6885. **`fs/smb/client/cifs_swn.c`** -> AI Confidence: **99.31%**
6886. **`fs/smb/client/cifsacl.c`** -> AI Confidence: **99.31%**
6887. **`fs/smb/client/cifsfs.c`** -> AI Confidence: **99.31%**
6888. **`fs/smb/client/cifsroot.c`** -> AI Confidence: **99.31%**
6889. **`fs/smb/client/cifssmb.c`** -> AI Confidence: **99.31%**
6890. **`fs/smb/client/compress.c`** -> AI Confidence: **99.31%**
6891. **`fs/smb/client/connect.c`** -> AI Confidence: **99.31%**
6892. **`fs/smb/client/dir.c`** -> AI Confidence: **99.31%**
6893. **`fs/smb/client/dns_resolve.c`** -> AI Confidence: **99.31%**
6894. **`fs/smb/client/inode.c`** -> AI Confidence: **99.31%**
6895. **`fs/smb/client/link.c`** -> AI Confidence: **99.31%**
6896. **`fs/smb/client/netmisc.c`** -> AI Confidence: **99.31%**
6897. **`fs/smb/client/readdir.c`** -> AI Confidence: **99.31%**
6898. **`fs/smb/client/reparse.c`** -> AI Confidence: **99.31%**
6899. **`fs/smb/client/sess.c`** -> AI Confidence: **99.31%**
6900. **`fs/smb/client/smb1session.c`** -> AI Confidence: **99.31%**
6901. **`fs/smb/client/smb2file.c`** -> AI Confidence: **99.31%**
6902. **`fs/smb/client/smb2inode.c`** -> AI Confidence: **99.31%**
6903. **`fs/smb/client/smb2ops.c`** -> AI Confidence: **99.31%**
6904. **`fs/smb/client/smb2pdu.c`** -> AI Confidence: **99.31%**
6905. **`fs/smb/client/smbdirect.c`** -> AI Confidence: **99.31%**
6906. **`fs/smb/client/smbencrypt.c`** -> AI Confidence: **99.31%**
6907. **`fs/smb/client/transport.c`** -> AI Confidence: **99.31%**
6908. **`fs/smb/client/xattr.c`** -> AI Confidence: **99.31%**
6909. **`fs/smb/server/auth.c`** -> AI Confidence: **99.31%**
6910. **`fs/smb/server/misc.c`** -> AI Confidence: **99.31%**
6911. **`fs/smb/server/oplock.c`** -> AI Confidence: **99.31%**
6912. **`fs/smb/server/server.c`** -> AI Confidence: **99.31%**
6913. **`fs/smb/server/smb2pdu.c`** -> AI Confidence: **99.31%**
6914. **`fs/smb/server/smb_common.c`** -> AI Confidence: **99.31%**
6915. **`fs/smb/server/smbacl.c`** -> AI Confidence: **99.31%**
6916. **`fs/smb/server/transport_rdma.c`** -> AI Confidence: **99.31%**
6917. **`fs/smb/server/vfs.c`** -> AI Confidence: **99.31%**
6918. **`fs/splice.c`** -> AI Confidence: **99.31%**
6919. **`fs/squashfs/block.c`** -> AI Confidence: **99.31%**
6920. **`fs/squashfs/cache.c`** -> AI Confidence: **99.31%**
6921. **`fs/squashfs/file.c`** -> AI Confidence: **99.31%**
6922. **`fs/squashfs/file_direct.c`** -> AI Confidence: **99.31%**
6923. **`fs/squashfs/namei.c`** -> AI Confidence: **99.31%**
6924. **`fs/squashfs/super.c`** -> AI Confidence: **99.31%**
6925. **`fs/squashfs/xattr.c`** -> AI Confidence: **99.31%**
6926. **`fs/squashfs/xz_wrapper.c`** -> AI Confidence: **99.31%**
6927. **`fs/squashfs/zlib_wrapper.c`** -> AI Confidence: **99.31%**
6928. **`fs/squashfs/zstd_wrapper.c`** -> AI Confidence: **99.31%**
6929. **`fs/ubifs/debug.c`** -> AI Confidence: **99.31%**
6930. **`fs/ubifs/super.c`** -> AI Confidence: **99.31%**
6931. **`fs/udf/dir.c`** -> AI Confidence: **99.31%**
6932. **`fs/udf/file.c`** -> AI Confidence: **99.31%**
6933. **`fs/udf/inode.c`** -> AI Confidence: **99.31%**
6934. **`fs/udf/namei.c`** -> AI Confidence: **99.31%**
6935. **`fs/udf/super.c`** -> AI Confidence: **99.31%**
6936. **`fs/udf/symlink.c`** -> AI Confidence: **99.31%**
6937. **`fs/ufs/balloc.c`** -> AI Confidence: **99.31%**
6938. **`fs/ufs/ialloc.c`** -> AI Confidence: **99.31%**
6939. **`fs/ufs/inode.c`** -> AI Confidence: **99.31%**
6940. **`fs/ufs/super.c`** -> AI Confidence: **99.31%**
6941. **`fs/ufs/util.c`** -> AI Confidence: **99.31%**
6942. **`fs/userfaultfd.c`** -> AI Confidence: **99.31%**
6943. **`fs/utimes.c`** -> AI Confidence: **99.31%**
6944. **`fs/xfs/libxfs/xfs_ag.c`** -> AI Confidence: **99.31%**
6945. **`fs/xfs/libxfs/xfs_ag_resv.c`** -> AI Confidence: **99.31%**
6946. **`fs/xfs/libxfs/xfs_alloc.c`** -> AI Confidence: **99.31%**
6947. **`fs/xfs/libxfs/xfs_attr.c`** -> AI Confidence: **99.31%**
6948. **`fs/xfs/libxfs/xfs_bmap.c`** -> AI Confidence: **99.31%**
6949. **`fs/xfs/libxfs/xfs_btree.c`** -> AI Confidence: **99.31%**
6950. **`fs/xfs/libxfs/xfs_btree_staging.c`** -> AI Confidence: **99.31%**
6951. **`fs/xfs/libxfs/xfs_da_btree.c`** -> AI Confidence: **99.31%**
6952. **`fs/xfs/libxfs/xfs_dir2_block.c`** -> AI Confidence: **99.31%**
6953. **`fs/xfs/libxfs/xfs_dir2_data.c`** -> AI Confidence: **99.31%**
6954. **`fs/xfs/libxfs/xfs_dir2_leaf.c`** -> AI Confidence: **99.31%**
6955. **`fs/xfs/libxfs/xfs_dir2_node.c`** -> AI Confidence: **99.31%**
6956. **`fs/xfs/libxfs/xfs_ialloc.c`** -> AI Confidence: **99.31%**
6957. **`fs/xfs/libxfs/xfs_inode_buf.c`** -> AI Confidence: **99.31%**
6958. **`fs/xfs/libxfs/xfs_inode_fork.c`** -> AI Confidence: **99.31%**
6959. **`fs/xfs/libxfs/xfs_inode_util.c`** -> AI Confidence: **99.31%**
6960. **`fs/xfs/libxfs/xfs_refcount.c`** -> AI Confidence: **99.31%**
6961. **`fs/xfs/libxfs/xfs_rmap.c`** -> AI Confidence: **99.31%**
6962. **`fs/xfs/libxfs/xfs_sb.c`** -> AI Confidence: **99.31%**
6963. **`fs/xfs/scrub/agheader.c`** -> AI Confidence: **99.31%**
6964. **`fs/xfs/scrub/attr.c`** -> AI Confidence: **99.31%**
6965. **`fs/xfs/scrub/attr_repair.c`** -> AI Confidence: **99.31%**
6966. **`fs/xfs/scrub/bmap.c`** -> AI Confidence: **99.31%**
6967. **`fs/xfs/scrub/btree.c`** -> AI Confidence: **99.31%**
6968. **`fs/xfs/scrub/cow_repair.c`** -> AI Confidence: **99.31%**
6969. **`fs/xfs/scrub/dabtree.c`** -> AI Confidence: **99.31%**
6970. **`fs/xfs/scrub/dir.c`** -> AI Confidence: **99.31%**
6971. **`fs/xfs/scrub/dir_repair.c`** -> AI Confidence: **99.31%**
6972. **`fs/xfs/scrub/dirtree.c`** -> AI Confidence: **99.31%**
6973. **`fs/xfs/scrub/dirtree_repair.c`** -> AI Confidence: **99.31%**
6974. **`fs/xfs/scrub/findparent.c`** -> AI Confidence: **99.31%**
6975. **`fs/xfs/scrub/fscounters.c`** -> AI Confidence: **99.31%**
6976. **`fs/xfs/scrub/ialloc.c`** -> AI Confidence: **99.31%**
6977. **`fs/xfs/scrub/ialloc_repair.c`** -> AI Confidence: **99.31%**
6978. **`fs/xfs/scrub/inode.c`** -> AI Confidence: **99.31%**
6979. **`fs/xfs/scrub/listxattr.c`** -> AI Confidence: **99.31%**
6980. **`fs/xfs/scrub/nlinks.c`** -> AI Confidence: **99.31%**
6981. **`fs/xfs/scrub/parent.c`** -> AI Confidence: **99.31%**
6982. **`fs/xfs/scrub/quota.c`** -> AI Confidence: **99.31%**
6983. **`fs/xfs/scrub/quota_repair.c`** -> AI Confidence: **99.31%**
6984. **`fs/xfs/scrub/quotacheck.c`** -> AI Confidence: **99.31%**
6985. **`fs/xfs/scrub/quotacheck_repair.c`** -> AI Confidence: **99.31%**
6986. **`fs/xfs/scrub/rcbag.c`** -> AI Confidence: **99.31%**
6987. **`fs/xfs/scrub/repair.c`** -> AI Confidence: **99.31%**
6988. **`fs/xfs/scrub/rtrefcount_repair.c`** -> AI Confidence: **99.31%**
6989. **`fs/xfs/scrub/scrub.c`** -> AI Confidence: **99.31%**
6990. **`fs/xfs/scrub/symlink.c`** -> AI Confidence: **99.31%**
6991. **`fs/xfs/scrub/symlink_repair.c`** -> AI Confidence: **99.31%**
6992. **`fs/xfs/scrub/tempfile.c`** -> AI Confidence: **99.31%**
6993. **`fs/xfs/scrub/trace.c`** -> AI Confidence: **99.31%**
6994. **`fs/xfs/scrub/xfile.c`** -> AI Confidence: **99.31%**
6995. **`fs/xfs/xfs_acl.c`** -> AI Confidence: **99.31%**
6996. **`fs/xfs/xfs_attr_inactive.c`** -> AI Confidence: **99.31%**
6997. **`fs/xfs/xfs_attr_list.c`** -> AI Confidence: **99.31%**
6998. **`fs/xfs/xfs_bmap_util.c`** -> AI Confidence: **99.31%**
6999. **`fs/xfs/xfs_buf_item_recover.c`** -> AI Confidence: **99.31%**
7000. **`fs/xfs/xfs_dir2_readdir.c`** -> AI Confidence: **99.31%**
7001. **`fs/xfs/xfs_discard.c`** -> AI Confidence: **99.31%**
7002. **`fs/xfs/xfs_export.c`** -> AI Confidence: **99.31%**
7003. **`fs/xfs/xfs_file.c`** -> AI Confidence: **99.31%**
7004. **`fs/xfs/xfs_fsmap.c`** -> AI Confidence: **99.31%**
7005. **`fs/xfs/xfs_fsops.c`** -> AI Confidence: **99.31%**
7006. **`fs/xfs/xfs_inode.c`** -> AI Confidence: **99.31%**
7007. **`fs/xfs/xfs_inode_item.c`** -> AI Confidence: **99.31%**
7008. **`fs/xfs/xfs_inode_item_recover.c`** -> AI Confidence: **99.31%**
7009. **`fs/xfs/xfs_ioctl.c`** -> AI Confidence: **99.31%**
7010. **`fs/xfs/xfs_ioctl32.c`** -> AI Confidence: **99.31%**
7011. **`fs/xfs/xfs_iomap.c`** -> AI Confidence: **99.31%**
7012. **`fs/xfs/xfs_log_recover.c`** -> AI Confidence: **99.31%**
7013. **`fs/xfs/xfs_mount.c`** -> AI Confidence: **99.31%**
7014. **`fs/xfs/xfs_pnfs.c`** -> AI Confidence: **99.31%**
7015. **`fs/xfs/xfs_qm.c`** -> AI Confidence: **99.31%**
7016. **`fs/xfs/xfs_qm_bhv.c`** -> AI Confidence: **99.31%**
7017. **`fs/xfs/xfs_reflink.c`** -> AI Confidence: **99.31%**
7018. **`fs/xfs/xfs_rtalloc.c`** -> AI Confidence: **99.31%**
7019. **`fs/xfs/xfs_super.c`** -> AI Confidence: **99.31%**
7020. **`fs/xfs/xfs_symlink.c`** -> AI Confidence: **99.31%**
7021. **`fs/xfs/xfs_trans.c`** -> AI Confidence: **99.31%**
7022. **`fs/xfs/xfs_trans_ail.c`** -> AI Confidence: **99.31%**
7023. **`fs/xfs/xfs_trans_dquot.c`** -> AI Confidence: **99.31%**
7024. **`fs/xfs/xfs_verify_media.c`** -> AI Confidence: **99.31%**
7025. **`fs/xfs/xfs_xattr.c`** -> AI Confidence: **99.31%**
7026. **`include/linux/hardirq.h`** -> AI Confidence: **99.31%**
7027. **`include/linux/jiffies.h`** -> AI Confidence: **99.31%**
7028. **`include/linux/kernel.h`** -> AI Confidence: **99.31%**
7029. **`include/linux/local_lock_internal.h`** -> AI Confidence: **99.31%**
7030. **`include/linux/mtd/map.h`** -> AI Confidence: **99.31%**
7031. **`include/linux/spinlock.h`** -> AI Confidence: **99.31%**
7032. **`include/linux/string.h`** -> AI Confidence: **99.31%**
7033. **`include/trace/events/fib.h`** -> AI Confidence: **99.31%**
7034. **`include/trace/events/filemap.h`** -> AI Confidence: **99.31%**
7035. **`include/trace/events/mptcp.h`** -> AI Confidence: **99.31%**
7036. **`init/calibrate.c`** -> AI Confidence: **99.31%**
7037. **`init/do_mounts.c`** -> AI Confidence: **99.31%**
7038. **`init/do_mounts_rd.c`** -> AI Confidence: **99.31%**
7039. **`init/initramfs.c`** -> AI Confidence: **99.31%**
7040. **`init/main.c`** -> AI Confidence: **99.31%**
7041. **`io_uring/bpf_filter.c`** -> AI Confidence: **99.31%**
7042. **`io_uring/nop.c`** -> AI Confidence: **99.31%**
7043. **`io_uring/opdef.c`** -> AI Confidence: **99.31%**
7044. **`io_uring/rsrc.c`** -> AI Confidence: **99.31%**
7045. **`io_uring/sqpoll.c`** -> AI Confidence: **99.31%**
7046. **`io_uring/wait.c`** -> AI Confidence: **99.31%**
7047. **`ipc/ipc_sysctl.c`** -> AI Confidence: **99.31%**
7048. **`ipc/msg.c`** -> AI Confidence: **99.31%**
7049. **`ipc/sem.c`** -> AI Confidence: **99.31%**
7050. **`kernel/audit.c`** -> AI Confidence: **99.31%**
7051. **`kernel/auditsc.c`** -> AI Confidence: **99.31%**
7052. **`kernel/bpf/btf.c`** -> AI Confidence: **99.31%**
7053. **`kernel/bpf/cgroup.c`** -> AI Confidence: **99.31%**
7054. **`kernel/bpf/log.c`** -> AI Confidence: **99.31%**
7055. **`kernel/bpf/lpm_trie.c`** -> AI Confidence: **99.31%**
7056. **`kernel/bpf/rqspinlock.c`** -> AI Confidence: **99.31%**
7057. **`kernel/bpf/syscall.c`** -> AI Confidence: **99.31%**
7058. **`kernel/bpf/verifier.c`** -> AI Confidence: **99.31%**
7059. **`kernel/cgroup/cgroup-v1.c`** -> AI Confidence: **99.31%**
7060. **`kernel/cgroup/cpuset.c`** -> AI Confidence: **99.31%**
7061. **`kernel/compat.c`** -> AI Confidence: **99.31%**
7062. **`kernel/crash_core.c`** -> AI Confidence: **99.31%**
7063. **`kernel/crash_reserve.c`** -> AI Confidence: **99.31%**
7064. **`kernel/cred.c`** -> AI Confidence: **99.31%**
7065. **`kernel/dma/pool.c`** -> AI Confidence: **99.31%**
7066. **`kernel/entry/common.c`** -> AI Confidence: **99.31%**
7067. **`kernel/hung_task.c`** -> AI Confidence: **99.31%**
7068. **`kernel/irq/manage.c`** -> AI Confidence: **99.31%**
7069. **`kernel/irq/spurious.c`** -> AI Confidence: **99.31%**
7070. **`kernel/kcsan/report.c`** -> AI Confidence: **99.31%**
7071. **`kernel/kexec.c`** -> AI Confidence: **99.31%**
7072. **`kernel/kexec_core.c`** -> AI Confidence: **99.31%**
7073. **`kernel/kexec_file.c`** -> AI Confidence: **99.31%**
7074. **`kernel/latencytop.c`** -> AI Confidence: **99.31%**
7075. **`kernel/locking/qrwlock.c`** -> AI Confidence: **99.31%**
7076. **`kernel/module/decompress.c`** -> AI Confidence: **99.31%**
7077. **`kernel/module/kmod.c`** -> AI Confidence: **99.31%**
7078. **`kernel/module/stats.c`** -> AI Confidence: **99.31%**
7079. **`kernel/nsproxy.c`** -> AI Confidence: **99.31%**
7080. **`kernel/power/hibernate.c`** -> AI Confidence: **99.31%**
7081. **`kernel/power/process.c`** -> AI Confidence: **99.31%**
7082. **`kernel/power/suspend.c`** -> AI Confidence: **99.31%**
7083. **`kernel/power/swap.c`** -> AI Confidence: **99.31%**
7084. **`kernel/power/user.c`** -> AI Confidence: **99.31%**
7085. **`kernel/ptrace.c`** -> AI Confidence: **99.31%**
7086. **`kernel/rcu/rcuscale.c`** -> AI Confidence: **99.31%**
7087. **`kernel/rcu/rcutorture.c`** -> AI Confidence: **99.31%**
7088. **`kernel/rcu/srcutree.c`** -> AI Confidence: **99.31%**
7089. **`kernel/resource.c`** -> AI Confidence: **99.31%**
7090. **`kernel/scftorture.c`** -> AI Confidence: **99.31%**
7091. **`kernel/seccomp.c`** -> AI Confidence: **99.31%**
7092. **`kernel/signal.c`** -> AI Confidence: **99.31%**
7093. **`kernel/sys.c`** -> AI Confidence: **99.31%**
7094. **`kernel/time/clocksource.c`** -> AI Confidence: **99.31%**
7095. **`kernel/time/posix-stubs.c`** -> AI Confidence: **99.31%**
7096. **`kernel/trace/blktrace.c`** -> AI Confidence: **99.31%**
7097. **`kernel/trace/trace_boot.c`** -> AI Confidence: **99.31%**
7098. **`kernel/trace/trace_eprobe.c`** -> AI Confidence: **99.31%**
7099. **`kernel/trace/trace_events.c`** -> AI Confidence: **99.31%**
7100. **`kernel/trace/trace_events_filter.c`** -> AI Confidence: **99.31%**
7101. **`kernel/trace/trace_events_hist.c`** -> AI Confidence: **99.31%**
7102. **`kernel/trace/trace_events_synth.c`** -> AI Confidence: **99.31%**
7103. **`kernel/trace/trace_preemptirq.c`** -> AI Confidence: **99.31%**
7104. **`kernel/trace/trace_syscalls.c`** -> AI Confidence: **99.31%**
7105. **`kernel/watch_queue.c`** -> AI Confidence: **99.31%**
7106. **`mm/compaction.c`** -> AI Confidence: **99.31%**
7107. **`mm/damon/ops-common.c`** -> AI Confidence: **99.31%**
7108. **`mm/debug.c`** -> AI Confidence: **99.31%**
7109. **`mm/fadvise.c`** -> AI Confidence: **99.31%**
7110. **`mm/filemap.c`** -> AI Confidence: **99.31%**
7111. **`mm/gup.c`** -> AI Confidence: **99.31%**
7112. **`mm/hmm.c`** -> AI Confidence: **99.31%**
7113. **`mm/huge_memory.c`** -> AI Confidence: **99.31%**
7114. **`mm/hugetlb.c`** -> AI Confidence: **99.31%**
7115. **`mm/hugetlb_cma.c`** -> AI Confidence: **99.31%**
7116. **`mm/kasan/init.c`** -> AI Confidence: **99.31%**
7117. **`mm/kfence/report.c`** -> AI Confidence: **99.31%**
7118. **`mm/khugepaged.c`** -> AI Confidence: **99.31%**
7119. **`mm/kmemleak.c`** -> AI Confidence: **99.31%**
7120. **`mm/memblock.c`** -> AI Confidence: **99.31%**
7121. **`mm/memfd.c`** -> AI Confidence: **99.31%**
7122. **`mm/memory-failure.c`** -> AI Confidence: **99.31%**
7123. **`mm/memory.c`** -> AI Confidence: **99.31%**
7124. **`mm/memory_hotplug.c`** -> AI Confidence: **99.31%**
7125. **`mm/mempolicy.c`** -> AI Confidence: **99.31%**
7126. **`mm/memremap.c`** -> AI Confidence: **99.31%**
7127. **`mm/migrate.c`** -> AI Confidence: **99.31%**
7128. **`mm/migrate_device.c`** -> AI Confidence: **99.31%**
7129. **`mm/mincore.c`** -> AI Confidence: **99.31%**
7130. **`mm/mlock.c`** -> AI Confidence: **99.31%**
7131. **`mm/mm_init.c`** -> AI Confidence: **99.31%**
7132. **`mm/mmap_lock.c`** -> AI Confidence: **99.31%**
7133. **`mm/mseal.c`** -> AI Confidence: **99.31%**
7134. **`mm/numa_emulation.c`** -> AI Confidence: **99.31%**
7135. **`mm/numa_memblks.c`** -> AI Confidence: **99.31%**
7136. **`mm/oom_kill.c`** -> AI Confidence: **99.31%**
7137. **`mm/page_frag_cache.c`** -> AI Confidence: **99.31%**
7138. **`mm/page_idle.c`** -> AI Confidence: **99.31%**
7139. **`mm/page_isolation.c`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `187` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `409545` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `drivers/gpu/drm/ci/igt_runner.sh` (SHELL) -> Cumulative Risk: **727.14**
- **Archetype:** `file_cluster_4` (Distance: 11.424 IQR)
- **Magnitude:** 9.89 | **LOC:** 102 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9999%), Safety Score (99.8659%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 18.8), `Anonymous_Block` (Impact: 9.3), `Anonymous_Block` (Impact: 5.2)

### 2. `drivers/gpu/drm/i915/display/intel_psr.c` (C) -> Cumulative Risk: **713.06**
- **Archetype:** `file_cluster_13` (Distance: 13.874 IQR)
- **Magnitude:** 2462.72 | **LOC:** 4609 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (98.4098%)
- **Heaviest Functions:** `_psr_compute_config` (Impact: 366.1), `_psr_flush_handle` (Impact: 343.0), `intel_psr2_config_valid` (Impact: 64.8)

### 3. `kernel/cgroup/cpuset.c` (C) -> Cumulative Risk: **711.53**
- **Archetype:** `file_cluster_8` (Distance: 13.577 IQR)
- **Magnitude:** 4349.82 | **LOC:** 4380 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 90.9%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Safety Score (86.6504%)
- **Heaviest Functions:** `remote_cpus_update` (Impact: 706.1), `validate_change` (Impact: 680.9), `update_parent_effective_cpumask` (Impact: 663.5)

### 4. `kernel/bpf/core.c` (C) -> Cumulative Risk: **706.51**
- **Archetype:** `file_cluster_8` (Distance: 13.735 IQR)
- **Magnitude:** 1737.94 | **LOC:** 3395 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (96.3358%)
- **Heaviest Functions:** `bpf_jit_get_func_addr` (Impact: 49.9), `bpf_prog_array_copy` (Impact: 47.5), `bpf_adj_branches` (Impact: 46.2)

### 5. `drivers/gpu/drm/msm/dsi/dsi_host.c` (C) -> Cumulative Risk: **706.21**
- **Archetype:** `file_cluster_8` (Distance: 13.868 IQR)
- **Magnitude:** 1678.34 | **LOC:** 2668 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (98.9851%)
- **Heaviest Functions:** `dsi_calc_clk_rate_v2` (Impact: 213.4), `msm_dsi_host_power_on` (Impact: 30.0), `dsi_host_parse_lane_data` (Impact: 23.5)

### 6. `arch/x86/kvm/svm/svm.c` (C) -> Cumulative Risk: **705.78**
- **Archetype:** `file_cluster_8` (Distance: 14.238 IQR)
- **Magnitude:** 3465.42 | **LOC:** 5624 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (95.2769%)
- **Heaviest Functions:** `svm_set_vintr` (Impact: 550.2), `svm_get_msr` (Impact: 131.1), `svm_set_msr` (Impact: 119.7)

### 7. `drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd.c` (C) -> Cumulative Risk: **701.26**
- **Archetype:** `file_cluster_13` (Distance: 13.641 IQR)
- **Magnitude:** 951.16 | **LOC:** 917 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9465%)
- **Heaviest Functions:** `amdgpu_amdkfd_get_pcie_bandwidth_mbytes` (Impact: 53.0), `amdgpu_amdkfd_alloc_kernel_mem` (Impact: 46.0), `amdgpu_amdkfd_get_dmabuf_info` (Impact: 43.6)

### 8. `kernel/bpf/tnum.c` (C) -> Cumulative Risk: **700.35**
- **Archetype:** `file_cluster_13` (Distance: 14.07 IQR)
- **Magnitude:** 299.2 | **LOC:** 328 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.5308%)
- **Heaviest Functions:** `tnum_sbin` (Impact: 14.9), `tnum_mul` (Impact: 11.4), `tnum_step` (Impact: 10.7)

### 9. `arch/x86/kvm/vmx/vmx.c` (C) -> Cumulative Risk: **699.76**
- **Archetype:** `file_cluster_8` (Distance: 14.35 IQR)
- **Magnitude:** 6434.5 | **LOC:** 8967 | **CtrlFlow:** 50.4% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (94.3589%)
- **Heaviest Functions:** `vmx_inject_exception` (Impact: 993.2), `handle_ept_violation` (Impact: 560.5), `vmx_setup_uret_msrs` (Impact: 353.5)

### 10. `drivers/gpu/drm/radeon/r600_dpm.c` (C) -> Cumulative Risk: **699.66**
- **Archetype:** `file_cluster_8` (Distance: 13.359 IQR)
- **Magnitude:** 1384.46 | **LOC:** 1369 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (94.8169%)
- **Heaviest Functions:** `r600_parse_extended_power_table` (Impact: 135.2), `r600_is_internal_thermal_sensor` (Impact: 33.1), `r600_dpm_print_class_info` (Impact: 33.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `virt/kvm/kvm_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.05 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.788 IQR)
- **Top Global Matches:** file_cluster_8: 14.05, file_cluster_13: 14.147, file_cluster_11: 14.33
- **Magnitude:** 57379.08 | **LOC:** 6597 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (83.9602%), Tech Debt (11.9103%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 545`, `structural_boundaries: 576`, `args: 99`, `func_start: 91`, `class_start: 126`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1166`, `planned_debt: 2`, `fragile_debt: 6`
* *Architecture:* `io: 3`, `api: 519`, `import: 49`
* *Defense:* `safety: 1`, `doc: 3`, `immutability_locks: 21`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` kvm_para.h, debugfs.h, cpumask.h, kthread.h, rseq.h, vfio.h, pagemap.h, profile.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `net/wireless/nl80211.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.004 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.607 IQR)
- **Top Global Matches:** file_cluster_8: 15.004, file_cluster_11: 15.236, file_cluster_13: 15.275
- **Magnitude:** 19964.26 | **LOC:** 22051 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (87.5997%), Tech Debt (12.2855%)
**Top Internal Functions/Classes:**
  * `nl80211_send_wiphy` (Impact: 948.9)
  * `nl80211_new_station` (Impact: 899.7)
  * `nl80211_trigger_scan` (Impact: 420.6)
  * `nl80211_send_station` (Impact: 351.7)
  * `nl80211_send_iface` (Impact: 193.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3911`, `structural_boundaries: 2831`, `args: 272`, `func_start: 266`, `class_start: 776`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 7174`, `dead_code: 5`, `fragile_debt: 4`, `orphaned_logic: 39`
* *Architecture:* `api: 2340`, `import: 22`
* *Defense:* `safety: 12`, `test: 2`, `immutability_locks: 141`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` nl80211.h, if.h, nospec.h, slab.h, core.h, err.h, netlink.h, if_vlan.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kernel/bpf/verifier.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.176 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.092 IQR)
- **Top Global Matches:** file_cluster_8: 15.176, file_cluster_13: 15.335, file_cluster_11: 15.345
- **Magnitude:** 17724.32 | **LOC:** 26244 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 18.2%
- **Risk Profile:** Cognitive Load (97.136%), Tech Debt (38.7229%)
**Top Internal Functions/Classes:**
  * `check_func_arg` (Impact: 1791.3)
  * `process_iter_arg` (Impact: 1549.3)
  * `do_check` (Impact: 1124.7)
  * `__add_used_map` (Impact: 557.4)
  * `btf_check_func_arg_match` (Impact: 540.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2443`, `structural_boundaries: 2145`, `args: 323`, `func_start: 292`, `class_start: 367`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 4661`, `dead_code: 10`, `planned_debt: 1`, `fragile_debt: 3`, `orphaned_logic: 95`
* *Architecture:* `io: 3`, `api: 1651`, `import: 29`
* *Defense:* `safety: 14`, `immutability_locks: 141`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` netlink.h, cpumask.h, bpf.h, poison.h, kallsyms.h, slab.h, perf_event.h, kernel.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/net/wireless/ath/ath12k/mac.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.063 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.969 IQR)
- **Top Global Matches:** file_cluster_8: 15.063, file_cluster_11: 15.326, file_cluster_13: 15.328
- **Magnitude:** 16391.3 | **LOC:** 15217 | **CtrlFlow:** 50.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (8.9307%)
**Top Internal Functions/Classes:**
  * `__ath12k_set_antenna` (Impact: 862.2)
  * `ath12k_mac_vif_setup_ps` (Impact: 833.2)
  * `ath12k_mac_fill_reg_tpc_info` (Impact: 825.5)
  * `ath12k_mac_update_key_cache` (Impact: 819.1)
  * `ath12k_mac_bitrate_mask_get_single_nss` (Impact: 126.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2074`, `structural_boundaries: 2043`, `args: 243`, `func_start: 258`, `class_start: 711`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 6093`, `dead_code: 1`, `planned_debt: 22`, `fragile_debt: 3`
* *Architecture:* `io: 6`, `api: 1923`, `import: 18`
* *Defense:* `safety: 3`, `immutability_locks: 91`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` debugfs_sta.h, etherdevice.h, mac.h, cfg80211.h, debugfs.h, dp_rx.h, wow.h, hif.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fs/btrfs/inode.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.968 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.959 IQR)
- **Top Global Matches:** file_cluster_13: 14.968, file_cluster_8: 14.984, file_cluster_11: 15.121
- **Magnitude:** 16160.98 | **LOC:** 10776 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (97.0842%), Tech Debt (8.6887%)
**Top Internal Functions/Classes:**
  * `cow_one_range` (Impact: 1211.0)
  * `insert_inline_extent` (Impact: 1142.6)
  * `cow_file_range` (Impact: 1064.2)
    * *Intent:* /* We cannot exceed the maximum inline data size. */
  * `btrfs_set_extent_delalloc` (Impact: 1027.9)
  * `__cow_file_range_inline` (Impact: 997.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 774`, `structural_boundaries: 701`, `args: 79`, `func_start: 79`, `class_start: 278`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2336`, `fragile_debt: 3`
* *Architecture:* `io: 4`, `api: 854`, `import: 69`
* *Defense:* `safety: 18`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` qgroup.h, accessors.h, delayed-inode.h, relocation.h, pagemap.h, magic.h, blk-cgroup.h, time.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/net/ethernet/intel/i40e/i40e_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.092 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.247 IQR)
- **Top Global Matches:** file_cluster_8: 15.092, file_cluster_7: 15.231, file_cluster_13: 15.25
- **Magnitude:** 15344.26 | **LOC:** 16679 | **CtrlFlow:** 55.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (75.9899%), Tech Debt (26.8362%)
**Top Internal Functions/Classes:**
  * `i40e_do_reset` (Impact: 956.0)
  * `i40e_watchdog_subtask` (Impact: 913.9)
    * *Intent:* /** * i40e_control_wait_rx_q * @pf: the PF structure * @pf_q: queue being configured * @enable: star...
  * `i40e_vsi_stop_rings` (Impact: 848.3)
  * `i40e_force_link_state` (Impact: 846.2)
  * `i40e_vsi_map_rings_to_vectors` (Impact: 838.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1547`, `structural_boundaries: 1242`, `args: 261`, `func_start: 217`, `class_start: 329`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 4473`, `dead_code: 14`, `planned_debt: 1`, `orphaned_logic: 65`
* *Architecture:* `io: 13`, `api: 1115`, `import: 15`
* *Defense:* `safety: 3`, `doc: 212`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` i40e.h, i40e_diag.h, i40e_lan_hmc.h, i40e_virtchnl_pf.h, if_macvlan.h, crash_dump.h, i40e_xsk.h, pkt_cls.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mm/percpu.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.71 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.58 IQR)
- **Top Global Matches:** file_cluster_13: 13.71, file_cluster_8: 13.718, file_cluster_11: 14.032
- **Magnitude:** 14441.58 | **LOC:** 3389 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.9287%), Tech Debt (9.1834%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 181`, `args: 49`, `func_start: 45`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 552`, `fragile_debt: 1`
* *Architecture:* `api: 168`, `import: 27`
* *Defense:* `safety: 22`, `doc: 19`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cpumask.h, kmemleak.h, percpu-internal.h, slab.h, percpu-km.c, err.h, log2.h, spinlock.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/net/ethernet/broadcom/bnxt/bnxt.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.807 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.128 IQR)
- **Top Global Matches:** file_cluster_8: 15.807, file_cluster_13: 15.943, file_cluster_11: 16.005
- **Magnitude:** 14431.76 | **LOC:** 17386 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (83.5191%), Tech Debt (25.1758%)
**Top Internal Functions/Classes:**
  * `bnxt_hwrm_set_pause` (Impact: 341.2)
  * `bnxt_gro_func_5731x` (Impact: 151.9)
  * `bnxt_start_xmit` (Impact: 125.9)
  * `__bnxt_hwrm_func_qcaps` (Impact: 94.8)
  * `bnxt_init_chip` (Impact: 78.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1871`, `structural_boundaries: 1819`, `args: 332`, `func_start: 311`, `class_start: 478`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 7558`, `planned_debt: 3`, `fragile_debt: 1`, `orphaned_logic: 76`
* *Architecture:* `io: 17`, `api: 1662`, `import: 64`
* *Defense:* `safety: 20`, `doc: 4`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` cpumask.h, delay.h, if.h, bpf.h, ip6_checksum.h, bnxt_dcb.h, slab.h, time.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/gpu/drm/amd/include/navi10_enum.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.458 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.304 IQR)
- **Top Global Matches:** file_cluster_8: 11.458, file_cluster_7: 12.01, file_cluster_13: 12.171
- **Magnitude:** 14082.78 | **LOC:** 22765 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.5311%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2780`, `class_start: 1390`
* *Risk/State:* `state_mutation: 12372`
* *Architecture:* `api: 1390`
* *Defense:* `doc: 84`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.036
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `drivers/scsi/qla4xxx/ql4_os.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.775 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.086 IQR)
- **Top Global Matches:** file_cluster_8: 14.775, file_cluster_7: 15.012, file_cluster_13: 15.029
- **Magnitude:** 12601.04 | **LOC:** 9959 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.5798%), Tech Debt (8.9452%)
**Top Internal Functions/Classes:**
  * `qla4xxx_recover_adapter` (Impact: 926.2)
  * `qla4xxx_cmd_wait` (Impact: 915.1)
  * `qla4xxx_get_iface_param` (Impact: 429.0)
  * `qla4_attr_is_visible` (Impact: 364.5)
  * `qla4xxx_set_ipv4` (Impact: 304.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2158`, `structural_boundaries: 866`, `args: 194`, `func_start: 148`, `class_start: 324`
* *Risk/State:* `safety_bypasses: 230`, `state_mutation: 4246`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `io: 7`, `api: 1568`, `import: 13`
* *Defense:* `safety: 3`, `doc: 39`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` scsicam.h, ql4_83xx.h, ql4_version.h, inet.h, slab.h, scsi_tcq.h, blkdev.h, iscsi_boot_sysfs.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/net/wireless/realtek/rtw89/fw.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.622 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.945 IQR)
- **Top Global Matches:** file_cluster_8: 14.622, file_cluster_11: 14.925, file_cluster_13: 14.937
- **Magnitude:** 12171.16 | **LOC:** 11220 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.9363%), Tech Debt (21.7467%)
**Top Internal Functions/Classes:**
  * `rtw89_fw_h2c_scan_offload_be` (Impact: 78.8)
  * `rtw89_hw_scan_add_chan_ax` (Impact: 74.1)
  * `rtw89_fw_h2c_add_general_pkt` (Impact: 56.6)
  * `rtw89_hw_scan_add_chan_be` (Impact: 54.6)
  * `fw_txpwr_byrate_entry_valid` (Impact: 52.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1519`, `structural_boundaries: 2373`, `args: 269`, `func_start: 250`, `class_start: 709`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 5713`, `dead_code: 1`, `orphaned_logic: 111`
* *Architecture:* `io: 93`, `api: 2236`, `import: 12`
* *Defense:* `safety: 7`, `immutability_locks: 249`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mac.h, util.h, cam.h, chan.h, fw.h, wow.h, reg.h, if_arp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/net/wireless/realtek/rtw89/coex.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.325 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.081 IQR)
- **Top Global Matches:** file_cluster_8: 15.325, file_cluster_11: 15.529, file_cluster_13: 15.551
- **Magnitude:** 12168.34 | **LOC:** 11907 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.0226%), Tech Debt (11.7222%)
**Top Internal Functions/Classes:**
  * `_set_bt_afh_info_v1` (Impact: 1014.6)
  * `_chk_btc_report` (Impact: 609.1)
  * `rtw89_btc_fw_rpt_ver` (Impact: 228.8)
  * `_set_bt_afh_info_v0` (Impact: 182.4)
  * `_chk_btc_err` (Impact: 170.4)
    * *Intent:* #define BTC_RPT_HDR_SIZE 3 #define BTC_CHK_WLSLOT_DRIFT_MAX 15 #define BTC_CHK_BTSLOT_DRIFT_MAX 15 #...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1708`, `structural_boundaries: 816`, `args: 80`, `func_start: 88`, `class_start: 377`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6246`, `dead_code: 5`, `planned_debt: 1`, `orphaned_logic: 19`
* *Architecture:* `io: 9`, `api: 960`, `import: 8`
* *Defense:* `safety: 31`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mac.h, fw.h, chan.h, reg.h, phy.h, coex.h, debug.h, ps.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/video/fbdev/sis/init301.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.966 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.674 IQR)
- **Top Global Matches:** file_cluster_8: 14.966, file_cluster_7: 15.205, file_cluster_13: 15.245
- **Magnitude:** 11932.0 | **LOC:** 11380 | **CtrlFlow:** 80.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.3489%), Tech Debt (19.2571%)
**Top Internal Functions/Classes:**
  * `SiS_GetVCLK2Ptr` (Impact: 1640.2)
  * `SiS_GetCRT2Data301` (Impact: 414.1)
  * `SetDelayComp661` (Impact: 395.3)
  * `SiS_EnableBridge` (Impact: 302.9)
  * `SiS_GetLVDSDesData` (Impact: 281.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2222`, `structural_boundaries: 535`, `args: 148`, `func_start: 120`
* *Risk/State:* `state_mutation: 4710`, `dead_code: 8`, `planned_debt: 1`, `fragile_debt: 3`, `orphaned_logic: 34`
* *Architecture:* `api: 440`, `import: 3`
* *Defense:* `doc: 50`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` oem300.h, oem310.h, init301.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mm/memory.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.548 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.773 IQR)
- **Top Global Matches:** file_cluster_8: 14.548, file_cluster_13: 14.564, file_cluster_11: 14.769
- **Magnitude:** 11513.36 | **LOC:** 7494 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (89.6348%), Tech Debt (59.2397%)
**Top Internal Functions/Classes:**
  * `vm_insert_pages` (Impact: 1220.7)
  * `vm_mixed_zeropage_allowed` (Impact: 1101.0)
    * *Intent:* * @orig_pte: pte value at @ptep * * Restore a device-exclusive non-swap entry to an ordinary present...
  * `copy_page_range` (Impact: 952.8)
  * `arch_wants_old_prefaulted_pte` (Impact: 772.9)
  * `remove_device_exclusive_entry` (Impact: 762.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 720`, `structural_boundaries: 665`, `args: 126`, `func_start: 122`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1596`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 49`
* *Architecture:* `io: 6`, `api: 697`, `import: 47`
* *Defense:* `doc: 24`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` debugfs.h, gfp.h, pagemap.h, kmem.h, perf_event.h, memory-tiers.h, mmu_context.h, init.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kernel/events/core.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.653 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.171 IQR)
- **Top Global Matches:** file_cluster_8: 14.653, file_cluster_13: 14.855, file_cluster_7: 14.956
- **Magnitude:** 11458.98 | **LOC:** 15373 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (93.486%), Tech Debt (35.5756%)
**Top Internal Functions/Classes:**
  * `__perf_read` (Impact: 770.5)
  * `perf_pmu_output_stop` (Impact: 697.8)
  * `perf_virt_to_phys` (Impact: 616.2)
  * `perf_check_permission` (Impact: 181.2)
  * `perf_event_stop` (Impact: 118.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1429`, `structural_boundaries: 2190`, `args: 448`, `func_start: 420`, `class_start: 540`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 3546`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 8`, `orphaned_logic: 79`
* *Architecture:* `io: 13`, `api: 1405`, `import: 52`
* *Defense:* `safety: 10`, `doc: 2`, `immutability_locks: 48`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hash.h, dcache.h, percpu-rwsem.h, bpf.h, mount.h, slab.h, perf_event.h, compat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/scsi/mpt3sas/mpt3sas_scsih.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.562 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.698 IQR)
- **Top Global Matches:** file_cluster_8: 14.562, file_cluster_7: 14.762, file_cluster_13: 14.847
- **Magnitude:** 11360.82 | **LOC:** 14171 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (63.9906%), Tech Debt (18.9927%)
**Top Internal Functions/Classes:**
  * `_mpt3sas_fw_work` (Impact: 521.4)
  * `_scsih_io_done` (Impact: 235.1)
  * `scsih_map_queues` (Impact: 201.6)
  * `_scsih_scsi_ioc_info` (Impact: 200.1)
  * `_scsih_scan_for_devices_after_reset` (Impact: 108.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2244`, `structural_boundaries: 1072`, `args: 206`, `func_start: 196`, `class_start: 336`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 4309`, `dead_code: 2`, `planned_debt: 6`, `duplicate_logic: 2`, `orphaned_logic: 50`
* *Architecture:* `io: 24`, `api: 1376`, `import: 13`
* *Defense:* `doc: 185`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` delay.h, raid_class.h, mpt3sas_base.h, blkdev.h, kernel.h, pci.h, module.h, sched.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/gpu/drm/amd/include/vega10_enum.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.424 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.346 IQR)
- **Top Global Matches:** file_cluster_8: 11.424, file_cluster_7: 11.986, file_cluster_13: 12.155
- **Magnitude:** 11345.74 | **LOC:** 22533 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.8621%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2900`, `class_start: 1450`
* *Risk/State:* `state_mutation: 9597`
* *Architecture:* `api: 1450`
* *Defense:* `doc: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `drivers/net/ethernet/broadcom/tg3.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.966 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.477 IQR)
- **Top Global Matches:** file_cluster_8: 14.966, file_cluster_13: 15.181, file_cluster_11: 15.256
- **Magnitude:** 11282.28 | **LOC:** 18437 | **CtrlFlow:** 70.1% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (95.6911%), Tech Debt (21.1117%)
**Top Internal Functions/Classes:**
  * `tg3_test_loopback` (Impact: 913.0)
  * `tg3_poll_fw` (Impact: 907.9)
    * *Intent:* /* OK, reset it, and poll the BMCR_RESET bit until it
  * `tg3_stop_block` (Impact: 428.5)
  * `tg3_setup_copper_phy` (Impact: 200.5)
  * `tg3_calc_dma_bndry` (Impact: 165.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1961`, `structural_boundaries: 836`, `args: 198`, `func_start: 199`, `class_start: 75`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 1`, `state_mutation: 4262`, `fragile_debt: 9`, `orphaned_logic: 40`
* *Architecture:* `io: 3`, `api: 791`, `import: 43`
* *Defense:* `safety: 12`, `doc: 2`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hwmon.h, delay.h, if.h, slab.h, hwmon-sysfs.h, netdevice.h, mii.h, brcmphy.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/gpu/drm/amd/display/dc/dml/dcn32/display_mode_vba_util_32.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.84 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.069 IQR)
- **Top Global Matches:** file_cluster_8: 14.84, file_cluster_7: 15.135, file_cluster_13: 15.139
- **Magnitude:** 11275.42 | **LOC:** 6351 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.9805%), Tech Debt (12.7981%)
**Top Internal Functions/Classes:**
  * `dml32_CalculateDETBufferSize` (Impact: 1277.5)
  * `dml32_CalculatePrefetchSchedule` (Impact: 924.0)
  * `dml32_CalculateWatermarksMALLUseAndDRAMS` (Impact: 490.2)
  * `dml32_CalculateOutputLink` (Impact: 353.6)
  * `dml32_TruncToValidBPP` (Impact: 224.2)
    * *Intent:* *RequiresDSC = true;
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1087`, `structural_boundaries: 437`, `args: 41`, `func_start: 49`, `class_start: 67`
* *Risk/State:* `state_mutation: 4592`, `dead_code: 1`, `orphaned_logic: 31`
* *Architecture:* `api: 1492`, `import: 4`
* *Defense:* `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` display_mode_vba_util_32.h, display_mode_lib.h, dml_inline_defs.h, display_mode_vba_32.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/net/ethernet/hisilicon/hns3/hns3pf/hclge_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.891 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.13 IQR)
- **Top Global Matches:** file_cluster_8: 14.891, file_cluster_13: 15.115, file_cluster_11: 15.184
- **Magnitude:** 11216.26 | **LOC:** 12944 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.0379%), Tech Debt (9.3214%)
**Top Internal Functions/Classes:**
  * `hclge_sync_from_add_list` (Impact: 582.5)
  * `hclge_init_ae_dev` (Impact: 137.6)
  * `hclge_get_mac_vlan_cmd_status` (Impact: 58.8)
  * `hclge_reset_ae_dev` (Impact: 53.0)
  * `hclge_set_vlan_filter` (Impact: 41.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1413`, `structural_boundaries: 2113`, `args: 384`, `func_start: 349`, `class_start: 574`
* *Risk/State:* `state_mutation: 5112`, `dead_code: 12`, `orphaned_logic: 17`
* *Architecture:* `io: 22`, `api: 1546`, `import: 26`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` hclge_main.h, hclge_comm_cmd.h, hclge_mbx.h, netdevice.h, hclge_mdio.h, hclge_cmd.h, kernel.h, irq.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fs/smb/server/smb2pdu.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.281 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.87 IQR)
- **Top Global Matches:** file_cluster_8: 15.281, file_cluster_13: 15.367, file_cluster_11: 15.394
- **Magnitude:** 11043.88 | **LOC:** 9271 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (90.2419%), Tech Debt (25.3762%)
**Top Internal Functions/Classes:**
  * `smb2_get_ea` (Impact: 1273.3)
  * `smb2_set_ea` (Impact: 1087.9)
  * `smb2_check_user_session` (Impact: 979.5)
  * `smb2_ioctl` (Impact: 236.8)
  * `smb2_lock` (Impact: 234.2)
    * *Intent:* /** * smb2_populate_readdir_entry() - encode directory entry in smb2 response * buffer * @conn: conn...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1319`, `structural_boundaries: 907`, `args: 133`, `func_start: 104`, `class_start: 250`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 3622`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 1`, `orphaned_logic: 40`
* *Architecture:* `io: 29`, `api: 961`, `import: 35`
* *Defense:* `safety: 12`, `doc: 43`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` mount.h, oplock.h, misc.h, smbacl.h, filelock.h, inetdevice.h, falloc.h, namei.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kernel/trace/trace.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.706 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.399 IQR)
- **Top Global Matches:** file_cluster_8: 14.706, file_cluster_13: 14.852, file_cluster_0: 14.938
- **Magnitude:** 10935.98 | **LOC:** 11036 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (88.5429%), Tech Debt (12.736%)
**Top Internal Functions/Classes:**
  * `trace_event_buffer_lock_reserve` (Impact: 1006.2)
    * *Intent:* /* * trace_parser_put - frees the buffer for trace parser
  * `__find_next_entry` (Impact: 871.1)
  * `set_tracer_flag` (Impact: 86.7)
    * *Intent:* #define STATIC_TEMP_BUF_SIZE 128
  * `tracing_buffers_splice_read` (Impact: 81.9)
  * `enable_instances` (Impact: 81.2)
    * *Intent:* /* * AARGH! We are left with different orders! * The max buffer is our "snapshot" buffer. * When a t...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1431`, `structural_boundaries: 1834`, `args: 390`, `func_start: 372`, `class_start: 383`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 17`, `state_mutation: 3910`, `dead_code: 3`, `planned_debt: 2`, `orphaned_logic: 28`
* *Architecture:* `io: 163`, `api: 1358`, `import: 45`
* *Defense:* `safety: 78`, `doc: 27`, `immutability_locks: 118`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` debugfs.h, pagemap.h, mount.h, kallsyms.h, stacktrace.h, slab.h, trace.h, cleanup.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kernel/bpf/syscall.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.532 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.726 IQR)
- **Top Global Matches:** file_cluster_8: 14.532, file_cluster_13: 14.606, file_cluster_11: 14.713
- **Magnitude:** 10901.86 | **LOC:** 6617 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (98.3795%), Tech Debt (11.7134%)
**Top Internal Functions/Classes:**
  * `bpf_prog_load` (Impact: 1449.7)
  * `bpf_prog_load_fixup_attach_type` (Impact: 1443.1)
  * `bpf_map_copy_value` (Impact: 1349.4)
  * `bpf_map_mmap` (Impact: 1226.1)
  * `bpf_prog_get_info_by_fd` (Impact: 184.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1292`, `structural_boundaries: 896`, `args: 99`, `func_start: 147`, `class_start: 135`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 2083`, `dead_code: 2`, `orphaned_logic: 18`
* *Architecture:* `io: 15`, `api: 984`, `import: 45`
* *Defense:* `safety: 6`, `immutability_locks: 88`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` overflow.h, bpf.h, nospec.h, mmzone.h, slab.h, bpf_trace.h, kernel.h, rcupdate_trace.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/scsi/lpfc/lpfc_init.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.594 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.494 IQR)
- **Top Global Matches:** file_cluster_8: 14.594, file_cluster_7: 14.819, file_cluster_13: 14.853
- **Magnitude:** 10654.26 | **LOC:** 15836 | **CtrlFlow:** 63.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (79.5269%), Tech Debt (9.8666%)
**Top Internal Functions/Classes:**
  * `lpfc_handle_eratt_s4` (Impact: 598.7)
  * `lpfc_sli4_async_sli_evt` (Impact: 566.8)
  * `lpfc_sli4_cgn_parm_chg_evt` (Impact: 216.3)
  * `lpfc_sli4_read_config` (Impact: 167.8)
  * `lpfc_sli4_queue_setup` (Impact: 163.2)
    * *Intent:* /** * lpfc_sli4_async_fc_evt - Process the asynchronous FC link event
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1796`, `structural_boundaries: 1025`, `args: 246`, `func_start: 193`, `class_start: 233`
* *Risk/State:* `safety_bypasses: 33`, `high_risk_execution: 9`, `state_mutation: 4480`, `dead_code: 4`, `orphaned_logic: 27`
* *Architecture:* `io: 17`, `api: 954`, `import: 40`
* *Defense:* `safety: 3`, `doc: 162`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` kthread.h, scsi_host.h, delay.h, slab.h, scsi_tcq.h, lpfc_sli.h, fc_fs.h, spinlock.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/gpu/drm/amd/display/dc/dml/dcn30/display_mode_vba_30.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.085 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.115 IQR)
- **Top Global Matches:** file_cluster_8: 15.085, file_cluster_7: 15.362, file_cluster_13: 15.378
- **Magnitude:** 10620.76 | **LOC:** 6360 | **CtrlFlow:** 71.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.1197%), Tech Debt (8.9582%)
**Top Internal Functions/Classes:**
  * `dml30_ModeSupportAndSystemConfigurationF` (Impact: 727.4)
  * `CalculatePrefetchSchedule` (Impact: 685.9)
  * `DISPCLKDPPCLKDCFCLKDeepSleepPrefetchPara` (Impact: 387.4)
    * *Intent:* *PTEBufferSizeNotExceeded = false;
  * `CalculateVMAndRowBytes` (Impact: 273.2)
    * *Intent:* *VInitPreFill = dml_floor((VRatio + vtaps + 1 + Interlace * 0.5 * VRatio) / 2.0, 1);
  * `CalculateMetaAndPTETimes` (Impact: 206.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1296`, `structural_boundaries: 516`, `args: 53`, `func_start: 33`, `class_start: 77`
* *Risk/State:* `state_mutation: 5045`, `dead_code: 1`, `planned_debt: 3`, `orphaned_logic: 5`
* *Architecture:* `api: 1359`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` display_mode_vba_30.h, display_mode_lib.h, dc.h, dml_inline_defs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `scripts/leaking_addresses.pl` (PERL) | Magnitude: 665.34 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 334, state_mutation: 284, structural_boundaries: 196, branch: 151
- `drivers/staging/rtl8723bs/core/rtw_sta_mgt.c` (C) | Magnitude: 497.04 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 337, indent_tabs: 307, state_mutation: 290, structural_boundaries: 101
- `rust/syn/lookahead.rs` (RUST) | Magnitude: 46.3 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 210, indent_spaces: 72, structural_boundaries: 32, dead_code: 29
- `drivers/usb/gadget/function/uvc_configfs.c` (C) | Magnitude: 2420.5 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 1372, state_mutation: 1261, pointers: 1196, api: 447
- `drivers/staging/rtl8723bs/include/rtw_recv.h` (C) | Magnitude: 238.78 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 184, indent_tabs: 179, structural_boundaries: 97, pointers: 84

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `tools/lib/python/feat/parse_features.py` (PYTHON) | Magnitude: 0.32 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 331, branch: 88, events: 76, state_mutation: 59

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tools/testing/selftests/amd-pstate/Makefile` (MAKEFILE) | Magnitude: 0.06 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 12, branch: 3, structural_boundaries: 2, reflection_metaprogramming: 2
- `scripts/Lindent` (SHELL) | Magnitude: 51.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 24, branch: 22, safety_bypasses: 9, indent_spaces: 8
- `tools/testing/selftests/bpf/prog_tests/btf.c` (C) | Magnitude: 5.34 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 6173, state_mutation: 3942, structural_boundaries: 467, pointers: 436
- `drivers/net/ethernet/intel/ixgbevf/vf.c` (C) | Magnitude: 1008.44 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 356, indent_tabs: 343, pointers: 138, api: 101
- `arch/hexagon/Makefile` (MAKEFILE) | Magnitude: 35.36 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 20, args: 4, reflection_metaprogramming: 4, io: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tools/perf/trace/beauty/clone.sh` (SHELL) | Magnitude: 0.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 12, branch: 6, io: 4, indent_tabs: 4
- `tools/perf/trace/beauty/fspick.sh` (SHELL) | Magnitude: 0.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 12, branch: 6, io: 4, indent_tabs: 4
- `tools/perf/trace/beauty/move_mount_flags.sh` (SHELL) | Magnitude: 0.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 12, branch: 6, io: 4, indent_tabs: 4
- `tools/perf/trace/beauty/sync_file_range.sh` (SHELL) | Magnitude: 0.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 12, branch: 6, io: 4, indent_tabs: 4
- `drivers/gpu/drm/xe/xe_sriov_printk.h` (C) | Magnitude: 15.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: macros: 15, reflection_metaprogramming: 11, indent_tabs: 9, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tools/net/ynl/pyynl/lib/nlspec.py` (PYTHON) | Magnitude: 0.47 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 320, state_mutation: 160, structural_boundaries: 110, branch: 82
- `tools/perf/tests/shell/lib/attr.py` (PYTHON) | Magnitude: 0.29 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 318, structural_boundaries: 90, branch: 86, state_mutation: 51
- `arch/arm64/boot/dts/rockchip/rk3399-nanopi-m4.dts` (C) | Magnitude: 1.77 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 3, ownership: 3, indent_tabs: 3, import: 1
- `arch/m68k/kernel/signal.h` (C) | Magnitude: 15.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, pointers: 7, args: 3, api: 3
- `arch/powerpc/include/asm/livepatch.h` (C) | Magnitude: 3.46 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, macros: 4, pointers: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tools/testing/kunit/kunit_config.py` (PYTHON) | Magnitude: 0.1 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 65, structural_boundaries: 38, branch: 26, api: 19
- `drivers/gpu/nova-core/falcon/gsp.rs` (RUST) | Magnitude: 10.38 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 7, generics: 7, args: 5
- `rust/kernel/module_param.rs` (RUST) | Magnitude: 32.84 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 57, indent_spaces: 51, structural_boundaries: 19, generics: 14
- `rust/macros/helpers.rs` (RUST) | Magnitude: 20.72 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 11, generics: 7, args: 6
- `rust/kernel/pci.rs` (RUST) | Magnitude: 56.24 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 122, indent_spaces: 108, structural_boundaries: 38, generics: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `arch/x86/coco/Makefile` (MAKEFILE) | Magnitude: 15.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 2, state_mutation: 2, dead_code: 1
- `kernel/gcov/Makefile` (MAKEFILE) | Magnitude: 15.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 2, state_mutation: 2, dead_code: 1
- `arch/arm/mach-lpc32xx/Makefile` (MAKEFILE) | Magnitude: 13.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 2, structural_boundaries: 1, dead_code: 1
- `samples/seccomp/Makefile` (MAKEFILE) | Magnitude: 13.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 2, structural_boundaries: 1, dead_code: 1
- `drivers/misc/ocxl/Makefile` (MAKEFILE) | Magnitude: 16.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 3, structural_boundaries: 1, dead_code: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tools/net/sunrpc/xdrgen/generators/enum.py` (PYTHON) | Magnitude: 0.04 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, doc: 16, structural_boundaries: 13, api: 12
- `tools/net/sunrpc/xdrgen/generators/typedef.py` (PYTHON) | Magnitude: 0.12 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 220, encapsulation: 54, structural_boundaries: 45, branch: 37
- `tools/net/sunrpc/xdrgen/generators/pointer.py` (PYTHON) | Magnitude: 0.06 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 216, encapsulation: 45, structural_boundaries: 43, doc: 32
- `tools/net/sunrpc/xdrgen/generators/struct.py` (PYTHON) | Magnitude: 0.06 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 216, encapsulation: 45, structural_boundaries: 43, doc: 32
- `tools/net/sunrpc/xdrgen/generators/union.py` (PYTHON) | Magnitude: 0.14 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 228, structural_boundaries: 67, branch: 64, encapsulation: 52

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tools/testing/selftests/mm/uffd-stress.c` (C) | Magnitude: 0.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 159, state_mutation: 133, pointers: 92, branch: 47
- `tools/testing/selftests/net/mptcp/mptcp_sockopt.sh` (SHELL) | Magnitude: 0.27 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 214, state_mutation: 102, safety_bypasses: 89, branch: 87
- `rust/kernel/rbtree.rs` (RUST) | Magnitude: 401.42 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: doc: 557, indent_spaces: 503, structural_boundaries: 200, generics: 171
- `tools/testing/selftests/ublk/test_common.sh` (SHELL) | Magnitude: 0.37 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 260, branch: 151, structural_boundaries: 94, state_mutation: 94
- `tools/testing/selftests/bpf/prog_tests/send_signal_sched_switch.c` (C) | Magnitude: 0.08 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 36, indent_tabs: 25, concurrency: 12, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `rust/syn/meta.rs` (RUST) | Magnitude: 58.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 336, indent_spaces: 79, dead_code: 43, structural_boundaries: 30
- `rust/kernel/alloc.rs` (RUST) | Magnitude: 13.32 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 136, indent_spaces: 26, pointers: 8, api: 7
- `drivers/spi/spi-bitbang-txrx.h` (C) | Magnitude: 137.08 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 78, state_mutation: 54, api: 22, bitwise_ops: 22
- `arch/um/kernel/skas/Makefile` (MAKEFILE) | Magnitude: 17.44 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 10, planned_debt: 5, args: 3, comprehensions: 3
- `rust/kernel/device.rs` (RUST) | Magnitude: 89.4 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 505, indent_spaces: 152, structural_boundaries: 37, generics: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `rust/kernel/static_assert.rs` (RUST) | Magnitude: 13.12 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 30, sec_high_risk_execution: 5, indent_spaces: 3, branch: 2
- `tools/testing/selftests/tc-testing/TdcPlugin.py` (PYTHON) | Magnitude: 0.06 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 36, doc: 18, structural_boundaries: 13, api: 11
- `rust/kernel/block.rs` (RUST) | Magnitude: 17.6 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, api: 5, encapsulation: 5, immutability_locks: 4
- `tools/perf/tests/shell/common/patterns.sh` (SHELL) | Magnitude: 0.05 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 59, safety_bypasses: 39, api: 33, doc: 27
- `tools/lib/python/kdoc/kdoc_re.py` (PYTHON) | Magnitude: 0.11 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 82, doc: 32, structural_boundaries: 31, state_mutation: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `drivers/cxl/core/Makefile` (MAKEFILE) | Magnitude: 24.42 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 9, structural_boundaries: 2, dead_code: 1
- `tools/bootconfig/scripts/xbc.sh` (SHELL) | Magnitude: 5.36 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 24, state_mutation: 20, branch: 17, safety_bypasses: 16
- `arch/arm/mach-imx/mach-imx7d.c` (C) | Magnitude: 30.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 33, structural_boundaries: 15, state_mutation: 9, import: 9
- `arch/arm64/kvm/hyp/exception.c` (C) | Magnitude: 314.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 153, indent_tabs: 149, branch: 59, bitwise_ops: 34
- `arch/mips/kernel/smp.c` (C) | Magnitude: 349.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 272, pointers: 103, structural_boundaries: 98, state_mutation: 88

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `drivers/gpu/drm/meson/Makefile` (MAKEFILE) | Magnitude: 16.64 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 3, structural_boundaries: 1, dead_code: 1
- `drivers/net/dsa/qca/Makefile` (MAKEFILE) | Magnitude: 19.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 6, branch: 2, dead_code: 1
- `drivers/gpu/drm/amd/display/dmub/src/dmub_dcn314.h` (C) | Magnitude: 15.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, ownership: 3, api: 2, macros: 2
- `scripts/Makefile.randstruct` (MAKEFILE) | Magnitude: 22.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 6, branch: 3, indent_tabs: 3, api: 1
- `include/linux/usb/otg.h` (C) | Magnitude: 50.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 29, indent_tabs: 23, pointers: 21, api: 20

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `sound/hda/codecs/realtek/alc269.c` -> Churn: **100.0%** | Cog Load: 82.565% | Debt: 12.8966%
- `kernel/sched/ext.c` -> Churn: **84.12%** | Cog Load: 78.9371% | Debt: 9.03%
- `sound/usb/quirks.c` -> Churn: **77.82%** | Cog Load: 87.6424% | Debt: 54.1776%
- `net/bluetooth/l2cap_core.c` -> Churn: **76.75%** | Cog Load: 95.2641% | Debt: 21.7227%
- `kernel/bpf/verifier.c` -> Churn: **75.4%** | Cog Load: 97.136% | Debt: 38.7229%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `virt/kvm/kvm_main.c` -> **Paolo Bonzini** (100.0% isolated ownership) | Magnitude: 57379.08
- `drivers/net/ethernet/intel/i40e/i40e_main.c` -> **Larysa Zaremba** (100.0% isolated ownership) | Magnitude: 15344.26
- `drivers/md/raid5.c` -> **Linus Torvalds** (100.0% isolated ownership) | Magnitude: 10501.36
- `drivers/net/wireless/ath/ath10k/mac.c` -> **Linus Torvalds** (100.0% isolated ownership) | Magnitude: 10113.28
- `drivers/scsi/lpfc/lpfc_sli.c` -> **Linus Torvalds** (100.0% isolated ownership) | Magnitude: 10021.5

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `drivers/gpu/drm/amd/amdgpu/amdgpu.h` -> **Severity: 0.002** (Bridge: 0.0001 * Flux: 32.2949%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tools/include/nolibc/stdlib.h` -> **Severity: 1037.656** (Blast Radius: 10.377 * Doc Risk: 99.9958%)
- `tools/include/nolibc/std.h` -> **Severity: 520.977** (Blast Radius: 5.21 * Doc Risk: 99.9956%)
- `tools/include/nolibc/getopt.h` -> **Severity: 167.114** (Blast Radius: 1.698 * Doc Risk: 98.418%)
- `drivers/gpu/drm/amd/amdgpu/amdgpu.h` -> **Severity: 105.6** (Blast Radius: 1.056 * Doc Risk: 100.0%)
- `drivers/gpu/drm/amd/display/dc/inc/core_types.h` -> **Severity: 92.7** (Blast Radius: 0.927 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
