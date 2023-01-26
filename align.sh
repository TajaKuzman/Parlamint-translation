#!/bin/sh
cd /home/tajak/Parlamint-translation/eflomal

python3 align.py -s source_sentences.txt -t English_sentences.txt --model 3 -r source-en.rev -f source-en.fwd