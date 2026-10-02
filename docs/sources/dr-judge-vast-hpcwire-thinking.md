## Off the Wire Press Releases

![](https://www.hpcwire.com/wp-content/uploads/2026/02/Hallak_Vast_FWD-1024x577.jpg)

## VAST Data Expands AI Data Stack, Keeps Eye on North Star

[Data Management](https://www.hpcwire.com/topic/data-management/)

by

[Alex Woodie](https://www.hpcwire.com/author/alex/)

\| February 25, 2026

Shares

[Share this on Facebook](https://www.facebook.com/share.php?u=https%3A%2F%2Fwww.hpcwire.com%2F2026%2F02%2F25%2Fvast-data-expands-ai-data-stack-keeps-eye-on-north-star%2F "Share this on Facebook")[Tweet this !](https://twitter.com/intent/tweet?text=VAST%20Data%20Expands%20AI%20Data%20Stack%2C%20Keeps%20Eye%20on%20North%20Star%20-%20https%3A%2F%2Fwww.hpcwire.com%2F2026%2F02%2F25%2Fvast-data-expands-ai-data-stack-keeps-eye-on-north-star%2F%20 "Tweet this !")[Add this to LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.hpcwire.com%2F2026%2F02%2F25%2Fvast-data-expands-ai-data-stack-keeps-eye-on-north-star%2F "Add this to LinkedIn")[Submit this to Reddit](https://reddit.com/submit?url=https%3A%2F%2Fwww.hpcwire.com%2F2026%2F02%2F25%2Fvast-data-expands-ai-data-stack-keeps-eye-on-north-star%2F&title=VAST%20Data%20Expands%20AI%20Data%20Stack%2C%20Keeps%20Eye%20on%20North%20Star "Submit this to Reddit")[Share this on HackerNews](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fwww.hpcwire.com%2F2026%2F02%2F25%2Fvast-data-expands-ai-data-stack-keeps-eye-on-north-star%2F&t=VAST%20Data%20Expands%20AI%20Data%20Stack%2C%20Keeps%20Eye%20on%20North%20Star "Share this on HackerNews")[Email this ](mailto:?subject=VAST%20Data%20Expands%20AI%20Data%20Stack%2C%20Keeps%20Eye%20on%20North%20Star&body=Ten%20years%20ago%2C%20VAST%20Data%20founders%20pondered%20what%20it%20would%20take%20to%20build%20a%20thinking%20machine%2C%20a%20compute%20-%20https%3A%2F%2Fwww.hpcwire.com%2F2026%2F02%2F25%2Fvast-data-expands-ai-data-stack-keeps-eye-on-north-star%2F "Email this ")[More share links](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "More share links")

* * *

Ten years ago, VAST Data founders pondered what it would take to build a thinking machine, a computer that would continuously learn from new data. While it hasn’t delivered that thinking machine yet, the company took a few more steps toward that goal this week at the inaugural VAST Forward conference in Salt Lake City, Utah.

VAST Data has come a long way since co-founders Renen Hallak, Shachar Fienblit, and Jeff Denworth started the journey to build a thinking machine back in 2016. They started by building a new data storage platform that could capitalize on recent developments, including the widespread availability of solid state drives and the introduction of NVMe over Fabric, and serve data for new exabyte-level HPC, AI, and big data workloads.

![](https://www.hpcwire.com/wp-content/uploads/2026/02/VAST_PolicyEngine-300x135.png)

_VAST PolicyEngine bolsters data security_

The cornerstone of the new system was an architecture dubbed Disaggregated and Shared Everything (DASE). The first element built atop DASE was DataStore, which is a unified object and file storage system. That was followed up with a storage system for tabular data (DataBase), a system for executing functions on the data (DataEngine), and a global namespace that united data silos (DataSpace).

Buoyed by early success, the company kept adding to the stack. In October 2024, VAST introduced [the InsightEngine](https://www.hpcwire.com/bigdatawire/bigdatawire/2024/10/03/vast-looks-inward-outward-for-an-ai-edge/) to trigger actions on the platform. It added support for Apache Kafka in early 2025, followed by a vector database, support for serverless triggers, and fine-grained access control. In May 2025, it launched what it calls an operating system for AI, with the AgentEngine as the key component. It followed that up in August with SyncEngine to function as a universal data router.

Today at VAST Forward in Salt Lake City, Utah, the company unveiled the next two engines: PolicyEngine and TuningEngine.

PolicyEngine is designed to give fine-grained control over the army of AI agents that are emerging in customer environments. VAST users can set policies governing what data agents are allowed to access and how they can communicate with other agents, tools, and remote data products. The software uses an explicit permission structure to grant or deny access in real time, and can also act upon AI-derived context.

![](https://www.hpcwire.com/wp-content/uploads/2026/02/ThinkingMachine-300x169.jpg)

_VAST has not wavered from its goal to build a thinking machine_

The goal of PolicyEngine is to reduce the chances of data spillage and make agentic AI trustworthy, Denworth said during a press briefing last week

“First, it’s a decisioning framework. But the second thing that it will do, it will determine the types of data and the ways in which data can be presented out to agents,” he said. “There will be interpretation and there will be transformations of data in certain cases where there needs to be some sort of redaction or some sort of transformation of data in order to make it safe for an endpoint to see.”

The VAST Data TuningEngine, meanwhile, complements the AgentEngine runtime to complete the “learning loop” needed to continuously improve AI models in customer environments. TuningEngine collects data that comes out of AgentEngine to create artifact tables that are then fed into a series of tuners, which could be based on LoRA fine tuning, supervised fine tuning, and reinforcement learning methods. TuningEngine uses the results of those fine-tuning runs to create (hopefully) a better AI model, which is then automatically redeployed into the customer environment.

While it’s ostensibly built for fine-tuning, there’s also a security aspect to TuningAgent, Denworth said.

“Our conclusion was if we don’t handle fine tuning, then that’s going to be a security gap that ultimately makes AI less trustable,” he said. “And it just happens to be this is the point in time in terms of our product development, where it becomes the right time to infuse model evolution into the platform to kind of get close, or as close as possible, to that thinking machine vision that we started with 10 years ago.”

![](https://www.hpcwire.com/wp-content/uploads/2026/02/10yrs_Vast_Hallak-300x169.jpg)

_Hallack delivers a keynote at VAST Forward 2026_

VAST is also delivering a new capability called Polaris that will simplify the management of VAST customer environments. Polaris is a global control plane designed to provision, operate, and orchestrate VAST clusters. It will start with support for major public cloud platforms, and will be expanded to support on-prem systems later.

VAST is making a slew of other announcements at its conference, which is expected to host 1,200 attendees jn Salt Lake City this week.

VAST has not wavered from that initial goal to build a thinking machine. DASE, the AI OS, and all of the many engines are stops on that journey, Hallak said during a press briefing at VAST Forward.

“It took us 10 years. It was a long journey. But over those 10 years we basically built…a lot of the parts that we think are needed to fill out this software infrastructure layer of the AI stack,” Hallak said. “We obviously started from storage and database and then DataEngine. Over the last few years, we’ve been adding more engines into it, to enable agents and to enable RAG and to add observability and security and all of these things that we think that we need for this AI operating system.”

Where will the company go next? It seems likely there will be more engines. But Hallak said that the company has not taken its eyes off the big prize.

“We always have our North Star, and that has been from day one, enabling these very, very large scale AI systems,” Hallak said in the press briefing. “Even before generative AI, it was hedge funds and it was life science institutes. That was our North Star, and it still is. We’re trying to build a thinking machine. We think if we can build a thinking machine, then it solves all the other problems for us.”

Topics:
[Data Management](https://www.hpcwire.com/topic/data-management/)

Tags:
[AI OS](https://www.hpcwire.com/tag/ai-os/), [data platform](https://www.hpcwire.com/tag/data-platform/), [Jeff Denworth](https://www.hpcwire.com/tag/jeff-denworth/), [Renen Hallak](https://www.hpcwire.com/tag/renen-hallak/), [thinking engine](https://www.hpcwire.com/tag/thinking-engine/), [VAST Forward](https://www.hpcwire.com/tag/vast-forward/)

- Related Articles

- Most Popular

- Most Recent


[![](https://www.hpcwire.com/wp-content/uploads/2026/08/Science_supercomputer_Shutterstock_vectorfusionart-150x79.jpg)](https://www.hpcwire.com/2026/08/13/new-gpu-method-compresses-science-data-at-60-gb-s/)

### [New GPU Method Compresses Scientific Simulation Data at 60 GB/s](https://www.hpcwire.com/2026/08/13/new-gpu-method-compresses-science-data-at-60-gb-s/)

Scientists running large simulations can end up with terabytes of data that then has to...

[![](https://www.hpcwire.com/wp-content/uploads/2026/06/server_shutterstock_panumas-nikhomkhai-150x100.jpg)](https://www.hpcwire.com/2026/06/24/hpe-gives-cray-customers-new-development-multi-tenancy-options/)

### [HPE Gives Cray Customers New Development, Multi-Tenancy Options](https://www.hpcwire.com/2026/06/24/hpe-gives-cray-customers-new-development-multi-tenancy-options/)

HPE rolled out several new products at ISC 2026 this week, including support for multi-tenancy...

[![](https://www.hpcwire.com/wp-content/uploads/2026/06/Charlie_Giancarlo_Accelerate2026-150x84.jpg)](https://www.hpcwire.com/2026/06/17/everpure-outlines-ambitious-pivot-to-data-centric-storage-at-accelerate-2026/)

### [Everpure Outlines Ambitious Pivot to Data-Centric Storage at Accelerate 2026](https://www.hpcwire.com/2026/06/17/everpure-outlines-ambitious-pivot-to-data-centric-storage-at-accelerate-2026/)

Everpure (formerly Pure Storage) may have changed its name a few months back, but the...

[![Hammerspace](https://www.hpcwire.com/wp-content/uploads/2026/06/HPC-Wire-Advertorial-v4-2-150x84.jpg)](https://www.hpcwire.com/2026/06/09/modernizing-hpc-infrastructure-in-an-ssd-constrained-era/)

### [Modernizing HPC Infrastructure in an SSD-Constrained Era](https://www.hpcwire.com/2026/06/09/modernizing-hpc-infrastructure-in-an-ssd-constrained-era/)

Three Practical Strategies for Scaling AI and HPC Infrastructure Despite Flash Constraints The rapid emergence...

[![](https://www.hpcwire.com/wp-content/uploads/2021/04/chemistry-molecules_shutterstock-1686700336_700x-150x92.jpg)](https://www.hpcwire.com/2026/06/05/foundation-models-offer-a-new-way-to-explore-chemical-space/)

### [Foundation Models Offer a New Way to Explore Chemical Space](https://www.hpcwire.com/2026/06/05/foundation-models-offer-a-new-way-to-explore-chemical-space/)

Chemists have a scale problem. It is estimated that chemical space contains as many as...

[![](https://www.hpcwire.com/wp-content/uploads/2026/06/HPC-Wire-Advertorial-v4-1-150x84.jpg)](https://www.hpcwire.com/2026/06/03/sovereign-ai-must-be-built-on-sovereign-data-infrastructure/)

### [Sovereign AI Must be Built on Sovereign Data Infrastructure](https://www.hpcwire.com/2026/06/03/sovereign-ai-must-be-built-on-sovereign-data-infrastructure/)

Across Europe and around the world, governments and research institutions are racing to build sovereign...

[![](https://www.hpcwire.com/wp-content/uploads/2026/07/Blackwell_Question_Mark-150x88.png)](https://www.hpcwire.com/2026/07/07/are-gpus-still-needed-maybe-not-hpc-experts-say/)

### [Are GPUs Still Needed? Maybe Not, HPC Experts Say](https://www.hpcwire.com/2026/07/07/are-gpus-still-needed-maybe-not-hpc-experts-say/)

The rise of an GPU-less supercomputer called LineShine on the TOP500 list last week has...

[![](https://www.hpcwire.com/wp-content/uploads/2026/07/code_shutterstock_Banana-Images-150x100.jpg)](https://www.hpcwire.com/2026/07/09/spectral-compute-aims-to-set-cuda-free-will-it-succeed/)

### [Spectral Compute Aims to Set CUDA Free. Will It Succeed?](https://www.hpcwire.com/2026/07/09/spectral-compute-aims-to-set-cuda-free-will-it-succeed/)

Nvidia is primarily known as a hardware company thanks to the wild success of its...

[![](https://www.hpcwire.com/wp-content/uploads/2026/08/AMD-MI430x-150x81.png)](https://www.hpcwire.com/2026/08/03/amds-fp64-boost-with-mi430x-is-even-bigger-than-expected/)

### [AMD’s FP64 Boost with MI430X Is Even Bigger Than Expected](https://www.hpcwire.com/2026/08/03/amds-fp64-boost-with-mi430x-is-even-bigger-than-expected/)

Computer scientists who can’t get enough FP64 performance for their modeling and simulation workloads, and...

[![](https://www.hpcwire.com/wp-content/uploads/2026/07/AMD_Instinct_Lisa-Su_3-150x89.png)](https://www.hpcwire.com/2026/07/24/amd-takes-on-nvidia-with-mi455-gpus-and-helios-racks/)

### [AMD Takes On Nvidia with MI455X GPUs and Helios Racks](https://www.hpcwire.com/2026/07/24/amd-takes-on-nvidia-with-mi455-gpus-and-helios-racks/)

During its Advancing AI 2026 launch event in San Francisco yesterday, AMD formally unveiled its...

[![](https://www.hpcwire.com/wp-content/uploads/2026/01/Genesis_mission_Shutterstock_Jack_the_Sparrow-150x100.png)](https://www.hpcwire.com/2026/07/22/doe-unveils-awards-for-nearly-300-genesis-mission-projects/)

### [DOE Unveils Awards for Nearly 300 Genesis Mission Projects](https://www.hpcwire.com/2026/07/22/doe-unveils-awards-for-nearly-300-genesis-mission-projects/)

The Department of Energy today announced plans to fund 278 projects as part of Genesis...

[![](https://www.hpcwire.com/wp-content/uploads/2026/03/QubitsComparison-Cropped_WEB_nH1yb4c.max-1400x800-1-150x84.jpg)](https://www.hpcwire.com/2026/07/21/oratomics-300m-bet-on-low-qubit-quantum-computing/)

### [Oratomic’s $300M Bet on Low-Qubit Quantum Computing](https://www.hpcwire.com/2026/07/21/oratomics-300m-bet-on-low-qubit-quantum-computing/)

Oratomic, a quantum computing startup that emerged from stealth just four months ago, has raised...

[![](https://www.hpcwire.com/wp-content/uploads/2026/10/data_center_shutterstock_Pete-Hansen-150x84.jpg)](https://www.hpcwire.com/2026/10/01/netapp-eliminates-metadata-bottleneck-for-zettascale-storage-with-new-novus-architecture/)

### [NetApp Eliminates Metadata Bottleneck for Zettascale Storage with New Novus Architecture](https://www.hpcwire.com/2026/10/01/netapp-eliminates-metadata-bottleneck-for-zettascale-storage-with-new-novus-architecture/)

NetApp this week rolled out Novus, a new class of storage architecture that it says...

[![](https://www.hpcwire.com/wp-content/uploads/2026/10/storage_data_center_Shutterstock_harhar38-150x87.jpg)](https://www.hpcwire.com/2026/10/01/vdura-v12-brings-the-hyperscaler-storage-playbook-to-ai-factories/)

### [VDURA V12 Brings the Hyperscaler Storage Playbook to AI Factories](https://www.hpcwire.com/2026/10/01/vdura-v12-brings-the-hyperscaler-storage-playbook-to-ai-factories/)

Neoclouds are spending a fortune on GPUs, and they need to keep those GPUs doing...

[![](https://www.hpcwire.com/wp-content/uploads/2025/09/people_metamorworks-150x100.png)](https://www.hpcwire.com/2026/09/30/hpc-career-notes-september-2026/)

### [HPC Career Notes September 2026](https://www.hpcwire.com/2026/09/30/hpc-career-notes-september-2026/)

Once again, it is time for HPC Career Notes, our monthly feature that’s designed to...

[![](https://www.hpcwire.com/wp-content/uploads/2026/09/storage_shutterstock-150x100.png)](https://www.hpcwire.com/2026/09/30/everpure-enhances-data-intelligence-to-bolster-customer-ai-projects/)

### [Everpure Enhances Data Intelligence to Bolster Customer AI Projects](https://www.hpcwire.com/2026/09/30/everpure-enhances-data-intelligence-to-bolster-customer-ai-projects/)

Everpure today rolled out several new data management capabilities designed to help customers improve their...

[![](https://www.hpcwire.com/wp-content/uploads/2026/09/Su-and-Li-150x84.png)](https://www.hpcwire.com/2026/09/29/amd-lands-fei-fei-li-the-godmother-of-ai-in-8-2b-world-labs-buy/)

### [AMD Lands Fei-Fei Li, the ‘Godmother of AI,’ In $8.2B World Labs Buy](https://www.hpcwire.com/2026/09/29/amd-lands-fei-fei-li-the-godmother-of-ai-in-8-2b-world-labs-buy/)

Nvidia may be buying Hugging Face, but AMD will soon have an AI software company...

[![](https://www.hpcwire.com/wp-content/uploads/2026/09/science_hand_shutterstock_everything-possible-150x83.jpg)](https://www.hpcwire.com/2026/09/29/hardware-alone-wont-drive-the-next-revolution-in-scientific-computing/)

### [Hardware Alone Won’t Drive the Next Revolution in Scientific Computing](https://www.hpcwire.com/2026/09/29/hardware-alone-wont-drive-the-next-revolution-in-scientific-computing/)

The future of scientific discovery will depend on trusted software ecosystems and the communities that...

HPCwire Preferences

Could you brief your team on what happened in HPC last week?

Catch our weekly breaking updates and always be the most informed person in the room.

#### Weekly Updates

HPCwire

BigDATAwire

AIwire

#### Biweekly Updates

HPC AI // Sync

#### Monthly Updates

QCwire (Quantum Computing)

Technology Leaders Showcase

Technology Conferences & Events

TCI Media Tech Jobs

#### Special Updates

Trillion Parameter Consortium's TPC26

HPC + AI Wall Street Events

<%\-\- the gray background --%>


YesNo

## MEET OUR EDITORS

[![](https://www.hpcwire.com/wp-content/uploads/2025/02/AlexWoodie.jpg)](https://www.hpcwire.com/author/alex/)

[Alex Woodie](https://www.hpcwire.com/author/alex/) Editorial Director +

HPCwire Managing Editor

[![](https://www.hpcwire.com/wp-content/uploads/2025/03/Jaime-Hampton-2023-600px-e1689613855942.png)](https://www.hpcwire.com/author/jaime/)

[Jaime Hampton](https://www.hpcwire.com/author/jaime/) AIwire Managing Editor

[![](https://www.hpcwire.com/wp-content/uploads/2025/02/Ali-headshot.jpg)](https://www.hpcwire.com/author/alitaborcommunications-com/)

[Ali Azhar](https://www.hpcwire.com/author/alitaborcommunications-com/) BigDATAwire Managing Editor

[![](https://www.hpcwire.com/wp-content/uploads/2025/02/Drew-Jolly-2023-600px-e1689613948667.webp)](https://www.hpcwire.com/author/drew/)

[Drew Jolly](https://www.hpcwire.com/author/drew/) QCwire Managing Editor

[![](https://www.hpcwire.com/wp-content/uploads/2025/03/Doug-Head-Full-2023-scaled-e1689613775505-300x300-1.jpg)](https://www.hpcwire.com/author/doug-eadline/)

[Douglas Eadline](https://www.hpcwire.com/author/doug-eadline/) Contributing Editor

[![](https://www.hpcwire.com/wp-content/uploads/2020/04/asnell-150x150.jpg)](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/#)

[Addison Snell](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/#) Contributing Editor

[![Elizabeth Headshot](https://www.hpcwire.com/wp-content/uploads/2025/10/ElizabethLeake.png)](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/#)

[Elizabeth Leake](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/#) Contributing Editor

[Meet the\\
team](https://www.hpcwire.com/about-hpcwire/)

## Off the Wire

### October 1, 2026

- [UC San Diego and University of Vermont Share $19M from NSF to Build National Biological Observatory](https://www.hpcwire.com/off-the-wire/uc-san-diego-and-university-of-vermont-share-19m-from-nsf-to-build-national-biological-observatory/)
- [TPC Fall 2026 Hackathon at LRZ Brings Together AI for Science Community](https://www.hpcwire.com/off-the-wire/tpc-fall-2026-hackathon-at-lrz-brings-together-ai-for-science-community/)
- [Volantis Raises $88M Series A to Advance Photonic Memory Architecture](https://www.hpcwire.com/off-the-wire/volantis-raises-88m-series-a-to-advance-photonic-memory-architecture/)
- [OpenStack Hibiscus Strengthens Trusted Infrastructure for the AI Era](https://www.hpcwire.com/off-the-wire/openstack-hibiscus-strengthens-trusted-infrastructure-for-the-ai-era/)
- [SDSC Helps Improve AI-Ready Geospatial Data Through GeoCroissant](https://www.hpcwire.com/off-the-wire/sdsc-helps-improve-ai-ready-geospatial-data-through-geocroissant/)
- [Alice & Bob Demonstrates New Approach to Stabilizing Cat Qubits with DC Voltage Bias](https://www.hpcwire.com/off-the-wire/alice-bob-demonstrates-new-approach-to-stabilizing-cat-qubits-with-dc-voltage-bias/)
- [High Performance Software Foundation Welcomes ClusterShell as a New Project](https://www.hpcwire.com/off-the-wire/high-performance-software-foundation-welcomes-clustershell-as-a-new-project/)
- [D-Wave Launches Gate-Model Simulator Beta Program, Advancing Error-Aware Programming Capabilities](https://www.hpcwire.com/off-the-wire/d-wave-launches-gate-model-simulator-beta-program-advancing-error-aware-programming-capabilities/)
- [Q/C Technologies Collaborates with Sandia on Optical Computing for AI Inference](https://www.hpcwire.com/off-the-wire/q-c-technologies-collaborates-with-sandia-on-optical-computing-for-ai-inference/)
- [Signaloid Joins CERN openlab’s Heterogeneous Architectures Testbed](https://www.hpcwire.com/off-the-wire/signaloid-joins-cern-openlabs-heterogeneous-architectures-testbed/)

[View All Off the Wire](https://www.hpcwire.com/off-the-wire/)

- ### Off The Wire

- ##### Quantum Computing Headlines


#### October 1, 2026

- [Alice & Bob Demonstrates New Approach to Stabilizing Cat Qubits with DC Voltage Bias](https://www.hpcwire.com/off-the-wire/alice-bob-demonstrates-new-approach-to-stabilizing-cat-qubits-with-dc-voltage-bias/ "Alice & Bob Demonstrates New Approach to Stabilizing Cat Qubits with DC Voltage Bias")
- [D-Wave Launches Gate-Model Simulator Beta Program, Advancing Error-Aware Programming Capabilities](https://www.hpcwire.com/off-the-wire/d-wave-launches-gate-model-simulator-beta-program-advancing-error-aware-programming-capabilities/ "D-Wave Launches Gate-Model Simulator Beta Program, Advancing Error-Aware Programming Capabilities")
- [Quantum Computing Inc. Announces Dirac-3S, Scaling to Nearly 10,000 Variables](https://www.hpcwire.com/off-the-wire/quantum-computing-inc-announces-dirac-3s-scaling-to-nearly-10000-variables/ "Quantum Computing Inc. Announces Dirac-3S, Scaling to Nearly 10,000 Variables")

#### September 30, 2026

- [OLCF Study Advances Quantum Fluid Dynamics with Help from Frontier](https://www.hpcwire.com/off-the-wire/olcf-study-advances-quantum-fluid-dynamics-with-help-from-frontier/ "OLCF Study Advances Quantum Fluid Dynamics with Help from Frontier")
- [Classiq Unveils Engine to Plan Fault-Tolerant Quantum Workloads](https://www.hpcwire.com/off-the-wire/classiq-unveils-engine-to-plan-fault-tolerant-quantum-workloads/ "Classiq Unveils Engine to Plan Fault-Tolerant Quantum Workloads")

#### September 29, 2026

- [Roadrunner Quantum Lab Opens in Albuquerque with IonQ, Diraq and QuEra Among Initial Tenants](https://www.hpcwire.com/off-the-wire/roadrunner-quantum-lab-opens-in-albuquerque-with-ionq-diraq-and-quera-among-initial-tenants/ "Roadrunner Quantum Lab Opens in Albuquerque with IonQ, Diraq and QuEra Among Initial Tenants")
- [Occam Foundry Gains Austin Mayor’s Support and TACC Partnership for Quantum Campus](https://www.hpcwire.com/off-the-wire/occam-foundry-gains-austin-mayors-support-and-tacc-partnership-for-quantum-campus/ "Occam Foundry Gains Austin Mayor’s Support and TACC Partnership for Quantum Campus")
- [Cloudflare Announces Public Certificate Authority for the Post-Quantum Web](https://www.hpcwire.com/off-the-wire/cloudflare-announces-public-certificate-authority-for-the-post-quantum-web/ "Cloudflare Announces Public Certificate Authority for the Post-Quantum Web")
- [Xanadu and Bluefors Target Compact Cooling for Utility-Scale Quantum Computing](https://www.hpcwire.com/off-the-wire/xanadu-and-bluefors-target-compact-cooling-for-utility-scale-quantum-computing/ "Xanadu and Bluefors Target Compact Cooling for Utility-Scale Quantum Computing")
- [Infleqtion Signs MOU with Riverlane to Evaluate Real-Time Quantum Error Correction](https://www.hpcwire.com/off-the-wire/infleqtion-and-riverlane-sign-mou-to-advance-quantum-error-correction-and-fault-tolerant-computing-in-the-uk/ "Infleqtion Signs MOU with Riverlane to Evaluate Real-Time Quantum Error Correction")

[More Off The Wire](https://www.hpcwire.com/qcwire/off-the-wire/)

![Alex's Weekly Round](https://www.hpcwire.com/wp-content/uploads/2025/11/hpcwire-11.07.2025.jpg)

## HPCwire    Weekly Roundup

[VIEW ALL](https://www.hpcwire.com/hpcwire-weekly-roundup/)

## CLICK FOR BREAKING NEWS ON LEADING VENDORS

[![](https://www.hpcwire.com/wp-content/uploads/2024/06/VIRIDIEN_833-768x82.jpg)](https://www.hpcwire.com/vendor/viridien/ "Viridien")

[![AMD](https://www.hpcwire.com/wp-content/uploads/2025/10/amd_150x60.jpg)](https://www.hpcwire.com/vendor/amd "AMD")[![Aspen Systems](https://www.hpcwire.com/wp-content/uploads/2025/10/aspensystem_150x60.jpg)](https://b.link/3rgft861 "Aspen Systems")[![Dell](https://www.hpcwire.com/wp-content/uploads/2025/10/delltechnologies_150x60.jpg)](https://www.hpcwire.com/vendor/dell "Dell")[![Drivenets](https://www.hpcwire.com/wp-content/uploads/2025/10/drivenets_150x60.jpg)](https://www.hpcwire.com/vendor/drivenets/ "Drivenets")[![Google](https://www.hpcwire.com/wp-content/uploads/2025/10/googlecloud_150x60.jpg)](https://www.hpcwire.com/vendor/google "Google")[![Hammerspace](https://www.hpcwire.com/wp-content/uploads/2025/10/hammerspace_150x60.jpg)](https://www.hpcwire.com/vendor/hammerspace "Hammerspace")[![HPE](https://www.hpcwire.com/wp-content/uploads/2025/10/hpe_150x60.jpg)](https://www.hpcwire.com/vendor/HPE "HPE")[![intel](https://www.hpcwire.com/wp-content/uploads/2025/10/intel_150x60.jpg)](https://www.hpcwire.com/vendor/intel "Intel")[![Lenovo](https://www.hpcwire.com/wp-content/uploads/2025/10/lenovo_150x60.jpg)](https://www.hpcwire.com/vendor/lenovo "Lenovo")[![Microsoft](https://www.hpcwire.com/wp-content/uploads/2025/10/microsoft_150x60.jpg)](https://www.hpcwire.com/vendor/microsoft "Microsoft")[![MiTAC](https://www.hpcwire.com/wp-content/uploads/2026/03/MiTAC_150x60.png)](https://www.hpcwire.com/vendor/mitac "MiTAC")[![Motivair](https://www.hpcwire.com/wp-content/uploads/2025/12/Motivair_SE-150x60_2.png)](https://www.hpcwire.com/vendor/motivair "Motivair")[![NEC](https://www.hpcwire.com/wp-content/uploads/2025/10/nec_150x60.jpg)](https://www.hpcwire.com/vendor/nec "NEC")[![NVIDIA](https://www.hpcwire.com/wp-content/uploads/2025/10/nvidia_150x60.jpg)](https://www.hpcwire.com/vendor/nvidia "Nvidia")[![Parallel Works](https://www.hpcwire.com/wp-content/uploads/2025/10/parallelworks_150x60.jpg)](https://www.hpcwire.com/vendor/parallel-works/ "Parallel Works")[![Quantinuum](https://www.hpcwire.com/wp-content/uploads/2025/10/quantinuum_150x60.jpg)](https://www.hpcwire.com/vendor/quantinuum "Quantinuum")[![Quantum Montion](https://www.hpcwire.com/wp-content/uploads/2025/10/quantinuummotion_150x60.jpg)](https://www.hpcwire.com/vendor/quantum-motion "Quantum Montion")[![SambaNova](https://www.hpcwire.com/wp-content/uploads/2026/05/sn-new-gray-logo_150x60.png)](https://www.hpcwire.com/vendor/sambanova "SambaNova")[![Siemens](https://www.hpcwire.com/wp-content/uploads/2026/02/siemens-logo_150x60.png)](https://www.hpcwire.com/vendor/siemens "Siemens")[![SimOps](https://www.hpcwire.com/wp-content/uploads/2025/12/simops_logo_150x60.png)](https://www.hpcwire.com/vendor/simops "SimOps")[![TotalCAE](https://www.hpcwire.com/wp-content/uploads/2025/10/totalcae_150x60.jpg)](https://www.hpcwire.com/vendor/totalcae "TotalCAE")

[![Viridien](https://www.hpcwire.com/wp-content/uploads/2025/10/HPCW-viridien-banner-360x90-1.jpg)](https://www.hpcwire.com/vendor/viridien "Viridien")

[Processors](https://www.hpcwire.com/topic/processors/)

## [OpenMoonRay™ Performance Accelerated by Lenovo and Intel® Xeon® 6](https://www.hpcwire.com/2026/09/28/openmoonray-performance-accelerated-by-lenovo-and-intel-xeon-6/)

As the demands of cinematic rendering continue to grow, creative applications are increasingly converging with traditional high-performance computing (HPC) workloads. Physically...

SPONSORED CONTENT

## FEATURED ADVANCE SCALE JOB

![Citadel Securities](https://www.hpcwire.com/wp-content/uploads/2026/01/CitadelSecurities_logo.png)

#### Citadel Securities

**Position:** High Performance Computing Engineer


**Location:** Switzerland

[View All Jobs](https://careers.hpcwire.com/)

## FEATURED EVENT

[![](https://www.hpcwire.com/wp-content/uploads/2026/09/ocpglobal_300x170.jpg)](https://www.opencompute.org/summit/global-summit)

#### October 12-15

The OCP Summit is the premier global event uniting the most forward-thinking minds in open IT ecosystem development to focus on sustainable open compute solutions.


[View All Events](https://www.hpcwire.com/events/)

[![AI Infra Summit](https://www.hpcwire.com/wp-content/uploads/2026/09/AIW-AISummit26-banner-300X250.jpg)](https://www.hpcwire.com/aiwire/special-feature/ai-infra-summit-2026/)

## UPCOMING EVENTS

Current Month

[_30_ _sep_ _All Day__01_ _oct_AI Conference_(All Day)(GMT-07:00)__San Francisco, CA_](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/#)

[**Learn More**](https://aiconference.com/)

[Calendar](https://www.hpcwire.com/export-events/187792_0/?key=7542a10713 "Add to your calendar") [GoogleCal](https://www.google.com/calendar/event?action=TEMPLATE&text=AI%20Conference&dates=20260930T070000Z/20261002T065959Z&ctz=America%2FLos_Angeles&details=AI%20Conference&location=San%20Francisco%2C%20CA "Add to google calendar")

[_05_ _oct_ _All Day__06_HPC User Forum_(All Day)(GMT+02:00)__Stuttgart, Germany_](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/#)

### Event Details

Join us for our 93rd HPC User Forum at the High Performance Computing Center (HLRS) in Stuttgart, Germany, October 5-6. Topics to include EuroHPC JU and the Rise of

### Event Details

Join us for our 93rd [HPC User Forum](https://www.hpcuserforum.com/international-hpc-user-forum-october-2026/) at the High Performance Computing Center (HLRS) in Stuttgart, Germany, October 5-6. Topics to include EuroHPC JU and the Rise of AI Factories in Europe, AI Leadership Computing at HLRS, Quantum Computing Updates, and more! A full [agenda](https://www.hpcuserforum.com/international-hpc-user-forum-october-2026/) is available on our website. The HPC User Forum, established in 1999, is a great way to connect with the HPC community. Our mission is to promote the health of the global HPC industry and address issues of common concern to users.

[Register](https://metroconnections.swoogo.com/2026stuttgartuserforum) today!

more

[**Learn More**](https://metroconnections.swoogo.com/2026stuttgartuserforum)

[Calendar](https://www.hpcwire.com/export-events/197759_0/?key=7542a10713 "Add to your calendar") [GoogleCal](https://www.google.com/calendar/event?action=TEMPLATE&text=HPC%20User%20Forum&dates=20261004T220000Z/20261006T215959Z&ctz=Europe%2FBerlin&details=HPC%20User%20Forum&location=Stuttgart%2C%20Germany "Add to google calendar")

[_07_ _oct_ _All Day__08_World Summit AI_(All Day)(GMT+02:00)__Amsterdam, Netherlands_](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/#)

### Event Details

World Summit AI is the world’s leading AI summit, bringing together the people shaping how AI is researched, governed and deployed globally. Since launching in Amsterdam in 2017, the summit

### Event Details

World Summit AI is the world’s leading AI summit, bringing together the people shaping how AI is researched, governed and deployed globally. Since launching in Amsterdam in 2017, the summit has become a critical meeting point for enterprise leaders, big tech, start-ups, researchers, policymakers, investors and ethical experts from across the global AI ecosystem.

Now entering its 10th anniversary edition, World Summit AI continues to set the global AI agenda, spotlighting real-world applications, emerging technologies, and the risks, benefits and opportunities of artificial intelligence. The summit is renowned for hosting the world’s most influential voices in AI and for fostering meaningful collaboration across industries and sectors.

World Summit AI sits as the anchor of World AI Week, the world’s leading gathering of the global AI community. A high-energy series of 100+ cutting-edge events across business, science, technology and networking.

more

[**Learn More**](https://hubs.li/Q04jTXq_0)

[Calendar](https://www.hpcwire.com/export-events/187797_0/?key=7542a10713 "Add to your calendar") [GoogleCal](https://www.google.com/calendar/event?action=TEMPLATE&text=World%20Summit%20AI&dates=20261006T220000Z/20261008T215959Z&ctz=Europe%2FAmsterdam&details=World%20Summit%20AI&location=Amsterdam%2C%20Netherlands "Add to google calendar")

[View All Events](https://www.hpcwire.com/events/)

![QCwire](https://www.hpcwire.com/wp-content/themes/hpc-theme/assets/img/qc-600.webp)

#### Current Stories

- [DOE’s $215M Quantum Competition Ties Awards to Verified Performance](https://www.hpcwire.com/2026/09/18/does-215m-quantum-competition-ties-awards-to-verified-performance/)
- [Quantum Hardware Is Ready for HPC, But Software Is Not, Alice & Bob Say](https://www.hpcwire.com/2026/09/09/quantum-hardware-is-ready-for-hpc-but-software-is-not-alice-bob-say/)
- [IBM Nighthawk r2 Tops 100,000 Circuits per Second with New Reset Architecture](https://www.hpcwire.com/2026/09/04/ibm-nighthawk-r2-tops-100000-circuits-per-second-with-new-reset-architecture/)

[GO TO QCwire](https://www.hpcwire.com/qcwire/)

![AIwire](https://www.hpcwire.com/wp-content/themes/hpc-theme/assets/img/ai-600.webp)

#### Current Stories

- [IBM Introduces Self-Hosted Deployment for IBM Bob](https://www.hpcwire.com/aiwire/2026/10/01/ibm-introduces-self-hosted-deployment-for-ibm-bob/)
- [Cohere Releases Embed 5 with Pro and Fast Tiers for Enterprise AI](https://www.hpcwire.com/aiwire/2026/10/01/cohere-releases-embed-5-with-pro-and-fast-tiers-for-enterprise-ai/)
- [Illinois Researcher Receives NSF Grant and Sets AI Agent Ecosystems ISO Standard](https://www.hpcwire.com/aiwire/2026/10/01/illinois-researcher-receives-nsf-grant-and-sets-ai-agent-ecosystems-iso-standard/)

[GO TO AIwire](https://www.hpcwire.com/aiwire/)

![BigDATAwire](https://www.hpcwire.com/wp-content/themes/hpc-theme/assets/img/data-600.webp)

#### Current Stories

- [Microsoft Pushes AI Deeper Into Scientific Discovery With Quine](https://www.hpcwire.com/bigdatawire/2026/09/30/microsoft-pushes-ai-deeper-into-scientific-discovery-with-quine/)
- [Why 70% of Enterprise AI Initiatives Fail, and It Isn’t the Model](https://www.hpcwire.com/bigdatawire/2026/09/29/why-70-of-enterprise-ai-initiatives-fail-and-it-isnt-the-model/)
- [How AI Agents Are Reshaping the Database](https://www.hpcwire.com/bigdatawire/2026/09/28/ai-agents-are-starting-to-reshape-the-database/)

[GO TO BigDATAwire](https://www.hpcwire.com/bigdatawire)

[Tweet this !](https://twitter.com/intent/tweet?text=VAST%20Data%20Expands%20AI%20Data%20Stack%2C%20Keeps%20Eye%20on%20North%20Star%20-%20https%3A%2F%2Fwww.hpcwire.com%2F2026%2F02%2F25%2Fvast-data-expands-ai-data-stack-keeps-eye-on-north-star%2F%20 "Tweet this !")[Share this on Facebook](https://www.facebook.com/share.php?u=https%3A%2F%2Fwww.hpcwire.com%2F2026%2F02%2F25%2Fvast-data-expands-ai-data-stack-keeps-eye-on-north-star%2F "Share this on Facebook")[Add this to LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.hpcwire.com%2F2026%2F02%2F25%2Fvast-data-expands-ai-data-stack-keeps-eye-on-north-star%2F "Add this to LinkedIn")[Submit this to Reddit](https://reddit.com/submit?url=https%3A%2F%2Fwww.hpcwire.com%2F2026%2F02%2F25%2Fvast-data-expands-ai-data-stack-keeps-eye-on-north-star%2F&title=VAST%20Data%20Expands%20AI%20Data%20Stack%2C%20Keeps%20Eye%20on%20North%20Star "Submit this to Reddit")[Email this ](mailto:?subject=VAST%20Data%20Expands%20AI%20Data%20Stack%2C%20Keeps%20Eye%20on%20North%20Star&body=Ten%20years%20ago%2C%20VAST%20Data%20founders%20pondered%20what%20it%20would%20take%20to%20build%20a%20thinking%20machine%2C%20a%20compute%20-%20https%3A%2F%2Fwww.hpcwire.com%2F2026%2F02%2F25%2Fvast-data-expands-ai-data-stack-keeps-eye-on-north-star%2F "Email this ")[More share links](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "More share links")

### Share

[Close](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Close")

[Blogger](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Post this on Blogger")

[Bluesky](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Post this on Bluesky")

[Email](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Email this ")

[Facebook](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Share this on Facebook")

[Facebook messenger](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Facebook messenger")

[Flipboard](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Flipboard")

[Hacker News](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Share this on HackerNews")

[Line](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Line")

[LinkedIn](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Add this to LinkedIn")

[Mastodon](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Share this on Mastodon")

[Odnoklassniki](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Odnoklassniki")

[PDF](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Convert to PDF")

[Pinterest](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Submit this to Pinterest")

[Print](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Print this article ")

[Reddit](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Submit this to Reddit")

[Short link](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Short link")

[SMS](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Share via SMS")

[Telegram](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Telegram")

[Tumblr](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Share this on Tumblr")

[Twitter](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Tweet this !")

[VKontakte](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Share this on VKontakte")

[wechat](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "WeChat")

[Weibo](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Weibo")

[WhatsApp](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "WhatsApp")

[X](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Share this on X")

[Xing](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Share this on Xing")

### Copy short link

[Close](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/# "Close")

[Copy link](https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/#)

X

Twitter Widget Iframe