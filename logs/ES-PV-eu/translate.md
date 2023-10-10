2023-10-09 08:55:03.772239: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-10-09 08:55:04.625693: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-10-09 08:55:04.625753: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-10-09 08:55:04.625760: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Entire corpus has 247085 sentences and 2893989 words.
Translation started.
Translation completed. It took 105.35 minutes for 247085 instances - 0.0004263714915919623 minutes per one sentence.
|      | file_path                                                                                                                             | file                                 | sentence_id                        | text                                  | tokenized_text                         | proper_nouns   |   length | lang   | translation                    |
|-----:|:--------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------|:-----------------------------------|:--------------------------------------|:---------------------------------------|:---------------|---------:|:-------|:-------------------------------|
| 1170 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-ES-PV.conllu/ParlaMint-ES-PV.conllu/2017/ParlaMint-ES-PV_2017-11-03-eu.conllu | ParlaMint-ES-PV_2017-11-03-eu.conllu | ParlaMint-ES-PV_2017-11-03.seg1.s1 | Egun on guztioi.                      | Egun on guztioi .                      | {}             |        3 | eu     | Good morning, everyone.        |
| 1171 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-ES-PV.conllu/ParlaMint-ES-PV.conllu/2017/ParlaMint-ES-PV_2017-11-03-eu.conllu | ParlaMint-ES-PV_2017-11-03-eu.conllu | ParlaMint-ES-PV_2017-11-03.seg1.s2 | Osoko bilkurari hasiera emango diogu. | Osoko bilkurari hasiera emango diogu . | {}             |        5 | eu     | We'll start the whole meeting. |
| 1172 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-ES-PV.conllu/ParlaMint-ES-PV.conllu/2017/ParlaMint-ES-PV_2017-11-03-eu.conllu | ParlaMint-ES-PV_2017-11-03-eu.conllu | ParlaMint-ES-PV_2017-11-03.seg2.s1 | Gai-zerrendako lehenengo puntua:      | Gai-zerrendako lehenengo puntua :      | {}             |        3 | eu     | First point in theme list:     |




The file is saved as /home/tajak/Parlamint-translation/results/ES-PV-eu/ParlaMint-ES-PV-eu-translated.csv
