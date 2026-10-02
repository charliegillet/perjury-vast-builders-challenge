PIE is a new dataset for studying pedestrian behavior in traffic. PIE contains over 6 hours of footage recorded in typical traffic scenes with on-board camera. It also provides accurate vehicle information from OBD sensor (vehicle speed, heading direction and GPS coordinates) synchronized with video footage.

Rich spatial and behavioral annotations are available for pedestrians and vehicles that potentially interact with the ego-vehicle as well as for the relevant elements of infrastructure (traffic lights, signs and zebra crossings).

There are over 300K labeled video frames with 1842 pedestrian samples making this the largest publicly available dataset for studying pedestrian behavior in traffic.

## PIE Features

* * *

#### Continuous Footage

6 hours of HD video are recorded with on-board camera at 30 FPS and split into approximately 10 minute chunks.

#### Spatial Annotations

Bounding boxes are provided for 1842 pedestrians and vehicles that interact with the driver, as well as for elements of infrastructure (traffic lights, signs, zebra crossings, road boundaries).

#### Behavioral Annotations

Behavior tags are provided for each pedestrian per frame, including actions like walking, standing, crossing, looking (at the traffic), etc.

#### Vehicle Information

Accurate ego-vehicle information from OBD sensor is available for each frame of the video. It includes speed, GPS coordinates and heading direction.

#### Intention Annotations

We conducted a large scale human experiment to determine early crossing intention of the 1842 annotated pedestrians. For each pedestrian we provide intention probability aggregated from the responses of human subjects.

#### Variety of scenarios

Videos were recorded in the streets of Toronto with different crowd densities ranging from busy one-way streets to wide boulevards.

## PIE Stats

* * *

| Total number of frames | 909,480 |
| Total number of annotated frames | 293,437 |
| Number of pedestrians with behavior annotations | 1,842 |
| Number of pedestrian bounding boxes | 738,970 |
| Number of traffic object bounding boxes | 2,353,983 |
| Average length of pedestrian track | 401 frames |
|  |
| Pedestrian counts |
| Intend to cross and cross | 519 |
| Intend to cross and don't cross | 894 |
| Do not intend to cross | 429 |

### Download PIE

* * *

#### Videos

Get MP4 files

[Download](http://data.nvision2.eecs.yorku.ca/PIE_dataset/PIE_clips/)

#### Annotations

Annotations are hosted on our github page

[Go to github](https://github.com/aras62/PIE)

#### Models

Models that use PIE data for intention estimation, trajectory and crossing prediction are available on our github

[Go to github](https://github.com/aras62/PIEPredict)

### Cite us

If you found our dataset or models useful in your research please consider citing our paper:

@inproceedings{Rasouli2019PIE,

author = {Amir Rasouli and Iuliia Kotseruba and Toni Kunic and John K. Tsotsos},

title = {PIE: A Large-Scale Dataset and Models for Pedestrian Intention Estimation and Trajectory Prediction},

booktitle = {International Conference on Computer Vision (ICCV)},

year = {2019}
}


With questions regarding the dataset please contact Amir Rasouli (aras@eecs.yorku.ca) and Iuliia Kotseruba (yulia\_k@eecs.yorku.ca).

The videos and annotations are released under the [MIT License](https://github.com/aras62/PIE/blob/master/LICENSE).