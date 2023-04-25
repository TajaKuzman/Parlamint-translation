2023-04-12 11:46:25.050075: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-04-12 11:46:25.720212: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-04-12 11:46:25.720282: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-04-12 11:46:25.720290: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Entire corpus has 1586348 sentences and 18398066 words.
Translation started.
Translation completed. It took 587.21 minutes for 1586348 instances - 0.00037016468013323687 minutes per one sentence.
|    | file_path                                                                                                                       | file                                 | sentence_id                         | text                                            | tokenized_text                                    | proper_nouns   |   length | translation                        |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------|:------------------------------------|:------------------------------------------------|:--------------------------------------------------|:---------------|---------:|:-----------------------------------|
|  0 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-UA.conllu/ParlaMint-UA.conllu/2013/ParlaMint-UA_2013-11-22-m0-ru.conllu | ParlaMint-UA_2013-11-22-m0-ru.conllu | ParlaMint-UA_2013-11-22-m0.u2.p2.s1 | Послухайте!                                     | Послухайте !                                      | {}             |        1 | Listen!                            |
|  1 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-UA.conllu/ParlaMint-UA.conllu/2013/ParlaMint-UA_2013-11-22-m0-ru.conllu | ParlaMint-UA_2013-11-22-m0-ru.conllu | ParlaMint-UA_2013-11-22-m0.u2.p2.s2 | Орать вы всегда можете, мы это знаем прекрасно. | Орать вы всегда можете , мы это знаем прекрасно . | {}             |        8 | You can always plow, we know that. |
|  2 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-UA.conllu/ParlaMint-UA.conllu/2013/ParlaMint-UA_2013-11-22-m0-ru.conllu | ParlaMint-UA_2013-11-22-m0-ru.conllu | ParlaMint-UA_2013-11-22-m0.u4.p2.s1 | Орет тут мне на ухо!                            | Орет тут мне на ухо !                             | {}             |        5 | I've got an earful!                |




The file is saved as /home/tajak/Parlamint-translation/results/UA/ParlaMint-UA-translated.csv
