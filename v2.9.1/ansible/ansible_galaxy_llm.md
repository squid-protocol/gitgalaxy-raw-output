# ARCHITECTURAL_BRIEF: ansible
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ansible/ansible` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 4698 analyzed artifact(s), 231992 LOC.
- **Load-bearing artifact:** `lib/ansible/module_utils/compat/typing.py` -- 318 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `lib/ansible/executor/module_common.py` -- pulls in 72 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `test/units/module_utils/urls/fixtures/cbt/ecdsa_sha256.pem` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 5822 |
| Analyzed Artifacts (Scanned) | 4698 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1124 |
| Total LOC | 231992 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 80.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5571 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2104 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.7287 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 120 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| YAML | 2080 | 55567 | 44.3% |
| PYTHON | 1766 | 147365 | 37.6% |
| SHELL | 251 | 4724 | 5.3% |
| POWERSHELL | 192 | 15138 | 4.1% |
| PLAINTEXT | 177 | 12 | 3.8% |
| JSON | 152 | 3290 | 3.2% |
| MARKDOWN | 35 | 0 | 0.7% |
| CSHARP | 17 | 5772 | 0.4% |
| M4 | 17 | 40 | 0.4% |
| CSV | 5 | 17 | 0.1% |
| BATCH | 3 | 5 | 0.1% |
| GO | 1 | 61 | 0.0% |
| XML | 1 | 0 | 0.0% |
| BINARY_THREAT | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `8.142`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +8.14; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 68%, Large Core Modules (2) 5%, Declarative / Non-Code 5%, Generic / Templated Code Files 4%, Parameter Forwarders Files 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4484 | 95.4% |
| Unknown | 13 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 200 | 4.3% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1124*

**Composition by Extension & Reason:**
- `no_extension`: 541x Unsupported Format (.undeterminable), 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unresolved Ambiguity (No Retainable Structure)
- `.j2`: 130x Excluded (Unsupported Extension: '.j2')
- `.yml`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Zero-Density Threshold (LOC: 54, Signals: 0), 4x Zero-Density Threshold (LOC: 52, Signals: 0)
- `.py`: 47x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 189 LOC), 1x Excluded (Machine-Generated Source Code Signature: 112 LOC)
- `.cfg`: 31x Excluded (Unsupported Extension: '.cfg')
- `.ini`: 28x Excluded (Unsupported Extension: '.ini')
- `.sh`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stdout`: 24x Excluded (Unsupported Extension: '.stdout')
- `.stderr`: 20x Excluded (Unsupported Extension: '.stderr')
- `.expected`: 16x Excluded (Unsupported Extension: '.expected')
- `.json`: 15x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 52 LOC)
- `.output`: 15x Excluded (Unsupported Extension: '.output')
- `.md`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.template`: 13x Excluded (Unsupported Extension: '.template')
- `.txt`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable), 1x Excluded: Neighborhood Micro-Mass Limit Exceeded

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 9.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 27.4 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 5.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 12.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 89.2 | 0.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.0 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 69.4 | 2.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 24.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5266 | 819 | 2 | `lib/ansible/modules/user.py` |
| cleanup | 448 | 179 | 0 | `test/integration/targets/ansible-galaxy/runme.sh` |
| guards | 11912 | 1139 | 4 | `test/units/cli/test_galaxy.py` |
| danger | 7312 | 996 | 3 | `test/integration/targets/module_utils_Ansible.Basic/library/ansible_basic_tests.ps1` |
| concurrency | 621 | 209 | 0 | `test/integration/targets/ansible-galaxy/runme.sh` |
| connectivity | 11446 | 1512 | 5 | `test/support/windows-integration/plugins/module_utils/Ansible.Service.cs` |
| io | 7115 | 676 | 2 | `test/integration/targets/handlers/runme.sh` |
| crypto | 28 | 25 | 0 | `lib/ansible/module_utils/urls.py` |
| ipc | 373 | 81 | 0 | `lib/ansible/plugins/connection/ssh.py` |
| time | 308 | 116 | 0 | `test/support/windows-integration/plugins/modules/win_wait_for.ps1` |
| serialization | 98 | 54 | 0 | `test/integration/targets/module_utils_Ansible.Become/library/ansible_become_tests.ps1` |
| regex | 1233 | 283 | 0 | `test/integration/targets/handlers/runme.sh` |
| events | 422 | 95 | 0 | `test/units/module_utils/urls/test_Request.py` |
| tests | 6007 | 372 | 0 | `test/units/_internal/templating/test_templar.py` |
| docs | 7988 | 1473 | 4 | `test/lib/ansible_test/_internal/host_profiles.py` |
| debt | 1945 | 631 | 1 | `test/integration/targets/ansible-vault/runme.sh` |
| mutation | 83865 | 2004 | 36 | `lib/ansible/modules/user.py` |
| dead_code | 3474 | 856 | 1 | `test/units/parsing/vault/test_vault.py` |
| credential | 163 | 39 | 0 | `test/integration/targets/ansible-vault/password-script.py` |
| threat | 2129 | 404 | 0 | `test/units/galaxy/test_api.py` |
| ml_ai | 108 | 25 | 0 | `test/units/cli/test_cli.py` |
| ui | 94 | 26 | 0 | `lib/ansible/_internal/_templating/_jinja_bits.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/integration/targets/handlers/runme.sh` (Hits: 191)
- `test/integration/targets/ansible-doc/runme.sh` (Hits: 143)
- `test/integration/targets/meta_tasks/runme.sh` (Hits: 132)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **typing.py** (`lib/ansible/module_utils/compat/typing.py`) — 318 inbound connections
2. **basic.py** (`lib/ansible/module_utils/basic.py`) — 218 inbound connections
3. **converters.py** (`lib/ansible/module_utils/common/text/converters.py`) — 207 inbound connections
4. **json.py** (`lib/ansible/module_utils/common/json.py`) — 171 inbound connections
5. **display.py** (`lib/ansible/utils/display.py`) — 151 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **module_common.py** (`lib/ansible/executor/module_common.py`) — 72 outbound dependencies
2. **default_collectors.py** (`lib/ansible/module_utils/facts/default_collectors.py`) — 58 outbound dependencies
3. **__init__.py** (`lib/ansible/galaxy/collection/__init__.py`) — 55 outbound dependencies
4. **basic.py** (`lib/ansible/module_utils/basic.py`) — 47 outbound dependencies
5. **galaxy.py** (`lib/ansible/cli/galaxy.py`) — 45 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_validate_argument_spec` **(Many-Argument Workhorses)** (@ `test/lib/ansible_test/_util/controller/sanity/validate-modules/validate_modules/main.py`) -> Impact: **440.3** | LOC: 604
- `run_command` **(Many-Argument Workhorses)** (@ `lib/ansible/module_utils/basic.py`) -> Impact: **339.0** | LOC: 273
- `Add-CSharpType` **(Many-Argument Workhorses)** (@ `lib/ansible/module_utils/powershell/Ansible.ModuleUtils.AddType.psm1`) -> Impact: **277.1** | LOC: 450
  * *Intent:* # Copyright (c) 2018 Ansible Project # Simplified BSD License (see licenses/simplified_bsd.txt or https://opensource.org/licenses/BSD-2-Clause)
- `present` **(Many-Argument Workhorses)** (@ `lib/ansible/modules/lineinfile.py`) -> Impact: **273.8** | LOC: 211
- `get_virtual_facts` **(Compute Cores)** (@ `lib/ansible/module_utils/facts/virtual/linux.py`) -> Impact: **215.1** | LOC: 371
  * *Intent:* # For more information, check: http://people.redhat.com/~rjones/virt-what/
- `get_config_value_and_origin` **(Many-Argument Workhorses)** (@ `lib/ansible/config/manager.py`) -> Impact: **211.8** | LOC: 155
  * *Intent:* """ Given a config key figure out the actual value and report on the origin of the settings """
- `_process_pending_results` **(Many-Argument Workhorses)** (@ `lib/ansible/plugins/strategy/__init__.py`) -> Impact: **204.5** | LOC: 244
  * *Intent:* """ Reads results off the final queue and takes appropriate action based on the result (executing callbacks, updating state, etc.). """
- `install` **(Many-Argument Workhorses)** (@ `lib/ansible/modules/apt.py`) -> Impact: **200.1** | LOC: 126
- `get_vars` **(Many-Argument Workhorses)** (@ `lib/ansible/vars/manager.py`) -> Impact: **194.5** | LOC: 286
- `_ensure_impl` **(Many-Argument Workhorses)** (@ `lib/ansible/module_utils/_embed/dnf.py`) -> Impact: **193.5** | LOC: 270
  * *Intent:* """Core implementation of ensure logic."""

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `test/units/module_utils/urls/fixtures/cbt` | 10 | 50000.0 | 0.0% | 0.0% |
| `lib/ansible/modules` | 73 | 23962.58 | 36.29% | 9.76% |
| `test/lib/ansible_test/_internal` | 44 | 10906.76 | 17.34% | 0.0% |
| `test/units/module_utils/urls/fixtures` | 4 | 10000.0 | 0.0% | 0.0% |
| `lib/ansible/cli` | 11 | 7731.82 | 65.39% | 20.73% |
| `lib/ansible/plugins/action` | 29 | 5296.96 | 55.43% | 43.62% |
| `lib/ansible/executor` | 9 | 4817.56 | 57.84% | 18.83% |
| `lib/ansible/module_utils` | 15 | 4766.3 | 36.17% | 16.97% |
| `lib/ansible/playbook` | 20 | 4396.46 | 49.31% | 10.26% |
| `test/lib/ansible_test/_util/controller/sanity/validate-modules/validate_modules` | 7 | 3720.46 | 52.06% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lib/ansible/_internal/_plugins/_cache.py` -> **100.0%** Exposure
- `lib/ansible/module_utils/_internal/_patches/_dataclass_annotation_patch.py` -> **100.0%** Exposure
- `lib/ansible/plugins/httpapi/__init__.py` -> **100.0%** Exposure
- `lib/ansible/utils/unsafe_proxy.py` -> **100.0%** Exposure
- `lib/ansible/utils/version.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `hacking/azp/download.py` -> **100.0%** Exposure
- `hacking/azp/get_recent_coverage_runs.py` -> **100.0%** Exposure
- `hacking/azp/incidental.py` -> **100.0%** Exposure
- `hacking/backport/backport_of_line_adder.py` -> **100.0%** Exposure
- `hacking/report.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/units/parsing/vault/test_vault.py` -> **87** Orphaned Functions | **0** Duplicates
- `test/units/_internal/templating/test_templar.py` -> **82** Orphaned Functions | **4** Duplicates
- `test/units/cli/test_galaxy.py` -> **71** Orphaned Functions | **9** Duplicates
- `test/units/playbook/test_base.py` -> **53** Orphaned Functions | **0** Duplicates
- `test/units/galaxy/test_collection.py` -> **51** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `test/integration/targets/ansible-vault/password-script.py` -> **100.0%** Exposure
- `test/units/modules/test_known_hosts.py` -> **100.0%** Exposure
- `test/integration/targets/user/tasks/test_create_user_password.yml` -> **99.9986%** Exposure
- `lib/ansible/modules/known_hosts.py` -> **99.6651%** Exposure
- `test/lib/ansible_test/_internal/ssh.py` -> **99.3923%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `8830` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `test/units/module_utils/urls/fixtures/cbt/ecdsa_sha256.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/units/module_utils/urls/fixtures/cbt/ecdsa_sha512.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/units/module_utils/urls/fixtures/cbt/rsa-pss_sha256.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/units/module_utils/urls/fixtures/cbt/rsa-pss_sha512.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/units/module_utils/urls/fixtures/cbt/rsa_md5.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/units/module_utils/urls/fixtures/cbt/rsa_sha.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/units/module_utils/urls/fixtures/cbt/rsa_sha1.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/units/module_utils/urls/fixtures/cbt/rsa_sha256.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/units/module_utils/urls/fixtures/cbt/rsa_sha384.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/units/module_utils/urls/fixtures/cbt/rsa_sha512.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/units/module_utils/urls/fixtures/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/units/module_utils/urls/fixtures/client.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/ansible/modules/user.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 4195.94 | **LOC:** 3554 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 28.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.7%)
- **Documentation Coverage:** 88.1481% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `modify_user_usermod` **(Compute Cores)** (Impact: 107.2)
  * `create_user_useradd` **(Compute Cores)** (Impact: 80.9)
  * `modify_user` **(Compute Cores)** (Impact: 76.3)
  * `modify_user_usermod` **(Compute Cores)** (Impact: 65.0)
  * `modify_user` **(Compute Cores)** (Impact: 61.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 854 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 2681
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 803`, `structural_boundaries: 335`, `args: 71`, `func_start: 71`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 1`, `state_mutation: 973`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 71`, `api: 68`, `import: 22`
* *Defense:* `safety: 43`, `doc: 25`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` __future__, ansible.module_utils, ansible.module_utils.basic, ansible.module_utils.common.locale, ansible.module_utils.common.sys_info, ansible.module_utils.common.text.converters, calendar, ctypes.util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/ansible_test/_util/controller/sanity/validate-modules/validate_modules/main.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2595.44 | **LOC:** 2648 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **36**; blast radius 0.271; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (93.2%), Complexity Load (formerly Cognitive Load) (93.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.3%), Connectivity (formerly Api Exposure) (25.4%)
- **Documentation Coverage:** 73.5043% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_validate_argument_spec` **(Many-Argument Workhorses)** (Impact: 440.3)
  * `_validate_docs` **(Many-Argument Workhorses)** (Impact: 97.8)
  * `_validate_required_if` **(Many-Argument Workhorses)** (Impact: 76.5)
  * `validate` **(Compute Cores)** (Impact: 63.9)
  * `_ensure_imports_below_docs` **(Many-Argument Workhorses)** (Impact: 49.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 330 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 1040
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 621`, `structural_boundaries: 421`, `args: 81`, `func_start: 81`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 44`, `high_risk_execution: 5`, `state_mutation: 380`, `dead_code: 1`, `planned_debt: 6`, `duplicate_logic: 4`
* *Architecture:* `io: 48`, `api: 42`, `import: 34`
* *Defense:* `safety: 119`, `doc: 23`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.271
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.00021
  * `Imports (Out-Degree: 14):` .constants, .module_args, .schema, .utils, __future__, abc, ansible, ansible.executor.module_common...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/ansible/module_utils/basic.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2372.36 | **LOC:** 2211 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **218** in-repo importer(s); it depends on **47**; blast radius 20.202; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.6%)
- **Documentation Coverage:** 68.0851% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_command` **(Many-Argument Workhorses)** (Impact: 339.0)
  * `atomic_move` **(Many-Argument Workhorses)** (Impact: 81.8)
    * *Intent:* """atomically move src to dest, copying attributes from dest, returns true on success it uses os.ren...
  * `set_mode_if_different` **(Many-Argument Workhorses)** (Impact: 62.4)
  * `_get_octal_mode_from_symbolic_perms` **(Many-Argument Workhorses)** (Impact: 62.1)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 46.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 327 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 1070
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 379`, `structural_boundaries: 328`, `args: 76`, `func_start: 74`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 51`, `high_risk_execution: 4`, `state_mutation: 416`, `dead_code: 5`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 115`, `api: 60`, `import: 47`
* *Defense:* `safety: 122`, `doc: 29`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 20.202
  * `Choke Point (Betweenness):` 0.001749 | `Ripple Effect (Closeness):` 0.048691
  * `Imports (Out-Degree: 21):` ._internal, .common.text.converters, __future__, __main__, ansible.module_utils.common, ansible.module_utils.common._utils, ansible.module_utils.common.arg_spec, ansible.module_utils.common.file...
  * `Imported By (In-Degree: 218):` (Excluded from Brief to save tokens)

### `lib/ansible/cli/doc.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2172.62 | **LOC:** 1677 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **33**; blast radius 0.209; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.6%)
- **Documentation Coverage:** 74.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_fields` **(Many-Argument Workhorses)** (Impact: 129.6)
  * `get_man_text` **(Many-Argument Workhorses)** (Impact: 69.5)
    * *Intent:* # Create a copy so we don't modify the original doc = dict(doc) DocCLI.IGNORE = DocCLI.IGNORE + (con...
  * `run` **(Compute Cores)** (Impact: 69.0)
  * `get_role_man_text` **(Many-Argument Workhorses)** (Impact: 48.0)
    * *Intent:* """Generate text for the supplied role suitable for display. This is similar to get_man_text(), but ...
  * `_add_seealso` **(Many-Argument Workhorses)** (Impact: 46.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 383 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 1242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 373`, `structural_boundaries: 239`, `args: 51`, `func_start: 49`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 476`, `dead_code: 3`, `planned_debt: 11`
* *Architecture:* `io: 21`, `api: 20`, `concurrency: 1`, `import: 36`
* *Defense:* `safety: 39`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.209
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.00021
  * `Imports (Out-Degree: 15):` __future__, ansible, ansible._internal, ansible._internal._templating, ansible._internal._yaml._loader, ansible.cli, ansible.cli.arguments, ansible.collections.list...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/ansible/plugins/loader.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1916.36 | **LOC:** 1880 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **55** in-repo importer(s); it depends on **39**; blast radius 3.268; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.1%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (59.6%)
- **Documentation Coverage:** 57.3913% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_find_fq_plugin` **(Many-Argument Workhorses)** (Impact: 77.4)
  * `_resolve_plugin_step` **(Many-Argument Workhorses)** (Impact: 70.1)
  * `all` **(Many-Argument Workhorses)** (Impact: 67.5)
    * *Intent:* """ Iterate through all plugins of this type, in configured paths (no collections) A plugin loader i...
  * `get_with_context` **(Many-Argument Workhorses)** (Impact: 65.2)
    * *Intent:* # FUTURE: now that the resulting plugins are closer, refactor base class method with some extra # ho...
  * `_find_plugin_legacy` **(Many-Argument Workhorses)** (Impact: 58.9)
    * *Intent:* """Search library and various *_plugins paths in order to find the file. This was behavior prior to ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 296 instances
* *State Mutation (weighted view):* 992
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 307`, `args: 63`, `func_start: 62`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 400`, `dead_code: 12`, `planned_debt: 13`, `fragile_debt: 19`
* *Architecture:* `io: 43`, `api: 38`, `import: 39`
* *Defense:* `safety: 67`, `doc: 39`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.268
  * `Choke Point (Betweenness):` 0.000694 | `Ripple Effect (Closeness):` 0.053783
  * `Imports (Out-Degree: 13):` , .._internal._plugins, .filter, .test, __future__, ansible, ansible._internal, ansible._internal._datatag...
  * `Imported By (In-Degree: 55):` (Excluded from Brief to save tokens)

### `lib/ansible/cli/galaxy.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1859.84 | **LOC:** 1890 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **45**; blast radius 0.834; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.0%)
- **Documentation Coverage:** 58.2524% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_install_options` **(Many-Argument Workhorses)** (Impact: 87.8)
  * `_parse_requirements_file` **(Many-Argument Workhorses)** (Impact: 66.4)
    * *Intent:* """ Parses an Ansible requirement.yml file and returns all the roles and/or collections defined in i...
  * `execute_init` **(Compute Cores)** (Impact: 66.3)
    * *Intent:* """ Creates the skeleton framework of a role or collection that complies with the Galaxy metadata fo...
  * `_execute_install_role` **(Many-Argument Workhorses)** (Impact: 64.7)
  * `execute_install` **(Many-Argument Workhorses)** (Impact: 54.6)
    * *Intent:* """ Install one or more roles(``ansible-galaxy role install``), or one or more collections(``ansible...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 269 instances
* *State Mutation (weighted view):* 904
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 393`, `structural_boundaries: 299`, `args: 58`, `func_start: 57`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 366`, `planned_debt: 2`
* *Architecture:* `io: 62`, `api: 46`, `import: 40`
* *Defense:* `safety: 20`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 6.2e-05 | `Ripple Effect (Closeness):` 0.002297
  * `Imports (Out-Degree: 21):` __future__, a, ansible, ansible._internal._datatag._tags, ansible._internal._templating._engine, ansible.cli, ansible.cli.arguments, ansible.constants...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `lib/ansible/galaxy/collection/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1750.46 | **LOC:** 1927 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **55**; blast radius 0.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.9%)
- **Documentation Coverage:** 83.1325% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `install_collections` **(Many-Argument Workhorses)** (Impact: 145.5)
    * *Intent:* % (api.name, api.api_server, import_uri))
  * `_resolve_depenency_map` **(Many-Argument Workhorses)** (Impact: 110.8)
  * `verify_local_collection` **(Many-Argument Workhorses)** (Impact: 80.7)
    * *Intent:* # type: (Candidate, t.Optional[Candidate], ConcreteArtifactsManager) -> CollectionVerifyResult """Ve...
  * `verify_collections` **(Many-Argument Workhorses)** (Impact: 67.7)
  * `verify_file_signatures` **(Many-Argument Workhorses)** (Impact: 58.0)
    * *Intent:* # type: (str, str, list[str], str, str, list[str]) -> bool successful = 0 error_messages = [] signat...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 188 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 674
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 300`, `args: 52`, `func_start: 51`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 298`, `planned_debt: 1`, `fragile_debt: 14`
* *Architecture:* `io: 100`, `api: 27`, `concurrency: 3`, `import: 51`
* *Defense:* `safety: 52`, `doc: 20`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` __future__, ansible.constants, ansible.errors, ansible.galaxy.api, ansible.galaxy.collection.concrete_artifact_manager, ansible.galaxy.collection.galaxy_api_proxy, ansible.galaxy.collection.gpg, ansible.galaxy.dependency_resolution...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/ansible/modules/service.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1725.72 | **LOC:** 1613 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `service_enable` **(Compute Cores)** (Impact: 123.8)
  * `execute_command` **(Many-Argument Workhorses)** (Impact: 48.4)
    * *Intent:* # =========================================== # Generic methods that should be used on all platforms...
  * `get_service_status` **(Compute Cores)** (Impact: 42.6)
  * `service_control` **(Compute Cores)** (Impact: 40.1)
    * *Intent:* # Decide what command to run svc_cmd = '' arguments = self.arguments if self.svc_cmd: if not self.sv...
  * `get_service_tools` **(Compute Cores)** (Impact: 36.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 309 instances
* *State Mutation (weighted view):* 968
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 391`, `structural_boundaries: 155`, `args: 47`, `func_start: 46`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 4`, `state_mutation: 350`, `dead_code: 6`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 45`, `api: 53`, `import: 17`
* *Defense:* `safety: 4`, `doc: 12`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` __future__, ansible.module_utils.basic, ansible.module_utils.common.locale, ansible.module_utils.common.sys_info, ansible.module_utils.common.text.converters, ansible.module_utils.compat.version, ansible.module_utils.service, glob...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/ansible/executor/module_common.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1633.26 | **LOC:** 1695 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **72**; blast radius 0.467; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.1%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.8%)
- **Documentation Coverage:** 77.4648% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_find_module_utils` **(Many-Argument Workhorses)** (Impact: 144.6)
  * `recursive_finder` **(Many-Argument Workhorses)** (Impact: 98.4)
  * `modify_module` **(Many-Argument Workhorses)** (Impact: 60.3)
  * `visit_ImportFrom` **(Many-Argument Workhorses)** (Impact: 43.6)
    * *Intent:* """ Handle from ansible.module_utils.MODLIB import [.MODLIBn] [as asname] Also has to handle relativ...
  * `_get_shebang` **(Many-Argument Workhorses)** (Impact: 43.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 257 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 848
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 259`, `args: 49`, `func_start: 49`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 2`, `state_mutation: 334`, `dead_code: 11`, `planned_debt: 2`, `fragile_debt: 11`
* *Architecture:* `io: 32`, `api: 24`, `import: 50`
* *Defense:* `safety: 40`, `doc: 22`, `sync_locks: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.467
  * `Choke Point (Betweenness):` 0.000665 | `Ripple Effect (Closeness):` 0.033205
  * `Imports (Out-Degree: 22):` , ..., ...executor, .module, AnsibleModule, IDENTIFIER, MODULEn, __future__...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `lib/ansible/plugins/action/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1573.34 | **LOC:** 1509 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 57.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **39**; blast radius 0.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.3%), Mutation Surface (formerly State Flux) (95.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.4%)
- **Documentation Coverage:** 34.4262% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_execute_module` **(Many-Argument Workhorses)** (Impact: 185.9)
  * `_fixup_perms2` **(Many-Argument Workhorses)** (Impact: 87.4)
    * *Intent:* """ We need the files we upload to be readable (and sometimes executable) by the user being sudo'd t...
  * `_get_diff_data` **(Many-Argument Workhorses)** (Impact: 80.5)
    * *Intent:* # Note: Since we do not diff the source and destination before we transform from bytes into # text t...
  * `_low_level_execute_command` **(Many-Argument Workhorses)** (Impact: 73.4)
    * *Intent:* # FIXME: move to connection base
  * `_configure_module` **(Many-Argument Workhorses)** (Impact: 51.7)
    * *Intent:* """ Handles the loading and templating of the module code through the modify_module() function. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 226 instances
* *State Mutation (weighted view):* 742
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 185`, `args: 39`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 290`, `dead_code: 12`, `planned_debt: 4`, `fragile_debt: 6`
* *Architecture:* `io: 7`, `api: 16`, `concurrency: 1`, `import: 38`
* *Defense:* `safety: 40`, `doc: 31`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` .., __future__, abc, ansible, ansible._internal._errors, ansible._internal._templating, ansible.errors, ansible.executor.interpreter_discovery...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/ansible/modules/apt.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1569.02 | **LOC:** 1626 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **24**; blast radius 0.271; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.2%)
- **Documentation Coverage:** 70.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `install` **(Many-Argument Workhorses)** (Impact: 200.1)
  * `upgrade` **(Many-Argument Workhorses)** (Impact: 137.6)
  * `install_deb` **(Many-Argument Workhorses)** (Impact: 102.1)
  * `main` **(I/O & Config Routines)** (Impact: 81.8)
  * `remove` **(Many-Argument Workhorses)** (Impact: 63.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 223 instances
* *State Mutation (weighted view):* 710
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 282`, `structural_boundaries: 144`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 264`, `dead_code: 11`, `fragile_debt: 1`
* *Architecture:* `io: 17`, `api: 25`, `import: 22`
* *Defense:* `safety: 46`, `doc: 11`, `sync_locks: 2`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.271
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.00021
  * `Imports (Out-Degree: 7):` C, __future__, ansible.module_utils.basic, ansible.module_utils.common.file, ansible.module_utils.common.locale, ansible.module_utils.common.respawn, ansible.module_utils.common.text.converters, ansible.module_utils.urls...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/ansible/modules/git.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1477.82 | **LOC:** 1438 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (65.6%)
- **Documentation Coverage:** 55.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clone` **(Many-Argument Workhorses)** (Impact: 114.8)
  * `main` **(I/O & Config Routines)** (Impact: 78.3)
    * *Intent:* # ===========================================
  * `fetch` **(Many-Argument Workhorses)** (Impact: 72.3)
    * *Intent:* """ updates repo from remote sources """
  * `switch_version` **(Many-Argument Workhorses)** (Impact: 47.0)
  * `get_remote_head` **(Many-Argument Workhorses)** (Impact: 44.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 215 instances
* *State Mutation (weighted view):* 679
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 150`, `args: 37`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 249`, `dead_code: 11`, `fragile_debt: 4`
* *Architecture:* `io: 52`, `api: 36`, `import: 15`
* *Defense:* `safety: 17`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` __future__, ansible.module_utils.basic, ansible.module_utils.common.locale, ansible.module_utils.common.process, ansible.module_utils.common.text.converters, ansible.module_utils.compat.version, filecmp, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/ansible_test/_internal/commands/sanity/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1426.78 | **LOC:** 1317 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 0.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.2%), Complexity Load (formerly Cognitive Load) (53.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.8%), Connectivity (formerly Api Exposure) (10.8%)
- **Documentation Coverage:** 9.4017% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `command_sanity` **(Compute Cores)** (Impact: 117.7)
    * *Intent:* """Run sanity tests."""
  * `__init__` **(Many-Argument Workhorses)** (Impact: 100.8)
  * `test_script` **(Many-Argument Workhorses)** (Impact: 55.9)
    * *Intent:* """Run the sanity test and return the result."""
  * `filter_targets` **(Compute Cores)** (Impact: 49.9)
    * *Intent:* """Return the given list of test targets, filtered to include only those relevant for the test."""
  * `create_sanity_virtualenv` **(Many-Argument Workhorses)** (Impact: 35.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 219 instances
* *State Mutation (weighted view):* 710
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 227`, `args: 65`, `func_start: 62`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 272`, `planned_debt: 1`, `duplicate_logic: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 33`, `api: 68`, `import: 29`
* *Defense:* `safety: 20`, `doc: 69`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` ...ansible_util, ...config, ...constants, ...content_config, ...data, ...encoding, ...executor, ...host_configs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `lib/ansible/plugins/action/__init__.py` -> Churn: **69.41%** | Cog Load: 61.2559% | Debt: 23.7598%
- `lib/ansible/modules/user.py` -> Churn: **64.46%** | Cog Load: 72.6676% | Debt: 15.3456%
- `lib/ansible/executor/module_common.py` -> Churn: **59.81%** | Cog Load: 59.4204% | Debt: 30.691%
- `lib/ansible/modules/apt.py` -> Churn: **53.72%** | Cog Load: 68.1642% | Debt: 9.2754%
- `lib/ansible/plugins/connection/psrp.py` -> Churn: **53.72%** | Cog Load: 64.95% | Debt: 65.7721%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/ansible/cli/doc.py` -> **Felix Fontein** (100.0% isolated ownership) | Magnitude: 2172.62
- `lib/ansible/modules/service.py` -> **zorun** (100.0% isolated ownership) | Magnitude: 1725.72
- `test/lib/ansible_test/_internal/commands/sanity/__init__.py` -> **Patrick Kingston** (100.0% isolated ownership) | Magnitude: 1426.78
- `lib/ansible/module_utils/csharp/Ansible.Basic.cs` -> **Jordan Borean** (100.0% isolated ownership) | Magnitude: 1322.2
- `lib/ansible/utils/collection_loader/_collection_finder.py` -> **sivel / Matt Martz** (100.0% isolated ownership) | Magnitude: 1272.86

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/ansible/galaxy/dependency_resolution/dataclasses.py` -> **Severity: 0.275** (Bridge: 0.0027 * Flux: 99.9997%)
- `lib/ansible/utils/display.py` -> **Severity: 0.21** (Bridge: 0.0021 * Flux: 100.0%)
- `lib/ansible/module_utils/basic.py` -> **Severity: 0.175** (Bridge: 0.0017 * Flux: 100.0%)
- `lib/ansible/playbook/task.py` -> **Severity: 0.149** (Bridge: 0.0015 * Flux: 100.0%)
- `lib/ansible/galaxy/api.py` -> **Severity: 0.12** (Bridge: 0.0012 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/ansible/module_utils/compat/typing.py` -> **Severity: 9.393** (Embedded: 0.1144 * Error Risk: 82.1378%)
- `lib/ansible/module_utils/facts/system/platform.py` -> **Severity: 6.182** (Embedded: 0.062 * Error Risk: 99.6455%)
- `lib/ansible/utils/display.py` -> **Severity: 6.143** (Embedded: 0.0641 * Error Risk: 95.8315%)
- `lib/ansible/galaxy/dependency_resolution/dataclasses.py` -> **Severity: 5.969** (Embedded: 0.0669 * Error Risk: 89.2073%)
- `test/lib/ansible_test/_internal/util.py` -> **Severity: 5.539** (Embedded: 0.0565 * Error Risk: 98.0503%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/ansible/module_utils/common/text/converters.py` -> **Severity: 1706.466** (Blast Radius: 19.795 * Doc Risk: 86.2069%)
- `lib/ansible/module_utils/basic.py` -> **Severity: 1375.455** (Blast Radius: 20.202 * Doc Risk: 68.0851%)
- `lib/ansible/utils/display.py` -> **Severity: 927.164** (Blast Radius: 11.332 * Doc Risk: 81.8182%)
- `lib/ansible/galaxy/dependency_resolution/dataclasses.py` -> **Severity: 769.259** (Blast Radius: 8.308 * Doc Risk: 92.5926%)
- `lib/ansible/_internal/_templating/_datatag.py` -> **Severity: 464.925** (Blast Radius: 6.199 * Doc Risk: 75.0%)

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
