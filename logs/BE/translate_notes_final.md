2023-06-27 09:16:16.359081: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-06-27 09:16:18.077819: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-06-27 09:16:18.077910: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-06-27 09:16:18.077920: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
Extraction of the notes and translation started.
No. of files: 2349.
Statistics before dropping duplicates:



|        | tag    | type      | content              | xml:lang   |
|:-------|:-------|:----------|:---------------------|:-----------|
| count  | 514166 | 514166    | 514166               | 514166     |
| unique | 5      | 15        | 235327               | 4          |
| top    | note   | editorial | L'incident est clos. | nl         |
| freq   | 508639 | 325002    | 24789                | 307983     |


|    | tag   | type      | content                                                                                                                                                                                                                   | xml:lang   |
|---:|:------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|
|  0 | note  | editorial | De vergadering wordt geopend om 14.20 uur en voorgezeten door Siegfried Bracke.                                                                                                                                           | nl         |
|  1 | note  | editorial | La séance est ouverte à 14.20 heures et présidée par M. Siegfried Bracke.                                                                                                                                                 | fr         |
|  2 | note  | speaker   | De voorzitter:                                                                                                                                                                                                            | nl         |
|  3 | note  | editorial | Een reeks mededelingen en besluiten moeten ter kennis gebracht worden van de Kamer. Zij worden op de website van de Kamer en in de bijlage bij het integraal verslag van deze vergadering opgenomen.                      | nl         |
|  4 | note  | editorial | Une série de communications et de décisions doivent être portées à la connaissance de la Chambre. Elles seront reprises sur le site web de la Chambre et insérées dans l'annexe du compte rendu intégral de cette séance. | fr         |


Statistics for tags:

|          |    tag |
|:---------|-------:|
| note     | 508639 |
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
| ('note', 'editorial')     | 320467 |
| ('note', 'speaker')       | 180801 |
| ('note', 'answer')        |   6940 |
| ('note', '')              |    431 |
| ('vocal', 'noise')        |    310 |
| ('vocal', 'laughter')     |    179 |
| ('vocal', 'exclamat')     |     64 |
| ('vocal', 'interruption') |      6 |
| ('vocal', 'speaking')     |      5 |
Most common notes:

|                             |   content |
|:----------------------------|----------:|
| L'incident est clos.        |     24789 |
| Het incident is gesloten.   |     24775 |
| De voorzitter:              |     12386 |
| Nee                         |      8097 |
| Non                         |      7020 |
| Le président:               |      6080 |
| Ja                          |      4624 |
| Oui                         |      4381 |
| Onthoudingen                |      4321 |
| Abstentions                 |      4321 |
| La présidente:              |      4145 |
| 000                         |      2528 |
| …                           |      1426 |
| Bespreking van de artikelen |      1404 |
| Discussion des articles     |      1404 |
| Algemene bespreking         |      1338 |
| Discussion générale         |      1337 |
| De voorzitster:             |      1016 |
| * * * * *                   |       678 |
| 02 Questions jointes de     |       564 |
Statistics after deduplication:

Number of words in the notes: 5504394

|        | tag    | type      | content   | xml:lang   |      length |
|:-------|:-------|:----------|:----------|:-----------|------------:|
| count  | 245357 | 245357    | 245357    | 245357     | 245357      |
| unique | 5      | 15        | 235327    | 4          |    nan      |
| top    | note   | editorial | Ja        | nl         |    nan      |
| freq   | 244807 | 171420    | 6         | 141384     |    nan      |
| mean   | nan    | nan       | nan       | nan        |     22.4342 |
| std    | nan    | nan       | nan       | nan        |     30.7014 |
| min    | nan    | nan       | nan       | nan        |      1      |
| 25%    | nan    | nan       | nan       | nan        |      4      |
| 50%    | nan    | nan       | nan       | nan        |     18      |
| 75%    | nan    | nan       | nan       | nan        |     27      |
| max    | nan    | nan       | nan       | nan        |    361      |


|    | tag   | type      | content                                                                                                                                                                                                                   | xml:lang   |   length |
|---:|:------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|---------:|
|  0 | note  | editorial | De vergadering wordt geopend om 14.20 uur en voorgezeten door Siegfried Bracke.                                                                                                                                           | nl         |       12 |
|  1 | note  | editorial | La séance est ouverte à 14.20 heures et présidée par M. Siegfried Bracke.                                                                                                                                                 | fr         |       13 |
|  2 | note  | speaker   | De voorzitter:                                                                                                                                                                                                            | nl         |        2 |
|  3 | note  | editorial | Een reeks mededelingen en besluiten moeten ter kennis gebracht worden van de Kamer. Zij worden op de website van de Kamer en in de bijlage bij het integraal verslag van deze vergadering opgenomen.                      | nl         |       33 |
|  4 | note  | editorial | Une série de communications et de décisions doivent être portées à la connaissance de la Chambre. Elles seront reprises sur le site web de la Chambre et insérées dans l'annexe du compte rendu intégral de cette séance. | fr         |       37 |


Statistics for tags:

|          |    tag |
|:---------|-------:|
| note     | 244807 |
| gap      |    386 |
| vocal    |     73 |
| kinesic  |     59 |
| incident |     32 |


|                           |   type |
|:--------------------------|-------:|
| ('gap', 'editorial')      |    386 |
| ('incident', 'action')    |     18 |
| ('incident', 'sound')     |     12 |
| ('incident', 'incident')  |      1 |
| ('incident', 'leaving')   |      1 |
| ('kinesic', 'applause')   |     34 |
| ('kinesic', 'gesture')    |     25 |
| ('note', 'editorial')     | 171034 |
| ('note', 'speaker')       |  73707 |
| ('note', '')              |     49 |
| ('note', 'answer')        |     17 |
| ('vocal', 'laughter')     |     25 |
| ('vocal', 'noise')        |     25 |
| ('vocal', 'exclamat')     |     20 |
| ('vocal', 'interruption') |      2 |
| ('vocal', 'speaking')     |      1 |
|    |   xml:lang |
|:---|-----------:|
| nl |     141384 |
| fr |      90572 |
| de |      12750 |
| en |        651 |
Three dataframes created:


|        | tag    | type      | content                     | xml:lang   |      length |
|:-------|:-------|:----------|:----------------------------|:-----------|------------:|
| count  | 141384 | 141384    | 141384                      | 141384     | 141384      |
| unique | 5      | 14        | 140433                      | 1          |    nan      |
| top    | note   | editorial | 01.03 Nahima Lanjri (CD&V): | nl         |    nan      |
| freq   | 141216 | 92970     | 2                           | 141384     |    nan      |
| mean   | nan    | nan       | nan                         | nan        |     23.3769 |
| std    | nan    | nan       | nan                         | nan        |     36.8155 |
| min    | nan    | nan       | nan                         | nan        |      1      |
| 25%    | nan    | nan       | nan                         | nan        |      4      |
| 50%    | nan    | nan       | nan                         | nan        |     16      |
| 75%    | nan    | nan       | nan                         | nan        |     26      |
| max    | nan    | nan       | nan                         | nan        |    329      |



|        | tag   | type      | content                             | xml:lang   |     length |
|:-------|:------|:----------|:------------------------------------|:-----------|-----------:|
| count  | 90572 | 90572     | 90572                               | 90572      | 90572      |
| unique | 5     | 12        | 90367                               | 1          |   nan      |
| top    | note  | editorial | 02.02 Cécile Thibaut (Ecolo-Groen): | fr         |   nan      |
| freq   | 90190 | 76845     | 2                                   | 90572      |   nan      |
| mean   | nan   | nan       | nan                                 | nan        |    23.2441 |
| std    | nan   | nan       | nan                                 | nan        |    17.8344 |
| min    | nan   | nan       | nan                                 | nan        |     1      |
| 25%    | nan   | nan       | nan                                 | nan        |    12      |
| 50%    | nan   | nan       | nan                                 | nan        |    22      |
| 75%    | nan   | nan       | nan                                 | nan        |    30      |
| max    | nan   | nan       | nan                                 | nan        |   361      |



|        | tag   | type    | content                      | xml:lang   |      length |
|:-------|:------|:--------|:-----------------------------|:-----------|------------:|
| count  | 12750 | 12750   | 12750                        | 12750      | 12750       |
| unique | 1     | 2       | 12689                        | 1          |   nan       |
| top    | note  | speaker | 09.01 Catherine Fonck (cdH): | de         |   nan       |
| freq   | 12750 | 11796   | 2                            | 12750      |   nan       |
| mean   | nan   | nan     | nan                          | nan        |     6.85522 |
| std    | nan   | nan     | nan                          | nan        |    22.8418  |
| min    | nan   | nan     | nan                          | nan        |     1       |
| 25%    | nan   | nan     | nan                          | nan        |     4       |
| 50%    | nan   | nan     | nan                          | nan        |     4       |
| 75%    | nan   | nan     | nan                          | nan        |     4       |
| max    | nan   | nan     | nan                          | nan        |   320       |
Translation started.
Translation completed. It took 142.76 minutes for 141384 instances for the entire process of extraction and translation.
|    | tag   | type      | content                                                                                                                                                                                              | xml:lang   |   length | translation                                                                                                                                                                             |
|---:|:------|:----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|---------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | note  | editorial | De vergadering wordt geopend om 14.20 uur en voorgezeten door Siegfried Bracke.                                                                                                                      | nl         |       12 | The meeting was opened at 2.20 p.m. and chaired by Siegfried Bracke.                                                                                                                    |
|  2 | note  | speaker   | De voorzitter:                                                                                                                                                                                       | nl         |        2 | The President shall:                                                                                                                                                                    |
|  3 | note  | editorial | Een reeks mededelingen en besluiten moeten ter kennis gebracht worden van de Kamer. Zij worden op de website van de Kamer en in de bijlage bij het integraal verslag van deze vergadering opgenomen. | nl         |       33 | A series of communications and decisions must be notified to the Chamber. They shall be included on the website of the Chamber and in the Annex to the integral report of this meeting. |
|  5 | note  | editorial | Aanwezig bij de opening van de vergadering zijn de ministers van de federale regering:                                                                                                               | nl         |       14 | At the opening of the meeting, the Ministers of the Federal Government:                                                                                                                 |
|  8 | note  | editorial | Berichten van verhindering                                                                                                                                                                           | nl         |        3 | Inhibited messages                                                                                                                                                                      |
Translation started.
Translation completed. It took 193.33 minutes for 90572 instances for the entire process of extraction and translation.
|    | tag   | type      | content                                                                                                                                                                                                                   | xml:lang   |   length | translation                                                                                                                                                                                        |
|---:|:------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|---------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | note  | editorial | La séance est ouverte à 14.20 heures et présidée par M. Siegfried Bracke.                                                                                                                                                 | fr         |       13 | The meeting was called to order at 2.20 p.m. and chaired by Mr. Siegfried Bracke.                                                                                                                  |
|  4 | note  | editorial | Une série de communications et de décisions doivent être portées à la connaissance de la Chambre. Elles seront reprises sur le site web de la Chambre et insérées dans l'annexe du compte rendu intégral de cette séance. | fr         |       37 | A series of communications and decisions must be brought to the attention of the House. They will be included on the House's website and included in the annex to the full record of this sitting. |
|  6 | note  | editorial | Ministres du gouvernement fédéral présents lors de l’ouverture de la séance:                                                                                                                                              | fr         |       11 | Ministers of the Federal Government present at the opening of the sitting:                                                                                                                         |
|  7 | note  | editorial | Charles Michel, Kris Peeters.                                                                                                                                                                                             | fr         |        4 | Charles Michel, Kris Peeters.                                                                                                                                                                      |
|  9 | note  | editorial | Excusés                                                                                                                                                                                                                   | fr         |        1 | Apologies                                                                                                                                                                                          |
Translation started.
Translation completed. It took 197.37 minutes for 12750 instances for the entire process of extraction and translation.
|     | tag   | type    | content                           | xml:lang   |   length | translation                       |
|----:|:------|:--------|:----------------------------------|:-----------|---------:|:----------------------------------|
|  39 | note  | speaker | 01.02 Barbara Pas (VB):           | de         |        4 | 01.02 Barbara Pas (VB):           |
|  44 | note  | speaker | 01.07 Barbara Pas (VB):           | de         |        4 | 01.07 Barbara Pas (VB):           |
|  62 | note  | speaker | 02.06 Dirk Van der Maelen (sp.a): | de         |        6 | 02.06 Dirk Van der Maelen (sp.a): |
|  78 | note  | speaker | 03.05 Gwenaëlle Grovonius (PS):   | de         |        4 | 03.05 Gwenaëlle Grovonius (PS):   |
| 100 | note  | speaker | 06.01 Johan Klaps (N-VA):         | de         |        4 | 06.01 Johan Klaps (N-VA):         |
The size of the final df:(244706, 6)
|        | tag    | type      | content                      | xml:lang   |      length | translation          |
|:-------|:-------|:----------|:-----------------------------|:-----------|------------:|:---------------------|
| count  | 244706 | 244706    | 244706                       | 244706     | 244706      | 244706               |
| unique | 5      | 15        | 234838                       | 3          |    nan      | 235801               |
| top    | note   | editorial | 14.01 Sophie Rohonyi (DéFI): | nl         |    nan      | Karine Lalieux (PS): |
| freq   | 244156 | 170769    | 5                            | 141384     |    nan      | 89                   |
| mean   | nan    | nan       | nan                          | nan        |     22.4669 | nan                  |
| std    | nan    | nan       | nan                          | nan        |     30.6823 | nan                  |
| min    | nan    | nan       | nan                          | nan        |      1      | nan                  |
| 25%    | nan    | nan       | nan                          | nan        |      4      | nan                  |
| 50%    | nan    | nan       | nan                          | nan        |     18      | nan                  |
| 75%    | nan    | nan       | nan                          | nan        |     27      | nan                  |
| max    | nan    | nan       | nan                          | nan        |    361      | nan                  |
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
|    | tag   | type      | content                                                                                                                                                                                              | xml:lang   |   length | translation                                                                                                                                                                             | corpus   |
|---:|:------|:----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|---------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | note  | editorial | De vergadering wordt geopend om 14.20 uur en voorgezeten door Siegfried Bracke.                                                                                                                      | nl         |       12 | The meeting was opened at 2.20 p.m. and chaired by Siegfried Bracke.                                                                                                                    | BE       |
|  1 | note  | speaker   | De voorzitter:                                                                                                                                                                                       | nl         |        2 | The President shall:                                                                                                                                                                    | BE       |
|  2 | note  | editorial | Een reeks mededelingen en besluiten moeten ter kennis gebracht worden van de Kamer. Zij worden op de website van de Kamer en in de bijlage bij het integraal verslag van deze vergadering opgenomen. | nl         |       33 | A series of communications and decisions must be notified to the Chamber. They shall be included on the website of the Chamber and in the Annex to the integral report of this meeting. | BE       |
|  3 | note  | editorial | Aanwezig bij de opening van de vergadering zijn de ministers van de federale regering:                                                                                                               | nl         |       14 | At the opening of the meeting, the Ministers of the Federal Government:                                                                                                                 | BE       |
|  4 | note  | editorial | Berichten van verhindering                                                                                                                                                                           | nl         |        3 | Inhibited messages                                                                                                                                                                      | BE       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-BE.notes.translated.tsv
