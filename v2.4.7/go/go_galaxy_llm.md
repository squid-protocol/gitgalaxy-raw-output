# ARCHITECTURAL_BRIEF: go
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/go` |
| **Timestamp** | `2026-08-07T04:59:49.964932+00:00` |
| **Scan Duration** | `25.46s` |
| **Git Branch** | `master` |
| **Git Commit** | `d247ed00e498e9717fb7c80d126bee5a8afdb4e8` |
| **Git Remote** | `https://github.com/golang/go` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 6628 malicious artifacts.

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
| Total Artifacts | 15154 |
| Analyzed Artifacts (Scanned) | 9299 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5855 |
| Total LOC | 953120 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 61.4% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.147 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 166 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 6455 | 827939 | 69.4% |
| PLAINTEXT | 1979 | 442 | 21.3% |
| ASSEMBLY | 555 | 104522 | 6.0% |
| C | 128 | 6178 | 1.4% |
| MARKDOWN | 59 | 0 | 0.6% |
| YAML | 32 | 3958 | 0.3% |
| JSON | 29 | 3215 | 0.3% |
| SHELL | 20 | 1128 | 0.2% |
| PERL | 9 | 1058 | 0.1% |
| HTML | 6 | 1787 | 0.1% |
| BATCH | 5 | 177 | 0.1% |
| M4 | 4 | 25 | 0.0% |
| JAVASCRIPT | 3 | 74 | 0.0% |
| BINARY_THREAT | 3 | 3 | 0.0% |
| FORTRAN | 2 | 8 | 0.0% |
| OBJECTIVE-C | 2 | 15 | 0.0% |
| DOCKERFILE | 2 | 61 | 0.0% |
| MAKEFILE | 2 | 3 | 0.0% |
| CPP | 1 | 7 | 0.0% |
| CSV | 1 | 2119 | 0.0% |
| CSS | 1 | 1 | 0.0% |
| PYTHON | 1 | 400 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.494`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 4936 | 53.1% |
| file_cluster_13 | 1064 | 11.4% |
| file_cluster_4 | 444 | 4.8% |
| Unknown | 441 | 4.7% |
| file_cluster_16 | 168 | 1.8% |
| file_cluster_11 | 140 | 1.5% |
| file_cluster_15 | 120 | 1.3% |
| file_cluster_12 | 98 | 1.1% |
| file_cluster_7 | 95 | 1.0% |
| file_cluster_6 | 72 | 0.8% |
| file_cluster_9 | 67 | 0.7% |
| file_cluster_0 | 48 | 0.5% |
| file_cluster_17 | 6 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1598 | 17.2% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5855*

**Composition by Extension & Reason:**
- `.go`: 4516x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Machine-Generated Source Code Signature: 1911 LOC), 5x Excluded (Saturation: Line 3 exceeds 500 chars)
- `no_extension`: 163x Unsupported Format (.undeterminable), 81x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 39x Excluded (Binary Format Detected)
- `.out`: 98x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.s`: 74x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 10701 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1066 LOC)
- `.png`: 56x Excluded (Explicitly Denied Extension: '.png')
- `.input`: 51x Unsupported Format (.input)
- `.test`: 41x Unsupported Format (.test), 1x Excluded (Binary Format Detected)
- `.tar`: 38x Excluded (Explicitly Denied Extension: '.tar')
- `.sng`: 34x Unsupported Format (.sng), 1x Excluded (Saturation: Line 9 exceeds 500 chars)
- `.zip`: 34x Excluded (Explicitly Denied Extension: '.zip')
- `.jpeg`: 30x Excluded (Explicitly Denied Extension: '.jpeg')
- `.md`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rules`: 24x Unsupported Format (.rules), 1x Excluded (Machine-Generated Source Code Signature: 3114 LOC)
- `.base64`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Unsupported Format (.base64), 5x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.syso`: 21x Excluded (Binary Format Detected), 1x Unsupported Format (.syso)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 27.1 | 29.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 66.7 | 80.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 42.9 | 27.6 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 15.8 | 2.3 | 0.0 |
| API Exposure | 0.0 | 19.9 | 2.5 | 0.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 8.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 70.7 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 86.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.4 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 22.7 | 11.9 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/cmd/asm/internal/asm/testdata/riscv64validation.s` (Hits: 537)
- `src/syscall/mkerrors.sh` (Hits: 218)
- `src/runtime/sys_linux_amd64.s` (Hits: 72)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **bytes.go** (`src/bytes/bytes.go`) — 774 inbound connections
2. **strconv.go** (`src/archive/tar/strconv.go`) — 447 inbound connections
3. **testenv.go** (`src/internal/testenv/testenv.go`) — 354 inbound connections
4. **reflect.go** (`src/cmd/compile/internal/reflectdata/reflect.go`) — 338 inbound connections
5. **atomic.go** (`src/cmd/vet/testdata/atomic/atomic.go`) — 248 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mldsa_test.go** (`src/crypto/internal/fips140test/mldsa_test.go`) — 466 outbound dependencies
2. **xml.go** (`src/encoding/xml/xml.go`) — 275 outbound dependencies
3. **acvp_test.go** (`src/crypto/internal/fips140test/acvp_test.go`) — 213 outbound dependencies
4. **arshal_test.go** (`src/encoding/json/v2/arshal_test.go`) — 167 outbound dependencies
5. **gcm_test.go** (`src/crypto/cipher/gcm_test.go`) — 163 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `main` (@ `src/regexp/testdata/testregex.c`) -> Impact: **909.2** | LOC: 1071
- `pkgIdx` (@ `src/cmd/compile/internal/noder/writer.go`) -> Impact: **775.1** | LOC: 1294
- `packEfaceData` (@ `src/reflect/value.go`) -> Impact: **754.8** | LOC: 1776
- `callReflect` (@ `src/reflect/value.go`) -> Impact: **734.7** | LOC: 1545
- `readRequest` (@ `src/net/http/server.go`) -> Impact: **727.8** | LOC: 1769
- `close` (@ `src/net/http/server.go`) -> Impact: **724.7** | LOC: 1927
  * *Intent:* // rwc is the underlying network connection. // This is never wrapped by other types and is the value given out // to [Hijacker] callers. It is usuall...
- `callMethod` (@ `src/reflect/value.go`) -> Impact: **702.1** | LOC: 1475
- `interfaceType` (@ `src/cmd/compile/internal/noder/writer.go`) -> Impact: **683.4** | LOC: 1126
- `linkname` (@ `src/cmd/compile/internal/noder/reader.go`) -> Impact: **663.6** | LOC: 1416
- `protocols` (@ `src/net/http/transport.go`) -> Impact: **631.9** | LOC: 1368
  * *Intent:* // GetProxyConnectHeader optionally specifies a func to return // headers to send to proxyURL during a CONNECT request to the

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/crypto/x509/testdata/nist-pkits/certs` | 405 | 2025000.0 | 0.0% | 0.0% |
| `src/crypto/x509/testdata` | 28 | 140000.0 | 0.0% | 0.0% |
| `src/runtime` | 770 | 96413.66 | 21.82% | 51.24% |
| `src/net` | 229 | 35978.96 | 31.89% | 67.25% |
| `src/net/http` | 70 | 32297.28 | 37.9% | 59.41% |
| `src/cmd/compile/internal/ssa` | 116 | 29554.62 | 43.76% | 50.99% |
| `src/syscall` | 274 | 22615.65 | 22.87% | 41.8% |
| `src/cmd/compile/internal/types2` | 97 | 19804.9 | 38.91% | 29.03% |
| `src/os` | 163 | 19435.93 | 28.81% | 64.72% |
| `src/go/types` | 109 | 19185.68 | 35.52% | 29.6% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `misc/cgo/gmp/gmp.go` -> **100.0%** Exposure
- `src/cmd/api/testdata/src/pkg/p4/p4.go` -> **100.0%** Exposure
- `src/cmd/cgo/doc.go` -> **100.0%** Exposure
- `src/cmd/cgo/internal/testcshared/testdata/go2c2go/go/shlib.go` -> **100.0%** Exposure
- `src/cmd/cgo/internal/testcshared/testdata/issue36233/issue36233.go` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `misc/cgo/gmp/fib.go` -> **100.0%** Exposure
- `misc/cgo/gmp/pi.go` -> **100.0%** Exposure
- `misc/go_android_exec/main.go` -> **100.0%** Exposure
- `misc/ios/detect.go` -> **100.0%** Exposure
- `misc/ios/go_ios_exec.go` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/math/all_test.go` -> **149** Orphaned Functions | **0** Duplicates
- `src/go/ast/ast.go` -> **0** Orphaned Functions | **129** Duplicates
- `src/runtime/race/testdata/mop_test.go` -> **121** Orphaned Functions | **4** Duplicates
- `src/cmd/cgo/internal/test/cgo_test.go` -> **104** Orphaned Functions | **0** Duplicates
- `src/cmd/compile/internal/ssa/rewrite.go` -> **100** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/archive/tar/stat_unix.go`** -> AI Confidence: **99.48%**
2. **`src/archive/zip/writer_test.go`** -> AI Confidence: **99.48%**
3. **`src/archive/zip/zip_test.go`** -> AI Confidence: **99.48%**
4. **`src/bufio/bufio_test.go`** -> AI Confidence: **99.48%**
5. **`src/bufio/scan_test.go`** -> AI Confidence: **99.48%**
6. **`src/bytes/buffer_test.go`** -> AI Confidence: **99.48%**
7. **`src/bytes/bytes_test.go`** -> AI Confidence: **99.48%**
8. **`src/cmd/addr2line/main.go`** -> AI Confidence: **99.48%**
9. **`src/cmd/asm/internal/asm/endtoend_test.go`** -> AI Confidence: **99.48%**
10. **`src/cmd/asm/internal/lex/input.go`** -> AI Confidence: **99.48%**
11. **`src/cmd/asm/main.go`** -> AI Confidence: **99.48%**
12. **`src/cmd/cgo/ast.go`** -> AI Confidence: **99.48%**
13. **`src/cmd/cgo/internal/test/callback_windows.go`** -> AI Confidence: **99.48%**
14. **`src/cmd/cgo/internal/test/issue18146.go`** -> AI Confidence: **99.48%**
15. **`src/cmd/cgo/internal/testfortran/fortran_test.go`** -> AI Confidence: **99.48%**
16. **`src/cmd/cgo/main.go`** -> AI Confidence: **99.48%**
17. **`src/cmd/compile/internal/amd64/versions_test.go`** -> AI Confidence: **99.48%**
18. **`src/cmd/compile/internal/arm64/ssa.go`** -> AI Confidence: **99.48%**
19. **`src/cmd/compile/internal/base/flag.go`** -> AI Confidence: **99.48%**
20. **`src/cmd/compile/internal/escape/escape.go`** -> AI Confidence: **99.48%**
21. **`src/cmd/compile/internal/gc/export.go`** -> AI Confidence: **99.48%**
22. **`src/cmd/compile/internal/gc/main.go`** -> AI Confidence: **99.48%**
23. **`src/cmd/compile/internal/gc/util.go`** -> AI Confidence: **99.48%**
24. **`src/cmd/compile/internal/ir/fmt.go`** -> AI Confidence: **99.48%**
25. **`src/cmd/compile/internal/loong64/ssa.go`** -> AI Confidence: **99.48%**
26. **`src/cmd/compile/internal/mips/ssa.go`** -> AI Confidence: **99.48%**
27. **`src/cmd/compile/internal/pkginit/init.go`** -> AI Confidence: **99.48%**
28. **`src/cmd/compile/internal/ppc64/ssa.go`** -> AI Confidence: **99.48%**
29. **`src/cmd/compile/internal/riscv64/ssa.go`** -> AI Confidence: **99.48%**
30. **`src/cmd/compile/internal/s390x/ssa.go`** -> AI Confidence: **99.48%**
31. **`src/cmd/compile/internal/ssa/compile.go`** -> AI Confidence: **99.48%**
32. **`src/cmd/compile/internal/ssa/cpufeatures.go`** -> AI Confidence: **99.48%**
33. **`src/cmd/compile/internal/ssa/cse_test.go`** -> AI Confidence: **99.48%**
34. **`src/cmd/compile/internal/ssa/debug.go`** -> AI Confidence: **99.48%**
35. **`src/cmd/compile/internal/ssa/prove.go`** -> AI Confidence: **99.48%**
36. **`src/cmd/compile/internal/ssa/regalloc.go`** -> AI Confidence: **99.48%**
37. **`src/cmd/compile/internal/ssa/writebarrier.go`** -> AI Confidence: **99.48%**
38. **`src/cmd/compile/internal/syntax/scanner.go`** -> AI Confidence: **99.48%**
39. **`src/cmd/compile/internal/syntax/scanner_test.go`** -> AI Confidence: **99.48%**
40. **`src/cmd/compile/internal/test/bench_test.go`** -> AI Confidence: **99.48%**
41. **`src/cmd/compile/internal/test/mulconst_test.go`** -> AI Confidence: **99.48%**
42. **`src/cmd/compile/internal/test/testdata/gen/arithConstGen.go`** -> AI Confidence: **99.48%**
43. **`src/cmd/compile/internal/test/testdata/gen/constFoldGen.go`** -> AI Confidence: **99.48%**
44. **`src/cmd/compile/internal/types2/call.go`** -> AI Confidence: **99.48%**
45. **`src/cmd/compile/internal/types2/resolver.go`** -> AI Confidence: **99.48%**
46. **`src/cmd/compile/internal/x86/ssa.go`** -> AI Confidence: **99.48%**
47. **`src/cmd/compile/script_test.go`** -> AI Confidence: **99.48%**
48. **`src/cmd/covdata/covdata.go`** -> AI Confidence: **99.48%**
49. **`src/cmd/go/internal/cache/cache_test.go`** -> AI Confidence: **99.48%**
50. **`src/cmd/go/internal/envcmd/env_test.go`** -> AI Confidence: **99.48%**
51. **`src/cmd/go/internal/fips140/fips_test.go`** -> AI Confidence: **99.48%**
52. **`src/cmd/go/internal/imports/scan_test.go`** -> AI Confidence: **99.48%**
53. **`src/cmd/go/internal/modfetch/codehost/shell.go`** -> AI Confidence: **99.48%**
54. **`src/cmd/go/internal/work/exec_test.go`** -> AI Confidence: **99.48%**
55. **`src/cmd/internal/bootstrap_test/reboot_test.go`** -> AI Confidence: **99.48%**
56. **`src/cmd/internal/buildid/buildid_test.go`** -> AI Confidence: **99.48%**
57. **`src/cmd/internal/objabi/flag.go`** -> AI Confidence: **99.48%**
58. **`src/cmd/internal/test2json/test2json_test.go`** -> AI Confidence: **99.48%**
59. **`src/cmd/link/internal/arm64/asm.go`** -> AI Confidence: **99.48%**
60. **`src/cmd/link/internal/ld/elf.go`** -> AI Confidence: **99.48%**
61. **`src/cmd/link/internal/ld/elf_test.go`** -> AI Confidence: **99.48%**
62. **`src/cmd/link/internal/ld/lib.go`** -> AI Confidence: **99.48%**
63. **`src/cmd/link/internal/ld/main.go`** -> AI Confidence: **99.48%**
64. **`src/cmd/link/internal/loader/loader_test.go`** -> AI Confidence: **99.48%**
65. **`src/cmd/link/internal/loong64/asm.go`** -> AI Confidence: **99.48%**
66. **`src/cmd/link/internal/ppc64/asm.go`** -> AI Confidence: **99.48%**
67. **`src/cmd/link/internal/wasm/asm.go`** -> AI Confidence: **99.48%**
68. **`src/cmd/link/main.go`** -> AI Confidence: **99.48%**
69. **`src/cmd/pack/pack.go`** -> AI Confidence: **99.48%**
70. **`src/cmd/pprof/pprof_test.go`** -> AI Confidence: **99.48%**
71. **`src/compress/flate/deflate_test.go`** -> AI Confidence: **99.48%**
72. **`src/compress/flate/flate_test.go`** -> AI Confidence: **99.48%**
73. **`src/compress/gzip/fuzz_test.go`** -> AI Confidence: **99.48%**
74. **`src/compress/lzw/reader_test.go`** -> AI Confidence: **99.48%**
75. **`src/crypto/cipher/cfb_test.go`** -> AI Confidence: **99.48%**
76. **`src/crypto/cipher/ctr_aes_test.go`** -> AI Confidence: **99.48%**
77. **`src/crypto/cipher/ctr_test.go`** -> AI Confidence: **99.48%**
78. **`src/crypto/cipher/example_test.go`** -> AI Confidence: **99.48%**
79. **`src/crypto/cipher/fuzz_test.go`** -> AI Confidence: **99.48%**
80. **`src/crypto/ecdsa/ecdsa_test.go`** -> AI Confidence: **99.48%**
81. **`src/crypto/ed25519/ed25519_test.go`** -> AI Confidence: **99.48%**
82. **`src/crypto/elliptic/p224_test.go`** -> AI Confidence: **99.48%**
83. **`src/crypto/elliptic/p256_test.go`** -> AI Confidence: **99.48%**
84. **`src/crypto/hkdf/hkdf_test.go`** -> AI Confidence: **99.48%**
85. **`src/crypto/hpke/hpke_test.go`** -> AI Confidence: **99.48%**
86. **`src/crypto/internal/fips140/bigmod/nat_test.go`** -> AI Confidence: **99.48%**
87. **`src/crypto/internal/fips140/edwards25519/edwards25519_test.go`** -> AI Confidence: **99.48%**
88. **`src/crypto/internal/fips140/rsa/keygen_test.go`** -> AI Confidence: **99.48%**
89. **`src/crypto/internal/fips140test/cast_test.go`** -> AI Confidence: **99.48%**
90. **`src/crypto/internal/fips140test/check_test.go`** -> AI Confidence: **99.48%**
91. **`src/crypto/internal/fips140test/entropy_test.go`** -> AI Confidence: **99.48%**
92. **`src/crypto/internal/fips140test/fips_test.go`** -> AI Confidence: **99.48%**
93. **`src/crypto/internal/fips140test/mldsa_test.go`** -> AI Confidence: **99.48%**
94. **`src/crypto/internal/fips140test/nistec_test.go`** -> AI Confidence: **99.48%**
95. **`src/crypto/internal/fips140test/xaes_test.go`** -> AI Confidence: **99.48%**
96. **`src/crypto/mlkem/mlkem_test.go`** -> AI Confidence: **99.48%**
97. **`src/crypto/pbkdf2/pbkdf2_test.go`** -> AI Confidence: **99.48%**
98. **`src/crypto/rsa/pss_test.go`** -> AI Confidence: **99.48%**
99. **`src/crypto/rsa/rsa_test.go`** -> AI Confidence: **99.48%**
100. **`src/crypto/sha3/sha3_test.go`** -> AI Confidence: **99.48%**
101. **`src/crypto/tls/generate_cert.go`** -> AI Confidence: **99.48%**
102. **`src/crypto/tls/handshake_messages_test.go`** -> AI Confidence: **99.48%**
103. **`src/crypto/tls/quic_test.go`** -> AI Confidence: **99.48%**
104. **`src/crypto/x509/hybrid_pool_test.go`** -> AI Confidence: **99.48%**
105. **`src/crypto/x509/parser_test.go`** -> AI Confidence: **99.48%**
106. **`src/crypto/x509/platform_test.go`** -> AI Confidence: **99.48%**
107. **`src/crypto/x509/root_unix_test.go`** -> AI Confidence: **99.48%**
108. **`src/crypto/x509/verify.go`** -> AI Confidence: **99.48%**
109. **`src/crypto/x509/verify_test.go`** -> AI Confidence: **99.48%**
110. **`src/encoding/base32/base32_test.go`** -> AI Confidence: **99.48%**
111. **`src/encoding/csv/example_test.go`** -> AI Confidence: **99.48%**
112. **`src/encoding/csv/reader.go`** -> AI Confidence: **99.48%**
113. **`src/encoding/csv/reader_test.go`** -> AI Confidence: **99.48%**
114. **`src/encoding/json/bench_test.go`** -> AI Confidence: **99.48%**
115. **`src/encoding/json/decode.go`** -> AI Confidence: **99.48%**
116. **`src/encoding/json/internal/jsonwire/decode_test.go`** -> AI Confidence: **99.48%**
117. **`src/encoding/json/jsontext/decode_test.go`** -> AI Confidence: **99.48%**
118. **`src/encoding/json/jsontext/encode_test.go`** -> AI Confidence: **99.48%**
119. **`src/encoding/json/jsontext/example_test.go`** -> AI Confidence: **99.48%**
120. **`src/encoding/json/jsontext/fuzz_test.go`** -> AI Confidence: **99.48%**
121. **`src/encoding/json/number_test.go`** -> AI Confidence: **99.48%**
122. **`src/encoding/json/v2/arshal_time_test.go`** -> AI Confidence: **99.48%**
123. **`src/encoding/json/v2_bench_test.go`** -> AI Confidence: **99.48%**
124. **`src/expvar/expvar_test.go`** -> AI Confidence: **99.48%**
125. **`src/fmt/print.go`** -> AI Confidence: **99.48%**
126. **`src/fmt/scan_test.go`** -> AI Confidence: **99.48%**
127. **`src/go/doc/comment/testdata_test.go`** -> AI Confidence: **99.48%**
128. **`src/go/printer/nodes.go`** -> AI Confidence: **99.48%**
129. **`src/go/printer/printer.go`** -> AI Confidence: **99.48%**
130. **`src/hash/maphash/smhasher_test.go`** -> AI Confidence: **99.48%**
131. **`src/html/template/clone_test.go`** -> AI Confidence: **99.48%**
132. **`src/html/template/multi_test.go`** -> AI Confidence: **99.48%**
133. **`src/image/gif/reader_test.go`** -> AI Confidence: **99.48%**
134. **`src/image/gif/writer_test.go`** -> AI Confidence: **99.48%**
135. **`src/image/jpeg/reader_test.go`** -> AI Confidence: **99.48%**
136. **`src/image/jpeg/writer_test.go`** -> AI Confidence: **99.48%**
137. **`src/image/png/writer.go`** -> AI Confidence: **99.48%**
138. **`src/image/png/writer_test.go`** -> AI Confidence: **99.48%**
139. **`src/index/suffixarray/suffixarray_test.go`** -> AI Confidence: **99.48%**
140. **`src/internal/buildcfg/cfg_test.go`** -> AI Confidence: **99.48%**
141. **`src/internal/cpu/cpu_test.go`** -> AI Confidence: **99.48%**
142. **`src/internal/runtime/gc/scan/scan_test.go`** -> AI Confidence: **99.48%**
143. **`src/internal/runtime/maps/map_test.go`** -> AI Confidence: **99.48%**
144. **`src/internal/strconv/atof_test.go`** -> AI Confidence: **99.48%**
145. **`src/internal/trace/reader_test.go`** -> AI Confidence: **99.48%**
146. **`src/internal/trace/trace_test.go`** -> AI Confidence: **99.48%**
147. **`src/internal/zstd/zstd_test.go`** -> AI Confidence: **99.48%**
148. **`src/io/ioutil/tempfile_test.go`** -> AI Confidence: **99.48%**
149. **`src/math/big/calibrate_test.go`** -> AI Confidence: **99.48%**
150. **`src/math/big/float_test.go`** -> AI Confidence: **99.48%**
151. **`src/math/big/floatconv_test.go`** -> AI Confidence: **99.48%**
152. **`src/math/big/floatmarsh_test.go`** -> AI Confidence: **99.48%**
153. **`src/math/big/int_test.go`** -> AI Confidence: **99.48%**
154. **`src/math/big/intmarsh_test.go`** -> AI Confidence: **99.48%**
155. **`src/math/big/nat_test.go`** -> AI Confidence: **99.48%**
156. **`src/math/big/natconv_test.go`** -> AI Confidence: **99.48%**
157. **`src/math/big/prime_test.go`** -> AI Confidence: **99.48%**
158. **`src/math/big/ratconv_test.go`** -> AI Confidence: **99.48%**
159. **`src/math/big/ratmarsh_test.go`** -> AI Confidence: **99.48%**
160. **`src/math/rand/rand_test.go`** -> AI Confidence: **99.48%**
161. **`src/math/rand/v2/chacha8_test.go`** -> AI Confidence: **99.48%**
162. **`src/math/rand/v2/regress_test.go`** -> AI Confidence: **99.48%**
163. **`src/mime/multipart/formdata_test.go`** -> AI Confidence: **99.48%**
164. **`src/mime/multipart/writer_test.go`** -> AI Confidence: **99.48%**
165. **`src/net/dnsconfig_unix.go`** -> AI Confidence: **99.48%**
166. **`src/net/http/fs_test.go`** -> AI Confidence: **99.48%**
167. **`src/net/http/internal/http2/connframes_test.go`** -> AI Confidence: **99.48%**
168. **`src/net/http/internal/http2/frame_test.go`** -> AI Confidence: **99.48%**
169. **`src/net/http/pprof/pprof_test.go`** -> AI Confidence: **99.48%**
170. **`src/net/http/request_test.go`** -> AI Confidence: **99.48%**
171. **`src/net/interface_unix_test.go`** -> AI Confidence: **99.48%**
172. **`src/net/ip_test.go`** -> AI Confidence: **99.48%**
173. **`src/net/listen_test.go`** -> AI Confidence: **99.48%**
174. **`src/net/lookup_windows_test.go`** -> AI Confidence: **99.48%**
175. **`src/net/mail/message_test.go`** -> AI Confidence: **99.48%**
176. **`src/net/netip/fuzz_test.go`** -> AI Confidence: **99.48%**
177. **`src/net/netip/netip_test.go`** -> AI Confidence: **99.48%**
178. **`src/net/textproto/reader_test.go`** -> AI Confidence: **99.48%**
179. **`src/net/udpsock_test.go`** -> AI Confidence: **99.48%**
180. **`src/os/exec/dot_test.go`** -> AI Confidence: **99.48%**
181. **`src/os/exec/exec_windows_test.go`** -> AI Confidence: **99.48%**
182. **`src/os/exec/lp_linux_test.go`** -> AI Confidence: **99.48%**
183. **`src/os/exec/lp_windows_test.go`** -> AI Confidence: **99.48%**
184. **`src/os/exec/read3.go`** -> AI Confidence: **99.48%**
185. **`src/os/getwd_unix_test.go`** -> AI Confidence: **99.48%**
186. **`src/os/os_test.go`** -> AI Confidence: **99.48%**
187. **`src/os/os_unix_test.go`** -> AI Confidence: **99.48%**
188. **`src/os/path_test.go`** -> AI Confidence: **99.48%**
189. **`src/os/pidfd_linux_test.go`** -> AI Confidence: **99.48%**
190. **`src/os/read_test.go`** -> AI Confidence: **99.48%**
191. **`src/os/readfrom_unix_test.go`** -> AI Confidence: **99.48%**
192. **`src/os/removeall_test.go`** -> AI Confidence: **99.48%**
193. **`src/os/signal/signal_cgo_test.go`** -> AI Confidence: **99.48%**
194. **`src/os/tempfile_test.go`** -> AI Confidence: **99.48%**
195. **`src/os/user/user_windows_test.go`** -> AI Confidence: **99.48%**
196. **`src/path/filepath/path_test.go`** -> AI Confidence: **99.48%**
197. **`src/path/filepath/path_windows_test.go`** -> AI Confidence: **99.48%**
198. **`src/reflect/iter_test.go`** -> AI Confidence: **99.48%**
199. **`src/regexp/all_test.go`** -> AI Confidence: **99.48%**
200. **`src/runtime/cgroup_linux_test.go`** -> AI Confidence: **99.48%**
201. **`src/runtime/coro_test.go`** -> AI Confidence: **99.48%**
202. **`src/runtime/hash_test.go`** -> AI Confidence: **99.48%**
203. **`src/runtime/hexdump_test.go`** -> AI Confidence: **99.48%**
204. **`src/runtime/malloc.go`** -> AI Confidence: **99.48%**
205. **`src/runtime/memmove_test.go`** -> AI Confidence: **99.48%**
206. **`src/runtime/mgcmark.go`** -> AI Confidence: **99.48%**
207. **`src/runtime/pprof/label_test.go`** -> AI Confidence: **99.48%**
208. **`src/runtime/pprof/proto_test.go`** -> AI Confidence: **99.48%**
209. **`src/runtime/proc.go`** -> AI Confidence: **99.48%**
210. **`src/runtime/profbuf_test.go`** -> AI Confidence: **99.48%**
211. **`src/runtime/runtime1.go`** -> AI Confidence: **99.48%**
212. **`src/runtime/secret/crash_test.go`** -> AI Confidence: **99.48%**
213. **`src/runtime/slice_test.go`** -> AI Confidence: **99.48%**
214. **`src/runtime/testdata/testprogcgo/callback_pprof.go`** -> AI Confidence: **99.48%**
215. **`src/runtime/trace/flightrecorder_test.go`** -> AI Confidence: **99.48%**
216. **`src/runtime/trace2map_test.go`** -> AI Confidence: **99.48%**
217. **`src/runtime/trace_cgo_test.go`** -> AI Confidence: **99.48%**
218. **`src/runtime/traceback.go`** -> AI Confidence: **99.48%**
219. **`src/simd/archsimd/_gen/simdgen/gen_simdTypes.go`** -> AI Confidence: **99.48%**
220. **`src/simd/archsimd/_gen/simdgen/gen_simdrules.go`** -> AI Confidence: **99.48%**
221. **`src/simd/archsimd/_gen/simdgen/main.go`** -> AI Confidence: **99.48%**
222. **`src/sort/sort_test.go`** -> AI Confidence: **99.48%**
223. **`src/strings/builder_test.go`** -> AI Confidence: **99.48%**
224. **`src/strings/strings_test.go`** -> AI Confidence: **99.48%**
225. **`src/sync/atomic/atomic_test.go`** -> AI Confidence: **99.48%**
226. **`src/syscall/dirent_test.go`** -> AI Confidence: **99.48%**
227. **`src/syscall/exec_linux_test.go`** -> AI Confidence: **99.48%**
228. **`src/syscall/exec_pdeathsig_test.go`** -> AI Confidence: **99.48%**
229. **`src/syscall/getdirentries_test.go`** -> AI Confidence: **99.48%**
230. **`src/syscall/syscall_unix_test.go`** -> AI Confidence: **99.48%**
231. **`src/syscall/wtf8_windows_test.go`** -> AI Confidence: **99.48%**
232. **`src/testing/benchmark_test.go`** -> AI Confidence: **99.48%**
233. **`src/testing/cryptotest/rand_test.go`** -> AI Confidence: **99.48%**
234. **`src/testing/fstest/mapfs_test.go`** -> AI Confidence: **99.48%**
235. **`src/text/template/multi_test.go`** -> AI Confidence: **99.48%**
236. **`src/time/format_test.go`** -> AI Confidence: **99.48%**
237. **`src/unicode/letter_test.go`** -> AI Confidence: **99.48%**
238. **`src/regexp/testdata/testregex.c`** -> AI Confidence: **99.48%**
239. **`src/cmd/link/internal/ld/data.go`** -> AI Confidence: **99.44%**
240. **`src/go/types/call.go`** -> AI Confidence: **99.44%**
241. **`src/runtime/stack.go`** -> AI Confidence: **99.43%**
242. **`src/archive/zip/reader_test.go`** -> AI Confidence: **99.39%**
243. **`src/cmd/api/api_test.go`** -> AI Confidence: **99.39%**
244. **`src/cmd/api/main_test.go`** -> AI Confidence: **99.39%**
245. **`src/cmd/asm/internal/asm/parse.go`** -> AI Confidence: **99.39%**
246. **`src/cmd/asm/internal/lex/lex_test.go`** -> AI Confidence: **99.39%**
247. **`src/cmd/buildid/buildid.go`** -> AI Confidence: **99.39%**
248. **`src/cmd/cgo/godefs.go`** -> AI Confidence: **99.39%**
249. **`src/cmd/cgo/internal/testcarchive/carchive_test.go`** -> AI Confidence: **99.39%**
250. **`src/cmd/cgo/internal/testcshared/cshared_test.go`** -> AI Confidence: **99.39%**
251. **`src/cmd/cgo/internal/testgodefs/testgodefs_test.go`** -> AI Confidence: **99.39%**
252. **`src/cmd/cgo/internal/testsanitizers/cshared_test.go`** -> AI Confidence: **99.39%**
253. **`src/cmd/cgo/internal/testso/so_test.go`** -> AI Confidence: **99.39%**
254. **`src/cmd/compile/internal/amd64/ssa.go`** -> AI Confidence: **99.39%**
255. **`src/cmd/compile/internal/arm/ssa.go`** -> AI Confidence: **99.39%**
256. **`src/cmd/compile/internal/dwarfgen/dwinl.go`** -> AI Confidence: **99.39%**
257. **`src/cmd/compile/internal/dwarfgen/scope_test.go`** -> AI Confidence: **99.39%**
258. **`src/cmd/compile/internal/inline/inlheur/funcprops_test.go`** -> AI Confidence: **99.39%**
259. **`src/cmd/compile/internal/inline/inlheur/scoring.go`** -> AI Confidence: **99.39%**
260. **`src/cmd/compile/internal/ir/html.go`** -> AI Confidence: **99.39%**
261. **`src/cmd/compile/internal/liveness/mergelocals.go`** -> AI Confidence: **99.39%**
262. **`src/cmd/compile/internal/liveness/plive.go`** -> AI Confidence: **99.39%**
263. **`src/cmd/compile/internal/loopvar/loopvar.go`** -> AI Confidence: **99.39%**
264. **`src/cmd/compile/internal/loopvar/loopvar_test.go`** -> AI Confidence: **99.39%**
265. **`src/cmd/compile/internal/mips64/ssa.go`** -> AI Confidence: **99.39%**
266. **`src/cmd/compile/internal/noder/linker.go`** -> AI Confidence: **99.39%**
267. **`src/cmd/compile/internal/pgoir/irgraph.go`** -> AI Confidence: **99.39%**
268. **`src/cmd/compile/internal/ssa/_gen/rulegen.go`** -> AI Confidence: **99.39%**
269. **`src/cmd/compile/internal/ssa/debug_lines_test.go`** -> AI Confidence: **99.39%**
270. **`src/cmd/compile/internal/ssa/html.go`** -> AI Confidence: **99.39%**
271. **`src/cmd/compile/internal/ssa/looprotate_test.go`** -> AI Confidence: **99.39%**
272. **`src/cmd/compile/internal/ssa/rewritetern.go`** -> AI Confidence: **99.39%**
273. **`src/cmd/compile/internal/ssa/stmtlines_test.go`** -> AI Confidence: **99.39%**
274. **`src/cmd/compile/internal/ssagen/abi.go`** -> AI Confidence: **99.39%**
275. **`src/cmd/compile/internal/test/inl_test.go`** -> AI Confidence: **99.39%**
276. **`src/cmd/compile/internal/walk/order.go`** -> AI Confidence: **99.39%**
277. **`src/cmd/compile/internal/walk/switch.go`** -> AI Confidence: **99.39%**
278. **`src/cmd/compile/internal/wasm/ssa.go`** -> AI Confidence: **99.39%**
279. **`src/cmd/compile/internal/x86/galign.go`** -> AI Confidence: **99.39%**
280. **`src/cmd/covdata/metamerge.go`** -> AI Confidence: **99.39%**
281. **`src/cmd/covdata/tool_test.go`** -> AI Confidence: **99.39%**
282. **`src/cmd/go/internal/auth/auth.go`** -> AI Confidence: **99.39%**
283. **`src/cmd/go/internal/auth/gitauth.go`** -> AI Confidence: **99.39%**
284. **`src/cmd/go/internal/doc/pkg.go`** -> AI Confidence: **99.39%**
285. **`src/cmd/go/internal/fips140/mkzip.go`** -> AI Confidence: **99.39%**
286. **`src/cmd/go/internal/modfetch/coderepo_test.go`** -> AI Confidence: **99.39%**
287. **`src/cmd/go/internal/modindex/build_read.go`** -> AI Confidence: **99.39%**
288. **`src/cmd/go/internal/modindex/index_test.go`** -> AI Confidence: **99.39%**
289. **`src/cmd/go/internal/modload/edit.go`** -> AI Confidence: **99.39%**
290. **`src/cmd/go/internal/modload/load.go`** -> AI Confidence: **99.39%**
291. **`src/cmd/go/internal/mvs/mvs_test.go`** -> AI Confidence: **99.39%**
292. **`src/cmd/go/internal/test/testflag.go`** -> AI Confidence: **99.39%**
293. **`src/cmd/go/internal/toolchain/select.go`** -> AI Confidence: **99.39%**
294. **`src/cmd/go/internal/work/build_test.go`** -> AI Confidence: **99.39%**
295. **`src/cmd/go/internal/work/buildid.go`** -> AI Confidence: **99.39%**
296. **`src/cmd/go/internal/work/security.go`** -> AI Confidence: **99.39%**
297. **`src/cmd/internal/archive/archive_test.go`** -> AI Confidence: **99.39%**
298. **`src/cmd/internal/bootstrap_test/experiment_toolid_test.go`** -> AI Confidence: **99.39%**
299. **`src/cmd/internal/goobj/objfile_test.go`** -> AI Confidence: **99.39%**
300. **`src/cmd/internal/pkgpath/pkgpath_test.go`** -> AI Confidence: **99.39%**
301. **`src/cmd/internal/script/scripttest/setup.go`** -> AI Confidence: **99.39%**
302. **`src/cmd/link/dwarf_test.go`** -> AI Confidence: **99.39%**
303. **`src/cmd/link/internal/amd64/asm.go`** -> AI Confidence: **99.39%**
304. **`src/cmd/link/internal/arm/asm.go`** -> AI Confidence: **99.39%**
305. **`src/cmd/link/internal/ld/deadcode.go`** -> AI Confidence: **99.39%**
306. **`src/cmd/link/internal/ld/go.go`** -> AI Confidence: **99.39%**
307. **`src/cmd/link/internal/ld/ld.go`** -> AI Confidence: **99.39%**
308. **`src/cmd/link/internal/ld/macho.go`** -> AI Confidence: **99.39%**
309. **`src/cmd/link/internal/ld/pcln.go`** -> AI Confidence: **99.39%**
310. **`src/cmd/link/internal/ld/symtab.go`** -> AI Confidence: **99.39%**
311. **`src/cmd/link/internal/loadelf/ldelf.go`** -> AI Confidence: **99.39%**
312. **`src/cmd/link/internal/loadpe/ldpe.go`** -> AI Confidence: **99.39%**
313. **`src/cmd/link/internal/riscv64/asm.go`** -> AI Confidence: **99.39%**
314. **`src/cmd/link/internal/s390x/asm.go`** -> AI Confidence: **99.39%**
315. **`src/cmd/link/link_test.go`** -> AI Confidence: **99.39%**
316. **`src/cmd/link/linkbig_test.go`** -> AI Confidence: **99.39%**
317. **`src/cmd/nm/nm_test.go`** -> AI Confidence: **99.39%**
318. **`src/cmd/objdump/main.go`** -> AI Confidence: **99.39%**
319. **`src/cmd/objdump/objdump_test.go`** -> AI Confidence: **99.39%**
320. **`src/cmd/relnote/relnote_test.go`** -> AI Confidence: **99.39%**
321. **`src/cmd/trace/jsontrace.go`** -> AI Confidence: **99.39%**
322. **`src/cmd/trace/jsontrace_test.go`** -> AI Confidence: **99.39%**
323. **`src/cmd/trace/pprof_test.go`** -> AI Confidence: **99.39%**
324. **`src/cmp/cmp_test.go`** -> AI Confidence: **99.39%**
325. **`src/compress/bzip2/bzip2_test.go`** -> AI Confidence: **99.39%**
326. **`src/compress/flate/example_test.go`** -> AI Confidence: **99.39%**
327. **`src/compress/gzip/example_test.go`** -> AI Confidence: **99.39%**
328. **`src/compress/lzw/writer_test.go`** -> AI Confidence: **99.39%**
329. **`src/compress/zlib/reader_test.go`** -> AI Confidence: **99.39%**
330. **`src/compress/zlib/writer_test.go`** -> AI Confidence: **99.39%**
331. **`src/crypto/cipher/cbc_aes_test.go`** -> AI Confidence: **99.39%**
332. **`src/crypto/cipher/gcm_test.go`** -> AI Confidence: **99.39%**
333. **`src/crypto/cipher/ofb_test.go`** -> AI Confidence: **99.39%**
334. **`src/crypto/ecdh/ecdh_test.go`** -> AI Confidence: **99.39%**
335. **`src/crypto/ed25519/ed25519vectors_test.go`** -> AI Confidence: **99.39%**
336. **`src/crypto/internal/cryptotest/allocations.go`** -> AI Confidence: **99.39%**
337. **`src/crypto/internal/fips140/edwards25519/field/fe_test.go`** -> AI Confidence: **99.39%**
338. **`src/crypto/internal/fips140/mldsa/mldsa_test.go`** -> AI Confidence: **99.39%**
339. **`src/crypto/internal/fips140deps/fipsdeps_test.go`** -> AI Confidence: **99.39%**
340. **`src/crypto/internal/sysrand/rand_test.go`** -> AI Confidence: **99.39%**
341. **`src/crypto/rand/rand_test.go`** -> AI Confidence: **99.39%**
342. **`src/crypto/rand/util_test.go`** -> AI Confidence: **99.39%**
343. **`src/crypto/rsa/pkcs1v15_test.go`** -> AI Confidence: **99.39%**
344. **`src/crypto/tls/bogo_shim_test.go`** -> AI Confidence: **99.39%**
345. **`src/crypto/tls/fips140_test.go`** -> AI Confidence: **99.39%**
346. **`src/crypto/tls/key_schedule_test.go`** -> AI Confidence: **99.39%**
347. **`src/crypto/tls/prf_test.go`** -> AI Confidence: **99.39%**
348. **`src/crypto/tls/tls_test.go`** -> AI Confidence: **99.39%**
349. **`src/crypto/x509/bettertls_test.go`** -> AI Confidence: **99.39%**
350. **`src/crypto/x509/pkits_test.go`** -> AI Confidence: **99.39%**
351. **`src/embed/internal/embedtest/embed_test.go`** -> AI Confidence: **99.39%**
352. **`src/encoding/base64/base64_test.go`** -> AI Confidence: **99.39%**
353. **`src/encoding/binary/binary_test.go`** -> AI Confidence: **99.39%**
354. **`src/encoding/json/internal/jsonwire/encode_test.go`** -> AI Confidence: **99.39%**
355. **`src/encoding/json/internal/jsonwire/wire.go`** -> AI Confidence: **99.39%**
356. **`src/encoding/json/jsontext/coder_test.go`** -> AI Confidence: **99.39%**
357. **`src/encoding/json/jsontext/state_test.go`** -> AI Confidence: **99.39%**
358. **`src/encoding/json/jsontext/value_test.go`** -> AI Confidence: **99.39%**
359. **`src/encoding/json/scanner_test.go`** -> AI Confidence: **99.39%**
360. **`src/encoding/json/v2_scanner_test.go`** -> AI Confidence: **99.39%**
361. **`src/encoding/json/v2_stream_test.go`** -> AI Confidence: **99.39%**
362. **`src/flag/flag_test.go`** -> AI Confidence: **99.39%**
363. **`src/go/constant/value_test.go`** -> AI Confidence: **99.39%**
364. **`src/go/doc/example.go`** -> AI Confidence: **99.39%**
365. **`src/go/doc/testdata/examples/issue43658.go`** -> AI Confidence: **99.39%**
366. **`src/go/parser/error_test.go`** -> AI Confidence: **99.39%**
367. **`src/go/scanner/scanner.go`** -> AI Confidence: **99.39%**
368. **`src/hash/crc32/crc32_test.go`** -> AI Confidence: **99.39%**
369. **`src/html/escape_test.go`** -> AI Confidence: **99.39%**
370. **`src/html/template/escape_test.go`** -> AI Confidence: **99.39%**
371. **`src/html/template/transition.go`** -> AI Confidence: **99.39%**
372. **`src/image/png/reader.go`** -> AI Confidence: **99.39%**
373. **`src/internal/godebug/godebug_test.go`** -> AI Confidence: **99.39%**
374. **`src/internal/godebugs/godebugs_test.go`** -> AI Confidence: **99.39%**
375. **`src/internal/pkgbits/encoder.go`** -> AI Confidence: **99.39%**
376. **`src/internal/poll/fd_windows_test.go`** -> AI Confidence: **99.39%**
377. **`src/internal/runtime/gc/scan/mkasm.go`** -> AI Confidence: **99.39%**
378. **`src/internal/runtime/maps/runtime.go`** -> AI Confidence: **99.39%**
379. **`src/internal/runtime/wasitest/nonblock_test.go`** -> AI Confidence: **99.39%**
380. **`src/internal/runtime/wasitest/tcpecho_test.go`** -> AI Confidence: **99.39%**
381. **`src/internal/strconv/fp_test.go`** -> AI Confidence: **99.39%**
382. **`src/internal/testenv/testenv.go`** -> AI Confidence: **99.39%**
383. **`src/internal/testenv/testenv_test.go`** -> AI Confidence: **99.39%**
384. **`src/internal/trace/internal/testgen/trace.go`** -> AI Confidence: **99.39%**
385. **`src/internal/trace/testdata/testprog/cpu-profile.go`** -> AI Confidence: **99.39%**
386. **`src/internal/trace/tracev1_test.go`** -> AI Confidence: **99.39%**
387. **`src/io/fs/readlink_test.go`** -> AI Confidence: **99.39%**
388. **`src/io/io_test.go`** -> AI Confidence: **99.39%**
389. **`src/io/multi_test.go`** -> AI Confidence: **99.39%**
390. **`src/math/big/calibrate_graph.go`** -> AI Confidence: **99.39%**
391. **`src/math/big/natconv.go`** -> AI Confidence: **99.39%**
392. **`src/math/rand/v2/rand_test.go`** -> AI Confidence: **99.39%**
393. **`src/mime/multipart/multipart_test.go`** -> AI Confidence: **99.39%**
394. **`src/mime/quotedprintable/reader_test.go`** -> AI Confidence: **99.39%**
395. **`src/mime/type_test.go`** -> AI Confidence: **99.39%**
396. **`src/mime/type_unix.go`** -> AI Confidence: **99.39%**
397. **`src/net/file_test.go`** -> AI Confidence: **99.39%**
398. **`src/net/http/cgi/cgi_main.go`** -> AI Confidence: **99.39%**
399. **`src/net/http/cgi/child_test.go`** -> AI Confidence: **99.39%**
400. **`src/net/http/clientconn_test.go`** -> AI Confidence: **99.39%**
401. **`src/net/http/cookie_test.go`** -> AI Confidence: **99.39%**
402. **`src/net/http/cookiejar/jar_test.go`** -> AI Confidence: **99.39%**
403. **`src/net/http/httptest/httptest.go`** -> AI Confidence: **99.39%**
404. **`src/net/http/httputil/dump_test.go`** -> AI Confidence: **99.39%**
405. **`src/net/http/internal/chunked_test.go`** -> AI Confidence: **99.39%**
406. **`src/net/http/internal/http2/gotrack.go`** -> AI Confidence: **99.39%**
407. **`src/net/http/main_test.go`** -> AI Confidence: **99.39%**
408. **`src/net/http/pattern_test.go`** -> AI Confidence: **99.39%**
409. **`src/net/http/server_test.go`** -> AI Confidence: **99.39%**
410. **`src/net/http/sniff_test.go`** -> AI Confidence: **99.39%**
411. **`src/net/lookup_test.go`** -> AI Confidence: **99.39%**
412. **`src/net/main_test.go`** -> AI Confidence: **99.39%**
413. **`src/net/net_windows_test.go`** -> AI Confidence: **99.39%**
414. **`src/net/platform_test.go`** -> AI Confidence: **99.39%**
415. **`src/net/timeout_test.go`** -> AI Confidence: **99.39%**
416. **`src/net/unixsock_test.go`** -> AI Confidence: **99.39%**
417. **`src/os/dir_unix.go`** -> AI Confidence: **99.39%**
418. **`src/os/dir_windows.go`** -> AI Confidence: **99.39%**
419. **`src/os/exec/example_test.go`** -> AI Confidence: **99.39%**
420. **`src/os/exec/exec_posix_test.go`** -> AI Confidence: **99.39%**
421. **`src/os/exec_unix_test.go`** -> AI Confidence: **99.39%**
422. **`src/os/exec_windows_test.go`** -> AI Confidence: **99.39%**
423. **`src/os/executable_test.go`** -> AI Confidence: **99.39%**
424. **`src/os/fifo_test.go`** -> AI Confidence: **99.39%**
425. **`src/os/file_test.go`** -> AI Confidence: **99.39%**
426. **`src/os/os_windows_test.go`** -> AI Confidence: **99.39%**
427. **`src/os/path_windows_test.go`** -> AI Confidence: **99.39%**
428. **`src/os/pipe_test.go`** -> AI Confidence: **99.39%**
429. **`src/os/readfrom_linux_test.go`** -> AI Confidence: **99.39%**
430. **`src/os/root_test.go`** -> AI Confidence: **99.39%**
431. **`src/os/stat_test.go`** -> AI Confidence: **99.39%**
432. **`src/os/writeto_linux_test.go`** -> AI Confidence: **99.39%**
433. **`src/path/filepath/match_test.go`** -> AI Confidence: **99.39%**
434. **`src/regexp/syntax/parse.go`** -> AI Confidence: **99.39%**
435. **`src/runtime/crash_test.go`** -> AI Confidence: **99.39%**
436. **`src/runtime/crash_unix_test.go`** -> AI Confidence: **99.39%**
437. **`src/runtime/malloc_test.go`** -> AI Confidence: **99.39%**
438. **`src/runtime/mbitmap.go`** -> AI Confidence: **99.39%**
439. **`src/runtime/metrics_test.go`** -> AI Confidence: **99.39%**
440. **`src/runtime/mgc.go`** -> AI Confidence: **99.39%**
441. **`src/runtime/mklockrank.go`** -> AI Confidence: **99.39%**
442. **`src/runtime/mpallocbits_test.go`** -> AI Confidence: **99.39%**
443. **`src/runtime/pprof/pprof_rusage.go`** -> AI Confidence: **99.39%**
444. **`src/runtime/pprof/proto.go`** -> AI Confidence: **99.39%**
445. **`src/runtime/runtime-gdb_unix_test.go`** -> AI Confidence: **99.39%**
446. **`src/runtime/runtime-seh_windows_test.go`** -> AI Confidence: **99.39%**
447. **`src/runtime/runtime_test.go`** -> AI Confidence: **99.39%**
448. **`src/runtime/security_test.go`** -> AI Confidence: **99.39%**
449. **`src/runtime/testdata/testexithooks/testexithooks.go`** -> AI Confidence: **99.39%**
450. **`src/runtime/testdata/testprog/finalizer_deadlock.go`** -> AI Confidence: **99.39%**
451. **`src/runtime/unsafepoint_test.go`** -> AI Confidence: **99.39%**
452. **`src/runtime/vdso_test.go`** -> AI Confidence: **99.39%**
453. **`src/simd/archsimd/_gen/simdgen/gen_simdIntrinsics.go`** -> AI Confidence: **99.39%**
454. **`src/simd/archsimd/_gen/simdgen/gen_simdMachineOps.go`** -> AI Confidence: **99.39%**
455. **`src/simd/archsimd/_gen/simdgen/gen_simdssa.go`** -> AI Confidence: **99.39%**
456. **`src/simd/archsimd/_gen/unify/unify_test.go`** -> AI Confidence: **99.39%**
457. **`src/slices/slices_test.go`** -> AI Confidence: **99.39%**
458. **`src/slices/sort_test.go`** -> AI Confidence: **99.39%**
459. **`src/sort/gen_sort_variants.go`** -> AI Confidence: **99.39%**
460. **`src/strconv/makeisprint.go`** -> AI Confidence: **99.39%**
461. **`src/strings/search_test.go`** -> AI Confidence: **99.39%**
462. **`src/sync/oncefunc_test.go`** -> AI Confidence: **99.39%**
463. **`src/sync/pool_test.go`** -> AI Confidence: **99.39%**
464. **`src/syscall/exec_windows_test.go`** -> AI Confidence: **99.39%**
465. **`src/syscall/js/js_test.go`** -> AI Confidence: **99.39%**
466. **`src/syscall/syscall_linux_test.go`** -> AI Confidence: **99.39%**
467. **`src/testing/fstest/testfs.go`** -> AI Confidence: **99.39%**
468. **`src/testing/fuzz.go`** -> AI Confidence: **99.39%**
469. **`src/testing/testing_test.go`** -> AI Confidence: **99.39%**
470. **`src/text/tabwriter/tabwriter_test.go`** -> AI Confidence: **99.39%**
471. **`src/text/template/parse/parse_test.go`** -> AI Confidence: **99.39%**
472. **`src/time/zoneinfo_test.go`** -> AI Confidence: **99.39%**
473. **`src/weak/pointer_test.go`** -> AI Confidence: **99.39%**
474. **`src/cmd/cgo/internal/testcarchive/testdata/main2.c`** -> AI Confidence: **99.39%**
475. **`src/cmd/cgo/internal/testcshared/testdata/main4.c`** -> AI Confidence: **99.39%**
476. **`src/archive/tar/writer_test.go`** -> AI Confidence: **99.35%**
477. **`src/cmd/compile/internal/gc/obj.go`** -> AI Confidence: **99.35%**
478. **`src/cmd/compile/internal/inline/inl.go`** -> AI Confidence: **99.35%**
479. **`src/cmd/compile/internal/ssa/debug_test.go`** -> AI Confidence: **99.35%**
480. **`src/cmd/compile/internal/staticinit/sched.go`** -> AI Confidence: **99.35%**
481. **`src/cmd/go/internal/modfetch/zip_sum_test/zip_sum_test.go`** -> AI Confidence: **99.35%**
482. **`src/cmd/internal/disasm/disasm.go`** -> AI Confidence: **99.35%**
483. **`src/cmd/link/internal/ld/dwarf.go`** -> AI Confidence: **99.35%**
484. **`src/cmd/link/internal/ld/pe.go`** -> AI Confidence: **99.35%**
485. **`src/crypto/tls/handshake_server_test.go`** -> AI Confidence: **99.35%**
486. **`src/go/doc/reader.go`** -> AI Confidence: **99.35%**
487. **`src/net/http/http_test.go`** -> AI Confidence: **99.35%**
488. **`src/runtime/mheap.go`** -> AI Confidence: **99.35%**
489. **`src/text/template/exec_test.go`** -> AI Confidence: **99.35%**
490. **`src/bytes/reader_test.go`** -> AI Confidence: **99.34%**
491. **`src/cmd/cgo/gcc.go`** -> AI Confidence: **99.34%**
492. **`src/cmd/cgo/internal/test/issue9400_linux.go`** -> AI Confidence: **99.34%**
493. **`src/cmd/cgo/internal/testplugin/testdata/host/host.go`** -> AI Confidence: **99.34%**
494. **`src/cmd/compile/internal/liveness/intervals_test.go`** -> AI Confidence: **99.34%**
495. **`src/cmd/compile/internal/reflectdata/alg.go`** -> AI Confidence: **99.34%**
496. **`src/cmd/compile/internal/reflectdata/map.go`** -> AI Confidence: **99.34%**
497. **`src/cmd/compile/internal/ssa/deadstore_test.go`** -> AI Confidence: **99.34%**
498. **`src/cmd/compile/internal/ssa/pair.go`** -> AI Confidence: **99.34%**
499. **`src/cmd/compile/internal/ssa/schedule.go`** -> AI Confidence: **99.34%**
500. **`src/cmd/compile/internal/ssagen/phi.go`** -> AI Confidence: **99.34%**
501. **`src/cmd/compile/internal/test/free_test.go`** -> AI Confidence: **99.34%**
502. **`src/cmd/compile/internal/typecheck/stmt.go`** -> AI Confidence: **99.34%**
503. **`src/cmd/compile/internal/types2/typeterm_test.go`** -> AI Confidence: **99.34%**
504. **`src/cmd/compile/internal/types2/unify.go`** -> AI Confidence: **99.34%**
505. **`src/cmd/compile/internal/walk/select.go`** -> AI Confidence: **99.34%**
506. **`src/cmd/go/internal/auth/userauth_test.go`** -> AI Confidence: **99.34%**
507. **`src/cmd/go/internal/work/shell_test.go`** -> AI Confidence: **99.34%**
508. **`src/cmd/internal/dwarf/dwarf.go`** -> AI Confidence: **99.34%**
509. **`src/cmd/link/internal/ld/asmb.go`** -> AI Confidence: **99.34%**
510. **`src/cmd/link/internal/ld/fallocate_test.go`** -> AI Confidence: **99.34%**
511. **`src/cmd/link/internal/ld/stackcheck_test.go`** -> AI Confidence: **99.34%**
512. **`src/cmd/link/internal/ld/sym.go`** -> AI Confidence: **99.34%**
513. **`src/cmd/link/internal/x86/asm.go`** -> AI Confidence: **99.34%**
514. **`src/compress/flate/inflate_test.go`** -> AI Confidence: **99.34%**
515. **`src/compress/flate/writer_test.go`** -> AI Confidence: **99.34%**
516. **`src/compress/gzip/gzip_test.go`** -> AI Confidence: **99.34%**
517. **`src/context/benchmark_test.go`** -> AI Confidence: **99.34%**
518. **`src/crypto/ecdsa/equal_test.go`** -> AI Confidence: **99.34%**
519. **`src/crypto/elliptic/elliptic_test.go`** -> AI Confidence: **99.34%**
520. **`src/crypto/internal/cryptotest/stream.go`** -> AI Confidence: **99.34%**
521. **`src/crypto/internal/fips140/aes/_asm/ctr/ctr_amd64_asm.go`** -> AI Confidence: **99.34%**
522. **`src/crypto/internal/fips140/aes/_asm/standard/aes_amd64.go`** -> AI Confidence: **99.34%**
523. **`src/crypto/internal/fips140/mlkem/field_test.go`** -> AI Confidence: **99.34%**
524. **`src/crypto/internal/fips140/subtle/constant_time_test.go`** -> AI Confidence: **99.34%**
525. **`src/crypto/internal/fips140test/nistec_ordinv_test.go`** -> AI Confidence: **99.34%**
526. **`src/crypto/rc4/rc4_test.go`** -> AI Confidence: **99.34%**
527. **`src/crypto/subtle/xor_test.go`** -> AI Confidence: **99.34%**
528. **`src/crypto/tls/auth_test.go`** -> AI Confidence: **99.34%**
529. **`src/crypto/x509/pem_decrypt_test.go`** -> AI Confidence: **99.34%**
530. **`src/crypto/x509/root_linux_test.go`** -> AI Confidence: **99.34%**
531. **`src/database/sql/example_test.go`** -> AI Confidence: **99.34%**
532. **`src/encoding/ascii85/ascii85_test.go`** -> AI Confidence: **99.34%**
533. **`src/encoding/csv/fuzz_test.go`** -> AI Confidence: **99.34%**
534. **`src/encoding/hex/hex_test.go`** -> AI Confidence: **99.34%**
535. **`src/encoding/json/internal/jsonopts/options_test.go`** -> AI Confidence: **99.34%**
536. **`src/encoding/json/internal/jsonwire/encode.go`** -> AI Confidence: **99.34%**
537. **`src/encoding/json/internal/jsonwire/wire_test.go`** -> AI Confidence: **99.34%**
538. **`src/encoding/json/v2/intern_test.go`** -> AI Confidence: **99.34%**
539. **`src/fmt/example_test.go`** -> AI Confidence: **99.34%**
540. **`src/go/doc/comment/wrap_test.go`** -> AI Confidence: **99.34%**
541. **`src/go/token/position_bench_test.go`** -> AI Confidence: **99.34%**
542. **`src/go/types/typeterm_test.go`** -> AI Confidence: **99.34%**
543. **`src/go/types/unify.go`** -> AI Confidence: **99.34%**
544. **`src/hash/adler32/adler32_test.go`** -> AI Confidence: **99.34%**
545. **`src/hash/crc64/crc64_test.go`** -> AI Confidence: **99.34%**
546. **`src/image/jpeg/dct_test.go`** -> AI Confidence: **99.34%**
547. **`src/image/jpeg/fuzz_test.go`** -> AI Confidence: **99.34%**
548. **`src/image/png/fuzz_test.go`** -> AI Confidence: **99.34%**
549. **`src/index/suffixarray/gen.go`** -> AI Confidence: **99.34%**
550. **`src/internal/chacha8rand/rand_test.go`** -> AI Confidence: **99.34%**
551. **`src/internal/poll/splice_linux_test.go`** -> AI Confidence: **99.34%**
552. **`src/internal/routebsd/message_test.go`** -> AI Confidence: **99.34%**
553. **`src/internal/runtime/atomic/atomic_test.go`** -> AI Confidence: **99.34%**
554. **`src/internal/runtime/cgroup/cgroup_test.go`** -> AI Confidence: **99.34%**
555. **`src/internal/trace/gc.go`** -> AI Confidence: **99.34%**
556. **`src/internal/trace/gc_test.go`** -> AI Confidence: **99.34%**
557. **`src/internal/trace/internal/tracev1/parser_test.go`** -> AI Confidence: **99.34%**
558. **`src/internal/trace/summary_test.go`** -> AI Confidence: **99.34%**
559. **`src/internal/trace/testtrace/helpers.go`** -> AI Confidence: **99.34%**
560. **`src/internal/trace/tracev2/events_test.go`** -> AI Confidence: **99.34%**
561. **`src/internal/zstd/fuzz_test.go`** -> AI Confidence: **99.34%**
562. **`src/internal/zstd/xxhash_test.go`** -> AI Confidence: **99.34%**
563. **`src/io/example_test.go`** -> AI Confidence: **99.34%**
564. **`src/io/ioutil/ioutil_test.go`** -> AI Confidence: **99.34%**
565. **`src/math/big/internal/asmgen/asm.go`** -> AI Confidence: **99.34%**
566. **`src/math/rand/regress_test.go`** -> AI Confidence: **99.34%**
567. **`src/net/external_test.go`** -> AI Confidence: **99.34%**
568. **`src/net/hosts_test.go`** -> AI Confidence: **99.34%**
569. **`src/net/http/cookie.go`** -> AI Confidence: **99.34%**
570. **`src/net/http/filetransport_test.go`** -> AI Confidence: **99.34%**
571. **`src/net/http/httptest/httptest_test.go`** -> AI Confidence: **99.34%**
572. **`src/net/http/internal/http2/databuffer_test.go`** -> AI Confidence: **99.34%**
573. **`src/net/netip/netip_pkg_test.go`** -> AI Confidence: **99.34%**
574. **`src/net/url/example_test.go`** -> AI Confidence: **99.34%**
575. **`src/net/writev_test.go`** -> AI Confidence: **99.34%**
576. **`src/os/root_unix_test.go`** -> AI Confidence: **99.34%**
577. **`src/regexp/find_test.go`** -> AI Confidence: **99.34%**
578. **`src/runtime/_mkmalloc/mksizeclasses.go`** -> AI Confidence: **99.34%**
579. **`src/runtime/decoratemappings_test.go`** -> AI Confidence: **99.34%**
580. **`src/runtime/mfinal.go`** -> AI Confidence: **99.34%**
581. **`src/runtime/rand_test.go`** -> AI Confidence: **99.34%**
582. **`src/runtime/runtime-lldb_test.go`** -> AI Confidence: **99.34%**
583. **`src/runtime/testdata/testprog/gc.go`** -> AI Confidence: **99.34%**
584. **`src/runtime/testdata/testprogcgo/tracebackctxt.go`** -> AI Confidence: **99.34%**
585. **`src/strconv/number_test.go`** -> AI Confidence: **99.34%**
586. **`src/strconv/quote_test.go`** -> AI Confidence: **99.34%**
587. **`src/strings/reader_test.go`** -> AI Confidence: **99.34%**
588. **`src/sync/map_bench_test.go`** -> AI Confidence: **99.34%**
589. **`src/syscall/env_unix_test.go`** -> AI Confidence: **99.34%**
590. **`src/syscall/exec_freebsd_test.go`** -> AI Confidence: **99.34%**
591. **`src/syscall/syscall_test.go`** -> AI Confidence: **99.34%**
592. **`src/testing/iotest/reader_test.go`** -> AI Confidence: **99.34%**
593. **`src/text/scanner/scanner.go`** -> AI Confidence: **99.34%**
594. **`src/text/scanner/scanner_test.go`** -> AI Confidence: **99.34%**
595. **`src/unicode/utf16/utf16_test.go`** -> AI Confidence: **99.34%**
596. **`src/unicode/utf8/utf8_test.go`** -> AI Confidence: **99.34%**
597. **`src/cmd/compile/internal/types/size.go`** -> AI Confidence: **99.33%**
598. **`src/encoding/xml/read.go`** -> AI Confidence: **99.33%**
599. **`src/bytes/boundary_test.go`** -> AI Confidence: **99.32%**
600. **`src/bytes/compare_test.go`** -> AI Confidence: **99.32%**
601. **`src/cmd/cgo/internal/testplugin/testdata/issue25756/main.go`** -> AI Confidence: **99.32%**
602. **`src/cmd/compile/internal/escape/expr.go`** -> AI Confidence: **99.32%**
603. **`src/cmd/compile/internal/escape/stmt.go`** -> AI Confidence: **99.32%**
604. **`src/cmd/compile/internal/ir/abi.go`** -> AI Confidence: **99.32%**
605. **`src/cmd/compile/internal/reflectdata/reflect.go`** -> AI Confidence: **99.32%**
606. **`src/cmd/compile/internal/ssa/deadstore.go`** -> AI Confidence: **99.32%**
607. **`src/cmd/compile/internal/ssa/decompose.go`** -> AI Confidence: **99.32%**
608. **`src/cmd/compile/internal/ssa/nilcheck.go`** -> AI Confidence: **99.32%**
609. **`src/cmd/compile/internal/ssa/rewriteCond_test.go`** -> AI Confidence: **99.32%**
610. **`src/cmd/compile/internal/ssa/sccp_test.go`** -> AI Confidence: **99.32%**
611. **`src/cmd/compile/internal/syntax/printer.go`** -> AI Confidence: **99.32%**
612. **`src/cmd/compile/internal/typebits/typebits.go`** -> AI Confidence: **99.32%**
613. **`src/cmd/go/internal/auth/auth_test.go`** -> AI Confidence: **99.32%**
614. **`src/cmd/go/internal/work/security_test.go`** -> AI Confidence: **99.32%**
615. **`src/compress/flate/dict_decoder_test.go`** -> AI Confidence: **99.32%**
616. **`src/crypto/internal/cryptotest/blockmode.go`** -> AI Confidence: **99.32%**
617. **`src/go/doc/comment/markdown.go`** -> AI Confidence: **99.32%**
618. **`src/go/printer/gobuild.go`** -> AI Confidence: **99.32%**
619. **`src/go/token/tree_test.go`** -> AI Confidence: **99.32%**
620. **`src/go/types/exprstring.go`** -> AI Confidence: **99.32%**
621. **`src/image/image_test.go`** -> AI Confidence: **99.32%**
622. **`src/internal/cpu/cpu.go`** -> AI Confidence: **99.32%**
623. **`src/internal/cpu/cpu_x86_test.go`** -> AI Confidence: **99.32%**
624. **`src/internal/dag/parse_test.go`** -> AI Confidence: **99.32%**
625. **`src/internal/poll/writev.go`** -> AI Confidence: **99.32%**
626. **`src/internal/runtime/cgroup/line_reader_test.go`** -> AI Confidence: **99.32%**
627. **`src/internal/saferio/io_test.go`** -> AI Confidence: **99.32%**
628. **`src/internal/strconv/math_test.go`** -> AI Confidence: **99.32%**
629. **`src/internal/sync/mutex.go`** -> AI Confidence: **99.32%**
630. **`src/internal/trace/mud_test.go`** -> AI Confidence: **99.32%**
631. **`src/math/big/bits_test.go`** -> AI Confidence: **99.32%**
632. **`src/math/big/floatexample_test.go`** -> AI Confidence: **99.32%**
633. **`src/math/big/ftoa.go`** -> AI Confidence: **99.32%**
634. **`src/math/big/internal/asmgen/pipe.go`** -> AI Confidence: **99.32%**
635. **`src/net/iprawsock_test.go`** -> AI Confidence: **99.32%**
636. **`src/net/smtp/example_test.go`** -> AI Confidence: **99.32%**
637. **`src/net/tcpconn_keepalive_illumos_test.go`** -> AI Confidence: **99.32%**
638. **`src/net/textproto/writer_test.go`** -> AI Confidence: **99.32%**
639. **`src/net/udpsock_plan9_test.go`** -> AI Confidence: **99.32%**
640. **`src/os/stat_darwin.go`** -> AI Confidence: **99.32%**
641. **`src/os/stat_dragonfly.go`** -> AI Confidence: **99.32%**
642. **`src/os/stat_freebsd.go`** -> AI Confidence: **99.32%**
643. **`src/os/stat_js.go`** -> AI Confidence: **99.32%**
644. **`src/os/stat_linux.go`** -> AI Confidence: **99.32%**
645. **`src/os/stat_netbsd.go`** -> AI Confidence: **99.32%**
646. **`src/os/stat_openbsd.go`** -> AI Confidence: **99.32%**
647. **`src/os/stat_solaris.go`** -> AI Confidence: **99.32%**
648. **`src/os/user/lookup_unix_test.go`** -> AI Confidence: **99.32%**
649. **`src/os/user/user_test.go`** -> AI Confidence: **99.32%**
650. **`src/runtime/histogram_test.go`** -> AI Confidence: **99.32%**
651. **`src/runtime/mwbbuf.go`** -> AI Confidence: **99.32%**
652. **`src/runtime/netpoll_kqueue.go`** -> AI Confidence: **99.32%**
653. **`src/runtime/select.go`** -> AI Confidence: **99.32%**
654. **`src/runtime/sema.go`** -> AI Confidence: **99.32%**
655. **`src/simd/archsimd/internal/simd_test/transpose_test.go`** -> AI Confidence: **99.32%**
656. **`src/strconv/example_test.go`** -> AI Confidence: **99.32%**
657. **`src/syscall/exec_freebsd.go`** -> AI Confidence: **99.32%**
658. **`src/syscall/exec_libc.go`** -> AI Confidence: **99.32%**
659. **`src/syscall/exec_libc2.go`** -> AI Confidence: **99.32%**
660. **`src/syscall/syscall_bsd_test.go`** -> AI Confidence: **99.32%**
661. **`src/testing/loop_test.go`** -> AI Confidence: **99.32%**
662. **`src/time/example_test.go`** -> AI Confidence: **99.32%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `src/crypto/tls/example_test.go` -> **100.0%** Exposure
- `src/crypto/x509/example_test.go` -> **100.0%** Exposure
- `src/crypto/x509/verify_test.go` -> **100.0%** Exposure
- `src/encoding/pem/example_test.go` -> **100.0%** Exposure
- `src/net/http/internal/testcert/testcert.go` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `131` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `34315` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/cmd/go/internal/work/build.go` (GO) -> Cumulative Risk: **802.03**
- **Archetype:** `file_cluster_4` (Distance: 13.176 IQR)
- **Magnitude:** 971.42 | **LOC:** 965 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 58.8%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `InstallPackages` (Impact: 68.5), `runBuild` (Impact: 65.0), `runInstall` (Impact: 40.1)

### 2. `src/internal/types/testdata/check/typeparams.go` (GO) -> Cumulative Risk: **746.93**
- **Archetype:** `file_cluster_11` (Distance: 23.496 IQR)
- **Magnitude:** 0.13 | **LOC:** 511 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (95.2267%)
- **Heaviest Functions:** `Unknown_Block` (Impact: 7.3), `reverse` (Impact: 7.2), `Unknown_Block` (Impact: 2.6)

### 3. `src/runtime/testdata/testgoroutineleakprofile/goker/moby27782.go` (GO) -> Cumulative Risk: **726.85**
- **Archetype:** `file_cluster_4` (Distance: 11.791 IQR)
- **Magnitude:** 0.27 | **LOC:** 250 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9773%), Documentation (85.6906%)
- **Heaviest Functions:** `readEvents` (Impact: 16.5), `isClosed` (Impact: 9.3), `followLogs_moby27782` (Impact: 8.9)

### 4. `src/runtime/testdata/testgoroutineleakprofile/goker/kubernetes30872.go` (GO) -> Cumulative Risk: **724.75**
- **Archetype:** `file_cluster_4` (Distance: 11.057 IQR)
- **Magnitude:** 0.19 | **LOC:** 224 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (98.3381%)
- **Heaviest Functions:** `OnAdd` (Impact: 4.7), `Kubernetes30872` (Impact: 4.3), `StartWithHandler` (Impact: 2.7)

### 5. `src/internal/syscall/windows/zsyscall_windows.go` (GO) -> Cumulative Risk: **714.75**
- **Archetype:** `file_cluster_12` (Distance: 14.717 IQR)
- **Magnitude:** 0.84 | **LOC:** 676 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 44.4%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.879%)
- **Heaviest Functions:** `errnoErr` (Impact: 8.6), `adjustTokenPrivileges` (Impact: 8.5), `WSAGetOverlappedResult` (Impact: 7.9)

### 6. `src/internal/types/testdata/check/stmt0.go` (GO) -> Cumulative Risk: **712.41**
- **Archetype:** `file_cluster_4` (Distance: 13.012 IQR)
- **Magnitude:** 1.45 | **LOC:** 995 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9994%)
- **Heaviest Functions:** `switches0` (Impact: 125.3), `rangeloops1` (Impact: 109.6), `switches1` (Impact: 100.9)

### 7. `src/net/http/httputil/dump.go` (GO) -> Cumulative Risk: **702.45**
- **Archetype:** `file_cluster_4` (Distance: 13.65 IQR)
- **Magnitude:** 297.1 | **LOC:** 337 | **CtrlFlow:** 42.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.976%), Concurrency (99.9368%)
- **Heaviest Functions:** `DumpRequest` (Impact: 27.3), `DumpRequestOut` (Impact: 21.5), `DumpResponse` (Impact: 19.0)

### 8. `src/net/http/transport.go` (GO) -> Cumulative Risk: **701.55**
- **Archetype:** `file_cluster_4` (Distance: 14.438 IQR)
- **Magnitude:** 2937.24 | **LOC:** 3373 | **CtrlFlow:** 56.4% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.7402%), Safety Score (96.8037%)
- **Heaviest Functions:** `protocols` (Impact: 631.9), `validateHeaders` (Impact: 551.0), `shouldRetryRequest` (Impact: 193.9)

### 9. `src/runtime/testdata/testprogcgo/bindm.c` (C) -> Cumulative Risk: **692.45**
- **Archetype:** `file_cluster_4` (Distance: 12.432 IQR)
- **Magnitude:** 0.04 | **LOC:** 35 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.965%), Cognitive Load (97.8821%)
- **Heaviest Functions:** `checkBindMThread` (Impact: 3.9), `CheckBindM` (Impact: 3.5)

### 10. `src/crypto/tls/handshake_test.go` (GO) -> Cumulative Risk: **687.99**
- **Archetype:** `file_cluster_4` (Distance: 13.978 IQR)
- **Magnitude:** 8.55 | **LOC:** 781 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Secrets Risk (99.7742%), Tech Debt (97.4607%)
- **Heaviest Functions:** `localPipe` (Impact: 36.5), `parseTestData` (Impact: 26.4), `TestServerHelloTrailingMessage` (Impact: 20.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/regexp/all_test.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.267 IQR)
- **Top Global Matches:** file_cluster_8: 13.267, file_cluster_7: 13.619, file_cluster_13: 13.749
- **Magnitude:** 12009.8 | **LOC:** 1006 | **CtrlFlow:** 85.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (52.5087%), Tech Debt (10.2281%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 26`, `args: 48`, `func_start: 48`, `class_start: 6`
* *Risk/State:* `state_mutation: 636`, `fragile_debt: 2`
* *Architecture:* `api: 48`, `import: 1`
* *Defense:* `safety: 16`, `doc: 21`, `test: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` slices, , syntax, bytes, testing, a, strings, utf8...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/reflect/value.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_12` (Drift: 15.01 IQR)
- **Top Global Matches:** file_cluster_12: 15.01, file_cluster_11: 15.022, file_cluster_15: 15.054
- **Magnitude:** 5851.44 | **LOC:** 3901 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 41.7%
- **Risk Profile:** Cognitive Load (49.8933%), Tech Debt (8.5825%)
**Top Internal Functions/Classes:**
  * `packEfaceData` (Impact: 754.8)
  * `callReflect` (Impact: 734.7)
  * `callMethod` (Impact: 702.1)
  * `IsZero` (Impact: 575.9)
  * `SetZero` (Impact: 514.1)
    * *Intent:* // Convert v to type typ if v is assignable to a variable // of type t in the language spec. // See ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 335`, `structural_boundaries: 184`, `args: 112`, `func_start: 112`, `class_start: 3`
* *Risk/State:* `state_mutation: 530`, `dead_code: 12`, `planned_debt: 3`
* *Architecture:* `api: 83`, `import: 1`
* *Defense:* `doc: 226`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` strconv, abi, math, goarch, iter, unsafeheader, unsafe, errors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/tls/testdata/example-cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/tls/testdata/example-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/platform_root_cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/platform_root_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/test-file.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/AllCertificatesNoPoliciesTest2EE.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/AllCertificatesSamePoliciesTest10EE.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/AllCertificatesSamePoliciesTest13EE.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/AllCertificatesanyPolicyTest11EE.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/AnyPolicyTest14EE.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/BadCRLIssuerNameCACert.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/BadCRLSignatureCACert.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/BadSignedCACert.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/BadnotAfterDateCACert.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/BadnotBeforeDateCACert.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/BasicSelfIssuedCRLSigningKeyCACert.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/BasicSelfIssuedCRLSigningKeyCRLCert.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/BasicSelfIssuedNewKeyCACert.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/BasicSelfIssuedNewKeyOldWithNewCACert.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/BasicSelfIssuedOldKeyCACert.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/BasicSelfIssuedOldKeyNewWithOldCACert.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/CPSPointerQualifierTest20EE.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crypto/x509/testdata/nist-pkits/certs/DSACACert.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/cmd/compile/internal/types2/compilersupport.go` (GO) | Magnitude: 12.88 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 9, indent_tabs: 7, structural_boundaries: 4, args: 3
- `src/cmd/go/internal/modindex/build.go` (GO) | Magnitude: 833.16 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 294, indent_tabs: 287, branch: 119, encapsulation: 89
- `src/net/http/internal/chunked.go` (GO) | Magnitude: 191.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 96, state_mutation: 82, branch: 41, encapsulation: 17
- `src/cmd/internal/cov/readcovdata.go` (GO) | Magnitude: 121.68 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 112, state_mutation: 57, encapsulation: 27, structural_boundaries: 23
- `src/internal/syscall/windows/registry/key.go` (GO) | Magnitude: 132.16 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 75, state_mutation: 54, api: 34, doc: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/cmd/compile/internal/ssa/sparsemap.go` (GO) | Magnitude: 66.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 38, indent_tabs: 32, encapsulation: 18, structural_boundaries: 17
- `src/cmd/link/internal/ld/outbuf_windows.go` (GO) | Magnitude: 72.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 47, state_mutation: 42, encapsulation: 16, pointers: 12
- `src/os/file_unix.go` (GO) | Magnitude: 242.78 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 178, state_mutation: 123, branch: 53, encapsulation: 47
- `src/cmd/compile/internal/noder/linker.go` (GO) | Magnitude: 148.86 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 145, state_mutation: 79, branch: 45, encapsulation: 37
- `src/cmd/compile/internal/slice/slice.go` (GO) | Magnitude: 78.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 71, state_mutation: 66, branch: 27, doc: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/crypto/internal/fips140/subtle/xor_generic.go` (GO) | Magnitude: 0.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 42, indent_tabs: 31, pointers: 16, encapsulation: 14
- `src/encoding/binary/binary.go` (GO) | Magnitude: 1157.18 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 700, state_mutation: 424, branch: 251, explicit_casts: 189
- `src/runtime/race0.go` (GO) | Magnitude: 54.04 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 37, encapsulation: 28, args: 27, func_start: 27
- `src/internal/runtime/atomic/atomic_arm.go` (GO) | Magnitude: 193.0 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 105, state_mutation: 94, pointers: 87, args: 36
- `src/runtime/tracemap.go` (GO) | Magnitude: 46.72 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 40, state_mutation: 26, encapsulation: 17, doc: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/cmd/link/internal/loader/symbolbuilder.go` (GO) | Magnitude: 74.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 54, state_mutation: 25, pointers: 15, structural_boundaries: 12
- `src/database/sql/convert.go` (GO) | Magnitude: 78.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 58, state_mutation: 30, structural_boundaries: 25, doc: 20
- `src/index/suffixarray/suffixarray.go` (GO) | Magnitude: 336.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 189, indent_tabs: 185, branch: 59, encapsulation: 49
- `src/cmd/compile/internal/test/inst_test.go` (GO) | Magnitude: 52.06 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 38, state_mutation: 34, encapsulation: 12, doc: 8
- `src/internal/trace/batch.go` (GO) | Magnitude: 78.5 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 71, state_mutation: 33, branch: 26, structural_boundaries: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/net/ip.go` (GO) | Magnitude: 653.9 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 306, state_mutation: 216, branch: 124, structural_boundaries: 88
- `src/go/types/alias.go` (GO) | Magnitude: 74.46 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 34, pointers: 31, doc: 28, state_mutation: 24
- `src/cmd/compile/internal/types2/alias.go` (GO) | Magnitude: 74.46 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 34, pointers: 31, doc: 27, state_mutation: 24
- `src/runtime/signal_freebsd_386.go` (GO) | Magnitude: 51.32 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 23, structural_boundaries: 20, args: 20, func_start: 20
- `src/sync/waitgroup.go` (GO) | Magnitude: 194.54 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 98, doc: 43, state_mutation: 36, branch: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/internal/types/testdata/check/map0.go` (GO) | Magnitude: 0.07 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 53, state_mutation: 33, structural_boundaries: 23, encapsulation: 19
- `src/slices/slices.go` (GO) | Magnitude: 393.2 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 158, state_mutation: 126, doc: 59, branch: 52
- `src/sync/poolqueue.go` (GO) | Magnitude: 143.54 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 88, state_mutation: 84, encapsulation: 41, doc: 28
- `src/time/sleep.go` (GO) | Magnitude: 14.58 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 5, args: 4, func_start: 4
- `src/internal/types/testdata/fixedbugs/issue48695.go` (GO) | Magnitude: 0.0 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 4, structural_boundaries: 2, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/net/http/pprof/pprof.go` (GO) | Magnitude: 49.6 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 71, state_mutation: 43, doc: 20, encapsulation: 19
- `src/runtime/time_plan9.go` (GO) | Magnitude: 14.94 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 9, indent_tabs: 8, doc: 4, encapsulation: 4
- `src/go/types/example_test.go` (GO) | Magnitude: 201.64 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 126, state_mutation: 112, encapsulation: 56, structural_boundaries: 41
- `src/internal/strconv/atoc.go` (GO) | Magnitude: 27.62 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 29, branch: 13, doc: 13, state_mutation: 12
- `src/cmd/compile/internal/types2/example_test.go` (GO) | Magnitude: 144.7 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 91, state_mutation: 79, encapsulation: 39, structural_boundaries: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/net/mptcpsock_linux_test.go` (GO) | Magnitude: 232.18 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 134, state_mutation: 126, branch: 38, encapsulation: 26
- `src/cmd/go/internal/envcmd/env.go` (GO) | Magnitude: 869.76 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 409, state_mutation: 329, branch: 136, encapsulation: 111
- `src/cmd/compile/internal/logopt/logopt_test.go` (GO) | Magnitude: 118.28 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 67, state_mutation: 59, structural_boundaries: 31, encapsulation: 24
- `src/cmd/compile/internal/test/clobberdead_test.go` (GO) | Magnitude: 45.08 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 25, state_mutation: 22, encapsulation: 9, structural_boundaries: 6
- `src/cmd/compile/internal/types2/builtins_test.go` (GO) | Magnitude: 154.82 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 128, state_mutation: 113, closures: 90, safety_bypasses: 85

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/encoding/json/v2_options.go` (GO) | Magnitude: 48.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 85, indent_tabs: 40, structural_boundaries: 16, branch: 12
- `src/errors/errors.go` (GO) | Magnitude: 9.72 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 11, dead_code: 6, structural_boundaries: 5, api: 4
- `src/crypto/rsa/rsa.go` (GO) | Magnitude: 2.49 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 143, state_mutation: 139, encapsulation: 39, branch: 37
- `src/runtime/rand.go` (GO) | Magnitude: 57.64 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 39, state_mutation: 30, encapsulation: 18, doc: 16
- `src/net/cgo_stub.go` (GO) | Magnitude: 11.26 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: reflection_metaprogramming: 10, planned_debt: 6, encapsulation: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/cmd/internal/script/scripttest/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 1
- `src/crypto/internal/fips140/edwards25519/doc.go` (GO) | Magnitude: 0.11 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 1
- `src/internal/types/testdata/fixedbugs/issue42695.go` (GO) | Magnitude: 0.01 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, state_mutation: 5, safety_bypasses: 3, globals: 3
- `src/math/sin.go` (GO) | Magnitude: 182.18 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 106, state_mutation: 104, doc: 35, branch: 27
- `src/runtime/race/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/cmd/cgo/internal/testplugin/testdata/method2/plugin.go` (GO) | Magnitude: 0.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, args: 2, func_start: 2, doc: 2
- `src/cmd/compile/internal/ppc64/galign.go` (GO) | Magnitude: 27.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 21, indent_tabs: 16, encapsulation: 11, structural_boundaries: 2
- `src/crypto/internal/entropy/entropy.go` (GO) | Magnitude: 0.04 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 7, indent_tabs: 3, structural_boundaries: 2, api: 2
- `src/internal/runtime/gc/scan/scan_test.go` (GO) | Magnitude: 376.1 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 245, indent_tabs: 178, encapsulation: 60, branch: 55
- `src/internal/syscall/unix/siginfo_linux_test.go` (GO) | Magnitude: 54.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 40, state_mutation: 36, encapsulation: 12, reflection_metaprogramming: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/runtime/runtime_noclearenv.go` (GO) | Magnitude: 9.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 3, state_mutation: 3, doc: 3, indent_tabs: 3
- `src/math/floor.go` (GO) | Magnitude: 132.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 66, indent_tabs: 61, doc: 21, branch: 19
- `src/internal/runtime/sys/nih.go` (GO) | Magnitude: 12.56 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 5, doc: 5, class_start: 2, api: 1
- `src/unsafe/unsafe.go` (GO) | Magnitude: 47.24 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 47, api: 11, dead_code: 9, args: 8
- `src/cmd/cgo/internal/test/issue29563/weak1.c` (C) | Magnitude: 6.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 4, structural_boundaries: 1, func_start: 1, state_mutation: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/cmd/compile/internal/ssa/prove.go` -> Churn: **100.0%** | Cog Load: 52.5665% | Debt: 28.3341%
- `src/cmd/go/internal/modload/init.go` -> Churn: **86.19%** | Cog Load: 52.9399% | Debt: 11.6987%
- `src/net/url/url.go` -> Churn: **79.4%** | Cog Load: 45.9887% | Debt: 97.7666%
- `src/cmd/link/link_test.go` -> Churn: **78.04%** | Cog Load: 34.4987% | Debt: 53.6699%
- `src/cmd/compile/internal/amd64/ssa.go` -> Churn: **74.64%** | Cog Load: 50.6586% | Debt: 87.1492%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/regexp/all_test.go` -> **Russ Cox** (100.0% isolated ownership) | Magnitude: 12009.8
- `src/math/all_test.go` -> **Meng Zhuo** (100.0% isolated ownership) | Magnitude: 4380.98
- `src/runtime/chan_test.go` -> **Tobias Klauser** (100.0% isolated ownership) | Magnitude: 2781.72
- `src/encoding/json/v2/arshal_default.go` -> **Joe Tsai** (100.0% isolated ownership) | Magnitude: 2488.06
- `src/cmd/cgo/internal/test/callback.go` -> **cuishuang** (100.0% isolated ownership) | Magnitude: 2365.5

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/bytes/bytes.go` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 100.0%)
- `src/cmd/go/internal/vcweb/vcstest/vcstest.go` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `src/internal/testenv/testenv.go` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `src/archive/tar/strconv.go` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `src/cmd/compile/internal/reflectdata/reflect.go` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/math/bits.go` -> **Severity: 1486.597** (Blast Radius: 27.969 * Doc Risk: 53.1516%)
- `src/internal/goarch/goarch.go` -> **Severity: 868.6** (Blast Radius: 8.686 * Doc Risk: 100.0%)
- `src/bytes/bytes.go` -> **Severity: 723.269** (Blast Radius: 52.015 * Doc Risk: 13.905%)
- `src/cmd/compile/internal/objw/objw.go` -> **Severity: 469.715** (Blast Radius: 4.704 * Doc Risk: 99.8544%)
- `src/cmd/compile/internal/syntax/syntax.go` -> **Severity: 363.2** (Blast Radius: 3.632 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
