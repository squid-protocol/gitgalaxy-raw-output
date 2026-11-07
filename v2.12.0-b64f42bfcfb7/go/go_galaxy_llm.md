# ARCHITECTURAL_BRIEF: go
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/golang/go` |
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
- **Scope:** 12206 analyzed artifact(s), 1406003 LOC.
- **Load-bearing artifact:** `src/runtime/runtime2.go` -- 216 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/cmd/go/internal/load/pkg.go` -- pulls in 43 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/cmd/compile/internal/ssagen/ssa.go` at magnitude 5918.22 (structural weight, not risk).
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
| Total Artifacts | 15154 |
| Analyzed Artifacts (Scanned) | 12206 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2948 |
| Total LOC | 1406003 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 80.5% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.9163 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0179 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8828 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 598 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 9707 | 1274741 | 79.5% |
| PLAINTEXT | 1613 | 6 | 13.2% |
| ASSEMBLY | 565 | 104605 | 4.6% |
| C | 127 | 6138 | 1.0% |
| MARKDOWN | 76 | 0 | 0.6% |
| JSON | 29 | 3215 | 0.2% |
| YAML | 26 | 2366 | 0.2% |
| SHELL | 20 | 1217 | 0.2% |
| PERL | 9 | 1058 | 0.1% |
| HTML | 7 | 9333 | 0.1% |
| JAVASCRIPT | 5 | 581 | 0.0% |
| BATCH | 5 | 120 | 0.0% |
| M4 | 4 | 26 | 0.0% |
| MAKEFILE | 3 | 16 | 0.0% |
| PYTHON | 2 | 425 | 0.0% |
| FORTRAN | 2 | 8 | 0.0% |
| OBJECTIVE-C | 2 | 15 | 0.0% |
| CPP | 1 | 7 | 0.0% |
| CSV | 1 | 2119 | 0.0% |
| DOCKERFILE | 1 | 6 | 0.0% |
| CSS | 1 | 1 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 3 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 12201 |
| latin-1 | latin-1-fallback | 2 |
| unknown | unknown | 2 |
| cp1252 | cp1252-fallback | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 32%, State Mutators Files 11%, Callbacks & Closures Files 11%, Large Core Modules (3) 8%, Large Core Modules (2) 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 10517 | 86.2% |
| Unknown | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1685 | 13.8% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2948*

**Composition by Extension & Reason:**
- `.go`: 1286x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Machine-Generated Source Code Signature: 1911 LOC), 5x Excluded (Machine-Generated Source Code Signature: 1329 LOC)
- `.crt`: 405x Excluded (Binary Format Detected), 2x Unsupported Format (.crt)
- `no_extension`: 167x Unsupported Format (.undeterminable), 72x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 37x Excluded (Binary Format Detected)
- `.s`: 64x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 10701 LOC), 1x Excluded (Embedded Array/Matrix Payload: 4602 commas in 1387 LOC)
- `.png`: 56x Excluded (Explicitly Denied Extension: '.png')
- `.input`: 51x Unsupported Format (.input)
- `.test`: 42x Unsupported Format (.test)
- `.tar`: 38x Excluded (Explicitly Denied Extension: '.tar')
- `.sng`: 34x Unsupported Format (.sng), 1x Excluded (Saturation: Line 9 exceeds 500 chars)
- `.zip`: 34x Excluded (Explicitly Denied Extension: '.zip')
- `.jpeg`: 30x Excluded (Explicitly Denied Extension: '.jpeg')
- `.out`: 30x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.pem`: 29x Unsupported Format (.pem)
- `.rules`: 24x Unsupported Format (.rules), 1x Excluded (Machine-Generated Source Code Signature: 3114 LOC)
- `.base64`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.base64), 5x Excluded (Saturation: Line 1 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 11.5 | 3.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 35.6 | 50.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 26.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.7 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 6.4 | 0.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 6.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 32.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.8 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 58.0 | 70.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 52889 | 4385 | 9 | `src/reflect/all_test.go` |
| cleanup | 3953 | 815 | 0 | `src/net/http/serve_test.go` |
| guards | 67751 | 5822 | 15 | `src/cmd/cgo/internal/test/callback.go` |
| danger | 26072 | 3522 | 5 | `test/return.go` |
| concurrency | 13430 | 1488 | 1 | `src/runtime/race/testdata/mop_test.go` |
| connectivity | 83339 | 5448 | 12 | `src/syscall/types_windows.go` |
| io | 6026 | 1013 | 0 | `doc/go_spec.html` |
| crypto | 2 | 2 | 0 | `lib/hg/goreposum.py` |
| ipc | 6572 | 1014 | 0 | `src/internal/syscall/windows/zsyscall_windows.go` |
| time | 1739 | 403 | 0 | `src/encoding/json/v2/arshal_test.go` |
| serialization | 234 | 76 | 0 | `src/encoding/json/v2_diff_test.go` |
| regex | 593 | 176 | 0 | `src/regexp/example_test.go` |
| events | 685 | 169 | 0 | `test/fixedbugs/issue13273.go` |
| tests | 15880 | 1500 | 1 | `src/net/http/serve_test.go` |
| docs | 112402 | 9556 | 21 | `src/runtime/proc.go` |
| debt | 13048 | 2691 | 2 | `test/return.go` |
| mutation | 239874 | 7060 | 45 | `src/cmd/compile/internal/ssagen/ssa.go` |
| dead_code | 33926 | 5826 | 6 | `test/escape2.go` |
| credential | 216 | 34 | 0 | `src/crypto/x509/x509_test.go` |
| threat | 1421 | 97 | 0 | `src/math/rand/v2/chacha8_test.go` |
| ml_ai | 2694 | 342 | 0 | `src/cmd/asm/internal/asm/testdata/amd64enc_extra.s` |
| ui | 619 | 112 | 0 | `doc/go_spec.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `doc/go_spec.html` (Hits: 1452)
- `src/syscall/mkerrors.sh` (Hits: 567)
- `src/syscall/mkall.sh` (Hits: 77)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **runtime2.go** (`src/runtime/runtime2.go`) — 216 inbound connections
2. **alg.go** (`src/cmd/compile/internal/types/alg.go`) — 161 inbound connections
3. **base.go** (`src/cmd/compile/internal/base/base.go`) — 147 inbound connections
4. **ir.go** (`src/cmd/compile/internal/ir/ir.go`) — 125 inbound connections
5. **pos.go** (`src/cmd/internal/src/pos.go`) — 117 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **pkg.go** (`src/cmd/go/internal/load/pkg.go`) — 43 outbound dependencies
2. **acvp_test.go** (`src/crypto/internal/fips140test/acvp_test.go`) — 40 outbound dependencies
3. **main.go** (`src/cmd/vet/main.go`) — 39 outbound dependencies
4. **go_test.go** (`src/cmd/go/go_test.go`) — 38 outbound dependencies
5. **serve_test.go** (`src/net/http/serve_test.go`) — 38 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `f` **(Many-Argument Workhorses)** (@ `test/fixedbugs/issue60982.go`) -> Impact: **1839.7** | LOC: 2015
- `test` **(Compute Cores)** (@ `test/fixedbugs/issue2615.go`) -> Impact: **749.9** | LOC: 516
  * *Intent:* // test returns the index of the lowest set bit in a 256-bit vector.
- `main` **(Many-Argument Workhorses)** (@ `src/regexp/testdata/testregex.c`) -> Impact: **710.0** | LOC: 1071
- `ssaGenValue` **(Many-Argument Workhorses)** (@ `src/cmd/compile/internal/amd64/ssa.go`) -> Impact: **577.3** | LOC: 1674
- `Load` **(Many-Argument Workhorses)** (@ `src/cmd/link/internal/loadelf/ldelf.go`) -> Impact: **552.0** | LOC: 600
  * *Intent:* // Load loads the ELF file pn from f. // Symbols are installed into the loader, and a slice of the text symbols is returned. // // On ARM systems, Loa...
- `builtin` **(Many-Argument Workhorses)** (@ `src/cmd/compile/internal/types2/builtins.go`) -> Impact: **546.1** | LOC: 962
  * *Intent:* // builtin type-checks a call to the built-in specified by id and // reports whether the call is valid, with *x holding the result; // but x.expr is n...
- `regalloc` **(Many-Argument Workhorses)** (@ `src/cmd/compile/internal/ssa/regalloc.go`) -> Impact: **510.4** | LOC: 1242
- `ssaGenValue` **(Many-Argument Workhorses)** (@ `src/cmd/compile/internal/ppc64/ssa.go`) -> Impact: **418.7** | LOC: 1957
- `update` **(Many-Argument Workhorses)** (@ `src/cmd/compile/internal/ssa/prove.go`) -> Impact: **399.0** | LOC: 387
  * *Intent:* // update updates the set of relations between v and w in domain d // restricting it to r.
- `ssaGenValue` **(Many-Argument Workhorses)** (@ `src/cmd/compile/internal/arm64/ssa.go`) -> Impact: **398.9** | LOC: 1361

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/runtime` | 769 | 83439.85 | 14.88% | 48.09% |
| `src/cmd/compile/internal/ssa` | 116 | 27727.57 | 29.55% | 46.16% |
| `test` | 360 | 26428.84 | 6.93% | 0.0% |
| `src/net/http` | 70 | 26135.62 | 21.97% | 53.24% |
| `test/fixedbugs` | 1830 | 24946.08 | 2.58% | 0.0% |
| `src/net` | 229 | 24284.02 | 17.75% | 56.74% |
| `src/syscall` | 274 | 20703.84 | 13.97% | 33.13% |
| `src/cmd/link/internal/ld` | 54 | 18431.2 | 23.02% | 42.22% |
| `src/go/types` | 109 | 17907.84 | 22.42% | 56.7% |
| `src/cmd/compile/internal/types2` | 97 | 17594.46 | 25.28% | 59.12% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `misc/cgo/gmp/gmp.go` -> **100.0%** Exposure
- `src/builtin/builtin.go` -> **100.0%** Exposure
- `src/cmd/asm/internal/lex/slice.go` -> **100.0%** Exposure
- `src/cmd/cgo/doc.go` -> **100.0%** Exposure
- `src/cmd/cgo/internal/testout/testdata/aligned.go` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `lib/hg/goreposum.py` -> **100.0%** Exposure
- `src/runtime/runtime-gdb.py` -> **100.0%** Exposure
- `misc/cgo/gmp/pi.go` -> **100.0%** Exposure
- `src/archive/tar/common.go` -> **100.0%** Exposure
- `src/archive/tar/reader.go` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/escape2.go` -> **220** Orphaned Functions | **0** Duplicates
- `test/escape2n.go` -> **220** Orphaned Functions | **0** Duplicates
- `test/prove.go` -> **203** Orphaned Functions | **0** Duplicates
- `src/reflect/all_test.go` -> **191** Orphaned Functions | **0** Duplicates
- `src/net/http/serve_test.go` -> **185** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `src/crypto/tls/example_test.go` -> **100.0%** Exposure
- `src/crypto/x509/example_test.go` -> **100.0%** Exposure
- `src/crypto/x509/verify_test.go` -> **100.0%** Exposure
- `src/crypto/x509/x509_test.go` -> **100.0%** Exposure
- `src/encoding/pem/example_test.go` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `118` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `25306` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/cmd/compile/internal/ssagen/ssa.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.503)
- **Top Global Matches:** file_cluster_4: 6.503, file_cluster_6: 9.242, file_cluster_15: 13.322
- **Magnitude:** 5918.22 | **LOC:** 8115 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 18.8%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **29**; blast radius 0.134; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.5%), Guard Balance (formerly Safety Score) (69.2%)
- **Documentation Coverage:** 72.0833% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exprCheckPtr` **(Many-Argument Workhorses)** (Impact: 339.5)
  * `genssa` **(Many-Argument Workhorses)** (Impact: 271.5)
    * *Intent:* // genssa appends entries to pp for each instruction in f.
  * `stmt` **(Many-Argument Workhorses)** (Impact: 252.5)
    * *Intent:* // stmt converts the statement n to SSA and adds it to s.
  * `conv` **(Many-Argument Workhorses)** (Impact: 222.4)
  * `buildssa` **(Many-Argument Workhorses)** (Impact: 162.3)
    * *Intent:* // buildssa builds an SSA function for fn. // worker indicates which of the backend workers is doing...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 709 instances
* *State Mutation (weighted view):* 2361
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1481`, `structural_boundaries: 659`, `args: 197`, `func_start: 197`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 14`, `state_mutation: 943`, `dead_code: 24`, `planned_debt: 53`
* *Architecture:* `io: 2`, `api: 61`, `import: 1`
* *Defense:* `safety: 3`, `doc: 538`, `immutability_locks: 7`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.134
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.001788
  * `Imports (Out-Degree: 18):` bufio, bytes, abi, base, ir, liveness, objw, reflectdata...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/crypto/tls/testdata/example-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/platform_root_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/net/http/serve_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.264)
- **Top Global Matches:** file_cluster_10: 8.264, file_cluster_15: 8.398, file_cluster_12: 8.483
- **Magnitude:** 4455.76 | **LOC:** 7665 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **38**; blast radius 0.165; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Mutation Surface (formerly State Flux) (97.0%), Debt Markers (formerly Tech Debt) (87.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.6%)
- **Documentation Coverage:** 64.4248% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testServerConnState` **(Many-Argument Workhorses)** (Impact: 44.4)
  * `TestHeaderToWire` **(Compute Cores)** (Impact: 36.7)
    * *Intent:* // Tests regarding the ordering of Write, WriteHeader, Header, and // Flush calls. In Go 1.0, rw.Wri...
  * `testServerExpect` **(Many-Argument Workhorses)** (Impact: 34.1)
  * `testServerTimeoutsWithTimeout` **(Many-Argument Workhorses)** (Impact: 33.6)
  * `testIdentityResponse` **(Many-Argument Workhorses)** (Impact: 33.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 14 instances
* *Mitigated Memory Allocs:* 75 instances
* *Amplified Race Conditions:* 121 instances
* *Amplified Cascading Flux:* 296 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 771
* *Memory Alloc (weighted view):* 39
* *State Mutation (weighted view):* 959
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 899`, `structural_boundaries: 731`, `args: 341`, `func_start: 341`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 17`, `state_mutation: 367`, `planned_debt: 7`, `fragile_debt: 2`, `unreferenced_by_name: 185`
* *Architecture:* `io: 58`, `api: 225`, `concurrency: 166`, `import: 1`
* *Defense:* `safety: 286`, `doc: 255`, `test: 196`, `sync_locks: 34`, `immutability_locks: 26`, `cleanup: 171`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001679
  * `Imports (Out-Degree: 18):` bufio, bytes, gzip, zlib, context, rand, tls, x509...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/net/http/transport_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.424)
- **Top Global Matches:** file_cluster_10: 8.424, file_cluster_15: 8.554, file_cluster_4: 8.695
- **Magnitude:** 4195.9 | **LOC:** 7769 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **36**; blast radius 0.483; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.2%), Mutation Surface (formerly State Flux) (97.5%), Debt Markers (formerly Tech Debt) (74.5%), Guard Balance (formerly Safety Score) (53.2%)
- **Documentation Coverage:** 64.657% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testTransportEventTrace` **(Many-Argument Workhorses)** (Impact: 57.0)
  * `testTransportGzip` **(Many-Argument Workhorses)** (Impact: 44.5)
  * `testSOCKS5Proxy` **(Defensive Guards)** (Impact: 39.8)
  * `testTransportRequestWriteRoundTrip` **(Many-Argument Workhorses)** (Impact: 34.3)
  * `TestOnProxyConnectResponse` **(Defensive Guards)** (Impact: 33.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Mitigated Memory Allocs:* 72 instances
* *Amplified Race Conditions:* 98 instances
* *Amplified Cascading Flux:* 307 instances
* *High Risk Execution (weighted view):* 8
* *Concurrency (weighted view):* 650
* *Memory Alloc (weighted view):* 42
* *State Mutation (weighted view):* 1008
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 851`, `structural_boundaries: 727`, `args: 299`, `func_start: 299`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 15`, `state_mutation: 394`, `planned_debt: 7`, `fragile_debt: 4`, `unreferenced_by_name: 146`
* *Architecture:* `io: 58`, `api: 180`, `concurrency: 160`, `import: 1`
* *Defense:* `safety: 250`, `doc: 247`, `test: 161`, `sync_locks: 105`, `immutability_locks: 31`, `cleanup: 158`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.483
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001819
  * `Imports (Out-Degree: 16):` bufio, bytes, gzip, context, rand, tls, x509, binary...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/reflect/all_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.383)
- **Top Global Matches:** file_cluster_4: 9.383, file_cluster_15: 9.807, file_cluster_10: 10.11
- **Magnitude:** 4147.36 | **LOC:** 8840 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.05; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.3%), Concurrency Surface (formerly Concurrency) (88.4%), Debt Markers (formerly Tech Debt) (81.5%), Guard Balance (formerly Safety Score) (56.9%)
- **Documentation Coverage:** 86.8601% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestSelect` **(Compute Cores)** (Impact: 92.0)
  * `TestChan` **(Compute Cores)** (Impact: 49.0)
  * `TestMethod` **(I/O & Config Routines)** (Impact: 41.6)
  * `TestConvert` **(Compute Cores)** (Impact: 39.7)
  * `TestMethodValue` **(Compute Cores)** (Impact: 33.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Race Conditions:* 62 instances
* *Amplified Cascading Flux:* 370 instances
* *High Risk Execution (weighted view):* 10
* *Concurrency (weighted view):* 390
* *Memory Alloc (weighted view):* 167
* *State Mutation (weighted view):* 1214
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 863`, `structural_boundaries: 1122`, `args: 276`, `func_start: 276`, `class_start: 145`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 14`, `state_mutation: 474`, `dead_code: 5`, `planned_debt: 8`, `fragile_debt: 2`, `unreferenced_by_name: 191`
* *Architecture:* `io: 13`, `api: 437`, `concurrency: 80`, `import: 1`
* *Defense:* `safety: 29`, `doc: 231`, `test: 206`, `sync_locks: 9`, `immutability_locks: 18`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` bytes, base64, flag, fmt, token, asan, goarch, msan...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/runtime/proc.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.536)
- **Top Global Matches:** file_cluster_4: 7.536, file_cluster_15: 10.354, file_cluster_16: 10.939
- **Magnitude:** 3697.46 | **LOC:** 8177 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 29.4%
- **Blast Radius:** changing it is visible to **68** in-repo importer(s); it depends on **11**; blast radius 2.533; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (72.4%), Guard Balance (formerly Safety Score) (64.8%)
- **Documentation Coverage:** 25.4045% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sigprof` **(Many-Argument Workhorses)** (Impact: 113.6)
    * *Intent:* // Called if we receive a SIGPROF signal. // Called by the signal handler, may run during STW. // //...
  * `findRunnable` **(I/O & Config Routines)** (Impact: 101.5)
    * *Intent:* // Finds a runnable goroutine to execute. // Tries to steal from other P's, get g from local or glob...
  * `casgstatus` **(Many-Argument Workhorses)** (Impact: 63.4)
    * *Intent:* // If asked to move to or from a Gscanstatus this will throw. Use the castogscanstatus // and casfro...
  * `procresize` **(Many-Argument Workhorses)** (Impact: 52.1)
    * *Intent:* // Change number of processors. // // sched.lock must be held, and the world must be stopped. // // ...
  * `newproc1` **(Many-Argument Workhorses)** (Impact: 47.4)
    * *Intent:* // Create a new g in state _Grunnable (or _Gwaiting if parked is true), starting at fn. // callerpc ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 489 instances
* *Concurrency (weighted view):* 20
* *State Mutation (weighted view):* 1555
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 975`, `structural_boundaries: 294`, `args: 245`, `func_start: 245`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 3`, `state_mutation: 577`, `dead_code: 1`, `planned_debt: 11`, `fragile_debt: 1`, `unreferenced_by_name: 58`
* *Architecture:* `api: 6`, `concurrency: 5`, `import: 1`
* *Defense:* `doc: 908`, `sync_locks: 52`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.533
  * `Choke Point (Betweenness):` 4.8e-05 | `Ripple Effect (Closeness):` 0.012085
  * `Imports (Out-Degree: 35):` abi, cpu, goarch, goexperiment, goos, atomic, exithook, sys...
  * `Imported By (In-Degree: 68):` (Excluded from Brief to save tokens)

### `src/database/sql/sql_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.726)
- **Top Global Matches:** file_cluster_12: 7.726, file_cluster_15: 8.178, file_cluster_10: 8.345
- **Magnitude:** 3291.62 | **LOC:** 5413 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.05; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Debt Markers (formerly Tech Debt) (84.4%), Concurrency Surface (formerly Concurrency) (67.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.4%)
- **Documentation Coverage:** 78.9238% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testManyErrBadConn` **(Defensive Guards)** (Impact: 42.1)
  * `testContextCancelDuringRawBytesScan` **(Many-Argument Workhorses)** (Impact: 41.8)
    * *Intent:* // From go.dev/issue/60304
  * `testMaxOpenConns` **(Compute Cores)** (Impact: 31.1)
  * `TestConnRequestSet` **(Compute Cores)** (Impact: 29.8)
  * `testStmtCloseDeps` **(Compute Cores)** (Impact: 25.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 11 instances
* *Amplified Race Conditions:* 34 instances
* *Amplified Cascading Flux:* 375 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 223
* *Memory Alloc (weighted view):* 36
* *State Mutation (weighted view):* 1158
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 693`, `structural_boundaries: 457`, `args: 285`, `func_start: 285`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 5`, `state_mutation: 408`, `planned_debt: 6`, `fragile_debt: 1`, `unreferenced_by_name: 121`
* *Architecture:* `io: 1`, `api: 155`, `concurrency: 53`, `import: 1`
* *Defense:* `safety: 286`, `doc: 135`, `test: 125`, `sync_locks: 46`, `immutability_locks: 11`, `cleanup: 118`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` bytes, context, driver, errors, fmt, race, testenv, rand...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cmd/go/internal/load/pkg.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.376)
- **Top Global Matches:** file_cluster_6: 6.376, file_cluster_4: 8.548, file_cluster_15: 16.467
- **Magnitude:** 3074.38 | **LOC:** 3619 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **43**; blast radius 0.107; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.3%), Connectivity (formerly Api Exposure) (54.0%)
- **Documentation Coverage:** 46.3087% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load` **(Many-Argument Workhorses)** (Impact: 303.8)
    * *Intent:* // load populates p using information from bp, err, which should // be the result of calling build.C...
  * `setBuildInfo` **(Many-Argument Workhorses)** (Impact: 172.7)
    * *Intent:* // setBuildInfo gathers build information and sets it into // p.Internal.BuildInfo, which will later...
  * `loadPackageData` **(Many-Argument Workhorses)** (Impact: 155.2)
    * *Intent:* // loadPackageData loads information needed to construct a *Package. The result // is cached, and la...
  * `loadImport` **(Many-Argument Workhorses)** (Impact: 92.1)
    * *Intent:* // loadImport scans the directory named by path, which must be an import path, // but possibly a loc...
  * `resolveEmbed` **(Many-Argument Workhorses)** (Impact: 87.8)
    * *Intent:* // resolveEmbed resolves //go:embed patterns to precise file lists. // It sets files to the list of ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 329 instances
* *High Risk Execution (weighted view):* 7
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 1009
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 702`, `structural_boundaries: 458`, `args: 89`, `func_start: 89`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 11`, `state_mutation: 351`, `planned_debt: 20`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `api: 172`, `concurrency: 11`, `import: 1`
* *Defense:* `safety: 44`, `doc: 335`, `test: 20`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000341
  * `Imports (Out-Degree: 23):` bytes, base, cfg, fips140, fsys, gover, imports, modfetch...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/cmd/cgo/gcc.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.083)
- **Top Global Matches:** file_cluster_6: 6.083, file_cluster_4: 12.54, file_cluster_8: 12.688
- **Magnitude:** 2801.78 | **LOC:** 3581 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **24**; blast radius 0.224; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.3%), Debt Markers (formerly Tech Debt) (43.3%)
- **Documentation Coverage:** 44.8276% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadType` **(Many-Argument Workhorses)** (Impact: 273.4)
    * *Intent:* // loadType recursively loads the requested dtype and its dependency graph.
  * `gccDebug` **(Many-Argument Workhorses)** (Impact: 254.3)
    * *Intent:* // gccDebug runs gcc -gdwarf-2 over the C program stdin and // returns the corresponding DWARF data ...
  * `guessKinds` **(Compute Cores)** (Impact: 85.5)
    * *Intent:* // guessKinds tricks gcc into revealing the kind of each // name xxx for the references C.xxx in the...
  * `rewriteCall` **(Many-Argument Workhorses)** (Impact: 73.9)
    * *Intent:* // rewriteCall rewrites one call to add pointer checks. // If any pointer checks are required, we re...
  * `hasPointer` **(Many-Argument Workhorses)** (Impact: 66.2)
    * *Intent:* // hasPointer is used by needsPointerCheck. If top is true it returns // whether t is or contains a ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 365 instances
* *Memory Alloc (weighted view):* 32
* *State Mutation (weighted view):* 1129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 788`, `structural_boundaries: 431`, `args: 68`, `func_start: 68`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 399`, `dead_code: 2`, `planned_debt: 8`, `fragile_debt: 18`, `unreferenced_by_name: 8`
* *Architecture:* `api: 13`, `import: 1`
* *Defense:* `safety: 9`, `doc: 249`, `sync_locks: 1`, `immutability_locks: 10`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000327
  * `Imports (Out-Degree: 4):` bytes, quoted, dwarf, elf, macho, pe, binary, errors...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/cmd/compile/internal/amd64/ssa.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.77)
- **Top Global Matches:** file_cluster_4: 6.77, file_cluster_15: 9.228, file_cluster_16: 10.526
- **Magnitude:** 2750.12 | **LOC:** 2582 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 42.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.05; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.9%), Debt Markers (formerly Tech Debt) (80.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 33.871% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ssaGenValue` **(Many-Argument Workhorses)** (Impact: 577.3)
  * `moveByRegsWidth` **(Many-Argument Workhorses)** (Impact: 46.4)
    * *Intent:* // moveByRegsWidth returns the reg->reg move instruction of the given dest/src registers of a given ...
  * `ssaGenBlock` **(Many-Argument Workhorses)** (Impact: 36.7)
  * `storeByRegWidth` **(Compute Cores)** (Impact: 29.5)
    * *Intent:* // storeByRegWidth returns the store instruction of the given register of a given width. // It's als...
  * `ssaMarkMoves` **(Compute Cores)** (Impact: 18.4)
    * *Intent:* // ssaMarkMoves marks any MOVXconst ops that need to avoid clobbering flags.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 534 instances
* *State Mutation (weighted view):* 1832
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 369`, `structural_boundaries: 104`, `args: 62`, `func_start: 62`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 764`, `dead_code: 1`, `planned_debt: 11`, `fragile_debt: 4`, `unreferenced_by_name: 44`
* *Architecture:* `import: 1`
* *Defense:* `doc: 160`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` base, ir, logopt, objw, ssa, ssagen, types, obj...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cmd/link/internal/ld/data.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.629)
- **Top Global Matches:** file_cluster_6: 6.629, file_cluster_4: 12.088, file_cluster_8: 13.815
- **Magnitude:** 2662.42 | **LOC:** 3437 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **20**; blast radius 0.173; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.1%), Guard Balance (formerly Safety Score) (71.7%), Complexity Load (formerly Cognitive Load) (52.0%)
- **Documentation Coverage:** 73.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `relocsym` **(Many-Argument Workhorses)** (Impact: 351.4)
    * *Intent:* // The main loop walks through the list of relocations attached to "s" // and resolves them where ap...
  * `dodataSect` **(Many-Argument Workhorses)** (Impact: 143.2)
  * `allocateDataSections` **(Many-Argument Workhorses)** (Impact: 93.2)
    * *Intent:* // allocateDataSections allocates sym.Section objects for data/rodata // (and related) symbols, and ...
  * `address` **(I/O & Config Routines)** (Impact: 77.8)
    * *Intent:* // address assigns virtual addresses to all segments and sections and // returns all segments in fil...
  * `extreloc` **(Many-Argument Workhorses)** (Impact: 70.0)
    * *Intent:* // Convert a Go relocation to an external relocation.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 362 instances
* *High Risk Execution (weighted view):* 8
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 1120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 702`, `structural_boundaries: 251`, `args: 65`, `func_start: 65`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 13`, `state_mutation: 396`, `planned_debt: 11`, `fragile_debt: 3`, `unreferenced_by_name: 20`
* *Architecture:* `api: 12`, `concurrency: 4`, `import: 1`
* *Defense:* `safety: 7`, `doc: 238`, `sync_locks: 1`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.173
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.002192
  * `Imports (Out-Degree: 18):` bytes, gcprog, objabi, sys, loader, loadpe, sym, zlib...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/sync/atomic/atomic_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.056)
- **Top Global Matches:** file_cluster_9: 8.056, file_cluster_15: 8.447, file_cluster_16: 9.087
- **Magnitude:** 2645.76 | **LOC:** 3001 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.05; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (79.5%), Guard Balance (formerly Safety Score) (70.4%), Debt Markers (formerly Tech Debt) (66.4%)
- **Documentation Coverage:** 97.4026% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestStoreLoadSeqCst32` **(Compute Cores)** (Impact: 20.4)
  * `TestStoreLoadSeqCst64` **(Compute Cores)** (Impact: 20.4)
  * `TestStoreLoadRelAcq32` **(Type Conversions)** (Impact: 17.8)
  * `TestStoreLoadRelAcq64` **(Type Conversions)** (Impact: 17.8)
  * `testCompareAndSwapUint64` **(Many-Argument Workhorses)** (Impact: 15.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 403 instances
* *Concurrency (weighted view):* 84
* *State Mutation (weighted view):* 1218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 571`, `structural_boundaries: 147`, `args: 141`, `func_start: 141`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 12`, `state_mutation: 412`, `unreferenced_by_name: 88`
* *Architecture:* `api: 94`, `concurrency: 14`, `import: 1`
* *Defense:* `safety: 6`, `doc: 19`, `test: 88`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fmt, reflect, runtime, debug, strings, atomic, testing, unsafe
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/prove.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.352)
- **Top Global Matches:** file_cluster_12: 8.352, file_cluster_15: 8.562, file_cluster_4: 9.961
- **Magnitude:** 2624.68 | **LOC:** 2901 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 56.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.05; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (85.7%), Guard Balance (formerly Safety Score) (64.9%), Complexity Load (formerly Cognitive Load) (16.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.0%)
- **Documentation Coverage:** 43.6939% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rightShiftBounds` **(Compute Cores)** (Impact: 87.6)
  * `unsignedRightShiftBounds` **(Compute Cores)** (Impact: 30.3)
  * `transitiveProofsThroughNonOverflowingSignedAddNegative` **(Compute Cores)** (Impact: 29.8)
  * `f13a` **(Many-Argument Workhorses)** (Impact: 28.4)
  * `issue75144if2` **(Many-Argument Workhorses)** (Impact: 23.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 247 instances
* *State Mutation (weighted view):* 772
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 735`, `structural_boundaries: 513`, `args: 213`, `func_start: 213`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 2`, `state_mutation: 278`, `planned_debt: 2`, `unreferenced_by_name: 203`
* *Architecture:* `import: 1`
* *Defense:* `doc: 485`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` math, bits
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cmd/go/internal/work/exec.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.103)
- **Top Global Matches:** file_cluster_6: 6.103, file_cluster_4: 12.248, file_cluster_8: 13.009
- **Magnitude:** 2598.16 | **LOC:** 3703 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **37**; blast radius 0.137; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.3%), Complexity Load (formerly Cognitive Load) (50.8%)
- **Documentation Coverage:** 68.1034% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build` **(Many-Argument Workhorses)** (Impact: 149.3)
    * *Intent:* // build is the action for building a single package. // Note that any new influence on this logic m...
  * `Do` **(Many-Argument Workhorses)** (Impact: 83.8)
    * *Intent:* // Do runs the action graph rooted at root.
  * `processCgoOutputs` **(Many-Argument Workhorses)** (Impact: 74.0)
  * `checkCacheForBuild` **(Many-Argument Workhorses)** (Impact: 70.0)
    * *Intent:* // checkCacheForBuild checks the cache for the outputs of the buildAction to determine // what work ...
  * `runCgo` **(Many-Argument Workhorses)** (Impact: 68.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 309 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 18
* *Memory Alloc (weighted view):* 17
* *State Mutation (weighted view):* 932
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 684`, `structural_boundaries: 485`, `args: 95`, `func_start: 95`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 9`, `state_mutation: 314`, `planned_debt: 18`, `fragile_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `io: 12`, `api: 34`, `concurrency: 3`, `import: 1`
* *Defense:* `safety: 123`, `doc: 254`, `test: 1`, `sync_locks: 11`, `immutability_locks: 6`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.137
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.001563
  * `Imports (Out-Degree: 21):` bytes, base, cache, cfg, fsys, gover, load, modload...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/cmd/compile/internal/ssa/regalloc.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.631)
- **Top Global Matches:** file_cluster_6: 6.631, file_cluster_4: 9.957, file_cluster_8: 16.149
- **Magnitude:** 2527.16 | **LOC:** 3520 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 0.068; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.2%), Complexity Load (formerly Cognitive Load) (51.8%)
- **Documentation Coverage:** 42.5926% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `regalloc` **(Many-Argument Workhorses)** (Impact: 510.4)
  * `processDest` **(Many-Argument Workhorses)** (Impact: 87.8)
    * *Intent:* // processDest generates code to put value vid into location loc. Returns true // if progress was ma...
  * `init` **(Compute Cores)** (Impact: 84.7)
  * `computeLive` **(I/O & Config Routines)** (Impact: 84.7)
    * *Intent:* // computeLive computes a map from block ID to a list of value IDs live at the end // of that block....
  * `allocValToReg` **(Many-Argument Workhorses)** (Impact: 63.7)
    * *Intent:* // allocValToReg allocates v to a register selected from regMask and // returns the register copy of...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 383 instances
* *State Mutation (weighted view):* 1164
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 741`, `structural_boundaries: 364`, `args: 51`, `func_start: 51`, `class_start: 13`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 398`, `planned_debt: 26`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `doc: 331`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.068
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000262
  * `Imports (Out-Degree: 14):` base, ir, types, src, sys, cmp, fmt, buildcfg...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/cmd/compile/internal/ssa/prove.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.702)
- **Top Global Matches:** file_cluster_6: 6.702, file_cluster_4: 9.406, file_cluster_8: 16.642
- **Magnitude:** 2502.34 | **LOC:** 3186 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 61.5%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 0.122; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.7%)
- **Documentation Coverage:** 40.3614% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Many-Argument Workhorses)** (Impact: 399.0)
    * *Intent:* // update updates the set of relations between v and w in domain d // restricting it to r.
  * `simplifyBlock` **(Many-Argument Workhorses)** (Impact: 244.8)
    * *Intent:* // simplifyBlock simplifies some constant values in b and evaluates // branches to non-uniquely domi...
  * `newLimit` **(Many-Argument Workhorses)** (Impact: 127.6)
    * *Intent:* // newLimit adds new limiting information for v.
  * `addLocalFacts` **(Many-Argument Workhorses)** (Impact: 107.5)
  * `checkForChunkedIndexBounds` **(Many-Argument Workhorses)** (Impact: 64.5)
    * *Intent:* // checkForChunkedIndexBounds looks for index expressions of the form // A[i+delta] where delta < K ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 236 instances
* *State Mutation (weighted view):* 727
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 791`, `structural_boundaries: 237`, `args: 79`, `func_start: 79`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 10`, `state_mutation: 255`, `dead_code: 10`, `planned_debt: 18`, `fragile_debt: 2`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 1`, `doc: 160`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000315
  * `Imports (Out-Degree: 12):` types, src, cmp, fmt, math, bits, slices, strings
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/math/all_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.875)
- **Top Global Matches:** file_cluster_15: 6.875, file_cluster_16: 8.103, file_cluster_2: 8.224
- **Magnitude:** 2423.48 | **LOC:** 4021 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.05; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (82.5%), Guard Balance (formerly Safety Score) (63.7%), Complexity Load (formerly Cognitive Load) (46.4%)
- **Documentation Coverage:** 98.0583% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestGamma` **(Compute Cores)** (Impact: 19.4)
  * `TestLdexp` **(Compute Cores)** (Impact: 16.9)
  * `TestRemainder` **(I/O & Config Routines)** (Impact: 15.6)
  * `TestFrexp` **(Compute Cores)** (Impact: 15.0)
  * `testExp2` **(Many-Argument Workhorses)** (Impact: 14.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 398 instances
* *State Mutation (weighted view):* 1196
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 421`, `structural_boundaries: 28`, `args: 160`, `func_start: 160`, `class_start: 2`
* *Risk/State:* `state_mutation: 400`, `unreferenced_by_name: 149`
* *Architecture:* `api: 234`, `import: 1`
* *Defense:* `doc: 38`, `test: 149`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` fmt, math, testing, unsafe
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cmd/compile/internal/syntax/parser.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.809)
- **Top Global Matches:** file_cluster_6: 6.809, file_cluster_4: 8.477, file_cluster_15: 16.133
- **Magnitude:** 2422.18 | **LOC:** 2901 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 0.997; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.7%), Complexity Load (formerly Cognitive Load) (41.0%)
- **Documentation Coverage:** 47.1264% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `paramList` **(Many-Argument Workhorses)** (Impact: 114.4)
    * *Intent:* // Parameters = "(" [ ParameterList [ "," ] ] ")" . // ParameterList = ParameterDecl { "," Parameter...
  * `pexpr` **(Many-Argument Workhorses)** (Impact: 71.7)
    * *Intent:* // Conversion | // PrimaryExpr Selector | // PrimaryExpr Index | // PrimaryExpr Slice | // PrimaryEx...
  * `paramDeclOrNil` **(Compute Cores)** (Impact: 65.4)
    * *Intent:* // ParameterDecl = [ IdentifierList ] [ "..." ] Type .
  * `simpleStmt` **(Many-Argument Workhorses)** (Impact: 49.8)
    * *Intent:* // ---------------------------------------------------------------------------- // Statements // Sim...
  * `header` **(Compute Cores)** (Impact: 47.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 416 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 1280
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 565`, `structural_boundaries: 299`, `args: 85`, `func_start: 85`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 8`, `state_mutation: 448`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 2`, `import: 1`
* *Defense:* `safety: 1`, `doc: 132`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.997
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.003641
  * `Imports (Out-Degree: 6):` fmt, constraint, io, strconv, strings
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/os/os_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.269)
- **Top Global Matches:** file_cluster_4: 6.269, file_cluster_6: 9.842, file_cluster_9: 12.265
- **Magnitude:** 2416.56 | **LOC:** 4083 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.05; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.5%), Debt Markers (formerly Tech Debt) (89.2%), Concurrency Surface (formerly Concurrency) (50.0%), Guard Balance (formerly Safety Score) (48.2%)
- **Documentation Coverage:** 83.8843% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testChtimesOmit` **(Many-Argument Workhorses)** (Impact: 60.8)
  * `TestCopyFSWithSymlinks` **(Defensive Guards)** (Impact: 50.6)
  * `verifyCopyFS` **(Many-Argument Workhorses)** (Impact: 40.5)
    * *Intent:* // verifyCopyFS checks the content and permission of each file inside copied FS to ensure // the cop...
  * `testOpenError` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `testHardLink` **(Many-Argument Workhorses)** (Impact: 34.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 12 instances
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 192 instances
* *Concurrency (weighted view):* 88
* *Memory Alloc (weighted view):* 13
* *State Mutation (weighted view):* 580
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 776`, `structural_boundaries: 229`, `args: 138`, `func_start: 138`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 196`, `planned_debt: 4`, `fragile_debt: 1`, `unreferenced_by_name: 104`
* *Architecture:* `io: 5`, `api: 104`, `concurrency: 18`, `import: 1`
* *Defense:* `safety: 298`, `doc: 113`, `test: 136`, `immutability_locks: 14`, `cleanup: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` bytes, errors, flag, fmt, testenv, io, fs, log...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cmd/compile/internal/ppc64/ssa.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 10.966)
- **Top Global Matches:** file_cluster_3: 10.966, file_cluster_8: 13.661, file_cluster_6: 26.332
- **Magnitude:** 2405.02 | **LOC:** 2152 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.05; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (48.2%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ssaGenValue` **(Many-Argument Workhorses)** (Impact: 418.7)
  * `ssaGenBlock` **(Many-Argument Workhorses)** (Impact: 38.5)
  * `loadByType` **(Compute Cores)** (Impact: 25.7)
    * *Intent:* // loadByType returns the load instruction of the given type.
  * `storeByType` **(Compute Cores)** (Impact: 16.7)
    * *Intent:* // storeByType returns the store instruction of the given type.
  * `spillArgReg` **(Many-Argument Workhorses)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 525 instances
* *State Mutation (weighted view):* 1866
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 27`, `args: 7`, `func_start: 7`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 816`, `dead_code: 6`, `planned_debt: 5`, `unreferenced_by_name: 5`
* *Architecture:* `import: 1`
* *Defense:* `doc: 222`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` base, ir, logopt, objw, ssa, ssagen, types, obj...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/net/http/internal/http2/transport_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.177)
- **Top Global Matches:** file_cluster_10: 7.177, file_cluster_15: 7.251, file_cluster_12: 8.157
- **Magnitude:** 2299.62 | **LOC:** 5517 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 90.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.05; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (96.2%), Mutation Surface (formerly State Flux) (90.0%), Concurrency Surface (formerly Concurrency) (71.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.6%)
- **Documentation Coverage:** 72.009% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testTransportResPatternBubble` **(Many-Argument Workhorses)** (Impact: 28.4)
  * `testTransportReturnsUnusedFlowControl` **(Many-Argument Workhorses)** (Impact: 22.6)
  * `testTransportGetGotConnHooks` **(Many-Argument Workhorses)** (Impact: 21.7)
  * `TestTransport` **(Defensive Guards)** (Impact: 21.3)
  * `TestDialRaceResumesDial` **(Defensive Guards)** (Impact: 21.1)
    * *Intent:* // TestDialRaceResumesDial tests that, given two concurrent requests // to the same address, when th...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 26 instances
* *Amplified Race Conditions:* 27 instances
* *Amplified Cascading Flux:* 158 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 191
* *Memory Alloc (weighted view):* 22
* *State Mutation (weighted view):* 537
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 449`, `structural_boundaries: 304`, `args: 263`, `func_start: 263`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 4`, `state_mutation: 221`, `planned_debt: 6`, `fragile_debt: 4`, `unreferenced_by_name: 163`
* *Architecture:* `io: 28`, `api: 181`, `concurrency: 56`, `import: 1`
* *Defense:* `safety: 108`, `doc: 244`, `test: 167`, `sync_locks: 17`, `immutability_locks: 36`, `cleanup: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` bufio, bytes, gzip, context, rand, tls, hex, errors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cmd/compile/internal/noder/reader.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.638)
- **Top Global Matches:** file_cluster_4: 7.638, file_cluster_15: 10.224, file_cluster_16: 10.701
- **Magnitude:** 2267.26 | **LOC:** 4149 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **21**; blast radius 0.066; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.6%)
- **Documentation Coverage:** 90.9774% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expr` **(I/O & Config Routines)** (Impact: 126.0)
    * *Intent:* // @@@ Expressions // expr reads and returns a typechecked expression.
  * `objIdxMayFail` **(Many-Argument Workhorses)** (Impact: 93.9)
    * *Intent:* // objIdxMayFail is equivalent to objIdx, but returns an error rather than // failing the build if t...
  * `stmt1` **(Many-Argument Workhorses)** (Impact: 48.6)
  * `unifiedInlineCall` **(Many-Argument Workhorses)** (Impact: 48.0)
    * *Intent:* // unifiedInlineCall implements inline.NewInline by re-reading the function // body from its Unified...
  * `objDictIdx` **(Many-Argument Workhorses)** (Impact: 38.3)
    * *Intent:* // objDictIdx reads and returns the specified object dictionary.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 316 instances
* *State Mutation (weighted view):* 976
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 581`, `structural_boundaries: 354`, `args: 132`, `func_start: 132`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 7`, `state_mutation: 344`, `dead_code: 7`, `planned_debt: 44`, `fragile_debt: 4`, `unreferenced_by_name: 4`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 3`, `doc: 140`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000262
  * `Imports (Out-Degree: 17):` base, dwarfgen, inline, interleaved, ir, objw, reflectdata, staticinit...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/net/http/internal/http2/transport.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.739)
- **Top Global Matches:** file_cluster_4: 6.739, file_cluster_15: 10.749, file_cluster_10: 10.981
- **Magnitude:** 2206.84 | **LOC:** 3353 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **29**; blast radius 0.185; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.4%), Complexity Load (formerly Cognitive Load) (52.7%)
- **Documentation Coverage:** 81.0345% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeRequest` **(Many-Argument Workhorses)** (Impact: 83.4)
    * *Intent:* // writeRequest sends a request. // // It returns nil after the request is written, the response rea...
  * `handleResponse` **(Many-Argument Workhorses)** (Impact: 76.1)
    * *Intent:* // may return error types nil, or ConnectionError. Any other error value // is a StreamError of type...
  * `writeRequestBody` **(Compute Cores)** (Impact: 47.6)
  * `cleanupWriteRequest` **(Compute Cores)** (Impact: 44.7)
    * *Intent:* // cleanupWriteRequest performs post-request tasks. // // If err (the result of writeRequest) is non...
  * `roundTrip` **(Many-Argument Workhorses)** (Impact: 38.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Race Conditions:* 32 instances
* *Amplified Cascading Flux:* 254 instances
* *Concurrency (weighted view):* 212
* *Memory Alloc (weighted view):* 21
* *State Mutation (weighted view):* 788
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 534`, `structural_boundaries: 433`, `args: 137`, `func_start: 137`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 280`, `planned_debt: 16`, `unreferenced_by_name: 19`
* *Architecture:* `io: 11`, `api: 72`, `concurrency: 52`, `import: 1`
* *Defense:* `safety: 51`, `doc: 211`, `sync_locks: 135`, `immutability_locks: 3`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000763
  * `Imports (Out-Degree: 10):` bufio, bytes, flate, gzip, context, rand, tls, errors...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/runtime/chan_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.786)
- **Top Global Matches:** file_cluster_6: 8.786, file_cluster_4: 9.052, file_cluster_9: 15.343
- **Magnitude:** 2196.8 | **LOC:** 1221 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.05; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.4%), Debt Markers (formerly Tech Debt) (72.0%)
- **Documentation Coverage:** 47.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestChan` **(Compute Cores)** (Impact: 72.9)
  * `TestSelectStress` **(Compute Cores)** (Impact: 40.0)
  * `TestSelectFairness` **(Compute Cores)** (Impact: 29.8)
  * `BenchmarkSelectProdCons` **(Compute Cores)** (Impact: 27.0)
  * `TestSelfSelect` **(Compute Cores)** (Impact: 25.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 150 instances
* *Amplified Cascading Flux:* 244 instances
* *Concurrency (weighted view):* 903
* *State Mutation (weighted view):* 732
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 195`, `args: 39`, `func_start: 39`, `class_start: 3`
* *Risk/State:* `state_mutation: 244`, `unreferenced_by_name: 36`
* *Architecture:* `api: 37`, `concurrency: 153`, `import: 1`
* *Defense:* `doc: 40`, `test: 36`, `sync_locks: 9`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` testenv, math, runtime, sync, atomic, testing, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/internal/fmtsort/sort_test.go` (GO) | Magnitude: 125.82 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 217, structural_boundaries: 60, reflection_metaprogramming: 45, branch: 33
- `src/container/heap/example_intheap_test.go` (GO) | Magnitude: 20.96 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 15, api: 7, structural_boundaries: 6, args: 6
- `src/runtime/secret/secret.go` (GO) | Magnitude: 23.82 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 23, doc: 22, args: 7, func_start: 7
- `test/typeparam/mdempsky/2.go` (GO) | Magnitude: 4.42 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 5, structural_boundaries: 3, args: 2, func_start: 2
- `test/typeparam/issue48454.dir/a.go` (GO) | Magnitude: 3.28 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 3, api: 2, doc: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `test/ken/rob2.go` (GO) | Magnitude: 259.3 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 179, branch: 52, state_mutation: 52, core_var_decl: 39
- `src/cmd/cgo/internal/swig/swig_test.go` (GO) | Magnitude: 92.34 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 113, branch: 22, structural_boundaries: 10, state_mutation: 10
- `src/time/internal_test.go` (GO) | Magnitude: 24.56 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 18, doc: 9, core_var_decl: 8, state_mutation: 7
- `src/runtime/mstats.go` (GO) | Magnitude: 263.74 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 327, doc: 164, state_mutation: 79, api: 51
- `src/cmd/compile/internal/importer/ureader.go` (GO) | Magnitude: 268.04 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 369, structural_boundaries: 88, branch: 69, state_mutation: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/syscall/pwd_plan9.go` (GO) | Magnitude: 46.06 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 61, structural_boundaries: 22, branch: 13, sync_locks: 7
- `test/interface/pointer.go` (GO) | Magnitude: 9.44 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 10, indent_tabs: 10, doc: 6, pointers: 6
- `src/internal/syscall/windows/syscall_windows.go` (GO) | Magnitude: 424.36 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 322, api: 254, globals: 94, core_var_decl: 82
- `test/fixedbugs/issue4518.go` (GO) | Magnitude: 26.3 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 28, structural_boundaries: 14, branch: 10, args: 8
- `test/chan/select.go` (GO) | Magnitude: 57.4 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 35, branch: 9, state_mutation: 8, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/cmd/internal/pgo/serialize_test.go` (GO) | Magnitude: 74.88 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 139, branch: 21, structural_boundaries: 20, explicit_casts: 8
- `test/literal.go` (GO) | Magnitude: 19.2 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 177, core_var_decl: 97, design_snake_case: 95, branch: 3
- `src/internal/types/testdata/check/methodsets.go` (GO) | Magnitude: 0.03 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 134, pointers: 40, closures: 23, core_var_decl: 13
- `src/net/http/internal/http2/config_test.go` (GO) | Magnitude: 30.72 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 71, bitwise_ops: 10, args: 8, func_start: 8
- `src/internal/types/testdata/check/cycles2.go` (GO) | Magnitude: 0.02 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 29, structural_boundaries: 28, api: 13, class_start: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/plugin/plugin_test.go` (GO) | Magnitude: 2.74 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, indent_tabs: 2, args: 1
- `src/runtime/stubs_amd64.go` (GO) | Magnitude: 33.22 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: args: 29, func_start: 29, encapsulation: 29, unreferenced_by_name: 29
- `src/cmd/cgo/internal/test/issue24161e1/main.go` (GO) | Magnitude: 7.0 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 6, structural_boundaries: 3, args: 3, func_start: 3
- `src/regexp/exec2_test.go` (GO) | Magnitude: 4.3 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 5, doc: 3, structural_boundaries: 2, test: 2
- `src/math/example_test.go` (GO) | Magnitude: 85.76 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 70, scientific: 50, debug_prints: 47, args: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `test/typeparam/builtins.go` (GO) | Magnitude: 89.78 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 61, indent_tabs: 38, api: 18, safety_bypasses: 16
- `test/fixedbugs/bug462.go` (GO) | Magnitude: 2.42 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 4, doc: 3, safety_bypasses: 2
- `test/fixedbugs/issue14321.go` (GO) | Magnitude: 8.68 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 7, doc: 7, api: 5, indent_tabs: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/io/fs/stat.go` (GO) | Magnitude: 9.12 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 11, structural_boundaries: 7, doc: 6, api: 3
- `src/bytes/example_test.go` (GO) | Magnitude: 232.12 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 275, explicit_casts: 189, debug_prints: 126, args: 69
- `src/crypto/internal/fips140/aes/aes.go` (GO) | Magnitude: 0.66 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 54, branch: 13, structural_boundaries: 13, api: 11
- `src/net/http/httputil/example_test.go` (GO) | Magnitude: 29.38 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 83, branch: 11, safety: 11, high_risk_execution: 10
- `src/cmd/addr2line/main.go` (GO) | Magnitude: 29.04 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 58, branch: 9, doc: 8, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/runtime/cgocheck.go` (GO) | Magnitude: 106.12 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 85, branch: 25, pointers: 20, doc: 17
- `src/cmd/cgo/internal/test/issue4339.c` (C) | Magnitude: 4.24 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 3, dead_code: 3, args: 2, func_start: 2
- `src/cmd/cgo/internal/test/callback.go` (GO) | Magnitude: 1585.96 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: encapsulation: 1276, args: 1271, func_start: 1271, indent_tabs: 396

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/sync/runtime.go` (GO) | Magnitude: 33.66 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 17, args: 13, func_start: 13, encapsulation: 13
- `src/math/hypot_noasm.go` (GO) | Magnitude: 2.0 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 2, encapsulation: 2, structural_boundaries: 1, args: 1
- `src/syscall/time_nofake.go` (GO) | Magnitude: 2.0 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 3, encapsulation: 2, structural_boundaries: 1, args: 1
- `src/runtime/cgo/openbsd.go` (GO) | Magnitude: 11.56 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 2, globals: 1, reflection_metaprogramming: 1
- `src/runtime/cgo/windows.go` (GO) | Magnitude: 11.56 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 2, globals: 1, reflection_metaprogramming: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/runtime/defs_darwin_amd64.go` (GO) | Magnitude: 111.04 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 272, state_mutation: 91, globals: 88, core_var_decl: 88
- `src/runtime/sys_nonppc64x.go` (GO) | Magnitude: 1.56 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, args: 1, func_start: 1
- `test/uintptrkeepalive.go` (GO) | Magnitude: 1.56 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 1, args: 1, func_start: 1
- `src/testing/iotest/writer_test.go` (GO) | Magnitude: 9.54 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 24, branch: 4, structural_boundaries: 4, doc: 2
- `test/fixedbugs/issue18419.dir/test.go` (GO) | Magnitude: 3.82 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/crypto/x509/oid_test.go` (GO) | Magnitude: 2.31 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 296, branch: 52, state_mutation: 39, structural_boundaries: 31
- `src/runtime/_mkmalloc/mksizeclasses.go` (GO) | Magnitude: 168.26 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 202, branch: 50, structural_boundaries: 38, doc: 23
- `src/html/template/html.go` (GO) | Magnitude: 134.82 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 159, branch: 44, structural_boundaries: 25, doc: 17
- `src/text/template/parse/parse.go` (GO) | Magnitude: 470.32 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 505, branch: 143, structural_boundaries: 109, pointers: 73
- `src/runtime/mpagealloc.go` (GO) | Magnitude: 415.88 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 416, doc: 140, state_mutation: 85, branch: 83

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `test/fixedbugs/issue73823.go` (GO) | Magnitude: 28.54 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 25, structural_boundaries: 14, args: 6, func_start: 6
- `test/typeparam/issue50642.go` (GO) | Magnitude: 44.42 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 21, structural_boundaries: 16, api: 7, state_mutation: 6
- `test/typeparam/issue45722.go` (GO) | Magnitude: 12.98 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 15, branch: 5, structural_boundaries: 4, args: 3
- `src/internal/types/testdata/check/builtins1.go` (GO) | Magnitude: 0.18 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_tabs: 191, structural_boundaries: 89, core_var_decl: 72, design_short_vars: 72
- `test/fixedbugs/issue77779.go` (GO) | Magnitude: 14.04 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 12, indent_tabs: 12, api: 8, class_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/internal/types/testdata/spec/range_int.go` (GO) | Magnitude: 0.09 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 140, structural_boundaries: 56, branch: 54, core_var_decl: 44
- `src/cmd/compile/internal/types2/decl.go` (GO) | Magnitude: 522.74 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 499, branch: 155, structural_boundaries: 74, state_mutation: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `test/fixedbugs/issue49282.go` (GO) | Magnitude: 16.3 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_tabs: 20, core_var_decl: 7, safety_bypasses: 6, design_short_vars: 6
- `test/fixedbugs/issue6269.go` (GO) | Magnitude: 8.5 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 14, structural_boundaries: 11, args: 4, func_start: 4
- `test/unsafebuiltins.go` (GO) | Magnitude: 17.58 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_tabs: 54, reflection_metaprogramming: 28, pointers: 19, core_var_decl: 19
- `src/internal/testenv/testenv_notwin.go` (GO) | Magnitude: 15.66 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 28, structural_boundaries: 9, branch: 7, doc: 4
- `src/runtime/race/testdata/io_test.go` (GO) | Magnitude: 0.05 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 58, structural_boundaries: 8, state_mutation: 8, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/crypto/tls/handshake_server_tls13.go` (GO) | Magnitude: 5.8 | Delta: **0.147** (centroid distance) | Secondary Pull: `file_cluster_3`
  * Top Architectural Signatures: indent_tabs: 858, branch: 239, structural_boundaries: 183, state_mutation: 78

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/crypto/internal/fips140/fips140.go` (GO) | Magnitude: 0.35 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 33, branch: 11, doc: 10, structural_boundaries: 9
- `src/cmd/addr2line/addr2line_test.go` (GO) | Magnitude: 72.0 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 81, branch: 17, structural_boundaries: 11, doc: 9
- `src/net/tcpsock_unix_test.go` (GO) | Magnitude: 71.78 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 87, structural_boundaries: 18, branch: 11, concurrency: 8
- `src/mime/type.go` (GO) | Magnitude: 76.62 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 165, branch: 22, structural_boundaries: 22, core_var_decl: 22
- `src/cmd/compile/internal/reflectdata/map.go` (GO) | Magnitude: 108.48 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 193, doc: 25, branch: 24, state_mutation: 20

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/cmd/link/link_test.go` -> Churn: **86.1%** | Cog Load: 29.452% | Debt: 64.0359%
- `src/net/url/url_test.go` -> Churn: **77.17%** | Cog Load: 7.8495% | Debt: 52.4612%
- `src/cmd/link/internal/ld/data.go` -> Churn: **73.12%** | Cog Load: 52.0066% | Debt: 34.7584%
- `src/runtime/mheap.go` -> Churn: **71.51%** | Cog Load: 40.4571% | Debt: 79.2317%
- `src/cmd/compile/internal/ssagen/ssa.go` -> Churn: **70.47%** | Cog Load: 51.3628% | Debt: 11.3429%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/cmd/go/internal/load/pkg.go` -> **Ian Alexander** (100.0% isolated ownership) | Magnitude: 3074.38
- `src/math/all_test.go` -> **Meng Zhuo** (100.0% isolated ownership) | Magnitude: 2423.48
- `src/cmd/compile/internal/syntax/parser.go` -> **Robert Griesemer** (100.0% isolated ownership) | Magnitude: 2422.18
- `src/cmd/compile/internal/ppc64/ssa.go` -> **Keith Randall** (100.0% isolated ownership) | Magnitude: 2405.02
- `src/net/http/internal/http2/transport_test.go` -> **Damien Neil** (90.9% isolated ownership) | Magnitude: 2299.62

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/runtime/mprof.go` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 99.9999%)
- `src/runtime/proc.go` -> **Severity: 0.005** (Bridge: 0.0 * Flux: 99.9984%)
- `src/runtime/export_test.go` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 99.9621%)
- `src/cmd/compile/internal/ssa/func.go` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `src/cmd/compile/internal/reflectdata/alg.go` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9981%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/runtime/runtime2.go` -> **Severity: 0.987** (Embedded: 0.0197 * Error Risk: 50.0834%)
- `src/runtime/mprof.go` -> **Severity: 0.98** (Embedded: 0.0143 * Error Risk: 68.3548%)
- `src/cmd/compile/internal/base/base.go` -> **Severity: 0.914** (Embedded: 0.0152 * Error Risk: 60.143%)
- `src/cmd/internal/src/pos.go` -> **Severity: 0.862** (Embedded: 0.0148 * Error Risk: 58.1908%)
- `src/runtime/sema.go` -> **Severity: 0.858** (Embedded: 0.0108 * Error Risk: 79.7282%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/net/parse.go` -> **Severity: 629.072** (Blast Radius: 8.807 * Doc Risk: 71.4286%)
- `src/runtime/runtime2.go` -> **Severity: 491.776** (Blast Radius: 12.165 * Doc Risk: 40.4255%)
- `src/os/error_test.go` -> **Severity: 469.9** (Blast Radius: 4.699 * Doc Risk: 100.0%)
- `src/runtime/mprof.go` -> **Severity: 381.584** (Blast Radius: 13.277 * Doc Risk: 28.7402%)
- `src/cmd/compile/internal/base/base.go` -> **Severity: 367.9** (Blast Radius: 3.679 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 8055 literal sites + 212 sites through wrappers = 8267
- **`panics_and_aborts`:** 8719 literal sites + 273 sites through wrappers = 8992

- `Printf` (function, debug_prints, primitive): 42 call sites in 1 files -- `src/cmd/vet/testdata/print/print.go`
- `ppanic` (function, panics_and_aborts, primitive): 28 call sites in 1 files -- `test/closure3.dir/main.go`
- `trace` (function, debug_prints, primitive): 21 call sites in 1 files -- `src/math/big/natmul.go`
- `bad` (function, debug_prints, primitive): 16 call sites in 1 files -- `src/regexp/testdata/testregex.c`
- `bad` (function, panics_and_aborts, primitive): 16 call sites in 1 files -- `src/regexp/testdata/testregex.c`
- `main` (function, debug_prints, primitive): 14 call sites in 1 files -- `src/cmd/go/go_test.go`
- `alarm` (function, panics_and_aborts, primitive): 13 call sites in 1 files -- `src/go/doc/testdata/testing.go`
- `min` (function, panics_and_aborts, primitive): 11 call sites in 1 files -- `src/internal/types/testdata/examples/inference.go`
- `unreachable` (function, panics_and_aborts, primitive): 11 call sites in 1 files -- `test/chan/select3.go`
- `die` (function, debug_prints, primitive): 9 call sites in 1 files -- `src/cmd/cgo/internal/testcarchive/testdata/main2.c`
- `die` (function, panics_and_aborts, primitive): 9 call sites in 1 files -- `src/cmd/cgo/internal/testcarchive/testdata/main2.c`
- `die` (function, debug_prints, primitive): 8 call sites in 1 files -- `src/cmd/cgo/internal/testcshared/testdata/main4.c`
*(+182 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 256925 call pairs -- scoped 29.5%, unique 5.0%, ambiguous 60.5%, external 5.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| go | 255487 | 29.6% | 5.1% | 60.8% | 4.5% |
| c | 709 | 11.6% | 1.0% | 3.2% | 84.2% |
| assembly | 283 | 0.0% | 1.1% | 0.0% | 98.9% |
| python | 157 | 20.4% | 0.0% | 0.0% | 79.6% |
| javascript | 149 | 27.5% | 0.0% | 0.0% | 72.5% |
| shell | 116 | 6.0% | 0.0% | 0.0% | 94.0% |
| perl | 16 | 12.5% | 0.0% | 0.0% | 87.5% |
| html | 5 | 0.0% | 0.0% | 0.0% | 100.0% |
| objective-c | 2 | 0.0% | 0.0% | 0.0% | 100.0% |
| cpp | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
