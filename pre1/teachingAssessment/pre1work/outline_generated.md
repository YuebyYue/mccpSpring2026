# Presentation Outline: 3D Gaussian Splatting for Real-Time Radiance Field Rendering

**Paper:** Kerbl, B., Kopanas, G., Leimkühler, T., & Drettakis, G. (2023). *3D Gaussian Splatting for Real-Time Radiance Field Rendering*. ACM Transactions on Graphics (SIGGRAPH 2023).

**Presentation Time:** 8 minutes (strict timing)  
**Target Slides:** 9 slides  
**Audience:** Non-specialists (no graphics/vision background)  
**Assessment:** Oral Presentation Assessment 1 – Research Story-telling by Experienced Writers

**Design Style:** Dark background, high-contrast visuals (SIGGRAPH-inspired)  
**Focus:** THREE core ideas, emphasis on intuitive understanding, minimal technical jargon

---

## Opening (~1 minute)

### Hook: The Magic Mirror Problem
> *Imagine you want to create a virtual replica of your room so realistic that you can view it from any angle on your computer—like having a magic mirror that can show you views you never photographed. This is what "novel view synthesis" aims to achieve.*

**Transition:** "Today I want to share with you a breakthrough paper in computer graphics that makes this possible in real-time—fast enough that you could walk through a virtual scene as smoothly as playing a video game."

### Context Setting
- **Field:** Computer Graphics and Computer Vision—specifically, the challenge of creating 3D representations from 2D photographs
- **Why it matters:** Applications range from virtual reality, video games, to architectural visualization and even film production
- **The central challenge:** Creating photorealistic 3D scenes that can be viewed from any angle, but doing so *fast enough* for real-time interaction

**Transition Statement:** "Let me explain what problem this paper tackles and why previous solutions weren't quite good enough."

### Presenter Notes:
- **Delivery:** Speak with enthusiasm. Make eye contact with the audience when introducing the "magic mirror" metaphor
- **Visual Aid:** Slide 1 should show a simple before/after comparison—a few photos of a scene transforming into a full 3D walkthrough
- **Language Strategy:** Avoid jargon like "novel view synthesis" initially; build up to it with the metaphor
- **Rubric Alignment:** The metaphor makes content accessible to non-specialists (Content appropriate to non-specialist audience)

---

## Section 1: Introduction to the Article (~1.5 minutes)

### What is the Research About?
**Plain Language Summary:** This paper solves a problem in computer graphics: how to create a 3D representation of a scene from photographs that is both *beautiful to look at* and *fast enough to interact with in real-time*.

### The Gap or Problem
**Previous Solutions Had a Trade-Off:**
1. **High Quality Methods (like Mip-NeRF360):**
   - Produce stunning visuals
   - BUT: Take up to 48 hours to train or prepare
   - AND: Render slowly (0.071 frames per second)—far too slow for real-time use
   
2. **Fast Methods (like InstantNGP or Plenoxels):**
   - Train quickly (minutes instead of hours)
   - Render at 8-10 frames per second
   - BUT: Lower visual quality
   - AND: Still not truly "real-time" (we need ≥30 fps at 1080p resolution)

**The Gap:** *No existing method could achieve both high quality AND real-time rendering for complex, real-world scenes.*

### Research Question/Objective
**Central Question:** Can we create a method that matches the best visual quality while achieving real-time rendering speeds—without sacrificing either?

**Specific Target:** Render at ≥30 frames per second at 1080p resolution (high-definition quality) while maintaining visual quality equal to or better than the best existing methods.

### Presenter Notes:
- **Content Strategy:** Use the comparison table metaphor: "Imagine a table with two columns—quality and speed. Previous methods excelled at one but not both."
- **Signaling Language:** "The key problem the researchers identified is..." / "This paper addresses a specific gap..."
- **Visual Aid:** Slide 2 should show a simple comparison chart: Method A (high quality, slow) vs Method B (lower quality, fast) vs "Ideal Solution" (high quality, fast)
- **Avoid Jargon:** Instead of "radiance field rendering," say "creating realistic 3D views from photos"
- **Rubric Alignment:** Explanations are in accessible language with clear metaphors (Content entirely appropriate to non-specialist audience)

---

## Section 2: Key Findings (~2 minutes) — THREE Core Ideas

### Idea 1: Use Fuzzy Blobs to Represent the Scene
**The Concept (Intuitive):**
Instead of using complex neural networks, the researchers discovered something simpler works better: represent the scene using thousands of "fuzzy 3D blobs"—imagine tiny, slightly transparent ellipsoids (like softballs or eggs) scattered throughout the space.

**Why Simple is Better:**
- These blobs are *easy* for computers to handle (unlike neural networks which are like black boxes)
- More blobs appear in detailed areas; fewer in empty space
- The system learns where to place them automatically during training

**Key Numbers:**
- Only 1-5 million blobs needed per scene (very efficient)
- Training starts from simple camera calibration data (no expensive preprocessing)

### Idea 2: System Auto-Tunes Detail Where Needed
**The Concept (Intuitive):**
During training, the system doesn't just freeze in place—it intelligently adds more blobs where detail is needed and removes unhelpful ones. It's like automatically adjusting your focus based on what matters most.

**Why This Works:**
- The system learns where to add detail (edges, textures) and where it's unnecessary (blank walls)
- Result: Optimal quality with minimal waste

**The Advantage:**
- Achieves quality comparable to methods that take 48 hours... in just 51 minutes!
- Matches the slowest, highest-quality method but 56× faster

### Idea 3: Ultra-Fast Rendering at Real-Time Speed
**The Concept (Intuitive):**
A new algorithm renders these blobs SO fast that you can interact with the 3D scene smoothly—like playing a video game, not waiting for images to load.

**Why This Matters:**
- **Previous best-case:** 0.071 fps (impossible to interact with—1 frame every 14 seconds!)
- **Fast but lower quality:** 8-9 fps (jerky, unpleasant)
- **This method:** 93-135 fps (smooth, real-time) ← **This is the breakthrough!**
- Achieves ≥30 fps (real-time standard) ✓
- Maintains high visual quality ✓

### Presenter Notes:
- **Key Focus:** 
  - Slide 4: Simple 3D blob visualization (the protagonist)
  - Slide 5: Before/during/after timeline of optimization
  - Slide 6: Dramatic FPS comparison bar chart (brief moment—let the visual speak)
- **Language Simplification:** 
  - Replace "anisotropic covariance" with "blob shape"
  - Replace "differentiable rendering" with "fast calculation"
  - Replace "density control" with "smart adjustment"
- **Delivery Emphasis:** 
  - Idea 1: Show wonder at simplicity ("surprisingly simple")
  - Idea 2: Show satisfaction at efficiency ("doing more with less")
  - Idea 3: Show excitement at speed (pause after "93-135 fps!")
- **Rubric Alignment:** Concrete evidence (numbers), accessible language (no jargon), three clear takeaways
- **Timing:** Aim for 1:50 total (leaving buffer)

---

## Section 3: Significance of the Research (~1 minute) — Real-World Impact

**Why This Matters:**

This breakthrough enables applications that were previously too slow:
- **Virtual Reality:** Photorealistic VR walkthroughs (not cardboard-quality fake)
- **Gaming:** Import real-world scenes directly into games
- **Architecture:** Show clients their building designs instantly (not as static renderings)
- **Film:** Hollywood virtual production techniques become accessible to smaller studios

**Broader Insight:**
This work teaches us that sometimes *simpler* representations work better than newer, fancier techniques. The researchers didn't follow the trend of complex neural networks—they thought about what actually works.

### Presenter Notes:
- **Connection:** Link each application to audience familiar experience (show brief enthusiasm)
- **Signaling Language:** "This enables..." / "Real-world applications include..." / "The broader lesson..."
- **Visual Aid:** Slide 8: 2×2 grid of application icons with one-word captions
- **Delivery:** Quick run through applications; focus on making audience feel the significance
- **Timing:** 1:00 exactly
- **Rubric Alignment:** Connect to real concerns (applications), show broader understanding

---

## Section 4: Personal Reflection — My Takeaways (~1 minute)

### What This Paper Teaches Me as a Researcher

**Research Design Lesson:**
The authors didn't follow the trend—they asked *"What actually solves this problem?"* rather than *"What's the newest technology?"* I learned to prioritize solving the problem over following trends.

**Writing Lesson:**
Every claim is backed by numbers: "135 fps," "51 minutes," "56× faster." Vague phrases like "much faster" disappear. The paper introduces "three key elements" in the abstract and returns to them throughout. This structure creates clarity.

### Presenter Notes:
- **Personal Voice:** Genuine reflection, not rote summary. Use "I learned..." / "I'll apply..."
- **Brevity:** Don't overexplain—audience will appreciate quick insights
- **Evidence:** Point to one specific example from the paper (the "three key elements" phrase)
- **Delivery:** Thoughtful, modest tone. This is personal insight, not teaching
- **Timing:** 1:00 exactly
- **Rubric Alignment:** In-depth but concise reflection with specific evidence

---

## Closing (~0.5 minutes)

### Summary: The Key Takeaway
**Main Point:**
"This paper achieves what many thought was a decade away—real-time, photorealistic rendering of captured scenes from photos. By rethinking scene representation using 3D Gaussians and designing all components (representation, optimization, rendering) to work together, the authors deliver both quality AND speed."

### Why This Matters Beyond Graphics
"More broadly, this work reminds us that innovation doesn't always require more complexity. Sometimes, choosing the *right* representation—one that fits both your problem and your computational constraints—matters more than using the newest techniques."

### Thank You & Invite Questions
"Thank you for listening. I'd be happy to answer any questions about the paper, the method, or how I plan to apply these insights to my own research."

### Presenter Notes:
- **Concluding Phrases:** "To sum up..." / "In conclusion..." / "The key takeaway is..."
- **Delivery:** Slow down for the closing statement. Make eye contact with multiple audience members
- **Body Language:** Open posture, smile
- **Visual Aid:** Final slide with key numbers prominently displayed and a "Thank you" / "Questions?" message
- **Transition to Q&A:** Pause for 2-3 seconds after "questions" to allow audience to formulate thoughts
- **Rubric Alignment:** Well-structured with clear logical flow; effective use of transition statements (Well-structured with clear logical flow)

---

## Appendix: Presenter's Delivery Checklist

### Before the Presentation:
- [ ] Practice timing each section (aim for 80% of target time to allow buffer)
- [ ] Prepare note cards with key points and transitions—NOT full sentences
- [ ] Memorize opening and closing statements
- [ ] Practice pronouncing technical terms: "Gaussian," "anisotropic," "radiance," "covariance"
- [ ] Anticipate 3-5 likely questions and prepare brief answers

### During the Presentation:
- [ ] **Body Language:** Stand with open posture, move naturally, use hand gestures to emphasize points
- [ ] **Eye Contact:** Look at different sections of the audience; don't fixate on slides or notes
- [ ] **Voice Modulation:** Vary pitch and pace; pause after important points
- [ ] **Emphasis:** Stress key numbers (30 fps, 135 fps, 10×) and transition phrases
- [ ] **Breathing:** Pause to breathe between sections—helps pacing and reduces "um/uh"
- [ ] **Slides:** Refer to visuals but don't read from them—use them as visual support

### Q&A Session:
- [ ] Listen actively to the full question before answering
- [ ] Repeat or paraphrase if unclear
- [ ] Answer directly and concisely
- [ ] Admit if you don't know something: "That's an excellent question—I'd need to review that specific aspect of the paper more closely"
- [ ] Connect answers back to your main points when possible

---

## Academic Language Bank for Presentation

### Opening & Transitions
- "Today, I'd like to share..."
- "This brings me to..."
- "Let me turn now to..."
- "Building on this point..."
- "This leads us to consider..."

### Introducing Research
- "The research addresses..."
- "The authors investigate..."
- "The study focuses on..."
- "The central challenge is..."

### Explaining Findings
- "The findings reveal..."
- "The data indicates..."
- "The results demonstrate..."
- "Notably, the researchers found..."

### Discussing Significance
- "This research contributes to the field by..."
- "The implications of these findings suggest..."
- "This work is particularly important because..."
- "The broader impact extends to..."

### Personal Reflection
- "What struck me most about this paper is..."
- "I found particularly insightful..."
- "This has influenced my thinking about..."
- "I plan to apply this approach by..."

### Concluding
- "To summarize..."
- "In conclusion..."
- "The key takeaway is..."
- "This work demonstrates that..."

---

# End of Presentation Outline

**Next Steps:**
1. Review this outline and provide feedback in `feedback.md`
2. After feedback incorporation, proceed to HTML slide generation using `slide_plan.md`
3. Practice delivery using this outline as a guide—NOT as a script to read verbatim
