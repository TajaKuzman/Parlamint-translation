2023-03-13 15:17:17.496242: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-03-13 15:17:18.451798: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-03-13 15:17:18.451884: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-03-13 15:17:18.451890: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
Extraction of the notes and translation started.
No. of files: 515.
Statistics before droping duplicates:



|        | tag    | type    | content   | xml:lang   |
|:-------|:-------|:--------|:----------|:-----------|
| count  | 226924 | 226924  | 226924    | 226924     |
| unique | 4      | 15      | 37048     | 1          |
| top    | note   | speaker | ELNÖK     |            |
| freq   | 135779 | 104521  | 52642     | 226924     |


|    | tag   | type    | content                                                           | xml:lang   |
|---:|:------|:--------|:------------------------------------------------------------------|:-----------|
|  0 | note  | speaker | ELNÖK                                                             |            |
|  1 | note  | speaker | DR. TÓTH BERTALAN (MSZP)                                          |            |
|  2 | note  | time    | 13.10                                                             |            |
|  3 | note  | speaker | ELNÖK                                                             |            |
|  4 | note  | speaker | DR. ARADSZKI ANDRÁS nemzeti fejlesztési minisztériumi államtitkár |            |


Statistics for tags:

|          |    tag |
|:---------|-------:|
| note     | 135779 |
| kinesic  |  44614 |
| vocal    |  43105 |
| incident |   3426 |


|                           |   type |
|:--------------------------|-------:|
| ('incident', '')          |   2968 |
| ('incident', 'action')    |    157 |
| ('incident', 'sound')     |    117 |
| ('incident', 'editorial') |    112 |
| ('incident', 'leaving')   |     72 |
| ('kinesic', 'applause')   |  30924 |
| ('kinesic', '')           |  13690 |
| ('note', 'speaker')       | 104521 |
| ('note', 'time')          |  24257 |
| ('note', 'voting')        |   6996 |
| ('note', '')              |      5 |
| ('vocal', 'interruption') |  37416 |
| ('vocal', 'laughter')     |   2590 |
| ('vocal', 'noise')        |   2013 |
| ('vocal', 'murmuring')    |    851 |
| ('vocal', 'speaking')     |    230 |
| ('vocal', 'exclamat')     |      5 |
Most common notes:

|                                                                        |   content |
|:-----------------------------------------------------------------------|----------:|
| ELNÖK                                                                  |     52642 |
| Taps a kormánypártok soraiban.                                         |      8597 |
| Szavazás.                                                              |      6898 |
| Taps a Jobbik soraiban.                                                |      3527 |
| Taps a kormánypárti padsorokban.                                       |      3342 |
| Jelzésre:                                                              |      2727 |
| DR. RÉTVÁRI BENCE, az Emberi Erőforrások Minisztériumának államtitkára |      2236 |
| Taps a kormánypártok soraiból.                                         |      2224 |
| Taps a kormánypártok padsoraiból.                                      |      2137 |
| Az elnök a csengő megkocogtatásával jelzi az időkeret leteltét.        |      1842 |
| Az elnök csenget.                                                      |      1203 |
| Az elnök a csengő megkocogtatásával jelzi az idő leteltét.             |      1138 |
| Z. KÁRPÁT DÁNIEL (Jobbik)                                              |      1011 |
| Nincs jelentkező.                                                      |       983 |
| Taps a Jobbik padsoraiból.                                             |       928 |
| Taps a Jobbik soraiból.                                                |       822 |
| Taps a Jobbik padsoraiban.                                             |       758 |
| Senki sem jelentkezik.                                                 |       719 |
| GÚR NÁNDOR (MSZP)                                                      |       672 |
| ORBÁN VIKTOR miniszterelnök                                            |       661 |
Statistics after deduplication:

Number of words in the notes: 289466

|        | tag   | type         | content   | xml:lang   |      length |
|:-------|:------|:-------------|:----------|:-----------|------------:|
| count  | 37048 | 37048        | 37048     | 37048      | 37048       |
| unique | 4     | 15           | 37048     | 1          |   nan       |
| top    | vocal | interruption | ELNÖK     |            |   nan       |
| freq   | 30790 | 29426        | 1         | 37048      |   nan       |
| mean   | nan   | nan          | nan       | nan        |     7.81327 |
| std    | nan   | nan          | nan       | nan        |     4.96648 |
| min    | nan   | nan          | nan       | nan        |     1       |
| 25%    | nan   | nan          | nan       | nan        |     5       |
| 50%    | nan   | nan          | nan       | nan        |     7       |
| 75%    | nan   | nan          | nan       | nan        |     9       |
| max    | nan   | nan          | nan       | nan        |   191       |


|    | tag   | type    | content                                                           | xml:lang   |   length |
|---:|:------|:--------|:------------------------------------------------------------------|:-----------|---------:|
|  0 | note  | speaker | ELNÖK                                                             |            |        1 |
|  1 | note  | speaker | DR. TÓTH BERTALAN (MSZP)                                          |            |        4 |
|  2 | note  | time    | 13.10                                                             |            |        1 |
|  4 | note  | speaker | DR. ARADSZKI ANDRÁS nemzeti fejlesztési minisztériumi államtitkár |            |        7 |
|  6 | note  | time    | 13.20                                                             |            |        1 |


Statistics for tags:

|          |   tag |
|:---------|------:|
| vocal    | 30790 |
| kinesic  |  3109 |
| note     |  2147 |
| incident |  1002 |


|                           |   type |
|:--------------------------|-------:|
| ('incident', '')          |    703 |
| ('incident', 'action')    |    152 |
| ('incident', 'editorial') |     62 |
| ('incident', 'leaving')   |     43 |
| ('incident', 'sound')     |     42 |
| ('kinesic', 'applause')   |   1877 |
| ('kinesic', '')           |   1232 |
| ('note', 'speaker')       |   1609 |
| ('note', 'time')          |    436 |
| ('note', 'voting')        |     97 |
| ('note', '')              |      5 |
| ('vocal', 'interruption') |  29426 |
| ('vocal', 'noise')        |    492 |
| ('vocal', 'laughter')     |    406 |
| ('vocal', 'murmuring')    |    244 |
| ('vocal', 'speaking')     |    217 |
| ('vocal', 'exclamat')     |      5 |
Translation started.
Translation completed. It took 16.86 minutes for 37048 instances for the entire process of extraction and translation.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
|    | tag   | type    | content                                                           | xml:lang   |   length | translation                                                                  |
|---:|:------|:--------|:------------------------------------------------------------------|:-----------|---------:|:-----------------------------------------------------------------------------|
|  0 | note  | speaker | ELNÖK                                                             |            |        1 | THE PRESIDENT                                                                |
|  1 | note  | speaker | DR. TÓTH BERTALAN (MSZP)                                          |            |        4 | Dr. Tóth Bertalan (MSZP)                                                     |
|  2 | note  | time    | 13.10                                                             |            |        1 | 13.10 p.m.                                                                   |
|  4 | note  | speaker | DR. ARADSZKI ANDRÁS nemzeti fejlesztési minisztériumi államtitkár |            |        7 | DR. ARADSZKI ANDRÁS State Secretary for the Ministry of National Development |
|  6 | note  | time    | 13.20                                                             |            |        1 | 13.20 p.m.                                                                   |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-HU.notes.translated.csv
