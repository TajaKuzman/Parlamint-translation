#!/bin/sh

export CUDA_VISIBLE_DEVICES=6

echo ${CUDA_VISIBLE_DEVICES}

lang_code="HR"

#python 1-conllu-to-df.py ${lang_code} > logs/${lang_code}/create-conllu.md

# Before translating, change the opus-lang-code in the dictionary in the translate.py (line 47)
python 3-translate.py ${lang_code}> logs/${lang_code}/translate.md

#python 4-word-alignment.py ${lang_code} > logs/${lang_code}/align.md

#python 5-create-conllu.py ${lang_code} > logs/${lang_code}/create_conllu.md