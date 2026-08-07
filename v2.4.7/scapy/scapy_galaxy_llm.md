# ARCHITECTURAL_BRIEF: scapy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/scapy` |
| **Timestamp** | `2026-08-07T05:35:51.424442+00:00` |
| **Scan Duration** | `3.61s` |
| **Git Branch** | `master` |
| **Git Commit** | `9ae49f850db81ae2023e667014cc0f1ed5aa7a35` |
| **Git Remote** | `https://github.com/secdev/scapy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 382 malicious artifacts.

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
| Total Artifacts | 867 |
| Analyzed Artifacts (Scanned) | 420 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 447 |
| Total LOC | 162107 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 48.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3433 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.274 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 25.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2147 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 371 | 161127 | 88.3% |
| XML | 18 | 753 | 4.3% |
| PLAINTEXT | 13 | 10 | 3.1% |
| MARKDOWN | 7 | 0 | 1.7% |
| SHELL | 7 | 143 | 1.7% |
| BATCH | 2 | 47 | 0.5% |
| MAKEFILE | 1 | 9 | 0.2% |
| RUBY | 1 | 18 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.548`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 252 | 60.0% |
| file_cluster_13 | 119 | 28.3% |
| Unknown | 10 | 2.4% |
| file_cluster_0 | 8 | 1.9% |
| file_cluster_16 | 1 | 0.2% |
| file_cluster_7 | 1 | 0.2% |
| file_cluster_9 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 18 | 4.3% |
| Static: Literature & Documentation | 10 | 2.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 447*

**Composition by Extension & Reason:**
- `.uts`: 209x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.uts)
- `.png`: 45x Excluded (Explicitly Denied Extension: '.png')
- `.rst`: 33x Excluded (Unsupported Extension: '.rst')
- `.py`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 197 LOC), 1x Excluded (Machine-Generated Source Code Signature: 228 LOC)
- `.gz`: 24x Excluded (Explicitly Denied Extension: '.gz')
- `.raw`: 23x Excluded (Unsupported Extension: '.raw')
- `.pcap`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.pcap')
- `.yml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.ipynb`: 7x Excluded (Unsupported Extension: '.ipynb')
- `.utsc`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ps1`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 8 LOC)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.4 | 13.1 | 7.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 41.3 | 51.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 43.6 | 27.1 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 35.8 | 2.5 | 80.0 |
| API Exposure | 0.0 | 14.1 | 5.0 | 5.1 | 0.0 |
| Concurrency Exposure | 0.0 | 85.4 | 0.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 35.1 | 16.2 | 0.0 |
| Commented Logic Exposure | 0.0 | 96.5 | 1.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 87.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.7 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 47.9 | 44.2 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scapy/layers/inet6.py` (Hits: 71)
- `scapy/utils.py` (Hits: 58)
- `scapy/utils6.py` (Hits: 51)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **packet.py** (`scapy/packet.py`) — 244 inbound connections
2. **fields.py** (`scapy/fields.py`) — 211 inbound connections
3. **config.py** (`scapy/config.py`) — 178 inbound connections
4. **compat.py** (`scapy/compat.py`) — 139 inbound connections
5. **error.py** (`scapy/error.py`) — 132 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **utils.py** (`scapy/utils.py`) — 53 outbound dependencies
2. **config.py** (`scapy/config.py`) — 51 outbound dependencies
3. **inet.py** (`scapy/layers/inet.py`) — 41 outbound dependencies
4. **kerberos.py** (`scapy/layers/kerberos.py`) — 37 outbound dependencies
5. **main.py** (`scapy/main.py`) — 35 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_NTLM_post_build` (@ `scapy/layers/ntlm.py`) -> Impact: **682.4** | LOC: 1842
- `addfield` (@ `scapy/layers/sixlowpan.py`) -> Impact: **577.0** | LOC: 1030
- `i2repr` (@ `scapy/layers/inet6.py`) -> Impact: **491.0** | LOC: 1740
- `send` (@ `scapy/sendrecv.py`) -> Impact: **369.7** | LOC: 917
- `tls_session_update` (@ `scapy/layers/tls/handshake.py`) -> Impact: **360.0** | LOC: 1068
- `getfield` (@ `scapy/fields.py`) -> Impact: **321.2** | LOC: 924
- `load_nss_keys` (@ `scapy/layers/tls/session.py`) -> Impact: **320.0** | LOC: 892
- `i2m` (@ `scapy/asn1fields.py`) -> Impact: **311.4** | LOC: 829
- `computeNIGroupAddr` (@ `scapy/layers/inet6.py`) -> Impact: **306.4** | LOC: 1175
- `_defrag_logic` (@ `scapy/layers/inet.py`) -> Impact: **289.3** | LOC: 590

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `test/scapy/layers/tls/pki` | 8 | 40000.0 | 0.0% | 0.0% |
| `scapy/layers` | 61 | 22044.24 | 11.37% | 50.35% |
| `scapy` | 34 | 14265.2 | 25.64% | 45.65% |
| `doc/notebooks/tls/raw_data/pki` | 2 | 10000.0 | 0.0% | 0.0% |
| `scapy/layers/tls` | 18 | 7143.86 | 18.31% | 72.39% |
| `scapy/modules` | 7 | 3502.64 | 26.1% | 46.06% |
| `scapy/asn1` | 4 | 2602.62 | 23.22% | 49.71% |
| `scapy/layers/msrpce` | 10 | 1419.86 | 12.06% | 22.57% |
| `scapy/arch/windows` | 3 | 863.66 | 14.55% | 57.32% |
| `scapy/arch` | 5 | 762.08 | 11.17% | 25.37% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `scapy/as_resolvers.py` -> **100.0%** Exposure
- `scapy/contrib/automotive/gm/gmlan_scanner.py` -> **100.0%** Exposure
- `scapy/contrib/automotive/kwp.py` -> **100.0%** Exposure
- `scapy/contrib/carp.py` -> **100.0%** Exposure
- `scapy/contrib/eigrp.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `scapy/contrib/automotive/gm/gmlan_ecu_states.py` -> **100.0%** Exposure
- `scapy/contrib/isotp/isotp_soft_socket.py` -> **100.0%** Exposure
- `scapy/layers/tls/crypto/ciphers.py` -> **100.0%** Exposure
- `run_scapy` -> **100.0%** Exposure
- `scapy/tools/check_spdx.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `scapy/fields.py` -> **0** Orphaned Functions | **163** Duplicates
- `scapy/layers/tls/cert.py` -> **0** Orphaned Functions | **76** Duplicates
- `scapy/contrib/dicom.py` -> **6** Orphaned Functions | **57** Duplicates
- `scapy/scapypipes.py` -> **0** Orphaned Functions | **63** Duplicates
- `scapy/contrib/bgp.py` -> **2** Orphaned Functions | **57** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`scapy/modules/p0f.py`** -> AI Confidence: **99.39%**
2. **`scapy/modules/p0fv2.py`** -> AI Confidence: **99.39%**
3. **`scapy/arch/bpf/pfroute.py`** -> AI Confidence: **99.31%**
4. **`scapy/arch/libpcap.py`** -> AI Confidence: **99.31%**
5. **`scapy/arch/linux/rtnetlink.py`** -> AI Confidence: **99.31%**
6. **`scapy/arch/unix.py`** -> AI Confidence: **99.31%**
7. **`scapy/arch/windows/__init__.py`** -> AI Confidence: **99.31%**
8. **`scapy/asn1/mib.py`** -> AI Confidence: **99.31%**
9. **`scapy/contrib/automotive/scanner/enumerator.py`** -> AI Confidence: **99.31%**
10. **`scapy/contrib/automotive/scanner/executor.py`** -> AI Confidence: **99.31%**
11. **`scapy/contrib/isotp/isotp_packet.py`** -> AI Confidence: **99.31%**
12. **`scapy/contrib/isotp/isotp_scanner.py`** -> AI Confidence: **99.31%**
13. **`scapy/contrib/isotp/isotp_soft_socket.py`** -> AI Confidence: **99.31%**
14. **`scapy/contrib/isotp/isotp_utils.py`** -> AI Confidence: **99.31%**
15. **`scapy/layers/dns.py`** -> AI Confidence: **99.31%**
16. **`scapy/layers/http.py`** -> AI Confidence: **99.31%**
17. **`scapy/layers/inet.py`** -> AI Confidence: **99.31%**
18. **`scapy/layers/ipsec.py`** -> AI Confidence: **99.31%**
19. **`scapy/layers/kerberos.py`** -> AI Confidence: **99.31%**
20. **`scapy/layers/ldap.py`** -> AI Confidence: **99.31%**
21. **`scapy/layers/msrpce/msnrpc.py`** -> AI Confidence: **99.31%**
22. **`scapy/layers/msrpce/rpcclient.py`** -> AI Confidence: **99.31%**
23. **`scapy/layers/msrpce/rpcserver.py`** -> AI Confidence: **99.31%**
24. **`scapy/layers/ntlm.py`** -> AI Confidence: **99.31%**
25. **`scapy/layers/sixlowpan.py`** -> AI Confidence: **99.31%**
26. **`scapy/layers/smbclient.py`** -> AI Confidence: **99.31%**
27. **`scapy/layers/smbserver.py`** -> AI Confidence: **99.31%**
28. **`scapy/layers/spnego.py`** -> AI Confidence: **99.31%**
29. **`scapy/layers/tls/automaton.py`** -> AI Confidence: **99.31%**
30. **`scapy/layers/tls/crypto/cipher_aead.py`** -> AI Confidence: **99.31%**
31. **`scapy/layers/tls/handshake.py`** -> AI Confidence: **99.31%**
32. **`scapy/layers/tls/record_sslv2.py`** -> AI Confidence: **99.31%**
33. **`scapy/layers/tls/session.py`** -> AI Confidence: **99.31%**
34. **`scapy/layers/tuntap.py`** -> AI Confidence: **99.31%**
35. **`scapy/main.py`** -> AI Confidence: **99.31%**
36. **`scapy/modules/ldaphero.py`** -> AI Confidence: **99.31%**
37. **`scapy/modules/nmap.py`** -> AI Confidence: **99.31%**
38. **`scapy/modules/ticketer.py`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3302` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `scapy/ansmachine.py` (PYTHON) -> Cumulative Risk: **664.01**
- **Archetype:** `file_cluster_13` (Distance: 11.584 IQR)
- **Magnitude:** 206.3 | **LOC:** 293 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.912%), State Flux (99.6731%), Documentation (82.3025%)
- **Heaviest Functions:** `parse_all_options` (Impact: 21.2), `reply` (Impact: 18.8), `sniff` (Impact: 13.8)

### 2. `scapy/automaton.py` (PYTHON) -> Cumulative Risk: **650.25**
- **Archetype:** `file_cluster_13` (Distance: 12.623 IQR)
- **Magnitude:** 1226.02 | **LOC:** 1630 | **CtrlFlow:** 42.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9728%), Tech Debt (97.2279%), Cognitive Load (82.9813%)
- **Heaviest Functions:** `build_graph` (Impact: 173.7), `_do_control` (Impact: 130.2), `_run` (Impact: 81.0)

### 3. `scapy/layers/tftp.py` (PYTHON) -> Cumulative Risk: **639.26**
- **Archetype:** `file_cluster_0` (Distance: 12.818 IQR)
- **Magnitude:** 441.18 | **LOC:** 558 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (99.1281%)
- **Heaviest Functions:** `mysummary` (Impact: 80.1), `parse_args` (Impact: 21.9), `RECEIVED_RRQ` (Impact: 20.4)

### 4. `scapy/volatile.py` (PYTHON) -> Cumulative Risk: **616.71**
- **Archetype:** `file_cluster_8` (Distance: 12.827 IQR)
- **Magnitude:** 1019.58 | **LOC:** 1425 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (99.7684%), Safety Score (88.2489%)
- **Heaviest Functions:** `__init__` (Impact: 130.0), `_fix` (Impact: 48.1), `_fix` (Impact: 34.6)

### 5. `scapy/contrib/cansocket_python_can.py` (PYTHON) -> Cumulative Risk: **610.12**
- **Archetype:** `file_cluster_13` (Distance: 12.257 IQR)
- **Magnitude:** 1.84 | **LOC:** 409 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.0278%), Tech Debt (98.3681%), Concurrency (85.366%)
- **Heaviest Functions:** `read_bus` (Impact: 73.5), `select` (Impact: 9.5), `_recv_internal` (Impact: 7.7)

### 6. `scapy/layers/dcerpc.py` (PYTHON) -> Cumulative Risk: **604.25**
- **Archetype:** `file_cluster_8` (Distance: 11.917 IQR)
- **Magnitude:** 1317.98 | **LOC:** 3407 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.8213%), Documentation (89.6562%), State Flux (82.6392%)
- **Heaviest Functions:** `in_pkt` (Impact: 143.4), `any2i` (Impact: 119.3), `addfield` (Impact: 99.0)

### 7. `scapy/layers/tls/handshake_sslv2.py` (PYTHON) -> Cumulative Risk: **591.76**
- **Archetype:** `file_cluster_8` (Distance: 11.292 IQR)
- **Magnitude:** 293.02 | **LOC:** 549 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.5832%)
- **Heaviest Functions:** `i2repr` (Impact: 57.6), `tls_session_update` (Impact: 20.3), `post_dissection_tls_session_update` (Impact: 19.6)

### 8. `scapy/layers/tls/cert.py` (PYTHON) -> Cumulative Risk: **589.83**
- **Archetype:** `file_cluster_13` (Distance: 13.079 IQR)
- **Magnitude:** 1058.82 | **LOC:** 1923 | **CtrlFlow:** 44.5% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.8372%), Verification (80.0%)
- **Heaviest Functions:** `__repr__` (Impact: 64.3), `__repr__` (Impact: 32.3), `fill_and_store` (Impact: 28.4)

### 9. `scapy/asn1fields.py` (PYTHON) -> Cumulative Risk: **588.63**
- **Archetype:** `file_cluster_8` (Distance: 12.525 IQR)
- **Magnitude:** 636.22 | **LOC:** 1037 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.7634%), Verification (80.0%)
- **Heaviest Functions:** `i2m` (Impact: 311.4), `__init__` (Impact: 39.4), `m2i` (Impact: 13.0)

### 10. `scapy/contrib/hicp.py` (PYTHON) -> Cumulative Risk: **585.19**
- **Archetype:** `file_cluster_8` (Distance: 10.753 IQR)
- **Magnitude:** 1.73 | **LOC:** 279 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), State Flux (99.4426%), Documentation (88.065%)
- **Heaviest Functions:** `post_build` (Impact: 25.1), `do_dissect` (Impact: 18.0), `post_build` (Impact: 14.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `doc/notebooks/tls/raw_data/pki/srv_cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.583
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/notebooks/tls/raw_data/pki/srv_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.583
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/scapy/layers/tls/pki/ca_cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.583
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/scapy/layers/tls/pki/ca_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.583
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/scapy/layers/tls/pki/cli_cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.583
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/scapy/layers/tls/pki/cli_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.583
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/scapy/layers/tls/pki/srv_cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.583
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/scapy/layers/tls/pki/srv_cert_ed25519.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.583
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/scapy/layers/tls/pki/srv_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.583
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/scapy/layers/tls/pki/srv_key_ed25519.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.583
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scapy/fields.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.048 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.393 IQR)
- **Top Global Matches:** file_cluster_8: 13.048, file_cluster_13: 13.148, file_cluster_7: 13.289
- **Magnitude:** 2110.94 | **LOC:** 4002 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.3578%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `getfield` (Impact: 321.2)
  * `getfield` (Impact: 69.7)
    * *Intent:* # type: (Optional[Packet], Any) -> K if x and pkt and hasattr(x, "add_parent"): cast("Packet", x).ad...
  * `i2repr` (Impact: 61.8)
    * *Intent:* # A bit of trickery to get precise floats if val is None: return val int_part = val >> self.frac_bit...
  * `randval` (Impact: 41.6)
  * `__repr__` (Impact: 38.0)
    * *Intent:* # type: () -> str
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 451`, `structural_boundaries: 933`, `args: 369`, `func_start: 359`, `class_start: 135`
* *Risk/State:* `safety_bypasses: 63`, `state_mutation: 302`, `planned_debt: 1`, `fragile_debt: 5`, `duplicate_logic: 163`
* *Architecture:* `io: 8`, `api: 341`, `import: 28`
* *Defense:* `safety: 204`, `doc: 125`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.091
  * `Choke Point (Betweenness):` 0.02661 | `Ripple Effect (Closeness):` 0.508858
  * `Imports (Out-Degree: 13):` scapy.utils, scapy.dadict, math, scapy.error, scapy.pton_ntop, time, inspect, scapy.route6...
  * `Imported By (In-Degree: 211):` (Excluded from Brief to save tokens)

### `scapy/asn1/mib.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.958 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.246 IQR)
- **Top Global Matches:** file_cluster_8: 7.958, file_cluster_7: 8.784, file_cluster_1: 9.009
- **Magnitude:** 1820.28 | **LOC:** 824 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (6.3705%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 32`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 13`
* *Architecture:* `io: 1`, `api: 2`, `import: 7`
* *Defense:* `safety: 1`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.749
  * `Choke Point (Betweenness):` 0.000297 | `Ripple Effect (Closeness):` 0.330054
  * `Imports (Out-Degree: 4):` scapy.config, scapy.utils, glob, scapy.dadict, scapy.compat, typing, re
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `scapy/packet.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.008 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.226 IQR)
- **Top Global Matches:** file_cluster_13: 13.008, file_cluster_8: 13.043, file_cluster_0: 13.156
- **Magnitude:** 1762.12 | **LOC:** 2687 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (32.9083%), Tech Debt (15.9702%)
**Top Internal Functions/Classes:**
  * `self_build` (Impact: 148.1)
  * `make_dump_txt` (Impact: 113.1)
  * `ls` (Impact: 102.4)
    * *Intent:* # Show popup
  * `json` (Impact: 86.4)
  * `getlayer` (Impact: 77.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 555`, `structural_boundaries: 414`, `args: 174`, `func_start: 161`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 298`, `dead_code: 3`, `planned_debt: 7`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 138`, `import: 27`
* *Defense:* `safety: 133`, `doc: 170`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 102.554
  * `Choke Point (Betweenness):` 0.026229 | `Ripple Effect (Closeness):` 0.610856
  * `Imports (Out-Degree: 11):` scapy.utils, itertools, scapy.error, scapy.main, time, re, copy, scapy.base_classes...
  * `Imported By (In-Degree: 244):` (Excluded from Brief to save tokens)

### `scapy/layers/inet6.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.315 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.759 IQR)
- **Top Global Matches:** file_cluster_8: 11.315, file_cluster_13: 11.585, file_cluster_7: 11.622
- **Magnitude:** 1620.2 | **LOC:** 4249 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (14.5661%), Tech Debt (74.184%)
**Top Internal Functions/Classes:**
  * `i2repr` (Impact: 491.0)
  * `computeNIGroupAddr` (Impact: 306.4)
  * `NDP_Attack_DAD_DoS_via_NA` (Impact: 127.4)
  * `_NDP_Attack_DAD_DoS` (Impact: 37.7)
  * `mysummary` (Impact: 33.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 450`, `structural_boundaries: 741`, `args: 239`, `func_start: 179`, `class_start: 135`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 129`, `dead_code: 6`, `planned_debt: 23`, `fragile_debt: 18`, `duplicate_logic: 10`
* *Architecture:* `io: 71`, `api: 285`, `import: 26`
* *Defense:* `safety: 84`, `doc: 86`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.513
  * `Choke Point (Betweenness):` 0.00534 | `Ripple Effect (Closeness):` 0.297478
  * `Imports (Out-Degree: 18):` scapy.utils, scapy.error, scapy.consts, scapy.pton_ntop, time, hashlib, scapy.route6, scapy.utils6...
  * `Imported By (In-Degree: 39):` (Excluded from Brief to save tokens)

### `scapy/layers/inet.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.323 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.655 IQR)
- **Top Global Matches:** file_cluster_13: 12.323, file_cluster_8: 12.373, file_cluster_0: 12.375
- **Magnitude:** 1587.72 | **LOC:** 2559 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (23.9612%), Tech Debt (80.2852%)
**Top Internal Functions/Classes:**
  * `_defrag_logic` (Impact: 289.3)
  * `world_trace` (Impact: 145.3)
  * `in4_pseudoheader` (Impact: 104.5)
  * `mysummary` (Impact: 87.0)
  * `parse_args` (Impact: 84.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 461`, `structural_boundaries: 468`, `args: 171`, `func_start: 135`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 231`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 2`, `duplicate_logic: 18`
* *Architecture:* `io: 17`, `api: 161`, `concurrency: 2`, `import: 40`
* *Defense:* `safety: 73`, `doc: 103`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.559
  * `Choke Point (Betweenness):` 0.058783 | `Ripple Effect (Closeness):` 0.330054
  * `Imports (Out-Degree: 22):` scapy.utils, scapy.plist, cartopy.crs, scapy.ansmachine, scapy.automaton, matplotlib.collections, multiprocessing, scapy.error...
  * `Imported By (In-Degree: 103):` (Excluded from Brief to save tokens)

### `scapy/layers/kerberos.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.767 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.254 IQR)
- **Top Global Matches:** file_cluster_8: 11.767, file_cluster_7: 12.066, file_cluster_13: 12.088
- **Magnitude:** 1510.76 | **LOC:** 5679 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (13.4201%), Tech Debt (49.8015%)
**Top Internal Functions/Classes:**
  * `_show_krb_error` (Impact: 257.1)
  * `GSS_WrapEx` (Impact: 100.3)
  * `GSS_UnwrapEx` (Impact: 85.3)
  * `_parse_spn` (Impact: 84.4)
  * `get_usage` (Impact: 32.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 521`, `structural_boundaries: 457`, `args: 117`, `func_start: 96`, `class_start: 114`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 321`, `dead_code: 4`, `planned_debt: 3`, `fragile_debt: 4`, `duplicate_logic: 24`
* *Architecture:* `io: 8`, `api: 204`, `import: 44`
* *Defense:* `safety: 90`, `doc: 167`, `test: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.157
  * `Choke Point (Betweenness):` 0.01369 | `Ripple Effect (Closeness):` 0.156193
  * `Imports (Out-Degree: 26):` scapy.utils, scapy.libs.rfc3961, scapy.layers.tls.crypto.hash, scapy.automaton, scapy.error, re, scapy.layers.tls.cert, cryptography.hazmat.primitives.asymmetric...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `scapy/layers/dcerpc.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.917 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.917 IQR)
- **Top Global Matches:** file_cluster_8: 11.917, file_cluster_13: 12.207, file_cluster_7: 12.212
- **Magnitude:** 1317.98 | **LOC:** 3407 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (17.8362%), Tech Debt (99.8213%)
**Top Internal Functions/Classes:**
  * `in_pkt` (Impact: 143.4)
    * *Intent:* # Detect if "Header Signing" is in use
  * `any2i` (Impact: 119.3)
  * `addfield` (Impact: 99.0)
  * `addfield` (Impact: 59.5)
  * `__repr__` (Impact: 24.3)
    * *Intent:* # --- API DceRpcOp = collections.namedtuple("DceRpcOp", ["request", "response"]) DCE_RPC_INTERFACES ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 481`, `args: 202`, `func_start: 145`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 226`, `planned_debt: 7`, `fragile_debt: 3`, `duplicate_logic: 52`
* *Architecture:* `api: 202`, `import: 24`
* *Defense:* `safety: 99`, `doc: 99`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.828
  * `Choke Point (Betweenness):` 0.004296 | `Ripple Effect (Closeness):` 0.132949
  * `Imports (Out-Degree: 14):` scapy.layers.msrpce.raw.ms_dcom, scapy.error, inspect, scapy.base_classes, scapy.layers.inet, scapy.contrib.rtps.common_types, typing, scapy.layers.kerberos...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `scapy/automaton.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.623 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.719 IQR)
- **Top Global Matches:** file_cluster_13: 12.623, file_cluster_0: 12.781, file_cluster_8: 12.785
- **Magnitude:** 1226.02 | **LOC:** 1630 | **CtrlFlow:** 42.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.9813%), Tech Debt (97.2279%)
**Top Internal Functions/Classes:**
  * `build_graph` (Impact: 173.7)
  * `_do_control` (Impact: 130.2)
    * *Intent:* # type: () -> None self.destroy() def _run_condition(self, cond, *args, **kargs): # type: (_StateWra...
  * `_run` (Impact: 81.0)
  * `__new__` (Impact: 60.3)
  * `select_objects` (Impact: 36.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 349`, `args: 130`, `func_start: 127`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 63`, `state_mutation: 315`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 19`
* *Architecture:* `io: 23`, `api: 104`, `concurrency: 16`, `import: 26`
* *Defense:* `safety: 56`, `doc: 14`, `sync_locks: 4`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.774
  * `Choke Point (Betweenness):` 0.000294 | `Ripple Effect (Closeness):` 0.301732
  * `Imports (Out-Degree: 10):` scapy.utils, scapy.plist, itertools, scapy.error, scapy.consts, time, inspect, select...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `scapy/layers/tls/session.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.742 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.543 IQR)
- **Top Global Matches:** file_cluster_13: 12.742, file_cluster_8: 12.849, file_cluster_7: 13.076
- **Magnitude:** 1219.26 | **LOC:** 1308 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.2321%), Tech Debt (72.7922%)
**Top Internal Functions/Classes:**
  * `load_nss_keys` (Impact: 320.0)
  * `__repr__` (Impact: 71.4)
  * `__init__` (Impact: 56.2)
  * `derive_keys` (Impact: 51.8)
  * `compute_tls13_verify_data` (Impact: 29.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 161`, `args: 55`, `func_start: 53`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 333`, `dead_code: 1`, `fragile_debt: 4`, `duplicate_logic: 5`
* *Architecture:* `io: 6`, `api: 63`, `import: 21`
* *Defense:* `safety: 24`, `doc: 34`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.315
  * `Choke Point (Betweenness):` 0.053425 | `Ripple Effect (Closeness):` 0.295236
  * `Imports (Out-Degree: 13):` scapy.utils, scapy.layers.tls.record, scapy.layers.tls.crypto.compression, scapy.error, scapy.pton_ntop, scapy.layers.tls.record_tls13, scapy.layers.tls.crypto.hkdf, scapy.layers.tls.crypto.prf...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `scapy/layers/ntlm.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.375 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.45 IQR)
- **Top Global Matches:** file_cluster_8: 11.375, file_cluster_13: 11.662, file_cluster_7: 11.71
- **Magnitude:** 1112.26 | **LOC:** 2314 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (17.3736%), Tech Debt (10.1659%)
**Top Internal Functions/Classes:**
  * `_NTLM_post_build` (Impact: 682.4)
  * `_getSessionBaseKey` (Impact: 78.5)
  * `getfield` (Impact: 30.0)
    * *Intent:* # Add padding if necessary if pad > 0: buf.append(pad * b"\x00", len(buf)) buf.append(field.addfield...
  * `addfield` (Impact: 17.0)
  * `_on_payload` (Impact: 16.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 291`, `structural_boundaries: 256`, `args: 87`, `func_start: 67`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 127`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 73`, `import: 30`
* *Defense:* `safety: 62`, `doc: 68`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.601
  * `Choke Point (Betweenness):` 0.014171 | `Ripple Effect (Closeness):` 0.156639
  * `Imports (Out-Degree: 18):` scapy.layers.tls.crypto.hash, scapy.error, time, copy, scapy.asn1.mib, cryptography.hazmat.decrepit.ciphers, scapy.layers.ldap, cryptography.hazmat.primitives.ciphers...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `scapy/layers/tls/cert.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.079 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.463 IQR)
- **Top Global Matches:** file_cluster_13: 13.079, file_cluster_0: 13.093, file_cluster_8: 13.298
- **Magnitude:** 1058.82 | **LOC:** 1923 | **CtrlFlow:** 44.5% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (38.8783%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 64.3)
  * `__repr__` (Impact: 32.3)
    * *Intent:* """ if self.issuer_hash != other.subject_hash: return False return other.pubkey.verifyCert(self) def...
  * `fill_and_store` (Impact: 28.4)
  * `__call__` (Impact: 27.0)
  * `__call__` (Impact: 26.5)
    * *Intent:* # cryptography raised the minimum RSA key length to 1024 in 43.0+ # https://github.com/pyca/cryptogr...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 301`, `args: 110`, `func_start: 110`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 259`, `dead_code: 2`, `planned_debt: 4`, `duplicate_logic: 76`
* *Architecture:* `io: 8`, `api: 108`, `import: 30`
* *Defense:* `safety: 69`, `doc: 130`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.173
  * `Choke Point (Betweenness):` 0.001101 | `Ripple Effect (Closeness):` 0.169935
  * `Imports (Out-Degree: 10):` scapy.utils, cryptography.hazmat.backends, private, scapy.layers.tls.crypto.pkcs1, scapy.error, time, certificate, scapy.layers.tls.cert...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `scapy/layers/tls/automaton_cli.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.492 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.95 IQR)
- **Top Global Matches:** file_cluster_0: 11.492, file_cluster_13: 11.914, file_cluster_8: 12.076
- **Magnitude:** 1034.52 | **LOC:** 1472 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.7105%), Tech Debt (90.7305%)
**Top Internal Functions/Classes:**
  * `parse_args` (Impact: 121.1)
  * `tls13_should_add_ClientHello` (Impact: 28.6)
  * `INIT_TLS_SESSION` (Impact: 26.3)
    * *Intent:* # Default to x25519 if supported self.curve = 29 else: # Or secp256r1 otherwise self.curve = 23 self...
  * `add_ClientData` (Impact: 20.7)
  * `should_store_session_ticket_file` (Impact: 18.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 279`, `args: 176`, `func_start: 176`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 134`, `dead_code: 1`, `fragile_debt: 12`, `duplicate_logic: 6`
* *Architecture:* `io: 13`, `api: 247`, `import: 22`
* *Defense:* `safety: 15`, `doc: 38`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.624
  * `Choke Point (Betweenness):` 0.000381 | `Ripple Effect (Closeness):` 0.003182
  * `Imports (Out-Degree: 19):` scapy.utils, scapy.layers.tls.record, scapy.automaton, scapy.layers.tls.handshake_sslv2, scapy.layers.tls.automaton, scapy.error, time, scapy.layers.tls.crypto.hkdf...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scapy/volatile.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.827 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.877 IQR)
- **Top Global Matches:** file_cluster_8: 12.827, file_cluster_13: 12.966, file_cluster_7: 13.15
- **Magnitude:** 1019.58 | **LOC:** 1425 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.0809%), Tech Debt (99.7684%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 130.0)
  * `_fix` (Impact: 48.1)
  * `_fix` (Impact: 34.6)
  * `_command_args` (Impact: 30.2)
  * `_command_args` (Impact: 30.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 335`, `args: 144`, `func_start: 144`, `class_start: 60`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 1`, `state_mutation: 404`, `duplicate_logic: 33`
* *Architecture:* `api: 79`, `import: 12`
* *Defense:* `safety: 18`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.201
  * `Choke Point (Betweenness):` 0.001248 | `Ripple Effect (Closeness):` 0.403345
  * `Imports (Out-Degree: 3):` scapy.utils, copy, scapy.base_classes, random, string, struct, scapy.compat, math...
  * `Imported By (In-Degree: 49):` (Excluded from Brief to save tokens)

### `scapy/modules/ticketer.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.605 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.892 IQR)
- **Top Global Matches:** file_cluster_8: 10.605, file_cluster_7: 10.982, file_cluster_13: 11.171
- **Magnitude:** 997.26 | **LOC:** 2773 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (10.9756%), Tech Debt (11.8902%)
**Top Internal Functions/Classes:**
  * `import_krb` (Impact: 232.2)
  * `_build_sid` (Impact: 160.7)
  * `show` (Impact: 64.3)
  * `edit_ticket` (Impact: 60.0)
  * `toPN` (Impact: 27.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 311`, `structural_boundaries: 238`, `args: 104`, `func_start: 92`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 106`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 89`, `import: 25`
* *Defense:* `safety: 31`, `doc: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.633
  * `Choke Point (Betweenness):` 0.000624 | `Ripple Effect (Closeness):` 0.130111
  * `Imports (Out-Degree: 12):` scapy.utils, scapy.libs.rfc3961, platform, datetime, scapy.error, re, scapy.layers.dcerpc, scapy.fields...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scapy/layers/dns.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.902 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.645 IQR)
- **Top Global Matches:** file_cluster_8: 11.902, file_cluster_13: 12.003, file_cluster_7: 12.155
- **Magnitude:** 960.54 | **LOC:** 2029 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (15.4914%), Tech Debt (28.8026%)
**Top Internal Functions/Classes:**
  * `mysummary` (Impact: 177.0)
  * `m2i` (Impact: 137.2)
    * *Intent:* # Decode the compressed DNS message decoded, left = dns_get_str(s, full=self.get_full(pkt)) # return...
  * `make_reply` (Impact: 132.2)
  * `dns_compress` (Impact: 38.9)
  * `dns_get_str` (Impact: 35.5)
    * *Intent:* # 12/2023 from https://www.iana.org/assignments/ds-rr-types/ds-rr-types.xhtml # 12/2023 from https:/...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 320`, `args: 115`, `func_start: 63`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 121`, `duplicate_logic: 9`
* *Architecture:* `io: 16`, `api: 100`, `import: 32`
* *Defense:* `safety: 61`, `doc: 88`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.046
  * `Choke Point (Betweenness):` 0.000378 | `Ripple Effect (Closeness):` 0.11563
  * `Imports (Out-Degree: 17):` scapy.utils, scapy.plist, abc, scapy.ansmachine, itertools, math, scapy.error, scapy.pton_ntop...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `scapy/modules/krack/automaton.py` (PYTHON) | Magnitude: 396.78 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 579, structural_boundaries: 140, branch: 81, state_mutation: 80
- `scapy/layers/smbclient.py` (PYTHON) | Magnitude: 954.7 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1332, branch: 252, structural_boundaries: 235, state_mutation: 199
- `scapy/libs/rfc3961.py` (PYTHON) | Magnitude: 522.76 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 816, structural_boundaries: 198, branch: 123, sec_reflection_metaprogramming: 120
- `scapy/layers/tftp.py` (PYTHON) | Magnitude: 441.18 | Delta: **0.178 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 358, state_mutation: 164, structural_boundaries: 119, api: 74
- `scapy/contrib/automotive/uds_logging.py` (PYTHON) | Magnitude: 1.16 | Delta: **0.261 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 98, structural_boundaries: 96, args: 43, func_start: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `scapy/contrib/automotive/obd/packet.py` (PYTHON) | Magnitude: 0.05 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, api: 3, indent_spaces: 2, args: 1
- `scapy/tools/automotive/xcpscanner.py` (PYTHON) | Magnitude: 0.06 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 20, branch: 19, io: 8
- `scapy/layers/tls/cert.py` (PYTHON) | Magnitude: 1058.82 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1136, structural_boundaries: 301, state_mutation: 259, branch: 241
- `scapy/contrib/tcpros.py` (PYTHON) | Magnitude: 1.22 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 214, structural_boundaries: 52, branch: 31, doc: 28
- `scapy/contrib/tcpao.py` (PYTHON) | Magnitude: 0.93 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 146, structural_boundaries: 66, branch: 26, args: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `scapy/contrib/dicom.py` (PYTHON) | Magnitude: 6.67 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1155, structural_boundaries: 356, generics: 174, api: 155

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `scapy/layers/tls/crypto/common.py` (PYTHON) | Magnitude: 0.12 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 2, class_start: 1, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `scapy/tools/generate_bluetooth.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 6, branch: 5, import: 5
- `scapy/tools/check_spdx.sh` (SHELL) | Magnitude: 0.03 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 12, indent_spaces: 11, branch: 10, structural_boundaries: 7
- `scapy/layers/gssapi.py` (PYTHON) | Magnitude: 147.56 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 361, structural_boundaries: 117, doc: 80, api: 53
- `scapy/contrib/automotive/__init__.py` (PYTHON) | Magnitude: 0.12 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, import: 1
- `scapy/utils6.py` (PYTHON) | Magnitude: 254.52 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 391, structural_boundaries: 159, branch: 127, doc: 94

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `scapy/layers/tls/crypto/kx_algs.py` (PYTHON) | Magnitude: 0.23 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 49, encapsulation: 26, structural_boundaries: 22, class_start: 14

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `scapy/layers/dcerpc.py` -> Churn: **77.0%** | Cog Load: 17.8362% | Debt: 99.8213%
- `scapy/layers/bluetooth.py` -> Churn: **66.67%** | Cog Load: 3.699% | Debt: 71.4442%
- `scapy/layers/msrpce/msdcom.py` -> Churn: **62.12%** | Cog Load: 4.9145% | Debt: 80.689%
- `scapy/tools/UTscapy.py` -> Churn: **56.09%** | Cog Load: 31.8818% | Debt: 64.1572%
- `scapy/layers/smb2.py` -> Churn: **50.68%** | Cog Load: 10.393% | Debt: 91.5397%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `scapy/layers/tls/handshake.py` -> **Gabriel** (100.0% isolated ownership) | Magnitude: 792.24
- `scapy/layers/ipsec.py` -> **Gabriel** (100.0% isolated ownership) | Magnitude: 757.44
- `scapy/layers/dot11.py` -> **Gabriel** (100.0% isolated ownership) | Magnitude: 604.56
- `scapy/layers/http.py` -> **Gabriel** (100.0% isolated ownership) | Magnitude: 586.22
- `scapy/libs/rfc3961.py` -> **Gabriel** (100.0% isolated ownership) | Magnitude: 522.76

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `scapy/layers/inet.py` -> **Severity: 5.445** (Bridge: 0.0588 * Flux: 92.6218%)
- `scapy/layers/tls/session.py` -> **Severity: 5.342** (Bridge: 0.0534 * Flux: 99.9999%)
- `scapy/config.py` -> **Severity: 4.79** (Bridge: 0.0542 * Flux: 88.4615%)
- `scapy/utils.py` -> **Severity: 4.506** (Bridge: 0.0674 * Flux: 66.8718%)
- `scapy/layers/http.py` -> **Severity: 4.287** (Bridge: 0.0483 * Flux: 88.7031%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `scapy/packet.py` -> **Severity: 37.212** (Embedded: 0.6109 * Error Risk: 60.9171%)
- `scapy/volatile.py` -> **Severity: 35.595** (Embedded: 0.4033 * Error Risk: 88.2489%)
- `scapy/config.py` -> **Severity: 33.384** (Embedded: 0.5357 * Error Risk: 62.3187%)
- `scapy/error.py` -> **Severity: 33.367** (Embedded: 0.4951 * Error Risk: 67.3977%)
- `scapy/base_classes.py` -> **Severity: 29.256** (Embedded: 0.3987 * Error Risk: 73.3861%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `scapy/packet.py` -> **Severity: 6909.894** (Blast Radius: 102.554 * Doc Risk: 67.3781%)
- `scapy/compat.py` -> **Severity: 6568.9** (Blast Radius: 65.689 * Doc Risk: 100.0%)
- `scapy/config.py` -> **Severity: 5996.891** (Blast Radius: 81.635 * Doc Risk: 73.4598%)
- `scapy/error.py` -> **Severity: 3680.551** (Blast Radius: 58.577 * Doc Risk: 62.8327%)
- `scapy/fields.py` -> **Severity: 3270.808** (Blast Radius: 36.091 * Doc Risk: 90.6267%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
