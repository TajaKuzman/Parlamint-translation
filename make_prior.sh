#!/bin/sh
cd /home/tajak/Parlamint-translation/eflomal

lang_code=$1

python3 makepriors.py -i ${lang_code}-en.file -f source-en_${lang_code}.fwd -r source-en_${lang_code}.rev --priors ${lang_code}-en.priors