No. of files: 25.
Number of words in the corpora: 1019396
Dataframe saved as /home/tajak/Parlamint-translation/results/AT/ParlaMint-AT-extracted-source-data-additional.csv
|        | file_path                                                                                                                                        | file                                                  | sentence_id                                           | text     | tokenized_text   | proper_nouns   |     length |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------|:------------------------------------------------------|:---------|:-----------------|:---------------|-----------:|
| count  | 66846                                                                                                                                            | 66846                                                 | 66846                                                 | 66846    | 66846            | 66846          | 66846      |
| unique | 25                                                                                                                                               | 25                                                    | 66846                                                 | 56094    | 56117            | 4311           |   nan      |
| top    | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-06-15-027-XXVII-NRSITZ-00162.conllu | ParlaMint-AT_2022-06-15-027-XXVII-NRSITZ-00162.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165_d2e194.s1 | – Bitte. | – Bitte .        | {}             |   nan      |
| freq   | 7373                                                                                                                                             | 7373                                                  | 1                                                     | 894      | 894              | 60580          |   nan      |
| mean   | nan                                                                                                                                              | nan                                                   | nan                                                   | nan      | nan              | nan            |    15.2499 |
| std    | nan                                                                                                                                              | nan                                                   | nan                                                   | nan      | nan              | nan            |    12.6157 |
| min    | nan                                                                                                                                              | nan                                                   | nan                                                   | nan      | nan              | nan            |     1      |
| 25%    | nan                                                                                                                                              | nan                                                   | nan                                                   | nan      | nan              | nan            |     6      |
| 50%    | nan                                                                                                                                              | nan                                                   | nan                                                   | nan      | nan              | nan            |    12      |
| 75%    | nan                                                                                                                                              | nan                                                   | nan                                                   | nan      | nan              | nan            |    21      |
| max    | nan                                                                                                                                              | nan                                                   | nan                                                   | nan      | nan              | nan            |   265      |




2023-08-22 11:35:38.836659: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-08-22 11:35:39.637103: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-08-22 11:35:39.637172: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-08-22 11:35:39.637178: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
2023-08-22 12:04:50 INFO: Loading these models for language: en (English):
========================
| Processor | Package  |
------------------------
| tokenize  | combined |
========================

2023-08-22 12:04:50 INFO: Use device: gpu
2023-08-22 12:04:50 INFO: Loading: tokenize
2023-08-22 12:04:50 INFO: Done loading processors!
|    | file_path                                                                                                                                     | file                                               | sentence_id                                           | text                                                                                                                        | tokenized_text                                                                                                                   | proper_nouns   |   length |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------|:------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|:---------------|---------:|
|  0 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/1999/ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165_d2e194.s1 | Meine Damen und Herren!                                                                                                     | Meine Damen und Herren !                                                                                                         | {}             |        4 |
|  1 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/1999/ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165_d2e194.s2 | Ich darf Sie alle herzlich begrüßen und eröffne die 165. Sitzung des Nationalrates.                                         | Ich darf Sie alle herzlich begrüßen und eröffne die 165. Sitzung des Nationalrates .                                             | {}             |       13 |
|  2 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/1999/ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165_d2e196.s1 | Ich gebe bekannt, daß die Amtlichen Protokolle der 162. und der 163. Sitzung vom 4.                                         | Ich gebe bekannt , daß die Amtlichen Protokolle der 162. und der 163. Sitzung von dem 4.                                         | {}             |       15 |
|  3 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/1999/ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165_d2e196.s2 | März 1999 sowie der 164. Sitzung vom 25. März 1999 in der Parlamentsdirektion aufgelegen und unbeeinsprucht geblieben sind. | März 1999 sowie der 164. Sitzung von dem 25. März 1999 in der Parlamentsdirektion aufgelegen und unbeeinsprucht geblieben sind . | {}             |       18 |
|  4 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/1999/ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165_d2e196.s3 | Sie gelten daher als genehmigt.                                                                                             | Sie gelten daher als genehmigt .                                                                                                 | {}             |        5 |




Entire corpus has 66846 sentences and 1019396 words.
Translation started.
Translation completed. It took 26.97 minutes for 66846 instances - 0.000403464680010771 minutes per one sentence.
|    | file_path                                                                                                                                     | file                                               | sentence_id                                           | text                                                                                | tokenized_text                                                                           | proper_nouns   |   length | translation                                                              |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------|:------------------------------------------------------|:------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|:---------------|---------:|:-------------------------------------------------------------------------|
|  0 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/1999/ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165_d2e194.s1 | Meine Damen und Herren!                                                             | Meine Damen und Herren !                                                                 | {}             |        4 | Ladies and gentlemen!                                                    |
|  1 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/1999/ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165_d2e194.s2 | Ich darf Sie alle herzlich begrüßen und eröffne die 165. Sitzung des Nationalrates. | Ich darf Sie alle herzlich begrüßen und eröffne die 165. Sitzung des Nationalrates .     | {}             |       13 | I can welcome you all and open the 165. Meeting of the National Council. |
|  2 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/1999/ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165_d2e196.s1 | Ich gebe bekannt, daß die Amtlichen Protokolle der 162. und der 163. Sitzung vom 4. | Ich gebe bekannt , daß die Amtlichen Protokolle der 162. und der 163. Sitzung von dem 4. | {}             |       15 | I declare that the official protocols of 162 and 163. Meeting of 4.      |




The file is saved as /home/tajak/Parlamint-translation/results/AT/ParlaMint-AT-translated-additional.csv
Tokenization of the translation started.
Tokenization completed. It took 2.03 minutes.
File saved as /home/tajak/Parlamint-translation/results/AT/ParlaMint-AT-translated-tokenized-additional.csv
|    | file_path                                                                                                                                     | file                                               | sentence_id                                           | text                                                                                | tokenized_text                                                                           | proper_nouns   |   length | translation                                                              | translation-tokenized                                                      | space-after-information                                                                                         |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------|:------------------------------------------------------|:------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|:---------------|---------:|:-------------------------------------------------------------------------|:---------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|
|  0 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/1999/ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165_d2e194.s1 | Meine Damen und Herren!                                                             | Meine Damen und Herren !                                                                 | {}             |        4 | Ladies and gentlemen!                                                    | Ladies and gentlemen !                                                     | ['Yes', 'Yes', 'No', 'Last']                                                                                    |
|  1 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/1999/ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165_d2e194.s2 | Ich darf Sie alle herzlich begrüßen und eröffne die 165. Sitzung des Nationalrates. | Ich darf Sie alle herzlich begrüßen und eröffne die 165. Sitzung des Nationalrates .     | {}             |       13 | I can welcome you all and open the 165. Meeting of the National Council. | I can welcome you all and open the 165 . Meeting of the National Council . | ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Last'] |
|  2 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/1999/ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165_d2e196.s1 | Ich gebe bekannt, daß die Amtlichen Protokolle der 162. und der 163. Sitzung vom 4. | Ich gebe bekannt , daß die Amtlichen Protokolle der 162. und der 163. Sitzung von dem 4. | {}             |       15 | I declare that the official protocols of 162 and 163. Meeting of 4.      | I declare that the official protocols of 162 and 163 . Meeting of 4 .      | ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Last']        |






Alignment started.

Number of aligned sentences: 66846


Issue: index 4: ['Abgeordneter', 'Abgeordnet']
Issue: index 11: ['Milošević', 'Milošević']
Issue: index 60: ['Milošević', 'Milošević']
Issue: index 1: ['Abgeordneter', 'Abgeordnet']
Issue: index 4: ['Abgeordneter', 'Abgeordnet']
Issue: index 6: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 6: ['Abgeordneter', 'Abgeordneter']
Issue: index 4: ['Abgeordneter', 'Abgeordnet']
Issue: index 4: ['Abgeordneter', 'Abgeordnet']
Issue: index 4: ['Abgeordneter', 'Abgeordnet']
Issue: index 4: ['Abgeordneter', 'Abgeordnet']
Issue: index 16: ['Bellen', 'Bellen']
Issue: index 4: ['Abgeordneter', 'Abgeordnet']
Issue: index 3: ['Abgeordneter', 'Abgeordnet']
Issue: index 4: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 4: ['Abgeordneter', 'Abgeordnet']
Issue: index 7: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 6: ['Abgeordneter', 'Abgeordnet']
Issue: index 4: ['Abgeordneter', 'Abgeordnet']
Issue: index 4: ['Abgeordneter', 'Abgeordneter']
Issue: index 6: ['Abgeordneter', 'Abgeordnet']
Issue: index 6: ['Abgeordneter', 'Abgeordnet']
Issue: index 12: ['Abgeordneter', 'Abgeordnet']
Issue: index 8: ['Einem', 'Einem']
Issue: index 6: ['Abgeordneter', 'Abgeordnet']
Issue: index 6: ['Abgeordneter', 'Abgeordnet']
Issue: index 8: ['Einem', 'Einem']
Issue: index 4: ['Abgeordneter', 'Abgeordneter']
Issue: index 4: ['Abgeordneter', 'Abgeordnet']
Issue: index 10: ['Abgeordneter', 'Abgeordnet']
Issue: index 1: ['Ministerin', 'Ministerin']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 2: ['Gewessler', 'Gewessler']
Issue: index 4: ['Abgeordneter', 'Abgeordnet']
Issue: index 1: ['Abgeordneter', 'Abgeordnet']
Issue: index 22: ['Fiedler', 'Fiedler']
Issue: index 6: ['Angerer', 'Angerer']
Issue: index 10: ['Ministerin', 'Ministerin']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 13: ['Abgeordneter', 'Abgeordneter']
Issue: index 8: ['Abgeordneter', 'Abgeordnet']
Issue: index 3: ['Abgeordneter', 'Abgeordnet']
Issue: index 1: ['Abgeordneter', 'Abgeordnet']
Issue: index 6: ['Abgeordneter', 'Abgeordnet']
Issue: index 1: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 1: ['Abgeordneter', 'Abgeordnet']
Issue: index 10: ['Herr', 'Herr']
Issue: index 2: ['Kollegin', 'Kollegin']
Issue: index 11: ['Fiedler', 'Fiedler']
Issue: index 1: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 7: ['Abgeordneter', 'Abgeordnet']
Issue: index 7: ['Abgeordneter', 'Abgeordnet']
Issue: index 1: ['Abgeordneter', 'Abgeordnet']
Issue: index 10: ['Minister', 'Minister']
Issue: index 29: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Götze', 'unknown']
Issue: index 3: ['Ministerin', 'Ministerin']
Issue: index 1: ['Abgeordneter', 'Abgeordnet']
Issue: index 14: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 2: ['Abgeordneter', 'Abgeordnet']
Issue: index 4: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 4: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 1: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 4: ['Ministerin', 'Ministerin']
Issue: index 13: ['Ministerin', 'Ministerin']
Issue: index 4: ['Ministerin', 'Ministerin']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 9: ['Abgeordneter', 'Abgeordneter']
Issue: index 1: ['Muchitsch', 'Muchitsch']
Issue: index 17: ['Wöginger', 'Wöginger']
Issue: index 1: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Kollegin', 'Kollegin']
Issue: index 1: ['Abgeordneter', 'Abgeordnet']
Issue: index 25: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 3: ['Abgeordneter', 'Abgeordnet']
Issue: index 36: ['Abgeordneter', 'Abgeordnet']
Issue: index 8: ['Abgeordneter', 'Abgeordnet']
Issue: index 1: ['Ministerin', 'Ministerin']
Issue: index 8: ['Abgeordneter', 'Abgeordnet']
Issue: index 15: ['Dagmar', 'Dagmar']
Issue: index 16: ['Belakowitsch', 'Belakowitsch']
Issue: index 4: ['Abgeordneter', 'Abgeordnet']
Issue: index 6: ['Abgeordneter', 'Abgeordnet']
Issue: index 1: ['Abgeordneter', 'Abgeordnet']
Issue: index 7: ['Abgeordneter', 'Abgeordnet']
Issue: index 15: ['Gewessler', 'Gewessler']
Issue: index 11: ['Kurz', 'Kurz']
Issue: index 1: ['Abgeordneter', 'Abgeordnet']
Issue: index 16: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 12: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 3: ['Abgeordneter', 'Abgeordnet']
Issue: index 3: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 10: ['Ottenschläger', 'Schläger']
Issue: index 1: ['Abgeordneter', 'Abgeordnet']
Issue: index 12: ['Ministerin', 'Ministerin']
Issue: index 1: ['Ministerin', 'Ministerin']
Issue: index 2: ['Ministerin', 'Ministerin']
Issue: index 3: ['Abgeordneter', 'Abgeordnet']
Issue: index 15: ['Dagmar', 'Dagmar']
Issue: index 16: ['Belakowitsch', 'Belakowitsch']
Issue: index 3: ['Abgeordneter', 'Abgeordnet']
Issue: index 7: ['Muchitsch', 'Muchitsch']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 4: ['Gewessler', 'Gewessler']
Issue: index 6: ['Abgeordneter', 'Abgeordnet']
Issue: index 2: ['Bernhardhat', 'Bernhardhat']
Issue: index 7: ['von', 'von']
Alignment completed. It took 0.65 minutes.
|                                    |   substituted_pairs |
|:-----------------------------------|--------------------:|
| 0                                  |               65160 |
| [('Belakovich', 'Belakowitsch')]   |                  64 |
| [('Neßler', 'Nessler')]            |                  41 |
| [('Ottenschlager', 'Schläger')]    |                  38 |
| [('Geessler', 'Gewessler')]        |                  38 |
| [('Vladimir', 'Wladimir')]         |                  34 |
| [('Putin', 'Putins')]              |                  32 |
| [('Minister', 'Ministerin')]       |                  31 |
| [('Kassinger', 'Kassegger')]       |                  28 |
| [('Meinl', 'Meinl-Reisinger')]     |                  27 |
| [('Putin', 'uknown')]              |                  22 |
| [('Schalmeiner', 'Schallmeiner')]  |                  22 |
| [('Ernst', 'Ernst-DZIedzic')]      |                  18 |
| [('God', 'Gott')]                  |                  17 |
| [('Muchich', 'Muchitsch')]         |                  16 |
| [('Prince', 'Fürst')]              |                  15 |
| [('Worm', 'Wurm')]                 |                  13 |
| [('Hartinger', 'Hartinger-klein')] |                  13 |
| [('Vogluer', 'Voglauer')]          |                  13 |
| [('Yılmaz', 'Yilmaz')]             |                  13 |



Number of errors:
(122, 19)



Example of sentences with substituted words.

|    | file_path                                                                                                                                     | file                                               | sentence_id                                           | text                                                                                                                                                                                                        | tokenized_text                                                                                                                                                                                                    | proper_nouns                                                                                                                                                                                                                                                                                                                                                                                                     |   length | translation                                                                                                                                                                                             | translation-tokenized                                                                                                                                                                                           | space-after-information                                                                                                                                                                                                                               | fwd_align_dict                                                                                                                                                                                                                                                                                                                               | bwd_align_dict                                                                                                                                                                                                                                                                                                               | alignments                                                                                                                                                                                                                                                   | new_translations                                                                                                                                                                                                       | substitution_info                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | substituted_pairs                 | substituted_words   | errors   | source_indices                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------|:------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------|:--------------------|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  5 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/1999/ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165_d2e198.s1 | Als verhindert gemeldet für die heutige Sitzung sind die Abgeordneten Smolle, Motter, Apfelbeck und Dr. Mertel.                                                                                             | Als verhindert gemeldet für die heutige Sitzung sind die Abgeordneten Smolle , Motter , Apfelbeck und Dr. Mertel .                                                                                                | {10: ['Smolle', 'Smolle'], 12: ['Motter', 'Motter'], 14: ['Apfelbeck', 'Apfelbeck'], 17: ['Mertel', 'Mertel']}                                                                                                                                                                                                                                                                                                   |       16 | Members Smolle, Motter, Applebeck and Dr. Mertel are reported to be prevented for today's meeting.                                                                                                      | Members Smolle , Motter , Applebeck and Dr. Mertel are reported to be prevented for today 's meeting .                                                                                                          | ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Last']                                                                                                                    | {1: '10', 2: '11', 3: '12', 4: '13', 5: '14', 6: '15', 7: '16', 8: '17', 9: '18', 10: '8', 11: '3', 12: '5', 13: '1', 14: '2', 15: '4', 16: '6', 17: '6', 18: '7', 19: '19'}                                                                                                                                                                 | {13: '1', 14: '2', 11: '3', 15: '4', 17: '5', 16: '6', 18: '7', 10: '8', 12: '9', 1: '10', 2: '11', 3: '12', 4: '13', 5: '14', 6: '15', 7: '16', 8: '17', 9: '18', 19: '19'}                                                                                                                                                 | {0: 12, 1: 13, 2: 10, 3: 14, 4: 16, 5: 15, 6: 17, 7: 9, 8: 11, 9: 0, 10: 1, 11: 2, 12: 3, 13: 4, 14: 5, 15: 6, 16: 7, 17: 8, 18: 18}                                                                                                                         | Members Smolle , Motter , Apfelbeck and Dr. Mertel are reported to be prevented for today 's meeting .                                                                                                                 | ["No substitution: ('Smolle', 'Smolle')", "No substitution: ('Motter', 'Motter')", ('Applebeck', 'Apfelbeck'), "No substitution: ('Mertel', 'Mertel')"]                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [('Applebeck', 'Apfelbeck')]      | {6: 'Applebeck'}    | No       | [['Als', 1], ['verhindert', 2], ['gemeldet', 3], ['für', 4], ['die', 5], ['heutige', 6], ['Sitzung', 7], ['sind', 8], ['die', 9], ['Abgeordneten', 10], ['Smolle', 11], [',', 12], ['Motter', 13], [',', 14], ['Apfelbeck', 15], ['und', 16], ['Dr.', 17], ['Mertel', 18], ['.', 19]]                                                                                                                                                                                                                                                |
|  8 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/1999/ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu | ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165_d2e205.s2 | Walter Guggenberger, Dr. Jörg Haider, Wilfried Tilg und Georg Wurmitzer auf ihre Mandate verzichtet haben und an ihrer Stelle Gerhard Reheis, Dr. Liane Höbinger-Lehrer, Ing. Walter Meischberger und Dkfm. | Walter Guggenberger , Dr. Jörg Haider , Wilfried Tilg und Georg Wurmitzer auf ihre Mandate verzichtet haben und an ihrer Stelle Gerhard Reheis , Dr. Liane Höbinger-Lehrer , Ing . Walter Meischberger und Dkfm . | {0: ['Walter', 'Walter'], 1: ['Guggenberger', 'Guggenberger'], 4: ['Jörg', 'Jörg'], 5: ['Haider', 'Haider'], 7: ['Wilfried', 'Wilfried'], 8: ['Tilg', 'Tilg'], 10: ['Georg', 'Georg'], 11: ['Wurmitzer', 'Wurmitzer'], 21: ['Gerhard', 'Gerhard'], 22: ['Reheis', 'Reheis'], 25: ['Liane', 'Liane'], 26: ['Höbinger-Lehrer', 'Höbinger-Lehrer'], 30: ['Walter', 'Walter'], 31: ['Meischberger', 'Meischberger']} |       29 | Walter Guggenberger, Dr. Jörg Haider, Wilfried Tilg and Georg Wurmitzer have renounced their mandates and in their place, Gerhard Reheis, Dr. Liane Höbinger-Lehrer, Ing. Walter Meischberger and Dkfm. | Walter Guggenberger , Dr. Jörg Haider , Wilfried Tilg and Georg Wurmitzer have renounced their mandates and in their place , Gerhard Reheis , Dr. Liane Höbinger - Lehrer , Ing. Walter Meischberger and Dkfm . | ['Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Last'] | {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: '11', 12: '12', 13: '17', 14: '16', 15: '14', 16: '15', 17: '18', 18: '19', 19: '20', 20: '21', 22: '22', 23: '23', 24: '24', 25: '25', 26: '26', 27: '27', 28: '27', 29: '27', 30: '28', 31: '29', 32: '31', 33: '32', 34: '33', 35: '34', 36: '35'} | {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: '11', 12: '12', 14: '13, 16', 15: '14', 16: '15', 13: '17', 17: '18', 18: '19', 19: '20', 20: '21', 22: '22', 23: '23', 24: '24', 25: '25', 26: '26', 27: '27', 30: '28', 31: '29', 32: '31', 33: '32', 34: '33', 35: '34', 36: '35'} | {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 13, 13: 14, 14: 15, 15: 13, 16: 12, 17: 16, 18: 17, 19: 18, 20: 19, 21: 21, 22: 22, 23: 23, 24: 24, 25: 25, 26: 26, 27: 29, 28: 30, 30: 31, 31: 32, 32: 33, 33: 34, 34: 35} | Walter Guggenberger , Dr. Jörg Haider , Wilfried Tilg and Georg Wurmitzer have renounced their mandates and in their place , Gerhard Reheis , Dr. Liane Höbinger-Lehrer - Lehrer , Ing. Walter Meischberger and Dkfm . | ["No substitution: ('Walter', 'Walter')", "No substitution: ('Guggenberger', 'Guggenberger')", "No substitution: ('Jörg', 'Jörg')", "No substitution: ('Haider', 'Haider')", "No substitution: ('Wilfried', 'Wilfried')", "No substitution: ('Tilg', 'Tilg')", "No substitution: ('Georg', 'Georg')", "No substitution: ('Wurmitzer', 'Wurmitzer')", "No substitution: ('Gerhard', 'Gerhard')", "No substitution: ('Reheis', 'Reheis')", "No substitution: ('Liane', 'Liane')", ('Höbinger', 'Höbinger-Lehrer'), "No substitution: ('Walter', 'Walter')", "No substitution: ('Meischberger', 'Meischberger')"] | [('Höbinger', 'Höbinger-Lehrer')] | {27: 'Höbinger'}    | No       | [['Walter', 1], ['Guggenberger', 2], [',', 3], ['Dr.', 4], ['Jörg', 5], ['Haider', 6], [',', 7], ['Wilfried', 8], ['Tilg', 9], ['und', 10], ['Georg', 11], ['Wurmitzer', 12], ['auf', 13], ['ihre', 14], ['Mandate', 15], ['verzichtet', 16], ['haben', 17], ['und', 18], ['an', 19], ['ihrer', 20], ['Stelle', 21], ['Gerhard', 22], ['Reheis', 23], [',', 24], ['Dr.', 25], ['Liane', 26], ['Höbinger-Lehrer', 27], [',', 28], ['Ing', 29], ['.', 30], ['Walter', 31], ['Meischberger', 32], ['und', 33], ['Dkfm', 34], ['.', 35]] |
NER substitution disabled and original translations are used.

                                                                                                                                                                                                                                                                                                                                                                                                                                                     text  ...                                                                                                                                                                                                                                                                                                                                                                                             post-processed_translations
65952                                                                                                                                                                                                                                                                                                                                                                                                      Nächste Rednerin ist Irene Neumann-Hartberger.  ...                                                                                                                                                                                                                                                                                                                                                                    Next speaker is Irene Neumann - Neumann-Hartberger .
65994                                                                                                                                            Die Reaktionen Österreichs, der EU, der internationalen Staatengemeinschaft waren auf diese Kriegssituationen hin unterschiedlich, auch gegenüber demselben Aggressor – Putin –, denn bereits in Aleppo wurden Tausende Zivilistinnen und Zivilisten durch Putins grausame Spiele getötet und gefährdet.  ...                                                                                                                                                          The reactions of Austria , the EU , the international community of states were different to these war situations , also to the same aggressor – Putin – because thousands of civilians were already killed and threatened by Putins 's cruel games in Aleppo .
66036                                                                                                                                                                                                                                                                                                                                                                                         Herr Abgeordneter Ralph Schallmeinerist der nächste Redner.  ...                                                                                                                                                                                                                                                                                                                                                                                    Mr Ralph Erist is the next speaker .
66070                                                                                                                                                                                                                                                                                                                                                        Da gilt es jetzt, nicht nachzulassen und Long Covid entsprechend mit in den Fokus zu rücken.  ...                                                                                                                                                                                                                                                                                                                                    Now it is important not to let down and put unknown Covid in the focus accordingly .
66126                                                                                                                                                                                                                                                                                                                                                                                             Zu Wort gelangt nun Frau Mag.a Carmen Jeitler-Cincelli.  ...                                                                                                                                                                                                                                                                                                                                                          Mrs Mag.a Carmen Jeitler-cincelli - Cincelli is now speaking .
66132                                                                                                            Ich möchte gleich zu Beginn einen Entschließungsantrag einbringen, den Entschließungsantrag der Abgeordneten Dr. Reinhold Lopatka , Dr. Ewa Ernst-Dziedzic , Dr. Helmut Brandstätter , Kolleginnen und Kollegen betreffend „weitere Solidarität und Unterstützung der Ukraine“, eingebracht im Zuge der Debatte zu Tagesordnungspunkt 1:  ...                                                                                                                         I would like to begin by submitting a motion for a resolution , the motion for a resolution tabled by Mr Reinhold Lopatka , Dr Ewa Ernst-DZIedzic - Dziedzic , Dr Helmut Brandstätter , colleagues on ‘ further solidarity and support for Ukraine ’ , as part of the debate on agenda item 1 :
66158                                                                                                                                                                                                                                                                                                                                                                                                  Ich muss Beate Meinl-Reisinger völlig recht geben:  ...                                                                                                                                                                                                                                                                                                                                                      I have to give Beate Meinl-Reisinger - Reisinger the right thing :
66176                      Jetzt haben wir die Chance, wenn wir alle miteinander, ich erwarte wirklich alle Fraktionen, auch Frau Rendi-Wagner – ich finde diese Instrumentalisierung des Themas nicht gut –, alle Fraktionen an einem Schulterschluss arbeiten, dass wir jetzt eine Sicherheitsarchitektur in Europa aufbauen, dass wir uns zu einer Verteidigungsunion entwickeln, zu einer Sicherheitsunion, an der alle Länder beteiligt sein können.  ...  Now we have the opportunity , if we all work together , I really expect all the political groups , including Mrs Rendi- Rendi-Wagner – I do not think this instrumentalisation of the subject – to work on a close - up of all political groups , that we are now building a security architecture in Europe , that we are developing into a defence union , a security union in which all countries can be involved .
66189                                                                                                                                                                                                                                                                                                                                                                Maksym schaut heute zu, ich habe gesagt, dass ich seine Zeichnungen herzeigen werde.  ...                                                                                                                                                                                                                                                                                                                                                        Maksym watching today , I said I 'm going to show his drawings .
66223                                                                                                                                                                                                                                                                                                                                                                                                    Zu Wort gemeldet ist nun Frau Dr. Susanne Fürst.  ...                                                                                                                                                                                                                                                                                                                                                                 Mrs. Dr. Susanne Fürst has now been reported to speak .
66232  Seine heutige vor einigen Stunden abgegebene Erklärung hat bewiesen, dass sie doch zur Debatte steht, denn bei allem Bekenntnis zur Neutralität, auch jetzt von der Vorrednerin Jeitler-Cincelli, merkt man an den weiteren Ausführungen, dass sie die Neutralität und den Inhalt und den Auftrag der Neutralität nicht verstehen , und dass auch der Bundeskanzler die Rolle und die Aufgabe, die ihm die Neutralität da zuweist, nicht begreift.  ...        Its statement , which was made a few hours ago , has proved that it is still a debate , because , in all its commitment to neutrality , even now by the previous speaker Jeitler-cincelli - Cincelli , it is noted that it does not understand the neutrality and content and the mandate of neutrality , and that the Chancellor also does not understand the role and the task assigned to him by neutrality .
66255                                                                                                                                                                                                                                                                                                                                                                                                         Zu Wort gemeldet ist nun Frau Bedrana Ribo.  ...                                                                                                                                                                                                                                                                                                                                                                      Mrs Bedrana Ribo. has now been reported to speak .
66315                                                                                                                                                                                                                                                                                                                                                                                                     Zu Wort gelangt Frau Abgeordnete Fiona Fiedler.  ...                                                                                                                                                                                                                                                                                                                                                                                   Mrs Fiedler Fionadier came to speak .
66370                                                                                                                                                                                                                                                                                                                                                                                              Frau Abgeordnete Katharina Kucharowitsgelangt zu Wort.  ...                                                                                                                                                                                                                                                                                                                                                                                      Mrs Katharina Kucharowitsgelangt .
66576                                                                                                                                                                                                                                                                                                                                                                                                  Zu Wort gelangt nun Frau Dr.in Ewa Ernst-Dziedzic.  ...                                                                                                                                                                                                                                                                                                                                                              Mrs. Dr.in Ewa Ernst-DZIedzic - Dziedzic is now speaking .
66678                                                                                                                                                                                                                                                                                                                                                 Der Name des russischen Staatspräsidenten Wladimir Putin wird in diesem Zusammenhang nicht erwähnt.  ...                                                                                                                                                                                                                                                                                                                                         The name of Russian President Wladimir Putin is not mentioned in this context .
66692                                                                                                                                                                                                                                                         Schaut her, da sind all die, die selber beim Putin mit waren, einen Vertrag mitunterschrieben haben und dann, als Putin mit der ehemaligen FPÖ-Außenministerin aufgetanzt hat, dabei waren.  ...                                                                                                                                                                                                                                                  Look , there are all those who were with the uknown themselves signed a contract and then , when Putin danced with the former FPÖ foreign minister , they were there .
66724                                                                                                                                                                                                                                                                                                                                                                                                                               Herr Dr. Martin Graf.  ...                                                                                                                                                                                                                                                                                                                                                                                                      Dr. Martin Graf. .
66811                                                                                                                                                                                                Wir gelangen nunmehr zur Abstimmung über den Entschließungsantrag der Abgeordneten Dr. Reinhold Lopatka, Dr.in Ewa Ernst-Dziedzic, Dr. Helmut Brandstätter, Kolleginnen und Kollegen betreffend „weitere Solidarität und Unterstützung der Ukraine“.  ...                                                                                                                                                                                                          We are now voting on the motion for a resolution tabled by Mr Reinhold Lopatka , Dr.in Ewa Ernst-DZIedzic - Dziedzic , Dr Helmut Brandstätter , colleagues on ‘ further solidarity and support for Ukraine ’ .
66818                                                                                                                                                                                                          Wir gelangen zur Abstimmung über den Entschließungsantrag der Abgeordneten Katharina Kucharowits, Kolleginnen und Kollegen betreffend „humanitäre Hilfe für die Bevölkerung in der Ukraine und Aufnahme von Flüchtlingen aus der Ukraine“.  ...                                                                                                                                                                                                                            We shall vote on the motion for a resolution tabled by Mrs Katharina Kucharowits , colleagues on ' humanitarian aid for the people of Ukraine and the reception of refugees from Ukraine ' .

[20 rows x 3 columns]2023-08-22 12:14:12 WARNING: Can not find mwt: default from official model list. Ignoring it.
2023-08-22 12:14:13 INFO: Loading these models for language: en (English):
========================
| Processor | Package  |
------------------------
| tokenize  | combined |
| pos       | combined |
| lemma     | combined |
| ner       | conll03  |
========================

2023-08-22 12:14:13 INFO: Use device: gpu
2023-08-22 12:14:13 INFO: Loading: tokenize
2023-08-22 12:14:13 INFO: Loading: pos
2023-08-22 12:14:13 INFO: Loading: lemma
2023-08-22 12:14:13 INFO: Loading: ner
2023-08-22 12:14:14 INFO: Done loading processors!

Processing started.
ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/1999/ParlaMint-AT_1999-04-21-020-XX-NRSITZ-00165.conllu is saved.
Current running time: 0.73
ParlaMint-AT_2022-06-15-027-XXVII-NRSITZ-00163.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-06-15-027-XXVII-NRSITZ-00163.conllu is saved.
Current running time: 0.75
ParlaMint-AT_2022-02-23-027-XXVII-NRSITZ-00142.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-02-23-027-XXVII-NRSITZ-00142.conllu is saved.
Current running time: 0.78
ParlaMint-AT_2022-06-15-027-XXVII-NRSITZ-00164.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-06-15-027-XXVII-NRSITZ-00164.conllu is saved.
Current running time: 0.8
ParlaMint-AT_2022-10-03-027-XXVII-NRSITZ-00174.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-10-03-027-XXVII-NRSITZ-00174.conllu is saved.
Current running time: 1.05
ParlaMint-AT_2022-03-24-027-XXVII-NRSITZ-00150.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-03-24-027-XXVII-NRSITZ-00150.conllu is saved.
Current running time: 1.08
ParlaMint-AT_2022-10-04-027-XXVII-NRSITZ-00176.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-10-04-027-XXVII-NRSITZ-00176.conllu is saved.
Current running time: 1.26
ParlaMint-AT_2022-07-08-027-XXVII-NRSITZ-00169.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-07-08-027-XXVII-NRSITZ-00169.conllu is saved.
Current running time: 1.91
ParlaMint-AT_2022-06-15-027-XXVII-NRSITZ-00162.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-06-15-027-XXVII-NRSITZ-00162.conllu is saved.
Current running time: 2.71
ParlaMint-AT_2022-06-14-027-XXVII-NRSITZ-00160.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-06-14-027-XXVII-NRSITZ-00160.conllu is saved.
Current running time: 3.25
ParlaMint-AT_2022-10-12-027-XXVII-NRSITZ-00178.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-10-12-027-XXVII-NRSITZ-00178.conllu is saved.
Current running time: 3.91
ParlaMint-AT_2022-07-08-027-XXVII-NRSITZ-00170.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-07-08-027-XXVII-NRSITZ-00170.conllu is saved.
Current running time: 3.94
ParlaMint-AT_2022-10-03-027-XXVII-NRSITZ-00175.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-10-03-027-XXVII-NRSITZ-00175.conllu is saved.
Current running time: 3.97
ParlaMint-AT_2022-09-21-027-XXVII-NRSITZ-00173.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-09-21-027-XXVII-NRSITZ-00173.conllu is saved.
Current running time: 3.99
ParlaMint-AT_2022-09-21-027-XXVII-NRSITZ-00171.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-09-21-027-XXVII-NRSITZ-00171.conllu is saved.
Current running time: 4.7
ParlaMint-AT_2022-10-04-027-XXVII-NRSITZ-00177.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-10-04-027-XXVII-NRSITZ-00177.conllu is saved.
Current running time: 4.72
ParlaMint-AT_2022-09-21-027-XXVII-NRSITZ-00172.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-09-21-027-XXVII-NRSITZ-00172.conllu is saved.
Current running time: 4.75
ParlaMint-AT_2022-03-08-027-XXVII-NRSITZ-00146.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-03-08-027-XXVII-NRSITZ-00146.conllu is saved.
Current running time: 4.77
ParlaMint-AT_2022-06-14-027-XXVII-NRSITZ-00161.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-06-14-027-XXVII-NRSITZ-00161.conllu is saved.
Current running time: 4.8
ParlaMint-AT_2022-07-07-027-XXVII-NRSITZ-00168.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-07-07-027-XXVII-NRSITZ-00168.conllu is saved.
Current running time: 5.56
ParlaMint-AT_2022-06-23-027-XXVII-NRSITZ-00166.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-06-23-027-XXVII-NRSITZ-00166.conllu is saved.
Current running time: 5.59
ParlaMint-AT_2022-06-23-027-XXVII-NRSITZ-00165.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-06-23-027-XXVII-NRSITZ-00165.conllu is saved.
Current running time: 5.93
ParlaMint-AT_2022-07-06-027-XXVII-NRSITZ-00167.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-07-06-027-XXVII-NRSITZ-00167.conllu is saved.
Current running time: 6.72
ParlaMint-AT_2022-03-24-027-XXVII-NRSITZ-00149.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-03-24-027-XXVII-NRSITZ-00149.conllu is saved.
Current running time: 7.34
ParlaMint-AT_2022-03-08-027-XXVII-NRSITZ-00145.conllu processed and saved.
Final file /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2022/ParlaMint-AT_2022-03-08-027-XXVII-NRSITZ-00145.conllu is saved.
Current running time: 7.64
Processing completed. It took 7.64 minutes.
