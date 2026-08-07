# ARCHITECTURAL_BRIEF: pyasn1
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/pyasn1` |
| **Timestamp** | `2026-08-07T05:25:09.531641+00:00` |
| **Scan Duration** | `0.42s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 65 malicious artifacts.

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
| Total Artifacts | 74 |
| Analyzed Artifacts (Scanned) | 68 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6 |
| Total LOC | 13272 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 91.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2383 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0617 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3442 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 65 | 13272 | 95.6% |
| MARKDOWN | 2 | 0 | 2.9% |
| PLAINTEXT | 1 | 0 | 1.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.832`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 44 | 64.7% |
| file_cluster_13 | 17 | 25.0% |
| file_cluster_0 | 3 | 4.4% |
| file_cluster_7 | 1 | 1.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 4.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6*

**Composition by Extension & Reason:**
- `.rst`: 3x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 1.5 | 52.7 | 13.9 | 5.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 83.6 | 24.4 | 4.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 28.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 17.6 | 0.0 | 0.0 |
| API Exposure | 0.0 | 13.0 | 4.3 | 2.5 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 27.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 5.7 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 70.6 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 97.9 | 19.6 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pyasn1-0.6.3/tests/codec/ber/test_decoder.py` (Hits: 19)
- `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py` (Hits: 12)
- `pyasn1-0.6.3/pyasn1/codec/streaming.py` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **base.py** (`pyasn1-0.6.3/tests/base.py`) — 18 inbound connections
2. **error.py** (`pyasn1-0.6.3/pyasn1/error.py`) — 13 inbound connections
3. **streaming.py** (`pyasn1-0.6.3/pyasn1/codec/streaming.py`) — 2 inbound connections
4. **integer.py** (`pyasn1-0.6.3/pyasn1/compat/integer.py`) — 1 inbound connections
5. **MANIFEST.in** (`pyasn1-0.6.3/MANIFEST.in`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_decoder.py** (`pyasn1-0.6.3/tests/codec/ber/test_decoder.py`) — 12 outbound dependencies
2. **decoder.py** (`pyasn1-0.6.3/pyasn1/codec/ber/decoder.py`) — 10 outbound dependencies
3. **test_univ.py** (`pyasn1-0.6.3/tests/type/test_univ.py`) — 8 outbound dependencies
4. **encoder.py** (`pyasn1-0.6.3/pyasn1/codec/ber/encoder.py`) — 7 outbound dependencies
5. **test_useful.py** (`pyasn1-0.6.3/tests/type/test_useful.py`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `fromBinaryString` (@ `pyasn1-0.6.3/pyasn1/type/univ.py`) -> Impact: **879.7** | LOC: 1762
- `valueDecoder` (@ `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py`) -> Impact: **462.3** | LOC: 455
- `__call__` (@ `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py`) -> Impact: **388.2** | LOC: 428
- `encodeValue` (@ `pyasn1-0.6.3/pyasn1/codec/ber/encoder.py`) -> Impact: **350.7** | LOC: 597
- `valueDecoder` (@ `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py`) -> Impact: **182.1** | LOC: 226
- `valueDecoder` (@ `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py`) -> Impact: **106.9** | LOC: 115
- `valueDecoder` (@ `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py`) -> Impact: **103.8** | LOC: 115
- `valueDecoder` (@ `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py`) -> Impact: **91.6** | LOC: 125
- `encodeLength` (@ `pyasn1-0.6.3/pyasn1/codec/ber/encoder.py`) -> Impact: **84.5** | LOC: 131
- `valueDecoder` (@ `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py`) -> Impact: **77.9** | LOC: 103

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `pyasn1-0.6.3/pyasn1/type` | 12 | 2420.18 | 28.32% | 68.18% |
| `pyasn1-0.6.3/pyasn1/codec/ber` | 4 | 2359.16 | 16.05% | 37.42% |
| `pyasn1-0.6.3/tests/codec/ber` | 4 | 2153.4 | 4.79% | 0.0% |
| `pyasn1-0.6.3/tests/type` | 10 | 1900.82 | 6.78% | 0.0% |
| `pyasn1-0.6.3/tests/codec/cer` | 4 | 702.8 | 6.47% | 0.0% |
| `pyasn1-0.6.3/tests/codec/der` | 4 | 502.68 | 6.6% | 0.0% |
| `pyasn1-0.6.3/pyasn1/codec/native` | 3 | 236.22 | 23.48% | 66.67% |
| `pyasn1-0.6.3/pyasn1/codec/cer` | 3 | 229.4 | 18.27% | 66.35% |
| `pyasn1-0.6.3/tests/codec/native` | 4 | 174.9 | 5.34% | 0.0% |
| `pyasn1-0.6.3/pyasn1/codec` | 2 | 114.52 | 11.36% | 48.2% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `pyasn1-0.6.3/pyasn1/codec/native/encoder.py` -> **100.0%** Exposure
- `pyasn1-0.6.3/pyasn1/error.py` -> **100.0%** Exposure
- `pyasn1-0.6.3/pyasn1/type/constraint.py` -> **100.0%** Exposure
- `pyasn1-0.6.3/pyasn1/type/namedval.py` -> **100.0%** Exposure
- `pyasn1-0.6.3/pyasn1/type/opentype.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `pyasn1-0.6.3/pyasn1/type/opentype.py` -> **99.9998%** Exposure
- `pyasn1-0.6.3/pyasn1/codec/ber/eoo.py` -> **99.8151%** Exposure
- `pyasn1-0.6.3/pyasn1/type/tag.py` -> **99.7819%** Exposure
- `pyasn1-0.6.3/pyasn1/debug.py` -> **99.6997%** Exposure
- `pyasn1-0.6.3/pyasn1/type/tagmap.py` -> **99.6112%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pyasn1-0.6.3/tests/type/test_univ.py` -> **83** Orphaned Functions | **215** Duplicates
- `pyasn1-0.6.3/tests/codec/ber/test_decoder.py` -> **99** Orphaned Functions | **181** Duplicates
- `pyasn1-0.6.3/tests/codec/ber/test_encoder.py` -> **37** Orphaned Functions | **194** Duplicates
- `pyasn1-0.6.3/tests/codec/cer/test_encoder.py` -> **15** Orphaned Functions | **103** Duplicates
- `pyasn1-0.6.3/tests/codec/der/test_encoder.py` -> **19** Orphaned Functions | **45** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`pyasn1-0.6.3/pyasn1/codec/ber/decoder.py`** -> AI Confidence: **99.39%**
2. **`pyasn1-0.6.3/pyasn1/codec/ber/encoder.py`** -> AI Confidence: **99.31%**
3. **`pyasn1-0.6.3/pyasn1/type/useful.py`** -> AI Confidence: **99.09%**
4. **`pyasn1-0.6.3/tests/codec/ber/test_decoder.py`** -> AI Confidence: **99.08%**
5. **`pyasn1-0.6.3/tests/type/test_univ.py`** -> AI Confidence: **99.08%**
6. **`pyasn1-0.6.3/tests/type/test_useful.py`** -> AI Confidence: **99.08%**
7. **`pyasn1-0.6.3/pyasn1/codec/cer/encoder.py`** -> AI Confidence: **99.06%**
8. **`pyasn1-0.6.3/pyasn1/compat/integer.py`** -> AI Confidence: **99.06%**
9. **`pyasn1-0.6.3/tests/codec/__main__.py`** -> AI Confidence: **99.06%**
10. **`pyasn1-0.6.3/tests/codec/ber/__main__.py`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `189` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pyasn1-0.6.3/pyasn1/debug.py` (PYTHON) -> Cumulative Risk: **633.76**
- **Archetype:** `file_cluster_8` (Distance: 10.618 IQR)
- **Magnitude:** 81.28 | **LOC:** 147 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.6997%), Tech Debt (98.8049%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 32.0), `__str__` (Impact: 14.0), `__init__` (Impact: 1.8)

### 2. `pyasn1-0.6.3/pyasn1/type/base.py` (PYTHON) -> Cumulative Risk: **598.56**
- **Archetype:** `file_cluster_13` (Distance: 11.637 IQR)
- **Magnitude:** 261.74 | **LOC:** 700 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.7814%), State Flux (99.0885%), Verification (80.0%)
- **Heaviest Functions:** `__setattr__` (Impact: 48.6), `__init__` (Impact: 41.5), `__repr__` (Impact: 14.6)

### 3. `pyasn1-0.6.3/pyasn1/codec/cer/encoder.py` (PYTHON) -> Cumulative Risk: **590.33**
- **Archetype:** `file_cluster_8` (Distance: 9.591 IQR)
- **Magnitude:** 180.02 | **LOC:** 332 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.5741%), State Flux (82.9719%), Documentation (82.349%)
- **Heaviest Functions:** `encodeValue` (Impact: 67.1), `encodeValue` (Impact: 34.6), `_componentSortKey` (Impact: 12.9)

### 4. `pyasn1-0.6.3/pyasn1/codec/native/encoder.py` (PYTHON) -> Cumulative Risk: **585.73**
- **Archetype:** `file_cluster_8` (Distance: 9.923 IQR)
- **Magnitude:** 133.5 | **LOC:** 286 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (97.9352%), Verification (80.0%)
- **Heaviest Functions:** `__call__` (Impact: 19.9), `encode` (Impact: 14.1), `__init__` (Impact: 11.3)

### 5. `pyasn1-0.6.3/pyasn1/type/useful.py` (PYTHON) -> Cumulative Risk: **568.62**
- **Archetype:** `file_cluster_13` (Distance: 10.807 IQR)
- **Magnitude:** 90.68 | **LOC:** 191 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (94.5711%), Documentation (88.1848%), Verification (80.0%)
- **Heaviest Functions:** `asDateTime` (Impact: 56.0), `__init__` (Impact: 2.1), `utcoffset` (Impact: 1.8)

### 6. `pyasn1-0.6.3/pyasn1/type/namedval.py` (PYTHON) -> Cumulative Risk: **560.53**
- **Archetype:** `file_cluster_8` (Distance: 11.234 IQR)
- **Magnitude:** 103.76 | **LOC:** 193 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (83.0752%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 32.5), `getValues` (Impact: 5.6), `__repr__` (Impact: 3.9)

### 7. `pyasn1-0.6.3/pyasn1/codec/streaming.py` (PYTHON) -> Cumulative Risk: **558.37**
- **Archetype:** `file_cluster_13` (Distance: 11.288 IQR)
- **Magnitude:** 104.0 | **LOC:** 235 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (96.4066%), State Flux (94.1179%), Verification (80.0%)
- **Heaviest Functions:** `readFromStream` (Impact: 15.1), `peekIntoStream` (Impact: 14.9), `asSeekableStream` (Impact: 13.2)

### 8. `pyasn1-0.6.3/pyasn1/codec/native/decoder.py` (PYTHON) -> Cumulative Risk: **549.94**
- **Archetype:** `file_cluster_8` (Distance: 9.866 IQR)
- **Magnitude:** 92.2 | **LOC:** 245 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), State Flux (89.4145%), Verification (80.0%)
- **Heaviest Functions:** `__call__` (Impact: 19.8), `__init__` (Impact: 11.3), `__call__` (Impact: 7.9)

### 9. `pyasn1-0.6.3/pyasn1/type/tag.py` (PYTHON) -> Cumulative Risk: **549.67**
- **Archetype:** `file_cluster_7` (Distance: 11.414 IQR)
- **Magnitude:** 117.86 | **LOC:** 336 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7819%), Tech Debt (97.4899%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 27.4), `tagExplicitly` (Impact: 7.3), `__getitem__` (Impact: 5.4)

### 10. `pyasn1-0.6.3/pyasn1/type/opentype.py` (PYTHON) -> Cumulative Risk: **546.98**
- **Archetype:** `file_cluster_8` (Distance: 12.205 IQR)
- **Magnitude:** 34.36 | **LOC:** 105 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9998%), Safety Score (83.5755%)
- **Heaviest Functions:** `__init__` (Impact: 6.3), `name` (Impact: 1.8), `values` (Impact: 1.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.677 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.082 IQR)
- **Top Global Matches:** file_cluster_8: 10.677, file_cluster_7: 10.881, file_cluster_13: 10.89
- **Magnitude:** 1713.16 | **LOC:** 2226 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.833%), Tech Debt (83.4998%)
**Top Internal Functions/Classes:**
  * `valueDecoder` (Impact: 462.3)
  * `__call__` (Impact: 388.2)
  * `valueDecoder` (Impact: 182.1)
  * `valueDecoder` (Impact: 106.9)
  * `valueDecoder` (Impact: 103.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 465`, `structural_boundaries: 179`, `args: 35`, `func_start: 35`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 40`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 3`, `duplicate_logic: 12`, `orphaned_logic: 1`
* *Architecture:* `io: 12`, `api: 61`, `import: 19`
* *Defense:* `safety: 76`, `doc: 14`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pyasn1, sys, io, pyasn1.compat, os, pyasn1.type, warnings, pyasn1.error...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/type/univ.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.247 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.965 IQR)
- **Top Global Matches:** file_cluster_8: 12.247, file_cluster_7: 12.378, file_cluster_0: 12.432
- **Magnitude:** 1278.74 | **LOC:** 3328 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.5316%), Tech Debt (26.1416%)
**Top Internal Functions/Classes:**
  * `fromBinaryString` (Impact: 879.7)
  * `prettyIn` (Impact: 70.8)
  * `isValue` (Impact: 5.6)
  * `__round__` (Impact: 5.5)
  * `__init__` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 392`, `structural_boundaries: 622`, `args: 245`, `func_start: 245`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 89`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 11`
* *Architecture:* `api: 115`, `import: 11`
* *Defense:* `safety: 118`, `doc: 128`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1, pyasn1.compat, sys, pyasn1.type, math, pyasn1.codec.ber
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/codec/ber/test_decoder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.295 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.695 IQR)
- **Top Global Matches:** file_cluster_8: 13.295, file_cluster_13: 13.526, file_cluster_0: 13.552
- **Magnitude:** 1267.38 | **LOC:** 2339 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.7211%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testErrorMessageContainsLimit` (Impact: 34.5)
    * *Intent:* # Each \x30\x80 opens a new indefinite-length SEQUENCE
  * `testZipfile` (Impact: 11.0)
  * `testZipfileMany` (Impact: 11.0)
  * `testInvalidFileContent` (Impact: 9.4)
  * `testOneObject` (Impact: 9.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 826`, `args: 316`, `func_start: 290`, `class_start: 48`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 58`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 181`, `orphaned_logic: 99`
* *Architecture:* `io: 19`, `api: 330`, `import: 18`
* *Defense:* `safety: 523`, `doc: 58`, `test: 385`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest, pyasn1, tempfile, sys, io, zipfile, gzip, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/type/test_univ.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.145 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.441 IQR)
- **Top Global Matches:** file_cluster_8: 13.145, file_cluster_0: 13.43, file_cluster_13: 13.474
- **Magnitude:** 1212.62 | **LOC:** 2207 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.8815%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testSubtypeSpec` (Impact: 11.4)
  * `testGetItem` (Impact: 9.8)
  * `testSetItem` (Impact: 9.8)
  * `testComponentConstraintsMatching` (Impact: 9.6)
  * `testComponentConstraintsMatching` (Impact: 9.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 977`, `args: 298`, `func_start: 298`, `class_start: 67`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 65`, `fragile_debt: 16`, `duplicate_logic: 215`, `orphaned_logic: 83`
* *Architecture:* `io: 2`, `api: 365`, `import: 14`
* *Defense:* `safety: 585`, `test: 536`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` unittest, platform, sys, pyasn1.type, pickle, pyasn1.error, math, tests.base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/codec/ber/test_encoder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.181 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.631 IQR)
- **Top Global Matches:** file_cluster_8: 12.181, file_cluster_13: 12.602, file_cluster_0: 12.623
- **Magnitude:** 861.86 | **LOC:** 1528 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.4453%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testEmpty` (Impact: 5.6)
  * `testEmpty` (Impact: 5.6)
  * `testEmpty` (Impact: 5.6)
  * `testImpossible1` (Impact: 5.5)
  * `testImpossible2` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 510`, `args: 231`, `func_start: 231`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 78`, `duplicate_logic: 194`, `orphaned_logic: 37`
* *Architecture:* `io: 5`, `api: 270`, `import: 10`
* *Defense:* `safety: 219`, `test: 198`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` unittest, pyasn1.type, sys, pyasn1.error, tests.base, pyasn1.codec.ber
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/codec/ber/encoder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.889 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.723 IQR)
- **Top Global Matches:** file_cluster_8: 9.889, file_cluster_13: 10.386, file_cluster_7: 10.52
- **Magnitude:** 626.0 | **LOC:** 955 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.3546%), Tech Debt (66.1667%)
**Top Internal Functions/Classes:**
  * `encodeValue` (Impact: 350.7)
  * `encodeLength` (Impact: 84.5)
  * `encodeValue` (Impact: 63.7)
  * `encodeValue` (Impact: 39.4)
  * `encodeTag` (Impact: 10.9)
    * *Intent:* # noinspection PyMethodMayBeStatic
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 115`, `args: 25`, `func_start: 25`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 28`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 34`, `import: 11`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pyasn1, pyasn1.compat.integer, pyasn1.compat, sys, pyasn1.type, warnings, pyasn1.codec.ber
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/codec/cer/test_encoder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.433 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.489 IQR)
- **Top Global Matches:** file_cluster_8: 12.433, file_cluster_13: 12.612, file_cluster_0: 12.683
- **Magnitude:** 527.36 | **LOC:** 956 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.8931%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testLocalTimezone` (Impact: 5.6)
    * *Intent:* # def testExtraZeroInSeconds(self): # try: # assert encoder.encode( # useful.GeneralizedTime('201505...
  * `testMissingTimezone` (Impact: 5.6)
  * `testDecimalCommaPoint` (Impact: 5.6)
  * `testFractionOfSecond` (Impact: 5.6)
  * `testMissingTimezone` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 283`, `args: 122`, `func_start: 122`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 112`, `dead_code: 2`, `duplicate_logic: 103`, `orphaned_logic: 15`
* *Architecture:* `io: 5`, `api: 125`, `import: 10`
* *Defense:* `safety: 111`, `test: 94`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` unittest, pyasn1.codec.cer, pyasn1.type, sys, pyasn1.error, tests.base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/codec/der/test_encoder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.511 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.445 IQR)
- **Top Global Matches:** file_cluster_8: 11.511, file_cluster_13: 11.803, file_cluster_0: 12.001
- **Magnitude:** 311.18 | **LOC:** 666 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.9139%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testEncodeOpenTypeUnknownId` (Impact: 4.0)
  * `testEncodeOpenTypeIncompatibleType` (Impact: 4.0)
  * `testEncodeOpenTypeUnknownId` (Impact: 4.0)
  * `testEncodeOpenTypeIncompatibleType` (Impact: 4.0)
  * `setUp` (Impact: 2.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 164`, `args: 68`, `func_start: 68`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 79`, `duplicate_logic: 45`, `orphaned_logic: 19`
* *Architecture:* `io: 5`, `api: 71`, `import: 9`
* *Defense:* `safety: 51`, `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` unittest, pyasn1.type, sys, pyasn1.codec.der, pyasn1.error, tests.base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/type/test_constraint.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.8 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.826 IQR)
- **Top Global Matches:** file_cluster_8: 12.8, file_cluster_13: 13.015, file_cluster_0: 13.078
- **Magnitude:** 268.56 | **LOC:** 421 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.6166%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testConst2` (Impact: 11.4)
  * `testConst1` (Impact: 7.6)
  * `testBadVal` (Impact: 5.8)
  * `testBadValExtraFields` (Impact: 5.8)
  * `testContains` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 137`, `args: 50`, `func_start: 50`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 21`, `planned_debt: 1`, `duplicate_logic: 35`, `orphaned_logic: 15`
* *Architecture:* `io: 1`, `api: 63`, `import: 5`
* *Defense:* `safety: 106`, `test: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest, tests.base, pyasn1.type, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/type/base.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.637 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.76 IQR)
- **Top Global Matches:** file_cluster_13: 11.637, file_cluster_0: 11.653, file_cluster_8: 11.698
- **Magnitude:** 261.74 | **LOC:** 700 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.9877%), Tech Debt (99.7814%)
**Top Internal Functions/Classes:**
  * `__setattr__` (Impact: 48.6)
  * `__init__` (Impact: 41.5)
    * *Intent:* # pickle protocol '__reduce__', '__reduce_ex__', '__getnewargs__', '__getinitargs__', '__getstate__'...
  * `__repr__` (Impact: 14.6)
    * *Intent:* """Create a specialization of |ASN.1| schema or value object. The subtype relationship between ASN.1...
  * `subtype` (Impact: 9.9)
  * `_moveSizeSpec` (Impact: 7.6)
    * *Intent:* ----
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 128`, `args: 58`, `func_start: 58`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 50`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 3`, `orphaned_logic: 7`
* *Architecture:* `api: 37`, `import: 5`
* *Defense:* `safety: 5`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1, pyasn1.type, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/type/constraint.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.288 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.738 IQR)
- **Top Global Matches:** file_cluster_8: 12.288, file_cluster_7: 12.439, file_cluster_13: 12.481
- **Magnitude:** 204.5 | **LOC:** 752 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.9686%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_testValue` (Impact: 41.6)
  * `__call__` (Impact: 11.0)
  * `_testValue` (Impact: 8.3)
    * *Intent:* # this will succeed divisor_of_six = DivisorOfSix(1) # this will raise ValueConstraintError divisor_...
  * `isSuperTypeOf` (Impact: 7.2)
    * *Intent:* # TODO: fix possible comparison of set vs scalars here return (otherConstraint is self or not self._...
  * `isSubTypeOf` (Impact: 7.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 91`, `args: 46`, `func_start: 46`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 34`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 14`, `orphaned_logic: 14`
* *Architecture:* `api: 18`, `import: 2`
* *Defense:* `safety: 8`, `doc: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/type/namedtype.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.402 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.523 IQR)
- **Top Global Matches:** file_cluster_0: 12.402, file_cluster_13: 12.484, file_cluster_8: 12.55
- **Magnitude:** 193.18 | **LOC:** 551 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.2247%), Tech Debt (56.9001%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 46.8)
  * `getPositionByName` (Impact: 31.2)
  * `__computeNameToPosMap` (Impact: 21.1)
  * `getNameByPosition` (Impact: 3.9)
  * `__init__` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 128`, `args: 54`, `func_start: 54`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 44`, `orphaned_logic: 6`
* *Architecture:* `io: 1`, `api: 28`, `import: 4`
* *Defense:* `safety: 18`, `doc: 24`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1, pyasn1.type, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/codec/cer/encoder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.591 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.514 IQR)
- **Top Global Matches:** file_cluster_8: 9.591, file_cluster_13: 9.845, file_cluster_7: 10.131
- **Magnitude:** 180.02 | **LOC:** 332 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.7933%), Tech Debt (99.5741%)
**Top Internal Functions/Classes:**
  * `encodeValue` (Impact: 67.1)
  * `encodeValue` (Impact: 34.6)
    * *Intent:* # CER encoding constraints: # - minutes are mandatory, seconds are optional # - sub-seconds must NOT...
  * `_componentSortKey` (Impact: 12.9)
    * *Intent:* """Sort SET components by tag Sort regardless of the Choice value (static sort) """
  * `encodeValue` (Impact: 10.6)
  * `encodeValue` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 47`, `args: 9`, `func_start: 8`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 17`, `duplicate_logic: 5`, `orphaned_logic: 1`
* *Architecture:* `api: 17`, `import: 5`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, pyasn1.codec.ber, pyasn1.type, pyasn1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/codec/der/test_decoder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.484 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.937 IQR)
- **Top Global Matches:** file_cluster_8: 11.484, file_cluster_13: 11.761, file_cluster_0: 12.017
- **Magnitude:** 167.34 | **LOC:** 410 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.4915%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDefiniteLenNesting` (Impact: 11.3)
  * `testNoRecursionError` (Impact: 9.6)
  * `testDecodeOpenTypesUnknownType` (Impact: 5.8)
  * `testDecodeOpenTypesUnknownType` (Impact: 5.8)
  * `testIndefMode` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 138`, `args: 34`, `func_start: 34`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 6`, `duplicate_logic: 30`, `orphaned_logic: 4`
* *Architecture:* `io: 3`, `api: 43`, `import: 9`
* *Defense:* `safety: 82`, `doc: 6`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` unittest, pyasn1.type, sys, pyasn1.codec.der, pyasn1.error, tests.base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/codec/cer/test_decoder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.454 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.072 IQR)
- **Top Global Matches:** file_cluster_8: 11.454, file_cluster_13: 11.71, file_cluster_0: 11.966
- **Magnitude:** 151.28 | **LOC:** 394 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.9782%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDecodeOpenTypesUnknownType` (Impact: 5.8)
  * `testDecodeOpenTypesUnknownType` (Impact: 5.8)
  * `testIndefLenNesting` (Impact: 5.7)
  * `testNoRecursionError` (Impact: 4.0)
  * `testEmpty` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 138`, `args: 36`, `func_start: 36`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 6`, `planned_debt: 2`, `duplicate_logic: 30`, `orphaned_logic: 6`
* *Architecture:* `io: 3`, `api: 46`, `import: 9`
* *Defense:* `safety: 77`, `doc: 6`, `test: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` unittest, pyasn1.codec.cer, pyasn1.type, sys, pyasn1.error, tests.base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/codec/native/encoder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.923 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.574 IQR)
- **Top Global Matches:** file_cluster_8: 9.923, file_cluster_13: 9.986, file_cluster_17: 10.464
- **Magnitude:** 133.5 | **LOC:** 286 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.4482%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__call__` (Impact: 19.9)
  * `encode` (Impact: 14.1)
  * `__init__` (Impact: 11.3)
  * `encode` (Impact: 7.0)
  * `__getattr__` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 78`, `args: 18`, `func_start: 18`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 13`, `duplicate_logic: 17`, `orphaned_logic: 1`
* *Architecture:* `api: 31`, `import: 10`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1, pyasn1.compat, pyasn1.type, warnings, collections
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/type/tag.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_7` (Drift: 11.414 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.631 IQR)
- **Top Global Matches:** file_cluster_7: 11.414, file_cluster_8: 11.444, file_cluster_0: 11.58
- **Magnitude:** 117.86 | **LOC:** 336 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.2424%), Tech Debt (97.4899%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 27.4)
  * `tagExplicitly` (Impact: 7.3)
  * `__getitem__` (Impact: 5.4)
  * `tagImplicitly` (Impact: 3.8)
  * `isSuperTagSetOf` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 78`, `args: 36`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `state_mutation: 29`, `orphaned_logic: 8`
* *Architecture:* `api: 13`, `import: 1`
* *Defense:* `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/codec/streaming.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.288 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.361 IQR)
- **Top Global Matches:** file_cluster_13: 11.288, file_cluster_0: 11.504, file_cluster_7: 11.657
- **Magnitude:** 104.0 | **LOC:** 235 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.7172%), Tech Debt (96.4066%)
**Top Internal Functions/Classes:**
  * `readFromStream` (Impact: 15.1)
  * `peekIntoStream` (Impact: 14.9)
  * `asSeekableStream` (Impact: 13.2)
    * *Intent:* # that we will not return back, and thus it is # safe to drop all cached data. if self._cache.tell()...
  * `isEndOfStream` (Impact: 9.6)
    * *Intent:* ------
  * `read` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 33`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `duplicate_logic: 2`
* *Architecture:* `io: 6`, `api: 16`, `import: 4`
* *Defense:* `safety: 9`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.029851
  * `Imports (Out-Degree: 0):` io, os, pyasn1.type, pyasn1
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyasn1-0.6.3/pyasn1/type/namedval.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.234 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.326 IQR)
- **Top Global Matches:** file_cluster_8: 11.234, file_cluster_13: 11.518, file_cluster_7: 11.565
- **Magnitude:** 103.76 | **LOC:** 193 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.8824%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 32.5)
  * `getValues` (Impact: 5.6)
  * `__repr__` (Impact: 3.9)
  * `__getitem__` (Impact: 3.8)
  * `__contains__` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 45`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 9`, `fragile_debt: 1`, `orphaned_logic: 20`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* `safety: 7`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/type/test_useful.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.864 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.077 IQR)
- **Top Global Matches:** file_cluster_13: 12.864, file_cluster_8: 12.981, file_cluster_7: 13.321
- **Magnitude:** 100.7 | **LOC:** 167 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.5259%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 2.1)
  * `testSchemaPickling` (Impact: 2.1)
  * `testSchemaPickling` (Impact: 2.1)
  * `testFromDateTimeRoundTrip` (Impact: 2.0)
  * `testValuePickling` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 89`, `args: 32`, `func_start: 32`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`, `duplicate_logic: 16`, `orphaned_logic: 15`
* *Architecture:* `io: 1`, `api: 37`, `import: 7`
* *Defense:* `safety: 34`, `doc: 10`, `test: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest, sys, pyasn1.type, pickle, copy, tests.base, datetime
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/codec/native/decoder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.866 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.167 IQR)
- **Top Global Matches:** file_cluster_8: 9.866, file_cluster_13: 9.936, file_cluster_7: 10.554
- **Magnitude:** 92.2 | **LOC:** 245 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.9975%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `__call__` (Impact: 19.8)
  * `__init__` (Impact: 11.3)
  * `__call__` (Impact: 7.9)
  * `__call__` (Impact: 7.8)
  * `__call__` (Impact: 5.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 52`, `args: 10`, `func_start: 10`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 16`, `duplicate_logic: 9`, `orphaned_logic: 1`
* *Architecture:* `api: 8`, `import: 9`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, pyasn1.compat, pyasn1.type, pyasn1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/type/useful.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.807 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.177 IQR)
- **Top Global Matches:** file_cluster_13: 10.807, file_cluster_8: 10.898, file_cluster_0: 11.138
- **Magnitude:** 90.68 | **LOC:** 191 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.6807%), Tech Debt (67.0624%)
**Top Internal Functions/Classes:**
  * `asDateTime` (Impact: 56.0)
  * `__init__` (Impact: 2.1)
  * `utcoffset` (Impact: 1.8)
  * `tzname` (Impact: 1.8)
  * `dst` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 28`, `args: 6`, `func_start: 6`, `class_start: 5`
* *Risk/State:* `state_mutation: 14`, `orphaned_logic: 3`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 6`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1, datetime, pyasn1.type
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/codec/native/test_encoder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.127 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.801 IQR)
- **Top Global Matches:** file_cluster_13: 12.127, file_cluster_8: 12.249, file_cluster_0: 12.564
- **Magnitude:** 85.46 | **LOC:** 141 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.2931%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testBadValueType` (Impact: 5.6)
  * `testEmpty` (Impact: 5.5)
  * `setUp` (Impact: 2.2)
  * `setUp` (Impact: 2.1)
  * `testSimple` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 65`, `args: 21`, `func_start: 21`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 5`, `duplicate_logic: 9`, `orphaned_logic: 12`
* *Architecture:* `io: 1`, `api: 32`, `import: 7`
* *Defense:* `safety: 20`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` unittest, pyasn1.type, sys, pyasn1.codec.native, pyasn1.error, tests.base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/debug.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.618 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.357 IQR)
- **Top Global Matches:** file_cluster_8: 10.618, file_cluster_13: 10.652, file_cluster_17: 10.946
- **Magnitude:** 81.28 | **LOC:** 147 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.6571%), Tech Debt (98.8049%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 32.0)
    * *Intent:* # noinspection PyShadowingNames
  * `__str__` (Impact: 14.0)
  * `__init__` (Impact: 1.8)
  * `push` (Impact: 1.8)
  * `pop` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 33`, `args: 15`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 19`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 9`, `import: 4`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` logging, pyasn1, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/type/test_char.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.63 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.473 IQR)
- **Top Global Matches:** file_cluster_13: 12.63, file_cluster_8: 12.732, file_cluster_0: 13.049
- **Magnitude:** 79.74 | **LOC:** 159 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.8511%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testSizeConstraint` (Impact: 7.6)
  * `testEmpty` (Impact: 5.5)
  * `testSchemaPickling` (Impact: 2.1)
  * `setUp` (Impact: 2.0)
  * `testInit` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 75`, `args: 20`, `func_start: 20`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`, `orphaned_logic: 17`
* *Architecture:* `io: 1`, `api: 26`, `import: 8`
* *Defense:* `safety: 35`, `test: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` unittest, pyasn1.type, sys, pickle, pyasn1.error, tests.base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `pyasn1-0.6.3/pyasn1/__init__.py` (PYTHON) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.628 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.821 IQR)
- `pyasn1-0.6.3/pyasn1/compat/__init__.py` (PYTHON) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.628 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.821 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `pyasn1-0.6.3/pyasn1/error.py` (PYTHON) | Magnitude: 19.56 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 18, structural_boundaries: 12, indent_spaces: 10, api: 9
- `pyasn1-0.6.3/pyasn1/type/namedtype.py` (PYTHON) | Magnitude: 193.18 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 225, structural_boundaries: 128, encapsulation: 127, args: 54
- `pyasn1-0.6.3/pyasn1/type/tagmap.py` (PYTHON) | Magnitude: 59.82 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 25, encapsulation: 23, branch: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pyasn1-0.6.3/tests/type/test_namedtype.py` (PYTHON) | Magnitude: 72.92 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 63, safety: 29, test: 29
- `pyasn1-0.6.3/pyasn1/type/base.py` (PYTHON) | Magnitude: 261.74 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 272, structural_boundaries: 128, encapsulation: 88, args: 58
- `pyasn1-0.6.3/tests/base.py` (PYTHON) | Magnitude: 8.74 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, api: 5, indent_spaces: 4, args: 3
- `pyasn1-0.6.3/pyasn1/type/useful.py` (PYTHON) | Magnitude: 90.68 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 97, encapsulation: 31, branch: 29, structural_boundaries: 28
- `pyasn1-0.6.3/tests/type/test_char.py` (PYTHON) | Magnitude: 79.74 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 75, safety: 35, test: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `pyasn1-0.6.3/pyasn1/type/tag.py` (PYTHON) | Magnitude: 117.86 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 124, encapsulation: 96, structural_boundaries: 78, args: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pyasn1-0.6.3/pyasn1/debug.py` (PYTHON) | Magnitude: 81.28 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 74, encapsulation: 37, structural_boundaries: 33, state_mutation: 19
- `pyasn1-0.6.3/pyasn1/type/opentype.py` (PYTHON) | Magnitude: 34.36 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 16, encapsulation: 15, state_mutation: 9
- `pyasn1-0.6.3/pyasn1/codec/native/encoder.py` (PYTHON) | Magnitude: 133.5 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 140, structural_boundaries: 78, api: 31, encapsulation: 23
- `pyasn1-0.6.3/pyasn1/codec/native/decoder.py` (PYTHON) | Magnitude: 92.2 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 121, structural_boundaries: 52, encapsulation: 26, branch: 17
- `pyasn1-0.6.3/pyasn1/codec/der/decoder.py` (PYTHON) | Magnitude: 14.96 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, sec_reflection_metaprogramming: 18, structural_boundaries: 13, encapsulation: 9

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pyasn1-0.6.3/pyasn1/error.py` -> **Severity: 9.502** (Embedded: 0.194 * Error Risk: 48.9738%)
- `pyasn1-0.6.3/pyasn1/codec/streaming.py` -> **Severity: 1.286** (Embedded: 0.0299 * Error Risk: 43.0795%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyasn1-0.6.3/pyasn1/error.py` -> **Severity: 3707.129** (Blast Radius: 80.159 * Doc Risk: 46.2472%)
- `pyasn1-0.6.3/pyasn1/codec/streaming.py` -> **Severity: 1893.696** (Blast Radius: 26.24 * Doc Risk: 72.1683%)
- `pyasn1-0.6.3/pyasn1/codec/native/encoder.py` -> **Severity: 1129.585** (Blast Radius: 11.534 * Doc Risk: 97.9352%)
- `pyasn1-0.6.3/pyasn1/type/useful.py` -> **Severity: 1017.123** (Blast Radius: 11.534 * Doc Risk: 88.1848%)
- `pyasn1-0.6.3/pyasn1/type/char.py` -> **Severity: 997.686** (Blast Radius: 11.534 * Doc Risk: 86.4996%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
