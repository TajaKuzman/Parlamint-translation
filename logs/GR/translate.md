2023-02-22 10:01:26.881716: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-02-22 10:01:27.619054: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-02-22 10:01:27.619138: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-02-22 10:01:27.619146: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Entire corpus has 2816249 sentences and 49982785 words.
Translation started.
Translation completed. It took 1268.57 minutes for 2816249 instances - 0.00045044667570232603 minutes per one sentence.
|    | file_path                                                                                                                            | file                                      | sentence_id                               | text                                                                                                                        | tokenized_text                                                                                                                 | proper_nouns   |   length | translation                                                                                                                       |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------|:------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|:---------------|---------:|:----------------------------------------------------------------------------------------------------------------------------------|
|  0 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-GR.conllu/ParlaMint-GR.conllu/2017/ParlaMint-GR_2017-01-12-S1-commons.conllu | ParlaMint-GR_2017-01-12-S1-commons.conllu | ParlaMint-GR_2017-01-12-S1-commons.seg1.1 | Κυρίες και κύριοι συνάδελφοι, αρχίζει η συνεδρίαση.                                                                         | Κυρίες και κύριοι συνάδελφοι , αρχίζει η συνεδρίαση .                                                                          | {}             |        7 | Ladies and gentlemen, the meeting begins.                                                                                         |
|  1 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-GR.conllu/ParlaMint-GR.conllu/2017/ParlaMint-GR_2017-01-12-S1-commons.conllu | ParlaMint-GR_2017-01-12-S1-commons.conllu | ParlaMint-GR_2017-01-12-S1-commons.seg2.1 | Έχω την τιμή να ανακοινώσω στο Σώμα το δελτίο επικαίρων ερωτήσεων της Παρασκευής 13 Ιανουαρίου 2017, το οποίο έχει ως εξής: | Έχω την τιμή να ανακοινώσω σ το Σώμα το δελτίο επικαίρων ερωτήσεων της Παρασκευής 13 Ιανουαρίου 2017 , το οποίο έχει ως εξής : | {}             |       21 | I have the honour to inform the House of the topical and urgent question issue of Friday 13 January 2017, which reads as follows: |
|  2 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-GR.conllu/ParlaMint-GR.conllu/2017/ParlaMint-GR_2017-01-12-S1-commons.conllu | ParlaMint-GR_2017-01-12-S1-commons.conllu | ParlaMint-GR_2017-01-12-S1-commons.seg3.1 | Α. ΕΠΙΚΑΙΡΕΣ ΕΡΩΤΗΣΕΙΣ Πρώτου Κύκλου (άρθρο 130 παράγραφοι 2 και 3 του Κανονισμού της Βουλής)                               | Α. ΕΠΙΚΑΙΡΕΣ ΕΡΩΤΗΣΕΙΣ Πρώτου Κύκλου ( άρθρο 130 παράγραφοι 2 και 3 του Κανονισμού της Βουλής )                                | {}             |       15 | A. PERSONS First Circle Questions (Rule 130(2) and (3) of the Rules of Procedure)                                                 |




The file is saved as /home/tajak/Parlamint-translation/results/GR/ParlaMint-GR-translated.csv