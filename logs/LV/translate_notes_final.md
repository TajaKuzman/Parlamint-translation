2023-05-12 14:49:30.061055: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-05-12 14:49:30.812752: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-05-12 14:49:30.812826: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-05-12 14:49:30.812832: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Extraction of the notes and translation started.
No. of files: 635.
Statistics before droping duplicates:



|        | tag    | type    | content         | xml:lang   |
|:-------|:-------|:--------|:----------------|:-----------|
| count  | 163720 | 163720  | 163720          | 163720     |
| unique | 1      | 1       | 798             | 1          |
| top    | note   | speaker | Sēdes vadītāja. | lv         |
| freq   | 163720 | 163720  | 76874           | 163720     |


|    | tag   | type    | content                                                                         | xml:lang   |
|---:|:------|:--------|:--------------------------------------------------------------------------------|:-----------|
|  0 | note  | speaker | Sēdi vada Latvijas Republikas 12.Saeimas priekšsēdētājas biedrs Gundars Daudze. | lv         |
|  1 | note  | speaker | Sēdes vadītājs.                                                                 | lv         |
|  2 | note  | speaker | O.Ē.Kalniņš (VIENOTĪBA).                                                        | lv         |
|  3 | note  | speaker | Sēdes vadītājs.                                                                 | lv         |
|  4 | note  | speaker | O.Ē.Kalniņš.                                                                    | lv         |


Statistics for tags:

|      |    tag |
|:-----|-------:|
| note | 163720 |


|                     |   type |
|:--------------------|-------:|
| ('note', 'speaker') | 163720 |
Most common notes:

|                                                     |   content |
|:----------------------------------------------------|----------:|
| Sēdes vadītāja.                                     |     76874 |
| Sēdes vadītājs.                                     |      5155 |
| K.Šadurskis.                                        |      2694 |
| M. Bondars.                                         |      2430 |
| M. Šteins.                                          |      1538 |
| V. Valainis (ZZS).                                  |      1409 |
| G.Bērziņš.                                          |      1407 |
| J.Vucāns.                                           |      1396 |
| I.Parādnieks.                                       |      1392 |
| E.Smiltēns.                                         |      1336 |
| A. Ašeradens.                                       |      1334 |
| E.Putra.                                            |      1226 |
| G.Kūtris.                                           |      1109 |
| J. Stepaņenko (pie frakcijām nepiederoša deputāte). |      1056 |
| A. Gobzems (pie frakcijām nepiederošs deputāts).    |       948 |
| K. Feldmans.                                        |       872 |
| J. Rancāns.                                         |       847 |
| I.Dālderis.                                         |       843 |
| A. T. Plešs.                                        |       820 |
| J. Butāns.                                          |       757 |
Statistics after deduplication:

Number of words in the notes: 2333

|        | tag   | type    | content                                                                         | xml:lang   |    length |
|:-------|:------|:--------|:--------------------------------------------------------------------------------|:-----------|----------:|
| count  | 798   | 798     | 798                                                                             | 798        | 798       |
| unique | 1     | 1       | 798                                                                             | 1          | nan       |
| top    | note  | speaker | Sēdi vada Latvijas Republikas 12.Saeimas priekšsēdētājas biedrs Gundars Daudze. | lv         | nan       |
| freq   | 798   | 798     | 1                                                                               | 798        | nan       |
| mean   | nan   | nan     | nan                                                                             | nan        |   2.92356 |
| std    | nan   | nan     | nan                                                                             | nan        |   1.84681 |
| min    | nan   | nan     | nan                                                                             | nan        |   1       |
| 25%    | nan   | nan     | nan                                                                             | nan        |   2       |
| 50%    | nan   | nan     | nan                                                                             | nan        |   2       |
| 75%    | nan   | nan     | nan                                                                             | nan        |   3       |
| max    | nan   | nan     | nan                                                                             | nan        |  11       |


|    | tag   | type    | content                                                                         | xml:lang   |   length |
|---:|:------|:--------|:--------------------------------------------------------------------------------|:-----------|---------:|
|  0 | note  | speaker | Sēdi vada Latvijas Republikas 12.Saeimas priekšsēdētājas biedrs Gundars Daudze. | lv         |        9 |
|  1 | note  | speaker | Sēdes vadītājs.                                                                 | lv         |        2 |
|  2 | note  | speaker | O.Ē.Kalniņš (VIENOTĪBA).                                                        | lv         |        2 |
|  4 | note  | speaker | O.Ē.Kalniņš.                                                                    | lv         |        1 |
| 14 | note  | speaker | J.Stepaņenko (SASKAŅA).                                                         | lv         |        2 |


Statistics for tags:

|      |   tag |
|:-----|------:|
| note |   798 |


|                     |   type |
|:--------------------|-------:|
| ('note', 'speaker') |    798 |
Translation started.
Translation completed. It took 1.24 minutes for 798 instances for the entire process of extraction and translation.
|    | tag   | type    | content                                                                         | xml:lang   |   length | translation                                                                                                    | corpus   |
|---:|:------|:--------|:--------------------------------------------------------------------------------|:-----------|---------:|:---------------------------------------------------------------------------------------------------------------|:---------|
|  0 | note  | speaker | Sēdi vada Latvijas Republikas 12.Saeimas priekšsēdētājas biedrs Gundars Daudze. | lv         |        9 | The meeting is chaired by Gundars Dauge, Member of the President of the 12th Saeima of the Republic of Latvia. | LV       |
|  1 | note  | speaker | Sēdes vadītājs.                                                                 | lv         |        2 | Head of the sitting.                                                                                           | LV       |
|  2 | note  | speaker | O.Ē.Kalniņš (VIENOTĪBA).                                                        | lv         |        2 | O.E.K. (MANNITY)                                                                                               | LV       |
|  4 | note  | speaker | O.Ē.Kalniņš.                                                                    | lv         |        1 | Oh, my God.                                                                                                    | LV       |
| 14 | note  | speaker | J.Stepaņenko (SASKAŅA).                                                         | lv         |        2 | J. Stepanenko.                                                                                                 | LV       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-LV.notes.translated.tsv
