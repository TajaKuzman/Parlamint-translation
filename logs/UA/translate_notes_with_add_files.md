2023-09-26 10:31:07.088332: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-09-26 10:31:07.768473: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-09-26 10:31:07.768545: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-09-26 10:31:07.768553: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
Extraction of the notes and translation started.
No. of files: 1116.
Statistics before dropping duplicates:



|        | tag    | type    | content     | xml:lang   |
|:-------|:-------|:--------|:------------|:-----------|
| count  | 362893 | 362893  | 362893      | 362893     |
| unique | 5      | 12      | 35268       | 1          |
| top    | note   | speaker | ГОЛОВУЮЧИЙ. | uk         |
| freq   | 345746 | 200875  | 98377       | 362893     |


|    | tag   | type      | content                                                | xml:lang   |
|---:|:------|:----------|:-------------------------------------------------------|:-----------|
|  0 | note  | date      | Стенограма пленарного засідання 03 вересня 2013        | uk         |
|  1 | note  | comment   | ЗАСІДАННЯ ДРУГЕ                                        | uk         |
|  2 | note  | comment   | Сесійна зала Верховної Ради України                    | uk         |
|  3 | note  | time      | 3 вересня 2013 року, 16 година                         | uk         |
|  4 | note  | narrative | Веде засідання Голова Верховної Ради України В.В.РИБАК | uk         |


Statistics for tags:

|          |    tag |
|:---------|-------:|
| note     | 345746 |
| vocal    |  10052 |
| kinesic  |   6042 |
| gap      |    597 |
| incident |    456 |


|                         |   type |
|:------------------------|-------:|
| ('gap', 'inaudible')    |    597 |
| ('incident', 'action')  |    456 |
| ('kinesic', 'applause') |   6042 |
| ('note', 'speaker')     | 200875 |
| ('note', 'time')        | 132450 |
| ('note', 'narrative')   |   7913 |
| ('note', 'comment')     |   3210 |
| ('note', 'date')        |   1116 |
| ('note', '')            |    182 |
| ('vocal', 'noise')      |   8788 |
| ('vocal', 'shouting')   |   1260 |
| ('vocal', 'exclamat')   |      4 |
Most common notes:

|                                                               |   content |
|:--------------------------------------------------------------|----------:|
| ГОЛОВУЮЧИЙ.                                                   |     98377 |
| Шум у залі                                                    |      8441 |
| Оплески                                                       |      5918 |
| ЧЕРНЕНКО О.М.                                                 |      3273 |
| ЛЯШКО О.В.                                                    |      1981 |
| ГЕРАЩЕНКО І.В.                                                |      1901 |
| Веде засідання Перший заступник Голови Верховної Ради України |      1616 |
| ШУФРИЧ Н.І.                                                   |      1503 |
| ЮЖАНІНА Н.П.                                                  |      1497 |
| КНЯЗЕВИЧ Р.П.                                                 |      1463 |
| КНЯЖИЦЬКИЙ М.Л.                                               |      1434 |
| Веде засідання Голова Верховної Ради України ПАРУБІЙ А.В.     |      1286 |
| ЄМЕЦЬ Л.О.                                                    |      1243 |
| ВЛАСЕНКО С.В.                                                 |      1157 |
| ТИМОШЕНКО Ю.В.                                                |      1132 |
| СТЕФАНЧУК Р.О.                                                |      1131 |
| Веде засідання Голова Верховної Ради України РАЗУМКОВ Д.О.    |      1124 |
| НІМЧЕНКО В.І.                                                 |      1121 |
| СОБОЛЄВ С.В.                                                  |      1118 |
| ЛЕВЧЕНКО Ю.В.                                                 |      1084 |
Statistics after deduplication:

Number of words in the notes: 51032

|        | tag   | type   | content      | xml:lang   |      length |
|:-------|:------|:-------|:-------------|:-----------|------------:|
| count  | 35280 | 35280  | 35280        | 35280      | 35280       |
| unique | 5     | 12     | 35268        | 1          |   nan       |
| top    | note  | time   | ПАРУБІЙ А.В. | uk         |   nan       |
| freq   | 34667 | 31794  | 3            | 35280      |   nan       |
| mean   | nan   | nan    | nan          | nan        |     1.44649 |
| std    | nan   | nan    | nan          | nan        |     1.51063 |
| min    | nan   | nan    | nan          | nan        |     1       |
| 25%    | nan   | nan    | nan          | nan        |     1       |
| 50%    | nan   | nan    | nan          | nan        |     1       |
| 75%    | nan   | nan    | nan          | nan        |     1       |
| max    | nan   | nan    | nan          | nan        |    57       |


|    | tag   | type      | content                                                | xml:lang   |   length |
|---:|:------|:----------|:-------------------------------------------------------|:-----------|---------:|
|  0 | note  | date      | Стенограма пленарного засідання 03 вересня 2013        | uk         |        6 |
|  1 | note  | comment   | ЗАСІДАННЯ ДРУГЕ                                        | uk         |        2 |
|  2 | note  | comment   | Сесійна зала Верховної Ради України                    | uk         |        5 |
|  3 | note  | time      | 3 вересня 2013 року, 16 година                         | uk         |        6 |
|  4 | note  | narrative | Веде засідання Голова Верховної Ради України В.В.РИБАК | uk         |        7 |


Statistics for tags:

|          |   tag |
|:---------|------:|
| note     | 34667 |
| vocal    |   572 |
| kinesic  |    27 |
| incident |    10 |
| gap      |     4 |


|                         |   type |
|:------------------------|-------:|
| ('gap', 'inaudible')    |      4 |
| ('incident', 'action')  |     10 |
| ('kinesic', 'applause') |     27 |
| ('note', 'time')        |  31794 |
| ('note', 'speaker')     |   1763 |
| ('note', 'date')        |    808 |
| ('note', 'comment')     |    150 |
| ('note', '')            |     77 |
| ('note', 'narrative')   |     75 |
| ('vocal', 'shouting')   |    563 |
| ('vocal', 'noise')      |      7 |
| ('vocal', 'exclamat')   |      2 |
Translation started.
Translation completed. It took 14.2 minutes for 35280 instances for the entire process of extraction and translation.


|    | tag   | type      | content                                                | xml:lang   |   length | translation                                           | corpus   |
|---:|:------|:----------|:-------------------------------------------------------|:-----------|---------:|:------------------------------------------------------|:---------|
|  0 | note  | date      | Стенограма пленарного засідання 03 вересня 2013        | uk         |        6 | Schedule of the plenary meeting on September 03, 2013 | UA       |
|  1 | note  | comment   | ЗАСІДАННЯ ДРУГЕ                                        | uk         |        2 | ANOTHER MEETING                                       | UA       |
|  2 | note  | comment   | Сесійна зала Верховної Ради України                    | uk         |        5 | The session hall of the Supreme Council of Ukraine    | UA       |
|  3 | note  | time      | 3 вересня 2013 року, 16 година                         | uk         |        6 | September 3, 2013, 16 hours                           | UA       |
|  4 | note  | narrative | Веде засідання Голова Верховної Ради України В.В.РИБАК | uk         |        7 | Head of the Supreme Council of Ukraine V.V. Ribak     | UA       |




/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-UA.notes.translated.tsv
