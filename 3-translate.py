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

# Define other paths
extracted_dataframe_path = "{}/results/{}/ParlaMint-{}-extracted-source-data.csv".format(main_path, lang_code, lang_code)

translated_dataframe_path = "{}/results/{}/ParlaMint-{}-translated.csv".format(main_path, lang_code, lang_code)

# -------------NO CHANGING OF THE CODE NEEDED FROM NOW ONWARDS------------------

def translate(lang_code, extracted_dataframe_path, translated_dataframe_path):
	"""
	This function translates the text from the dataframe, created with the extract_text() function
	with OPUS-MT models using EasyNMT. It returns a dataframe with the translation.

	Args:
	- opus_lang_code: the lang code to be used in the OPUS-MT model - use the one that performed the best in the comparison (see function choose_model())
	"""
	import pandas as pd
	import regex as re
	from easynmt import EasyNMT
	from IPython.display import display
	import time

	# Open the file, created in the previous step
	df = pd.read_csv("{}".format(extracted_dataframe_path), sep="\t", index_col=0)

	# Define the model
	model = EasyNMT('opus-mt')

	print("Entire corpus has {} sentences and {} words.".format(df["text"].count(), df["length"].sum()))

	# Create a list of sentences from the df
	sentence_list = df.text.to_list()

	lang_models_dict = {"BG": ["bg", "sla", "zls"], "HR": ["zls", "sla"], "CZ": ["cs", "sla", "zlw" ], "DK": ["da", "gmq", "gem"], "NL": ["nl", "gem", "gmw"], "FR": ["fr", "itc","roa"], "HU": ["hu", "fiu", "urj"], "IS": ["is","gmq", "gem"], "IT": ["it", "roa", "itc"], "LV": ["lv","bat"], "LT": ["bat"], "PL": ["pl", "sla", "zlw"], "SI": ["sla"], "ES": ["es", "roa", "itc"], "TR": ["tr", "trk" ], "AT": ["de", "gem", "gmw"], "ES-PV": ["eu", "mul"], "BA": ["sla", "zls"], "ES-CT": ["ca", "roa", "itc"], "EE": ["et", "urj", "fiu"], "FI": ["fi", "urj", "fiu"], "ES-GA": ["gl", "roa", "itc"], "GR": ["el","grk"], "NO": ["gem", "gmq"], "PT": ["pt", "roa", "itc"], "RO":["roa", "itc"], "RS": ["zls", "sla"], "SE": ["sv", "gmq", "gem"], "UA":["uk", "sla", "zle"]}

	print("Translation started.")

	start_time = time.time()

	#Translate the list of sentences - you need to provide the source language as it is in the name of the model - the opus_lang_code
	for opus_lang_code in lang_models_dict[lang_code]:
		translation_list = model.translate(sentence_list, source_lang = "{}".format(opus_lang_code), target_lang='en')

	translation_time = round((time.time() - start_time)/60,2)

	print("Translation completed. It took {} minutes for {} instances - {} minutes per one sentence.".format(translation_time, len(sentence_list), translation_time/len(sentence_list)))

	# Add the translations to the df
	df["translation"] = translation_list

	# Display the df
	print(df[:3].to_markdown())

	print("\n\n\n")

	# Save the df
	df.to_csv("{}".format(translated_dataframe_path), sep="\t")

	print("The file is saved as {}".format(translated_dataframe_path))

	return df

df = translate(lang_code, extracted_dataframe_path, translated_dataframe_path)