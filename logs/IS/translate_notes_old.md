Extraction of the notes and translation started.
No. of files: 928.
Statistics before droping duplicates:



|        | tag     | type    | content          | xml:lang   |
|:-------|:--------|:--------|:-----------------|:-----------|
| count  | 49947   | 49947   | 49947            | 49947      |
| unique | 4       | 13      | 2378             | 1          |
| top    | kinesic | ringing | Forseti hringir. |            |
| freq   | 40193   | 39447   | 39445            | 49947      |


|    | tag     | type    | content                                                                                                                            | xml:lang   |
|---:|:--------|:--------|:-----------------------------------------------------------------------------------------------------------------------------------|:-----------|
|  0 | note    | signing | Þorsteinn V. Einarsson, 10. þm. Reykv. n., og Eva Einarsdóttir, 10. þm. Reykv. s., undirrituðu drengskaparheit að stjórnarskránni. |            |
|  1 | kinesic | ringing | Forseti hringir.                                                                                                                   |            |
|  2 | kinesic | ringing | Forseti hringir.                                                                                                                   |            |
|  3 | kinesic | ringing | Forseti hringir.                                                                                                                   |            |
|  4 | kinesic | ringing | Forseti hringir.                                                                                                                   |            |


Statistics for tags:

|          |   tag |
|:---------|------:|
| kinesic  | 40193 |
| vocal    |  9553 |
| note     |   137 |
| incident |    64 |


|                                 |   type |
|:--------------------------------|-------:|
| ('incident', '')                |     60 |
| ('incident', 'editorial')       |      3 |
| ('incident', 'incident')        |      1 |
| ('kinesic', 'ringing')          |  39447 |
| ('kinesic', 'laughter')         |    741 |
| ('kinesic', 'noise')            |      3 |
| ('kinesic', 'applause')         |      2 |
| ('note', 'signing')             |     94 |
| ('note', '')                    |     32 |
| ('note', 'musical_performance') |      6 |
| ('note', 'voting')              |      5 |
| ('vocal', 'interruption')       |   9306 |
| ('vocal', 'noise')              |    244 |
| ('vocal', 'shouting')           |      2 |
| ('vocal', 'speaking')           |      1 |
Most common notes:

|                              |   content |
|:-----------------------------|----------:|
| Forseti hringir.             |     39445 |
| Gripið fram í.               |      5022 |
| Gripið fram í: Heyr, heyr.   |      1466 |
| Hlátur í þingsal.            |       713 |
| Kliður í þingsal.            |       150 |
| Gripið fram í: Nei.          |        92 |
| Háreysti í þingsal.          |        83 |
| Gripið fram í: Já.           |        59 |
| Frammíköll í þingsal.        |        49 |
| Þingmenn risu úr sætum.      |        49 |
| Gripið fram í: Heyr, heyr!   |        35 |
| Gripið fram í: Nákvæmlega.   |        35 |
| Gripið fram í: Jú.           |        29 |
| Nei.                         |        24 |
| Gripið fram í: Rétt.         |        19 |
| Gripið fram í: Ha?           |        17 |
| Gripið fram í: Nú?           |        16 |
| Já.                          |        14 |
| Gripið fram í: Rangt.        |        14 |
| Gripið fram í: Það er rangt. |        13 |
Statistics after deduplication:

Number of words in the notes: 14404

|        | tag   | type         | content                                                                                                                            | xml:lang   |     length |
|:-------|:------|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------|:-----------|-----------:|
| count  | 2378  | 2378         | 2378                                                                                                                               | 2378       | 2378       |
| unique | 4     | 13           | 2378                                                                                                                               | 1          |  nan       |
| top    | vocal | interruption | Þorsteinn V. Einarsson, 10. þm. Reykv. n., og Eva Einarsdóttir, 10. þm. Reykv. s., undirrituðu drengskaparheit að stjórnarskránni. |            |  nan       |
| freq   | 2218  | 2208         | 1                                                                                                                                  | 2378       |  nan       |
| mean   | nan   | nan          | nan                                                                                                                                | nan        |    6.05719 |
| std    | nan   | nan          | nan                                                                                                                                | nan        |    4.38139 |
| min    | nan   | nan          | nan                                                                                                                                | nan        |    1       |
| 25%    | nan   | nan          | nan                                                                                                                                | nan        |    4       |
| 50%    | nan   | nan          | nan                                                                                                                                | nan        |    5       |
| 75%    | nan   | nan          | nan                                                                                                                                | nan        |    7       |
| max    | nan   | nan          | nan                                                                                                                                | nan        |   63       |


|    | tag     | type         | content                                                                                                                            | xml:lang   |   length |
|---:|:--------|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------|:-----------|---------:|
|  0 | note    | signing      | Þorsteinn V. Einarsson, 10. þm. Reykv. n., og Eva Einarsdóttir, 10. þm. Reykv. s., undirrituðu drengskaparheit að stjórnarskránni. |            |       18 |
|  1 | kinesic | ringing      | Forseti hringir.                                                                                                                   |            |        2 |
| 87 | kinesic | laughter     | Hlátur í þingsal.                                                                                                                  |            |        3 |
| 88 | vocal   | interruption | Gripið fram í.                                                                                                                     |            |        3 |
| 90 | vocal   | interruption | Gripið fram í: Vanhæfur.                                                                                                           |            |        4 |


Statistics for tags:

|          |   tag |
|:---------|------:|
| vocal    |  2218 |
| note     |   132 |
| kinesic  |    16 |
| incident |    12 |


2023-03-14 10:46:52.063714: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-03-14 10:46:52.759711: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-03-14 10:46:52.759800: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-03-14 10:46:52.759806: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
|                                 |   type |
|:--------------------------------|-------:|
| ('incident', '')                |      8 |
| ('incident', 'editorial')       |      3 |
| ('incident', 'incident')        |      1 |
| ('kinesic', 'laughter')         |      9 |
| ('kinesic', 'noise')            |      3 |
| ('kinesic', 'applause')         |      2 |
| ('kinesic', 'ringing')          |      2 |
| ('note', 'signing')             |     93 |
| ('note', '')                    |     31 |
| ('note', 'voting')              |      5 |
| ('note', 'musical_performance') |      3 |
| ('vocal', 'interruption')       |   2208 |
| ('vocal', 'noise')              |      8 |
| ('vocal', 'shouting')           |      1 |
| ('vocal', 'speaking')           |      1 |
Translation started.
Translation completed. It took 1.67 minutes for 2378 instances for the entire process of extraction and translation.

|    | tag     | type         | content                                                                                                                            | xml:lang   |   length | translation                                                                                                                               |
|---:|:--------|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------|:-----------|---------:|:------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | note    | signing      | Þorsteinn V. Einarsson, 10. þm. Reykv. n., og Eva Einarsdóttir, 10. þm. Reykv. s., undirrituðu drengskaparheit að stjórnarskránni. |            |       18 | Stone of V. Einarsson, 1 0th. Smoke. No., and Eva Einarsdóttir, the 10th. Smoke. As an example, sign your commitment to the constitution. |
|  1 | kinesic | ringing      | Forseti hringir.                                                                                                                   |            |        2 | The president calls.                                                                                                                      |
| 87 | kinesic | laughter     | Hlátur í þingsal.                                                                                                                  |            |        3 | Laughter at the Hall of Congress.                                                                                                         |
| 88 | vocal   | interruption | Gripið fram í.                                                                                                                     |            |        3 | Up front.                                                                                                                                 |
| 90 | vocal   | interruption | Gripið fram í: Vanhæfur.                                                                                                           |            |        4 | To the point: Incompetent.                                                                                                                |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-IS.notes.translated.csv
