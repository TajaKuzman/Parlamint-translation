import os

# Unzip the folder with the files
#with zipfile.ZipFile("/home/tajak/Parlamint-translation/ParlaMint-CZ/ParlaMint-CZ.conllu.zip", 'r') as zip_ref:
#    zip_ref.extractall("/home/tajak/Parlamint-translation/ParlaMint-CZ/ParlaMint-CZ.conllu")

# Define the language code, used in the file names
lang_code = "CZ"

# Main path
main_path = "/home/tajak/Parlamint-translation"

# Check in your directory whether the path to the folder with conllu files is ok:
path = "{}/Source-data/ParlaMint-{}.conllu/ParlaMint-{}.conllu".format(main_path, lang_code, lang_code)

# Create a folder with results for this language, e.g. results/CZ

# Create (manually) a "temp" folder inside the results/CZ

# Currently, the number of files to be processed is set to 5 - change this in the code (line 210) to process everything.

# --------------------NO CHANGING OF THE CODE NEEDED FROM NOW ONWARDS------------------

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
	from IPython.display import display
	from itertools import islice
	import math
	import numpy as np

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

	# Split the dataframe into 3 batches based on the list of files
	file_list = list(df.file.unique())

	def chunk(arr_range, arr_size):
		arr_range = iter(arr_range)
		return iter(lambda: tuple(islice(arr_range, arr_size)), ())

	batches_list = list(chunk(file_list, math.ceil(len(file_list)/3)))

	print("File is separated into {} batches, sizes of batches (in no. of files): {}, {}, {}.".format(len(batches_list), len(batches_list[0]), len(batches_list[1]), len(batches_list[2])))

	# Add information on the batch in the dataframe
	for i in range(len(batches_list)):
		if i==0:
			df["batch"] = np.where((df["file"].isin(list(batches_list[i]))), int(i+1), "none")
		else:
			df["batch"] = np.where((df["file"].isin(list(batches_list[i]))), int(i+1), df["batch"])

	# Save the dataframe
	df.to_csv("{}".format(extracted_dataframe_path), sep="\t")

	print("Dataframe saved as {}".format(extracted_dataframe_path))
	
	# Show the results
	print(df.describe(include="all").to_markdown())

	print("\n\n\n")

	print(df.head().to_markdown())

	print("\n\n\n")

	# Save each batch separately to be translated separately
	for i in list(df.batch.unique()):
		df[df["batch"] == i].to_csv("{}.{}.csv".format(extracted_dataframe_path, i), sep="\t")
		print("Batch {} saved as {}.{}.csv".format(i, extracted_dataframe_path, i))

	return df

#Extract information from the conllu files
df = conllu_to_df(parl_list[:20], file_name_list[:20], extracted_dataframe_path)