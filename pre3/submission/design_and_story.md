# Design and Story Rationale

## Research Positioning

This 3MT slide presents my proposed doctoral research direction, inspired by Professor Xiaoqing Guo's work and the UltraVision+ Lab. I do not present the existing lab work as my own completed research. Instead, I frame my direction as a future research story: how AI could become a real-time co-pilot for ultrasound scanning.

The research area is medical AI for ultrasound. The key problem is that ultrasound is highly operator-dependent. A useful scan depends not only on the machine, but also on the skill of the person holding the probe, recognizing anatomical structures, checking image quality, and deciding what to scan next.

## Slide Design

The slide is designed as a left-to-right story:

1. The left side shows the problem: ultrasound requires expert eyes and steady hands.
2. The center shows the proposed solution: an AI co-pilot that can combine video, voice, probe motion, and reports.
3. The right side shows the goal: real-time guidance through simple questions a learner might ask during scanning.
4. The bottom impact band summarizes the intended significance: shorter learning curve, more consistent scans, and better access to skilled care.

I used a "co-pilot" or "GPS" metaphor because it is familiar to non-specialist audiences. A GPS does not replace the driver, but it helps the driver understand where they are, what is missing, and where to move next. In the same way, the AI system is presented as a guide for ultrasound users, not as a replacement for clinicians.

The slide is intentionally text-light. It uses one main visual pathway and four short guidance questions instead of technical terms. The file is written in HTML with inline SVG and CSS, so it is machine-readable and not just a static image.

## Alignment with Course Materials

This submission follows the Presentation 3 brief and the Session 9 guidance in `pre3/materials/`.

- The slide is a single static visual, not a multi-slide deck.
- The slide is machine-readable HTML with inline SVG and CSS, not only a PNG, JPG, or PDF.
- The talk structure follows the 3MT moves introduced in Session 9: hook, research motivation, objective, brief method, expected findings or outcomes, and significance.
- The content is designed for a non-specialist audience, so technical terms are minimized and explained through everyday language.
- The slide avoids heavy reading demand within three minutes, which matches the rubric's emphasis on a simple and supportive visual aid.
- The recording notes are key-point notes only, not a full script to read aloud.

I also checked the local `pre3/SlidesGen/` materials. Those files demonstrate how HTML diagrams can be created or edited for presentation slides. I used the same general idea of an editable, text-based HTML visual, but created a new slide specifically for this 3MT topic instead of copying the sample diagram.

The `pre3/3MT_auto_analyze/` folder contains tools and notes for analysing 3MT examples as multimodal texts. I used its general insight that strong 3MT talks can be understood through structure, accessibility, timing, and visual support, but the submitted slide itself is custom-made for my research direction.

## Storytelling Approach for a Non-specialist Audience

I will avoid technical terms such as "multimodal representation learning" or "visual-language alignment" during the talk. Instead, I will explain the idea in everyday language:

- The AI "watches" the ultrasound video.
- It "listens" to spoken questions or instructions.
- It "follows" how the probe moves.
- It "checks" whether important views are missing.

The story will follow the 3MT structure:

- Hook: ultrasound is not just taking a picture; it is a moving skill that depends on the hand, the eye, and experience.
- Problem: this makes ultrasound hard to learn and uneven across different users and clinics.
- Aim: my proposed research asks how AI can provide real-time guidance during scanning.
- Method in plain language: the AI learns from several sources of information, including video, language, reports, and probe movement.
- Expected impact: the system could help trainees learn faster, support clinicians in busy settings, and make high-quality ultrasound more accessible.

## Sources Used

- Professor Xiaoqing Guo homepage: https://guo-xiaoqing.github.io/
- UltraVision+ Lab: https://ultravisionlab.github.io/
- UltraVision+ Lab publications page: https://ultravisionlab.github.io/publications
- Sonomate article page: https://www.nature.com/articles/s41551-025-01578-3
