2023-05-15 08:39:25.561629: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-05-15 08:39:26.302985: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-05-15 08:39:26.303056: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-05-15 08:39:26.303062: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
Extraction of the notes and translation started.
No. of files: 1091.
Statistics before droping duplicates:



|        | tag    | type    | content     | xml:lang   |
|:-------|:-------|:--------|:------------|:-----------|
| count  | 352938 | 352938  | 352938      | 352938     |
| unique | 5      | 12      | 34691       | 1          |
| top    | note   | speaker | ГОЛОВУЮЧИЙ. | uk         |
| freq   | 336392 | 195711  | 95800       | 352938     |


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
| note     | 336392 |
| vocal    |   9853 |
| kinesic  |   5719 |
| gap      |    574 |
| incident |    400 |


|                         |   type |
|:------------------------|-------:|
| ('gap', 'inaudible')    |    574 |
| ('incident', 'action')  |    400 |
| ('kinesic', 'applause') |   5719 |
| ('note', 'speaker')     | 195711 |
| ('note', 'time')        | 128545 |
| ('note', 'narrative')   |   7757 |
| ('note', 'comment')     |   3133 |
| ('note', 'date')        |   1091 |
| ('note', '')            |    155 |
| ('vocal', 'noise')      |   8624 |
| ('vocal', 'shouting')   |   1225 |
| ('vocal', 'exclamat')   |      4 |
Most common notes:

|                                                               |   content |
|:--------------------------------------------------------------|----------:|
| ГОЛОВУЮЧИЙ.                                                   |     95800 |
| (Шум у залі)                                                  |      8271 |
| (Оплески)                                                     |      5526 |
| ЧЕРНЕНКО О.М.                                                 |      3273 |
| ЛЯШКО О.В.                                                    |      1981 |
| ГЕРАЩЕНКО І.В.                                                |      1790 |
| Веде засідання Перший заступник Голови Верховної Ради України |      1583 |
| КНЯЗЕВИЧ Р.П.                                                 |      1463 |
| ШУФРИЧ Н.І.                                                   |      1443 |
| КНЯЖИЦЬКИЙ М.Л.                                               |      1420 |
| ЮЖАНІНА Н.П.                                                  |      1389 |
| Веде засідання Голова Верховної Ради України ПАРУБІЙ А.В.     |      1282 |
| ЄМЕЦЬ Л.О.                                                    |      1243 |
| Веде засідання Голова Верховної Ради України РАЗУМКОВ Д.О.    |      1124 |
| СТЕФАНЧУК Р.О.                                                |      1123 |
| НІМЧЕНКО В.І.                                                 |      1120 |
| ВЛАСЕНКО С.В.                                                 |      1117 |
| СОБОЛЄВ С.В.                                                  |      1108 |
| ЛЕВЧЕНКО Ю.В.                                                 |      1084 |
| ТИМОШЕНКО Ю.В.                                                |      1048 |
Statistics after deduplication:

Number of words in the notes: 50097

|        | tag   | type   | content      | xml:lang   |      length |
|:-------|:------|:-------|:-------------|:-----------|------------:|
| count  | 34703 | 34703  | 34703        | 34703      | 34703       |
| unique | 5     | 12     | 34691        | 1          |   nan       |
| top    | note  | time   | ПАРУБІЙ А.В. | uk         |   nan       |
| freq   | 34093 | 31290  | 3            | 34703      |   nan       |
| mean   | nan   | nan    | nan          | nan        |     1.44359 |
| std    | nan   | nan    | nan          | nan        |     1.50581 |
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
| note     | 34093 |
| vocal    |   569 |
| kinesic  |    26 |
| incident |    11 |
| gap      |     4 |


|                         |   type |
|:------------------------|-------:|
| ('gap', 'inaudible')    |      4 |
| ('incident', 'action')  |     11 |
| ('kinesic', 'applause') |     26 |
| ('note', 'time')        |  31290 |
| ('note', 'speaker')     |   1732 |
| ('note', 'date')        |    783 |
| ('note', 'comment')     |    151 |
| ('note', 'narrative')   |     75 |
| ('note', '')            |     62 |
| ('vocal', 'shouting')   |    558 |
| ('vocal', 'noise')      |      9 |
| ('vocal', 'exclamat')   |      2 |
Translation started.
Translation completed. It took 13.81 minutes for 34703 instances for the entire process of extraction and translation.
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
