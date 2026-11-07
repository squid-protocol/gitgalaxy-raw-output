# ARCHITECTURAL_BRIEF: platform_dalvik
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/aosp-mirror/platform_dalvik.git` |
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
- **Scope:** 1264 analyzed artifact(s), 207762 LOC.
- **Load-bearing artifact:** `dx/src/com/android/dx/util/Hex.java` -- 86 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `dx/src/com/android/dx/command/dexer/Main.java` -- pulls in 62 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `dx/tests/128-multidex-option-overflow/src/FillerField.java` at magnitude 66826.04 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 1264 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 610 |
| Total LOC | 207762 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 67.4% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5893 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2214 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 8.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.4838 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 31 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 754 | 205105 | 59.7% |
| PLAINTEXT | 345 | 0 | 27.3% |
| SHELL | 152 | 1880 | 12.0% |
| HTML | 9 | 78 | 0.7% |
| BATCH | 2 | 156 | 0.2% |
| MAKEFILE | 1 | 8 | 0.1% |
| C | 1 | 535 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 1264 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 41%, Large Core Modules (3) 20%, State Mutators Files 6%, Encapsulated Accessors Files 6%, Interface Declarations Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 919 | 72.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 345 | 27.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 610*

**Composition by Extension & Reason:**
- `.class`: 289x Excluded (Explicitly Denied Extension: '.class')
- `.j`: 179x Excluded (Unsupported Extension: '.j')
- `no_extension`: 105x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bp`: 4x Excluded (Unsupported Extension: '.bp'), 3x Unsupported Format (.bp)
- `.css`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jar`: 4x Excluded (Explicitly Denied Extension: '.jar')
- `.java`: 1x Excluded (Saturation: Line 4 exceeds 500 chars), 1x Unrecognized Syntax (Dense Structure / Global Regex Timeout), 1x Excluded (Machine-Generated Source Code Signature: 186 LOC)
- `.rules`: 2x Excluded (Unsupported Extension: '.rules')
- `.list`: 2x Excluded (Unsupported Extension: '.list')
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.flags`: 1x Excluded (Unsupported Extension: '.flags')
- `.awk`: 1x Excluded (Unsupported Extension: '.awk')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.2 | 11.2 | 4.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.7 | 40.7 | 53.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 22.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 12.2 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 23.0 | 7.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 35.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 17.6 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 17.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1047 | 316 | 2 | `dx/tests/141-invoke-polymorphic-varhandles/VarHandleDexTest.java` |
| cleanup | 45 | 22 | 0 | `CleanSpec.mk` |
| guards | 8663 | 623 | 15 | `dexgen/src/com/android/dexgen/dex/code/DalvOps.java` |
| danger | 4952 | 556 | 13 | `dx/src/com/android/dx/command/dexer/Main.java` |
| concurrency | 159 | 39 | 0 | `dx/src/com/android/dx/command/dexer/Main.java` |
| connectivity | 140059 | 749 | 14 | `dx/tests/128-multidex-option-overflow/src/FillerField.java` |
| io | 518 | 105 | 0 | `dx/tests/run-test` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 6 | 3 | 0 | `dx/tests/131-perf/run` |
| serialization | 0 | 0 | 0 | - |
| regex | 52 | 31 | 0 | `dx/tests/135-invoke-custom/run` |
| events | 31 | 11 | 0 | `dx/src/com/android/dx/ssa/SsaMethod.java` |
| tests | 254 | 23 | 0 | `dx/junit-tests/com/android/dex/EncodedValueReaderTest.java` |
| docs | 8683 | 635 | 17 | `dx/src/com/android/dx/rop/code/Rops.java` |
| debt | 518 | 155 | 1 | `dx/tests/135-invoke-custom/src/invokecustom/InvokeCustom.java` |
| mutation | 19366 | 647 | 40 | `dx/src/com/android/dx/command/dexer/Main.java` |
| dead_code | 1566 | 355 | 4 | `dx/junit-tests/com/android/dx/util/BitsTest.java` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 86 | 51 | 0 | `dx/etc/dx` |
| ui | 8 | 8 | 0 | `dx/src/com/android/dx/cf/attrib/package.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `dx/tests/run-test` (Hits: 31)
- `dx/etc/mainDexClasses` (Hits: 27)
- `dx/src/com/android/dx/command/dexer/Main.java` (Hits: 23)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Hex.java** (`dx/src/com/android/dx/util/Hex.java`) — 86 inbound connections
2. **Type.java** (`dx/src/com/android/dx/rop/type/Type.java`) — 85 inbound connections
3. **AnnotatedOutput.java** (`dx/src/com/android/dx/util/AnnotatedOutput.java`) — 78 inbound connections
4. **AnnotatedOutput.java** (`dexgen/src/com/android/dexgen/util/AnnotatedOutput.java`) — 75 inbound connections
5. **Constant.java** (`dx/src/com/android/dx/rop/cst/Constant.java`) — 69 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Main.java** (`dx/src/com/android/dx/command/dexer/Main.java`) — 62 outbound dependencies
2. **CfTranslator.java** (`dx/src/com/android/dx/dex/cf/CfTranslator.java`) — 52 outbound dependencies
3. **StdAttributeFactory.java** (`dx/src/com/android/dx/cf/direct/StdAttributeFactory.java`) — 45 outbound dependencies
4. **IndexMap.java** (`dx/src/com/android/dx/merge/IndexMap.java`) — 36 outbound dependencies
5. **ConstantPoolParser.java** (`dx/src/com/android/dx/cf/cst/ConstantPoolParser.java`) — 35 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parseInstruction` **(Many-Argument Workhorses)** (@ `dx/src/com/android/dx/cf/code/BytecodeArray.java`) -> Impact: **392.1** | LOC: 602
  * *Intent:* * <li>Numeric conversion ops ({@code i2l}, etc.) are left alone * to avoid too much confustion, but their {@code type} is * the pushed type. E.g., {@c...
- `visitNoArgs` **(Many-Argument Workhorses)** (@ `dx/src/com/android/dx/cf/code/Simulator.java`) -> Impact: **213.9** | LOC: 297
  * *Intent:* /** {@inheritDoc} */
- `run` **(Many-Argument Workhorses)** (@ `dx/src/com/android/dx/cf/code/ValueAwareMachine.java`) -> Impact: **210.4** | LOC: 168
  * *Intent:* /** {@inheritDoc} */
- `jopToRopOpcode` **(Many-Argument Workhorses)** (@ `dx/src/com/android/dx/cf/code/RopperMachine.java`) -> Impact: **180.4** | LOC: 247
  * *Intent:* /** * Gets the register opcode for the given Java opcode. * * @param jop {@code jop >= 0;} the Java opcode * @param cst {@code null-ok;} the constant ...
- `ropFor` **(Many-Argument Workhorses)** (@ `dx/src/com/android/dx/rop/code/Rops.java`) -> Impact: **142.8** | LOC: 128
  * *Intent:* * shared instance. * * <p><b>Note:</b> This method does not do complete error checking on * its arguments, and so it may return an instance which seem...
- `ropFor` **(Many-Argument Workhorses)** (@ `dexgen/src/com/android/dexgen/rop/code/Rops.java`) -> Impact: **137.7** | LOC: 116
  * *Intent:* * shared instance. * * <p><b>Note:</b> This method does not do complete error checking on * its arguments, and so it may return an instance which seem...
- `run` **(Many-Argument Workhorses)** (@ `dx/src/com/android/dx/cf/code/RopperMachine.java`) -> Impact: **124.5** | LOC: 371
  * *Intent:* /** {@inheritDoc} */
- `parseFlags` **(Compute Cores)** (@ `dx/src/com/android/dx/command/dexer/Main.java`) -> Impact: **109.4** | LOC: 123
- `dopFor` **(Compute Cores)** (@ `dx/src/com/android/dx/dex/code/RopToDop.java`) -> Impact: **98.8** | LOC: 137
  * *Intent:* /** * Returns the dalvik opcode appropriate for the given register-based * instruction. * * @param insn {@code non-null;} the original instruction * @...
- `parse0` **(Many-Argument Workhorses)** (@ `dx/src/com/android/dx/cf/direct/StdAttributeFactory.java`) -> Impact: **98.5** | LOC: 118
  * *Intent:* /** {@inheritDoc} */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `dx/tests/128-multidex-option-overflow/src` | 2 | 133652.08 | 0.0% | 0.0% |
| `dx/src/com/android/dx/cf/code` | 27 | 5192.48 | 23.06% | 31.12% |
| `dx/src/com/android/dx/dex/file` | 55 | 3796.02 | 14.98% | 69.13% |
| `dexgen/src/com/android/dexgen/dex/file` | 50 | 3556.38 | 13.71% | 82.56% |
| `dx/src/com/android/dx/ssa` | 24 | 3455.5 | 25.96% | 36.0% |
| `dx/src/com/android/dx/dex/code` | 31 | 3252.22 | 19.0% | 42.6% |
| `dexgen/src/com/android/dexgen/dex/code` | 32 | 3188.02 | 17.9% | 41.19% |
| `dx/src/com/android/dx/rop/code` | 29 | 3027.46 | 13.69% | 5.19% |
| `dexgen/src/com/android/dexgen/rop/code` | 27 | 2784.38 | 14.04% | 20.52% |
| `dexgen/src/com/android/dexgen/util` | 29 | 1791.94 | 14.32% | 25.89% |

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
- `dx/junit-tests/com/android/dx/util/BitsTest.java` -> **28** Orphaned Functions | **0** Duplicates
- `dexgen/src/com/android/dexgen/dex/file/ClassDefItem.java` -> **21** Orphaned Functions | **0** Duplicates
- `dexgen/src/com/android/dexgen/dex/file/DexFile.java` -> **21** Orphaned Functions | **0** Duplicates
- `dx/src/com/android/dx/cf/code/BaseMachine.java` -> **21** Orphaned Functions | **0** Duplicates
- `dx/tests/070-dex-multianewarray/Blort.java` -> **18** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3380` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `dx/tests/128-multidex-option-overflow/src/FillerField.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.725)
- **Top Global Matches:** file_cluster_2: 4.725, file_cluster_17: 6.332, file_cluster_15: 7.425
- **Magnitude:** 66826.04 | **LOC:** 65503 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (20.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 65501`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.442
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dx/tests/128-multidex-option-overflow/src/FillerStatic.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.725)
- **Top Global Matches:** file_cluster_2: 4.725, file_cluster_17: 6.332, file_cluster_15: 7.425
- **Magnitude:** 66826.04 | **LOC:** 65503 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (20.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 65501`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.442
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dx/src/com/android/dx/command/dexer/Main.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.203)
- **Top Global Matches:** file_cluster_5: 8.203, file_cluster_12: 8.662, file_cluster_7: 10.172
- **Magnitude:** 1182.14 | **LOC:** 1975 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **62**; blast radius 0.442; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (95.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.9%)
- **Documentation Coverage:** 53.7634% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseFlags` **(Compute Cores)** (Impact: 109.4)
  * `dumpMethod` **(Many-Argument Workhorses)** (Impact: 32.4)
    * *Intent:* /** * Dumps any method with the given name in the given file. * * @param dex {@code non-null;} the d...
  * `processAllFiles` **(I/O & Config Routines)** (Impact: 27.6)
    * *Intent:* /** * Constructs the output {@link DexFile}, fill it in with all the * specified classes, and popula...
  * `processFileBytes` **(Many-Argument Workhorses)** (Impact: 22.2)
    * *Intent:* /** * Processes one file, which may be either a class or a resource. * * @param name {@code non-null...
  * `parse` **(Compute Cores)** (Impact: 19.7)
    * *Intent:* /** * Parses all command-line arguments and updates the state of the {@code Arguments} object * acco...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 150 instances
* *Concurrency (weighted view):* 95
* *State Mutation (weighted view):* 508
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 300`, `args: 64`, `func_start: 64`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 79`, `high_risk_execution: 1`, `state_mutation: 208`, `planned_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 23`, `api: 64`, `concurrency: 30`, `import: 62`
* *Defense:* `safety: 46`, `doc: 91`, `sync_locks: 9`, `immutability_locks: 21`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.442
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` com.android.dex.Dex, com.android.dex.DexException, com.android.dex.DexFormat, com.android.dex.util.FileUtils, com.android.dx.Version, com.android.dx.cf.code.SimException, com.android.dx.cf.direct.ClassPathOpener, com.android.dx.cf.direct.ClassPathOpener.FileNameFilter...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dx/src/com/android/dx/rop/code/Rops.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.411)
- **Top Global Matches:** file_cluster_12: 9.411, file_cluster_4: 10.34, file_cluster_7: 11.14
- **Magnitude:** 832.06 | **LOC:** 2132 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **10**; blast radius 0.854; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.9%), Complexity Load (formerly Cognitive Load) (9.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ropFor` **(Many-Argument Workhorses)** (Impact: 142.8)
    * *Intent:* * shared instance. * * <p><b>Note:</b> This method does not do complete error checking on * its argu...
  * `pickBinaryOp` **(Many-Argument Workhorses)** (Impact: 49.1)
    * *Intent:* * Returns the appropriate binary arithmetic rop for the given type * and arguments. The result is a ...
  * `opConv` **(Compute Cores)** (Impact: 47.0)
    * *Intent:* /** * Returns the appropriate {@code conv} rop for the given types. The * result is a shared instanc...
  * `pickIf` **(Many-Argument Workhorses)** (Impact: 33.6)
    * *Intent:* /** * Helper for all the {@code if*}-related methods, which * checks types and picks one of the four...
  * `opNewArray` **(Compute Cores)** (Impact: 16.7)
    * *Intent:* /** * Returns the appropriate {@code new-array} rop for the given * type. The result is a shared ins...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 492`, `args: 51`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 9`, `planned_debt: 1`
* *Architecture:* `api: 253`, `import: 10`
* *Defense:* `doc: 259`, `immutability_locks: 208`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.00029 | `Ripple Effect (Closeness):` 0.015574
  * `Imports (Out-Degree: 14):` com.android.dx.rop.cst.Constant, com.android.dx.rop.cst.CstBaseMethodRef, com.android.dx.rop.cst.CstCallSiteRef, com.android.dx.rop.cst.CstMethodRef, com.android.dx.rop.cst.CstType, com.android.dx.rop.type.Prototype, com.android.dx.rop.type.StdTypeList, com.android.dx.rop.type.Type...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `dexgen/src/com/android/dexgen/rop/code/Rops.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.513)
- **Top Global Matches:** file_cluster_12: 9.513, file_cluster_4: 10.237, file_cluster_7: 11.259
- **Magnitude:** 812.92 | **LOC:** 2087 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 0.513; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (80.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.6%), Complexity Load (formerly Cognitive Load) (8.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ropFor` **(Many-Argument Workhorses)** (Impact: 137.7)
    * *Intent:* * shared instance. * * <p><b>Note:</b> This method does not do complete error checking on * its argu...
  * `pickBinaryOp` **(Many-Argument Workhorses)** (Impact: 49.1)
    * *Intent:* * Returns the appropriate binary arithmetic rop for the given type * and arguments. The result is a ...
  * `opConv` **(Compute Cores)** (Impact: 39.9)
    * *Intent:* /** * Returns the appropriate {@code conv} rop for the given types. The * result is a shared instanc...
  * `pickIf` **(Many-Argument Workhorses)** (Impact: 33.6)
    * *Intent:* /** * Helper for all the {@code if*}-related methods, which * checks types and picks one of the four...
  * `opNewArray` **(Compute Cores)** (Impact: 16.7)
    * *Intent:* /** * Returns the appropriate {@code new-array} rop for the given * type. The result is a shared ins...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 481`, `args: 49`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 9`, `planned_debt: 1`
* *Architecture:* `api: 252`, `import: 9`
* *Defense:* `doc: 257`, `immutability_locks: 208`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.513
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.001781
  * `Imports (Out-Degree: 11):` com.android.dexgen.rop.cst.Constant, com.android.dexgen.rop.cst.CstBaseMethodRef, com.android.dexgen.rop.cst.CstMethodRef, com.android.dexgen.rop.cst.CstType, com.android.dexgen.rop.type.Prototype, com.android.dexgen.rop.type.StdTypeList, com.android.dexgen.rop.type.Type, com.android.dexgen.rop.type.TypeBearer...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/cf/code/BytecodeArray.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.169)
- **Top Global Matches:** file_cluster_4: 7.169, file_cluster_12: 8.239, file_cluster_15: 9.089
- **Magnitude:** 794.24 | **LOC:** 1440 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **15**; blast radius 0.614; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.0%), Connectivity (formerly Api Exposure) (55.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseInstruction` **(Many-Argument Workhorses)** (Impact: 392.1)
    * *Intent:* * <li>Numeric conversion ops ({@code i2l}, etc.) are left alone * to avoid too much confustion, but ...
  * `parseNewarray` **(Many-Argument Workhorses)** (Impact: 74.8)
    * *Intent:* /** * Helper to deal with {@code newarray}. * * @param offset the offset to the {@code newarray} opc...
  * `parseWide` **(Many-Argument Workhorses)** (Impact: 29.5)
    * *Intent:* /** * Helper to deal with {@code wide}. * * @param offset the offset to the {@code wide} opcode itse...
  * `parseTableswitch` **(Stateful Encapsulated Methods)** (Impact: 8.7)
    * *Intent:* /** * Helper to deal with {@code tableswitch}. * * @param offset the offset to the {@code tableswitc...
  * `processWorkSet` **(Compute Cores)** (Impact: 7.7)
    * *Intent:* /** * Processes the given "work set" by repeatedly finding the lowest bit * in the set, clearing it,...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 189`, `args: 42`, `func_start: 42`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 54`
* *Architecture:* `api: 39`, `import: 15`
* *Defense:* `safety: 8`, `doc: 48`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.614
  * `Choke Point (Betweenness):` 0.000103 | `Ripple Effect (Closeness):` 0.008331
  * `Imports (Out-Degree: 18):` com.android.dx.rop.cst.Constant, com.android.dx.rop.cst.ConstantPool, com.android.dx.rop.cst.CstDouble, com.android.dx.rop.cst.CstFloat, com.android.dx.rop.cst.CstInteger, com.android.dx.rop.cst.CstInvokeDynamic, com.android.dx.rop.cst.CstKnownNull, com.android.dx.rop.cst.CstLiteralBits...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/cf/code/Ropper.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.278)
- **Top Global Matches:** file_cluster_12: 7.278, file_cluster_5: 7.581, file_cluster_7: 9.381
- **Magnitude:** 704.68 | **LOC:** 1802 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **32**; blast radius 0.517; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.8%), Complexity Load (formerly Cognitive Load) (46.8%)
- **Documentation Coverage:** 8.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processBlock` **(Many-Argument Workhorses)** (Impact: 71.8)
    * *Intent:* /** * Processes the given block. * * @param block {@code non-null;} block to process * @param frame ...
  * `mergeAndWorkAsNecessary` **(Many-Argument Workhorses)** (Impact: 21.2)
    * *Intent:* /** * Helper for {@link #processBlock}, which merges frames and * adds to the work set, as necessary...
  * `copyBlock` **(Many-Argument Workhorses)** (Impact: 17.3)
    * *Intent:* /** * Copies a basic block, mapping its successors along the way. * * @param origLabel original bloc...
  * `addSetupBlocks` **(I/O & Config Routines)** (Impact: 13.8)
    * *Intent:* /** * Constructs and adds the blocks that perform setup for the rest of * the method. This includes ...
  * `forEachNonSubBlockDepthFirst0` **(Stateful Encapsulated Methods)** (Impact: 11.5)
    * *Intent:* /** * Visits each block once in depth-first successor order, ignoring * {@code jsr} targets. Worker ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 363
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 181`, `args: 55`, `func_start: 56`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 161`, `dead_code: 1`
* *Architecture:* `api: 6`, `import: 32`
* *Defense:* `safety: 8`, `doc: 91`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.517
  * `Choke Point (Betweenness):` 0.00023 | `Ripple Effect (Closeness):` 0.004311
  * `Imports (Out-Degree: 45):` com.android.dx.cf.iface.MethodList, com.android.dx.dex.DexOptions, com.android.dx.rop.code.AccessFlags, com.android.dx.rop.code.BasicBlock, com.android.dx.rop.code.BasicBlockList, com.android.dx.rop.code.Insn, com.android.dx.rop.code.InsnList, com.android.dx.rop.code.PlainCstInsn...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/merge/DexMerger.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.845)
- **Top Global Matches:** file_cluster_12: 7.845, file_cluster_16: 8.002, file_cluster_15: 8.579
- **Magnitude:** 671.48 | **LOC:** 1202 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **19**; blast radius 0.798; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (66.1%), Complexity Load (formerly Cognitive Load) (65.3%), Debt Markers (formerly Tech Debt) (8.0%)
- **Documentation Coverage:** 82.3529% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transformDebugInfoItem` **(Many-Argument Workhorses)** (Impact: 31.2)
  * `transformCode` **(Stateful Encapsulated Methods)** (Impact: 12.1)
  * `readIntoMap` **(Stateful Encapsulated Methods)** (Impact: 11.3)
  * `readSortableTypes` **(Stateful Encapsulated Methods)** (Impact: 10.7)
    * *Intent:* /** * Reads just enough data on each class so that we can sort it and then find * it later. */
  * `transformEncodedCatchHandler` **(Stateful Encapsulated Methods)** (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 65 instances
* *State Mutation (weighted view):* 292
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 172`, `args: 91`, `func_start: 91`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 162`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 12`, `import: 18`
* *Defense:* `doc: 20`, `test: 5`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.798
  * `Choke Point (Betweenness):` 0.000205 | `Ripple Effect (Closeness):` 0.003167
  * `Imports (Out-Degree: 20):` com.android.dex.Annotation, com.android.dex.CallSiteId, com.android.dex.ClassData, com.android.dex.ClassDef, com.android.dex.Code, com.android.dex.Dex, com.android.dex.DexException, com.android.dex.DexIndexOverflowException...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/cf/code/RopperMachine.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.914)
- **Top Global Matches:** file_cluster_4: 10.914, file_cluster_6: 12.168, file_cluster_12: 13.388
- **Magnitude:** 633.62 | **LOC:** 1033 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **31**; blast radius 0.452; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.9%), Complexity Load (formerly Cognitive Load) (52.0%)
- **Documentation Coverage:** 3.125% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `jopToRopOpcode` **(Many-Argument Workhorses)** (Impact: 180.4)
    * *Intent:* /** * Gets the register opcode for the given Java opcode. * * @param jop {@code jop >= 0;} the Java ...
  * `run` **(Many-Argument Workhorses)** (Impact: 124.5)
    * *Intent:* /** {@inheritDoc} */
  * `getSources` **(Many-Argument Workhorses)** (Impact: 20.6)
    * *Intent:* /** * Helper for {@link #run}, which gets the list of sources for the. * instruction. * * @param opc...
  * `updateReturnOp` **(Stateful Encapsulated Methods)** (Impact: 13.3)
    * *Intent:* /** * Sets or updates the information about the return block. * * @param op {@code non-null;} the op...
  * `RopperMachine` **(Many-Argument Workhorses)** (Impact: 10.5)
    * *Intent:* /** * Constructs an instance. * * @param ropper {@code non-null;} ropper controlling this instance *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 241
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 152`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 109`, `planned_debt: 1`, `unreferenced_by_name: 10`
* *Architecture:* `api: 14`, `import: 31`
* *Defense:* `safety: 2`, `doc: 36`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.452
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.002586
  * `Imports (Out-Degree: 41):` com.android.dx.cf.iface.Method, com.android.dx.cf.iface.MethodList, com.android.dx.rop.code.AccessFlags, com.android.dx.rop.code.FillArrayDataInsn, com.android.dx.rop.code.Insn, com.android.dx.rop.code.InvokePolymorphicInsn, com.android.dx.rop.code.PlainCstInsn, com.android.dx.rop.code.PlainInsn...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/io/instructions/InstructionCodec.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.254)
- **Top Global Matches:** file_cluster_12: 7.254, file_cluster_7: 9.569, file_cluster_5: 9.572
- **Magnitude:** 592.2 | **LOC:** 1113 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 1.202; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.3%), Guard Balance (formerly Safety Score) (56.6%)
- **Documentation Coverage:** 95.082% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decode` **(Compute Cores)** (Impact: 23.3)
  * `FORMAT_FILL_ARRAY_DATA_PAYLOAD` **(I/O & Config Routines)** (Impact: 21.8)
  * `decodeRegisterList` **(Many-Argument Workhorses)** (Impact: 20.6)
    * *Intent:* /** * Helper method that decodes any of the register-list formats. */
  * `encode` **(Compute Cores)** (Impact: 13.2)
  * `codeUnit` **(Stateful Encapsulated Methods)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 218`, `args: 132`, `func_start: 132`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 19`, `planned_debt: 1`, `duplicate_logic: 16`
* *Architecture:* `api: 113`, `import: 7`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.202
  * `Choke Point (Betweenness):` 0.001921 | `Ripple Effect (Closeness):` 0.025308
  * `Imports (Out-Degree: 21):` com.android.dex.DexException, com.android.dx.io.IndexType, com.android.dx.io.OpcodeInfo, com.android.dx.io.Opcodes, com.android.dx.util.Hex, java.io.EOFException, java.util.Arrays
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/ssa/back/FirstFitLocalCombiningAllocator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.723)
- **Top Global Matches:** file_cluster_12: 6.723, file_cluster_5: 7.033, file_cluster_16: 9.491
- **Magnitude:** 589.72 | **LOC:** 1260 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **22**; blast radius 0.464; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.1%), Complexity Load (formerly Cognitive Load) (36.9%)
- **Documentation Coverage:** 5.3571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findAnyFittingRange` **(Many-Argument Workhorses)** (Impact: 38.3)
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
* *Structure:* `branch: 124`, `structural_boundaries: 117`, `args: 47`, `func_start: 46`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 96`, `unreferenced_by_name: 6`
* *Architecture:* `api: 11`, `import: 22`
* *Defense:* `safety: 2`, `doc: 57`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.464
  * `Choke Point (Betweenness):` 0.000618 | `Ripple Effect (Closeness):` 0.007522
  * `Imports (Out-Degree: 21):` com.android.dx.dex.DexOptions, com.android.dx.rop.code.CstInsn, com.android.dx.rop.code.LocalItem, com.android.dx.rop.code.RegOps, com.android.dx.rop.code.RegisterSpec, com.android.dx.rop.code.RegisterSpecList, com.android.dx.rop.code.Rop, com.android.dx.rop.cst.CstInteger...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/cf/code/Simulator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.405)
- **Top Global Matches:** file_cluster_4: 9.405, file_cluster_6: 9.768, file_cluster_12: 14.084
- **Magnitude:** 550.46 | **LOC:** 956 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.452; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.4%), Complexity Load (formerly Cognitive Load) (27.4%)
- **Documentation Coverage:** 18.4211% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visitNoArgs` **(Many-Argument Workhorses)** (Impact: 213.9)
    * *Intent:* /** {@inheritDoc} */
  * `visitConstant` **(Many-Argument Workhorses)** (Impact: 56.4)
    * *Intent:* /** {@inheritDoc} */
  * `visitBranch` **(Many-Argument Workhorses)** (Impact: 53.8)
    * *Intent:* /** {@inheritDoc} */
  * `visitLocal` **(Many-Argument Workhorses)** (Impact: 37.8)
    * *Intent:* /** {@inheritDoc} */
  * `checkInvokeInterfaceSupported` **(Many-Argument Workhorses)** (Impact: 17.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 114`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 32`, `dead_code: 1`, `unreferenced_by_name: 7`
* *Architecture:* `api: 15`, `import: 16`
* *Defense:* `safety: 7`, `doc: 29`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.452
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.002981
  * `Imports (Out-Degree: 26):` com.android.dex.DexFormat, com.android.dx.dex.DexOptions, com.android.dx.rop.code.LocalItem, com.android.dx.rop.cst.Constant, com.android.dx.rop.cst.CstFieldRef, com.android.dx.rop.cst.CstInteger, com.android.dx.rop.cst.CstInterfaceMethodRef, com.android.dx.rop.cst.CstInvokeDynamic...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/ssa/SCCP.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.535)
- **Top Global Matches:** file_cluster_6: 10.535, file_cluster_8: 14.787, file_cluster_4: 15.922
- **Magnitude:** 494.96 | **LOC:** 681 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.442; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.9%), Complexity Load (formerly Cognitive Load) (42.7%)
- **Documentation Coverage:** 12.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `simulateMath` **(Many-Argument Workhorses)** (Impact: 58.6)
    * *Intent:* /** * Simulates math insns, if possible. * * @param insn non-null insn to simulate * @param resultTy...
  * `simulateBranch` **(Compute Cores)** (Impact: 55.3)
    * *Intent:* /** * Simulates branch insns, if possible. Adds reachable successor blocks * to the CFG worklists. *...
  * `simulateStmt` **(Compute Cores)** (Impact: 38.9)
    * *Intent:* /** * Simulates a statement and set the result lattice value. * @param insn instruction to simulate ...
  * `simulatePhi` **(Stateful Encapsulated Methods)** (Impact: 16.0)
    * *Intent:* /** * Simulates a PHI node and set the lattice for the result * to the appropriate value. * Meet val...
  * `run` **(I/O & Config Routines)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 233
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 94`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 83`, `planned_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 15`
* *Defense:* `safety: 5`, `doc: 24`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.442
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` com.android.dx.rop.code.CstInsn, com.android.dx.rop.code.Insn, com.android.dx.rop.code.PlainInsn, com.android.dx.rop.code.RegOps, com.android.dx.rop.code.RegisterSpec, com.android.dx.rop.code.RegisterSpecList, com.android.dx.rop.code.Rop, com.android.dx.rop.code.Rops...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dx/src/com/android/dx/ssa/EscapeAnalysis.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.443)
- **Top Global Matches:** file_cluster_4: 9.443, file_cluster_5: 9.572, file_cluster_12: 10.466
- **Magnitude:** 479.9 | **LOC:** 847 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.442; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.2%), Complexity Load (formerly Cognitive Load) (48.6%)
- **Documentation Coverage:** 29.4118% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processUse` **(Many-Argument Workhorses)** (Impact: 66.7)
    * *Intent:* /** * Handles non-phi uses of new objects. Checks to see how instruction is * used and updates the e...
  * `replaceUse` **(Many-Argument Workhorses)** (Impact: 32.9)
    * *Intent:* /** * Replaces the use for a scalar replaceable array. Gets and puts become * move instructions, and...
  * `processMoveResultPseudoInsn` **(Compute Cores)** (Impact: 25.9)
    * *Intent:* /** * Determine the origin of a move result pseudo instruction that generates * an object. Creates a...
  * `insertPlainInsnBefore` **(Stateful Encapsulated Methods)** (Impact: 13.6)
    * *Intent:* /** * Inserts a new PlainInsn before the given instruction. * TODO: move this somewhere more appropr...
  * `processPhiUse` **(Stateful Encapsulated Methods)** (Impact: 11.1)
    * *Intent:* /** * Handles phi uses of new objects. Will merge together the sources of a phi * into a single Esca...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 215
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 110`, `args: 27`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 81`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 9`, `import: 27`
* *Defense:* `doc: 32`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.442
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` com.android.dx.rop.code.Exceptions, com.android.dx.rop.code.FillArrayDataInsn, com.android.dx.rop.code.Insn, com.android.dx.rop.code.PlainCstInsn, com.android.dx.rop.code.PlainInsn, com.android.dx.rop.code.RegOps, com.android.dx.rop.code.RegisterSpec, com.android.dx.rop.code.RegisterSpecList...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dx/src/com/android/dx/cf/direct/StdAttributeFactory.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.734)
- **Top Global Matches:** file_cluster_12: 8.734, file_cluster_7: 9.305, file_cluster_5: 9.686
- **Magnitude:** 425.06 | **LOC:** 862 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **45**; blast radius 0.785; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.4%), Complexity Load (formerly Cognitive Load) (14.1%)
- **Documentation Coverage:** 3.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse0` **(Many-Argument Workhorses)** (Impact: 98.5)
    * *Intent:* /** {@inheritDoc} */
  * `code` **(Many-Argument Workhorses)** (Impact: 36.3)
    * *Intent:* /** * Parses a {@code Code} attribute. */
  * `parseBootstrapMethods` **(Many-Argument Workhorses)** (Impact: 24.9)
  * `parseLocalVariables` **(Many-Argument Workhorses)** (Impact: 17.0)
    * *Intent:* /** * Parse the table part of either a {@code LocalVariableTable} * or a {@code LocalVariableTypeTab...
  * `innerClasses` **(Many-Argument Workhorses)** (Impact: 16.1)
    * *Intent:* /** * Parses an {@code InnerClasses} attribute. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 157`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 37`
* *Architecture:* `api: 4`, `import: 45`
* *Defense:* `safety: 2`, `doc: 27`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.000417 | `Ripple Effect (Closeness):` 0.006334
  * `Imports (Out-Degree: 50):` com.android.dx.cf.attrib.AttAnnotationDefault, com.android.dx.cf.attrib.AttBootstrapMethods, com.android.dx.cf.attrib.AttCode, com.android.dx.cf.attrib.AttConstantValue, com.android.dx.cf.attrib.AttDeprecated, com.android.dx.cf.attrib.AttEnclosingMethod, com.android.dx.cf.attrib.AttExceptions, com.android.dx.cf.attrib.AttInnerClasses...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/dex/code/OutputFinisher.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.542)
- **Top Global Matches:** file_cluster_5: 7.542, file_cluster_12: 8.122, file_cluster_7: 9.455
- **Magnitude:** 415.28 | **LOC:** 947 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **17**; blast radius 0.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.1%), Complexity Load (formerly Cognitive Load) (37.5%)
- **Documentation Coverage:** 20.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `align64bits` **(Compute Cores)** (Impact: 29.7)
  * `performExpansion` **(Stateful Encapsulated Methods)** (Impact: 18.7)
    * *Intent:* /** * Helper for {@link #massageInstructions}, which constructs a * replacement list, where each {li...
  * `addConstants` **(Stateful Encapsulated Methods)** (Impact: 18.4)
    * *Intent:* /** * Helper for {@link #getAllConstants} which adds all the info for * a single instruction. * * @p...
  * `addConstants` **(Stateful Encapsulated Methods)** (Impact: 11.7)
    * *Intent:* /** * Helper for {@link #getAllConstants} which adds all the info for * a single {@code RegisterSpec...
  * `hasLocalInfo` **(Stateful Encapsulated Methods)** (Impact: 10.8)
    * *Intent:* /** * Helper for {@link #add} which scrutinizes a single * instruction for local variable informatio...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 176
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 77`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 74`, `planned_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 12`, `import: 17`
* *Defense:* `safety: 22`, `doc: 35`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.799
  * `Choke Point (Betweenness):` 0.000816 | `Ripple Effect (Closeness):` 0.005458
  * `Imports (Out-Degree: 24):` com.android.dex.DexException, com.android.dx.dex.DexOptions, com.android.dx.io.Opcodes, com.android.dx.rop.code.LocalItem, com.android.dx.rop.code.RegisterSpec, com.android.dx.rop.code.RegisterSpecList, com.android.dx.rop.code.RegisterSpecSet, com.android.dx.rop.code.SourcePosition...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/ssa/SsaMethod.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.435)
- **Top Global Matches:** file_cluster_5: 6.435, file_cluster_7: 8.398, file_cluster_12: 8.594
- **Magnitude:** 401.28 | **LOC:** 858 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **17**; blast radius 1.858; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.9%), Connectivity (formerly Api Exposure) (52.8%)
- **Documentation Coverage:** 8.046% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `forEachBlockDepthFirst` **(Compute Cores)** (Impact: 13.8)
    * *Intent:* /** * Walks the basic block tree in depth-first order, calling the visitor * method once for every b...
  * `deleteInsns` **(Compute Cores)** (Impact: 13.4)
    * *Intent:* /** * Deletes all insns in the set from this method. * * @param deletedInsns {@code non-null;} insns...
  * `updateOneDefinition` **(Compute Cores)** (Impact: 11.4)
    * *Intent:* /** * Updates a single definition. * * @param insn {@code non-null;} insn who's result should be rec...
  * `onSourceChanged` **(Compute Cores)** (Impact: 8.8)
    * *Intent:* /** * Updates the use list for a single change in source register. * * @param insn {@code non-null;}...
  * `isRegALocal` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* /** * Checks to see if the given SSA reg is ever associated with a local * local variable. Each SSA ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 106`, `args: 48`, `func_start: 50`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 77`, `planned_debt: 1`
* *Architecture:* `api: 40`, `import: 17`
* *Defense:* `doc: 58`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.858
  * `Choke Point (Betweenness):` 0.000358 | `Ripple Effect (Closeness):` 0.017589
  * `Imports (Out-Degree: 16):` com.android.dx.rop.code.BasicBlockList, com.android.dx.rop.code.Insn, com.android.dx.rop.code.PlainInsn, com.android.dx.rop.code.RegOps, com.android.dx.rop.code.RegisterSpec, com.android.dx.rop.code.RegisterSpecList, com.android.dx.rop.code.Rop, com.android.dx.rop.code.RopMethod...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/ssa/SsaBasicBlock.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.85)
- **Top Global Matches:** file_cluster_12: 5.85, file_cluster_5: 7.348, file_cluster_15: 8.339
- **Magnitude:** 376.18 | **LOC:** 1012 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **19**; blast radius 1.59; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.3%), Connectivity (formerly Api Exposure) (53.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scheduleUseBeforeAssigned` **(Compute Cores)** (Impact: 16.1)
    * *Intent:* /** * Ensures that all move operations in this block occur such that * reads of any register happen ...
  * `scheduleMovesFromPhis` **(I/O & Config Routines)** (Impact: 15.0)
    * *Intent:* /** * Sorts move instructions added via {@code addMoveToEnd} during * phi removal so that results do...
  * `addMoveToEnd` **(Many-Argument Workhorses)** (Impact: 13.2)
    * *Intent:* /** * Adds a move instruction to the end of this basic block, just * before the last instruction. If...
  * `replaceSuccessor` **(Compute Cores)** (Impact: 10.0)
    * *Intent:* /** * Replaces an old successor with a new successor. This will throw * RuntimeException if {@code o...
  * `newFromRop` **(Many-Argument Workhorses)** (Impact: 9.7)
    * *Intent:* /** * Creates a new SSA basic block from a ROP form basic block. * * @param rmeth original method * ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 106`, `args: 44`, `func_start: 44`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 71`, `planned_debt: 3`
* *Architecture:* `api: 44`, `import: 19`
* *Defense:* `safety: 2`, `doc: 61`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.59
  * `Choke Point (Betweenness):` 0.000423 | `Ripple Effect (Closeness):` 0.014291
  * `Imports (Out-Degree: 22):` com.android.dx.rop.code.BasicBlock, com.android.dx.rop.code.BasicBlockList, com.android.dx.rop.code.Insn, com.android.dx.rop.code.InsnList, com.android.dx.rop.code.PlainInsn, com.android.dx.rop.code.RegisterSpec, com.android.dx.rop.code.RegisterSpecList, com.android.dx.rop.code.Rop...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dex/Dex.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 8.001)
- **Top Global Matches:** file_cluster_11: 8.001, file_cluster_15: 8.044, file_cluster_0: 8.106
- **Magnitude:** 359.44 | **LOC:** 820 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **24** in-repo importer(s); it depends on **27**; blast radius 5.527; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.3%), Guard Balance (formerly Safety Score) (53.5%)
- **Documentation Coverage:** 84.0237% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Dex` **(Defensive Guards)** (Impact: 10.9)
    * *Intent:* /** * Creates a new dex buffer from the dex file {@code file}. */
  * `findCatchHandlerIndex` **(Stateful Encapsulated Methods)** (Impact: 5.6)
  * `readCode` **(I/O & Config Routines)** (Impact: 5.5)
  * `readCatchHandler` **(Stateful Encapsulated Methods)** (Impact: 4.8)
  * `readShortArray` **(Compute Cores)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 223`, `args: 91`, `func_start: 91`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 33`, `duplicate_logic: 2`
* *Architecture:* `io: 13`, `api: 80`, `import: 27`
* *Defense:* `safety: 16`, `doc: 15`, `test: 1`, `immutability_locks: 26`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.527
  * `Choke Point (Betweenness):` 0.000809 | `Ripple Effect (Closeness):` 0.022159
  * `Imports (Out-Degree: 17):` com.android.dex.Code.CatchHandler, com.android.dex.Code.Try, com.android.dex.MethodHandle.MethodHandleType, com.android.dex.util.ByteInput, com.android.dex.util.ByteOutput, com.android.dex.util.FileUtils, java.io.ByteArrayOutputStream, java.io.File...
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `dexgen/src/com/android/dexgen/dex/code/LocalList.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.955)
- **Top Global Matches:** file_cluster_12: 6.955, file_cluster_5: 7.926, file_cluster_7: 7.935
- **Magnitude:** 354.28 | **LOC:** 949 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **9**; blast radius 0.742; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.7%), Connectivity (formerly Api Exposure) (43.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `startLocal` **(Many-Argument Workhorses)** (Impact: 29.9)
    * *Intent:* /** * Starts a local at the given address. * * @param address {@code >= 0;} the address * @param sta...
  * `debugVerify0` **(Compute Cores)** (Impact: 21.4)
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
* *Structure:* `branch: 81`, `structural_boundaries: 86`, `args: 33`, `func_start: 33`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 46`, `planned_debt: 2`
* *Architecture:* `api: 31`, `import: 9`
* *Defense:* `safety: 8`, `doc: 54`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.742
  * `Choke Point (Betweenness):` 0.000881 | `Ripple Effect (Closeness):` 0.032333
  * `Imports (Out-Degree: 8):` com.android.dexgen.rop.code.RegisterSpec, com.android.dexgen.rop.code.RegisterSpecSet, com.android.dexgen.rop.cst.CstType, com.android.dexgen.rop.cst.CstUtf8, com.android.dexgen.rop.type.Type, com.android.dexgen.util.FixedSizeList, java.io.PrintStream, java.util.ArrayList...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/dex/code/LocalList.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.83)
- **Top Global Matches:** file_cluster_12: 6.83, file_cluster_5: 7.668, file_cluster_7: 7.913
- **Magnitude:** 351.28 | **LOC:** 948 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 0.574; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.6%), Connectivity (formerly Api Exposure) (41.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `startLocal` **(Many-Argument Workhorses)** (Impact: 29.9)
    * *Intent:* /** * Starts a local at the given address. * * @param address {@code >= 0;} the address * @param sta...
  * `debugVerify0` **(Compute Cores)** (Impact: 21.4)
    * *Intent:* /** * Helper for {@link #debugVerify} which does most of the work. */
  * `checkForEmptyRange` **(Many-Argument Workhorses)** (Impact: 20.6)
    * *Intent:* * Helper for {@link #endLocal}, which handles the cases where * and end local is issued at the same ...
  * `snapshot` **(Compute Cores)** (Impact: 18.7)
    * *Intent:* /** * Sets the local state at the given address to the given snapshot. * The first call on this inst...
  * `make` **(Defensive Guards)** (Impact: 10.6)
    * *Intent:* /** * Constructs an instance for the given method, based on the given * block order and intermediate...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 86`, `args: 33`, `func_start: 33`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 46`, `planned_debt: 2`
* *Architecture:* `api: 31`, `import: 9`
* *Defense:* `safety: 7`, `doc: 54`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.574
  * `Choke Point (Betweenness):` 0.000494 | `Ripple Effect (Closeness):` 0.017162
  * `Imports (Out-Degree: 9):` com.android.dx.rop.code.RegisterSpec, com.android.dx.rop.code.RegisterSpecSet, com.android.dx.rop.cst.CstString, com.android.dx.rop.cst.CstType, com.android.dx.rop.type.Type, com.android.dx.util.FixedSizeList, java.io.PrintStream, java.util.ArrayList...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `dexgen/src/com/android/dexgen/util/ByteArrayAnnotatedOutput.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.389)
- **Top Global Matches:** file_cluster_12: 5.389, file_cluster_15: 8.521, file_cluster_7: 8.522
- **Magnitude:** 340.58 | **LOC:** 640 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **3**; blast radius 0.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (70.6%), Connectivity (formerly Api Exposure) (53.0%), Complexity Load (formerly Cognitive Load) (34.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `enableAnnotations` **(Compute Cores)** (Impact: 11.4)
    * *Intent:* /** * Indicates that this instance should keep annotations. This method may * be called only once pe...
  * `write` **(Compute Cores)** (Impact: 11.1)
    * *Intent:* /** {@inheritDoc} */
  * `writeAnnotationsTo` **(Compute Cores)** (Impact: 10.9)
    * *Intent:* /** * Writes the annotated content of this instance to the given writer. * * @param out {@code non-n...
  * `annotate` **(Compute Cores)** (Impact: 9.6)
    * *Intent:* /** {@inheritDoc} */
  * `alignTo` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* /** {@inheritDoc} */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 67`, `args: 36`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 66`
* *Architecture:* `io: 4`, `api: 34`, `import: 3`
* *Defense:* `doc: 49`, `test: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.806
  * `Choke Point (Betweenness):` 5.2e-05 | `Ripple Effect (Closeness):` 0.017419
  * `Imports (Out-Degree: 3):` java.io.IOException, java.io.Writer, java.util.ArrayList
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/util/ByteArrayAnnotatedOutput.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.833)
- **Top Global Matches:** file_cluster_12: 5.833, file_cluster_5: 8.37, file_cluster_7: 8.741
- **Magnitude:** 320.52 | **LOC:** 656 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **7**; blast radius 1.35; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (67.5%), Connectivity (formerly Api Exposure) (55.7%), Complexity Load (formerly Cognitive Load) (30.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `enableAnnotations` **(Compute Cores)** (Impact: 11.4)
    * *Intent:* /** * Indicates that this instance should keep annotations. This method may * be called only once pe...
  * `write` **(Compute Cores)** (Impact: 11.2)
    * *Intent:* /** {@inheritDoc} */
  * `writeAnnotationsTo` **(Compute Cores)** (Impact: 10.9)
    * *Intent:* /** * Writes the annotated content of this instance to the given writer. * * @param out {@code non-n...
  * `annotate` **(Compute Cores)** (Impact: 9.7)
    * *Intent:* /** {@inheritDoc} */
  * `alignTo` **(Compute Cores)** (Impact: 8.3)
    * *Intent:* /** {@inheritDoc} */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 71`, `args: 37`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 59`
* *Architecture:* `io: 4`, `api: 35`, `import: 7`
* *Defense:* `doc: 50`, `test: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.35
  * `Choke Point (Betweenness):` 0.000612 | `Ripple Effect (Closeness):` 0.023357
  * `Imports (Out-Degree: 6):` com.android.dex.Leb128, com.android.dex.util.ByteOutput, com.android.dex.util.ExceptionWithContext, java.io.IOException, java.io.Writer, java.util.ArrayList, java.util.Arrays
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `dexgen/src/com/android/dexgen/dex/file/DebugInfoDecoder.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.616)
- **Top Global Matches:** file_cluster_6: 7.616, file_cluster_4: 8.889, file_cluster_12: 15.867
- **Magnitude:** 320.26 | **LOC:** 654 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.47; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.2%), Complexity Load (formerly Cognitive Load) (48.1%)
- **Documentation Coverage:** 17.3913% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateEncode0` **(Many-Argument Workhorses)** (Impact: 70.3)
  * `decode0` **(I/O & Config Routines)** (Impact: 31.6)
  * `readSignedLeb128` **(Compute Cores)** (Impact: 8.3)
    * *Intent:* /** * Reads a DWARFv3-style signed LEB128 integer to the specified stream. * See DWARF v3 section 7....
  * `DebugInfoDecoder` **(Many-Argument Workhorses)** (Impact: 6.8)
    * *Intent:* /** * Constructs an instance. * * @param encoded encoded debug info * @param codesize size of code b...
  * `readUnsignedLeb128` **(Compute Cores)** (Impact: 6.5)
    * *Intent:* /** * Reads a DWARFv3-style unsigned LEB128 integer to the specified stream. * See DWARF v3 section ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 83`, `args: 14`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 67`, `planned_debt: 4`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 18`, `import: 15`
* *Defense:* `safety: 10`, `doc: 32`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.001056
  * `Imports (Out-Degree: 16):` com.android.dexgen.dex.code.DalvCode, com.android.dexgen.dex.code.DalvInsnList, com.android.dexgen.dex.code.LocalList, com.android.dexgen.dex.code.PositionList, com.android.dexgen.dex.file.DebugInfoConstants.*, com.android.dexgen.rop.cst.CstMethodRef, com.android.dexgen.rop.cst.CstUtf8, com.android.dexgen.rop.type.Prototype...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `dx/src/com/android/dx/dex/file/DebugInfoEncoder.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.172)
- **Top Global Matches:** file_cluster_5: 8.172, file_cluster_7: 9.173, file_cluster_12: 9.457
- **Magnitude:** 317.36 | **LOC:** 933 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **32** in-repo importer(s); it depends on **30**; blast radius 2.83; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.2%), Complexity Load (formerly Cognitive Load) (20.2%)
- **Documentation Coverage:** 25.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emitHeader` **(Many-Argument Workhorses)** (Impact: 36.7)
    * *Intent:* /** * Emits the header sequence, which consists of LEB128-encoded initial * line number and string i...
  * `emitLocalsAtAddress` **(Compute Cores)** (Impact: 15.8)
    * *Intent:* /** * Emits all local variable activity that occurs at the current * {@link #address} starting at th...
  * `convert0` **(I/O & Config Routines)** (Impact: 12.7)
  * `emitPosition` **(Stateful Encapsulated Methods)** (Impact: 10.8)
    * *Intent:* /** * Emits the necessary byte sequences to emit the given position table * entry. This will typical...
  * `entryAnnotationString` **(Stateful Encapsulated Methods)** (Impact: 10.0)
    * *Intent:* /** * Returns a string representation of this LocalList entry that is * appropriate for emitting as ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 94`, `args: 29`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 47`, `planned_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 8`, `import: 30`
* *Defense:* `safety: 2`, `doc: 33`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.83
  * `Choke Point (Betweenness):` 0.002961 | `Ripple Effect (Closeness):` 0.027115
  * `Imports (Out-Degree: 18):` com.android.dex.util.ExceptionWithContext, com.android.dx.dex.code.LocalList, com.android.dx.dex.code.PositionList, com.android.dx.dex.file.DebugInfoConstants.DBG_ADVANCE_LINE, com.android.dx.dex.file.DebugInfoConstants.DBG_ADVANCE_PC, com.android.dx.dex.file.DebugInfoConstants.DBG_END_LOCAL, com.android.dx.dex.file.DebugInfoConstants.DBG_END_SEQUENCE, com.android.dx.dex.file.DebugInfoConstants.DBG_FIRST_SPECIAL...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `dx/tests/139-lambda-metafactory/Main.java` (JAVA) | Magnitude: 6.0 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 7, args: 4, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `dx/junit-tests/com/android/dex/EncodedValueReaderTest.java` (JAVA) | Magnitude: 38.44 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 92, test: 57, structural_boundaries: 20, args: 12
- `dx/src/com/android/dex/Dex.java` (JAVA) | Magnitude: 359.44 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 622, structural_boundaries: 223, core_var_decl: 134, args: 91
- `dx/src/com/android/dx/io/instructions/DecodedInstruction.java` (JAVA) | Magnitude: 149.32 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 232, structural_boundaries: 73, api: 43, args: 42
- `dx/tests/089-dex-define-object/Object.java` (JAVA) | Magnitude: 26.28 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 21, api: 12, structural_boundaries: 11, func_start: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `dx/src/com/android/dx/command/dexer/DxContext.java` (JAVA) | Magnitude: 15.1 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 15, api: 8, import: 5
- `dx/src/com/android/dx/merge/SortableType.java` (JAVA) | Magnitude: 70.18 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 22, branch: 17, core_var_decl: 10
- `dx/src/com/android/dx/ssa/PhiTypeResolver.java` (JAVA) | Magnitude: 73.8 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 89, core_var_decl: 30, structural_boundaries: 22, branch: 17
- `dx/src/com/android/dx/dex/code/DalvInsn.java` (JAVA) | Magnitude: 161.68 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 168, structural_boundaries: 43, doc: 33, branch: 30
- `dx/src/com/android/dx/util/FixedSizeList.java` (JAVA) | Magnitude: 90.9 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 126, structural_boundaries: 28, branch: 16, doc: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `dx/src/com/android/dx/cf/attrib/AttBootstrapMethods.java` (JAVA) | Magnitude: 19.24 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 23, core_var_decl: 7, structural_boundaries: 6, immutability_locks: 6
- `dx/src/com/android/dx/cf/iface/Field.java` (JAVA) | Magnitude: 3.22 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 4, api: 2, doc: 2, indent_spaces: 2
- `dexgen/src/com/android/dexgen/rop/FieldList.java` (JAVA) | Magnitude: 7.84 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 4, doc: 4, args: 3, func_start: 3
- `dexgen/src/com/android/dexgen/rop/type/TypeBearer.java` (JAVA) | Magnitude: 11.7 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 6, doc: 6, indent_spaces: 6, args: 5
- `dx/src/com/android/dx/rop/type/TypeBearer.java` (JAVA) | Magnitude: 11.7 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 6, doc: 6, indent_spaces: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `dx/src/com/android/dx/rop/code/LocalItem.java` (JAVA) | Magnitude: 54.42 | Delta: **0.184** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 21, branch: 16, safety_bypasses: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `dx/tests/062-dex-synch-method/Blort.java` (JAVA) | Magnitude: 51.34 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 15, api: 11, args: 10
- `dx/src/com/android/dex/DexFormat.java` (JAVA) | Magnitude: 83.78 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 66, core_var_decl: 28, api: 24, doc: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `dx/src/com/android/dex/Leb128.java` (JAVA) | Magnitude: 83.4 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 65, core_var_decl: 16, state_mutation: 15, design_snake_case: 13
- `dexgen/src/com/android/dexgen/dex/file/AnnotationUtils.java` (JAVA) | Magnitude: 100.38 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 111, structural_boundaries: 54, core_var_decl: 35, state_mutation: 26
- `dx/tests/135-invoke-custom/src/invokecustom/InvokeCustom.java` (JAVA) | Magnitude: 74.52 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 49, debug_prints: 34, args: 26
- `dx/src/com/android/dx/dex/file/AnnotationUtils.java` (JAVA) | Magnitude: 105.3 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 118, structural_boundaries: 55, core_var_decl: 37, state_mutation: 28
- `dx/tests/137-dexmerger-dex38/src/invokecustom/InvokeCustom.java` (JAVA) | Magnitude: 70.66 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 128, structural_boundaries: 43, debug_prints: 33, args: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `dexgen/src/com/android/dexgen/dex/code/DalvOps.java` (JAVA) | Magnitude: 266.38 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 261, api: 260, immutability_locks: 260, globals: 259

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `dx/tests/069-dex-source-position/Blort.java` (JAVA) | Magnitude: 13.22 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 4, branch: 2, safety: 2
- `dx/src/com/android/dx/cf/iface/Method.java` (JAVA) | Magnitude: 3.24 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, api: 2, doc: 2, indent_spaces: 2
- `dx/src/com/android/dx/cf/code/SimException.java` (JAVA) | Magnitude: 9.38 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, api: 4, args: 3
- `dx/src/com/android/dx/cf/iface/ParseException.java` (JAVA) | Magnitude: 9.38 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, api: 4, args: 3
- `dx/src/com/android/dx/util/MutabilityException.java` (JAVA) | Magnitude: 9.38 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, api: 4, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `dx/src/com/android/dx/ssa/EscapeAnalysis.java` (JAVA) | Magnitude: 479.9 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 485, structural_boundaries: 110, core_var_decl: 106, branch: 92

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `dx/src/com/android/dx/cf/code/BootstrapMethodArgumentsList.java` (JAVA) | Magnitude: 13.88 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 16, import: 10, safety: 8
- `dx/src/com/android/dx/dex/code/LocalSnapshot.java` (JAVA) | Magnitude: 31.1 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 19, doc: 9, api: 8
- `dexgen/src/com/android/dexgen/rop/cst/CstArray.java` (JAVA) | Magnitude: 55.7 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 25, doc: 16, api: 15
- `dexgen/src/com/android/dexgen/dex/file/UniformItemSection.java` (JAVA) | Magnitude: 23.96 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 13, api: 8, doc: 8
- `dx/src/com/android/dx/dex/file/UniformItemSection.java` (JAVA) | Magnitude: 23.96 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 13, api: 8, doc: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `dexgen/src/com/android/dexgen/dex/file/ClassDefItem.java` (JAVA) | Magnitude: 148.2 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 184, structural_boundaries: 49, doc: 32, api: 24
- `dx/src/com/android/dx/dex/file/ClassDefItem.java` (JAVA) | Magnitude: 148.38 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 183, structural_boundaries: 49, doc: 31, branch: 23
- `dx/src/com/android/dx/dex/code/form/Form20t.java` (JAVA) | Magnitude: 23.12 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 15, doc: 9, api: 8
- `dx/src/com/android/dx/dex/code/DalvInsnList.java` (JAVA) | Magnitude: 116.3 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 133, core_var_decl: 39, structural_boundaries: 35, design_snake_case: 34
- `dexgen/src/com/android/dexgen/dex/code/DalvInsnList.java` (JAVA) | Magnitude: 97.3 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 121, structural_boundaries: 32, core_var_decl: 31, design_snake_case: 28

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `dx/src/com/android/dx/dex/file/DebugInfoEncoder.java` -> **Severity: 0.296** (Bridge: 0.003 * Flux: 99.8043%)
- `dx/src/com/android/dx/dex/file/DexFile.java` -> **Severity: 0.213** (Bridge: 0.0022 * Flux: 98.4863%)
- `dx/src/com/android/dx/dex/code/DalvInsnList.java` -> **Severity: 0.148** (Bridge: 0.0015 * Flux: 99.9932%)
- `dx/src/com/android/dx/dex/code/Dop.java` -> **Severity: 0.143** (Bridge: 0.0019 * Flux: 74.6165%)
- `dx/src/com/android/dx/ssa/Optimizer.java` -> **Severity: 0.135** (Bridge: 0.0013 * Flux: 99.9844%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `dx/src/com/android/dx/util/Hex.java` -> **Severity: 10.135** (Embedded: 0.125 * Error Risk: 81.0728%)
- `dexgen/src/com/android/dexgen/util/Hex.java` -> **Severity: 7.684** (Embedded: 0.0948 * Error Risk: 81.0728%)
- `dexgen/src/com/android/dexgen/rop/code/RegisterSpec.java` -> **Severity: 6.9** (Embedded: 0.0862 * Error Risk: 80.0%)
- `dx/src/com/android/dx/rop/cst/CstString.java` -> **Severity: 6.785** (Embedded: 0.0972 * Error Risk: 69.8114%)
- `dx/src/com/android/dx/rop/type/Type.java` -> **Severity: 6.446** (Embedded: 0.1142 * Error Risk: 56.451%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `dx/tests/089-dex-define-object/Object.java` -> **Severity: 2289.2** (Blast Radius: 22.892 * Doc Risk: 100.0%)
- `dx/src/com/android/dex/Dex.java` -> **Severity: 464.399** (Blast Radius: 5.527 * Doc Risk: 84.0237%)
- `dx/src/com/android/dex/util/ByteArrayByteInput.java` -> **Severity: 149.6** (Blast Radius: 1.496 * Doc Risk: 100.0%)
- `dx/src/com/android/dx/util/ByteArray.java` -> **Severity: 128.939** (Blast Radius: 5.265 * Doc Risk: 24.4898%)
- `dx/src/com/android/dex/TypeList.java` -> **Severity: 121.2** (Blast Radius: 1.212 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 393 literal sites + 5 sites through wrappers = 398
- **`memory_alloc`:** 5 literal sites + 2 sites through wrappers = 7
- **`panics_and_aborts`:** 1437 literal sites + 145 sites through wrappers = 1582

- `throwBadType` (function, panics_and_aborts, primitive): 17 call sites in 1 files -- `dexgen/src/com/android/dexgen/rop/code/Rops.java`
- `throwBadType` (function, panics_and_aborts, primitive): 17 call sites in 1 files -- `dx/src/com/android/dx/rop/code/Rops.java`
- `throwBadLength` (function, panics_and_aborts, primitive): 12 call sites in 1 files -- `dx/src/com/android/dx/cf/direct/StdAttributeFactory.java`
- `throwSeverelyTruncated` (function, panics_and_aborts, primitive): 12 call sites in 1 files -- `dx/src/com/android/dx/cf/direct/StdAttributeFactory.java`
- `fail` (function, panics_and_aborts, primitive): 11 call sites in 5 files -- `dx/src/com/android/dx/cf/code/Simulator.java`
- `throwBadUtf8` (function, panics_and_aborts, primitive): 9 call sites in 1 files -- `dexgen/src/com/android/dexgen/rop/cst/CstUtf8.java`
- `throwBadUtf8` (function, panics_and_aborts, primitive): 9 call sites in 1 files -- `dx/src/com/android/dx/rop/cst/CstString.java`
- `throwBounds` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `dexgen/src/com/android/dexgen/util/ByteArrayAnnotatedOutput.java`
- `throwBounds` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `dx/src/com/android/dx/util/ByteArrayAnnotatedOutput.java`
- `throwSimException` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `dx/src/com/android/dx/cf/code/OneLocalsArray.java`
- `throwTruncated` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `dx/src/com/android/dx/cf/direct/StdAttributeFactory.java`
- `getStarts0` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `dexgen/src/com/android/dexgen/rop/code/LocalVariableInfo.java`
*(+17 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 16985 call pairs -- scoped 59.0%, unique 0.7%, ambiguous 20.8%, external 19.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| java | 16573 | 60.2% | 0.7% | 21.3% | 17.8% |
| shell | 345 | 5.2% | 0.0% | 0.0% | 94.8% |
| c | 67 | 49.3% | 0.0% | 0.0% | 50.7% |

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
