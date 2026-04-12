# Audio Script for Sample Poster

This script is for `pre2/sample/samplePoster.html`.

- **Poster title:** *3D Gaussian Splatting for Real-Time Radiance Field Rendering*
- **Main version length:** about **2 min 10 s to 2 min 20 s** at a normal student speaking pace
- **Short backup version:** about **1 min 40 s to 1 min 50 s**

---

## Main Recording Script

Hello everyone. Today I am going to introduce my poster, **3D Gaussian Splatting for Real-Time Radiance Field Rendering**.

This work is about **novel-view synthesis**, which means generating new views of a scene from a set of input images. This is an important task in computer graphics and computer vision, because it is useful for applications like virtual reality, augmented reality, and interactive 3D scene capture.

The main problem is that previous radiance field methods often face a **trade-off between quality and speed**. Some methods can produce very realistic images, but they are too slow to render in real time. This is especially difficult for **large scenes** and for **1080p rendering**.

This paper tries to solve that problem with three main ideas.

First, it represents the scene using many **3D Gaussians**. These Gaussians are initialized from **Structure-from-Motion points**, so the model starts with a basic scene structure.

Second, the method uses **optimization with density control**. During training, the system can refine the Gaussians and adjust their distribution, so important regions can be represented more accurately.

Third, the paper designs a **fast differentiable rendering method** based on **tile-based rasterization** and **visibility-aware splatting**. This makes the rendering process much more efficient on the GPU.

In the results section, the method is tested on benchmark datasets such as **NeRF synthetic**, **Mip-NeRF360**, **Tanks and Temples**, and **Deep Blending**. It is compared with strong baselines like **Mip-NeRF360**, **InstantNGP**, and **Plenoxels**.

The evaluation uses metrics such as **PSNR**, **SSIM**, **training time**, and **rendering FPS**. The main result is that Gaussian Splatting achieves strong visual quality while also reaching **real-time rendering at 1080p**, which is the key contribution of this paper.

Of course, the method still has some limitations. For example, **memory usage** can still be high, and there can be artifacts in regions that are not well observed. But overall, this paper is very influential because it shows that high quality and real-time performance do not have to be treated as opposites.

In conclusion, this work presents a practical solution to the speed-quality trade-off in novel-view synthesis by combining a Gaussian-based scene representation, adaptive optimization, and fast GPU rendering.

Thank you for listening.

---

## Short Backup Script

Hello everyone. This poster is about **3D Gaussian Splatting for Real-Time Radiance Field Rendering**.

The paper studies **novel-view synthesis**, which means generating new scene views from existing images. A major challenge in this area is the **speed-quality trade-off**. Earlier methods may produce high-quality images, but they are often too slow for real-time use, especially for full scenes at **1080p**.

This paper addresses that problem in three steps. First, it represents the scene with **3D Gaussians**. Second, it improves the representation through **optimization with density control**. Third, it uses a **fast GPU rendering pipeline** with tile-based rasterization and visibility-aware splatting.

The method is evaluated on several benchmark datasets and compared with methods such as **Mip-NeRF360**, **InstantNGP**, and **Plenoxels**. The main metrics are **PSNR**, **SSIM**, **training time**, and **FPS**.

The key takeaway is that Gaussian Splatting achieves strong visual quality together with **real-time rendering performance**, which makes it an important contribution in this field.

Thank you.

---

## Delivery Tips

- Speak slowly and clearly. Do not rush the technical terms.
- Pause slightly after these phrases:
  - **novel-view synthesis**
  - **speed-quality trade-off**
  - **three main ideas**
  - **real-time rendering at 1080p**
- If a sentence feels long when recording, split it into two shorter sentences instead of reading it in one breath.
- For a more natural student style, stress meaning, not every word.

---

## Easy Chinese Meaning Guide

You can remember the structure like this:

1. **What is the topic?**  
   This paper is about generating new views of a 3D scene from many photos.

2. **What is the problem?**  
   Earlier methods usually had a trade-off between image quality and rendering speed.

3. **What is the solution?**  
   The paper uses 3D Gaussians, density control, and a fast GPU rendering pipeline.

4. **What is the result?**  
   It achieves strong visual quality and real-time 1080p rendering.

5. **What is the conclusion?**  
   This paper makes real-time, high-quality radiance field rendering much more practical.
