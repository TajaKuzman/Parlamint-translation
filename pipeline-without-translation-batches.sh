#!/bin/sh

gpu_device=2

CUDA_VISIBLE_DEVICES=${gpu_device}, python 1-conllu-to-df.py

CUDA_VISIBLE_DEVICES=${gpu_device}, python 3-translate.py

CUDA_VISIBLE_DEVICES=${gpu_device}, python 4-word-alignment-without-translation-in-batches.py

#CUDA_VISIBLE_DEVICES=${gpu_device}, python 5-create-conllu.py