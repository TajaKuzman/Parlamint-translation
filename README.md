# Machine translating the ParlaMint output

Tasks:
- extract data to be translated based on the Parlamint format: see code in *1-Prepare-and-translate-data.ipynb*
- use OPUSMT through EasyNMT/Hugging Face to machine translate the output - see code in *1-Prepare-and-translate-data.ipynb*
- use eftomal to get word alignments (train it with the MT output) and assure that proper names are correctly translated based on the word alignments - see code in *2-Word_alignments.ipynb*. I've ran this script in Google Colab, because you need sudo to install eflomal (which I don't have in the virtual machine).

Problems:
1) there can be errors in proper name annotation: some names are incorrectly annotated as proper names, substituting them will lead to wrong translations (e.g. “Slovenci ne rabimo ISIS-a. -> Slovenians don't need ISIS.” - Slovenci annotated as proper name of a person (name type=”PER”), substituting the word with its lemma will ruin a good translation (-> Slovenec don't need ISIS)

2) there can be errors in word alignment which will also ruin the translation - there are many such errors in the sample (see instances in the code) - we don’t know whether we introduce more errors than solutions
