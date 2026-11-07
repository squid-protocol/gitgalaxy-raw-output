# ARCHITECTURAL_BRIEF: ansible
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ansible/ansible` |
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
- **Scope:** 4673 analyzed artifact(s), 230500 LOC.
- **Load-bearing artifact:** `lib/ansible/module_utils/basic.py` -- 226 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `lib/ansible/module_utils/facts/default_collectors.py` -- pulls in 58 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `test/units/module_utils/urls/fixtures/client.key` at magnitude 5000.0 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 4673 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1149 |
| Total LOC | 230500 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 80.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6025 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1652 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.2991 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 145 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| YAML | 2070 | 53897 | 44.3% |
| PYTHON | 1767 | 147504 | 37.8% |
| SHELL | 251 | 4724 | 5.4% |
| POWERSHELL | 192 | 15138 | 4.1% |
| PLAINTEXT | 165 | 1 | 3.5% |
| JSON | 153 | 3341 | 3.3% |
| MARKDOWN | 31 | 0 | 0.7% |
| CSHARP | 17 | 5772 | 0.4% |
| M4 | 17 | 40 | 0.4% |
| CSV | 5 | 17 | 0.1% |
| BATCH | 3 | 5 | 0.1% |
| GO | 1 | 61 | 0.0% |
| XML | 1 | 0 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 4672 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 67%, Large Core Modules (2) 5%, Declarative / Non-Code 5%, Generic / Templated Code Files 5%, Parameter Forwarders Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4476 | 95.8% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 195 | 4.2% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1149*

**Composition by Extension & Reason:**
- `no_extension`: 537x Unsupported Format (.undeterminable), 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unresolved Ambiguity (No Retainable Structure)
- `.j2`: 91x Excluded (Unsupported Extension: '.j2'), 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Zero-Density Threshold (LOC: 54, Signals: 0), 4x Zero-Density Threshold (LOC: 52, Signals: 0)
- `.py`: 47x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 112 LOC)
- `.cfg`: 29x Excluded (Unsupported Extension: '.cfg'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 28x Excluded (Unsupported Extension: '.ini')
- `.sh`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stdout`: 24x Excluded (Unsupported Extension: '.stdout')
- `.stderr`: 20x Excluded (Unsupported Extension: '.stderr')
- `.md`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.expected`: 16x Excluded (Unsupported Extension: '.expected')
- `.output`: 15x Excluded (Unsupported Extension: '.output')
- `.json`: 15x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.template`: 13x Excluded (Unsupported Extension: '.template')
- `.pem`: 11x Excluded (Unsupported Extension: '.pem')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 9.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.1 | 22.4 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 5.6 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 12.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 89.2 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.5 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 80.5 | 2.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 24.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4972 | 816 | 2 | `lib/ansible/modules/user.py` |
| cleanup | 448 | 179 | 0 | `test/integration/targets/ansible-galaxy/runme.sh` |
| guards | 11932 | 1140 | 5 | `test/units/cli/test_galaxy.py` |
| danger | 7311 | 995 | 3 | `test/integration/targets/module_utils_Ansible.Basic/library/ansible_basic_tests.ps1` |
| concurrency | 621 | 209 | 0 | `test/integration/targets/ansible-galaxy/runme.sh` |
| connectivity | 11454 | 1514 | 5 | `test/support/windows-integration/plugins/module_utils/Ansible.Service.cs` |
| io | 7115 | 676 | 2 | `test/integration/targets/handlers/runme.sh` |
| crypto | 51 | 27 | 0 | `lib/ansible/_internal/_ssh/_ssh_agent.py` |
| ipc | 373 | 81 | 0 | `lib/ansible/plugins/connection/ssh.py` |
| time | 308 | 116 | 0 | `test/support/windows-integration/plugins/modules/win_wait_for.ps1` |
| serialization | 98 | 54 | 0 | `test/integration/targets/module_utils_Ansible.Become/library/ansible_become_tests.ps1` |
| regex | 1234 | 284 | 0 | `test/integration/targets/handlers/runme.sh` |
| events | 423 | 96 | 0 | `test/units/module_utils/urls/test_Request.py` |
| tests | 6007 | 372 | 0 | `test/units/_internal/templating/test_templar.py` |
| docs | 7958 | 1471 | 4 | `test/lib/ansible_test/_internal/host_profiles.py` |
| debt | 1948 | 632 | 1 | `test/integration/targets/ansible-vault/runme.sh` |
| mutation | 83959 | 2002 | 36 | `lib/ansible/modules/user.py` |
| dead_code | 3100 | 739 | 1 | `test/units/parsing/vault/test_vault.py` |
| credential | 166 | 41 | 0 | `test/integration/targets/ansible-vault/password-script.py` |
| threat | 74 | 17 | 0 | `test/units/module_utils/urls/test_channel_binding.py` |
| ml_ai | 14 | 7 | 0 | `test/support/windows-integration/plugins/modules/setup.ps1` |
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

1. **basic.py** (`lib/ansible/module_utils/basic.py`) — 226 inbound connections
2. **__init__.py** (`lib/ansible/errors/__init__.py`) — 220 inbound connections
3. **converters.py** (`lib/ansible/module_utils/common/text/converters.py`) — 207 inbound connections
4. **display.py** (`lib/ansible/utils/display.py`) — 175 inbound connections
5. **__init__.py** (`lib/ansible/__init__.py`) — 128 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **default_collectors.py** (`lib/ansible/module_utils/facts/default_collectors.py`) — 58 outbound dependencies
2. **__init__.py** (`lib/ansible/galaxy/collection/__init__.py`) — 54 outbound dependencies
3. **basic.py** (`lib/ansible/module_utils/basic.py`) — 47 outbound dependencies
4. **module_common.py** (`lib/ansible/executor/module_common.py`) — 45 outbound dependencies
5. **galaxy.py** (`lib/ansible/cli/galaxy.py`) — 44 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_validate_argument_spec` **(Many-Argument Workhorses)** (@ `test/lib/ansible_test/_util/controller/sanity/validate-modules/validate_modules/main.py`) -> Impact: **440.3** | LOC: 604
- `run_command` **(Many-Argument Workhorses)** (@ `lib/ansible/module_utils/basic.py`) -> Impact: **339.0** | LOC: 273
- `Add-CSharpType` **(Many-Argument Workhorses)** (@ `lib/ansible/module_utils/powershell/Ansible.ModuleUtils.AddType.psm1`) -> Impact: **277.1** | LOC: 450
  * *Intent:* # Copyright (c) 2018 Ansible Project # Simplified BSD License (see licenses/simplified_bsd.txt or https://opensource.org/licenses/BSD-2-Clause)
- `present` **(Many-Argument Workhorses)** (@ `lib/ansible/modules/lineinfile.py`) -> Impact: **273.8** | LOC: 211
- `Get-AnsibleWebRequest` **(Many-Argument Workhorses)** (@ `lib/ansible/module_utils/powershell/Ansible.ModuleUtils.WebRequest.psm1`) -> Impact: **237.5** | LOC: 350
  * *Intent:* # Copyright (c) 2019 Ansible Project # Simplified BSD License (see licenses/simplified_bsd.txt or https://opensource.org/licenses/BSD-2-Clause)
- `Get-AnsibleWindowsWebRequest` **(Many-Argument Workhorses)** (@ `test/support/windows-integration/collections/ansible_collections/ansible/windows/plugins/module_utils/WebRequest.psm1`) -> Impact: **237.3** | LOC: 346
  * *Intent:* # Copyright (c) 2020 Ansible Project # Simplified BSD License (see licenses/simplified_bsd.txt or https://opensource.org/licenses/BSD-2-Clause)
- `get_virtual_facts` **(Compute Cores)** (@ `lib/ansible/module_utils/facts/virtual/linux.py`) -> Impact: **215.1** | LOC: 371
  * *Intent:* # For more information, check: http://people.redhat.com/~rjones/virt-what/
- `get_config_value_and_origin` **(Many-Argument Workhorses)** (@ `lib/ansible/config/manager.py`) -> Impact: **211.8** | LOC: 155
  * *Intent:* """ Given a config key figure out the actual value and report on the origin of the settings """
- `_process_pending_results` **(Many-Argument Workhorses)** (@ `lib/ansible/plugins/strategy/__init__.py`) -> Impact: **204.5** | LOC: 244
  * *Intent:* """ Reads results off the final queue and takes appropriate action based on the result (executing callbacks, updating state, etc.). """
- `install` **(Many-Argument Workhorses)** (@ `lib/ansible/modules/apt.py`) -> Impact: **200.1** | LOC: 126

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib/ansible/modules` | 73 | 23962.58 | 36.29% | 8.53% |
| `test/lib/ansible_test/_internal` | 44 | 10911.86 | 17.34% | 0.0% |
| `lib/ansible/cli` | 11 | 7731.82 | 65.39% | 17.02% |
| `lib/ansible/plugins/action` | 29 | 5296.96 | 55.43% | 32.83% |
| `test/units/module_utils/urls/fixtures` | 3 | 5000.0 | 0.0% | 0.0% |
| `lib/ansible/executor` | 9 | 4817.56 | 57.84% | 16.9% |
| `lib/ansible/module_utils` | 15 | 4766.3 | 36.17% | 13.73% |
| `lib/ansible/playbook` | 20 | 4396.46 | 49.31% | 8.08% |
| `test/lib/ansible_test/_util/controller/sanity/validate-modules/validate_modules` | 7 | 3720.46 | 52.06% | 0.0% |
| `test/support/windows-integration/plugins/modules` | 35 | 3608.06 | 40.03% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lib/ansible/module_utils/_internal/_patches/_dataclass_annotation_patch.py` -> **100.0%** Exposure
- `lib/ansible/plugins/httpapi/__init__.py` -> **100.0%** Exposure
- `lib/ansible/utils/unsafe_proxy.py` -> **100.0%** Exposure
- `lib/ansible/utils/version.py` -> **100.0%** Exposure
- `lib/ansible/_internal/_plugins/_cache.py` -> **99.9999%** Exposure
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
- `test/integration/targets/user/tasks/test_create_user_password.yml` -> **100.0%** Exposure
- `test/integration/targets/ansible-vault/password-script.py` -> **100.0%** Exposure
- `test/units/modules/test_known_hosts.py` -> **100.0%** Exposure
- `test/integration/targets/become_unprivileged/setup_unpriv_users.yml` -> **99.9997%** Exposure
- `lib/ansible/modules/known_hosts.py` -> **99.6651%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `8660` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `test/units/module_utils/urls/fixtures/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.13
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/ansible/modules/user.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.131)
- **Top Global Matches:** file_cluster_8: 6.131, file_cluster_6: 12.177, file_cluster_4: 20.866
- **Magnitude:** 4195.94 | **LOC:** 3554 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 28.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.13; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.5%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 1`, `state_mutation: 973`, `planned_debt: 1`, `duplicate_logic: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 71`, `api: 68`, `import: 22`
* *Defense:* `safety: 43`, `doc: 25`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.13
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` __future__, ansible.module_utils, ansible.module_utils.basic, ansible.module_utils.common.locale, ansible.module_utils.common.sys_info, ansible.module_utils.common.text.converters, calendar, ctypes.util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/ansible_test/_util/controller/sanity/validate-modules/validate_modules/main.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.75)
- **Top Global Matches:** file_cluster_4: 7.75, file_cluster_6: 9.534, file_cluster_12: 13.621
- **Magnitude:** 2595.44 | **LOC:** 2648 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **36**; blast radius 0.24; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (93.0%), Guard Balance (formerly Safety Score) (70.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.8%), Connectivity (formerly Api Exposure) (25.4%)
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
* *Risk/State:* `safety_bypasses: 44`, `high_risk_execution: 5`, `state_mutation: 380`, `planned_debt: 6`, `duplicate_logic: 4`
* *Architecture:* `io: 48`, `api: 42`, `import: 34`
* *Defense:* `safety: 119`, `doc: 23`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.000211
  * `Imports (Out-Degree: 16):` .constants, .module_args, .schema, .utils, __future__, abc, ansible, ansible.executor.module_common...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/ansible/module_utils/basic.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.133)
- **Top Global Matches:** file_cluster_4: 8.133, file_cluster_6: 11.249, file_cluster_12: 11.818
- **Magnitude:** 2372.36 | **LOC:** 2211 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **226** in-repo importer(s); it depends on **47**; blast radius 19.173; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.7%), Complexity Load (formerly Cognitive Load) (75.6%)
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
* *Risk/State:* `safety_bypasses: 51`, `high_risk_execution: 4`, `state_mutation: 416`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 115`, `api: 60`, `import: 47`
* *Defense:* `safety: 122`, `doc: 29`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.173
  * `Choke Point (Betweenness):` 0.000619 | `Ripple Effect (Closeness):` 0.062423
  * `Imports (Out-Degree: 17):` ._internal, .common.text.converters, __future__, __main__, ansible.module_utils.common, ansible.module_utils.common._utils, ansible.module_utils.common.arg_spec, ansible.module_utils.common.file...
  * `Imported By (In-Degree: 226):` (Excluded from Brief to save tokens)

### `lib/ansible/cli/doc.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.577)
- **Top Global Matches:** file_cluster_4: 9.577, file_cluster_6: 9.618, file_cluster_12: 14.476
- **Magnitude:** 2172.62 | **LOC:** 1677 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **33**; blast radius 0.167; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.6%)
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
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 476`, `planned_debt: 11`
* *Architecture:* `io: 21`, `api: 20`, `concurrency: 1`, `import: 36`
* *Defense:* `safety: 39`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.167
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.000211
  * `Imports (Out-Degree: 22):` __future__, ansible, ansible._internal, ansible._internal._templating, ansible._internal._yaml._loader, ansible.cli, ansible.cli.arguments, ansible.collections.list...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/ansible/plugins/loader.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.545)
- **Top Global Matches:** file_cluster_4: 8.545, file_cluster_6: 11.264, file_cluster_5: 12.192
- **Magnitude:** 1916.36 | **LOC:** 1880 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **65** in-repo importer(s); it depends on **35**; blast radius 3.252; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (58.7%)
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
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 400`, `dead_code: 7`, `planned_debt: 13`, `fragile_debt: 19`
* *Architecture:* `io: 43`, `api: 38`, `import: 39`
* *Defense:* `safety: 67`, `doc: 39`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.252
  * `Choke Point (Betweenness):` 0.000441 | `Ripple Effect (Closeness):` 0.045483
  * `Imports (Out-Degree: 19):` .._internal._plugins, ._AnsiblePluginInfoMixin, .filter, .test, __future__, ansible, ansible._internal, ansible._internal._datatag...
  * `Imported By (In-Degree: 65):` (Excluded from Brief to save tokens)

### `lib/ansible/cli/galaxy.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.224)
- **Top Global Matches:** file_cluster_4: 7.224, file_cluster_6: 7.486, file_cluster_12: 14.018
- **Magnitude:** 1859.84 | **LOC:** 1890 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **44**; blast radius 0.628; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.2%), Complexity Load (formerly Cognitive Load) (65.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.628
  * `Choke Point (Betweenness):` 7.4e-05 | `Ripple Effect (Closeness):` 0.002304
  * `Imports (Out-Degree: 27):` __future__, ansible, ansible._internal._datatag._tags, ansible._internal._templating._engine, ansible.cli, ansible.cli.arguments, ansible.constants, ansible.errors...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `lib/ansible/galaxy/collection/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.681)
- **Top Global Matches:** file_cluster_6: 5.681, file_cluster_4: 9.354, file_cluster_8: 15.973
- **Magnitude:** 1750.46 | **LOC:** 1927 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **54**; blast radius 0.317; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.4%), Complexity Load (formerly Cognitive Load) (63.9%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.317
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.002799
  * `Imports (Out-Degree: 22):` __future__, ansible.constants, ansible.errors, ansible.galaxy.api, ansible.galaxy.collection.concrete_artifact_manager, ansible.galaxy.collection.galaxy_api_proxy, ansible.galaxy.collection.gpg, ansible.galaxy.dependency_resolution...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/ansible/modules/service.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.465)
- **Top Global Matches:** file_cluster_6: 6.465, file_cluster_8: 12.633, file_cluster_4: 12.989
- **Magnitude:** 1725.72 | **LOC:** 1613 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.13; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.6%)
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
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 4`, `state_mutation: 350`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 45`, `api: 53`, `import: 17`
* *Defense:* `safety: 4`, `doc: 12`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.13
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` __future__, ansible.module_utils.basic, ansible.module_utils.common.locale, ansible.module_utils.common.sys_info, ansible.module_utils.common.text.converters, ansible.module_utils.compat.version, ansible.module_utils.service, glob...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/ansible/executor/module_common.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.078)
- **Top Global Matches:** file_cluster_4: 8.078, file_cluster_5: 10.836, file_cluster_12: 11.092
- **Magnitude:** 1633.26 | **LOC:** 1695 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **45**; blast radius 0.394; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.1%)
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
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 2`, `state_mutation: 334`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 11`
* *Architecture:* `io: 32`, `api: 24`, `import: 50`
* *Defense:* `safety: 40`, `doc: 22`, `sync_locks: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.394
  * `Choke Point (Betweenness):` 0.000274 | `Ripple Effect (Closeness):` 0.029107
  * `Imports (Out-Degree: 30):` __future__, ansible, ansible._internal, ansible._internal._ansiballz, ansible._internal._datatag, ansible._internal._datatag._tags, ansible._internal._powershell, ansible._internal._templating._engine...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `lib/ansible/plugins/action/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.985)
- **Top Global Matches:** file_cluster_6: 6.985, file_cluster_4: 12.078, file_cluster_8: 14.605
- **Magnitude:** 1573.34 | **LOC:** 1509 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **67** in-repo importer(s); it depends on **37**; blast radius 4.519; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Guard Balance (formerly Safety Score) (83.6%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.7%)
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
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 290`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 6`
* *Architecture:* `io: 7`, `api: 16`, `concurrency: 1`, `import: 38`
* *Defense:* `safety: 40`, `doc: 31`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.519
  * `Choke Point (Betweenness):` 0.000514 | `Ripple Effect (Closeness):` 0.029735
  * `Imports (Out-Degree: 27):` .._AnsiblePluginInfoMixin, __future__, abc, ansible, ansible._internal._errors, ansible._internal._templating, ansible.errors, ansible.executor.interpreter_discovery...
  * `Imported By (In-Degree: 67):` (Excluded from Brief to save tokens)

### `lib/ansible/modules/apt.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.34)
- **Top Global Matches:** file_cluster_6: 7.34, file_cluster_8: 11.605, file_cluster_4: 14.474
- **Magnitude:** 1569.02 | **LOC:** 1626 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **23**; blast radius 0.24; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.2%)
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
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 264`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 17`, `api: 25`, `import: 22`
* *Defense:* `safety: 46`, `doc: 11`, `sync_locks: 2`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.000211
  * `Imports (Out-Degree: 6):` __future__, ansible.module_utils.basic, ansible.module_utils.common.file, ansible.module_utils.common.locale, ansible.module_utils.common.respawn, ansible.module_utils.common.text.converters, ansible.module_utils.urls, apt...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/ansible/modules/git.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.4)
- **Top Global Matches:** file_cluster_4: 7.4, file_cluster_6: 8.756, file_cluster_12: 13.513
- **Magnitude:** 1477.82 | **LOC:** 1438 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.13; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (65.6%)
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
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 249`, `dead_code: 1`, `fragile_debt: 4`
* *Architecture:* `io: 52`, `api: 36`, `import: 15`
* *Defense:* `safety: 17`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.13
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` __future__, ansible.module_utils.basic, ansible.module_utils.common.locale, ansible.module_utils.common.process, ansible.module_utils.common.text.converters, ansible.module_utils.compat.version, filecmp, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/ansible_test/_internal/commands/sanity/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.637)
- **Top Global Matches:** file_cluster_5: 9.637, file_cluster_4: 10.095, file_cluster_12: 11.186
- **Magnitude:** 1426.78 | **LOC:** 1317 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **29**; blast radius 0.809; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (82.9%), Complexity Load (formerly Cognitive Load) (53.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.5%), Connectivity (formerly Api Exposure) (10.8%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.809
  * `Choke Point (Betweenness):` 0.000118 | `Ripple Effect (Closeness):` 0.001949
  * `Imports (Out-Degree: 18):` ...ansible_util, ...config, ...constants, ...content_config, ...data, ...encoding, ...executor, ...host_configs...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `lib/ansible/plugins/strategy/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.655)
- **Top Global Matches:** file_cluster_4: 7.655, file_cluster_12: 10.333, file_cluster_5: 11.07
- **Magnitude:** 1395.48 | **LOC:** 1202 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **34**; blast radius 0.177; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.3%), Complexity Load (formerly Cognitive Load) (74.2%)
- **Documentation Coverage:** 56.1644% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_process_pending_results` **(Many-Argument Workhorses)** (Impact: 204.5)
    * *Intent:* """ Reads results off the final queue and takes appropriate action based on the result (executing ca...
  * `_execute_meta` **(Many-Argument Workhorses)** (Impact: 183.0)
  * `_queue_task` **(Many-Argument Workhorses)** (Impact: 48.1)
    * *Intent:* """ handles queueing the task up to be sent to a worker """
  * `inner` **(Many-Argument Workhorses)** (Impact: 34.4)
  * `search_handlers_by_notification` **(Many-Argument Workhorses)** (Impact: 28.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 169 instances
* *Api Near Db Sink:* 1 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 578
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 274`, `structural_boundaries: 182`, `args: 41`, `func_start: 41`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 3`, `state_mutation: 240`, `planned_debt: 2`
* *Architecture:* `io: 4`, `api: 33`, `concurrency: 4`, `import: 35`
* *Defense:* `safety: 46`, `doc: 20`, `sync_locks: 2`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.177
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.000843
  * `Imports (Out-Degree: 23):` __future__, ansible, ansible._internal._templating._engine, ansible.errors, ansible.executor.play_iterator, ansible.executor.process.worker, ansible.executor.task_queue_manager, ansible.executor.task_result...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib/ansible/module_utils/urls.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.787)
- **Top Global Matches:** file_cluster_4: 7.787, file_cluster_12: 10.791, file_cluster_6: 11.379
- **Magnitude:** 1315.38 | **LOC:** 1409 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **35**; blast radius 1.643; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.2%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (76.1%)
- **Documentation Coverage:** 72.9167% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `open` **(Many-Argument Workhorses)** (Impact: 106.1)
  * `fetch_url` **(Many-Argument Workhorses)** (Impact: 62.7)
  * `redirect_request` **(Many-Argument Workhorses)** (Impact: 62.4)
  * `_configure_auth` **(Many-Argument Workhorses)** (Impact: 50.9)
  * `http_error_401` **(Many-Argument Workhorses)** (Impact: 42.6)
    * *Intent:* # If we've already attempted the auth and we've reached this again then there was a failure. if self...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 181 instances
* *State Mutation (weighted view):* 624
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 215`, `args: 54`, `func_start: 54`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 262`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `io: 30`, `api: 51`, `import: 36`
* *Defense:* `safety: 47`, `doc: 38`, `test: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.643
  * `Choke Point (Betweenness):` 0.000171 | `Ripple Effect (Closeness):` 0.006019
  * `Imports (Out-Degree: 4):` __future__, ansible.module_utils.basic, ansible.module_utils.common.collections, ansible.module_utils.common.text.converters, base64, contextlib, cryptography, cryptography.exceptions...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `lib/ansible/utils/collection_loader/_collection_finder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.989)
- **Top Global Matches:** file_cluster_12: 6.989, file_cluster_16: 8.027, file_cluster_15: 9.002
- **Magnitude:** 1272.86 | **LOC:** 1275 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **24** in-repo importer(s); it depends on **20**; blast radius 2.106; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.6%), Guard Balance (formerly Safety Score) (83.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 90.2256% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 37.1)
    * *Intent:* """ Create an AnsibleCollectionRef from components :param collection_name: a collection name of the ...
  * `_get_loader` **(Stateful Encapsulated Methods)** (Impact: 30.0)
  * `_iter_modules_impl` **(Stateful Encapsulated Methods)** (Impact: 22.0)
    * *Intent:* # NB: this currently only iterates what's on disk- redirected modules are not considered if not pref...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 21.8)
    * *Intent:* # TODO: accept metadata loader override self._ansible_pkg_path = _to_text(os.path.dirname(_to_bytes(...
  * `_get_subpackage_search_paths` **(Stateful Encapsulated Methods)** (Impact: 21.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 198 instances
* *State Mutation (weighted view):* 633
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 256`, `args: 87`, `func_start: 87`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 3`, `state_mutation: 237`, `dead_code: 5`, `planned_debt: 9`, `fragile_debt: 11`, `duplicate_logic: 4`
* *Architecture:* `io: 71`, `api: 42`, `import: 18`
* *Defense:* `safety: 39`, `doc: 9`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.106
  * `Choke Point (Betweenness):` 7e-05 | `Ripple Effect (Closeness):` 0.035512
  * `Imports (Out-Degree: 4):` ._collection_config, ._collection_meta, ._to_bytes, ._to_text, __future__, contextlib, hook, importlib...
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `lib/ansible/plugins/connection/ssh.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.668)
- **Top Global Matches:** file_cluster_6: 8.668, file_cluster_4: 9.495, file_cluster_12: 15.656
- **Magnitude:** 1232.9 | **LOC:** 1626 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.13; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.1%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.1%)
- **Documentation Coverage:** 51.9231% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_bare_run` **(Many-Argument Workhorses)** (Impact: 166.7)
    * *Intent:* """ Starts the command and communicates with it until it ends. """
  * `_build_command` **(Many-Argument Workhorses)** (Impact: 70.0)
    * *Intent:* """ Takes an executable (ssh, scp, sftp or wrapper) and optional extra arguments and returns the rem...
  * `_handle_error` **(Many-Argument Workhorses)** (Impact: 58.7)
  * `_file_transport_command` **(Many-Argument Workhorses)** (Impact: 50.6)
    * *Intent:* # scp and sftp require square brackets for IPv6 addresses, but # accept them for hostnames and IPv4 ...
  * `_examine_output` **(Many-Argument Workhorses)** (Impact: 39.1)
    * *Intent:* # This is separate from _run() because we need to do the same thing for stdout # and stderr. """ Tak...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 184 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 583
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 144`, `args: 30`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 6`, `state_mutation: 215`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `io: 27`, `api: 14`, `concurrency: 1`, `import: 32`
* *Defense:* `safety: 24`, `doc: 18`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.13
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` __future__, ansible, ansible._internal._powershell, ansible._internal._ssh, ansible.errors, ansible.module_utils.common.text.converters, ansible.plugins.connection, ansible.utils.display...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/ansible/executor/task_executor.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.147)
- **Top Global Matches:** file_cluster_6: 9.147, file_cluster_8: 12.656, file_cluster_4: 15.681
- **Magnitude:** 1216.34 | **LOC:** 1277 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **35**; blast radius 0.198; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.2%)
- **Documentation Coverage:** 37.8378% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_execute_internal` **(Many-Argument Workhorses)** (Impact: 185.7)
    * *Intent:* """ The primary workhorse of the executor system, this runs the task on the specified host (which ma...
  * `_run_loop` **(Many-Argument Workhorses)** (Impact: 64.3)
    * *Intent:* """ Runs the task with the loop items specified and collates the result into an array named 'results...
  * `run` **(Defensive Guards)** (Impact: 52.8)
    * *Intent:* """ The main executor entrypoint, where we determine if the specified task requires looping and eith...
  * `_poll_async_result` **(Many-Argument Workhorses)** (Impact: 37.1)
    * *Intent:* """ Polls for the specified JID to be complete """
  * `start_connection` **(Many-Argument Workhorses)** (Impact: 33.2)
    * *Intent:* """ Starts the persistent connection """
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 198 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 650
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 142`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 1`, `state_mutation: 254`, `planned_debt: 7`, `fragile_debt: 7`
* *Architecture:* `io: 8`, `api: 6`, `concurrency: 4`, `import: 35`
* *Defense:* `safety: 51`, `doc: 14`, `sync_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.198
  * `Choke Point (Betweenness):` 0.000277 | `Ripple Effect (Closeness):` 0.032265
  * `Imports (Out-Degree: 30):` __future__, ansible, ansible._internal, ansible._internal._datatag, ansible._internal._datatag._tags, ansible._internal._errors, ansible._internal._templating._engine, ansible._internal._templating._jinja_plugins...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `test/lib/ansible_test/_internal/util.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.758)
- **Top Global Matches:** file_cluster_5: 8.758, file_cluster_12: 10.325, file_cluster_4: 10.685
- **Magnitude:** 1211.36 | **LOC:** 1256 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **91** in-repo importer(s); it depends on **32**; blast radius 6.319; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (78.5%), Complexity Load (formerly Cognitive Load) (18.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.9%)
- **Documentation Coverage:** 11.4035% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `raw_command` **(Many-Argument Workhorses)** (Impact: 183.7)
  * `find_executable` **(Many-Argument Workhorses)** (Impact: 49.4)
    * *Intent:* """ Find the specified executable and return the full path, or None if it could not be found. If req...
  * `communicate_with_process` **(Many-Argument Workhorses)** (Impact: 42.3)
  * `print_message` **(Many-Argument Workhorses)** (Impact: 28.3)
  * `detect_architecture` **(Defensive Guards)** (Impact: 25.1)
    * *Intent:* """Detect the architecture of the specified Python and return a normalized version, or None if it ca...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 157 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 515
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 205`, `args: 64`, `func_start: 63`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 2`, `state_mutation: 201`, `fragile_debt: 1`
* *Architecture:* `io: 74`, `api: 64`, `import: 32`
* *Defense:* `safety: 21`, `doc: 72`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.319
  * `Choke Point (Betweenness):` 0.000151 | `Ripple Effect (Closeness):` 0.019827
  * `Imports (Out-Degree: 6):` .constants, .encoding, .io, .locale_util, .thread, __future__, abc, ansible_release...
  * `Imported By (In-Degree: 91):` (Excluded from Brief to save tokens)

### `lib/ansible/module_utils/facts/system/distribution.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.578)
- **Top Global Matches:** file_cluster_4: 8.578, file_cluster_12: 9.695, file_cluster_7: 11.234
- **Magnitude:** 1162.76 | **LOC:** 743 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **8**; blast radius 0.694; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.7%), Complexity Load (formerly Cognitive Load) (82.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_distribution_file_Debian` **(Many-Argument Workhorses)** (Impact: 95.0)
  * `parse_distribution_file_SUSE` **(Many-Argument Workhorses)** (Impact: 71.9)
  * `parse_distribution_file_Amazon` **(Many-Argument Workhorses)** (Impact: 28.1)
  * `get_distribution_SunOS` **(Compute Cores)** (Impact: 23.5)
  * `parse_distribution_file_ClearLinux` **(Many-Argument Workhorses)** (Impact: 18.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 215 instances
* *State Mutation (weighted view):* 684
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 110`, `args: 32`, `func_start: 32`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 254`, `planned_debt: 6`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 6`, `api: 28`, `import: 8`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.694
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.001685
  * `Imports (Out-Degree: 3):` __future__, ansible.module_utils.common.sys_info, ansible.module_utils.facts.collector, ansible.module_utils.facts.utils, os, platform, re, typing
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `lib/ansible/module_utils/csharp/Ansible.Basic.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.714)
- **Top Global Matches:** file_cluster_4: 5.714, file_cluster_6: 10.682, file_cluster_16: 10.966
- **Magnitude:** 1159.6 | **LOC:** 1850 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **16**; blast radius 0.571; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.8%), Guard Balance (formerly Safety Score) (56.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CheckUnsupportedArguments` **(Many-Argument Workhorses)** (Impact: 40.3)
  * `ParseDict` **(Compute Cores)** (Impact: 36.7)
  * `ValidateArgumentSpec` **(Defensive Guards)** (Impact: 34.8)
  * `RemoveValueConditions` **(Many-Argument Workhorses)** (Impact: 34.4)
  * `CheckArguments` **(Many-Argument Workhorses)** (Impact: 31.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 121 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 402
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 159`, `args: 78`, `func_start: 63`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 160`, `unreferenced_by_name: 2`
* *Architecture:* `io: 19`, `api: 56`, `import: 16`
* *Defense:* `safety: 95`, `immutability_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000843
  * `Imports (Out-Degree: 0):` Microsoft.Win32.SafeHandles, System, System.Collections, System.Collections.Generic, System.ComponentModel, System.Diagnostics, System.IO, System.Linq...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/ansible/modules/unarchive.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.364)
- **Top Global Matches:** file_cluster_6: 8.364, file_cluster_4: 10.896, file_cluster_12: 16.812
- **Magnitude:** 1075.94 | **LOC:** 1179 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 0.24; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.3%), Complexity Load (formerly Cognitive Load) (83.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 82.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `is_unarchived` **(Many-Argument Workhorses)** (Impact: 124.6)
    * *Intent:* # BSD unzip doesn't support zipinfo listings with timestamp. if self.zipinfoflag: cmd = [self.zipinf...
  * `is_unarchived` **(Compute Cores)** (Impact: 33.8)
  * `main` **(I/O & Config Routines)** (Impact: 29.2)
  * `_valid_time_stamp` **(Stateful Encapsulated Methods)** (Impact: 28.8)
    * *Intent:* """ Return a valid time object from the given time string """
  * `files_in_archive` **(Compute Cores)** (Impact: 21.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 205 instances
* *State Mutation (weighted view):* 668
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 152`, `args: 26`, `func_start: 26`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 258`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 18`, `api: 21`, `import: 23`
* *Defense:* `safety: 44`, `doc: 8`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.000211
  * `Imports (Out-Degree: 5):` __future__, ansible.module_utils.basic, ansible.module_utils.common.locale, ansible.module_utils.common.process, ansible.module_utils.common.text.converters, ansible.module_utils.urls, binascii, codecs...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/ansible/module_utils/facts/hardware/linux.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.233)
- **Top Global Matches:** file_cluster_4: 9.233, file_cluster_6: 10.136, file_cluster_12: 13.609
- **Magnitude:** 1071.0 | **LOC:** 944 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **18**; blast radius 0.28; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.3%)
- **Documentation Coverage:** 86.0465% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_cpu_facts` **(Many-Argument Workhorses)** (Impact: 80.4)
  * `get_device_facts` **(Many-Argument Workhorses)** (Impact: 55.7)
  * `get_mount_facts` **(Compute Cores)** (Impact: 33.5)
  * `get_dmi_facts` **(Compute Cores)** (Impact: 26.3)
    * *Intent:* """ learn dmi facts from system Try /sys first for dmi related facts. If that is not available, fall...
  * `get_lvm_facts` **(Compute Cores)** (Impact: 17.1)
    * *Intent:* """ Get LVM Facts if running as root and lvm utils are available """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 215 instances
* *State Mutation (weighted view):* 699
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 116`, `args: 26`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 269`, `planned_debt: 1`
* *Architecture:* `io: 31`, `api: 18`, `import: 18`
* *Defense:* `safety: 31`, `doc: 5`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.28
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000843
  * `Imports (Out-Degree: 8):` __future__, ansible.module_utils._internal, ansible.module_utils._internal._concurrent, ansible.module_utils.common.locale, ansible.module_utils.common.text.converters, ansible.module_utils.common.text.formatters, ansible.module_utils.facts, ansible.module_utils.facts.hardware.base...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/ansible/module_utils/_embed/dnf.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.056)
- **Top Global Matches:** file_cluster_6: 8.056, file_cluster_4: 11.522, file_cluster_8: 16.624
- **Magnitude:** 1046.0 | **LOC:** 830 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.13; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%), Complexity Load (formerly Cognitive Load) (47.7%)
- **Documentation Coverage:** 6.0606% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_ensure_impl` **(Many-Argument Workhorses)** (Impact: 193.5)
    * *Intent:* """Core implementation of ensure logic."""
  * `_parse_spec_group_file` **(Many-Argument Workhorses)** (Impact: 43.4)
    * *Intent:* """Parse the names list into package specs, group specs, module specs, and filenames."""
  * `_mark_package_install` **(Defensive Guards)** (Impact: 38.4)
    * *Intent:* """Mark a package for installation."""
  * `_configure_base` **(Many-Argument Workhorses)** (Impact: 31.8)
    * *Intent:* """Configure the dnf Base object. Returns list of warnings."""
  * `_configure_repos` **(Stateful Encapsulated Methods)** (Impact: 21.0)
    * *Intent:* """Enable and disable repositories matching the provided patterns."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 162 instances
* *State Mutation (weighted view):* 521
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 119`, `args: 25`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `high_risk_execution: 1`, `state_mutation: 197`
* *Architecture:* `io: 6`, `api: 7`, `import: 10`
* *Defense:* `safety: 79`, `doc: 26`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.13
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dnf, dnf.const, dnf.exceptions, dnf.module.module_base, dnf.package, dnf.subject, dnf.util, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `test/lib/ansible_test/_internal/cli/parsers/__init__.py` (PYTHON) | Magnitude: 200.86 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 161, structural_boundaries: 84, generics: 50, doc: 38
- `test/units/_internal/test_event_formatting.py` (PYTHON) | Magnitude: 6.16 | Delta: **0.118** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 11, import: 6, state_mutation: 3
- `lib/ansible/galaxy/collection/gpg.py` (PYTHON) | Magnitude: 78.5 | Delta: **0.151** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 137, structural_boundaries: 60, core_var_decl: 25, design_snake_case: 23
- `test/integration/targets/test_utils/scripts/timeout.py` (PYTHON) | Magnitude: 16.04 | Delta: **0.157** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 11, core_var_decl: 8, design_snake_case: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `test/integration/targets/module_utils_Ansible.ModuleUtils.ArgvParser/library/argv_parser_test.ps1` (POWERSHELL) | Magnitude: 53.58 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 37, state_mutation: 24, branch: 6, closures: 3
- `test/integration/targets/win_app_control/ansible_collections/ns/col/plugins/modules/inline_signed.ps1` (POWERSHELL) | Magnitude: 13.64 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4, core_var_decl: 3, design_snake_case: 3, closures: 1
- `test/integration/targets/win_app_control/ansible_collections/ns/col/plugins/modules/inline_signed_not_trusted.ps1` (POWERSHELL) | Magnitude: 13.64 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4, core_var_decl: 3, design_snake_case: 3, closures: 1
- `test/integration/targets/win_app_control/ansible_collections/ns/col/plugins/modules/signed.ps1` (POWERSHELL) | Magnitude: 13.64 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4, core_var_decl: 3, design_snake_case: 3, closures: 1
- `test/integration/targets/win_app_control/ansible_collections/ns/invalid_manifest/plugins/modules/module.ps1` (POWERSHELL) | Magnitude: 13.64 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4, core_var_decl: 3, design_snake_case: 3, closures: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `test/units/plugins/inventory/test_constructed.py` (PYTHON) | Magnitude: 128.26 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 274, structural_boundaries: 64, core_var_decl: 53, design_snake_case: 53
- `test/integration/targets/ansible-test-config/ansible_collections/ns/col/tests/unit/plugins/module_utils/test_test.py` (PYTHON) | Magnitude: 2.18 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 6, import: 2, args: 1, func_start: 1
- `test/integration/targets/ansible-test-docker/ansible_collections/ns/col/tests/unit/plugins/module_utils/test_my_util.py` (PYTHON) | Magnitude: 2.18 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 6, import: 2, args: 1, func_start: 1
- `test/integration/targets/ansible-test-units/ansible_collections/ns/col/tests/unit/plugins/module_utils/test_my_util.py` (PYTHON) | Magnitude: 2.18 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 6, import: 2, args: 1, func_start: 1
- `test/integration/targets/ansible-test-units-constraints/ansible_collections/ns/col/tests/unit/plugins/modules/test_constraints.py` (PYTHON) | Magnitude: 2.18 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 5, import: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `lib/ansible/utils/helpers.py` (PYTHON) | Magnitude: 42.04 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 13, branch: 12, indent_spaces: 11, explicit_casts: 5
- `test/integration/targets/missing_required_lib/library/missing_required_lib.py` (PYTHON) | Magnitude: 21.34 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 9, state_mutation: 6, branch: 5
- `lib/ansible/_internal/_ssh/_agent_launch.py` (PYTHON) | Magnitude: 35.06 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 35, core_var_decl: 21, design_snake_case: 20
- `test/lib/ansible_test/_internal/provider/source/unversioned.py` (PYTHON) | Magnitude: 51.86 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 14, state_mutation: 12, branch: 9
- `test/lib/ansible_test/_util/controller/tools/collection_detail.py` (PYTHON) | Magnitude: 0.06 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 25, core_var_decl: 23, state_mutation: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `lib/ansible/executor/powershell/powershell_mkdtemp.ps1` (POWERSHELL) | Magnitude: 18.24 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 6, decorators: 3, state_mutation: 2, explicit_casts: 2
- `test/units/module_utils/urls/test_channel_binding.py` (PYTHON) | Magnitude: 18.94 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 63, sec_reflection_metaprogramming: 47, structural_boundaries: 16, import: 7
- `lib/ansible/module_utils/csharp/Ansible.AccessToken.cs` (CSHARP) | Magnitude: 245.52 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 396, api: 78, core_var_decl: 68, structural_boundaries: 59
- `test/units/module_utils/facts/network/test_iscsi_get_initiator.py` (PYTHON) | Magnitude: 8.1 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 27, test: 8, core_var_decl: 8, structural_boundaries: 7
- `test/units/module_utils/facts/test_utils.py` (PYTHON) | Magnitude: 12.42 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 11, test: 8, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `test/integration/targets/module_utils_distro/runme.sh` (SHELL) | Magnitude: 6.46 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: io: 9, structural_boundaries: 4, core_var_decl: 4, state_mutation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `test/units/galaxy/test_role_install.py` (PYTHON) | Magnitude: 79.2 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 93, structural_boundaries: 49, state_mutation: 29, test: 18
- `test/units/module_utils/facts/system/test_user.py` (PYTHON) | Magnitude: 6.9 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 6, state_mutation: 4, import: 3
- `test/integration/targets/ansiballz_python/ansible_collections/ansible_test/ansiballz_python/plugins/modules/embed_module_alias.py` (PYTHON) | Magnitude: 7.78 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 7, import: 3, core_var_decl: 3
- `test/units/galaxy/test_collection_install.py` (PYTHON) | Magnitude: 537.68 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 675, state_mutation: 272, core_var_decl: 258, design_snake_case: 258
- `test/integration/targets/ansible-test-sanity-use-compat-six/ansible_collections/ns/col/do-not-check-me.py` (PYTHON) | Magnitude: 2.18 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 5, import: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `test/units/plugins/connection/test_ssh.py` (PYTHON) | Magnitude: 272.06 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 428, state_mutation: 166, structural_boundaries: 113, core_var_decl: 64

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `lib/ansible/module_utils/facts/default_collectors.py` (PYTHON) | Magnitude: 25.6 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 118, import: 59, indent_spaces: 56, state_mutation: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `test/units/modules/test_apt.py` (PYTHON) | Magnitude: 5.64 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 8, test: 7, core_var_decl: 6
- `test/integration/targets/task-args/action_plugins/echo_raw.py` (PYTHON) | Magnitude: 6.24 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 4, core_var_decl: 3, design_snake_case: 3
- `test/integration/targets/ansiballz_python/ansible_collections/ansible_test/ansiballz_python/plugins/modules/embed_module_import.py` (PYTHON) | Magnitude: 7.78 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 7, import: 3, core_var_decl: 3
- `test/integration/targets/uri/files/testserver.py` (PYTHON) | Magnitude: 24.32 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 10, state_mutation: 5, branch: 4
- `test/lib/ansible_test/_util/controller/tools/yaml_to_json.py` (PYTHON) | Magnitude: 0.01 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 16, import: 7, indent_spaces: 5, safety: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `test/lib/ansible_test/_util/controller/sanity/pylint/plugins/deprecated_calls.py` (PYTHON) | Magnitude: 472.46 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 381, branch: 120, structural_boundaries: 98, core_var_decl: 91
- `lib/ansible/modules/group.py` (PYTHON) | Magnitude: 820.38 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 432, state_mutation: 184, branch: 136, structural_boundaries: 118
- `lib/ansible/cli/doc.py` (PYTHON) | Magnitude: 2172.62 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 1090, state_mutation: 476, core_var_decl: 382, branch: 373
- `lib/ansible/module_utils/facts/network/generic_bsd.py` (PYTHON) | Magnitude: 427.38 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 203, state_mutation: 81, branch: 74, structural_boundaries: 47
- `lib/ansible/plugins/connection/paramiko_ssh.py` (PYTHON) | Magnitude: 396.04 | Delta: **0.203** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 284, core_var_decl: 91, design_snake_case: 84, structural_boundaries: 83

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `lib/ansible/_internal/_yaml/_constructor.py` (PYTHON) | Magnitude: 161.84 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 143, structural_boundaries: 69, core_var_decl: 40, design_snake_case: 40
- `test/units/plugins/connection/test_paramiko_ssh.py` (PYTHON) | Magnitude: 19.22 | Delta: **0.158** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 44, indent_spaces: 29, safety: 12, import: 12
- `lib/ansible/inventory/data.py` (PYTHON) | Magnitude: 273.3 | Delta: **0.18** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 152, branch: 60, structural_boundaries: 47, state_mutation: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `test/lib/ansible_test/_internal/delegation.py` (PYTHON) | Magnitude: 281.22 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 227, structural_boundaries: 75, state_mutation: 53, branch: 49
- `test/lib/ansible_test/_internal/cli/compat.py` (PYTHON) | Magnitude: 575.78 | Delta: **0.191** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 336, core_var_decl: 121, branch: 118, design_snake_case: 114

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `lib/ansible/plugins/terminal/__init__.py` (PYTHON) | Magnitude: 32.06 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 25, args: 9, func_start: 9
- `test/integration/targets/ansible-test-units-forked/ansible_collections/ns/col/tests/unit/plugins/modules/test_ansible_forked.py` (PYTHON) | Magnitude: 14.3 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 10, test: 9, io: 8
- `test/integration/targets/inventory/inventory_plugins/constructed_with_hostvars.py` (PYTHON) | Magnitude: 28.46 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 17, indent_spaces: 17, core_var_decl: 10, design_snake_case: 8
- `test/units/_vendor/test_vendor.py` (PYTHON) | Magnitude: 37.64 | Delta: **0.122** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 28, indent_spaces: 26, test: 10, import: 10
- `lib/ansible/plugins/cliconf/__init__.py` (PYTHON) | Magnitude: 234.12 | Delta: **0.135** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 131, structural_boundaries: 67, branch: 32, state_mutation: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `test/sanity/code-smell/boilerplate.py` (PYTHON) | Magnitude: 43.92 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 21, branch: 13, state_mutation: 9
- `lib/ansible/utils/color.py` (PYTHON) | Magnitude: 84.16 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 45, branch: 24, structural_boundaries: 24, core_var_decl: 14
- `test/integration/targets/inventory_cache/plugins/inventory/cache_host.py` (PYTHON) | Magnitude: 51.14 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 10, state_mutation: 10, core_var_decl: 10
- `test/support/windows-integration/plugins/modules/win_file.ps1` (POWERSHELL) | Magnitude: 76.26 | Delta: **0.169** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 71, branch: 36, state_mutation: 22, closures: 19

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `lib/ansible/modules/user.py` -> Churn: **80.53%** | Cog Load: 72.6676% | Debt: 14.9217%
- `lib/ansible/plugins/action/__init__.py` -> Churn: **74.72%** | Cog Load: 61.2559% | Debt: 22.7251%
- `lib/ansible/executor/module_common.py` -> Churn: **67.12%** | Cog Load: 59.4204% | Debt: 29.7042%
- `lib/ansible/plugins/connection/ssh.py` -> Churn: **67.12%** | Cog Load: 63.4564% | Debt: 9.0799%
- `lib/ansible/cli/galaxy.py` -> Churn: **57.81%** | Cog Load: 64.9921% | Debt: 8.1031%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/ansible/module_utils/basic.py` -> **Felix Fontein** (100.0% isolated ownership) | Magnitude: 2372.36
- `lib/ansible/plugins/loader.py` -> **Matt Davis** (100.0% isolated ownership) | Magnitude: 1916.36
- `lib/ansible/modules/service.py` -> **zorun** (100.0% isolated ownership) | Magnitude: 1725.72
- `test/lib/ansible_test/_internal/commands/sanity/__init__.py` -> **Patrick Kingston** (100.0% isolated ownership) | Magnitude: 1426.78
- `lib/ansible/plugins/strategy/__init__.py` -> **Abhijeet Kasurde** (100.0% isolated ownership) | Magnitude: 1395.48

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/ansible/utils/display.py` -> **Severity: 0.275** (Bridge: 0.0027 * Flux: 100.0%)
- `lib/ansible/executor/task_queue_manager.py` -> **Severity: 0.12** (Bridge: 0.0012 * Flux: 100.0%)
- `lib/ansible/executor/process/worker.py` -> **Severity: 0.109** (Bridge: 0.0011 * Flux: 99.9875%)
- `lib/ansible/playbook/task.py` -> **Severity: 0.095** (Bridge: 0.0009 * Flux: 100.0%)
- `lib/ansible/module_utils/basic.py` -> **Severity: 0.062** (Bridge: 0.0006 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/ansible/module_utils/compat/typing.py` -> **Severity: 5.32** (Embedded: 0.0665 * Error Risk: 80.0%)
- `lib/ansible/module_utils/_internal/_datatag/__init__.py` -> **Severity: 5.3** (Embedded: 0.0663 * Error Risk: 80.0%)
- `lib/ansible/module_utils/basic.py` -> **Severity: 4.913** (Embedded: 0.0624 * Error Risk: 78.7111%)
- `lib/ansible/module_utils/_internal/__init__.py` -> **Severity: 4.855** (Embedded: 0.0939 * Error Risk: 51.7136%)
- `lib/ansible/module_utils/common/text/converters.py` -> **Severity: 4.614** (Embedded: 0.0946 * Error Risk: 48.7695%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/ansible/module_utils/common/text/converters.py` -> **Severity: 1389.569** (Blast Radius: 16.119 * Doc Risk: 86.2069%)
- `lib/ansible/module_utils/basic.py` -> **Severity: 1305.396** (Blast Radius: 19.173 * Doc Risk: 68.0851%)
- `lib/ansible/utils/display.py` -> **Severity: 968.155** (Blast Radius: 11.833 * Doc Risk: 81.8182%)
- `lib/ansible/errors/__init__.py` -> **Severity: 868.748** (Blast Radius: 11.342 * Doc Risk: 76.5957%)
- `lib/ansible/plugins/__init__.py` -> **Severity: 793.835** (Blast Radius: 8.582 * Doc Risk: 92.5%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1015 literal sites + 12 sites through wrappers = 1027
- **`panics_and_aborts`:** 2702 literal sites + 6 sites through wrappers = 2708

- `info` (function, debug_prints, primitive): 9 call sites in 1 files -- `hacking/create-bulk-issues.py`
- `_unhexlify` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `lib/ansible/parsing/vault/__init__.py`
- `read_file` (function, debug_prints, primitive): 2 call sites in 1 files -- `test/sanity/code-smell/ansible-requirements.py`
- `function_catches_all_exceptions` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `test/units/module_utils/facts/test_timeout.py`
- `jdump` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `lib/ansible/cli/doc.py`
- `prompt_add` (function, debug_prints, primitive): 1 call sites in 1 files -- `hacking/backport/backport_of_line_adder.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 42605 call pairs -- scoped 36.8%, unique 0.1%, ambiguous 18.1%, external 45.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 40626 | 37.7% | 0.0% | 18.9% | 43.5% |
| csharp | 1001 | 34.7% | 0.0% | 3.9% | 61.4% |
| shell | 720 | 3.8% | 0.0% | 0.0% | 96.2% |
| powershell | 247 | 5.3% | 11.3% | 0.0% | 83.4% |
| go | 11 | 36.4% | 0.0% | 0.0% | 63.6% |

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
