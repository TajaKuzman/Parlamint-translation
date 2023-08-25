import argparse
import regex as re
import pandas as pd
from bs4 import BeautifulSoup as bs
import os
from knockknock import discord_sender
from easynmt import EasyNMT
from IPython.display import display
import time
import csv
import numpy as np


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("lang_code", help="lang code used in the files")
    parser.add_argument("opus_lang_code", help="lang code used by the MT system")
    args = parser.parse_args()

# Define the language code, used in the file names
#lang_code = "CZ"
lang_code = args.lang_code
opus_lang_code = args.opus_lang_code

# Define the path to the Source TEI folder
path = "/home/tajak/Parlamint-translation/Note-translation/Source-data-TEI/ParlaMint-{}.TEI.ana".format(lang_code)

# Define final path
notes_path = "/home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-{}.notes.translated.ana.tsv".format(lang_code)

temp_path = "/home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/before-sorting/ParlaMint-{}.notes.translated-before-sorting.ana.csv".format(lang_code)


def extract_tag(tag, df, content):
	if tag in ["note", "head"]:
		# Extract all notes from the file
		note_list = content.find_all(tag)
		note_list_final = []

		for i in note_list:
			current_note = []
			type = ""

			if i.attrs.get('type', 'None') != "None":
			
			#if len(list(i.attrs.values())) == 1:
			#	current_note.append(list(i.attrs.values())[0])
			#elif len(list(i.attrs.values())) == 0:
			#	current_note.append("")
			#else:
			#	print("Error: there are more than 1 attribute!")
			#	print(i)

				type = i.get("type")

			elif i.attrs.get('reason', 'None') != "None":
				type = i.get("reason")
			
			else:
				type = ""

			if i.attrs.get("xml:lang", "None") != "None":
				lang = i.get("xml:lang")
			else:
				# If note does not have lang id, take the lang id of its parent
				lang = i.find_parent(attrs={"xml:lang":True}).attrs.get("xml:lang")
			
			current_note.append(type)
			current_note.append(i.get_text().strip())
			current_note.append(lang)
			note_list_final.append(current_note)
		
		new_df = pd.DataFrame({"type": [x[0] for x in note_list_final], "content": [x[1] for x in note_list_final], "xml:lang": [x[2] for x in note_list_final]})
		new_df["tag"] = tag

		# Merge df to the previous df
		df = pd.concat([df, new_df])
	
	else:
		# Extract all other notes from the file
		note_list = content.find_all(tag)
		note_list_final = []

		for i in note_list:
			desc_list = []
			type = ""
			if i.attrs.get('type', 'None') != "None":
				type = i.get("type")

			elif i.attrs.get('reason', 'None') != "None":
				type = i.get("reason")
			
			else:
				type = ""

			desc_list = i.find_all("desc")
			if len(desc_list) == 0:
				print("Error - empty desc_list")
				print(i)
			else:
				for desc in desc_list:
					current_note = []
					if "xml:lang" in list(desc.attrs.keys()):
						lang = desc.get("xml:lang")
					else:
						lang = i.find_parent(attrs={"xml:lang":True}).attrs.get("xml:lang")
					current_note.append(type)
					current_note.append(desc.get_text().strip())
					current_note.append(lang)
					note_list_final.append(current_note)
		
		new_df = pd.DataFrame({"type": [x[0] for x in note_list_final], "content": [x[1] for x in note_list_final], "xml:lang": [x[2] for x in note_list_final]})
		new_df["tag"] = tag

		# Merge df to the previous df
		df = pd.concat([df, new_df])

	return df

# Get notified once the code ends
webhook_url = open("/home/tajak/Parlamint-translation/discord_key.txt", "r").read()
@discord_sender(webhook_url=webhook_url)
def translate_notes(path, lang_code, opus_lang_code, notes_path, temp_path):

	start_time = time.time()
	print("Extraction of the notes and translation started.")

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
					if ".xml" in file:
						final_path = "{}/{}".format(full_path, file)
						parl_list.append(final_path)
						file_name_list.append(file)

	# See how many files we have:
	print("No. of files: {}.".format(len(parl_list)))


	# Create an empty df
	df = pd.DataFrame({"tag": [""],"type": [""], "content": [""], "xml:lang": [""]})

	# Go through all files in the list of files and extract notes from all of them
	for path in parl_list:
		file = open(path, "r")
		# Parse the file with beautifulsoup
		content = bs(file, "xml")

		# Extract all tags from the file
		for tag in ["note", "gap", "head", "kinesic", "vocal", "incident"]:
			df = extract_tag(tag, df, content)

	# At the end, edit the df by deleting the first (empty) row and reseting the index
	# Reset index
	df = df.reset_index(drop=True)

	# Remove the first row
	df = df.drop([0], axis="index")

	# Reset index
	df = df.reset_index(drop=True)

	print("Statistics before droping duplicates:\n\n\n")

	# Show the results
	print(df.describe(include="all").to_markdown())

	print("\n")

	print(df.head().to_markdown())

	print("\n")

	print("Statistics for tags:\n")

	print(df.tag.value_counts().to_markdown())

	print("\n")

	print(df.groupby("tag").type.value_counts().to_markdown())

	print("Most common notes:\n")

	print(df.content.value_counts()[:20].to_markdown())

	# Remove duplicated rows (exact duplicates - all values in all columns match)
	df = df.drop_duplicates()

	print("Statistics after deduplication:\n")

	# Add information on length
	df["length"] = df["content"].str.split().str.len()

	print("Number of words in the notes: {}\n".format(df["length"].sum()))

	print(df.describe(include="all").to_markdown())

	print("\n")

	print(df.head().to_markdown())

	print("\n")

	print("Statistics for tags:\n")

	print(df.tag.value_counts().to_markdown())

	print("\n")

	print(df.groupby("tag").type.value_counts().to_markdown())

	# Define the MT model
	model = EasyNMT('opus-mt')

	# Create a list of sentences from the df
	sentence_list = df.content.to_list()

	print("Translation started.")

	#Translate the list of sentences - you need to provide the source language as it is in the name of the model - the opus_lang_code
	#for opus_lang_code in lang_models_dict[lang_code]:
	translation_list = model.translate(sentence_list, source_lang = "{}".format(opus_lang_code), target_lang='en')

	translation_time = round((time.time() - start_time)/60,2)

	print("Translation completed. It took {} minutes for {} instances for the entire process of extraction and translation.".format(translation_time, len(sentence_list)))

	# Add the translations to the df
	df["translation"] = translation_list

	#translation shortening of long MT repetition errors: if len (words) of EN sentence is more than 4X len (words) of original sentence, shorten the EN sentence to length 4X original sentence (to the nearest word) - applicable only if len of translation is longer than 6 words (to avoid cases where a couple of words in source language would be translated with a longer sequences in English that are still correct)

	# Add translation length
	df["tran_length"] = df["translation"].str.split().str.len()

	# Add info where tran length is more than 4 times longer than original length
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

	# Add the country code to the df
	df["corpus"] = lang_code

	# Display the df
	print(df.head().to_markdown())

	print("\n\n\n")

	# Save the df
	df.to_csv("{}".format(temp_path), sep="\t", index=False)

	# Sort the values
	df = df.sort_values(by=["tag", "type"])

	# Save the final df
	df.to_csv("{}".format(notes_path), index=False, sep="\t", quoting=csv.QUOTE_NONE, quotechar="",  escapechar="\\")

	print("The file is saved as {}".format(notes_path))

	return df

df = translate_notes(path, lang_code, opus_lang_code, notes_path, temp_path)