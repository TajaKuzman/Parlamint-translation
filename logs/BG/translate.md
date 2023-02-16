2023-02-14 15:49:02.047674: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-02-14 15:49:02.752329: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-02-14 15:49:02.752406: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-02-14 15:49:02.752413: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Entire corpus has 1626624 sentences and 26662522 words.
Translation started.
Translation completed. It took 1504.38 minutes for 1626624 instances - 0.0009248480288007555 minutes per one sentence.
|    | file_path                                                                                                                 | file                           | sentence_id                    | text                                       | tokenized_text                               | proper_nouns   |   length | translation               |
|---:|:--------------------------------------------------------------------------------------------------------------------------|:-------------------------------|:-------------------------------|:-------------------------------------------|:---------------------------------------------|:---------------|---------:|:--------------------------|
|  0 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-BG.conllu/ParlaMint-BG.conllu/2017/ParlaMint-BG_2017-01-25.conllu | ParlaMint-BG_2017-01-25.conllu | ParlaMint-BG_2017-01-25.seg1.1 | Уважаеми народни представители, добър ден! | Уважаеми народни представители , добър ден ! | {}             |        5 | Dear MPs, good afternoon! |
|  1 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-BG.conllu/ParlaMint-BG.conllu/2017/ParlaMint-BG_2017-01-25.conllu | ParlaMint-BG_2017-01-25.conllu | ParlaMint-BG_2017-01-25.seg1.2 | Моля да се регистрираме.                   | Моля да се регистрираме .                    | {}             |        4 | Please register.          |
|  2 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-BG.conllu/ParlaMint-BG.conllu/2017/ParlaMint-BG_2017-01-25.conllu | ParlaMint-BG_2017-01-25.conllu | ParlaMint-BG_2017-01-25.seg2.1 | Прекратете регистрацията.                  | Прекратете регистрацията .                   | {}             |        2 | Abort registration.       |




The file is saved as /home/tajak/Parlamint-translation/results/BG/ParlaMint-BG-translated.csv
