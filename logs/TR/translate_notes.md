2023-03-13 13:39:56.768555: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-03-13 13:39:57.459363: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-03-13 13:39:57.459433: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-03-13 13:39:57.459440: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Extraction of the notes and translation started.
No. of files: 1335.
Statistics before droping duplicates:



|        | tag    | type     | content                                      | xml:lang   |
|:-------|:-------|:---------|:---------------------------------------------|:-----------|
| count  | 223934 | 223934   | 223934                                       | 223934     |
| unique | 4      | 13       | 4182                                         | 2          |
| top    | note   | applause | Mikrofon otomatik cihaz tarafından kapatıldı | tr         |
| freq   | 109556 | 103152   | 40465                                        | 210944     |


|    | tag   | type      | content                                      | xml:lang   |
|---:|:------|:----------|:---------------------------------------------|:-----------|
|  0 | note  | time      | 15.01                                        |            |
|  1 | note  | president | Meral Akşener                                |            |
|  2 | note  | quorum    | Elektronik cihazla yoklama yapıldı           | tr         |
|  3 | note  |           | Mikrofon otomatik cihaz tarafından kapatıldı | tr         |
|  4 | note  |           | Mikrofon otomatik cihaz tarafından kapatıldı | tr         |


Statistics for tags:

|          |    tag |
|:---------|-------:|
| note     | 109556 |
| kinesic  | 104527 |
| vocal    |   9655 |
| incident |    196 |


|                           |   type |
|:--------------------------|-------:|
| ('incident', 'action')    |    159 |
| ('incident', 'leaving')   |     37 |
| ('kinesic', 'applause')   | 103152 |
| ('kinesic', 'gesture')    |   1237 |
| ('kinesic', 'snapping')   |    138 |
| ('note', '')              |  92040 |
| ('note', 'president')     |   6495 |
| ('note', 'time')          |   6495 |
| ('note', 'vote')          |   2653 |
| ('note', 'quorum')        |   1873 |
| ('vocal', 'noise')        |   8488 |
| ('vocal', 'interruption') |   1008 |
| ('vocal', 'laughter')     |    159 |
Most common notes:

|                                              |   content |
|:---------------------------------------------|----------:|
| Mikrofon otomatik cihaz tarafından kapatıldı |     40465 |
| CHP sıralarından alkışlar                    |     32841 |
| AK PARTİ sıralarından alkışlar               |     25003 |
| HDP sıralarından alkışlar                    |     14006 |
| MHP sıralarından alkışlar                    |     10779 |
| İstanbul                                     |      6681 |
| İYİ PARTİ sıralarından alkışlar              |      4072 |
| AK PARTİ sıralarından gürültüler             |      3547 |
| Devam                                        |      3352 |
| İYİ Parti sıralarından alkışlar              |      2551 |
| İzmir                                        |      1942 |
| Elektronik cihazla yoklama yapıldı           |      1869 |
| BDP sıralarından alkışlar                    |      1857 |
| Ankara                                       |      1710 |
| Adana                                        |      1599 |
| Bursa                                        |      1583 |
| Elektronik cihazla oylama yapıldı            |      1572 |
| CHP sıralarından gürültüler                  |      1563 |
| TL                                           |      1561 |
| Mersin                                       |      1530 |
Statistics after deduplication:

Number of words in the notes: 23914

|        | tag   | type   |   content | xml:lang   |     length |
|:-------|:------|:-------|----------:|:-----------|-----------:|
| count  | 4182  | 4182   |   4182    | 4182       | 4182       |
| unique | 4     | 13     |   4182    | 2          |  nan       |
| top    | note  |        |     15.01 | tr         |  nan       |
| freq   | 1881  | 966    |      1    | 3298       |  nan       |
| mean   | nan   | nan    |    nan    | nan        |    5.71832 |
| std    | nan   | nan    |    nan    | nan        |    4.98714 |
| min    | nan   | nan    |    nan    | nan        |    0       |
| 25%    | nan   | nan    |    nan    | nan        |    1       |
| 50%    | nan   | nan    |    nan    | nan        |    6       |
| 75%    | nan   | nan    |    nan    | nan        |    8       |
| max    | nan   | nan    |    nan    | nan        |  124       |


|    | tag   | type      | content                                      | xml:lang   |   length |
|---:|:------|:----------|:---------------------------------------------|:-----------|---------:|
|  0 | note  | time      | 15.01                                        |            |        1 |
|  1 | note  | president | Meral Akşener                                |            |        2 |
|  2 | note  | quorum    | Elektronik cihazla yoklama yapıldı           | tr         |        4 |
|  3 | note  |           | Mikrofon otomatik cihaz tarafından kapatıldı | tr         |        5 |
| 10 | note  |           | İstanbul                                     | tr         |        1 |


Statistics for tags:

|          |   tag |
|:---------|------:|
| note     |  1881 |
| vocal    |  1256 |
| kinesic  |   897 |
| incident |   148 |


|                           |   type |
|:--------------------------|-------:|
| ('incident', 'action')    |    128 |
| ('incident', 'leaving')   |     20 |
| ('kinesic', 'applause')   |    842 |
| ('kinesic', 'snapping')   |     28 |
| ('kinesic', 'gesture')    |     27 |
| ('note', '')              |    966 |
| ('note', 'time')          |    852 |
| ('note', 'president')     |     32 |
| ('note', 'vote')          |     29 |
| ('note', 'quorum')        |      2 |
| ('vocal', 'interruption') |    810 |
| ('vocal', 'noise')        |    417 |
| ('vocal', 'laughter')     |     29 |
Translation started.
Translation completed. It took 6.85 minutes for 4182 instances for the entire process of extraction and translation.
|    | tag   | type      | content                                      | xml:lang   |   length | translation                               |
|---:|:------|:----------|:---------------------------------------------|:-----------|---------:|:------------------------------------------|
|  0 | note  | time      | 15.01                                        |            |        1 | 15.01                                     |
|  1 | note  | president | Meral Akşener                                |            |        2 | Coral Akşener                             |
|  2 | note  | quorum    | Elektronik cihazla yoklama yapıldı           | tr         |        4 | Checked with electronic device            |
|  3 | note  |           | Mikrofon otomatik cihaz tarafından kapatıldı | tr         |        5 | Microphone turned off by automatic device |
| 10 | note  |           | İstanbul                                     | tr         |        1 | İstanbul                                  |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-TR.notes.translated.csv
