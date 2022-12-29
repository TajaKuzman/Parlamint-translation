# Machine translating the Parlamint output

Tasks:
- extract data to be translated based on the Parlamint format
- use OPUSMT through EasyNMT/Hugging Face to machine translate the output
- use eftomal to get word alignments (train it with the MT output)
- assure that proper names are correctly translated based on the word alignments