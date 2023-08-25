2023-05-12 10:11:06.251977: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-05-12 10:11:06.840153: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-05-12 10:11:06.840215: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-05-12 10:11:06.840222: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Extraction of the notes and translation started.
No. of files: 3266.
Statistics before droping duplicates:



|        | tag     | type    | content      | xml:lang   |
|:-------|:--------|:--------|:-------------|:-----------|
| count  | 1585820 | 1585820 | 1585820      | 1585820    |
| unique | 2       | 3       | 649619       | 3          |
| top    | note    | comment | Presidenten: | nb         |
| freq   | 1565697 | 1256396 | 34316        | 1583638    |


|    | tag   | type    | content                                                      | xml:lang   |
|---:|:------|:--------|:-------------------------------------------------------------|:-----------|
|  0 | note  | comment | Dag Terje Andersen                                           | nb         |
|  1 | note  | comment | Dagsorden                                                    | nb         |
|  2 | note  | comment | (nr. 51):                                                    | nb         |
|  3 | note  | comment | 1.                                                           | nb         |
|  4 | note  | comment | Debatt om utenriksministerens utenrikspolitiske redegjørelse | nb         |


Statistics for tags:

|      |            tag |
|:-----|---------------:|
| note |     1.5657e+06 |
| head | 20123          |


|                     |            type |
|:--------------------|----------------:|
| ('head', '')        |  20123          |
| ('note', 'comment') |      1.2564e+06 |
| ('note', 'speaker') | 309301          |
Most common notes:

|                                             |   content |
|:--------------------------------------------|----------:|
| Presidenten:                                |     34316 |
| Votering:                                   |     31199 |
| med                                         |     22092 |
| 1                                           |     16676 |
| 70                                          |     10833 |
| kan overføres                               |     10026 |
| ,                                           |      9245 |
| Driftsutgifter                              |      7992 |
| 21                                          |      6402 |
| II                                          |      5660 |
| 71                                          |      5506 |
| I                                           |      5291 |
| Referat                                     |      5194 |
| økes                                        |      4906 |
| hadde her overtatt presidentplassen.        |      4375 |
| 2                                           |      4363 |
| Komiteens innstilling ble enstemmig bifalt. |      4346 |
| 72                                          |      4336 |
| forhøyes                                    |      4143 |
| 1.                                          |      3905 |
Statistics after deduplication:

Number of words in the notes: 7514052

|        | tag    | type    | content             | xml:lang   |      length |
|:-------|:-------|:--------|:--------------------|:-----------|------------:|
| count  | 650031 | 650031  | 650031              | 650031     | 650031      |
| unique | 2      | 3       | 649619              | 3          |    nan      |
| top    | note   | comment | (Munterhet i salen) | nb         |    nan      |
| freq   | 637198 | 426659  | 3                   | 649096     |    nan      |
| mean   | nan    | nan     | nan                 | nan        |     11.5595 |
| std    | nan    | nan     | nan                 | nan        |     14.6602 |
| min    | nan    | nan     | nan                 | nan        |      0      |
| 25%    | nan    | nan     | nan                 | nan        |      4      |
| 50%    | nan    | nan     | nan                 | nan        |      5      |
| 75%    | nan    | nan     | nan                 | nan        |     13      |
| max    | nan    | nan     | nan                 | nan        |    670      |


|    | tag   | type    | content                                                      | xml:lang   |   length |
|---:|:------|:--------|:-------------------------------------------------------------|:-----------|---------:|
|  0 | note  | comment | Dag Terje Andersen                                           | nb         |        3 |
|  1 | note  | comment | Dagsorden                                                    | nb         |        1 |
|  2 | note  | comment | (nr. 51):                                                    | nb         |        2 |
|  3 | note  | comment | 1.                                                           | nb         |        1 |
|  4 | note  | comment | Debatt om utenriksministerens utenrikspolitiske redegjørelse | nb         |        5 |


Statistics for tags:

|      |    tag |
|:-----|-------:|
| note | 637198 |
| head |  12833 |


|                     |   type |
|:--------------------|-------:|
| ('head', '')        |  12833 |
| ('note', 'comment') | 426659 |
| ('note', 'speaker') | 210539 |

Translation started.
Translation completed. It took 323.21 minutes for 650031 instances for the entire process of extraction and translation.

|    | tag   | type    | content                                                      | xml:lang   |   length | translation                                                                   | corpus   |
|---:|:------|:--------|:-------------------------------------------------------------|:-----------|---------:|:------------------------------------------------------------------------------|:---------|
|  0 | note  | comment | Dag Terje Andersen                                           | nb         |        3 | Dag Terje Andersen                                                            | NO       |
|  1 | note  | comment | Dagsorden                                                    | nb         |        1 | Agenda                                                                        | NO       |
|  2 | note  | comment | (nr. 51):                                                    | nb         |        2 | (no 51):                                                                      | NO       |
|  3 | note  | comment | 1.                                                           | nb         |        1 | 1st@item: inlistbox                                                           | NO       |
|  4 | note  | comment | Debatt om utenriksministerens utenrikspolitiske redegjørelse | nb         |        5 | Debate on the foreign policy presentation by the Minister for Foreign Affairs | NO       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-NO.notes.translated.tsv
