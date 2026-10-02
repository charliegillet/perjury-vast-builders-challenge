![Refer to caption](https://arxiv.org/html/2609.31823v1/img/human_det_graphs.png)Figure 3: HPC Robustness: Accuracy across DORI-calibrated distances under different lighting conditions. The left, middle, and right subplots correspond to day, night-vision (NV), and night settings, respectively. With each subplot, distance increases from left to right, corresponding to progressively more difficult evaluation conditions.
To demonstrate a deeper robustness investigation via metadata stratification analysis, we analyze how degradation patterns vary with illumination by stratifying by lighting conditions. We report human-presence classification (HPC) performance over distances separately for day, night-vision, and night settings in [table7](https://arxiv.org/html/2609.31823#A1.T7 "In A.5.2 HPC Performance Over Lightings ‣ A.5 Additional Results ‣ Appendix A Technical Appendices and Supplementary Material ‣ SynDORBench: Evaluating LVLM Perceptual Robustness Under Physically Constrained Visibility Conditions") and [fig.3](https://arxiv.org/html/2609.31823#A1.F3 "In A.5.2 HPC Performance Over Lightings ‣ A.5 Additional Results ‣ Appendix A Technical Appendices and Supplementary Material ‣ SynDORBench: Evaluating LVLM Perceptual Robustness Under Physically Constrained Visibility Conditions"). Under day conditions, nearly all LVLMs outperform YOLO11x, with the exception of SmolVLM2-256M-Video-Instruct and SmolVLM2-500M-Video-Instruct. This indicates that, in well-lit environments, LVLMs above roughly 1B parameters are generally capable of surpassing conventional detectors in terms of HPC and suggests that in general, LVLMs may have better perception capabilities. When inspecting how parameters affect performance, as seen in [fig.3](https://arxiv.org/html/2609.31823#A1.F3 "In A.5.2 HPC Performance Over Lightings ‣ A.5 Additional Results ‣ Appendix A Technical Appendices and Supplementary Material ‣ SynDORBench: Evaluating LVLM Perceptual Robustness Under Physically Constrained Visibility Conditions"), YOLO and SVLMs degrade sharply at 23m, meaning that already in ideal lighting conditions, SVLMs and YOLO perform worse than our proposed failure threshold (80%) based on reported operational performance of models \[ [37](https://arxiv.org/html/2609.31823#bib.bib15 ""), [30](https://arxiv.org/html/2609.31823#bib.bib16 ""), [55](https://arxiv.org/html/2609.31823#bib.bib17 ""), [39](https://arxiv.org/html/2609.31823#bib.bib18 "")\].
In contrast, night conditions lead to a substantial collapse in performance. No model attains an F1-score of 0.8, levels that many models comfortably achieve during the day, highlighting the severe degradation induced by low-light environments. In such scenarios, all evaluated LVLMs become effectively non-operational.
Encouragingly, applying night-vision enhancement yields partial recovery in model performance. Several models show modest but consistent gains, including gemma-3-4b-it and gemma-3n-E2B-it, suggesting that algorithmic illumination compensation is beneficial for vision-language understanding.
Across all lighting conditions and distances, the Gemma3 family: Gemma3 and Gemma3n, consistently achieves the strongest HPC performance, and specifically, gemma-3-4b-it and gemma-3n-E2B-it achieve the best overall performance. Interestingly, the smaller variants tend to outperform their larger counterparts, indicating that model scale within this family does not linearly translate to better HPC robustness. However, for the night lighting conditions, the Mid-sized LVLMs show promise in beating gemma-3-4b-it and gemma-3n-E2B-it, this could be due to the higher reasoning capabilities of the larger models to understand the contextual clues.
---
| Model | 5.4 m | 10.8m | 23.0 m |
|  | Acc | F1 | Acc | F1 | Acc | F1 |
| YOLO11x | 73.92 | 50.17 | 65.38 | 50.36 | 50.29 | 42.98 |
| SmolVLM2-256M-Video-<br>Instruct | 10.02 | 9.63 | 13.47 | 12.68 | 22.70 | 18.69 |
| SmolVLM2-500M-Video-<br>Instruct | 23.20 | 20.23 | 26.51 | 24.04 | 27.19 | 22.08 |
| InternVL3-1B-hf | 87.77 | 59.63 | 85.69 | 64.58 | 83.97 | 68.13 |
| Perception-LM-1B | 69.77 | 48.21 | 62.64 | 49.11 | 45.94 | 39.89 |
| SmolVLM2-2.2B-Instruct | 80.84 | 55.07 | 75.89 | 57.64 | 66.51 | 56.22 |
| Perception-LM-3B | 75.76 | 50.83 | 71.76 | 53.77 | 58.80 | 48.37 |
| Qwen2.5-VL-3B-Instruct | 66.70 | 45.49 | 64.00 | 48.86 | 54.75 | 45.16 |
| gemma-3-4b-it | 94.66 | 50.44 | 92.91 | 54.04 | 85.66 | 67.68 |
| gemma-3n-E2B-it | 87.10 | 75.78 | 86.29 | 65.27 | 88.87 | 72.12 |
| SVLM (mean) | 66.20 | 46.14 | 64.35 | 47.78 | 59.38 | 48.71 |
| Phi-4-multimodal-instruct | 84.97 | 56.59 | 83.42 | 62.74 | 79.53 | 65.76 |
| LLaVAction-7B | 81.80 | 55.96 | 74.70 | 57.33 | 57.88 | 50.01 |
| LLaVA-NeXT-Video-7B-<br>hf | 81.99 | 54.84 | 73.15 | 54.76 | 54.90 | 47.17 |
| Molmo-7B-D-0924 | 84.63 | 57.68 | 80.61 | 60.82 | 70.76 | 59.06 |
| Qwen2.5-VL-7B-Instruct | 86.13 | 58.41 | 84.75 | 63.86 | 80.24 | 64.99 |
| gemma-3n-E4B-it | 87.77 | 59.08 | 86.73 | 65.05 | 87.76 | 70.40 |
| InternVL3-8B-hf | 85.45 | 58.08 | 83.13 | 62.67 | 71.66 | 59.84 |
| MVLM (mean) | 84.68 | 57.24 | 80.93 | 61.03 | 71.82 | 59.61 |
| gpt-4o-mini-2024-07-18 | 82.72 | 55.79 | 77.87 | 58.72 | 69.60 | 59.03 |

##### Discussion

Interestingly, while MVLMs achieve the strongest overall group performance, robustness does not scale monotonically with parameter count. Several compact SVLMs remain highly competitive and, in some cases, outperform larger models under degraded visibility conditions. This suggests that multimodal robustness depends not only on model scale, but also on factors such as vision encoder design, visual alignment quality, and robustness of multimodal feature integration. These findings indicate that physically grounded perception may require architectural properties distinct from those optimized by conventional semantic reasoning benchmarks.
Another notable observation is the substantial robustness gap between LVLMs and traditional detector-based systems. YOLO11x exhibits rapid degradation under long-range and heterogeneous illumination conditions, even falling below operational reliability thresholds at relatively favorable visibility regimes. In contrast, LVLMs retain stronger discriminability under the same conditions, potentially because multimodal architectures can leverage broader contextual and semantic priors rather than relying solely on local appearance cues. This suggests that modern LVLMs may offer a more resilient perception framework for low-information environments where conventional detectors become brittle.
## 5 Conclusion

In this paper, we introduced SynDORBench, the first physically grounded benchmark for evaluating LVLM perceptual robustness under DORI-calibrated imaging conditions. Unlike existing multimodal benchmarks that primarily assess semantic reasoning under ideal visual settings, SynDORBench systematically studies how multimodal perception degrades as visual evidence deteriorates under controlled physical constraints.
Through large-scale evaluation across open-source LVLMs, commercial LVLMs, and detector-based baselines, we show that pixel density and imaging conditions play a central role in determining multimodal perceptual reliability. Our experiments further demonstrate that modern LVLMs substantially outperform traditional detector-based pipelines under long-range and low-visibility conditions, while several compact open-source models achieve robustness comparable to larger commercial systems.
Overall, SynDORBench establishes physically grounded multimodal evaluation as an important and previously underexplored dimension of LVLM assessment.
---
|  | day | night | night-vision |
| --- | --- | --- | --- |
| radius(m) | 5.4 | 10.8 | 23 | avg | 5.4 | 10.8 | 23 | avg | 5.4 | 10.8 | 23 | avg |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| metrics | acc | acc | acc | acc | acc | f1-score | acc | f1-score | acc | f1-score | acc | f1-score | acc | f1-score | acc | f1-score | acc | f1-score | acc | f1-score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| YOLO11x | 95.06 | 85.42 | 53.49 | 77.99 | 62.80 | 50.51 | 54.29 | 51.65 | 47.00 | 44.96 | 54.70 | 49.04 | 63.90 | 51.25 | 56.43 | 53.36 | 50.39 | 49.11 | 56.91 | 51.24 |
| SmolVLM2-256M-Video-Instruct | 9.88 | 8.54 | 7.79 | 8.74 | 12.48 | 12.44 | 15.20 | 15.14 | 27.02 | 23.47 | 18.23 | 17.02 | 7.71 | 7.46 | 16.68 | 15.03 | 33.31 | 25.37 | 19.23 | 15.95 |
| SmolVLM2-500M-Video-Instruct | 23.49 | 26.40 | 11.53 | 20.47 | 7.82 | 7.57 | 16.87 | 15.20 | 33.11 | 24.88 | 19.27 | 15.88 | 38.29 | 34.09 | 36.24 | 36.05 | 36.93 | 31.02 | 37.16 | 33.72 |
| Internvl3-1B-hf | 99.95 | 99.77 | 95.09 | 98.27 | 78.20 | 61.48 | 74.94 | 68.32 | 71.96 | 71.49 | 75.03 | 67.10 | 85.17 | 67.41 | 82.35 | 75.46 | 84.87 | 84.16 | 84.13 | 75.68 |
| Perception-LM-1B | 90.80 | 78.79 | 40.33 | 69.97 | 43.88 | 37.99 | 39.05 | 38.65 | 35.92 | 29.44 | 39.62 | 35.36 | 74.64 | 59.07 | 70.07 | 64.61 | 61.58 | 61.50 | 68.76 | 61.73 |
| SmolVLM2-2.2B-Instruct | 95.73 | 92.02 | 71.57 | 86.44 | 64.79 | 51.92 | 57.95 | 54.62 | 54.37 | 53.72 | 59.04 | 53.42 | 82.01 | 64.39 | 77.71 | 70.39 | 73.60 | 73.24 | 77.77 | 69.34 |
| Perception-LM-3B | 99.33 | 95.42 | 70.20 | 88.31 | 60.82 | 49.23 | 52.96 | 50.57 | 46.53 | 44.37 | 53.44 | 48.06 | 67.14 | 53.43 | 66.91 | 61.92 | 59.67 | 59.50 | 64.58 | 58.29 |
| Qwen2.5-VL-3B-Instruct | 94.10 | 86.68 | 63.12 | 81.30 | 39.42 | 34.89 | 39.56 | 39.10 | 40.44 | 36.20 | 39.81 | 36.73 | 66.57 | 53.09 | 65.78 | 61.03 | 60.69 | 60.57 | 64.35 | 58.23 |
| gemma-3-4b-it | 99.98 | 99.95 | 100.00 | 99.97 | 92.67 | 51.26 | 90.71 | 57.49 | 75.59 | 48.54 | 86.32 | 52.43 | 91.33 | 50.05 | 88.07 | 54.64 | 81.40 | 54.49 | 86.93 | 53.06 |
| gemma-3n-E2B-it | 100.00 | 99.72 | 98.75 | 99.49 | 75.08 | 58.11 | 76.42 | 70.11 | 79.49 | 79.08 | 77.00 | 69.10 | 86.22 | 69.23 | 82.74 | 75.75 | 88.38 | 87.61 | 85.78 | 77.53 |
| phi4-multimodal-instruct | 99.93 | 98.51 | 86.10 | 94.85 | 72.85 | 57.54 | 71.59 | 65.89 | 75.70 | 75.44 | 73.38 | 66.29 | 82.13 | 62.25 | 80.16 | 72.71 | 76.79 | 75.57 | 79.70 | 70.18 |
| LLaVAction-7B | 97.20 | 89.92 | 58.74 | 81.95 | 65.07 | 52.11 | 56.78 | 53.67 | 47.70 | 45.84 | 56.52 | 50.54 | 83.14 | 66.49 | 77.40 | 70.99 | 67.20 | 67.19 | 75.91 | 68.22 |
| LLaVA-NeXT-Video-7B-hf | 96.69 | 87.48 | 56.86 | 80.35 | 68.88 | 54.73 | 59.94 | 56.22 | 52.77 | 51.95 | 60.53 | 54.30 | 80.39 | 60.65 | 72.02 | 61.40 | 55.07 | 53.31 | 69.16 | 58.45 |
| Molmo-7B-D-0924 | 99.81 | 97.36 | 78.82 | 92.00 | 69.85 | 55.49 | 66.56 | 61.68 | 59.48 | 59.29 | 65.30 | 58.82 | 84.24 | 67.58 | 77.90 | 71.46 | 73.99 | 73.82 | 78.71 | 70.96 |
| Qwen2.5-VL-7B-Instruct | 99.93 | 99.57 | 93.80 | 97.77 | 81.24 | 64.19 | 79.15 | 72.43 | 75.66 | 75.42 | 78.68 | 70.68 | 77.23 | 61.07 | 75.53 | 69.27 | 71.26 | 71.14 | 74.67 | 67.16 |
| gemma-3n-E4B-it | 99.98 | 99.55 | 99.07 | 99.53 | 76.46 | 59.28 | 78.29 | 71.80 | 81.71 | 81.18 | 78.82 | 70.75 | 86.87 | 67.97 | 82.35 | 73.46 | 82.49 | 80.25 | 83.90 | 73.89 |
| internVL3-8B-hf | 99.98 | 98.97 | 79.58 | 92.84 | 72.49 | 57.46 | 70.42 | 64.91 | 62.32 | 62.27 | 68.41 | 61.54 | 83.87 | 66.79 | 80.01 | 73.37 | 73.09 | 72.95 | 78.99 | 71.04 |
| gpt-4o-mini-2024-07-18 | 98.97 | 95.82 | 73.84 | 89.54 | 69.25 | 55.05 | 63.21 | 58.91 | 60.34 | 60.20 | 64.26 | 58.05 | 79.94 | 62.59 | 74.59 | 68.31 | 74.61 | 74.42 | 76.38 | 68.44 |
---
Since utility depends on semantic proximity rather than exact lexical reproduction, we evaluate using E5Score \[ [56](https://arxiv.org/html/2609.31823#bib.bib3 "")\] to quantify sentence-level semantic alignment, following the same embedding-similarity paradigm as CLIPScore \[ [19](https://arxiv.org/html/2609.31823#bib.bib26 "")\] and SigLIPScore which is commonly used for Image-Text alignment \[ [38](https://arxiv.org/html/2609.31823#bib.bib4 "")\], but modifying to fit our Text-to-Text setting. We use E5Score to avoid score bias due to the LVLMs using the vision encoders as the scoring metrics (e.g., CLIP, SigLIP). To improve interpretability, we report a distance-based z-score that highlights relative performance differences across models. Additionally, we obtain a human baseline from one non-expert annotator on a uniformly random sample of 300 instances.
### A.4 Computational Resources

Raw image rendering was conducted on 4 NVIDIA A6000 GPUs, totaling approximately 535.7 GPU hours. Night-vision enhanced image creation was conducted on the CPU, totaling approximately 19 CPU hours. Experimental evaluations were conducted on 2–3 NVIDIA L40S GPUs, depending on availability. Each model required approximately 4 GPU hours across both tasks, totaling approximately 72 GPU hours for the full evaluation across 18 models.
### A.5 Additional Results

#### A.5.1 Action Recognition Robustness Across Distances

Table 6: Action recognition performance across DORI distances. Mean E5Score and corresponding z-score per distance. Best z-scores are in bold.
| Model | 5.4 m | 10.8 m | 23.0 m |
| Non-Expert Human | 0.94 | 0.91 | 0.83 |
| SmolVLM2-256M-Video-Instruct | 0.78 (-1.45) | 0.77 (-1.39) | 0.77 (-1.15) |
| SmolVLM2-500M-Video-Instruct | 0.80 (-0.76) | 0.79 (-0.75) | 0.78 (-0.69) |
| Internvl3-1B-hf | 0.81 (-0.23) | 0.80 (-0.43) | 0.78 (-0.72) |
| Perception-LM-1B | 0.77 (-1.87) | 0.76 (-1.78) | 0.75 (-1.72) |
| SmolVLM2-2.2B-Instruct | 0.84 (0.93) | 0.83 (0.98) | 0.83 (1.09) |
| Perception-LM-3B | 0.77 (-1.98) | 0.76 (-1.98) | 0.75 (-1.83) |
| Qwen2.5-VL-3B-Instruct | 0.83 (0.69) | 0.82 (0.61) | 0.82 (0.65) |
| gemma-3-4b-it | 0.80 (-0.59) | 0.80 (-0.52) | 0.78 (-0.63) |
| gemma-3n-E2B-it | 0.84 (1.04) | 0.84 (1.14) | 0.83 (1.13) |
| SVLM (mean) | 0.80 (-0.79) | 0.80 (-0.65) | 0.79 (-0.39) |
| Phi4-multimodal-instruct | 0.84 (0.90) | 0.83 (0.95) | 0.83 (1.12) |
| LLaVAction-7B | 0.84 (0.89) | 0.83 (0.95) | 0.83 (0.98) |
| LLaVA-NeXT-Video-7B-hf | 0.82 (-0.02) | 0.80 (-0.23) | 0.78 (-0.64) |
| Molmo-7B-D-0924 | 0.82 (0.23) | 0.82 (0.39) | 0.82 (0.51) |
| Qwen2.5-VL-7B-Instruct | 0.84 (0.88) | 0.83 (0.88) | 0.83 (0.90) |
| gemma-3n-E4B-it | 0.83 (0.57) | 0.82 (0.64) | 0.82 (0.59) |
| internVL3-8B-hf | 0.82 (0.34) | 0.81 (0.17) | 0.81 (0.18) |
| MVLM (mean) | 0.83 (0.44) | 0.82 (0.59) | 0.82 (0.53) |
| gpt-4o-mini-2024-07-18 | 0.83 (0.44) | 0.82 (0.39) | 0.81 (0.23) |

We evaluate all LVLMs on SynDORBench-54k and then average over non-distance factor similarly to before, so that the reported scores reflect the effect of distance alone. Results are detailed in [table6](https://arxiv.org/html/2609.31823#A1.T6 "In A.5.1 Action Recognition Robustness Across Distances ‣ A.5 Additional Results ‣ Appendix A Technical Appendices and Supplementary Material ‣ SynDORBench: Evaluating LVLM Perceptual Robustness Under Physically Constrained Visibility Conditions"). Across all three distances, we observe a monotonic decrease in performance as radius increases, indicating that action recognition is strongly distance-sensitive and degrades as pixel density falls. For group means, the MLVLMs exceed that of the SVLMs at all radii, suggesting that parameter count continues to provide a net advantage for open-ended action classification when visual detail becomes sparse.