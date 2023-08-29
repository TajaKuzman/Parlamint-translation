# Machine translating the ParlaMint output

A pipeline for machine translation (using OPUS-MT models) of parliamentary text collections in 30+ languages (ParlaMint corpora). The pipeline includes parsing TEI XLM and CONLL-u files, linguistic processing with the Stanza pipeline, machine translation and word alignment with the Eflomal tool.

Table of contents:
- [pipeline and code](#pipeline)
- [workflow in details](#workflow)
- [translation of notes](#translation-of-notes)
- [list of machine translation models used](#machine-translation-models-used)
- [analysis of errors: proper noun substitutions, space_after errors, MT errors in notes](#sample-analysis)
- [information on processing each corpus](#information-on-processing-each-corpus)

## Pipeline

1. Parse source CONLL-u file: extract info from the source CONLL-u files into a dataframe: `CUDA_VISIBLE_DEVICES=1 nohup python 1-conllu-to-df.py "AT" > logs/AT/to_conllu.md &`
	- output: results/{lang_code}/ParlaMint-{lang_code}-extracted-source-data.csv

2. Choose the model (compare available models on a sample): `2-choose_MT_model.ipynb`
	- The spreadsheet with analyses of samples is available [here](https://docs.google.com/spreadsheets/d/1eeI_ZroO3a4pIb5vl--JW7_UpxANikopkKDOLQ6_1fI/edit?usp=sharing).

3. Machine translate: `CUDA_VISIBLE_DEVICES=1 nohup python 3-translate.py "DK" "da" > logs/DK/translate.md &` (Provide the lang_code and the lang_code as is used by the OPUS-MT system)
	- Output: results/{lang_code}/ParlaMint-{lang_code}-translated.csv

4. Align: `CUDA_VISIBLE_DEVICES=2 nohup python 4-word-alignment.py "IS" > logs/IS/align.md &`:
	- Output:
		1. tokenized text is saved as: results/{lang_code}/ParlaMint-{lang_code}-translated-tokenized.csv
		2. corrected text is saved as: results/{lang_code}/ParlaMint-{lang_code}-final-dataframe.csv
	- if the analysis of most common substitutions reveals that it is better not to do the substitutions:
		- save the translations without the substitutions as the "new-translations" in the final file (in analyse_results.ipynb)
		- in 5-create-conllu.py, add the language code to the exceptions in line 108 (add it also to the file  `9-translate-additional-files.py` in lines 681 and 786)
5. Linguistically process translation and create final CONLL-u files: `CUDA_VISIBLE_DEVICES=2 nohup python 5-create-conllu.py "IS" > logs/IS/create_conllu.md &`
6. If the statistics for the corpus in to_conllu.md showed that some files are missing from the df (because they are empty), add the empty files to the final corpus: `CUDA_VISIBLE_DEVICES=2 nohup python 6-add-empty-files.py "SE" > logs/SE/add_missing_files.md &`
7. Send to partners: `scp -r Final-data/ParlaMint-IS.conllu/ParlaMint-IS.conllu machine_address:~/`.
8. Note translation: `CUDA_VISIBLE_DEVICES=0 nohup python 7-note-translation.py "IS" "is" > logs/IS/translate_notes_final.md &`
	- This code uses the TEI files. If you want to use TEI.ana files, use the following code:
`CUDA_VISIBLE_DEVICES=0 nohup python 7-note-translation-TEI.ana.py "IS" "is" > logs/IS/translate_notes_final_ana.md &` (The code saves the notes as: ParlaMint-IS.notes.translated.ana.tsv)
9. Analyse notes in `8-inspect-and-finalize-notes.ipynb` and delete any notes, written in non-target language.
10. Send the notes to partners: `scp -r Note-translation/Final-data-CSV/ParlaMint-NL.notes.translated.tsv machine_address:~/Notes-translated`

If the corpus consists of two languages (indicated by lang. code at the end of each file, e.g., `-ru.conllu`), first check if they can be both translated well with the same MT system. In that case, process it as usual. If not:
- perform the 1. step as usual
- then separate the df into two dfs in `analyse_results.ipynb` (section Creating 2 datasets in case of bilingual corpora), they will be named for instance `ParlaMint-BE-fr-extracted-source-data.csv` and `ParlaMint-BE-nl-extracted-source-data.csv`
- continue with next steps, but process each file separately by using "BE-fr" and "BE-nl" as the argument instead of BE
- if there are any files missing from the df (because they are empty), use the step 6, but here use "BE" (without lang suffix) as the argument, and add this as an exception to line 19 in `6-add-empty-files.py`.
- for note translation, first add the dictionary of lang and opus codes to line 23 in *7-note-translation-bilingual.py*. Then, use the following code: `CUDA_VISIBLE_DEVICES=2 nohup python 7-note-translation-bilingual.py "BE" > logs/BE/translate_notes_final.md &`

Corpora with more than one language:
- Parlamint-BE (Belgian), which has nl + fr. This is marked on the segments in the TEI, and we produce two sets of CoNLL-U files for them.
- ParlaMint-NO (Norwegian) also has two languages in TEI (Bokmal and Nynorsk), but these are processed with the same model (because the model performs well on both languages), so they have just one CoNLL-U set. We did the same with Ukrainian and Catalan corpus.

If you need to translate just a couple of additional files:
1. Rename the folder with all the files in Source-data to ParlaMint-AT.conllu.main. Create a new folder ParlaMint-AT.conllu/ParlaMint-AT.conllu from which we will process additional files (save the files there).
2. Repeat the steps as when translating the entire corpus with the following code:
 `CUDA_VISIBLE_DEVICES=1 nohup python 9-translate-additional-files.py "DK" "da" > logs/DK/process_additional_files.md &`
3. If the statistics for the corpus in process_additional_files.md showed that some files are missing from the df (because they are empty), add the empty files to the final corpus: `CUDA_VISIBLE_DEVICES=2 nohup python 6.2-add-empty-files-additional.py "SE" > logs/SE/add_missing_files.md &`
4. Send to partners: `scp -r Final-data/ParlaMint-IS.conllu/ParlaMint-IS.conllu machine_address:~/`.
5. We haven't considered translating notes for additional files yet.

The code aligns the words based on the prior file created from the main corpus (which is much larger and thus ensures better alignment). The additional files are saved in the same folder as the original main corpus, so if there were any files with the same name, they overwrite them.

## Workflow

1. Extract information from the CONLL-U
2. Translate with OPUS-MT
3. Tokenize English translations with Stanza
4. Word alignment with Eflomal, get information on NE annotations for each translated word from the source annotations
5. Linguistically process English translation with Stanza (lemmas, POS, NER)
6. Parse CONLL-u file and add additional information (sentence ids, alignments in both directions, source text, SpaceAfter information)

More details:
1. Extract from each sentence in the CONLL-u file:
	- sent_id (in metadata) (# sent_id = ParlaMint-SI_2014-08-01-SDZ7-Redna-01.seg1.1)
	- "text" (in metadata): to be feed into the MT system (# text = Spoštovani, prosim, da zasedete svoja mesta.) - in case of syntactic units, we use the multiword token, not the subparts ("Dovolte mi tedy, abych vás seznámila s omluvami, které předložili členové vlády." - to translate actual words)
	- tokenized text (punctuation separated from words by space): by iterating through the tokens in the sentence - create a list of tokens and join them into a string (["Spoštovani", "prosim", ",", "da"] -> "Spoštovani prosim , da). In case of multiword tokens, we add the subword tokens to the tokenized text and skip the multiword token. We will also get all necessary information about the ids and lemmas from the subword tokens. The subword tokens do not have the NER annotation, so we will use the multiword annotation for all of its subparts. We use the subword tokens instead of multiword tokens to get the correct lemma (multiword tokens do not have lemmata) and also in case that the target proper noun would be aligned with the proper noun in the subword token. So, for alignment, we use the tokenized text with subword tokens (e.g., Dovolte mi tedy, abych vás seznámila s omluvami, které předložili členové vlády.)
	- information on the proper nouns: if the word is annotated as a proper noun (has "PER" in ner attribute), take its index, form and lemma and save it into a dictionary for each sentence ({0: (Taje, Taja), 1: (Kuzman, Kuzman)})
2. Translate
3. Word alignment:
	- We apply the Stanza tokenization over the translation; use tokenize_no_ssplit to avoid splitting sentences in multiple sentences. Save also information on whether there was initially a space around punctuation (based on start_char and end_char information) which we use at the end to remove spaces around the punctuation in the translation.
	- Perform word alignment.
	- Save forward and reverse alignment information for each word - they should be connected with the indices of source words as they appear in the source conllu file. The conllu files start counting with 1, while alignment starts with 0, so to get those indices, we will add "1" to each aligned index.
	- Substitute translated NE words with lemmas based on the alignment to create the new translation. For the words that were substituted, save also a list of the original words (to be added to the conllu).
4. Linguistic processing of translated text:
	- We use Stanza to get POS, lemmas and NER (the 4-tag package: conll03).  We send in the "pre-tokenized text" (created in previous steps).
	- Transform the result into CONLL-u (which should contain tokens, lemmas, pos). Parse the CONLL-u file and add:
		1) sentence_id as metadata
		2) based on alignment, add SpaceAfter information - I add this information only if "SpaceAfter" is "No" (as it is in the source CONLL-u files)
		3) source text ("source")
		4) original translated text (before improvements - #initial_translation metadata) (used only for testing, won't be added in the final conllu)
		5) improved translated text (#text metadata): based on SpaceAfter information, remove spaces around punctuation
		6) Delete startchar and endchar information from ["misc"] metadata element
		7) Change the NER tags so that they correspond to the source NER tags: "S-" to "B-", "E-" to "I-"
		8) For the words that were substituted, add the original translation (#Translated metadata) to ["misc"]
		9) For all words, add information on alignment (#ForwardAlignment and #BackwardAlignment) with the conllu indices of source words (in case of syntactic units, as the alignment is done on subword level, indices point to subwords, not multitokens)
		19) source word indices as metadata ("source_indices") - used only for testing, won't be added in the final conllu
	- Save the file as CONLLU with the same name as the source CONLLU file (so each file will be saved separately). The number of sentences should be the same as in the source CONLLU and TEI.ana file.

This is now implemented, the sample files are:
- sample file with additional information for debugging purposes (initial translation, source_indices: ["results/CZ-old/final_translated_conllu/sample_with_dev_metadata_ParlaMint-CZ_2013-11-25-ps2013-001-01-002-002.conllu"](https://github.com/TajaKuzman/Parlamint-translation/blob/master/results/CZ-old/final_translated_conllu/sample_with_dev_metadata_ParlaMint-CZ_2013-11-25-ps2013-001-01-002-002.conllu)
- final format: ["results/CZ-old/final_translated_conllu/final_sample_ParlaMint-CZ_2013-11-25-ps2013-001-01-002-002.conllu"](https://github.com/TajaKuzman/Parlamint-translation/blob/master/results/CZ-old/final_translated_conllu/final_sample_ParlaMint-CZ_2013-11-25-ps2013-001-01-002-002.conllu)

Some remarks:
- Stanza does not output "SpaceAfter" information, I added it manually based on the start_char and end_char information


## Translation of notes

The notes are taken from the TEI corpus. The elements that are extracted:
- < note >, further specified with the "type" attribute
- < gap >, further specified with the "reason" attribute
- < head >
- < vocal >, further specified with the "type" attribute
- < kinesic >, further specified with the "type" attribute
- < incident >, further specified with the "type" attribute

In < head > and < note >, the text is not encapsulated by additional tags, while in other tags, the text is encapsulated by < desc > and there could be multiple < desc > tags in the element.

If the note is not in the main language of the corpus (a different language is specified by the "xml:lang" attribute), then we do not translate it.

Example of note in foreign language:

```
<gap reason="foreign">
	<desc xml:lang="und">Huliniahuanngittunga</desc>
</gap>
```


Examples of notes in TEI:
```
 <note type="speaker">The president, Dr. Milan Brglez:</note>
...
<note type="vote-ayes">84 voted for the adoption of the measure.</note>
...
<note type="vote-noes">2 voted against the adoption of the measure.</note>

 <vocal type="interruption">
	<desc>sounds from the chamber</desc>
</vocal>
...
<kinesic type="signal">
	<desc>signal for end of debate</desc>
</kinesic>
...
<incident type="action">
	<desc>minute of silence</desc>
</incident>

<vocal type="interruption">
	<desc xml:lang="sl">oglašanje z dvoraner</desc>
	<desc xml:lang="en">sounds from the chamber</desc>
</vocal>¸


... I would further state that
<gap reason="inaudible">
	<desc>speaker spoke too quietly, not understood</desc>
</gap>
and furthermore ...

```

## Machine-translation models used

We used the following models which showed to be the most suitable for each language based on a manual analysis of a translated sample:

| Language | OPUS-MT model |
|---|---|
| Bosnian | zls |
| Bulgarian | bg |
| Catalan | roa |
| Czech | cs |
| Croatian | zls |
| Danish | da |
| Dutch | nl |
| Estonian | et |
| French | fr |
| Galician | itc |
| German | gmw |
| Greek | grk |
| Hungarian | hu |
| Icelandic | is |
| Italian | it |
| Latvian | bat |
| Norwegian | gem |
| Polish | pl |
| Portugese | itc |
| Russian | sla |
| Serbian | zls |
| Slovenian | sla |
| Spanish | roa |
| Swedish | sv |
| Turkish | tr |
| Ukrainian | sla |
| Basque |  |
| Finnish |  |
| Lithuanian |  |
| Romanian |  |

This lang. code was used in the following code:
```
model = EasyNMT('opus-mt')

model.translate(sentence_list, source_lang = "{}".format(opus_lang_code), target_lang='en')
```

### TO DO:


## Sample analysis

I've created a sample of 40 files from the ParlaMint-SI. The sample has 115,993 sentences and 2,496,942 words. It represents roughly 10% of the entire ParlaMint-SI.

Translation took app. 1 hour and alignment took 5 minutes.

In the sample, around 10% of sentences (10,472) consist of proper names. Out of them, in 6039 sentences, at least one proper name was substituted - this means that substitution occurred in 58 % of all sentences with proper nouns, and in 5% of all sentences in the sample.

I analysed the most common substitutions (substitutions that occurred more than 20 times) which represent 30% of all substitutions. Out of all instances of these substitutions, 87% are correct. Incorrect substitutions are connected with wrong NER: "Slovenians", "Slovenec", "Christmas", "Ombudsman" were annotated as proper names.

Most common substitutions:

|                                                          |   substituted_words (word in translation, corrected word) |
|:---------------------------------------------------------|--------------------:|
| [('Mir', 'Miro')]                                        |                 157 |
| [('Slovenians', 'Slovenec')]                             |                 141 |
| [('Left', 'Levica')]                                     |                 112 |
| [('Joseph', 'Jožef')]                                    |                 112 |
| [('Goranak', 'Gorenak')]                                 |                  98 |
| [('Weber', 'Veber')]                                     |                  77 |
| [('Sarca', 'Šarec')]                                     |                  61 |
| [('Levia', 'Levica')]                                    |                  60 |
| [('Fisher', 'Fišer')]                                    |                  57 |
| [('Matthew', 'Matej')]                                   |                  55 |
| [('Trtek', 'Trček')]                                     |                  53 |
| [('Mira', 'Miro')]                                       |                  52 |
| [('Jean', 'Žan')]                                        |                  51 |
| [('Ange', 'Anže')]                                       |                  48 |
| [('Vrtovac', 'Vrtovec')]                                 |                  43 |
| [('Serva', 'Sluga')]                                     |                  42 |
| [('Shabeder', 'Šabeder')]                                |                  41 |
| [('Moon', 'Mesec')]                                      |                  41 |
| [('Sharec', 'Šarec')]                                    |                  38 |
| [('Kordish', 'Kordiš')]                                  |                  38 |
| [('Christmas', 'Božič')]                                 |                  34 |
| [('Jožet', 'Jože'), ('Tank', 'Tanko')]                   |                  33 |
| [('Wilfan', 'Vilfan')]                                   |                  32 |
| [('Franz', 'Franc')]                                     |                  32 |
| [('Murš', 'Muršič')]                                     |                  31 |
| [('Chernach', 'Černač')]                                 |                  30 |
| [('Ombudsman', 'varuh')]                                 |                  30 |
| [('Slovenians', 'Slovenka'), ('Slovenians', 'Slovenec')] |                  29 |
| [('Klemenč', 'Klemenčič')]                               |                  28 |
| [('left', 'Levica')]                                     |                  27 |
| [('Beznik', 'Breznik')]                                  |                  27 |
| [('Makovac', 'Makovec')]                                 |                  26 |
| [('Matic', 'Matić')]                                     |                  25 |
| [('Andrew', 'Andrej'), ('Shirley', 'Šircelj')]           |                  24 |
| [('Ludmila', 'Ljudmila')]                                |                  22 |
| [('Podkraš', 'Podkrajšek')]                              |                  22 |
| [('Dusan', 'Dušan'), ('Verbich', 'Verbič')]              |                  22 |
| [('Alexander', 'Aleksander')]                            |                  21 |
| [('Desus', 'DeSUS')]                                     |                  21 |
| [('Slovenian', 'Slovenec')]                              |                  20 |

### Errors in the substitution process

There were 42 errors (0.4% of sentences with proper nouns) which prevented substitution. Reasons for errors:
- in the machine translation, the proper name was omitted (66% of errors) - inspection of results showed that the MT model is very prone to omitting parts of sentences
- some pairs of sentences (especially quotes) were annotated and tokenized as being one sentence, which led to wrong NER (18% of errors) - words with which the quotes began, were annotated as a proper name (see instances below). This also led to null alignment, because they were not found in the translation.
- null alignments (16% of errors) - some translations differ from the original words so much that eflomal did not align the word to anything

Examples of omission of the proper name:

|       | text                                                                                                                                                                                 | new_translations                                                                                                                                                                 | alignments                                                                                                                                                                                                              | errors                                         |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
|  2086 | Predlagam , da se držite poslovnika na   isti način , kot to zahteva od drugih vaš kolega Trček .                                                                                    | I suggest you stick to the Rules of   Procedure in the same way as it requires of your other colleagues .                                                                        | {0: 1, 2: 2, 4: 3, 5: 6, 6: 9, 7: 11, 8:   12, 10: 13, 11: 14, 12: 15, 13: 16, 14: 18, 15: 17, 16: 19, 18: 20}                                                                                                          | Issue: index 17: ['Trček', 'Trček']            |
| 10679 | Prej je poslanec Trček – potem se mu   je pridružil še poslanec Pavšič – govoril o tem , kako smo vsi soodgovorni ;   tudi tisti , ki nasprotujemo odločitvam v tem državnem zboru . | Earlier , the MEP Trček , who was then   joined by the MEP , spoke about how co-responsible we are , including those   who oppose decisions in this national assembly .          | {0: 0, 1: 1, 2: 3, 3: 4, 4: 5, 5: 8,   9: 9, 11: 12, 13: 13, 14: 14, 15: 15, 18: 16, 19: 18, 21: 17, 22: 20, 23: 21,   24: 22, 26: 23, 27: 24, 28: 25, 29: 26, 30: 27, 31: 28, 32: 29, 33: 30}                          | Issue: index 12: ['Pavšič', 'Pavšič']          |
| 13017 | Kolega Matić je rekel : " Ne   rabimo spoštovati Ustave , zato ker tudi vi , ko ste bili na oblasti , niste   spoštovali odločitev Ustavnega sodišča . " Totalna laž .               | He said : " We do not have to   respect the Constitution , because you too , when you were in power , did not   respect the decision of the Constitutional Court . " Total lie . | {0: 0, 3: 1, 4: 2, 5: 3, 6: 6, 7: 8,   8: 9, 9: 11, 10: 12, 12: 13, 14: 14, 15: 16, 16: 17, 17: 18, 18: 19, 19: 20,   20: 21, 21: 22, 22: 24, 23: 25, 24: 27, 25: 30, 26: 31, 27: 32, 28: 33, 29:   34, 30: 35, 31: 36} | Issue: index 1: ['Matić', 'Matić']             |
| 24027 | Jaz sem od vlade Mira Cerarja   pričakoval , da bo ta zakon ena izmed njihovih prioritetnih nalog .                                                                                  | I expected this law to be one of their   priorities .                                                                                                                            | {0: 0, 6: 1, 8: 4, 9: 5, 10: 2, 11: 3,   12: 6, 13: 7, 14: 8, 15: 9, 16: 9, 17: 10}                                                                                                                                     | Issue: index 5: ['Cerarja', 'Cerar']           |
| 24912 | Naj povem , da sem to poslansko   vprašanje že v prejšnjem mandatu postavil dvakrat ministru gospodu Židanu ,   ker tega denarja še nismo dobili izplačanega .                       | Let me say that I have already asked   this question in the previous term of office twice to the Minister , because   this money has not yet been paid off .                     | {0: 0, 1: 2, 3: 3, 4: 4, 5: 8, 6: 9,   7: 7, 8: 6, 9: 10, 10: 12, 11: 13, 13: 16, 14: 19, 17: 20, 18: 21, 19: 22,   20: 23, 21: 24, 22: 25, 23: 27, 24: 28, 25: 30}                                                     | Issue: index 16: ['Židanu', 'Židan']           |
| 44899 | Spoštovani minister Počivalšek , malo   me pravzaprav boli ta vaš odgovor , ki ga berete kot da bi brala o mojih   podplatih čevlja , ki jih nisem pravočasno popravila .            | Dear Minister , I don't really care   about your answer , which you read as if you were reading about my shoe soles   , which I didn't fix in time .                             | {0: 0, 1: 1, 3: 2, 4: 4, 6: 5, 7: 6,   9: 8, 10: 9, 11: 10, 12: 11, 13: 12, 14: 13, 15: 14, 16: 15, 17: 17, 18: 18,   19: 19, 20: 20, 21: 21, 22: 22, 23: 23, 24: 24, 25: 25, 26: 26, 27: 29, 28:   27, 29: 30}         | Issue: index 2: ['Počivalšek',   'Počivalšek'] |
| 60819 | Samo pri tej vladi Mira Cerarja   doživimo pač to , da je nedotakljivo vse , da je to idealno narejeno .                                                                             | Only in this government do we Miro the   fact that it is untouchable that this is ideally done .                                                                                 | {0: 0, 1: 1, 2: 2, 3: 3, 4: 6, 6: 8,   8: 9, 11: 11, 12: 12, 15: 13, 17: 14, 18: 16, 19: 17, 20: 18}                                                                                                                    | Issue: index 5: ['Cerarja', 'Cerar']           |

Examples of wrong NER:

|        | text                                                                                                                                                                                                                                                                                               | new_translations                                                                                                                                                                                                                                                                                                                                        | alignments                                                                                                                                                                                                                                                                                                                         | errors                                           |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
|  47299 | In jaz vprašam župana : » Ali ni   minister zagotovil , da se bo to sofinanciralo ? « Je rekel : » Ja ,   zagotovil je , ampak denarja ni , niti odločbe ni . «                                                                                                                                    | And I ask the mayor : " Isn't the   Minister sure that this will be co-financed ? « He said : “ Yes , he provided   , but there is no money , and there is no decision . ”                                                                                                                                                                              | {0: 0, 1: 1, 2: 2, 3: 4, 4: 5, 5: 6,   7: 7, 8: 9, 9: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15, 16: 16, 17: 17,   18: 18, 19: 19, 20: 20, 21: 21, 22: 22, 23: 23, 24: 25, 26: 26, 27: 27, 28:   31, 29: 34, 31: 36, 32: 37, 34: 38, 35: 39}                                                                                      | Issue: index 6: ['Ali', 'ali']                   |
|  49376 | Gospod Jernej Vrtovec , imate zahtevo   za postopkovni predlog Izvolite .                                                                                                                                                                                                                          | Mr Jernej Vrtovec , you have a request   for a procedural proposal .                                                                                                                                                                                                                                                                                    | {0: 0, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7,   6: 8, 7: 10, 8: 11, 10: 12}                                                                                                                                                                                                                                                                 | Issue: index 9: ['Izvolite',   'izvoliti']       |
|  62430 | Predsedujoči , dajte , prosim , kolega   Trčka Sicer je fino , da je tukaj pa govori , sicer je veliko tveganje , da   bi granitne kocke metal .                                                                                                                                                   | Chairman , give , please , a colleague   of Trtka Trček is fine that he is here talking , otherwise it is a great risk   to make granite cubes metal .                                                                                                                                                                                                  | {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5,   6: 7, 7: 10, 9: 11, 10: 12, 12: 13, 13: 15, 14: 16, 16: 17, 17: 18, 18: 19,   19: 21, 20: 23, 21: 24, 23: 25, 24: 26, 25: 27, 26: 28, 27: 29, 28: 30}                                                                                                                                       | Issue: index 8: ['Sicer', 'sicer']               |
| 108351 | Ne morem mimo tega , da opozorim na to   , kar je Vlada zapisala v svojem mnenju Pravi , « Vlada ne nasprotuje namenu   predlagateljev in predlaganim rešitvam , ocenjuje pa , da bi bilo treba   hkrati , ko se sprejemajo predlagane rešitve , ustrezno prilagoditi tudi   sistemske rešitve « . | I cannot go past the fact that I   should draw attention to what the Government has written in its opinion   " The Government does not oppose the purpose of the proposings and the   proposed solutions , but it is estimated that , at the same time as the proposed   solutions are adopted , systemic solutions should be adapted accordingly .   " | {0: 0, 1: 1, 2: 3, 3: 5, 5: 6, 6: 9,   7: 10, 8: 11, 10: 12, 11: 13, 12: 14, 13: 16, 14: 17, 15: 18, 16: 19, 19: 20,   20: 22, 21: 24, 22: 25, 23: 27, 24: 30, 25: 31, 26: 33, 27: 34, 28: 35, 29:   39, 32: 40, 35: 41, 36: 44, 38: 45, 39: 50, 40: 51, 41: 48, 42: 49, 43: 52,   44: 58, 45: 57, 47: 53, 48: 54, 49: 60, 50: 59} | Issue: index 17: ['Pravi', 'praviti']            |
| 108948 | Lahko bi , če bi se malo potrudili ,   pa našli argumente za to trditev oziroma argumente proti našemu predlogu …   Razmišljal sem samo , kaj boste rekli in s kakšnimi argumenti boste proti ,   pa bi našel boljše argumente proti svojemu zakonu , pa ste jih vi.                               | I could have been thinking about what   you're going to say and with what arguments you're going against , and I   would have found better arguments against your law , and you would have made   them .                                                                                                                                                | {0: 1, 1: 1, 7: 8, 9: 22, 10: 23, 11:   25, 16: 25, 17: 26, 18: 26, 21: 4, 24: 5, 25: 6, 26: 7, 27: 10, 28: 11, 29:   12, 30: 13, 31: 14, 32: 16, 33: 17, 34: 18, 35: 19, 36: 21, 37: 23, 38: 24,   39: 25, 40: 26, 41: 27, 42: 28, 43: 29, 44: 30, 45: 31, 46: 35, 47: 36}                                                        | Issue: index 20: ['Razmišljal',   'razmišljati'] |
| 111267 | Že vnaprej obsojati preiskovalno   komisijo , da bo delovala nezakonito … Nisem nič rekla kdo , slišali smo v   razpravi .                                                                                                                                                                         | I have not said anything about who ,   we heard in the debate .                                                                                                                                                                                                                                                                                         | {2: 0, 9: 1, 11: 2, 12: 4, 13: 3, 14:   6, 15: 7, 16: 9, 17: 8, 18: 10, 19: 12, 20: 13}                                                                                                                                                                                                                                            | Issue: index 10: ['Nisem', 'biti']               |

Examples of null alignment:

|       | text                                                                                                                                                                                                                                                                         | new_translations                                                                                                                                                                                                                                                                         | alignments                                                                                                                                                                                                                                                                                                         | errors                                    |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
|  2345 | Nikogar ne boste zadržali v Sloveniji   , podjetja zaradi tega ne bodo nič boljše poslovala … Celo tako , kot je   Šircelj prej rekel , tam , kjer nimajo kolektivnih pogodb , boste mogoče celo   omogočil delodajalcem , da ohranijo isti neto ob nekoliko manjšem brutu . | You will not keep anyone in Slovenia ,   businesses will do nothing better . . . Even as Shircelj said before , where   they do not have collective contracts , you may even allow employers to keep   the same net with a slightly smaller gross .                                      | {0: 4, 1: 2, 2: 1, 3: 3, 4: 5, 5: 6,   6: 7, 7: 8, 11: 9, 12: 11, 13: 12, 14: 13, 15: 15, 16: 16, 19: 17, 21: 18,   22: 20, 23: 19, 24: 21, 27: 22, 28: 25, 29: 27, 30: 28, 31: 29, 32: 30, 33:   31, 34: 32, 35: 33, 36: 34, 38: 35, 39: 36, 40: 38, 41: 39, 42: 40, 43: 42,   44: 43, 45: 44, 46: 45}            | Issue: index 20: ['Šircelj',   'Šircelj'] |
| 64747 | Želi besedo gospa Vlada Nussdorfer ?                                                                                                                                                                                                                                         | Does Mrs . Vlad Nussdorfer want the   word ?                                                                                                                                                                                                                                             | {0: 5, 1: 7, 2: 1, 4: 4, 5: 8}                                                                                                                                                                                                                                                                                     | Issue: index 3: ['Vlada', 'vlada']        |
| 73749 | Besedo ima gospod Jurij Lep .                                                                                                                                                                                                                                                | Mr . Jurij Leprechaun has the word .                                                                                                                                                                                                                                                     | {0: 6, 1: 4, 2: 0, 3: 2, 5: 7}                                                                                                                                                                                                                                                                                     | Issue: index 4: ['Lep', 'lep']            |
| 82229 | Na predstavitvi svoje kandidature je   dr. Rok Čeferin sicer povedal , da je posamezne medije , ki niso pod okriljem   Vlade , res označil za tovarne laži , a da je to storil pod vplivom jeze in   uporabil izraz , ki ga morda ne bi smel .                               | In the presentation of his candidacy ,   Dr . Roc Čeferin said that he had indeed designated individual media not   under the auspices of the Government as factory lies , but that he had done   so under the influence of anger and used an expression that he might not have   used . | {0: 0, 1: 2, 2: 4, 3: 5, 4: 6, 5: 7,   7: 10, 9: 11, 11: 12, 12: 13, 13: 17, 14: 18, 17: 19, 18: 20, 19: 22, 20: 25,   22: 15, 23: 16, 24: 26, 25: 27, 26: 28, 27: 29, 28: 30, 29: 31, 30: 32, 32:   34, 33: 36, 34: 38, 35: 40, 36: 41, 37: 42, 38: 44, 40: 45, 41: 46, 42: 47,   43: 48, 44: 49, 45: 50, 46: 51} | Issue: index 6: ['Rok', 'Rok']            |

### Errors in SpaceAfter when producing final conllu files

Inspection revealed that the reason for this are errors in the tokenization, produced by Stanza's tokenizer: in a very rare number of sentences (e.g, 7 sentences out of 3.9M), especially if the sentence is long, Stanza's tokenizer makes an error in word tokenization and outputs as one token two words that are separated by spaces.

Example - problematic tokens in ParlaMint-SI:
```
('also solidarity', 'also')
184
('a public', 'a')
449
('Court of', 'Court')
223
('internal transport', 'internal')
151
('who are', 'who')
230
('European Union', 'European')
379
('Court of', 'Court')
225
```

And the output of the tokenizer that is the reason behind it:
```
185	also solidarity	_	_	_	_	184	_	_	start_char=996|end_char=1011
```

Based on tokenization, we produce a list of tokens and a list of SpaceAfter information of the same length. Then we produce the string of tokenized text by joining tokens in the list of tokens by space (["I", "am", ",", "Taja", "."] -> "I am , Taja ."; list of SpaceAfter information: ["Yes", "No", "Yes", "No", "Last"] -> resulting final string based on this information: "I am, Taja.").

The problem occurs because for alignment, we need tokenized text in a string, not a list of words. That is why we merged the list of tokens into a string in a previous step. And then to get a list of words out of it again for assigning alignment information, proper name substitution, SpaceAfter information to each token, we split the tokenized string into a list again by " " (space). As in the first tokenized list, there occurred tokens which had space inside, the number of tokens in the initial tokenized list and corresponding space_after list is different than the number of tokens when the final list was created by joining the initial list and splitting it again by space.

To sum up, the error occurs due to error in the tokenizer which encoded two words, separated by a space, as one token. However, as this error is very very rare, we left it at it is.

Possible solutions: using spacy tokenizer instead of stanza tokenizer; encoding the initial list of tokens and comparing the lengths for each sentence, and if the lists are not the same, adding an element into the SpaceAfter list so that each element is connected with correct word.

### Report on the translation of notes

The report on the process of translation of notes, based on ParlaMint-SI:

- Main finding: errors in proper name translation are very common. Tag "note speaker" represents 71% of notes (before the duplication) and most are incorrect.  Examples: "Romana Tomc" -> "Tomc of Romania", "Ljudmila Novak" -> "Human Novak", "Zmago Jelinčič Plemeniti" -> "Flamming Flammers", "Zmago Jelinčič Plemeniti" -> "The Winner of the Welcomes", "Nevenka Ribič" -> "Newenka Fish"

- Errors per tag and tag type (in the parentheses, I added number of occurrences in corpus before duplication so that we have a feeling of the general occurrence of this note in the source corpus) :

	- mostly incorrect tags: note speaker (311,372, bad proper name translation), vocal interruption (2608, bad translations), head chairman (1567; wrong proper names),  note error (234, bad proper names),  incident action (19, bad translations), kinesic slapping (12, bad translations: "tlesk s prsti" -> "finger-toed clap"), gap editorial (7; "nagovor v italijanščini" -> "address in Italian)

	- others are mostly correct (note (without additional type: 63680), gap inaudible (38647), note vote-ayes (5771), note vote-noes (5737), note time (5127), head (without additional type: 1570), head session (1569) , vote answer (802), kinesic signal (672), kinesic gesture (122),  vocal laughter (117),  kinesic applause (95),  incident sound (21), note description (9), note vote (2), kinesic playback (2))

Other findings (less common errors):

- Some translations are bad (maybe also due to the lack of context): "oglašanje iz klopi" -> "bench advertising", "advertising from the hall; "razkuževanje" -> "infection"; "razkuževanje govornice" -> "disinfection of the phone"; "aplavz" -> "let's hear it"; "plosk" -> "flat"

- Some of source notes are bad (spelling mistakes) which results in wrong translations: "izkop mikrofona" -> "microphone dig"; "izlop mikrofona" -> "microphone extrusion"; "znak zakonec razprave" -> "sign of the spouse of the debate" (also "nak za konec razprave", "zank za konec razprave")

Other errors in notes that were identified:

- common MT hallucinations when translating numbers, see the following example for ParlaMint-DK:

```
0	note	agendaItem	2017-11-22-0		1	This Regulation shall be binding in its entirety and directly applicable in all Member States.
1	note	agendaItem	2017-11-22-1		1	This Regulation shall be binding in its entirety and directly applicable in all Member States.
2	note	agendaItem	2017-11-22-2		1	This Regulation shall be binding in its entirety and directly applicable in all Member States.
```

## Information on processing each corpus

### ParlaMint-CZ

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

There is no < head > tag in the corpus.

### ParlaMint-BG

Most frequent substitutions:

|                                  |   substituted_pairs |
|:---------------------------------|--------------------:|
| [('Chairman', 'председател')]    |     14506           |
| [('President', 'председател')]   |     10281           |
| [('Ivanov', 'иванов')]           |      4720           |
| [('Kirilov', 'кирилов')]         |      3733           |
| [('Popov', 'попов')]             |      2584           |
| [('Gokov', 'гьоков')]            |      2047           |
| [('Ermenkov', 'ерменков')]       |      1934           |
| [('Dimitrov', 'димитров')]       |      1898           |
| [('Borisov', 'борисов')]         |      1822           |
| [('Deputy', 'вицепремиер')]      |      1794           |
| [('Stoyanova', 'стоянова')]      |      1784           |
| [('Svilensky', 'свиленски')]     |      1758           |
| [('Ademov', 'адемов')]           |      1714           |
| [('Ninova', 'нинова')]           |      1669           |
| [('Zarkov', 'зарков')]           |      1570           |
| [('Ananiev', 'ананиев')]         |      1559           |
| [('Tsonev', 'цонев')]            |      1545           |
| [('Slavov', 'славов')]           |      1495           |
| [('Bayraktarov', 'байрактаров')] |      1482           |

As we can see, post-processing in Bulgarian would introduce many errors, because the lemmas which would be inserted into original translations are in cyrillic and the substitution with the original lemma looks like this: "Importer : иван станков ". That is why, we won't use the post-processed translations in BG corpus. Consequently, there is no "Translated" value in the final CONLL-u files.

The processing into the final conll-u files revealed errors (similar to errors in ParlaMint-DK) in translation and spaces between words in following 38 sentences:
- /home/tajak/Parlamint-translation/Final-data/ParlaMint-BG.conllu/ParlaMint-BG.conllu/2017/ParlaMint-BG_2017-07-26.conllu: ParlaMint-BG_2017-07-26.seg1009.1
- /home/tajak/Parlamint-translation/Final-data/ParlaMint-BG.conllu/ParlaMint-BG.conllu/2017/
- ... (for all sentences, see logs/BG/create_conllu.md)

Corpus has no note tags < note >, < head > and < gap >.

### ParlaMint-DK

Most frequent substitutions:

|                                                          |   substituted_pairs |
|:---------------------------------------------------------|--------------------:|
| [('Messerschmidt', 'Messerschmide')]                     |       963           |
| [('Hylllested', 'Hyllested')]                            |       943           |
| [('Løjberg', 'Støjberg')]                                |       926           |
| [('Ellemann', 'Ellemann-Jensen')]                        |       803           |
| [('Rohde', 'Roh')]                                       |       798           |
| [('Mathisen', 'Mathiesen')]                              |       797           |
| [('Naser', 'Nase')]                                      |       759           |
| [('Jeppe', 'Jep')]                                       |       579           |
| [('Blixt', 'Blix')]                                      |       404           |
| [('Nielsen', 'Schmidt-Nielsen')]                         |       400           |
| [('Krarup', 'Marie'), ('Marie', 'Krarup')]               |       398           |
| [('Britt', 'May-Britt')]                                 |       381           |
| [('Baker', 'Bager')]                                     |       378           |
| [('Silverhøj', 'Sølvhøj')]                               |       332           |
| [('Schmidt', 'Johanne'), ('Nielsen', 'Schmidt-Nielsen')] |       290           |
| [('Bille', 'Ammitzbøll-Bille')]                          |       288           |
| [('Rosenkrantz', 'Rosenkrantz-Theil')]                   |       286           |
| [('Sea', 'Hav')]                                         |       285           |
| [('Engel', 'Engel-Schmidt')]                             |       285           |

The processing into CONLL-u files revealed some errors in translations when unwanted repetition occurred - this is the case of the following 15 sentences:
- ParlaMint-DK_2016-05-03-20151-M86.conllu: ParlaMint-DK_20160503174318.seg453.10:
	`That is to say, the rapporteur believes that the people per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per; per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per definition has the right tocitizenship.`
- ParlaMint-DK_2021-06-03-20201-M128.conllu: ParlaMint-DK_20210603165102.seg595.5:
	`And as far as starting the fight against knowledge is concerned, Fonsmark has a point, namely that it is wrong to throw knowledge on the dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dang dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d dd `
- ... (for all sentences, see logs/DK/create_conllu.md)

Notes are only encoded as < note > or < head > (no other notes tags were found).

### ParlaMint-IS

Most frequent substitutions:

|                                                                            |   substituted_pairs |
|:---------------------------------------------------------------------------|--------------------:|
| [('Catherine', 'Katrín'), ('Jacob', 'Jakobsdóttir')]                       |       561           |
| [('Levi', 'Björn'), ('son', 'Leví'), ('Gunnar', 'Gunnarsson')]             |       493           |
| [('John', 'Jón')]                                                          |       389           |
| [('Steingrimur', 'Steingrímur'), ('Sigfusson', 'Sigfússon')]               |       354           |
| [('Thor', 'Þór'), ('Thorsson', 'Þórsson')]                                 |       334           |
| [('Katrin', 'Katrín'), ('Jacob', 'Jakobsdóttir')]                          |       207           |
| [('Harald', 'Haraldur'), ('Benedict', 'Benediktsson')]                     |       207           |
| [('Skarphéðinn', 'Össur'), ('Össur', 'Skarphéðinsson')]                    |       172           |
| [('weekend', 'Helgi')]                                                     |       165           |
| [('J.', 'Steingrímur'), ('Steingrímur', 'J.'), ('Sigfusson', 'Sigfússon')] |       156           |
| [('Niel', 'Brynjar'), ('Brynjar', 'Níelsson')]                             |       154           |
| [('Benedictsson', 'Benediktsson')]                                         |       143           |
| [('Thor', 'Þór')]                                                          |       134           |
| [('Harald', 'Bryndís'), ('daughter', 'Haraldsdóttir')]                     |       131           |
| [('Kristoff', 'Kristján')]                                                 |       127           |
| [('Ola', 'Óli'), ('Birni', 'Björn'), ('Kálsson', 'Kárason')]               |       125           |
| [('Robert', 'Róbert')]                                                     |       124           |
| [('William', 'Vilhjálmur'), ('Arnason', 'Árnason')]                        |       121           |
| [('Skarphéðinn', 'Össur'), ('ossuary', 'Skarphéðinsson')]                  |       120           |

No errors occurred in CONLL-u creation.

There are no < gap > and < head > tags in the corpus.

### ParlaMint-PT

The analysis of the substitutions revealed that Portuguese NER model is much worse (or different) than the models for other languages - words, annotated as Proper Nouns: Ministro, Presidente, Deputado, Equipa, sr., ...

Based on the list of most frequent substitutions, I won't use the substitution process for this language, because we would introduce more errors than solutions.

Most frequent substitutions:

|                                                                       |   substituted_pairs |
|:----------------------------------------------------------------------|--------------------:|
| [('Mr.', 'sr.'), ('President', 'Presidente')]                         |               14470 |
| [('President', 'Presidente')]                                         |               11686 |
| [('Minister', 'Ministro')]                                            |                6162 |
| [('Mr', 'sr.'), ('President', 'Presidente')]                          |                6123 |
| [('Mr', 'sr.')]                                                       |                5147 |
| [('Mr', 'sr.'), ('President', 'Deputado')]                            |                4152 |
| [('Mr.', 'sr.'), ('Prime', 'Primeiro-Ministro')]                      |                4053 |
| [('Mr.', 'sr.'), ('Deputies', 'Deputado')]                            |                3454 |
| [('Mr.', 'sr.'), ('Deputy', 'Deputado')]                              |                2946 |
| [('ladies', 'Sr.as')]                                                 |                2433 |
| [('Minister', 'sr.'), ('Prime', 'Primeiro-Ministro')]                 |                2025 |
| [('Mr.', 'sr.')]                                                      |                1972 |
| [('Mr', 'sr.'), ('Prime', 'Primeiro-Ministro')]                       |                1827 |
| [('Mr.', 'sr.'), ('President', 'Presidente'), ('Members', 'Membros')] |                1550 |
| [('Minister', 'Ministra')]                                            |                1524 |
| [('Secretary', 'Secretário'), ('of', 'de'), ('State', 'Estado')]      |                1510 |
| [('President', 'Presidente'), ('ladies', 'Sr.as')]                    |                1507 |
| [('honourable', 'sr.'), ('Member', 'Deputado')]                       |                1480 |
| [('Mr', 'sr.'), ('Luís', 'deputado'), ('deputado', 'Luís')]           |                1292 |

We found 12 errors in sentences (as in ParlaMint-DK and others) due to MT model hallucinations:
- ParlaMint-PT_2017-02-02.seg250.s: /home/tajak/Parlamint-translation/Final-data/ParlaMint-PT.conllu/ParlaMint-PT.conllu/2017/ParlaMint-PT_2017-02-02.conllu
- ... (see all instances in logs/PT/create_conllu.md)

Corpus has no < gap > and < incident > tags.

### ParlaMint-HR

Most frequent substitutions:

|                                |   substituted_pairs |
|:-------------------------------|--------------------:|
| [('Croats', 'Hrvat')]          |      7243           |
| [('Plenkovic', 'Plenković')]   |      5699           |
| [('Maric', 'Marić')]           |      5656           |
| [('Shuker', 'Šuker')]          |      5440           |
| [('God', 'Bog')]               |      5380           |
| [('Cain', 'Kajin')]            |      5376           |
| [('Stazic', 'Stazić')]         |      4819           |
| [('Grubisic', 'Grubišić')]     |      4669           |
| [('Boric', 'Borić')]           |      4192           |
| [('Linic', 'Linić')]           |      3127           |
| [('Djakic', 'Đakić')]          |      3005           |
| [('Bacic', 'Bačić')]           |      2920           |
| [('Bull', 'Bulj')]             |      2898           |
| [('Milanovic', 'Milanović')]   |      2847           |
| [('Vuksic', 'Vukšić')]         |      2747           |
| [('Kovacevic', 'Kovačević')]   |      2430           |
| [('Hajdukovic', 'Hajduković')] |      2393           |
| [('Zekanovic', 'Zekanović')]   |      2243           |
| [('Zeljko', 'Željko')]         |      2136           |

Since the most frequent substitution would introduce errors, we will disable the substitution.

There were 48 errors in final files due to repetitions in MT:
- ParlaMint-HR_2017-12-13-0.u64797.seg0.71: /home/tajak/Parlamint-translation/Final-data/ParlaMint-HR.conllu/ParlaMint-HR.conllu/2017/ParlaMint-HR_2017-12-13-0.conllu
- ... (see logs/HR/create_conllu.md)

There is no < head > tag in TEI files.

### ParlaMint-IT

Most frequent substitutions:

|                                                                     |   substituted_pairs |
|:--------------------------------------------------------------------|--------------------:|
| [('FI', 'FI-PdL'), ('XVII', 'diciassettesimo')]                     |      1990           |
| [('Mario', 'mario')]                                                |      1064           |
| [('Gentiloni', 'gentiloni')]                                        |       895           |
| [('Matteo', 'matteo')]                                              |       860           |
| [('Calderoli', 'CALDEROLI')]                                        |       827           |
| [('MALAN', 'malan'), ('FI', 'FI-PdL'), ('XVII', 'diciassettesimo')] |       730           |
| [('Montevecchi', 'Montevecche')]                                    |       722           |
| [('Count', 'Conte')]                                                |       705           |
| [('Barani', 'BARANI')]                                              |       659           |
| [("D'Alì", "D'"), ("D'", 'Alì')]                                    |       610           |
| [('Please', 'pregare')]                                             |       592           |
| [('Mixed', 'Misto')]                                                |       578           |
| [('Centinario', 'Centinaio')]                                       |       575           |
| [('God', 'Dio')]                                                    |       555           |
| [('La', 'il')]                                                      |       544           |
| [('Arrigoni', 'ARRIGONI')]                                          |       461           |
| [('Cirinna', 'Cirinnà')]                                            |       443           |
| [("D'Anna", "D'"), ("D'", 'Anna')]                                  |       436           |
| [('Crimes', 'Crimi')]                                               |       432           |

As in Portuguese, alignment would introduce more errors than corrections due to bad Italian NER, so we will disable it.

The creation of CONLL-u files revealed errors in 11 sentences (due to repetitions in translations):
- ParlaMint-IT_2017-03-16-LEG17-Senato-sed-787.ana.seg18.49: /home/tajak/Parlamint-translation/Final-data/ParlaMint-IT.conllu/ParlaMint-IT.conllu/2017/ParlaMint-IT_2017-03-16-LEG17-Senato-sed-787.conllu
- ... (see all in logs/IT/create_conllu.md)

There are no < gap > notes.

### ParlaMint-AT

|                                                       |   substituted_pairs |
|:------------------------------------------------------|--------------------:|
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

As in Portuguese and Italian, alignment would introduce more errors than corrections due to bad Austrian NER, so we will disable it.

There were 19 errors in sentences:
- ParlaMint-AT_2013-01-30-024-XXIV-NRSITZ-00187_d2e2125.s3: /home/tajak/Parlamint-translation/Final-data/ParlaMint-AT.conllu/ParlaMint-AT.conllu/2013/ParlaMint-AT_2013-01-30-024-XXIV-NRSITZ-00187.conllu
- ... (see logs/AT/create_conllu.md for all errors)

There were no < incident > and < head > tags in corpus.

### ParlaMint-SE

Most frequent substitutions:

|                                                    |   substituted_pairs |
|:---------------------------------------------------|--------------------:|
| [('Mrs', 'Maria')]                                 |        587          |
| [('OSCE', 'OSSE')]                                 |        580          |
| [('Mr', 'Thomas')]                                 |        440          |
| [('Mr', 'Johan')]                                  |        433          |
| [('Mr', 'Lars')]                                   |        353          |
| [('Mr', 'Jonas')]                                  |        297          |
| [('Sven', 'Sven-Erik')]                            |        293          |
| [('Wallström', 'Margot'), ('Margot', 'Wallström')] |        272          |
| [('Mr', 'Roger')]                                  |        268          |
| [('Löfven', 'Lövven')]                             |        262          |
| [('Mr', 'Jens')]                                   |        254          |
| [('ERTMS', 'Ertms')]                               |        247          |
| [('Mr', 'Mikael')]                                 |        246          |
| [('Mr', 'Daniel')]                                 |        221          |
| [('Oskar', 'Carl-Oskar')]                          |        209          |
| [('Mr', 'Edward')]                                 |        205          |
| [('Mr', 'Fredrik')]                                |        194          |
| [('Arne', 'Kjell-Arne')]                           |        189          |
| [('Mr', 'Joar')]                                   |        182          |

Interestingly, the Swedish MT model seems to be very prone to changing people's first name into Mr or Mrs. Based on an analysis of some instances of substitution, the changes are correct, so we will use the substitution.

There were no errors with SpaceAfter due to MT repetitions in this corpus :) 

There are no < gap >, < vocal > or < incident > notes.

### ParlaMint-NL

Most frequent substitutions:

|                                                |   substituted_pairs |
|:-----------------------------------------------|--------------------:|
| [('Van', 'van'), ('Dijk', 'dijk')]             |      4531           |
| [('Van', 'van')]                               |      4324           |
| [('Van', 'van'), ('Staaij', 'staaij')]         |      3804           |
| [('Van', 'van'), ('Weyenberg', 'weyenberg')]   |      3775           |
| [('Bishop', 'bisschop')]                       |      3751           |
| [('Van', 'van'), ('Meenen', 'meenen')]         |      3063           |
| [('Van', 'van'), ('Rooijen', 'rooijen')]       |      3048           |
| [('Van', 'van'), ('Nispen', 'nispen')]         |      3029           |
| [('Klaver', 'klaver')]                         |      2939           |
| [('Van', 'van'), ('Raak', 'raak')]             |      2896           |
| [('Dik', 'Dik-Faber')]                         |      2688           |
| [('Van', 'van'), ('Toorenburg', 'toorenburg')] |      2661           |
| [('De', 'de'), ('Vries', 'vries')]             |      2621           |
| [('Van', 'van'), ('Lee', 'lee')]               |      2361           |
| [('Van', 'van'), ('Tongeren', 'tongeren')]     |      2320           |
| [('Van', 'van'), ('Raan', 'raan')]             |      2045           |
| [('Van', 'van'), ('Haga', 'haga')]             |      1970           |
| [('De', 'de'), ('Graaf', 'graaf')]             |      1846           |
| [('Van', 'van'), ('Ojik', 'ojik')]             |      1838           |

As we can see, we cannot use the Dutch lemmas, because they don't capitalize the proper names in the lemmas. So we won't use the substitution in post-processing.

3 errors occured due to repetitions in MT:
- ParlaMint-NL_2016-10-27-tweedekamer-9.s771: /home/tajak/Parlamint-translation/Final-data/ParlaMint-NL.conllu/ParlaMint-NL.conllu/2016/ParlaMint-NL_2016-10-27-tweedekamer-9.conllu
- ParlaMint-NL_2014-04-16-tweedekamer-6.s777: /home/tajak/Parlamint-translation/Final-data/ParlaMint-NL.conllu/ParlaMint-NL.conllu/2014/ParlaMint-NL_2014-04-16-tweedekamer-6.conllu
- ParlaMint-NL_2020-10-08-tweedekamer-4.s2131: /home/tajak/Parlamint-translation/Final-data/ParlaMint-NL.conllu/ParlaMint-NL.conllu/2020/ParlaMint-NL_2020-10-08-tweedekamer-4.conllu

Translation of notes revealed that there are no < gap >, < vocal >, < kinesic > or < incident > notes in ParlaMint-NL (also verified by searching through the files with grep).

### ParlaMint-NO

Most frequent substitutions:

|                                   |   substituted_pairs |
|:----------------------------------|--------------------:|
| [('King', 'Kongen')]              |      2564           |
| [('Höie', 'Høie')]                |      2059           |
| [('Lundtigen', 'Lundteigen')]     |      2021           |
| [('Solvik', 'Solvik-Olsen')]      |      1557           |
| [('.', 'I.')]                     |      1516           |
| [('Greece', 'Helleland')]         |       815           |
| [('Tybring', 'Tybring-Gjedde')]   |       795           |
| [('Schjøtt', 'Schjøtt-Pedersen')] |       710           |
| [('Haltbrecken', 'Haltbrekken')]  |       665           |
| [('Hemdal', 'Hjemdal')]           |       663           |
| [('Nävra', 'Nævra')]              |       610           |
| [('Soreide', 'Søreide')]          |       592           |
| [('Davøy', 'Dåvøy')]              |       578           |
| [('Elvesuen', 'Elvestuen')]       |       574           |
| [('Rikvam', 'Reikvam')]           |       559           |
| [('Fleet', 'Flåtten')]            |       528           |
| [('Schlagsvold', 'Slagsvold')]    |       510           |
| [('Bears', 'Bjørnar')]            |       498           |
| [('Battle', 'Slagsvold')]         |       481           |

Since the most frequent substitution (King) is wrong, we won't use the substitutions.

There were 19 errors based on repetition in MT:
- ParlaMint-NO_2013-06-21.ana.segd581e13177.4: /home/tajak/Parlamint-translation/Final-data/ParlaMint-NO.conllu/ParlaMint-NO.conllu/2013/ParlaMint-NO_2013-06-21.conllu
- ... (see logs/NO/create_conllu.md)

Notes are only in < note > and < head > tags.

When translating notes, there were two notes, marked with lang code "en", but that are in Norwegian. So, I did not delete them, I just changed the lang code.

### ParlaMint-GR

Most frequent substitutions:

|                                                          |   substituted_pairs |
|:---------------------------------------------------------|--------------------:|
| [('Tsipras', 'Τσίπρας')]                                 |      8875           |
| [('Mitsotakis', 'Μητσοτάκης')]                           |      7936           |
| [('Kegeroglu', 'Κεγκέρογλου')]                           |      3253           |
| [('Georgiadis', 'Γεωργιάδης')]                           |      2703           |
| [('Kyriakos', 'Κυριάκος'), ('Mitsotakis', 'Μητσοτάκης')] |      2188           |
| [('Hatzidakis', 'Χατζηδάκης')]                           |      2091           |
| [('Loverdo', 'Λοβέρδος')]                                |      1803           |
| [('Loverdos', 'Λοβέρδος')]                               |      1791           |
| [('Kammenos', 'Καμμένος')]                               |      1663           |
| [('Voridis', 'Βορίδης')]                                 |      1467           |
| [('Brutsi', 'Βρούτσης')]                                 |      1349           |
| [('Polakis', 'Πολάκης')]                                 |      1337           |
| [('Varoufakis', 'Βαρουφάκης')]                           |      1307           |
| [('Alexis', 'Αλέξης'), ('Tsipras', 'Τσίπρας')]           |      1092           |
| [('Samaras', 'Σαμαράς')]                                 |      1048           |
| [('Erdogan', 'Ερντογάν')]                                |      1048           |
| [('Amyras', 'Αμυράς')]                                   |      1023           |
| [('Stathakis', 'Σταθάκης')]                              |       975           |
| [('Venizelos', 'Βενιζέλος')]                             |       964           |

Like with Bulgarian, we will disable substitution, because otherwise there would be names in Greek script in the English translation.

There were 8 sentences with errors due to errors in translation:
- ParlaMint-GR_2017-06-19-S1-commons.seg309.1: /home/tajak/Parlamint-translation/Final-data/ParlaMint-GR.conllu/ParlaMint-GR.conllu/2017/ParlaMint-GR_2017-06-19-S1-commons.conllu
- ... (see all instances in logs/GR/create_conllu.md)

### ParlaMint-BA

Most frequent substitutions:

|                                        |   substituted_pairs |
|:---------------------------------------|--------------------:|
| [('Spiric', 'Špirić')]                 |                3241 |
| [('Novakovic', 'Novaković')]           |                2639 |
| [('Zivkovic', 'Živković')]             |                2415 |
| [('Belkic', 'Belkić')]                 |                2154 |
| [('Jaferovic', 'Džaferović')]          |                1966 |
| [('Becirovic', 'Bećirović')]           |                1760 |
| [('Mike', 'Majkić')]                   |                1494 |
| [('Lagumdzija', 'Lagumdžija')]         |                1347 |
| [('Zoric', 'Zorić')]                   |                1068 |
| [('God', 'Bog')]                       |                1063 |
| [('Križanovic', 'Križanović')]         |                1015 |
| [('Hadjiahmetovic', 'Hadžiahmetović')] |                 996 |
| [('Dokic', 'Dokić')]                   |                 964 |
| [('Lozancic', 'Lozančić')]             |                 934 |
| [('Cengic', 'Čengić')]                 |                 927 |
| [('Beqirovic', 'Bećirović')]           |                 871 |
| [('Kalabic', 'Kalabić')]               |                 865 |
| [('Tokic', 'Tokić')]                   |                 831 |
| [('Dzaferovic', 'Džaferović')]         |                 797 |

There were 14 errors reported, connected to Spaceafter information due to errors in machine translation:
- ParlaMint-BA_2013-09-19-0.u16851.seg0.17: home/tajak/Parlamint-translation/Final-data/ParlaMint-BA.conllu/ParlaMint-BA.conllu/2013/ParlaMint-BA_2013-09-19-0.conllu
- ... (see logs/BA/create_conllu.md)

There are no notes in < head > tags in ParlaMint-BA.

### ParlaMint-HU

Most frequent substitutions:

|                                                                |   substituted_pairs |
|:---------------------------------------------------------------|--------------------:|
| [('Parliament', 'Országgyűlés')]                               |     23746           |
| [('Viktor', 'Orbán'), ('Orbán', 'Viktor')]                     |      3894           |
| [('Here', 'parancsol')]                                        |      1543           |
| [('Bence', 'Rétvári'), ('Rétvári', 'Bence')]                   |      1139           |
| [('Congressman', 'Úr')]                                        |      1117           |
| [('Ferenc', 'Gyurcsány'), ('Gyurcsány', 'Ferenc')]             |      1006           |
| [('Erzsébet', 'Schmuck'), ('Schmuck', 'Erzsébet')]             |       987           |
| [('Nándor', 'Gúr'), ('Gúr', 'Nándor')]                         |       969           |
| [('Dániel', 'Z.'), ('Z.', 'Kárpát'), ('Kárpát', 'Dániel')]     |       864           |
| [('gentlemen', 'Képviselőtárs')]                               |       844           |
| [('Members', 'Képviselőtárs')]                                 |       696           |
| [('Secretary', 'Államtitkár')]                                 |       643           |
| [('Christmas', 'Karácsony')]                                   |       638           |
| [('Dr.', 'dr.')]                                               |       621           |
| [('Orbán', 'Viktor')]                                          |       614           |
| [('Dániel', 'Z.'), ('Z.', 'Kárpát'), ('Carpathian', 'Dániel')] |       546           |
| [('minute', 'kétperces')]                                      |       535           |
| [('Márta', 'Demeter'), ('Demeter', 'Márta')]                   |       529           |
| [('Mónika', 'Dunai'), ('Dunai', 'Mónika')]                     |       480           |

Since based on NER annotations, we would substitute "Parliament", "Members", etc., we will disable substitution.

There were 4 errors in sentences:
- ParlaMint-HU_2017-05-22.seg401.1: /home/tajak/Parlamint-translation/Final-data/ParlaMint-HU.conllu/ParlaMint-HU.conllu/2017/ParlaMint-HU_2017-05-22.conllu
- ParlaMint-HU_2021-02-16.seg350.2: /home/tajak/Parlamint-translation/Final-data/ParlaMint-HU.conllu/ParlaMint-HU.conllu/2021/ParlaMint-HU_2021-02-16.conllu
- ParlaMint-HU_2020-06-16.seg57.2: /home/tajak/Parlamint-translation/Final-data/ParlaMint-HU.conllu/ParlaMint-HU.conllu/2020/ParlaMint-HU_2020-06-16.conllu
- ParlaMint-HU_2020-12-01.seg106.2: /home/tajak/Parlamint-translation/Final-data/ParlaMint-HU.conllu/ParlaMint-HU.conllu/2020/ParlaMint-HU_2020-04-07.conllu

There are no notes in < head > and < gap > tags.

### ParlaMint-TR

Most frequent substitutions:

|                                                        |   substituted_pairs |
|:-------------------------------------------------------|--------------------:|
| [('Mr.', 'sayın'), ('President', 'başkan')]            |    123489           |
| [('Mr.', 'sayın')]                                     |     48883           |
| [('Mr.', 'sayın'), ('Secretary', 'bakan')]             |     15603           |
| [('Congressmans', 'sayın'), ('sayın', 'milletvekili')] |      9416           |
| [('General', 'genel'), ('Assembly', 'kurul')]          |      9263           |
| [('God', 'allah')]                                     |      7207           |
| [('Turkey', 'Türkiye')]                                |      5635           |
| [('Mr.', 'sayın'), ('Special', 'özel')]                |      3700           |
| [('Mr.', 'sayın'), ('President', 'cumhurbaşkanı')]     |      3674           |
| [('Minister', 'sayın'), ('sayın', 'bakan')]            |      3534           |
| [('Constitution', 'anayasa')]                          |      3336           |
| [('respects', 'saygı')]                                |      3261           |
| [('Mr.', 'bey')]                                       |      3109           |
| [('Minister', 'sayın'), ('Prime', 'başbakan')]         |      2941           |
| [('I', 'ben')]                                         |      2903           |
| [("'m", 'i')]                                          |      2533           |
| [('Mr.', 'sayın'), ('Prime', 'başbakan')]              |      2095           |
| [('Recep', 'recep'), ('Erdogan', 'Erdoğan')]           |      2090           |
| [('high', 'yüce')]                                     |      2023           |

Since based on NER annotations, we would substitute "President", "Mr.", etc., we will disable substitution.

Turkish has more problems with MT hallucinations than the others.

There were errors based on spaceafter and repetitions in translations in 51 sentences - there is especially a problem with repetition of "on and on and on" in multiple sentences:
- "tbmm-2013-05-29sit03spe0065par0090-000060": /home/tajak/Parlamint-translation/Final-data/ParlaMint-TR.conllu/ParlaMint-TR.conllu/2013/ParlaMint-TR_2013-05-29-tbmm-T24.conllu
- ... (see all instances in logs/TR/create_conllu.md)

Translation of notes: ParlaMint-TR has not notes in < gap > and < head > tags.

### ParlaMint-RS

Most frequent substitutions:

|                                                        |   substituted_pairs |
|:-------------------------------------------------------|--------------------:|
| [('Serbs', 'Srbin')]                                   |      11365          |
| [('Markovic', 'Marković')]                             |       9612          |
| [('Nikolic', 'Nikolić')]                               |       9503          |
| [('Vukic', 'Vučić')]                                   |       6800          |
| [('Jovanovic', 'Jovanović')]                           |       6666          |
| [('Arsic', 'Arsić')]                                   |       6348          |
| [('Krasic', 'Krasić')]                                 |       6239          |
| [('Martinovic', 'Martinović')]                         |       6045          |
| [('Seselj', 'Šešelj')]                                 |       5841          |
| [('Alexander', 'Aleksandar'), ('Vukic', 'Vučić')]      |       5624          |
| [('Tadic', 'Tadić')]                                   |       5597          |
| [('Gilas', 'Đilas')]                                   |       5348          |
| [('Zivkovic', 'Živković')]                             |       4949          |
| [('Dinkic', 'Dinkić')]                                 |       4351          |
| [('Zivkovic', 'Živković'), ('Pavicevic', 'Pavićević')] |       4292          |
| [('Stefanovic', 'Stefanović')]                         |       3997          |
| [('Batic', 'Batić')]                                   |       3877          |
| [('Djurisic', 'Đurišić')]                              |       3865          |
| [('Babic', 'Babić')]                                   |       3733          |

Based on the fact that among most frequent substitutions, we have obvious incorrect substitution for "Serbs", we don't use the substitutions.

There were 35 errors due to repetition in MT:
- ParlaMint-RS_2013-10-01-0.u23369.seg0.6: /home/tajak/Parlamint-translation/Final-data/ParlaMint-RS.conllu/ParlaMint-RS.conllu/2013/ParlaMint-RS_2013-10-01-0.conllu
- ... (see more in logs/RS/create_conllu.md)

### ParlaMint-SI

Most frequent substitutions:

|                              |   substituted_pairs |
|:-----------------------------|--------------------:|
| [('Slovenians', 'Slovenec')] |      5204           |
| [('Weber', 'Veber')]         |      2303           |
| [('Franz', 'Franc')]         |      2273           |
| [('Grimes', 'Grims')]        |      2181           |
| [('Anderlich', 'Anderlič')]  |      2163           |
| [('Sok', 'sok')]             |      2022           |
| [('Barovic', 'Barovič')]     |      1462           |
| [('Joseph', 'Jožef')]        |      1409           |
| [('Matthew', 'Matej')]       |      1299           |
| [('Squeakle', 'Cvikl')]      |      1219           |
| [('Kordish', 'Kordiš')]      |      1204           |
| [('Mir', 'Miro')]            |      1073           |
| [('Petty', 'Drobnič')]       |      1039           |
| [('Saiovic', 'Sajovic')]     |      1031           |
| [('Jankovic', 'Janković')]   |       990           |
| [('Bayuk', 'Bajuk')]         |       977           |
| [('Left', 'Levica')]         |       976           |
| [('Barovich', 'Barovič')]    |       968           |
| [('Horvath', 'Horvat')]      |       906           |

As in Serbian, the most frequent substitution ("Slovenes") would introduce errors, so we won't use the substitution.

There were 7 errors due to repetition in MT:
- ParlaMint-SI_2010-12-02-SDZ5-Izredna-34.ana.seg542.1: /home/tajak/Parlamint-translation/Final-data/ParlaMint-SI.conllu/ParlaMint-SI.conllu/2010/ParlaMint-SI_2010-12-02-SDZ5-Izredna-34.conllu
- ... (more in log/SI/create_conllu.md)

### ParlaMint-LV

Most frequent substitutions:

|                                                        |   substituted_pairs |
|:-------------------------------------------------------|--------------------:|
| [('Julia', 'Jūlija'), ('Stepanenko', 'Stepaņenko')]    |                1392 |
| [('Zarins', 'Zariņš')]                                 |                1274 |
| [('Mr', 'kungs')]                                      |                1009 |
| [('Aldi', 'Aldis'), ('Gobzem', 'Gobzems')]             |                 985 |
| [('Viktor', 'Viktors'), ('Valain', 'Valainis')]        |                 949 |
| [('Mrs', 'kundze')]                                    |                 810 |
| [('John', 'Jānis'), ('Reir', 'Reirs')]                 |                 706 |
| [('Mr.', 'kungs')]                                     |                 591 |
| [('Dzintars', 'dzintars')]                             |                 585 |
| [('Putra', 'putra')]                                   |                 583 |
| [('John', 'Jānis'), ('Bordan', 'Bordāns')]             |                 582 |
| [('Sergey', 'Sergejs'), ('Dolgopolov', 'Dolgopolovs')] |                 557 |
| [('Reira', 'Reirs')]                                   |                 546 |
| [('Valaiņa', 'Valaiņs')]                               |                 512 |
| [('Rihard', 'Rihards'), ('Cole', 'kols')]              |                 482 |
| [('A.', 'a.'), ('Kamiņš', 'kaimiņš')]                  |                 478 |
| [('Igor', 'Igors'), ('Pimenov', 'Pimenovs')]           |                 467 |
| [('Viktoras', 'Viktors'), ('Valaiņš', 'Valaiņs')]      |                 412 |
| [('Stepanenko', 'Stepaņenko')]                         |                 400 |

Since "Mr" and "Mrs" is among the most frequent substitutions, we will disable this process.

There were 5 errors due to repetition in MT:
- "ParlaMint-LV_2022-09-29-PT13-2410-U18-P1.41" in /home/tajak/Parlamint-translation/Final-data/ParlaMint-LV.conllu/ParlaMint-LV.conllu/2022/ParlaMint-LV_2022-09-29-PT13-2410.conllu
- ... (see logs/LV/create_conllu.md)

The corpus has only notes in the tag < note >.

### ParlaMint-UA

Most frequent substitutions:

|                                                           |   substituted_pairs |
|:----------------------------------------------------------|--------------------:|
| [('President', 'президент')]                              |      5889           |
| [('Head', 'голово')]                                      |      4213           |
| [('President', 'президент'), ('Ukraine', 'Україна')]      |      2534           |
| [('Lazko', 'Ляшко')]                                      |      1623           |
| [('Head', 'Голово')]                                      |      1410           |
| [('Prime', 'прем’єрний')]                                 |       991           |
| [('Krulko', 'Крулько')]                                   |       909           |
| [('Vladimir', 'Володимир'), ('Vasilovich', 'Васильович')] |       865           |
| [('Shahov', 'Шахов')]                                     |       828           |
| [('Putin', 'Путін')]                                      |       780           |
| [('Volodymyrovich', 'Володимирович')]                     |       737           |
| [('Vlasenko', 'Власенко')]                                |       725           |
| [('Irina', 'Ірина')]                                      |       706           |
| [('God', 'бог')]                                          |       680           |
| [('Yvchenko', 'Івченко')]                                 |       672           |
| [('Nina', 'Ніна'), ('Petrovna', 'Петрівна')]              |       649           |
| [('Ivanovich', 'Іванович')]                               |       642           |
| [('Odarchenko', 'Одарченко')]                             |       617           |
| [('Nestor', 'Нестор'), ('Ivanovich', 'Іванович')]         |       612           |

We won't use the substitutions.

There was only 1 error due to repetition in MT:
- ParlaMint-UA_2020-11-17-m0.u40.p2.s1: /home/tajak/Parlamint-translation/Final-data/ParlaMint-UA.conllu/ParlaMint-UA.conllu/2020/ParlaMint-UA_2020-11-17-m0-uk.conllu

### ParlaMint-ES-GA

Most frequent substitutions:

|                                              |   substituted_pairs |
|:---------------------------------------------|--------------------:|
| [('Feijóo', 'feijóo')]                       |                5506 |
| [('Sánchez', 'sánchez')]                     |                1427 |
| [('Bará', 'bará')]                           |                1383 |
| [('Mrs.', 'señor'), ('Prado', 'prado')]      |                1275 |
| [('Pontón', 'pontón')]                       |                1260 |
| [('Villares', 'villares')]                   |                1210 |
| [('Mrs.', 'señor'), ('Pontón', 'pontón')]    |                1149 |
| [('Tellado', 'tellar')]                      |                1111 |
| [('Prado', 'prado')]                         |                1036 |
| [('Rueda', 'rueda')]                         |                 961 |
| [('Leicega', 'leiceaga')]                    |                 947 |
| [('Torrado', 'torrar')]                      |                 915 |
| [('Puy', 'puy')]                             |                 840 |
| [('Rajoy', 'rajoy')]                         |                 758 |
| [('Pedro', 'pedro'), ('Sánchez', 'sánchez')] |                 711 |
| [('Losada', 'losada')]                       |                 694 |
| [('Mrs.', 'señor'), ('Presas', 'preso')]     |                 615 |
| [('Mr.', 'señor'), ('Sánchez', 'sánchez')]   |                 611 |
| [('Solla', 'solla')]                         |                 608 |

As we can see, performing substitutions would not be good, because Mrs. and similar words are annotated as PER, and the lemmas are not capitalized. We disabled this option.

There are 207 errors connected with repetition in MT:
- ParlaMint-ES-GA_2017-02-21-DSPG017.seg351.s2: /home/tajak/Parlamint-translation/Final-data/ParlaMint-ES-GA.conllu/ParlaMint-ES-GA.conllu/2017/ParlaMint-ES-GA_2017-02-21-DSPG017.conllu
- ... (see logs/ES-GA/create_conllu.md)

Example:
`
Are, you, going, to, meet, the, Committee, of, Workers, and, Ferroatlantic, Workers, or, not, ?, Ssh, shsh, shsh, shsh, shsh, shsh, shsh, shsh, shsh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh, sh,
`

### ParlaMint-ES-CT

Most frequent substitutions:

|                                                          |   substituted_pairs |
|:---------------------------------------------------------|--------------------:|
| [('Thank', 'gràcies')]                                   |               20426 |
| [('Torra', 'torra')]                                     |                1815 |
| [('Thank', 'gracias')]                                   |                1271 |
| [('Counselor', 'conseller')]                             |                1063 |
| [('Puigdemont', 'puigdemont')]                           |                 936 |
| [('Spain', 'españa')]                                    |                 881 |
| [('President', 'president')]                             |                 866 |
| [('Aragonès', 'aragonès')]                               |                 768 |
| [('Junqueras', 'junqueras')]                             |                 474 |
| [('Carrizosa', 'carrizosa')]                             |                 470 |
| [('Counselor', 'consellera')]                            |                 460 |
| [('Quiet', 'silenci')]                                   |                 434 |
| [('Citizens', 'ciudadanos')]                             |                 423 |
| [('Iceta', 'iceta')]                                     |                 408 |
| [('MPs', 'diputats')]                                    |                 376 |
| [('Pot', 'pot')]                                         |                 373 |
| [('Arrimadas', 'arrimadas')]                             |                 342 |
| [('Alejandro', 'alejandro'), ('Fernández', 'fernández')] |                 336 |
| [('Pedro', 'pedro'), ('Sánchez', 'sánchez')]             |                 326 |

We can see that "Thank", "President", "Spain" and so on would be substituted, so we won't use the substitution.

There are 5 errors due to repetition in MT:
- ParlaMint-ES-CT_2017-10-27-4402.46.0.0.1: /home/tajak/Parlamint-translation/Final-data/ParlaMint-ES-CT.conllu/ParlaMint-ES-CT.conllu/2017/ParlaMint-ES-CT_2017-10-27-4402-ca.conllu
- ... (see logs/ES-CT/create_conllu.md)

### ParlaMint-PL

Most frequent substitutions:

|                                      |   substituted_pairs |
|:-------------------------------------|--------------------:|
| [('God', 'bóg')]                     |      2001           |
| [('Czerwinski', 'Czerwiński')]       |      1510           |
| [('Augustine', 'Augustyn')]          |      1132           |
| [('Kaminski', 'Kamiński')]           |       952           |
| [('Ziobra', 'Ziobro')]               |       808           |
| [('Płępek', 'Pępek')]                |       706           |
| [('Richard', 'Ryszard')]             |       684           |
| [('Kukiz.15', 'Kukiz')]              |       670           |
| [('John', 'Jan'), ('Paul', 'Paweł')] |       612           |
| [('Boris', 'Borys')]                 |       608           |
| [('Mark', 'Marek')]                  |       565           |
| [('Left', 'lewica')]                 |       486           |
| [('Blackbay', 'Czarnobaj')]          |       452           |
| [('Poles', 'Polek')]                 |       449           |
| [('Zwierzan', 'Zwiercan')]           |       438           |
| [('Wind', 'Wiatr')]                  |       414           |
| [('Jack', 'Jacek')]                  |       390           |
| [('Michael', 'Michał')]              |       382           |
| [('Owa', 'Sowa')]                    |       382           |

Ones of the most frequent substitutions are connected with the fact that "God", "Poles" and so on are annotated as a PER, so we won't use substitution.

There are 8 errors due to repetition in MT:
- seg802630.10: /home/tajak/Parlamint-translation/Final-data/ParlaMint-PL.conllu/ParlaMint-PL.conllu/2020/ParlaMint-PL_2020-12-16-sejm-23-2.conllu
- ... (see logs/PL/create_conllu.md)


### ParlaMint-FR

Most frequent substitutions:

|                                                      |   substituted_pairs |
|:-----------------------------------------------------|--------------------:|
| [('Mr', 'Monsieur')]                                 |     71665           |
| [('Mrs', 'Monsieur')]                                |     46860           |
| [('Prime', 'premier'), ('Minister', 'ministre')]     |      8962           |
| [('rapporteur', 'Monsieur')]                         |      8707           |
| [('floor', 'Monsieur')]                              |      8090           |
| [('Mr.', 'Monsieur')]                                |      7073           |
| [('Minister', 'Monsieur')]                           |      6769           |
| [('Madam', 'Monsieur')]                              |      4096           |
| [('Minister', 'Monsieur'), ('Monsieur', 'ministre')] |      3777           |
| [('Mr', 'Monsieur'), ('Eric', 'Éric')]               |      2906           |
| [('speaker', 'Monsieur')]                            |      2068           |
| [('Mrs.', 'Monsieur')]                               |      1943           |
| [('Jean', 'Monsieur'), ('Paul', 'Jean-Paul')]        |      1799           |
| [('Mr', 'Monsieur'), ('Sebastien', 'Sébastien')]     |      1766           |
| [('Secretary', 'Monsieur')]                          |      1681           |
| [('Ms.', 'Monsieur')]                                |      1412           |
| [('Jean', 'Monsieur'), ('Louis', 'Jean-Louis')]      |      1412           |
| [('Le', 'le')]                                       |      1318           |
| [('minister', 'Monsieur')]                           |      1295           |

We can see that NER is bad, so we will disable the substitution of proper names.

There were no errors due to MT repetition recorded when creating final dfs.

### ParlaMint-BE

The corpus consists of two non-related languages: French and Dutch. So, I separated the dataframe, created from all conllu files, based on the language (indicated as the suffix of conllu files) and from then onwards processed each language as a separate corpus: BE-nl and BE-fr.

Most frequent substitutions in BE-nl:

|                                                    |   substituted_pairs |
|:---------------------------------------------------|--------------------:|
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

We will disable substitution based on this information (lemmas in lowercase).

In BE-nl, there were 3 errors in production of final files due to repetition in MT:
- ParlaMint-BE_2021-03-18-definitief-55-plenair-ip093x.s835: /home/tajak/Parlamint-translation/Final-data/ParlaMint-BE.conllu/ParlaMint-BE.conllu/2021/ParlaMint-BE_2021-03-18-definitief-55-plenair-ip093x-nl.conllu
- ... (see logs/BE-nl/create-conllu.md)

Most frequent substitutions in BE-fr:

|                                                                                          |   substituted_pairs |
|:-----------------------------------------------------------------------------------------|--------------------:|
| [('Mr', 'monsieur')]                                                                     |               14350 |
| [('Minister', 'monsieur')]                                                               |               14107 |
| [('Mrs', 'madame')]                                                                      |                6845 |
| [('Mr', 'monsieur'), ('President', 'président')]                                         |                6267 |
| [('Minister', 'madame'), ('madame', 'ministre')]                                         |                4288 |
| [('Mr.', 'monsieur')]                                                                    |                4088 |
| [('Madam', 'madame'), ('President', 'président')]                                        |                3955 |
| [('Madam', 'madame'), ('Minister', 'ministre')]                                          |                1777 |
| [('Mr.', 'M')]                                                                           |                1408 |
| [('Prime', 'monsieur')]                                                                  |                1389 |
| [('De', 'de')]                                                                           |                1225 |
| [('Ms.', 'madame')]                                                                      |                1139 |
| [('Minister', 'monsieur'), ('monsieur', 'ministre')]                                     |                 963 |
| [('Mrs.', 'madame')]                                                                     |                 919 |
| [('Madam', 'madame'), ('Chair', 'président')]                                            |                 779 |
| [('Prime', 'monsieur'), ('Minister', 'le'), ('monsieur', 'premier'), ('le', 'ministre')] |                 692 |
| [('Mr', 'monsieur'), ('Secretary', 'secrétaire'), ('of', 'de'), ('State', 'état')]       |                 653 |
| [('Ms', 'madame')]                                                                       |                 558 |
| [('Mr.', 'monsieur'), ('President', 'président')]                                        |                 513 |

We can see that NER is bad, so we will disable the substitution of proper names.

There was one error in processing due to repetition of the MT output in BE-fr:
- "ParlaMint-BE_2016-05-11-54-commissie-ic414x.s517": /home/tajak/Parlamint-translation/Final-data/ParlaMint-BE.conllu/ParlaMint-BE.conllu/2016/ParlaMint-BE_2016-05-11-54-commissie-ic414x-fr.conll

### ParlaMint-EE

Most frequent substitutions:

|                                                        |   substituted_pairs |
|:-------------------------------------------------------|--------------------:|
| [('Peter', 'Peeter')]                                  |       3168          |
| [('Ligi', 'ligi')]                                     |       2611          |
| [('Mikhail', 'Mihhail'), ('Stalnukhin', 'Stalnuhhin')] |       1650          |
| [('Kruusimäe', 'Kruusi_mägi')]                         |       1356          |
| [('Chef', 'Kokk')]                                     |       1235          |
| [('Tiidus', 'Tiit')]                                   |       1109          |
| [('Helir', 'Helir-Valdor')]                            |       1025          |
| [('Põllamaas', 'Põllu_aas')]                           |       1002          |
| [('Ratas', 'ratas')]                                   |        993          |
| [('Vassilyev', 'Vassiljev')]                           |        925          |
| [('Hunter', 'Kütt')]                                   |        897          |
| [('Tuus', 'Tuus-Laul')]                                |        887          |
| [('Baltic', 'Balticu')]                                |        860          |
| [('George', 'Jüri')]                                   |        821          |
| [('Hatter', 'Külliki'), ('Külliki', 'Kübar_sepp')]     |        768          |
| [('Evgeny', 'Jevgeni')]                                |        759          |
| [('Mikhail', 'Mihhail')]                               |        699          |
| [('Echo', 'Kaja')]                                     |        691          |
| [('Savisaar', 'Savi_saar')]                            |        593          |

Most frequent substitutions include substitutions with words in lower case and lemmas with unusual symbols ('Kruusi_mägi', 'Savi_saar', etc.) which are different than the words in the running text. So, we will disable proper name substitution.

There were 3 errors in creation of the CONLL-u files based on the repetition in the MT:
- "ParlaMint-EE_2016-03-15_U4-P1.2": /home/tajak/Parlamint-translation/Final-data/ParlaMint-EE.conllu/ParlaMint-EE.conllu/2016/ParlaMint-EE_2016-03-15
- see more in logs/EE/create_conllu.md


### ParlaMint-ES

Most frequent substitutions:

|                              |   substituted_pairs |
|:-----------------------------|--------------------:|
| [('Mr', 'Señor')]            |                2815 |
| [('Mr.', 'Señor')]           |                2417 |
| [('Mrs.', 'Señora')]         |                1627 |
| [('Mrs', 'Señora')]          |                1570 |
| [('Ladies', 'Señorías')]     |                 975 |
| [('Mr', 'señor')]            |                 964 |
| [('Mr.', 'señor')]           |                 954 |
| [('Mrs', 'señora')]          |                 948 |
| [('Sanchez', 'Sánchez')]     |                 863 |
| [('Married', 'Casado')]      |                 735 |
| [('los', 'el')]              |                 486 |
| [('Citizens', 'Ciudadanos')] |                 372 |
| [('Churches', 'Iglesias')]   |                 328 |
| [('la', 'el')]               |                 266 |
| [('Candaimil', 'Candamil')]  |                 262 |
| [('Maria', 'María')]         |                 261 |
| [('Rodriguez', 'Rodríguez')] |                 254 |
| [('Moro', 'GonzáleZ-moro')]  |                 233 |
| [('Mrs.', 'señora')]         |                 226 |

Based on this, we will disable proper name correction based on substitutions (we would introduce more errors than solutions).