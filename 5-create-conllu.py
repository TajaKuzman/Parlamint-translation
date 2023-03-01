import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("lang_code", help="lang code used in the files")
    args = parser.parse_args()

# Define the language code, used in the file names
#lang_code = "CZ"
lang_code = args.lang_code

# Main path
main_path = "/home/tajak/Parlamint-translation"

# --------------------NO CHANGING OF THE CODE NEEDED FROM NOW ONWARDS------------------
final_dataframe = "{}/results/{}/ParlaMint-{}-final-dataframe.csv".format(main_path,lang_code, lang_code)

from knockknock import discord_sender

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
			# If it is, add information on the original translated word - do not do this for Bulgarian and Portuguese
			if lang_code not in ["BG", "PT", "IT", "AT", "GR", "HU", "NO", "TR"]:
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
webhook_url = "https://discord.com/api/webhooks/1078298985346899989/sq3rnJdR91A-0175s4Sb-pdfStNC5dOxivuIjMm_8apLIsn41yT89U-NGc-lKSeqqIAm"
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