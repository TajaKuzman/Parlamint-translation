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

# For experimentation, I will take 100 files so that we will see results more quickly

# --------------------NO CHANGING OF THE CODE NEEDED FROM NOW ONWARDS------------------

final_dataframe = "{}/results/{}/ParlaMint-{}-final-dataframe.csv".format(main_path,lang_code, lang_code)

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
	df = pd.read_csv("{}".format(final_dataframe), sep="\t", index_col = 0)

	# Filter out only instances from the file in question
	df = df[df["file"] == file]


	# When we open the dataframe file, the lists and dictionaries turn into strings - change them back
	for column in ["space-after-information", 'fwd_align_dict', 'bwd_align_dict', 'substituted_words', "source_indices"]:
		df[column] = df[column].astype("str")
		df[column] = df[column].apply(lambda x: ast.literal_eval(x))

	# tokenized_text_list = df["source_indices"].to_list()
	sentence_list = df.new_translations.to_list()

	# To feed the entire list into the pipeline, we need to create lists of tokens, split by space
	sentence_list = [x.split(" ") for x in sentence_list]
	
	# Linguistically process the list
	doc = nlp(sentence_list)

	# Save the conllu file
	#CoNLL.write_doc2conll(doc, "{}/results/{}/temp/{}".format(main_path, lang_code, file))

	#print("{} processed.".format(file))



def produce_final_conllu(lang_code, final_dataframe):
	import pandas as pd
	import stanza
	import time
	
	df = pd.read_csv("{}".format(final_dataframe), sep="\t", index_col=0)

	# Create a list of files
	files = list(df.file.unique())

	files = files[:10]
	
	start_time = time.time()

	print("Processing started.")

	# Define the pipeline, instruct it to use a specific package: 	CoNLL03
	nlp = stanza.Pipeline(lang='en', processors="tokenize,mwt,pos,lemma,ner", package={"ner": ["conll03"]}, tokenize_pretokenized=True)

	# We will go with batch_size=200 which seems to improve the processing.
	nlp = stanza.Pipeline(lang='en', processors="tokenize,mwt,pos,lemma,ner", mwt_batch_size=200, lemma_batch_size=200, package={"ner": ["conll03"]}, tokenize_pretokenized=True)

	# Test file
	#for file in ["ParlaMint-CZ_2013-11-25-ps2013-001-01-002-002.conllu"]:
	#	create_conllu(file, lang_code)

	for file in files:
		create_conllu(file, lang_code, main_path, final_dataframe, nlp)
	
	end_time = round((time.time() - start_time)/60,2)

	print("Lemma batch 200: processing completed. It took {} minutes for 10 files.".format(end_time))


produce_final_conllu(lang_code, final_dataframe)