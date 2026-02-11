# My First Draft

## Source Information

**Date written:** November 2024  

**Context:** This draft is based on my research paper titled *“Guided MRI Reconstruction via Schrödinger Bridge”*. It is prepared as a writing sample for academic evaluation and reflects my research manuscript structure.  

**Status:** Partial draft – Introduction and Background sections are fully written; Method, Experiments, and Discussion sections are completed in the research manuscript.

---

## Introduction

### Move 1: Establishing a Territory

Magnetic Resonance Imaging (MRI) is a widely used medical imaging modality capable of providing detailed anatomical and functional information. However, long acquisition times remain a major limitation for clinical deployment. A common strategy to address this issue is k-space undersampling followed by reconstruction using prior knowledge. Traditional compressed sensing methods rely on handcrafted priors such as sparsity and low-rank constraints, but these approaches often require careful tuning and achieve limited acceleration.

With the rapid development of deep learning, data-driven MRI reconstruction methods have demonstrated superior performance. Supervised unrolling-based networks and generative models such as diffusion models have significantly improved reconstruction quality while reducing reliance on handcrafted priors.

### Move 2: Identifying a Niche

Despite recent progress, current diffusion-based reconstruction methods primarily rely on undersampled k-space measurements for guidance. However, MRI is inherently a multi-contrast imaging modality, where different contrasts share strong structural similarities. Existing conditional diffusion models do not fully exploit this structural correspondence between contrasts for guided reconstruction. Furthermore, structural discrepancies between guiding and target contrasts may introduce reconstruction errors due to regression-to-the-mean effects.

These limitations highlight the need for a more flexible distribution modeling framework capable of explicitly bridging different image distributions while preserving structural alignment.

### Move 3: Occupying the Niche

To address these challenges, we propose a novel guided MRI reconstruction framework based on the Schrödinger Bridge (SB). The SB provides a nonlinear diffusion process that establishes a probabilistic bridge between two arbitrary distributions. By constructing a diffusion bridge between guiding and target contrast distributions, structural priors can be effectively transferred during reconstruction.

Moreover, we introduce an inversion strategy to correct structural inconsistencies between guiding and reconstructed images. Experimental results on paired T1 and T2-FLAIR datasets demonstrate that the proposed method achieves high acceleration factors and outperforms existing supervised and diffusion-based approaches in both reconstruction accuracy and stability.

---

## Literature Review

### Move 1: Thematic Overview

MRI reconstruction methods can generally be categorized into traditional model-based approaches and deep learning-based approaches. Traditional methods such as compressed sensing rely on handcrafted priors including sparsity and low-rank constraints. Deep learning approaches include supervised unrolling networks and generative models such as diffusion models.

Diffusion models, particularly score-based generative models (SGMs), have shown strong performance in inverse problems by learning the data distribution and incorporating data consistency during sampling.

### Move 2: Critical Analysis

Supervised unrolling networks achieve strong reconstruction accuracy but require large amounts of fully sampled data and often suffer from limited generalization. Diffusion-based approaches alleviate data pairing constraints and provide improved generalization, yet most current methods only use measurement consistency as guidance.

Recent studies have attempted multi-contrast modeling through joint diffusion learning. However, these approaches model joint distributions rather than explicitly constructing transport between distributions, which limits their ability to enforce structural alignment.

The Schrödinger Bridge (SB) extends diffusion models by enabling optimal transport between arbitrary distributions. While promising, its computational complexity has historically limited practical application. The recent Image-to-Image Schrödinger Bridge (I²SB) framework makes nonlinear diffusion computationally tractable.

### Move 3: Research Gaps

Current MRI reconstruction methods lack a principled framework for explicitly bridging guiding and target contrast distributions. Moreover, structural discrepancies between multi-contrast images are often not properly handled, leading to suboptimal performance in guided reconstruction settings.

There is limited exploration of SB-based guided reconstruction in multi-contrast MRI scenarios.

### Move 4: Conclusion

The existing literature demonstrates the effectiveness of diffusion models and supervised learning in MRI reconstruction, but it does not fully exploit cross-contrast structural priors within a nonlinear diffusion transport framework. This gap motivates the development of an SB-based guided reconstruction model with an inversion mechanism to enhance structural consistency.

---

## Notes

This manuscript reflects my research writing style in a technical and mathematically rigorous domain. One challenge I faced during writing was balancing theoretical explanation with practical algorithmic clarity. Another difficulty was structuring the Introduction to clearly highlight the research gap without overloading it with technical details.

In drafting this paper, I aimed to follow a structured move-based academic writing approach (territory–niche–occupation) to strengthen logical coherence. My goal is to improve clarity, reduce redundancy, and enhance critical positioning of my work within the existing literature.
