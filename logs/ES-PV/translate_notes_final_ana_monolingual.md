2023-10-10 08:58:31.071594: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-10-10 08:58:31.683843: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-10-10 08:58:31.683903: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-10-10 08:58:31.683910: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Extraction of the notes and translation started.
No. of files: 338.
Statistics before droping duplicates:



|        | tag   | type    | content        | xml:lang   |
|:-------|:------|:--------|:---------------|:-----------|
| count  | 47882 | 47882   | 47882          | 47882      |
| unique | 1     | 2       | 639            | 1          |
| top    | note  | speaker | LEHENDAKARIAK: | eu         |
| freq   | 47882 | 39148   | 20699          | 47882      |


|    | tag   | type    | content                          | xml:lang   |
|---:|:------|:--------|:---------------------------------|:-----------|
|  0 | note  | speaker | LEHENDAKARIAK (Tejeria Otermin): | eu         |
|  1 | note  | speaker | DAMBORENEA BASTERRECHEA jaunak:  | eu         |
|  2 | note  | speaker | LEHENDAKARIAK:                   | eu         |
|  3 | note  | speaker | CASTELO DE SA andreak:           | eu         |
|  4 | note  | speaker | LEHENDAKARIAK:                   | eu         |


Statistics for tags:

|      |   tag |
|:-----|------:|
| note | 47882 |


|                     |   type |
|:--------------------|-------:|
| ('note', 'speaker') |  39148 |
| ('note', '')        |   8734 |
Most common notes:

|                                                 |   content |
|:------------------------------------------------|----------:|
| LEHENDAKARIAK:                                  |     20699 |
| Geldiunea                                       |      2476 |
| JAURLARITZAKO LEHENDAKARIAK (Urkullu Renteria): |       878 |
| BARRIO BAROJA jaunak:                           |       604 |
| GARRIDO KNÖRR andreak:                          |       534 |
| MANEIRO LABAYEN jaunak:                         |       479 |
| UBERA ARANZETA andreak:                         |       433 |
| LEHENDAKARIAK (Tejeria Otermin):                |       389 |
| HERNÁNDEZ HIDALGO jaunak:                       |       380 |
| Berbotsa                                        |       378 |
| MARTÍNEZ GRISALEÑA andreak:                     |       363 |
| CASANOVA ALONSO jaunak:                         |       348 |
| LLANOS GÓMEZ andreak:                           |       339 |
| LÓPEZ DE OCARIZ LÓPEZ DE MUNAIN andreak:        |       335 |
| BECERRA CAROLLO jaunak:                         |       284 |
| MARTÍNEZ ZATÓN jaunak:                          |       275 |
| CORCUERA LEUNDA andreak:                        |       244 |
| SÁNCHEZ MARTÍN andreak:                         |       241 |
| OTERO GABIRONDO jaunak:                         |       236 |
| DAMBORENEA BASTERRECHEA jaunak:                 |       232 |
Statistics after deduplication:

Number of words in the notes: 2578

|        | tag   | type    | content                          | xml:lang   |    length |
|:-------|:------|:--------|:---------------------------------|:-----------|----------:|
| count  | 639   | 639     | 639                              | 639        | 639       |
| unique | 1     | 2       | 639                              | 1          | nan       |
| top    | note  | speaker | LEHENDAKARIAK (Tejeria Otermin): | eu         | nan       |
| freq   | 639   | 354     | 1                                | 639        | nan       |
| mean   | nan   | nan     | nan                              | nan        |   4.03443 |
| std    | nan   | nan     | nan                              | nan        |   3.60452 |
| min    | nan   | nan     | nan                              | nan        |   1       |
| 25%    | nan   | nan     | nan                              | nan        |   3       |
| 50%    | nan   | nan     | nan                              | nan        |   3       |
| 75%    | nan   | nan     | nan                              | nan        |   4       |
| max    | nan   | nan     | nan                              | nan        |  60       |


|    | tag   | type    | content                          | xml:lang   |   length |
|---:|:------|:--------|:---------------------------------|:-----------|---------:|
|  0 | note  | speaker | LEHENDAKARIAK (Tejeria Otermin): | eu         |        3 |
|  1 | note  | speaker | DAMBORENEA BASTERRECHEA jaunak:  | eu         |        3 |
|  2 | note  | speaker | LEHENDAKARIAK:                   | eu         |        1 |
|  3 | note  | speaker | CASTELO DE SA andreak:           | eu         |        4 |
|  6 | note  | speaker | BOLLAIN URBIETA jaunak:          | eu         |        3 |


Statistics for tags:

|      |   tag |
|:-----|------:|
| note |   639 |


|                     |   type |
|:--------------------|-------:|
| ('note', 'speaker') |    354 |
| ('note', '')        |    285 |
Translation started.
Translation completed. It took 22.44 minutes for 639 instances for the entire process of extraction and translation.
|    | tag   | type    | content                          | xml:lang   |   length | translation               | corpus   |
|---:|:------|:--------|:---------------------------------|:-----------|---------:|:--------------------------|:---------|
|  0 | note  | speaker | LEHENDAKARIAK (Tejeria Otermin): | eu         |        3 | DEGREES (Elegia Otermin): | ES-PV    |
|  1 | note  | speaker | DAMBORENEA BASTERRECHEA jaunak:  | eu         |        3 | Mr. DAMBOLACE:            | ES-PV    |
|  2 | note  | speaker | LEHENDAKARIAK:                   | eu         |        1 | DEBABES:                  | ES-PV    |
|  3 | note  | speaker | CASTELO DE SA andreak:           | eu         |        4 | Mrs. CASTEL DE SAA:       | ES-PV    |
|  6 | note  | speaker | BOLLAIN URBIETA jaunak:          | eu         |        3 | Mr. BLOLAIN URBIET:       | ES-PV    |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-ES-PV.notes.translated.ana.tsv
