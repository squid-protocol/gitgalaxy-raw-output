# ARCHITECTURAL_BRIEF: impacket
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/impacket` |
| **Timestamp** | `2026-08-03T20:58:50.053158+00:00` |
| **Scan Duration** | `2.85s` |
| **Git Branch** | `master` |
| **Git Commit** | `76ee87746d49522fc9c3f8d8fc8d5b15126d389e` |
| **Git Remote** | `https://github.com/fortra/impacket.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 315 malicious artifacts.

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
| Total Artifacts | 351 |
| Analyzed Artifacts (Scanned) | 321 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 30 |
| Total LOC | 120301 |
| Volatility Index | 0.016 |
| % Scanned of codebase = | 91.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4986 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1245 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8498 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 34 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 314 | 120289 | 97.8% |
| MARKDOWN | 4 | 0 | 1.2% |
| PLAINTEXT | 2 | 0 | 0.6% |
| DOCKERFILE | 1 | 12 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.162`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 146 | 45.5% |
| file_cluster_8 | 135 | 42.1% |
| file_cluster_9 | 17 | 5.3% |
| file_cluster_17 | 10 | 3.1% |
| file_cluster_0 | 6 | 1.9% |
| file_cluster_12 | 1 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 1.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 30*

**Composition by Extension & Reason:**
- `.py`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 23 exceeds 500 chars), 1x Excluded (Saturation: Line 92 exceeds 500 chars)
- `no_extension`: 6x Excluded (Binary Format Detected), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.template`: 1x Excluded (Unsupported Extension: '.template')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 21.8 | 14.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 83.5 | 15.7 | 6.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 14.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 18.0 | 0.0 | 0.0 |
| API Exposure | 0.0 | 15.5 | 5.5 | 5.5 | 0.0 |
| Concurrency Exposure | 0.0 | 83.7 | 1.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 14.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 48.0 | 7.1 | 5.6 | 23.1 |
| Specification Exposure | 6.7 | 100.0 | 95.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.8 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 8.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 80.6 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 76.6 | 100.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `impacket/smbserver.py` (Hits: 181)
- `examples/psexec.py` (Hits: 30)
- `examples/goldenPac.py` (Hits: 28)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **rpcrt.py** (`impacket/dcerpc/v5/rpcrt.py`) — 72 inbound connections
2. **dtypes.py** (`impacket/dcerpc/v5/dtypes.py`) — 68 inbound connections
3. **utils.py** (`impacket/examples/utils.py`) — 59 inbound connections
4. **ndr.py** (`impacket/dcerpc/v5/ndr.py`) — 52 inbound connections
5. **uuid.py** (`impacket/uuid.py`) — 50 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **goldenPac.py** (`examples/goldenPac.py`) — 43 outbound dependencies
2. **secretsdump.py** (`impacket/examples/secretsdump.py`) — 43 outbound dependencies
3. **raiseChild.py** (`examples/raiseChild.py`) — 41 outbound dependencies
4. **smbserver.py** (`impacket/smbserver.py`) — 35 outbound dependencies
5. **ticketer.py** (`examples/ticketer.py`) — 31 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_kerberos_auth` (@ `impacket/smbserver.py`) -> Impact: **5739.4** | LOC: 2508
- `__decryptHash` (@ `impacket/examples/secretsdump.py`) -> Impact: **3333.4** | LOC: 615
- `read` (@ `examples/ntfs-read.py`) -> Impact: **2735.4** | LOC: 949
  * *Intent:* # Clamp read to data_size (EOF) if offset >= self.data_size: return b'' length = min(length, self.data_size - offset) self.ClusterSize = self.NTFSVolu...
- `findFirst2` (@ `impacket/smbserver.py`) -> Impact: **2700.5** | LOC: 671
- `addComputer` (@ `impacket/examples/ntlmrelayx/attacks/ldapattack.py`) -> Impact: **2628.6** | LOC: 771
- `__extract_local_history` (@ `impacket/examples/regsecrets.py`) -> Impact: **2504.2** | LOC: 622
- `bind` (@ `impacket/dcerpc/v5/rpcrt.py`) -> Impact: **2461.5** | LOC: 706
- `__init__` (@ `impacket/examples/smbclient.py`) -> Impact: **2396.4** | LOC: 658
  * *Intent:* #If the tcpShell parameter is passed (used in ntlmrelayx), # all input and output is redirected to a tcp socket # instead of to stdin / stdout if tcpS...
- `__str__` (@ `impacket/dcerpc/v5/dcom/wmi.py`) -> Impact: **2181.7** | LOC: 3408
- `getData` (@ `impacket/structure.py`) -> Impact: **2149.0** | LOC: 545

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `processRecord` (@ `examples/GetADUsers.py`) -> **O(2^N) [Recursive]**
- `run` (@ `examples/GetNPUsers.py`) -> **O(2^N) [Recursive]**
- `backup` (@ `examples/dacledit.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `examples/dacledit.py`) -> **O(2^N) [Recursive]**
- `remove` (@ `examples/dacledit.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Creates ACEs with the specified GUIDs and the SID, or FullControl if no GUID is specified # These ACEs will be used as comparison templates if self....
- `getInterface` (@ `examples/dcomexec.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Now let's parse the answer and build an Interface instance objRefType = OBJREF(b''.join(resp))['flags'] objRef = None if objRefType == FLAGS_OBJREF_...
- `exportTable` (@ `examples/esentutl.py`) -> **O(2^N) [Recursive]**
- `print_htable` (@ `examples/exchanger.py`) -> **O(2^N) [Recursive]**
- `getForestSid` (@ `examples/goldenPac.py`) -> **O(2^N) [Recursive]**
- `findFirst2` (@ `examples/karmaSMB.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `_kerberos_auth` (@ `impacket/smbserver.py`) -> DB Complexity: **360**
- `__init__` (@ `impacket/examples/smbclient.py`) -> DB Complexity: **132**
  * *Intent:* #If the tcpShell parameter is passed (used in ntlmrelayx), # all input and output is redirected to a tcp socket # instead of to stdin / stdout if tcpS...
- `read` (@ `examples/ntfs-read.py`) -> DB Complexity: **122**
  * *Intent:* # Clamp read to data_size (EOF) if offset >= self.data_size: return b'' length = min(length, self.data_size - offset) self.ClusterSize = self.NTFSVolu...
- `findFirst2` (@ `impacket/smbserver.py`) -> DB Complexity: **105**
- `smbComTreeDisconnect` (@ `impacket/smbserver.py`) -> DB Complexity: **99**
- `bind` (@ `impacket/dcerpc/v5/rpcrt.py`) -> DB Complexity: **90**
- `send` (@ `impacket/nmb.py`) -> DB Complexity: **80**
  * *Intent:* # We try to bind to a port for 10 tries try: s.bind((INADDR_ANY, rand.randint(10000, 60000))) s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) ...
- `smbTransaction` (@ `impacket/smbserver.py`) -> DB Complexity: **77**
- `get_server_time` (@ `impacket/smb.py`) -> DB Complexity: **65**
  * *Intent:* # filename = "\PIPE\epmapper" # ntCreate = SMBCommand(SMB.SMB_COM_NT_CREATE_ANDX) # ntCreate['Data'] = SMBNtCreateAndX_Data() # ntCreate['Parameters']...
- `_initializeTransport` (@ `examples/DumpNTLMInfo.py`) -> DB Complexity: **64**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `impacket` | 40 | 43791.68 | 22.46% | 50.92% |
| `examples` | 68 | 42680.48 | 34.4% | 0.0% |
| `impacket/dcerpc/v5` | 35 | 22862.6 | 11.44% | 47.48% |
| `impacket/examples` | 11 | 19912.52 | 31.65% | 0.0% |
| `impacket/examples/ntlmrelayx/servers` | 11 | 13595.49 | 37.08% | 0.0% |
| `tests/dcerpc` | 21 | 5917.68 | 4.23% | 0.0% |
| `impacket/krb5` | 11 | 5741.02 | 24.72% | 31.78% |
| `impacket/examples/ntlmrelayx/attacks` | 9 | 5029.7 | 31.53% | 0.0% |
| `impacket/dcerpc/v5/dcom` | 6 | 4046.64 | 6.75% | 51.42% |
| `impacket/examples/ntlmrelayx/clients` | 10 | 2859.86 | 39.32% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `impacket/IP6_Extension_Headers.py` -> **100.0%** Exposure
- `impacket/ImpactDecoder.py` -> **100.0%** Exposure
- `impacket/cdp.py` -> **100.0%** Exposure
- `impacket/dcerpc/v5/transport.py` -> **100.0%** Exposure
- `impacket/krb5/crypto.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `impacket/examples/ntlmrelayx/utils/config.py` -> **100.0%** Exposure
- `impacket/examples/ntlmrelayx/utils/enum.py` -> **100.0%** Exposure
- `impacket/examples/ntlmrelayx/utils/targetsutils.py` -> **100.0%** Exposure
- `impacket/examples/ntlmrelayx/utils/tcpshell.py` -> **100.0%** Exposure
- `impacket/http.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `impacket/ImpactDecoder.py` -> **0** Orphaned Functions | **101** Duplicates
- `impacket/dcerpc/v5/dcom/comev.py` -> **63** Orphaned Functions | **38** Duplicates
- `impacket/dot11.py` -> **0** Orphaned Functions | **98** Duplicates
- `impacket/examples/os_ident.py` -> **6** Orphaned Functions | **83** Duplicates
- `tests/dcerpc/test_samr.py` -> **89** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`examples/attrib.py`** -> AI Confidence: **99.39%**
2. **`examples/secretsdump.py`** -> AI Confidence: **99.39%**
3. **`examples/smbserver.py`** -> AI Confidence: **99.39%**
4. **`impacket/examples/ldap_shell.py`** -> AI Confidence: **99.39%**
5. **`examples/services.py`** -> AI Confidence: **99.35%**
6. **`examples/Get-GPPPassword.py`** -> AI Confidence: **99.31%**
7. **`examples/GetADComputers.py`** -> AI Confidence: **99.31%**
8. **`examples/GetADUsers.py`** -> AI Confidence: **99.31%**
9. **`examples/GetNPUsers.py`** -> AI Confidence: **99.31%**
10. **`examples/GetUserSPNs.py`** -> AI Confidence: **99.31%**
11. **`examples/addcomputer.py`** -> AI Confidence: **99.31%**
12. **`examples/atexec.py`** -> AI Confidence: **99.31%**
13. **`examples/badsuccessor.py`** -> AI Confidence: **99.31%**
14. **`examples/changepasswd.py`** -> AI Confidence: **99.31%**
15. **`examples/checkMSSQLStatus.py`** -> AI Confidence: **99.31%**
16. **`examples/dacledit.py`** -> AI Confidence: **99.31%**
17. **`examples/dcomexec.py`** -> AI Confidence: **99.31%**
18. **`examples/describeTicket.py`** -> AI Confidence: **99.31%**
19. **`examples/dpapi.py`** -> AI Confidence: **99.31%**
20. **`examples/esentutl.py`** -> AI Confidence: **99.31%**
21. **`examples/exchanger.py`** -> AI Confidence: **99.31%**
22. **`examples/filetime.py`** -> AI Confidence: **99.31%**
23. **`examples/findDelegation.py`** -> AI Confidence: **99.31%**
24. **`examples/getST.py`** -> AI Confidence: **99.31%**
25. **`examples/karmaSMB.py`** -> AI Confidence: **99.31%**
26. **`examples/keylistattack.py`** -> AI Confidence: **99.31%**
27. **`examples/mssqlclient.py`** -> AI Confidence: **99.31%**
28. **`examples/net.py`** -> AI Confidence: **99.31%**
29. **`examples/netview.py`** -> AI Confidence: **99.31%**
30. **`examples/ntlmrelayx.py`** -> AI Confidence: **99.31%**
31. **`examples/owneredit.py`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `impacket/dcerpc/v5/epm.py` -> **100.0%** Exposure
- `tests/SMB_RPC/test_acl.py` -> **100.0%** Exposure
- `tests/misc/test_dpapi.py` -> **100.0%** Exposure
- `impacket/krb5/crypto.py` -> **96.5099%** Exposure
- `tests/misc/test_dns.py` -> **0.0565%** Exposure
### Exploit Generation Surface
- `examples/CheckLDAPStatus.py` -> **100.0%** Exposure
- `examples/DumpNTLMInfo.py` -> **100.0%** Exposure
- `examples/Get-GPPPassword.py` -> **100.0%** Exposure
- `examples/GetADComputers.py` -> **100.0%** Exposure
- `examples/GetADUsers.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `examples/net.py` -> **100.0%** Exposure
- `examples/raiseChild.py` -> **100.0%** Exposure
- `examples/smbexec.py` -> **100.0%** Exposure
- `examples/wmiquery.py` -> **100.0%** Exposure
- `impacket/dcerpc/v5/dcom/comev.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `examples/DumpNTLMInfo.py` -> **100.0%** Exposure
- `examples/Get-GPPPassword.py` -> **100.0%** Exposure
- `examples/GetADComputers.py` -> **100.0%** Exposure
- `examples/GetADUsers.py` -> **100.0%** Exposure
- `examples/GetLAPSPassword.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2730` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `impacket/krb5/types.py` (PYTHON) -> Cumulative Risk: **806.35**
- **Archetype:** `file_cluster_13` (Distance: 12.969 IQR)
- **Magnitude:** 398.46 | **LOC:** 288 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 97.4), `__eq__` (Impact: 26.4), `from_asn1` (Impact: 14.4)

### 2. `impacket/krb5/crypto.py` (PYTHON) -> Cumulative Risk: **799.86**
- **Archetype:** `file_cluster_0` (Distance: 10.488 IQR)
- **Magnitude:** 873.76 | **LOC:** 771 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `generate_kerberos_keys` (Impact: 180.6), `mit_des_string_to_key` (Impact: 123.4), `decrypt` (Impact: 45.6)

### 3. `impacket/krb5/keytab.py` (PYTHON) -> Cumulative Risk: **793.89**
- **Archetype:** `file_cluster_13` (Distance: 12.663 IQR)
- **Magnitude:** 676.44 | **LOC:** 293 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getKey` (Impact: 284.0), `prettyPrint` (Impact: 236.4), `getData` (Impact: 14.1)

### 4. `impacket/dcerpc/v5/transport.py` (PYTHON) -> Cumulative Risk: **793.78**
- **Archetype:** `file_cluster_13` (Distance: 12.414 IQR)
- **Magnitude:** 1167.2 | **LOC:** 606 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 83.7), `recv` (Impact: 72.7), `send` (Impact: 67.6)

### 5. `impacket/dcerpc/v5/rpcrt.py` (PYTHON) -> Cumulative Risk: **752.27**
- **Archetype:** `file_cluster_8` (Distance: 10.926 IQR)
- **Magnitude:** 3481.68 | **LOC:** 2268 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `bind` (Impact: 2461.5), `request` (Impact: 135.8), `set_credentials` (Impact: 48.4)

### 6. `impacket/pcapfile.py` (PYTHON) -> Cumulative Risk: **750.0**
- **Archetype:** `file_cluster_13` (Distance: 11.76 IQR)
- **Magnitude:** 121.88 | **LOC:** 121 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9908%), Documentation (99.956%)
- **Heaviest Functions:** `read` (Impact: 10.8), `packets` (Impact: 10.7), `__init__` (Impact: 6.2)

### 7. `impacket/ImpactPacket.py` (PYTHON) -> Cumulative Risk: **739.99**
- **Archetype:** `file_cluster_8` (Distance: 10.912 IQR)
- **Magnitude:** 3438.5 | **LOC:** 2151 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__str__` (Impact: 836.5), `add_option` (Impact: 713.5), `get_header_size` (Impact: 562.2)

### 8. `impacket/winregistry.py` (PYTHON) -> Cumulative Risk: **735.37**
- **Archetype:** `file_cluster_13` (Distance: 11.322 IQR)
- **Magnitude:** 1823.56 | **LOC:** 809 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__walkSubNodes` (Impact: 1094.3), `printValue` (Impact: 209.2), `__setValueData` (Impact: 142.2)

### 9. `impacket/IP6_Extension_Headers.py` (PYTHON) -> Cumulative Risk: **732.82**
- **Archetype:** `file_cluster_8` (Distance: 10.307 IQR)
- **Magnitude:** 319.14 | **LOC:** 332 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `get_extension_headers` (Impact: 35.3), `add_padding` (Impact: 31.0), `get_decoder` (Impact: 27.6)

### 10. `impacket/nmb.py` (PYTHON) -> Cumulative Risk: **722.25**
- **Archetype:** `file_cluster_13` (Distance: 11.704 IQR)
- **Magnitude:** 1424.96 | **LOC:** 1015 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.1017%)
- **Heaviest Functions:** `send` (Impact: 848.9), `polling_read` (Impact: 85.6), `non_polling_read` (Impact: 41.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `impacket/smbserver.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.131 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.019 IQR)
- **Top Global Matches:** file_cluster_8: 12.131, file_cluster_0: 12.185, file_cluster_13: 12.3
- **Magnitude:** 12748.28 | **LOC:** 5408 | **CtrlFlow:** 64.0% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 360
- **Risk Profile:** Cognitive Load (42.4677%), Tech Debt (13.1635%)
**Top Internal Functions/Classes:**
  * `_kerberos_auth` (Impact: 5739.4 | O(2^N) | DB: 360)
  * `findFirst2` (Impact: 2700.5 | O(2^N) | DB: 105)
  * `smbTransaction` (Impact: 1388.9 | O(N^6) | DB: 77)
  * `outputToJohnFormat` (Impact: 608.3 | O(2^N) | DB: 58)
    * *Intent:* # We don't want to add a possible failure here, since this is an # extra bonus. We try, if it fails,...
  * `smbComTreeDisconnect` (Impact: 553.7 | O(N^6) | DB: 99)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 921`, `structural_boundaries: 519`, `args: 156`, `func_start: 156`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 74`, `state_mutation: 403`, `dead_code: 11`, `planned_debt: 39`, `fragile_debt: 3`
* *Architecture:* `io: 181`, `api: 162`, `concurrency: 7`, `import: 39`
* *Defense:* `safety: 109`, `doc: 22`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.627
  * `Choke Point (Betweenness):` 0.001127 | `Ripple Effect (Closeness):` 0.034615
  * `Imports (Out-Degree: 8):` impacket.nt_errors, impacket.dcerpc.v5.dtypes, struct, sys, six.moves, impacket.dcerpc.v5.srvs, impacket.dcerpc.v5, random...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `impacket/examples/secretsdump.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.396 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.495 IQR)
- **Top Global Matches:** file_cluster_8: 12.396, file_cluster_13: 12.59, file_cluster_17: 12.752
- **Magnitude:** 7602.84 | **LOC:** 3722 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 60
- **Risk Profile:** Cognitive Load (47.2353%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__decryptHash` (Impact: 3333.4 | O(2^N) | DB: 15)
  * `dump` (Impact: 1071.3 | O(N^6) | DB: 41)
  * `__getLastVSS` (Impact: 780.9 | O(2^N) | DB: 18)
  * `__str__` (Impact: 489.1 | O(N^6) | DB: 60)
  * `beginTransaction` (Impact: 408.1 | O(N^6) | DB: 37)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 698`, `structural_boundaries: 477`, `args: 130`, `func_start: 127`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 93`, `high_risk_execution: 1`, `state_mutation: 388`, `dead_code: 4`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 13`, `api: 115`, `import: 47`
* *Defense:* `safety: 129`, `doc: 4`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.677
  * `Choke Point (Betweenness):` 0.001666 | `Ripple Effect (Closeness):` 0.028409
  * `Imports (Out-Degree: 17):` impacket.nt_errors, impacket.dcerpc.v5.dtypes, codecs, struct, impacket.crypto, Cryptodome.Cipher, impacket.dcerpc.v5.dcomrt, re...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `impacket/dcerpc/v5/ndr.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.258 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.963 IQR)
- **Top Global Matches:** file_cluster_8: 12.258, file_cluster_0: 12.339, file_cluster_17: 12.388
- **Magnitude:** 4579.28 | **LOC:** 1721 | **CtrlFlow:** 60.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (27.1316%), Tech Debt (98.0976%)
**Top Internal Functions/Classes:**
  * `__setitem__` (Impact: 1651.2 | O(2^N))
  * `getData` (Impact: 782.4 | O(2^N) | DB: 3)
  * `fromString` (Impact: 569.2 | O(2^N) | DB: 10)
  * `getData` (Impact: 288.0 | O(N^6) | DB: 5)
  * `changeTransferSyntax` (Impact: 195.6 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 365`, `structural_boundaries: 235`, `args: 70`, `func_start: 70`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 101`, `dead_code: 9`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 19`
* *Architecture:* `api: 83`, `import: 9`
* *Defense:* `safety: 116`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 40.401
  * `Choke Point (Betweenness):` 0.001193 | `Ripple Effect (Closeness):` 0.214663
  * `Imports (Out-Degree: 2):` impacket.dcerpc.v5.enum, struct, impacket, inspect, __future__, random, six, impacket.uuid
  * `Imported By (In-Degree: 52):` (Excluded from Brief to save tokens)

### `impacket/examples/ntlmrelayx/servers/socksserver.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.453 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.011 IQR)
- **Top Global Matches:** file_cluster_13: 11.453, file_cluster_17: 11.585, file_cluster_0: 11.601
- **Magnitude:** 4005.11 | **LOC:** 506 | **CtrlFlow:** 47.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (46.3159%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 87`, `args: 21`, `func_start: 21`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 84`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 7`, `api: 28`, `concurrency: 1`, `import: 15`
* *Defense:* `safety: 12`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.953
  * `Choke Point (Betweenness):` 0.000339 | `Ripple Effect (Closeness):` 0.055125
  * `Imports (Out-Degree: 2):` impacket.examples, time, socketserver, struct, socket, impacket, flask, __future__...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `impacket/dcerpc/v5/rpcrt.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.926 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.063 IQR)
- **Top Global Matches:** file_cluster_8: 10.926, file_cluster_7: 11.355, file_cluster_13: 11.369
- **Magnitude:** 3481.68 | **LOC:** 2268 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 90
- **Risk Profile:** Cognitive Load (31.91%), Tech Debt (97.445%)
**Top Internal Functions/Classes:**
  * `bind` (Impact: 2461.5 | O(2^N) | DB: 90)
  * `request` (Impact: 135.8 | O(2^N) | DB: 4)
  * `set_credentials` (Impact: 48.4 | O(N^4) | DB: 10)
  * `__init__` (Impact: 45.4 | O(2^N) | DB: 5)
    * *Intent:* """ def __init__(self, error_string=None, error_code=None, packet=None): """
  * `processRequest` (Impact: 31.7 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 205`, `args: 79`, `func_start: 79`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 286`, `dead_code: 2`, `planned_debt: 6`, `fragile_debt: 1`, `duplicate_logic: 30`
* *Architecture:* `io: 8`, `api: 93`, `concurrency: 1`, `import: 19`
* *Defense:* `safety: 14`, `doc: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.017
  * `Choke Point (Betweenness):` 0.002621 | `Ripple Effect (Closeness):` 0.241472
  * `Imports (Out-Degree: 4):` impacket.dcerpc.v5.ndr, impacket.dcerpc.v5.dtypes, socket, impacket, impacket.krb5, threading, Cryptodome.Cipher, sys...
  * `Imported By (In-Degree: 72):` (Excluded from Brief to save tokens)

### `impacket/ImpactPacket.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.912 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.749 IQR)
- **Top Global Matches:** file_cluster_8: 10.912, file_cluster_7: 11.243, file_cluster_13: 11.32
- **Magnitude:** 3438.5 | **LOC:** 2151 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (20.5536%), Tech Debt (99.4452%)
**Top Internal Functions/Classes:**
  * `__str__` (Impact: 836.5 | O(2^N) | DB: 4)
  * `add_option` (Impact: 713.5 | O(2^N) | DB: 7)
    * *Intent:* # def calculate_checksum(self, buffer = None): # tmp_value = self.get_ip_sum() # if self.auto_checks...
  * `get_header_size` (Impact: 562.2 | O(2^N) | DB: 16)
  * `get_packet` (Impact: 40.0 | O(N^3) | DB: 1)
  * `get_code_name` (Impact: 30.8 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 617`, `args: 326`, `func_start: 321`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 122`, `dead_code: 5`, `planned_debt: 2`, `duplicate_logic: 32`
* *Architecture:* `io: 7`, `api: 347`, `import: 9`
* *Defense:* `safety: 2`, `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 39.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.088167
  * `Imports (Out-Degree: 0):` struct, socket, __future__, functools, string, sys, array, binascii
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `impacket/examples/regsecrets.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.961 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.843 IQR)
- **Top Global Matches:** file_cluster_8: 11.961, file_cluster_13: 12.041, file_cluster_17: 12.315
- **Magnitude:** 3397.18 | **LOC:** 1111 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (62.9929%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__extract_local_history` (Impact: 2504.2 | O(2^N) | DB: 42)
  * `getBootKey` (Impact: 327.8 | O(N^6) | DB: 25)
  * `__checkServiceStatus` (Impact: 138.8 | O(2^N) | DB: 9)
  * `getMachineKerberosSalt` (Impact: 123.7 | O(2^N))
    * *Intent:* """ Returns Kerberos salt for the current connection if we have the correct information """
  * `finish` (Impact: 47.7 | O(N^5))
    * *Intent:* # If service is stopped it'll trigger an exception # If service does not exist it'll trigger an exce...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 181`, `args: 45`, `func_start: 45`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 166`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 28`, `import: 23`
* *Defense:* `safety: 57`, `doc: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.694
  * `Choke Point (Betweenness):` 0.000152 | `Ripple Effect (Closeness):` 0.003125
  * `Imports (Out-Degree: 5):` codecs, struct, impacket.crypto, re, impacket.dcerpc.v5, impacket.system_errors, impacket.structure, time...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/ntfs-read.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.538 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.435 IQR)
- **Top Global Matches:** file_cluster_8: 11.538, file_cluster_13: 11.717, file_cluster_7: 11.879
- **Magnitude:** 3352.64 | **LOC:** 1458 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 122
- **Risk Profile:** Cognitive Load (48.8984%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `read` (Impact: 2735.4 | O(2^N) | DB: 122)
    * *Intent:* # Clamp read to data_size (EOF) if offset >= self.data_size: return b'' length = min(length, self.da...
  * `__init__` (Impact: 135.8 | O(2^N) | DB: 8)
  * `readClusters` (Impact: 112.5 | O(2^N))
  * `__init__` (Impact: 12.3 | O(N^3) | DB: 4)
  * `__init__` (Impact: 6.9 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 278`, `args: 101`, `func_start: 99`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 195`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 12`, `api: 109`, `import: 14`
* *Defense:* `safety: 12`, `doc: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.397
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` impacket.examples, struct, impacket, argparse, __future__, datetime, sys, ntpath...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `impacket/smb.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.304 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.499 IQR)
- **Top Global Matches:** file_cluster_8: 11.304, file_cluster_7: 11.64, file_cluster_13: 11.71
- **Magnitude:** 3352.24 | **LOC:** 4666 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 65
- **Risk Profile:** Cognitive Load (21.4329%), Tech Debt (87.3282%)
**Top Internal Functions/Classes:**
  * `get_server_time` (Impact: 1082.4 | O(N^6) | DB: 65)
    * *Intent:* # filename = "\PIPE\epmapper" # ntCreate = SMBCommand(SMB.SMB_COM_NT_CREATE_ANDX) # ntCreate['Data']...
  * `__init__` (Impact: 154.5 | O(N^5) | DB: 55)
  * `neg_session` (Impact: 100.8 | O(N^6) | DB: 6)
  * `tree_connect_andx` (Impact: 95.3 | O(N^4) | DB: 8)
  * `__init__` (Impact: 59.1 | O(N^4) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 532`, `args: 164`, `func_start: 164`, `class_start: 144`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 362`, `dead_code: 5`, `planned_debt: 6`, `fragile_debt: 13`, `duplicate_logic: 33`
* *Architecture:* `io: 15`, `api: 349`, `import: 22`
* *Defense:* `safety: 45`, `doc: 60`, `sync_locks: 3`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.203
  * `Choke Point (Betweenness):` 0.000821 | `Ripple Effect (Closeness):` 0.111197
  * `Imports (Out-Degree: 6):` struct, contextlib, impacket.structure, os, impacket.krb5.asn1, ctypes, pyasn1.type.univ, impacket.krb5.types...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `impacket/examples/ntlmrelayx/attacks/ldapattack.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.028 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.07 IQR)
- **Top Global Matches:** file_cluster_8: 11.028, file_cluster_13: 11.143, file_cluster_17: 11.383
- **Magnitude:** 3308.96 | **LOC:** 1202 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (24.087%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addComputer` (Impact: 2628.6 | O(2^N) | DB: 37)
  * `run` (Impact: 439.1 | O(N^6) | DB: 9)
  * `__init__` (Impact: 74.4 | O(2^N) | DB: 3)
  * `fromString` (Impact: 28.4 | O(2^N))
  * `__init__` (Impact: 5.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 168`, `args: 29`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 86`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 29`, `import: 30`
* *Defense:* `safety: 29`, `doc: 8`, `test: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.397
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` dns.resolver, ldap3, codecs, ldap3.protocol.formatters.formatters, impacket.ldap.ldaptypes, ldap3.utils.conv, ldapdomaindump, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `impacket/smb3.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.223 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.566 IQR)
- **Top Global Matches:** file_cluster_8: 11.223, file_cluster_13: 11.398, file_cluster_6: 11.63
- **Magnitude:** 3308.6 | **LOC:** 2104 | **CtrlFlow:** 57.2% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (28.8146%), Tech Debt (20.9253%)
**Top Internal Functions/Classes:**
  * `__str__` (Impact: 891.5 | O(N^6) | DB: 53)
  * `timestampForSnapshot` (Impact: 744.8 | O(2^N) | DB: 7)
  * `login` (Impact: 371.3 | O(N^6) | DB: 8)
    * *Intent:* # If we have hashes, normalize them if lmhash != '' or nthash != '': if len(lmhash) % 2: lmhash = '0...
  * `create` (Impact: 185.3 | O(N^4))
  * `write` (Impact: 172.0 | O(2^N))
    * *Intent:* # IMPORTANT NOTE: As you can see, this was coded as a recursive function # Hence, you can exhaust th...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 309`, `structural_boundaries: 231`, `args: 77`, `func_start: 77`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 132`, `dead_code: 4`, `planned_debt: 34`
* *Architecture:* `io: 4`, `api: 87`, `import: 34`
* *Defense:* `safety: 36`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.965
  * `Choke Point (Betweenness):` 0.000205 | `Ripple Effect (Closeness):` 0.009375
  * `Imports (Out-Degree: 9):` copy, impacket.nt_errors, struct, contextlib, Cryptodome.Cipher, random, Cryptodome.Hash, impacket.krb5.asn1...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `impacket/dot11.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.079 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.202 IQR)
- **Top Global Matches:** file_cluster_8: 10.079, file_cluster_7: 10.646, file_cluster_0: 10.828
- **Magnitude:** 2871.18 | **LOC:** 3093 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (8.3033%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `__set_field_values` (Impact: 516.2 | O(2^N) | DB: 1)
  * `get_supported_rates` (Impact: 383.5 | O(2^N) | DB: 2)
  * `get_supported_rates` (Impact: 259.5 | O(2^N) | DB: 2)
  * `get_supported_rates` (Impact: 71.6 | O(N^5) | DB: 1)
  * `_set_element` (Impact: 58.0 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 680`, `args: 333`, `func_start: 332`, `class_start: 60`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 11`, `dead_code: 16`, `planned_debt: 4`, `duplicate_logic: 98`
* *Architecture:* `api: 430`, `import: 4`
* *Defense:* `safety: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.71
  * `Choke Point (Betweenness):` 0.000392 | `Ripple Effect (Closeness):` 0.06875
  * `Imports (Out-Degree: 2):` binascii, impacket.Dot11Crypto, struct, impacket.ImpactPacket
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `impacket/dcerpc/v5/dcom/wmi.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.392 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.338 IQR)
- **Top Global Matches:** file_cluster_8: 10.392, file_cluster_7: 10.929, file_cluster_13: 11.009
- **Magnitude:** 2672.28 | **LOC:** 3491 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 49
- **Risk Profile:** Cognitive Load (10.1395%), Tech Debt (8.848%)
**Top Internal Functions/Classes:**
  * `__str__` (Impact: 2181.7 | O(N^6) | DB: 49)
  * `format_structure` (Impact: 56.1 | O(2^N))
  * `__init__` (Impact: 6.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 442`, `args: 102`, `func_start: 98`, `class_start: 193`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 117`, `dead_code: 6`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `api: 257`, `import: 20`
* *Defense:* `safety: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.694
  * `Choke Point (Betweenness):` 3.8e-05 | `Ripple Effect (Closeness):` 0.003125
  * `Imports (Out-Degree: 8):` copy, impacket.dcerpc.v5.ndr, impacket.dcerpc.v5.dcom.oaut, impacket.dcerpc.v5.dtypes, struct, impacket.dcerpc.v5.enum, impacket, __future__...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `impacket/examples/os_ident.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.702 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.633 IQR)
- **Top Global Matches:** file_cluster_8: 10.702, file_cluster_7: 11.202, file_cluster_13: 11.208
- **Magnitude:** 2656.12 | **LOC:** 2185 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (38.1463%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `add_seqclass` (Impact: 316.1 | O(N^6) | DB: 14)
  * `process` (Impact: 170.7 | O(N^4) | DB: 7)
    * *Intent:* # R, DFI, T*, TG*, TOSI, CD, SI, DLI* if self.icmp_num_responses != 2: self.add_result("R","N") retu...
  * `process` (Impact: 156.4 | O(N^4))
  * `get_win` (Impact: 144.9 | O(N^6))
    * *Intent:* # TCP initial window size (W, W1-W6) # This test simply records the 16-bit TCP window size of the re...
  * `process` (Impact: 106.8 | O(N^5) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 319`, `structural_boundaries: 402`, `args: 170`, `func_start: 169`, `class_start: 48`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 154`, `dead_code: 2`, `fragile_debt: 2`, `duplicate_logic: 83`, `orphaned_logic: 6`
* *Architecture:* `io: 1`, `api: 167`, `import: 9`
* *Defense:* `safety: 4`, `test: 24`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.397
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` impacket, pcapy, math, impacket.ImpactDecoder, warnings, six.moves, array, impacket.ImpactPacket
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `impacket/examples/smbclient.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.339 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.58 IQR)
- **Top Global Matches:** file_cluster_13: 12.339, file_cluster_8: 12.485, file_cluster_0: 12.682
- **Magnitude:** 2626.0 | **LOC:** 731 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 132
- **Risk Profile:** Cognitive Load (60.1852%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 2396.4 | O(2^N) | DB: 132)
    * *Intent:* #If the tcpShell parameter is passed (used in ntlmrelayx), # all input and output is redirected to a...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 126`, `args: 41`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 177`, `dead_code: 1`
* *Architecture:* `io: 23`, `api: 41`, `import: 19`
* *Defense:* `safety: 19`, `doc: 2`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.942
  * `Choke Point (Betweenness):` 0.000104 | `Ripple Effect (Closeness):` 0.00625
  * `Imports (Out-Degree: 4):` impacket.smb3structs, impacket.dcerpc.v5.dtypes, time, getpass, charset_normalizer, impacket, __future__, io...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `impacket/structure.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.916 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.08 IQR)
- **Top Global Matches:** file_cluster_8: 10.916, file_cluster_13: 11.078, file_cluster_0: 11.222
- **Magnitude:** 2289.48 | **LOC:** 687 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (55.7159%), Tech Debt (15.2942%)
**Top Internal Functions/Classes:**
  * `getData` (Impact: 2149.0 | O(2^N) | DB: 6)
  * `packField` (Impact: 48.8 | O(2^N))
    * *Intent:* %s will output a string %s\\x00 will output a NUL terminated string %d%d will output 2 decimal digit...
  * `__init__` (Impact: 16.6 | O(N^3) | DB: 5)
  * `fromFile` (Impact: 2.8 | O(N^2))
  * `setAlignment` (Impact: 2.7 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 136`, `args: 27`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 33`, `dead_code: 2`, `fragile_debt: 2`
* *Architecture:* `api: 25`, `import: 7`
* *Defense:* `safety: 25`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 83.354
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.327896
  * `Imports (Out-Degree: 0):` struct, __future__, re, binascii, six
  * `Imported By (In-Degree: 48):` (Excluded from Brief to save tokens)

### `impacket/tds.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.62 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.271 IQR)
- **Top Global Matches:** file_cluster_8: 10.62, file_cluster_13: 11.027, file_cluster_7: 11.146
- **Magnitude:** 2225.54 | **LOC:** 2318 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (24.7855%), Tech Debt (38.4779%)
**Top Internal Functions/Classes:**
  * `parseRow` (Impact: 721.9 | O(N^6) | DB: 4)
  * `_parseValue` (Impact: 415.2 | O(N^5))
  * `parseReply` (Impact: 122.0 | O(N^6) | DB: 4)
  * `printReplies` (Impact: 108.0 | O(N^6) | DB: 1)
  * `processColMeta` (Impact: 90.6 | O(N^5))
    * *Intent:* # - A NTLMSSP_CHALLENGE packet # - The response for the local authentication from the MSSQL server t...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 196`, `args: 42`, `func_start: 42`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 115`, `dead_code: 2`, `planned_debt: 9`, `duplicate_logic: 7`
* *Architecture:* `io: 17`, `api: 64`, `import: 27`
* *Defense:* `safety: 22`, `doc: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.684
  * `Choke Point (Betweenness):` 0.000434 | `Ripple Effect (Closeness):` 0.009375
  * `Imports (Out-Degree: 11):` struct, random, impacket.structure, impacket.mssql.version, impacket.krb5.asn1, math, uuid, decimal...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `examples/exchanger.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.076 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.832 IQR)
- **Top Global Matches:** file_cluster_8: 11.076, file_cluster_13: 11.25, file_cluster_0: 11.575
- **Magnitude:** 2070.58 | **LOC:** 1080 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (63.7629%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `print_htable` (Impact: 1389.0 | O(2^N) | DB: 13)
  * `run` (Impact: 272.6 | O(N^6) | DB: 18)
  * `_parse_and_set_htable` (Impact: 40.3 | O(N^4) | DB: 1)
  * `print` (Impact: 35.0 | O(2^N))
  * `_split_lines` (Impact: 30.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 130`, `args: 37`, `func_start: 37`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 103`, `dead_code: 1`, `duplicate_logic: 2`, `orphaned_logic: 4`
* *Architecture:* `io: 15`, `api: 32`, `import: 18`
* *Defense:* `safety: 12`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.397
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` impacket.examples, impacket.http, getpass, codecs, impacket.dcerpc.v5.rpch, impacket, argparse, __future__...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `impacket/dcerpc/v5/enum.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_12` (Drift: 12.693 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.121 IQR)
- **Top Global Matches:** file_cluster_12: 12.693, file_cluster_0: 12.786, file_cluster_17: 12.89
- **Magnitude:** 2042.2 | **LOC:** 765 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (49.5798%), Tech Debt (12.5845%)
**Top Internal Functions/Classes:**
  * `__new__` (Impact: 1907.0 | O(2^N) | DB: 3)
    * *Intent:* # enum overwriting a descriptor?
  * `__setitem__` (Impact: 90.9 | O(2^N) | DB: 1)
  * `__init__` (Impact: 5.3 | O(2^N) | DB: 1)
  * `__prepare__` (Impact: 3.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 141`, `args: 48`, `func_start: 47`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 20`, `dead_code: 7`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 7`, `import: 1`
* *Defense:* `safety: 40`, `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.190644
  * `Imports (Out-Degree: 0):` sys
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `examples/raiseChild.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.668 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.023 IQR)
- **Top Global Matches:** file_cluster_13: 11.668, file_cluster_8: 11.761, file_cluster_17: 12.008
- **Magnitude:** 1959.08 | **LOC:** 1319 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 51
- **Risk Profile:** Cognitive Load (24.2889%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getDNSMachineName` (Impact: 494.2 | O(2^N) | DB: 4)
  * `__decryptHash` (Impact: 383.9 | O(2^N) | DB: 4)
    * *Intent:* # Give me only the AES256
  * `makeGolden` (Impact: 209.6 | O(N^4) | DB: 2)
  * `__init__` (Impact: 184.0 | O(N^6) | DB: 13)
  * `raiseUp` (Impact: 154.0 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 188`, `args: 35`, `func_start: 35`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 33`, `high_risk_execution: 6`, `state_mutation: 110`, `dead_code: 2`, `duplicate_logic: 10`, `orphaned_logic: 5`
* *Architecture:* `io: 28`, `api: 34`, `concurrency: 1`, `import: 47`
* *Defense:* `safety: 54`, `doc: 2`, `sync_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.397
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` impacket.nt_errors, impacket.dcerpc.v5.ndr, impacket.dcerpc.v5.dtypes, struct, impacket.dcerpc.v5.lsad, sys, impacket.dcerpc.v5, random...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `impacket/krb5/kerberosv5.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.49 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.16 IQR)
- **Top Global Matches:** file_cluster_13: 11.49, file_cluster_8: 11.533, file_cluster_0: 11.92
- **Magnitude:** 1958.6 | **LOC:** 750 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (18.5551%), Tech Debt (9.975%)
**Top Internal Functions/Classes:**
  * `sendReceive` (Impact: 1784.4 | O(2^N) | DB: 32)
  * `__str__` (Impact: 109.9 | O(2^N) | DB: 5)
  * `__init__` (Impact: 4.3 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 110`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 40`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 7`, `api: 10`, `import: 23`
* *Defense:* `safety: 54`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.328
  * `Choke Point (Betweenness):` 0.003322 | `Ripple Effect (Closeness):` 0.155676
  * `Imports (Out-Degree: 8):` struct, random, impacket.krb5.asn1, pyasn1.type.univ, impacket.krb5.types, impacket.ntlm, impacket.smbconnection, pyasn1.codec.der...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `impacket/winregistry.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.322 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.609 IQR)
- **Top Global Matches:** file_cluster_13: 11.322, file_cluster_0: 11.336, file_cluster_8: 11.367
- **Magnitude:** 1823.56 | **LOC:** 809 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (37.2792%), Tech Debt (54.2374%)
**Top Internal Functions/Classes:**
  * `__walkSubNodes` (Impact: 1094.3 | O(2^N) | DB: 19)
  * `printValue` (Impact: 209.2 | O(N^5) | DB: 3)
  * `__setValueData` (Impact: 142.2 | O(2^N) | DB: 3)
  * `__init__` (Impact: 107.5 | O(N^6) | DB: 12)
  * `__findSubKey` (Impact: 50.4 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 158`, `args: 48`, `func_start: 48`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 61`, `dead_code: 5`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 5`, `api: 40`, `import: 11`
* *Defense:* `safety: 19`, `doc: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.946
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.0125
  * `Imports (Out-Degree: 1):` struct, abc, impacket, __future__, sys, re, ntpath, impacket.structure...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `examples/dacledit.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.782 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.972 IQR)
- **Top Global Matches:** file_cluster_13: 11.782, file_cluster_8: 11.811, file_cluster_17: 12.062
- **Magnitude:** 1822.02 | **LOC:** 794 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (46.9402%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `backup` (Impact: 653.6 | O(2^N) | DB: 23)
  * `__init__` (Impact: 396.0 | O(2^N) | DB: 28)
  * `printparsedACE` (Impact: 311.3 | O(N^6) | DB: 12)
  * `remove` (Impact: 293.7 | O(2^N) | DB: 6)
    * *Intent:* # Creates ACEs with the specified GUIDs and the SID, or FullControl if no GUID is specified # These ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 99`, `args: 20`, `func_start: 20`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 130`, `dead_code: 1`
* *Architecture:* `io: 6`, `api: 26`, `import: 21`
* *Defense:* `safety: 22`, `doc: 2`, `test: 3`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.397
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ldap3, codecs, ldap3.protocol.formatters.formatters, ldap3.utils.conv, sys, ldapdomaindump, os, ldap3.protocol.microsoft...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `impacket/examples/ldap_shell.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.787 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.277 IQR)
- **Top Global Matches:** file_cluster_8: 10.787, file_cluster_13: 11.02, file_cluster_7: 11.327
- **Magnitude:** 1697.5 | **LOC:** 759 | **CtrlFlow:** 72.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (22.7081%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 1007.8 | O(2^N) | DB: 23)
  * `do_search` (Impact: 386.2 | O(N^5) | DB: 4)
  * `do_clear_rbcd` (Impact: 99.2 | O(N^4))
  * `do_clear_shadow_creds` (Impact: 74.8 | O(N^5))
  * `do_dirsync` (Impact: 22.7 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 71`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 39`, `dead_code: 1`
* *Architecture:* `io: 4`, `api: 41`, `import: 16`
* *Defense:* `safety: 10`, `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.595
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003125
  * `Imports (Out-Degree: 3):` impacket.ldap, ldap3, ldap3.core.results, ldap3.protocol.microsoft, impacket.ldap.ldaptypes, impacket, shlex, impacket.examples.ntlmrelayx.utils...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `impacket/dcerpc/v5/dcomrt.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.602 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.749 IQR)
- **Top Global Matches:** file_cluster_8: 10.602, file_cluster_13: 11.053, file_cluster_7: 11.094
- **Magnitude:** 1618.08 | **LOC:** 1959 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 62
- **Risk Profile:** Cognitive Load (22.9859%), Tech Debt (68.0581%)
**Top Internal Functions/Classes:**
  * `initConnection` (Impact: 665.8 | O(N^6) | DB: 62)
  * `RemoteCreateInstance` (Impact: 232.2 | O(2^N) | DB: 11)
  * `pingServer` (Impact: 147.6 | O(2^N))
  * `initTimer` (Impact: 26.4 | O(N^5))
  * `__init__` (Impact: 16.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 247`, `args: 67`, `func_start: 67`, `class_start: 107`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 147`, `dead_code: 4`, `planned_debt: 3`, `duplicate_logic: 12`
* *Architecture:* `io: 2`, `api: 160`, `concurrency: 1`, `import: 11`
* *Defense:* `safety: 14`, `doc: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.302
  * `Choke Point (Betweenness):` 0.000122 | `Ripple Effect (Closeness):` 0.047232
  * `Imports (Out-Degree: 4):` impacket.dcerpc.v5.ndr, impacket.dcerpc.v5.dtypes, struct, socket, impacket, __future__, threading, traceback...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/SMB_RPC/test_smb.py` (PYTHON) | Magnitude: 139.44 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 258, structural_boundaries: 61, api: 39, test: 36
- `tests/dcerpc/test_dcomrt.py` (PYTHON) | Magnitude: 89.12 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 38, test: 32, api: 20
- `tests/dcerpc/test_fasp.py` (PYTHON) | Magnitude: 19.38 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, test: 14, structural_boundaries: 13, api: 7
- `impacket/krb5/crypto.py` (PYTHON) | Magnitude: 873.76 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 458, structural_boundaries: 159, sec_reflection_metaprogramming: 134, branch: 95
- `tests/dcerpc/test_drsuapi.py` (PYTHON) | Magnitude: 91.44 | Delta: **0.139 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 279, structural_boundaries: 32, test: 26, api: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `impacket/dcerpc/v5/enum.py` (PYTHON) | Magnitude: 2042.2 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 389, encapsulation: 274, structural_boundaries: 141, branch: 139

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `setup.py` (PYTHON) | Magnitude: 131.19 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 9, io: 7, branch: 6
- `examples/owneredit.py` (PYTHON) | Magnitude: 412.32 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 216, branch: 44, structural_boundaries: 42, state_mutation: 23
- `examples/mssqlclient.py` (PYTHON) | Magnitude: 16.56 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 69, branch: 27, structural_boundaries: 18, import: 8
- `tests/dot11/test_FrameManagementDeauthentication.py` (PYTHON) | Magnitude: 91.72 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 89, sec_reflection_metaprogramming: 44, structural_boundaries: 25, test: 14
- `tests/dot11/test_FrameManagementDisassociation.py` (PYTHON) | Magnitude: 91.72 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 25, test: 14, state_mutation: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `examples/mssqlinstance.py` (PYTHON) | Magnitude: 15.58 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 11, branch: 8, import: 7
- `examples/secretsdump.py` (PYTHON) | Magnitude: 1428.3 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 396, encapsulation: 242, branch: 174, state_mutation: 133
- `examples/findDelegation.py` (PYTHON) | Magnitude: 398.72 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 191, state_mutation: 73, branch: 65, encapsulation: 42
- `impacket/examples/ntlmrelayx/servers/socksplugins/imap.py` (PYTHON) | Magnitude: 339.52 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 150, branch: 44, structural_boundaries: 37, state_mutation: 37
- `examples/samedit.py` (PYTHON) | Magnitude: 16.42 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, branch: 30, structural_boundaries: 14, io: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tests/misc/test_ccache.py` (PYTHON) | Magnitude: 114.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, branch: 20, test: 17, structural_boundaries: 16
- `examples/registry-read.py` (PYTHON) | Magnitude: 257.24 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 33, branch: 25, debug_prints: 13
- `impacket/dcerpc/v5/icpr.py` (PYTHON) | Magnitude: 29.1 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 29, branch: 14, import: 9
- `impacket/krb5/ccache.py` (PYTHON) | Magnitude: 1095.92 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 572, structural_boundaries: 125, state_mutation: 108, branch: 74
- `tests/ImpactPacket/test_IP6.py` (PYTHON) | Magnitude: 18.16 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 8, test: 6, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tests/dot11/test_helper.py` (PYTHON) | Magnitude: 8.46 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 6, test: 5, api: 3
- `impacket/examples/ntlmrelayx/utils/ssl.py` (PYTHON) | Magnitude: 27.52 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 8, api: 3, branch: 2
- `tests/ImpactPacket/__init__.py` (PYTHON) | Magnitude: 10.52 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 1
- `tests/SMB_RPC/__init__.py` (PYTHON) | Magnitude: 10.52 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 1
- `tests/dot11/__init__.py` (PYTHON) | Magnitude: 10.52 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `examples/secretsdump.py` -> Churn: **82.24%** | Cog Load: 79.5211% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `impacket/examples/ntlmrelayx/servers/socksserver.py` -> **Gabriel Gonzalez** (100.0% isolated ownership) | Magnitude: 4005.11
- `impacket/dcerpc/v5/rpcrt.py` -> **Roman Karwacik** (100.0% isolated ownership) | Magnitude: 3481.68
- `examples/ntfs-read.py` -> **alexisbalbachan** (100.0% isolated ownership) | Magnitude: 3352.64
- `impacket/examples/os_ident.py` -> **adrian manrique** (100.0% isolated ownership) | Magnitude: 2656.12
- `impacket/structure.py` -> **alexisbalbachan** (100.0% isolated ownership) | Magnitude: 2289.48

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `impacket/smbconnection.py` -> **Severity: 0.305** (Bridge: 0.0031 * Flux: 97.8233%)
- `impacket/dcerpc/v5/rpcrt.py` -> **Severity: 0.255** (Bridge: 0.0026 * Flux: 97.2739%)
- `impacket/krb5/kerberosv5.py` -> **Severity: 0.238** (Bridge: 0.0033 * Flux: 71.5042%)
- `impacket/smbserver.py` -> **Severity: 0.096** (Bridge: 0.0011 * Flux: 85.2715%)
- `impacket/dcerpc/v5/ndr.py` -> **Severity: 0.089** (Bridge: 0.0012 * Flux: 74.8283%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `impacket/smbconnection.py` -> **Severity: 10.087** (Embedded: 0.1591 * Error Risk: 63.3952%)
- `impacket/krb5/kerberosv5.py` -> **Severity: 7.784** (Embedded: 0.1557 * Error Risk: 50.0%)
- `impacket/krb5/types.py` -> **Severity: 6.608** (Embedded: 0.161 * Error Risk: 41.055%)
- `impacket/examples/ntlmrelayx/servers/socksserver.py` -> **Severity: 2.882** (Embedded: 0.0551 * Error Risk: 52.2841%)
- `impacket/dcerpc/v5/rpcrt.py` -> **Severity: 2.862** (Embedded: 0.2415 * Error Risk: 11.8509%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `impacket/structure.py` -> **Severity: 8335.4** (Blast Radius: 83.354 * Doc Risk: 100.0%)
- `impacket/uuid.py` -> **Severity: 4265.2** (Blast Radius: 42.652 * Doc Risk: 100.0%)
- `impacket/dcerpc/v5/ndr.py` -> **Severity: 4011.852** (Blast Radius: 40.401 * Doc Risk: 99.3008%)
- `impacket/ImpactPacket.py` -> **Severity: 3900.8** (Blast Radius: 39.008 * Doc Risk: 100.0%)
- `impacket/dcerpc/v5/dtypes.py` -> **Severity: 3315.0** (Blast Radius: 33.156 * Doc Risk: 99.9819%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
