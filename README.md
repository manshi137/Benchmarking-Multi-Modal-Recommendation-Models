# COL865_MMRS

## Conda Environment
Create a conda environment using the requirements.txt file

## How to run
Go to mmrec_toolbox/src/

Use the command:

python main.py -m {MODEL_NAME} -d ml100k

MODEL_NAME:

    BM3

    FREEDOM

    DRAGON

    LATTICE

    MGCN

    DualGNN


## Log files
Log files are stored in mmrec_toolbox/src/log/

## i_id_mapping
Movie name to ItemId mapping

## u_id_mapping
Original UserId to new 0-indexed UserId mapping

## ml100k.inter 
x_label = 0 for Training

x_label = 1 for Valid

x_label = 2 for Test


## image_feat.npy
Image embeddings generated using resnet.ipynb

## text_feat.npy
Text embeddings generated using bert.ipynb

