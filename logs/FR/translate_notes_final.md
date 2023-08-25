2023-05-15 09:07:20.027072: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-05-15 09:07:20.771914: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-05-15 09:07:20.771980: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-05-15 09:07:20.771986: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Extraction of the notes and translation started.
No. of files: 1564.
Statistics before droping duplicates:



|        | tag     | type     | content           | xml:lang   |
|:-------|:--------|:---------|:------------------|:-----------|
| count  | 135377  | 135377   | 135377            | 135377     |
| unique | 5       | 10       | 25161             | 1          |
| top    | kinesic | applause | DISC_ARTICLES_2_4 | fr         |
| freq   | 69105   | 61682    | 8209              | 135377     |


|    | tag   | type   | content                             | xml:lang   |
|---:|:------|:-------|:------------------------------------|:-----------|
|  0 | note  | debate | APPEL_PLF_1_20                      | fr         |
|  1 | note  | debate | TITRE_TEXTE_DISCUSSION              | fr         |
|  2 | note  | debate | APPEL_PLF_1_20                      | fr         |
|  3 | note  | debate | FIN_SEAN_1_2                        | fr         |
|  4 | head  |        | Projet de loi de finances pour 2018 | fr         |


Statistics for tags:

|          |   tag |
|:---------|------:|
| kinesic  | 69105 |
| note     | 22126 |
| head     | 22123 |
| vocal    | 14518 |
| incident |  7505 |


|                          |   type |
|:-------------------------|-------:|
| ('head', '')             |  22123 |
| ('incident', 'incident') |   4809 |
| ('incident', 'action')   |   2696 |
| ('kinesic', 'applause')  |  61682 |
| ('kinesic', 'smiling')   |   7423 |
| ('note', 'debate')       |  22126 |
| ('vocal', 'exclamat')    |  10473 |
| ('vocal', 'speaking')    |   2567 |
| ('vocal', 'laughter')    |    978 |
| ('vocal', 'murmuring')   |    500 |
Most common notes:

|                                                           |   content |
|:----------------------------------------------------------|----------:|
| DISC_ARTICLES_2_4                                         |      8209 |
| Sourires                                                  |      6677 |
| Applaudissements sur les bancs du groupe LR               |      3897 |
| Applaudissements sur les bancs du groupe LaREM            |      3769 |
| QG_1_1                                                    |      3743 |
| Applaudissements sur plusieurs bancs du groupe LaREM      |      2844 |
| Applaudissements sur quelques bancs du groupe LaREM       |      2837 |
| Applaudissements sur les bancs du groupe FI               |      2722 |
| Mêmes mouvements                                          |      2256 |
| Exclamations sur les bancs du groupe LR                   |      2120 |
| Applaudissements sur les bancs des groupes LaREM et MODEM |      1932 |
| FIN_SEAN_1_2                                              |      1552 |
| Ordre du jour de la prochaine séance                      |      1549 |
| Exclamations sur les bancs du groupe LaREM                |      1418 |
| TITRE_TEXTE_DISCUSSION                                    |      1302 |
| QOSD_1_1                                                  |      1254 |
| SOUS_TITRE_TEXTE_DISCUSSION                               |      1182 |
| Applaudissements sur les bancs du groupe REM              |       999 |
| Applaudissements sur les bancs des groupes REM et MODEM   |       842 |
| Applaudissements sur plusieurs bancs du groupe LR         |       832 |
Statistics after deduplication:

Number of words in the notes: 274839

|        | tag     | type     | content        | xml:lang   |      length |
|:-------|:--------|:---------|:---------------|:-----------|------------:|
| count  | 25161   | 25161    | 25161          | 25161      | 25161       |
| unique | 5       | 10       | 25161          | 1          |   nan       |
| top    | kinesic | applause | APPEL_PLF_1_20 | fr         |   nan       |
| freq   | 13987   | 13738    | 1              | 25161      |   nan       |
| mean   | nan     | nan      | nan            | nan        |    10.9232  |
| std    | nan     | nan      | nan            | nan        |     6.39316 |
| min    | nan     | nan      | nan            | nan        |     1       |
| 25%    | nan     | nan      | nan            | nan        |     5       |
| 50%    | nan     | nan      | nan            | nan        |    10       |
| 75%    | nan     | nan      | nan            | nan        |    16       |
| max    | nan     | nan      | nan            | nan        |    73       |


|    | tag   | type   | content                                | xml:lang   |   length |
|---:|:------|:-------|:---------------------------------------|:-----------|---------:|
|  0 | note  | debate | APPEL_PLF_1_20                         | fr         |        1 |
|  1 | note  | debate | TITRE_TEXTE_DISCUSSION                 | fr         |        1 |
|  3 | note  | debate | FIN_SEAN_1_2                           | fr         |        1 |
|  4 | head  |        | Projet de loi de finances pour 2018    | fr         |        7 |
|  5 | head  |        | Annulation de l’élection d’une députée | fr         |        5 |


Statistics for tags:

|          |   tag |
|:---------|------:|
| kinesic  | 13987 |
| head     |  6254 |
| vocal    |  2738 |
| incident |  2113 |
| note     |    69 |


|                          |   type |
|:-------------------------|-------:|
| ('head', '')             |   6254 |
| ('incident', 'incident') |   1985 |
| ('incident', 'action')   |    128 |
| ('kinesic', 'applause')  |  13738 |
| ('kinesic', 'smiling')   |    249 |
| ('note', 'debate')       |     69 |
| ('vocal', 'speaking')    |   1272 |
| ('vocal', 'exclamat')    |   1247 |
| ('vocal', 'laughter')    |    118 |
| ('vocal', 'murmuring')   |    101 |
Translation started.
Translation completed. It took 12.39 minutes for 25161 instances for the entire process of extraction and translation.
|    | tag   | type   | content                                | xml:lang   |   length | translation                                         | corpus   |
|---:|:------|:-------|:---------------------------------------|:-----------|---------:|:----------------------------------------------------|:---------|
|  0 | note  | debate | APPEL_PLF_1_20                         | fr         |        1 | APPEAL_PLF_1_20                                     | FR       |
|  1 | note  | debate | TITRE_TEXTE_DISCUSSION                 | fr         |        1 | TITLE_TEXT_DISCUSSION                               | FR       |
|  3 | note  | debate | FIN_SEAN_1_2                           | fr         |        1 | FIN_SEAN_1_2                                        | FR       |
|  4 | head  |        | Projet de loi de finances pour 2018    | fr         |        7 | 2018 Finance Bill                                   | FR       |
|  5 | head  |        | Annulation de l’élection d’une députée | fr         |        5 | Annulment of the election of a Member of Parliament | FR       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-FR.notes.translated.tsv
