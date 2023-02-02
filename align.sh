#!/bin/sh
cd /home/tajak/Parlamint-translation/eflomal

lang_code=$1

python3 align.py -s source_sentences_${lang_code}.txt -t English_sentences_${lang_code}.txt --model 3 -r source-en_${lang_code}.rev -f source-en_${lang_code}.fwd --overwrite