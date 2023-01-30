#!/bin/sh

export CUDA_VISIBLE_DEVICES=7

echo ${CUDA_VISIBLE_DEVICES}

python 1-conllu-to-df.py

python 3-translate.py

#python 4-word-alignment.py

#python 5-create-conllu.py