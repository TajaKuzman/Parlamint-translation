import os
import argparse
import zipfile
import gzip
import shutil
import pandas as pd
from knockknock import discord_sender

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("lang_code", help="lang code used in the files")
    parser.add_argument("opus_lang_code", help="lang code used by the MT system")
    args = parser.parse_args()

# Define the language code, used in the file names
#lang_code = "CZ"
lang_code = args.lang_code
opus_lang_code = args.opus_lang_code

# Main path
main_path = "/home/tajak/Parlamint-translation"

# Check in your directory whether the path to the folder with conllu files is ok:
path = "{}/Source-data/ParlaMint-{}.conllu/ParlaMint-{}.conllu".format(main_path, lang_code, lang_code)

# Define final path
extracted_dataframe_path = "{}/results/{}/ParlaMint-{}-extracted-source-data-additional.csv".format(main_path, lang_code, lang_code)

translated_dataframe_path = "{}/results/{}/ParlaMint-{}-translated-additional.csv".format(main_path, lang_code, lang_code)

translated_tokenized_dataframe_path = "{}/results/{}/ParlaMint-{}-translated-tokenized-additional.csv".format(main_path,lang_code, lang_code)

final_dataframe = "{}/results/{}/ParlaMint-{}-final-dataframe-additional.csv".format(main_path,lang_code, lang_code)

# Extract a list with paths to conllu files and a list with their names
parl_list = []
file_name_list = []

for dir1 in os.listdir(path):
    full_path = os.path.join(path, dir1)
    if os.path.isdir(full_path):
        current = os.listdir(full_path)
        # Keep only files with parliamentary sessions:
        for file in current:
            if "ParlaMint-{}_".format(lang_code) in file:
                if ".conllu" in file:
                    final_path = "{}/{}".format(full_path, file)
                    parl_list.append(final_path)
                    file_name_list.append(file)

# See how many files we have:
print("No. of files: {}.".format(len(parl_list)))


# Get notified once the code ends
webhook_url = open("/home/tajak/Parlamint-translation/discord_key.txt", "r").read()

@discord_sender(webhook_url=webhook_url)
def conllu_to_df(parl_list, file_name_list, extracted_dataframe_path):
	"""
	Take the conllu files and extract relevant information. Save everything in a DataFrame.

	Args:
	- parl_list: list of documents with their entire paths to be included (see step above).
	- file_name_list: list of names of the files (see step above)
	- extracted_dataframe_path: path to the output file
	"""
	from conllu import parse
	import pandas as pd

	# Create an empty df
	df = pd.DataFrame({"file_path": [""],"file": [""], "sentence_id": [""], "text": [""], "tokenized_text": [""], "proper_nouns": [""]})

	# Check whether there are any problems with parsing the documents
	"""
	
	error_count = 0
	problematic_doc_list = []

	for doc in parl_list:
		try:
			# Open the file
			data = open("{}".format(doc), "r").read()

			sentences = parse(data)
		except:
			error_count += 1
			problematic_doc_list.append(doc)

	print(error_count)
	print(problematic_doc_list)
	"""
	# Parse the data with CONLL-u parser
	for doc in parl_list:
		# Open the file
		data = open("{}".format(doc), "r").read()
		
		sentences = parse(data)

		sentence_id_list = []
		text_list = []
		tokenized_text_list = []
		proper_noun_list = []

		for sentence in sentences:
			# Find sentence ids
			current_sentence_id = sentence.metadata["sent_id"]
			sentence_id_list.append(current_sentence_id)

			# Find text - if texts consists of multiword tokens, these tokens will appear as they are,
			# not separated into subwords
			current_text = sentence.metadata["text"]
			text_list.append(current_text)

			# Create a string out of tokens
			current_token_list = []
			word_dict = {}

			for token in sentence:
				# Find multiword tokens and take their NER
				if type(token["id"]) != int:
					multiword_ner = token["misc"]["NER"]
				
				else:
				# Append to the tokenized text tokens that are not multiword tokens
				# (we append subtokens to the tokenized texts, not multiword tokens)
					current_token_list.append(token["form"])
					

					# Create a list of NE annotations with word indices.
					# I'll substract one from the word index,
					# because indexing in the CONLLU file starts with 1, not 0
					current_index = int(token["id"]) - 1

					# If the word does not have NER annotation,
					# take the annotation from the multiword token
					if token["misc"] is None:
						current_ner = multiword_ner
					else:
						current_ner = token["misc"]["NER"]

					# Add information on the lemma if the NE is personal name
					if "PER" in current_ner:
						word_dict[current_index] = [token["form"], token["lemma"]]

			proper_noun_list.append(word_dict)

			current_string = " ".join(current_token_list)

			tokenized_text_list.append(current_string)

		
		new_df = pd.DataFrame({"sentence_id": sentence_id_list, "text": text_list, "tokenized_text": tokenized_text_list, "proper_nouns": proper_noun_list})

		new_df["file_path"] = doc

		# Get the file name
		file_name = file_name_list[parl_list.index(doc)]
		new_df["file"] = file_name

		# Merge df to the previous df
		df = pd.concat([df, new_df])
	
	# Reset index
	df = df.reset_index(drop=True)

	# Remove the first row
	df = df.drop([0], axis="index")

	# Reset index
	df = df.reset_index(drop=True)

	# Add information on length
	df["length"] = df["text"].str.split().str.len()

	print("Number of words in the corpora: {}".format(df["length"].sum()))

	# Save the dataframe
	df.to_csv("{}".format(extracted_dataframe_path), sep="\t")

	print("Dataframe saved as {}".format(extracted_dataframe_path))
	
	# Show the results
	print(df.describe(include="all").to_markdown())

	print("\n\n\n")

	print(df.head().to_markdown())

	print("\n\n\n")
	
	return df

#Extract information from the conllu files
df = conllu_to_df(parl_list, file_name_list, extracted_dataframe_path)


# Get notified once the code ends
@discord_sender(webhook_url=webhook_url)
def translate(lang_code, opus_lang_code, extracted_dataframe_path, translated_dataframe_path):
	"""
	This function translates the text from the dataframe, created with the extract_text() function
	with OPUS-MT models using EasyNMT. It returns a dataframe with the translation.

	Args:
	- opus_lang_code: the lang code to be used in the OPUS-MT model - use the one that performed the best in the comparison (see function choose_model())
	"""
	import pandas as pd
	import numpy as np
	import regex as re
	from easynmt import EasyNMT
	from IPython.display import display
	import time

	# Open the file, created in the previous step
	df = pd.read_csv("{}".format(extracted_dataframe_path), sep="\t", index_col=0, na_filter = False)

	# Define the model
	model = EasyNMT('opus-mt')

	print("Entire corpus has {} sentences and {} words.".format(df["text"].count(), df["length"].sum()))

	# Create a list of sentences from the df
	sentence_list = df.text.to_list()

	print("Translation started.")

	start_time = time.time()

	#Translate the list of sentences - you need to provide the source language as it is in the name of the model - the opus_lang_code
	#for opus_lang_code in lang_models_dict[lang_code]:
	translation_list = model.translate(sentence_list, source_lang = "{}".format(opus_lang_code), target_lang='en')

	translation_time = round((time.time() - start_time)/60,2)

	print("Translation completed. It took {} minutes for {} instances - {} minutes per one sentence.".format(translation_time, len(sentence_list), translation_time/len(sentence_list)))

	# Add the translations to the df
	df["translation"] = translation_list

	#translation shortening of long MT repetition errors: if len (words) of EN sentence is more than 4X len (words) of original sentence, shorten the EN sentence to length 4X original sentence (to the nearest word) - applicable only if len of translation is longer than 6 words (to avoid cases where a couple of words in source language would be translated with a longer sequences in English that are still correct)

	# Add translation length
	df["tran_length"] = df["translation"].str.split().str.len()

	# Add info where tran length is more than 3 times longer than original length
	df["shorten"] = np.where((df["tran_length"] > 6) & (df["tran_length"] > 4*df["length"]), df["translation"], "no")

	# Shorten translations and substitute the longer translations with them
	shorten_translation = []

	for i in list(zip(df["translation"], df["shorten"], df["length"])):
		if i[1] == "no":
			shorten_translation.append(i[0])
		else:
			new_length = 4*i[2]
			# Shorten too long translations to the length of four times the length of the original sentence
			new_translation_list = i[0].split()[:new_length]
			new_translation = " ".join(new_translation_list)
			shorten_translation.append(new_translation)

	# Substitute previous translations with the new list
	df["translation"] = shorten_translation

	# Drop the "shorten" and "tran length" columns
	df = df.drop(columns=["shorten", "tran_length"])

	# Display the df
	print(df[:3].to_markdown())

	print("\n\n\n")

	# Save the df
	df.to_csv("{}".format(translated_dataframe_path), sep="\t")

	print("The file is saved as {}".format(translated_dataframe_path))

	return df

df = translate(lang_code, opus_lang_code, extracted_dataframe_path, translated_dataframe_path)

# Get notified once the code ends

@discord_sender(webhook_url=webhook_url)
def tokenize_translation(translated_dataframe_path, translated_tokenized_dataframe_path):
	import stanza
	import time
	import gc
	import torch
	from stanza.pipeline.core import DownloadMethod
	
	print("Tokenization of the translation started.")

	nlp = stanza.Pipeline(lang='en', processors='tokenize', tokenize_no_ssplit = True, download_method=DownloadMethod.REUSE_RESOURCES, use_gpu=True)

	# Apply tokenization to English translation and add the sentences to the df
	# Open the df
	df = pd.read_csv("{}".format(translated_dataframe_path), sep="\t", index_col = 0, na_filter = False)

	# Save also the information on whether there is a space after or before punctuation
	# which we will need later, to remove unnecessary spaces
	En_sentences = df.translation.to_list()

	tokenized_sentences = []
	space_after_list = []

	start_time = time.time()

	for i in En_sentences:
		doc = nlp(i).to_dict()
		current_sentence_list = []
		current_space_after_list = []

		# Define a list of start_char and end_char
		start_chars = []
		end_chars = []

		# Loop through the tokens in the sentence and add them to a current sentence list
		for sentence in doc:
			for word in sentence:
				current_sentence_list.append(word["text"])

				# Add information on start and end chars to the list
				start_chars.append(word["start_char"])
				end_chars.append(word["end_char"])
			
		# Now loop through the start_char and end_char lists and find instances
		# where the end_char of one word is the same as the start_char of the next one
		# this means there is no space between them
		for char_index in range(len(start_chars)-1):
			if end_chars[char_index] == start_chars[(char_index+1)]:
				current_space_after_list.append("No")
			else:
				current_space_after_list.append("Yes")
	
		# This loop is not possible for the end token, so let's add information for the last token
		# just to avoid errors due to different lengths of lists
		current_space_after_list.append("Last")

		# Join the list into a space-separated string
		current_string = " ".join(current_sentence_list)

		tokenized_sentences.append(current_string)

		space_after_list.append(current_space_after_list)

	# Add the result to the df
	df["translation-tokenized"] = tokenized_sentences
	df["space-after-information"] = space_after_list

	# Save the df
	df.to_csv("{}".format(translated_tokenized_dataframe_path), sep="\t")

	end_time = round((time.time() - start_time)/60,2)

	print("Tokenization completed. It took {} minutes.".format(end_time))

	#Delete nlp element, clean memory
	del nlp
	torch.cuda.empty_cache()
	gc.collect()
	torch.cuda.empty_cache()

	print("File saved as {}".format(translated_tokenized_dataframe_path))
	
	return df

# Create a dictionary from the returned alignment files which will be added to each word in the final conllu

def alignment_file_to_target_dict(file):
	"""
	The output of the eflomal aligner is in the source to target direction. We want to get the alignments in the other direction
	and for each target word add to the conllu its aligned source word index (as it appears in conllu). In conllu, indices start
	with 1, not 0. So, we take the eflomal files, reverse the order and create dictionaries with target indexes as keys
	and source indexes as values. If there are more than one words aligned to the same target word, it looks like this: '1, 2'.
	We use the conllu indexes which means that we add 1 to each index in the alingment pairs. 

	Args:
		- file: the path to the .fwd and .rev file that is produced by the eflomal tool

	The result is a list of dictionaries, each dictionary corresponds to one sentence.
	"""
	# Create target alignments from the source alignment direction (by changing the direction in the file)
	aligns_list_target = open(file, "r").readlines()
	aligns_list_target = [i.replace("\n", "") for i in aligns_list_target]
	aligns_list_target = [i.split(" ") for i in aligns_list_target]

	aligns_list_target_dict_list = []

	# Loop through the alignments for sentences
	for i in aligns_list_target:
		# Create a dictionary for each sentence
		current_sentence_align = {}
		# If alignment line is empty, keep the dictionary empty
		if len(i) == 1 and len(i[0]) == 0:
			current_sentence_align = {}
		else:
			# For each alignment pair in the sentence:
			for pair in i:
				# Split the pair: result is a list of lists with source index as the first element
				# and target index as the second element: [[0,0], [1,2], [1,3]]
				current_pair = pair.split("-")

				# Get the indices for target and source and add 1 to them (to get the conllu indices)
				current_t_index = int(current_pair[1]) + 1
				current_s_index = int(current_pair[0]) + 1

				# Check whether the target index is already aligned to anything (a case of 1-to-many alignment),
				# if not, save it as a key and save the source index as value.
				if current_sentence_align.get(current_t_index, None) == None:
					current_sentence_align[current_t_index] = str(current_s_index)
				# If the index was already aligned to a previous source word, add the additional source word alignment as a string
				# (result: {0: "1, 2"))
				else:
					current_sentence_align[current_t_index] += str(", ")
					current_sentence_align[current_t_index] += str(current_s_index)

		aligns_list_target_dict_list.append(current_sentence_align)

	return aligns_list_target_dict_list

@discord_sender(webhook_url=webhook_url)
def correct_proper_nouns(translated_tokenized_dataframe_path, final_dataframe, lang_code):
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

	In case you don't have sudo permission, you can skip !sudo make install. I did, and I also used a virtual environment (venv), and managed to install eflomal.

	"""
	import pandas as pd
	import re
	import ast
	from IPython.display import display
	import time
	import subprocess
	import os

	# Open the file, created in the previous step
	df = pd.read_csv("{}".format(translated_tokenized_dataframe_path), sep="\t", index_col=0, na_filter = False)

	# Move into the eflomal folder
	os.chdir("/home/tajak/Parlamint-translation/eflomal")

	# Create a prior file from alignments, created on the big file, to align the sentences based on them

	# First, we need to create a fasttext format from the two sentence files
	subprocess.call(["/home/tajak/Parlamint-translation/create_aligned_prior_file.sh", lang_code])

	# Now, create the prior file
	subprocess.call(["/home/tajak/Parlamint-translation/make_prior.sh", lang_code])

	# Then we need to create files for all texts and all translations
	source_sentences = open("source_sentences_{}_add.txt".format(lang_code), "w")
	English_sentences = open("English_sentences_{}_add.txt".format(lang_code), "w")

	for i in df["tokenized_text"].to_list():
		source_sentences.write(i)
		source_sentences.write("\n")

	for i in df["translation-tokenized"].to_list():
		English_sentences.write(i)
		English_sentences.write("\n")

	source_sentences.close()
	English_sentences.close()

	print("\n\n")
	print("Alignment started.")
	start_time = time.time()

	# Align sentences with eflomal and get out a file with alignments based on the prior
	subprocess.call(["/home/tajak/Parlamint-translation/align_with_prior.sh", lang_code])
	
	# Create a list of dictionaries of alignments from the returned files which will be added to the final conllu for each word
	forward_alignment_dict_list = alignment_file_to_target_dict("source-en-{}-add-file.fwd".format(lang_code))
	backward_alignment_dict_list = alignment_file_to_target_dict("source-en-{}-add-file.rev".format(lang_code))

	# Add to the df
	df["fwd_align_dict"] = forward_alignment_dict_list
	df["bwd_align_dict"] = backward_alignment_dict_list

	# Create forward target alignments from the source alignment direction (by changing the direction in the rev file)
	aligns_list = open("source-en-{}-add-file.rev".format(lang_code), "r").readlines()
	aligns_list = [i.replace("\n", "") for i in aligns_list]

	# Continue with processing the list to create the final alignments format which I'll use to correct proper names
	aligns_list = [i.split(" ") for i in aligns_list]

	for i in aligns_list:
		# If alignment line is empty, keep the dictionary empty
		if len(i) == 1 and len(i[0]) == 0:
			aligns_list[aligns_list.index(i)] = []
		else:
			for pair in i:
				current_pair = pair.split("-")
				i[i.index(pair)] = {int(current_pair[0]): int(current_pair[1])}
	
	final_aligns = []

	# Create a dictionary out of the rev alignments
	for i in aligns_list:
		current_line = {}

		try:
			for element in i:
				a = list(element.items())[0][0]
				b = list(element.items())[0][1]
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
		
	print("\nNumber of aligned sentences: {}\n\n".format(len(final_aligns)))

	# Add a to the df
	df["alignments"] = final_aligns

	# When we open the dataframe file, the dictionaries with proper names changed into strings - Change strings in the column proper_nouns into dictionaries

	df["proper_nouns"] = df.proper_nouns.astype("str")
	df["proper_nouns"] = df.proper_nouns.apply(lambda x: ast.literal_eval(x))

	# Change nan values in the proper_nouns columns
	df = df.fillna(0)

	# Substitute words in the translation based on alignments
	intermediate_list = list(zip(df["translation-tokenized"], df["proper_nouns"], df["alignments"]))

	new_translations = []
	substituted_all_info = []
	substituted_only = []
	substituted_words = []

	# Add information whether an error occurred
	error_list = []

	for i in intermediate_list:
		current_substituted_list = []
		current_substituted_only = []
		current_substituted_words = {}
		current_error = "No"

		# If no proper names were detected, do not change the translation
		if i[1] == 0:
			new_translations.append(i[0])
		
		else:
			current_translation = i[0]

			# Substitute the word with the source lemma based on the index - loop through the proper nouns to be changed
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

						# Save information on which word was substituted with its conllu index (index + 1) as the key
						current_substituted_words[int(substituted_word_index+1)] = word_list[substituted_word_index]

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
		if len(substituted_all_info) != 0:
			substituted_all_info.append(current_substituted_list)
		else:
			substituted_all_info.append(0)

		if len(current_substituted_only) != 0:
			substituted_only.append(current_substituted_only)
		else:
			substituted_only.append(0)

		error_list.append(current_error)

		substituted_words.append(current_substituted_words)


	# Add to the df
	df["new_translations"] = new_translations
	df["substitution_info"] = substituted_all_info
	df["substituted_pairs"] = substituted_only
	df["substituted_words"] = substituted_words
	df["errors"] = error_list

	end_time = round((time.time() - start_time)/60,2)

	print("Alignment completed. It took {} minutes.".format(end_time))

	# Change the working directory once again
	os.chdir("..")

	# Add the word list with indices to the df
	tokenized_text_list = df.tokenized_text.to_list()
	tokenized_text_list = [i.split(" ") for i in tokenized_text_list]
	tokenized_text_dict_list = []

	for sentence in tokenized_text_list:
		sentence_list = []
		counter = 1
		for word in sentence:
			sentence_list.append([word, counter])
			counter += 1
		tokenized_text_dict_list.append(sentence_list)

	df["source_indices"] = tokenized_text_dict_list

	# Save the df
	df.to_csv("{}".format(final_dataframe), sep="\t")

	# Display most common substitutions
	df_substituted = df[df["proper_nouns"] != "0"]
	print(df_substituted.substituted_pairs.value_counts()[:20].to_markdown())
	print("\n\n")

	return df

df = tokenize_translation(translated_dataframe_path, translated_tokenized_dataframe_path)

print(df.head(3).to_markdown())
print("\n\n")

df = correct_proper_nouns(translated_tokenized_dataframe_path, final_dataframe, lang_code)

# See if there were any errors in word substitution
print("Number of errors:")
print(df[df["errors"]!="No"].shape)
print("\n\n")

# See example of sentences with substituted words
print("Example of sentences with substituted words.")
print(df[df["substituted_pairs"]!= 0][:2].to_markdown())

# If the analysis of most common substitutions for this language revealed that it is better not to do the substitutions:
#		- save the translations without the substitutions as the "new-translations" in the final file (in analyse_results.ipynb)

if lang_code in ["BG", "PT", "IT", "AT", "GR", "HU", "NO", "TR", "NL", "SI", "HR", "RS", "LV", "UA", "ES-GA", "PL", "ES-CT", "FR", "BE-nl", "BE-fr", "EE", "ES"]:
	df = pd.read_csv(final_dataframe, sep="\t", index_col = 0, na_filter = False)

	# I will substitute the new_translations with the original ones and use the original translations in the next steps.
	df["post-processed_translations"] = df["new_translations"]

	df["new_translations"] = df["translation-tokenized"]

	# Save the new df
	df.to_csv("{}".format(final_dataframe), sep="\t")

	print("NER substitution disabled and original translations are used.")

	# Show differences between translations that we will use and translations after post-processing
	with pd.option_context('display.max_colwidth', None):
		print(df[df["substituted_pairs"] !="0"][['text','new_translations', 'post-processed_translations']].tail(20).to_markdown())

def create_conllu(file, lang_code, main_path, final_dataframe, nlp):
	"""
	The function takes the dataframe (df), created in previous steps and takes only the instances from the df that belong
	to the file that is in the argument. It linguistically processes the translated sentences from the file and saves the file.
	Then we add additional information (metadata and NER annotations) to it with the conllu parser and save the final conllu file.

	Args:
		- file (str): file name from the files list (see above)
		- lang_code (str): the lang code that is used in the names of the files, it should be the same as for extract_text()
	"""

	# Process all sentences in the dataframe and save them to a conllu file
	from stanza.utils.conll import CoNLL
	import stanza
	from conllu import parse
	import ast
	import regex as re
	import os
	import pandas as pd

	# Use the dataframe, created in previous steps
	df = pd.read_csv("{}".format(final_dataframe), sep="\t", index_col = 0, na_filter = False)

	# Filter out only instances from the file in question
	df = df[df["file"] == file]

	# Add information on the target path
	df["target_path"] = df.file_path.str.replace("Source-data", "Final-data")

	# Get target path
	target_path = list(df.target_path.unique())[0]

	# When we open the dataframe file, the lists and dictionaries turn into strings - change them back
	for column in ["space-after-information", 'fwd_align_dict', 'bwd_align_dict', 'substituted_words', "source_indices"]:
		df[column] = df[column].astype("str")
		df[column] = df[column].apply(lambda x: ast.literal_eval(x))

	# Create lists of information that we need to add to the conllu file
	ids_list = df.sentence_id.to_list()
	source_text = df.text.to_list()
	# initial_translation = df.translation.to_list()
	space_after_list = df["space-after-information"].to_list()
	fwd_align_list = df['fwd_align_dict'].to_list()
	bwd_align_list = df['bwd_align_dict'].to_list()
	substituted_words_list = df['substituted_words'].to_list()
	# tokenized_text_list = df["source_indices"].to_list()
	sentence_list = df.new_translations.to_list()

	# To feed the entire list into the pipeline, we need to create lists of tokens, split by space
	sentence_list = [x.split(" ") for x in sentence_list]
	
	# Linguistically process the list
	doc = nlp(sentence_list)

	# Save the conllu file
	CoNLL.write_doc2conll(doc, "{}/results/{}/temp/{}".format(main_path, lang_code, file))

	print("{} processed and saved.".format(file))

	# Open the CONLL-u file with the CONLL-u parser

	data = open("{}/results/{}/temp/{}".format(main_path, lang_code, file), "r").read()

	sentences = parse(data)

	# Adding additional information to the conllu
	for sentence in sentences:
		# Get the sentence index
		sentence_index = sentences.index(sentence)

		# Add metadata
		sentence.metadata["sent_id"] = ids_list[sentence_index]
		sentence.metadata["source"] = source_text[sentence_index]
		# sentence.metadata["source_indices"] = tokenized_text_list[sentence_index]
		# sentence.metadata["initial_translation"] = initial_translation[sentence_index]

		# Delete the current metadata for text
		del sentence.metadata["text"]

		new_translation_text = ""

		# Iterate through tokens
		for word in sentence:
			word_index = sentence.index(word)
			word_conllu_index = word["id"]

			# Check whether the word conllu index (word id) is in the substituted_words_list (it is if it was substituted)
			# If it is, add information on the original translated word - do not do this for Bulgarian, Portuguese and other languages mentioned
			if lang_code not in ["BG", "PT", "IT", "AT", "GR", "HU", "NO", "TR", "NL", "SI", "HR", "RS", "LV", "UA", "ES-GA", "PL", "ES-CT", "FR", "BE-nl", "BE-fr", "EE", "ES"]:
				if substituted_words_list[sentence_index].get(word_conllu_index, None) != None:
					word["misc"]["Translated"] = substituted_words_list[sentence_index][word_conllu_index]
			
			# Do the same for the forward and backward alignment
			if fwd_align_list[sentence_index].get(word_conllu_index, None) != None:
				word["misc"]["ForwardAlignment"] = fwd_align_list[sentence_index][word_conllu_index]

			if bwd_align_list[sentence_index].get(word_conllu_index, None) != None:
				word["misc"]["BackwardAlignment"] = bwd_align_list[sentence_index][word_conllu_index]

			# Remove information on start_char and end_char from the annotation
			del word["misc"]["start_char"]
			del word["misc"]["end_char"]
			
			# Change the NER tags so that they are the same as in the source
			current_ner = word["misc"]["ner"]
			del word["misc"]["ner"]
			
			# Substitute parts of the tags so that they are the same as in source
			current_ner = re.sub("S-", "B-", current_ner)
			current_ner = re.sub("E-", "I-", current_ner)

			word["misc"]["NER"] = current_ner

			try:
				# Get information about the space after based on the index
				current_space_after = space_after_list[sentence_index][word_index]
			except:
				print("Error based on current_space after in sentence {}, sentence index: {}, word {}, word index {}.".format(sentence, sentence_index, word, word_index))
				current_space_after = "Yes"

		# Create new text from translation, correcting the spaces around words
		# based on the SpaceAfter information
			if current_space_after == "No":
				word["misc"]["SpaceAfter"] = "No"
				new_translation_text += word["form"]
			elif current_space_after == "Last":
				new_translation_text += word["form"]
			else:
				new_translation_text += word["form"]
				new_translation_text += " "
		
		sentence.metadata["text"] = new_translation_text
	
	# Create a new conllu file with the updated information
	os.makedirs(os.path.dirname(target_path), exist_ok=True)
	final_file = open("{}".format(target_path), "w")

	for sentence in sentences:
		final_file.write(sentence.serialize())
	
	final_file.close()

	print("Final file {} is saved.".format(target_path))

# Get notified once the code ends
@discord_sender(webhook_url=webhook_url)
def produce_final_conllu(lang_code, final_dataframe):
	import pandas as pd
	import stanza
	import time
	from stanza.pipeline.core import DownloadMethod
	
	df = pd.read_csv("{}".format(final_dataframe), sep="\t", index_col=0, na_filter = False)

	# Create a list of files
	files = list(df.file.unique())
	
	start_time = time.time()

	print("Processing started.")

	# Define the pipeline, instruct it to use a specific package: 	CoNLL03
	nlp = stanza.Pipeline(lang='en', processors="tokenize,mwt,pos,lemma,ner", package={"ner": ["conll03"]}, tokenize_pretokenized=True, download_method=DownloadMethod.REUSE_RESOURCES, use_gpu=True)

	for file in files:
		create_conllu(file, lang_code, main_path, final_dataframe, nlp)
		current_end_time = round((time.time() - start_time)/60,2)
		print("Current running time: {}".format(current_end_time))
	
	end_time = round((time.time() - start_time)/60,2)

	print("Processing completed. It took {} minutes.".format(end_time))


produce_final_conllu(lang_code, final_dataframe)