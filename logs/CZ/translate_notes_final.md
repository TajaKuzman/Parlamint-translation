2023-05-12 12:23:50.207371: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-05-12 12:23:50.967103: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-05-12 12:23:50.967174: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-05-12 12:23:50.967180: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Extraction of the notes and translation started.
No. of files: 6328.
Statistics before droping duplicates:



|        | tag    | type    | content                         | xml:lang   |
|:-------|:-------|:--------|:--------------------------------|:-----------|
| count  | 255506 | 255506  | 255506                          | 255506     |
| unique | 5      | 15      | 20031                           | 1          |
| top    | note   | speaker | Místopředseda PSP Vojtěch Filip | cs         |
| freq   | 223783 | 181310  | 18742                           | 255506     |


|    | tag   | type    | content                                  | xml:lang   |
|---:|:------|:--------|:-----------------------------------------|:-----------|
|  0 | note  | speaker | Místopředsedkyně PSP Jaroslava Jermanová | cs         |
|  1 | note  | speaker | Poslanec Martin Kolovratník              | cs         |
|  2 | note  | time    | (11.50 hodin)                            | cs         |
|  3 | note  | speaker | Místopředsedkyně PSP Jaroslava Jermanová | cs         |
|  4 | note  | speaker | Poslanec Martin Kolovratník              | cs         |


Statistics for tags:

|          |    tag |
|:---------|-------:|
| note     | 223783 |
| vocal    |  18129 |
| kinesic  |  12404 |
| gap      |   1021 |
| incident |    169 |


|                          |   type |
|:-------------------------|-------:|
| ('gap', 'inaudible')     |   1021 |
| ('incident', 'entering') |     73 |
| ('incident', 'leaving')  |     59 |
| ('incident', 'break')    |     32 |
| ('incident', 'sound')    |      5 |
| ('kinesic', 'applause')  |   8713 |
| ('kinesic', 'gesture')   |   2936 |
| ('kinesic', 'signal')    |    398 |
| ('kinesic', 'kinesic')   |    188 |
| ('kinesic', 'noise')     |    169 |
| ('note', 'speaker')      | 181310 |
| ('note', 'time')         |  27640 |
| ('note', 'comment')      |  14833 |
| ('vocal', 'speaking')    |  10870 |
| ('vocal', 'noise')       |   5691 |
| ('vocal', 'laughter')    |   1568 |
Most common notes:

|                                          |   content |
|:-----------------------------------------|----------:|
| Místopředseda PSP Vojtěch Filip          |     18742 |
| Místopředseda PSP Petr Gazdík            |      9849 |
| Místopředseda PSP Jan Bartošek           |      9826 |
| Místopředseda PSP Tomio Okamura          |      7966 |
| Místopředseda PSP Vojtěch Pikal          |      7932 |
| Místopředseda PSP Petr Fiala             |      7505 |
| Předseda PSP Radek Vondráček             |      7319 |
| Předseda PSP Jan Hamáček                 |      6591 |
| Místopředseda PSP Tomáš Hanzel           |      5261 |
| Místopředsedkyně PSP Jaroslava Jermanová |      5118 |
| Poslanec Zbyněk Stanjura                 |      3452 |
| Poslanec Miroslav Kalousek               |      2467 |
| Poslanec Martin Kolovratník              |      2094 |
| Místopředseda PSP Radek Vondráček        |      1699 |
| Místopředseda PSP Jan Skopeček           |      1486 |
| (Nesouhlasné.)                           |      1484 |
| Poslanec Jan Volný                       |      1338 |
| Místopředsedkyně PSP Věra Kovářová       |      1209 |
| (Nesouhlas.)                             |      1203 |
| Předsedkyně PSP Markéta Pekarová Adamová |      1177 |
Statistics after deduplication:

Number of words in the notes: 110907

|        | tag   | type    | content                                  | xml:lang   |      length |
|:-------|:------|:--------|:-----------------------------------------|:-----------|------------:|
| count  | 20031 | 20031   | 20031                                    | 20031      | 20031       |
| unique | 5     | 15      | 20031                                    | 1          |   nan       |
| top    | note  | comment | Místopředsedkyně PSP Jaroslava Jermanová | cs         |   nan       |
| freq   | 11842 | 9251    | 1                                        | 20031      |   nan       |
| mean   | nan   | nan     | nan                                      | nan        |     5.53677 |
| std    | nan   | nan     | nan                                      | nan        |     5.41548 |
| min    | nan   | nan     | nan                                      | nan        |     1       |
| 25%    | nan   | nan     | nan                                      | nan        |     3       |
| 50%    | nan   | nan     | nan                                      | nan        |     5       |
| 75%    | nan   | nan     | nan                                      | nan        |     7       |
| max    | nan   | nan     | nan                                      | nan        |   214       |


|    | tag   | type    | content                                  | xml:lang   |   length |
|---:|:------|:--------|:-----------------------------------------|:-----------|---------:|
|  0 | note  | speaker | Místopředsedkyně PSP Jaroslava Jermanová | cs         |        4 |
|  1 | note  | speaker | Poslanec Martin Kolovratník              | cs         |        3 |
|  2 | note  | time    | (11.50 hodin)                            | cs         |        2 |
|  6 | note  | comment | (proti nikdo)                            | cs         |        2 |
|  7 | note  | speaker | Místopředseda PSP Vojtěch Filip          | cs         |        4 |


Statistics for tags:

|          |   tag |
|:---------|------:|
| note     | 11842 |
| vocal    |  4928 |
| kinesic  |  3026 |
| incident |   164 |
| gap      |    71 |


|                          |   type |
|:-------------------------|-------:|
| ('gap', 'inaudible')     |     71 |
| ('incident', 'entering') |     70 |
| ('incident', 'leaving')  |     58 |
| ('incident', 'break')    |     31 |
| ('incident', 'sound')    |      5 |
| ('kinesic', 'applause')  |   1756 |
| ('kinesic', 'gesture')   |    944 |
| ('kinesic', 'kinesic')   |    175 |
| ('kinesic', 'noise')     |     79 |
| ('kinesic', 'signal')    |     72 |
| ('note', 'comment')      |   9251 |
| ('note', 'time')         |   1928 |
| ('note', 'speaker')      |    663 |
| ('vocal', 'speaking')    |   2993 |
| ('vocal', 'noise')       |   1523 |
| ('vocal', 'laughter')    |    412 |
Translation started.
Translation completed. It took 11.89 minutes for 20031 instances for the entire process of extraction and translation.

|    | tag   | type    | content                                  | xml:lang   |   length | translation                                   | corpus   |
|---:|:------|:--------|:-----------------------------------------|:-----------|---------:|:----------------------------------------------|:---------|
|  0 | note  | speaker | Místopředsedkyně PSP Jaroslava Jermanová | cs         |        4 | Vice-President of the PSP Jaroslava Jermanová | CZ       |
|  1 | note  | speaker | Poslanec Martin Kolovratník              | cs         |        3 | Member Martin Kolohradík                      | CZ       |
|  2 | note  | time    | (11.50 hodin)                            | cs         |        2 | (11.50 hours)                                 | CZ       |
|  6 | note  | comment | (proti nikdo)                            | cs         |        2 | (against no one)                              | CZ       |
|  7 | note  | speaker | Místopředseda PSP Vojtěch Filip          | cs         |        4 | Vice-President of the PSP Vojtěch Filip       | CZ       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-CZ.notes.translated.tsv
