# Revised Draft — Introduction and Literature Review

## Source Information

**Date written:** March 2026 (revised from November 2024 draft)

**Context:** This draft is based on my research paper titled *"Guided MRI Reconstruction via Schrödinger Bridge"*. It has been substantially revised following TMI reviewer feedback (TMI-2024-3060) and course instruction on rhetorical moves.

**Status:** Revised draft — Introduction and Literature Review rewritten to address reviewer concerns regarding clarity, literature positioning, and structural organization.

---

## Introduction

<!-- Move 1 – Establishing a Territory -->

### Move 1: Establishing a Territory

Magnetic Resonance Imaging (MRI) is an indispensable diagnostic tool in modern clinical practice, offering superior soft-tissue contrast without ionizing radiation. In routine clinical workflows, multiple contrasts — such as T1-weighted, T2-weighted, and FLAIR sequences — are acquired to provide complementary anatomical and pathological information (Liang & Lauterbur, 2000). However, the inherently slow data acquisition process of MRI remains a major bottleneck, particularly when multiple contrasts are required. Accelerating MRI acquisition by undersampling k-space data and computationally reconstructing images has therefore become a central research objective in the field.

Early efforts to address this challenge relied on model-based approaches, including parallel imaging techniques such as GRAPPA (Griswold et al., 2002) and compressed sensing (CS) methods (Lustig et al., 2007) that exploit sparsity priors in transform domains. While effective at moderate acceleration, these classical approaches depend on handcrafted regularizers — such as total variation and wavelet sparsity — that require careful parameter tuning and yield diminishing returns at high acceleration factors. More recently, deep learning has transformed MRI reconstruction: supervised unrolling networks such as MoDL (Aggarwal et al., 2019) and Variational Networks (VN) (Hammernik et al., 2018) achieve substantial improvements by learning data-driven priors from training data, significantly outperforming traditional CS methods in both speed and image quality.

Beyond supervised approaches, generative models have emerged as a promising paradigm. Score-based diffusion models (Song et al., 2021; Chung et al., 2022) learn the prior distribution of MRI images and incorporate measurement consistency during iterative sampling, offering improved generalization compared to supervised methods that overfit to specific acquisition settings. These developments underscore the growing sophistication of MRI reconstruction methods, progressing from handcrafted priors to learned data distributions.

<!-- Move 2 – Identifying a Niche -->

### Move 2: Identifying a Niche

Despite significant progress, a fundamental limitation remains unresolved in existing reconstruction frameworks: the underutilization of cross-contrast structural priors. Clinical MRI sessions routinely acquire multiple contrasts that share strong anatomical structures, yet the majority of reconstruction methods — whether CS-based, supervised, or diffusion-based — treat each contrast independently, relying solely on undersampled k-space measurements for guidance. Although several studies have explored multi-contrast reconstruction through joint variational models (Ehrhardt & Betcke, 2016), coupled dictionary learning (Song et al., 2019), and GAN-based cross-modal synthesis (Dar et al., 2019), these approaches either impose rigid assumptions about inter-contrast relationships or lack principled mechanisms for transferring structural information across contrasts. Recent conditional diffusion models (Xie et al., 2022) attempt to incorporate guidance from auxiliary contrasts, but they model the joint distribution implicitly rather than constructing an explicit transport pathway between distributions. Consequently, structural discrepancies between guiding and target contrasts — arising from differences in tissue contrast and pathological appearance — can introduce regression-to-the-mean artifacts and limit reconstruction fidelity. No existing approach provides a mathematically principled framework that explicitly bridges two contrast distributions while preserving structural alignment and correcting inter-contrast inconsistencies.

<!-- Move 3 – Occupying the Niche -->

### Move 3: Occupying the Niche

To address these gaps, this study proposes a novel guided MRI reconstruction framework based on the Schrödinger Bridge (SB). Unlike standard diffusion models that map between a data distribution and Gaussian noise, the SB establishes an optimal transport process between two arbitrary distributions — in this case, the distributions of the guiding contrast and the target contrast — thereby enabling principled structural transfer during reconstruction. Specifically, the contributions of this work are threefold: (1) we formulate multi-contrast guided MRI reconstruction as a Schrödinger Bridge problem, leveraging the Image-to-Image Schrödinger Bridge (I²SB) framework (Liu et al., 2023) to make nonlinear inter-distribution diffusion computationally tractable; (2) we introduce an inversion module that detects and corrects structural inconsistencies between the guiding and target contrasts, mitigating regression-to-the-mean effects; and (3) we demonstrate on paired T1-weighted and T2-FLAIR brain MRI datasets that the proposed method outperforms both supervised baselines (MoDL, VN) and diffusion-based approaches (Score-MRI) across multiple acceleration factors, achieving improvements of over 1.5 dB in PSNR at 8× acceleration while maintaining perceptual quality.

---

## Literature Review

<!-- Move 1 – Thematic Overview -->

### Move 1: Thematic Overview

This review examines the evolution of accelerated MRI reconstruction methods, with particular focus on multi-contrast guided approaches. The relevant literature is organized into four thematic groups: (a) classical model-based reconstruction, (b) supervised deep learning methods, (c) generative and diffusion-based methods, and (d) Schrödinger Bridge and optimal transport frameworks. Key terms used throughout include *multi-contrast MRI* (simultaneous use of different pulse sequences), *k-space undersampling* (acquiring fewer measurements than required by the Nyquist criterion), and *structural priors* (shared anatomical information across contrasts). This progression from handcrafted to learned to transport-based priors provides the context for understanding our proposed approach.

<!-- Move 2 – Critical Analysis -->

### Move 2: Critical Analysis

**Classical model-based approaches.** Compressed sensing (Lustig et al., 2007) and parallel imaging (Griswold et al., 2002) pioneered accelerated MRI by exploiting signal sparsity and coil sensitivity, respectively. Joint reconstruction methods extended this paradigm to multi-contrast settings: coupled dictionary learning (Song et al., 2019) and joint total variation (Ehrhardt & Betcke, 2016) enforce structural similarity across contrasts through shared regularization. Bayesian compressed sensing frameworks (Bilgic et al., 2011) provide a probabilistic formulation that models uncertainty in the reconstruction. While these classical methods offer theoretical guarantees and interpretability, they are constrained by the expressiveness of handcrafted priors and require extensive parameter tuning, limiting reconstruction quality at high acceleration factors (beyond 4–6×).

**Supervised deep learning approaches.** Unrolling-based networks such as MoDL (Aggarwal et al., 2019), Variational Networks (Hammernik et al., 2018), and their joint multi-contrast extensions like jVN (Hammernik et al., 2021) significantly advance reconstruction quality by learning data-driven priors from large training datasets. These methods achieve notable improvements: for example, MoDL reports 2–4 dB PSNR gains over CS at equivalent acceleration factors. However, supervised methods require abundant fully sampled training data, which is often scarce in clinical settings, and tend to generalize poorly across different acquisition protocols, anatomies, and acceleration factors. GAN-based methods (Dar et al., 2019; Quan et al., 2018) offer an alternative by synthesizing target contrasts from available ones, yet they suffer from hallucination artifacts and mode collapse, raising reliability concerns for clinical diagnosis.

**Generative and diffusion-based approaches.** Score-based diffusion models (Song et al., 2021) and their MRI reconstruction adaptations, such as Score-MRI (Chung et al., 2022), represent a paradigm shift toward distribution-level modeling. By learning the score function of the MRI image distribution and iteratively enforcing data consistency during reverse diffusion, these methods achieve strong generalization without requiring paired training data at specific acceleration factors. Recent conditional diffusion models (Xie et al., 2022) extend this framework to incorporate guidance from auxiliary contrasts. Nevertheless, these approaches model the joint distribution of contrasts implicitly through conditioning mechanisms, without establishing an explicit mapping between contrast distributions. This implicit coupling limits their capacity to enforce fine-grained structural alignment and leaves structural discrepancies unaddressed.

**Schrödinger Bridge and optimal transport.** The Schrödinger Bridge (SB) problem, rooted in optimal transport theory, seeks the most likely stochastic process connecting two probability distributions under entropy constraints (Léonard, 2014). Unlike standard diffusion models that bridge data and noise, SB bridges two data distributions directly, making it conceptually suited for image-to-image translation tasks. The Image-to-Image Schrödinger Bridge (I²SB) framework (Liu et al., 2023) demonstrates that tractable SB computation is achievable through iterative proportional fitting and achieves state-of-the-art results in natural image translation. However, at the time of writing, the application of SB to guided MRI reconstruction remains largely unexplored, and no existing work addresses the critical challenge of correcting structural inconsistencies that arise during cross-contrast transport.

<!-- Move 3 – Research Gaps -->

### Move 3: Research Gaps

The above analysis reveals three interrelated gaps in the current literature. First, existing multi-contrast methods — whether classical joint regularization, supervised joint networks, or conditional diffusion models — lack a mathematically grounded mechanism for constructing explicit distribution-level transport between contrasts, relying instead on implicit coupling or rigid structural assumptions. Second, the problem of structural inconsistency between guiding and target contrasts (e.g., lesions visible in FLAIR but absent in T1) has not been systematically addressed, leading to regression-to-the-mean artifacts in guided reconstruction. Third, although the Schrödinger Bridge provides a theoretically appealing framework for inter-distribution mapping, its potential for guided MRI reconstruction has not been investigated. These gaps collectively point to the need for a principled transport-based reconstruction framework with built-in mechanisms for handling cross-contrast structural discrepancies.

<!-- Move 4 – Conclusion -->

### Move 4: Conclusion

In summary, MRI reconstruction has evolved from handcrafted regularization through supervised deep learning to distribution-level generative modeling, each stage offering improved reconstruction quality but also introducing new limitations. The convergence of multi-contrast imaging, diffusion-based reconstruction, and optimal transport theory creates a compelling opportunity: by formulating guided reconstruction as a Schrödinger Bridge problem, it becomes possible to explicitly transport structural information between contrasts while maintaining theoretical rigor. The present study addresses this opportunity by proposing an SB-based guided reconstruction framework with an inversion module, bridging the gap between distribution-level generative modeling and practical multi-contrast MRI reconstruction.

---

**Word count:** approximately 1,350 words (excluding references and annotations)

---

## Annotations

<!-- Annotations of techniques/concepts applied, as required by the assessment rubric -->

- **Move 1 (Introduction):** Establishes territory by progressing chronologically from classical CS/parallel imaging → supervised DL → diffusion models, addressing TMI reviewer concern about missing classical methods.
- **Move 2 (Introduction):** Uses explicit gap language ("remains unresolved," "no existing approach provides") to clearly signal the research niche. Addresses five method categories (joint variational, dictionary learning, GAN-based, conditional diffusion, Bayesian CS) as required by TMI reviewers.
- **Move 3 (Introduction):** Provides numbered contributions (threefold) with quantitative preview, as recommended in writing feedback.
- **Literature Review Move 2:** Organized into four thematic groups (classical → supervised DL → diffusion → SB) following chronological-thematic progression. Includes critical evaluation with specific performance comparisons and limitations.
- **Hedging language:** "approximately," "largely unexplored," "tends to" — used to qualify claims appropriately.
- **Cohesive devices:** "Despite significant progress," "Nevertheless," "In summary," "The convergence of" — used to link sections and signal transitions.
- **Citation style:** IEEE-style author-year references used consistently throughout, following conventions in the medical imaging field.
- **Accessibility:** Technical concepts (Schrödinger Bridge, score-based diffusion, k-space undersampling) are briefly defined at first use to ensure readability for non-specialist readers.

---

## References

Aggarwal, H. K., Mani, M. P., & Jacob, M. (2019). MoDL: Model-based deep learning architecture for inverse problems. *IEEE Transactions on Medical Imaging*, 38(2), 394–405.

Bilgic, B., Goyal, V. K., & Adalsteinsson, E. (2011). Multi-contrast reconstruction with Bayesian compressed sensing. *Magnetic Resonance in Medicine*, 66(6), 1601–1615.

Chung, H., & Ye, J. C. (2022). Score-based diffusion models for accelerated MRI. *Medical Image Analysis*, 80, 102479.

Dar, S. U. H., Yurt, M., Karacan, L., Erdem, A., Erdem, E., & Çukur, T. (2019). Image synthesis in multi-contrast MRI with conditional generative adversarial networks. *IEEE Transactions on Medical Imaging*, 38(10), 2375–2388.

Ehrhardt, M. J., & Betcke, M. M. (2016). Multicontrast MRI reconstruction with structure-guided total variation. *SIAM Journal on Imaging Sciences*, 9(3), 1084–1106.

Griswold, M. A., et al. (2002). Generalized autocalibrating partially parallel acquisitions (GRAPPA). *Magnetic Resonance in Medicine*, 47(6), 1202–1210.

Hammernik, K., et al. (2018). Learning a variational network for reconstruction of accelerated MRI data. *Magnetic Resonance in Medicine*, 79(6), 3055–3071.

Hammernik, K., et al. (2021). Systematic evaluation of iterative deep neural networks for fast parallel MRI reconstruction with sensitivity-weighted coil combination. *Magnetic Resonance in Medicine*, 86(4), 1859–1872.

Léonard, C. (2014). A survey of the Schrödinger problem and some of its connections with optimal transport. *Discrete and Continuous Dynamical Systems*, 34(4), 1533–1574.

Liang, Z. P., & Lauterbur, P. C. (2000). *Principles of Magnetic Resonance Imaging: A Signal Processing Perspective*. IEEE Press.

Liu, G. H., et al. (2023). I²SB: Image-to-Image Schrödinger Bridge. In *Proceedings of the International Conference on Machine Learning (ICML)*.

Lustig, M., Donoho, D., & Pauly, J. M. (2007). Sparse MRI: The application of compressed sensing for rapid MR imaging. *Magnetic Resonance in Medicine*, 58(6), 1182–1195.

Quan, T. M., Nguyen-Duc, T., & Jeong, W. K. (2018). Compressed sensing MRI reconstruction using a generative adversarial network with a cyclic loss. *IEEE Transactions on Medical Imaging*, 37(6), 1488–1497.

Song, P., et al. (2019). Coupled dictionary learning for multi-contrast MRI reconstruction. *IEEE Transactions on Medical Imaging*, 38(1), 621–633.

Song, Y., Sohl-Dickstein, J., Kingma, D. P., Kumar, A., Ermon, S., & Poole, B. (2021). Score-based generative modeling through stochastic differential equations. In *Proceedings of ICLR*.

Xie, Y., et al. (2022). Measurement-conditioned denoising diffusion probabilistic model for under-sampled medical image reconstruction. In *Proceedings of MICCAI*.

---

## Notes

This revised draft addresses the following TMI reviewer concerns:
1. **Clarity:** Schrödinger Bridge is now defined intuitively before technical use; diffusion model background is expanded.
2. **Literature gaps:** Classical methods (CS, parallel imaging, Bayesian CS, joint TV), GAN-based methods, and key baselines (MoDL, VN, Score-MRI) are now covered.
3. **Structure:** Literature review follows chronological-thematic progression (classical → supervised DL → diffusion → SB).
4. **Gap signaling:** Explicit language used in Move 2 to identify research niche.
5. **Contributions:** Numbered threefold contributions with quantitative preview in Move 3.

See `revision_checklist.md` for the full checklist of reviewer concerns and their status.
