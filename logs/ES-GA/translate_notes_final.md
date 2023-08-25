2023-05-17 09:27:00.114404: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-05-17 09:27:00.854868: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-05-17 09:27:00.854931: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-05-17 09:27:00.854937: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
Extraction of the notes and translation started.
No. of files: 302.
Statistics before droping duplicates:



|        | tag    | type    | content     | xml:lang   |
|:-------|:-------|:--------|:------------|:-----------|
| count  | 149858 | 149858  | 149858      | 149858     |
| unique | 3      | 7       | 4227        | 1          |
| top    | note   | speaker | (Aplausos.) | gl         |
| freq   | 91441  | 83078   | 32609       | 149858     |


|    | tag   | type    | content                                                                                                                               | xml:lang   |
|---:|:------|:--------|:--------------------------------------------------------------------------------------------------------------------------------------|:-----------|
|  0 | note  | time    | Retómase a sesión ás dez e dous minutos da mañá.                                                                                      | gl         |
|  1 | note  | speaker | O señor PRESIDENTE:                                                                                                                   | gl         |
|  2 | note  |         | (Todos os membros da Cámara e do Goberno, así como os asistentes a esta sesión plenaria, postos en pé, gardan un minuto de silencio.) | gl         |
|  3 | note  | speaker | O señor PRESIDENTE:                                                                                                                   | gl         |
|  4 | note  | speaker | A señora PONTÓN MONDELO:                                                                                                              | gl         |


Statistics for tags:

|         |   tag |
|:--------|------:|
| note    | 91441 |
| kinesic | 32703 |
| vocal   | 25714 |


|                           |   type |
|:--------------------------|-------:|
| ('kinesic', 'applause')   |  32702 |
| ('kinesic', 'laughter')   |      1 |
| ('note', 'speaker')       |  83078 |
| ('note', '')              |   7549 |
| ('note', 'time')          |    814 |
| ('vocal', 'murmuring')    |  23416 |
| ('vocal', 'laughter')     |   1701 |
| ('vocal', 'interruption') |    597 |
Most common notes:

|                                                                                  |   content |
|:---------------------------------------------------------------------------------|----------:|
| (Aplausos.)                                                                      |     32609 |
| O señor PRESIDENTE:                                                              |     27765 |
| (Murmurios.)                                                                     |     11802 |
| O señor PRESIDENTE (Calvo Pouso):                                                |      8140 |
| (Pronúncianse palabras que non se perciben.)                                     |      7802 |
| A señora PRESIDENTA:                                                             |      5499 |
| O señor PRESIDENTE DA XUNTA DE GALICIA (Núñez Feijóo):                           |      2189 |
| O señor PRESIDENTE (Santalices Vieira):                                          |      1970 |
| (Unha persoa dos servizos de limpeza da Cámara procede a desinfectar o estrado.) |      1876 |
| (Risos.)                                                                         |      1679 |
| A señora PRADO CORES:                                                            |      1484 |
| A señora PONTÓN MONDELO:                                                         |      1200 |
| O señor SÁNCHEZ GARCÍA:                                                          |      1140 |
| A señora PRESAS BERGANTIÑOS:                                                     |      1042 |
| O señor BARÁ TORRES:                                                             |       996 |
| A señora PRESIDENTA (Rodríguez Arias):                                           |       934 |
| (Pausa.)                                                                         |       919 |
| O señor LOSADA ÁLVAREZ:                                                          |       873 |
| O señor TELLADO FILGUEIRA:                                                       |       868 |
| O señor TORRADO QUINTELA:                                                        |       795 |
Statistics after deduplication:

Number of words in the notes: 296429

|        | tag   | type   | content                                          | xml:lang   |    length |
|:-------|:------|:-------|:-------------------------------------------------|:-----------|----------:|
| count  | 4227  | 4227   | 4227                                             | 4227       | 4227      |
| unique | 3     | 7      | 4227                                             | 1          |  nan      |
| top    | note  |        | Retómase a sesión ás dez e dous minutos da mañá. | gl         |  nan      |
| freq   | 3894  | 3009   | 1                                                | 4227       |  nan      |
| mean   | nan   | nan    | nan                                              | nan        |   70.1275 |
| std    | nan   | nan    | nan                                              | nan        |  116.088  |
| min    | nan   | nan    | nan                                              | nan        |    1      |
| 25%    | nan   | nan    | nan                                              | nan        |    9      |
| 50%    | nan   | nan    | nan                                              | nan        |   12      |
| 75%    | nan   | nan    | nan                                              | nan        |  109      |
| max    | nan   | nan    | nan                                              | nan        | 2028      |


|    | tag   | type    | content                                                                                                                               | xml:lang   |   length |
|---:|:------|:--------|:--------------------------------------------------------------------------------------------------------------------------------------|:-----------|---------:|
|  0 | note  | time    | Retómase a sesión ás dez e dous minutos da mañá.                                                                                      | gl         |       10 |
|  1 | note  | speaker | O señor PRESIDENTE:                                                                                                                   | gl         |        3 |
|  2 | note  |         | (Todos os membros da Cámara e do Goberno, así como os asistentes a esta sesión plenaria, postos en pé, gardan un minuto de silencio.) | gl         |       24 |
|  4 | note  | speaker | A señora PONTÓN MONDELO:                                                                                                              | gl         |        4 |
|  6 | note  | speaker | O señor PRESIDENTE DA XUNTA DE GALICIA (Núñez Feijóo):                                                                                | gl         |        9 |


Statistics for tags:

|         |   tag |
|:--------|------:|
| note    |  3894 |
| vocal   |   312 |
| kinesic |    21 |


|                           |   type |
|:--------------------------|-------:|
| ('kinesic', 'applause')   |     20 |
| ('kinesic', 'laughter')   |      1 |
| ('note', '')              |   3009 |
| ('note', 'time')          |    540 |
| ('note', 'speaker')       |    345 |
| ('vocal', 'murmuring')    |    290 |
| ('vocal', 'interruption') |     12 |
| ('vocal', 'laughter')     |     10 |
Translation started.
Translation completed. It took 7.61 minutes for 4227 instances for the entire process of extraction and translation.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
|    | tag   | type    | content                                                                                                                               | xml:lang   |   length | translation                                                                                                                            | corpus   |
|---:|:------|:--------|:--------------------------------------------------------------------------------------------------------------------------------------|:-----------|---------:|:---------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | note  | time    | Retómase a sesión ás dez e dous minutos da mañá.                                                                                      | gl         |       10 | The session is resumed at ten in the morning.                                                                                          | ES-GA    |
|  1 | note  | speaker | O señor PRESIDENTE:                                                                                                                   | gl         |        3 | Mr. President:                                                                                                                         | ES-GA    |
|  2 | note  |         | (Todos os membros da Cámara e do Goberno, así como os asistentes a esta sesión plenaria, postos en pé, gardan un minuto de silencio.) | gl         |       24 | (All members of the House and of the Government, as well as those attending this plenary session, standing, keep a minute of silence.) | ES-GA    |
|  4 | note  | speaker | A señora PONTÓN MONDELO:                                                                                                              | gl         |        4 | Mrs. MONDELO:                                                                                                                          | ES-GA    |
|  6 | note  | speaker | O señor PRESIDENTE DA XUNTA DE GALICIA (Núñez Feijóo):                                                                                | gl         |        9 | THE PRESIDENT OF THE GALICIA COMMITTEE (Nunez Feijóo):                                                                                 | ES-GA    |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-ES-GA.notes.translated.tsv
