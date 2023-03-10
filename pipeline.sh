#!/bin/sh

export CUDA_VISIBLE_DEVICES=2

echo ${CUDA_VISIBLE_DEVICES}

lang_code="CZ"

#python 1-conllu-to-df.py ${lang_code} > logs/${lang_code}/create-conllu.md

#python 3-translate.py > logs/${lang_code}/translate.md

python 4-word-alignment.py ${lang_code} > logs/${lang_code}/align.md

python 5-create-conllu.py ${lang_code} > logs/${lang_code}/create_conllu.md