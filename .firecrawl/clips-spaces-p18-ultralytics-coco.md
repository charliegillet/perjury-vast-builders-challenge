[Ultralytics YOLO27:Coming soon. Join the waitlist.](https://www.ultralytics.com/yolo/yolo27)

 [Skip to main content](https://docs.ultralytics.com/datasets/detect/coco#main-content)

- [Ultralytics](https://docs.ultralytics.com/)

Search...Ctrl K

- [Home](https://docs.ultralytics.com/)
- [Quickstart](https://docs.ultralytics.com/quickstart)

- Home
- Modes
- Tasks
- Models
- Compare
- Datasets


  - [Overview](https://docs.ultralytics.com/datasets)
  - Detection


    - [Overview](https://docs.ultralytics.com/datasets/detect)
    - [African-wildlife](https://docs.ultralytics.com/datasets/detect/african-wildlife)
    - [Argoverse](https://docs.ultralytics.com/datasets/detect/argoverse)
    - [Brain-tumor](https://docs.ultralytics.com/datasets/detect/brain-tumor)
    - [COCO](https://docs.ultralytics.com/datasets/detect/coco)
    - [COCO8](https://docs.ultralytics.com/datasets/detect/coco8)
    - [COCO8-Grayscale](https://docs.ultralytics.com/datasets/detect/coco8-grayscale)
    - [COCO8-Multispectral](https://docs.ultralytics.com/datasets/detect/coco8-multispectral)
    - [COCO12-Formats](https://docs.ultralytics.com/datasets/detect/coco12-formats)
    - [COCO128](https://docs.ultralytics.com/datasets/detect/coco128)
    - [Construction-PPE](https://docs.ultralytics.com/datasets/detect/construction-ppe)
    - [GlobalWheat2020](https://docs.ultralytics.com/datasets/detect/globalwheat2020)
    - [HomeObjects-3K](https://docs.ultralytics.com/datasets/detect/homeobjects-3k)
    - [KITTI](https://docs.ultralytics.com/datasets/detect/kitti)
    - [LVIS](https://docs.ultralytics.com/datasets/detect/lvis)
    - [Medical-pills](https://docs.ultralytics.com/datasets/detect/medical-pills)
    - [Objects365](https://docs.ultralytics.com/datasets/detect/objects365)
    - [OpenImagesV7](https://docs.ultralytics.com/datasets/detect/open-images-v7)
    - [RF100](https://docs.ultralytics.com/datasets/detect/roboflow-100)
    - [Signature](https://docs.ultralytics.com/datasets/detect/signature)
    - [SKU-110K](https://docs.ultralytics.com/datasets/detect/sku-110k)
    - [TT100K](https://docs.ultralytics.com/datasets/detect/tt100k)
    - [VisDrone](https://docs.ultralytics.com/datasets/detect/visdrone)
    - [VOC](https://docs.ultralytics.com/datasets/detect/voc)
    - [xView](https://docs.ultralytics.com/datasets/detect/xview)

  - Segmentation
  - Semantic Segmentation
  - Depth Estimation
  - Pose
  - Classification
  - Oriented Bounding Boxes (OBB)
  - [Multi-Object Tracking](https://docs.ultralytics.com/datasets/track)
  - Explorer

- Solutions
- Guides
- Integrations
- Platform
- [Rust Inference](https://docs.ultralytics.com/inference)
- Reference
- Help

### Get Started

Annotate, train and deploy YOLO models in one click.

- Cloud training
- Dataset annotation
- One-click inference

[$25 free creditswith work email](https://platform.ultralytics.com/signup)

[Get Started](https://platform.ultralytics.com/signup) [Sign in](https://docs.ultralytics.com/signin?redirect_url=%2Fdatasets%2Fdetect%2Fcoco)

[CC BY 4.0](https://cocodataset.org/#termsofuse)

[Edit page on GitHub](https://github.com/ultralytics/ultralytics/blob/main/docs/en/datasets/detect/coco.md)

# COCO Dataset [\#](https://docs.ultralytics.com/datasets/detect/coco\#coco-dataset)

[![COCO 2017 preview 1](https://cdn.ul.run/eu/t/7219561b793f26d813ee4a34447ae398_256.webp?Expires=1790967600&KeyName=key-v1&Signature=jYT5FIDh0Th4Gn_1cINTHD-0hCo)\\
\\
![COCO 2017 preview 2](https://cdn.ul.run/eu/t/23cd5c2dae5c446366435a457ac3ce39_256.webp?Expires=1790967600&KeyName=key-v1&Signature=w3JvvjVWlraShqHyIJX2l7Usuw0)\\
\\
![COCO 2017 preview 3](https://cdn.ul.run/eu/t/b7607ddbfd621492b60db6a2331ba652_256.webp?Expires=1790967600&KeyName=key-v1&Signature=_9iQAJbMHaukERnsaX6QGOonO4U)\\
\\
![COCO 2017 preview 4](https://cdn.ul.run/eu/t/351191fb288040f2187e0504c729e35a_256.webp?Expires=1790967600&KeyName=key-v1&Signature=0FinAIsxhO5eltK6ChmtsJwtQ0A)\\
\\
123,272\\
\\
COCO 2017\\
\\
ultralytics\\
\\
publicDetect\\
\\
COCO 2017 is the canonical Common Objects in Context detection benchmark. Its complex everyday scenes contain dense bounding-box annotations across 80 classes, with varied object scale, occlusion, crowding, and contextual relationships for standardized model comparison.\\
\\
180classes11.6 GBSep 2, 2026\\
\\
personbicyclecarmotorcycle+76\\
\\
object-detectioncocococo2017+1](https://platform.ultralytics.com/ultralytics/datasets/coco2017?utm_source=docs&utm_medium=card)

The [COCO](https://cocodataset.org/#home) (Common Objects in Context) dataset is a large-scale object detection, segmentation, and captioning dataset. It is designed to encourage research on a wide variety of object categories and is commonly used for benchmarking [computer vision](https://www.ultralytics.com/glossary/computer-vision-cv) models. It is an essential dataset for researchers and developers working on object detection, segmentation, and pose estimation tasks.

**Watch:** Ultralytics COCO Dataset Overview

## COCO Pretrained Models [\#](https://docs.ultralytics.com/datasets/detect/coco\#coco-pretrained-models)

| Model | size<br>(pixels) | mAPval<br>50-95 | mAPval<br>50-95(e2e) | Speed<br>CPU ONNX<br>(ms) | Speed<br>T4 TensorRT10<br>(ms) | params<br>(M) | FLOPs<br>(B) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [YOLO26n](https://platform.ultralytics.com/ultralytics/yolo26/yolo26n) | 640 | 40.9 | 40.1 | **38.9 ± 0.7** | **1.7 ± 0.0** | **2.4** | **5.5** |
| [YOLO26s](https://platform.ultralytics.com/ultralytics/yolo26/yolo26s) | 640 | 48.6 | 47.8 | 87.2 ± 0.9 | 2.5 ± 0.0 | 9.5 | 20.9 |
| [YOLO26m](https://platform.ultralytics.com/ultralytics/yolo26/yolo26m) | 640 | 53.1 | 52.5 | 220.0 ± 1.4 | 4.7 ± 0.1 | 20.4 | 68.4 |
| [YOLO26l](https://platform.ultralytics.com/ultralytics/yolo26/yolo26l) | 640 | 55.0 | 54.4 | 286.2 ± 2.0 | 6.2 ± 0.2 | 24.8 | 86.8 |
| [YOLO26x](https://platform.ultralytics.com/ultralytics/yolo26/yolo26x) | 640 | **57.5** | **56.9** | 525.8 ± 4.0 | 11.8 ± 0.2 | 55.7 | 194.4 |

## Key Features [\#](https://docs.ultralytics.com/datasets/detect/coco\#key-features)

- COCO contains 330K images, with 200K images having annotations for object detection, segmentation, and captioning tasks.
- The dataset comprises 80 object categories, including common objects like cars, bicycles, and animals, as well as more specific categories such as umbrellas, handbags, and sports equipment.
- Annotations include object bounding boxes, segmentation masks, and captions for each image.
- COCO provides standardized evaluation metrics like [mean Average Precision](https://www.ultralytics.com/glossary/mean-average-precision-map) (mAP) and Average [Recall](https://www.ultralytics.com/glossary/recall) (AR) for object detection and segmentation, making it suitable for comparing model performance.

## Dataset Structure [\#](https://docs.ultralytics.com/datasets/detect/coco\#dataset-structure)

The COCO dataset is split into three subsets:

1. **Train2017**: 118,287 images for training object detection, segmentation, and captioning models.
2. **Val2017**: 5,000 images used for validation during model training.
3. **Test2017**: 20,288 test-dev images used for benchmarking trained models. Ground truth annotations for this subset are not publicly available, and results are submitted to the [COCO evaluation server](https://cocodataset.org/#upload) for performance evaluation.

## Applications [\#](https://docs.ultralytics.com/datasets/detect/coco\#applications)

The COCO dataset is widely used for training and evaluating [deep learning](https://www.ultralytics.com/glossary/deep-learning-dl) models in object detection (such as [Ultralytics YOLO](https://docs.ultralytics.com/models/yolo26), [Faster R-CNN](https://arxiv.org/abs/1506.01497), and [SSD](https://arxiv.org/abs/1512.02325)), [instance segmentation](https://www.ultralytics.com/glossary/instance-segmentation) (such as [Mask R-CNN](https://arxiv.org/abs/1703.06870)), and keypoint detection (such as [OpenPose](https://arxiv.org/abs/1812.08008)). The dataset's diverse set of object categories, large number of annotated images, and standardized evaluation metrics make it an essential resource for computer vision researchers and practitioners.

Annotations exported from labeling tools in COCO JSON follow this same structure. To train on your own COCO-format data, see [Convert COCO Annotations to YOLO](https://docs.ultralytics.com/guides/coco-to-yolo).

## Dataset YAML [\#](https://docs.ultralytics.com/datasets/detect/coco\#dataset-yaml)

A YAML file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. In the case of the COCO dataset, the `coco.yaml` file is maintained at [https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml](https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml).

ultralytics/cfg/datasets/coco.yaml

```
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# COCO 2017 dataset https://cocodataset.org by Microsoft
# Documentation: https://docs.ultralytics.com/datasets/detect/coco
# Example usage: yolo train data=coco.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── coco ← downloads here (20.3 GB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: coco # dataset root dir
train: train2017.txt # train images (relative to 'path') 118287 images
val: val2017.txt # val images (relative to 'path') 5000 images
test: test-dev2017.txt # 20288 of 40670 images, submit via https://cocodataset.org/#detection-eval

# Classes
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  4: airplane
  5: bus
  6: train
  7: truck
  8: boat
  9: traffic light
  10: fire hydrant
  11: stop sign
  12: parking meter
  13: bench
  14: bird
  15: cat
  16: dog
  17: horse
  18: sheep
  19: cow
  20: elephant
  21: bear
  22: zebra
  23: giraffe
  24: backpack
  25: umbrella
  26: handbag
  27: tie
  28: suitcase
  29: frisbee
  30: skis
  31: snowboard
  32: sports ball
  33: kite
  34: baseball bat
  35: baseball glove
  36: skateboard
  37: surfboard
  38: tennis racket
  39: bottle
  40: wine glass
  41: cup
  42: fork
  43: knife
  44: spoon
  45: bowl
  46: banana
  47: apple
  48: sandwich
  49: orange
  50: broccoli
  51: carrot
  52: hot dog
  53: pizza
  54: donut
  55: cake
  56: chair
  57: couch
  58: potted plant
  59: bed
  60: dining table
  61: toilet
  62: tv
  63: laptop
  64: mouse
  65: remote
  66: keyboard
  67: cell phone
  68: microwave
  69: oven
  70: toaster
  71: sink
  72: refrigerator
  73: book
  74: clock
  75: vase
  76: scissors
  77: teddy bear
  78: hair drier
  79: toothbrush

# Download script/URL (optional)
download: |
  from pathlib import Path

  from ultralytics.utils import ASSETS_URL
  from ultralytics.utils.downloads import download

  # Download labels
  segments = True  # segment or box labels
  dir = Path(yaml["path"])  # dataset root dir
  urls = [ASSETS_URL + ("/coco2017labels-segments.zip" if segments else "/coco2017labels.zip")]  # labels
  download(urls, dir=dir.parent)

  # Download data (test2017.zip excluded: ground truth is withheld, only used for the eval-server test-dev split)
  urls = [\
      "http://images.cocodataset.org/zips/train2017.zip",  # 19G, 118k images\
      "http://images.cocodataset.org/zips/val2017.zip",  # 1G, 5k images\
  ]
  download(urls, dir=dir / "images", threads=3)
```

## Usage [\#](https://docs.ultralytics.com/datasets/detect/coco\#usage)

The COCO2017 training and validation data (20.3 GB) downloads automatically the first time you start training. To train a YOLO26n model on COCO for 100 [epochs](https://www.ultralytics.com/glossary/epoch) with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model [Training](https://docs.ultralytics.com/modes/train) page. You can also run COCO training in the cloud with [Ultralytics Platform](https://platform.ultralytics.com/ultralytics/datasets/coco2017).

Train Example

PythonCLI

```
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="coco.yaml", epochs=100, imgsz=640)
```

## Sample Images and Annotations [\#](https://docs.ultralytics.com/datasets/detect/coco\#sample-images-and-annotations)

The COCO dataset contains a diverse set of images with various object categories and complex scenes. Here are some examples of images from the dataset, along with their corresponding annotations:

![COCO dataset mosaic training batch with object detection](https://cdn.ul.run/i/f9843f887d8186a8b43fdec6f570dcba.avif)

- **Mosaiced Image**: This image demonstrates a training batch composed of mosaiced dataset images. Mosaicing is a technique used during training that combines multiple images into a single image to increase the variety of objects and scenes within each training batch. This helps improve the model's ability to generalize to different object sizes, aspect ratios, and contexts.

The example showcases the variety and complexity of the images in the COCO dataset and the benefits of using mosaicing during the training process.

## Citations and Acknowledgments [\#](https://docs.ultralytics.com/datasets/detect/coco\#citations-and-acknowledgments)

If you use the COCO dataset in your research or development work, please cite the following paper:

Quote

BibTeX

```
@misc{lin2015microsoft,
      title={Microsoft COCO: Common Objects in Context},
      author={Tsung-Yi Lin and Michael Maire and Serge Belongie and Lubomir Bourdev and Ross Girshick and James Hays and Pietro Perona and Deva Ramanan and C. Lawrence Zitnick and Piotr Dollár},
      year={2015},
      eprint={1405.0312},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

We would like to acknowledge the COCO Consortium for creating and maintaining this valuable resource for the computer vision community. For more information about the COCO dataset and its creators, visit the [COCO dataset website](https://cocodataset.org/#home).

## FAQ [\#](https://docs.ultralytics.com/datasets/detect/coco\#faq)

- ### What is the COCO dataset and why is it important for computer vision?








The [COCO dataset](https://cocodataset.org/#home) (Common Objects in Context) is a large-scale dataset used for [object detection](https://www.ultralytics.com/glossary/object-detection), segmentation, and captioning. It contains 330K images with detailed annotations for 80 object categories, making it essential for benchmarking and training computer vision models. Researchers use COCO due to its diverse categories and standardized evaluation metrics like mean Average [Precision](https://www.ultralytics.com/glossary/precision) (mAP).

- ### How can I train a YOLO model using the COCO dataset?








To train a YOLO26 model using the COCO dataset, you can use the following code snippets:



Train Example







PythonCLI







```
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="coco.yaml", epochs=100, imgsz=640)
```











Refer to the [Training page](https://docs.ultralytics.com/modes/train) for more details on available arguments.

- ### What are the key features of the COCO dataset?








The COCO dataset includes:



  - 330K images, with 200K annotated for object detection, segmentation, and captioning.
  - 80 object categories ranging from common items like cars and animals to specific ones like handbags and sports equipment.
  - Standardized evaluation metrics (mAP and Average Recall) for object detection and segmentation.
  - **Mosaicing** technique in training batches to enhance model generalization across various object sizes and contexts.

- ### Where can I find pretrained YOLO26 models trained on the COCO dataset?








Pretrained YOLO26 models on the COCO dataset can be downloaded from the links provided in the documentation. Examples include:



  - [YOLO26n](https://platform.ultralytics.com/ultralytics/yolo26/yolo26n)
  - [YOLO26s](https://platform.ultralytics.com/ultralytics/yolo26/yolo26s)
  - [YOLO26m](https://platform.ultralytics.com/ultralytics/yolo26/yolo26m)
  - [YOLO26l](https://platform.ultralytics.com/ultralytics/yolo26/yolo26l)
  - [YOLO26x](https://platform.ultralytics.com/ultralytics/yolo26/yolo26x)

These models vary in size, mAP, and inference speed, providing options for different performance and resource requirements.

- ### How is the COCO dataset structured and how do I use it?








The COCO dataset is split into three subsets:



1. **Train2017**: 118,287 images for training.
2. **Val2017**: 5,000 images for validation during training.
3. **Test2017**: 20,288 test-dev images for benchmarking trained models. Results need to be submitted to the [COCO evaluation server](https://cocodataset.org/#upload) for performance evaluation.

The dataset's YAML configuration file is available at [coco.yaml](https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml), which defines paths, classes, and dataset details.

Contributors

[Edit page on GitHub](https://github.com/ultralytics/ultralytics/blob/main/docs/en/datasets/detect/coco.md)

[![glenn-jocher](https://avatars.githubusercontent.com/u/26833433?s=48)glenn-jocher19](https://github.com/glenn-jocher) [![raimbekovm](https://avatars.githubusercontent.com/u/144048515?s=48)raimbekovm5](https://github.com/raimbekovm) [![RizwanMunawar](https://avatars.githubusercontent.com/u/62513924?s=48)RizwanMunawar3](https://github.com/RizwanMunawar) [![pderrenger](https://avatars.githubusercontent.com/u/107626595?s=48)pderrenger1](https://github.com/pderrenger) [![jk4e](https://avatars.githubusercontent.com/u/116908874?s=48)jk4e1](https://github.com/jk4e) [![ambitious-octopus](https://avatars.githubusercontent.com/u/3855193?s=48)ambitious-octopus1](https://github.com/ambitious-octopus) [![MatthewNoyce](https://avatars.githubusercontent.com/u/131261051?s=48)MatthewNoyce1](https://github.com/MatthewNoyce)

CreatedNov 12, 2023Updated4 days ago

## Comments

Ask AIUltralytics