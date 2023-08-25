2023-05-30 07:47:24.745699: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-05-30 07:47:25.502497: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-05-30 07:47:25.502559: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-05-30 07:47:25.502566: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Extraction of the notes and translation started.
No. of files: 1317.
Statistics before droping duplicates:



|        | tag    | type    | content    | xml:lang   |
|:-------|:-------|:--------|:-----------|:-----------|
| count  | 233814 | 233814  | 233814     | 233814     |
| unique | 1      | 3       | 1445       | 1          |
| top    | note   | speaker | Jüri Ratas | et         |
| freq   | 233814 | 227872  | 14474      | 233814     |


|    | tag   | type    | content           | xml:lang   |
|---:|:------|:--------|:------------------|:-----------|
|  0 | note  | speaker | EneErgma          | et         |
|  1 | note  | speaker | HeiliTõnisson     | et         |
|  2 | note  | speaker | EneErgma          | et         |
|  3 | note  | speaker | MihhailStalnuhhin | et         |
|  4 | note  | speaker | EneErgma          | et         |


Statistics for tags:

|      |    tag |
|:-----|-------:|
| note | 233814 |


|                     |   type |
|:--------------------|-------:|
| ('note', 'speaker') | 227872 |
| ('note', '')        |   5919 |
| ('note', 'comment') |     23 |
Most common notes:

|                     |   content |
|:--------------------|----------:|
| Jüri Ratas          |     14474 |
| Eiki Nestor         |     14427 |
| Hanno Pevkur        |     10122 |
| Helir-Valdor Seeder |     10105 |
| LaineRandjärv       |      9158 |
| EneErgma            |      7858 |
| Martin Helme        |      7628 |
| Henn Põlluaas       |      7298 |
| JüriRatas           |      7261 |
| Enn Eesmaa          |      6651 |
| Siim Kallas         |      3261 |
| Taavi Rõivas        |      2858 |
| Peeter Ernits       |      2779 |
| EikiNestor          |      2556 |
| Kalle Laanet        |      2200 |
| Jürgen Ligi         |      1985 |
| Mart Helme          |      1916 |
| Laine Randjärv      |      1844 |
| Kaja Kallas         |      1831 |
| Aivar Kokk          |      1760 |
Statistics after deduplication:

Number of words in the notes: 4371

|        | tag   | type   | content                            | xml:lang   |     length |
|:-------|:------|:-------|:-----------------------------------|:-----------|-----------:|
| count  | 1446  | 1446   | 1446                               | 1446       | 1446       |
| unique | 1     | 3      | 1445                               | 1          |  nan       |
| top    | note  |        | (Lauldakse Eesti Vabariigi hümni.) | et         |  nan       |
| freq   | 1446  | 793    | 2                                  | 1446       |  nan       |
| mean   | nan   | nan    | nan                                | nan        |    3.02282 |
| std    | nan   | nan    | nan                                | nan        |    2.15333 |
| min    | nan   | nan    | nan                                | nan        |    1       |
| 25%    | nan   | nan    | nan                                | nan        |    2       |
| 50%    | nan   | nan    | nan                                | nan        |    2       |
| 75%    | nan   | nan    | nan                                | nan        |    4       |
| max    | nan   | nan    | nan                                | nan        |   17       |


|    | tag   | type    | content           | xml:lang   |   length |
|---:|:------|:--------|:------------------|:-----------|---------:|
|  0 | note  | speaker | EneErgma          | et         |        1 |
|  1 | note  | speaker | HeiliTõnisson     | et         |        1 |
|  3 | note  | speaker | MihhailStalnuhhin | et         |        1 |
|  5 | note  | speaker | KadriSimson       | et         |        1 |
|  7 | note  | speaker | AndresAnvelt      | et         |        1 |


Statistics for tags:

|      |   tag |
|:-----|------:|
| note |  1446 |


|                     |   type |
|:--------------------|-------:|
| ('note', '')        |    793 |
| ('note', 'speaker') |    643 |
| ('note', 'comment') |     10 |
Translation started.
Translation completed. It took 2.03 minutes for 1446 instances for the entire process of extraction and translation.
|    | tag   | type    | content           | xml:lang   |   length | translation       | corpus   |
|---:|:------|:--------|:------------------|:-----------|---------:|:------------------|:---------|
|  0 | note  | speaker | EneErgma          | et         |        1 | EneErgma          | EE       |
|  1 | note  | speaker | HeiliTõnisson     | et         |        1 | HeiliTõnisson     | EE       |
|  3 | note  | speaker | MihhailStalnuhhin | et         |        1 | MikhailStalnukhin | EE       |
|  5 | note  | speaker | KadriSimson       | et         |        1 | KadriSimson       | EE       |
|  7 | note  | speaker | AndresAnvelt      | et         |        1 | AndresAnvelt      | EE       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-EE.notes.translated.tsv
