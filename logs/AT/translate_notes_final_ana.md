2023-08-29 09:42:31.363300: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-08-29 09:42:32.014362: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-08-29 09:42:32.014432: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-08-29 09:42:32.014438: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
Extraction of the notes and translation started.
No. of files: 1221.
Statistics before droping duplicates:



|        | tag     | type     | content              | xml:lang   |
|:-------|:--------|:---------|:---------------------|:-----------|
| count  | 1048771 | 1048771  | 1048771              | 1048771    |
| unique | 4       | 17       | 292413               | 2          |
| top    | note    | applause | Beifall bei der SPÖ. | de         |
| freq   | 680688  | 247162   | 36573                | 1033609    |


|    | tag   | type         | content                                                                                                    | xml:lang   |
|---:|:------|:-------------|:-----------------------------------------------------------------------------------------------------------|:-----------|
|  0 | note  | time         | 09:05:32                                                                                                   | de         |
|  1 | note  | time         | Beginn der Sitzung:9:05Uhr                                                                                 | de         |
|  2 | note  | chairpersons | Präsidentin Mag. Barbara Prammer Zweiter Präsident Fritz Neugebauer Dritter Präsident Mag. Dr. Martin Graf | de         |
|  3 | note  | speaker      | Präsidentin Mag. Barbara Prammer                                                                           | de         |
|  4 | note  | speaker      | Präsidentin Mag. Barbara Prammer                                                                           | de         |


Statistics for tags:

|         |    tag |
|:--------|-------:|
| note    | 680688 |
| kinesic | 253015 |
| vocal   |  84744 |
| gap     |  30324 |


|                                       |   type |
|:--------------------------------------|-------:|
| ('gap', 'editorial')                  |  30324 |
| ('kinesic', 'applause')               | 247162 |
| ('kinesic', 'signal')                 |   5853 |
| ('note', 'speaker')                   | 231773 |
| ('note', 'unauthorized_interruption') | 231356 |
| ('note', 'time')                      | 187824 |
| ('note', 'procedural')                |  11442 |
| ('note', 'comment')                   |  10170 |
| ('note', 'speaker_action')            |   3772 |
| ('note', 'inquietude')                |   1235 |
| ('note', 'chairpersons')              |   1218 |
| ('note', 'objection')                 |    956 |
| ('note', 'side_talk')                 |    582 |
| ('note', 'referencing_document')      |    353 |
| ('note', 'p')                         |      7 |
| ('vocal', 'interruption')             |  73137 |
| ('vocal', 'laughter')                 |  11607 |
Most common notes:

|                                             |   content |
|:--------------------------------------------|----------:|
| Beifall bei der SPÖ.                        |     36573 |
| Beifall bei der ÖVP.                        |     27464 |
| Beifall bei der FPÖ.                        |     20440 |
| Präsidentin Mag. Barbara Prammer            |     18848 |
| Präsident Dr. Heinz Fischer                 |     18575 |
| Beifall bei den Grünen.                     |     17912 |
| Beifall bei den Freiheitlichen.             |     15172 |
| Zitierte Druckfassung entfernt              |     13938 |
| Quoted printed matter omited                |     13938 |
| Präsidentin Doris Bures                     |     13147 |
| Präsident Mag. Wolfgang Sobotka             |     10270 |
| Beifall bei der ÖVP und den Freiheitlichen. |      9603 |
| Präsident Dr. Andreas Khol                  |      8525 |
| Beifall beim BZÖ.                           |      8363 |
| Präsident Ing. Norbert Hofer                |      7953 |
| Präsident Fritz Neugebauer                  |      7938 |
| Präsident Dipl.-Ing. Thomas Prinzhorn       |      7883 |
| Präsident Mag. Dr. Martin Graf              |      6980 |
| Präsident Karlheinz Kopf                    |      6388 |
| Beifall bei den Freiheitlichen und der ÖVP. |      6246 |
Statistics after deduplication:

Number of words in the notes: 2198401

|        | tag    | type                      | content                        | xml:lang   |       length |
|:-------|:-------|:--------------------------|:-------------------------------|:-----------|-------------:|
| count  | 292427 | 292427                    | 292427                         | 292427     | 292427       |
| unique | 4      | 17                        | 292413                         | 2          |    nan       |
| top    | note   | unauthorized_interruption | Präsident Mag. Dr. Martin Graf | de         |    nan       |
| freq   | 272448 | 217420                    | 2                              | 292423     |    nan       |
| mean   | nan    | nan                       | nan                            | nan        |      7.51778 |
| std    | nan    | nan                       | nan                            | nan        |      4.75163 |
| min    | nan    | nan                       | nan                            | nan        |      1       |
| 25%    | nan    | nan                       | nan                            | nan        |      5       |
| 50%    | nan    | nan                       | nan                            | nan        |      7       |
| 75%    | nan    | nan                       | nan                            | nan        |     10       |
| max    | nan    | nan                       | nan                            | nan        |    247       |


|    | tag   | type         | content                                                                                                    | xml:lang   |   length |
|---:|:------|:-------------|:-----------------------------------------------------------------------------------------------------------|:-----------|---------:|
|  0 | note  | time         | 09:05:32                                                                                                   | de         |        1 |
|  1 | note  | time         | Beginn der Sitzung:9:05Uhr                                                                                 | de         |        3 |
|  2 | note  | chairpersons | Präsidentin Mag. Barbara Prammer Zweiter Präsident Fritz Neugebauer Dritter Präsident Mag. Dr. Martin Graf | de         |       14 |
|  3 | note  | speaker      | Präsidentin Mag. Barbara Prammer                                                                           | de         |        4 |
|  5 | note  | comment      | siehe S. 37                                                                                                | de         |        3 |


Statistics for tags:

|         |    tag |
|:--------|-------:|
| note    | 272448 |
| vocal   |  10365 |
| kinesic |   9606 |
| gap     |      8 |


|                                       |   type |
|:--------------------------------------|-------:|
| ('gap', 'editorial')                  |      8 |
| ('kinesic', 'applause')               |   9464 |
| ('kinesic', 'signal')                 |    142 |
| ('note', 'unauthorized_interruption') | 217420 |
| ('note', 'time')                      |  40820 |
| ('note', 'comment')                   |   6541 |
| ('note', 'speaker_action')            |   3057 |
| ('note', 'speaker')                   |   2362 |
| ('note', 'procedural')                |    934 |
| ('note', 'side_talk')                 |    576 |
| ('note', 'referencing_document')      |    353 |
| ('note', 'objection')                 |    197 |
| ('note', 'chairpersons')              |    110 |
| ('note', 'inquietude')                |     72 |
| ('note', 'p')                         |      6 |
| ('vocal', 'interruption')             |   8015 |
| ('vocal', 'laughter')                 |   2350 |
Translation started.
Translation completed. It took 238.26 minutes for 292427 instances for the entire process of extraction and translation.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(

|    | tag   | type         | content                                                                                                    | xml:lang   |   length | translation                                                                                          | corpus   |
|---:|:------|:-------------|:-----------------------------------------------------------------------------------------------------------|:-----------|---------:|:-----------------------------------------------------------------------------------------------------|:---------|
|  0 | note  | time         | 09:05:32                                                                                                   | de         |        1 | 09:05:32                                                                                             | AT       |
|  1 | note  | time         | Beginn der Sitzung:9:05Uhr                                                                                 | de         |        3 | Start of meeting:9:05                                                                                | AT       |
|  2 | note  | chairpersons | Präsidentin Mag. Barbara Prammer Zweiter Präsident Fritz Neugebauer Dritter Präsident Mag. Dr. Martin Graf | de         |       14 | President Mag. Barbara Prammer Second President Fritz Neugebauer Third President Mag. Dr Martin Graf | AT       |
|  3 | note  | speaker      | Präsidentin Mag. Barbara Prammer                                                                           | de         |        4 | President Mag. Barbara Prammer                                                                       | AT       |
|  5 | note  | comment      | siehe S. 37                                                                                                | de         |        3 | See page 37                                                                                          | AT       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-AT.notes.translated.ana.tsv
