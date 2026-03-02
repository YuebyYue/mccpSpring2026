# Writing Feedback — WANG Yue (王越)

## Feedback on WANG Yue's Writing Samples: Introduction and Literature Review

**Student:** WANG Yue (王越)
**Topic:** Guided MRI Reconstruction via Schrödinger Bridge
**Date:** 2 March 2026
**Reviewer:** Simon Wang (with AI-assisted analysis)

**Your samples:** writing/writingSampleCollection/writingSamples.md
**Your comments:** writing/writingSampleCollection/comments.md
**Your reflection:** writing/writingSampleCollection/reflection.md
**Assessment rubric:** writing/assessment/writing_instructions_formatted.md

---

## Overall Assessment

You are in a unique position among the class: you have real reviewer feedback from an IEEE TMI submission (Reject/Resubmit), which provides concrete, actionable insights into your writing weaknesses. Your writing samples (labeled as Move 2 and Move 3 excerpts) demonstrate solid technical understanding and a clear research direction. However, the samples reveal several issues that align closely with the TMI reviewer comments: (1) the writing assumes too much reader familiarity with advanced concepts like Schrödinger Bridge; (2) the literature positioning is underdeveloped — reviewers noted missing discussion of classical methods and disorganized structure; and (3) the samples tend toward description rather than critical analysis. The good news is that you already have a clear diagnosis from the reviewers; the task now is to systematically address each point.

**Estimated current level:** Satisfactory (6–7 range) — The technical foundation is strong and you have genuine research experience, but the writing needs better structure, accessibility, and critical depth.

---

## Part 1: Introduction Feedback (Based on Your Move 2 Sample)

### What Works Well

- Your Move 2 sample effectively identifies the gap: existing video-pretraining pipelines are costly and can hurt transfer
- The framing of "cost and potential negative transfer" as dual motivations is compelling
- You show awareness of the move structure by labeling your samples

### Issue 1: The "Context" Provided Is Insufficient

Your Move 2 sample mentions "conventional video-pretraining pipelines" but does not define what these are or why they exist. A reader unfamiliar with video-language models would be lost. This mirrors the TMI reviewer feedback: "Need to rewrite theory/method sections for readers unfamiliar with Schrödinger Bridge."

**Action:** For each technical concept you introduce, ask: "Would a reader from a neighboring field (e.g., NLP researcher reading about video models) understand this?" If not, add one sentence of explanation before using the term.

### Issue 2: Move 2 Does Not Clearly Signal the Gap

Your sample describes the cost problem but does not explicitly frame it as a gap in the literature. Compare:

**Your version:** "Opening/motivation + gap statement (why conventional video-pretraining pipelines are costly and can hurt transfer)"

**Stronger Move 2 signal:** "Despite significant progress in video-language models, a fundamental tension remains unresolved: achieving strong temporal understanding requires expensive video pretraining [citations], yet this pretraining often introduces negative transfer when the target domain differs from the pretraining corpus [citations]. No existing approach successfully eliminates the pretraining requirement while maintaining competitive performance."

The revised version uses explicit gap language ("remains unresolved," "no existing approach") that signals Move 2 to the reader.

### Issue 3: Connecting Your TMI Experience to This Draft

Your TMI reviewers provided specific writing feedback that directly applies to your Introduction:
- "Missing discussion of classical and modern multi-contrast MRI reconstruction methods"
- "Insufficient positioning relative to joint reconstruction, Bayesian compressed sensing, GAN-based guidance"
- "Literature review structure was described as somewhat disorganized"

**Action:** When writing your Introduction for this assignment, ensure Move 1 covers the classical methods first, then transitions to modern deep learning approaches, and then to diffusion/Schrödinger Bridge methods. This chronological-thematic progression is what reviewers expect.

---

## Part 2: Literature Review Feedback (Based on Your Move 2 and Move 3 Samples)

### What Works Well

- Your Move 2 Literature Review sample shows genuine synthesis: you group methods into (a) task-specific multimodal models and (b) video large language models — this is exactly the thematic organization expected
- The final synthesis sentence ("the literature suggests a tension between generality and practicality") is excellent — this is the kind of critical insight that elevates a literature review
- Your Move 3 sample clearly describes your proposed approach (MTransLLAMA) and how it addresses the identified gaps

### Issue 4: Strengthen Critical Evaluation Within Each Group

Your grouping of methods is good, but the evaluation within each group could be deeper. For example:

**Your sentence:** "task-specific models can be effective, they typically require learning attention-based fusion from scratch and struggle in low-data regimes"

**Deeper analysis:** "Task-specific models such as [Name et al., Year] and [Name et al., Year] achieve strong performance on benchmark datasets (e.g., X% accuracy on [benchmark]) but require dataset-specific attention fusion modules that do not transfer across tasks. In low-data regimes (fewer than N training examples), these models show F1 drops of X–Y% [citation], making them impractical for emerging video understanding tasks where labeled data is scarce."

The deeper version adds specific papers, specific numbers, and specific failure conditions.

### Issue 5: Address the TMI Reviewer Feedback on Literature Gaps

The TMI reviewers specifically noted missing coverage of:
- Classical multi-contrast MRI reconstruction
- Joint reconstruction methods
- Bayesian compressed sensing
- GAN-based guidance approaches
- Traditional regularization-based approaches

**Action:** For your revised draft, create a comprehensive literature map that covers these areas systematically. Even if your assignment focuses on your video/MRI approach, demonstrating awareness of the broader methodological landscape is essential.

### Issue 6: Move 3 Needs Quantitative Contribution Preview

Your Move 3 describes MTransLLAMA's approach qualitatively but doesn't preview specific results or contributions.

**Suggestion:** Add numbered contributions: "(1) We propose channel swapping for temporal attention reuse, reducing trainable parameters by X%; (2) We introduce early text-visual fusion in the Q-former, improving [metric] by X points; (3) We demonstrate competitive performance on [benchmarks] without any video pretraining."

---

## Part 3: Language and Process Feedback

### Issue 7: Your "Structure First, Language Later" Strategy Is Sound

Your reflection describes a "structure first, language later" approach — this is a good strategy. However, make sure "structure" includes the rhetorical moves, not just the section headings. A well-structured draft has clear Move 1 → Move 2 → Move 3 progression in the Introduction and Move 1 → Move 2 → Move 3 → Move 4 in the Literature Review.

### Issue 8: Leverage Your TMI Review Experience

You have a rare advantage: real reviewer feedback on real writing. Most students in the class do not have this. Use it systematically:
- Create a checklist from the reviewer comments
- Check each point against your new draft
- Address each point explicitly in your revision

Your reflection wisely notes: "clarity is as important as innovation." This is a lesson many researchers learn too late.

---

## Summary of Priority Actions

| Priority | Action | Impact |
|----------|--------|--------|
| 🔴 High | Write a full Introduction with clearly separated Moves 1, 2, 3 | Addresses structural weakness |
| 🔴 High | Cover classical methods before modern methods in Move 1 | Addresses TMI reviewer concern |
| 🔴 High | Add explicit gap language in Move 2 | Makes research motivation clear |
| 🟡 Medium | Deepen critical analysis with specific numbers and comparisons | Elevates literature review quality |
| 🟡 Medium | Add numbered contribution preview in Move 3 | Signals clear research value |
| 🟡 Medium | Address each TMI reviewer point systematically | Demonstrates growth and revision skill |
| 🟢 Lower | Ensure accessibility — explain advanced concepts for non-specialist readers | Improves readability |

---

## Next Steps

1. Read the [full writing instructions](https://github.com/tesolchina/mccpSpring2026/blob/main/writing/assessment/writing_instructions_formatted.md)
2. Write a complete Introduction and Literature Review (1000–1500 words) for your MRI/video research
3. Use the TMI reviewer feedback as a revision checklist
4. Submit by **15 March 2026** via Moodle forum and Turnitin
