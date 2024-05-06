2024-02-23 09:53:11.042234: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2024-02-23 09:53:11.619515: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2024-02-23 09:53:11.619595: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2024-02-23 09:53:11.619603: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
Extraction of the notes and translation started.
No. of files: 2407.
Statistics before droping duplicates:



|        | tag    | type    | content     | xml:lang   |
|:-------|:-------|:--------|:------------|:-----------|
| count  | 754096 | 754096  | 754096      | 754096     |
| unique | 5      | 12      | 61374       | 2          |
| top    | note   | speaker | ГОЛОВУЮЧИЙ. | uk         |
| freq   | 730120 | 429510  | 177822      | 753176     |


|    | tag   | type      | content                                                | xml:lang   |
|---:|:------|:----------|:-------------------------------------------------------|:-----------|
|  0 | note  | date      | Стенограма пленарного засідання 20 березня 2013        | uk         |
|  1 | note  | comment   | ЗАСІДАННЯ ЧЕТВЕРТЕ                                     | uk         |
|  2 | note  | comment   | Сесійна зала Верховної Ради України                    | uk         |
|  3 | note  | time      | 20 березня 2013 року, 10 година                        | uk         |
|  4 | note  | narrative | Веде засідання Голова Верховної Ради України В.В.РИБАК | uk         |


Statistics for tags:

|          |    tag |
|:---------|-------:|
| note     | 730120 |
| vocal    |  14504 |
| kinesic  |   7772 |
| gap      |   1157 |
| incident |    543 |


|                         |   type |
|:------------------------|-------:|
| ('gap', 'inaudible')    |   1157 |
| ('incident', 'action')  |    543 |
| ('kinesic', 'applause') |   7772 |
| ('note', 'speaker')     | 429510 |
| ('note', 'time')        | 248720 |
| ('note', '')            |  29826 |
| ('note', 'narrative')   |  10940 |
| ('note', 'comment')     |   8717 |
| ('note', 'date')        |   2407 |
| ('vocal', 'noise')      |  11606 |
| ('vocal', 'shouting')   |   2894 |
| ('vocal', 'exclamat')   |      4 |
Most common notes:

|                                                               |   content |
|:--------------------------------------------------------------|----------:|
| ГОЛОВУЮЧИЙ.                                                   |    177822 |
| ГОЛОВА.                                                       |     29002 |
| Шум у залі                                                    |     11226 |
| Оплески                                                       |      7546 |
| КАРМАЗІН Ю.А.                                                 |      6997 |
| ЛЯШКО О.В.                                                    |      3280 |
| ЧЕРНЕНКО О.М.                                                 |      3273 |
| Ш у м у з а л і                                               |      2441 |
| ГЕРАЩЕНКО І.В.                                                |      2058 |
| КНЯЗЕВИЧ Р.П.                                                 |      1933 |
| ЯВОРІВСЬКИЙ В.О.                                              |      1850 |
| ШУФРИЧ Н.І.                                                   |      1766 |
| Веде засідання Перший заступник Голови Верховної Ради України |      1726 |
| Сесійний зал Верховної Ради України                           |      1666 |
| О п л е с к и                                                 |      1621 |
| ЗАРУБІНСЬКИЙ О.О.                                             |      1585 |
| ЮЖАНІНА Н.П.                                                  |      1581 |
| СУХИЙ Я.М.                                                    |      1564 |
| ТИМОШЕНКО Ю.В.                                                |      1535 |
| СИМОНЕНКО П.М.                                                |      1532 |
Statistics after deduplication:

Number of words in the notes: 157966

|        | tag   | type   | content       | xml:lang   |      length |
|:-------|:------|:-------|:--------------|:-----------|------------:|
| count  | 61443 | 61443  | 61443         | 61443      | 61443       |
| unique | 5     | 12     | 61374         | 2          |   nan       |
| top    | note  | time   | МАРТИНЮК А.І. | uk         |   nan       |
| freq   | 59962 | 38323  | 3             | 60853      |   nan       |
| mean   | nan   | nan    | nan           | nan        |     2.57094 |
| std    | nan   | nan    | nan           | nan        |     3.00835 |
| min    | nan   | nan    | nan           | nan        |     1       |
| 25%    | nan   | nan    | nan           | nan        |     1       |
| 50%    | nan   | nan    | nan           | nan        |     1       |
| 75%    | nan   | nan    | nan           | nan        |     3       |
| max    | nan   | nan    | nan           | nan        |    86       |


|    | tag   | type      | content                                                | xml:lang   |   length |
|---:|:------|:----------|:-------------------------------------------------------|:-----------|---------:|
|  0 | note  | date      | Стенограма пленарного засідання 20 березня 2013        | uk         |        6 |
|  1 | note  | comment   | ЗАСІДАННЯ ЧЕТВЕРТЕ                                     | uk         |        2 |
|  2 | note  | comment   | Сесійна зала Верховної Ради України                    | uk         |        5 |
|  3 | note  | time      | 20 березня 2013 року, 10 година                        | uk         |        6 |
|  4 | note  | narrative | Веде засідання Голова Верховної Ради України В.В.РИБАК | uk         |        7 |


Statistics for tags:

|          |   tag |
|:---------|------:|
| note     | 59962 |
| vocal    |  1424 |
| kinesic  |    35 |
| incident |    14 |
| gap      |     8 |


|                         |   type |
|:------------------------|-------:|
| ('gap', 'inaudible')    |      8 |
| ('incident', 'action')  |     14 |
| ('kinesic', 'applause') |     35 |
| ('note', 'time')        |  38323 |
| ('note', '')            |  15813 |
| ('note', 'speaker')     |   3627 |
| ('note', 'date')        |   1723 |
| ('note', 'comment')     |    318 |
| ('note', 'narrative')   |    158 |
| ('vocal', 'shouting')   |   1407 |
| ('vocal', 'noise')      |     15 |
| ('vocal', 'exclamat')   |      2 |
Translation started.
Translation completed. It took 107.0 minutes for 61443 instances for the entire process of extraction and translation.
|    | tag   | type      | content                                                | xml:lang   |   length | translation                                        | corpus   |
|---:|:------|:----------|:-------------------------------------------------------|:-----------|---------:|:---------------------------------------------------|:---------|
|  0 | note  | date      | Стенограма пленарного засідання 20 березня 2013        | uk         |        6 | Schedule of the plenary meeting March 20, 2013     | UA       |
|  1 | note  | comment   | ЗАСІДАННЯ ЧЕТВЕРТЕ                                     | uk         |        2 | MEETING OF THE FOURTH                              | UA       |
|  2 | note  | comment   | Сесійна зала Верховної Ради України                    | uk         |        5 | The session hall of the Supreme Council of Ukraine | UA       |
|  3 | note  | time      | 20 березня 2013 року, 10 година                        | uk         |        6 | March 20, 2013, 10 a.m.                            | UA       |
|  4 | note  | narrative | Веде засідання Голова Верховної Ради України В.В.РИБАК | uk         |        7 | Head of the Supreme Council of Ukraine V.V. Ribak  | UA       |




/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-UA.notes.translated.ana.tsv
