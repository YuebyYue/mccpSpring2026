# Comments and Feedback on My Writing

## Supervisor Comments

No formal written supervisor comments are included in this submission. However, discussions with my supervisor emphasized improving clarity, strengthening the literature positioning, and clarifying the methodological novelty.

**Date received:** Ongoing discussions during manuscript revision  

**Context:** Guided MRI Reconstruction via Schrödinger Bridge (TMI submission)

---

## Peer Review Comments

No formal peer review comments are available for this manuscript.

**Date received:** N/A  

**Context:** N/A

---

## Reviewer Comments

The manuscript “Guided MRI Reconstruction via Schrödinger Bridge” (TMI-2024-3060) received a Reject/Resubmit decision from IEEE Transactions on Medical Imaging, with major revisions required and new external review.

**Date received:** 2024  

**Context:** IEEE TMI submission (initial review round)

### Major Themes from Reviewer Feedback:

**1. Clarity and Presentation Issues**
- The algorithmic description was considered difficult to follow.
- Background sections on diffusion models and Schrödinger Bridge lacked sufficient explanation and references.
- Notation inconsistencies and unclear connection between figures and equations.
- The inversion mechanism was not clearly motivated or intuitively explained.
- Need to rewrite theory/method sections for readers unfamiliar with Schrödinger Bridge.

**2. Literature Review Weaknesses**
- Missing discussion of classical and modern multi-contrast MRI reconstruction methods.
- Insufficient positioning relative to joint reconstruction, Bayesian compressed sensing, GAN-based guidance, and traditional regularization-based approaches.
- Literature review structure was described as somewhat disorganized.
- Claims regarding diffusion and unsupervised training needed correction.

**3. Experimental Design Concerns**
- Limited experimental diversity (single dataset).
- High PSNR values for all methods made differences difficult to assess.
- Insufficient ablation strength for inversion module.
- Lack of comparison with key SOTA methods (MoDL, VN, jVN, PICS, Score-MRI, etc.).
- Unclear handling of spatial registration and motion between contrasts.
- Questions about acceleration factors and potential data leakage (“data crime”).

**4. Practical and Theoretical Significance**
- Improvements were considered visually and quantitatively marginal.
- Computational complexity and training cost not sufficiently discussed.
- Limited justification for choosing Schrödinger Bridge over standard diffusion models.
- Mathematical formulation of certain optimization steps potentially incorrect or unclear.

**5. Writing and Structural Issues**
- Terminology inconsistencies.
- Typos and grammar errors.
- Need for stronger discussion section addressing limitations.

Overall, reviewers acknowledged potential merit but expressed concern regarding clarity, novelty positioning, and experimental rigor.

---

## Teacher/Instructor Feedback

No direct instructor feedback is included for this manuscript.

**Date received:** N/A  

**Context:** N/A

---

## Other Feedback

Editorial feedback indicated that while the work shows promise, revising for TMI would be challenging unless substantial improvements are made in clarity, evaluation strength, and literature positioning.

---

## Notes

The TMI review process highlighted several writing-related weaknesses in my manuscript:

1. I tended to assume reader familiarity with advanced concepts (e.g., Schrödinger Bridge), which reduced accessibility.
2. The literature review lacked a clear structural narrative linking joint reconstruction and diffusion bridges.
3. Experimental validation was not sufficiently designed to emphasize practical impact.
4. Mathematical explanations were sometimes overly abstract without intuitive grounding.

These comments significantly influenced my revision strategy. I plan to:
- Restructure the Introduction to clearly separate motivation, gap, and contribution.
- Reorganize the Literature Review into traditional joint reconstruction vs diffusion-based vs bridge-based frameworks.
- Improve algorithm visualization and step-by-step explanations.
- Strengthen experimental comparisons and include clearer ablation studies.
- Explicitly discuss limitations, computational cost, and practical constraints.

Although the decision was Reject/Resubmit, the feedback provided concrete guidance for improving both scientific positioning and academic writing clarity.
