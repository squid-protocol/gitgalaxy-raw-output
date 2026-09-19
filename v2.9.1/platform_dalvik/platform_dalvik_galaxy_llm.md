# ARCHITECTURAL_BRIEF: platform_dalvik
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/aosp-mirror/platform_dalvik.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1249 analyzed artifact(s), 73736 LOC.
- **Load-bearing artifact:** `dx/src/com/android/dx/util/Hex.java` -- 83 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `dx/src/com/android/dx/command/dexer/Main.java` -- pulls in 62 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `dx/src/com/android/dx/command/dexer/Main.java` at magnitude 1253.44 (structural weight, not risk).
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
| Total Artifacts | 1874 |
| Analyzed Artifacts (Scanned) | 1249 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 625 |
| Total LOC | 73736 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.6% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5625 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2775 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9414 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 37 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 747 | 71307 | 59.8% |
| PLAINTEXT | 341 | 0 | 27.3% |
| SHELL | 148 | 1652 | 11.8% |
| HTML | 9 | 78 | 0.7% |
| BATCH | 2 | 156 | 0.2% |
| MAKEFILE | 1 | 8 | 0.1% |
| C | 1 | 535 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `2.945`
> **Composition Archetype:** `Hub-Coupled App` (z +2.94; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 41%, Large Core Modules (3) 21%, State Mutators Files 7%, Interface Declarations Files 6%, Encapsulated Accessors Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 908 | 72.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 341 | 27.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 625*

**Composition by Extension & Reason:**
- `.class`: 289x Excluded (Explicitly Denied Extension: '.class')
- `.j`: 179x Excluded (Unsupported Extension: '.j')
- `no_extension`: 109x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.java`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Monolithic Amalgamation: 65503 LOC exceeds safe regex boundaries), 1x Excluded (Machine-Generated Source Code Signature: 1296 LOC)
- `.bp`: 4x Excluded (Unsupported Extension: '.bp'), 3x Unsupported Format (.bp)
- `.txt`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jar`: 4x Excluded (Explicitly Denied Extension: '.jar')
- `.rules`: 2x Excluded (Unsupported Extension: '.rules')
- `.list`: 2x Excluded (Unsupported Extension: '.list')
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.flags`: 1x Excluded (Unsupported Extension: '.flags')
- `.awk`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.4 | 12.3 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 48.3 | 60.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 22.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.1 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 23.1 | 7.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 35.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 10.4 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 17.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1093 | 318 | 2 | `dx/tests/141-invoke-polymorphic-varhandles/VarHandleDexTest.java` |
| cleanup | 43 | 21 | 0 | `CleanSpec.mk` |
| guards | 8418 | 621 | 15 | `dexgen/src/com/android/dexgen/dex/code/DalvOps.java` |
| danger | 4910 | 550 | 13 | `dx/src/com/android/dx/command/dexer/Main.java` |
| concurrency | 158 | 38 | 0 | `dx/src/com/android/dx/command/dexer/Main.java` |
| connectivity | 8775 | 741 | 14 | `dexgen/src/com/android/dexgen/dex/code/DalvOps.java` |
| io | 452 | 100 | 0 | `dx/etc/mainDexClasses` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 6 | 3 | 0 | `dx/tests/131-perf/run` |
| serialization | 0 | 0 | 0 | - |
| regex | 46 | 29 | 0 | `dx/tests/135-invoke-custom/run` |
| events | 31 | 11 | 0 | `dx/src/com/android/dx/ssa/SsaMethod.java` |
| tests | 254 | 23 | 0 | `dx/junit-tests/com/android/dex/EncodedValueReaderTest.java` |
| docs | 8673 | 634 | 17 | `dx/src/com/android/dx/rop/code/Rops.java` |
| debt | 480 | 151 | 1 | `dx/tests/135-invoke-custom/src/invokecustom/InvokeCustom.java` |
| mutation | 19003 | 643 | 40 | `dx/src/com/android/dx/command/dexer/Main.java` |
| dead_code | 1583 | 351 | 4 | `dx/src/com/android/dx/io/instructions/InstructionCodec.java` |
| credential | 0 | 0 | 0 | - |
| threat | 125 | 30 | 0 | `tools/hprof-conv/HprofConv.c` |
| ml_ai | 77 | 48 | 0 | `dx/etc/dx` |
| ui | 8 | 8 | 0 | `dx/src/com/android/dx/cf/attrib/package.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `dx/etc/mainDexClasses` (Hits: 27)
- `dx/src/com/android/dx/command/dexer/Main.java` (Hits: 20)
- `dx/src/com/android/dx/cf/direct/ClassPathOpener.java` (Hits: 14)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Hex.java** (`dx/src/com/android/dx/util/Hex.java`) — 83 inbound connections
2. **Type.java** (`dx/src/com/android/dx/rop/type/Type.java`) — 81 inbound connections
3. **AnnotatedOutput.java** (`dx/src/com/android/dx/util/AnnotatedOutput.java`) — 78 inbound connections
4. **AnnotatedOutput.java** (`dexgen/src/com/android/dexgen/util/AnnotatedOutput.java`) — 75 inbound connections
5. **Constant.java** (`dx/src/com/android/dx/rop/cst/Constant.java`) — 66 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Main.java** (`dx/src/com/android/dx/command/dexer/Main.java`) — 62 outbound dependencies
2. **CfTranslator.java** (`dx/src/com/android/dx/dex/cf/CfTranslator.java`) — 52 outbound dependencies
3. **StdAttributeFactory.java** (`dx/src/com/android/dx/cf/direct/StdAttributeFactory.java`) — 45 outbound dependencies
4. **IndexMap.java** (`dx/src/com/android/dx/merge/IndexMap.java`) — 36 outbound dependencies
5. **ConstantPoolParser.java** (`dx/src/com/android/dx/cf/cst/ConstantPoolParser.java`) — 35 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parseInstruction` **(Many-Argument Workhorses)** (@ `dx/src/com/android/dx/cf/code/BytecodeArray.java`) -> Impact: **748.9** | LOC: 602
  * *Intent:* * <li>Numeric conversion ops ({@code i2l}, etc.) are left alone * to avoid too much confustion, but their {@code type} is * the pushed type. E.g., {@c...
- `run` **(Compute Cores)** (@ `dx/src/com/android/dx/cf/code/ValueAwareMachine.java`) -> Impact: **394.4** | LOC: 168
  * *Intent:* /** {@inheritDoc} */
- `visitNoArgs` **(Many-Argument Workhorses)** (@ `dx/src/com/android/dx/cf/code/Simulator.java`) -> Impact: **336.8** | LOC: 297
  * *Intent:* /** {@inheritDoc} */
- `jopToRopOpcode` **(Compute Cores)** (@ `dx/src/com/android/dx/cf/code/RopperMachine.java`) -> Impact: **336.2** | LOC: 247
  * *Intent:* /** * Gets the register opcode for the given Java opcode. * * @param jop {@code jop >= 0;} the Java opcode * @param cst {@code null-ok;} the constant ...
- `ropFor` **(Many-Argument Workhorses)** (@ `dx/src/com/android/dx/rop/code/Rops.java`) -> Impact: **263.5** | LOC: 128
  * *Intent:* * shared instance. * * <p><b>Note:</b> This method does not do complete error checking on * its arguments, and so it may return an instance which seem...
- `ropFor` **(Many-Argument Workhorses)** (@ `dexgen/src/com/android/dexgen/rop/code/Rops.java`) -> Impact: **254.0** | LOC: 116
  * *Intent:* * shared instance. * * <p><b>Note:</b> This method does not do complete error checking on * its arguments, and so it may return an instance which seem...
- `opName` **(Compute Cores)** (@ `dx/src/com/android/dx/rop/code/RegOps.java`) -> Impact: **180.0** | LOC: 64
  * *Intent:* /** * Gets the name of the given opcode. * * @param opcode the opcode * @return {@code non-null;} its name */
- `opName` **(Compute Cores)** (@ `dexgen/src/com/android/dexgen/rop/code/RegOps.java`) -> Impact: **174.2** | LOC: 62
  * *Intent:* /** * Gets the name of the given opcode. * * @param opcode {@code >= 0, <= 255;} the opcode * @return {@code non-null;} its name */
- `dopFor` **(Compute Cores)** (@ `dx/src/com/android/dx/dex/code/RopToDop.java`) -> Impact: **166.7** | LOC: 137
  * *Intent:* /** * Returns the dalvik opcode appropriate for the given register-based * instruction. * * @param insn {@code non-null;} the original instruction * @...
- `dopFor` **(Compute Cores)** (@ `dexgen/src/com/android/dexgen/dex/code/RopToDop.java`) -> Impact: **153.6** | LOC: 130
  * *Intent:* /** * Returns the dalvik opcode appropriate for the given register-based * instruction. * * @param insn {@code non-null;} the original instruction * @...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `dx/src/com/android/dx/cf/code` | 27 | 6350.68 | 25.08% | 31.12% |
| `dx/src/com/android/dx/dex/file` | 55 | 4274.12 | 17.39% | 69.13% |
| `dexgen/src/com/android/dexgen/dex/file` | 50 | 4006.58 | 16.05% | 82.56% |
| `dx/src/com/android/dx/ssa` | 24 | 3698.7 | 27.22% | 36.0% |
| `dx/src/com/android/dx/rop/code` | 29 | 3621.26 | 16.07% | 5.19% |
| `dx/src/com/android/dx/dex/code` | 31 | 3439.82 | 20.96% | 42.6% |
| `dexgen/src/com/android/dexgen/dex/code` | 32 | 3363.32 | 19.87% | 41.19% |
| `dexgen/src/com/android/dexgen/rop/code` | 27 | 3292.48 | 15.67% | 20.52% |
| `dexgen/src/com/android/dexgen/util` | 29 | 1860.84 | 14.8% | 25.89% |
| `dx/src/com/android/dx/util` | 23 | 1685.18 | 15.12% | 4.35% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `dexgen/src/com/android/dexgen/util/Output.java` -> **100.0%** Exposure
- `dx/src/com/android/dx/cf/code/LocalsArray.java` -> **100.0%** Exposure
- `dx/src/com/android/dx/cf/code/Machine.java` -> **100.0%** Exposure
- `dx/src/com/android/dx/util/Output.java` -> **100.0%** Exposure
- `dexgen/src/com/android/dexgen/dex/file/Section.java` -> **99.9999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `dexgen/src/com/android/dexgen/dex/code/RopToDop.java` -> **100.0%** Exposure
- `dexgen/src/com/android/dexgen/rop/code/LocalVariableExtractor.java` -> **100.0%** Exposure
- `dexgen/src/com/android/dexgen/rop/code/RopMethod.java` -> **100.0%** Exposure
- `dexgen/src/com/android/dexgen/util/BitIntSet.java` -> **100.0%** Exposure
- `dexgen/src/com/android/dexgen/util/Bits.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `dx/src/com/android/dx/io/instructions/InstructionCodec.java` -> **38** Orphaned Functions | **16** Duplicates
- `dx/junit-tests/com/android/dx/util/BitsTest.java` -> **28** Orphaned Functions | **0** Duplicates
- `dexgen/src/com/android/dexgen/dex/file/ClassDefItem.java` -> **21** Orphaned Functions | **0** Duplicates
- `dexgen/src/com/android/dexgen/dex/file/DexFile.java` -> **21** Orphaned Functions | **0** Duplicates
- `dx/src/com/android/dx/cf/code/BaseMachine.java` -> **21** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3378` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `dx/src/com/android/dx/command/dexer/Main.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1253.44 | **LOC:** 1975 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **62**; blast radius 0.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (95.2%), Guard Balance (formerly Safety Score) (95.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 57.8431% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseFlags` **(Compute Cores)** (Impact: 116.5)
  * `dumpMethod` **(Many-Argument Workhorses)** (Impact: 52.4)
    * *Intent:* /** * Dumps any method with the given name in the given file. * * @param dex {@code non-null;} the d...
  * `processAllFiles` **(I/O & Config Routines)** (Impact: 32.5)
    * *Intent:* /** * Constructs the output {@link DexFile}, fill it in with all the * specified classes, and popula...
  * `processFileBytes` **(Stateful Encapsulated Methods)** (Impact: 22.2)
    * *Intent:* /** * Processes one file, which may be either a class or a resource. * * @param name {@code non-null...
  * `parse` **(Compute Cores)** (Impact: 19.7)
    * *Intent:* /** * Parses all command-line arguments and updates the state of the {@code Arguments} object * acco...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 149 instances
* *Concurrency (weighted view):* 95
* *State Mutation (weighted view):* 506
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 300`, `args: 64`, `func_start: 73`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 79`, `high_risk_execution: 1`, `state_mutation: 208`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 4`, `unreferenced_by_name: 3`
* *Architecture:* `io: 20`, `api: 64`, `concurrency: 30`, `import: 62`
* *Defense:* `safety: 46`, `doc: 91`, `sync_locks: 9`, `immutability_locks: 21`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` com.android.dex.Dex, com.android.dex.DexException, com.android.dex.DexFormat, com.android.dex.util.FileUtils, com.android.dx.Version, com.android.dx.cf.code.SimException, com.android.dx.cf.direct.ClassPathOpener, com.android.dx.cf.direct.ClassPathOpener.FileNameFilter...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dx/src/com/android/dx/cf/code/BytecodeArray.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1204.74 | **LOC:** 1440 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **15**; blast radius 0.692; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.9%), Connectivity (formerly Api Exposure) (55.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseInstruction` **(Many-Argument Workhorses)** (Impact: 748.9)
    * *Intent:* * <li>Numeric conversion ops ({@code i2l}, etc.) are left alone * to avoid too much confustion, but ...
  * `parseNewarray` **(Many-Argument Workhorses)** (Impact: 106.0)
    * *Intent:* /** * Helper to deal with {@code newarray}. * * @param offset the offset to the {@code newarray} opc...
  * `parseWide` **(Compute Cores)** (Impact: 52.0)
    * *Intent:* /** * Helper to deal with {@code wide}. * * @param offset the offset to the {@code wide} opcode itse...
  * `parseTableswitch` **(Stateful Encapsulated Methods)** (Impact: 8.7)
    * *Intent:* /** * Helper to deal with {@code tableswitch}. * * @param offset the offset to the {@code tableswitc...
  * `processWorkSet` **(Compute Cores)** (Impact: 7.7)
    * *Intent:* /** * Processes the given "work set" by repeatedly finding the lowest bit * in the set, clearing it,...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 508`, `structural_boundaries: 189`, `args: 42`, `func_start: 42`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 54`
* *Architecture:* `api: 39`, `import: 15`
* *Defense:* `safety: 8`, `doc: 48`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.692
  * `Choke Point (Betweenness):` 6.2e-05 | `Ripple Effect (Closeness):` 0.006259
  * `Imports (Out-Degree: 14):` com.android.dx.rop.cst.Constant, com.android.dx.rop.cst.ConstantPool, com.android.dx.rop.cst.CstDouble, com.android.dx.rop.cst.CstFloat, com.android.dx.rop.cst.CstInteger, com.android.dx.rop.cst.CstInvokeDynamic, com.android.dx.rop.cst.CstKnownNull, com.android.dx.rop.cst.CstLiteralBits...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/rop/code/Rops.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1179.16 | **LOC:** 2132 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **10**; blast radius 0.914; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.2%), Complexity Load (formerly Cognitive Load) (19.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ropFor` **(Many-Argument Workhorses)** (Impact: 263.5)
    * *Intent:* * shared instance. * * <p><b>Note:</b> This method does not do complete error checking on * its argu...
  * `opConv` **(Compute Cores)** (Impact: 81.7)
    * *Intent:* /** * Returns the appropriate {@code conv} rop for the given types. The * result is a shared instanc...
  * `pickBinaryOp` **(Many-Argument Workhorses)** (Impact: 80.7)
    * *Intent:* * Returns the appropriate binary arithmetic rop for the given type * and arguments. The result is a ...
  * `pickIf` **(Many-Argument Workhorses)** (Impact: 48.3)
    * *Intent:* /** * Helper for all the {@code if*}-related methods, which * checks types and picks one of the four...
  * `opNewArray` **(Compute Cores)** (Impact: 29.4)
    * *Intent:* /** * Returns the appropriate {@code new-array} rop for the given * type. The result is a shared ins...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 442`, `structural_boundaries: 492`, `args: 51`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 9`, `planned_debt: 1`
* *Architecture:* `api: 253`, `import: 10`
* *Defense:* `doc: 259`, `immutability_locks: 208`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.914
  * `Choke Point (Betweenness):` 8.1e-05 | `Ripple Effect (Closeness):` 0.01047
  * `Imports (Out-Degree: 10):` com.android.dx.rop.cst.Constant, com.android.dx.rop.cst.CstBaseMethodRef, com.android.dx.rop.cst.CstCallSiteRef, com.android.dx.rop.cst.CstMethodRef, com.android.dx.rop.cst.CstType, com.android.dx.rop.type.Prototype, com.android.dx.rop.type.StdTypeList, com.android.dx.rop.type.Type...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `dexgen/src/com/android/dexgen/rop/code/Rops.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1148.62 | **LOC:** 2087 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.539; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (80.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.6%), Complexity Load (formerly Cognitive Load) (19.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ropFor` **(Many-Argument Workhorses)** (Impact: 254.0)
    * *Intent:* * shared instance. * * <p><b>Note:</b> This method does not do complete error checking on * its argu...
  * `pickBinaryOp` **(Many-Argument Workhorses)** (Impact: 80.7)
    * *Intent:* * Returns the appropriate binary arithmetic rop for the given type * and arguments. The result is a ...
  * `opConv` **(Compute Cores)** (Impact: 67.6)
    * *Intent:* /** * Returns the appropriate {@code conv} rop for the given types. The * result is a shared instanc...
  * `pickIf` **(Many-Argument Workhorses)** (Impact: 48.3)
    * *Intent:* /** * Helper for all the {@code if*}-related methods, which * checks types and picks one of the four...
  * `opNewArray` **(Compute Cores)** (Impact: 29.4)
    * *Intent:* /** * Returns the appropriate {@code new-array} rop for the given * type. The result is a shared ins...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 430`, `structural_boundaries: 481`, `args: 49`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 9`, `planned_debt: 1`
* *Architecture:* `api: 252`, `import: 9`
* *Defense:* `doc: 257`, `immutability_locks: 208`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.539
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000801
  * `Imports (Out-Degree: 9):` com.android.dexgen.rop.cst.Constant, com.android.dexgen.rop.cst.CstBaseMethodRef, com.android.dexgen.rop.cst.CstMethodRef, com.android.dexgen.rop.cst.CstType, com.android.dexgen.rop.type.Prototype, com.android.dexgen.rop.type.StdTypeList, com.android.dexgen.rop.type.Type, com.android.dexgen.rop.type.TypeBearer...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/cf/code/RopperMachine.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 800.72 | **LOC:** 1033 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **31**; blast radius 0.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (53.8%)
- **Documentation Coverage:** 3.125% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `jopToRopOpcode` **(Compute Cores)** (Impact: 336.2)
    * *Intent:* /** * Gets the register opcode for the given Java opcode. * * @param jop {@code jop >= 0;} the Java ...
  * `run` **(Many-Argument Workhorses)** (Impact: 130.6)
    * *Intent:* /** {@inheritDoc} */
  * `getSources` **(Many-Argument Workhorses)** (Impact: 24.0)
    * *Intent:* /** * Helper for {@link #run}, which gets the list of sources for the. * instruction. * * @param opc...
  * `updateReturnOp` **(Stateful Encapsulated Methods)** (Impact: 15.1)
    * *Intent:* /** * Sets or updates the information about the return block. * * @param op {@code non-null;} the op...
  * `RopperMachine` **(Many-Argument Workhorses)** (Impact: 10.5)
    * *Intent:* /** * Constructs an instance. * * @param ropper {@code non-null;} ropper controlling this instance *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 241
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 152`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 109`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 10`
* *Architecture:* `api: 14`, `import: 31`
* *Defense:* `safety: 2`, `doc: 36`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` com.android.dx.cf.iface.Method, com.android.dx.cf.iface.MethodList, com.android.dx.rop.code.AccessFlags, com.android.dx.rop.code.FillArrayDataInsn, com.android.dx.rop.code.Insn, com.android.dx.rop.code.InvokePolymorphicInsn, com.android.dx.rop.code.PlainCstInsn, com.android.dx.rop.code.PlainInsn...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dx/src/com/android/dx/cf/code/Simulator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 795.36 | **LOC:** 956 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.8%), Complexity Load (formerly Cognitive Load) (41.5%)
- **Documentation Coverage:** 18.4211% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visitNoArgs` **(Many-Argument Workhorses)** (Impact: 336.8)
    * *Intent:* /** {@inheritDoc} */
  * `visitBranch` **(Compute Cores)** (Impact: 100.8)
    * *Intent:* /** {@inheritDoc} */
  * `visitConstant` **(Many-Argument Workhorses)** (Impact: 93.2)
    * *Intent:* /** {@inheritDoc} */
  * `visitLocal` **(Many-Argument Workhorses)** (Impact: 59.0)
    * *Intent:* /** {@inheritDoc} */
  * `checkInvokeInterfaceSupported` **(Many-Argument Workhorses)** (Impact: 20.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 278`, `structural_boundaries: 114`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 32`, `unreferenced_by_name: 7`
* *Architecture:* `api: 15`, `import: 16`
* *Defense:* `safety: 7`, `doc: 29`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` com.android.dex.DexFormat, com.android.dx.dex.DexOptions, com.android.dx.rop.code.LocalItem, com.android.dx.rop.cst.Constant, com.android.dx.rop.cst.CstFieldRef, com.android.dx.rop.cst.CstInteger, com.android.dx.rop.cst.CstInterfaceMethodRef, com.android.dx.rop.cst.CstInvokeDynamic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dx/src/com/android/dx/cf/code/Ropper.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 727.78 | **LOC:** 1802 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **32**; blast radius 0.578; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (47.4%)
- **Documentation Coverage:** 8.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processBlock` **(Many-Argument Workhorses)** (Impact: 81.8)
    * *Intent:* /** * Processes the given block. * * @param block {@code non-null;} block to process * @param frame ...
  * `mergeAndWorkAsNecessary` **(Many-Argument Workhorses)** (Impact: 21.2)
    * *Intent:* /** * Helper for {@link #processBlock}, which merges frames and * adds to the work set, as necessary...
  * `copyBlock` **(Many-Argument Workhorses)** (Impact: 19.0)
    * *Intent:* /** * Copies a basic block, mapping its successors along the way. * * @param origLabel original bloc...
  * `addSetupBlocks` **(I/O & Config Routines)** (Impact: 17.9)
    * *Intent:* /** * Constructs and adds the blocks that perform setup for the rest of * the method. This includes ...
  * `forEachNonSubBlockDepthFirst0` **(Stateful Encapsulated Methods)** (Impact: 11.5)
    * *Intent:* /** * Visits each block once in depth-first successor order, ignoring * {@code jsr} targets. Worker ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 363
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 181`, `args: 55`, `func_start: 56`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 161`
* *Architecture:* `api: 6`, `import: 32`
* *Defense:* `safety: 8`, `doc: 91`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.578
  * `Choke Point (Betweenness):` 4.9e-05 | `Ripple Effect (Closeness):` 0.003339
  * `Imports (Out-Degree: 27):` com.android.dx.cf.iface.MethodList, com.android.dx.dex.DexOptions, com.android.dx.rop.code.AccessFlags, com.android.dx.rop.code.BasicBlock, com.android.dx.rop.code.BasicBlockList, com.android.dx.rop.code.Insn, com.android.dx.rop.code.InsnList, com.android.dx.rop.code.PlainCstInsn...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/merge/DexMerger.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 727.78 | **LOC:** 1202 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 0.515; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.7%), Complexity Load (formerly Cognitive Load) (68.8%), Debt Markers (formerly Tech Debt) (8.0%)
- **Documentation Coverage:** 82.3529% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transformDebugInfoItem` **(Compute Cores)** (Impact: 50.3)
  * `readIntoMap` **(Stateful Encapsulated Methods)** (Impact: 13.9)
  * `readSortableTypes` **(Stateful Encapsulated Methods)** (Impact: 12.7)
    * *Intent:* /** * Reads just enough data on each class so that we can sort it and then find * it later. */
  * `transformCode` **(Stateful Encapsulated Methods)** (Impact: 12.1)
  * `transformMethods` **(Stateful Encapsulated Methods)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 300
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 172`, `args: 91`, `func_start: 91`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 162`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 12`, `import: 18`
* *Defense:* `doc: 20`, `test: 5`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.515
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.000801
  * `Imports (Out-Degree: 16):` com.android.dex.Annotation, com.android.dex.CallSiteId, com.android.dex.ClassData, com.android.dex.ClassDef, com.android.dex.Code, com.android.dex.Dex, com.android.dex.DexException, com.android.dex.DexIndexOverflowException...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/io/instructions/InstructionCodec.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 629.5 | **LOC:** 1113 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.2%), Mutation Surface (formerly State Flux) (51.6%)
- **Documentation Coverage:** 95.0413% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decodeRegisterList` **(Many-Argument Workhorses)** (Impact: 36.5)
    * *Intent:* /** * Helper method that decodes any of the register-list formats. */
  * `FORMAT_FILL_ARRAY_DATA_PAYLOAD` **(Compute Cores)** (Impact: 33.8)
  * `decode` **(Compute Cores)** (Impact: 33.7)
  * `encode` **(Compute Cores)** (Impact: 23.6)
  * `decode` **(Compute Cores)** (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 218`, `args: 132`, `func_start: 132`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 19`, `planned_debt: 1`, `duplicate_logic: 16`, `unreferenced_by_name: 38`
* *Architecture:* `api: 75`, `import: 7`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` com.android.dex.DexException, com.android.dx.io.IndexType, com.android.dx.io.OpcodeInfo, com.android.dx.io.Opcodes, com.android.dx.util.Hex, java.io.EOFException, java.util.Arrays
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dx/src/com/android/dx/ssa/back/FirstFitLocalCombiningAllocator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 609.52 | **LOC:** 1260 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (37.9%)
- **Documentation Coverage:** 5.3571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findAnyFittingRange` **(Many-Argument Workhorses)** (Impact: 40.6)
    * *Intent:* /** * Finds an unreserved range that will fit the sources of the * specified instruction. Does not b...
  * `fitPlanForRange` **(Many-Argument Workhorses)** (Impact: 27.4)
    * *Intent:* /** * Attempts to build a plan for fitting a range of sources into rop * registers. * * @param ropRe...
  * `findRangeAndAdjust` **(Compute Cores)** (Impact: 20.1)
    * *Intent:* /** * Find a contiguous rop register range that fits the specified * instruction's sources. First, t...
  * `processInsn` **(Stateful Encapsulated Methods)** (Impact: 14.3)
    * *Intent:* /** * This method collects three types of instructions: * * 1) Adds a local variable assignment to t...
  * `processPhiInsn` **(Stateful Encapsulated Methods)** (Impact: 14.0)
    * *Intent:* /** * Attempts to map the sources and result of a phi to a common register. * Will try existing mapp...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 117`, `args: 47`, `func_start: 46`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 96`, `unreferenced_by_name: 6`
* *Architecture:* `api: 11`, `import: 22`
* *Defense:* `safety: 2`, `doc: 57`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` com.android.dx.dex.DexOptions, com.android.dx.rop.code.CstInsn, com.android.dx.rop.code.LocalItem, com.android.dx.rop.code.RegOps, com.android.dx.rop.code.RegisterSpec, com.android.dx.rop.code.RegisterSpecList, com.android.dx.rop.code.Rop, com.android.dx.rop.cst.CstInteger...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dx/src/com/android/dx/ssa/SCCP.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 581.56 | **LOC:** 681 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (47.0%)
- **Documentation Coverage:** 12.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `simulateMath` **(Many-Argument Workhorses)** (Impact: 84.6)
    * *Intent:* /** * Simulates math insns, if possible. * * @param insn non-null insn to simulate * @param resultTy...
  * `simulateBranch` **(Compute Cores)** (Impact: 80.8)
    * *Intent:* /** * Simulates branch insns, if possible. Adds reachable successor blocks * to the CFG worklists. *...
  * `simulateStmt` **(Compute Cores)** (Impact: 60.1)
    * *Intent:* /** * Simulates a statement and set the result lattice value. * @param insn instruction to simulate ...
  * `simulatePhi` **(Stateful Encapsulated Methods)** (Impact: 16.0)
    * *Intent:* /** * Simulates a PHI node and set the lattice for the result * to the appropriate value. * Meet val...
  * `run` **(I/O & Config Routines)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 233
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 94`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 83`, `planned_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 15`
* *Defense:* `safety: 5`, `doc: 24`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` com.android.dx.rop.code.CstInsn, com.android.dx.rop.code.Insn, com.android.dx.rop.code.PlainInsn, com.android.dx.rop.code.RegOps, com.android.dx.rop.code.RegisterSpec, com.android.dx.rop.code.RegisterSpecList, com.android.dx.rop.code.Rop, com.android.dx.rop.code.Rops...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dx/src/com/android/dx/ssa/EscapeAnalysis.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 551.9 | **LOC:** 847 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (50.8%)
- **Documentation Coverage:** 29.4118% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processUse` **(Many-Argument Workhorses)** (Impact: 102.4)
    * *Intent:* /** * Handles non-phi uses of new objects. Checks to see how instruction is * used and updates the e...
  * `replaceUse` **(Many-Argument Workhorses)** (Impact: 46.3)
    * *Intent:* /** * Replaces the use for a scalar replaceable array. Gets and puts become * move instructions, and...
  * `processMoveResultPseudoInsn` **(Compute Cores)** (Impact: 38.6)
    * *Intent:* /** * Determine the origin of a move result pseudo instruction that generates * an object. Creates a...
  * `insertPlainInsnBefore` **(Stateful Encapsulated Methods)** (Impact: 13.6)
    * *Intent:* /** * Inserts a new PlainInsn before the given instruction. * TODO: move this somewhere more appropr...
  * `processRegister` **(Stateful Encapsulated Methods)** (Impact: 11.6)
    * *Intent:* /** * Iterate through all the uses of a new object. * * @param result {@code non-null;} register whe...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 215
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 110`, `args: 27`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 81`, `planned_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 9`, `import: 27`
* *Defense:* `doc: 32`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` com.android.dx.rop.code.Exceptions, com.android.dx.rop.code.FillArrayDataInsn, com.android.dx.rop.code.Insn, com.android.dx.rop.code.PlainCstInsn, com.android.dx.rop.code.PlainInsn, com.android.dx.rop.code.RegOps, com.android.dx.rop.code.RegisterSpec, com.android.dx.rop.code.RegisterSpecList...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dx/src/com/android/dx/cf/direct/StdAttributeFactory.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 498.16 | **LOC:** 862 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **45**; blast radius 1.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.0%), Guard Balance (formerly Safety Score) (86.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (17.3%)
- **Documentation Coverage:** 3.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse0` **(Many-Argument Workhorses)** (Impact: 109.1)
    * *Intent:* /** {@inheritDoc} */
  * `code` **(Many-Argument Workhorses)** (Impact: 49.7)
    * *Intent:* /** * Parses a {@code Code} attribute. */
  * `parseBootstrapMethods` **(Many-Argument Workhorses)** (Impact: 30.5)
  * `innerClasses` **(Many-Argument Workhorses)** (Impact: 27.2)
    * *Intent:* /** * Parses an {@code InnerClasses} attribute. */
  * `lineNumberTable` **(Many-Argument Workhorses)** (Impact: 17.5)
    * *Intent:* /** * Parses a {@code LineNumberTable} attribute. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 157`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 37`
* *Architecture:* `api: 4`, `import: 45`
* *Defense:* `safety: 2`, `doc: 27`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.18
  * `Choke Point (Betweenness):` 0.000293 | `Ripple Effect (Closeness):` 0.005723
  * `Imports (Out-Degree: 44):` com.android.dx.cf.attrib.AttAnnotationDefault, com.android.dx.cf.attrib.AttBootstrapMethods, com.android.dx.cf.attrib.AttCode, com.android.dx.cf.attrib.AttConstantValue, com.android.dx.cf.attrib.AttDeprecated, com.android.dx.cf.attrib.AttEnclosingMethod, com.android.dx.cf.attrib.AttExceptions, com.android.dx.cf.attrib.AttInnerClasses...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/dex/code/OutputFinisher.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 423.28 | **LOC:** 947 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (38.1%)
- **Documentation Coverage:** 20.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `align64bits` **(Compute Cores)** (Impact: 31.1)
  * `performExpansion` **(Stateful Encapsulated Methods)** (Impact: 20.1)
    * *Intent:* /** * Helper for {@link #massageInstructions}, which constructs a * replacement list, where each {li...
  * `addConstants` **(Stateful Encapsulated Methods)** (Impact: 18.4)
    * *Intent:* /** * Helper for {@link #getAllConstants} which adds all the info for * a single instruction. * * @p...
  * `reserveRegisters` **(Stateful Encapsulated Methods)** (Impact: 12.1)
    * *Intent:* /** * Helper for {@link #finishProcessingAndGetList}, which figures * out how many reserved register...
  * `addConstants` **(Stateful Encapsulated Methods)** (Impact: 11.7)
    * *Intent:* /** * Helper for {@link #getAllConstants} which adds all the info for * a single {@code RegisterSpec...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 176
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 77`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 74`, `planned_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 12`, `import: 17`
* *Defense:* `safety: 22`, `doc: 35`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` com.android.dex.DexException, com.android.dx.dex.DexOptions, com.android.dx.io.Opcodes, com.android.dx.rop.code.LocalItem, com.android.dx.rop.code.RegisterSpec, com.android.dx.rop.code.RegisterSpecList, com.android.dx.rop.code.RegisterSpecSet, com.android.dx.rop.code.SourcePosition...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dx/src/com/android/dx/ssa/SsaMethod.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 418.68 | **LOC:** 858 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **17**; blast radius 0.913; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (52.8%)
- **Documentation Coverage:** 8.046% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `forEachBlockDepthFirst` **(Compute Cores)** (Impact: 17.3)
    * *Intent:* /** * Walks the basic block tree in depth-first order, calling the visitor * method once for every b...
  * `deleteInsns` **(Compute Cores)** (Impact: 16.2)
    * *Intent:* /** * Deletes all insns in the set from this method. * * @param deletedInsns {@code non-null;} insns...
  * `updateOneDefinition` **(Compute Cores)** (Impact: 11.4)
    * *Intent:* /** * Updates a single definition. * * @param insn {@code non-null;} insn who's result should be rec...
  * `isRegALocal` **(Compute Cores)** (Impact: 9.6)
    * *Intent:* /** * Checks to see if the given SSA reg is ever associated with a local * local variable. Each SSA ...
  * `onSourceChanged` **(Compute Cores)** (Impact: 8.8)
    * *Intent:* /** * Updates the use list for a single change in source register. * * @param insn {@code non-null;}...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 106`, `args: 48`, `func_start: 50`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 77`, `planned_debt: 1`
* *Architecture:* `api: 40`, `import: 17`
* *Defense:* `doc: 58`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 5.4e-05 | `Ripple Effect (Closeness):` 0.005298
  * `Imports (Out-Degree: 11):` com.android.dx.rop.code.BasicBlockList, com.android.dx.rop.code.Insn, com.android.dx.rop.code.PlainInsn, com.android.dx.rop.code.RegOps, com.android.dx.rop.code.RegisterSpec, com.android.dx.rop.code.RegisterSpecList, com.android.dx.rop.code.Rop, com.android.dx.rop.code.RopMethod...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/cf/code/ValueAwareMachine.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 405.54 | **LOC:** 211 | **CtrlFlow:** 108.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.1%), Complexity Load (formerly Cognitive Load) (27.1%), Mutation Surface (formerly State Flux) (15.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Compute Cores)** (Impact: 394.4)
    * *Intent:* /** {@inheritDoc} */
  * `ValueAwareMachine` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /** * Constructs an instance. * * @param prototype {@code non-null;} the prototype for the associate...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 25`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` com.android.dx.rop.cst.CstCallSiteRef, com.android.dx.rop.cst.CstType, com.android.dx.rop.type.Prototype, com.android.dx.rop.type.Type, com.android.dx.rop.type.TypeBearer, com.android.dx.util.Hex
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dx/src/com/android/dx/ssa/SsaBasicBlock.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 382.88 | **LOC:** 1012 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **19**; blast radius 0.718; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (53.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scheduleMovesFromPhis` **(I/O & Config Routines)** (Impact: 17.0)
    * *Intent:* /** * Sorts move instructions added via {@code addMoveToEnd} during * phi removal so that results do...
  * `scheduleUseBeforeAssigned` **(Compute Cores)** (Impact: 16.1)
    * *Intent:* /** * Ensures that all move operations in this block occur such that * reads of any register happen ...
  * `addMoveToEnd` **(Many-Argument Workhorses)** (Impact: 13.2)
    * *Intent:* /** * Adds a move instruction to the end of this basic block, just * before the last instruction. If...
  * `newFromRop` **(Many-Argument Workhorses)** (Impact: 11.7)
    * *Intent:* /** * Creates a new SSA basic block from a ROP form basic block. * * @param rmeth original method * ...
  * `replaceSuccessor` **(Compute Cores)** (Impact: 10.0)
    * *Intent:* /** * Replaces an old successor with a new successor. This will throw * RuntimeException if {@code o...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 106`, `args: 44`, `func_start: 44`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 71`, `planned_debt: 3`
* *Architecture:* `api: 44`, `import: 19`
* *Defense:* `safety: 2`, `doc: 61`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.718
  * `Choke Point (Betweenness):` 3.7e-05 | `Ripple Effect (Closeness):` 0.004364
  * `Imports (Out-Degree: 14):` com.android.dx.rop.code.BasicBlock, com.android.dx.rop.code.BasicBlockList, com.android.dx.rop.code.Insn, com.android.dx.rop.code.InsnList, com.android.dx.rop.code.PlainInsn, com.android.dx.rop.code.RegisterSpec, com.android.dx.rop.code.RegisterSpecList, com.android.dx.rop.code.Rop...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dex/Dex.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 369.24 | **LOC:** 820 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **27**; blast radius 2.356; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.3%), Guard Balance (formerly Safety Score) (60.3%)
- **Documentation Coverage:** 84.0237% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Dex` **(Defensive Guards)** (Impact: 12.3)
    * *Intent:* /** * Creates a new dex buffer from the dex file {@code file}. */
  * `readCatchHandler` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `findCatchHandlerIndex` **(Stateful Encapsulated Methods)** (Impact: 5.6)
  * `readCode` **(I/O & Config Routines)** (Impact: 5.5)
  * `checkBounds` **(Encapsulated Accessors)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 223`, `args: 91`, `func_start: 91`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 33`, `duplicate_logic: 2`
* *Architecture:* `io: 11`, `api: 80`, `import: 27`
* *Defense:* `safety: 16`, `doc: 15`, `test: 1`, `immutability_locks: 26`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.356
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.010417
  * `Imports (Out-Degree: 3):` com.android.dex.Code.CatchHandler, com.android.dex.Code.Try, com.android.dex.MethodHandle.MethodHandleType, com.android.dex.util.ByteInput, com.android.dex.util.ByteOutput, com.android.dex.util.FileUtils, java.io.ByteArrayOutputStream, java.io.File...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `dexgen/src/com/android/dexgen/dex/code/LocalList.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 358.08 | **LOC:** 949 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 0.648; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (90.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (43.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `startLocal` **(Many-Argument Workhorses)** (Impact: 29.9)
    * *Intent:* /** * Starts a local at the given address. * * @param address {@code >= 0;} the address * @param sta...
  * `debugVerify0` **(Compute Cores)** (Impact: 22.8)
    * *Intent:* /** * Helper for {@link #debugVerify} which does most of the work. */
  * `checkForEmptyRange` **(Many-Argument Workhorses)** (Impact: 20.6)
    * *Intent:* * Helper for {@link #endLocal}, which handles the cases where * and end local is issued at the same ...
  * `snapshot` **(Compute Cores)** (Impact: 18.7)
    * *Intent:* /** * Sets the local state at the given address to the given snapshot. * The first call on this inst...
  * `make` **(Defensive Guards)** (Impact: 13.6)
    * *Intent:* /** * Constructs an instance for the given method, based on the given * block order and intermediate...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 86`, `args: 33`, `func_start: 33`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 46`, `planned_debt: 2`
* *Architecture:* `api: 31`, `import: 9`
* *Defense:* `safety: 8`, `doc: 54`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.648
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.003205
  * `Imports (Out-Degree: 6):` com.android.dexgen.rop.code.RegisterSpec, com.android.dexgen.rop.code.RegisterSpecSet, com.android.dexgen.rop.cst.CstType, com.android.dexgen.rop.cst.CstUtf8, com.android.dexgen.rop.type.Type, com.android.dexgen.util.FixedSizeList, java.io.PrintStream, java.util.ArrayList...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `dexgen/src/com/android/dexgen/rop/type/Type.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 357.78 | **LOC:** 928 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **51** in-repo importer(s); it depends on **2**; blast radius 16.634; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (75.2%), Mutation Surface (formerly State Flux) (50.2%), Complexity Load (formerly Cognitive Load) (31.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `intern` **(Compute Cores)** (Impact: 30.5)
    * *Intent:* /** * Returns the unique instance corresponding to the type with the * given descriptor. See vmspec-...
  * `toHuman` **(Compute Cores)** (Impact: 26.1)
    * *Intent:* /** {@inheritDoc} */
  * `isPrimitive` **(Compute Cores)** (Impact: 20.9)
    * *Intent:* /** * Gets whether this type is a primitive type. All types are either * primitive or reference type...
  * `getFrameType` **(Compute Cores)** (Impact: 12.7)
    * *Intent:* /** {@inheritDoc} */
  * `getBasicFrameType` **(Compute Cores)** (Impact: 12.7)
    * *Intent:* /** {@inheritDoc} */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 111`, `args: 35`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 27`
* *Architecture:* `api: 82`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 6`, `doc: 93`, `sync_locks: 1`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.634
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.060192
  * `Imports (Out-Degree: 1):` com.android.dexgen.util.Hex, java.util.HashMap
  * `Imported By (In-Degree: 51):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/dex/code/LocalList.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 355.08 | **LOC:** 948 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 0.627; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (90.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (41.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `startLocal` **(Many-Argument Workhorses)** (Impact: 29.9)
    * *Intent:* /** * Starts a local at the given address. * * @param address {@code >= 0;} the address * @param sta...
  * `debugVerify0` **(Compute Cores)** (Impact: 22.8)
    * *Intent:* /** * Helper for {@link #debugVerify} which does most of the work. */
  * `checkForEmptyRange` **(Many-Argument Workhorses)** (Impact: 20.6)
    * *Intent:* * Helper for {@link #endLocal}, which handles the cases where * and end local is issued at the same ...
  * `snapshot` **(Compute Cores)** (Impact: 18.7)
    * *Intent:* /** * Sets the local state at the given address to the given snapshot. * The first call on this inst...
  * `compareTo` **(Compute Cores)** (Impact: 10.7)
    * *Intent:* /** * Compares by (in priority order) address, end then start * disposition (variants of end are all...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 86`, `args: 33`, `func_start: 33`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 46`, `planned_debt: 2`
* *Architecture:* `api: 31`, `import: 9`
* *Defense:* `safety: 7`, `doc: 54`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.627
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.002404
  * `Imports (Out-Degree: 6):` com.android.dx.rop.code.RegisterSpec, com.android.dx.rop.code.RegisterSpecSet, com.android.dx.rop.cst.CstString, com.android.dx.rop.cst.CstType, com.android.dx.rop.type.Type, com.android.dx.util.FixedSizeList, java.io.PrintStream, java.util.ArrayList...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `dexgen/src/com/android/dexgen/dex/file/DebugInfoDecoder.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 353.66 | **LOC:** 654 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (49.4%)
- **Documentation Coverage:** 17.3913% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateEncode0` **(Many-Argument Workhorses)** (Impact: 82.3)
  * `decode0` **(I/O & Config Routines)** (Impact: 42.6)
  * `validateEncode` **(Many-Argument Workhorses)** (Impact: 10.8)
    * *Intent:* /** * Validates an encoded debug info stream against data used to encode it, * throwing an exception...
  * `readSignedLeb128` **(Compute Cores)** (Impact: 8.3)
    * *Intent:* /** * Reads a DWARFv3-style signed LEB128 integer to the specified stream. * See DWARF v3 section 7....
  * `DebugInfoDecoder` **(Many-Argument Workhorses)** (Impact: 6.8)
    * *Intent:* /** * Constructs an instance. * * @param encoded encoded debug info * @param codesize size of code b...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 83`, `args: 14`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 67`, `planned_debt: 4`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 18`, `import: 15`
* *Defense:* `safety: 10`, `doc: 32`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` com.android.dexgen.dex.code.DalvCode, com.android.dexgen.dex.code.DalvInsnList, com.android.dexgen.dex.code.LocalList, com.android.dexgen.dex.code.PositionList, com.android.dexgen.dex.file.DebugInfoConstants.*, com.android.dexgen.rop.cst.CstMethodRef, com.android.dexgen.rop.cst.CstUtf8, com.android.dexgen.rop.type.Prototype...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dx/src/com/android/dx/dex/file/DebugInfoEncoder.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 349.26 | **LOC:** 933 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **30**; blast radius 0.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (94.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (22.5%)
- **Documentation Coverage:** 25.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emitHeader` **(Many-Argument Workhorses)** (Impact: 47.1)
    * *Intent:* /** * Emits the header sequence, which consists of LEB128-encoded initial * line number and string i...
  * `emitLocalsAtAddress` **(Compute Cores)** (Impact: 15.8)
    * *Intent:* /** * Emits all local variable activity that occurs at the current * {@link #address} starting at th...
  * `convert0` **(I/O & Config Routines)** (Impact: 13.7)
  * `emitPosition` **(Stateful Encapsulated Methods)** (Impact: 12.2)
    * *Intent:* /** * Emits the necessary byte sequences to emit the given position table * entry. This will typical...
  * `annotate` **(Stateful Encapsulated Methods)** (Impact: 11.0)
    * *Intent:* /** * Annotates or writes a message to the {@code debugPrint} writer * if applicable. * * @param len...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 94`, `args: 29`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 47`, `planned_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 8`, `import: 30`
* *Defense:* `safety: 2`, `doc: 33`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` com.android.dex.util.ExceptionWithContext, com.android.dx.dex.code.LocalList, com.android.dx.dex.code.PositionList, com.android.dx.dex.file.DebugInfoConstants.DBG_ADVANCE_LINE, com.android.dx.dex.file.DebugInfoConstants.DBG_ADVANCE_PC, com.android.dx.dex.file.DebugInfoConstants.DBG_END_LOCAL, com.android.dx.dex.file.DebugInfoConstants.DBG_END_SEQUENCE, com.android.dx.dex.file.DebugInfoConstants.DBG_FIRST_SPECIAL...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dexgen/src/com/android/dexgen/dex/file/DebugInfoEncoder.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 348.68 | **LOC:** 921 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (94.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (23.6%)
- **Documentation Coverage:** 25.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emitHeader` **(Many-Argument Workhorses)** (Impact: 47.1)
    * *Intent:* /** * Emits the header sequence, which consists of LEB128-encoded initial * line number and string i...
  * `emitLocalsAtAddress` **(Compute Cores)** (Impact: 15.8)
    * *Intent:* /** * Emits all local variable activity that occurs at the current * {@link #address} starting at th...
  * `convert0` **(I/O & Config Routines)** (Impact: 13.7)
  * `emitPosition` **(Stateful Encapsulated Methods)** (Impact: 12.2)
    * *Intent:* /** * Emits the necessary byte sequences to emit the given position table * entry. This will typical...
  * `annotate` **(Stateful Encapsulated Methods)** (Impact: 11.0)
    * *Intent:* /** * Annotates or writes a message to the {@code debugPrint} writer * if applicable. * * @param len...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 84`, `args: 29`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 47`, `planned_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 8`, `import: 19`
* *Defense:* `safety: 2`, `doc: 33`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` com.android.dexgen.dex.code.LocalList, com.android.dexgen.dex.code.PositionList, com.android.dexgen.dex.file.DebugInfoConstants.*, com.android.dexgen.rop.code.RegisterSpec, com.android.dexgen.rop.code.SourcePosition, com.android.dexgen.rop.cst.CstMethodRef, com.android.dexgen.rop.cst.CstType, com.android.dexgen.rop.cst.CstUtf8...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dexgen/src/com/android/dexgen/util/ByteArrayAnnotatedOutput.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 346.48 | **LOC:** 640 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **3**; blast radius 0.771; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.3%), Connectivity (formerly Api Exposure) (53.0%), Complexity Load (formerly Cognitive Load) (35.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `enableAnnotations` **(Compute Cores)** (Impact: 11.4)
    * *Intent:* /** * Indicates that this instance should keep annotations. This method may * be called only once pe...
  * `annotate` **(Compute Cores)** (Impact: 11.3)
    * *Intent:* /** {@inheritDoc} */
  * `write` **(Compute Cores)** (Impact: 11.1)
    * *Intent:* /** {@inheritDoc} */
  * `writeAnnotationsTo` **(Compute Cores)** (Impact: 10.9)
    * *Intent:* /** * Writes the annotated content of this instance to the given writer. * * @param out {@code non-n...
  * `writeSignedLeb128` **(Compute Cores)** (Impact: 9.4)
    * *Intent:* /** {@inheritDoc} */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 67`, `args: 36`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 66`
* *Architecture:* `io: 4`, `api: 34`, `import: 3`
* *Defense:* `doc: 49`, `test: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.771
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004808
  * `Imports (Out-Degree: 0):` java.io.IOException, java.io.Writer, java.util.ArrayList
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `dx/src/com/android/dx/cf/direct/StdAttributeFactory.java` -> **Severity: 0.029** (Bridge: 0.0003 * Flux: 97.9645%)
- `dx/src/com/android/dx/cf/direct/DirectClassFile.java` -> **Severity: 0.018** (Bridge: 0.0002 * Flux: 99.1912%)
- `dx/src/com/android/dx/ssa/Optimizer.java` -> **Severity: 0.017** (Bridge: 0.0002 * Flux: 99.9844%)
- `dx/src/com/android/dx/ssa/back/SsaToRop.java` -> **Severity: 0.013** (Bridge: 0.0001 * Flux: 99.8081%)
- `dx/src/com/android/dx/dex/cf/OptimizerOptions.java` -> **Severity: 0.012** (Bridge: 0.0001 * Flux: 99.0048%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `dx/src/com/android/dx/util/Hex.java` -> **Severity: 10.837** (Embedded: 0.1097 * Error Risk: 98.7436%)
- `dx/src/com/android/dx/rop/type/Type.java` -> **Severity: 7.254** (Embedded: 0.104 * Error Risk: 69.7339%)
- `dexgen/src/com/android/dexgen/util/Hex.java` -> **Severity: 6.905** (Embedded: 0.0699 * Error Risk: 98.7436%)
- `dx/src/com/android/dx/rop/cst/CstString.java` -> **Severity: 6.142** (Embedded: 0.0664 * Error Risk: 92.5187%)
- `dx/src/com/android/dx/util/FixedSizeList.java` -> **Severity: 4.813** (Embedded: 0.0601 * Error Risk: 80.0911%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `dx/src/com/android/dex/MethodHandle.java` -> **Severity: 350.0** (Blast Radius: 3.5 * Doc Risk: 100.0%)
- `dx/src/com/android/dex/util/Unsigned.java` -> **Severity: 246.72** (Blast Radius: 6.168 * Doc Risk: 40.0%)
- `dx/src/com/android/dex/Dex.java` -> **Severity: 197.96** (Blast Radius: 2.356 * Doc Risk: 84.0237%)
- `dx/src/com/android/dex/util/ByteArrayByteInput.java` -> **Severity: 153.7** (Blast Radius: 1.537 * Doc Risk: 100.0%)
- `dx/src/com/android/dx/util/MutabilityException.java` -> **Severity: 146.867** (Blast Radius: 2.203 * Doc Risk: 66.6667%)

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
