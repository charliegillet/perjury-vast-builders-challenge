Title:

Content selection saved. Describe the issue below:

Description:

![](https://arxiv.org/static/base/1.0.1/images/icons/smileybones-small.svg)arXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×

[License: arXiv.org perpetual non-exclusive license](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2301.11198v2 \[eess.IV\] 30 Jan 2023

# I-24 MOTION:    An instrument for freeway traffic science

Derek Gloudemans13, Yanbing Wang2, Junyi Ji2, Gergely Zachar2, Will Barbour2, Daniel B. Work12Affiliation: 1Vanderbilt University Department of Computer Science
Affiliation: 2Vanderbilt University Department of Civil and Environmental Engineering
Affiliation: 3derek.gloudemans@vanderbilt.edu

###### Abstract

The Interstate-24 MObility Technology Interstate Observation Network (I-24 MOTION) is a new instrument for traffic science located near Nashville, Tennessee. I-24 MOTION consists of 276 pole-mounted high-resolution traffic cameras that provide seamless coverage of approximately 4.2 miles I-24, a 4-5 lane (each direction) freeway with frequently observed congestion. The cameras are connected via fiber optic network to a compute facility where vehicle trajectories are extracted from the video imagery using computer vision techniques. Approximately 230 million vehicle miles of travel occur within I-24 MOTION annually. The main output of the instrument are vehicle trajectory datasets that contain the position of each vehicle on the freeway, as well as other supplementary information, vehicle dimensions, and class. This article describes the design and creation of the instrument, and provides the first publicly available datasets generated from the instrument. The datasets published with this article contains at least 4 hours of vehicle trajectory data for each of 10 days. As the system continues to mature, all trajectory data will be made publicly available at i24motion.org.

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/first_image_v2_small.png)Fig. 1: Time-space diagram for four hours of I-24 W morning rush hour traffic on Nov 25, 2022, generated from I-24 MOTION vehicle trajectories. x-axis: time of day (HH:MM); y-axis roadway postmile (mi). Postmile decreases for travelers in the westbound direction. A typical congestion pattern is shown with frequent oscillatory traffic observed; and recurring waves travel upstream relative to the direction of traffic at 12-13 mph. The names of interchanges and overpasses appear on the right. The figure inset shows a zoomed in portion of the data which is 0.25 mi in length and 4 min in duration.

## I Introduction

Transportation science is undergoing a digital transformation in which increasingly automated vehicles are being developed and deployed on roadways, changing the fundamental physics of traffic flow. Even a small number of automated vehicles can have a direct impact on the macroscopic behavior of traffic flow, highlighting the need to monitor and observe traffic flows across microscopic and macroscopic scales.

At the same time new vehicles are being introduced that may alter the flow, new technologies are advancing that ease the ability to capture the behavior of traffic at scales that were impossible to realize even a few years ago. For example, automated vehicles now transmit critical contextual data about the surrounding environment on the vehicle Controller Area Network (CAN), allowing opportunities to measure vehicle spacings and relative velocities, which were not possible using only GPS devices in phones and vehicles. Drone technologies have reached a degree of maturity that now facilitate camera based monitoring over roadways at impressive spatial scales. While these advancements offer opportunities to accelerate traffic flow science, there are still direct needs for monitoring the individual and collective behavior of vehicles over long temporal and spatial resolutions.

Recognizing the impact of freeway trajectory data collection efforts such as NGSIM \[ [1](https://arxiv.org/html/2301.11198v2#bib.bib1 "")\] and HighD \[ [2](https://arxiv.org/html/2301.11198v2#bib.bib2 "")\] (see also Table [I](https://arxiv.org/html/2301.11198v2#S1.T1 "TABLE I ‣ I Introduction ‣ I-24 MOTION: An instrument for freeway traffic science")), and emerging urban datasets exemplified by pNEUMA \[ [3](https://arxiv.org/html/2301.11198v2#bib.bib3 "")\], and at the same time the limited availability of sources for trajectory data, we started on a 5-year effort to instrument a section of freeway that could help enable the next wave of empirical traffic science that depends on abundant trajectory datasets. This article presents the outcome of that effort, resulting in an instrument known as I-24 MOTION.

I-24 MOTION is a camera-based trajectory generation system located on I-24 near Nashville, TN. The instrument consists of 276 4K resolution video cameras mounted on 40 poles ranging from 110 ft to 135 ft above the freeway. The cameras are positioned with overlapping fields of view and are connected by a fiber optic network to a compute facility where the videos are converted to vehicle trajectories. The instrument captures approximately 230 million vehicle-miles of travel annually, and experiences regular recurring congestion.

Figure [1](https://arxiv.org/html/2301.11198v2#S0.F1 "Fig. 1 ‣ I-24 MOTION: An instrument for freeway traffic science") illustrates the data captured by I-24 MOTION, showing a time-space diagram spanning 4.2 miles of I-24 westbound traffic during 4 hours of morning congestion starting at 6:00AM. The image is created by plotting all westbound vehicle trajectories and color-coding the points based on the speed of the vehicle. Vehicle lengths, widths, heights, and lateral positions are also measured but not shown. The waves visible in the image propagate at approximately 12-13 miles per hour. Data used to generate this diagram are released with this work.

The main contribution of this article is the creation of the I-24 MOTION instrument, which generates the trajectory datasets released with this work. The article provides the description of key elements of the instrument, including the road network geometry and features, the features of the cyber-physical assets that compose the instrument, and the general data processing steps. It also shares initial datasets and introduces the location for where future datasets will be released.

These elements of this article are critical to understand the uses and limitations of the current and future datasets. For example, as we explain in Section [III](https://arxiv.org/html/2301.11198v2#S3 "III System Description ‣ I-24 MOTION: An instrument for freeway traffic science"), the cameras are pole-mounted. The height of the poles are selected to minimize occlusion (excellent for generating accurate vehicle trajectories), but the height can allow sway in strong winds (bad for generating accurate vehicle trajectories). Thus, the physical design directly influences the types of artifacts that can be introduced. The datasets released by I-24 MOTION will be provisioned with a digital object identifier and change logs as new data processing algorithms are deployed and as artifacts are removed.

We also provide a preliminary description of the datasets, the known artifacts today, and our plans to improve them over time. It is clear that at a macroscopic scale, the data in the initial release can already support novel macroscopic analysis and insight, since no interpolation is required - all 4 miles are observed. At the same time, we describe known issues (e.g., fragmented trajectories due to tracking failures; fragmented trajectories due to a vehicle crash which damaged hardware on one pole, etc.). Some of these issues will be resolved through instrument maintenance cycles; while others will be resolved with the advancement of better automated data generation methods. As individual datasets mature, and new datasets are introduced, this article will serve as the reference point for users of all future datasets generated by the instrument.

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Dataset | Location | Context | Year | Cameras | Time Scale | Spatial Scale | Vehicles |
| NGSIM US-101\[ [1](https://arxiv.org/html/2301.11198v2#bib.bib1 "")\] | Los Angeles, CA | 5-6 lane highway | 2005 | 8 | 0.75 hr | 0.64 km | 9,206 |
| HighD \[ [2](https://arxiv.org/html/2301.11198v2#bib.bib2 "")\] | Cologne, GE | 2-3 lane highway | 2018 | 1 | 16.5 hr | 0.42 km | 110,500 |
| ExiD \[ [4](https://arxiv.org/html/2301.11198v2#bib.bib4 "")\] | Aachen and Cologne, GE | 2-4 lane interchanges | 2021 | 1 | 16.1 hr | 0.42 km | 69,172 |
| Automatum \[ [5](https://arxiv.org/html/2301.11198v2#bib.bib5 "")\] | GE | 2-4 lane highway | 2021 | 1 | 30 hr | 0.66 km | 60,000 |
| HIGH-SIM \[ [6](https://arxiv.org/html/2301.11198v2#bib.bib6 "")\] | I-75, FL | 3-4 lane highway | 2021 | 3 | 2 hr | 2.44 km | - |
| Zen Traffic Dataset \[ [7](https://arxiv.org/html/2301.11198v2#bib.bib7 "")\] | Osaka, JP | 2 lane highways | 2018 | - | 5 hr | ∼\\sim2 km | - |
| I24-MOTION (released) | Nashville, TN | 4-5 lane highway | 2022 | 276 | 47 hr | 6.75 km | ∼\\sim600,000 |
| I24-MOTION (planned) | Nashville, TN | 4-5 lane highway | 2023 | 276 | daylight | 6.75 km | ∼\\sim150,000/day |

TABLE I: Comparison of existing highway complete vehicle trajectory datasets. “∼\\sim” indicates approximate value. “-” indicates data is not available.

The remainder of this article is organized as follows: Section [II](https://arxiv.org/html/2301.11198v2#S2 "II Related Work ‣ I-24 MOTION: An instrument for freeway traffic science") reviews the literature landscape around vehicle trajectory data, situating this work among existing research efforts. Section [III](https://arxiv.org/html/2301.11198v2#S3 "III System Description ‣ I-24 MOTION: An instrument for freeway traffic science") describes the physical infrastructure, hardware, and software systems of I-24 MOTION. Section [IV](https://arxiv.org/html/2301.11198v2#S4 "IV Trajectory Data ‣ I-24 MOTION: An instrument for freeway traffic science") describes the data produced in more detail, including the recorded quantities, coordinate system, and a comparison in spatio-temporal scale to existing vehicle trajectory dataset. Section [V](https://arxiv.org/html/2301.11198v2#S5 "V Discussion ‣ I-24 MOTION: An instrument for freeway traffic science") provides some preliminary analysis of the data including a characterization of the wave propagation speeds observed in the datasets. Lastly, Section [VI](https://arxiv.org/html/2301.11198v2#S6 "VI Conclusion ‣ I-24 MOTION: An instrument for freeway traffic science") highlights the future direction of the instrument.

## II Related Work

### II-AData collection for traffic modeling

At the macroscopic level, traffic phenomena are often observed and described with three quantities of interest, i.e., flow, speed, and density \[ [8](https://arxiv.org/html/2301.11198v2#bib.bib8 "")\]. Fundamental diagrams \[ [9](https://arxiv.org/html/2301.11198v2#bib.bib9 "")\] like the Greenshields and Greenberg models \[ [10](https://arxiv.org/html/2301.11198v2#bib.bib10 ""), [11](https://arxiv.org/html/2301.11198v2#bib.bib11 "")\] relate the traffic quantities while models such as the Lighthill-Whitham-Richards (LWR) \[ [12](https://arxiv.org/html/2301.11198v2#bib.bib12 "")\] and the Aw–Rascle–Zhang (ARZ)  \[ [13](https://arxiv.org/html/2301.11198v2#bib.bib13 "")\] are developed to describe the spatio-temporal evolution of traffic. These models can be validated with data collected from radar-based devices and loop detectors \[ [14](https://arxiv.org/html/2301.11198v2#bib.bib14 "")\]. Large-scale macroscopic data monitoring systems such as the freeway performance measurement system (PeMS) \[ [15](https://arxiv.org/html/2301.11198v2#bib.bib15 "")\]
in the United States; the A5 freeway near Frankfurt \[ [16](https://arxiv.org/html/2301.11198v2#bib.bib16 "")\] in Germany; and the M42 highway \[ [17](https://arxiv.org/html/2301.11198v2#bib.bib17 "")\] in England; and later floating-vehicle measurement-based on cell phone carrier data \[ [18](https://arxiv.org/html/2301.11198v2#bib.bib18 "")\] or GPS positional data \[ [19](https://arxiv.org/html/2301.11198v2#bib.bib19 "")\] have enabled research on macroscopic traffic flow dynamics \[ [20](https://arxiv.org/html/2301.11198v2#bib.bib20 ""), [21](https://arxiv.org/html/2301.11198v2#bib.bib21 ""), [22](https://arxiv.org/html/2301.11198v2#bib.bib22 ""), [23](https://arxiv.org/html/2301.11198v2#bib.bib23 ""), [24](https://arxiv.org/html/2301.11198v2#bib.bib24 "")\]. A challenge is that the data typically must be interpolated spatially (in the case of inductive loops), or scaled up across all vehicles (in the case of probe data) to gain a complete spatio-temporal picture.

Unlike the accumulated average macroscopic data and models, microscopic models give attention to the interactions between individual vehicles. Since the early car-following experiments \[ [25](https://arxiv.org/html/2301.11198v2#bib.bib25 "")\] conducted by physically connecting vehicles to measure space gap, many emerging in-vehicle technologies including on-board radar detectors \[ [26](https://arxiv.org/html/2301.11198v2#bib.bib26 "")\], cameras \[ [27](https://arxiv.org/html/2301.11198v2#bib.bib27 "")\], laser sensors \[ [28](https://arxiv.org/html/2301.11198v2#bib.bib28 "")\] and global positioning system (GPS) devices \[ [29](https://arxiv.org/html/2301.11198v2#bib.bib29 ""), [30](https://arxiv.org/html/2301.11198v2#bib.bib30 "")\] have been applied to measure vehicle spacing, speed and relative speed.

With the advances in visual sensing, video-based trajectory data from road-side cameras, high buildings, helicopters and drones gradually has become a mainstream source for microscopic modeling \[ [31](https://arxiv.org/html/2301.11198v2#bib.bib31 ""), [1](https://arxiv.org/html/2301.11198v2#bib.bib1 ""), [32](https://arxiv.org/html/2301.11198v2#bib.bib32 ""), [33](https://arxiv.org/html/2301.11198v2#bib.bib33 ""), [34](https://arxiv.org/html/2301.11198v2#bib.bib34 ""), [2](https://arxiv.org/html/2301.11198v2#bib.bib2 "")\]. Trajectory data with the complete information for specific road segments supported a range of efforts including the development, calibration and validation of car-following models \[ [35](https://arxiv.org/html/2301.11198v2#bib.bib35 ""), [36](https://arxiv.org/html/2301.11198v2#bib.bib36 "")\], lane-change modeling, trajectory prediction \[ [37](https://arxiv.org/html/2301.11198v2#bib.bib37 ""), [38](https://arxiv.org/html/2301.11198v2#bib.bib38 "")\], and traffic oscillation analysis \[ [39](https://arxiv.org/html/2301.11198v2#bib.bib39 "")\].

Some traffic phenomena benefit from observation of traffic across the micro and macroscopic scales. For example, traffic waves observable at the macroscopic scale can result from instabilities and disturbances in the flow at the level of individual vehicles \[ [31](https://arxiv.org/html/2301.11198v2#bib.bib31 ""), [40](https://arxiv.org/html/2301.11198v2#bib.bib40 "")\]. Macroscopic data, frequently used for traffic wave studies, can cover a great spatiotemporal scale that reveals the dynamics of traffic waves on road networks, but it is unable to provide insight into why the wave is generated and how it is propagated. Trajectory data can help provide these insights \[ [41](https://arxiv.org/html/2301.11198v2#bib.bib41 ""), [42](https://arxiv.org/html/2301.11198v2#bib.bib42 ""), [24](https://arxiv.org/html/2301.11198v2#bib.bib24 "")\] when available with adequate spatiotemporal coverage. Hence, abundant trajectory datasets, as highlighted in the article \[ [43](https://arxiv.org/html/2301.11198v2#bib.bib43 "")\], can enable traffic research at both the macroscopic and microscopic scales, aiding in understanding traffic phenomena like jam clusters and state transition dynamics \[ [16](https://arxiv.org/html/2301.11198v2#bib.bib16 ""), [44](https://arxiv.org/html/2301.11198v2#bib.bib44 ""), [45](https://arxiv.org/html/2301.11198v2#bib.bib45 "")\]. It can also capture the complex interaction within multiple-class traffic participants for heterogeneous traffic flow \[ [46](https://arxiv.org/html/2301.11198v2#bib.bib46 ""), [47](https://arxiv.org/html/2301.11198v2#bib.bib47 ""), [48](https://arxiv.org/html/2301.11198v2#bib.bib48 "")\].

### II-BExisting Testbeds

I-24 MOTION also operates as an open road testbed, which allows experiments to be conducted on the freeway and measured using the instrument. Existing closed course and open road testbeds already address some critical emerging research needs \[ [49](https://arxiv.org/html/2301.11198v2#bib.bib49 "")\]. Closed course testbeds, such as the American Center for Mobility \[ [50](https://arxiv.org/html/2301.11198v2#bib.bib50 "")\], MCity \[ [51](https://arxiv.org/html/2301.11198v2#bib.bib51 "")\], GoMentum Station \[ [52](https://arxiv.org/html/2301.11198v2#bib.bib52 "")\], and Suntrax \[ [53](https://arxiv.org/html/2301.11198v2#bib.bib53 "")\], have the distinct advantage of being capable of hosting experiments and data collection for cutting edge technologies and techniques including those under active research and development. By testing in highly controlled settings, they can assure safety and eliminate external factors such as unpredictable drivers and road conditions that can confound experiments. Because of the motivating objectives of closed course testbeds, they can be limited in their ability to test in real traffic conditions with regular drivers encountered on public roads.
Open road testbeds exist in many forms on a variety of road types; examples include the Minnesota Traffic Observatory \[ [54](https://arxiv.org/html/2301.11198v2#bib.bib54 "")\], The Ray \[ [55](https://arxiv.org/html/2301.11198v2#bib.bib55 "")\], the California Connected Vehicle Test Bed \[ [56](https://arxiv.org/html/2301.11198v2#bib.bib56 "")\], Ann Arbor Connected Vehicle Test Environment \[ [57](https://arxiv.org/html/2301.11198v2#bib.bib57 "")\], and Providentia \[ [58](https://arxiv.org/html/2301.11198v2#bib.bib58 "")\]. They support experiments in live traffic, similar to the I-24 instrument. Currently, the collection of high-fidelity trajectory data on each and every vehicle on the roadway over a multi-mile scale does not exist the United States, though the Lower Saxony testbed and the Zen Traffic initiative support these objectives in Germany and Japan. Table [II](https://arxiv.org/html/2301.11198v2#S2.T2 "TABLE II ‣ II-B Existing Testbeds ‣ II Related Work ‣ I-24 MOTION: An instrument for freeway traffic science") summarizes these existing vehicle testbeds.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Testbed | Location | Sensors | Type | Intended Usage |
| ACTION \[ [59](https://arxiv.org/html/2301.11198v2#bib.bib59 "")\] | Tuscaloosa, AL | DSRC, Cameras | Open road | CV, V2I |
| M-City \[ [51](https://arxiv.org/html/2301.11198v2#bib.bib51 "")\] | Ann Arbor, MI | DSRC, Cameras | Closed course | AV |
| The Ray \[ [55](https://arxiv.org/html/2301.11198v2#bib.bib55 "")\] | Interstate 85, GA | DSRC | Open road | CV, V2I |
| California CV Testbed \[ [56](https://arxiv.org/html/2301.11198v2#bib.bib56 "")\] | Palo Alto, CA | DSRC | Open road | CV, V2I |
| Gomentum \[ [52](https://arxiv.org/html/2301.11198v2#bib.bib52 "")\] | Concord, CA | LIDAR, DSRC, Cameras | Closed course | CV, AV |
| ACM Proving Grounds \[ [50](https://arxiv.org/html/2301.11198v2#bib.bib50 "")\] | Ypsilanti, MI | DSRC | Closed course | AV |
| SunTrax \[ [53](https://arxiv.org/html/2301.11198v2#bib.bib53 "")\] | Orlando, FL | DSRC | Open road | V2I |
| AACTVE \[ [57](https://arxiv.org/html/2301.11198v2#bib.bib57 "")\] | Ann Arbor, MI | DSRC | Open road | V2I |
| Providentia \[ [58](https://arxiv.org/html/2301.11198v2#bib.bib58 "")\] | Munich, DE | Radar,Cameras | Open road | Trajectories |
| Minnesota Traffic Observatory \[ [54](https://arxiv.org/html/2301.11198v2#bib.bib54 "")\] | Minneapolis, MN | Radar | Open road | Trajectories |
| Lower Saxony Testbed \[ [60](https://arxiv.org/html/2301.11198v2#bib.bib60 "")\] | Braunschweig, DE | LIDAR, DSRC, Cameras | Open road | Trajectories, CV, AV |
| Zen Traffic Roadways \[ [7](https://arxiv.org/html/2301.11198v2#bib.bib7 "")\] | Osaka, JP | Cameras | Open road | Trajectories, CV, AV |
| I-24 MOTION | Nashville, TN | Cameras | Open road | Trajectories, CV, AV |

TABLE II: Existing vehicle testbeds. DSRC indicates direct short range communications, Trajectories indicates complete vehicle trajectory generation, CV indicates connected vehicle testing, V2I indicates vehicle to infrastructure testing, and AV indicates autonomous vehicle testing.

### II-CEmerging Observation Technologies

In a parallel thread, significant research has been devoted to the computer vision tasks of object detection (locating relevant objects within an image) and object tracking (associating distinct objects in video frames across time). Especially in the past 10 years, rapid progress has been made in the use of modern hardware \[ [61](https://arxiv.org/html/2301.11198v2#bib.bib61 "")\], neural network architectures \[ [62](https://arxiv.org/html/2301.11198v2#bib.bib62 ""), [63](https://arxiv.org/html/2301.11198v2#bib.bib63 ""), [64](https://arxiv.org/html/2301.11198v2#bib.bib64 ""), [65](https://arxiv.org/html/2301.11198v2#bib.bib65 "")\], and massive-scale image datasets \[ [66](https://arxiv.org/html/2301.11198v2#bib.bib66 ""), [67](https://arxiv.org/html/2301.11198v2#bib.bib67 "")\] to fit accurate object detection algorithms. Approaches for extracting vehicle trajectory data utilizing these techniques have been proposed. For example, the work \[ [68](https://arxiv.org/html/2301.11198v2#bib.bib68 "")\] proposes a method to detect vehicle 3D rectangular prism bounding boxes using background subtraction and blob segmentation, relying on automatic parameter extraction of the scene homography proposed in \[ [69](https://arxiv.org/html/2301.11198v2#bib.bib69 "")\]. The work \[ [70](https://arxiv.org/html/2301.11198v2#bib.bib70 "")\] uses this data to train a convolutional neural network (CNN) to produce the same data without the need for scene-wide calibration. In \[ [71](https://arxiv.org/html/2301.11198v2#bib.bib71 "")\], 2D object detectors are used to estimate vehicle positions on the road plane (the ambiguity of vehicle position within a 2D bounding box is not fully addressed). \[ [72](https://arxiv.org/html/2301.11198v2#bib.bib72 "")\] uses ground plane projection of vehicle pixels from multiple cameras to estimate the vehicle’s position, validating with turning movement counts. Other solutions rely on re-identification of 2D tracked objects, without addressing 2D annotation position ambiguity \[ [73](https://arxiv.org/html/2301.11198v2#bib.bib73 ""), [74](https://arxiv.org/html/2301.11198v2#bib.bib74 "")\]. Other methods utilize instance segmentation networks \[ [75](https://arxiv.org/html/2301.11198v2#bib.bib75 ""), [76](https://arxiv.org/html/2301.11198v2#bib.bib76 "")\] on traffic scenes with little occlusion. A few approaches \[ [77](https://arxiv.org/html/2301.11198v2#bib.bib77 ""), [78](https://arxiv.org/html/2301.11198v2#bib.bib78 "")\] avoid object detection by measuring object presence in longitudinal scanlines along each roadway lane, but occlusion and lane changes pose difficult challenges in this problem formulation. In theory, such methods promise to address the shortage of trajectory data.

These advances, along with the increasing prevalence of aerial drones, have enabled recent research efforts to revisit the task of vehicle trajectory extraction and make marked advancements to the state of the art. The HighD, \[ [2](https://arxiv.org/html/2301.11198v2#bib.bib2 "")\], ExiD \[ [4](https://arxiv.org/html/2301.11198v2#bib.bib4 "")\], AUTOMATUM \[ [5](https://arxiv.org/html/2301.11198v2#bib.bib5 "")\], and HIGH-SIM \[ [6](https://arxiv.org/html/2301.11198v2#bib.bib6 "")\] datasets all utilize aerial imagery shot from either drone or helicopter-mounted cameras to produce complete highway vehicle trajectory data, and the Third Generation Simulation (TGSIM) \[ [79](https://arxiv.org/html/2301.11198v2#bib.bib79 "")\] is a similar in-progress effort designed to capture trajectory data containing deployed automated vehicle technologies. Similarly, the pNEUMA \[ [3](https://arxiv.org/html/2301.11198v2#bib.bib3 "")\], inD \[ [80](https://arxiv.org/html/2301.11198v2#bib.bib80 "")\], rounD \[ [81](https://arxiv.org/html/2301.11198v2#bib.bib81 "")\], OpenDD \[ [82](https://arxiv.org/html/2301.11198v2#bib.bib82 "")\], Interaction \[ [83](https://arxiv.org/html/2301.11198v2#bib.bib83 "")\] and CitySim \[ [84](https://arxiv.org/html/2301.11198v2#bib.bib84 "")\] datasets utilize drones or swarms of drones to study complex urban vehicle and pedestrian interactions in more detail. High aerial fields of view make modern image segmentation algorithms \[ [76](https://arxiv.org/html/2301.11198v2#bib.bib76 "")\] well posed for vehicle tracking in these contexts, but these methods are temporally limited by the relatively short battery life of drones (generally under an hour) and the requirement for human pilots.

## III System Description

![Refer to caption](https://arxiv.org/html/2301.11198v2/testbed_overview.png)Fig. 2: Overview of I-24 MOTION site showing location relative to Nashville, TN. The major TDOT fiber network elements and their connection to Vanderbilt University, which houses the trajectory generation algorithms that operate on the live video feeds, are also shown on the map.

This section describes the I-24 MOTION instrument, detailing the physical infrastructure, network and compute hardware, and core algorithms required to provide accurate and complete vehicle trajectory data across a large spatial and temporal scale. The system is still in active development, and continual improvements to improve the reliability, accuracy, and processing speed of the system will be made over the following years.

![Refer to caption](https://arxiv.org/html/2301.11198v2/testbed_diagram.png)Fig. 3: TOP: Diagram of the I-24 MOTION instrument, spanning from Mill Creek (postmile 58.8) to milemarker 62.8. Camera poles (blue circles) are spaced at roughly 550-foot intervals and are shown in the image relative to other key infrastructure elements. The system spans three overpasses and one underpass, as well as three interchanges with 13 entrance/exit ramps. Relative positions of all elements are correct but diagram is not drawn to scale. Bottom: Elevation and road grade along the freeway. Grade is measured in the eastbound (diagram left to right) direction.

### III-APhysical Infrastructure

The I-24 MOTION instrument provides a continuous field of view of 4.2 miles (6.75 km) on the 4-5 lanes (each direction) I-24 freeway, southeast of Nashville, Tennessee, USA. Pole mounted cameras are connected via a fiber network to a data center, where computer vision tracking and trajectory processing takes place. A total of 276 4K resolution cameras are mounted on 40 poles, each 110-135 feet tall, spaced every 500-600 feet along the freeway. The poles provide an overhead vantage point of the road to reduce occlusion, and to provide overlapping fields of view. (A separate 3-pole, 18 camera validation system \[ [85](https://arxiv.org/html/2301.11198v2#bib.bib85 "")\] is located about 0.75 miles eastbound on I-24 from the primary instrument and was used for technology testing and system planning).

#### III-A1 Location

The location for I-24 MOTION was selected based on traffic conditions, constructability factors, and co-location with other Tennessee Department of Transportation (TDOT) initiatives. The four mile section of Interstate 24 is located ten miles southeast of Downtown Nashville and exhibits an annual average daily traffic (AADT) of approximately 150,000 vehicles per day across its length \[ [86](https://arxiv.org/html/2301.11198v2#bib.bib86 "")\]. Morning and afternoon rush hour traffic exhibits reliably heavy congestion in opposite directions, frequently reaching stop-and-go conditions, with easily-observable traffic waves on a typical day. I-24 near Nashville is a heavy commuter and freight corridor (10-15% of the vehicle traffic are heavy trucks): it links smaller cities of Murfreesboro, La Vergne, and Smryna with Nashville, and serves as a major shipping and industrial transportation route for Middle Tennessee and the southeast United States.

This section of the I-24 corridor was also selected for the state’s first Integrated Corridor Management (ICM) project, called the I-24 SMART Corridor, which operates on the 28-mile route between Nashville and Murfreesboro. The ICM project includes Interstate 24, the parallel arterial route SR 1, and connector routes between I-24 and SR 1. The ICM project has deployed an upgraded communications network and Intelligent Transportation System (ITS) devices, such as variable speed limit control, lane control, and ramp metering, for increased operational management of the corridor. This collocation will eventually allow the study of a variety of implemented ITS solutions associated with the I-24 SMART Corridor using I-24 MOTION \[ [87](https://arxiv.org/html/2301.11198v2#bib.bib87 ""), [88](https://arxiv.org/html/2301.11198v2#bib.bib88 "")\], when the active traffic management systems are enabled.

#### III-A2 Camera poles

The 40 I-24 MOTION camera poles are each composed of a steel pole structure, ground-level communications and power cabinet, camera lowering device at the top of the pole, and custom camera cluster assembly, each detailed below. Figure [4](https://arxiv.org/html/2301.11198v2#S3.F4 "Fig. 4 ‣ III-A2 Camera poles ‣ III-A Physical Infrastructure ‣ III System Description ‣ I-24 MOTION: An instrument for freeway traffic science") shows select system components. Camera pole locations, as well as various other landmarks of interest, are included in Appendix [A](https://arxiv.org/html/2301.11198v2#A1 "Appendix A I-24 MOTION Infrastructure Locations ‣ I-24 MOTION: An instrument for freeway traffic science").

The camera pole system was prototyped across three years at existing pole locations on the TDOT network and with a purpose-built three-pole validation system constructed in 2020 \[ [89](https://arxiv.org/html/2301.11198v2#bib.bib89 ""), [85](https://arxiv.org/html/2301.11198v2#bib.bib85 "")\]. Valuable lessons from the validation system regarding camera selection, camera cluster mounting position, and pole-to-pole spacing were incorporated in the full system design. The details of the pole components are as follows:

![Refer to caption](https://arxiv.org/html/2301.11198v2/testbed_components.png)Fig. 4: Testbed components: a) view of a camera pole base showing the electrical disconnect, transformer, and ground cabinet; b) camera cluster in the process of lowering to the ground with the CLD; c) view of camera cluster at the top of a pole; d) fiber optic junction at network hub building and GPS network time servers.

- •


Steel pole structure: To observe all vehicles on the roadway with minimal occlusion, the poles are significantly taller than standard 30-50 ft poles used on many other CCTV systems. New poles and corresponding foundations were designed and built to a standard that the total deflection at the top of the pole is less than 1.5 inches in a 30 mph wind. Average pole-to-pole spacing is 550 feet across the instrument, with a minimum of 425ft and a maximum of 625ft due to roadside obstacles and entrance/exit ramps.

- •


Ground-level cabinet: A pole-mounted cabinet (shown in Figure [4](https://arxiv.org/html/2301.11198v2#S3.F4 "Fig. 4 ‣ III-A2 Camera poles ‣ III-A Physical Infrastructure ‣ III System Description ‣ I-24 MOTION: An instrument for freeway traffic science") a) houses a network switch for the fiber optic network, a fiber patch panel, and two power supplies. Power supplies in the cabinet provide DC power to the fiber network switch in the cabinet (65W supply) and to the camera cluster at the top of the pole (240W supply). A fiber communications backbone is present throughout the instrument and links each pole to a communications hub building (shown in Figure [4](https://arxiv.org/html/2301.11198v2#S3.F4 "Fig. 4 ‣ III-A2 Camera poles ‣ III-A Physical Infrastructure ‣ III System Description ‣ I-24 MOTION: An instrument for freeway traffic science") d) and the rest of the TDOT network. Each pole maintains a one gigabit per second network link to an aggregation network switch in a star network topology. This network topology helps simplify configuration and troubleshooting and has additional resilience in the case of some physical damage scenarios.

- •


Camera lowering device: The camera lowering device (CLD) is a critical component of all traffic monitoring cameras in the instrument. It allows the camera cluster to be safely lowered to the ground (see Figure [4](https://arxiv.org/html/2301.11198v2#S3.F4 "Fig. 4 ‣ III-A2 Camera poles ‣ III-A Physical Infrastructure ‣ III System Description ‣ I-24 MOTION: An instrument for freeway traffic science") b) for routine cleaning and maintenance using a winch at the base of the pole. While typically configured for only a single camera on a CLD, manufacturer collaboration and internal bench testing confirmed that the lowering device could support simultaneous data transmission from six 4K resolution video cameras to the ground-level cabinet where it ties into the fiber network. The CLD also contains redundant ethernet and power connections that can be utilized without the need for physical access to the top of the pole in case of a connector failure. The CLD is mounted to the top of the pole with a 54-inch extension arm and angled support strut (shown in Figure [4](https://arxiv.org/html/2301.11198v2#S3.F4 "Fig. 4 ‣ III-A2 Camera poles ‣ III-A Physical Infrastructure ‣ III System Description ‣ I-24 MOTION: An instrument for freeway traffic science") c) for added rigidity.

- •


Camera cluster assembly: Mounted on each pole is a custom, 6-camera mount attached to the camera lowering device (shown in Figure [4](https://arxiv.org/html/2301.11198v2#S3.F4 "Fig. 4 ‣ III-A2 Camera poles ‣ III-A Physical Infrastructure ‣ III System Description ‣ I-24 MOTION: An instrument for freeway traffic science") c). The orientation of the camera cluster is orthogonal to the roadway direction(s) of travel. The weather-tight camera mount holds a network switch which aggregates six video data streams to transmit them through a single gigabit ethernet connection on the CLD. The network switch receives DC power from the pole cabinet and supplies power over ethernet (PoE+) to each of the six cameras at 25.5W. On the six poles adjacent to the three interchanges within the instrument, a second camera cluster assembly is mounted in an orientation pointing towards the under/overpass; in the future these cameras will support trajectory generation for vehicles as they enter and exit the highway.


#### III-A3 Video cameras

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/6_cam_view.png)Fig. 5: Example camera fields of view for a single 6-camera pole. Each portion of the roadway is covered by at least one camera, with overlaps long enough to allow objects to be tracked between cameras.

The cameras on the instrument are a 4K resolution pan/tilt/zoom (PTZ) network IP model, powered by power over ethernet. The PTZ capabilities allow remote alignment to achieve the necessary 180-degree overlapping field of view across cameras on each pole, as seen in Figure [5](https://arxiv.org/html/2301.11198v2#S3.F5 "Fig. 5 ‣ III-A3 Video cameras ‣ III-A Physical Infrastructure ‣ III System Description ‣ I-24 MOTION: An instrument for freeway traffic science"), and between camera poles. Deploying multiple cameras to each pole extends coverage of the instrument and reduces the number of poles needed. While cameras with wider image field of view exist, these suffered in testing from distortion at the edges of the image that could not easily be corrected to the accuracy needed for coordinate localization.

A critical technical consideration with network IP cameras is time synchronization across cameras and true frame capture time reporting. Cameras are synchronized over network time protocol (NTP) to a primary and secondary stratum 1 GPS-based time servers on the local network (in the network hub building) and frequently re-synchronize (roughly every 15 minutes). The camera firmware provides timestamps associated with video frames corresponding at about 10 microsecond accuracy relative to the camera clock time. Cameras capture up to 4K resolution video at 30 frames per second. Frame-to-frame timing is typically observed to be uniform (33.3 ms), but in some cases non-negligible time differences result from duplicated or skipped frames (an artifact of camera exposure requirements as implemented in camera firmware.) Although the camera clocks are are precisely synchronized and the exact frame capture times are different for all devices, accurate time-stamping of each frame allows processing algorithms to compensate for the relative time offsets for each camera.

### III-BNetwork and Compute Hardware Architecture

All video data feeds are received from the TDOT network into a Vanderbilt data center for processing across a dedicated 40 gigabit fiber network connection. Centralized computing in a data center provides the computing hardware with dedicated, long-term support and infrastructure, in addition to future expansion possibilities. Two network switches support the cluster of servers: a data layer switch with two 25 gigabit connections to each server and a management layer switch for 1 gigabit user connectivity, control, and IPMI. A system control server directs the processing functions of the cluster across ten or more servers/nodes. It hosts a control interface where system managers dispatch processing jobs and propagates job configurations to each node. Nine processing nodes are dedicated to computer vision tracking and the initial trajectory construction. Each node contains eight graphics processing units (GPUs) that decode incoming video and perform object detection and tracking tasks. The nodes track vehicles across cameras, but each node operates independently with statically-assigned cameras. A vehicle traversing the entire instrument will generate a partial trajectory fragment on each of the (nine) processing nodes. Incoming video is buffered on its respective compute node and discarded after processing. Following initial trajectory generation, a post-processing server performs the complete trajectory assembly and reconciliation tasks. The cluster contains two data storage arrays responsible for storing the resulting trajectories – both initial trajectory fragments and post-processed complete trajectories – as well as log messages, monitoring data, algorithm training data, and instrument experiment data. Additionally, two servers within the cluster serve as a development and testing environment for new software versions and one server performs ancillary tasks such as large-scale visualization and traffic analysis.

### III-CSoftware Architecture

A prototype software architecture comprises of three main modules: video ingest, vehicle detection and tracking, and trajectory post-processing and reconstruction, managed by the system control server. Before a run session starts, related configuration files and metadata are registered and stored in database for record-keeping or re-processing.

#### III-C1 Video ingestion and recording

The cameras produce a H.264 encoded video, currently at 1080p resolution and 30 frames per second to reduce the data size. The streams are split into 10 minute chunks and recorded into a Matroska (MKV) container. The timestamps, corresponding to the exact exposure moment of each frame (streamed separately in a custom field) which are incorporated into the PTS (Presentation timestamp) metadata during recording. This field is mandatory for video files, thus providing a standardized method for frame timing information, and enables interoperability with any conforming software. The video stream, with the current configuration and all 276 cameras, occupies ∼\\sim1 TB for each recorded hour at 1080p resolution.

#### III-C2 Vehicle Detection and Tracking

Vehicle detection and tracking is performed using Crop-based Tracking, a joint detection and tracking method \[ [90](https://arxiv.org/html/2301.11198v2#bib.bib90 "")\]. This method processes only cropped portions of each overall image, drastically reducing detection inference time relative to processing each frame fully. Implicit in the use of this method is an accurate object motion model; object priors from this motion model are used to produce cropping boxes for each object, and only crops are processed by the object detector on most frames. For the base object detector, Retinanet with a ResNet-50 backbone is used \[ [91](https://arxiv.org/html/2301.11198v2#bib.bib91 "")\]. For the motion model, a Kalman filter with linear dynamics is used. Objects are assumed to travel with constant velocity along the primary direction of roadway travel, and are assumed to have zero velocity perpendicular to the primary roadway direction (note that this motion constraint is relaxed during data postprocessing and is only used during initial object tracking). The intersection-over-union metric is used to compute affinity between object positions and new detections \[ [92](https://arxiv.org/html/2301.11198v2#bib.bib92 "")\]. IOU is computed based on vehicle footprints in space rather than bounding box coordinates within an image, which allows detections from multiple cameras with distinct fields of view to be incorporated provided accurate homography information is available for each camera (for more information on camera homographies and data coordinate system, see Section [IV-B](https://arxiv.org/html/2301.11198v2#S4.SS2 "IV-B Data Coordinate System ‣ IV Trajectory Data ‣ I-24 MOTION: An instrument for freeway traffic science") and Appendix [C](https://arxiv.org/html/2301.11198v2#A3 "Appendix C Coordinate System Conversion ‣ I-24 MOTION: An instrument for freeway traffic science"). The multi-camera tracking problem is solved by detection fusion (as in \[ [93](https://arxiv.org/html/2301.11198v2#bib.bib93 ""), [94](https://arxiv.org/html/2301.11198v2#bib.bib94 "")\]) rather than trajectory fusion (as in \[ [95](https://arxiv.org/html/2301.11198v2#bib.bib95 "")\]) to reduce redundant tracking of the same object in multiple fields of view. Figure [6](https://arxiv.org/html/2301.11198v2#S3.F6 "Fig. 6 ‣ III-C2 Vehicle Detection and Tracking ‣ III-C Software Architecture ‣ III System Description ‣ I-24 MOTION: An instrument for freeway traffic science") shows the result of object detection and tracking within image coordinates, and the corresponding roadway coordinate object positions obtained using image homography.

The complete set of 276 camera fields of view is subdivided across multiple processing nodes. On each node, all cameras are processed together (that is, roughly one frame from each camera is processed at a time, subject to some frame skips to keep cameras tightly time-synchronized). Processing nodes are not synchronized, so a single object traveling through the full instrument extents will be tracked as a separate vehicle with a unique ID on each processing node. This decouples the computation and allows the system to scale gracefully with a large number of cameras.

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/tracking-transform.png)Fig. 6: Vehicles are represented as 3D rectangular prism objects (various colors above) using object detection algorithms within each camera frame. The resulting detected objects are transformed into roadway coordinates shared among all cameras, and tracked in this unified coordinate system. Each blue rectangle in the projected 2D birds-eye view represents a vehicle position.

#### III-C3 Trajectory Post-processing

Although raw trajectory data from dense deployment of cameras and CV algorithms can achieve complete spatial and temporal coverage of a roadway segment, such data contains inaccuracies from camera errors (dropped, doubled, and corrupted frames) network errors (data packet drops), object detection and tracking (fragmentations, ID swaps, false negatives and false positives \[ [96](https://arxiv.org/html/2301.11198v2#bib.bib96 "")\]) often caused by object-object or infrastructure-object occlusions, timestamp quantization errors, homography assumption errors, and infeasible derivative quantities resulting from finite difference approximation over very short timescales. Treatments for specific sources of errors that rely on multiple iterations of rectification or require manual fine-tuning are not viable for longer term streaming datasets the I-24 MOTION is designed to produce. For small datasets, data cleaning and rectification with some manual involvement can address many common errors created in vehicular datasets \[ [97](https://arxiv.org/html/2301.11198v2#bib.bib97 "")\].

I-24 MOTION uses an automatic data post-processing pipeline \[ [98](https://arxiv.org/html/2301.11198v2#bib.bib98 "")\] which will be continuously improved to automate as much of the data cleaning steps as possible. Currently, it consists of a) an online data association algorithm to solve a min-cost flow problem, which consequently matches fragments that belong to the same object, and b) a trajectory reconciliation algorithm, which is formulated as a quadratic program. This algorithm reconstructs realistic vehicle dynamics from disturbed detection data with trajectory derivative smoothing and outlier correction while minimally perturbing the original vehicle detections. The resulting trajectories automatically satisfy the internal consistency (differentiation of trajectories with speeds and accelerations). Future post-processing development will consider conflict resolution along with trajectory smoothing to produce feasible inter-vehicular distances for accurate microscopic traffic studies.

## IV Trajectory Data

This section provides an overview of the data created by the I-24 MOTION system: its attributes, scale, conventions and coordinate system, known artifacts in the data, and a preliminary analysis of data accuracy.

### IV-AData Description

One single continuous recording session on the I-24 MOTION instrument processed through the software pipeline (from Section [III-C](https://arxiv.org/html/2301.11198v2#S3.SS3 "III-C Software Architecture ‣ III System Description ‣ I-24 MOTION: An instrument for freeway traffic science")) results in a vehicle trajectory dataset. Each dataset produced by the system consists of a collection of individual vehicle trajectories. An individual vehicle trajectory consists of vehicle attributes as well as motion information (see Table [III](https://arxiv.org/html/2301.11198v2#S4.T3 "TABLE III ‣ IV-A Data Description ‣ IV Trajectory Data ‣ I-24 MOTION: An instrument for freeway traffic science")). Trajectory positions record the 2D footprint of the back center of each car, and are re-sampled at a frequency of 25 Hz to allow exact timestamp-based indexing. Derivative quantities such as velocity, acceleration and steering angle can be directly computed with position information via, for example, finite difference. An example vehicle trajectory is included in Appendix [B](https://arxiv.org/html/2301.11198v2#A2 "Appendix B Example Vehicle Trajectory ‣ I-24 MOTION: An instrument for freeway traffic science").

|     |     |     |     |
| --- | --- | --- | --- |
| Attribute | Type | Unit | Description |
| \_id | 12-byte BSON | −- | vehicle identifier unique across all I-24 MOTION data |
| vehicle class | int | −- | 0: sedan, 1: midsize, 2: pickup, 3: van, 4: semi, 5: truck, 6: motorcycle |
| first timestamp | float | s | minimum unix timestamp for this trajectory |
| last timestamp | float | s | maximum unix timestamp for this trajectory |
| timestamp | \[float\] | s | array of times at which vehicle positions are recorded |
| x position | \[float\] | ft | array of longitudinal positions on roadway corresponding to each timestamp |
| y position | \[float\] | ft | array of lateral positions on roadway corresponding to each timestamp |
| starting x | float | ft | longitudinal position on roadway at first timestamp |
| ending x | float | ft | longitudinal position on roadway at last timestamp |
| length | float | ft | vehicle length |
| width | float | ft | vehicle width |
| height | float | ft | vehicle height |
| direction | int | −- | -1 if westbound, 1 if eastbound |
| configuration ID | int | −- | identifier linking data to a unique metadata indicating trajectory generation algorithm settings |

TABLE III: Data attributes for a single vehicle trajectory. Square brackets indicate an array of values.

Accompanying this work, 10 days of trajectory data are released from weekday morning traffic. Each dataset spans typically 4 hours, from 6:00 AM to 10:00 AM, covering morning rush hour conditions. (Data from Friday, November 25th instead covers 11 hours.) A variety of traffic conditions are present throughout the various days of data, including at least three crash-induced bottlenecks, one debris-induced bottleneck, high-traffic conditions with travelling waves, and free-flow traffic conditions. Table [IV](https://arxiv.org/html/2301.11198v2#S4.T4 "TABLE IV ‣ IV-A Data Description ‣ IV Trajectory Data ‣ I-24 MOTION: An instrument for freeway traffic science") summarizes the data released with this work. Additional metrics, statistics, time-space diagrams, and useful information can be found with the data release, as this information will change as the data is updated in future versions. Time-space diagrams for the westbound portion of the roadway on each day of trajectory data are included in Appendix [D](https://arxiv.org/html/2301.11198v2#A4 "Appendix D Additional space time diagrams ‣ I-24 MOTION: An instrument for freeway traffic science"), and individual lane time-space diagrams for one day are shown in Appendix [E](https://arxiv.org/html/2301.11198v2#A5 "Appendix E Lane-Dis-aggregated Time-Space Diagrams ‣ I-24 MOTION: An instrument for freeway traffic science"). Details on the data release are included in Section [IV-E](https://arxiv.org/html/2301.11198v2#S4.SS5 "IV-E Data Availability ‣ IV Trajectory Data ‣ I-24 MOTION: An instrument for freeway traffic science").

| Date | Day | ID | Start time (AM) | Duration (hours) | Notes |
| --- | --- | --- | --- | --- | --- |
| Nov 21, 2022 | Monday | 637b023440527bf2daa5932f | 6:00 | 4 | crash, debris induced bottleneck |
| Nov 22, 2022 | Tuesday | 637c399add50d54aa5af0cf4 | 6:00 | 4 | −- |
| Nov 23, 2022 | Wednesday | 637d8ea678f0cb97981425dd | 6:00 | 4 | crash |
| Nov 24, 2022 | Thursday | 637f0d5f78f0cb97981425de | 6:00 | 4 | low traffic volume (holiday) |
| Nov 25, 2022 | Friday | 6380728cdd50d54aa5af0cf5 | 6:00 | 11 | low traffic volume (holiday) |
| Nov 28, 2022 | Monday | 638450a3dd50d54aa5af0cf6 | 6:00 | 4 | stopped vehicles induced slowdown |
| Nov 29, 2022 | Tuesday | 63858a2cfb3ff533c12df166 | 6:00 | 4 | −- |
| Nov 30, 2022 | Wednesday | 6386d89efb3ff533c12df167 | 6:00 | 4 | −- |
| Dec 1, 2022 | Thursday | 63882be478f0cb97981425df | 6:00 | 4 | merge induced slowdown |
| Dec 2, 2022 | Friday | 63898d48d430891009401330 | 6:00 | 4 | crash |

TABLE IV: Details of the released dataset. “ID” indicates the unique dataset identifier used to associate all data and metadata for this dataset. Additional summary and statistic information is included with the data release.

### IV-BData Coordinate System

Data is provided natively in a curvilinear 2D roadway coordinate system, with the primary (xx) axis aligned along the interstate roadway median and the secondary (yy) axis defined locally perpendicular to the primary axis. This means that xx is roughly equivalent to station or mile marker along the roadway, while yy gives lateral or lane-position data. A second-order spline defines the xx-axis in global (state plane) coordinates. (Control points for the center-line in state plane coordinates are included in metadata). This allows for the direct conversion of roadway coordinates into state plane coordinates, with a trivial conversion from state plane coordinates to GPS WGS84 coordinates. Both coordinate directions are stored natively in feet. The positive xx-direction is defined in the eastbound direction (direction of increasing post-mile as defined by the Interstate 24 mile markers), and xx-coordinates are offset such that the xx-coordinate for post-mile 60 corresponds exactly to 5280×60=3168005280\\times 60=316800 ft. (Other postmiles are approximately but not exactly located in this way (e.g. post-mile 61 ≈5280×61=322080\\approx 5280\\times 61=322080 ft.) Adopting the left-hand rule convention, the yy-coordinate is positive on the eastbound side of the roadway (vehicle is moving in increasing xx-direction). Figure [7](https://arxiv.org/html/2301.11198v2#S4.F7 "Fig. 7 ‣ IV-B Data Coordinate System ‣ IV Trajectory Data ‣ I-24 MOTION: An instrument for freeway traffic science") illustrates the coordinate system, and Appendix [C](https://arxiv.org/html/2301.11198v2#A3 "Appendix C Coordinate System Conversion ‣ I-24 MOTION: An instrument for freeway traffic science") details the conversion of coordinates between the roadway coordinate system and state plane coordinates.

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/coordinates.png)Fig. 7: Spline-curvilinear xx-axis (green) and locally perpendicular yy-axis (red) for roadway coordinates. State plane coordinates are shown in black for comparison. Position of the vehicle can be expressed either in state plane coordinates (black dashes) or roadway coordinates (white dots).

The primary advantages of a curvilinear coordinate system are twofold: i.) The coordinate system aligns lateral (lane position) information along the yy-axis, while accounting for the longitudinal curvature of the roadway and aligning the direction of travel with the xx-axis. ii.) A perpendicular slice of the roadway has a uniform xx-coordinate.

While definition of the y-axis as locally perpendicular to the xx-axis does allow for the same point to have multiple (x,y)(x,y) locations, for reasonable roadway curvatures these points occur suitably far from the roadway surface where the coordinate system is relevant. This coordinate system also slightly underestimates the distance travelled (and therefore the instantaneous speed) of vehicles on the exterior of a curve, relative to vehicles on the interior of a curve. the magnitude of this effect is no more than the ratio of roadway width to radius of curvature, which tends to be small (less than 5%) on typical roadways. Exact distances travelled and speeds can instead be calculated by converting positions into state plane coordinates followed by finite difference calculation.

### IV-CPositional Accuracy

To assess the accuracy and suitability of I-24 MOTION trajectory data for micro-scale traffic analysis, output trajectory data is compared against an internal, manually labeled ground truth trajectory dataset, and onboard GPS information from instrumented vehicles traveling on the roadway.

#### IV-C1 Manually Labeled Ground Truth

Manual labeling of vehicles as 3D rectangular prism bounding boxes within videos from a subset of 18 cameras was performed for two scenarios: a free-flow traffic scenario and a highly congested (one side of roadway) scenario. In total, over 600,000 individual vehicle positions were labeled manually. The resulting vehicle trajectories were compared against the trajectory data output by running the I-24 MOTION trajectory generation algorithms on the same video data. For comparison, object positions were matched to ground truth (GT) object positions as in \[ [99](https://arxiv.org/html/2301.11198v2#bib.bib99 "")\] at each timestep. A minimum intersection-over-union (IOU) between the predicted and ground truth vehicle position was required to consider the predicted vehicle position a match for that ground truth object. Table [V](https://arxiv.org/html/2301.11198v2#S4.T5 "TABLE V ‣ IV-C1 Manually Labeled Ground Truth ‣ IV-C Positional Accuracy ‣ IV Trajectory Data ‣ I-24 MOTION: An instrument for freeway traffic science") reports a number of multiple object tracking metrics for each scenario, as well as some metrics indicating the physical feasibility of the output trajectories. 97-98% of ground truth objects have at least one predicted trajectory assigned to them (GT Match Rate) and for ground truth objects, on average 91-95% of the overall trajectory is covered by matching predicted vehicle positions (Per GT Recall). Moreover, all vehicles have feasible accelerations, only 0-2% of vehicle observations have infeasible heading angles, and only 0-2% of vehicle trajectories overlap with another trajectory at some point.

| Metric (1.0 best) | Congested | Free-flow | Description |
| --- | --- | --- | --- |
| MOTA | 0.93 | 0.93 | Aggregate object tracking metric |
| MOTP (IOU) | 0.73 | 0.72 | Average precision (IOU) of matched object positions |
| Precision | 0.98 | 0.97 | Proportion of predicted object positions matched to a ground truth position |
| Recall | 0.95 | 0.96 | Proportion of ground truth object positions matched to a predicted object position |
| GT Match Rate | 0.97 | 0.98 | Proportion of ground truth trajectories matched to at least one predicted trajectory |
| Pred Match Rate | 0.99 | 0.76 | Proportion of predicted trajectories matched to at least one ground truth trajectory |
| Per GT Recall | 0.91 | 0.95 | Average proportion of a ground truth trajectory with correctly matched predicted object positions |
| Per Pred Precision | 0.98 | 0.74 | Average proportion of predicted trajectory correctly matched to a ground truth object |
| Feas. Accel. | 1.00 | 1.00 | Proportion of finite difference accelerations that are feasible (<10​f​t/s2<10ft/s^{2}) |
| Feas. Heading Angle | 0.98 | 1.00 | Proportion of finite difference heading angles that are feasible (<30∘<30^{\\circ}) |
| Feas. Direction | 0.99 | 1.00 | Proportion of finite difference velocities with correct magnitude (no backwards movement) |
| Feas. Overlapping | 0.98 | 1.00 | Proportion of predicted trajectories that never overlap with another trajectory |

TABLE V: Multiple object tracking and trajectory feasibility metrics for two ground truth scenarios (congested and free flow).

For matched vehicle positions, Figure [8](https://arxiv.org/html/2301.11198v2#S4.F8 "Fig. 8 ‣ IV-C1 Manually Labeled Ground Truth ‣ IV-C Positional Accuracy ‣ IV Trajectory Data ‣ I-24 MOTION: An instrument for freeway traffic science") shows the relative error between the predicted and ground truth vehicle position. 84% of predicted object positions fall within 3 feet of the ground truth position, and 36% fall within 1 foot of the corresponding ground truth. Table [VI](https://arxiv.org/html/2301.11198v2#S4.T6 "TABLE VI ‣ IV-C1 Manually Labeled Ground Truth ‣ IV-C Positional Accuracy ‣ IV Trajectory Data ‣ I-24 MOTION: An instrument for freeway traffic science") reports the relative error between the predicted and ground truth vehicle dimensions. All dimensions have a mean absolute error of less than 1.2 feet.

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/bullseye_semifinal.png)Fig. 8: Positional error histogram for trajectory data relative to ground truth trajectories. Contours show the proportion of data is contained within, and are at intervals of 0.1 unless otherwise indicated. Single positional errors are shown as black dots. A red circle shows the proportion of data with less than 1-meter positional error (0.87) and an orange circle shows the proportion of data with less than 1-foot positional error (0.36).

| Quantity | Mean Error (ft) | Standard Deviation(ft) | Mean Absolute Error (ft) |
| --- | --- | --- | --- |
| Longitudinal (X) Position | 0.2 | 2.6 | 1.7 |
| Lateral (Y) Position | -0.3 | 0.6 | 0.6 |
| Length | -0.6 | 2.5 | 1.2 |
| Width | 0.1 | 0.5 | 0.3 |
| Height | 0.5 | 0.8 | 0.7 |

TABLE VI: I-24 MOTION vehicle position and dimension errors relative to matched ground truth vehicles.

#### IV-C2 GPS Data

Trajectory data was compared against onboard vehicle GPS sensor data, a commonly used sensor modality for obtaining single vehicle trajectories. GPS-equipped vehicles were driven in eastbound and westbound lanes of traffic on the I-24 MOTION instrument. Over 600 vehicle runs through the instrument extents were conducted. Regular (1 sec) positional data for each vehicle run was recorded. The reported circular error probable (CEP) for the sensor was 2.5 meters. Figure [9](https://arxiv.org/html/2301.11198v2#S4.F9 "Fig. 9 ‣ IV-C2 GPS Data ‣ IV-C Positional Accuracy ‣ IV Trajectory Data ‣ I-24 MOTION: An instrument for freeway traffic science") shows a histogram of lateral positional data for each sensor modality (I-24 MOTION and GPS data), aggregated for several longitudinal slices along the instrument. The I-24 MOTION data shows strong lateral peaks corresponding to vehicle presence in a specific lane of travel, whereas the GPS lateral positional data does not show this characteristic. This is a strong indicator that I-24 MOTION yields strong lane-positional data, whereas this data is not necessarily available from an onboard GPS sensor without heavy filtering.

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/gps_y_hist.png)Fig. 9: Lateral position histogram aggregated over several 1000-foot longitudinal slices, for I-24 MOTION camera trajectory data (blue-green) and onboard GPS data (pink-red). Strong peaks I-24 MOTION camera positional data correspond to lanes of travel. Data produced during AM rush-hour (higher traffic volume on westbound, negative lateral position, side of roadway).

### IV-DData Artifacts

Relative to previous complete vehicle trajectory datasets, the data and instrument proposed in this work offer new challenges to perfect the data. Previous works were conducted in areas of sufficiently small spatio-temporal scale that physical occlusions could mostly be avoided (by overhead vantage point and careful roadway segment selection). Moreover, they were of sufficiently small temporal scale that errors remaining in the data after trajectory generation could be removed with manual efforts \[ [97](https://arxiv.org/html/2301.11198v2#bib.bib97 "")\]). This approach is not scalable to the I-24 MOTION data, and some errors will always remain in the final data regardless of the algorithm employed. Enumerated here are a number of known errors in the initial data release that are artifacts of system hardware and software errors. We intend to partially or fully address each of these artifacts; moreover, open communication with I-24 MOTION data users will be maintained such that systematic errors in data creation can be addressed and data quality can be iteratively improved over time.

Figure [10](https://arxiv.org/html/2301.11198v2#S4.F10 "Fig. 10 ‣ IV-D Data Artifacts ‣ IV Trajectory Data ‣ I-24 MOTION: An instrument for freeway traffic science") shows time-space data with each type of data artifact present. Known data artifacts include:

- •


Missing Pole: Data from a single pole is occasionally missing from one of two sources. Brief outages can occur due to network communication issues. or to physical hardware damage (a camera pole was hit by a car in the week prior to most of the data in this work being generated). This manifests as a horizontal band on the time-space diagram (a contiguous spatial range of data missing across all recording time). Such issues are rare because poles are protected by guardrails, but these issues cannot be eliminated entirely.

- •


Overpass Occlusion: Overpass occlusion results in lost tracked vehicles, which also manifests as a contiguous spatial range of data missing across all recording time. This artifact will be addressed with an intelligent data processing step that matches objects disappearing under bridges with objects reappearing on the other side.

- •


Static Homography Errors: Initially, homographies for each camera were statically defined. However, pole deflection due to temperature and sunlight cause subtle shifts in camera positions. This manifests in very narrow (a few feet wide) horizontal bands on the time-space diagram that contain missing or doubled trajectory positional data. This issue will be corrected by periodically accounting for subtle camera motion by re-defining homographies.

- •


Packet Drops / Frame Corruptions: Network bandwidth limitations (especially near night-time hours when low light conditions create noisier and therefore larger video data) result in occasional packet drops or frame corruptions, which manifest as a band of missing positional data for a contiguous region of space and time. This issue will be mostly addressed by IP camera stream profile optimization and network connectivity improvements.

- •


Fragmentations: Ideally, each vehicle passing through the instrument is represented by a single recorded trajectory. In practice though, vehicles are often represented by several trajectory fragments, which are often the product of the above artifacts or other tracking or post-processing failures. Fragmentations manifest as discontinuous chunks of trajectory corresponding to a single vehicle. Fragmentations will be iteratively decreased over time as the above artifacts and other tracking issues are removed.


![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/artifacts_tiled2.png)Fig. 10: Example artifacts. For all figures, horizontal scale = 4 min. and vertical scale = 0.4 mi. a.) Missing pole causes a wide band of missing data. b.) Overpass causes a narrow band of missing data. In some cases post-processing can successfully stitch trajectories through this occlusion. c.) Homography error causes multiple trajectories corresponding to the same vehicle, or else results in a narrow band with no coverage. d.) Packet drops cause bands of missing trajectory data with a discrete start and end. Post-processing only partially fills in this data.

### IV-EData Availability

At the time of publication, data from I-24 MOTION will be made available on the project website located at https://i24motion.org/data. Data will be associated with a DOI for permanent referencing, and new versions of data will be assigned new DOIs according to standard DOI issuing guidelines. A README file contains information relevant to downloading, formatting, and using the data. Each processed day of data (a JSON set of JSON-like trajectories) is made available for download, as well as additional metadata including: scene homography for the data, trajectory extraction algorithm settings, and in-depth descriptions of data attributes. Data is initially released “as is”, recognizing over time the data will be reprocessed and improved as the instrument matures.

Video data is in general not persistently recorded or made available with trajectory data. This is because the raw video data potentially contains personally identifiable information. The instrument and data processing was designed to avoid collecting PII but it is difficult to guarantee no information was collected for all but very small subsets of data. We also note that the size of raw video files from the entire instrument is too large for easy distribution. For example the initial data release corresponds to approximately 47TB of video files. Depending on research community needs and IRB considerations, it is possible this may be reconsidered in the future.

## V Discussion

This section provides some initial analysis of the datasets that are released with the publication. We generate the time-space diagrams of all of the published datasets, as well as illustrations of the type of analysis that can be conducted on the current data.

### V-ATraffic wave properties

Traffic oscillations are characterized by regular acceleration/deceleration cycles in congested traffic, and is shown to have negative impact on the overall traffic efficiency and energy consumption \[ [16](https://arxiv.org/html/2301.11198v2#bib.bib16 ""), [101](https://arxiv.org/html/2301.11198v2#bib.bib101 "")\]. In this subsection we provide a few examples of macroscopic observations from a dataset captured by the I-24 MOTION system during the morning rush hours of two weekdays (Nov. 21 and Nov. 23, 2022) containing muiltiple events. The time space diagrams for these days are shown in Figure [11](https://arxiv.org/html/2301.11198v2#S5.F11 "Fig. 11 ‣ V-A Traffic wave properties ‣ V Discussion ‣ I-24 MOTION: An instrument for freeway traffic science")) including a variety of traffic patterns, such as free-flow, congested and stop-and-go traffic as well as bottlenecks caused by various incidents.

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/heatmap_post1.png)(a)Monday Nov. 21 2022

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/heatmap_post3.png)(b)Wednesday Nov. 23 2022

Fig. 11: Velocity field in (mph) obtained from the westbound (decreasing milemarkers) trajectory data on (a) Nov. 21 and (b) Nov. 23, 2022. Each plot depicts traffic velocity evolution during the morning rush hours on the 4-mile of I-24 MOTION main corridor. The velocity field is aggregated into small bins from trajectory data according to Edie’s definitions \[ [102](https://arxiv.org/html/2301.11198v2#bib.bib102 "")\] with grid size of Δ​t=30\\Delta t=30s and Δ​x=100\\Delta x=100ft, respectively. The window sizes are selected to preserve fine-scale traffic wave properties.

| Event Information | Upstream Wave Properties |
| --- | --- |
| Index | Date | Duration | |     |
| --- |
| Nearest |
| Milemarker | | Description | |     |
| --- |
| Blocked |
| Lanes | | |     |
| --- |
| Propagation |
| Speed (mph) | | |     |
| --- |
| Period |
| (min) | | |     |
| --- |
| Fluctuation |
| range (mph) | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | Nov 21 | 6:14-7:43AM | MM59.5 | Severe rear-end accident | 1,2 and left shoulder | 12.6 | 2.1 | 0-14.8 |
| B | Nov 21 | 7:40-7:44AM | MM58.8 | Debris in lane | 3 | 12.5 | 5.0 | 8.4-42.5 |
| C | Nov 23 | 7:35-7:45AM | MM59.5 | Sideswipe accident | 1 & 2 | 13.1 | 1.8 | 8.7-19.5 |

TABLE VII: Approximate traffic wave properties in the upstream segment of selected events. The wave properties are obtained by a combination of wavelet transform and visual inspection (see Appendix [F](https://arxiv.org/html/2301.11198v2#A6 "Appendix F Traffic Wave Calculations ‣ I-24 MOTION: An instrument for freeway traffic science")). Almost all waves appear to be “quasi-periodic” and non-stationary and therefore only the most prominent values are reported.

We select three signature events from these days (termed as Events A-C, see Table [VII](https://arxiv.org/html/2301.11198v2#S5.T7 "TABLE VII ‣ V-A Traffic wave properties ‣ V Discussion ‣ I-24 MOTION: An instrument for freeway traffic science")), which are incident-induced bottlenecks. Specifically, Event A is a severe rear-end crash on the HOV lane that was immediately followed by an onset of upstream queuing on lane 1 and lane 2. The congestion lasted for about 1.5 hrs before the crash was cleared. Event B is a slowdown on lane 3 caused by a large object falling out of a pickup truck. The roadway was cleared about 2.5 minutes later. Event C is a sideswipe crash due to a vehicle changing from lane 1 to lane 2 that caused a collision with another car travelling in lane 2. These events are summarized in Table [VII](https://arxiv.org/html/2301.11198v2#S5.T7 "TABLE VII ‣ V-A Traffic wave properties ‣ V Discussion ‣ I-24 MOTION: An instrument for freeway traffic science").

Characteristics of the waves upstream of the selected events are calculated and also summarized in Table [VII](https://arxiv.org/html/2301.11198v2#S5.T7 "TABLE VII ‣ V-A Traffic wave properties ‣ V Discussion ‣ I-24 MOTION: An instrument for freeway traffic science"), including the wave propagation speed, period (time it takes to experience a complete slowdown and speedup cycle at a fixed location), and amplitude (or fluctuation range). Here the wave property calculations are based on visual inspections combined with various well-known techniques such as wavelet transform \[ [103](https://arxiv.org/html/2301.11198v2#bib.bib103 "")\] and cross-correlation \[ [104](https://arxiv.org/html/2301.11198v2#bib.bib104 "")\]. We direct interested readers to common references such as \[ [24](https://arxiv.org/html/2301.11198v2#bib.bib24 ""), [104](https://arxiv.org/html/2301.11198v2#bib.bib104 "")\] for details.

Figure [11](https://arxiv.org/html/2301.11198v2#S5.F11 "Fig. 11 ‣ V-A Traffic wave properties ‣ V Discussion ‣ I-24 MOTION: An instrument for freeway traffic science") shows that perturbations in different times and locations all propagate upstream. Although the periodicity and magnitude of the waves vary, depending on factors such as the severity of the bottleneck, road geometry, and heterogeneity of driver-vehicle units \[ [104](https://arxiv.org/html/2301.11198v2#bib.bib104 "")\], they generally travel against the direction of traffic at a constant characteristic speed of approximately 13 mph (see also \[ [105](https://arxiv.org/html/2301.11198v2#bib.bib105 ""), [106](https://arxiv.org/html/2301.11198v2#bib.bib106 ""), [44](https://arxiv.org/html/2301.11198v2#bib.bib44 "")\]). We observe that oscillations with longer periods are often accompanied by larger amplitudes. For example, Event A has prominent waves with period 2.1 min and a speed range of 14.8 mph, Event B with period 5 min and a speed range of 34 mph, and Event C with period 1.8 min and a speed range of 10.8 mph, although the severity and the traffic conditions vary. The strong correlation between traffic wave period and amplitude is also discussed in \[ [107](https://arxiv.org/html/2301.11198v2#bib.bib107 "")\].

Even in the present form, data from I-24 MOTION already suitable to study traffic waves and other macroscopic quantities. This allows I-24 MOTION data to be used for speed analysis directly without needing to extrapolate long distances between fixed sensors (data cleaning is, however still required). Moreover, the camera-based sensors yield useful insight into the initial causes of bottlenecks not visible in any other sensing modality (e.g., debris on the roadway). Figure [12](https://arxiv.org/html/2301.11198v2#S5.F12 "Fig. 12 ‣ V-A Traffic wave properties ‣ V Discussion ‣ I-24 MOTION: An instrument for freeway traffic science") shows other example traffic phenomena not easily visible in traditional traffic sensing regimes.

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/phenomena_tile2.png)Fig. 12: Examples of data phenomena difficult to observe in fixed-point or sparse GPS floating vehicle sensing schemes. For all figures, horizontal scale = 4 min. and vertical scale = 0.4 mi. a.) Vehicle collision and resulting small-scale bottleneck. b.) Low-wavelength (≈30\\approx 30 sec) traffic waves in high-density flow. c.) A stopped vehicle on side of roadway. d.) Off-ramp queuing during otherwise free-flow conditions.

### V-BFundamental diagrams (FDs)

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/fd_post1.png)Fig. 13: Traffic data immediately downstream and upstream of the crash on Monday Nov 21 (event A).![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/fd_post3.png)Fig. 14: Traffic data immediately downstream and upstream of the crash on Wednesday Nov 23 (event C).

The empirical data from I-24 MOTION provides high resolution spatial-temporal evolution of traffic, which allows us to investigate more closely the changes of traffic properties on a finer scale. It also provides the possibility of computing fundamental diagrams at arbitrary locations around incidents.

For example, Figures [13](https://arxiv.org/html/2301.11198v2#S5.F13 "Fig. 13 ‣ V-B Fundamental diagrams (FDs) ‣ V Discussion ‣ I-24 MOTION: An instrument for freeway traffic science") and [14](https://arxiv.org/html/2301.11198v2#S5.F14 "Fig. 14 ‣ V-B Fundamental diagrams (FDs) ‣ V Discussion ‣ I-24 MOTION: An instrument for freeway traffic science") show fundamental diagrams and speed density plots computed immediately upstream and downstream of individual incidents, as well as the across the remainder of the dataset for the day. In each figure, the blue points correspond to speed/density/flow values downstream of the incident location, and the orange points correspond to the conditions immediately upstream of the crash at the same time. Data points shown in grey were collected at the same location on the day of the incident for reference. The points are computed from the trajectory data using Edie’s definitions. This illustrates a a capability that is possible to explore precisely because the complete roadway is monitored, allowing us to analyze the data around each event location.

The current illustrations provided here are not comprehensive but are rather designed to show that the data in its current form can already be used to support different research questions. As the datasets continue to improve, it will allow further investigations that bridge microscopic and macroscopic scales.

## VI Conclusion

This work introduces the I-24 MOTION instrument, which is designed to produce large scale trajectory datasets to support new directions in traffic science and traffic flow theory research. We also provide our initial datasets that will be improved and maintained as the instrument software continues to mature.

Physical infrastructure construction on the instrument completed in November 2022, and the processing algorithms are far from final. In our ongoing work, we will be providing more datasets, tools, and methods, and software implementations that allow the instrument to support a wider range of applications and increase the overall data quality. Recognizing the evolving nature of the instrument, this work serves as a single reference to I-24 MOTION, with future works outlining the methodological improvements that advance data quality and provide insights into the traffic phenomena captured by the instrument.

The instrument was also designed to support live experiments in traffic, including large deployments of automated vehicles which are designed to smooth traffic jams. The instrument will also support experiments conducted in collaboration with Tennessee Department of Transportation to support active traffic management, including experiments using variable speed limits, ramp meters, and lane closure systems. Such experiments will allow further investigation of the consequences of emerging technologies on traffic flow.

## Appendix A I-24 MOTION Infrastructure Locations

| Pole Number | Longitude | Latitude |
| --- | --- | --- |
| 1 | -86.6683396697044 | 36.0510246530758 |
| 2 | -86.6668725013732 | 36.0501702406015 |
| 3 | -86.6654402017593 | 36.0493331676102 |
| 4 | -86.6640186309814 | 36.0485112660384 |
| 5 | -86.6623315215110 | 36.0475679119687 |
| 6 | -86.6608375310897 | 36.0466917753056 |
| 7 | -86.6592979431152 | 36.0457939419758 |
| 8 | -86.6576912999153 | 36.0448483866264 |
| 9 | -86.6563770174980 | 36.0441218627600 |
| 10 | -86.6548401117324 | 36.0432196625972 |
| 11 | -86.6532951593399 | 36.0423391399701 |
| 12 | -86.6516268253326 | 36.0413740238091 |
| 13 | -86.6499182581901 | 36.0404305842180 |
| 14 | -86.6484859585762 | 36.0394762889946 |
| 15 | -86.6472119092941 | 36.0386521156311 |
| 16 | -86.6460505127906 | 36.0376630962090 |
| 17 | -86.6449534893035 | 36.0366393612687 |
| 18 | -86.6437357664108 | 36.0355310230575 |
| 19 | -86.6425502300262 | 36.0344812323649 |
| 20 | -86.6412305831909 | 36.0333142998429 |
| 21 | -86.6399243474006 | 36.0321169830776 |
| 22 | -86.6383659839630 | 36.0307396124762 |
| 23 | -86.6372233629226 | 36.0297092801383 |
| 24 | -86.6360297799110 | 36.0286377202112 |
| 25 | -86.6349676251411 | 36.0276897896641 |
| 26 | -86.6338652372360 | 36.0267006325845 |
| 27 | -86.6323256492614 | 36.0253340135559 |
| 28 | -86.6313627362251 | 36.0244836608630 |
| 29 | -86.6299653053283 | 36.0232428236304 |
| 30 | -86.6286617517471 | 36.0220887406933 |
| 31 | -86.6275808215141 | 36.0210930051775 |
| 32 | -86.6263175010681 | 36.0199736012082 |
| 33 | -86.6250273585319 | 36.0188173009549 |
| 34 | -86.6237318515777 | 36.0176848478644 |
| 35 | -86.6225999593734 | 36.0167042431535 |
| 36 | -86.6218060255050 | 36.0158603058791 |
| 37 | -86.6208162903785 | 36.0149816469298 |
| 38 | -86.6197273135185 | 36.0140248738225 |
| 39 | -86.6183325648307 | 36.0128055679068 |
| 40 | -86.6171014308929 | 36.0116643499086 |
| Validation 1 | -86.6094464063644 | 36.0041353684958 |
| Validation 2 | -86.6082850098609 | 36.0030981786895 |
| Validation 3 | -86.6070619225502 | 36.0020240870002 |

TABLE VIII: I-24 MOTION camera pole locations.

## Appendix B Example Vehicle Trajectory

|     |     |     |     |
| --- | --- | --- | --- |
| Attribute | Type | Unit | Value |
| \_id | 12-byte BSON | −- | 63732b74e1fa5a45ae0c2fdd |
| vehicle class | int | −- | 0 |
| first timestamp | float | s | 1668436223.30 |
| last timestamp | float | s | 1668436257.60 |
| timestamp | \[float\] | s | See Table [X](https://arxiv.org/html/2301.11198v2#A2.T10 "TABLE X ‣ Appendix B Example Vehicle Trajectory ‣ I-24 MOTION: An instrument for freeway traffic science") |
| x position | \[float\] | ft | See Table [X](https://arxiv.org/html/2301.11198v2#A2.T10 "TABLE X ‣ Appendix B Example Vehicle Trajectory ‣ I-24 MOTION: An instrument for freeway traffic science") |
| y position | \[float\] | ft | See Table [X](https://arxiv.org/html/2301.11198v2#A2.T10 "TABLE X ‣ Appendix B Example Vehicle Trajectory ‣ I-24 MOTION: An instrument for freeway traffic science") |
| starting x | float | ft | 325400.5531 |
| ending x | float | ft | 329300.5458 |
| length | float | ft | 15.6381 |
| width | float | ft | 5.8521 |
| height | float | ft | 4.7021 |
| direction | int | −- | 1 |
| Configuration ID | int | −- | -1 |

TABLE IX: Detailed information of the example trajectory.

|     |     |     |
| --- | --- | --- |
| timestamp (s) | x position (ft) | y position (ft) |
| 1668436223.30 | 325400.5531 | -19.19265508 |
| 1668436223.34 | 325405.0238 | -19.12047988 |
| 1668436223.38 | 325409.4943 | -19.04921183 |
| 1668436223.42 | 325413.9646 | -18.97885093 |
| 1668436223.46 | 325418.4349 | -18.90939717 |
| ⋯\\cdots | ⋯\\cdots | ⋯\\cdots |
| 1668436257.42 | 329281.8317 | -43.03453987 |
| 1668436257.46 | 329286.5097 | -43.09132499 |
| 1668436257.50 | 329291.1881 | -43.14893520 |
| 1668436257.54 | 329295.8668 | -43.20737050 |
| 1668436257.58 | 329300.5458 | -43.26663087 |

TABLE X: The first 5 and the last 5 trajectory points for the example trajectory.

## Appendix C Coordinate System Conversion

I-24 MOTION relies on 3 sets of coordinates:

- •


Image Coordinates: are given in pixels. (y(i​m),x(i​m))(y^{(im)},x^{(im)}) denotes the row and column of the specified pixel. By convention the top left pixel is (0,0).

- •


State Plane Coordinates: specify a rectilinear and orthogonal coordinate system. The EPSG 2274 state plane coordinate system for Tennessee is specified in feet relative to a known survey point. (x(s​t),y(s​t))(x^{(st)},y^{(st)}) indicates the coordinate (in feet) along the first (roughly horizontal) and second (roughly vertical) coordinate axis defined by the state plane coordinate system. (Note that a common conversion from state plane coordinates to latitude/longitude coordinates (e.g. WSG84 or NAD83) can be utilized if desired.) A third orthogonal coordinate axis (z-axis) is defined and corresponds to distance off the roadway, such that z(s​t)=0z^{(st)}=0 for all points on the roadway plane.

- •


Roadway Coordinates: are defined such that the primary (x) axis lies along the median (or more precisely, midway between the two interior yellow lines for the interstate) at all points within the instrument extents, and the secondary (y) axis is defined locally to perpendicular to the primary axis at all points along the roadway. Note that all coordinates with a distance from the primary axis less than the local radius of curvature have a unique (xr,yr)(x\_{r},y\_{r}) coordinate. By left-hand rule convention, we define the positive y-axis to be in the direction of the eastbound roadway lanes at all points along the roadway.


Throughout the rest of this appendix to disambiguate the various coordinate systems, the following notation is used: xx,yy, and zz refer to coordinate axes. A superscript (i​m)(im), (s​t)(st), or (r)(r) specifies all variables corresponding to a specific coordinate system (e.g. x(s​t)x^{(st)}). Vectors and matrices in that coordinate system are denoted in bold (e.g. O(s​t)\\textbf{O}^{(st)}). Parameter matrices will be listed in “mathcal” script (e.g ℋ\\mathcal{H}). A subscript indexes a specific point (e.g. xb​b​l(s​t)x^{(st)}\_{bbl}), and subscript ii indicates an arbitrary element index from a set of elements (e.g aia\_{i}). An xx,yy, or zz without a subscript indicates a generic variable along the specified axis within the specified coordinate system. A list of all variables along with their descriptions is given in Table [XI](https://arxiv.org/html/2301.11198v2#A3.T11 "TABLE XI ‣ Appendix C Coordinate System Conversion ‣ I-24 MOTION: An instrument for freeway traffic science"):

| Symbol | Definition |
| --- | --- |
| ℋ\\mathcal{H} | 3×\\times3 matrix of homography parameters hi​jh\_{ij} |
| 𝒫\\mathcal{P} | 3×\\times4 matrix of homography parameters pi​jp\_{ij} |
| ss | homography scale parameter |
| x(i​m)x^{(im)}, y(i​m)y^{(im)} | image coordinates (y indicates pixel row and x indicates pixel column) |
| x(s​t)x^{(st)}, y(s​t)y^{(st)}, z(s​t)z^{(st)} | state plane coordinates |
| x(r)x^{(r)}, y(r)y^{(r)} | roadway coordinates |
| 𝐎(s​t)\\mathbf{O}^{(st)} | state plane coordinates for object, equal to \[𝐨b​b​l(s​t)\\mathbf{o}^{(st)}\_{bbl},𝐨b​b​r(s​t)\\mathbf{o}^{(st)}\_{bbr},𝐨b​t​l(s​t)\\mathbf{o}^{(st)}\_{btl} ,𝐨b​t​r(s​t)\\mathbf{o}^{(st)}\_{btr} ,𝐨f​b​l(s​t)\\mathbf{o}^{(st)}\_{fbl} ,𝐨f​b​r(s​t)\\mathbf{o}^{(st)}\_{fbr} ,𝐨f​t​l(s​t)\\mathbf{o}^{(st)}\_{ftl} ,𝐨f​t​r(s​t)\\mathbf{o}^{(st)}\_{ftr}\] |
| 𝐨b​b​l(s​t)\\mathbf{o}^{(st)}\_{bbl} | back bottom left state plane coordinate of object, equal to \[xb​b​l(s​t),yb​b​l(s​t),zb​b​l(s​t)x^{(st)}\_{bbl},y^{(st)}\_{bbl},z^{(st)}\_{bbl}\] |
| 𝐨c(s​t)\\mathbf{o}^{(st)}\_{c} | back bottom center state plane coordinate, primary reference coordinate for the object |
| 𝐨s​p​l(s​t)\\mathbf{o}^{(st)}\_{spl} | state plane coordinates of point on center-line spline (y(r)=0y^{(r)}=0) with the same x(r)x^{(r)} coordinate as 𝐨c(s​t)\\mathbf{o}^{(st)}\_{c} |
| 𝐎(r)\\mathbf{O}^{(r)} | roadway coordinates for object, \[x(r)o,y(r)o,l,w,h\]\[x^{(r)\_{o}},y^{(r)\_{o}},l,w,h\] |
| x(r)x^{(r)} | generic longitudinal roadway coordinate along curvilinear spline axis |
| y(r)y^{(r)} | generic lateral roadway coordinate along axis locally perpendicular to longitudinal roadway coordinate axis |
| xo(r)x^{(r)}\_{o} | object longitudinal roadway coordinate along curvilinear spline axis |
| yo(r)y^{(r)}\_{o} | object lateral roadway coordinate along axis locally perpendicular to longitudinal roadway coordinate axis |
| ll,ww,hh | rectangular prism dimensions (length, width and height) |
| F⁡(x(r))F(x^{(r)}) | spline defining state plane coordinate roadway center-line spline parameterized by x(r)x^{(r)} |
| G~​(x(s​t))\\tilde{G}(x^{(st)}) | spline approximating the center-line spline in roadway coordinates x(r)x^{(r)} parameterized by x(s​t)x^{(st)} |

TABLE XI: Summary of symbols used in Appendix [C](https://arxiv.org/html/2301.11198v2#A3 "Appendix C Coordinate System Conversion ‣ I-24 MOTION: An instrument for freeway traffic science")

Transformations between image and state plane coordinates, and transformations between state plane and roadway coordinates are detailed in the next two sections.

### C-AImage to State Plane Conversion

A homography relates two views of a planar surface. For each camera, we provide homography information such that the 8-corner coordinates of the stored 3D bounding-box annotation can be projected into any camera view for which the vehicle is visible, creating a monocular 3D bounding box within that camera field of view. For each direction of travel in each camera view, for each scene, a homography relating the image pixel coordinates to the state plane coordinate system is defined. (Though the same cameras are used for different scenes, the positions of the cameras changes slightly over time due). A local flat plane assumption is used (the state plane coordinate system is assumed to be piece-wise flat) \[ [108](https://arxiv.org/html/2301.11198v2#bib.bib108 "")\]. A series of correspondence points series of correspondence points ai=\[x(i​m),y(i​m),x(s​t),y(s​t),z(s​t)\]a\_{i}=\[x^{(im)},y^{(im)},x^{(st)},y^{(st)},z^{(st)}\] are used to define this relation, where (y(i​m),x(i​m))(y^{(im)},x^{(im)}) is the coordinate of selected correspondence point aa in pixel coordinates (row, column) and (x(s​t),y(s​t),z(s​t))(x^{(st)},y^{(st)},z^{(st)}) is the selected correspondence point in state plane coordinates.

All selected points are assumed to lie on the state plane, so z(s​t)=0z^{(st)}=0 for all selected correspondence points. Visible lane marking lines and other easily recognizable landmarks on the roadway are used as correspondence points in each camera field of view. Each correspondence point is also labeled in global information system (GIS) software, giving the precise GPS / state-plane coordinate system coordinates for each labeled corresponding point. The corresponding pixel coordinates are manually selected in each camera field of view, for each direction of travel on the roadway.

A perspective transform (Equation [2](https://arxiv.org/html/2301.11198v2#A3.E2 "In C-A Image to State Plane Conversion ‣ Appendix C Coordinate System Conversion ‣ I-24 MOTION: An instrument for freeway traffic science")) is fit to these correspondence points. We first define a 2D perspective transform which defines a linear mapping (Equation [1](https://arxiv.org/html/2301.11198v2#A3.E1 "In C-A Image to State Plane Conversion ‣ Appendix C Coordinate System Conversion ‣ I-24 MOTION: An instrument for freeway traffic science")) of points from one plane to another that preserves straight lines. The correspondence points are then used to solve for the best perspective transform ℋ\\mathcal{H} as defined in equation [2](https://arxiv.org/html/2301.11198v2#A3.E2 "In C-A Image to State Plane Conversion ‣ Appendix C Coordinate System Conversion ‣ I-24 MOTION: An instrument for freeway traffic science"), where ss is a scale factor.

|     |     |     |     |
| --- | --- | --- | --- |
|  | s​\[xi(s​t)yi(s​t)1\]∼ℋ​\[xi(i​m)yi(i​m)1\]s\\begin{bmatrix}x^{(st)}\_{i}\\\<br>y^{(st)}\_{i}\\\<br>1\\end{bmatrix}\\sim\\mathcal{H}\\begin{bmatrix}x^{(im)}\_{i}\\\<br>y^{(im)}\_{i}\\\<br>1\\end{bmatrix} |  | (1) |

where ℋ\\mathcal{H} is a 3×33\\times 3 matrix of parameters:

|     |     |     |     |
| --- | --- | --- | --- |
|  | ℋ=\[h11h12h13h21h22h23h31h32h33\]\\mathcal{H}=\\begin{bmatrix}h\_{11}&h\_{12}&h\_{13}\\\<br>h\_{21}&h\_{22}&h\_{23}\\\<br>h\_{31}&h\_{32}&h\_{33}\\end{bmatrix} |  | (2) |

For each camera field of view and each direction of travel, the best perspective transform ℋ∗\\mathcal{H}^{\*} is determined by minimizing the sum of squared re-projection errors according to equation [3](https://arxiv.org/html/2301.11198v2#A3.E3 "In C-A Image to State Plane Conversion ‣ Appendix C Coordinate System Conversion ‣ I-24 MOTION: An instrument for freeway traffic science") as implemented in OpenCV’s f​i​n​d​\_​h​o​m​o​g​r​a​p​h​yfind\\mathunderscore homography function \[ [109](https://arxiv.org/html/2301.11198v2#bib.bib109 "")\]:

|     |     |     |     |
| --- | --- | --- | --- |
|  | ℋ∗=arg​minℋ∑i(xi(st)−h11​xi(im)+h12​yi(im)+h13h31​xi(im)+h32​yi(im)+h33)2+(yi(st)−h21​xi(im)+h22​yi(im)+h23h31​xi(im)+h32​yi(im)+h33)2\\mathcal{H}^{\*}=\\argmin\_{\\mathcal{H}}\\sum\_{i}\\left(x^{(st)}\_{i}-\\frac{h\_{11}x^{(im)}\_{i}+h\_{12}y^{(im)}\_{i}+h\_{13}}{h\_{31}x^{(im)}\_{i}+h\_{32}y^{(im)}\_{i}+h\_{33}}\\right)^{2}+\\left(y^{(st)}\_{i}-\\frac{h\_{21}x^{(im)}\_{i}+h\_{22}y^{(im)}\_{i}+h\_{23}}{h\_{31}x^{(im)}\_{i}+h\_{32}y^{(im)}\_{i}+h\_{33}}\\right)^{2} |  | (3) |

The resulting matrix ℋ∗\\mathcal{H}^{\*} allows any point lying on the plane within the camera field of view to be converted into state plane coordinates. The corresponding matrix ℋi​n​v\\mathcal{H}\_{inv} can easily be obtained to convert roadway coordinates on the plane into image coordinates. However, since each vehicle is represented by a 3D bounding box, the top corner coordinates of the box do not lie on the ground plane. A 3D perspective transform 𝒫\\mathcal{P} is needed to linearly map coordinates from 3D state plane coordinate space to 2D image coordinate space, where 𝒫\\mathcal{P} is a 3×43\\times 4 matrix of parameters:

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝒫=\[p11p12p13p14p21p22p23p24p31p32p33p34\]\\mathcal{P}=\\begin{bmatrix}p\_{11}&p\_{12}&p\_{13}&p\_{14}\\\<br>p\_{21}&p\_{22}&p\_{23}&p\_{24}\\\<br>p\_{31}&p\_{32}&p\_{33}&p\_{34}\\end{bmatrix} |  | (4) |

and 𝒫\\mathcal{P} projects a point in 3D space (x′,y′,z′)(x^{\\prime},y^{\\prime},z^{\\prime}) into the corresponding image point (x,y)(x,y) according to:

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝒫​\[x(s​t)y(s​t)z(s​t)1\]∼s′​\[x(i​m)y(i​m)1\]\\mathcal{P}\\begin{bmatrix}x^{(st)}\\\<br>y^{(st)}\\\<br>z^{(st)}\\\<br>1\\end{bmatrix}\\sim s^{\\prime}\\begin{bmatrix}x^{(im)}\\\<br>y^{(im)}\\\<br>1\\end{bmatrix} |  | (5) |

where s′s^{\\prime} is a new scaling parameter. By observing the case where z(s​t)=0z^{(st)}=0, it is evident columns 1,2, and 4 of 𝒫\\mathcal{P} are equivalent to the columns of ℋi​n​v\\mathcal{H}\_{inv} and can be fit in the same way. Thus, we need only solve for column 3 of 𝒫\\mathcal{P}. Next, we note as in \[ [108](https://arxiv.org/html/2301.11198v2#bib.bib108 "")\] that (p11p31,p21p31)(\\frac{p\_{11}}{p\_{31}},\\frac{p\_{21}}{p\_{31}}) is the vanishing point (in image coordinates) of perspective lines drawn in the same direction as the state plane coordinate x-axis. The same is true for the 2nd column and the state plane coordinate y-axis, the 3rd column and the state plane coordinate z-axis, and the 4th column and the state plane coordinate origin.

Thus, to fully determine 𝒫\\mathcal{P} it is sufficient to locate the vanishing point of the z-axis in state plane coordinates and to estimate the scaling parameter p33p\_{33}. The vanishing point is located in image coordinates by finding the intersection point between lines drawn in the z-direction. Such lines are obtained by manually annotating vertical lines in each camera field of view. The scale parameter is estimated by minimizing the sum of squared reprojection errors defined in equation [6](https://arxiv.org/html/2301.11198v2#A3.Ex1 "In C-A Image to State Plane Conversion ‣ Appendix C Coordinate System Conversion ‣ I-24 MOTION: An instrument for freeway traffic science") for a sufficiently large set of state plane coordinates and corresponding, manually annotated coordinates in image space.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
|  | 𝒫∗=arg​minp33∑i\\displaystyle\\mathcal{P}^{\*}=\\argmin\_{p\_{33}}\\sum\_{i} | (xi(i​m)−p11​xi(s​t)+p12​yi(s​t)+p13​zi(s​t)+p14p31​xi(s​t)+p32​yi(s​t)+p33​zi(s​t)+p34)2+\\displaystyle\\left(x^{(im)}\_{i}-\\frac{p\_{11}x^{(st)}\_{i}+p\_{12}y^{(st)}\_{i}+p\_{13}z^{(st)}\_{i}+p\_{14}}{p\_{31}x^{(st)}\_{i}+p\_{32}y^{(st)}\_{i}+p\_{33}z^{(st)}\_{i}+p\_{34}}\\right)^{2}+ |  |
|  |  | (yi(i​m)−p21​xi(s​t)+p22​yi(s​t)+p23​zi(s​t)+h24p31​xi(s​t)+p32​yi(s​t)+p33​zi(s​t)+h34)2\\displaystyle\\left(y^{(im)}\_{i}-\\frac{p\_{21}x^{(st)}\_{i}+p\_{22}y^{(st)}\_{i}+p\_{23}z^{(st)}\_{i}+h\_{24}}{p\_{31}x^{(st)}\_{i}+p\_{32}y^{(st)}\_{i}+p\_{33}z^{(st)}\_{i}+h\_{34}}\\right)^{2} |  | (6) |

The resulting 3D perspective transform 𝒫∗\\mathcal{P}^{\*} allows for the lossless conversion of points in roadway coordinates to the corresponding points in image coordinates. Observing that a lossless conversion from image coordinates to state plane coordinates is available provided that the converted point lies on the z(s​t)=0z^{(st)}=0 plane, it is possible to precisely convert a rectangular prism from image space to state plane coordinates by i.) converting the footprint of the prism near-losslessly into state plane coordinates (the only source of error comes from a set of 4 image coordinates that cannot be perfectly converted into a rectangle in state plane coordinates), ii.) shifting the footprint in state plane coordinates along the z-axis, iii.) re-projecting the resulting points back into the image, iv.) comparing the reprojected “top points” to the original top of the rectangular prism in image coordinates, and v.) adjusting the height iterative to minimize the re-projection error until convergence.

### C-BState Plane to Roadway Coordinate Conversion

Next, we consider the conversion of points in state plane coordinates to roadway coordinates. In most cases, we care to convert a set of state plane coordinate points roughly in a rectangular prism (i.e. vehicle 3D bounding box) into roadway coordinates; thus, we define this conversion for a rectangular prism. A single point can be converted between state plane coordinates and roadway coordinates by treating it as a rectangular prism with zero length, width and height.

Let 𝐎(s​t)\\mathbf{O}^{(st)} be a 3D bounding box representation in state plane coordinates, an 8×\\times3 matrix of x,y, and z coordinates for each corner of the box. (Note that these corners need not exactly correspond to an orthogonal rectangular prism, but the roadway coordinate equivalent will be exactly orthogonal so some truncation error will occur.) We reference, for example, the back bottom right (from the perspective of the rear of the vehicle) of object 𝐎(s​t)\\mathbf{O}^{(st)} as 𝐨b​b​r(s​t)=\[xb​b​r(s​t),yb​b​r(s​t),zb​b​r(s​t)\]\\mathbf{o}\_{bbr}^{(st)}=\[x^{(st)}\_{bbr},y^{(st)}\_{bbr},z^{(st)}\_{bbr}\], such that = 𝐎(s​t)=\[𝐨b​b​l(s​t),𝐨b​b​r(s​t),𝐨b​t​l(s​t),𝐨b​t​r(s​t),𝐨f​b​l(s​t),𝐨f​b​r(s​t),𝐨f​t​l(s​t),𝐨f​t​r(s​t)\]\\mathbf{O}^{(st)}=\[\\mathbf{o}^{(st)}\_{bbl},\\mathbf{o}^{(st)}\_{bbr},\\mathbf{o}^{(st)}\_{btl},\\mathbf{o}^{(st)}\_{btr},\\mathbf{o}^{(st)}\_{fbl},\\mathbf{o}^{(st)}\_{fbr},\\mathbf{o}^{(st)}\_{ftl},\\mathbf{o}^{(st)}\_{ftr}\]. (For the single-point case described above, all 8 corner coordinates are identical).

Next, Let 𝐎(r)=\[xo(r),yo(r),l,w,h\]\\mathbf{O}^{(r)}=\[x^{(r)}\_{o},y^{(r)}\_{o},l,w,h\] be the corresponding object representation of 𝐎(s​t)\\mathbf{O}^{(st)} in roadway coordinates. x(r)x^{(r)} and y(r)y^{(r)} are the roadway coordinate longitudinal and lateral coordinates (in feet), and ll, ww,and hh are the length, width, and height of the object respectively (in feet).

Let 𝐨(s​t)c\\mathbf{o}^{(st)\_{c}} denote the back bottom center coordinate of object 𝐎(s​t)\\mathbf{O}^{(st)}. By convention, this point is referenced as the primary position of object 𝐎(s​t)\\mathbf{O}^{(st)}. Let 𝐨(s​t)s​p​l\\mathbf{o}^{(st)\_{spl}} denote the point on the center-line spline (i.e. y(r)=0y^{(r)}=0) with the same x(r)x^{(r)} coordinate as 𝐨c(s​t)\\mathbf{o}^{(st)}\_{c}.

Let FF be the second-order spline parameterizing the roadway center-line in state plane coordinates. In other words, FF defines the longitudinal curvilinear axis y(r)=0y^{(r)}=0 along this spline. FF is fit by manually labeling a sufficiently large number of points along the interior yellow line for both directions of travel (in state plane coordinates). A spline is fit to each yellow line, and a third spline is fit to lie precisely halfway between these two splines. Spline control points are selected at suitably sparse intervals (200 foot minimum spacing) such that the spline is relatively smooth while still capturing the roadway curvature.

Given 𝐎(s​t)\\mathbf{O}^{(st)}, we first obtain ll,ww and hh by computing the average distance between points on the front and back, left and right, or top and bottom of the vehicle respectively. Next, we obtain 𝐨c(s​t)\\mathbf{o}^{(st)}\_{c} by computing the average x(s​t)x^{(st)} and y(s​t)y^{(st)} state plane coordinates of the 4 back rectangular prism corners.

Next, we solve for xo(r)x^{(r)}\_{o} by solving the following optimization:

|     |     |     |     |
| --- | --- | --- | --- |
|  | xo(r)=arg​minx(r)⁡(dist​(F⁡(x(r)),𝐨c(st)))x^{(r)}\_{o}=\\argmin\_{x^{(r)}}(\\text{dist}(F(x^{(r)}),\\mathbf{o}^{(st)}\_{c})) |  | (7) |

Where “dist” indicates the Euclidean distance between the two points in state plane coordinate space. In other words, determine the point on the roadway spline closest to the back center of the rectangular prism 𝐨c(s​t)\\mathbf{o}^{(st)}\_{c}. This minimizing point is the corresponding roadway longitudinal coordinate xo(r)x^{(r)}\_{o}, and the distance from the minimum distance point is roadway lateral coordinate yo(r)y^{(r)}\_{o}.

|     |     |     |     |
| --- | --- | --- | --- |
|  | yo(r)=minx(r)⁡(dist​(F⁡(x(r)),𝐨c(s​t)))y^{(r)}\_{o}=\\min\_{x^{(r)}}(\\text{dist}(F(x^{(r)}),\\mathbf{o}^{(st)}\_{c})) |  | (8) |

Noting that the I-24 MOTION roadway segment has monotonically increasing x(s​t)x^{(st)} coordinate, we define a secondary spline G~​(x(s​t))\\tilde{G}(x^{(st)}) to parameterize x(r)x^{(r)} as a function of x(s​t)x^{(st)}, which yields a good initial guess for the closest roadway longitudinal coordinate for a given point in state plane coordinates. This optimization can then be solved to arbitrary precision, yielding the complete roadway coordinate for the object 𝐎(r)=\[xo(r),yo(r),l,w,h\]\\mathbf{O}^{(r)}=\[x^{(r)}\_{o},y^{(r)}\_{o},l,w,h\].

### C-CRoadway to State Plane Coordinate Conversion

Given roadway coordinates for an object 𝐎(r)\\mathbf{O}^{(r)}, first find the corresponding point on the roadway center-line spline in state plane coordinates 𝐨c(s​t)\\mathbf{o}^{(st)}\_{c} according to:

|     |     |     |     |
| --- | --- | --- | --- |
|  | F⁡(xo(r))=𝐨s​p​l(s​t)F(x^{(r)}\_{o})=\\mathbf{o}^{(st)}\_{spl} |  | (9) |

To obtain the back center coordinate 𝐨c(s​t)\\mathbf{o}^{(st)}\_{c}, we must offset 𝐨s​p​l(s​t)\\mathbf{o}^{(st)}\_{spl} by length y(r)y^{(r)} in the direction perpendicular to the roadway centerline spline at 𝐨c(s​t)\\mathbf{o}^{(st)}\_{c}. Let 𝐮→F\\overrightarrow{\\mathbf{u}}\_{F} be the unit vector in the same direction as the derivative spline F′F^{\\prime}, and let 𝐮→1/F\\overrightarrow{\\mathbf{u}}\_{1/F} be the unit vector in the perpendicular direction (along the state plane, i.e. z(s​t)=0z^{(st)}=0. Note that care should be given to ensure that the positive direction of 𝐮→1/F\\overrightarrow{\\mathbf{u}}\_{1/F} points towards the eastbound side of the roadway with positive y(r)y^{(r)}.) Then, 𝐨c(s​t)\\mathbf{o}^{(st)}\_{c} is given by:

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝐨c(s​t)=𝐨s​p​l(s​t)+y(r)⋅𝐮→1/F\\mathbf{o}^{(st)}\_{c}=\\mathbf{o}^{(st)}\_{spl}+y^{(r)}\\cdot\\overrightarrow{\\mathbf{u}}\_{1/F} |  | (10) |

From here, the corner state plane coordinates for the right and left coordinates of the rectangular prism can be obtained by offsetting 𝐨c(s​t)\\mathbf{o}^{(st)}\_{c} by ±12\\pm\\frac{1}{2} times ww in the direction of 𝐮→1/F\\overrightarrow{\\mathbf{u}}\_{1/F}, and the front coordinates of the rectangular prism can similarly be obtained by offsetting by ll in the direction of 𝐮→F\\overrightarrow{\\mathbf{u}}\_{F} or in the opposite direction for objects on the westbound or negative y(r)y^{(r)} side of the roadway. Similarly, the top coordinates can be obtained by offsetting by a factor of hh in the z(s​t)z^{(st)} direction. The direction of travel for an object can be obtained as the sign of the y(r)y^{(r)} coordinate (negative for WB, positive for EB).For example, for an eastbound object the front top left coordinate can be obtained as:

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝐨f​t​l(s​t)=𝐨c(s​t)−12⋅w⋅𝐮→1/F+l⋅𝐮→F+h⋅\[𝟎,𝟎,𝟏\]\\mathbf{o}^{(st)}\_{ftl}=\\mathbf{o}^{(st)}\_{c}-\\frac{1}{2}\\cdot w\\cdot\\overrightarrow{\\mathbf{u}}\_{1/F}+l\\cdot\\overrightarrow{\\mathbf{u}}\_{F}+h\\cdot\\mathbf{\[0,0,1\]} |  | (11) |

## Appendix D Additional space time diagrams

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/TS_2022-11-21_resized.png)(a)Monday Nov 21 2022

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/TS_2022-11-22_resized.png)(b)Tuesday Nov 22 2022

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/TS_2022-11-23_resized.png)(c)Wednesday Nov 23 2022

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/TS_2022-11-24_resized.png)(d)Thursday Nov 24 2022 (Thanksgiving)

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/TS_2022-11-25_resized.png)(e)Friday Nov 25 2022 (Black Friday)

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/TS_2022-11-28_resized.png)(a)Monday Nov 28 2022

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/TS_2022-11-29_resized.png)(b)Tuesday Nov 29 2022

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/TS_2022-11-30_resized.png)(c)Wednesday Nov 30 2022

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/TS_2022-12-01_resized.png)(d)Thursday Dec 1 2022

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/TS_2022-12-02_resized.png)(e)Friday Dec 2 2022

Fig. 16: Additional time-space diagrams for I-24 westbound during morning rush hours on a) Nov 21, b) Nov 23, c) Nov 29, d) Dec 1 and e) Dec 2, 2022.

## Appendix E Lane-Dis-aggregated Time-Space Diagrams

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/Lane1.png)(a)Lane 1 (HOV Lane)

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/Lane2.png)(b)Lane 2

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/Lane3.png)(c)Lane 3

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/Lane4.png)(d)Lane 4

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/cbar.png)

Fig. 17: Lane separated time-space diagrams (Wednesday, Nov 30 2022, 6:00-10:00 AM).

## Appendix F Traffic Wave Calculations

### F-AWave propagation speed

The wave propagation speed is characterized by the slope of the slowdown that propagates upstream in the time-space diagram shown in [11](https://arxiv.org/html/2301.11198v2#S5.F11 "Fig. 11 ‣ V-A Traffic wave properties ‣ V Discussion ‣ I-24 MOTION: An instrument for freeway traffic science"). The slope is calculated based on the cross-correlation method as used in \[ [110](https://arxiv.org/html/2301.11198v2#bib.bib110 ""), [104](https://arxiv.org/html/2301.11198v2#bib.bib104 "")\], which compares the time series of the speed signals observed at two nearby locations on the same congested freeway. The idea is to shift one signal relative to another until the first non-trivial peaks are matched. The wave propagation speed is therefore the ratio between the time shifted and the distance of these two locations. We randomly select a few pairs of locations from one trajectory dataset and obtain a distribution of propagation speed. The distribution for the morning of Nov 22 2022, for example, has a mean of 12.8 mph and a standard deviation of 0.5 mph.

### F-BWave frequency analysis

Wavelet transform is a time-frequency decomposition tool to effectively extract the non-stationary wave properties present in signals. The continuous wavelet transform is a convolution of the time-series signal x⁡(t)x(t) with a set of functions generated by the mother wavelet ψ⁡(t)\\psi(t):

|     |     |     |     |
| --- | --- | --- | --- |
|  | Xw​(a,b)=1\|a\|1/2​∫−∞∞x⁡(t)​ψ​(t−ba)​𝑑t,X\_{w}(a,b)=\\frac{1}{\|a\|^{1/2}}\\int\_{-\\infty}^{\\infty}x(t){\\psi}\\left(\\frac{t-b}{a}\\right)dt, |  | (12) |

where Xw​(a,b)X\_{w}(a,b) is a transformed signal at location bb and scale aa in the wavelet dimension. The scaling factor and the translation factor vary continuously, providing an overcomplete representation of the signals. We select a commonly used mother wavelet as a Morlet wavelet:

|     |     |     |     |
| --- | --- | --- | --- |
|  | ψ⁡(t)=e−t22​cos⁡(5​t).\\psi(t)=e^{-\\frac{t^{2}}{2}}\\cos(5t). |  | (13) |

![Refer to caption](https://arxiv.org/html/2301.11198v2/figures/wt_post9.png)Fig. 18: Top: the speed time-series sampled from MM61.2 on Tuesday, Nov 29 2022. Bottom: a scaleogram produced by continuous wavelet transform of the speed signal. The color represents log-scale of the power distribution across both frequency and time domain of the signal.

An example of wavelet transform result is shown in Figure [18](https://arxiv.org/html/2301.11198v2#A6.F18 "Fig. 18 ‣ F-B Wave frequency analysis ‣ Appendix F Traffic Wave Calculations ‣ I-24 MOTION: An instrument for freeway traffic science"). The top figure shows the time-series of speed sampled at a fixed location (in this case MM61.2) on Tuesday, Nov 29 2022. The bottom one is the corresponding wavelet transform scaleogram of the signal. It is obvious that the traffic waves do not appear to be stationary, i.e., the speed oscillation does not have a unique and consistent frequency across time. For example, during 6:50AM-7:30AM, the power of the signal peaks around 6.7min, corresponding to a salient wave period of 6.7min; during 8:30AM-9:30AM, the prominent wave period is near 9min.

## Acknowledgment

The authors would like to thank Lee Smith, Brad Freeze, the Tennessee Department of Transportation, Meredith Cebelak, Matt D’Angelo and Gresham Smith for their efforts on conceptualizing, designing and implementing the system, Craig Philip and Janos Sztipanovits for their assistance conceptualizing I-24 MOTION. The authors would like to thank Eric Hall for his support on network, hardware, and software integration, and Zi Nean Teoh and Lisa Liu for their contributions to develop, build and deploy the I-24 MOTION system software architecture. The authors are grateful to Davis H. Elliot for constructing the instrument and WSP for serving as CEI for I-24 MOTION construction. This work is supported by the National Science Foundation (NSF) under Grant No. 2135579, the NSF Graduate Research Fellowship Grant No. DGE-1937963 and the USDOT Dwight D. Eisenhower Fellowship program under Grant No. 693JJ32245006 (Gloudemans) and No. 693JJ322NF5201 (Wang). This material is based upon work supported by the U.S. Department of Energy’s Office of Energy Efficiency and Renewable Energy (EERE) award number CID DE-EE0008872. The views expressed herein do not necessarily represent the views of the U.S. Department of Energy or the United States Government.

## References

- \[1\]
V. Alexiadis, J. Colyar, J. Halkias, R. Hranac, and G. McHale, “The next
generation simulation program,” _Institute of Transportation Engineers._
_ITE Journal_, vol. 74, no. 8, p. 22, 2004.

- \[2\]
R. Krajewski, J. Bock, L. Kloeker, and L. Eckstein, “The highd dataset: A
drone dataset of naturalistic vehicle trajectories on german highways for
validation of highly automated driving systems,” in _2018 21st_
_International Conference on Intelligent Transportation Systems (ITSC)_. IEEE, 2018, pp. 2118–2125.

- \[3\]
E. Barmpounakis and N. Geroliminis, “On the new era of urban traffic
monitoring with massive drone data: The pneuma large-scale field
experiment,” _Transportation research part C: emerging technologies_,
vol. 111, pp. 50–71, 2020.

- \[4\]
T. Moers, L. Vater, R. Krajewski, J. Bock, A. Zlocki, and L. Eckstein, “The
exid dataset: A real-world trajectory dataset of highly interactive highway
scenarios in germany,” in _2022 IEEE Intelligent Vehicles Symposium_
_(IV)_, 2022, pp. 958–964.

- \[5\]
P. Spannaus, P. Zechel, and K. Lenz, “Automatum data: Drone-based highway
dataset for the development and validation of automated driving software for
research and commercial applications,” in _2021 IEEE Intelligent_
_Vehicles Symposium (IV)_. IEEE, 2021,
pp. 1372–1377.

- \[6\]
X. Shi, D. Zhao, H. Yao, X. Li, D. K. Hale, and A. Ghiasi, “Video-based
trajectory extraction with deep learning for high-granularity highway
simulation (high-sim),” _Communications in transportation research_,
vol. 1, p. 100014, 2021.

- \[7\]
T. Seo, Y. Tago, N. Shinkai, M. Nakanishi, J. Tanabe, D. Ushirogochi,
S. Kanamori, A. Abe, T. Kodama, S. Yoshimura _et al._, “Evaluation of
large-scale complete vehicle trajectories dataset on two kilometers highway
segment for one hour duration: Zen traffic data,” in _2020_
_International Symposium on Transportation Data and Modelling_, 2020.

- \[8\]
A. D. May, _Traffic flow fundamentals_. Prentice Hall, 1990.

- \[9\]
D. S. Turner, _75 Years of the Fundamental Diagram for Traffic Flow_
_Theory: Greenshields Symposium: July 8-10, 2008, Woods Hole,_
_Massachusetts_. Transportation
Research Board, 2011.

- \[10\]
B. Greenshields, J. Bibbins, W. Channing, and H. Miller, “A study of traffic
capacity,” in _Highway research board proceedings_, vol. 1935. National Research Council (USA), Highway
Research Board, 1935.

- \[11\]
H. Greenberg, “An analysis of traffic flow,” _Operations research_,
vol. 7, no. 1, pp. 79–85, 1959.

- \[12\]
M. J. Lighthill and G. B. Whitham, “On kinematic waves ii. a theory of traffic
flow on long crowded roads,” _Proceedings of the Royal Society of_
_London. Series A. Mathematical and Physical Sciences_, vol. 229, no. 1178,
pp. 317–345, 1955.

- \[13\]
A. Aw and M. Rascle, “Resurrection of” second order” models of traffic flow,”
_SIAM journal on applied mathematics_, vol. 60, no. 3, pp. 916–938,
2000.

- \[14\]
R. P. Roess, E. S. Prassas, and W. R. McShane, _Traffic_
_engineering_. Pearson/Prentice Hall,
2004.

- \[15\]
T. Choe, A. Skabardonis, and P. Varaiya, “Freeway performance measurement
system: operational analysis tool,” _Transportation research record_,
vol. 1811, no. 1, pp. 67–75, 2002.

- \[16\]
M. Schönhof and D. Helbing, “Empirical features of congested traffic
states and their implications for traffic modeling,” _Transportation_
_Science_, vol. 41, no. 2, pp. 135–166, 2007.

- \[17\]
R. Stewart, M. Freeman, N. Taylor, and D. Fereday, “Highways agency active
traffic management: initial driver reactions to its implementation on the
m42,” in _PROCEEDINGS OF THE 13th ITS WORLD CONGRESS, LONDON, 8-12_
_OCTOBER 2006_, 2006.

- \[18\]
H. Bar-Gera, “Evaluation of a cellular phone-based system for measurements of
traffic speeds and travel times: A case study from israel,”
_Transportation Research Part C: Emerging Technologies_, vol. 15, no. 6,
pp. 380–391, 2007.

- \[19\]
J. C. Herrera, D. B. Work, R. Herring, X. J. Ban, Q. Jacobson, and A. M. Bayen,
“Evaluation of traffic data obtained via gps-enabled mobile phones: The
mobile century field experiment,” _Transportation Research Part C:_
_Emerging Technologies_, vol. 18, no. 4, pp. 568–583, 2010.

- \[20\]
D. Helbing, “Empirical traffic data and their implications for traffic
modeling,” _Physical Review E_, vol. 55, no. 1, p. R25, 1997.

- \[21\]
D. Helbing and M. Treiber, “Jams, waves, and clusters,” _Science_, vol.
282, no. 5396, pp. 2001–2003, 1998.

- \[22\]
B. S. Kerner, “The physics of traffic,” _Physics World_, vol. 12, no. 8,
p. 25, 1999.

- \[23\]
M. Treiber, A. Hennecke, and D. Helbing, “Congested traffic states in
empirical observations and microscopic simulations,” _Physical review_
_E_, vol. 62, no. 2, p. 1805, 2000.

- \[24\]
Z. Zheng, S. Ahn, D. Chen, and J. Laval, “Applications of wavelet transform
for analysis of freeway traffic: Bottlenecks, transient traffic, and traffic
oscillations,” _Transportation Research Part B: Methodological_,
vol. 45, no. 2, pp. 372–384, 2011.

- \[25\]
R. E. Chandler, R. Herman, and E. W. Montroll, “Traffic dynamics: studies in
car following,” _Operations research_, vol. 6, no. 2, pp. 165–184,
1958.

- \[26\]
A. Kesting and M. Treiber, “Calibrating car-following models by using
trajectory data: Methodological study,” _Transportation Research_
_Record_, vol. 2088, no. 1, pp. 148–156, 2008.

- \[27\]
W. D. Jones, “Keeping cars from crashing,” _IEEE spectrum_, vol. 38,
no. 9, pp. 40–45, 2001.

- \[28\]
D. Göhring, M. Wang, M. Schnürmacher, and T. Ganjineh, “Radar/lidar
sensor fusion for car-following on highways,” in _The 5th International_
_Conference on Automation, Robotics and Applications_. IEEE, 2011, pp. 407–412.

- \[29\]
G. S. Gurusinghe, T. Nakatsuji, Y. Azuta, P. Ranjitkar, and Y. Tanaboriboon,
“Multiple car-following data with real-time kinematic global positioning
system,” _Transportation Research Record_, vol. 1802, no. 1, pp.
166–180, 2002.

- \[30\]
X. Ma and I. Andréasson, “Estimation of driver reaction time from
car-following data: Application in evaluation of general motor–type model,”
_Transportation research record_, vol. 1965, no. 1, pp. 130–141, 2006.

- \[31\]
J. Treiterer and J. Myers, “The hysteresis phenomenon in traffic flow,”
_Transportation and traffic theory_, vol. 6, pp. 13–38, 1974.

- \[32\]
S. Ossen and S. P. Hoogendoorn, “Car-following behavior analysis from
microscopic trajectory data,” _Transportation Research Record_, vol.
1934, no. 1, pp. 13–21, 2005.

- \[33\]
S. Ossen, S. P. Hoogendoorn, and B. G. Gorte, “Interdriver differences in
car-following: A vehicle trajectory–based study,” _Transportation_
_Research Record_, vol. 1965, no. 1, pp. 121–129, 2006.

- \[34\]
S. Ossen and S. P. Hoogendoorn, “Validity of trajectory-based calibration
approach of car-following models in presence of measurement errors,”
_Transportation Research Record_, vol. 2088, no. 1, pp. 117–125, 2008.

- \[35\]
A. Tordeux, S. Lassarre, and M. Roussignol, “An adaptive time gap
car-following model,” _Transportation research part B: methodological_,
vol. 44, no. 8-9, pp. 1115–1131, 2010.

- \[36\]
H. N. Koutsopoulos and H. Farah, “Latent class model for car following
behavior,” _Transportation research part B: methodological_, vol. 46,
no. 5, pp. 563–578, 2012.

- \[37\]
N. Deo and M. M. Trivedi, “Multi-modal trajectory prediction of surrounding
vehicles with maneuver based lstms,” in _2018 IEEE Intelligent Vehicles_
_Symposium (IV)_. IEEE, 2018, pp.
1179–1184.

- \[38\]
F. Altché and A. de La Fortelle, “An lstm network for highway trajectory
prediction,” in _2017 IEEE 20th international conference on intelligent_
_transportation systems (ITSC)_. IEEE,
2017, pp. 353–359.

- \[39\]
H. Yeo and A. Skabardonis, “Understanding stop-and-go traffic in view of
asymmetric traffic theory,” in _Transportation and Traffic Theory 2009:_
_Golden Jubilee_. Springer, 2009, pp.
99–115.

- \[40\]
J. A. Laval and C. F. Daganzo, “Lane-changing in traffic streams,”
_Transportation Research Part B: Methodological_, vol. 40, no. 3, pp.
251–264, 2006.

- \[41\]
X. Li, J. Cui, S. An, and M. Parsafard, “Stop-and-go traffic analysis:
Theoretical properties, environmental impacts and oscillation mitigation,”
_Transportation Research Part B: Methodological_, vol. 70, pp. 319–339,
2014.

- \[42\]
J. A. Laval and L. Leclercq, “A mechanism to describe the formation and
propagation of stop-and-go waves in congested freeway traffic,”
_Philosophical Transactions of the Royal Society A: Mathematical,_
_Physical and Engineering Sciences_, vol. 368, no. 1928, pp. 4519–4541, 2010.

- \[43\]
L. Li, R. Jiang, Z. He, X. M. Chen, and X. Zhou, “Trajectory data-based
traffic flow studies: A revisit,” _Transportation Research Part C:_
_Emerging Technologies_, vol. 114, pp. 225–240, 2020.

- \[44\]
B. S. Kerner and H. Lieu, “The physics of traffic: Empirical freeway pattern
features, engineering applications; and theory,” _Physics Today_,
vol. 58, no. 11, pp. 54–56, 2005.

- \[45\]
T. Seo, A. M. Bayen, T. Kusakabe, and Y. Asakura, “Traffic state estimation on
highway: A comprehensive survey,” _Annual reviews in control_, vol. 43,
pp. 128–151, 2017.

- \[46\]
S. I. Khan and P. Maini, “Modeling heterogeneous traffic flow,”
_Transportation research record_, vol. 1678, no. 1, pp. 234–241, 1999.

- \[47\]
V. T. Arasan and R. Z. Koshy, “Methodology for modeling highly heterogeneous
traffic flow,” _Journal of Transportation Engineering_, vol. 131,
no. 7, pp. 544–551, 2005.

- \[48\]
L. Ambarwati, A. J. Pel, R. Verhaeghe, and B. van Arem, “Empirical analysis of
heterogeneous traffic flow and calibration of porous flow model,”
_Transportation research part C: emerging technologies_, vol. 48, pp.
418–436, 2014.

- \[49\]
A. Emami, M. Sarvi, and S. Asadi Bagloee, “A review of the critical elements
and development of real-world connected vehicle testbeds around the world,”
_Transportation Letters_, pp. 1–26, 2020.

- \[50\]
American Center for Mobility, “Mobility research,” Online, accessed April
2021, https://www.acmwillowrun.org/.

- \[51\]
U. Briefs, “Mcity grand opening,” _Research Review_, vol. 46, no. 3,
2015.

- \[52\]
A. Cosgun, L. Ma, J. Chiu, J. Huang, M. Demir, A. M. Anon, T. Lian, H. Tafish,
and S. Al-Stouhi, “Towards full automated drive in urban environments: A
demonstration in gomentum station, california,” in _2017 IEEE_
_Intelligent Vehicles Symposium (IV)_. IEEE, 2017, pp. 1811–1818.

- \[53\]
F. Heery Sr _et al._, “The florida connected and automated vehicle
initiative: a focus on deployment,” _Institute of Transportation_
_Engineers. ITE Journal_, vol. 87, no. 10, pp. 33–41, 2017.

- \[54\]
G. Parikh and J. Hourdos, “Implementation of high accuracy radar detectors for
traffic safety countermeasure evaluation,” 2014.

- \[55\]
Ray C. Anderson Foundation, “Welcome to The Ray,” Online, accessed April
2021, https://theray.org/technology/.

- \[56\]
J. Farrell, M. J. Barth _et al._, “Precision mapping of the California
Connected Vehicle Testbed corridor,” California. Dept. of Transportation,
Tech. Rep., 2015.

- \[57\]
University of Michigan Engineering, “About Ann Arbor Connected Vehicle Test
Environment (AACVTE),” Online, accessed April 2021,
https://aacvte.engin.umich.edu.

- \[58\]
A. Krämmer, C. Schöller, D. Gulati, and A. Knoll, “Providentia-a large
scale sensing system for the assistance of autonomous vehicles,” in
_Robotics: Science and Systems (RSS), Workshop on Scene and Situation_
_Understanding for Autonomous Driving_, 2019.

- \[59\]
FHWA, “West central alabama action,” 2022,
https://ops.fhwa.dot.gov/fastact/atcmtd/2017/applications/univalabama/project.htm.

- \[60\]
A. von Schmidt, M. López Díaz, and A. Schengen, “Creating a baseline
scenario for simulating travel demand: A case study for preparing the region
test bed lower saxony, germany,” in _International Conference on_
_Advances in System Simulation (SIMUL)_. ThinkMind, 2021, pp. 51–57.

- \[61\]
A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet classification with
deep convolutional neural networks,” _Advances in neural information_
_processing systems_, vol. 25, pp. 1097–1105, 2012.

- \[62\]
K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image
recognition,” in _Proceedings of the IEEE conference on computer vision_
_and pattern recognition_, 2016, pp. 770–778.

- \[63\]
J. Redmon, S. Divvala, R. Girshick, and A. Farhadi, “You only look once:
Unified, real-time object detection,” in _Proceedings of the IEEE_
_conference on computer vision and pattern recognition_, 2016, pp. 779–788.

- \[64\]
R. Girshick, “Fast r-cnn,” in _Proceedings of the IEEE international_
_conference on computer vision_, 2015, pp. 1440–1448.

- \[65\]
K. Duan, S. Bai, L. Xie, H. Qi, Q. Huang, and Q. Tian, “Centernet: Keypoint
triplets for object detection,” in _Proceedings of the IEEE/CVF_
_International Conference on Computer Vision_, 2019, pp. 6569–6578.

- \[66\]
J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei, “Imagenet: A
large-scale hierarchical image database,” in _2009 IEEE conference on_
_computer vision and pattern recognition_. Ieee, 2009, pp. 248–255.

- \[67\]
T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan,
P. Dollár, and C. L. Zitnick, “Microsoft coco: Common objects in
context,” in _European conference on computer vision_. Springer, 2014, pp. 740–755.

- \[68\]
M. Dubská, A. Herout, and J. Sochor, “Automatic camera calibration for
traffic understanding.” in _BMVC_, vol. 4, 2014, p. 8.

- \[69\]
M. Dubská, A. Herout, R. Juránek, and J. Sochor, “Fully automatic
roadside camera calibration for traffic surveillance,” _IEEE_
_Transactions on Intelligent Transportation Systems_, vol. 16, pp. 1162–1171,
2014.

- \[70\]
J. Sochor, J. Špaňhel, and A. Herout, “Boxcars: Improving
fine-grained recognition of vehicles using 3-d bounding boxes in traffic
surveillance,” _IEEE transactions on intelligent transportation_
_systems_, vol. 20, no. 1, pp. 97–108, 2018.

- \[71\]
X. Ren, D. Wang, M. Laskey, and K. Goldberg, “Learning traffic behaviors by
extracting vehicle trajectories from online video streams,” in _2018_
_IEEE 14th International Conference on Automation Science and Engineering_
_(CASE)_. IEEE, 2018, pp. 1276–1283.

- \[72\]
S. Subedi and H. Tang, “Development of a multiple-camera 3d vehicle tracking
system for traffic data collection at intersections,” _IET Intelligent_
_Transport Systems_, vol. 13, no. 4, pp. 614–621, 2019.

- \[73\]
Z. Tang, G. Wang, H. Xiao, A. Zheng, and J.-N. Hwang, “Single-camera and
inter-camera vehicle tracking and 3d speed estimation based on fusion of
visual and semantic features,” in _Proceedings of the IEEE conference_
_on computer vision and pattern recognition workshops_, 2018, pp. 108–115.

- \[74\]
Y. Chen, L. Jing, E. Vahdani, L. Zhang, M. He, and Y. Tian, “Multi-camera
vehicle tracking and re-identification on ai city challenge 2019.” in
_CVPR Workshops_, vol. 2, 2019, pp. 324–332.

- \[75\]
D. Zhao and X. Li, “Real-world trajectory extraction from aerial videos-a
comprehensive and effective solution,” in _2019 IEEE Intelligent_
_Transportation Systems Conference (ITSC)_. IEEE, 2019, pp. 2854–2859.

- \[76\]
K. He, G. Gkioxari, P. Dollár, and R. Girshick, “Mask r-cnn,” in
_Proceedings of the IEEE international conference on computer vision_,
2017, pp. 2961–2969.

- \[77\]
T. Zhang and P. J. Jin, “A longitudinal scanline based vehicle trajectory
reconstruction method for high-angle traffic video,” _Transportation_
_research part C: emerging technologies_, vol. 103, pp. 104–128, 2019.

- \[78\]
Y. Malinovskiy, Y.-J. Wu, and Y. Wang, “Video-based vehicle detection and
tracking using spatiotemporal maps,” _Transportation research record_,
vol. 2121, no. 1, pp. 81–89, 2009.

- \[79\]
R. James, “Third generation simulation: A closer look at the impact of
automated driving systems on traffic,” 2023. \[Online\]. Available:
https://highways.dot.gov/research/projects/third-generation-simulation-closer-look-impact-automated-driving-systems-traffic
- \[80\]
J. Bock, R. Krajewski, T. Moers, S. Runde, L. Vater, and L. Eckstein, “The ind
dataset: A drone dataset of naturalistic road user trajectories at german
intersections,” in _2020 IEEE Intelligent Vehicles Symposium (IV)_,
2020, pp. 1929–1934.

- \[81\]
R. Krajewski, T. Moers, J. Bock, L. Vater, and L. Eckstein, “The round
dataset: A drone dataset of road user trajectories at roundabouts in
germany,” in _2020 IEEE 23rd International Conference on Intelligent_
_Transportation Systems (ITSC)_, 2020, pp. 1–6.

- \[82\]
A. Breuer, J.-A. Termöhlen, S. Homoceanu, and T. Fingscheidt, “opendd: A
large-scale roundabout drone dataset,” in _2020 IEEE 23rd International_
_Conference on Intelligent Transportation Systems (ITSC)_. IEEE, 2020, pp. 1–6.

- \[83\]
W. Zhan, L. Sun, D. Wang, H. Shi, A. Clausse, M. Naumann, J. Kummerle,
H. Konigshof, C. Stiller, A. de La Fortelle _et al._, “Interaction
dataset: An international, adversarial and cooperative motion dataset in
interactive driving scenarios with semantic maps,” _arXiv preprint_
_arXiv:1910.03088_, 2019.

- \[84\]
O. Zheng, M. Abdel-Aty, L. Yue, A. Abdelraouf, Z. Wang, and N. Mahmoud,
“Citysim: A drone-based vehicle trajectory dataset for safety oriented
research and digital twins,” _arXiv preprint arXiv:2208.11036_, 2022.

- \[85\]
W. Barbour, D. Gloudemans, M. Cebelak, P. Freeze, and D. Work, “Interstate 24
motion open road testbed,” in _Proceedings of the ITS America Annual_
_Meeting, to appear_, location, 12 2021.

- \[86\]
Tennessee Department of Transportation, “Annual Average Daily Traffic
(AADT) Maps,” Online, accessed December 2022,
https://tdot.ms2soft.com/tcds.

- \[87\]
D. Chen and S. Ahn, “Variable speed limit control for severe non-recurrent
freeway bottlenecks,” _Transportation Research Part C: Emerging_
_Technologies_, vol. 51, pp. 210–230, 2015.

- \[88\]
M. Papageorgiou, C. Diakaki, V. Dinopoulou, A. Kotsialos, and Y. Wang, “Review
of road traffic control strategies,” _Proceedings of the IEEE_,
vol. 91, no. 12, pp. 2043–2067, 2003.

- \[89\]
D. Gloudemans, W. Barbour, N. Gloudemans, M. Neuendorf, B. Freeze, S. ElSaid,
and D. B. Work, “Interstate-24 motion: Closing the loop on smart mobility,”
in _2020 IEEE Workshop on Design Automation for CPS and IoT_
_(DESTION)_. IEEE, 2020, pp. 49–55.

- \[90\]
D. Gloudemans and D. B. Work, “Vehicle tracking with crop-based detection,”
in _2021 20th IEEE International Conference on Machine Learning and_
_Applications (ICMLA)_. IEEE, 2021, pp.
312–319.

- \[91\]
T.-Y. Lin, P. Goyal, R. Girshick, K. He, and P. Dollar, “Focal loss for dense
object detection,” in _The IEEE International Conference on Computer_
_Vision (ICCV)_, Oct 2017.

- \[92\]
E. Bochinski, V. Eiselein, and T. Sikora, “High-speed tracking-by-detection
without using image information,” in _2017 14th IEEE International_
_Conference on Advanced Video and Signal Based Surveillance (AVSS)_. IEEE, 2017, pp. 1–6.

- \[93\]
E. Strigel, D. Meissner, and K. Dietmayer, “Vehicle detection and tracking at
intersections by fusing multiple camera views,” in _2013 IEEE_
_Intelligent Vehicles Symposium (IV)_. IEEE, 2013, pp. 882–887.

- \[94\]
E. Luna, J. C. SanMiguel, J. M. Martínez, and M. Escudero-Viñolo,
“Online clustering-based multi-camera vehicle tracking in scenarios with
overlapping fovs,” _Multimedia Tools and Applications_, pp. 1–21,
2022.

- \[95\]
M. Wu, G. Zhang, N. Bi, L. Xie, Y. Hu, and Z. Shi, “Multiview vehicle tracking
by graph matching model.” in _CVPR Workshops_, 2019, pp. 29–36.

- \[96\]
K. Bernardin and R. Stiefelhagen, “Evaluating multiple object tracking
performance: the clear mot metrics,” _EURASIP Journal on Image and_
_Video Processing_, vol. 2008, pp. 1–10, 2008.

- \[97\]
B. Coifman and L. Li, “A critical evaluation of the next generation simulation
(ngsim) vehicle trajectory dataset,” _Transportation Research Part B:_
_Methodological_, vol. 105, pp. 362–377, 2017.

- \[98\]
Y. Wang, D. Gloudemans, Z. N. Teoh, L. Liu, G. Zachár, W. Barbour, and
D. Work, “Automatic vehicle trajectory data reconstruction at scale,” 2022.
\[Online\]. Available: https://arxiv.org/abs/2212.07907
- \[99\]
J. Berclaz, F. Fleuret, and P. Fua, “Multiple object tracking using flow
linear programming,” in _2009 Twelfth IEEE international workshop on_
_performance evaluation of tracking and surveillance_. IEEE, 2009, pp. 1–8.

- \[100\]
D. Gloudemans, Y. Wang, J. Ji, G. Zachar, W. Barbour, and D. B. Work, “I-24
motion trajectory dataset: Review release,” 2023. \[Online\]. Available:
https://i24motion.org/data
- \[101\]
R. E. Stern, S. Cui, M. L. Delle Monache, R. Bhadani, M. Bunting, M. Churchill,
N. Hamilton, H. Pohlmann, F. Wu, B. Piccoli _et al._, “Dissipation of
stop-and-go waves via control of autonomous vehicles: Field experiments,”
_Transportation Research Part C: Emerging Technologies_, vol. 89, pp.
205–221, 2018.

- \[102\]
L. C. Edie _et al._, _Discussion of traffic stream measurements and_
_definitions_. Port of New York
Authority New York, 1963.

- \[103\]
I. Daubechies, _Ten lectures on wavelets_. SIAM, 1992.

- \[104\]
B. A. Zielke, R. L. Bertini, and M. Treiber, “Empirical measurement of freeway
oscillation characteristics,” _Transportation Research Record: Journal_
_of the Transportation Research Board_, vol. 2088, pp. 57–67, 1 2008.
\[Online\]. Available: http://journals.sagepub.com/doi/10.3141/2088-07
- \[105\]
M. Treiber, A. Kesting, and D. Helbing, “Three-phase traffic theory and
two-phase models with a fundamental diagram in the light of empirical
stylized facts,” _Transportation Research Part B: Methodological_,
vol. 44, no. 8-9, pp. 983–1000, 2010.

- \[106\]
D. Helbing, M. Treiber, A. Kesting, and M. Schönhof, “Theoretical vs.
empirical classification and prediction of congested traffic states,”
_European Physics Journal B_, 3 2009. \[Online\]. Available:
http://arxiv.org/abs/0903.0929http://dx.doi.org/10.1140/epjb/e2009-00140-5
- \[107\]
N. H. Gartner, C. J. Messer, and A. Rathi, “Traffic flow theory-a
state-of-the-art report: revised monograph on traffic flow theory,”
_Transportation Research International Documentation_, 2002.

- \[108\]
R. Hartley and A. Zisserman, _Multiple view geometry in computer_
_vision_. Cambridge university press,
2003.

- \[109\]
G. Bradski, “The opencv library.” _Dr. Dobb’s Journal: Software Tools_
_for the Professional Programmer_, vol. 25, no. 11, pp. 120–123, 2000.

- \[110\]
B. A. Coifman and Y. Wang, “Average velocity of waves propagating through
congested freeway traffic,” in _Transportation and Traffic Theory._
_Flow, Dynamics and Human Interaction. 16th International Symposium on_
_Transportation and Traffic TheoryUniversity of Maryland, College Park_, 2005.