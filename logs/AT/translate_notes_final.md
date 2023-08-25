2023-04-25 15:42:41.837745: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-04-25 15:42:42.668553: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-04-25 15:42:42.668623: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-04-25 15:42:42.668630: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Extraction of the notes and translation started.
No. of files: 1197.
Statistics before droping duplicates:



|        | tag     | type     | content                | xml:lang   |
|:-------|:--------|:---------|:-----------------------|:-----------|
| count  | 1029730 | 1029730  | 1029730                | 1029730    |
| unique | 4       | 17       | 287499                 | 2          |
| top    | note    | applause | (Beifall bei der SPÖ.) | de         |
| freq   | 668670  | 242865   | 35771                  | 1014866    |


|    | tag   | type         | content                          | xml:lang   |
|---:|:------|:-------------|:---------------------------------|:-----------|
|  0 | note  | time         | 4:31:17                          | de         |
|  1 | note  | time         | Beginn der Sitzung:14:31Uhr      | de         |
|  2 | note  | chairpersons | Zweiter Präsident Karlheinz Kopf | de         |
|  3 | note  | speaker      | Präsident Karlheinz Kopf         | de         |
|  4 | note  | time         | 14:31:24                         | de         |


Statistics for tags:

|         |    tag |
|:--------|-------:|
| note    | 668670 |
| kinesic | 248599 |
| vocal   |  82733 |
| gap     |  29728 |


|                                       |   type |
|:--------------------------------------|-------:|
| ('gap', 'editorial')                  |  29728 |
| ('kinesic', 'applause')               | 242865 |
| ('kinesic', 'signal')                 |   5734 |
| ('note', 'speaker')                   | 228004 |
| ('note', 'unauthorized_interruption') | 226865 |
| ('note', 'time')                      | 184662 |
| ('note', 'procedural')                |  11289 |
| ('note', 'comment')                   |   9858 |
| ('note', 'speaker_action')            |   3729 |
| ('note', 'inquietude')                |   1204 |
| ('note', 'chairpersons')              |   1194 |
| ('note', 'objection')                 |    931 |
| ('note', 'side_talk')                 |    574 |
| ('note', 'referencing_document')      |    353 |
| ('note', 'p')                         |      7 |
| ('vocal', 'interruption')             |  71304 |
| ('vocal', 'laughter')                 |  11429 |
Most common notes:

|                                               |   content |
|:----------------------------------------------|----------:|
| (Beifall bei der SPÖ.)                        |     35771 |
| (Beifall bei der ÖVP.)                        |     27121 |
| (Beifall bei der FPÖ.)                        |     19887 |
| Präsidentin Mag. Barbara Prammer              |     18848 |
| Präsident Dr. Heinz Fischer                   |     18575 |
| (Beifall bei den Grünen.)                     |     17752 |
| (Beifall bei den Freiheitlichen.)             |     15172 |
| Quoted printed matter omited                  |     13664 |
| Zitierte Druckfassung entfernt                |     13664 |
| Präsidentin Doris Bures                       |     12546 |
| (Beifall bei der ÖVP und den Freiheitlichen.) |      9603 |
| Präsident Mag. Wolfgang Sobotka               |      9241 |
| Präsident Dr. Andreas Khol                    |      8525 |
| (Beifall beim BZÖ.)                           |      8362 |
| Präsident Fritz Neugebauer                    |      7938 |
| Präsident Dipl.-Ing. Thomas Prinzhorn         |      7883 |
| Präsident Ing. Norbert Hofer                  |      7515 |
| Präsident Mag. Dr. Martin Graf                |      6980 |
| Präsident Karlheinz Kopf                      |      6388 |
| (Beifall bei den Freiheitlichen und der ÖVP.) |      6246 |
Statistics after deduplication:

Number of words in the notes: 2160689

|        | tag    | type                      | content                 | xml:lang   |       length |
|:-------|:-------|:--------------------------|:------------------------|:-----------|-------------:|
| count  | 287513 | 287513                    | 287513                  | 287513     | 287513       |
| unique | 4      | 17                        | 287499                  | 2          |    nan       |
| top    | note   | unauthorized_interruption | Präsidentin Doris Bures | de         |    nan       |
| freq   | 267589 | 213265                    | 2                       | 287509     |    nan       |
| mean   | nan    | nan                       | nan                     | nan        |      7.5151  |
| std    | nan    | nan                       | nan                     | nan        |      4.75234 |
| min    | nan    | nan                       | nan                     | nan        |      1       |
| 25%    | nan    | nan                       | nan                     | nan        |      5       |
| 50%    | nan    | nan                       | nan                     | nan        |      7       |
| 75%    | nan    | nan                       | nan                     | nan        |     10       |
| max    | nan    | nan                       | nan                     | nan        |    247       |


|    | tag   | type         | content                          | xml:lang   |   length |
|---:|:------|:-------------|:---------------------------------|:-----------|---------:|
|  0 | note  | time         | 4:31:17                          | de         |        1 |
|  1 | note  | time         | Beginn der Sitzung:14:31Uhr      | de         |        3 |
|  2 | note  | chairpersons | Zweiter Präsident Karlheinz Kopf | de         |        4 |
|  3 | note  | speaker      | Präsident Karlheinz Kopf         | de         |        3 |
|  4 | note  | time         | 14:31:24                         | de         |        1 |


Statistics for tags:

|         |    tag |
|:--------|-------:|
| note    | 267589 |
| vocal   |  10419 |
| kinesic |   9497 |
| gap     |      8 |


|                                       |   type |
|:--------------------------------------|-------:|
| ('gap', 'editorial')                  |      8 |
| ('kinesic', 'applause')               |   9357 |
| ('kinesic', 'signal')                 |    140 |
| ('note', 'unauthorized_interruption') | 213265 |
| ('note', 'time')                      |  40351 |
| ('note', 'comment')                   |   6373 |
| ('note', 'speaker_action')            |   3020 |
| ('note', 'speaker')                   |   2352 |
| ('note', 'procedural')                |    925 |
| ('note', 'side_talk')                 |    568 |
| ('note', 'referencing_document')      |    353 |
| ('note', 'objection')                 |    193 |
| ('note', 'chairpersons')              |    111 |
| ('note', 'inquietude')                |     72 |
| ('note', 'p')                         |      6 |
| ('vocal', 'interruption')             |   8109 |
| ('vocal', 'laughter')                 |   2310 |
Translation started.
Translation completed. It took 134.01 minutes for 287513 instances for the entire process of extraction and translation.
|    | tag   | type         | content                          | xml:lang   |   length | translation                       | corpus   |
|---:|:------|:-------------|:---------------------------------|:-----------|---------:|:----------------------------------|:---------|
|  0 | note  | time         | 4:31:17                          | de         |        1 | 4:31:17                           | AT       |
|  1 | note  | time         | Beginn der Sitzung:14:31Uhr      | de         |        3 | Start of meeting: 14 a.m.:31 p.m. | AT       |
|  2 | note  | chairpersons | Zweiter Präsident Karlheinz Kopf | de         |        4 | Second President Karlheinz Kopf   | AT       |
|  3 | note  | speaker      | Präsident Karlheinz Kopf         | de         |        3 | President Karlheinz Kopp          | AT       |
|  4 | note  | time         | 14:31:24                         | de         |        1 | 14:31:24                          | AT       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-AT.notes.translated.csv
