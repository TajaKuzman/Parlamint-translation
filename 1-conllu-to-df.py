import os
import argparse
import zipfile
import gzip
import shutil

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("lang_code", help="lang code used in the files")
    args = parser.parse_args()

# Define the language code, used in the file names
#lang_code = "CZ"
lang_code = args.lang_code

# Unzip the ZIP folder with the files
#with zipfile.ZipFile("/home/tajak/Parlamint-translation/Source-data/ParlaMint-{}/ParlaMint-{}.conllu.zip".format(lang_code, lang_code), 'r') as zip_ref:
#    zip_ref.extractall("/home/tajak/Parlamint-translation/Source-data/ParlaMint-{}/ParlaMint-{}.conllu".format(lang_code, lang_code))

# Unzip the TGZ file: write to command line: `tar -xf dir_name`

# Main path
main_path = "/home/tajak/Parlamint-translation"

# Check in your directory whether the path to the folder with conllu files is ok:
path = "{}/Source-data/ParlaMint-{}.conllu/ParlaMint-{}.conllu".format(main_path, lang_code, lang_code)

# Create a folder with results for this language, e.g. results/CZ
os.mkdir("/home/tajak/Parlamint-translation/results/{}".format(lang_code))

# Create (manually) a "temp" folder inside the results/CZ
os.mkdir("/home/tajak/Parlamint-translation/results/{}/temp".format(lang_code))

# ------------NO CHANGING OF THE CODE NEEDED FROM NOW ONWARDS--------------

# Define final path
extracted_dataframe_path = "{}/results/{}/ParlaMint-{}-extracted-source-data.csv".format(main_path, lang_code, lang_code)

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
