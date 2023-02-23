2023-02-21 14:51:47 INFO: Loading these models for language: en (English):
========================
| Processor | Package  |
------------------------
| tokenize  | combined |
========================

2023-02-21 14:51:47 INFO: Use device: gpu
2023-02-21 14:51:47 INFO: Loading: tokenize
2023-02-21 14:51:49 INFO: Done loading processors!
Tokenization of the translation started.
Tokenization completed. It took 128.31 minutes.
File saved as /home/tajak/Parlamint-translation/results/AT/ParlaMint-AT-translated-tokenized.csv
|    | file_path                                                                                                                                       | file                                                 | sentence_id                                             | text                                                                                                                                                                                                                                              | tokenized_text                                                                                                                                                                                                                                               | proper_nouns   |   length | translation                                                                                                                                                                                                                                  | translation-tokenized                                                                                                                                                                                                                              | space-after-information                                                                                                                                                                                                                                                                                                |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------|:--------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|---------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2013/ParlaMint-AT_2013-02-19-024-XXIV-NRSITZ-00190.conllu | ParlaMint-AT_2013-02-19-024-XXIV-NRSITZ-00190.conllu | ParlaMint-AT_2013-02-19-024-XXIV-NRSITZ-00190_d2e196.s1 | Guten Tag, meine Damen und Herren!                                                                                                                                                                                                                | Guten Tag , meine Damen und Herren !                                                                                                                                                                                                                         | {}             |        6 | Good day, ladies and gentlemen!                                                                                                                                                                                                              | Good day , ladies and gentlemen !                                                                                                                                                                                                                  | ['Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Last']                                                                                                                                                                                                                                                                       |
|  1 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2013/ParlaMint-AT_2013-02-19-024-XXIV-NRSITZ-00190.conllu | ParlaMint-AT_2013-02-19-024-XXIV-NRSITZ-00190.conllu | ParlaMint-AT_2013-02-19-024-XXIV-NRSITZ-00190_d2e196.s2 | Ich eröffne die 190. Sitzung des Nationalrates, die aufgrund eines ausreichend unterstützten Verlangens gemäß § 46 Abs. 7 des Geschäftsordnungsgesetzes einberufen wurde.                                                                         | Ich eröffne die 190. Sitzung des Nationalrates , die aufgrund eines ausreichend unterstützten Verlangens gemäß § 46 Abs. 7 des Geschäftsordnungsgesetzes einberufen wurde .                                                                                  | {}             |       22 | I'll open the 190. Meeting of the National Council, which is based on a sufficiently supported request in accordance with § 46 para. 7 of the Rules of Procedure.                                                                            | I 'll open the 190 . Meeting of the National Council , which is based on a sufficiently supported request in accordance with § 46 para . 7 of the Rules of Procedure .                                                                             | ['No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Last']                                                                             |
|  2 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2013/ParlaMint-AT_2013-02-19-024-XXIV-NRSITZ-00190.conllu | ParlaMint-AT_2013-02-19-024-XXIV-NRSITZ-00190.conllu | ParlaMint-AT_2013-02-19-024-XXIV-NRSITZ-00190_d2e198.s1 | Die nicht verlesenen Teile des Amtlichen Protokolls der 187. Sitzung vom 30. Jän- ner 2013 sowie die Amtlichen Protokolle der 188. und 189. Sitzung vom 31. Jän- ner 2013 sind in der Parlamentsdirektion aufgelegen und unbeanstandet geblieben. | Die nicht verlesenen Teile des Amtlichen Protokolls der 187. Sitzung von dem 30. Jän - ner 2013 sowie die Amtlichen Protokolle der 188. und 189. Sitzung von dem 31. Jän - ner 2013 sind in der Parlamentsdirektion aufgelegen und unbeanstandet geblieben . | {}             |       37 | The unreaded parts of the 187 Official Protocol. Meeting of 30 March 1990 In January 2013 as well as the official protocols of 188 and 189. Meeting of 31. In January 2013, the Parliament's Directorate remained disquieted and undisputed. | The unreaded parts of the 187 Official Protocol . Meeting of 30 March 1990 In January 2013 as well as the official protocols of 188 and 189 . Meeting of 31 . In January 2013 , the Parliament 's Directorate remained disquieted and undisputed . | ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Last'] |






Alignment started.

Number of aligned sentences: 3919672


Issue: index 7: ['Auer', 'Auer']
Issue: index 9: ['Auer', 'Auer']
Issue: index 0: ['Auer', 'Auer']
Issue: index 0: ['Scheibner', 'Scheibner']
Issue: index 10: ['der', 'der']
Issue: index 1: ['Botschafterin', 'Botschafterin']
Issue: index 6: ['von', 'von']
Issue: index 6: ['DEM', 'der']
Issue: index 10: ['Kammerlander', 'Kammerlander']
Issue: index 3: ['Abgeordneter', 'Abgeordnet']
Issue: index 30: ['der', 'der']
Issue: index 6: ['der', 'der']
Issue: index 39: ['DEM', 'der']
Issue: index 4: ['Schüssel', 'Schüssel']
Issue: index 27: ['Schüssel', 'Schüssel']
Issue: index 0: ['Kammerlander', 'Kammerlander']
Issue: index 9: ['der', 'der']
Issue: index 14: ['Scheibner', 'Scheibner']
Issue: index 11: ['von', 'von']
Issue: index 44: ['von', 'von']
Issue: index 4: ['Abgeordneter', 'Abgeordneter']
Issue: index 10: ['Einem', 'Einem']
Issue: index 7: ['Einem', 'Einem']
Issue: index 9: ['Schüssel', 'Schüssel']
Issue: index 7: ['Einem', 'Einem']
Issue: index 12: ['Scheibner', 'Scheibner']
Issue: index 7: ['von', 'von']
Issue: index 15: ['der', 'der']
Issue: index 18: ['–', '–']
Issue: index 5: ['Auer', 'Auer']
Issue: index 7: ['Auer', 'Auer']
Issue: index 3: ['Einem', 'Einem']
Issue: index 22: ['Ausserwinkler', 'Ausserwinkler']
Issue: index 3: ['Klima', 'Klima']
Issue: index 22: ['drinnen', 'drinnen']
Issue: index 25: ['Kurz', 'Kurz']
Issue: index 17: ['von', 'von']
Issue: index 15: ['Schüssel', 'Schüssel']
Issue: index 7: ['Schüssel', 'Schüssel']
Issue: index 7: ['nen', 'nen']
Issue: index 25: ['Schüssel', 'Schüssel']
Issue: index 0: ['Ausserwinkler', 'Ausserwinkler']
Issue: index 1: ['Schüssel', 'Schüssel']
Issue: index 5: ['Auer', 'Auer']
Issue: index 11: ['„', '„']
Issue: index 11: ['Strache', 'Strache']
Issue: index 0: ['Auer', 'Auer']
Issue: index 10: ['Einem', 'Einem']
Issue: index 1: ['der', 'der']
Issue: index 19: ['Schüssel', 'Schüssel']
Issue: index 24: ['dem', 'dem']
Issue: index 5: ['Einem', 'ein']
Issue: index 3: ['Vor', 'Vor']
Issue: index 4: ['dem', 'dem']
Issue: index 9: ['Einem', 'Einem']
Issue: index 40: ['Schüssel', 'Schüssel']
Issue: index 2: ['Gott', 'Gott']
Issue: index 13: ['Schüssel', 'Schüssel']
Issue: index 19: ['Schüssel', 'Schüssel']
Issue: index 13: ['II', 'II']
Issue: index 9: ['Einem', 'Einem']
Issue: index 45: ['–', '–']
Issue: index 14: ['Schüssel', 'Schüssel']
Issue: index 0: ['Auer', 'Auer']
Issue: index 13: ['der', 'der']
Issue: index 6: ['Scheibner', 'Scheibner']
Issue: index 13: ['Gott', 'Gott']
Issue: index 12: ['Gott', 'Gott']
Issue: index 19: ['Abgeordneter', 'Abgeordnet']
Issue: index 7: ['Strache', 'Strache']
Issue: index 12: ['nen', 'nen']
Issue: index 23: ['Troch', 'Troch']
Issue: index 1: ['Troch', 'Troch']
Issue: index 34: ['Aha', 'Aha']
Issue: index 16: ['Pilz', 'Pilz']
Issue: index 4: ['Strache', 'Strache']
Issue: index 14: ['Gott', 'Gott']
Issue: index 9: ['Einem', 'Einem']
Issue: index 8: ['Schüssel', 'Schüssel']
Issue: index 12: ['Scheibner', 'Scheibner']
Issue: index 18: ['der', 'der']
Issue: index 6: ['Einem', 'Einem']
Issue: index 4: ['der', 'der']
Issue: index 125: ['von', 'von']
Issue: index 6: ['Niederwieser', 'Niederwieser']
Issue: index 4: ['Niederwieser', 'Niederwieser']
Issue: index 8: ['Einem', 'Einem']
Issue: index 10: ['Einem', 'Einem']
Issue: index 8: ['Scheibner', 'Scheibner']
Issue: index 20: ['Schüssel', 'Schüssel']
Issue: index 18: ['der', 'der']
Issue: index 1: ['Auer', 'Auer']
Issue: index 19: ['Ahnen', 'Ahnen']
Issue: index 3: ['nämlich', 'nämlich']
Issue: index 0: ['Schüssel', 'Schüssel']
Issue: index 8: ['Einem', 'Einem']
Issue: index 1: ['Ministerin', 'Ministerin']
Issue: index 44: ['Gott', 'Gott']
Issue: index 32: ['Vor', 'Vor']
Issue: index 33: ['dem', 'dem']
Issue: index 4: ['Schüssel', 'Schüssel']
Issue: index 0: ['Schüssel', 'Schüssel']
Issue: index 2: ['dem', 'dem']
Issue: index 7: ['Klima', 'Klima']
Issue: index 5: ['Schüssel', 'Schüssel']
Issue: index 8: ['Schüssel', 'Schüssel']
Issue: index 2: ['Schüssel', 'Schüssel']
Issue: index 2: ['der', 'der']
Issue: index 0: ['Schüssel', 'Schüssel']
Issue: index 8: ['Einem', 'Einem']
Issue: index 8: ['Einem', 'Einem']
Issue: index 8: ['Schüssel', 'Schüssel']
Issue: index 12: ['Schüssel', 'Schüssel']
Issue: index 21: ['Schüssel', 'Schüssel']
Issue: index 19: ['Wurm', 'Wurm']
Issue: index 10: ['Schüssel', 'Schüssel']
Issue: index 21: ['Einem', 'ein']
Issue: index 1: ['Einem', 'Einem']
Issue: index 5: ['Scheibner', 'Scheibner']
Issue: index 6: ['Einem', 'Einem']
Issue: index 7: ['Einem', 'Einem']
Issue: index 60: ['Einem', 'ein']
Issue: index 0: ['Stacher', 'Stacher']
Issue: index 0: ['Stacher', 'Stacher']
Issue: index 0: ['Anschober', 'Anschober']
Issue: index 1: ['der', 'der']
Issue: index 14: ['Einem', 'Einem']
Issue: index 2: ['Ausserwinkler', 'Ausserwinkler']
Issue: index 0: ['Schüssel', 'Schüssel']
Issue: index 24: ['Einem', 'ein']
Issue: index 3: ['etwa', 'etwa']
Issue: index 0: ['Schüssel', 'Schüssel']
Issue: index 10: ['Anschober', 'Anschober']
Issue: index 6: ['Abgeordneter', 'Abgeordnet']
Issue: index 3: ['Scheibner', 'Scheibner']
Issue: index 0: ['Kammerlander', 'Kammerlander']
Issue: index 9: ['der', 'der']
Issue: index 19: ['von', 'von']
Issue: index 32: ['von', 'von']
Issue: index 33: ['der', 'der']
Issue: index 13: ['der', 'der']
Issue: index 5: ['Brauneder', 'Brauneder']
Issue: index 22: ['Gott', 'Gott']
Issue: index 16: ['Gross', 'Gross']
Issue: index 15: ['Rosenstingl', 'Rosenstingl']
Issue: index 8: ['Einem', 'Einem']
Issue: index 7: ['Einem', 'Einem']
Issue: index 6: ['der', 'der']
Issue: index 11: ['Schlögl', 'Schlögl']
Issue: index 2: ['Brauneder', 'Brauneder']
Issue: index 3: ['Einem', 'Einem']
Issue: index 6: ['Anschober', 'Anschober']
Issue: index 68: ['Anschober', 'Anschober']
Issue: index 5: ['drinnen', 'drinnen']
Issue: index 1: ['Abgeordneten', 'Abgeordnet']
Issue: index 13: ['Schüssel', 'Schüssel']
Issue: index 9: ['Klima', 'Klima']
Issue: index 1: ['Scheibner', 'Scheibner']
Issue: index 8: ['Ministerin', 'Ministerin']
Issue: index 11: ['von', 'von']
Issue: index 7: ['Strache', 'Strache']
Issue: index 0: ['Auer', 'Auer']
Issue: index 4: ['Gott', 'Gott']
Issue: index 9: ['Auer', 'Auer']
Issue: index 9: ['der', 'der']
Issue: index 14: ['Gott', 'Gott']
Issue: index 0: ['Auer', 'Auer']
Issue: index 0: ['Schüssel', 'Schüssel']
Issue: index 21: ['Schüssel', 'Schüssel']
Issue: index 15: ['Gott', 'Gott']
Issue: index 0: ['Schüssel', 'Schüssel']
Issue: index 29: ['Schüssel', 'Schüssel']
Issue: index 11: ['Schüssel', 'Schüssel']
Issue: index 15: ['der', 'der']
Issue: index 0: ['Schüssel', 'Schüssel']
Issue: index 17: ['von', 'von']
Issue: index 3: ['DEM', 'DEM']
Issue: index 11: ['Klement', 'Klement']
Issue: index 9: ['der', 'der']
Issue: index 9: ['Schüssel', 'Schüssel']
Issue: index 0: ['Schüssel', 'Schüssel']
Issue: index 6: ['der', 'der']
Issue: index 4: ['Gott', 'Gott']
Issue: index 27: ['Scheibner', 'Scheibner']
Issue: index 0: ['Strache', 'Strache']
Issue: index 4: ['Scheibner', 'Scheibner']
Issue: index 4: ['Scheibner', 'Scheibner']
Issue: index 13: ['Ernst“', 'Ernst“']
Issue: index 0: ['Schüssel', 'Schüssel']
Issue: index 14: ['Schüssel', 'Schüssel']
Issue: index 54: ['Strache', 'Strache']
Issue: index 8: ['Bösch', 'Bösch']
Issue: index 0: ['Auer', 'Auer']
Issue: index 8: ['Einem', 'Einem']
Issue: index 7: ['Gott', 'Gott']
Issue: index 1: ['Gross', 'Gross']
Issue: index 8: ['der', 'der']
Issue: index 13: ['Scheibner', 'Scheibner']
Issue: index 10: ['Einem', 'Einem']
Issue: index 9: ['Einem', 'Einem']
Issue: index 0: ['Schüssel', 'Schüssel']
Issue: index 12: ['Ministerin', 'Ministerin']
Issue: index 7: ['Einem', 'Einem']
Issue: index 9: ['Einem', 'Einem']
Issue: index 32: ['Abgeordneter', 'Abgeordneter']
Issue: index 4: ['Verzetnitsch', 'Verzetnitsch']
Issue: index 2: ['Kollege', 'Kollege']
Issue: index 7: ['von', 'von']
Issue: index 3: ['Pröll', 'Pröll']
Issue: index 26: ['terreich', 'terreich']
Issue: index 19: ['Abgeordneter', 'Abgeordnet']
Issue: index 2: ['Strache', 'Strache']
Issue: index 0: ['Anschober', 'Anschober']
Issue: index 25: ['–', '–']
Issue: index 6: ['Strache', 'Strache']
Issue: index 0: ['Auer', 'Auer']
Issue: index 29: ['Abgeordneten', 'Abgeordnet']
Issue: index 40: ['Strache', 'Strache']
Issue: index 4: ['Auer', 'Auer']
Issue: index 10: ['Ausserwinkler', 'Ausserwinkler']
Issue: index 9: ['Einem', 'Einem']
Issue: index 10: ['Einem', 'Einem']
Issue: index 13: ['zu', 'zu']
Issue: index 6: ['Einem', 'Einem']
Issue: index 0: ['Auer', 'Auer']
Issue: index 8: ['Einem', 'Einem']
Issue: index 7: ['Einem', 'Einem']
Issue: index 34: ['Einem', 'ein']
Issue: index 13: ['–', '–']
Issue: index 14: ['Schüssel', 'Schüssel']
Issue: index 9: ['Schüssel', 'Schüssel']
Issue: index 89: ['Scheibner', 'Scheibner']
Issue: index 21: ['Auer', 'Auer']
Issue: index 3: ['Einem', 'ein']
Issue: index 24: ['Ministerin', 'Ministerin']
Issue: index 0: ['Gehrer', 'Gehrer']
Issue: index 0: ['Einem', 'ein']
Issue: index 29: ['von', 'von']
Issue: index 70: ['Strache', 'Strache']
Issue: index 0: ['Auer', 'Auer']
Issue: index 0: ['Pröll', 'Pröll']
Issue: index 30: ['Pröll', 'Pröll']
Issue: index 0: ['Auer', 'Auer']
Issue: index 27: ['Schüssel', 'Schüssel']
Issue: index 37: ['Bösch', 'Bösch']
Issue: index 13: ['Schüssel', 'Schüssel']
Issue: index 22: ['Schüssel', 'Schüssel']
Issue: index 1: ['Schüssel', 'Schüssel']
Issue: index 9: ['Einem', 'Einem']
Issue: index 11: ['Gott', 'Gott']
Issue: index 1: ['Schender', 'Schender']
Issue: index 7: ['vor', 'vor']
Issue: index 8: ['dem', 'dem']
Issue: index 45: ['Kickl', 'Kickl']
Issue: index 5: ['Abgeordneter', 'Abgeordnet']
Issue: index 7: ['Kurz', 'Kurz']
Issue: index 27: ['von', 'von']
Issue: index 28: ['der', 'der']
Issue: index 3: ['la', 'la']
Issue: index 15: ['Anschober', 'Anschober']
Issue: index 27: ['von', 'von']
Issue: index 10: ['Strache', 'Strache']
Issue: index 19: ['von', 'von']
Issue: index 4: ['Anschober', 'Anschober']
Issue: index 21: ['Anschober', 'Anschober']
Issue: index 10: ['Willkür', 'Willkür']
Issue: index 24: ['–', '–']
Issue: index 3: ['Abgeordneter', 'Abgeordneter']
Issue: index 4: ['Bösch', 'Bösch']
Issue: index 4: ['der', 'der']
Issue: index 22: ['dran', 'dran']
Issue: index 32: ['Auer', 'Auer']
Issue: index 6: ['Einem', 'Einem']
Issue: index 6: ['Schüssel', 'Schüssel']
Issue: index 16: ['Gehrer', 'Gehrer']
Issue: index 6: ['Ministerin', 'Ministerin']
Issue: index 11: ['Schüssel', 'Schüssel']
Issue: index 7: ['Einem', 'ein']
Issue: index 8: ['Einem', 'Einem']
Issue: index 2: ['Schüssel', 'Schüssel']
Issue: index 8: ['plump', 'plump']
Issue: index 1: ['Schüssel', 'Schüssel']
Issue: index 10: ['Abgeordneter', 'Abgeordnet']
Issue: index 35: ['Schüssel', 'Schüssel']
Issue: index 5: ['Auer', 'Auer']
Issue: index 8: ['Einem', 'Einem']
Issue: index 12: ['Klement', 'Klement']
Issue: index 4: ['Scheibner', 'Scheibner']
Issue: index 4: ['Scheibner', 'Scheibner']
Issue: index 6: ['Abgeordneter', 'Abgeordnet']
Issue: index 23: ['Pröll', 'Pröll']
Issue: index 6: ['vor', 'vor']
Issue: index 7: ['dem', 'dem']
Issue: index 10: ['Schüssel', 'Schüssel']
Issue: index 7: ['Einem', 'Einem']
Issue: index 6: ['Schüssel', 'Schüssel']
Issue: index 1: ['Schüssel', 'Schüssel']
Issue: index 10: ['Mitterlehner', 'Mitterlehner']
Issue: index 4: ['Schüssel', 'Schüssel']
Issue: index 3: ['dem', 'dem']
Issue: index 6: ['Schüssel', 'Schüssel']
Issue: index 19: ['Bösch', 'Bösch']
Issue: index 10: ['Klug', 'Klug']
Issue: index 8: ['Gott', 'Gott']
Issue: index 11: ['Gott', 'Gott']
Issue: index 5: ['Strache', 'Strache']
Issue: index 31: ['Gott', 'Gott']
Issue: index 20: ['Mitterlehner', 'Mitterlehner']
Issue: index 21: ['II', 'II']
Issue: index 15: ['Krainer', 'Krainer']
Issue: index 1: ['Anschober', 'Anschober']
Issue: index 7: ['Ministerin', 'Ministerin']
Issue: index 0: ['Strache', 'Strache']
Issue: index 13: ['von', 'von']
Issue: index 0: ['Von', 'Von']
Issue: index 5: ['von', 'von']
Issue: index 24: ['Gott', 'Gott']
Issue: index 16: ['Ministerin', 'Ministerin']
Issue: index 0: ['Strache', 'Strache']
Issue: index 22: ['der', 'der']
Issue: index 0: ['Strache', 'Strache']
Issue: index 27: ['Strache', 'Strache']
Issue: index 2: ['An', 'An']
Alignment completed. It took 13.83 minutes.
|                                                       |   substituted_pairs |
|:------------------------------------------------------|--------------------:|
| 0                                                     |         3.80466e+06 |
| [('Mr', 'Abgeordnet')]                                |     17349           |
| [('Minister', 'Ministerin')]                          |      2577           |
| [('Oellinger', 'Öllinger')]                           |      2232           |
| [('Rosenkranz', 'Kranz')]                             |      1628           |
| [('Thank', 'Danke')]                                  |      1623           |
| [('Magistrate', 'Abgeordnet'), ('Abgeordnet', 'Mag')] |      1524           |
| [('Partik', 'Partik-Pablé')]                          |      1074           |
| [('Mr', 'Abgeordneter')]                              |       973           |
| [('Glavischnig', 'Glawischnig')]                      |       843           |
| [('Novotny', 'Nowotny')]                              |       798           |
| [('Heinz', 'Karl-Heinz')]                             |       696           |
| [('Worm', 'Wurm')]                                    |       686           |
| [('God', 'Gott')]                                     |       660           |
| [('Gaßner', 'Gassner')]                               |       653           |
| [('Mr', 'Abgeordnet'), ('Oellinger', 'Öllinger')]     |       648           |
| [('Belakovich', 'Belakowitsch')]                      |       637           |
| [('Heinisch', 'Heinisch-Hosek')]                      |       623           |
| [('thank', 'Gott')]                                   |       562           |
| [('Ollinger', 'Öllinger')]                            |       555           |



Number of errors:
(314, 19)



Example of sentences with substituted words.
|    | file_path                                                                                                                                       | file                                                 | sentence_id                                             | text                                                                                                           | tokenized_text                                                                                                      | proper_nouns                                                                                                                                            |   length | translation                                                                                         | translation-tokenized                                                                                      | space-after-information                                                                                                  | fwd_align_dict                                                                                                                                                      | bwd_align_dict                                                                                                                                    | alignments                                                                                                      | new_translations                                                                                                    | substitution_info                                                                                                                                                       | substituted_pairs                                               | substituted_words               | errors   | source_indices                                                                                                                                                                                                                                                       |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------|:--------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|---------:|:----------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------|:--------------------------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  3 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2013/ParlaMint-AT_2013-02-19-024-XXIV-NRSITZ-00190.conllu | ParlaMint-AT_2013-02-19-024-XXIV-NRSITZ-00190.conllu | ParlaMint-AT_2013-02-19-024-XXIV-NRSITZ-00190_d2e200.s1 | Als verhindert gemeldet sind die Abgeordneten Dr. Bartenstein, Fürntrath-Moretti, Großruck, Obernosterer, Mag. | Als verhindert gemeldet sind die Abgeordneten Dr. Bartenstein , Fürntrath-Moretti , Großruck , Obernosterer , Mag . | {7: ['Bartenstein', 'Bartenstein'], 9: ['Fürntrath-Moretti', 'Fürntrath-Moretti'], 11: ['Großruck', 'Grossruck'], 13: ['Obernosterer', 'Obernosterer']} |       12 | Deputies Dr. Bartenstein, Fürntrath-Moretti, Großruck, Obernosterer, Mag are reported as prevented. | Deputies Dr. Bartenstein , Fürntrath - Moretti , Großruck , Obernosterer , Mag are reported as prevented . | ['Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Last'] | {1: '6', 2: '7', 3: '8', 4: '9', 5: '10', 6: '10', 7: '10', 8: '11', 9: '12', 10: '13', 11: '14', 12: '15', 13: '16', 14: '4', 15: '3', 16: '1', 17: '2', 18: '17'} | {16: '1', 17: '2', 15: '3', 14: '4', 1: '6', 2: '7', 3: '8', 4: '9', 5: '10', 8: '11', 9: '12', 10: '13', 11: '14', 12: '15', 13: '16', 18: '17'} | {0: 15, 1: 16, 2: 14, 3: 13, 5: 0, 6: 1, 7: 2, 8: 3, 9: 4, 10: 7, 11: 8, 12: 9, 13: 10, 14: 11, 15: 12, 16: 17} | Deputies Dr. Bartenstein , Fürntrath-Moretti - Moretti , Grossruck , Obernosterer , Mag are reported as prevented . | ["No substitution: ('Bartenstein', 'Bartenstein')", ('Fürntrath', 'Fürntrath-Moretti'), ('Großruck', 'Grossruck'), "No substitution: ('Obernosterer', 'Obernosterer')"] | [('Fürntrath', 'Fürntrath-Moretti'), ('Großruck', 'Grossruck')] | {5: 'Fürntrath', 9: 'Großruck'} | No       | [['Als', 1], ['verhindert', 2], ['gemeldet', 3], ['sind', 4], ['die', 5], ['Abgeordneten', 6], ['Dr.', 7], ['Bartenstein', 8], [',', 9], ['Fürntrath-Moretti', 10], [',', 11], ['Großruck', 12], [',', 13], ['Obernosterer', 14], [',', 15], ['Mag', 16], ['.', 17]] |
|  7 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2013/ParlaMint-AT_2013-02-19-024-XXIV-NRSITZ-00190.conllu | ParlaMint-AT_2013-02-19-024-XXIV-NRSITZ-00190.conllu | ParlaMint-AT_2013-02-19-024-XXIV-NRSITZ-00190_d2e200.s5 | Schwentner, Dr. Walser, Windbüchler-Souschill, Scheibner, Mag.                                                 | Schwentner , Dr. Walser , Windbüchler-Souschill , Scheibner , Mag .                                                 | {0: ['Schwentner', 'Schwentner'], 3: ['Walser', 'Walser'], 5: ['Windbüchler-Souschill', 'Souschill'], 7: ['Scheibner', 'Scheibner']}                    |        6 | Schwentner, Dr. Walser, Windbüchler-Souschill, Scheibner, Mag.                                      | Schwentner , Dr. Walser , Windbüchler - Souschill , Scheibner , Mag .                                      | ['No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'Last']                                    | {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '6', 8: '6', 9: '7', 10: '8', 11: '9', 12: '10', 13: '11'}                                                      | {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 9: '7', 10: '8', 11: '9', 12: '10', 13: '11'}                                                    | {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 8, 7: 9, 8: 10, 9: 11, 10: 12}                                          | Schwentner , Dr. Walser , Souschill - Souschill , Scheibner , Mag .                                                 | ["No substitution: ('Schwentner', 'Schwentner')", "No substitution: ('Walser', 'Walser')", ('Windbüchler', 'Souschill'), "No substitution: ('Scheibner', 'Scheibner')"] | [('Windbüchler', 'Souschill')]                                  | {6: 'Windbüchler'}              | No       | [['Schwentner', 1], [',', 2], ['Dr.', 3], ['Walser', 4], [',', 5], ['Windbüchler-Souschill', 6], [',', 7], ['Scheibner', 8], [',', 9], ['Mag', 10], ['.', 11]]                                                                                                       |