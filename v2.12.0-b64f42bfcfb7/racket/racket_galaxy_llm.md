# ARCHITECTURAL_BRIEF: racket
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/racket/racket` |
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
- **Scope:** 722 analyzed artifact(s), 144298 LOC.
- **Load-bearing artifact:** `racket/collects/racket/private/list-predicates.rkt` -- 200 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `.github/workflows/ci-push-x86_linux.yml` -- pulls in 6 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `racket/collects/setup/private/pkg-deps.rkt` at magnitude 5544.42 (structural weight, not risk).
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
| Total Artifacts | 5834 |
| Analyzed Artifacts (Scanned) | 722 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5112 |
| Total LOC | 144298 |
| Volatility Index | 0.007 |
| % Scanned of codebase = | 12.4% |
| Dominant Lang | SCHEME |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.35 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1445 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 21.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.5285 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 62 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| SCHEME | 678 | 142614 | 93.9% |
| YAML | 15 | 1317 | 2.1% |
| PLAINTEXT | 13 | 1 | 1.8% |
| MARKDOWN | 10 | 0 | 1.4% |
| SHELL | 4 | 87 | 0.6% |
| DOCKERFILE | 1 | 11 | 0.1% |
| MAKEFILE | 1 | 268 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 721 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 24%, Many-Argument Workhorses Files 19%, Large Core Modules 14%, Data / Markup / Trivial 14%, Large Core Modules (3) 11%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 699 | 96.8% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 22 | 3.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5112*

**Composition by Extension & Reason:**
- `.rkt`: 1893x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 660 LOC)
- `.scrbl`: 517x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.scrbl')
- `.c`: 515x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ss`: 287x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 218x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.h`: 210x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rktl`: 193x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zuo`: 161x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.zuo)
- `.txt`: 89x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.inc`: 85x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.m4`: 62x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sch`: 56x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.s`: 56x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rktd`: 55x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 52x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 89.2 | 10.0 | 8.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 13.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 7.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 24.6 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 29.0 | 0.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 28.2 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 93.5 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.7 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 66.3 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 743 | 176 | 3 | `racket/collects/compiler/private/xform.rkt` |
| cleanup | 145 | 40 | 0 | `racket/collects/racket/port.rkt` |
| guards | 181 | 77 | 1 | `racket/collects/racket/file.rkt` |
| danger | 798 | 210 | 3 | `.github/workflows/ubsan-x86.yml` |
| concurrency | 17 | 13 | 0 | `racket/collects/racket/file.rkt` |
| connectivity | 73 | 41 | 0 | `racket/collects/racket/private/unit/unit-core.rkt` |
| io | 1505 | 254 | 7 | `racket/collects/compiler/private/xform.rkt` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `.github/images/Dockerfile` |
| time | 0 | 0 | 0 | - |
| serialization | 2 | 1 | 0 | `.github/scripts/adjust-sarif-tool.sh` |
| regex | 1 | 1 | 0 | `.github/scripts/test.sh` |
| events | 55 | 21 | 0 | `racket/collects/compiler/private/xform.rkt` |
| tests | 185 | 12 | 0 | `racket/collects/file/private/glob.rkt` |
| docs | 95 | 24 | 0 | `racket/collects/net/uri-codec.rkt` |
| debt | 558 | 147 | 2 | `.github/workflows/ubsan-x86.yml` |
| mutation | 1685 | 202 | 4 | `racket/collects/file/gzip.rkt` |
| dead_code | 338 | 130 | 1 | `Makefile` |
| credential | 3 | 1 | 0 | `racket/collects/compiler/private/xform.rkt` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 176 | 51 | 0 | `racket/collects/racket/math.rkt` |
| ui | 2 | 1 | 0 | `.github/images/Dockerfile` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `racket/collects/compiler/private/xform.rkt` (Hits: 59)
- `racket/collects/launcher/launcher.rkt` (Hits: 40)
- `racket/collects/setup/unpack.rkt` (Hits: 36)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **list-predicates.rkt** (`racket/collects/racket/private/list-predicates.rkt`) — 200 inbound connections
2. **elf.rkt** (`racket/collects/compiler/private/elf.rkt`) — 139 inbound connections
3. **interfaces.rkt** (`racket/collects/db/private/generic/interfaces.rkt`) — 134 inbound connections
4. **coercion.rkt** (`racket/collects/racket/place/private/coercion.rkt`) — 104 inbound connections
5. **string.rkt** (`racket/collects/racket/string.rkt`) — 92 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ci-push-x86_linux.yml** (`.github/workflows/ci-push-x86_linux.yml`) — 6 outbound dependencies
2. **ci-pr.yml** (`.github/workflows/ci-pr.yml`) — 4 outbound dependencies
3. **ci-push_macos.yml** (`.github/workflows/ci-push_macos.yml`) — 3 outbound dependencies
4. **codeql-analysis.yml** (`.github/workflows/codeql-analysis.yml`) — 3 outbound dependencies
5. **README.md** (`README.md`) — 2 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `install-packages` **(Many-Argument Workhorses)** (@ `racket/collects/pkg/private/install.rkt`) -> Impact: **1633.5** | LOC: 1332
- `get-ffi-lib` **(Many-Argument Workhorses)** (@ `racket/collects/ffi/unsafe.rkt`) -> Impact: **958.4** | LOC: 1430
- `git-checkout` **(Many-Argument Workhorses)** (@ `racket/collects/net/git-checkout.rkt`) -> Impact: **857.0** | LOC: 1267
  * *Intent:* ;; Like `git clone`, but producing just the checkout
- `get-code` **(Many-Argument Workhorses)** (@ `racket/collects/compiler/embed.rkt`) -> Impact: **732.2** | LOC: 724
  * *Intent:* ;; Loads module code, using .zo if there, compiling from .scm if not
- `pretty-print-extend-style-table` **(Many-Argument Workhorses)** (@ `racket/collects/racket/pretty.rkt`) -> Impact: **707.1** | LOC: 1542
- `delete-files-in-directory` **(Many-Argument Workhorses)** (@ `racket/collects/setup/setup-core.rkt`) -> Impact: **533.7** | LOC: 1074
- `arg` **(Many-Argument Workhorses)** (@ `racket/collects/ffi/unsafe.rkt`) -> Impact: **510.4** | LOC: 1328
- `xform` **(Many-Argument Workhorses)** (@ `racket/collects/compiler/private/xform.rkt`) -> Impact: **510.1** | LOC: 1222
- `clean-collection` **(Many-Argument Workhorses)** (@ `racket/collects/setup/setup-core.rkt`) -> Impact: **470.7** | LOC: 1065
- `maybe-add-exe` **(Many-Argument Workhorses)** (@ `racket/collects/compiler/private/xform.rkt`) -> Impact: **456.1** | LOC: 1599

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `racket/collects/racket/private` | 113 | 12016.14 | 12.0% | 3.04% |
| `racket/collects/racket` | 103 | 10981.26 | 10.18% | 2.67% |
| `racket/collects/setup/private` | 13 | 6030.82 | 5.66% | 4.79% |
| `racket/collects/openssl` | 9 | 5901.78 | 6.42% | 2.4% |
| `racket/collects/racket/contract/private` | 54 | 5499.36 | 12.49% | 5.8% |
| `racket/collects/pkg/private` | 45 | 5154.12 | 8.17% | 10.7% |
| `racket/collects/compiler/private` | 24 | 4945.22 | 8.24% | 20.44% |
| `racket/collects/setup` | 32 | 4775.2 | 8.77% | 3.83% |
| `racket/collects/syntax/parse/private` | 26 | 3521.5 | 15.71% | 29.96% |
| `racket/collects/net` | 13 | 3410.44 | 11.5% | 3.91% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/workflows/ci-push-x86_linux.yml` -> **100.0%** Exposure
- `.github/workflows/ubsan-x86.yml` -> **100.0%** Exposure
- `racket/collects/syntax/parse/private/tree-util.rkt` -> **100.0%** Exposure
- `.github/workflows/ci-push_macos.yml` -> **99.9993%** Exposure
- `Makefile` -> **99.9962%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `racket/collects/file/gzip.rkt` -> **100.0%** Exposure
- `racket/collects/file/gunzip.rkt` -> **99.9991%** Exposure
- `racket/collects/syntax/to-string.rkt` -> **99.9731%** Exposure
- `racket/collects/racket/random.rkt` -> **99.394%** Exposure
- `racket/collects/ffi/unsafe/atomic.rkt` -> **98.7973%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `.github/workflows/ubsan-x86.yml` -> **0** Orphaned Functions | **40** Duplicates
- `Makefile` -> **34** Orphaned Functions | **0** Duplicates
- `.github/workflows/ci-push-x86_linux.yml` -> **0** Orphaned Functions | **24** Duplicates
- `.github/workflows/ci-push_macos.yml` -> **0** Orphaned Functions | **15** Duplicates
- `racket/collects/db/private/generic/functions.rkt` -> **9** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `230` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `racket/collects/setup/private/pkg-deps.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.722)
- **Top Global Matches:** file_cluster_2: 3.722, file_cluster_10: 4.903, file_cluster_17: 5.257
- **Magnitude:** 5544.42 | **LOC:** 788 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.5%), Mutation Surface (formerly State Flux) (9.7%), Complexity Load (formerly Cognitive Load) (6.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 11`, `args: 22`, `func_start: 22`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 18`, `import: 1`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.643
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/collects/openssl/test.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.643
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/collects/compiler/private/xform.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.136)
- **Top Global Matches:** file_cluster_6: 9.136, file_cluster_8: 9.383, file_cluster_4: 16.891
- **Magnitude:** 2958.5 | **LOC:** 4353 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); blast radius 10.952; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.7%), Mutation Surface (formerly State Flux) (23.2%), Complexity Load (formerly Cognitive Load) (17.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `xform` **(Many-Argument Workhorses)** (Impact: 510.1)
  * `maybe-add-exe` **(Many-Argument Workhorses)** (Impact: 456.1)
  * `push-vars` **(Many-Argument Workhorses)** (Impact: 386.2)
  * `get-variable-size` **(Compute Cores)** (Impact: 323.8)
    * *Intent:* ;; gets the size of a variable in terms of the number of ;; __gc_var_stack__ slots it needs
  * `check-pointer-type` **(Compute Cores)** (Impact: 298.8)
    * *Intent:* ;; e is a typedef; drop the "typedef" keyword and ;; parse it as a variable declaration using `get-v...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 744`, `structural_boundaries: 258`, `args: 123`, `func_start: 124`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 54`, `fragile_debt: 5`, `unreferenced_by_name: 7`
* *Architecture:* `io: 59`, `import: 1`
* *Defense:* `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.952
  * `Choke Point (Betweenness):` 0.023377 | `Ripple Effect (Closeness):` 0.189169
  * `Imports (Out-Degree: 17):` None
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `racket/collects/pkg/private/install.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.217)
- **Top Global Matches:** file_cluster_8: 7.217, file_cluster_6: 12.169, file_cluster_4: 20.504
- **Magnitude:** 2315.6 | **LOC:** 1482 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.95; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (10.9%), Debt Markers (formerly Tech Debt) (8.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `install-packages` **(Many-Argument Workhorses)** (Impact: 1633.5)
  * `show-dependencies` **(Many-Argument Workhorses)** (Impact: 394.9)
  * `pkg-update` **(Many-Argument Workhorses)** (Impact: 168.5)
  * `checksum-for-pkg-source` **(Many-Argument Workhorses)** (Impact: 39.6)
    * *Intent:* ;; A [prefetch-shared] annotation means that a hash table is shared ;; with prefetch threads. If a p...
  * `disallow-package-path-overlaps` **(Many-Argument Workhorses)** (Impact: 20.5)
    * *Intent:* #:type type #:prefetch? prefetch? #:prefetch-group prefetch-group #:catalog-lookup-cache catalog-loo...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 14`, `args: 21`, `func_start: 21`
* *Risk/State:* `unreferenced_by_name: 2`
* *Architecture:* `io: 5`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.95
  * `Choke Point (Betweenness):` 0.021431 | `Ripple Effect (Closeness):` 0.093823
  * `Imports (Out-Degree: 26):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `racket/collects/net/git-checkout.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.357)
- **Top Global Matches:** file_cluster_8: 6.357, file_cluster_6: 14.957, file_cluster_3: 22.582
- **Magnitude:** 2025.96 | **LOC:** 1306 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **1**; blast radius 1.483; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.3%), Mutation Surface (formerly State Flux) (20.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `git-checkout` **(Many-Argument Workhorses)** (Impact: 857.0)
    * *Intent:* ;; Like `git clone`, but producing just the checkout
  * `initial-connect` **(Many-Argument Workhorses)** (Impact: 321.8)
    * *Intent:* ;; initial-connect: transport-sym string bool natural string status-proc string string ;; -> (values...
  * `maybe-save-objects` **(Many-Argument Workhorses)** (Impact: 294.4)
  * `parse-initial-refs` **(Many-Argument Workhorses)** (Impact: 162.3)
    * *Intent:* ;; parse-initial-refs : (listof bytes) -> (listof (list bytes string)) ;; In each element of the ret...
  * `extract-tree` **(Many-Argument Workhorses)** (Impact: 72.4)
    * *Intent:* ;; extract-tree : bytes (hash/c bytes object) tmp-info path -> void ;; Extract the designated tree t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 16`, `args: 55`, `func_start: 56`
* *Risk/State:* `state_mutation: 10`, `unreferenced_by_name: 1`
* *Architecture:* `io: 7`, `import: 2`
* *Defense:* `safety: 4`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.483
  * `Choke Point (Betweenness):` 0.016237 | `Ripple Effect (Closeness):` 0.078172
  * `Imports (Out-Degree: 22):` cmdline
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `racket/collects/ffi/unsafe.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.52)
- **Top Global Matches:** file_cluster_4: 7.52, file_cluster_6: 9.126, file_cluster_15: 13.876
- **Magnitude:** 1985.14 | **LOC:** 2317 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); blast radius 4.05; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.2%), Mutation Surface (formerly State Flux) (35.1%), Complexity Load (formerly Cognitive Load) (33.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get-ffi-lib` **(Many-Argument Workhorses)** (Impact: 958.4)
  * `arg` **(Many-Argument Workhorses)** (Impact: 510.4)
  * `coretype-plain-pointer` **(Compute Cores)** (Impact: 165.5)
  * `make-syntax` **(Many-Argument Workhorses)** (Impact: 34.7)
  * `cpointer-maker` **(Compute Cores)** (Impact: 30.4)
    * *Intent:* #'(lambda (cptr tag) (cpointer-push-tag! cptr tag))]))
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 347`, `structural_boundaries: 120`, `args: 72`, `func_start: 79`
* *Risk/State:* `state_mutation: 38`, `fragile_debt: 2`
* *Architecture:* `io: 12`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.05
  * `Choke Point (Betweenness):` 0.010842 | `Ripple Effect (Closeness):` 0.127679
  * `Imports (Out-Degree: 17):` None
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `racket/collects/setup/setup-core.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 12.273)
- **Top Global Matches:** file_cluster_3: 12.273, file_cluster_8: 13.369, file_cluster_6: 25.735
- **Magnitude:** 1866.22 | **LOC:** 2244 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); blast radius 1.564; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.5%), Mutation Surface (formerly State Flux) (15.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `delete-files-in-directory` **(Many-Argument Workhorses)** (Impact: 533.7)
  * `clean-collection` **(Many-Argument Workhorses)** (Impact: 470.7)
  * `tidy-launchers` **(Many-Argument Workhorses)** (Impact: 234.8)
  * `get-path` **(Many-Argument Workhorses)** (Impact: 180.9)
  * `delete` **(Compute Cores)** (Impact: 147.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 400`, `structural_boundaries: 44`, `args: 87`, `func_start: 88`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 13`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 18`, `import: 1`
* *Defense:* `safety: 1`, `doc: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.564
  * `Choke Point (Betweenness):` 0.042024 | `Ripple Effect (Closeness):` 0.11568
  * `Imports (Out-Degree: 40):` None
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `racket/collects/racket/port.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.539)
- **Top Global Matches:** file_cluster_4: 7.539, file_cluster_6: 9.924, file_cluster_15: 13.632
- **Magnitude:** 1720.68 | **LOC:** 2096 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **1**; blast radius 1.734; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.0%), Complexity Load (formerly Cognitive Load) (41.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `merge-input` **(Compute Cores)** (Impact: 217.2)
    * *Intent:* ;; ----------------------------------------
  * `reencode-output-port` **(Many-Argument Workhorses)** (Impact: 177.3)
    * *Intent:* ;; --------------------------------------------------
  * `write-it` **(Many-Argument Workhorses)** (Impact: 167.5)
    * *Intent:* ;; The main writing entry point:
  * `make-input-port/read-to-peek` **(I/O & Config Routines)** (Impact: 137.1)
    * *Intent:* ;; Not kill-safe. ;; If the `read' proc returns an event, the event must produce ;; 0 always (which ...
  * `bytes-convert/post-nl` **(Many-Argument Workhorses)** (Impact: 97.4)
    * *Intent:* ;; -------------------------------------------------- ;; Helper for reencode-input-port: simulate th...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 65 instances
* *State Mutation (weighted view):* 215
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 373`, `structural_boundaries: 142`, `args: 99`, `func_start: 114`
* *Risk/State:* `state_mutation: 85`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 13`, `api: 2`, `import: 1`
* *Defense:* `safety: 2`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.734
  * `Choke Point (Betweenness):` 0.001336 | `Ripple Effect (Closeness):` 0.105043
  * `Imports (Out-Degree: 12):` base
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `racket/collects/racket/private/more-scheme.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.755)
- **Top Global Matches:** file_cluster_10: 4.755, file_cluster_17: 5.057, file_cluster_2: 5.099
- **Magnitude:** 1480.28 | **LOC:** 394 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.4%), Complexity Load (formerly Cognitive Load) (23.0%), Mutation Surface (formerly State Flux) (15.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 31`, `args: 12`, `func_start: 14`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* None
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.643
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/collects/racket/private/set-types.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.774)
- **Top Global Matches:** file_cluster_6: 7.774, file_cluster_8: 12.199, file_cluster_4: 14.229
- **Magnitude:** 1327.14 | **LOC:** 1137 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.717; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (9.9%), Complexity Load (formerly Cognitive Load) (9.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `chaperone-hash-set` **(Many-Argument Workhorses)** (Impact: 201.9)
  * `custom-set-subtract` **(Many-Argument Workhorses)** (Impact: 175.8)
  * `custom-set-union` **(Many-Argument Workhorses)** (Impact: 172.2)
  * `custom-set-symmetric-difference` **(Many-Argument Workhorses)** (Impact: 169.7)
  * `custom-set-intersect` **(Many-Argument Workhorses)** (Impact: 165.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 4`, `args: 125`, `func_start: 125`
* *Risk/State:* `unreferenced_by_name: 3`
* *Architecture:* `io: 10`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.717
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.001849
  * `Imports (Out-Degree: 7):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `racket/collects/compiler/embed.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.484)
- **Top Global Matches:** file_cluster_4: 7.484, file_cluster_6: 9.251, file_cluster_15: 13.864
- **Magnitude:** 1128.88 | **LOC:** 2041 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 1.509; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.3%), Complexity Load (formerly Cognitive Load) (16.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get-code` **(Many-Argument Workhorses)** (Impact: 732.2)
    * *Intent:* ;; Loads module code, using .zo if there, compiling from .scm if not
  * `do-write-module-bundle` **(Many-Argument Workhorses)** (Impact: 200.8)
    * *Intent:* ;; Write a module bundle that can be loaded with 'load' (do not embed it ;; into an executable). The...
  * `create-embedding-executable` **(Many-Argument Workhorses)** (Impact: 29.7)
    * *Intent:* #:mred? mred? #:verbose? verbose? #:modules modules #:literal-files literal-files #:literal-expressi...
  * `filters` **(Compute Cores)** (Impact: 20.6)
  * `find-relevant-lib-dir` **(Many-Argument Workhorses)** (Impact: 14.7)
    * *Intent:* ;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 393`, `structural_boundaries: 96`, `args: 57`, `func_start: 58`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 12`, `fragile_debt: 3`
* *Architecture:* `io: 33`, `import: 1`
* *Defense:* `safety: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.509
  * `Choke Point (Betweenness):` 0.000598 | `Ripple Effect (Closeness):` 0.004161
  * `Imports (Out-Degree: 19):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `racket/collects/file/gzip.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.128)
- **Top Global Matches:** file_cluster_4: 7.128, file_cluster_15: 9.584, file_cluster_16: 10.145
- **Magnitude:** 1113.28 | **LOC:** 2219 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **1**; blast radius 1.398; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `code` **(I/O & Config Routines)** (Impact: 225.8)
    * *Intent:* #x026d930a #x9c0906a9 #xeb0e363f #x72076785 #x05005713 #x95bf4a82 #xe2b87a14 #x7bb12bae #x0cb61b38 #...
  * `flush_block` **(Many-Argument Workhorses)** (Impact: 56.5)
    * *Intent:* ;; /* =========================================================================== ;; * Determine the...
  * `do-deflate` **(I/O & Config Routines)** (Impact: 23.9)
    * *Intent:* ;; /* =========================================================================== ;; * Same as above...
  * `gen_bitlen` **(Compute Cores)** (Impact: 20.0)
    * *Intent:* ;; /* =========================================================================== ;; * Compute the o...
  * `send_tree` **(Many-Argument Workhorses)** (Impact: 16.4)
    * *Intent:* ;; /* =========================================================================== ;; * Send a litera...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 141 instances
* *State Mutation (weighted view):* 522
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 92`, `args: 54`, `func_start: 56`
* *Risk/State:* `state_mutation: 240`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 3`, `import: 1`
* *Defense:* `safety: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.102638
  * `Imports (Out-Degree: 2):` base
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `racket/collects/launcher/launcher.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.466)
- **Top Global Matches:** file_cluster_6: 7.466, file_cluster_4: 9.251, file_cluster_15: 16.381
- **Magnitude:** 1089.36 | **LOC:** 1117 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 1.542; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.4%), Connectivity (formerly Api Exposure) (22.5%), Complexity Load (formerly Cognitive Load) (15.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make-unix-launcher` **(Many-Argument Workhorses)** (Impact: 188.7)
  * `relativize` **(Many-Argument Workhorses)** (Impact: 172.9)
  * `dos-str` **(Compute Cores)** (Impact: 164.9)
  * `trans` **(Compute Cores)** (Impact: 164.7)
  * `variant-available` **(Many-Argument Workhorses)** (Impact: 62.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 67`, `args: 83`, `func_start: 83`
* *Risk/State:* `high_risk_execution: 1`, `planned_debt: 1`
* *Architecture:* `io: 40`, `api: 3`, `import: 1`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.542
  * `Choke Point (Betweenness):` 0.004176 | `Ripple Effect (Closeness):` 0.139276
  * `Imports (Out-Degree: 14):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `racket/collects/racket/treelist.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.577)
- **Top Global Matches:** file_cluster_4: 6.577, file_cluster_15: 11.019, file_cluster_6: 11.651
- **Magnitude:** 1013.38 | **LOC:** 1718 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 0.893; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.0%), Complexity Load (formerly Cognitive Load) (11.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assert-node` **(Compute Cores)** (Impact: 334.3)
    * *Intent:* ;; `node*` refers to a leftwise dense node
  * `treelist-append` **(Many-Argument Workhorses)** (Impact: 156.4)
  * `treelist-add` **(Many-Argument Workhorses)** (Impact: 76.6)
    * *Intent:* ;; add `el` to end of vector
  * `chaperone-treelist` **(Many-Argument Workhorses)** (Impact: 45.4)
  * `check-treelist-bound-index` **(Many-Argument Workhorses)** (Impact: 34.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 26`, `args: 112`, `func_start: 113`
* *Risk/State:* `state_mutation: 2`, `planned_debt: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 12`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.893
  * `Choke Point (Betweenness):` 0.008399 | `Ripple Effect (Closeness):` 0.08007
  * `Imports (Out-Degree: 10):` for-body
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `racket/collects/racket/private/serialize.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.306)
- **Top Global Matches:** file_cluster_8: 7.306, file_cluster_6: 11.356, file_cluster_4: 19.654
- **Magnitude:** 920.38 | **LOC:** 791 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.864; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.7%), Mutation Surface (formerly State Flux) (44.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find-mutable` **(Many-Argument Workhorses)** (Impact: 233.7)
    * *Intent:* ;; Finds a mutable object among those that make the ;; current cycle.
  * `protect-path` **(Many-Argument Workhorses)** (Impact: 230.5)
    * *Intent:* ;; If a module is dynamic-required through a path, ;; then it can cause simplified module paths to b...
  * `serialize-one` **(Many-Argument Workhorses)** (Impact: 209.1)
  * `serial-shell` **(Many-Argument Workhorses)** (Impact: 113.5)
  * `mod-to-id` **(Many-Argument Workhorses)** (Impact: 13.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 61`, `args: 24`, `func_start: 24`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 4`
* *Architecture:* `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.864
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.056567
  * `Imports (Out-Degree: 4):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `racket/collects/racket/pretty.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.004)
- **Top Global Matches:** file_cluster_4: 7.004, file_cluster_6: 10.017, file_cluster_15: 12.687
- **Magnitude:** 820.1 | **LOC:** 1700 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **1**; blast radius 2.48; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.9%), Complexity Load (formerly Cognitive Load) (19.7%), Mutation Surface (formerly State Flux) (16.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pretty-print-extend-style-table` **(Many-Argument Workhorses)** (Impact: 707.1)
  * `decimal-string` **(Compute Cores)** (Impact: 16.5)
  * `pretty-format` **(Compute Cores)** (Impact: 10.4)
  * `read-macro` **(Many-Argument Workhorses)** (Impact: 10.3)
  * `read-macro-prefix` **(Compute Cores)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 335`, `structural_boundaries: 108`, `args: 77`, `func_start: 84`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `io: 12`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.48
  * `Choke Point (Betweenness):` 0.012994 | `Ripple Effect (Closeness):` 0.117784
  * `Imports (Out-Degree: 10):` mutable-treelist
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `racket/collects/openssl/mzssl.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.833)
- **Top Global Matches:** file_cluster_4: 6.833, file_cluster_6: 8.93, file_cluster_15: 13.347
- **Magnitude:** 816.16 | **LOC:** 1794 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.931; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.2%), Debt Markers (formerly Tech Debt) (21.6%), Mutation Surface (formerly State Flux) (20.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrap-ports` **(Many-Argument Workhorses)** (Impact: 208.7)
  * `ssl-make-client-context` **(Many-Argument Workhorses)** (Impact: 93.0)
  * `pump-output-once` **(Many-Argument Workhorses)** (Impact: 60.6)
  * `ssl-set-verify-hostname` **(Compute Cores)** (Impact: 33.8)
  * `ssl-set-verify` **(Compute Cores)** (Impact: 31.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 268`, `structural_boundaries: 112`, `args: 94`, `func_start: 94`
* *Risk/State:* `state_mutation: 15`, `planned_debt: 2`, `fragile_debt: 5`, `unreferenced_by_name: 3`
* *Architecture:* `io: 12`, `import: 1`
* *Defense:* `safety: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.931
  * `Choke Point (Betweenness):` 0.005434 | `Ripple Effect (Closeness):` 0.072408
  * `Imports (Out-Degree: 20):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `racket/collects/racket/private/hash.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.429)
- **Top Global Matches:** file_cluster_2: 2.429, file_cluster_17: 4.612, file_cluster_10: 5.214
- **Magnitude:** 808.41 | **LOC:** 142 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (10.3%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 4`, `args: 6`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.643
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/collects/compiler/private/mach-o.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.879)
- **Top Global Matches:** file_cluster_6: 7.879, file_cluster_8: 10.204, file_cluster_4: 15.428
- **Magnitude:** 746.4 | **LOC:** 790 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.643; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.4%), Complexity Load (formerly Cognitive Load) (28.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add-plt-segment` **(Many-Argument Workhorses)** (Impact: 322.1)
    * *Intent:* ;; existing signature to be at the end of the linkedit segment. The ;; signature is 16-byte aligned,...
  * `check-exe-id` **(Many-Argument Workhorses)** (Impact: 311.7)
  * `fixup` **(Compute Cores)** (Impact: 15.0)
  * `file-has-signature` **(I/O & Config Routines)** (Impact: 7.1)
  * `round-up-page` **(Compute Cores)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 50`, `args: 22`, `func_start: 22`
* *Risk/State:* `state_mutation: 42`, `unreferenced_by_name: 1`
* *Architecture:* `io: 14`, `import: 1`
* *Defense:* `safety: 3`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.643
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` promise
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/collects/racket/contract/private/list.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.091)
- **Top Global Matches:** file_cluster_4: 7.091, file_cluster_6: 9.048, file_cluster_15: 13.185
- **Magnitude:** 733.82 | **LOC:** 1146 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.693; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (15.3%), Complexity Load (formerly Cognitive Load) (10.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `listof-generate` **(Many-Argument Workhorses)** (Impact: 225.9)
  * `listof-exercise` **(Many-Argument Workhorses)** (Impact: 215.7)
    * *Intent:* #f)))]))
  * `cons/dc-late-neg-projection` **(I/O & Config Routines)** (Impact: 114.5)
  * `list/c-late-neg-projection` **(Many-Argument Workhorses)** (Impact: 34.5)
  * `listof-late-neg-projection` **(I/O & Config Routines)** (Impact: 19.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 13`, `args: 49`, `func_start: 49`
* *Risk/State:* `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.693
  * `Choke Point (Betweenness):` 2.9e-05 | `Ripple Effect (Closeness):` 0.001387
  * `Imports (Out-Degree: 14):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `racket/collects/pkg/private/stage.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.359)
- **Top Global Matches:** file_cluster_6: 7.359, file_cluster_4: 8.258, file_cluster_15: 15.437
- **Magnitude:** 688.16 | **LOC:** 1066 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); blast radius 1.623; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.2%), Mutation Surface (formerly State Flux) (14.4%), Complexity Load (formerly Cognitive Load) (12.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `communication-type` **(Many-Argument Workhorses)** (Impact: 271.4)
    * *Intent:* #:prefab)
  * `checksum` **(Many-Argument Workhorses)** (Impact: 222.4)
    * *Intent:* ;; ----------------------------------------
  * `remote-package-checksum` **(Many-Argument Workhorses)** (Impact: 69.9)
  * `lookup-normally` **(I/O & Config Routines)** (Impact: 25.5)
    * *Intent:* #:type [type #f] #:prefetch? [prefetch? #f] #:prefetch-group [prefetch-group #f] #:catalog-lookup-ca...
  * `normalize-url` **(Many-Argument Workhorses)** (Impact: 13.2)
    * *Intent:* ;; ---------------------------------------- ;; Disambiguate `str` as needed to ensure that it will b...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 7`, `args: 23`, `func_start: 23`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 2`
* *Architecture:* `io: 13`, `import: 1`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.623
  * `Choke Point (Betweenness):` 0.020611 | `Ripple Effect (Closeness):` 0.084563
  * `Imports (Out-Degree: 26):` None
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `racket/collects/racket/private/class-internal.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.846)
- **Top Global Matches:** file_cluster_6: 7.846, file_cluster_4: 8.633, file_cluster_15: 15.79
- **Magnitude:** 638.08 | **LOC:** 4838 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 0.804; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.7%), Mutation Surface (formerly State Flux) (14.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unused-args-error` **(Many-Argument Workhorses)** (Impact: 79.6)
  * `field-names` **(Compute Cores)** (Impact: 68.9)
    * *Intent:* #t)))) ;; ensure that only #t and #f leak out, not bindings in ht
  * `do-method` **(Many-Argument Workhorses)** (Impact: 59.8)
  * `check-arg-contracts` **(Many-Argument Workhorses)** (Impact: 35.3)
  * `check-generic` **(I/O & Config Routines)** (Impact: 28.3)
    * *Intent:* #'(generic-name gen) #'((generic-applicable gen) obj) #'obj)))))))]))
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 472`, `structural_boundaries: 198`, `args: 114`, `func_start: 116`
* *Risk/State:* `state_mutation: 43`, `planned_debt: 2`, `unreferenced_by_name: 3`
* *Architecture:* `io: 23`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.804
  * `Choke Point (Betweenness):` 0.011506 | `Ripple Effect (Closeness):` 0.067644
  * `Imports (Out-Degree: 16):` base
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `racket/collects/racket/private/kw.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.108)
- **Top Global Matches:** file_cluster_8: 7.108, file_cluster_6: 11.911, file_cluster_4: 20.245
- **Magnitude:** 629.82 | **LOC:** 2320 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); blast radius 2.486; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.4%), Complexity Load (formerly Cognitive Load) (12.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `raise-wrong-kws` **(Many-Argument Workhorses)** (Impact: 196.7)
  * `keyword-procedure-extract/method` **(Many-Argument Workhorses)** (Impact: 184.3)
    * *Intent:* ;; Extracts the procedure using the keyword-argument protocol. ;; If `p' doesn't accept keywords, ma...
  * `procedure-reduce-keyword-arity-mask` **(Many-Argument Workhorses)** (Impact: 153.6)
  * `application-message` **(I/O & Config Routines)** (Impact: 15.9)
  * `normalize-proc` **(I/O & Config Routines)** (Impact: 8.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 124`, `args: 27`, `func_start: 30`
* *Risk/State:* `state_mutation: 3`, `dead_code: 9`, `unreferenced_by_name: 1`
* *Architecture:* `io: 26`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.486
  * `Choke Point (Betweenness):` 0.000465 | `Ripple Effect (Closeness):` 0.121721
  * `Imports (Out-Degree: 3):` None
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `racket/collects/racket/file.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.549)
- **Top Global Matches:** file_cluster_4: 7.549, file_cluster_6: 10.317, file_cluster_9: 12.04
- **Magnitude:** 615.76 | **LOC:** 1190 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); blast radius 5.306; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.3%), Connectivity (formerly Api Exposure) (13.3%), Mutation Surface (formerly State Flux) (11.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do-make-temporary-file/directory` **(Many-Argument Workhorses)** (Impact: 209.2)
  * `call-with-file-lock/timeout` **(Many-Argument Workhorses)** (Impact: 148.7)
  * `fold-files` **(Many-Argument Workhorses)** (Impact: 30.8)
    * *Intent:* ;; fold-files : (pathname sym alpha -> alpha) alpha pathname/#f -> alpha
  * `pathlist-closure` **(Many-Argument Workhorses)** (Impact: 30.1)
  * `make-handle-get-preference-locked` **(Many-Argument Workhorses)** (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 41`, `args: 51`, `func_start: 52`
* *Risk/State:* `state_mutation: 3`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 21`, `api: 1`, `import: 2`
* *Defense:* `safety: 11`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.306
  * `Choke Point (Betweenness):` 0.047558 | `Ripple Effect (Closeness):` 0.149395
  * `Imports (Out-Degree: 13):` None
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `racket/collects/racket/list.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.557)
- **Top Global Matches:** file_cluster_4: 6.557, file_cluster_6: 8.54, file_cluster_15: 13.251
- **Magnitude:** 614.78 | **LOC:** 956 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **33** in-repo importer(s); it depends on **1**; blast radius 24.856; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.4%), Mutation Surface (formerly State Flux) (22.0%), Complexity Load (formerly Cognitive Load) (19.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `in-combinations` **(Many-Argument Workhorses)** (Impact: 155.3)
    * *Intent:* ;; Generate combinations of the list `l`. ;; - If `k` is a natural number, generate all combinations...
  * `alist-update` **(Many-Argument Workhorses)** (Impact: 70.7)
    * *Intent:* ;; like hash-update, but for alists
  * `remove-duplicates` **(Many-Argument Workhorses)** (Impact: 56.8)
  * `list-prefix` **(Many-Argument Workhorses)** (Impact: 49.4)
    * *Intent:* ; list-prefix? : list? list? -> boolean? ; Is ls a prefix of rs?
  * `indexes-of` **(Many-Argument Workhorses)** (Impact: 21.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 63`, `args: 61`, `func_start: 65`
* *Risk/State:* `state_mutation: 9`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.856
  * `Choke Point (Betweenness):` 0.024862 | `Ripple Effect (Closeness):` 0.211357
  * `Imports (Out-Degree: 13):` base
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `racket/collects/racket/private/local.rkt` (SCHEME) | Magnitude: 17.26 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 109, structural_boundaries: 12, comprehensions: 10, closures: 8
- `racket/collects/syntax/kerncase.rkt` (SCHEME) | Magnitude: 18.18 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 108, branch: 10, reflection_metaprogramming: 10, macros: 10
- `racket/collects/racket/private/unix-rand.rkt` (SCHEME) | Magnitude: 4.14 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 8, args: 2, func_start: 2, branch: 1
- `racket/collects/syntax/parse/experimental/template.rkt` (SCHEME) | Magnitude: 15.6 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 24, branch: 3, closures: 3, reflection_metaprogramming: 3
- `racket/collects/racket/help.rkt` (SCHEME) | Magnitude: 152.02 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 57, branch: 7, closures: 5, structural_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `racket/collects/racket/match/runtime.rkt` (SCHEME) | Magnitude: 38.36 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 113, branch: 14, args: 11, func_start: 11
- `racket/collects/data/queue.rkt` (SCHEME) | Magnitude: 36.66 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 76, branch: 16, args: 9, func_start: 9
- `racket/collects/syntax/parse/private/parse.rkt` (SCHEME) | Magnitude: 63.26 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 274, reflection_metaprogramming: 28, macros: 28, structural_boundaries: 16
- `racket/collects/racket/generic.rkt` (SCHEME) | Magnitude: 74.22 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 310, branch: 24, reflection_metaprogramming: 20, macros: 20
- `racket/collects/racket/contract/private/opt.rkt` (SCHEME) | Magnitude: 25.16 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 326, branch: 32, reflection_metaprogramming: 18, macros: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `racket/collects/racket/private/class-undef.rkt` (SCHEME) | Magnitude: 528.61 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 143, branch: 30, structural_boundaries: 26, reflection_metaprogramming: 10
- `racket/collects/syntax/parse/experimental/specialize.rkt` (SCHEME) | Magnitude: 15.78 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 4, reflection_metaprogramming: 3, macros: 3
- `racket/collects/syntax/parse/private/runtime.rkt` (SCHEME) | Magnitude: 14.64 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 174, reflection_metaprogramming: 28, macros: 28, structural_boundaries: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `racket/collects/racket/match/parse-quasi.rkt` (SCHEME) | Magnitude: 16.86 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 71, func_start: 7, branch: 6, args: 6
- `racket/collects/racket/os.rkt` (SCHEME) | Magnitude: 9.98 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 36, branch: 8, structural_boundaries: 5, args: 4
- `racket/collects/racket/contract/combinator.rkt` (SCHEME) | Magnitude: 64.66 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 187, args: 15, func_start: 15, branch: 11
- `racket/collects/racket/logging.rkt` (SCHEME) | Magnitude: 16.64 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 4, args: 4, func_start: 4
- `racket/collects/setup/language-family.rkt` (SCHEME) | Magnitude: 8.82 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 12, branch: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `racket/collects/racket/contract/private/arrow-common.rkt` (SCHEME) | Magnitude: 152.94 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 354, branch: 81, args: 22, func_start: 22
- `racket/collects/racket/mutable-treelist.rkt` (SCHEME) | Magnitude: 174.88 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 357, args: 45, func_start: 45, branch: 39
- `racket/collects/syntax/parse/private/runtime-report.rkt` (SCHEME) | Magnitude: 187.12 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 447, branch: 69, args: 60, func_start: 60

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `racket/collects/net/head.rkt` (SCHEME) | Magnitude: 126.24 | Delta: **0.154** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 256, branch: 64, structural_boundaries: 47, args: 19

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/ci-pr.yml` -> Churn: **97.42%** | Cog Load: 0.0% | Debt: 99.8937%
- `.github/workflows/ci-push-x86_linux.yml` -> Churn: **97.42%** | Cog Load: 6.244% | Debt: 100.0%
- `.github/workflows/ci-push_macos.yml` -> Churn: **97.42%** | Cog Load: 4.8722% | Debt: 99.9993%
- `.github/workflows/ubsan-x86.yml` -> Churn: **77.95%** | Cog Load: 4.9177% | Debt: 100.0%
- `.github/workflows/ci-snapshot.yml` -> Churn: **71.38%** | Cog Load: 9.2053% | Debt: 62.2459%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `racket/collects/setup/private/pkg-deps.rkt` -> **Matthew Flatt** (100.0% isolated ownership) | Magnitude: 5544.42
- `racket/collects/net/git-checkout.rkt` -> **Matthew Flatt** (100.0% isolated ownership) | Magnitude: 2025.96
- `racket/collects/ffi/unsafe.rkt` -> **Matthew Flatt** (100.0% isolated ownership) | Magnitude: 1985.14
- `racket/collects/setup/setup-core.rkt` -> **Matthew Flatt** (100.0% isolated ownership) | Magnitude: 1866.22
- `racket/collects/racket/private/more-scheme.rkt` -> **Jade Sailor** (100.0% isolated ownership) | Magnitude: 1480.28

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `racket/collects/setup/setup-core.rkt` -> **Severity: 0.643** (Bridge: 0.042 * Flux: 15.3026%)
- `racket/collects/racket/file.rkt` -> **Severity: 0.552** (Bridge: 0.0476 * Flux: 11.6088%)
- `racket/collects/racket/list.rkt` -> **Severity: 0.548** (Bridge: 0.0249 * Flux: 22.0401%)
- `racket/collects/compiler/private/xform.rkt` -> **Severity: 0.543** (Bridge: 0.0234 * Flux: 23.2157%)
- `racket/collects/compiler/distribute.rkt` -> **Severity: 0.407** (Bridge: 0.0335 * Flux: 12.1567%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `racket/collects/racket/string.rkt` -> **Severity: 12.814** (Embedded: 0.2486 * Error Risk: 51.538%)
- `racket/collects/racket/list.rkt` -> **Severity: 10.86** (Embedded: 0.2114 * Error Risk: 51.383%)
- `racket/collects/racket/private/list.rkt` -> **Severity: 10.788** (Embedded: 0.2126 * Error Risk: 50.7334%)
- `racket/collects/compiler/private/xform.rkt` -> **Severity: 9.783** (Embedded: 0.1892 * Error Risk: 51.7136%)
- `racket/collects/racket/private/string.rkt` -> **Severity: 9.506** (Embedded: 0.1898 * Error Risk: 50.0862%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `racket/collects/racket/private/list-predicates.rkt` -> **Severity: 7771.1** (Blast Radius: 77.711 * Doc Risk: 100.0%)
- `racket/collects/compiler/private/elf.rkt` -> **Severity: 5260.2** (Blast Radius: 52.602 * Doc Risk: 100.0%)
- `racket/collects/racket/place/private/coercion.rkt` -> **Severity: 3511.2** (Blast Radius: 35.112 * Doc Risk: 100.0%)
- `racket/collects/db/private/generic/interfaces.rkt` -> **Severity: 3430.2** (Blast Radius: 34.302 * Doc Risk: 100.0%)
- `racket/collects/racket/string.rkt` -> **Severity: 2999.3** (Blast Radius: 29.993 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 288 literal sites + 1 sites through wrappers = 289
- **`panics_and_aborts`:** 712 literal sites + 1 sites through wrappers = 713

- `clean` (function, debug_prints, primitive): 1 call sites in 1 files -- `Makefile`
- `clean` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `Makefile`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 49108 call pairs -- scoped 6.6%, unique 8.4%, ambiguous 4.6%, external 80.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| scheme | 49093 | 6.6% | 8.4% | 4.6% | 80.4% |
| shell | 15 | 20.0% | 0.0% | 0.0% | 80.0% |

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
