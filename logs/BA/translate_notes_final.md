2023-05-12 09:24:18.219554: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-05-12 09:24:18.944974: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-05-12 09:24:18.945041: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-05-12 09:24:18.945047: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Extraction of the notes and translation started.
No. of files: 743.
Statistics before droping duplicates:



|        | tag    | type    | content           | xml:lang   |
|:-------|:-------|:--------|:------------------|:-----------|
| count  | 133488 | 133488  | 133488            | 133488     |
| unique | 5      | 7       | 939               | 1          |
| top    | note   | speaker | Džaferović, Šefik | bs         |
| freq   | 126326 | 126286  | 8822              | 133488     |


|    | tag   | type    | content          | xml:lang   |
|---:|:------|:--------|:-----------------|:-----------|
|  0 | note  | speaker | Bećirović, Denis | bs         |
|  1 | note  | speaker | Belkić, Beriz    | bs         |
|  2 | note  | speaker | Bećirović, Denis | bs         |
|  3 | note  | speaker | Belkić, Beriz    | bs         |
|  4 | note  | speaker | Bećirović, Denis | bs         |


Statistics for tags:

|          |    tag |
|:---------|-------:|
| note     | 126326 |
| gap      |   3679 |
| incident |   1864 |
| vocal    |   1539 |
| kinesic  |     80 |


|                           |   type |
|:--------------------------|-------:|
| ('gap', 'inaudible')      |   3679 |
| ('incident', 'pause')     |    988 |
| ('incident', 'action')    |    876 |
| ('kinesic', 'applause')   |     80 |
| ('note', 'speaker')       | 126286 |
| ('note', 'time')          |     40 |
| ('vocal', 'interruption') |   1539 |
Most common notes:

|                          |   content |
|:-------------------------|----------:|
| Džaferović, Šefik        |      8822 |
| Živković, Milorad        |      7946 |
| Belkić, Beriz            |      6780 |
| Špirić, Nikola           |      5445 |
| Bećirović, Denis         |      5436 |
| Krišto, Borjana          |      5131 |
| Raguž, Martin            |      3929 |
| Lozančić, Niko           |      3483 |
| Bosić, Mladen            |      3300 |
| /nije uključen mikrofon/ |      3131 |
| Majkić, Dušanka          |      2257 |
| Ljubić, Božo             |      2042 |
| Filipović, Ilija         |      1971 |
| Novaković, Momčilo       |      1922 |
| Genjac, Halid            |      1858 |
| Banjac, Mirko            |      1806 |
| Tadić, Ognjen            |      1687 |
| Pamuk, Mustafa           |      1601 |
| Radmanović, Nebojša      |      1580 |
| Lagumdžija, Zlatko       |      1518 |
Statistics after deduplication:

Number of words in the notes: 2857

|        | tag   | type    | content          | xml:lang   |    length |
|:-------|:------|:--------|:-----------------|:-----------|----------:|
| count  | 939   | 939     | 939              | 939        | 939       |
| unique | 5     | 7       | 939              | 1          | nan       |
| top    | note  | speaker | Bećirović, Denis | bs         | nan       |
| freq   | 630   | 608     | 1                | 939        | nan       |
| mean   | nan   | nan     | nan              | nan        |   3.0426  |
| std    | nan   | nan     | nan              | nan        |   2.10905 |
| min    | nan   | nan     | nan              | nan        |   1       |
| 25%    | nan   | nan     | nan              | nan        |   2       |
| 50%    | nan   | nan     | nan              | nan        |   2       |
| 75%    | nan   | nan     | nan              | nan        |   3       |
| max    | nan   | nan     | nan              | nan        |  18       |


|    | tag   | type    | content              | xml:lang   |   length |
|---:|:------|:--------|:---------------------|:-----------|---------:|
|  0 | note  | speaker | Bećirović, Denis     | bs         |        2 |
|  1 | note  | speaker | Belkić, Beriz        | bs         |        2 |
|  5 | note  | speaker | Hadžiahmetović, Azra | bs         |        2 |
|  7 | note  | speaker | Fazlić, Amir         | bs         |        2 |
|  9 | note  | speaker | Mehmedović, Šemsudin | bs         |        2 |


Statistics for tags:

|          |   tag |
|:---------|------:|
| note     |   630 |
| gap      |   147 |
| vocal    |   109 |
| incident |    47 |
| kinesic  |     6 |


|                           |   type |
|:--------------------------|-------:|
| ('gap', 'inaudible')      |    147 |
| ('incident', 'action')    |     39 |
| ('incident', 'pause')     |      8 |
| ('kinesic', 'applause')   |      6 |
| ('note', 'speaker')       |    608 |
| ('note', 'time')          |     22 |
| ('vocal', 'interruption') |    109 |
Translation started.
Translation completed. It took 0.98 minutes for 939 instances for the entire process of extraction and translation.

|    | tag   | type    | content              | xml:lang   |   length | translation           | corpus   |
|---:|:------|:--------|:---------------------|:-----------|---------:|:----------------------|:---------|
|  0 | note  | speaker | Bećirović, Denis     | bs         |        2 | Becirović, Denis      | BA       |
|  1 | note  | speaker | Belkić, Beriz        | bs         |        2 | Belkić, Beriz         | BA       |
|  5 | note  | speaker | Hadžiahmetović, Azra | bs         |        2 | Hadjiahmetović, Azra  | BA       |
|  7 | note  | speaker | Fazlić, Amir         | bs         |        2 | Fazlic, Amir          | BA       |
|  9 | note  | speaker | Mehmedović, Šemsudin | bs         |        2 | Mehmedović, Shemsudin | BA       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-BA.notes.translated.tsv
