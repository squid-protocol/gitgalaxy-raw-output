# ARCHITECTURAL_BRIEF: RaspberryPi
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/RaspberryPi` |
| **Timestamp** | `2026-08-07T03:49:06.390960+00:00` |
| **Scan Duration** | `2.65s` |
| **Git Branch** | `master` |
| **Git Commit** | `5783e31ba16353413a9248431da464e37a5619d1` |
| **Git Remote** | `https://github.com/PeterLemon/RaspberryPi.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 69 malicious artifacts.

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
| Total Artifacts | 959 |
| Analyzed Artifacts (Scanned) | 333 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 626 |
| Total LOC | 72600 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 34.7% |
| Dominant Lang | BINARY_THREAT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ASSEMBLY | 259 | 72531 | 77.8% |
| BINARY_THREAT | 69 | 69 | 20.7% |
| MARKDOWN | 4 | 0 | 1.2% |
| PLAINTEXT | 1 | 0 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.998`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 259 | 77.8% |
| Unknown | 69 | 20.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 1.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 626*

**Composition by Extension & Reason:**
- `.inc`: 341x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.img`: 255x Excluded (Unsupported Extension: '.img')
- `.gb`: 13x Excluded (Unsupported Extension: '.gb')
- `.asm`: 8x Excluded (Embedded Array/Matrix Payload: 5323 commas in 957 LOC)
- `.lz`: 3x Excluded (Unsupported Extension: '.lz')
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.huff`: 2x Excluded (Unsupported Extension: '.huff')
- `.bmp`: 1x Excluded (Explicitly Denied Extension: '.bmp')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 40.5 | 9.6 | 6.8 | 0.0 |
| Error & Exception Exposure | 0.0 | 77.2 | 47.0 | 53.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 98.6 | 16.3 | 14.5 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.8 | 2.4 | 0.0 |
| API Exposure | 0.0 | 2.3 | 0.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 98.3 | 26.6 | 15.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 51.3 | 3.8 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 79.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 40.0 | 15.5 | 13.2 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `SMP/SMPINIT/kernel7.asm` (Hits: 4)
- `SMP/SMPINIT/kernel8.asm` (Hits: 4)
- `Compress/HUFFMAN/HUFFMANDecode/kernel.asm` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **MEM.INC** (`EMU/GameBoy/MEM.INC`) — 1 inbound connections
2. **kernel.asm** (`Compress/HUFFMAN/HUFFMANDecode/kernel.asm`) — 0 inbound connections
3. **kernel7.asm** (`Compress/HUFFMAN/HUFFMANDecode/kernel7.asm`) — 0 inbound connections
4. **kernel8.asm** (`Compress/HUFFMAN/HUFFMANDecode/kernel8.asm`) — 0 inbound connections
5. **kernel.asm** (`Compress/HUFFMAN/HUFFMANGFX/kernel.asm`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **kernel.asm** (`EMU/GameBoy/kernel.asm`) — 6 outbound dependencies
2. **kernel.asm** (`V3D/ControlList/Clear_Color/kernel.asm`) — 4 outbound dependencies
3. **kernel7.asm** (`V3D/ControlList/Clear_Color/kernel7.asm`) — 4 outbound dependencies
4. **kernel.asm** (`V3D/ControlList/Multi_Sample/kernel.asm`) — 4 outbound dependencies
5. **kernel7.asm** (`V3D/ControlList/Multi_Sample/kernel7.asm`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `FB_Init` (@ `V3D/V3DINIT/kernel8.asm`) -> Impact: **115.0** | LOC: 2243
- `FB_Init` (@ `V3D/V3DINIT/kernel.asm`) -> Impact: **108.1** | LOC: 2105
- `FB_Init` (@ `V3D/V3DINIT/kernel7.asm`) -> Impact: **108.1** | LOC: 2105
- `FB_Init` (@ `TagsChannel/kernel8.asm`) -> Impact: **22.3** | LOC: 389
- `FB_Init` (@ `TagsChannel/kernel.asm`) -> Impact: **17.0** | LOC: 284
- `FB_Init` (@ `TagsChannel/kernel7.asm`) -> Impact: **17.0** | LOC: 284
- `InputClock` (@ `Input/SNES/Mouse/GFXDemo/kernel8.asm`) -> Impact: **13.2** | LOC: 38
- `LoopInputData` (@ `Input/SNES/Mouse/GFXDemo/kernel7.asm`) -> Impact: **12.0** | LOC: 43
- `InputClock` (@ `Input/SNES/Mouse/TextDemo/kernel8.asm`) -> Impact: **11.8** | LOC: 38
- `FB_Init` (@ `SMP/SMPINIT/kernel8.asm`) -> Impact: **11.4** | LOC: 86

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `Input/SNES/Controller/GFXDemo` | 25 | 11339.12 | 0.92% | 3.68% |
| `Input/NES/Controller/GFXDemo` | 17 | 7251.0 | 1.49% | 7.68% |
| `Input/SNES/Mouse/GFXDemo` | 8 | 2786.42 | 3.63% | 14.92% |
| `EMU/GameBoy` | 6 | 2528.36 | 4.94% | 16.28% |
| `TagsChannel` | 3 | 746.82 | 5.42% | 44.67% |
| `V3D/V3DINIT` | 3 | 597.7 | 5.12% | 11.51% |
| `Sound/PWM/13Bit/44100Hz/Stereo/DMA` | 4 | 560.8 | 12.65% | 0.0% |
| `Sound/PWM/12Bit/44100Hz/Mono/DMA` | 4 | 559.72 | 12.9% | 0.0% |
| `Sound/PWM/12Bit/44100Hz/Stereo/DMA` | 4 | 559.72 | 12.9% | 0.0% |
| `Sound/PWM/12Bit/48000Hz/Mono/DMA` | 4 | 559.72 | 12.9% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Input/NES/Controller/TextDemo/kernel8.asm` -> **98.6183%** Exposure
- `Input/SNES/Controller/TextDemo/kernel8.asm` -> **98.6183%** Exposure
- `EMU/GameBoy/kernel.asm` -> **97.7023%** Exposure
- `SMP/SMPINIT/kernel8.asm` -> **96.8512%** Exposure
- `SMP/SMPINIT/kernel7.asm` -> **96.763%** Exposure
### Highest State Flux (Mutation/Volatility)
- `Sound/PWM/12Bit/44100Hz/Mono/CPU/kernel7.asm` -> **98.2941%** Exposure
- `Sound/PWM/12Bit/48000Hz/Mono/CPU/kernel7.asm` -> **98.2941%** Exposure
- `Sound/PWM/8BIT/44100Hz/Mono/CPU/kernel7.asm` -> **98.2941%** Exposure
- `Sound/PWM/8BIT/48000Hz/Mono/CPU/kernel7.asm` -> **98.2941%** Exposure
- `Sound/PWM/13Bit/44100Hz/Mono/CPU/kernel7.asm` -> **98.016%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `TagsChannel/kernel8.asm` -> **5** Orphaned Functions | **10** Duplicates
- `Input/NES/Controller/TextDemo/kernel8.asm` -> **11** Orphaned Functions | **0** Duplicates
- `Input/SNES/Controller/TextDemo/kernel8.asm` -> **11** Orphaned Functions | **0** Duplicates
- `Input/SNES/Mouse/TextDemo/kernel8.asm` -> **11** Orphaned Functions | **0** Duplicates
- `TagsChannel/kernel.asm` -> **5** Orphaned Functions | **6** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`Compress/RaspiLogo24BPP.bin`** -> AI Confidence: **98.84%**
2. **`EMU/GameBoy/DMG_ROM.bin`** -> AI Confidence: **98.84%**
3. **`Input/NES/Controller/GFXDemo/BG.bin`** -> AI Confidence: **98.84%**
4. **`Input/NES/Controller/GFXDemo/ButtonA.bin`** -> AI Confidence: **98.84%**
5. **`Input/NES/Controller/GFXDemo/ButtonAPress.bin`** -> AI Confidence: **98.84%**
6. **`Input/NES/Controller/GFXDemo/ButtonB.bin`** -> AI Confidence: **98.84%**
7. **`Input/NES/Controller/GFXDemo/ButtonBPress.bin`** -> AI Confidence: **98.84%**
8. **`Input/NES/Controller/GFXDemo/ButtonSelect.bin`** -> AI Confidence: **98.84%**
9. **`Input/NES/Controller/GFXDemo/ButtonSelectPress.bin`** -> AI Confidence: **98.84%**
10. **`Input/NES/Controller/GFXDemo/ButtonStart.bin`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `14` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `668` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `Input/NES/Controller/TextDemo/kernel8.asm` (ASSEMBLY) -> Cumulative Risk: **390.85**
- **Archetype:** `file_cluster_8` (Distance: 10.781 IQR)
- **Magnitude:** 61.02 | **LOC:** 239 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (98.6183%), Verification (80.0%), Safety Score (57.2252%)
- **Heaviest Functions:** `.DelayLoop` (Impact: 5.5), `InputClock` (Impact: 5.5), `.DrawHEXCharB` (Impact: 5.3)

### 2. `Input/SNES/Controller/TextDemo/kernel8.asm` (ASSEMBLY) -> Cumulative Risk: **390.85**
- **Archetype:** `file_cluster_8` (Distance: 10.781 IQR)
- **Magnitude:** 61.02 | **LOC:** 239 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (98.6183%), Verification (80.0%), Safety Score (57.2252%)
- **Heaviest Functions:** `.DelayLoop` (Impact: 5.5), `InputClock` (Impact: 5.5), `.DrawHEXCharB` (Impact: 5.3)

### 3. `Input/SNES/Mouse/TextDemo/kernel.asm` (ASSEMBLY) -> Cumulative Risk: **382.87**
- **Archetype:** `file_cluster_8` (Distance: 10.504 IQR)
- **Magnitude:** 63.48 | **LOC:** 296 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (87.8252%), Verification (80.0%), Safety Score (57.179%)
- **Heaviest Functions:** `LoopInputData` (Impact: 7.8), `.DrawHEXCharB` (Impact: 5.4), `.DrawChar` (Impact: 5.3)

### 4. `Input/SNES/Mouse/TextDemo/kernel7.asm` (ASSEMBLY) -> Cumulative Risk: **380.92**
- **Archetype:** `file_cluster_8` (Distance: 10.488 IQR)
- **Magnitude:** 68.18 | **LOC:** 305 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (86.765%), Verification (80.0%), Safety Score (57.0395%)
- **Heaviest Functions:** `LoopInputData` (Impact: 7.8), `.DelayLoop` (Impact: 6.0), `.DrawHEXCharB` (Impact: 5.4)

### 5. `Input/SNES/Mouse/TextDemo/kernel8.asm` (ASSEMBLY) -> Cumulative Risk: **377.35**
- **Archetype:** `file_cluster_8` (Distance: 10.271 IQR)
- **Magnitude:** 88.44 | **LOC:** 319 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (92.1254%), Verification (80.0%), Safety Score (55.4557%)
- **Heaviest Functions:** `InputClock` (Impact: 11.8), `SkipXPos` (Impact: 6.4), `.DelayLoop` (Impact: 6.1)

### 6. `SMP/SMPINIT/kernel7.asm` (ASSEMBLY) -> Cumulative Risk: **371.9**
- **Archetype:** `file_cluster_8` (Distance: 9.833 IQR)
- **Magnitude:** 70.64 | **LOC:** 471 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (96.763%), Verification (80.0%), Safety Score (53.7743%)
- **Heaviest Functions:** `FB_Init` (Impact: 11.1), `.DrawHEXCharB` (Impact: 6.0), `.DrawChar` (Impact: 5.3)

### 7. `SMP/SMPINIT/kernel8.asm` (ASSEMBLY) -> Cumulative Risk: **368.95**
- **Archetype:** `file_cluster_8` (Distance: 9.592 IQR)
- **Magnitude:** 78.92 | **LOC:** 520 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (96.8512%), Verification (80.0%), Safety Score (53.0443%)
- **Heaviest Functions:** `FB_Init` (Impact: 11.4), `.DrawHEXCharB` (Impact: 5.9), `.DrawChar` (Impact: 5.2)

### 8. `Sound/PWM/12Bit/44100Hz/Mono/CPU/kernel7.asm` (ASSEMBLY) -> Cumulative Risk: **353.95**
- **Archetype:** `file_cluster_8` (Distance: 10.448 IQR)
- **Magnitude:** 22.08 | **LOC:** 60 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.2941%), Safety Score (77.2123%), Cognitive Load (40.54%)
- **Heaviest Functions:** `FIFO_Wait` (Impact: 7.5), `Loop` (Impact: 3.0), `CoreLoop` (Impact: 2.1)

### 9. `Sound/PWM/12Bit/48000Hz/Mono/CPU/kernel7.asm` (ASSEMBLY) -> Cumulative Risk: **353.95**
- **Archetype:** `file_cluster_8` (Distance: 10.448 IQR)
- **Magnitude:** 22.08 | **LOC:** 60 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.2941%), Safety Score (77.2123%), Cognitive Load (40.54%)
- **Heaviest Functions:** `FIFO_Wait` (Impact: 7.5), `Loop` (Impact: 3.0), `CoreLoop` (Impact: 2.1)

### 10. `Sound/PWM/8BIT/44100Hz/Mono/CPU/kernel7.asm` (ASSEMBLY) -> Cumulative Risk: **353.95**
- **Archetype:** `file_cluster_8` (Distance: 10.448 IQR)
- **Magnitude:** 22.08 | **LOC:** 60 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.2941%), Safety Score (77.2123%), Cognitive Load (40.54%)
- **Heaviest Functions:** `FIFO_Wait` (Impact: 7.5), `Loop` (Impact: 3.0), `CoreLoop` (Impact: 2.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `EMU/GameBoy/CPU.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.518 IQR)
- **Top Global Matches:** file_cluster_8: 10.518, file_cluster_7: 11.333, file_cluster_1: 11.453
- **Magnitude:** 1815.74 | **LOC:** 5159 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.2446%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `HEX27` (Impact: 4.8)
  * `DAA_H_FLAG` (Impact: 4.6)
  * `HEX88` (Impact: 4.1)
  * `HEX89` (Impact: 4.1)
  * `HEX8A` (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 517`, `structural_boundaries: 1141`, `args: 4499`, `func_start: 517`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Compress/RaspiLogo24BPP.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `EMU/GameBoy/DMG_ROM.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/GFXDemo/BG.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/GFXDemo/ButtonA.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/GFXDemo/ButtonAPress.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/GFXDemo/ButtonB.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/GFXDemo/ButtonBPress.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/GFXDemo/ButtonSelect.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/GFXDemo/ButtonSelectPress.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/GFXDemo/ButtonStart.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/GFXDemo/ButtonStartPress.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/GFXDemo/Direction.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/GFXDemo/DirectionDownPress.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/GFXDemo/DirectionLeftPress.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/GFXDemo/DirectionRightPress.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/GFXDemo/DirectionUpPress.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/SNES/Controller/GFXDemo/BG.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/SNES/Controller/GFXDemo/ButtonA.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/SNES/Controller/GFXDemo/ButtonAPress.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/SNES/Controller/GFXDemo/ButtonB.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/SNES/Controller/GFXDemo/ButtonBPress.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/SNES/Controller/GFXDemo/ButtonL.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/SNES/Controller/GFXDemo/ButtonLPress.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/SNES/Controller/GFXDemo/ButtonR.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `V3D/ControlList/Multi_Sample/kernel.asm` (ASSEMBLY) | Magnitude: 39.92 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 123, args: 47, func_start: 18, structural_boundaries: 17
- `V3D/ControlList/Multi_Sample/kernel7.asm` (ASSEMBLY) | Magnitude: 42.12 | Delta: **0.177 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 124, args: 49, func_start: 19, structural_boundaries: 17
- `V3D/ControlList/Refresh/kernel.asm` (ASSEMBLY) | Magnitude: 43.24 | Delta: **0.233 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 153, args: 78, structural_boundaries: 30, pointers: 22
- `V3D/ControlList/Refresh/kernel7.asm` (ASSEMBLY) | Magnitude: 45.44 | Delta: **0.241 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 154, args: 80, structural_boundaries: 30, pointers: 22
- `V3D/ControlList/Multi_Sample/kernel8.asm` (ASSEMBLY) | Magnitude: 41.16 | Delta: **0.258 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 125, args: 59, structural_boundaries: 21, func_start: 19

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `EMU/GameBoy/MEM.INC` -> **Severity: 125.671** (Blast Radius: 5.541 * Doc Risk: 22.6802%)
- `Sound/PWM/12Bit/44100Hz/Mono/CPU/kernel.asm` -> **Severity: 119.847** (Blast Radius: 2.995 * Doc Risk: 40.0156%)
- `Sound/PWM/12Bit/48000Hz/Mono/CPU/kernel.asm` -> **Severity: 119.847** (Blast Radius: 2.995 * Doc Risk: 40.0156%)
- `Sound/PWM/8BIT/44100Hz/Mono/CPU/kernel.asm` -> **Severity: 119.847** (Blast Radius: 2.995 * Doc Risk: 40.0156%)
- `Sound/PWM/8BIT/48000Hz/Mono/CPU/kernel.asm` -> **Severity: 119.847** (Blast Radius: 2.995 * Doc Risk: 40.0156%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
