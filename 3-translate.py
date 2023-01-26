from conllu import parse
import pandas as pd
from IPython.display import display
import os
import zipfile
import utils

# Define the language code, used in the file names
lang_code = "CZ"

# Define the translation model to be used
opus_lang_code = "cs"

# Main path
main_path = "/home/tajak/Parlamint-translation"


# Check whether the path to the folder with conllu files is ok
path = "{}/Source-data/ParlaMint-{}.conllu/ParlaMint-{}.conllu".format(main_path, lang_code, lang_code)

# Define other paths
extracted_dataframe_path = "{}/results/{}/ParlaMint-{}-extracted-source-data.csv".format(main_path, lang_code, lang_code)

translated_dataframe_path = "{}/results/{}/ParlaMint-{}-translated.csv".format(main_path, lang_code, lang_code)

def translate(lang_code, opus_lang_code, main_path):
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
	from IPython.display import display
	import time

	extracted_dataframe_path = "{}/results/{}/ParlaMint-{}-extracted-source-data.csv".format(main_path, lang_code, lang_code)

	translated_dataframe_path = "{}/results/{}/ParlaMint-{}-translated.csv".format(main_path, lang_code, lang_code)

	# Open the file, created in the previous step
	df = pd.read_csv("{}".format(extracted_dataframe_path), sep="\t", index_col=0)

	# Define the model
	model = EasyNMT('opus-mt')

	print("Entire corpus has {} sentences and {} words.".format(df["text"].count(), df["length"].sum()))

	# Create a list of sentences from the df
	sentence_list = df.text.to_list()

	print("Translation started.")

	start_time = time.time()

	#Translate the list of sentences - you need to provide the source language as it is in the name of the model - the opus_lang_code
	translation_list = model.translate(sentence_list, source_lang = "{}".format(opus_lang_code), target_lang='en')

	translation_time = round((time.time() - start_time)/60,2)

	print("Translation completed. It took {} minutes for {} instances - {} minutes per one sentence.".format(translation_time, len(sentence_list), translation_time/len(sentence_list)))

	# Add the translations to the df
	df["translation"] = translation_list

	# Display the df
	print(df[:3].to_markdown())

	# Save the df
	df.to_csv("{}".format(translated_dataframe_path), sep="\t")

	print("The file is saved as {}".format(translated_dataframe_path))

	return df

df = translate(lang_code, opus_lang_code, main_path)