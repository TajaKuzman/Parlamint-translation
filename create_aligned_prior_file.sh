#!/bin/sh
cd /home/tajak/Parlamint-translation/eflomal

lang_code=$1

python3 mergefiles.py source_sentences_${lang_code}.txt English_sentences_${lang_code}.txt > ${lang_code}-en.file