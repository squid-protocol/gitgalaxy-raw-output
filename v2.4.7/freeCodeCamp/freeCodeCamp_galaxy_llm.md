# ARCHITECTURAL_BRIEF: freeCodeCamp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/freeCodeCamp` |
| **Timestamp** | `2026-08-07T04:24:27.150206+00:00` |
| **Scan Duration** | `22.19s` |
| **Git Branch** | `main` |
| **Git Commit** | `a72fe073991cf3c824da02a4ff2e991ac8b0a4a8` |
| **Git Remote** | `https://github.com/freeCodeCamp/freeCodeCamp.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 957 malicious artifacts.

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
| Total Artifacts | 18528 |
| Analyzed Artifacts (Scanned) | 16402 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2126 |
| Total LOC | 175617 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 88.5% |
| Dominant Lang | MARKDOWN |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2185 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 74 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 14218 | 0 | 86.7% |
| JSON | 1077 | 72825 | 6.6% |
| TYPESCRIPT | 777 | 68212 | 4.7% |
| JAVASCRIPT | 176 | 25024 | 1.1% |
| CSS | 86 | 7618 | 0.5% |
| YAML | 35 | 815 | 0.2% |
| PLAINTEXT | 18 | 1 | 0.1% |
| XML | 10 | 1006 | 0.1% |
| DOCKERFILE | 2 | 98 | 0.0% |
| SHELL | 2 | 15 | 0.0% |
| HTML | 1 | 3 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.17`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1845 | 11.2% |
| file_cluster_13 | 234 | 1.4% |
| file_cluster_2 | 34 | 0.2% |
| file_cluster_4 | 19 | 0.1% |
| file_cluster_17 | 12 | 0.1% |
| file_cluster_16 | 6 | 0.0% |
| file_cluster_0 | 3 | 0.0% |
| file_cluster_1 | 2 | 0.0% |
| file_cluster_11 | 1 | 0.0% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 14235 | 86.8% |
| Static: Minified & Vendor Opaque Mass | 10 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2126*

**Composition by Extension & Reason:**
- `.md`: 1704x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Machine-Generated Source Code Signature: 53 LOC), 2x Excluded (Machine-Generated Source Code Signature: 82 LOC)
- `.ts`: 122x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.json`: 74x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 11x Excluded (Static Asset Blob without Intent: 1531 LOC), 5x Excluded (Massive Static Asset Blob: 10022 LOC)
- `.tsx`: 8x Excluded (Saturation: Line 13 exceeds 500 chars), 7x Excluded (Saturation: Line 18 exceeds 500 chars), 3x Excluded (Saturation: Line 16 exceeds 500 chars)
- `.yml`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.woff`: 23x Excluded (Explicitly Denied Extension: '.woff')
- `.snap`: 17x Unsupported Format (.snap), 1x Excluded (Saturation: Line 6 exceeds 500 chars), 1x Excluded (Saturation: Line 59 exceeds 500 chars)
- `no_extension`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 14x Excluded (Explicitly Denied Extension: '.png')
- `.mjs`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.woff2`: 5x Excluded (Explicitly Denied Extension: '.woff2')
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 31800 LOC exceeds safe regex boundaries)
- `.prisma`: 3x Excluded (Unsupported Extension: '.prisma')
- `.css`: 1x Excluded (Saturation: Line 74 exceeds 500 chars), 1x Excluded (Saturation: Line 28 exceeds 500 chars)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 8.4 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.4 | 6.8 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 7.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 2.5 | 2.0 | 2.3 |
| API Exposure | 0.0 | 19.6 | 1.8 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 8.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 80.2 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 89.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.9 | 0.5 | 0.4 | 0.4 |
| Volatility Exposure | 0.0 | 87.1 | 10.0 | 12.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 46.0 | 41.3 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tools/scripts/seed/user-data.js` (Hits: 111)
- `client/src/assets/icons/top-contributor-badge-emblem.tsx` (Hits: 80)
- `client/src/components/formHelpers/form-validators.test.ts` (Hits: 48)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **react.json** (`curriculum/structure/blocks/react.json`) — 343 inbound connections
2. **react-i18next.js** (`client/__mocks__/react-i18next.js`) — 186 inbound connections
3. **prop-types.ts** (`client/src/redux/prop-types.ts`) — 92 inbound connections
4. **css.tsx** (`client/src/assets/icons/css.tsx`) — 85 inbound connections
5. **redux.json** (`curriculum/structure/blocks/redux.json`) — 59 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **schemas.ts** (`api/src/schemas.ts`) — 47 outbound dependencies
2. **show.tsx** (`client/src/templates/Challenges/classic/show.tsx`) — 46 outbound dependencies
3. **default.tsx** (`client/src/components/layouts/default.tsx`) — 39 outbound dependencies
4. **show.tsx** (`client/src/templates/Challenges/codeally/show.tsx`) — 36 outbound dependencies
5. **show.tsx** (`client/src/templates/Challenges/generic/show.tsx`) — 35 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `FastifyPluginCallbackTypebox` (@ `api/src/routes/protected/challenge.ts`) -> Impact: **236.1** | LOC: 922
  * *Intent:* /**
- `DesktopLayout` (@ `client/src/templates/Challenges/classic/desktop-layout.tsx`) -> Impact: **178.4** | LOC: 304
- `FastifyPluginCallbackTypebox` (@ `api/src/routes/protected/settings.ts`) -> Impact: **177.3** | LOC: 626
- `describe` (@ `api/src/exam-environment/routes/exam-environment.test.ts`) -> Impact: **136.9** | LOC: 1388
- `FastifyPluginCallbackTypebox` (@ `api/src/routes/protected/user.ts`) -> Impact: **131.2** | LOC: 504
- `ExperienceSettings` (@ `client/src/components/profile/components/experience.tsx`) -> Impact: **125.0** | LOC: 379
- `describe` (@ `api/src/exam-environment/routes/exam-environment.test.ts`) -> Impact: **109.9** | LOC: 1194
- `PortfolioSettings` (@ `client/src/components/profile/components/portfolio.tsx`) -> Impact: **100.0** | LOC: 319
- `ShowCertification` (@ `client/src/client-only-routes/show-certification.tsx`) -> Impact: **86.3** | LOC: 295
- `describe` (@ `api/src/plugins/auth0.test.ts`) -> Impact: **74.1** | LOC: 374

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `curriculum/structure/blocks` | 903 | 14738.48 | 5.73% | 0.0% |
| `__monolith__` | 10 | 5094.12 | 5.54% | 0.0% |
| `curriculum/structure/superblocks` | 94 | 1412.9 | 5.97% | 0.0% |
| `curriculum/challenges/english/blocks/learn-basic-string-and-array-methods-by-building-a-music-player` | 99 | 1409.68 | 0.0% | 0.0% |
| `client/src/templates/Challenges/redux` | 12 | 839.24 | 11.52% | 19.87% |
| `curriculum/challenges/english/blocks/learn-basic-javascript-by-building-a-role-playing-game` | 173 | 836.44 | 0.0% | 0.0% |
| `curriculum/challenges/english/blocks/learn-intermediate-oop-by-building-a-platformer-game` | 117 | 709.7 | 0.0% | 0.0% |
| `packages/challenge-builder/src` | 9 | 688.12 | 34.85% | 37.33% |
| `curriculum/challenges/english/blocks/workshop-music-player` | 46 | 665.74 | 0.0% | 0.0% |
| `curriculum/challenges/english/blocks/learn-css-variables-by-building-a-city-skyline` | 118 | 601.1 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `api/src/exam-environment/utils/exam-environment.ts` -> **100.0%** Exposure
- `api/src/plugins/redirect-with-message.ts` -> **100.0%** Exposure
- `api/src/routes/helpers/is-restricted.ts` -> **100.0%** Exposure
- `client/src/templates/Challenges/components/preview.tsx` -> **100.0%** Exposure
- `client/src/templates/Challenges/components/scene/scene.tsx` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `curriculum/src/test/utils/challenge-titles.js` -> **100.0%** Exposure
- `curriculum/src/test/utils/mongo-ids.js` -> **100.0%** Exposure
- `curriculum/src/test/utils/pseudo-worker.js` -> **100.0%** Exposure
- `packages/challenge-builder/src/worker-executor.js` -> **100.0%** Exposure
- `tools/challenge-parser/parser/plugins/table-and-strikethrough.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `api/src/exam-environment/routes/exam-environment.test.ts` -> **0** Orphaned Functions | **113** Duplicates
- `api/src/routes/protected/user.test.ts` -> **1** Orphaned Functions | **65** Duplicates
- `api/src/routes/protected/challenge.test.ts` -> **0** Orphaned Functions | **65** Duplicates
- `client/src/templates/Challenges/components/pinyin-to-hanzi-input.test.tsx` -> **0** Orphaned Functions | **56** Duplicates
- `client/src/templates/Challenges/components/speaking-modal-helpers.test.ts` -> **0** Orphaned Functions | **56** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`tools/challenge-parser/parser/plugins/add-video-question.js`** -> AI Confidence: **99.39%**
2. **`tools/challenge-parser/parser/plugins/add-text.js`** -> AI Confidence: **99.34%**
3. **`client/src/templates/Challenges/redux/create-question-epic.js`** -> AI Confidence: **99.31%**
4. **`tools/challenge-parser/parser/index.js`** -> AI Confidence: **99.31%**
5. **`tools/challenge-parser/parser/plugins/add-fill-in-the-blank.js`** -> AI Confidence: **99.31%**
6. **`tools/challenge-parser/parser/plugins/add-solution.js`** -> AI Confidence: **99.31%**
7. **`client/src/components/Intro/index.tsx`** -> AI Confidence: **99.31%**
8. **`client/src/components/daily-coding-challenge/calendar-day.tsx`** -> AI Confidence: **99.31%**
9. **`client/src/templates/Challenges/classic/desktop-layout.tsx`** -> AI Confidence: **99.31%**
10. **`client/src/templates/Challenges/classic/mobile-layout.tsx`** -> AI Confidence: **99.31%**
11. **`client/src/templates/Challenges/exam-download/show.tsx`** -> AI Confidence: **99.31%**
12. **`client/src/templates/Introduction/components/block-header.tsx`** -> AI Confidence: **99.31%**
13. **`curriculum/src/file-handler.ts`** -> AI Confidence: **99.31%**
14. **`tools/challenge-helper-scripts/create-language-block.ts`** -> AI Confidence: **99.31%**
15. **`tools/challenge-helper-scripts/create-project.ts`** -> AI Confidence: **99.31%**
16. **`client/utils/gatsby/path-prefix.js`** -> AI Confidence: **99.29%**
17. **`tools/client-plugins/gatsby-source-challenges/create-challenge-nodes.js`** -> AI Confidence: **99.29%**
18. **`client/src/components/profile/components/utils/certification.ts`** -> AI Confidence: **99.29%**
19. **`client/tools/read-env.ts`** -> AI Confidence: **99.29%**
20. **`client/src/redux/donation-saga.js`** -> AI Confidence: **99.24%**
21. **`client/src/templates/Challenges/redux/completion-epic.js`** -> AI Confidence: **99.24%**
22. **`tools/scripts/seed-exams/create-exams.js`** -> AI Confidence: **99.24%**
23. **`api/src/routes/protected/challenge.ts`** -> AI Confidence: **99.24%**
24. **`api/src/routes/public/user.ts`** -> AI Confidence: **99.24%**
25. **`client/src/client-only-routes/show-certification.tsx`** -> AI Confidence: **99.24%**
26. **`client/src/client-only-routes/show-daily-coding-challenge.tsx`** -> AI Confidence: **99.24%**
27. **`client/src/components/Donation/donate-form.tsx`** -> AI Confidence: **99.24%**
28. **`client/src/components/profile/components/experience.tsx`** -> AI Confidence: **99.24%**
29. **`client/src/components/search/searchBar/search-bar.tsx`** -> AI Confidence: **99.24%**
30. **`client/src/templates/Challenges/classic/action-row.tsx`** -> AI Confidence: **99.24%**
31. **`client/src/templates/Challenges/classic/editor.tsx`** -> AI Confidence: **99.24%**
32. **`client/src/templates/Challenges/classic/lower-jaw.tsx`** -> AI Confidence: **99.24%**
33. **`client/src/templates/Challenges/components/multiple-choice-questions.tsx`** -> AI Confidence: **99.24%**
34. **`client/src/templates/Challenges/components/preview-portal.tsx`** -> AI Confidence: **99.24%**
35. **`client/src/templates/Challenges/components/speaking-modal.tsx`** -> AI Confidence: **99.24%**
36. **`client/src/templates/Challenges/components/tool-panel.tsx`** -> AI Confidence: **99.24%**
37. **`client/src/templates/Challenges/utils/frame.ts`** -> AI Confidence: **99.24%**
38. **`client/src/templates/Introduction/components/super-block-intro.tsx`** -> AI Confidence: **99.24%**
39. **`client/tools/generate-search-placeholder.ts`** -> AI Confidence: **99.24%**
40. **`curriculum/src/build-superblock.ts`** -> AI Confidence: **99.24%**
41. **`tools/challenge-helper-scripts/rename-block.ts`** -> AI Confidence: **99.24%**
42. **`api/src/routes/public/donate.ts`** -> AI Confidence: **99.23%**
43. **`client/src/components/helpers/index.ts`** -> AI Confidence: **99.23%**
44. **`client/src/components/profile/components/bio.tsx`** -> AI Confidence: **99.23%**
45. **`client/src/components/profile/components/social-icons.tsx`** -> AI Confidence: **99.23%**
46. **`client/src/templates/Challenges/components/mobile-app-modal.tsx`** -> AI Confidence: **99.23%**
47. **`client/src/templates/Challenges/components/test-suite.tsx`** -> AI Confidence: **99.23%**
48. **`client/src/templates/Challenges/generic/content-outline.tsx`** -> AI Confidence: **99.23%**
49. **`client/src/redux/selectors.js`** -> AI Confidence: **99.18%**
50. **`api/src/plugins/auth0.test.ts`** -> AI Confidence: **99.18%**
51. **`api/src/plugins/auth0.ts`** -> AI Confidence: **99.18%**
52. **`api/src/routes/protected/settings.test.ts`** -> AI Confidence: **99.18%**
53. **`client/src/client-only-routes/show-profile-or-four-oh-four.tsx`** -> AI Confidence: **99.18%**
54. **`client/src/client-only-routes/show-settings.tsx`** -> AI Confidence: **99.18%**
55. **`client/src/client-only-routes/show-unsubscribed.tsx`** -> AI Confidence: **99.18%**
56. **`client/src/client-only-routes/show-update-email.tsx`** -> AI Confidence: **99.18%**
57. **`client/src/components/Donation/donation-modal.tsx`** -> AI Confidence: **99.18%**
58. **`client/src/components/Footer/index.tsx`** -> AI Confidence: **99.18%**
59. **`client/src/components/Intro/email-sign-up-alert.tsx`** -> AI Confidence: **99.18%**
60. **`client/src/components/Map/index.tsx`** -> AI Confidence: **99.18%**
61. **`client/src/components/daily-coding-challenge/widget.tsx`** -> AI Confidence: **99.18%**
62. **`client/src/components/growth-book/growth-book-redux-connector.tsx`** -> AI Confidence: **99.18%**
63. **`client/src/components/landing/components/landing-top.tsx`** -> AI Confidence: **99.18%**
64. **`client/src/components/landing/components/two-button-cta.tsx`** -> AI Confidence: **99.18%**
65. **`client/src/components/profile/components/about.tsx`** -> AI Confidence: **99.18%**
66. **`client/src/components/profile/components/certifications.tsx`** -> AI Confidence: **99.18%**
67. **`client/src/components/profile/components/experience-display.tsx`** -> AI Confidence: **99.18%**
68. **`client/src/components/profile/components/internet.tsx`** -> AI Confidence: **99.18%**
69. **`client/src/components/search/with-instant-search.tsx`** -> AI Confidence: **99.18%**
70. **`client/src/components/settings/certification.tsx`** -> AI Confidence: **99.18%**
71. **`client/src/pages/donate.tsx`** -> AI Confidence: **99.18%**
72. **`client/src/pages/email-sign-up.tsx`** -> AI Confidence: **99.18%**
73. **`client/src/pages/learn.tsx`** -> AI Confidence: **99.18%**
74. **`client/src/pages/supporters.tsx`** -> AI Confidence: **99.18%**
75. **`client/src/redux/create-store.ts`** -> AI Confidence: **99.18%**
76. **`client/src/templates/Challenges/classic/editor-tabs.tsx`** -> AI Confidence: **99.18%**
77. **`client/src/templates/Challenges/classic/show.tsx`** -> AI Confidence: **99.18%**
78. **`client/src/templates/Challenges/classic/xterm.tsx`** -> AI Confidence: **99.18%**
79. **`client/src/templates/Challenges/components/help-modal.tsx`** -> AI Confidence: **99.18%**
80. **`client/src/templates/Challenges/components/hotkeys.tsx`** -> AI Confidence: **99.18%**
81. **`client/src/templates/Challenges/components/side-panel.tsx`** -> AI Confidence: **99.18%**
82. **`client/src/templates/Challenges/ms-trophy/link-ms-user.tsx`** -> AI Confidence: **99.18%**
83. **`client/src/templates/Challenges/projects/tool-panel.tsx`** -> AI Confidence: **99.18%**
84. **`client/src/templates/Challenges/quiz/show.tsx`** -> AI Confidence: **99.18%**
85. **`tools/challenge-helper-scripts/create-next-task.ts`** -> AI Confidence: **99.18%**
86. **`tools/challenge-helper-scripts/delete-task.ts`** -> AI Confidence: **99.18%**
87. **`tools/challenge-parser/parser/plugins/add-hooks.js`** -> AI Confidence: **99.17%**
88. **`tools/challenge-parser/parser/plugins/utils/get-file-visitor.js`** -> AI Confidence: **99.17%**
89. **`client/src/components/formHelpers/form-ip-utils.ts`** -> AI Confidence: **99.17%**
90. **`client/src/templates/Challenges/components/pinyin-to-hanzi-input.tsx`** -> AI Confidence: **99.17%**
91. **`client/tools/create-env.ts`** -> AI Confidence: **99.17%**
92. **`tools/scripts/test_challenges.sh`** -> AI Confidence: **99.17%**
93. **`client/src/templates/Challenges/redux/code-storage-epic.js`** -> AI Confidence: **99.16%**
94. **`client/src/templates/Challenges/redux/execute-challenge-saga.js`** -> AI Confidence: **99.16%**
95. **`curriculum/src/test/test-challenges.js`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `87` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2369` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/challenge-builder/src/worker-executor.js` (JAVASCRIPT) -> Cumulative Risk: **642.27**
- **Archetype:** `file_cluster_4` (Distance: 13.459 IQR)
- **Magnitude:** 240.56 | **LOC:** 150 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.6676%)
- **Heaviest Functions:** `getWorker` (Impact: 15.8), `eventify` (Impact: 12.4), `execute` (Impact: 9.2)

### 2. `packages/challenge-builder/src/typescript-worker-handler.ts` (TYPESCRIPT) -> Cumulative Risk: **634.08**
- **Archetype:** `file_cluster_4` (Distance: 9.845 IQR)
- **Magnitude:** 6.15 | **LOC:** 46 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9977%), Tech Debt (99.9976%)
- **Heaviest Functions:** `compileTypeScriptCode` (Impact: 10.8), `onMessage` (Impact: 10.6), `setupTSCompiler` (Impact: 8.6)

### 3. `client/src/templates/Challenges/components/scene/scene.tsx` (TYPESCRIPT) -> Cumulative Risk: **612.53**
- **Archetype:** `file_cluster_13` (Distance: 12.014 IQR)
- **Magnitude:** 17.66 | **LOC:** 449 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (81.6846%)
- **Heaviest Functions:** `setCharacters` (Impact: 23.1), `useEffect` (Impact: 19.1), `pauseAnimation` (Impact: 15.7)

### 4. `client/src/components/Progress/progress-inner.tsx` (TYPESCRIPT) -> Cumulative Risk: **578.33**
- **Archetype:** `file_cluster_2` (Distance: 10.277 IQR)
- **Magnitude:** 7.92 | **LOC:** 135 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9827%), Concurrency (94.0836%), Verification (80.0%)
- **Heaviest Functions:** `animateProgressInner` (Impact: 15.6), `clearInterval` (Impact: 9.8), `setShownPercent` (Impact: 8.4)

### 5. `curriculum/src/build-superblock.ts` (TYPESCRIPT) -> Cumulative Risk: **537.95**
- **Archetype:** `file_cluster_4` (Distance: 11.961 IQR)
- **Magnitude:** 24.51 | **LOC:** 528 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9982%), Concurrency (99.7319%), State Flux (80.1236%)
- **Heaviest Functions:** `addMetaToChallenge` (Impact: 20.7), `createValidator` (Impact: 12.6), `log` (Impact: 12.1)

### 6. `tools/client-plugins/browser-scripts/modules/typescript-compiler.ts` (TYPESCRIPT) -> Cumulative Risk: **536.15**
- **Archetype:** `file_cluster_4` (Distance: 13.705 IQR)
- **Magnitude:** 3.07 | **LOC:** 112 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9825%), Concurrency (99.8982%), Safety Score (81.9112%)
- **Heaviest Functions:** `setup` (Impact: 4.0), `constructor` (Impact: 1.9)

### 7. `client/src/components/profile/components/username.tsx` (TYPESCRIPT) -> Cumulative Risk: **499.64**
- **Archetype:** `file_cluster_13` (Distance: 11.503 IQR)
- **Magnitude:** 15.13 | **LOC:** 245 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (86.9816%), Safety Score (83.9727%)
- **Heaviest Functions:** `renderAlerts` (Impact: 28.4), `render` (Impact: 10.5), `handleChange` (Impact: 7.9)

### 8. `client/src/utils/ajax.ts` (TYPESCRIPT) -> Cumulative Risk: **498.74**
- **Archetype:** `file_cluster_16` (Distance: 11.434 IQR)
- **Magnitude:** 22.59 | **LOC:** 520 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9981%), Concurrency (99.8032%)
- **Heaviest Functions:** `parseApiResponseToClientUser` (Impact: 14.7), `getCSRFToken` (Impact: 7.2), `get` (Impact: 4.1)

### 9. `e2e/utils/email.ts` (TYPESCRIPT) -> Cumulative Risk: **497.35**
- **Archetype:** `file_cluster_8` (Distance: 9.193 IQR)
- **Magnitude:** 1.99 | **LOC:** 34 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9996%), Concurrency (99.9993%)
- **Heaviest Functions:** `getAllEmails` (Impact: 2.2), `deleteAllEmails` (Impact: 2.0), `getFirstEmail` (Impact: 1.1)

### 10. `client/src/components/sidebar-panel/use-active-heading.ts` (TYPESCRIPT) -> Cumulative Risk: **485.25**
- **Archetype:** `file_cluster_2` (Distance: 10.999 IQR)
- **Magnitude:** 7.77 | **LOC:** 63 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9938%), Verification (80.0%), Safety Score (58.2836%)
- **Heaviest Functions:** `useActiveHeading` (Impact: 25.0), `useEffect` (Impact: 20.5), `update` (Impact: 18.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `curriculum/src/test/test-challenges.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.334 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.088 IQR)
- **Top Global Matches:** file_cluster_4: 11.334, file_cluster_13: 11.593, file_cluster_0: 11.765
- **Magnitude:** 452.36 | **LOC:** 529 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 87.5%
- **Risk Profile:** Cognitive Load (42.6774%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getChallenges` (Impact: 64.4)
  * `describe` (Impact: 63.6)
  * `describe` (Impact: 57.7)
    * *Intent:* // We have to dynamically import this because otherwise it will not be mocked. // Presumably this is...
  * `describe` (Impact: 37.5)
    * *Intent:* // We have to dynamically import this because otherwise it will not be mocked. // Presumably this is...
  * `describe` (Impact: 29.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 95`, `args: 42`, `func_start: 39`
* *Risk/State:* `state_mutation: 18`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 21`
* *Architecture:* `io: 1`, `api: 6`, `concurrency: 63`, `import: 20`
* *Defense:* `safety: 22`, `doc: 1`, `test: 26`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` file-handler.js, curriculum-schema.js, sort-challenges.js, vitest, pseudo-worker.js, lodash, get-lines, jsdom...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/challenge-builder/src/worker-executor.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.88 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 7.312 IQR)
- **Top Global Matches:** file_cluster_4: 11.88, file_cluster_8: 12.211, file_cluster_1: 12.403
- **Magnitude:** 259.88 | **LOC:** 250 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.8573%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `it` (Impact: 12.3)
  * `mockWorker` (Impact: 12.0)
  * `postMessage` (Impact: 9.4)
  * `setImmediate` (Impact: 9.3)
  * `setImmediate` (Impact: 7.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 35`, `args: 23`, `func_start: 66`
* *Risk/State:* `state_mutation: 45`, `duplicate_logic: 29`
* *Architecture:* `concurrency: 105`, `import: 2`
* *Defense:* `doc: 1`, `test: 60`, `immutability_locks: 48`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, worker-executor
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/challenge-builder/src/worker-executor.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.459 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.811 IQR)
- **Top Global Matches:** file_cluster_4: 13.459, file_cluster_11: 14.006, file_cluster_8: 14.009
- **Magnitude:** 240.56 | **LOC:** 150 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (99.371%), Tech Debt (99.6676%)
**Top Internal Functions/Classes:**
  * `getWorker` (Impact: 15.8)
  * `eventify` (Impact: 12.4)
    * *Intent:* // Error and completion handling
  * `execute` (Impact: 9.2)
  * `_execute` (Impact: 8.6)
  * `onmessage` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 30`, `args: 24`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 87`, `duplicate_logic: 4`
* *Architecture:* `api: 3`, `concurrency: 43`
* *Defense:* `safety: 10`, `immutability_locks: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.139
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `curriculum/src/test/utils/pseudo-worker.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.791 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.534 IQR)
- **Top Global Matches:** file_cluster_4: 11.791, file_cluster_8: 12.758, file_cluster_17: 13.021
- **Magnitude:** 196.12 | **LOC:** 94 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createPseudoWorker` (Impact: 28.8)
  * `listenToWorker` (Impact: 16.5)
  * `postMessage` (Impact: 9.9)
  * `produce` (Impact: 6.4)
  * `send` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 20`, `args: 16`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 31`
* *Architecture:* `io: 4`, `api: 2`, `concurrency: 91`
* *Defense:* `safety: 4`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `curriculum/src/build-superblock.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.23 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.307 IQR)
- **Top Global Matches:** file_cluster_8: 8.23, file_cluster_7: 9.19, file_cluster_1: 9.351
- **Magnitude:** 194.1 | **LOC:** 589 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (2.9147%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 36.2)
  * `describe` (Impact: 20.9)
  * `describe` (Impact: 8.2)
  * `test` (Impact: 6.2)
  * `describe` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 60`, `args: 52`, `func_start: 81`
* *Risk/State:* `safety_bypasses: 10`, `duplicate_logic: 46`
* *Architecture:* `io: 1`, `concurrency: 3`, `import: 3`
* *Defense:* `safety: 2`, `test: 85`, `immutability_locks: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` build-superblock.js, vitest, polyvinyl
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/src/templates/Challenges/redux/completion-epic.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.418 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.317 IQR)
- **Top Global Matches:** file_cluster_8: 10.418, file_cluster_13: 10.526, file_cluster_17: 10.974
- **Magnitude:** 183.0 | **LOC:** 329 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (15.7892%), Tech Debt (70.3093%)
**Top Internal Functions/Classes:**
  * `completionEpic` (Impact: 35.3)
  * `submitModern` (Impact: 19.8)
  * `postChallenge` (Impact: 16.7)
  * `canAllowDonationRequest` (Impact: 14.6)
  * `tap` (Impact: 11.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 53`, `args: 18`, `func_start: 29`
* *Risk/State:* `state_mutation: 22`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `import: 18`
* *Defense:* `safety: 15`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.115
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` selectors, gatsby, redux-observable, action-types, post-update, challenge-request-helpers, actions, challenge-types...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `docker/devcontainer/Dockerfile` (DOCKERFILE | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.636 IQR)
- **Top Global Matches:** file_cluster_13: 15.636, file_cluster_17: 15.641, file_cluster_0: 15.757
- **Magnitude:** 167.16 | **LOC:** 97 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (37.3498%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 6`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `state_mutation: 7`, `dead_code: 2`
* *Architecture:* `io: 30`, `import: 4`
* *Defense:* `safety: 25`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` base, builder, node:24-bookworm
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/challenge-builder/src/transformers.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.358 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.451 IQR)
- **Top Global Matches:** file_cluster_8: 10.358, file_cluster_17: 10.66, file_cluster_13: 10.682
- **Magnitude:** 156.6 | **LOC:** 418 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (27.3648%), Tech Debt (98.9303%)
**Top Internal Functions/Classes:**
  * `embedFilesInHtml` (Impact: 51.5)
  * `embedStylesAndScript` (Impact: 39.3)
  * `embedScript` (Impact: 8.3)
  * `embedScript` (Impact: 4.5)
  * `embedScript` (Impact: 4.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 44`, `args: 24`, `func_start: 23`
* *Risk/State:* `high_risk_execution: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 9`, `concurrency: 9`, `import: 6`
* *Defense:* `safety: 19`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.108
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` package.json, typescript-worker-handler, polyvinyl, loop-protect, lodash-es, worker-executor
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `client/src/templates/Challenges/redux/code-storage-epic.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.019 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.1 IQR)
- **Top Global Matches:** file_cluster_17: 11.019, file_cluster_13: 11.175, file_cluster_8: 11.39
- **Magnitude:** 130.86 | **LOC:** 239 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (21.6893%), Tech Debt (94.2839%)
**Top Internal Functions/Classes:**
  * `loadCodeEpic` (Impact: 41.4)
  * `saveCodeEpic` (Impact: 14.3)
  * `map` (Impact: 10.0)
    * *Intent:* // do not save challenge if code is locked
  * `isFilesAllPoly` (Impact: 7.5)
  * `getLegacyCode` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 58`, `args: 25`, `func_start: 19`
* *Risk/State:* `state_mutation: 21`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 1`, `import: 13`
* *Defense:* `safety: 13`, `immutability_locks: 28`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` selectors, redux-observable, polyvinyl, flash-messages, action-types, actions, challenge-types, store...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `api/src/exam-environment/routes/exam-environment.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.725 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.092 IQR)
- **Top Global Matches:** file_cluster_8: 10.725, file_cluster_4: 10.762, file_cluster_7: 11.161
- **Magnitude:** 125.52 | **LOC:** 1470 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.0188%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 136.9)
  * `describe` (Impact: 109.9)
  * `describe` (Impact: 34.2)
  * `describe` (Impact: 28.6)
  * `describe` (Impact: 22.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 244`, `args: 177`, `func_start: 171`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 57`, `planned_debt: 1`, `duplicate_logic: 113`
* *Architecture:* `io: 1`, `concurrency: 442`, `import: 12`
* *Defense:* `safety: 6`, `doc: 27`, `test: 165`, `immutability_locks: 131`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exam-environment-exam.js, type-provider-typebox, exam-environment.js, client, index.js, vitest, env.js, jsonwebtoken...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/src/templates/Challenges/redux/selectors.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.001 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.014 IQR)
- **Top Global Matches:** file_cluster_8: 11.001, file_cluster_13: 11.205, file_cluster_17: 11.277
- **Magnitude:** 121.38 | **LOC:** 197 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.6674%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `challengeDataSelector` (Impact: 37.1)
  * `isModuleNewlyCompletedSelector` (Impact: 14.9)
  * `consoleOutputSelector` (Impact: 9.0)
  * `isBlockNewlyCompletedSelector` (Impact: 3.8)
  * `projectFormValuesSelector` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 104`, `args: 47`, `func_start: 39`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 45`, `import: 6`
* *Defense:* `safety: 27`, `immutability_locks: 59`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` selectors, challenge-types, get-completion-percentage, reselect, action-types, curriculum-data
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/src/templates/Challenges/redux/create-question-epic.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.326 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.816 IQR)
- **Top Global Matches:** file_cluster_8: 9.326, file_cluster_13: 9.613, file_cluster_17: 9.88
- **Magnitude:** 119.86 | **LOC:** 233 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (17.1807%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `insertEditableRegions` (Impact: 28.6)
  * `editableRegionsToMarkdown` (Impact: 24.0)
  * `filesToMarkdown` (Impact: 23.7)
  * `editableRegionStrings` (Impact: 14.7)
  * `linksOrMarkdown` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 40`, `args: 12`, `func_start: 10`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 6`, `test: 4`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.115
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` redux-observable, utils, i18next, actions, challenge-types, env.json, action-types, operators...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `client/src/templates/Challenges/redux/execute-challenge-saga.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.638 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.524 IQR)
- **Top Global Matches:** file_cluster_13: 10.638, file_cluster_17: 10.788, file_cluster_0: 10.925
- **Magnitude:** 114.64 | **LOC:** 408 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 70.0%
- **Risk Profile:** Cognitive Load (12.1709%), Tech Debt (73.7952%)
**Top Internal Functions/Classes:**
  * `executeTests` (Impact: 34.9)
  * `updatePreviewSaga` (Impact: 13.0)
    * *Intent:* // If there's an error building the challenge then throwing it here will // let the user know there'...
  * `previewChallengeSaga` (Impact: 9.7)
  * `executeCancellableChallengeSaga` (Impact: 6.6)
    * *Intent:* // when 'run tests' is clicked, do this first
  * `fireConfetti` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 85`, `args: 19`, `func_start: 20`
* *Risk/State:* `state_mutation: 6`, `dead_code: 2`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 6`, `import: 18`
* *Defense:* `safety: 31`, `immutability_locks: 40`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` redux-saga, action-types, effects, i18next, flash-messages, challenge-request-helpers, build, challenge-types...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `docker/api/Dockerfile` (DOCKERFILE | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.11 IQR)
- **Top Global Matches:** file_cluster_13: 13.11, file_cluster_8: 13.521, file_cluster_11: 13.656
- **Magnitude:** 113.4 | **LOC:** 63 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (28.905%), Tech Debt (86.7036%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 5`, `args: 2`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 1`
* *Architecture:* `io: 20`, `import: 9`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` deps, builder, node:24-bookworm
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `curriculum/src/filter.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.509 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.896 IQR)
- **Top Global Matches:** file_cluster_8: 7.509, file_cluster_7: 8.602, file_cluster_1: 8.738
- **Magnitude:** 89.42 | **LOC:** 269 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (2.6364%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 8.4)
  * `describe` (Impact: 7.7)
  * `describe` (Impact: 5.1)
  * `describe` (Impact: 4.8)
  * `it` (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 21`, `args: 19`, `func_start: 34`
* *Risk/State:* `duplicate_logic: 26`
* *Architecture:* `import: 2`
* *Defense:* `test: 36`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, filter
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/src/redux/selectors.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.796 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.698 IQR)
- **Top Global Matches:** file_cluster_13: 10.796, file_cluster_8: 10.902, file_cluster_17: 11.0
- **Magnitude:** 82.56 | **LOC:** 251 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (16.4701%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `shouldRequestDonationSelector` (Impact: 20.0)
  * `renderStartTimeSelector` (Impact: 17.5)
  * `donatableSectionRecentlyCompletedSelecto` (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 69`, `args: 30`, `func_start: 32`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 29`, `import: 7`
* *Defense:* `safety: 8`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` session-storage, curriculum-data, random-between, cert-and-project-map, reselect, certification-settings, action-types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/src/redux/donation-saga.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.799 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.265 IQR)
- **Top Global Matches:** file_cluster_13: 9.799, file_cluster_8: 10.035, file_cluster_0: 10.14
- **Magnitude:** 64.32 | **LOC:** 215 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.9754%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `stripeCardErrorHandler` (Impact: 21.1)
  * `showDonateModalSaga` (Impact: 11.8)
  * `updateCardSaga` (Impact: 7.6)
  * `setDonationCookieIfDonating` (Impact: 3.7)
  * `setDonationCookie` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 47`, `args: 9`, `func_start: 11`
* *Risk/State:* `state_mutation: 1`, `dead_code: 1`
* *Architecture:* `io: 3`, `api: 6`, `concurrency: 2`, `import: 11`
* *Defense:* `safety: 18`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` call-ga, session-storage, effects, i18next, ajax, donation-settings, actions, analytics-strings...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `curriculum/src/test/daily-challenges.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.678 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 6.02 IQR)
- **Top Global Matches:** file_cluster_17: 11.678, file_cluster_8: 11.691, file_cluster_13: 11.806
- **Magnitude:** 62.14 | **LOC:** 85 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.5822%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 21.1)
  * `it` (Impact: 19.3)
  * `it` (Impact: 2.3)
  * `it` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 10`, `args: 7`, `func_start: 4`
* *Risk/State:* `state_mutation: 12`, `duplicate_logic: 3`
* *Architecture:* `concurrency: 4`, `import: 3`
* *Defense:* `safety: 7`, `test: 11`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test-challenges.js, vitest, config.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/protected/challenge.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.46 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.127 IQR)
- **Top Global Matches:** file_cluster_8: 10.46, file_cluster_13: 10.953, file_cluster_4: 11.048
- **Magnitude:** 59.96 | **LOC:** 1268 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (21.4655%), Tech Debt (99.79%)
**Top Internal Functions/Classes:**
  * `FastifyPluginCallbackTypebox` (Impact: 236.1)
    * *Intent:* /**
  * `async` (Impact: 71.7)
  * `async` (Impact: 30.2)
  * `postDailyCodingChallengeCompleted` (Impact: 29.4)
  * `async` (Impact: 26.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 122`, `args: 31`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 17`, `planned_debt: 4`, `duplicate_logic: 19`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 50`, `import: 18`
* *Defense:* `safety: 62`, `doc: 4`, `immutability_locks: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` index.js, get-challenges.js, progress.js, exam.js, challenge-helpers.js, fastify, validator, type-provider-typebox...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/src/redux/donation-saga.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.2 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.485 IQR)
- **Top Global Matches:** file_cluster_8: 7.2, file_cluster_7: 8.261, file_cluster_13: 8.399
- **Magnitude:** 59.08 | **LOC:** 224 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.0557%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 22.1)
  * `it` (Impact: 6.8)
  * `it` (Impact: 6.1)
  * `it` (Impact: 4.5)
  * `it` (Impact: 4.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 22`, `args: 9`, `func_start: 8`
* *Risk/State:* `duplicate_logic: 7`
* *Architecture:* `io: 2`, `concurrency: 1`, `import: 6`
* *Defense:* `test: 10`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` call-ga, ajax, actions, redux-saga-test-plan, vitest, donation-saga.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/src/templates/Challenges/redux/actions.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.251 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.723 IQR)
- **Top Global Matches:** file_cluster_8: 6.251, file_cluster_7: 7.35, file_cluster_13: 7.411
- **Magnitude:** 58.36 | **LOC:** 79 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 44`
* *Risk/State:* None
* *Architecture:* `api: 42`, `import: 2`
* *Defense:* `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` action-types, redux-actions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/protected/challenge.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.956 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.26 IQR)
- **Top Global Matches:** file_cluster_8: 9.956, file_cluster_4: 10.121, file_cluster_13: 10.503
- **Magnitude:** 58.07 | **LOC:** 2556 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (31.9482%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 65.2)
  * `describe` (Impact: 65.1)
  * `describe` (Impact: 40.1)
  * `describe` (Impact: 33.1)
  * `test` (Impact: 25.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 141`, `args: 126`, `func_start: 120`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 13`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 65`
* *Architecture:* `io: 21`, `concurrency: 130`, `import: 13`
* *Defense:* `safety: 13`, `doc: 2`, `test: 114`, `immutability_locks: 82`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` challenge-helpers.js, exam-types.js, exam.js, challenge-types, type-provider-typebox, get-session-user.js, client, vitest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/protected/settings.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.775 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.072 IQR)
- **Top Global Matches:** file_cluster_8: 10.775, file_cluster_7: 11.29, file_cluster_13: 11.336
- **Magnitude:** 52.41 | **LOC:** 898 | **CtrlFlow:** 38.4% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (7.5788%), Tech Debt (99.9786%)
**Top Internal Functions/Classes:**
  * `FastifyPluginCallbackTypebox` (Impact: 177.3)
  * `FastifyPluginCallbackTypebox` (Impact: 35.6)
  * `async` (Impact: 30.0)
  * `async` (Impact: 26.7)
  * `async` (Impact: 19.7)
    * *Intent:* /** * Plugin for endpoints that redirect if the user is not authenticated. * * @param fastify The Fa...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 165`, `args: 34`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1`, `planned_debt: 6`, `duplicate_logic: 20`
* *Architecture:* `io: 2`, `api: 5`, `concurrency: 50`, `import: 10`
* *Defense:* `safety: 85`, `doc: 26`, `immutability_locks: 91`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.1
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` is-restricted.js, fastify, validator, type-provider-typebox, tokens.js, env.js, date-fns, schemas.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `client/src/redux/settings/actions.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.542 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.451 IQR)
- **Top Global Matches:** file_cluster_8: 6.542, file_cluster_7: 7.669, file_cluster_13: 7.715
- **Magnitude:** 49.12 | **LOC:** 120 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (3.8583%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkForSuccessPayload` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 50`, `args: 2`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 46`, `import: 2`
* *Defense:* `safety: 2`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` action-types, redux-actions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `client/src/utils/path-parsers.ts` (TYPESCRIPT) | Magnitude: 2.36 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 8, immutability_locks: 6, branch: 5
- `client/src/declarations.d.ts` (TYPESCRIPT) | Magnitude: 1.0 | Delta: **0.221 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 28, indent_spaces: 17, decorators: 5, branch: 4
- `api/src/exam-environment/schemas/challenges.ts` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.251 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 3, api: 1, dead_code: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `api/src/utils/drip-campaign.ts` (TYPESCRIPT) | Magnitude: 0.68 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 3, doc: 3, branch: 2
- `e2e/eslint.config.mjs` (JAVASCRIPT) | Magnitude: 16.22 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 4, decorators: 4, events: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `client/src/utils/growthbook-cookie.ts` (TYPESCRIPT) | Magnitude: 3.43 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 8, immutability_locks: 7, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `api/src/schemas/signout/signout.ts` (TYPESCRIPT) | Magnitude: 1.52 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, import: 2, branch: 1
- `client/src/components/helpers/avatar-renderer.tsx` (TYPESCRIPT) | Magnitude: 1.4 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 12, ui_framework: 10, branch: 9
- `client/src/templates/Challenges/components/tool-panel.tsx` (TYPESCRIPT) | Magnitude: 2.15 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 105, structural_boundaries: 27, branch: 19, ui_framework: 15
- `api/src/plugins/auth.test.ts` (TYPESCRIPT) | Magnitude: 2.06 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 17, args: 8, func_start: 8
- `docker/devcontainer/Dockerfile` (DOCKERFILE) | Magnitude: 167.16 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: io: 30, safety: 25, indent_spaces: 17, branch: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `api/src/utils/index.ts` (TYPESCRIPT) | Magnitude: 3.22 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 31, generics: 11, api: 10
- `client/src/components/helpers/interleave.ts` (TYPESCRIPT) | Magnitude: 1.18 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, state_mutation: 6, structural_boundaries: 4, doc: 4
- `client/src/utils/ajax.ts` (TYPESCRIPT) | Magnitude: 22.59 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 200, structural_boundaries: 94, api: 59, generics: 55
- `api/src/routes/helpers/user-utils.ts` (TYPESCRIPT) | Magnitude: 0.29 | Delta: **0.256 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, generics: 5, doc: 3, indent_spaces: 2
- `packages/shared/src/utils/shuffle-array.ts` (TYPESCRIPT) | Magnitude: 0.89 | Delta: **0.333 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 3, state_mutation: 3, scientific: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `curriculum/src/test/daily-challenges.test.js` (JAVASCRIPT) | Magnitude: 62.14 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 61, state_mutation: 12, test: 11, structural_boundaries: 10
- `client/src/templates/Challenges/components/speaking-modal.tsx` (TYPESCRIPT) | Magnitude: 13.34 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 310, args: 60, structural_boundaries: 55, func_start: 48
- `api/src/plugins/shadow-capture.ts` (TYPESCRIPT) | Magnitude: 5.37 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 27, args: 26, func_start: 17
- `tools/challenge-parser/parser/plugins/add-solution.test.js` (JAVASCRIPT) | Magnitude: 0.04 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 76, func_start: 37, test: 37, structural_boundaries: 29
- `packages/challenge-linter/src/linter/markdown-yaml.js` (JAVASCRIPT) | Magnitude: 13.42 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 8, safety: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/challenge-builder/src/awaitable-messenger.ts` (TYPESCRIPT) | Magnitude: 1.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 15, doc: 12, args: 10
- `client/src/components/helpers/link.test.tsx` (TYPESCRIPT) | Magnitude: 1.24 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 8, args: 7, func_start: 7
- `client/src/components/daily-coding-challenge/calendar-day.tsx` (TYPESCRIPT) | Magnitude: 0.54 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 76, ui_framework: 21, structural_boundaries: 14, branch: 13
- `client/src/components/settings/exam-token.tsx` (TYPESCRIPT) | Magnitude: 2.72 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 97, args: 23, ui_framework: 20, structural_boundaries: 18
- `client/src/components/Intro/index.tsx` (TYPESCRIPT) | Magnitude: 0.44 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 79, ui_framework: 20, branch: 16, structural_boundaries: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tools/client-plugins/browser-scripts/sass-compile.ts` (TYPESCRIPT) | Magnitude: 2.38 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 8, safety: 7, branch: 4
- `tools/challenge-helper-scripts/insert-challenge.ts` (TYPESCRIPT) | Magnitude: 1.75 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 13, immutability_locks: 10, concurrency: 9
- `curriculum/src/build-superblock.ts` (TYPESCRIPT) | Magnitude: 24.51 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 324, structural_boundaries: 93, branch: 61, state_mutation: 57
- `e2e/utils/logout.ts` (TYPESCRIPT) | Magnitude: 0.52 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, concurrency: 2, args: 1, func_start: 1
- `client/src/pages/status/version.tsx` (TYPESCRIPT) | Magnitude: 5.47 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, concurrency: 13, structural_boundaries: 12, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `api/src/schemas/user/reset-my-progress.ts` (TYPESCRIPT) | Magnitude: 1.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, import: 2, branch: 1
- `client/__mocks__/react-i18next.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 22, args: 13, branch: 12
- `client/src/components/helpers/full-width-row.tsx` (TYPESCRIPT) | Magnitude: 0.26 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 5, ui_framework: 3, branch: 2
- `client/src/assets/images/components/index.tsx` (TYPESCRIPT) | Magnitude: 1.64 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, import: 8, indent_spaces: 8, api: 1
- `client/src/templates/Challenges/projects/tool-panel.tsx` (TYPESCRIPT) | Magnitude: 1.14 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 15, import: 7, func_start: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `curriculum/src/build-curriculum.ts` -> Churn: **59.93%** | Cog Load: 3.3254% | Debt: 59.6324%
- `tools/challenge-helper-scripts/create-language-block.ts` -> Churn: **51.69%** | Cog Load: 36.1685% | Debt: 55.5353%
- `client/src/templates/Challenges/classic/editor.tsx` -> Churn: **51.3%** | Cog Load: 9.5759% | Debt: 97.4667%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `curriculum/src/test/test-challenges.js` -> **Oliver Eyton-Williams** (87.5% isolated ownership) | Magnitude: 452.36
- `packages/challenge-builder/src/worker-executor.test.js` -> **Oliver Eyton-Williams** (100.0% isolated ownership) | Magnitude: 259.88
- `packages/challenge-builder/src/worker-executor.js` -> **Oliver Eyton-Williams** (100.0% isolated ownership) | Magnitude: 240.56
- `client/src/templates/Challenges/redux/code-storage-epic.js` -> **Oliver Eyton-Williams** (100.0% isolated ownership) | Magnitude: 130.86
- `api/src/exam-environment/routes/exam-environment.test.ts` -> **Shaun Hamilton** (100.0% isolated ownership) | Magnitude: 125.52

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `client/src/redux/prop-types.ts` -> **Severity: 179.382** (Blast Radius: 1.795 * Doc Risk: 99.9344%)
- `client/__mocks__/react-i18next.js` -> **Severity: 136.622** (Blast Radius: 3.211 * Doc Risk: 42.5481%)
- `client/__mocks__/gatsby.ts` -> **Severity: 76.501** (Blast Radius: 0.784 * Doc Risk: 97.5775%)
- `packages/shared/src/utils/polyvinyl.ts` -> **Severity: 70.1** (Blast Radius: 0.701 * Doc Risk: 100.0%)
- `packages/shared/src/config/donation-settings.ts` -> **Severity: 56.5** (Blast Radius: 0.565 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
