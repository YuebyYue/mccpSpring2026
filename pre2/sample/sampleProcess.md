# Sample poster process and requirement alignment

This document explains how the sample poster materials were generated from the paper source in `literature/YW*/2308.04079/GaussianSplattingVisualization.html` and how the resulting poster structure aligns with the `pre2` assessment instructions and the HKBU Department of Mathematics poster guidelines.

---

## 1. Source and scope

- **Paper topic:** *3D Gaussian Splatting for Real-Time Radiance Field Rendering*.
- **Paper source used for this sample workflow:** `literature/YW*/2308.04079/GaussianSplattingVisualization.html`.
- **Important constraint:** all content extraction for this sample process should be based on the Gaussian Splatting visualization file above, not on any other paper or earlier sample.
- **Instructions used:** materials in `pre2/`, especially the poster task description and `pre2/demo/institutionalGuidelines/math.md`.

---

## 2. Process followed

1. **Read the source visualization**
   - Use `literature/YW*/2308.04079/GaussianSplattingVisualization.html` as the single paper-content source.
   - Extract the macro-level organization already identified in the visualization:
     - Introduction
     - Related Work
     - Method
     - Experiments
     - Discussion and Conclusion

2. **Identify the paper's core message**
   - Problem: existing radiance field methods achieve strong visual quality, but real-time rendering for full scenes at 1080p remains difficult.
   - Gap: prior methods face a speed-quality trade-off and do not achieve the target real-time display rate for unbounded scenes.
   - Main solution: the paper combines three technical elements:
     - 3D Gaussian scene representation
     - interleaved optimization with density control
     - fast differentiable rendering using tile-based rasterization
   - Main outcome: state-of-the-art visual quality with competitive training time and real-time rendering performance.

3. **Map paper content to poster sections**
   - **Introduction**: explain novel-view synthesis, why the problem matters, and the specific rendering-speed gap.
   - **Methodology**: summarize the three technical elements from the paper source:
     - 3D Gaussian representation
     - optimization and adaptive density control
     - fast differentiable rendering
   - **Results**: highlight evaluation dimensions named in the source:
     - PSNR
     - SSIM
     - training time
     - rendering FPS
     - benchmark datasets and baselines
   - **Discussion / Conclusion**: restate contributions, limitations, applications, and future directions.
   - **References**: include the paper itself and any baseline systems explicitly mentioned in the poster.
   - **Layman's summary**: add a short non-technical explanation for readers outside graphics / vision.

4. **Adapt the paper to the poster format**
   - Reduce long method explanations into short bullets and figure placeholders.
   - Preserve the paper's problem-solution-results logic so the poster can be scanned quickly.
   - Keep quantitative claims visible, especially real-time rendering, 1080p, training efficiency, and evaluation metrics.
   - Reserve visual areas for diagrams, pipeline summaries, and benchmark plots because the guidelines expect a balanced text-visual layout.

5. **Apply layout and guideline constraints**
   - Use a portrait poster structure with a strong header, section blocks, and a layman's summary near the top.
   - Keep section names close to the academic structure in the source while simplifying them for poster readability.
   - Use sans-serif headings and serif body text to match the departmental guidance.
   - Prepare the HTML so it can later be exported to print-ready PDF or preview PNG.

6. **Deliverables produced in `pre2/sample`**
   - `samplePoster.html`: the sample poster draft in HTML.
   - `sampleProcess.md`: this workflow and alignment note.
   - `outlineScript.md`: a short presentation outline and speaking script.

---

## 3. How the sample aligns with requirements

### MCCP6020 poster presentation requirements

| Requirement | Alignment |
|-------------|-----------|
| Summarize topic, objectives, methodology, findings, and conclusions | The sample workflow maps the Gaussian Splatting source into Introduction, Methodology, Results, and Discussion / Conclusion. |
| Poster format instead of full paper | Long paper sections are condensed into poster-friendly bullets, short paragraphs, and figure placeholders. |
| Clear organization and readable presentation | The poster uses distinct sections, concise statements, and a top-down reading flow. |
| Appropriate use of visuals | The workflow explicitly reserves space for method diagrams, benchmark plots, and result comparisons. |

### HKBU Department of Mathematics poster guidelines

| Requirement | Alignment |
|-------------|-----------|
| Portrait academic poster with formal header | The sample poster format uses a top header with title, presenter, supervisor, and department placement. |
| Required core sections | The workflow includes Introduction, Methodology, Results, Discussion / Conclusion, and References. |
| Layman's summary for non-specialists | The sample includes a separate plain-language summary near the top. |
| Large, readable headings and body text | The HTML poster is structured so font sizes can be scaled for final PDF export and printing. |
| Balance between text and visuals | The workflow avoids turning the poster into a text wall and expects figure/table areas to carry a substantial part of the explanation. |
| Accessibility and comprehensibility | The source paper is highly technical, so the workflow deliberately simplifies the message around problem, method, and impact. |

---

## 4. Content decisions taken from the Gaussian Splatting source

The following details come from `literature/YW*/2308.04079/GaussianSplattingVisualization.html` and should drive the poster content:

- **Introduction content**
  - Radiance field methods are important for novel-view synthesis.
  - The concrete niche is real-time rendering for unbounded or complete scenes at 1080p.
  - The poster should keep the quantitative gap visible instead of describing the problem only in general terms.

- **Methodology content**
  - The poster should present the method as three coordinated components, because the source explicitly frames the contribution that way.
  - Those components are:
    - 3D Gaussian representation
    - optimization with adaptive density control
    - fast differentiable rendering

- **Results content**
  - The sample should use the evaluation categories named in the source:
    - image quality metrics such as PSNR and SSIM
    - rendering speed in FPS
    - training time
    - benchmark datasets such as NeRF synthetic, Mip-NeRF360, Tanks and Temples, and Deep Blending
    - comparisons with baselines such as Mip-NeRF360, InstantNGP, and Plenoxels

- **Discussion content**
  - The closing section should mention impact, limitations, and future work.
  - The source highlights representation size, memory requirements, real-time applications, and directions such as dynamic scenes or interactive editing.

---

## 5. Gaps and next steps for a polished submission

- Ensure `samplePoster.html` is also updated so its topic and technical details match the Gaussian Splatting paper source consistently.
- Replace all placeholders with actual presenter, supervisor, logo, and department details.
- Insert real figures or recreated diagrams based on the Gaussian Splatting source instead of generic placeholders.
- Check the final exported PDF against the required page size, font size, and visual balance rules before submission.
- If students revise the poster with an AI agent, keep `sampleProcess.md` updated so the documented workflow still matches the actual poster content.

---

## 6. References

- `literature/YW*/2308.04079/GaussianSplattingVisualization.html` — the paper-content source used for this sample process.
- `pre2/createPoster.md` — task description for generating the sample poster materials.
- `pre2/demo/institutionalGuidelines/math.md` — HKBU Mathematics poster guideline reference.
- `pre2/materials/pre2AssessmentRubrics.md` — poster presentation assessment guidance, if used in the local course materials.
