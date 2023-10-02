2023-09-05 13:36:55.056465: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-09-05 13:36:55.765311: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-09-05 13:36:55.765378: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-09-05 13:36:55.765384: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Extraction of the notes and translation started.
No. of files: 6832.
Statistics before dropping duplicates:



|        | tag    | type    | content                         | xml:lang   |
|:-------|:-------|:--------|:--------------------------------|:-----------|
| count  | 277549 | 277549  | 277549                          | 277549     |
| unique | 5      | 15      | 21672                           | 1          |
| top    | note   | speaker | Místopředseda PSP Vojtěch Filip | cs         |
| freq   | 243108 | 196185  | 18674                           | 277549     |


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
| note     | 243108 |
| vocal    |  19550 |
| kinesic  |  13625 |
| gap      |   1086 |
| incident |    180 |


|                          |   type |
|:-------------------------|-------:|
| ('gap', 'inaudible')     |   1086 |
| ('incident', 'entering') |     77 |
| ('incident', 'leaving')  |     61 |
| ('incident', 'break')    |     37 |
| ('incident', 'sound')    |      5 |
| ('kinesic', 'applause')  |   9649 |
| ('kinesic', 'gesture')   |   3195 |
| ('kinesic', 'signal')    |    385 |
| ('kinesic', 'kinesic')   |    215 |
| ('kinesic', 'noise')     |    181 |
| ('note', 'speaker')      | 196185 |
| ('note', 'time')         |  30301 |
| ('note', 'comment')      |  16622 |
| ('vocal', 'speaking')    |  11775 |
| ('vocal', 'noise')       |   6032 |
| ('vocal', 'laughter')    |   1743 |
Most common notes:

|                                          |   content |
|:-----------------------------------------|----------:|
| Místopředseda PSP Vojtěch Filip          |     18674 |
| Místopředseda PSP Jan Bartošek           |     11054 |
| Místopředseda PSP Petr Gazdík            |      9859 |
| Místopředseda PSP Vojtěch Pikal          |      7869 |
| Místopředseda PSP Tomio Okamura          |      7794 |
| Místopředseda PSP Petr Fiala             |      7418 |
| Předseda PSP Radek Vondráček             |      7156 |
| Předseda PSP Jan Hamáček                 |      6605 |
| Místopředseda PSP Tomáš Hanzel           |      5133 |
| Místopředsedkyně PSP Jaroslava Jermanová |      5125 |
| Poslanec Zbyněk Stanjura                 |      3442 |
| Místopředsedkyně PSP Věra Kovářová       |      2817 |
| Místopředseda PSP Karel Havlíček         |      2509 |
| Místopředseda PSP Jan Skopeček           |      2479 |
| Místopředsedkyně PSP Olga Richterová     |      2477 |
| Poslanec Miroslav Kalousek               |      2462 |
| Poslanec Martin Kolovratník              |      2290 |
| Předsedkyně PSP Markéta Pekarová Adamová |      1991 |
| Místopředseda PSP Radek Vondráček        |      1700 |
| Nesouhlasné.                             |      1477 |
Statistics after deduplication:

Number of words in the notes: 118525

|        | tag   | type    | content                                  | xml:lang   |      length |
|:-------|:------|:--------|:-----------------------------------------|:-----------|------------:|
| count  | 21672 | 21672   | 21672                                    | 21672      | 21672       |
| unique | 5     | 15      | 21672                                    | 1          |   nan       |
| top    | note  | comment | Místopředsedkyně PSP Jaroslava Jermanová | cs         |   nan       |
| freq   | 12835 | 10129   | 1                                        | 21672      |   nan       |
| mean   | nan   | nan     | nan                                      | nan        |     5.46904 |
| std    | nan   | nan     | nan                                      | nan        |     4.22287 |
| min    | nan   | nan     | nan                                      | nan        |     1       |
| 25%    | nan   | nan     | nan                                      | nan        |     3       |
| 50%    | nan   | nan     | nan                                      | nan        |     5       |
| 75%    | nan   | nan     | nan                                      | nan        |     7       |
| max    | nan   | nan     | nan                                      | nan        |   164       |


|    | tag   | type    | content                                  | xml:lang   |   length |
|---:|:------|:--------|:-----------------------------------------|:-----------|---------:|
|  0 | note  | speaker | Místopředsedkyně PSP Jaroslava Jermanová | cs         |        4 |
|  1 | note  | speaker | Poslanec Martin Kolovratník              | cs         |        3 |
|  2 | note  | time    | (11.50 hodin)                            | cs         |        2 |
|  6 | note  | comment | proti nikdo                              | cs         |        2 |
|  7 | note  | speaker | Místopředseda PSP Vojtěch Filip          | cs         |        4 |


Statistics for tags:

|          |   tag |
|:---------|------:|
| note     | 12835 |
| vocal    |  5306 |
| kinesic  |  3286 |
| incident |   173 |
| gap      |    72 |


|                          |   type |
|:-------------------------|-------:|
| ('gap', 'inaudible')     |     72 |
| ('incident', 'entering') |     73 |
| ('incident', 'leaving')  |     60 |
| ('incident', 'break')    |     35 |
| ('incident', 'sound')    |      5 |
| ('kinesic', 'applause')  |   1862 |
| ('kinesic', 'gesture')   |   1067 |
| ('kinesic', 'kinesic')   |    200 |
| ('kinesic', 'noise')     |     83 |
| ('kinesic', 'signal')    |     74 |
| ('note', 'comment')      |  10129 |
| ('note', 'time')         |   2022 |
| ('note', 'speaker')      |    684 |
| ('vocal', 'speaking')    |   3277 |
| ('vocal', 'noise')       |   1580 |
| ('vocal', 'laughter')    |    449 |
Translation started.
Translation completed. It took 14.74 minutes for 21672 instances for the entire process of extraction and translation.
|    | tag   | type    | content                                  | xml:lang   |   length | translation                                   | corpus   |
|---:|:------|:--------|:-----------------------------------------|:-----------|---------:|:----------------------------------------------|:---------|
|  0 | note  | speaker | Místopředsedkyně PSP Jaroslava Jermanová | cs         |        4 | Vice-President of the PSP Jaroslava Jermanová | CZ       |
|  1 | note  | speaker | Poslanec Martin Kolovratník              | cs         |        3 | Member Martin Kolohradík                      | CZ       |
|  2 | note  | time    | (11.50 hodin)                            | cs         |        2 | (11.50 hours)                                 | CZ       |
|  6 | note  | comment | proti nikdo                              | cs         |        2 | against no one                                | CZ       |
|  7 | note  | speaker | Místopředseda PSP Vojtěch Filip          | cs         |        4 | Vice-President of the PSP Vojtěch Filip       | CZ       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-CZ.notes.translated.tsv
