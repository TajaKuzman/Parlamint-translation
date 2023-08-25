import argparse

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

# Define other paths
extracted_dataframe_path = "{}/results/{}/ParlaMint-{}-extracted-source-data.csv".format(main_path, lang_code, lang_code)

translated_dataframe_path = "{}/results/{}/ParlaMint-{}-translated.csv".format(main_path, lang_code, lang_code)

# -------------NO CHANGING OF THE CODE NEEDED FROM NOW ONWARDS------------------
from knockknock import discord_sender

# Get notified once the code ends
webhook_url = open("/home/tajak/Parlamint-translation/discord_key.txt", "r").read()
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