2023-08-22 09:31:06.849803: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-08-22 09:31:07.407623: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-08-22 09:31:07.407690: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-08-22 09:31:07.407697: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
Extraction of the notes and translation started.
No. of files: 450.
Statistics before droping duplicates:



|        | tag     | type     | content   | xml:lang   |
|:-------|:--------|:---------|:----------|:-----------|
| count  | 80402   | 80402    | 80402     | 80402      |
| unique | 6       | 17       | 10739     | 1          |
| top    | kinesic | applause | Aplausos  | es         |
| freq   | 46629   | 42472    | 35236     | 80402      |


|    | tag   | type    | content                         | xml:lang   |
|---:|:------|:--------|:--------------------------------|:-----------|
|  0 | note  | comment | EAJ-PNV                         | es         |
|  1 | note  | comment | EAJ-PNV                         | es         |
|  2 | note  | comment | SEÑOR MARTÍNEZ OBLANCA          | es         |
|  3 | note  | comment | Número de expediente 173/000056 | es         |
|  4 | note  | comment | señor Martínez Oblanca          | es         |


Statistics for tags:

|          |   tag |
|:---------|------:|
| kinesic  | 46629 |
| incident | 13516 |
| vocal    | 11037 |
| note     |  5886 |
| head     |  2640 |
| gap      |   694 |


|                            |   type |
|:---------------------------|-------:|
| ('gap', 'inaudible')       |    694 |
| ('head', '')               |   2640 |
| ('incident', 'pause')      |  11837 |
| ('incident', 'action')     |   1636 |
| ('incident', 'leaving')    |     28 |
| ('incident', 'entering')   |     15 |
| ('kinesic', 'applause')    |  42472 |
| ('kinesic', 'gesture')     |   2421 |
| ('kinesic', 'laughter')    |   1005 |
| ('kinesic', 'signal')      |    731 |
| ('note', 'comment')        |   5885 |
| ('note', '')               |      1 |
| ('vocal', 'murmuring')     |   7452 |
| ('vocal', 'speaking')      |   1528 |
| ('vocal', 'shouting')      |   1457 |
| ('vocal', 'clarification') |    531 |
| ('vocal', 'interruption')  |     68 |
| ('vocal', 'greeting')      |      1 |
Most common notes:

|                                                                                              |   content |
|:---------------------------------------------------------------------------------------------|----------:|
| Aplausos                                                                                     |     35236 |
| Pausa                                                                                        |      6177 |
| Rumores                                                                                      |      6101 |
| Pausa.-Una trabajadora del servicio de limpieza procede a desinfectar la tribuna de oradores |      5250 |
| aplausos                                                                                     |      1671 |
| EAJ-PNV                                                                                      |      1111 |
| La señora                                                                                    |       832 |
| Risas                                                                                        |       801 |
| Protestas                                                                                    |       686 |
| El señor                                                                                     |       610 |
| rumores                                                                                      |       552 |
| Aplausos de las señoras y los señores diputados del Grupo Parlamentario VOX, puestos en pie  |       512 |
| Aplausos.-Rumores                                                                            |       413 |
| Rumores.-Aplausos                                                                            |       372 |
| Aplausos.                                                                                    |       246 |
| Continúan los rumores                                                                        |       241 |
| Protestas.-Aplausos                                                                          |       213 |
| Risas.-Aplausos                                                                              |       205 |
| Risas y aplausos                                                                             |       198 |
| Asentimiento                                                                                 |       187 |
Statistics after deduplication:

Number of words in the notes: 171469

|        | tag     | type    | content                                                                           | xml:lang   |     length |
|:-------|:--------|:--------|:----------------------------------------------------------------------------------|:-----------|-----------:|
| count  | 10742   | 10742   | 10742                                                                             | 10742      | 10742      |
| unique | 6       | 17      | 10739                                                                             | 1          |   nan      |
| top    | kinesic | comment | Aplausos.-Rumores.-El señor Hernando Fraile pronuncia palabras que no se perciben | es         |   nan      |
| freq   | 3214    | 2725    | 2                                                                                 | 10742      |   nan      |
| mean   | nan     | nan     | nan                                                                               | nan        |    15.9625 |
| std    | nan     | nan     | nan                                                                               | nan        |    37.6264 |
| min    | nan     | nan     | nan                                                                               | nan        |     1      |
| 25%    | nan     | nan     | nan                                                                               | nan        |     4      |
| 50%    | nan     | nan     | nan                                                                               | nan        |     8      |
| 75%    | nan     | nan     | nan                                                                               | nan        |    19      |
| max    | nan     | nan     | nan                                                                               | nan        |  1841      |


|    | tag   | type    | content                         | xml:lang   |   length |
|---:|:------|:--------|:--------------------------------|:-----------|---------:|
|  0 | note  | comment | EAJ-PNV                         | es         |        1 |
|  2 | note  | comment | SEÑOR MARTÍNEZ OBLANCA          | es         |        3 |
|  3 | note  | comment | Número de expediente 173/000056 | es         |        4 |
|  4 | note  | comment | señor Martínez Oblanca          | es         |        3 |
|  6 | note  | comment | Número de expediente 173/000057 | es         |        4 |


Statistics for tags:

|          |   tag |
|:---------|------:|
| kinesic  |  3214 |
| note     |  2726 |
| head     |  2173 |
| vocal    |  2061 |
| gap      |   429 |
| incident |   139 |


|                            |   type |
|:---------------------------|-------:|
| ('gap', 'inaudible')       |    429 |
| ('head', '')               |   2173 |
| ('incident', 'pause')      |     58 |
| ('incident', 'action')     |     41 |
| ('incident', 'leaving')    |     25 |
| ('incident', 'entering')   |     15 |
| ('kinesic', 'applause')    |   1368 |
| ('kinesic', 'gesture')     |   1301 |
| ('kinesic', 'signal')      |    507 |
| ('kinesic', 'laughter')    |     38 |
| ('note', 'comment')        |   2725 |
| ('note', '')               |      1 |
| ('vocal', 'speaking')      |   1257 |
| ('vocal', 'murmuring')     |    316 |
| ('vocal', 'shouting')      |    258 |
| ('vocal', 'clarification') |    196 |
| ('vocal', 'interruption')  |     33 |
| ('vocal', 'greeting')      |      1 |
Translation started.
Translation completed. It took 40.34 minutes for 10742 instances for the entire process of extraction and translation.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
|    | tag   | type    | content                         | xml:lang   |   length | translation            | corpus   |
|---:|:------|:--------|:--------------------------------|:-----------|---------:|:-----------------------|:---------|
|  0 | note  | comment | EAJ-PNV                         | es         |        1 | EAJ-PNV                | ES       |
|  2 | note  | comment | SEÑOR MARTÍNEZ OBLANCA          | es         |        3 | LORD MARTÍNEZ OBLANCA  | ES       |
|  3 | note  | comment | Número de expediente 173/000056 | es         |        4 | File number 173/000056 | ES       |
|  4 | note  | comment | señor Martínez Oblanca          | es         |        3 | Mr. Martínez Oblanca   | ES       |
|  6 | note  | comment | Número de expediente 173/000057 | es         |        4 | File number 173/000057 | ES       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-ES.notes.translated.ana.tsv
