2023-09-26 15:56:14.126083: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-09-26 15:56:14.763675: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-09-26 15:56:14.763739: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-09-26 15:56:14.763746: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
Extraction of the notes and translation started.
No. of files: 579.
Statistics before droping duplicates:



|        | tag    | type    | content   | xml:lang   |
|:-------|:-------|:--------|:----------|:-----------|
| count  | 254340 | 254340  | 254340    | 254340     |
| unique | 5      | 16      | 41863     | 9          |
| top    | note   | speaker | ELNÖK     | hu         |
| freq   | 154671 | 116346  | 58620     | 254303     |


|    | tag   | type    | content                                                                      | xml:lang   |
|---:|:------|:--------|:-----------------------------------------------------------------------------|:-----------|
|  0 | note  | speaker | ELNÖK                                                                        | hu         |
|  1 | note  | speaker | DR. SZÉKELY LÁSZLÓ, az alapvető jogok biztosa, a napirendi pont előadója     | hu         |
|  2 | note  | time    | 9.10                                                                         | hu         |
|  3 | note  | speaker | ELNÖK                                                                        | hu         |
|  4 | note  | speaker | DEMETER ZOLTÁN, az Igazságügyi bizottság előadója, a napirendi pont előadója | hu         |


Statistics for tags:

|          |    tag |
|:---------|-------:|
| note     | 154671 |
| kinesic  |  50570 |
| vocal    |  45361 |
| incident |   3701 |
| gap      |     37 |


|                           |   type |
|:--------------------------|-------:|
| ('gap', 'foreign')        |     37 |
| ('incident', '')          |   3178 |
| ('incident', 'action')    |    188 |
| ('incident', 'editorial') |    135 |
| ('incident', 'sound')     |    120 |
| ('incident', 'leaving')   |     80 |
| ('kinesic', 'applause')   |  35260 |
| ('kinesic', '')           |  15310 |
| ('note', 'speaker')       | 116346 |
| ('note', 'time')          |  27168 |
| ('note', 'voting')        |   7801 |
| ('note', '')              |   3356 |
| ('vocal', 'interruption') |  39074 |
| ('vocal', 'laughter')     |   2886 |
| ('vocal', 'noise')        |   2179 |
| ('vocal', 'murmuring')    |    924 |
| ('vocal', 'speaking')     |    293 |
| ('vocal', 'exclamat')     |      5 |
Most common notes:

|                                                                        |   content |
|:-----------------------------------------------------------------------|----------:|
| ELNÖK                                                                  |     58620 |
| Taps a kormánypártok soraiban.                                         |      9656 |
| Szavazás.                                                              |      7696 |
| Taps a kormánypárti padsorokban.                                       |      3636 |
| Taps a Jobbik soraiban.                                                |      3616 |
| Jelzésre:                                                              |      3022 |
| Taps a kormánypártok padsoraiból.                                      |      2505 |
| Taps a kormánypártok soraiból.                                         |      2416 |
| DR. RÉTVÁRI BENCE, az Emberi Erőforrások Minisztériumának államtitkára |      2236 |
| Az elnök a csengő megkocogtatásával jelzi az időkeret leteltét.        |      1984 |
| Az elnök csenget.                                                      |      1384 |
| Az elnök a csengő megkocogtatásával jelzi az idő leteltét.             |      1206 |
| Z. KÁRPÁT DÁNIEL (Jobbik)                                              |      1099 |
| Nincs jelentkező.                                                      |      1058 |
| Taps a Jobbik padsoraiból.                                             |       973 |
| Taps a Jobbik soraiból.                                                |       847 |
| Senki sem jelentkezik.                                                 |       794 |
| Taps a Jobbik padsoraiban.                                             |       775 |
| Taps a kormánypárti padsorokból.                                       |       764 |
| ORBÁN VIKTOR miniszterelnök                                            |       757 |
Statistics after deduplication:

Number of words in the notes: 326512

|        | tag   | type         | content               | xml:lang   |      length |
|:-------|:------|:-------------|:----------------------|:-----------|------------:|
| count  | 42051 | 42051        | 42051                 | 42051      | 42051       |
| unique | 5     | 16           | 41863                 | 9          |   nan       |
| top    | vocal | interruption | Vargha Tamás: Később. | hu         |   nan       |
| freq   | 31843 | 30343        | 2                     | 42014      |   nan       |
| mean   | nan   | nan          | nan                   | nan        |     7.76467 |
| std    | nan   | nan          | nan                   | nan        |     4.99175 |
| min    | nan   | nan          | nan                   | nan        |     1       |
| 25%    | nan   | nan          | nan                   | nan        |     5       |
| 50%    | nan   | nan          | nan                   | nan        |     7       |
| 75%    | nan   | nan          | nan                   | nan        |     9       |
| max    | nan   | nan          | nan                   | nan        |   191       |


|    | tag   | type    | content                                                                      | xml:lang   |   length |
|---:|:------|:--------|:-----------------------------------------------------------------------------|:-----------|---------:|
|  0 | note  | speaker | ELNÖK                                                                        | hu         |        1 |
|  1 | note  | speaker | DR. SZÉKELY LÁSZLÓ, az alapvető jogok biztosa, a napirendi pont előadója     | hu         |       11 |
|  2 | note  | time    | 9.10                                                                         | hu         |        1 |
|  4 | note  | speaker | DEMETER ZOLTÁN, az Igazságügyi bizottság előadója, a napirendi pont előadója | hu         |       10 |
|  5 | note  | time    | 9.20                                                                         | hu         |        1 |


Statistics for tags:

|          |   tag |
|:---------|------:|
| vocal    | 31843 |
| note     |  5312 |
| kinesic  |  3732 |
| incident |  1127 |
| gap      |    37 |


|                           |   type |
|:--------------------------|-------:|
| ('gap', 'foreign')        |     37 |
| ('incident', '')          |    784 |
| ('incident', 'action')    |    181 |
| ('incident', 'editorial') |     71 |
| ('incident', 'leaving')   |     46 |
| ('incident', 'sound')     |     45 |
| ('kinesic', 'applause')   |   2215 |
| ('kinesic', '')           |   1517 |
| ('note', '')              |   2951 |
| ('note', 'speaker')       |   1812 |
| ('note', 'time')          |    445 |
| ('note', 'voting')        |    104 |
| ('vocal', 'interruption') |  30343 |
| ('vocal', 'noise')        |    527 |
| ('vocal', 'laughter')     |    442 |
| ('vocal', 'speaking')     |    267 |
| ('vocal', 'murmuring')    |    259 |
| ('vocal', 'exclamat')     |      5 |
Translation started.
Translation completed. It took 70.52 minutes for 42051 instances for the entire process of extraction and translation.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
|    | tag   | type    | content                                                                      | xml:lang   |   length | translation                                                                                    | corpus   |
|---:|:------|:--------|:-----------------------------------------------------------------------------|:-----------|---------:|:-----------------------------------------------------------------------------------------------|:---------|
|  0 | note  | speaker | ELNÖK                                                                        | hu         |        1 | THE PRESIDENT                                                                                  | HU       |
|  1 | note  | speaker | DR. SZÉKELY LÁSZLÓ, az alapvető jogok biztosa, a napirendi pont előadója     | hu         |       11 | Dr. László SZÉKELY, Commissioner for Fundamental Rights, rapporteur for the item on the agenda | HU       |
|  2 | note  | time    | 9.10                                                                         | hu         |        1 | 9.10 p.m.                                                                                      | HU       |
|  4 | note  | speaker | DEMETER ZOLTÁN, az Igazságügyi bizottság előadója, a napirendi pont előadója | hu         |       10 | Mr Zoltán DEMETER, rapporteur for the Judicial Committee, rapporteur for the item              | HU       |
|  5 | note  | time    | 9.20                                                                         | hu         |        1 | 9.20 p.m.                                                                                      | HU       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-HU.notes.translated.ana.tsv
