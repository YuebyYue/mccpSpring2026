# HTML Slide Generation Plan for 3D Gaussian Splatting Presentation

**Based on:** outline_generated.md (REVISED for 9 slides, non-specialist audience)  
**Target Duration:** 8 minutes (strict)  
**Total Slides:** 9 slides  
**Format:** Reveal.js HTML presentation  
**Style:** Dark background (SIGGRAPH-inspired), high-contrast visuals

---

## Overall Design Philosophy

### Visual Principles
- **Simplicity First:** ONE clear idea per slide
- **Visual Dominance:** Charts, diagrams, and images are the stars—text is minimal
- **Dark = Professional:** Dark background creates cinema-like feel (like SIGGRAPH presentations)
- **High Contrast:** Text must be extremely legible from distance (minimum 24pt)
- **Breathing Room:** Generous whitespace prevents overwhelming the viewer

### Color Palette (Dark Theme)
- **Background:** Very Dark Gray/Black (#1A1A1A or #0F172A)
- **Primary Text:** Pure White (#FFFFFF) or very light gray (#F0F0F0)
- **Accent Color:** Bright Cyan (#00D9FF) or Electric Blue (#2563EB) - stands out on dark
- **Highlight Color:** Warm Orange (#FF8C42) - for key numbers and emphasis
- **Success/Confirmatory:** Bright Green (#10B981) - for improvements, achievements
- **Secondary:** Light Gray (#CCCCCC) - for supporting text

### Typography
- **Headings:** 'Montserrat' Bold, 42-48pt
- **Subheadings:** 'Montserrat' SemiBold, 32-36pt
- **Body Text:** 'Open Sans' Regular, 24-28pt
- **Emphasis:** 'Open Sans' Bold for key terms
- **Code/Technical:** 'Fira Code' for any technical notation

---

## Slide-by-Slide Detailed Plan (9 Slides Total)

### Slide 1: Hook & Motivation (60 seconds)
**Purpose:** Capture attention with relatable problem

**Title:** "From Photos to 3D Walkthroughs"  
**Subtitle:** "Making Interactive Virtual Worlds Real"

**Content:**
- Split vision: Input photos on left → 3D rendered scene on right
- Minimal text: Just title and subtitle
- Question implicitly posed by the visual: "How do we do this?"

**Visual Elements:**
- Dominant central image showing 2-3 input photos transforming into an interactive 3D view
- Google Street View visual as comparison
- Arrows showing the transformation

**Design Notes:**
- Dark background makes the visual POP
- No technical explanation yet—pure visual hook
- Bright cyan or electric blue for subtitle

**Animation:**
- Photos appear left to right
- Transformation arrow animates
- 3D scene reveals on right

---

### Slide 2: The Problem (60 seconds)
**Purpose:** Establish the challenge clearly

**Title:** "Two Impossible Choices"

**Content:**
- **Option A: Beautiful But Slow**
  - High quality (⭐⭐⭐⭐⭐)
  - 48 HOURS to prepare
  - 0.071 fps (unusable)
  
- **Option B: Fast But Ugly**
  - Lower quality (⭐⭐⭐)
  - Quick (6-7 min)
  - 8-9 fps (jerky, uncomfortable)

- **The Question:** "Can we have BOTH: High quality AND real-time?"

**Visual Elements:**
- Two columns with large, glaring icons (slow turtle vs. pixelated mess)
- Bright orange X marks on both options
- Large question mark in center

**Design Notes:**
- Make the dilemma feel genuinely stuck
- Use color opposite: gray for "bad choice" areas, bright for question mark
- Keep numbers BIG and BOLD

---

### Slide 3: Existing Methods & The Gap (30 seconds)
**Purpose:** Set up what the paper solves

**Title:** "The Gap: Need ≥30 fps + High Quality"

**Content:**
- Horizontal timeline/spectrum:
  - Left: Mip-NeRF360 (quality, slow)
  - Middle: InstantNGP, Plenoxels (balanced but not enough)
  - Right: **EMPTY SPACE** with big question mark
  - Goal: "Real-time + High Quality"

**Visual Elements:**
- Scale from slow → fast (horizontal axis with speed icons)
- Quality indicator (vertical)
- Previous methods plotted; gap highlighted in accent color

**Design Notes:**
- Gap should visually stick out (bright accent color, empty space)
- Make it look like there's something *missing*

---

### Slide 4: Core Idea 1 — "Fuzzy Blobs" (50 seconds)
**Purpose:** Introduce 3D Gaussian concept intuitively

**Title:** "Idea 1: Represent with Blobs"

**Content:**
- Simple explanation: "Thousands of soft, fuzzy 3D ellipsoids"
- Key insight: "Simple geometry = computers can process FAST"
- Visual dominates ~ 70% of slide

**Visual Elements:**
- **Central graphic:** 3D visualization of colorful ellipsoids in space
  - Varying sizes, slight transparency
  - Some dense (detailed areas), some sparse (empty areas)
  - Natural-looking arrangement
- Callout: "1-5 million = enough for ANY scene"
- Icon comparison: Complex neural network (tangled) → Simple blob cloud (clean)

**Design Notes:**
- The blob visualization IS the message
- Keep text minimal
- Cyan accent for callout box

**Animation:**
- Blobs appear in stages: sparse → increasingly dense → final state
- Network → Blobs transformation

---

### Slide 5: Idea 2 — Smart Optimization (40 seconds)
**Purpose:** Show adaptive density control intuitively

**Title:** "Idea 2: Auto-Adjust Detail"

**Content:**
- Process: "System adds MORE blobs where needed, removes waste"
- Three-stage before/during/after visualization
- Key metric: "51 minutes to beat 48-HOUR previous best"

**Visual Elements:**
- Three-panel timeline (left → center → right):
  - Panel 1: Few sparse blobs (initial)
  - Panel 2: Partial density increase (mid-training)
  - Panel 3: Optimized dense regions (final)
- Number callout: "56× faster training!"
- Progress bars showing quality improvement

**Design Notes:**
- Arrow flow showing progression
- Color progression: Gray (start) → Yellow (adjusting) → Green (optimized)
- Emphasis on the speed victory

---

### Slide 6: Idea 3 — Real-Time Rendering (60 seconds)
**Purpose:** Deliver the breakthrough result

**Title:** "Idea 3: Render FAST"

**Content:**
- **THE NUMBERS:**
  - Previous best (InstantNGP): 9.2 fps
  - Previous best (Plenoxels): 8.2 fps
  - **THIS METHOD: 135 fps** ← Enormous highlight
  - Real-time threshold: 30 fps ✓

**Visual Elements:**
- Horizontal bar chart (previous methods small, this method HUGE):
  ```
  InstantNGP    ▁▃▅▇ 9.2 fps
  Plenoxels     ▁▃▅▇ 8.2 fps
  Real-time     ──────── 30 fps (threshold)
  
  THIS METHOD   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 135 fps 🏆
  ```
- Trophy or medal icon on winning bar
- Callout: "15× faster! Real-time interaction!"

**Design Notes:**
- Bar should be VISUALLY OVERWHELMING in size
- Use bright orange for the 135 fps number
- Green for achievement/success

**Animation:**
- Bars animate in sequence: competitors first (discouraging), then THIS METHOD scales enormously

---

### Slide 7: Visual Quality Proof (45 seconds)
**Purpose:** Show this LOOKS good

**Title:** "Still Looks Amazing"

**Content:**
- Side-by-side image comparison (2-3 images):
  - Ground truth
  - This method
  - (Optional: previous method for comparison)
- Caption: "High quality + Real-time speed"

**Visual Elements:**
- Three equal-sized image tiles
- Images should fill most of slide
- Subtle border/frame on images
- Brief labels below each (no technical metrics)

**Design Notes:**
- Minimal text—images speak for themselves
- High-resolution images (properly compressed)
- Dark background around images makes them dramatic

---

### Slide 8: Why It Matters (50 seconds)
**Purpose:** Connect to real-world significance

**Title:** "What This Enables"

**Content:**
- 2×2 grid of applications:
  1. **VR Icon** → "Photorealistic VR"
  2. **Game Controller** → "Real-world in games"
  3. **Architecture** → "Instant walkthroughs"
  4. **Film Camera** → "Virtual film sets"

**Visual Elements:**
- Four equal boxes in 2×2 grid
- Large, clear icons (Font Awesome or custom)
- One-word captions per box
- Each box slight glow or border in accent color

**Design Notes:**
- Keep each box simple (icon + one word)
- Eye-catching but not overwhelming
- Subtle connecting lines or background unity graphic

**Animation:**
- Boxes appear one by one as presenter explains applications

---

### Slide 9: My Takeaway + Thank You (60 seconds)
**Purpose:** Personal reflection + close Q&A

**Content (upper half):**
- **Research Lesson:** "Simplicity > Complexity: Solve the problem, don't follow trends"
- **Writing Lesson:** "Numbers > Vagueness: 135 fps is better than 'very fast'"

**Content (lower half):**
- Large, centered: "Thank You!"
- "Questions?"
- Key numbers as reminder:
  - 135 fps (real-time)
  - 51 min (vs 48 hours)
  - 56× faster

**Visual Elements:**
- Upper box: Two-column layout (Research | Writing) with checkmarks
- Lower area: Minimal, inviting
- Optional: QR code to paper
- Return to opening visual (photos → 3D)

**Design Notes:**
- Professional but warm
- Encourage questions (welcoming design)
- Key numbers in bright orange
- Generous whitespace

**Animation:**
- Lessons appear (left then right)
- "Thank You!" grows in size
- Optional: opening visual fades in background

---

## Technical Implementation Details

### Reveal.js Configuration

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>3D Gaussian Splatting Presentation</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4/dist/reveal.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4/dist/theme/black.css">
  <link rel="stylesheet" href="custom-styles.css">
</head>
<body>
  <div class="reveal">
    <div class="slides">
      <!-- Slides go here -->
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@4/dist/reveal.js"></script>
  <script>
    Reveal.initialize({
      controls: true,
      progress: true,
      center: true,
      hash: true,
      transition: 'fade',
      transitionSpeed: 'default',
      width: 1920,
      height: 1080,
      margin: 0.1
    });
  </script>
</body>
</html>
```

### Custom CSS (custom-styles.css) — Dark Theme

```css
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&family=Open+Sans:wght@400;600&display=swap');

/* Override Reveal.js defaults for DARK THEME */
.reveal {
  font-family: 'Open Sans', sans-serif;
  font-size: 28px;
  color: #F0F0F0;
  background-color: #0F172A;
}

.reveal-viewport {
  background: #0F172A;
}

.reveal h1, .reveal h2, .reveal h3 {
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  color: #FFFFFF;
  text-transform: none;
  margin-bottom: 0.5em;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
}

.reveal h1 { font-size: 52px; }
.reveal h2 { font-size: 40px; }
.reveal h3 { font-size: 32px; }

.reveal p { color: #E0E0E0; }

/* Accent colors for dark theme */
.accent { color: #00D9FF; font-weight: 600; }
.accent-orange { color: #FF8C42; font-weight: 600; }
.accent-green { color: #10B981; font-weight: 600; }

.highlight { 
  background-color: rgba(255, 140, 66, 0.2); 
  padding: 0.2em 0.5em;
  border-left: 3px solid #FF8C42;
}

/* Tables */
.reveal table {
  border-collapse: separate;
  border-spacing: 0 10px;
  background: rgba(255,255,255,0.05);
}

.reveal th {
  background-color: rgba(0, 217, 255, 0.2);
  color: #00D9FF;
  padding: 15px;
  font-weight: 600;
  border-bottom: 2px solid #00D9FF;
}

.reveal td {
  padding: 15px;
  color: #E0E0E0;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}

/* Callout boxes */
.callout {
  background-color: rgba(0, 217, 255, 0.1);
  border-left: 5px solid #00D9FF;
  padding: 20px;
  margin: 20px 0;
  border-radius: 8px;
}

/* Two-column layout */
.two-column {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  align-items: start;
}

/* Icon styling */
.icon {
  font-size: 48px;
  margin-bottom: 15px;
}

/* Bar chart styling */
.bar-chart {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin: 30px 0;
}

.bar {
  background: linear-gradient(90deg, rgba(0,217,255,0.3), rgba(0,217,255,0.1));
  padding: 10px 15px;
  border-radius: 8px;
  position: relative;
  transition: width 0.8s ease;
  color: #E0E0E0;
}

.bar.highlight {
  background: linear-gradient(90deg, #10B981, rgba(16,185,129,0.5));
  color: white;
  font-weight: 600;
}

.bar.record {
  background: linear-gradient(90deg, #FF8C42, rgba(255,140,66,0.5));
  color: white;
  font-weight: 700;
}

/* Image comparison */
.image-comparison {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.image-comparison img {
  width: 100%;
  border-radius: 8px;
  border: 2px solid rgba(0,217,255,0.3);
  box-shadow: 0 8px 16px rgba(0,0,0,0.5);
}

/* Grid layouts */
.grid-2x2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 30px;
  margin: 40px 0;
}

.grid-box {
  background: rgba(0,217,255,0.05);
  border: 2px solid rgba(0,217,255,0.3);
  border-radius: 8px;
  padding: 20px;
  text-align: center;
}

.grid-box .icon {
  font-size: 64px;
}

/* Link styling */
.reveal a {
  color: #00D9FF;
}

.reveal a:hover {
  color: #FF8C42;
}
```

### Folder Structure

```
presentation/
├── index.html
├── css/
│   └── custom-styles.css
├── images/
│   ├── gaussian-visualization.png
│   ├── performance-chart.png
│   ├── quality-comparison.jpg
│   ├── applications/
│   │   ├── vr-icon.svg
│   │   ├── gaming-icon.svg
│   │   ├── architecture-icon.svg
│   │   └── film-icon.svg
│   └── input-photos/
├── js/
│   └── (Reveal.js plugins if needed)
└── README.md
```

### Animation Guidelines

- **Slide Transitions:** Use 'fade' for professional feel
- **Element Animations:** Use Reveal.js fragments for step-by-step reveals
  ```html
  <p class="fragment">First point appears</p>
  <p class="fragment">Second point appears</p>
  ```
- **Chart/Graph Animations:** Consider using CSS transitions or simple JavaScript
- **Timing:** Animations should be quick (0.3-0.5s) to maintain momentum

### Accessibility Considerations

- **Alt Text:** Every image must have descriptive alt text
- **Color Contrast:** Minimum 4.5:1 ratio for all text
- **Keyboard Navigation:** Arrow keys, space bar work out of the box with Reveal.js
- **Screen Reader:** Use semantic HTML (`<section>`, `<h1>`, etc.)
- **Font Size:** Minimum 24pt ensures readability from distance

### Image Sources & Preparation

**Images Needed:**
1. Input photos example (create or use from paper)
2. 3D Gaussian visualization (from paper Fig. 1 or create)
3. Performance comparison charts (create from paper data)
4. Quality comparison images (from paper with attribution)
5. Application icons (Font Awesome or custom SVG)
6. Timeline/process diagrams (create in Figma or similar)

**Image Optimization:**
- Format: WebP for photos, SVG for icons/diagrams
- Resolution: 1920×1080 maximum for slides
- Compression: Balance quality vs. file size
- Attribution: Include "Source: Kerbl et al. 2023" for paper images

---

## Delivery Tips Mapped to 9 Slides

| Slide | Content | Delivery Focus | Pacing | Emphasis |
|-------|---------|----------------|--------|----------|
| 1 | Hook & Motivation | Hook with visual (photos→3D) | Warm, inviting | Let the visual do the work |
| 2 | The Problem | Emphasize the dilemma | Measured, show frustration | Two impossible choices |
| 3 | The Gap | Frame the question | Slow, let sink in | Empty space = opportunity |
| 4 | Blobs Concept | Simplicity is brilliant | Moderate energy | Show wonder at elegance |
| 5 | Auto-Tuning | Efficiency magic | Clear, methodical | Emphasize 56× faster |
| 6 | Real-Time Speed | **BIG REVEAL** | Dramatic, pause for effect | 135 fps is massive! |
| 7 | Visual Quality | Visual confidence | Quiet, let images speak | Quality is maintained ✓ |
| 8 | Applications | Audience connection | Friendly, relatable | "Your world" tone |
| 9 | Reflection + Q&A | Genuine personal | Thoughtful, inviting | Open, encouraging |

---

## Pre-Presentation Checklist (9-Slide Version)

### Technical Setup:
- [ ] Test presentation on actual display/projector
- [ ] Verify dark theme renders correctly (not washed out)
- [ ] Check all animations work smoothly and don't distract
- [ ] Verify all images load and look sharp
- [ ] Test keyboard navigation (arrow keys, space)
- [ ] Have backup PDF version ready
- [ ] Check font rendering on actual screen (web fonts loaded)

### Timing Verification:
- [ ] Run through with timer (MUST be 7:45-8:00, not longer)
  - Slide 1: 60 sec (hook)
  - Slide 2: 60 sec (problem)
  - Slide 3: 30 sec (gap)
  - Slide 4: 50 sec (blobs)
  - Slide 5: 40 sec (tuning)
  - Slide 6: 60 sec (speed) ← **PAUSE here**
  - Slide 7: 45 sec (quality)
  - Slide 8: 50 sec (applications)
  - Slide 9: 60 sec (reflection + Q&A)

### Content Preparation:
- [ ] Memorize opening hook (first 30 seconds)
- [ ] Memorize closing (last 15 seconds)
- [ ] Practice the "135 fps" reveal (dramatic pause!)
- [ ] Know where to pause for effect
- [ ] Prepare for likely questions:
  1. "How does it compare to NeRF?"
  2. "What's the catch/limitation?"
  3. "Can it do dynamic scenes?"
  4. "When will this be available?"
  5. "What hardware is needed?"

### Physical Preparation:
- [ ] Note cards with ONLY key transitions (not script!)
- [ ] Water bottle available
- [ ] Comfortable, professional clothing
- [ ] Arrive 15 minutes early to test equipment
- [ ] Practice standing in presentation area (practice stage awareness)
- [ ] Avoid reading from notes—use them for transitions only

### Visual & Language Checks:
- [ ] No technical jargon remains unexplained
- [ ] All numbers are accurate and memorable
- [ ] Dark background is ACTUALLY dark (not gray)
- [ ] Accent colors (cyan/orange) pop well
- [ ] All text is readable from distance (test from 10 feet away)
- [ ] Transitions between slides feel natural (practice verbal cues)

---

## Post-Generation Testing Plan

1. **Self-Review (30 min):**
  - Click through all 9 slides in full-screen mode
  - Check if each slide's message is clear within 3 seconds
  - Verify text readability from distance (simulate classroom view)
  - Test all animations (must support message, not distract)

2. **Timing Rehearsal (2-3 times):**
  - Present with timer using the 9-slide allocation
  - Confirm total is 7:45-8:00
  - Mark slides where pacing drifts or explanations become too technical
  - Trim wording on those slides immediately

3. **Non-Specialist Validation (critical):**
  - Present to one listener with no graphics background
  - Ask: "What are the three main ideas you remember?"
  - Ask: "Do you understand why this work matters?"
  - Revise any slide that fails this comprehension check

4. **Final Polish:**
  - Remove remaining jargon or explain it visually
  - Keep each slide to minimal text (visual-first)
  - Ensure dark theme contrast remains high on projector
  - Export backup PDF

---

## Success Metrics for 9-Slide Presentation

The presentation will be successful if:
- ✓ Timing is 7:45-8:00 (strict 8-minute limit respected)
- ✓ Non-specialists understand the core problem (quality vs speed trade-off)
- ✓ THREE main ideas are clear: blobs, auto-tuning, fast rendering
- ✓ Audience remembers key numbers: 135 fps, 51 minutes, 56× faster
- ✓ Visual quality comparison impresses viewers
- ✓ Real-world applications feel relevant and exciting
- ✓ Personal reflection is genuine and concise
- ✓ Slides look professional with dark background and high contrast
- ✓ No technical jargon confuses non-specialists
- ✓ Q&A questions show engagement with concepts (not methods)

---

# Next Steps

1. **Generate HTML:** Use this plan to create `index.html` and `custom-styles.css`
2. **Source Images:** Gather or create all required visuals
3. **Build Slides:** Implement each slide according to specifications
4. **Test & Iterate:** Run through presentation, make adjustments
5. **Practice:** Rehearse 3-5 times before actual presentation
6. **Deliver with Confidence!**

**End of Slide Plan**
