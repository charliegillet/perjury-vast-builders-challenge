Furthermore, we observe an interesting point: at the most severe low-light level (L5), some VLMs achieve accuracy lower than that of GPT-4 (Blind-LLM baseline), which operates solely on textual input without any visual information. This indicates that for images under extreme degradation, the models are unable to effectively utilize these visual information, leading to a poorer understanding of semantic information compared to relying purely on language priors.
To contextualize the severe-degradation results, we additionally compute a random-choice baseline on the full DarkQA evaluation set. The overall chance accuracy is 33.35%, due to the mixed candidate-set sizes across question families. Thus, model accuracies around 30–35% at L4/L5 indicate near chance-level performance, and should not be interpreted as evidence of successful visual understanding.
##### Impact of illumination drop and sensor noise

To understand the robustness of VLMs against visual illumination degradation, we first observe their performance under two types of low-light simulation: (1) pure EV drop and (2) physics-motivated noise modeling.
As shown in Fig. [6](https://arxiv.org/html/2512.24985#S4.F6 "Fig. 6 ‣ LLIE model ‣ IV-B Baseline Models ‣ IV EXPERIMENTS ‣ DarkQA: Benchmarking Vision-Language Models on Visual-Primitive Question Answering in Low-Light Indoor Scenes")-(b), both degradations consistently lead to a significant decrease in VLM accuracy. Notably, the introduction of sensor noise compounds this decline, resulting in a more pronounced performance drop compared to pure EV reduction. This confirms that VLMs are indeed highly sensitive to such visual degradation, with noise being a critical factor.
##### Effectiveness of low-light image enhancement (LLIE) pre-processing

Given the observed performance degradation, we investigate whether pre-processing low-light images with a state-of-the-art Low-Light Image Enhancement (LLIE) model \[ [20](https://arxiv.org/html/2512.24985#bib.bib7 "")\] can mitigate these issues. We apply LLIE models to the noise-added low-light images before feeding them into the VLMs. As illustrated in Fig. [6](https://arxiv.org/html/2512.24985#S4.F6 "Fig. 6 ‣ LLIE model ‣ IV-B Baseline Models ‣ IV EXPERIMENTS ‣ DarkQA: Benchmarking Vision-Language Models on Visual-Primitive Question Answering in Low-Light Indoor Scenes")-(c), this approach yields mixed results. While we observe a significant accuracy improvement at more severe low-light levels (L4 and L5), performance decreases at moderate levels (L1–L3). This unstable behavior highlights the challenge of reliably enhancing low-light images across different levels of degradation. While current LLIE models enhance perceptual quality, the results suggest that current LLIE models may be biased to certain degradation levels as in Fig. [6](https://arxiv.org/html/2512.24985#S4.F6 "Fig. 6 ‣ LLIE model ‣ IV-B Baseline Models ‣ IV EXPERIMENTS ‣ DarkQA: Benchmarking Vision-Language Models on Visual-Primitive Question Answering in Low-Light Indoor Scenes")-(d).
##### Question-wise analysis

To gain a more granular understanding of the performance decline, we further analyze the accuracy degradation across different question types, as shown
in Fig. [7](https://arxiv.org/html/2512.24985#S4.F7 "Fig. 7 ‣ LLIE model ‣ IV-B Baseline Models ‣ IV EXPERIMENTS ‣ DarkQA: Benchmarking Vision-Language Models on Visual-Primitive Question Answering in Low-Light Indoor Scenes"). While most categories exhibit a steady decline, we observe a critical phenomenon in two specific types: “Room Type Recognition” and “Object Attribute - Color”. For these categories, the VLM accuracy drops below that of the GPT-4 (Blind-LLM) baseline at severe degradation levels (L5 for the former, and L4 and L5 for the latter).
---
Our DarkQA benchmarks a diverse set of vision–language models (VLMs), including both open- and closed-source systems \[ [15](https://arxiv.org/html/2512.24985#bib.bib14 ""), [16](https://arxiv.org/html/2512.24985#bib.bib12 ""), [17](https://arxiv.org/html/2512.24985#bib.bib11 ""), [18](https://arxiv.org/html/2512.24985#bib.bib13 ""), [19](https://arxiv.org/html/2512.24985#bib.bib15 "")\].
We also evaluate four low-light image enhancement (LLIE) models\[ [20](https://arxiv.org/html/2512.24985#bib.bib7 "")\]\[ [21](https://arxiv.org/html/2512.24985#bib.bib27 ""), [22](https://arxiv.org/html/2512.24985#bib.bib28 ""), [23](https://arxiv.org/html/2512.24985#bib.bib29 "")\] as preprocessing baselines.
Our evaluation yields two observations.
First, all tested VLMs show a clear performance decline as the images degrade.
Second, LLIE preprocessing is method- and severity-dependent: it can improve QA accuracy at some degradation levels, but is not uniformly beneficial and does not recover well-lit performance.
Together, these results show that current VLMs remain brittle under low-light corruption, and that perceptual enhancement alone is insufficient as a general solution, motivating robustness-oriented evaluation and method development.
![Refer to caption](https://arxiv.org/html/2512.24985v4/low_light_image_synthesis_2_rb.png)

Fig. 2: Low-light synthesis pipeline with disentangled illumination and noise factors.
To generate controlled low-light inputs for our benchmark, we adopt an ISP-inspired unprocessing and noise formulation from prior work \[ [24](https://arxiv.org/html/2512.24985#bib.bib16 ""), [25](https://arxiv.org/html/2512.24985#bib.bib18 "")\]. Crucially, we produce _paired_ variants for each original image to disentangle failure sources in VLM-based QA: (a) a physics-based branch (top) that unprocesses sRGB to Bayer RAW, injects four noise components in RAW, and then applies EV drop and gamma compression; and (b) a noise-free branch (bottom) that applies the same EV drop in linear RGB without noise injection. This paired design enables separate evaluation of performance degradation due to illumination reduction versus sensor noise. The bottom-left panel summarizes the sRGB→\\rightarrowRAW unprocessing steps, and the bottom-right panel visualizes the four noise components (shot, read, row-pattern, and quantization noise) as independent signals. The small red boxes in the read and row noise examples indicate zoomed-in crops for visualization.
## II RELATED WORK

### II-AEgocentric Question Answering Benchmarks

Egocentric question answering evaluates visual-language reasoning from first-person observations. Prior benchmarks study large-scale egocentric video understanding \[ [5](https://arxiv.org/html/2512.24985#bib.bib30 "")\], episodic-memory QA \[ [6](https://arxiv.org/html/2512.24985#bib.bib31 "")\], task-level reasoning \[ [7](https://arxiv.org/html/2512.24985#bib.bib32 "")\], long-form video QA \[ [8](https://arxiv.org/html/2512.24985#bib.bib33 "")\], and scene-text-aware assistance \[ [9](https://arxiv.org/html/2512.24985#bib.bib34 "")\]. However, none of these benchmarks evaluates VLMs under controlled dark or low-light visual degradation. Unlike prior work \[ [26](https://arxiv.org/html/2512.24985#bib.bib35 "")\], our benchmark evaluates VLM robustness under controlled, multi-level synthesized low-light degradation.
Embodied QA benchmarks such as EmbodiedQA \[ [10](https://arxiv.org/html/2512.24985#bib.bib3 "")\], ScanQA \[ [11](https://arxiv.org/html/2512.24985#bib.bib24 "")\], and OpenEQA \[ [12](https://arxiv.org/html/2512.24985#bib.bib8 "")\] are closely related, as they evaluate agents that answer questions about embodied or 3D environments. Yet they focus on navigation, 3D scene QA, or environment-level memory rather than isolating low-light visual robustness.
---
Title:

Content selection saved. Describe the issue below:

Description:

![](https://arxiv.org/static/base/1.0.1/images/icons/smileybones-small.svg)arXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×

[License: arXiv.org perpetual non-exclusive license](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2512.24985v4 \[cs.CV\] 12 May 2026

# DarkQA: Benchmarking Vision-Language Models on    Visual-Primitive Question Answering in Low-Light Indoor Scenes

Yohan Park
Affiliation: Yohan Park and Tae-Hyun Oh are with Korea Advanced Institute of Science and Technology (KAIST), Daejeon 34141, South Korea (e-mail: john.a.park@kaist.ac.kr, taehyun.oh@kaist.ac.kr).Hyunwoo Ha
Affiliation: Hyunwoo Ha and Wonjun Jo are with Pohang University of Science and Technology (POSTECH), Pohang 37673, South Korea (e-mail: hyunwooha@postech.ac.kr, jo1jun@postech.ac.kr).Wonjun Jo
Affiliation: Hyunwoo Ha and Wonjun Jo are with Pohang University of Science and Technology (POSTECH), Pohang 37673, South Korea (e-mail: hyunwooha@postech.ac.kr, jo1jun@postech.ac.kr).Tae-Hyun Oh
††thanks: Corresponding author: Tae-Hyun Oh.
This work has been submitted to the IEEE for possible publication. Copyright may be transferred without notice, after which this version may no longer be accessible.Affiliation: Yohan Park and Tae-Hyun Oh are with Korea Advanced Institute of Science and Technology (KAIST), Daejeon 34141, South Korea (e-mail: john.a.park@kaist.ac.kr, taehyun.oh@kaist.ac.kr).
###### Abstract

Vision Language Models (VLMs) are increasingly adopted as central reasoning modules for embodied agents. Existing benchmarks evaluate their capabilities under ideal, well-lit conditions, yet robust 24/7 operation demands performance under a wide range of visual degradations, including low-light conditions at night or in dark environments–a core necessity that has been largely overlooked.
To address this underexplored challenge, we present DarkQA, an open-source benchmark for evaluating perceptual primitives under multi-level low-light conditions in embodied scenarios.
DarkQA evaluates single-view egocentric observations across controlled degradation levels, isolating low-light perceptual failures before they are entangled with complex embodied tasks.
The benchmark contains 9.4K deterministically generated and verifiable question–image pairs spanning five visual-primitive families. A key design feature of DarkQA is its physical fidelity:
visual degradations are modeled in linear RAW space, simulating physics-based illumination drop and sensor noise followed by an ISP-inspired rendering pipeline; we further validate the synthesis against real paired low-light camera data.
We evaluate representative VLMs and Low-Light Image Enhancement (LLIE) preprocessing methods.
Results show consistent VLM degradation under low illumination and sensor noise, while LLIE provides severity-dependent but unstable recovery.
We demonstrate the utility of DarkQA by evaluating a wide range of state-of-the-art VLMs and Low-Light Image Enhancement (LLIE) models, and systematically reveal VLMs’ limitations when operating under these challenging visual conditions.
Our code and benchmark dataset will be released upon acceptance.
Project website: https://darkqa-benchmark.github.io

## I INTRODUCTION

Advances in vision-language models (VLMs) have significantly enhanced robotic perception and decision-making, supporting semantic scene understanding \[ [1](https://arxiv.org/html/2512.24985#bib.bib2 "")\], spatial reasoning \[ [2](https://arxiv.org/html/2512.24985#bib.bib19 "")\], and vision-language-action (VLA) policies \[ [3](https://arxiv.org/html/2512.24985#bib.bib20 ""), [4](https://arxiv.org/html/2512.24985#bib.bib21 "")\].
However, household robots are often intended for 24/7 operation, which means they will frequently encounter low-light scenarios, such as nighttime, entering dark rooms or power blackouts.
---
We keep the original scenes, trajectories, viewpoints, questions, and answers fixed, apply our physics-based low-light synthesis only to the RGB observations in episodic memory, and evaluate GPT-4o with the original LLM-Match protocol.
This experiment is intended as a complementary validation. DarkQA is designed as a controlled visual-primitive QA benchmark, but OpenEQA allows us to check whether the same low-light degradation trend also appears in an open-ended episodic-memory QA format without predefined answer choices. Since all non-illumination factors are kept fixed, the consistent drop in LLM-Match suggests that low-light degradation affects not only our controlled visual-primitive QA setting, but also broader embodied QA settings built on episodic visual observations.
Table [II](https://arxiv.org/html/2512.24985#S4.T2 "TABLE II ‣ IV-D Realism of physics-motivated low-light synthesis pipeline ‣ IV EXPERIMENTS ‣ DarkQA: Benchmarking Vision-Language Models on Visual-Primitive Question Answering in Low-Light Indoor Scenes") shows that GPT-4o drops from 75.0% at L0 to 66.8% at L4, while human performance from 32 HM3D scenes drops from 85.1% to 50.7%.
This result supports our main finding: low-light degradation harms not only visual-primitive QA, but also open-ended embodied QA.
## V CONCLUSION

We introduce DarkQA, a new benchmark designed to address an overlooked and critical regime in VLM evaluation: the lack of systematic analysis for embodied scenario in low-light conditions. Using a physically-grounded low-light image synthesis pipeline, we create a reproducible benchmark to measure VLM robustness against realistic visual degradations.
Our findings reveal that current VLMs are brittle in the dark, and that seemingly straightforward solutions like LLIE pre-processing can yield unstable results.
While our benchmark reveal the vulnerabilities of VLMs to low-light conditions, a detailed failure analysis remains a valuable direction.
## References

- \[1\]S. Peng, K. Genova, C. Jiang, A. Tagliasacchi, M. Pollefeys, T. Funkhouser, et al. (2023)Openscene: 3d scene understanding with open vocabularies.
In IEEE/CVF Conference on Computer Vision and Pattern Recognition,
pp. 815–824.
Cited by: [§I](https://arxiv.org/html/2512.24985#S1.p1.1 "I INTRODUCTION ‣ DarkQA: Benchmarking Vision-Language Models on Visual-Primitive Question Answering in Low-Light Indoor Scenes").
- \[2\]J. Yang, S. Yang, A. W. Gupta, R. Han, L. Fei-Fei, and S. Xie (2025)Thinking in space: how multimodal large language models see, remember, and recall spaces.
In IEEE/CVF Conference on Computer Vision and Pattern Recognition,
pp. 10632–10643.
Cited by: [§I](https://arxiv.org/html/2512.24985#S1.p1.1 "I INTRODUCTION ‣ DarkQA: Benchmarking Vision-Language Models on Visual-Primitive Question Answering in Low-Light Indoor Scenes").
- \[3\]B. Zitkovich, T. Yu, S. Xu, P. Xu, T. Xiao, F. Xia, J. Wu, P. Wohlhart, S. Welker, A. Wahid, et al. (2023)Rt-2: vision-language-action models transfer web knowledge to robotic control.
In Conference on Robot Learning,
pp. 2165–2183.
Cited by: [§I](https://arxiv.org/html/2512.24985#S1.p1.1 "I INTRODUCTION ‣ DarkQA: Benchmarking Vision-Language Models on Visual-Primitive Question Answering in Low-Light Indoor Scenes").
- \[4\]D. Driess, F. Xia, M. S. M. Sajjadi, C. Lynch, A. Chowdhery, A. Wahid, J. Tompson, Q. Vuong, T. Yu, W. Huang, et al. (2023)PaLM-e: an embodied multimodal language model.
External Links: 2303.03378Cited by: [§I](https://arxiv.org/html/2512.24985#S1.p1.1 "I INTRODUCTION ‣ DarkQA: Benchmarking Vision-Language Models on Visual-Primitive Question Answering in Low-Light Indoor Scenes").
- \[5\]K. Grauman, A. Westbury, E. Byrne, Z. Chavis, A. Furnari, R. Girdhar, J. Hamburger, H. Jiang, M. Liu, X. Liu, et al. (2022)Ego4d: around the world in 3,000 hours of egocentric video.
In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition,
pp. 18995–19012.