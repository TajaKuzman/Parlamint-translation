# Machine translating the ParlaMint output

Tasks:
- analyse various MT models on a sample data (ParlaMint-sample-sentence-tokenized.txt): see [code in Kaggle](https://www.kaggle.com/code/tajakuz/simple-machine-translation-with-various-mt-systems), results in the spreadsheet *ParlaMint_MT_Comparison-all-models.xlsx*
- extract data to be translated based on the Parlamint format: see code in *1-Prepare-and-translate-data.ipynb*
- use OPUSMT through EasyNMT/Hugging Face to machine translate the output - see code in *1-Prepare-and-translate-data.ipynb*
- use eftomal to get word alignments (train it with the MT output) and assure that proper names are correctly translated based on the word alignments - see code in *2-Word_alignments.ipynb*. I've ran this script in Google Colab, because you need sudo to install eflomal (which I don't have in the virtual machine).

To do: in 71 cases (9% of instances with proper nouns), the length of English translation is longer than the length of the original text - if we look at alignments from Slovene to English, we don't get the values for the proper nouns - I will check also alignments in the other direction to fix this.

Problems:
1) there can be errors in proper name annotation: some names are incorrectly annotated as proper names, substituting them will lead to wrong translations (e.g. “Slovenci ne rabimo ISIS-a. -> Slovenians don't need ISIS.” - Slovenci annotated as proper name of a person (name type=”PER”), substituting the word with its lemma will ruin a good translation (-> Slovenec don't need ISIS)

2) there can be errors in word alignment which will also ruin the translation - there are many such errors in the sample (see instances in the [code](https://github.com/TajaKuzman/Parlamint-translation/blob/master/2-Word_alignments.ipynb)) - we don’t know whether we introduce more errors than solutions

3) if the proper noun is followed by a punctuation mark (without a space), the punctuation mark will be lost after substitution

Sample analysis:
- 816 out of 8217 instances (10%) contain proper nouns.

Most common substitutions:

|                                                                        |   substituted_word |
|:-----------------------------------------------------------------------|-------------------:|
| []                                                                     |                 71 |
| [('Brglez', 'Brglez')]                                                 |                  5 |
| [('Luka', 'Luka'), ('Moon,', 'Mesec')]                                 |                  5 |
| [('Tomic.', 'Violeta')]                                                |                  5 |
| [('Left,', 'Levica')]                                                  |                  5 |
| [('Left', 'Levica')]                                                   |                  5 |
| [('Prikl.', 'Uroš')]                                                   |                  4 |
| [('Mir', 'Miro'), ('Cerar', 'Cerar')]                                  |                  4 |
| [('Levia,', 'Levica')]                                                 |                  4 |
| [('Moon.', 'Luka')]                                                    |                  4 |
| [('Juliana', 'Julijana'), ('Bizjak', 'Bizjak'), ('Mlakar,', 'Mlakar')] |                  3 |
| [('Brglez,', 'Brglez')]                                                |                  3 |
| [('and', 'Levica')]                                                    |                  3 |
| [('Milan', 'Milan'), ('Brglez', 'Brglez')]                             |                  3 |
| [('Milan', 'Milan'), ('Brglez,', 'Brglez')]                            |                  3 |
| [('Matic,', 'Matić')]                                                  |                  3 |
| [('Luka', 'Luka'), ('Moon.', 'Mesec')]                                 |                  3 |
| [('Natasa', 'Nataša'), ('Sukič,', 'Sukič')]                            |                  3 |
| [('Horvat', 'Horvat')]                                                 |                  3 |
| [('Carrot,', 'Trček')]                                                 |                  3 |