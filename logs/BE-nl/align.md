2023-04-26 08:02:23 INFO: Loading these models for language: en (English):
========================
| Processor | Package  |
------------------------
| tokenize  | combined |
========================

2023-04-26 08:02:24 INFO: Use device: gpu
2023-04-26 08:02:24 INFO: Loading: tokenize
2023-04-26 08:02:26 INFO: Done loading processors!
Tokenization of the translation started.
Tokenization completed. It took 43.67 minutes.
File saved as /home/tajak/Parlamint-translation/results/BE-nl/ParlaMint-BE-nl-translated-tokenized.csv
|    | file_path                                                                                                                                      | file                                                | sentence_id                                   | text                                                                                                                                                                              | tokenized_text                                                                                                                                                                        | proper_nouns   |   length | lang   | translation                                                                                                                                                                   | translation-tokenized                                                                                                                                                             | space-after-information                                                                                                                                                                                                |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------|:----------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|---------:|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-BE.conllu/ParlaMint-BE.conllu/2017/ParlaMint-BE_2017-05-04-54-plenair-ip166x-nl.conllu | ParlaMint-BE_2017-05-04-54-plenair-ip166x-nl.conllu | ParlaMint-BE_2017-05-04-54-plenair-ip166x.s4  | De vergadering is geopend.                                                                                                                                                        | De vergadering is geopend .                                                                                                                                                           | {}             |        4 | nl     | The meeting is open.                                                                                                                                                          | The meeting is open .                                                                                                                                                             | ['Yes', 'Yes', 'Yes', 'No', 'Last']                                                                                                                                                                                    |
|  1 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-BE.conllu/ParlaMint-BE.conllu/2017/ParlaMint-BE_2017-05-04-54-plenair-ip166x-nl.conllu | ParlaMint-BE_2017-05-04-54-plenair-ip166x-nl.conllu | ParlaMint-BE_2017-05-04-54-plenair-ip166x.s34 | Mijnheer de minister, in 2016 gaf de Belg online 9,1 miljard euro uit.                                                                                                            | Mijnheer de minister , in 2016 gaf de Belg online 9,1 miljard euro uit .                                                                                                              | {}             |       13 | nl     | Minister, in 2016, Belgium spent EUR 9.1 billion online.                                                                                                                      | Minister , in 2016 , Belgium spent EUR 9.1 billion online .                                                                                                                       | ['No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Last']                                                                                                                                     |
|  2 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-BE.conllu/ParlaMint-BE.conllu/2017/ParlaMint-BE_2017-05-04-54-plenair-ip166x-nl.conllu | ParlaMint-BE_2017-05-04-54-plenair-ip166x-nl.conllu | ParlaMint-BE_2017-05-04-54-plenair-ip166x.s35 | Dat wil zeggen dat de Belg ongeveer 16 procent van zijn inkomen online uitgeeft, vooral aan vliegtuigtickets, concerttickets en aan internetbedrijven, zoals Bol.com en Coolblue. | Dat wil zeggen dat de Belg ongeveer 16 procent van zijn inkomen online uitgeeft , vooral aan vliegtuigtickets , concerttickets en aan internetbedrijven , zoals Bol.com en Coolblue . | {}             |       25 | nl     | This means that the Belgian spends around 16 percent of its income online, especially on plane tickets, concert tickets and Internet companies, such as Bol.com and Coolblue. | This means that the Belgian spends around 16 percent of its income online , especially on plane tickets , concert tickets and Internet companies , such as Bol.com and Coolblue . | ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Last'] |






Alignment started.

Number of aligned sentences: 1408103


Issue: index 11: ['Geens', 'Geens']
Issue: index 2: ['De', 'de']
Issue: index 43: ['Van', 'van']
Issue: index 44: ['den', 'den']
Issue: index 5: ['Pas', 'pas']
Issue: index 5: ['Pas', 'pas']
Issue: index 10: ['Peter', 'peter']
Issue: index 15: ['de', 'de']
Issue: index 1: ['de', 'de']
Issue: index 0: ['Wil', 'willen']
Issue: index 6: ['Annick', 'annick']
Issue: index 34: ['Van', 'van']
Issue: index 3: ['De', 'de']
Issue: index 9: ['Pas', 'pas']
Issue: index 20: ['de', 'de']
Issue: index 1: ['David', 'david']
Issue: index 1: ['De', 'de']
Issue: index 0: ['Wil', 'willen']
Issue: index 6: ['Jan', 'jan']
Issue: index 5: ['De', 'de']
Issue: index 23: ['Van', 'van']
Issue: index 3: ['De', 'de']
Issue: index 12: ['De', 'de']
Issue: index 8: ['Top', 'top']
Issue: index 12: ['Van', 'van']
Issue: index 16: ['Pas', 'pas']
Issue: index 23: ['de', 'de']
Issue: index 9: ['Top', 'Top']
Issue: index 3: ['Dan', 'dan']
Issue: index 4: ['Dan', 'dan']
Issue: index 23: ['Personen', 'persoon']
Issue: index 12: ['Bij', 'bij']
Issue: index 11: ['De', 'de']
Issue: index 32: ['De', 'de']
Issue: index 6: ['de', 'de']
Issue: index 1: ['Pas', 'pas']
Issue: index 1: ['D’Haese', 'D’Haese']
Issue: index 2: ['Van', 'van']
Issue: index 0: ['Wil', 'willen']
Issue: index 29: ['Van', 'van']
Issue: index 17: ['Dan', 'dan']
Issue: index 0: ['Wil', 'willen']
Issue: index 5: ['Van', 'van']
Issue: index 5: ['De', 'de']
Issue: index 8: ['de', 'de']
Issue: index 7: ['Pas', 'pas']
Issue: index 4: ['Troosters', 'trooster']
Issue: index 1: ['Vooruit', 'vooruit']
Issue: index 1: ['Troosters', 'trooster']
Issue: index 3: ['Vooruit', 'vooruit']
Issue: index 12: ['Vooruit', 'Vooruit']
Issue: index 20: ['Frank', 'frank']
Issue: index 4: ['Van', 'van']
Issue: index 5: ['der', 'der']
Issue: index 0: ['Houdt', 'houden']
Issue: index 10: ['De', 'de']
Issue: index 16: ['Peter', 'peter']
Issue: index 8: ['Vooruit', 'Vooruit']
Issue: index 0: ['Houdt', 'houden']
Issue: index 1: ['Vooruit', 'vooruit']
Issue: index 8: ['Ben', 'ben']
Issue: index 4: ['Vooruit', 'vooruit']
Issue: index 2: ['Kluge', 'Kluge']
Issue: index 0: ['Van', 'van']
Issue: index 2: ['De', 'de']
Issue: index 4: ['Van', 'van']
Issue: index 5: ['der', 'der']
Issue: index 20: ['De', 'de']
Issue: index 5: ['Pas', 'pas']
Issue: index 5: ['Pas', 'pas']
Issue: index 4: ['Vooruit', 'vooruit']
Issue: index 10: ['De', 'de']
Issue: index 5: ['Nabil', 'nabil']
Issue: index 13: ['De', 'de']
Issue: index 4: ['Dan', 'dan']
Issue: index 7: ['Ben', 'ben']
Issue: index 1: ['Troosters', 'trooster']
Issue: index 19: ['Pas', 'pas']
Issue: index 4: ['Vooruit', 'vooruit']
Issue: index 17: ['De', 'de']
Issue: index 16: ['Van', 'van']
Issue: index 0: ['Verlinden', 'Verlinden']
Issue: index 20: ['Peter', 'peter']
Issue: index 4: ['De', 'de']
Issue: index 5: ['Van', 'van']
Issue: index 9: ['Van', 'van']
Issue: index 3: ['Van', 'van']
Issue: index 10: ['Ben', 'zijn']
Issue: index 9: ['Van', 'van']
Issue: index 10: ['de', 'de']
Issue: index 4: ['Van', 'van']
Issue: index 8: ['Van', 'van']
Issue: index 26: ['Pas', 'pas']
Issue: index 11: ['Brecht', 'brecht']
Issue: index 1: ['De', 'de']
Issue: index 27: ['Pas', 'pas']
Issue: index 16: ['De', 'de']
Issue: index 17: ['De', 'de']
Issue: index 14: ['Van', 'van']
Issue: index 4: ['Van', 'van']
Issue: index 18: ['Maggie', 'maggie']
Issue: index 0: ['De', 'de']
Issue: index 5: ['D’Haese', 'D’Haese']
Issue: index 22: ['van', 'van']
Issue: index 2: ['Wim', 'wim']
Issue: index 5: ['Wim', 'wim']
Issue: index 1: ['Troosters', 'trooster']
Issue: index 16: ['Van', 'van']
Issue: index 8: ['Wim', 'wim']
Issue: index 11: ['CEO', 'CEO']
Issue: index 27: ['Peter', 'peter']
Issue: index 13: ['Troosters', 'trooster']
Issue: index 3: ['De', 'de']
Issue: index 10: ['De', 'de']
Issue: index 3: ['De', 'de']
Issue: index 3: ['De', 'de']
Issue: index 7: ['De', 'de']
Issue: index 3: ['De', 'de']
Issue: index 19: ['Van', 'van']
Issue: index 5: ['Peter', 'peter']
Issue: index 0: ['Wil', 'willen']
Issue: index 16: ['De', 'de']
Issue: index 4: ['Van', 'van']
Issue: index 5: ['De', 'de']
Issue: index 3: ['De', 'de']
Issue: index 11: ['Jan', 'jan']
Issue: index 6: ['Pas', 'pas']
Issue: index 12: ['De', 'de']
Issue: index 12: ['De', 'de']
Issue: index 6: ['Pas', 'pas']
Issue: index 6: ['Pas', 'pas']
Issue: index 4: ['De', 'de']
Issue: index 11: ['Staat', 'staat']
Issue: index 8: ['A', 'a']
Issue: index 14: ['Ben', 'ben']
Issue: index 91: ['De', 'de']
Issue: index 30: ['Van', 'van']
Issue: index 18: ['De', 'de']
Issue: index 28: ['De', 'de']
Issue: index 19: ['Pas', 'pas']
Issue: index 40: ['Jan', 'jan']
Issue: index 41: ['De', 'de']
Issue: index 42: ['Volder', 'volder']
Issue: index 0: ['Wil', 'willen']
Issue: index 19: ['Ben', 'ben']
Issue: index 5: ['cs', 'cs']
Issue: index 13: ['Van', 'van']
Issue: index 13: ['Van', 'van']
Issue: index 7: ['Egbert', 'egbert']
Issue: index 4: ['Van', 'van']
Issue: index 5: ['der', 'der']
Issue: index 4: ['Van', 'van']
Issue: index 5: ['der', 'der']
Issue: index 4: ['Van', 'van']
Issue: index 5: ['der', 'der']
Issue: index 4: ['Wim', 'wim']
Issue: index 4: ['Ben', 'ben']
Alignment completed. It took 4.55 minutes.
|                                                    |   substituted_pairs |
|:---------------------------------------------------|--------------------:|
| 0                                                  |         1.36156e+06 |
| [('De', 'de')]                                     |      1573           |
| [('Vote', 'Stemming/vote')]                        |      1346           |
| [('De', 'de'), ('Roover', 'roover')]               |      1040           |
| [('De', 'de'), ('Block', 'block')]                 |       873           |
| [('De', 'de'), ('Vriendt', 'vriendt')]             |       683           |
| [('Van', 'van'), ('Quickenborne', 'quickenborne')] |       665           |
| [('Van', 'van'), ('Camp', 'camp')]                 |       621           |
| [('Van', 'van'), ('Hecke', 'hecke')]               |       613           |
| [('De', 'de'), ('Coninck', 'coninck')]             |       518           |
| [('Voting', 'Stemming/vote')]                      |       504           |
| [('De', 'de'), ('Croo', 'croo')]                   |       492           |
| [('Catherine', 'catherine'), ('Fonck', 'fonck')]   |       476           |
| [('Van', 'van'), ('Hoof', 'hoof')]                 |       453           |
| [('Van', 'van'), ('Overtveldt', 'overtveldt')]     |       424           |
| [('Van', 'van'), ('Rompuy', 'rompuy')]             |       410           |
| [('Van', 'van'), ('Peteghem', 'peteghem')]         |       383           |
| [('Van', 'van'), ('Maelen', 'maelen')]             |       378           |
| [('Pas', 'pas')]                                   |       345           |
| [('Van', 'van'), ('Bossuyt', 'bossuyt')]           |       327           |



Number of errors:
(147, 20)



Example of sentences with substituted words.
|    | file_path                                                                                                                                      | file                                                | sentence_id                                   | text                                                                                                                                                                                 | tokenized_text                                                                                                                                                                            | proper_nouns                                            |   length | lang   | translation                                                                                                                              | translation-tokenized                                                                                                                          | space-after-information                                                                                                                                                                                                     | fwd_align_dict                                                                                                                                                                                                                                                                                        | bwd_align_dict                                                                                                                                                                                                                                                    | alignments                                                                                                                                                                                                | new_translations                                                                                                                                | substitution_info                                                  | substituted_pairs       | substituted_words   | errors   | source_indices                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------|:----------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------|---------:|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------|:------------------------|:--------------------|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 42 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-BE.conllu/ParlaMint-BE.conllu/2017/ParlaMint-BE_2017-05-04-54-plenair-ip166x-nl.conllu | ParlaMint-BE_2017-05-04-54-plenair-ip166x-nl.conllu | ParlaMint-BE_2017-05-04-54-plenair-ip166x.s77 | Dat is volledig het voorstel van collega Ceysens dat in de wet werd ingeschreven.                                                                                                    | Dat is volledig het voorstel van collega Ceysens dat in de wet werd ingeschreven .                                                                                                        | {7: ['Ceysens', 'Ceysens']}                             |       14 | nl     | That is the proposal put forward by Mr Ceysen, who has been incorporated into the law.                                                   | That is the proposal put forward by Mr Ceysen , who has been incorporated into the law .                                                       | ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Last']                                                                                               | {1: '1', 2: '2', 3: '4', 4: '5', 7: '6', 8: '7', 9: '8', 11: '9', 13: '13', 14: '14', 15: '10', 16: '11', 17: '12', 18: '15'}                                                                                                                                                                         | {1: '1', 2: '2', 3: '4', 4: '5', 7: '6', 8: '7', 9: '8', 11: '9', 15: '10', 16: '11', 17: '12', 13: '13', 14: '14', 18: '15'}                                                                                                                                     | {0: 0, 1: 1, 3: 2, 4: 3, 5: 6, 6: 7, 7: 8, 8: 10, 9: 14, 10: 15, 11: 16, 12: 12, 13: 13, 14: 17}                                                                                                          | That is the proposal put forward by Mr Ceysens , who has been incorporated into the law .                                                       | [('Ceysen', 'Ceysens')]                                            | [('Ceysen', 'Ceysens')] | {9: 'Ceysen'}       | No       | [['Dat', 1], ['is', 2], ['volledig', 3], ['het', 4], ['voorstel', 5], ['van', 6], ['collega', 7], ['Ceysens', 8], ['dat', 9], ['in', 10], ['de', 11], ['wet', 12], ['werd', 13], ['ingeschreven', 14], ['.', 15]]                                                                                                                                                                                                                                                        |
| 43 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-BE.conllu/ParlaMint-BE.conllu/2017/ParlaMint-BE_2017-05-04-54-plenair-ip166x-nl.conllu | ParlaMint-BE_2017-05-04-54-plenair-ip166x-nl.conllu | ParlaMint-BE_2017-05-04-54-plenair-ip166x.s78 | Die kader-cao, mijnheer Janssen, ligt eigenlijk al achter ons: wij hebben die netjes in de wet ingeschreven, overeenkomstig het wetsvoorstel van collega Ceysens een tijdje geleden. | Die kader-cao , mijnheer Janssen , ligt eigenlijk al achter ons : wij hebben die netjes in de wet ingeschreven , overeenkomstig het wetsvoorstel van collega Ceysens een tijdje geleden . | {4: ['Janssen', 'Janssen'], 26: ['Ceysens', 'Ceysens']} |       26 | nl     | In fact, Mr Janssen, this framework cao is behind us: we duly registered it in the law, in accordance with Mr Ceysen's bill a while ago. | In fact , Mr Janssen , this framework cao is behind us : we duly registered it in the law , in accordance with Mr Ceysen 's bill a while ago . | ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Last'] | {2: '8', 3: '3', 4: '4', 5: '5', 6: '6', 7: '1', 8: '2', 9: '2', 10: '7', 11: '10', 12: '11', 13: '12', 14: '13', 15: '16', 16: '20', 17: '15', 18: '17', 19: '18', 20: '19', 21: '21', 22: '22', 23: '22', 24: '22', 25: '26', 26: '27', 27: '23', 28: '24', 29: '28', 30: '29', 31: '30', 32: '31'} | {7: '1', 8: '2', 3: '3', 4: '4', 5: '5', 6: '6', 10: '7', 11: '10', 12: '11', 13: '12', 14: '13', 15: '16', 18: '17', 19: '18', 20: '19', 16: '20', 21: '21', 23: '22', 27: '23', 28: '24', 24: '25', 25: '26', 26: '27', 29: '28', 30: '29', 31: '30', 32: '31'} | {0: 6, 1: 7, 2: 2, 3: 3, 4: 4, 5: 5, 6: 9, 9: 10, 10: 11, 11: 12, 12: 13, 15: 14, 16: 17, 17: 18, 18: 19, 19: 15, 20: 20, 21: 22, 22: 26, 23: 27, 24: 23, 25: 24, 26: 25, 27: 28, 28: 29, 29: 30, 30: 31} | In fact , Mr Janssen , this framework cao is behind us : we duly registered it in the law , in accordance with Mr Ceysens 's bill a while ago . | ["No substitution: ('Janssen', 'Janssen')", ('Ceysen', 'Ceysens')] | [('Ceysen', 'Ceysens')] | {26: 'Ceysen'}      | No       | [['Die', 1], ['kader-cao', 2], [',', 3], ['mijnheer', 4], ['Janssen', 5], [',', 6], ['ligt', 7], ['eigenlijk', 8], ['al', 9], ['achter', 10], ['ons', 11], [':', 12], ['wij', 13], ['hebben', 14], ['die', 15], ['netjes', 16], ['in', 17], ['de', 18], ['wet', 19], ['ingeschreven', 20], [',', 21], ['overeenkomstig', 22], ['het', 23], ['wetsvoorstel', 24], ['van', 25], ['collega', 26], ['Ceysens', 27], ['een', 28], ['tijdje', 29], ['geleden', 30], ['.', 31]] |
