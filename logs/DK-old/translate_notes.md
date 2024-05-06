2023-03-14 08:49:38.030553: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-03-14 08:49:38.842453: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-03-14 08:49:38.842533: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-03-14 08:49:38.842540: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Extraction of the notes and translation started.
No. of files: 947.
Statistics before droping duplicates:



|        | tag   | type       | content   | xml:lang   |
|:-------|:------|:-----------|:----------|:-----------|
| count  | 28604 | 28604      | 28604     | 28604      |
| unique | 2     | 2          | 24275     | 1          |
| top    | note  | agendaItem | Punkt 0   |            |
| freq   | 14302 | 14302      | 2026      | 28604      |


|    | tag   | type       | content        | xml:lang   |
|---:|:------|:-----------|:---------------|:-----------|
|  0 | note  | agendaItem | 2017-11-22-0   |            |
|  1 | note  | agendaItem | 2017-11-22-1   |            |
|  2 | note  | agendaItem | 2017-11-22-2   |            |
|  3 | note  | agendaItem | 2017-11-22-2-1 |            |
|  4 | note  | agendaItem | 2017-11-22-2-2 |            |


Statistics for tags:

|      |   tag |
|:-----|------:|
| note | 14302 |
| head | 14302 |


|                        |   type |
|:-----------------------|-------:|
| ('head', '')           |  14302 |
| ('note', 'agendaItem') |  14302 |
Most common notes:

|                                                                          |   content |
|:-------------------------------------------------------------------------|----------:|
| Punkt 0                                                                  |      2026 |
| Besvarelse af oversendte spørgsmål til ministrene (spørgetid).           |       186 |
| Indstilling fra Udvalget til Valgs Prøvelse                              |        81 |
| Spørgetime med statsministeren.                                          |        36 |
| Spørgsmål om meddelelse af orlov til og indkaldelse af stedfortræder for |        35 |
| Udvidet spørgetime med statsministeren.                                  |        20 |
| Meddelelser fra formanden                                                |        13 |
| Forhandling af R 1: Om statsministerens åbningsredegørelse.              |        11 |
| Valg af formand.                                                         |        10 |
| Valg af stående udvalg m.v.                                              |        10 |
| Valg af 4 tingsekretærer.                                                |        10 |
| Valg af 4 næstformænd.                                                   |        10 |
| Spm. nr. US 8                                                            |         8 |
| Spm. nr. US 7                                                            |         8 |
| Spm. nr. US 14                                                           |         8 |
| Spm. nr. US 3                                                            |         8 |
| Spm. nr. US 24                                                           |         8 |
| Spm. nr. US 13                                                           |         8 |
| 2020-03-31-0                                                             |         8 |
| Spm. nr. US 15                                                           |         8 |
Statistics after deduplication:

Number of words in the notes: 161277

|        | tag   | type       | content      | xml:lang   |      length |
|:-------|:------|:-----------|:-------------|:-----------|------------:|
| count  | 24275 | 24275      | 24275        | 24275      | 24275       |
| unique | 2     | 2          | 24275        | 1          |   nan       |
| top    | note  | agendaItem | 2017-11-22-0 |            |   nan       |
| freq   | 12950 | 12950      | 1            | 24275      |   nan       |
| mean   | nan   | nan        | nan          | nan        |     6.64375 |
| std    | nan   | nan        | nan          | nan        |     6.67187 |
| min    | nan   | nan        | nan          | nan        |     1       |
| 25%    | nan   | nan        | nan          | nan        |     1       |
| 50%    | nan   | nan        | nan          | nan        |     1       |
| 75%    | nan   | nan        | nan          | nan        |    12       |
| max    | nan   | nan        | nan          | nan        |    27       |


|    | tag   | type       | content        | xml:lang   |   length |
|---:|:------|:-----------|:---------------|:-----------|---------:|
|  0 | note  | agendaItem | 2017-11-22-0   |            |        1 |
|  1 | note  | agendaItem | 2017-11-22-1   |            |        1 |
|  2 | note  | agendaItem | 2017-11-22-2   |            |        1 |
|  3 | note  | agendaItem | 2017-11-22-2-1 |            |        1 |
|  4 | note  | agendaItem | 2017-11-22-2-2 |            |        1 |


Statistics for tags:

|      |   tag |
|:-----|------:|
| note | 12950 |
| head | 11325 |


|                        |   type |
|:-----------------------|-------:|
| ('head', '')           |  11325 |
| ('note', 'agendaItem') |  12950 |
Translation started.
Translation completed. It took 36.81 minutes for 24275 instances for the entire process of extraction and translation.
|    | tag   | type       | content        | xml:lang   |   length | translation                                                                                    |
|---:|:------|:-----------|:---------------|:-----------|---------:|:-----------------------------------------------------------------------------------------------|
|  0 | note  | agendaItem | 2017-11-22-0   |            |        1 | This Regulation shall be binding in its entirety and directly applicable in all Member States. |
|  1 | note  | agendaItem | 2017-11-22-1   |            |        1 | This Regulation shall be binding in its entirety and directly applicable in all Member States. |
|  2 | note  | agendaItem | 2017-11-22-2   |            |        1 | This Regulation shall be binding in its entirety and directly applicable in all Member States. |
|  3 | note  | agendaItem | 2017-11-22-2-1 |            |        1 | 2017-11-222-1                                                                                  |
|  4 | note  | agendaItem | 2017-11-22-2-2 |            |        1 | 2017-11-22-2-2                                                                                 |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-DK.notes.translated.csv
