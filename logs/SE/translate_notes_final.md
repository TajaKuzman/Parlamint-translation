2023-05-12 09:26:06.590950: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-05-12 09:26:07.221748: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-05-12 09:26:07.221815: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-05-12 09:26:07.221821: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
Extraction of the notes and translation started.
No. of files: 938.
Statistics before droping duplicates:



|        | tag    | type   | content    | xml:lang   |
|:-------|:-------|:-------|:-----------|:-----------|
| count  | 396026 | 396026 | 396026     | 396026     |
| unique | 3      | 3      | 150582     | 1          |
| top    | note   |        | (Applåder) | sv         |
| freq   | 370551 | 289625 | 9656       | 396026     |


|    | tag   | type    | content                                                                                                                                                            | xml:lang   |
|---:|:------|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|
|  0 | note  |         | Välkomsthälsning                                                                                                                                                   | sv         |
|  1 | note  | speaker | Anf. 1 TALMANNEN:                                                                                                                                                  | sv         |
|  2 | note  |         | First of all, I would lik e to say warmly welcome to the S peaker of the Parliament of Cyprus, Demetris Syllouris. You are most welcome to the Swedish Parliament. | sv         |
|  3 | note  | speaker | Anf. 2 Statsminister STEFAN LÖFVEN (S):                                                                                                                            | sv         |
|  4 | note  | speaker | Anf. 3 ANNA KINBERG BATRA (M):                                                                                                                                     | sv         |


Statistics for tags:

|         |    tag |
|:--------|-------:|
| note    | 370551 |
| head    |  15819 |
| kinesic |   9656 |


|                         |   type |
|:------------------------|-------:|
| ('head', '')            |  15819 |
| ('kinesic', 'applause') |   9656 |
| ('note', '')            | 273806 |
| ('note', 'speaker')     |  96745 |
Most common notes:

|                                                            |   content |
|:-----------------------------------------------------------|----------:|
| (Applåder)                                                 |      9656 |
| Kammaren biföll utskottets förslag.                        |      7017 |
| Partivis fördelning av rösterna:                           |      5064 |
| 1. utskottet                                               |      5033 |
| Votering:                                                  |      4256 |
| Överläggningen var härmed avslutad.                        |      3527 |
| föredrogs.                                                 |      2486 |
| till justitie- och migrationsminister Morgan Johansson (S) |      2407 |
| till socialminister Lena Hallengren (S)                    |      2127 |
| till finansminister Magdalena Andersson (S)                |      1795 |
| Till riksdagen                                             |      1730 |
| till utrikesminister Ann Linde (S)                         |      1643 |
| Interpellationsdebatten var härmed avslutad.               |      1584 |
| till statsrådet Anders Ygeman (S)                          |      1531 |
| till infrastrukturminister Tomas Eneroth (S)               |      1508 |
| Enligt uppdrag                                             |      1469 |
| av Björn Söder (SD)                                        |      1148 |
| Följande dokument anmäldes och bordlades:                  |      1104 |
| till statsrådet Mikael Damberg (S)                         |      1089 |
| av Markus Wiechel (SD)                                     |      1079 |
Statistics after deduplication:

Number of words in the notes: 1107821

|        | tag    | type   | content          | xml:lang   |       length |
|:-------|:-------|:-------|:-----------------|:-----------|-------------:|
| count  | 152069 | 152069 | 152069           | 152069     | 152069       |
| unique | 3      | 3      | 150582           | 1          |    nan       |
| top    | note   |        | § 16 Äldrefrågor | sv         |    nan       |
| freq   | 143695 | 89699  | 2                | 152069     |    nan       |
| mean   | nan    | nan    | nan              | nan        |      7.28499 |
| std    | nan    | nan    | nan              | nan        |      5.73819 |
| min    | nan    | nan    | nan              | nan        |      1       |
| 25%    | nan    | nan    | nan              | nan        |      5       |
| 50%    | nan    | nan    | nan              | nan        |      6       |
| 75%    | nan    | nan    | nan              | nan        |      7       |
| max    | nan    | nan    | nan              | nan        |    283       |


|    | tag   | type    | content                                                                                                                                                            | xml:lang   |   length |
|---:|:------|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|---------:|
|  0 | note  |         | Välkomsthälsning                                                                                                                                                   | sv         |        1 |
|  1 | note  | speaker | Anf. 1 TALMANNEN:                                                                                                                                                  | sv         |        3 |
|  2 | note  |         | First of all, I would lik e to say warmly welcome to the S peaker of the Parliament of Cyprus, Demetris Syllouris. You are most welcome to the Swedish Parliament. | sv         |       30 |
|  3 | note  | speaker | Anf. 2 Statsminister STEFAN LÖFVEN (S):                                                                                                                            | sv         |        6 |
|  4 | note  | speaker | Anf. 3 ANNA KINBERG BATRA (M):                                                                                                                                     | sv         |        6 |


Statistics for tags:

|         |    tag |
|:--------|-------:|
| note    | 143695 |
| head    |   8373 |
| kinesic |      1 |


|                         |   type |
|:------------------------|-------:|
| ('head', '')            |   8373 |
| ('kinesic', 'applause') |      1 |
| ('note', '')            |  81326 |
| ('note', 'speaker')     |  62369 |
Translation started.
Translation completed. It took 67.16 minutes for 152069 instances for the entire process of extraction and translation.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
    
|    | tag   | type    | content                                                                                                                                                            | xml:lang   |   length | translation                                                                                                                                                        | corpus   |
|---:|:------|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|---------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | note  |         | Välkomsthälsning                                                                                                                                                   | sv         |        1 | Welcome                                                                                                                                                            | SE       |
|  1 | note  | speaker | Anf. 1 TALMANNEN:                                                                                                                                                  | sv         |        3 | Anf. 1 THE TALMAN:                                                                                                                                                 | SE       |
|  2 | note  |         | First of all, I would lik e to say warmly welcome to the S peaker of the Parliament of Cyprus, Demetris Syllouris. You are most welcome to the Swedish Parliament. | sv         |       30 | First of all, I would like to say warmly welcome to the S speaker of the Parliament of Cyprus, Demetris Syllouris. You are most welcome to the Swedish Parliament. | SE       |
|  3 | note  | speaker | Anf. 2 Statsminister STEFAN LÖFVEN (S):                                                                                                                            | sv         |        6 | Anf. 2 Prime Minister STEFAN LÖFVEN (S):                                                                                                                           | SE       |
|  4 | note  | speaker | Anf. 3 ANNA KINBERG BATRA (M):                                                                                                                                     | sv         |        6 | Anf. 3 OTHER KINBERG BATRA (M):                                                                                                                                    | SE       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-SE.notes.translated.tsv
