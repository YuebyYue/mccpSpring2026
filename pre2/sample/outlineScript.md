# Outline and script for poster presentation (2-3 minutes)

Use this outline and script with the Gaussian Splatting sample poster. The content is based on `literature/YW*/2308.04079/GaussianSplattingVisualization.html` and should stay consistent with `sampleProcess.md`.

---

## Presentation outline

1. **Opening (15-20 s)**
   - Introduce the topic and the one-line takeaway.

2. **Problem and gap (25-30 s)**
   - Explain novel-view synthesis and why real-time 1080p rendering is difficult for full scenes.

3. **Method (40-50 s)**
   - Present the three-part solution:
     - 3D Gaussian scene representation
     - optimization with density control
     - fast differentiable rendering

4. **Results (25-30 s)**
   - Summarize the evaluation dimensions and the main outcome: high quality with real-time performance.

5. **Closing (10-15 s)**
   - State the impact and invite questions.

---

## Script (about 2 min 30 s)

**Opening**  
"Hello. This poster is about **3D Gaussian Splatting for Real-Time Radiance Field Rendering**. The main takeaway is that the paper achieves both **high visual quality** and **real-time 1080p rendering**, which is a major goal in novel-view synthesis."

**Problem and gap**  
"Radiance field methods are very effective for generating new views of a scene from many input images. However, a common problem is the trade-off between quality and speed. Existing methods may look good, but for large or unbounded scenes they are often too slow for real-time display. The paper identifies this as a concrete gap: current approaches do not achieve real-time rendering at 1080p for full scenes."

**Method**  
"The solution is built from three connected ideas. First, the scene is represented using **3D Gaussians**, initialized from Structure-from-Motion points. Second, the method uses **interleaved optimization and density control** so the representation becomes more accurate during training. Third, it uses **fast differentiable rendering** with tile-based rasterization and visibility-aware splatting, which makes the rendering pipeline efficient on the GPU."

**Results**  
"The method is evaluated on datasets such as **NeRF synthetic, Mip-NeRF360, Tanks and Temples, and Deep Blending**. The paper reports image-quality metrics like **PSNR and SSIM**, along with **training time** and **rendering FPS**. The overall result is that Gaussian Splatting delivers strong visual quality while also reaching real-time rendering performance."

**Closing**  
"So the contribution of this work is not only a new representation, but a complete pipeline that makes high-quality scene rendering practical in real time. This is important for applications such as VR, AR, and interactive 3D scene capture. Thank you, and I welcome questions."

---

## Possible Q&A

- **What is novel-view synthesis?**  
  It means generating new camera views of a scene from a set of existing images.

- **Why use Gaussians?**  
  They provide a flexible scene representation that works well with efficient splatting-based rendering.

- **What makes this method fast?**  
  The rendering stage is designed for GPU efficiency through tile-based rasterization and visibility-aware processing.

- **What are the main evaluation metrics?**  
  PSNR, SSIM, training time, and rendering FPS.

- **What are the limitations?**  
  The paper still notes issues such as representation size, memory requirements, and the need for extensions to more complex dynamic scenes.

---

## Timing checklist

- [ ] Keep the talk within 2-3 minutes.
- [ ] Point to the layman's summary, methodology section, and result placeholders while speaking.
- [ ] Prepare one short answer about datasets, one about the three-part method, and one about practical applications.
