2023-05-12 12:07:23.638438: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-05-12 12:07:24.356023: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-05-12 12:07:24.356089: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-05-12 12:07:24.356096: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Extraction of the notes and translation started.
No. of files: 1572.
Statistics before droping duplicates:



|        | tag    | type    | content   | xml:lang   |
|:-------|:-------|:--------|:----------|:-----------|
| count  | 439762 | 439762  | 439762    | 439762     |
| unique | 6      | 22      | 9955      | 1          |
| top    | note   | speaker | ...       | sl         |
| freq   | 392734 | 311372  | 25004     | 439762     |


|    | tag   | type    | content                       | xml:lang   |
|---:|:------|:--------|:------------------------------|:-----------|
|  0 | note  | time    | Seja se je začela ob 12. uri. | sl         |
|  1 | note  | speaker | PREDSEDNIK JANKO VEBER:       | sl         |
|  2 | note  |         | Za je glasovalo 56.           | sl         |
|  3 | note  |         | Proti 1.                      | sl         |
|  4 | note  |         | Za je glasovalo 56.           | sl         |


Statistics for tags:

|          |    tag |
|:---------|-------:|
| note     | 392734 |
| gap      |  38654 |
| head     |   4706 |
| vocal    |   2725 |
| kinesic  |    903 |
| incident |     40 |


|                           |   type |
|:--------------------------|-------:|
| ('gap', 'inaudible')      |  38647 |
| ('gap', 'editorial')      |      7 |
| ('head', '')              |   1570 |
| ('head', 'session')       |   1569 |
| ('head', 'chairman')      |   1567 |
| ('incident', 'sound')     |     21 |
| ('incident', 'action')    |     19 |
| ('kinesic', 'signal')     |    672 |
| ('kinesic', 'gesture')    |    122 |
| ('kinesic', 'applause')   |     95 |
| ('kinesic', 'snapping')   |     12 |
| ('kinesic', 'playback')   |      2 |
| ('note', 'speaker')       | 311372 |
| ('note', '')              |  63680 |
| ('note', 'vote-ayes')     |   5771 |
| ('note', 'vote-noes')     |   5737 |
| ('note', 'time')          |   5127 |
| ('note', 'answer')        |    802 |
| ('note', 'error')         |    234 |
| ('note', 'description')   |      9 |
| ('note', 'vote')          |      2 |
| ('vocal', 'interruption') |   2608 |
| ('vocal', 'laughter')     |    117 |
Most common notes:

|                                     |   content |
|:------------------------------------|----------:|
| ...                                 |     25004 |
| PODPREDSEDNIK MAG. VASJA KLAVORA:   |     13302 |
| PREDSEDNIK DR. MILAN BRGLEZ:        |     12003 |
| PREDSEDNIK FRANCE CUKJATI:          |     11013 |
| PREDSEDNIK DR. PAVEL GANTAR:        |     10280 |
| PODPREDSEDNICA IRMA PAVLINIČ KREBS: |     10006 |
| …                                   |      9936 |
| PREDSEDNIK BORUT PAHOR:             |      9348 |
| Proti nihče.                        |      8549 |
| PODPREDSEDNIK SAŠO PEČE:            |      7960 |
| PODPREDSEDNIK PRIMOŽ HAINZ:         |      7073 |
| PODPREDSEDNIK JOŽE TANKO:           |      6012 |
| PODPREDSEDNIK BRANKO SIMONOVIČ:     |      5722 |
| PODPREDSEDNIK MIRAN POTRČ:          |      5657 |
| PODPREDSEDNICA TINA HEFERLE:        |      5406 |
| PREDSEDNIK IGOR ZORČIČ:             |      5363 |
| PREDSEDNIK JANKO VEBER:             |      4625 |
| PODPREDSEDNIK DR. MARKO PAVLIHA:    |      4288 |
| PODPREDSEDNIK FRANCE CUKJATI:       |      4176 |
| PODPREDSEDNIK VALENTIN POHOREC:     |      4105 |
Statistics after deduplication:

Number of words in the notes: 69869

|        | tag   | type   | content   | xml:lang   |      length |
|:-------|:------|:-------|:----------|:-----------|------------:|
| count  | 10236 | 10236  | 10236     | 10236      | 10236       |
| unique | 6     | 22     | 9955      | 1          |   nan       |
| top    | note  | time   | Je ni.    | sl         |   nan       |
| freq   | 9482  | 3675   | 3         | 10236      |   nan       |
| mean   | nan   | nan    | nan       | nan        |     6.82581 |
| std    | nan   | nan    | nan       | nan        |     4.66904 |
| min    | nan   | nan    | nan       | nan        |     1       |
| 25%    | nan   | nan    | nan       | nan        |     3       |
| 50%    | nan   | nan    | nan       | nan        |     5       |
| 75%    | nan   | nan    | nan       | nan        |    10       |
| max    | nan   | nan    | nan       | nan        |    63       |


|    | tag   | type    | content                       | xml:lang   |   length |
|---:|:------|:--------|:------------------------------|:-----------|---------:|
|  0 | note  | time    | Seja se je začela ob 12. uri. | sl         |        7 |
|  1 | note  | speaker | PREDSEDNIK JANKO VEBER:       | sl         |        3 |
|  2 | note  |         | Za je glasovalo 56.           | sl         |        4 |
|  3 | note  |         | Proti 1.                      | sl         |        2 |
|  5 | note  |         | Proti nihče.                  | sl         |        2 |


Statistics for tags:

|          |   tag |
|:---------|------:|
| note     |  9482 |
| head     |   588 |
| vocal    |    58 |
| gap      |    49 |
| kinesic  |    41 |
| incident |    18 |


|                           |   type |
|:--------------------------|-------:|
| ('gap', 'inaudible')      |     43 |
| ('gap', 'editorial')      |      6 |
| ('head', 'session')       |    327 |
| ('head', 'chairman')      |    250 |
| ('head', '')              |     11 |
| ('incident', 'sound')     |     11 |
| ('incident', 'action')    |      7 |
| ('kinesic', 'gesture')    |     14 |
| ('kinesic', 'signal')     |     12 |
| ('kinesic', 'applause')   |     10 |
| ('kinesic', 'snapping')   |      3 |
| ('kinesic', 'playback')   |      2 |
| ('note', 'time')          |   3675 |
| ('note', '')              |   2786 |
| ('note', 'speaker')       |   2623 |
| ('note', 'vote-ayes')     |    192 |
| ('note', 'vote-noes')     |    161 |
| ('note', 'answer')        |     21 |
| ('note', 'error')         |     15 |
| ('note', 'description')   |      7 |
| ('note', 'vote')          |      2 |
| ('vocal', 'interruption') |     51 |
| ('vocal', 'laughter')     |      7 |
Translation started.
Translation completed. It took 7.3 minutes for 10236 instances for the entire process of extraction and translation.

|    | tag   | type    | content                       | xml:lang   |   length | translation                        | corpus   |
|---:|:------|:--------|:------------------------------|:-----------|---------:|:-----------------------------------|:---------|
|  0 | note  | time    | Seja se je začela ob 12. uri. | sl         |        7 | The meeting started at 12 o'clock. | SI       |
|  1 | note  | speaker | PREDSEDNIK JANKO VEBER:       | sl         |        3 | President JANKO WEBER:             | SI       |
|  2 | note  |         | Za je glasovalo 56.           | sl         |        4 | 56 votes in favour.                | SI       |
|  3 | note  |         | Proti 1.                      | sl         |        2 | Against one.                       | SI       |
|  5 | note  |         | Proti nihče.                  | sl         |        2 | No one.                            | SI       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-SI.notes.translated.tsv
