2023-03-30 10:03:49.318046: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-03-30 10:03:49.972454: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-03-30 10:03:49.972526: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-03-30 10:03:49.972533: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Extraction of the notes and translation started.
No. of files: 1708.
Statistics before droping duplicates:



|        | tag    | type    | content        | xml:lang   |
|:-------|:-------|:--------|:---------------|:-----------|
| count  | 579103 | 579103  | 579103         | 579103     |
| unique | 5      | 7       | 13444          | 1          |
| top    | note   | speaker | Reiner, Željko |            |
| freq   | 498874 | 497196  | 42021          | 579103     |


|    | tag   | type    | content          | xml:lang   |
|---:|:------|:--------|:-----------------|:-----------|
|  0 | note  | speaker | Zgrebec, Dragica |            |
|  1 | note  | speaker | Vrdoljak, Ivan   |            |
|  2 | note  | speaker | Zgrebec, Dragica |            |
|  3 | note  | speaker | Bačić, Branko    |            |
|  4 | note  | speaker | Zgrebec, Dragica |            |


Statistics for tags:

|          |    tag |
|:---------|-------:|
| note     | 498874 |
| gap      |  51084 |
| vocal    |  27487 |
| kinesic  |   1651 |
| incident |      7 |


|                           |   type |
|:--------------------------|-------:|
| ('gap', 'inaudible')      |  51084 |
| ('incident', 'action')    |      7 |
| ('kinesic', 'applause')   |   1651 |
| ('note', 'speaker')       | 497196 |
| ('note', 'time')          |   1678 |
| ('vocal', 'interruption') |  27482 |
| ('vocal', 'murmuring')    |      5 |
Most common notes:

|                            |   content |
|:---------------------------|----------:|
| Reiner, Željko             |     42021 |
| Šeks, Vladimir             |     37467 |
| Jandroković, Gordan        |     27078 |
| /Govornik se ne razumije./ |     25010 |
| Bebić, Luka                |     19705 |
| Radin, Furio               |     19704 |
| Zgrebec, Dragica           |     15444 |
| Leko, Josip                |     15254 |
| Stazić, Nenad              |     13277 |
| Sanader, Ante              |     11609 |
| Brkić, Milijan             |     11484 |
| Batinić, Milorad           |      9071 |
| Jarnjak, Ivan              |      8207 |
| Bulj, Miro                 |      5861 |
| Petrov, Božo               |      5765 |
| Hajdaš Dončić, Siniša      |      5594 |
| /Upadica se ne razumije./  |      5338 |
| /Upadica se ne čuje./      |      5226 |
| Milinović, Darko           |      5121 |
| Maras, Gordan              |      4565 |
Statistics after deduplication:

Number of words in the notes: 82630

|        | tag   | type         | content          | xml:lang   |      length |
|:-------|:------|:-------------|:-----------------|:-----------|------------:|
| count  | 13444 | 13444        | 13444            | 13444      | 13444       |
| unique | 5     | 7            | 13444            | 1          |   nan       |
| top    | vocal | interruption | Zgrebec, Dragica |            |   nan       |
| freq   | 10917 | 10913        | 1                | 13444      |   nan       |
| mean   | nan   | nan          | nan              | nan        |     6.14624 |
| std    | nan   | nan          | nan              | nan        |     3.95745 |
| min    | nan   | nan          | nan              | nan        |     1       |
| 25%    | nan   | nan          | nan              | nan        |     4       |
| 50%    | nan   | nan          | nan              | nan        |     5       |
| 75%    | nan   | nan          | nan              | nan        |     7       |
| max    | nan   | nan          | nan              | nan        |    36       |


|    | tag   | type    | content          | xml:lang   |   length |
|---:|:------|:--------|:-----------------|:-----------|---------:|
|  0 | note  | speaker | Zgrebec, Dragica |            |        2 |
|  1 | note  | speaker | Vrdoljak, Ivan   |            |        2 |
|  3 | note  | speaker | Bačić, Branko    |            |        2 |
|  7 | note  | speaker | Šuker, Ivan      |            |        2 |
| 11 | note  | speaker | Matušić, Frano   |            |        2 |


Statistics for tags:

|          |   tag |
|:---------|------:|
| vocal    | 10917 |
| note     |  1727 |
| gap      |   788 |
| kinesic  |    11 |
| incident |     1 |


|                           |   type |
|:--------------------------|-------:|
| ('gap', 'inaudible')      |    788 |
| ('incident', 'action')    |      1 |
| ('kinesic', 'applause')   |     11 |
| ('note', 'speaker')       |   1034 |
| ('note', 'time')          |    693 |
| ('vocal', 'interruption') |  10913 |
| ('vocal', 'murmuring')    |      4 |
Translation started.
Translation completed. It took 9.34 minutes for 13444 instances for the entire process of extraction and translation.
|    | tag   | type    | content          | xml:lang   |   length | translation     |
|---:|:------|:--------|:-----------------|:-----------|---------:|:----------------|
|  0 | note  | speaker | Zgrebec, Dragica |            |        2 | Zrebec, Darling |
|  1 | note  | speaker | Vrdoljak, Ivan   |            |        2 | Vrdoljak, Ivan  |
|  3 | note  | speaker | Bačić, Branko    |            |        2 | Bačić, Branko   |
|  7 | note  | speaker | Šuker, Ivan      |            |        2 | Shuker, Ivan    |
| 11 | note  | speaker | Matušić, Frano   |            |        2 | Matušić, Frano  |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-HR.notes.translated.csv
