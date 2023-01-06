def extract_text(files_path, lang_code):
	"""
	This function finds paths to all TEI.ana files from the files_path (directory with the files) and saves them to a list.Based on the list, it takes all files,
	extracts text and information on proper nouns from each and saves it into a dataframe.
	It returns the dataframe with extracted text, information on file and sentence_id and proper nouns,
	saved as "ParlaMint-{lang_code}-file-for-MT.csv".

	Args:
	- files_path (string): the directory with the annotated XLM TEI files.
	- lang_code: the lang code that is used in the names of the files, e.g. "SI" in "ParlaMint-SI_2014-08-01-SDZ7-Redna-01.ana"
	"""
	import pandas as pd
	import regex as re
	from bs4 import BeautifulSoup as bs
	import os
	from IPython.display import display

	
	# Get a list of TEI.ana files
	dir_list = os.listdir(files_path)

	# Keep only files with parliamentary sessions (do not include metadata in the list):

	parl_list = []

	for i in dir_list:
		if "ParlaMint-{}_".format(lang_code) in i:
			parl_list.append("{}/{}".format(files_path, i))

	print("Number of files is: {}".format(len(parl_list)))

	# Create an empty df
	df = pd.DataFrame({"file": [""], "sentence_id": [""], "text": [""], "proper_nouns": [""]})

	# Create a regex to separate word id into segment id and word index
	word_seg_re = re.compile("(.*)\.(\d+)")

	for doc in parl_list:
		# Open the file
		file = open("{}".format(doc), "r")
		content = bs(file, 'lxml')

		# Create a list of sentences
		sentence_list = []
		sen_id_list = []
		proper_nouns_list = []

		# Search for all segments
		seg_list = content.find_all("seg")

		for segment in seg_list:
			sentences = segment.find_all("s")
			for sentence in sentences:
				# Get text, replace \n with a space and remove spaces from the beginning and end of string
				sentence_list.append(sentence.getText().replace("\n", " ").strip(" "))
				
				# Add information on sentence id
				sen_id = sentence["xml:id"]
				sen_id_list.append(sen_id)

				# Add information on proper nouns
				current_proper_nouns_list = []

				result = sentence.find_all("name", type = "PER", recursive=False)

				if len(result) > 0:
					word_dict = {}
					for i in result:
						words = i.find_all("w", recursive = False)
						for word in words:
							current_name = word.getText()
							current_lemma = word["lemma"]
							current_word_id = word["xml:id"]
							current_word_index = word_seg_re.findall(current_word_id)[0][1]
							# I'll substract one from the word index, because indexing in the TEI file starts with 1, not 0
							current_word_index = int(current_word_index) - 1
							word_dict[current_word_index] = [current_name, current_lemma]
					
					current_proper_nouns_list.append(word_dict)

				proper_nouns_list.append(current_proper_nouns_list)

		new_df = pd.DataFrame({"sentence_id": sen_id_list, "text": sentence_list, "proper_nouns": proper_nouns_list})
		new_df["file"] = doc

		# Merge df to the previous df
		df = pd.concat([df, new_df])

	# Reset index
	df = df.reset_index(drop=True)

	# Remove the first (empty) row
	df = df.drop([0], axis="index")

	# Add information on length
	df["length"] = df["text"].str.split().str.len()

	print("Number of words in the corpora: {}".format(df["length"].sum()))
	
	# Show the df information
	display(df.describe(include="all"))

	# Save the dataframe
	df.to_csv("results/{}/ParlaMint-{}-file-for-MT.csv".format(lang_code,lang_code), sep="\t")

	return df

def choose_model(lang_code):
	"""
	Compare a small sample of translations of all OPUS-MT models that are available
	for the language, to decide which one to use. The function prints out a dataframe with all translations of the sample and saves it as ParlaMint-{lang_code}-sample-model-comparison.csv.

	Args:
	- lang_code: the lang code that is used in the names of the files, it should be the same as for extract_text()
	"""
	import pandas as pd
	import regex as re
	from easynmt import EasyNMT
	from IPython.display import display
	
	lang_models_dict = {"BG": ["bg", "sla", "zls"], "HR": ["zls"], "CZ": ["cs", "sla", "zlw" ], "DK": ["da", "gmq", "gem"], "NL": ["nl", "gem", "gmw"], "FR": ["fr", "itc","roa"], "HU": ["mul"], "IS": ["is","gmq", "gem"], "IT": ["it", "roa", "itc"], "LV": ["lv","bat"], "LT": ["bat"], "PL": ["pl", "sla", "zlw"], "SI": ["sla", "zls"], "ES": ["es", "roa", "itc"], "TR": ["tr", "trk" ], "AT": ["de", "gem", "gmw"], "ES-PV": ["eu", "mul"], "BA": ["sla", "zls"], "ES-CT": ["ca", "roa", "itc"], "EE": ["et", "urj", "fiu"], "FI": ["fi", "urj", "fiu"], "ES-GA": ["gl", "roa", "itc"], "GR": ["grk"], "PT": ["roa", "itc"], "RO":["roa", "itc"], "RS": ["zls", "sla"], "SE": ["sv", "gmq", "gem"], "UA":["uk", "sla", "zle"]}

	# Open the file, created in the previous step
	df = pd.read_csv("results/{}/ParlaMint-{}-file-for-MT.csv".format(lang_code, lang_code), sep="\t", index_col=0)

	# Define the model
	model = EasyNMT('opus-mt')

	print("Entire corpus has {} sentences and {} words.".format(df["text"].count(), df["length"].sum()))

	# Create a smaller sample - just a couple of sentences from one file
	df = df[df.file == list(df["file"].unique())[0]][:20]

	print("Sample files has {} sentences and {} words.".format(df["text"].count(), df["length"].sum()))

	# Create a list of sentences from the df
	sentence_list = df.text.to_list()

	# Translate the sample using all available models for this language
	for opus_lang_code in lang_models_dict[lang_code]:
		translation_list = model.translate(sentence_list, source_lang = "{}".format(opus_lang_code), target_lang='en')

		# Add the translations to the df
		df["translation-{}".format(opus_lang_code)] = translation_list
	
	# Display the df
	with pd.option_context('display.max_colwidth', None):
		display(df.drop(columns=["file", "sentence_id", "proper_nouns", "length"]))

	# Save the df
	df.to_csv("results/{}/ParlaMint-{}-sample-model-comparison.csv".format(lang_code, lang_code), sep="\t")

def translate(lang_code, opus_lang_code):
	"""
	This function translates the text from the dataframe, created with the extract_text() function
	with OPUS-MT models using EasyNMT. It returns a dataframe with the translation.

	Args:
	- lang_code: the lang code that is used in the names of the files, it should be the same as for extract_text()
	- opus_lang_code: the lang code to be used in the OPUS-MT model - use the one that performed the best in the comparison (see function choose_model())
	"""
	import pandas as pd
	import regex as re
	from easynmt import EasyNMT

	# Open the file, created in the previous step
	df = pd.read_csv("results/{}/ParlaMint-{}-file-for-MT.csv".format(lang_code, lang_code), sep="\t", index_col=0)

	# Define the model
	model = EasyNMT('opus-mt')

	print("Entire corpus has {} sentences and {} words.".format(df["text"].count(), df["length"].sum()))

	# Create a list of sentences from the df
	sentence_list = df.text.to_list()

	#Translate the list of sentences - you need to provide the source language as it is in the name of the model - the opus_lang_code
	translation_list = model.translate(sentence_list, source_lang = "{}".format(opus_lang_code), target_lang='en')

	# Add the translations to the df
	df["translation"] = translation_list

	# Display the df
	print(df[:3].to_markdown())

	# Save the df
	df.to_csv("results/{}/ParlaMint-{}-translated.csv".format(lang_code, lang_code), sep="\t")

	return df

def correct_proper_nouns(lang_code):
	"""
	This function takes the translated text and the source text, aligns words with eflomal and corrects proper nouns.
	It takes the dataframe that was created in the function extract_text() and to which the translation was added
	in the function translate().

	To use eflomal, you need to install it first:
	!git clone https://github.com/robertostling/eflomal
	%cd eflomal
	!make
	!sudo make install
	!python3 setup.py install

	Args:
	- lang_code: the lang code that is used in the names of the files, it should be the same as for extract_text()
	"""
	import pandas as pd
	import re
	import ast
	import os

	# Open the file, created in the previous step
	df = pd.read_csv("results/{}/ParlaMint-{}-translated.csv".format(lang_code, lang_code), sep="\t", index_col=0)

	# Move into the eflomal folder
	os.chdir("./eflomal")

	# In the source text, the punctuation marks are separated from the words.
	# To assure good alignment, we'll do that for the translated text as well.

	translation_list = df.translation.to_list()
	translation_added_spaces = []

	for translation in translation_list:
		# Add spaces around each punctuation
		translation = re.sub('([.,!?:;()])', r' \1 ', translation)
		# Remove duplicated spaces
		translation = re.sub('\s{2,}', ' ', translation)
		translation_added_spaces.append(translation)

	df["translation_added_spaces"] = translation_added_spaces

	# Maybe we'll need to move to the eflomal folder
	#%cd eflomal

	# Then we need to create files for all texts and all translations
	source_sentences = open("source_sentences.txt", "w")
	English_sentences = open("English_sentences.txt", "w")

	for i in df.text.to_list():
		source_sentences.write(i)
		source_sentences.write("\n")

	for i in df.translation_added_spaces.to_list():
		English_sentences.write(i)
		English_sentences.write("\n")

	source_sentences.close()
	English_sentences.close()

	# Align sentences with eflomal and get out a file with alignments
	os.system("python3 align.py -s source_sentences.txt -t English_sentences.txt --model 3 -r source-en.rev")

	# Create a list of alignments from the returned file
	aligns_list = open("source-en.rev", "r").readlines()
	aligns_list = [i.replace("\n", "") for i in aligns_list]
	aligns_list = [i.split(" ") for i in aligns_list]

	final_aligns = []

	# Create a dictionary out of the list
	for i in aligns_list:
		current_line = {}

		try:
			for element in i:
				new_list = element.split("-")

				a = int(new_list[0])
				b = int(new_list[1])
				current_line[a] = b
		
			# Check whether the number of pairs in the list is the same as number of items
			if len(i) != len(list(current_line.items())):
				print("Not okay:")
				print(i)
				print(current_line)

			final_aligns.append(current_line)
		
		except:
			print("error")
			print(aligns_list.index(i))
			print(i)
			final_aligns.append("Error")
		
	print("Number of aligned sentences: {}".format(len(final_aligns)))

	# Add a to the df
	df["alignments"] = final_aligns

	# Remove the rev file
	os.remove("source-en.rev")

	# When we open the dataframe file, the dictionaries with proper names changed into strings - Change strings in the column proper_nouns into dictionaries

	df["proper_nouns"] = df.proper_nouns.astype("str")
	df["proper_nouns"] = df.proper_nouns.apply(lambda x: ast.literal_eval(x))

	# Remove the list brackets
	df["proper_nouns"] = df.proper_nouns.str[0]

	# Change nan values in the proper_nouns columns
	df = df.fillna(0)

	# Substitute words in the translation based on alignments
	intermediate_list = list(zip(df["translation_added_spaces"], df["proper_nouns"], df["alignments"]))

	new_translations = []
	substituted_all_info = []
	substituted_only = []

	# Add information whether an error occurred
	error_list = []

	for i in intermediate_list:
		current_substituted_list = []
		current_substituted_only = []
		current_error = "No"

		# If no proper names were detected, do not change the translation
		if i[1] == 0:
			new_translations.append(i[0])
		
		else:
			current_translation = i[0]

			# Substitute the word with the Slovene lemma based on the index - loop through the proper nouns to be changed
			for word_index in list(i[1].keys()):
				try:
					# split the translation into list of words
					word_list = current_translation.split()

					# Get index of the substituted word
					substituted_word_index = i[2][word_index]

					# Get the lemma to substitute the word with
					correct_lemma = i[1][word_index][1]

					# If the substitute word and lemma are not the same, get substituted word and its match
					if word_list[substituted_word_index] != correct_lemma:
						current_substituted_list.append((word_list[substituted_word_index], correct_lemma))
						current_substituted_only.append((word_list[substituted_word_index], correct_lemma))

						# Substitute the word in the word list
						word_list[substituted_word_index] = correct_lemma
					
					else:
						# Add information that substitution was not performed
						current_substituted_list.append(f"No substitution: {word_list[substituted_word_index], correct_lemma}")
					
					# Change the translation by merging the words back into a string
					current_translation = " ".join(word_list)

				except:
					print(f"Issue: index {word_index}: {i[1][word_index]}")
					current_error = f"Issue: index {word_index}: {i[1][word_index]}"

			# After the loop through proper nouns, save the new translation
			new_translations.append(current_translation)
		
		# Add information on what was substituted
		substituted_all_info.append(current_substituted_list)
		substituted_only.append(current_substituted_only)
		error_list.append(current_error)


	# Add to the df
	df["new_translations"] = new_translations
	df["substitution_info"] = substituted_all_info
	df["substituted_words"] = substituted_only
	df["errors"] = error_list

	# Change the working directory once again
	os.chdir("..")

	# Save the df
	df.to_csv("results/{}/ParlaMint-{}-final.csv".format(lang_code, lang_code), sep="\t")

	# Display most common substitutions
	df_substituted = df[df["proper_nouns"] != "0"]
	print(df_substituted.substituted_words.value_counts()[:20].to_markdown())

	return df