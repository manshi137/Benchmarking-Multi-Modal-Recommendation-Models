## Overview
This project provides a comprehensive exploration of multimodal recommendation models on Enhanced Movielens 100k Dataset, delving into their underlying technologies, benchmarking their performance using MMRec Tooblbox, and shedding light on their potential applications across diverse domains.

## Requirements
Create a conda environment using the 'requirements.txt' file

    conda create --name myenv --file requirements.txt
    conda activate myenv
    
## How to run
Go to 'mmrec_toolbox/src/'

Use the command:

    'python main.py -m {MODEL_NAME} -d ml100k'

MODEL_NAME:
- BM3
- FREEDOM
- DRAGON
- LATTICE
- MGCN
- DualGNN


## Log files
Log files are stored in 'mmrec_toolbox/src/log/'

### i_id_mapping
Movie Name to ItemId mapping

### u_id_mapping
Original UserId to new 0-indexed UserId mapping

### ml100k.inter 
x_label = 0 for Training

x_label = 1 for Valid

x_label = 2 for Test


### image_feat.npy
Image embeddings generated using resnet.ipynb

### text_feat.npy
Text embeddings generated using bert.ipynb


## Bechmarked Models
source code at: `src\models`

| **Model**       | **Paper**                                                                                             | **Conference/Journal** | **Code**    |
|------------------|--------------------------------------------------------------------------------------------------------|------------------------|-------------|
| DualGNN           | [DualGNN: Dual Graph Neural Network for Multimedia Recommendation](https://ieeexplore.ieee.org/abstract/document/9662655)                   | TMM'21                 | dualgnn.py   |
| LATTICE           | [Mining Latent Structures for Multimedia Recommendation](https://arxiv.org/abs/2104.09036)                                               | MM'21                  | lattice.py  |
| BM3         | [Bootstrap Latent Representations for Multi-modal Recommendation](https://dl.acm.org/doi/10.1145/3543507.3583251)                                          | WWW'23                 | bm3.py |
| FREEDOM | [A Tale of Two Graphs: Freezing and Denoising Graph Structures for Multimodal Recommendation](https://arxiv.org/abs/2211.06924)                                 | MM'23                  | freedom.py  |
| MGCN     | [Multi-View Graph Convolutional Network for Multimedia Recommendation](https://arxiv.org/abs/2308.03588)                       | MM'23               | mgcn.py          |
| DRAGON  | [Enhancing Dyadic Relations with Homogeneous Graphs for Multimodal Recommendation](https://arxiv.org/abs/2301.12097)                                 | ECAI'23                | dragon.py  |


