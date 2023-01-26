#!/bin/sh

gpu_device=7

CUDA_VISIBLE_DEVICES=${gpu_device}, python 1-conllu-to-df.py

CUDA_VISIBLE_DEVICES=7, python 3-translate-part1.py &
CUDA_VISIBLE_DEVICES=7, python 3-translate-part2.py &
CUDA_VISIBLE_DEVICES=7, python 3-translate-part3.py &

wait

CUDA_VISIBLE_DEVICES=${gpu_device}, python 4-word-alignment.py

#CUDA_VISIBLE_DEVICES=${gpu_device}, python 5-create-conllu.py