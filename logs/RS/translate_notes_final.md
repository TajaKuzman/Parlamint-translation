2023-05-15 08:38:19.588625: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-05-15 08:38:20.670600: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-05-15 08:38:20.670664: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-05-15 08:38:20.670670: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Extraction of the notes and translation started.
No. of files: 2060.
Statistics before droping duplicates:



|        | tag    | type    | content        | xml:lang   |
|:-------|:-------|:--------|:---------------|:-----------|
| count  | 324686 | 324686  | 324686         | 324686     |
| unique | 5      | 10      | 3288           | 1          |
| top    | note   | speaker | Gojković, Maja | sr         |
| freq   | 318697 | 316071  | 20543          | 324686     |


|    | tag   | type    | content             | xml:lang   |
|---:|:------|:--------|:--------------------|:-----------|
|  0 | note  | speaker | Stefanović, Nebojša | sr         |
|  1 | note  | speaker | Veselinović, Janko  | sr         |
|  2 | note  | speaker | Stefanović, Nebojša | sr         |
|  3 | note  | speaker | Veselinović, Janko  | sr         |
|  4 | note  | speaker | Kovač, Vesna        | sr         |


Statistics for tags:

|          |    tag |
|:---------|-------:|
| note     | 318697 |
| kinesic  |   2390 |
| gap      |   1786 |
| vocal    |   1710 |
| incident |    103 |


|                           |   type |
|:--------------------------|-------:|
| ('gap', 'inaudible')      |   1786 |
| ('incident', 'pause')     |     98 |
| ('incident', 'action')    |      5 |
| ('kinesic', 'applause')   |   2390 |
| ('note', 'speaker')       | 316071 |
| ('note', 'time')          |   2622 |
| ('note', 'comment')       |      4 |
| ('vocal', 'interruption') |   1031 |
| ('vocal', 'murmuring')    |    503 |
| ('vocal', 'laughter')     |    176 |
Most common notes:

|                          |   content |
|:-------------------------|----------:|
| Gojković, Maja           |     20543 |
| Čomić, Gordana           |     20434 |
| Arsić, Veroljub          |     16086 |
| Đukić-Dejanović, Slavica |     15050 |
| Bečić, Igor              |     12019 |
| Marinković, Vladimir     |      9134 |
| Mićić, Nataša            |      7221 |
| Milićević, Đorđe         |      6752 |
| Marković, Predrag        |      6209 |
| Arsenović, Konstantin    |      6116 |
| Kovač, Vesna             |      5833 |
| Stefanović, Nebojša      |      5522 |
| Maršićanin, Dragan       |      5268 |
| Novaković, Nikola        |      4242 |
| Mihailović, Vojislav     |      4060 |
| Radeta, Vjerica          |      3579 |
| Krasić, Zoran            |      3451 |
| Rističević, Marijan      |      3285 |
| Orlić, Vladimir          |      2993 |
| Nikolić, Tomislav        |      2854 |
Statistics after deduplication:

Number of words in the notes: 14247

|        | tag   | type    | content             | xml:lang   |     length |
|:-------|:------|:--------|:--------------------|:-----------|-----------:|
| count  | 3288  | 3288    | 3288                | 3288       | 3288       |
| unique | 5     | 10      | 3288                | 1          |  nan       |
| top    | note  | speaker | Stefanović, Nebojša | sr         |  nan       |
| freq   | 2060  | 1495    | 1                   | 3288       |  nan       |
| mean   | nan   | nan     | nan                 | nan        |    4.33303 |
| std    | nan   | nan     | nan                 | nan        |    3.05384 |
| min    | nan   | nan     | nan                 | nan        |    1       |
| 25%    | nan   | nan     | nan                 | nan        |    2       |
| 50%    | nan   | nan     | nan                 | nan        |    3       |
| 75%    | nan   | nan     | nan                 | nan        |    6       |
| max    | nan   | nan     | nan                 | nan        |   25       |


|    | tag   | type    | content             | xml:lang   |   length |
|---:|:------|:--------|:--------------------|:-----------|---------:|
|  0 | note  | speaker | Stefanović, Nebojša | sr         |        2 |
|  1 | note  | speaker | Veselinović, Janko  | sr         |        2 |
|  4 | note  | speaker | Kovač, Vesna        | sr         |        2 |
|  9 | note  | speaker | Krstić, Lazar       | sr         |        2 |
| 11 | note  | speaker | Đurić, Bojan        | sr         |        2 |


Statistics for tags:

|          |   tag |
|:---------|------:|
| note     |  2060 |
| vocal    |   957 |
| gap      |   105 |
| kinesic  |    94 |
| incident |    72 |


|                           |   type |
|:--------------------------|-------:|
| ('gap', 'inaudible')      |    105 |
| ('incident', 'pause')     |     70 |
| ('incident', 'action')    |      2 |
| ('kinesic', 'applause')   |     94 |
| ('note', 'speaker')       |   1495 |
| ('note', 'time')          |    564 |
| ('note', 'comment')       |      1 |
| ('vocal', 'interruption') |    881 |
| ('vocal', 'murmuring')    |     53 |
| ('vocal', 'laughter')     |     23 |
Translation started.
Translation completed. It took 3.9 minutes for 3288 instances for the entire process of extraction and translation.
|    | tag   | type    | content             | xml:lang   |   length | translation         | corpus   |
|---:|:------|:--------|:--------------------|:-----------|---------:|:--------------------|:---------|
|  0 | note  | speaker | Stefanović, Nebojša | sr         |        2 | Stefanović, Nebojsa | RS       |
|  1 | note  | speaker | Veselinović, Janko  | sr         |        2 | Veselinović, Janko  | RS       |
|  4 | note  | speaker | Kovač, Vesna        | sr         |        2 | Blacksmith, Vesna   | RS       |
|  9 | note  | speaker | Krstić, Lazar       | sr         |        2 | Krstic, Lazar       | RS       |
| 11 | note  | speaker | Đurić, Bojan        | sr         |        2 | Đurić, Bojan        | RS       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-RS.notes.translated.tsv
