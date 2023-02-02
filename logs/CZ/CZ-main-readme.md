# MT of ParlaMint-CZ

Entire corpus has:
- 6,327 files
- 1,804,657 sentences
- 27,952,326 words.

There are 6328 files in the source conll-u folder, but we processed 6327 (one less), because the file "ParlaMint-CZ_2016-10-26-ps2013-050-06-005-217.conllu" is empty.

Time:
- translation took 1011 minutes (around 17 hours)
- tokenization took 89 minutes
- alignment took around 12 minutes
- creation of final conllus took

Unusual things the code reveal: two sentences that have only one word:
- ParlaMint-CZ_2021-07-08-ps2017-111-02-007-395.u16.p24.s5:

```
# sent_id = ParlaMint-CZ_2021-07-08-ps2017-111-02-007-395.u16.p24.s5
# text = s
1	s	s	ADP	_	AdpType=Prep|Case=Ins	0	root	_	NER=O
```
- ParlaMint-CZ_2015-01-23-ps2013-025-04-004-088.u8.p1.s5:

```
# sent_id = ParlaMint-CZ_2015-01-23-ps2013-025-04-004-088.u8.p1.s5
# text = To -
1	To	ten	DET	_	Case=Nom|Gender=Neut|Number=Sing|PronType=Dem	0	root	_	NER=O
2	-	-	PUNCT	_	_	1	punct	_	NER=O
```

83,698 sentences were corrected with proper noun correction - 4.6% of all sentences.

Most frequent substitutions:

|                               |   substituted_pairs |
|:------------------------------|--------------------:|
| [('Faltynek', 'Faltýnek')]    |      2423           |
| [('Andrei', 'Andrej')]        |      2051           |
| [('Schiller', 'Schillerová')] |      1902           |
| [('Pirates', 'pirát')]        |      1289           |
| [('Richter', 'Richterová')]   |      1210           |
| [('Laudat', 'Laudát')]        |      1208           |
| [('Free', 'Volný')]           |      1187           |
| [('Excellent', 'Výborný')]    |      1086           |
| [('Austrian', 'Rakušan')]     |       964           |
| [('Peter', 'Petr')]           |       841           |
| [('Michalek', 'Michálek')]    |       716           |
| [('Philip', 'Filip')]         |       633           |
| [('Mark', 'Marek')]           |       557           |
| [('Wark', 'Válková')]         |       547           |
| [('Vera', 'Věra')]            |       438           |
| [('Kaňkovsky', 'Kaňkovský')]  |       436           |
| [('Pastuch', 'Pastuchová')]   |       434           |
| [('Zaoralek', 'Zaorálek')]    |       426           |
| [('Marks', 'Marksová')]       |       420           |