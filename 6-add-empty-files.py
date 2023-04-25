import argparse
import pandas as pd
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("lang_code", help="lang code used in the files")
    args = parser.parse_args()

# Define the language code, used in the file names
#lang_code = "CZ"
lang_code = args.lang_code

# Main path
main_path = "/home/tajak/Parlamint-translation"

path = "{}/Source-data/ParlaMint-{}.conllu/ParlaMint-{}.conllu".format(main_path, lang_code, lang_code)

if lang_code != "BE":
    final_dataframe = "{}/results/{}/ParlaMint-{}-final-dataframe.csv".format(main_path,lang_code, lang_code)
else:
    final_dataframe = "{}/results/{}/ParlaMint-{}-extracted-source-data.csv".format(main_path, lang_code, lang_code)

df = pd.read_csv(final_dataframe, sep="\t", index_col = 0, na_filter = False)

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

print("Instances of the lists of source files:\n")
print(parl_list[:2])
print(file_name_list[:2])

# See how many files we have:
print("Number of files in the source folder: {}".format(len(parl_list)))

missing_files = []

# Inspect which file is not in the final dataframe, print it and print its length (check if it is empty)
for i in file_name_list:
    if i not in list(df.file.unique()):
        file = open(parl_list[file_name_list.index(i)], "r").read()
        # Print file length to check that it is empty:
        print("Missing file length: {}". format(len(file.split())))
        # Add the full path of this file to the missing_files list
        missing_files.append(parl_list[file_name_list.index(i)])

# Print the number of missing files
print("Number of missing files: {}".format(len(missing_files)))

missing_files_target = []

# Change the source path to target path for these files
for x in missing_files:
    new_x = x.replace("Source-data", "Final-data")
    missing_files_target.append(new_x)
#missing_files_target = [x.replace("Source-data", "Final-data") for x in missing_files]

# Print instance of this:
print("Changes paths in the missing file list: {}". format(missing_files_target[:3]))


# For each file in the missing_files list, save it in the final files folder
for i in list(zip(missing_files, missing_files_target)):
    source_path = i[0]
    target_path = i[1]
    file = open(source_path, "r").read()
    target_file = open(target_path, "w")
    target_file.write(file)
    target_file.close()
    print("File {} saved as {}.".format(source_path, target_path))

print("Additional files saved to the the final folder.")