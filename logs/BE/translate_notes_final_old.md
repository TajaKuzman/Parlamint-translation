2023-05-16 09:06:23.783501: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-05-16 09:06:24.551999: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-05-16 09:06:24.552066: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-05-16 09:06:24.552072: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
Extraction of the notes and translation started.
No. of files: 2349.
Statistics before dropping duplicates:



|        | tag    | type   | content        | xml:lang   |
|:-------|:-------|:-------|:---------------|:-----------|
| count  | 193699 | 193699 | 193699         | 193699     |
| unique | 5      | 14     | 66372          | 3          |
| top    | note   |        | De voorzitter: | nl         |
| freq   | 188172 | 181232 | 12386          | 112402     |


|    | tag   | type   | content                                | xml:lang   |
|---:|:------|:-------|:---------------------------------------|:-----------|
|  0 | note  |        | De voorzitter:                         | nl         |
|  1 | note  |        | 01.01 Raoul Hedebouw (PTB-GO!):        | nl         |
|  2 | note  |        | 01.02 Barbara Pas (VB):                | de         |
|  3 | note  |        | 01.03 Véronique Caprasse (DéFI):       | fr         |
|  4 | note  |        | 01.04 Wouter De Vriendt (Ecolo-Groen): | nl         |


Statistics for tags:

|          |    tag |
|:---------|-------:|
| note     | 188172 |
| gap      |   4535 |
| vocal    |    564 |
| kinesic  |    388 |
| incident |     40 |


|                           |   type |
|:--------------------------|-------:|
| ('gap', 'editorial')      |   4535 |
| ('incident', 'action')    |     24 |
| ('incident', 'sound')     |     13 |
| ('incident', 'incident')  |      2 |
| ('incident', 'leaving')   |      1 |
| ('kinesic', 'applause')   |    363 |
| ('kinesic', 'gesture')    |     25 |
| ('note', '')              | 181232 |
| ('note', 'answer')        |   6940 |
| ('vocal', 'noise')        |    310 |
| ('vocal', 'laughter')     |    179 |
| ('vocal', 'exclamat')     |     64 |
| ('vocal', 'interruption') |      6 |
| ('vocal', 'speaking')     |      5 |
Most common notes:

|                                        |   content |
|:---------------------------------------|----------:|
| De voorzitter:                         |     12386 |
| Le président:                          |      6080 |
| La présidente:                         |      4144 |
| (Nee)                                  |      3768 |
| (Non)                                  |      2691 |
| Sentence could not be parsed: (…)      |      1403 |
| De voorzitster:                        |      1016 |
| (Ja)                                   |       287 |
| Sentence could not be parsed: (…): (…) |       266 |
| Sentence could not be parsed: 80       |       221 |
| (Applaudissements)                     |       150 |
| (Brouhaha)                             |       149 |
| Sentence could not be parsed: 140      |       136 |
| (Instemming)                           |       126 |
| (Applaus)                              |       118 |
| Sentence could not be parsed: )        |       117 |
| Marie-Christine Marghem, ministre:     |       106 |
| Jean-Marc Nollet (Ecolo-Groen):        |       102 |
| Sentence could not be parsed: 45       |        96 |
| Sentence could not be parsed: 84       |        90 |
Statistics after deduplication:

Number of words in the notes: 332232

|        | tag   | type   | content                      | xml:lang   |      length |
|:-------|:------|:-------|:-----------------------------|:-----------|------------:|
| count  | 75785 | 75785  | 75785                        | 75785      | 75785       |
| unique | 5     | 14     | 66372                        | 3          |   nan       |
| top    | note  |        | 03.10 Catherine Fonck (cdH): | nl         |   nan       |
| freq   | 75229 | 75212  | 3                            | 42521      |   nan       |
| mean   | nan   | nan    | nan                          | nan        |     4.38388 |
| std    | nan   | nan    | nan                          | nan        |     3.83326 |
| min    | nan   | nan    | nan                          | nan        |     1       |
| 25%    | nan   | nan    | nan                          | nan        |     4       |
| 50%    | nan   | nan    | nan                          | nan        |     4       |
| 75%    | nan   | nan    | nan                          | nan        |     4       |
| max    | nan   | nan    | nan                          | nan        |   295       |


|    | tag   | type   | content                                | xml:lang   |   length |
|---:|:------|:-------|:---------------------------------------|:-----------|---------:|
|  0 | note  |        | De voorzitter:                         | nl         |        2 |
|  1 | note  |        | 01.01 Raoul Hedebouw (PTB-GO!):        | nl         |        4 |
|  2 | note  |        | 01.02 Barbara Pas (VB):                | de         |        4 |
|  3 | note  |        | 01.03 Véronique Caprasse (DéFI):       | fr         |        4 |
|  4 | note  |        | 01.04 Wouter De Vriendt (Ecolo-Groen): | nl         |        5 |


Statistics for tags:

|          |   tag |
|:---------|------:|
| note     | 75229 |
| gap      |   390 |
| vocal    |    75 |
| kinesic  |    59 |
| incident |    32 |


|                           |   type |
|:--------------------------|-------:|
| ('gap', 'editorial')      |    390 |
| ('incident', 'action')    |     18 |
| ('incident', 'sound')     |     12 |
| ('incident', 'incident')  |      1 |
| ('incident', 'leaving')   |      1 |
| ('kinesic', 'applause')   |     34 |
| ('kinesic', 'gesture')    |     25 |
| ('note', '')              |  75212 |
| ('note', 'answer')        |     17 |
| ('vocal', 'noise')        |     27 |
| ('vocal', 'laughter')     |     25 |
| ('vocal', 'exclamat')     |     20 |
| ('vocal', 'interruption') |      2 |
| ('vocal', 'speaking')     |      1 |
|    |   xml:lang |
|:---|-----------:|
| nl |      42521 |
| fr |      21414 |
| de |      11850 |
Three dataframes created:


|        | tag   | type   | content        | xml:lang   |      length |
|:-------|:------|:-------|:---------------|:-----------|------------:|
| count  | 42521 | 42521  | 42521          | 42521      | 42521       |
| unique | 5     | 13     | 42521          | 1          |   nan       |
| top    | note  |        | De voorzitter: | nl         |   nan       |
| freq   | 42352 | 42341  | 1              | 42521      |   nan       |
| mean   | nan   | nan    | nan            | nan        |     4.38428 |
| std    | nan   | nan    | nan            | nan        |     2.33086 |
| min    | nan   | nan    | nan            | nan        |     1       |
| 25%    | nan   | nan    | nan            | nan        |     4       |
| 50%    | nan   | nan    | nan            | nan        |     4       |
| 75%    | nan   | nan    | nan            | nan        |     5       |
| max    | nan   | nan    | nan            | nan        |   244       |



|        | tag   | type   | content                          | xml:lang   |      length |
|:-------|:------|:-------|:---------------------------------|:-----------|------------:|
| count  | 21414 | 21414  | 21414                            | 21414      | 21414       |
| unique | 5     | 11     | 21414                            | 1          |   nan       |
| top    | note  |        | 01.03 Véronique Caprasse (DéFI): | fr         |   nan       |
| freq   | 21027 | 21021  | 1                                | 21414      |   nan       |
| mean   | nan   | nan    | nan                              | nan        |     4.46516 |
| std    | nan   | nan    | nan                              | nan        |     6.40573 |
| min    | nan   | nan    | nan                              | nan        |     1       |
| 25%    | nan   | nan    | nan                              | nan        |     4       |
| 50%    | nan   | nan    | nan                              | nan        |     4       |
| 75%    | nan   | nan    | nan                              | nan        |     4       |
| max    | nan   | nan    | nan                              | nan        |   295       |



/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
7-note-translation-bilingual.py:246: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df["translation"] = translation_list
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
7-note-translation-bilingual.py:246: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df["translation"] = translation_list
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
7-note-translation-bilingual.py:246: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df["translation"] = translation_list
|        | tag   | type   | content                 | xml:lang   |       length |
|:-------|:------|:-------|:------------------------|:-----------|-------------:|
| count  | 11850 | 11850  | 11850                   | 11850      | 11850        |
| unique | 1     | 1      | 11850                   | 1          |   nan        |
| top    | note  |        | 01.02 Barbara Pas (VB): | de         |   nan        |
| freq   | 11850 | 11850  | 1                       | 11850      |   nan        |
| mean   | nan   | nan    | nan                     | nan        |     4.23553  |
| std    | nan   | nan    | nan                     | nan        |     0.543775 |
| min    | nan   | nan    | nan                     | nan        |     2        |
| 25%    | nan   | nan    | nan                     | nan        |     4        |
| 50%    | nan   | nan    | nan                     | nan        |     4        |
| 75%    | nan   | nan    | nan                     | nan        |     4        |
| max    | nan   | nan    | nan                     | nan        |     6        |
Translation started.
Translation completed. It took 12.99 minutes for 42521 instances for the entire process of extraction and translation.
|    | tag   | type   | content                                | xml:lang   |   length | translation                            |
|---:|:------|:-------|:---------------------------------------|:-----------|---------:|:---------------------------------------|
|  0 | note  |        | De voorzitter:                         | nl         |        2 | The President shall:                   |
|  1 | note  |        | 01.01 Raoul Hedebouw (PTB-GO!):        | nl         |        4 | 01.01. Raoul Hedebouw (PTB-GO!):       |
|  4 | note  |        | 01.04 Wouter De Vriendt (Ecolo-Groen): | nl         |        5 | 01.04 Wouter De Vriendt (Ecolo-Green): |
|  6 | note  |        | 01.06 Raoul Hedebouw (PTB-GO!):        | nl         |        4 | 01.06 Raoul Hedebouw (PTB-GO!):        |
|  9 | note  |        | 01.09 Wouter De Vriendt (Ecolo-Groen): | nl         |        5 | 01.09 Wouter De Vriendt (Ecolo-Green): |
Translation started.
Translation completed. It took 17.95 minutes for 21414 instances for the entire process of extraction and translation.
|    | tag   | type   | content                                 | xml:lang   |   length | translation                           |
|---:|:------|:-------|:----------------------------------------|:-----------|---------:|:--------------------------------------|
|  3 | note  |        | 01.03 Véronique Caprasse (DéFI):        | fr         |        4 | 01.03 Véronique Caprasse (DEFI):      |
|  5 | note  |        | 01.05 Charles Michel, premier ministre: | fr         |        5 | 01.05 Charles Michel, Prime Minister: |
|  8 | note  |        | 01.08 Véronique Caprasse (DéFI):        | fr         |        4 | 01.08 Véronique Caprasse (DEFI):      |
| 10 | note  |        | 02.01 Stéphane Crusnière (PS):          | fr         |        4 | 02.01 Stéphane Crusnière (PS):        |
| 13 | note  |        | 02.04 Charles Michel, premier ministre: | fr         |        5 | 02.04 Charles Michel, Prime Minister: |
Translation started.
Translation completed. It took 20.57 minutes for 11850 instances for the entire process of extraction and translation.
|    | tag   | type   | content                           | xml:lang   |   length | translation                       |
|---:|:------|:-------|:----------------------------------|:-----------|---------:|:----------------------------------|
|  2 | note  |        | 01.02 Barbara Pas (VB):           | de         |        4 | 01.02 Barbara Pas (VB):           |
|  7 | note  |        | 01.07 Barbara Pas (VB):           | de         |        4 | 01.07 Barbara Pas (VB):           |
| 15 | note  |        | 02.06 Dirk Van der Maelen (sp.a): | de         |        6 | 02.06 Dirk Van der Maelen (sp.a): |
| 21 | note  |        | 03.05 Gwenaëlle Grovonius (PS):   | de         |        4 | 03.05 Gwenaëlle Grovonius (PS):   |
| 31 | note  |        | 06.01 Johan Klaps (N-VA):         | de         |        4 | 06.01 Johan Klaps (N-VA):         |
The size of the final df:(75785, 6)
|        | tag   | type   | content                        | xml:lang   |      length | translation          |
|:-------|:------|:-------|:-------------------------------|:-----------|------------:|:---------------------|
| count  | 75785 | 75785  | 75785                          | 75785      | 75785       | 75785                |
| unique | 5     | 14     | 66372                          | 3          |   nan       | 69173                |
| top    | note  |        | 07.01 Christophe Bombled (MR): | nl         |   nan       | Karine Lalieux (PS): |
| freq   | 75229 | 75212  | 3                              | 42521      |   nan       | 89                   |
| mean   | nan   | nan    | nan                            | nan        |     4.38388 | nan                  |
| std    | nan   | nan    | nan                            | nan        |     3.83326 | nan                  |
| min    | nan   | nan    | nan                            | nan        |     1       | nan                  |
| 25%    | nan   | nan    | nan                            | nan        |     4       | nan                  |
| 50%    | nan   | nan    | nan                            | nan        |     4       | nan                  |
| 75%    | nan   | nan    | nan                            | nan        |     4       | nan                  |
| max    | nan   | nan    | nan                            | nan        |   295       | nan                  |
|    | tag   | type   | content                                | xml:lang   |   length | translation                            | corpus   |
|---:|:------|:-------|:---------------------------------------|:-----------|---------:|:---------------------------------------|:---------|
|  0 | note  |        | De voorzitter:                         | nl         |        2 | The President shall:                   | BE       |
|  1 | note  |        | 01.01 Raoul Hedebouw (PTB-GO!):        | nl         |        4 | 01.01. Raoul Hedebouw (PTB-GO!):       | BE       |
|  2 | note  |        | 01.04 Wouter De Vriendt (Ecolo-Groen): | nl         |        5 | 01.04 Wouter De Vriendt (Ecolo-Green): | BE       |
|  3 | note  |        | 01.06 Raoul Hedebouw (PTB-GO!):        | nl         |        4 | 01.06 Raoul Hedebouw (PTB-GO!):        | BE       |
|  4 | note  |        | 01.09 Wouter De Vriendt (Ecolo-Groen): | nl         |        5 | 01.09 Wouter De Vriendt (Ecolo-Green): | BE       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-BE.notes.translated.tsv
