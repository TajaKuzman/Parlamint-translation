2023-03-13 13:21:47.016948: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-03-13 13:21:47.813166: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-03-13 13:21:47.813238: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-03-13 13:21:47.813245: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Extraction of the notes and translation started.
No. of files: 6100.
Statistics before droping duplicates:



|        | tag    | type    | content       | xml:lang   |
|:-------|:-------|:--------|:--------------|:-----------|
| count  | 789776 | 789776  | 789776        | 789776     |
| unique | 2      | 4       | 130717        | 1          |
| top    | note   | speaker | De voorzitter |            |
| freq   | 783676 | 530090  | 139293        | 789776     |


|    | tag   | type    | content                   | xml:lang   |
|---:|:------|:--------|:--------------------------|:-----------|
|  0 | note  | speaker | De voorzitter             |            |
|  1 | note  | speaker | Mevrouw Ouwehand (PvdD)   |            |
|  2 | note  | comment | Motie                     |            |
|  3 | note  | comment | De Kamer,                 |            |
|  4 | note  | comment | gehoord de beraadslaging, |            |


Statistics for tags:

|      |    tag |
|:-----|-------:|
| note | 783676 |
| head |   6100 |


|                     |   type |
|:--------------------|-------:|
| ('head', '')        |   6100 |
| ('note', 'speaker') | 530090 |
| ('note', 'comment') | 249023 |
| ('note', 'time')    |   4563 |
Most common notes:

|                                                    |   content |
|:---------------------------------------------------|----------:|
| De voorzitter                                      |    139293 |
| De Kamer,                                          |     23776 |
| gehoord de beraadslaging,                          |     23776 |
| en gaat over tot de orde van de dag.               |     23775 |
| Motie                                              |     23772 |
| Minister Rutte                                     |     13233 |
| Minister De Jonge                                  |      6793 |
| Mevrouw Leijten (SP)                               |      4595 |
| Minister Hoekstra                                  |      4165 |
| Minister Blok                                      |      3907 |
| Minister Grapperhaus                               |      3859 |
| De heer Klaver (GroenLinks)                        |      3699 |
| Minister Ollongren                                 |      3566 |
| Minister Schouten                                  |      3538 |
| De vergadering wordt enkele ogenblikken geschorst. |      3412 |
| Mevrouw Ouwehand (PvdD)                            |      3322 |
| Minister Wiebes                                    |      3304 |
| De heer Omtzigt (CDA)                              |      3304 |
| De heer Wilders (PVV)                              |      3193 |
| De heer Nijboer (PvdA)                             |      3047 |
Statistics after deduplication:

Number of words in the notes: 2429525

|        | tag    | type    | content       | xml:lang   |      length |
|:-------|:-------|:--------|:--------------|:-----------|------------:|
| count  | 130717 | 130717  | 130717        | 130717     | 130717      |
| unique | 2      | 4       | 130717        | 1          |    nan      |
| top    | note   | comment | De voorzitter |            |    nan      |
| freq   | 127617 | 122829  | 1             | 130717     |    nan      |
| mean   | nan    | nan     | nan           | nan        |     18.5861 |
| std    | nan    | nan     | nan           | nan        |     12.2304 |
| min    | nan    | nan     | nan           | nan        |      0      |
| 25%    | nan    | nan     | nan           | nan        |     10      |
| 50%    | nan    | nan     | nan           | nan        |     18      |
| 75%    | nan    | nan     | nan           | nan        |     25      |
| max    | nan    | nan     | nan           | nan        |    188      |


|    | tag   | type    | content                   | xml:lang   |   length |
|---:|:------|:--------|:--------------------------|:-----------|---------:|
|  0 | note  | speaker | De voorzitter             |            |        2 |
|  1 | note  | speaker | Mevrouw Ouwehand (PvdD)   |            |        3 |
|  2 | note  | comment | Motie                     |            |        1 |
|  3 | note  | comment | De Kamer,                 |            |        2 |
|  4 | note  | comment | gehoord de beraadslaging, |            |        3 |


Statistics for tags:

|      |    tag |
|:-----|-------:|
| note | 127617 |
| head |   3100 |


|                     |   type |
|:--------------------|-------:|
| ('head', '')        |   3100 |
| ('note', 'comment') | 122829 |
| ('note', 'time')    |   4026 |
| ('note', 'speaker') |    762 |
Translation started.
Translation completed. It took 101.49 minutes for 130717 instances for the entire process of extraction and translation.
|    | tag   | type    | content                   | xml:lang   |   length | translation         |
|---:|:------|:--------|:--------------------------|:-----------|---------:|:--------------------|
|  0 | note  | speaker | De voorzitter             |            |        2 | The President       |
|  1 | note  | speaker | Mevrouw Ouwehand (PvdD)   |            |        3 | Mrs Ouwehand (PvdD) |
|  2 | note  | comment | Motie                     |            |        1 | Motion              |
|  3 | note  | comment | De Kamer,                 |            |        2 | The Chamber,        |
|  4 | note  | comment | gehoord de beraadslaging, |            |        3 | heard the debate,   |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-NL.notes.translated.csv
