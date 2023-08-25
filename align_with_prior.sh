#!/bin/sh
cd /home/tajak/Parlamint-translation/eflomal

lang_code=$1

python3 align.py -s source_sentences_${lang_code}_add.txt -t English_sentences_${lang_code}_add.txt --priors ${lang_code}-en.priors --model 3 -f source-en-${lang_code}-add-file.fwd -r source-en-${lang_code}-add-file.rev