# Machine translating the ParlaMint output

Table of contents:
- [summary of the tasks](#tasks)
- [overview of datasets and their status](#datasets)
- [pipeline and code](#pipeline)
- [workflow in details](#workflow)
- [next steps](#next-steps)
- [analysis of reasons for errors in proper noun substitutions](#sample-analysis)
- [information on processing each corpus](#information-on-processing-each-corpus):
	- [ParlaMint-CZ](#parlamint-cz)
	- [ParlaMint-HR](#parlamint-hr)
	- [ParlaMint-BG](#parlamint-bg)
	- [ParlaMint-DK](#parlamint-dk)
	- [ParlaMint-IS](#parlamint-is)
	- [ParlaMint-PT](#parlamint-pt)

## Tasks:
- analyse various MT models on a sample data (ParlaMint-sample-sentence-tokenized.txt): see [code in Kaggle](https://www.kaggle.com/code/tajakuz/simple-machine-translation-with-various-mt-systems), results in the spreadsheet *ParlaMint_MT_Comparison-all-models.xlsx*
- extract data to be translated based on the Parlamint format
- use OPUSMT through EasyNMT to machine translate the output
- use eftomal to get word alignments (train it with the MT output) and assure that proper names are correctly translated based on the word alignments

## Datasets

Order of corpora to be translated: AT GR NO - (sample being evaluated:) HU TR NL - (evaluate by yourself:) SE NO RS BA

Status of the corpora and sizes are [available here](
https://docs.google.com/spreadsheets/d/1pfkaBgdacHdaC8-CMVYKze6MLe8EoSZVKs2viP_78fE/edit?usp=sharing).

Corpora with more than one language (marked with * in the table above):
- Parlamint-BE (Belgian), which has nl + fr. This is marked on the segments in the TEI, and we produce two sets of CoNLL-U files for them.
- ParlaMint-NO (Norwegian) also has two languages in TEI (Bokmal and Nynorsk), but these are are processed with the same model, so they have just one CoNLL-U set.

## Pipeline

1. Extract info from the source conll-u files into a dataframe: `CUDA_VISIBLE_DEVICES=1 nohup python 1-conllu-to-df.py "AT" > logs/AT/to_conllu.md &`
	- output: results/{lang_code}/ParlaMint-{lang_code}-extracted-source-data.csv

2. Choose the model (compare available models on a sample): 2-choose_MT_model.ipynb

3. Translate: `CUDA_VISIBLE_DEVICES=1 nohup python 3-translate.py "DK" "da" > logs/DK/translate.md &` (Provide the lang_code and the lang_code as is used by the OPUS-MT system)
	- Output: results/{lang_code}/ParlaMint-{lang_code}-translated.csv

4. Align: `CUDA_VISIBLE_DEVICES=2 nohup python 4-word-alignment.py "IS" > logs/IS/align.md &`:
	- Output:
		1. tokenized text is saved as: results/{lang_code}/ParlaMint-{lang_code}-translated-tokenized.csv
		2. corrected text is saved as: results/{lang_code}/ParlaMint-{lang_code}-final-dataframe.csv
	- if the analysis of most common substitutions reveals that it is better not to do the substitutions:
		- save the translations without the substitutions as the "new-translations" in the final file (in analyse_results.ipynb)
		- in 5-create-conllu.py, add the language code to the exceptions in line 107
5. Linguistically process translation and create final CONLL-u files: `CUDA_VISIBLE_DEVICES=2 nohup python 5-create-conllu.py "IS" > logs/IS/create_conllu.md &`
6. Send to new tantra: scp -r Final-data/ParlaMint-IS.conllu/ParlaMint-IS.conllu machine_address:~/.

## Workflow

1. Extract information from the CONLL-U
2. Translate
3. Tokenize English translations with Stanza
4. Word alignment, get information on NE annotations for each translated word from the source annotations
5. Linguistically process English translation with Stanza (lemmas, POS, ner)
6. Parse CONLL-u file and add additional information (sentence ids, alignments in both directions, source text, SpaceAfter information)

More details:
1. Extract from each sentence in the CONLL-u file:
	- sent_id (in metadata) (# sent_id = ParlaMint-SI_2014-08-01-SDZ7-Redna-01.seg1.1)
	- "text" (in metadata): to be feed into the MT system (# text = Spoštovani, prosim, da zasedete svoja mesta.) - in case of syntactic units, we use the multiword token, not the subparts ("Dovolte mi tedy, abych vás seznámila s omluvami, které předložili členové vlády." - to translate actual words)
	- tokenized text (punctuation separated from words by space): by iterating through the tokens in the sentence - create a list of tokens and join them into a string (["Spoštovani", "prosim", ",", "da"] -> "Spoštovani prosim , da). In case of multiword tokens, we add the subword tokens to the tokenized text and skip the multiword token. We will also get all necessary information about the ids and lemmas from the subword tokens. The subword tokens do not have the NER annotation, so we will use the multiword annotation for all of its subparts. We use the subword tokens instead of multiword tokens to get the correct lemma (multiword tokens do not have lemmata) and also in case that the target proper noun would be aligned with the proper noun in the subword token. So, for alignment, we use the tokenized text with subword tokens (e.g., Dovolte mi tedy, abych vás seznámila s omluvami, které předložili členové vlády.)
	- information on the proper nouns: if the word is annotated as a proper noun (has "PER" in ner attribute), take its index, form and lemma and save it into a dictionary for each sentence ({0: (Taje, Taja), 1: (Kuzman, Kuzman)})
2. Translate
3. Word alignment:
	- We apply the stanza tokenization over the translation; use tokenize_no_ssplit to avoid splitting sentences in multiple sentences. Save also information on whether there was initially a space around punctuation (based on start_char and end_char information) which we use at the end to remove spaces around the punctuation in the translation.
	- Perform word alignment.
	- Save forward and reverse alignment information for each word - they should be connected with the indices of source words as they appear in the source conllu file. The conllu files start counting with 1, while alignment starts with 0, so to get those indices, we will add "1" to each aligned index.
	- Substitute translated NE words with lemmas based on the annotation to create the new translation. For the words that were substituted, save also a list of the original words (to be added to the conllu).
4. Linguistic processing of translated text:
	- We use Stanza to get POS, lemmas and NER (the 4 tag package: conll03). Send in the "pre-tokenized text" (created in previous steps).
	- Transform the result into CONLL-u (which should contain tokens, lemmas, pos). Parse the CONLL-u file and add:
		1) sentence_id as metadata
		2) based on alignment, add SpaceAfter information - I add this information only if "SpaceAfter" is "No" (as it is in the original texts)
		3) source text ("source")
		4) original translated text (before improvements - #initial_translation metadata) (used only for testing, won't be added in the final conllu)
		5) improved translated text (#text metadata): based on SpaceAfter information, remove spaces around punctuation
		6) Delete startchar and endchar information from ["misc"] metadata element
		7) Change the NER tags so that they correspond to the source NER tags: "S-" to "B-", "E-" to "I-"
		8) For the words that were substituted, add the original translation (#Translated metadata) to ["misc"]
		9) For all words, add information on alignment (#ForwardAlignment and #BackwardAlignment) with the conllu indices of source words (in case of syntactic units, as the alignment is done on subword level, indices point to subwords, not multitokens)
		19) source word indices as metadata ("source_indices") - used only for testing, won't be added in the final conllu
	- Save the file as CONLLU with the same name as the source CONLLU file (so each file will be saved separately). The number of sentences should be the same as in the source CONLLU and ANA file.

This is now implemented, the sample files are:
- sample file with additional information for debugging purposes (initial translation, source_indices: ["results/CZ-old/final_translated_conllu/sample_with_dev_metadata_ParlaMint-CZ_2013-11-25-ps2013-001-01-002-002.conllu"](https://github.com/TajaKuzman/Parlamint-translation/blob/master/results/CZ-old/final_translated_conllu/sample_with_dev_metadata_ParlaMint-CZ_2013-11-25-ps2013-001-01-002-002.conllu)
- final format: ["results/CZ-old/final_translated_conllu/final_sample_ParlaMint-CZ_2013-11-25-ps2013-001-01-002-002.conllu"](https://github.com/TajaKuzman/Parlamint-translation/blob/master/results/CZ-old/final_translated_conllu/final_sample_ParlaMint-CZ_2013-11-25-ps2013-001-01-002-002.conllu)

Some remarks:
- Stanza does not output "SpaceAfter" information, I added it manually based on the start_char and end_char information


## Next steps
- metadata translation: **we want to translate all the text contents of non-s elements**, but in a lexicon-based approach, so extracting all "Ploskanje" etc., deduplicating, translating, and **returning as a tab-separated dataset - what should the dataset include - source, translation, maybe also tag name, anything else?**, to be applied in the translated resource by Tomaž and Matyaš.

- other possible corrections as part of post-processing:
	- Danish: "All the models have problems with numbering e.g. § 19, stk. 4 and with punctuation in abbreviations. Could that be corrected in a post process?"

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
- /home/tajak/Parlamint-translation/Final-data/ParlaMint-BG.conllu/ParlaMint-BG.conllu/2017/ParlaMint-BG_2017-11-08.conllu: ParlaMint-BG_2017-11-08.seg1140.1, ParlaMint-BG_2017-11-08.seg1250.1
- /home/tajak/Parlamint-translation/Final-data/ParlaMint-BG.conllu/ParlaMint-BG.conllu/2017/ParlaMint-BG_2017-09-20.conllu: ParlaMint-BG_2017-09-20.seg14.2
- ParlaMint-BG_2018-07-19.seg746.1 - /home/tajak/Parlamint-translation/Final-data/ParlaMint-BG.conllu/ParlaMint-BG.conllu/2018/ParlaMint-BG_2018-07-19.conllu
- ParlaMint-BG_2018-10-12.seg204.1 - /home/tajak/Parlamint-translation/Final-data/ParlaMint-BG.conllu/ParlaMint-BG.conllu/2018/ParlaMint-BG_2018-10-12.conllu
- ParlaMint-BG_2018-04-19.seg252.1 - /home/tajak/Parlamint-translation/Final-data/ParlaMint-BG.conllu/ParlaMint-BG.conllu/2018/ParlaMint-BG_2018-04-19.conllu
- ParlaMint-BG_2018-03-21.seg385.1 - /home/tajak/Parlamint-translation/Final-data/ParlaMint-BG.conllu/ParlaMint-BG.conllu/2018/ParlaMint-BG_2018-03-21.conllu
- ParlaMint-BG_2018-07-18.seg780.1 - /home/tajak/Parlamint-translation/Final-data/ParlaMint-BG.conllu/ParlaMint-BG.conllu/2018/ParlaMint-BG_2018-07-18.conllu
- ParlaMint-BG_2018-10-24.seg922.1 - /home/tajak/Parlamint-translation/Final-data/ParlaMint-BG.conllu/ParlaMint-BG.conllu/2018/ParlaMint-BG_2018-10-24.conllu
- ParlaMint-BG_2018-07-11.seg873.1 - /home/tajak/Parlamint-translation/Final-data/ParlaMint-BG.conllu/ParlaMint-BG.conllu/2018/ParlaMint-BG_2018-07-11.conllu
- ParlaMint-BG_2018-04-04.seg629.1 - /home/tajak/Parlamint-translation/Final-data/ParlaMint-BG.conllu/ParlaMint-BG.conllu/2018/ParlaMint-BG_2018-04-04.conllu
- ... (for all sentences, see logs/BG/create_conllu.md)


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
- ParlaMint-DK_2017-10-04-20171-M2.conllu: ParlaMint-DK_20171004130237.seg2.20
- ParlaMint-DK_2017-05-30-20161-M104.conllu: ParlaMint-DK_20170530131245.seg28.24
	`The next item is the joint debate on the following motions for resolutions: 8, adopted by a majority (S, DF, V, LA and CF) on Amendment No 8, tabled by the Group of the European People's Party (Christian Democrats) and European Democrats, on behalf of the Group of the European People's Party (Christian Democrats) and European Democrats, on behalf of the Group of the European People's Party (Christian Democrats) and European Democrats, on behalf of the Group of the European People's Party (Christian Democrats) and European Democrats, on behalf of the Group of the European People's Party (Christian Democrats) and European Democrats, on behalf of the Group of the European People's Party (Christian Democrats) and European Democrats, on behalf of the Group of the European People's Party (Christian Democrats), on behalf of the Group of the European People's Party (Christian Democrats) and European Democrats, on behalf of the Liberal, Democratic and Reformist Group, on behalf of the European Democratic Group. 11-13, adopted by the Committee on Amendment No. 14, adopted by a majority (Committee with the exception of EL and ALT), on Amendment No. 15-17, adopted by the committee, on Amendment No 17. 18. adopted by a majority (Committee with the exception of EL and ALT) on Amendment No 18. 19 and 20, adopted by the Committee, on Amendments Nos 19 and 20. 21, adopted by a majority (S, DF, V, LA and CF), on Amendment No 21, tabled by the Group of the European People's Party (Christian Democrats) and European Democrats (Christian Democrats ) and European Democrats(Christian Democrats) and European Democrats (Christian Democrats) and European Democrats (Christian Democrats) and European Democrats (Christian Democrats) and European Democrats (Christian Democrats) and European Democrats). 22, 26, 27, 29-35 and 37-39, adopted by the Committee, on Amendments Nos. 41. adopted by a majority (S, DF, V, LA and CF) on Amendment No. 42-44, as agreed by the committee, on Amendment No. 47, adopted by a majority (S, DF, V, LA and CF) or on Amendment No 7. 48th meeting of the Committee?`
- ParlaMint-DK_2018-10-03-20181-M2.conllu: ParlaMint-DK_20181003130302.seg2.9
- ParlaMint-DK_2016-11-08-20161-M12.conllu: ParlaMint-DK_20161108142038.seg96.5
- ParlaMint-DK_2016-05-03-20151-M86.conllu: ParlaMint-DK_20160503174318.seg453.10:
	`That is to say, the rapporteur believes that the people per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per; per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per definition has the right tocitizenship.`
- ParlaMint-DK_2022-03-16-20211-M75.conllu: ParlaMint-DK_20220316131402.seg27.2
- ParlaMint-DK_2022-03-01-20211-M69.conllu: ParlaMint-DK_20220301130003.seg1.4
- ParlaMint-DK_2021-06-03-20201-M128.conllu: ParlaMint-DK_20210603165102.seg595.5:
	`And as far as starting the fight against knowledge is concerned, Fonsmark has a point, namely that it is wrong to throw knowledge on the dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dang dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d dd `
- ParlaMint-DK_2015-07-03-20142-M2.conllu: ParlaMint-DK_20150703110004.seg1.5
- ParlaMint-DK_2020-12-17-20201-M39.conllu: ParlaMint-DK_20201217161351-2.seg600.3
- ParlaMint-DK_2020-03-13-20191-M76.conllu
: ParlaMint-DK_20200313122701.seg34.8
- ParlaMint-DK_2020-04-28-20191-M100.conllu: ParlaMint-DK_20200428165944.seg296.14
- ParlaMint-DK_2019-10-02-20191-M2.conllu: ParlaMint-DK_20191002130244.seg2.30
- ParlaMint-DK_2019-10-10-20191-M6.conllu: ParlaMint-DK_20191010100051.seg3.10
- ParlaMint-DK_2019-12-13-20191-M37.conllu: ParlaMint-DK_20191213124228.seg250.6


The processing into CONLL-u files revealed some errors in translations when unwanted repetition occurred - this is the case of the following 15 sentences:
- ParlaMint-DK_2017-10-04-20171-M2.conllu: ParlaMint-DK_20171004130237.seg2.20
- ParlaMint-DK_2017-05-30-20161-M104.conllu: ParlaMint-DK_20170530131245.seg28.24
	`The next item is the joint debate on the following motions for resolutions: 8, adopted by a majority (S, DF, V, LA and CF) on Amendment No 8, tabled by the Group of the European People's Party (Christian Democrats) and European Democrats, on behalf of the Group of the European People's Party (Christian Democrats) and European Democrats, on behalf of the Group of the European People's Party (Christian Democrats) and European Democrats, on behalf of the Group of the European People's Party (Christian Democrats) and European Democrats, on behalf of the Group of the European People's Party (Christian Democrats) and European Democrats, on behalf of the Group of the European People's Party (Christian Democrats) and European Democrats, on behalf of the Group of the European People's Party (Christian Democrats), on behalf of the Group of the European People's Party (Christian Democrats) and European Democrats, on behalf of the Liberal, Democratic and Reformist Group, on behalf of the European Democratic Group. 11-13, adopted by the Committee on Amendment No. 14, adopted by a majority (Committee with the exception of EL and ALT), on Amendment No. 15-17, adopted by the committee, on Amendment No 17. 18. adopted by a majority (Committee with the exception of EL and ALT) on Amendment No 18. 19 and 20, adopted by the Committee, on Amendments Nos 19 and 20. 21, adopted by a majority (S, DF, V, LA and CF), on Amendment No 21, tabled by the Group of the European People's Party (Christian Democrats) and European Democrats (Christian Democrats ) and European Democrats(Christian Democrats) and European Democrats (Christian Democrats) and European Democrats (Christian Democrats) and European Democrats (Christian Democrats) and European Democrats (Christian Democrats) and European Democrats). 22, 26, 27, 29-35 and 37-39, adopted by the Committee, on Amendments Nos. 41. adopted by a majority (S, DF, V, LA and CF) on Amendment No. 42-44, as agreed by the committee, on Amendment No. 47, adopted by a majority (S, DF, V, LA and CF) or on Amendment No 7. 48th meeting of the Committee?`
- ParlaMint-DK_2018-10-03-20181-M2.conllu: ParlaMint-DK_20181003130302.seg2.9
- ParlaMint-DK_2016-11-08-20161-M12.conllu: ParlaMint-DK_20161108142038.seg96.5
- ParlaMint-DK_2016-05-03-20151-M86.conllu: ParlaMint-DK_20160503174318.seg453.10:
	`That is to say, the rapporteur believes that the people per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per; per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per person per definition has the right tocitizenship.`
- ParlaMint-DK_2022-03-16-20211-M75.conllu: ParlaMint-DK_20220316131402.seg27.2
- ParlaMint-DK_2022-03-01-20211-M69.conllu: ParlaMint-DK_20220301130003.seg1.4
- ParlaMint-DK_2021-06-03-20201-M128.conllu: ParlaMint-DK_20210603165102.seg595.5:
	`And as far as starting the fight against knowledge is concerned, Fonsmark has a point, namely that it is wrong to throw knowledge on the dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dang dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung dung d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d dd `
- ParlaMint-DK_2015-07-03-20142-M2.conllu: ParlaMint-DK_20150703110004.seg1.5
- ParlaMint-DK_2020-12-17-20201-M39.conllu: ParlaMint-DK_20201217161351-2.seg600.3
- ParlaMint-DK_2020-03-13-20191-M76.conllu
: ParlaMint-DK_20200313122701.seg34.8
- ParlaMint-DK_2020-04-28-20191-M100.conllu: ParlaMint-DK_20200428165944.seg296.14
- ParlaMint-DK_2019-10-02-20191-M2.conllu: ParlaMint-DK_20191002130244.seg2.30
- ParlaMint-DK_2019-10-10-20191-M6.conllu: ParlaMint-DK_20191010100051.seg3.10
- ParlaMint-DK_2019-12-13-20191-M37.conllu: ParlaMint-DK_20191213124228.seg250.6


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

No errors occurred in CONLL-u creation.

### ParlaMint-PT

The analysis of the substitutions revealed that Portuguese NER model is much worse (or different) than the models for other languages - words, annotated as Proper Nouns: Ministro, Presidente, Deputado, Equipa, sr., ...

Based on the list of most frequent substitutions, I won't use the substitution process for this language, because we would introduce more errors than solutions.

Most frequent substitutions:

|                                                                       |   substituted_pairs |
|:----------------------------------------------------------------------|--------------------:|
| 0                                                                     |              282730 |
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
- ParlaMint-PT_2018-05-04.seg808.s: /home/tajak/Parlamint-translation/Final-data/ParlaMint-PT.conllu/ParlaMint-PT.conllu/2018/ParlaMint-PT_2018-05-04.conllu
- ... (see all instances in logs/PT/create_conllu.md)

### ParlaMint-HR

Most frequent substitutions:

### ParlaMint-IT

Most frequent substitutions:

|                                                                     |   substituted_pairs |
|:--------------------------------------------------------------------|--------------------:|
| 0                                                                   |         1.24942e+06 |
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
- ParlaMint-IT_2017-01-12-LEG17-Senato-sed-740.ana.seg7.1: /home/tajak/Parlamint-translation/Final-data/ParlaMint-IT.conllu/ParlaMint-IT.conllu/2017/ParlaMint-IT_2017-01-12-LEG17-Senato-sed-740.conllu
- ... (see all in logs/IT/create_conllu.md)

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

### ParlaMint-SE

The following 9 files were revealed to be empty and are not included in the df:

ParlaMint-SE_2018-08-09-prot-201718--141.conllu

ParlaMint-SE_2018-05-14-prot-201718--110.conllu

ParlaMint-SE_2018-11-27-prot-201819--21.conllu

ParlaMint-SE_2018-11-20-prot-201819--18.conllu

ParlaMint-SE_2018-12-10-prot-201819--25.conllu

ParlaMint-SE_2018-12-13-prot-201819--28.conllu

ParlaMint-SE_2018-11-06-prot-201819--12.conllu

ParlaMint-SE_2018-12-04-prot-201819--23.conllu

ParlaMint-SE_2018-11-13-prot-201819--15.conllu

ParlaMint-SE_2016-10-19-prot-201617--17.conllu

ParlaMint-SE_2016-09-21-prot-201617--6.conllu

ParlaMint-SE_2022-02-28-prot-202122--74.conllu

ParlaMint-SE_2022-04-13-prot-202122--97.conllu

ParlaMint-SE_2022-03-14-prot-202122--80.conllu

ParlaMint-SE_2021-01-04-prot-202021--58.conllu

ParlaMint-SE_2021-11-26-prot-202122--35.conllu

ParlaMint-SE_2021-09-28-prot-202122--11.conllu

ParlaMint-SE_2021-01-05-prot-202021--59.conllu

ParlaMint-SE_2021-07-06-prot-202021--151.conllu

ParlaMint-SE_2021-11-16-prot-202122--28.conllu

ParlaMint-SE_2021-01-07-prot-202021--60.conllu

ParlaMint-SE_2021-06-29-prot-202021--149.conllu

ParlaMint-SE_2021-12-07-prot-202122--40.conllu

ParlaMint-SE_2021-11-04-prot-202122--25.conllu

ParlaMint-SE_2021-08-17-prot-202021--154.conllu

ParlaMint-SE_2021-06-28-prot-202021--148.conllu

ParlaMint-SE_2021-12-20-prot-202122--49.conllu

ParlaMint-SE_2020-04-27-prot-201920--112.conllu

ParlaMint-SE_2020-04-21-prot-201920--108.conllu

ParlaMint-SE_2020-04-07-prot-201920--101.conllu

ParlaMint-SE_2020-05-12-prot-201920--119.conllu

ParlaMint-SE_2020-03-30-prot-201920--96.conllu

ParlaMint-SE_2020-06-29-prot-201920--144.conllu

ParlaMint-SE_2020-03-24-prot-201920--92.conllu

ParlaMint-SE_2020-04-09-prot-201920--103.conllu

ParlaMint-SE_2020-05-19-prot-201920--122.conllu

ParlaMint-SE_2020-03-19-prot-201920--89.conllu

ParlaMint-SE_2020-04-30-prot-201920--115.conllu

ParlaMint-SE_2020-06-30-prot-201920--145.conllu

ParlaMint-SE_2020-05-20-prot-201920--123.conllu

ParlaMint-SE_2020-09-29-prot-202021--16.conllu

ParlaMint-SE_2019-01-14-prot-201819--36.conllu

ParlaMint-SE_2019-01-17-prot-201819--38.conllu

ParlaMint-SE_2019-01-22-prot-201819--41.conllu


### ParlaMint-NL

The following 55 files were revealed to be empty and are not included in the df:

ParlaMint-NL_2017-03-23-tweedekamer-4.conllu

ParlaMint-NL_2017-03-23-tweedekamer-3.conllu

ParlaMint-NL_2017-10-25-tweedekamer-3.conllu

ParlaMint-NL_2017-09-07-tweedekamer-4.conllu

ParlaMint-NL_2017-10-31-tweedekamer-2.conllu

ParlaMint-NL_2017-03-28-eerstekamer-3.conllu

ParlaMint-NL_2017-03-23-tweedekamer-5.conllu

ParlaMint-NL_2018-10-02-eerstekamer-3.conllu

ParlaMint-NL_2018-06-07-tweedekamer-9.conllu

ParlaMint-NL_2018-09-13-tweedekamer-7.conllu

ParlaMint-NL_2018-01-18-tweedekamer-5.conllu

ParlaMint-NL_2018-09-05-tweedekamer-3.conllu

ParlaMint-NL_2018-10-10-tweedekamer-3.conllu

ParlaMint-NL_2018-12-12-tweedekamer-6.conllu

ParlaMint-NL_2018-06-07-tweedekamer-14.conllu

ParlaMint-NL_2018-06-13-tweedekamer-6.conllu

ParlaMint-NL_2018-04-03-tweedekamer-6.conllu

ParlaMint-NL_2018-06-06-tweedekamer-6.conllu

ParlaMint-NL_2018-11-07-tweedekamer-9.conllu

ParlaMint-NL_2018-06-05-tweedekamer-7.conllu

ParlaMint-NL_2016-04-20-tweedekamer-7.conllu

ParlaMint-NL_2016-12-14-tweedekamer-5.conllu

ParlaMint-NL_2016-01-26-tweedekamer-6.conllu

ParlaMint-NL_2016-03-01-tweedekamer-6.conllu

ParlaMint-NL_2016-01-12-tweedekamer-6.conllu

ParlaMint-NL_2016-09-13-eerstekamer-6.conllu

ParlaMint-NL_2016-01-27-tweedekamer-4.conllu

ParlaMint-NL_2016-11-30-tweedekamer-5.conllu

ParlaMint-NL_2015-06-09-eerstekamer-4.conllu

ParlaMint-NL_2015-11-03-tweedekamer-6.conllu

ParlaMint-NL_2015-09-22-tweedekamer-8.conllu

ParlaMint-NL_2015-06-16-eerstekamer-3.conllu

ParlaMint-NL_2015-01-13-tweedekamer-7.conllu

ParlaMint-NL_2015-06-16-eerstekamer-5.conllu

ParlaMint-NL_2015-11-05-tweedekamer-6.conllu

ParlaMint-NL_2015-05-20-tweedekamer-7.conllu

ParlaMint-NL_2015-08-19-tweedekamer-3.conllu

ParlaMint-NL_2020-05-20-tweedekamer-5.conllu

ParlaMint-NL_2020-05-07-tweedekamer-3.conllu

ParlaMint-NL_2020-09-01-tweedekamer-7.conllu

ParlaMint-NL_2020-01-22-tweedekamer-4.conllu

ParlaMint-NL_2020-09-22-tweedekamer-6.conllu

ParlaMint-NL_2019-07-03-tweedekamer-11.conllu

ParlaMint-NL_2019-06-25-tweedekamer-5.conllu

ParlaMint-NL_2019-06-05-tweedekamer-4.conllu

ParlaMint-NL_2019-06-11-eerstekamer-3.conllu

ParlaMint-NL_2019-06-18-eerstekamer-3.conllu

ParlaMint-NL_2019-03-26-tweedekamer-6.conllu

ParlaMint-NL_2019-03-12-tweedekamer-6.conllu

ParlaMint-NL_2019-07-02-eerstekamer-5.conllu

ParlaMint-NL_2019-06-11-eerstekamer-4.conllu

ParlaMint-NL_2019-02-20-tweedekamer-6.conllu

ParlaMint-NL_2019-06-11-tweedekamer-5.conllu

ParlaMint-NL_2019-06-11-eerstekamer-6.conllu

ParlaMint-NL_2019-05-29-tweedekamer-6.conllu


