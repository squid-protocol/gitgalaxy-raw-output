# ARCHITECTURAL_BRIEF: scapy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/scapy` |
| **Timestamp** | `2026-08-03T21:35:21.692113+00:00` |
| **Scan Duration** | `4.03s` |
| **Git Branch** | `master` |
| **Git Commit** | `9ae49f850db81ae2023e667014cc0f1ed5aa7a35` |
| **Git Remote** | `https://github.com/secdev/scapy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 382 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
| Cognitive Load Exposure | 0.0 | 99.4 | 13.2 | 7.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 15.8 | 5.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 43.1 | 26.7 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 47.5 | 80.0 | 80.0 |
| API Exposure | 0.0 | 14.1 | 5.0 | 5.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 35.1 | 16.2 | 0.0 |
| Commented Logic Exposure | 0.0 | 96.5 | 1.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 87.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.7 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 71.0 | 95.2 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 64.2 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 62.6 | 100.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 8.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `_NTLM_post_build` (@ `scapy/layers/ntlm.py`) -> Impact: **4224.4** | LOC: 1842
- `i2repr` (@ `scapy/layers/inet6.py`) -> Impact: **2915.0** | LOC: 1740
- `send` (@ `scapy/sendrecv.py`) -> Impact: **2313.1** | LOC: 917
- `tls_session_update` (@ `scapy/layers/tls/handshake.py`) -> Impact: **2199.4** | LOC: 1068
- `getfield` (@ `scapy/fields.py`) -> Impact: **1971.5** | LOC: 924
- `i2m` (@ `scapy/asn1fields.py`) -> Impact: **1931.5** | LOC: 829
- `addfield` (@ `scapy/layers/sixlowpan.py`) -> Impact: **1890.7** | LOC: 1030
- `_defrag_logic` (@ `scapy/layers/inet.py`) -> Impact: **1848.2** | LOC: 590
- `_show_krb_error` (@ `scapy/layers/kerberos.py`) -> Impact: **1535.4** | LOC: 882
- `__init__` (@ `scapy/layers/ldap.py`) -> Impact: **1507.2** | LOC: 463
  * *Intent:* # "Each buffer of protected data is transferred over the underlying # transport connection as a sequence of octets prepended with a four- # buffer." f...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `class_ref` (@ `doc/scapy/_ext/scapy_doc.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Tabs are 3-wide in autodoc
- `__init__` (@ `scapy/arch/libpcap.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # type: (Packet) -> NoReturn
- `__init__` (@ `scapy/arch/libpcap.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # pcap sockets class L2pcapListenSocket(_L2libpcapSocket): desc = "read packets at layer 2 using libpcap" def __init__(self, iface=None, # type: Optio...
- `send` (@ `scapy/arch/linux/__init__.py`) -> **O(2^N) [Recursive]**
- `_guess_iface_name` (@ `scapy/arch/unix.py`) -> **O(2^N) [Recursive]**
  * *Intent:* ################## # Routes stuff # ################## def _guess_iface_name(netif): # type: (str) -> Optional[str] """
- `_route_add_loopback` (@ `scapy/arch/windows/__init__.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # type: (...) -> None cset = [] # candidate set (possible source addresses) if iface == conf.loopback_name: if dpref == '::': return cset = ['::1'] el...
- `__init__` (@ `scapy/as_resolvers.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # type: (*AS_resolver) -> None AS_resolver.__init__(self) if reslist: self.resolvers_list = reslist else: self.resolvers_list = (AS_resolver_radb(), A...
- `__repr__` (@ `scapy/asn1/asn1.py`) -> **O(2^N) [Recursive]**
- `__repr__` (@ `scapy/asn1/asn1.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # type: () -> str h = hex(self.val) if h[-1] == "L": h = h[:-1] # cut at 22 because with leading '0x', x509 serials should be < 23 if len(h) > 22: h =...
- `BER_tagging_dec` (@ `scapy/asn1/ber.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # The functions below provide implicit and explicit tagging support.

### Highest Data Gravity (Database Complexity)
- `load_nss_keys` (@ `scapy/layers/tls/session.py`) -> DB Complexity: **156**
- `addfield` (@ `scapy/layers/sixlowpan.py`) -> DB Complexity: **146**
- `__init__` (@ `scapy/arch/windows/native.py`) -> DB Complexity: **123**
- `build_graph` (@ `scapy/automaton.py`) -> DB Complexity: **99**
- `computeNIGroupAddr` (@ `scapy/layers/inet6.py`) -> DB Complexity: **92**
- `send` (@ `scapy/sendrecv.py`) -> DB Complexity: **85**
- `on_can_recv` (@ `scapy/contrib/isotp/isotp_soft_socket.py`) -> DB Complexity: **72**
- `i2repr` (@ `scapy/layers/inet6.py`) -> DB Complexity: **70**
- `recv` (@ `scapy/supersocket.py`) -> DB Complexity: **68**
- `__repr__` (@ `scapy/layers/smbserver.py`) -> DB Complexity: **62**
  * *Intent:* """ def __init__(self, name, path=".", type=None, remark="", encryptdata=False): # Set the default type if type is None: type = 0 # DISKTREE if name.e...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `scapy/layers` | 61 | 59778.34 | 11.37% | 50.28% |
| `scapy` | 34 | 40486.2 | 25.42% | 42.37% |
| `test/scapy/layers/tls/pki` | 8 | 40000.0 | 0.0% | 0.0% |
| `scapy/layers/tls` | 18 | 18990.16 | 18.35% | 70.59% |
| `doc/notebooks/tls/raw_data/pki` | 2 | 10000.0 | 0.0% | 0.0% |
| `scapy/modules` | 7 | 9755.04 | 23.76% | 45.77% |
| `scapy/asn1` | 4 | 4330.32 | 23.22% | 49.71% |
| `scapy/layers/msrpce` | 10 | 3552.56 | 12.07% | 22.57% |
| `scapy/arch` | 5 | 2871.08 | 10.68% | 25.37% |
| `scapy/cbor` | 3 | 2198.92 | 10.58% | 66.54% |

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

### Exploit Generation Surface
- `doc/scapy/_ext/scapy_doc.py` -> **100.0%** Exposure
- `scapy/__init__.py` -> **100.0%** Exposure
- `scapy/ansmachine.py` -> **100.0%** Exposure
- `scapy/arch/__init__.py` -> **100.0%** Exposure
- `scapy/arch/bpf/core.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `doc/scapy/_ext/scapy_doc.py` -> **100.0%** Exposure
- `scapy/__init__.py` -> **100.0%** Exposure
- `scapy/arch/windows/native.py` -> **100.0%** Exposure
- `scapy/asn1fields.py` -> **100.0%** Exposure
- `scapy/base_classes.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `doc/scapy/_ext/scapy_doc.py` -> **100.0%** Exposure
- `scapy/__init__.py` -> **100.0%** Exposure
- `scapy/ansmachine.py` -> **100.0%** Exposure
- `scapy/arch/__init__.py` -> **100.0%** Exposure
- `scapy/arch/bpf/core.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3302` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `scapy/ansmachine.py` (PYTHON) -> Cumulative Risk: **910.87**
- **Archetype:** `file_cluster_13` (Distance: 11.584 IQR)
- **Magnitude:** 437.7 | **LOC:** 293 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9999%)
- **Heaviest Functions:** `reply` (Impact: 72.5), `__new__` (Impact: 57.2), `parse_all_options` (Impact: 51.2)

### 2. `scapy/contrib/cansocket_python_can.py` (PYTHON) -> Cumulative Risk: **887.66**
- **Archetype:** `file_cluster_13` (Distance: 12.257 IQR)
- **Magnitude:** 6.43 | **LOC:** 409 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `read_bus` (Impact: 468.4), `send` (Impact: 25.2), `select` (Impact: 18.2)

### 3. `scapy/asn1fields.py` (PYTHON) -> Cumulative Risk: **870.19**
- **Archetype:** `file_cluster_8` (Distance: 12.525 IQR)
- **Magnitude:** 2374.12 | **LOC:** 1037 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `i2m` (Impact: 1931.5), `__init__` (Impact: 96.3), `m2i` (Impact: 43.0)

### 4. `scapy/automaton.py` (PYTHON) -> Cumulative Risk: **868.26**
- **Archetype:** `file_cluster_13` (Distance: 12.629 IQR)
- **Magnitude:** 3141.92 | **LOC:** 1630 | **CtrlFlow:** 42.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9728%)
- **Heaviest Functions:** `build_graph` (Impact: 1077.8), `_do_control` (Impact: 432.1), `__new__` (Impact: 395.7)

### 5. `scapy/arch/windows/native.py` (PYTHON) -> Cumulative Risk: **859.38**
- **Archetype:** `file_cluster_13` (Distance: 10.781 IQR)
- **Magnitude:** 386.28 | **LOC:** 244 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 351.0), `__init__` (Impact: 7.2)

### 6. `scapy/layers/inet.py` (PYTHON) -> Cumulative Risk: **850.49**
- **Archetype:** `file_cluster_13` (Distance: 12.331 IQR)
- **Magnitude:** 5116.22 | **LOC:** 2559 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_defrag_logic` (Impact: 1848.2), `in4_pseudoheader` (Impact: 584.5), `parse_args` (Impact: 534.0)

### 7. `scapy/modules/p0f.py` (PYTHON) -> Cumulative Risk: **843.33**
- **Archetype:** `file_cluster_8` (Distance: 11.352 IQR)
- **Magnitude:** 2112.8 | **LOC:** 961 | **CtrlFlow:** 73.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `prnp0f` (Impact: 715.0), `from_packet` (Impact: 296.8), `tcp_find_match` (Impact: 255.5)

### 8. `scapy/layers/tls/keyexchange.py` (PYTHON) -> Cumulative Risk: **841.75**
- **Archetype:** `file_cluster_13` (Distance: 11.863 IQR)
- **Magnitude:** 1103.8 | **LOC:** 993 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 96.8), `_verify_sig` (Impact: 71.0), `getfield` (Impact: 70.5)

### 9. `scapy/contrib/automotive/obd/scanner.py` (PYTHON) -> Cumulative Risk: **822.82**
- **Archetype:** `file_cluster_13` (Distance: 10.42 IQR)
- **Magnitude:** 4.58 | **LOC:** 302 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `_get_table_entry_y` (Impact: 158.6), `_get_table_entry_y` (Impact: 89.4), `get_supported` (Impact: 47.8)

### 10. `scapy/utils.py` (PYTHON) -> Cumulative Risk: **819.6**
- **Archetype:** `file_cluster_13` (Distance: 12.839 IQR)
- **Magnitude:** 1170.88 | **LOC:** 4186 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `fletcher16_checkbytes` (Impact: 94.1), `run` (Impact: 61.4), `hexdump` (Impact: 58.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `scapy/fields.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.048 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.393 IQR)
- **Top Global Matches:** file_cluster_8: 13.048, file_cluster_13: 13.148, file_cluster_7: 13.289
- **Magnitude:** 6421.94 | **LOC:** 4002 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (23.3362%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `getfield` (Impact: 1971.5 | O(2^N) | DB: 36)
  * `getfield` (Impact: 453.7 | O(2^N) | DB: 4)
    * *Intent:* # type: (Optional[Packet], Any) -> K if x and pkt and hasattr(x, "add_parent"): cast("Packet", x).ad...
  * `i2repr` (Impact: 331.8 | O(2^N) | DB: 8)
    * *Intent:* # A bit of trickery to get precise floats if val is None: return val int_part = val >> self.frac_bit...
  * `__repr__` (Impact: 185.3 | O(2^N) | DB: 10)
    * *Intent:* # type: () -> str
  * `i2repr` (Impact: 133.3 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 451`, `structural_boundaries: 933`, `args: 369`, `func_start: 359`, `class_start: 135`
* *Risk/State:* `safety_bypasses: 63`, `state_mutation: 302`, `planned_debt: 1`, `fragile_debt: 5`, `duplicate_logic: 163`
* *Architecture:* `io: 8`, `api: 341`, `import: 28`
* *Defense:* `safety: 204`, `doc: 125`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.091
  * `Choke Point (Betweenness):` 0.02661 | `Ripple Effect (Closeness):` 0.508858
  * `Imports (Out-Degree: 13):` socket, scapy.config, loop, scapy.volatile, scapy.error, scapy.base_classes, types, typing...
  * `Imported By (In-Degree: 211):` (Excluded from Brief to save tokens)

### `scapy/packet.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.006 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.225 IQR)
- **Top Global Matches:** file_cluster_13: 13.006, file_cluster_8: 13.04, file_cluster_0: 13.153
- **Magnitude:** 5781.02 | **LOC:** 2687 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (32.9481%), Tech Debt (15.9702%)
**Top Internal Functions/Classes:**
  * `self_build` (Impact: 927.5 | O(2^N) | DB: 16)
  * `getlayer` (Impact: 521.5 | O(2^N))
  * `json` (Impact: 491.7 | O(2^N) | DB: 9)
  * `sprintf` (Impact: 396.5 | O(2^N))
  * `_command` (Impact: 390.6 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 555`, `structural_boundaries: 414`, `args: 172`, `func_start: 161`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 298`, `dead_code: 3`, `planned_debt: 7`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 138`, `import: 27`
* *Defense:* `safety: 133`, `doc: 170`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 102.554
  * `Choke Point (Betweenness):` 0.026229 | `Ripple Effect (Closeness):` 0.610856
  * `Imports (Out-Degree: 11):` scapy.config, pyx, scapy.volatile, scapy.error, scapy.base_classes, types, typing, re...
  * `Imported By (In-Degree: 244):` (Excluded from Brief to save tokens)

### `scapy/layers/inet6.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.315 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.76 IQR)
- **Top Global Matches:** file_cluster_8: 11.315, file_cluster_13: 11.585, file_cluster_7: 11.622
- **Magnitude:** 5367.4 | **LOC:** 4249 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 92
- **Risk Profile:** Cognitive Load (14.4693%), Tech Debt (71.4362%)
**Top Internal Functions/Classes:**
  * `i2repr` (Impact: 2915.0 | O(2^N) | DB: 70)
  * `computeNIGroupAddr` (Impact: 925.6 | O(N^6) | DB: 92)
  * `NDP_Attack_DAD_DoS_via_NA` (Impact: 412.5 | O(N^6) | DB: 12)
  * `_NDP_Attack_DAD_DoS` (Impact: 243.5 | O(2^N) | DB: 6)
  * `mysummary` (Impact: 210.3 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 450`, `structural_boundaries: 741`, `args: 239`, `func_start: 179`, `class_start: 135`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 129`, `dead_code: 6`, `planned_debt: 23`, `fragile_debt: 18`, `duplicate_logic: 9`
* *Architecture:* `io: 71`, `api: 285`, `import: 26`
* *Defense:* `safety: 84`, `doc: 86`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.513
  * `Choke Point (Betweenness):` 0.00534 | `Ripple Effect (Closeness):` 0.297478
  * `Imports (Out-Degree: 18):` socket, scapy.config, scapy.arch, scapy.volatile, scapy.error, scapy.base_classes, typing, scapy.fields...
  * `Imported By (In-Degree: 39):` (Excluded from Brief to save tokens)

### `scapy/layers/inet.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.331 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.656 IQR)
- **Top Global Matches:** file_cluster_13: 12.331, file_cluster_8: 12.381, file_cluster_0: 12.383
- **Magnitude:** 5116.22 | **LOC:** 2559 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (24.1438%), Tech Debt (80.2852%)
**Top Internal Functions/Classes:**
  * `_defrag_logic` (Impact: 1848.2 | O(2^N) | DB: 45)
  * `in4_pseudoheader` (Impact: 584.5 | O(2^N) | DB: 25)
  * `parse_args` (Impact: 534.0 | O(2^N) | DB: 9)
  * `mysummary` (Impact: 468.1 | O(2^N) | DB: 22)
  * `getfield` (Impact: 236.3 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 461`, `structural_boundaries: 468`, `args: 171`, `func_start: 135`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 233`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 2`, `duplicate_logic: 18`
* *Architecture:* `io: 17`, `api: 160`, `concurrency: 2`, `import: 40`
* *Defense:* `safety: 73`, `doc: 103`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.559
  * `Choke Point (Betweenness):` 0.058783 | `Ripple Effect (Closeness):` 0.330054
  * `Imports (Out-Degree: 22):` scapy.plist, socket, scapy.config, matplotlib, scapy.volatile, geoip2.database, scapy.error, scapy.base_classes...
  * `Imported By (In-Degree: 103):` (Excluded from Brief to save tokens)

### `scapy/layers/ntlm.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.376 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.451 IQR)
- **Top Global Matches:** file_cluster_8: 11.376, file_cluster_13: 11.664, file_cluster_7: 11.712
- **Magnitude:** 5028.76 | **LOC:** 2314 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 58
- **Risk Profile:** Cognitive Load (17.3064%), Tech Debt (10.1659%)
**Top Internal Functions/Classes:**
  * `_NTLM_post_build` (Impact: 4224.4 | O(2^N) | DB: 58)
  * `getfield` (Impact: 198.0 | O(2^N) | DB: 1)
    * *Intent:* # Add padding if necessary if pad > 0: buf.append(pad * b"\x00", len(buf)) buf.append(field.addfield...
  * `addfield` (Impact: 95.2 | O(2^N) | DB: 3)
  * `setfieldval` (Impact: 85.4 | O(2^N) | DB: 2)
  * `getfield_and_val` (Impact: 61.7 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 291`, `structural_boundaries: 256`, `args: 87`, `func_start: 67`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 127`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 72`, `import: 30`
* *Defense:* `safety: 62`, `doc: 68`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.601
  * `Choke Point (Betweenness):` 0.014171 | `Ripple Effect (Closeness):` 0.156639
  * `Imports (Out-Degree: 18):` scapy.layers.dcerpc, scapy.layers.msrpce.raw.ms_nrpc, scapy.asn1packet, scapy.error, typing, cryptography.hazmat.decrepit.ciphers, scapy.asn1.mib, enum...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `doc/notebooks/tls/raw_data/pki/srv_cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
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

### `scapy/layers/kerberos.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.767 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.254 IQR)
- **Top Global Matches:** file_cluster_8: 11.767, file_cluster_7: 12.066, file_cluster_13: 12.088
- **Magnitude:** 4361.16 | **LOC:** 5679 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (13.4421%), Tech Debt (49.8015%)
**Top Internal Functions/Classes:**
  * `_show_krb_error` (Impact: 1535.4 | O(2^N) | DB: 47)
  * `_parse_spn` (Impact: 500.1 | O(2^N) | DB: 6)
  * `GSS_WrapEx` (Impact: 329.5 | O(N^6) | DB: 9)
  * `GSS_UnwrapEx` (Impact: 281.0 | O(N^6) | DB: 3)
  * `m2i` (Impact: 126.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 521`, `structural_boundaries: 457`, `args: 117`, `func_start: 96`, `class_start: 114`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 321`, `dead_code: 4`, `planned_debt: 3`, `fragile_debt: 4`, `duplicate_logic: 24`
* *Architecture:* `io: 8`, `api: 204`, `import: 44`
* *Defense:* `safety: 90`, `doc: 167`, `test: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.157
  * `Choke Point (Betweenness):` 0.01369 | `Ripple Effect (Closeness):` 0.156193
  * `Imports (Out-Degree: 26):` socket, scapy.config, scapy.asn1packet, scapy.volatile, scapy.libs.rfc3961, scapy.error, typing, scapy.automaton...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `scapy/layers/dcerpc.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.914 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.916 IQR)
- **Top Global Matches:** file_cluster_8: 11.914, file_cluster_13: 12.203, file_cluster_7: 12.208
- **Magnitude:** 4322.08 | **LOC:** 3407 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (17.8362%), Tech Debt (99.8213%)
**Top Internal Functions/Classes:**
  * `in_pkt` (Impact: 881.3 | O(2^N) | DB: 17)
    * *Intent:* # Detect if "Header Signing" is in use
  * `any2i` (Impact: 731.3 | O(2^N) | DB: 35)
  * `addfield` (Impact: 582.0 | O(2^N) | DB: 6)
  * `addfield` (Impact: 316.7 | O(2^N) | DB: 9)
  * `__repr__` (Impact: 128.3 | O(2^N) | DB: 4)
    * *Intent:* # --- API DceRpcOp = collections.namedtuple("DceRpcOp", ["request", "response"]) DCE_RPC_INTERFACES ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 481`, `args: 198`, `func_start: 145`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 226`, `planned_debt: 7`, `fragile_debt: 3`, `duplicate_logic: 52`
* *Architecture:* `api: 202`, `import: 24`
* *Defense:* `safety: 99`, `doc: 99`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.828
  * `Choke Point (Betweenness):` 0.004296 | `Ripple Effect (Closeness):` 0.132949
  * `Imports (Out-Degree: 14):` scapy.config, scapy.error, scapy.base_classes, typing, inspect, enum, functools, scapy.layers.msrpce.raw.ms_dcom...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `scapy/sendrecv.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.754 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.48 IQR)
- **Top Global Matches:** file_cluster_13: 12.754, file_cluster_0: 12.906, file_cluster_8: 12.943
- **Magnitude:** 3533.26 | **LOC:** 1568 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 85
- **Risk Profile:** Cognitive Load (20.7062%), Tech Debt (8.2623%)
**Top Internal Functions/Classes:**
  * `send` (Impact: 2313.1 | O(2^N) | DB: 85)
  * `__init__` (Impact: 541.2 | O(N^6) | DB: 27)
  * `_sndrcv_snd` (Impact: 317.3 | O(N^6) | DB: 24)
    * *Intent:* # Clean the ans list to delete the field _answered if multi: for snd, _ in self.ans: if hasattr(snd,...
  * `_send` (Impact: 49.7 | O(N^6) | DB: 18)
  * `_stop_sniffer_if_done` (Impact: 35.1 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 175`, `args: 51`, `func_start: 47`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 207`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 26`, `api: 33`, `concurrency: 1`, `import: 26`
* *Defense:* `safety: 64`, `doc: 136`, `test: 1`, `sync_locks: 3`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.687
  * `Choke Point (Betweenness):` 0.001629 | `Ripple Effect (Closeness):` 0.342843
  * `Imports (Out-Degree: 14):` scapy.plist, threading, socket, scapy.config, scapy.error, scapy.base_classes, typing, scapy.automaton...
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `scapy/layers/tls/handshake.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.243 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.183 IQR)
- **Top Global Matches:** file_cluster_8: 11.243, file_cluster_13: 11.399, file_cluster_7: 11.514
- **Magnitude:** 3248.94 | **LOC:** 1771 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (18.5271%), Tech Debt (98.1822%)
**Top Internal Functions/Classes:**
  * `tls_session_update` (Impact: 2199.4 | O(2^N) | DB: 28)
  * `tls_session_update` (Impact: 147.9 | O(2^N) | DB: 1)
  * `tls_session_update` (Impact: 135.0 | O(2^N) | DB: 1)
  * `tls_session_update` (Impact: 122.5 | O(2^N) | DB: 1)
    * *Intent:* # RFC8446 4.2.11.2 # "Each entry in the binders list is computed as an HMAC # over a transcript hash...
  * `post_build` (Impact: 73.2 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 265`, `args: 129`, `func_start: 84`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 89`, `dead_code: 2`, `fragile_debt: 6`, `duplicate_logic: 17`
* *Architecture:* `io: 3`, `api: 109`, `import: 23`
* *Defense:* `safety: 32`, `doc: 54`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.8
  * `Choke Point (Betweenness):` 0.012025 | `Ripple Effect (Closeness):` 0.1725
  * `Imports (Out-Degree: 17):` scapy.config, scapy.layers.tls.crypto.compression, scapy.error, scapy.fields, scapy.layers.tls.extensions, scapy.packet, scapy.layers.x509, struct...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `scapy/automaton.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.629 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.727 IQR)
- **Top Global Matches:** file_cluster_13: 12.629, file_cluster_8: 12.787, file_cluster_0: 12.788
- **Magnitude:** 3141.92 | **LOC:** 1630 | **CtrlFlow:** 42.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 99
- **Risk Profile:** Cognitive Load (82.7463%), Tech Debt (60.708%)
**Top Internal Functions/Classes:**
  * `build_graph` (Impact: 1077.8 | O(2^N) | DB: 99)
  * `_do_control` (Impact: 432.1 | O(N^6) | DB: 20)
    * *Intent:* # type: () -> None self.destroy() def _run_condition(self, cond, *args, **kargs): # type: (_StateWra...
  * `__new__` (Impact: 395.7 | O(2^N) | DB: 21)
  * `select_objects` (Impact: 118.7 | O(N^6) | DB: 4)
  * `_wincreate` (Impact: 87.5 | O(N^5) | DB: 21)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 349`, `args: 130`, `func_start: 127`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 63`, `state_mutation: 315`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `io: 23`, `api: 104`, `concurrency: 16`, `import: 26`
* *Defense:* `safety: 56`, `doc: 14`, `sync_locks: 4`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.774
  * `Choke Point (Betweenness):` 0.000294 | `Ripple Effect (Closeness):` 0.301732
  * `Imports (Out-Degree: 10):` scapy.plist, ctypes, threading, socket, scapy.config, scapy.arch, scapy.error, types...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `scapy/modules/ldaphero.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.847 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.219 IQR)
- **Top Global Matches:** file_cluster_8: 11.847, file_cluster_7: 12.192, file_cluster_13: 12.237
- **Magnitude:** 2949.0 | **LOC:** 2124 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (18.9383%), Tech Debt (11.9701%)
**Top Internal Functions/Classes:**
  * `load_guids` (Impact: 1038.6 | O(2^N) | DB: 11)
  * `_members_popup` (Impact: 510.4 | O(2^N) | DB: 10)
    * *Intent:* # Offsets need to be recalculated
  * `connect` (Impact: 503.0 | O(2^N) | DB: 22)
  * `_showsearchresult` (Impact: 199.7 | O(2^N) | DB: 2)
  * `new` (Impact: 137.9 | O(2^N))
    * *Intent:* # Get dialog popup = BasePopup(self.root) dlg = popup.dlg # Duplicate UI dlg.grid_columnconfigure(1,...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 187`, `args: 45`, `func_start: 44`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 205`, `duplicate_logic: 3`
* *Architecture:* `api: 37`, `import: 13`
* *Defense:* `safety: 83`, `doc: 78`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.583
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` scapy.layers.dcerpc, scapy.layers.spnego, uuid, scapy.layers.gssapi, scapy.layers.ldap, tkinter, scapy.layers.ntlm, scapy.layers.windows.security...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scapy/modules/ticketer.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.606 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.892 IQR)
- **Top Global Matches:** file_cluster_8: 10.606, file_cluster_7: 10.983, file_cluster_13: 11.172
- **Magnitude:** 2874.26 | **LOC:** 2773 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (11.0116%), Tech Debt (11.8902%)
**Top Internal Functions/Classes:**
  * `_build_sid` (Impact: 964.6 | O(2^N) | DB: 7)
  * `import_krb` (Impact: 752.7 | O(N^6) | DB: 4)
  * `show` (Impact: 207.2 | O(N^6))
  * `edit_ticket` (Impact: 177.4 | O(N^6))
  * `_resign_ticket` (Impact: 72.8 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 311`, `structural_boundaries: 238`, `args: 104`, `func_start: 92`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 106`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 89`, `import: 25`
* *Defense:* `safety: 31`, `doc: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.633
  * `Choke Point (Betweenness):` 0.000624 | `Ripple Effect (Closeness):` 0.130111
  * `Imports (Out-Degree: 12):` scapy.layers.dcerpc, tkinter, scapy.config, scapy.error, scapy.libs.rfc3961, re, enum, prompt_toolkit...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scapy/layers/dns.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.903 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.644 IQR)
- **Top Global Matches:** file_cluster_8: 11.903, file_cluster_13: 12.004, file_cluster_7: 12.156
- **Magnitude:** 2692.34 | **LOC:** 2029 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (15.4939%), Tech Debt (28.8026%)
**Top Internal Functions/Classes:**
  * `m2i` (Impact: 749.2 | O(2^N) | DB: 14)
    * *Intent:* # Decode the compressed DNS message decoded, left = dns_get_str(s, full=self.get_full(pkt)) # return...
  * `mysummary` (Impact: 584.0 | O(N^6) | DB: 43)
  * `make_reply` (Impact: 435.3 | O(N^6) | DB: 9)
  * `dns_compress` (Impact: 125.5 | O(N^6) | DB: 2)
  * `dns_get_str` (Impact: 115.5 | O(N^6) | DB: 1)
    * *Intent:* # 12/2023 from https://www.iana.org/assignments/ds-rr-types/ds-rr-types.xhtml # 12/2023 from https:/...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 320`, `args: 114`, `func_start: 63`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 121`, `duplicate_logic: 9`
* *Architecture:* `io: 16`, `api: 99`, `import: 32`
* *Defense:* `safety: 61`, `doc: 88`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.046
  * `Choke Point (Betweenness):` 0.000378 | `Ripple Effect (Closeness):` 0.11563
  * `Imports (Out-Degree: 17):` scapy.plist, socket, scapy.config, abc, scapy.arch, scapy.volatile, scapy.error, scapy.base_classes...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `scapy/layers/ldap.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.186 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.268 IQR)
- **Top Global Matches:** file_cluster_8: 11.186, file_cluster_13: 11.448, file_cluster_7: 11.554
- **Magnitude:** 2656.9 | **LOC:** 2506 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (19.7995%), Tech Debt (16.9425%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 1507.2 | O(2^N) | DB: 53)
    * *Intent:* # "Each buffer of protected data is transferred over the underlying # transport connection as a sequ...
  * `from_rfc2254_string` (Impact: 544.7 | O(N^6) | DB: 11)
  * `is_request` (Impact: 58.5 | O(N^5))
  * `make_reply` (Impact: 57.8 | O(N^6))
  * `tcp_reassemble` (Impact: 34.1 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 283`, `structural_boundaries: 258`, `args: 37`, `func_start: 35`, `class_start: 74`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 164`, `planned_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 13`, `api: 106`, `import: 34`
* *Defense:* `safety: 41`, `doc: 53`, `test: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.742
  * `Choke Point (Betweenness):` 0.002414 | `Ripple Effect (Closeness):` 0.131547
  * `Imports (Out-Degree: 22):` scapy.layers.netbios, string, socket, scapy.config, scapy.arch, scapy.asn1packet, scapy.error, ssl...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `scapy/layers/ipsec.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.589 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.929 IQR)
- **Top Global Matches:** file_cluster_13: 12.589, file_cluster_8: 12.65, file_cluster_7: 12.795
- **Magnitude:** 2547.14 | **LOC:** 1270 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (26.5936%), Tech Debt (20.2671%)
**Top Internal Functions/Classes:**
  * `_encrypt_esp` (Impact: 617.5 | O(2^N) | DB: 6)
  * `check_key` (Impact: 584.2 | O(2^N) | DB: 15)
  * `verify` (Impact: 476.5 | O(N^6) | DB: 30)
  * `__init__` (Impact: 199.8 | O(N^6) | DB: 21)
  * `_decrypt_esp` (Impact: 139.8 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 195`, `structural_boundaries: 137`, `args: 31`, `func_start: 26`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 193`, `planned_debt: 1`, `fragile_debt: 5`
* *Architecture:* `io: 20`, `api: 26`, `import: 23`
* *Defense:* `safety: 22`, `doc: 127`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.698
  * `Choke Point (Betweenness):` 5.8e-05 | `Ripple Effect (Closeness):` 0.004773
  * `Imports (Out-Degree: 9):` socket, scapy.config, scapy.error, scapy.layers.inet6, cryptography.hazmat.decrepit.ciphers, cryptography.hazmat.primitives.ciphers, scapy.fields, scapy.packet...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `scapy/modules/krack/automaton.py` (PYTHON) | Magnitude: 961.18 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 579, structural_boundaries: 140, branch: 81, state_mutation: 80
- `scapy/layers/smbclient.py` (PYTHON) | Magnitude: 2309.0 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1332, branch: 252, structural_boundaries: 235, state_mutation: 199
- `scapy/libs/rfc3961.py` (PYTHON) | Magnitude: 851.16 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 816, structural_boundaries: 198, branch: 123, sec_reflection_metaprogramming: 120
- `scapy/layers/tftp.py` (PYTHON) | Magnitude: 766.58 | Delta: **0.178 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 358, state_mutation: 164, structural_boundaries: 119, api: 74
- `scapy/contrib/automotive/uds_logging.py` (PYTHON) | Magnitude: 1.45 | Delta: **0.261 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 98, structural_boundaries: 96, args: 43, func_start: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `scapy/contrib/automotive/obd/packet.py` (PYTHON) | Magnitude: 0.06 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, api: 3, indent_spaces: 2, args: 1
- `scapy/tools/automotive/xcpscanner.py` (PYTHON) | Magnitude: 0.14 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 20, branch: 19, io: 8
- `scapy/layers/tls/cert.py` (PYTHON) | Magnitude: 2255.52 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1136, structural_boundaries: 301, state_mutation: 259, branch: 241
- `scapy/contrib/tcpros.py` (PYTHON) | Magnitude: 2.43 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 214, structural_boundaries: 52, branch: 31, doc: 28
- `scapy/contrib/tcpao.py` (PYTHON) | Magnitude: 2.46 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 146, structural_boundaries: 66, branch: 26, args: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `scapy/contrib/dicom.py` (PYTHON) | Magnitude: 15.19 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1155, structural_boundaries: 356, generics: 174, api: 155

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `scapy/layers/tls/crypto/common.py` (PYTHON) | Magnitude: 0.12 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 2, class_start: 1, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `scapy/tools/check_spdx.sh` (SHELL) | Magnitude: 0.05 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 12, indent_spaces: 11, branch: 10, structural_boundaries: 8
- `scapy/tools/generate_bluetooth.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 6, branch: 5, import: 5
- `scapy/layers/gssapi.py` (PYTHON) | Magnitude: 308.06 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 361, structural_boundaries: 117, doc: 80, api: 53
- `scapy/contrib/automotive/__init__.py` (PYTHON) | Magnitude: 0.12 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, import: 1
- `scapy/utils6.py` (PYTHON) | Magnitude: 402.72 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 391, structural_boundaries: 159, branch: 127, doc: 94

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `scapy/layers/tls/crypto/kx_algs.py` (PYTHON) | Magnitude: 0.77 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 49, encapsulation: 26, structural_boundaries: 22, class_start: 14

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `scapy/layers/dcerpc.py` -> Churn: **77.0%** | Cog Load: 17.8362% | Debt: 99.8213%
- `scapy/layers/bluetooth.py` -> Churn: **66.67%** | Cog Load: 3.699% | Debt: 71.4442%
- `scapy/layers/msrpce/msdcom.py` -> Churn: **62.12%** | Cog Load: 4.9145% | Debt: 80.689%
- `scapy/tools/UTscapy.py` -> Churn: **56.09%** | Cog Load: 32.019% | Debt: 64.1572%
- `scapy/layers/smb2.py` -> Churn: **50.68%** | Cog Load: 10.393% | Debt: 91.5397%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `scapy/layers/tls/handshake.py` -> **Gabriel** (100.0% isolated ownership) | Magnitude: 3248.94
- `scapy/layers/ipsec.py` -> **Gabriel** (100.0% isolated ownership) | Magnitude: 2547.14
- `scapy/main.py` -> **Guillaume Valadon** (100.0% isolated ownership) | Magnitude: 1856.34
- `scapy/layers/http.py` -> **Gabriel** (100.0% isolated ownership) | Magnitude: 1599.22
- `scapy/cbor/cborcodec.py` -> **Nils Weiss** (100.0% isolated ownership) | Magnitude: 1452.5

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `scapy/layers/inet.py` -> **Severity: 5.461** (Bridge: 0.0588 * Flux: 92.9014%)
- `scapy/layers/tls/session.py` -> **Severity: 5.342** (Bridge: 0.0534 * Flux: 99.9999%)
- `scapy/config.py` -> **Severity: 4.79** (Bridge: 0.0542 * Flux: 88.4615%)
- `scapy/utils.py` -> **Severity: 4.506** (Bridge: 0.0674 * Flux: 66.8718%)
- `scapy/layers/http.py` -> **Severity: 4.287** (Bridge: 0.0483 * Flux: 88.7031%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `scapy/error.py` -> **Severity: 32.123** (Embedded: 0.4951 * Error Risk: 64.8837%)
- `scapy/packet.py` -> **Severity: 30.536** (Embedded: 0.6109 * Error Risk: 49.9893%)
- `scapy/config.py` -> **Severity: 29.294** (Embedded: 0.5357 * Error Risk: 54.6843%)
- `scapy/asn1/asn1.py` -> **Severity: 26.693** (Embedded: 0.3337 * Error Risk: 80.0%)
- `scapy/compat.py` -> **Severity: 25.442** (Embedded: 0.5005 * Error Risk: 50.8333%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `scapy/packet.py` -> **Severity: 10255.4** (Blast Radius: 102.554 * Doc Risk: 100.0%)
- `scapy/config.py` -> **Severity: 8163.5** (Blast Radius: 81.635 * Doc Risk: 100.0%)
- `scapy/compat.py` -> **Severity: 5970.618** (Blast Radius: 65.689 * Doc Risk: 90.8922%)
- `scapy/error.py` -> **Severity: 5824.446** (Blast Radius: 58.577 * Doc Risk: 99.4323%)
- `scapy/fields.py` -> **Severity: 3608.31** (Blast Radius: 36.091 * Doc Risk: 99.9781%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
