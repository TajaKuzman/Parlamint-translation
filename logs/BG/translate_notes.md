2023-03-14 08:49:11.459150: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-03-14 08:49:12.093148: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-03-14 08:49:12.093213: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-03-14 08:49:12.093220: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
Extraction of the notes and translation started.
No. of files: 921.
Statistics before droping duplicates:



|        | tag   | type         | content          | xml:lang   |
|:-------|:------|:-------------|:-----------------|:-----------|
| count  | 51652 | 51652        | 51652            | 51652      |
| unique | 3     | 17           | 11697            | 1          |
| top    | vocal | interruption | (Шум и реплики.) |            |
| freq   | 32153 | 23728        | 4881             | 51652      |


|    | tag     | type     | content                               | xml:lang   |
|---:|:--------|:---------|:--------------------------------------|:-----------|
|  0 | kinesic | ringing  | (Звъни.)                              |            |
|  1 | kinesic | applause | (Единични ръкопляскания от ДПС.)      |            |
|  2 | kinesic | applause | (Ръкопляскания.)                      |            |
|  3 | kinesic | kinesic  | (Показва.)                            |            |
|  4 | kinesic | applause | (Ръкопляскания от „БСП за България“.) |            |


Statistics for tags:

|          |   tag |
|:---------|------:|
| vocal    | 32153 |
| kinesic  | 17930 |
| incident |  1569 |


|                           |   type |
|:--------------------------|-------:|
| ('incident', 'action')    |    720 |
| ('incident', 'incident')  |    373 |
| ('incident', 'break')     |    231 |
| ('incident', 'leaving')   |    164 |
| ('incident', 'entering')  |     81 |
| ('kinesic', 'applause')   |  12621 |
| ('kinesic', 'signal')     |   2647 |
| ('kinesic', 'ringing')    |   1538 |
| ('kinesic', 'kinesic')    |   1124 |
| ('vocal', 'interruption') |  23728 |
| ('vocal', 'noise')        |   3259 |
| ('vocal', 'exclamat')     |   2121 |
| ('vocal', 'laughter')     |   1737 |
| ('vocal', 'speaking')     |    820 |
| ('vocal', 'question')     |    231 |
| ('vocal', 'shouting')     |    222 |
| ('vocal', 'greeting')     |     35 |
Most common notes:

|                                                    |   content |
|:---------------------------------------------------|----------:|
| (Шум и реплики.)                                   |      4881 |
| (Ръкопляскания от „БСП за България“.)              |      2149 |
| (Реплики.)                                         |      1950 |
| (Председателят дава сигнал, че времето е изтекло.) |      1759 |
| (Ръкопляскания от ГЕРБ.)                           |      1689 |
| (Звъни.)                                           |      1532 |
| (Ръкопляскания от ГЕРБ-СДС.)                       |      1134 |
| (Ръкопляскания.)                                   |       981 |
| (Ръкопляскания от ДПС.)                            |       954 |
| (Шум и реплики от ГЕРБ.)                           |       944 |
| (Ръкопляскания от „Продължаваме Промяната“.)       |       761 |
| (Шум и реплики от „БСП за България“.)              |       701 |
| (Реплики от „БСП за България“.)                    |       641 |
| (Оживление.)                                       |       634 |
| (Реплики от ГЕРБ.)                                 |       623 |
| (Шум и реплики от ГЕРБ-СДС.)                       |       491 |
| (председателят дава сигнал, че времето е изтекло)  |       477 |
| (Силен шум и реплики.)                             |       476 |
| (Ръкопляскания от БСП ЛБ.)                         |       407 |
| (Ръкопляскания от ГЕРБ и ОП.)                      |       298 |
Statistics after deduplication:

Number of words in the notes: 91174

|        | tag   | type         | content                                                                                      | xml:lang   |      length |
|:-------|:------|:-------------|:---------------------------------------------------------------------------------------------|:-----------|------------:|
| count  | 11986 | 11986        | 11986                                                                                        | 11986      | 11986       |
| unique | 3     | 17           | 11697                                                                                        | 1          |   nan       |
| top    | vocal | interruption | (Председателят изключва микрофоните. Ораторът продължава да говори при изключени микрофони.) |            |   nan       |
| freq   | 9387  | 5688         | 3                                                                                            | 11986      |   nan       |
| mean   | nan   | nan          | nan                                                                                          | nan        |     7.60671 |
| std    | nan   | nan          | nan                                                                                          | nan        |     4.04326 |
| min    | nan   | nan          | nan                                                                                          | nan        |     1       |
| 25%    | nan   | nan          | nan                                                                                          | nan        |     5       |
| 50%    | nan   | nan          | nan                                                                                          | nan        |     7       |
| 75%    | nan   | nan          | nan                                                                                          | nan        |     9       |
| max    | nan   | nan          | nan                                                                                          | nan        |    74       |


|    | tag     | type     | content                               | xml:lang   |   length |
|---:|:--------|:---------|:--------------------------------------|:-----------|---------:|
|  0 | kinesic | ringing  | (Звъни.)                              |            |        1 |
|  1 | kinesic | applause | (Единични ръкопляскания от ДПС.)      |            |        4 |
|  2 | kinesic | applause | (Ръкопляскания.)                      |            |        1 |
|  3 | kinesic | kinesic  | (Показва.)                            |            |        1 |
|  4 | kinesic | applause | (Ръкопляскания от „БСП за България“.) |            |        5 |


Statistics for tags:

|          |   tag |
|:---------|------:|
| vocal    |  9387 |
| kinesic  |  1619 |
| incident |   980 |


|                           |   type |
|:--------------------------|-------:|
| ('incident', 'action')    |    465 |
| ('incident', 'incident')  |    286 |
| ('incident', 'leaving')   |    148 |
| ('incident', 'entering')  |     76 |
| ('incident', 'break')     |      5 |
| ('kinesic', 'applause')   |    959 |
| ('kinesic', 'kinesic')    |    331 |
| ('kinesic', 'signal')     |    320 |
| ('kinesic', 'ringing')    |      9 |
| ('vocal', 'interruption') |   5688 |
| ('vocal', 'exclamat')     |   1518 |
| ('vocal', 'noise')        |    924 |
| ('vocal', 'speaking')     |    573 |
| ('vocal', 'laughter')     |    447 |
| ('vocal', 'shouting')     |    173 |
| ('vocal', 'greeting')     |     34 |
| ('vocal', 'question')     |     30 |
Translation started.
Translation completed. It took 22.83 minutes for 11986 instances for the entire process of extraction and translation.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
|    | tag     | type     | content                               | xml:lang   |   length | translation                       |
|---:|:--------|:---------|:--------------------------------------|:-----------|---------:|:----------------------------------|
|  0 | kinesic | ringing  | (Звъни.)                              |            |        1 | (PHONE RINGING)                   |
|  1 | kinesic | applause | (Единични ръкопляскания от ДПС.)      |            |        4 | (Single applause from DPS.)       |
|  2 | kinesic | applause | (Ръкопляскания.)                      |            |        1 | (Applause.)                       |
|  3 | kinesic | kinesic  | (Показва.)                            |            |        1 | (Shows.)                          |
|  4 | kinesic | applause | (Ръкопляскания от „БСП за България“.) |            |        5 | (Applause from BSP for Bulgaria.) |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-BG.notes.translated.csv
