# TMI Reviewer Feedback — Revision Checklist

**Based on:** IEEE TMI submission (TMI-2024-3060), "Guided MRI Reconstruction via Schrödinger Bridge"
**Purpose:** Systematically address each reviewer concern in the revised Introduction and Literature Review

---

## Clarity and Presentation

- [ ] Explain Schrödinger Bridge concept for readers unfamiliar with it (add intuitive definition before using the term)
- [ ] Provide sufficient background on diffusion models before introducing SB
- [ ] Ensure notation is consistent throughout the text
- [ ] Motivate the inversion mechanism intuitively, not just mathematically
- [ ] Avoid assuming reader familiarity with advanced concepts

## Literature Review Completeness

- [ ] Include classical multi-contrast MRI reconstruction methods (e.g., compressed sensing, parallel imaging, regularization-based)
- [ ] Discuss joint reconstruction methods (e.g., joint variational models, coupled dictionaries)
- [ ] Cover Bayesian compressed sensing approaches
- [ ] Address GAN-based guidance methods for MRI reconstruction
- [ ] Position relative to traditional regularization-based approaches (total variation, wavelet, low-rank)
- [ ] Compare against key SOTA methods: MoDL, VN, jVN, PICS, Score-MRI
- [ ] Correct claims regarding diffusion models and unsupervised training

## Literature Review Structure

- [ ] Organize thematically: classical → deep learning → diffusion → Schrödinger Bridge (chronological-thematic progression)
- [ ] Group methods clearly with explicit thematic headings
- [ ] Synthesize across studies (show connections, contrasts) rather than summarizing one-by-one
- [ ] Add critical evaluation with specific comparisons (performance metrics, limitations)

## Introduction Structure (Rhetorical Moves)

- [ ] Move 1: Cover classical methods first, then transition to modern DL approaches, then to diffusion/SB
- [ ] Move 2: Use explicit gap language ("remains unresolved," "no existing approach," "however")
- [ ] Move 3: Add numbered contributions clearly stating each novelty
- [ ] Ensure clear logical flow: Move 1 → Move 2 → Move 3

## Research Significance

- [ ] Justify why Schrödinger Bridge is preferred over standard diffusion models
- [ ] Discuss computational complexity and training cost
- [ ] Address practical significance: acceleration factors, clinical applicability
- [ ] Discuss limitations explicitly

## Writing Quality

- [ ] Eliminate terminology inconsistencies
- [ ] Fix grammar and typos
- [ ] Ensure each paragraph has a clear topic sentence and purpose
- [ ] Use cohesive devices to link paragraphs (transitions)
- [ ] Keep within 1000–1500 words

---

## Progress Tracking

| Section | Status | Notes |
|---------|--------|-------|
| Introduction Move 1 | ✅ | Covers CS, parallel imaging, supervised DL, diffusion — chronological progression |
| Introduction Move 2 | ✅ | Explicit gap language: "remains unresolved," "no existing approach provides" |
| Introduction Move 3 | ✅ | Threefold numbered contributions with quantitative preview |
| Lit Review Move 1 | ✅ | Scope/purpose statement + key term definitions |
| Lit Review Move 2 | ✅ | Four thematic groups with critical evaluation and performance comparisons |
| Lit Review Move 3 | ✅ | Three interrelated gaps clearly articulated |
| Lit Review Move 4 | ✅ | Bridges to SB-based research contribution |

**Revised draft:** `revisedDraft.md`
