# Define the language code, used in the file names
lang_code = "CZ"

# Main path
main_path = "/home/tajak/Parlamint-translation"

# --------------------NO CHANGING OF THE CODE NEEDED FROM NOW ONWARDS------------------
import pandas as pd

translated_dataframe_path = "{}/results/{}/ParlaMint-{}-translated.csv".format(main_path, lang_code, lang_code)
translated_tokenized_dataframe_path = "{}/results/{}/ParlaMint-{}-translated-tokenized.csv".format(main_path,lang_code, lang_code)
final_dataframe = "{}/results/{}/ParlaMint-{}-final-dataframe.csv".format(main_path,lang_code, lang_code)


def tokenize_translation(translated_dataframe_path, translated_tokenized_dataframe_path):
	import stanza
	import time
	import gc
	import torch
	
	print("Tokenization of the translation started.")

	nlp = stanza.Pipeline(lang='en', processors='tokenize', tokenize_no_ssplit = True)

	# Apply tokenization to English translation and add the sentences to the df
	# Open the df
	df = pd.read_csv("{}".format(translated_dataframe_path), sep="\t", index_col = 0)

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

def correct_proper_nouns(translated_tokenized_dataframe_path, final_dataframe):
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
	df = pd.read_csv("{}".format(translated_tokenized_dataframe_path), sep="\t", index_col=0)

	# Move into the eflomal folder
	os.chdir("/home/tajak/Parlamint-translation/eflomal")

	# Then we need to create files for all texts and all translations
	source_sentences = open("source_sentences.txt", "w")
	English_sentences = open("English_sentences.txt", "w")

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
	
	# Align sentences with eflomal and get out a file with alignments
	#!python3 align.py -s source_sentences.txt -t English_sentences.txt --model 3 -r source-en.rev -f source-en.fwd
	subprocess.call("/home/tajak/Parlamint-translation/align.sh")

	# Create a list of dictionaries of alignments from the returned files which will be added to the final conllu for each word
	forward_alignment_dict_list = alignment_file_to_target_dict("source-en.fwd")
	backward_alignment_dict_list = alignment_file_to_target_dict("source-en.rev")

	# Add to the df
	df["fwd_align_dict"] = forward_alignment_dict_list
	df["bwd_align_dict"] = backward_alignment_dict_list

	# Create forward target alignments from the source alignment direction (by changing the direction in the rev file)
	aligns_list = open("source-en.rev", "r").readlines()
	aligns_list = [i.replace("\n", "") for i in aligns_list]

	# Continue with processing the list to create the final alignments format which I'll use to correct proper names
	aligns_list = [i.split(" ") for i in aligns_list]

	for i in aligns_list:
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

	# Remove the rev and fwd file
	os.remove("source-en.rev")
	os.remove("source-en.fwd")

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

df = correct_proper_nouns(translated_tokenized_dataframe_path, final_dataframe)

# See if there were any errors in word substitution
print("Number of errors:")
print(df[df["errors"]!="No"].shape)
print("\n\n")

# See example of sentences with substituted words
print("Example of sentences with substituted words.")
print(df[df["substituted_pairs"]!= 0][:2].to_markdown())