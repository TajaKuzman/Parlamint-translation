2023-05-15 08:55:25.264508: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-05-15 08:55:25.932857: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-05-15 08:55:25.932930: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-05-15 08:55:25.932937: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
Extraction of the notes and translation started.
No. of files: 686.
Statistics before droping duplicates:



|        | tag    | type    | content   | xml:lang   |
|:-------|:-------|:--------|:----------|:-----------|
| count  | 492094 | 492094  | 492094    | 492094     |
| unique | 6      | 17      | 108463    | 1          |
| top    | note   | speaker | Oklaski   | pl         |
| freq   | 241406 | 228326  | 68144     | 492094     |


|    | tag   | type    | content                                                                                                     | xml:lang   |
|---:|:------|:--------|:------------------------------------------------------------------------------------------------------------|:-----------|
|  0 | note  | time    | Wznowienie posiedzenia o godzinie 9 minut 02                                                                | pl         |
|  1 | note  | debate  | Posiedzeniu przewodniczą marszałek Stanisław Karczewski oraz wicemarszałkowie Grzegorz Czelej i Adam Bielan | pl         |
|  2 | note  | speaker | Marszałek Stanisław Karczewski:                                                                             | pl         |
|  3 | note  | speaker | Senator Sprawozdawca Grzegorz Peczkis:                                                                      | pl         |
|  4 | note  | speaker | Marszałek Stanisław Karczewski:                                                                             | pl         |


Statistics for tags:

|          |    tag |
|:---------|-------:|
| note     | 241406 |
| vocal    | 106762 |
| kinesic  |  94217 |
| incident |  47417 |
| gap      |   1606 |
| head     |    686 |


|                          |   type |
|:-------------------------|-------:|
| ('gap', 'inaudible')     |   1606 |
| ('head', '')             |    686 |
| ('incident', '')         |  45386 |
| ('incident', 'action')   |   1972 |
| ('incident', 'entering') |     32 |
| ('incident', 'leaving')  |     27 |
| ('kinesic', 'applause')  |  71763 |
| ('kinesic', 'ringing')   |  21587 |
| ('kinesic', 'signal')    |    583 |
| ('kinesic', 'playback')  |    284 |
| ('note', 'speaker')      | 228326 |
| ('note', 'vote')         |   6821 |
| ('note', 'time')         |   3172 |
| ('note', 'debate')       |   3087 |
| ('vocal', 'speaking')    |  93680 |
| ('vocal', 'noise')       |   9993 |
| ('vocal', 'laughter')    |   2650 |
| ('vocal', 'shouting')    |    439 |
Most common notes:

|                                           |   content |
|:------------------------------------------|----------:|
| Oklaski                                   |     68144 |
| Dzwonek                                   |     20146 |
| Wicemarszałek Ryszard Terlecki:           |     13917 |
| Marszałek:                                |     13615 |
| Wicemarszałek Małgorzata Kidawa-Błońska:  |     13017 |
| Wicemarszałek Barbara Dolniak:            |      7211 |
| Wicemarszałek Stanisław Tyszka:           |      7087 |
| Wicemarszałek Joachim Brudziński:         |      5748 |
| Wicemarszałek Bogdan Borusewicz:          |      5664 |
| Wicemarszałek Maria Koc:                  |      5641 |
| Wicemarszałek Małgorzata Gosiewska:       |      5240 |
| Rozmowy na sali                           |      5121 |
| Wicemarszałek Włodzimierz Czarzasty:      |      4508 |
| Wicemarszałek Piotr Zgorzelski:           |      4314 |
| Wicemarszałek Adam Bielan:                |      3948 |
| Marszałek Stanisław Karczewski:           |      3349 |
| Wicemarszałek Michał Seweryński:          |      3348 |
| Wicemarszałek Gabriela Morawska-Stanecka: |      3227 |
| Poruszenie na sali                        |      3040 |
| Wicemarszałek Grzegorz Czelej:            |      2759 |
Statistics after deduplication:

Number of words in the notes: 674344

|        | tag    | type     | content   | xml:lang   |       length |
|:-------|:-------|:---------|:----------|:-----------|-------------:|
| count  | 108513 | 108513   | 108513    | 108513     | 108513       |
| unique | 6      | 17       | 108463    | 1          |    nan       |
| top    | vocal  | speaking | Ale jaką? | pl         |    nan       |
| freq   | 71724  | 71411    | 2         | 108513     |    nan       |
| mean   | nan    | nan      | nan       | nan        |      6.21441 |
| std    | nan    | nan      | nan       | nan        |      5.35647 |
| min    | nan    | nan      | nan       | nan        |      1       |
| 25%    | nan    | nan      | nan       | nan        |      3       |
| 50%    | nan    | nan      | nan       | nan        |      5       |
| 75%    | nan    | nan      | nan       | nan        |      8       |
| max    | nan    | nan      | nan       | nan        |    583       |


|    | tag   | type    | content                                                                                                     | xml:lang   |   length |
|---:|:------|:--------|:------------------------------------------------------------------------------------------------------------|:-----------|---------:|
|  0 | note  | time    | Wznowienie posiedzenia o godzinie 9 minut 02                                                                | pl         |        7 |
|  1 | note  | debate  | Posiedzeniu przewodniczą marszałek Stanisław Karczewski oraz wicemarszałkowie Grzegorz Czelej i Adam Bielan | pl         |       12 |
|  2 | note  | speaker | Marszałek Stanisław Karczewski:                                                                             | pl         |        3 |
|  3 | note  | speaker | Senator Sprawozdawca Grzegorz Peczkis:                                                                      | pl         |        4 |
|  5 | note  | speaker | Sekretarz Stanu w Ministerstwie Cyfryzacji Marek Zagórski:                                                  | pl         |        7 |


Statistics for tags:

|          |   tag |
|:---------|------:|
| vocal    | 71724 |
| incident | 29788 |
| note     |  6013 |
| head     |   686 |
| kinesic  |   291 |
| gap      |    11 |


|                          |   type |
|:-------------------------|-------:|
| ('gap', 'inaudible')     |     11 |
| ('head', '')             |    686 |
| ('incident', '')         |  29494 |
| ('incident', 'action')   |    238 |
| ('incident', 'entering') |     32 |
| ('incident', 'leaving')  |     24 |
| ('kinesic', 'applause')  |    170 |
| ('kinesic', 'signal')    |     51 |
| ('kinesic', 'playback')  |     39 |
| ('kinesic', 'ringing')   |     31 |
| ('note', 'time')         |   2682 |
| ('note', 'speaker')      |   2547 |
| ('note', 'debate')       |    510 |
| ('note', 'vote')         |    274 |
| ('vocal', 'speaking')    |  71411 |
| ('vocal', 'shouting')    |    252 |
| ('vocal', 'noise')       |     45 |
| ('vocal', 'laughter')    |     16 |
Translation started.
Translation completed. It took 46.88 minutes for 108513 instances for the entire process of extraction and translation.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
|    | tag   | type    | content                                                                                                     | xml:lang   |   length | translation                                                                                                | corpus   |
|---:|:------|:--------|:------------------------------------------------------------------------------------------------------------|:-----------|---------:|:-----------------------------------------------------------------------------------------------------------|:---------|
|  0 | note  | time    | Wznowienie posiedzenia o godzinie 9 minut 02                                                                | pl         |        7 | Resumption of the meeting at 9 minutes 02                                                                  | PL       |
|  1 | note  | debate  | Posiedzeniu przewodniczą marszałek Stanisław Karczewski oraz wicemarszałkowie Grzegorz Czelej i Adam Bielan | pl         |       12 | The meeting is chaired by Marshal Stanisław Karczewski and Deputy Marshals Grzegorz Czelej and Adam Bielan | PL       |
|  2 | note  | speaker | Marszałek Stanisław Karczewski:                                                                             | pl         |        3 | Marshal Stanisław Karczewski:                                                                              | PL       |
|  3 | note  | speaker | Senator Sprawozdawca Grzegorz Peczkis:                                                                      | pl         |        4 | Rapporteur Senator Grzegorz Pekkis:                                                                        | PL       |
|  5 | note  | speaker | Sekretarz Stanu w Ministerstwie Cyfryzacji Marek Zagórski:                                                  | pl         |        7 | Secretary of State at the Ministry of Digitalization Marek Zagórski:                                       | PL       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-PL.notes.translated.tsv
