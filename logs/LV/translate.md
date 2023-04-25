2023-03-28 12:33:38.259523: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-03-28 12:33:38.990953: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-03-28 12:33:38.991029: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-03-28 12:33:38.991036: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Entire corpus has 930377 sentences and 9451541 words.
Translation started.
Translation completed. It took 573.39 minutes for 930377 instances - 0.00061629855424199 minutes per one sentence.
|    | file_path                                                                                                                          | file                                    | sentence_id                              | text                                    | tokenized_text                            | proper_nouns   |   length | translation                                            |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------|:-----------------------------------------|:----------------------------------------|:------------------------------------------|:---------------|---------:|:-------------------------------------------------------|
|  0 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-LV.conllu/ParlaMint-LV.conllu/2017/ParlaMint-LV_2017-03-09-PT12-407.conllu | ParlaMint-LV_2017-03-09-PT12-407.conllu | ParlaMint-LV_2017-03-09-PT12-407-U1-P1.1 | Labrīt, godātie deputāti!               | Labrīt , godātie deputāti !               | {}             |        3 | Good morning, honourable Members!                      |
|  1 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-LV.conllu/ParlaMint-LV.conllu/2017/ParlaMint-LV_2017-03-09-PT12-407.conllu | ParlaMint-LV_2017-03-09-PT12-407.conllu | ParlaMint-LV_2017-03-09-PT12-407-U1-P1.2 | Aicinu ieņemt vietas Saeimas Sēžu zālē. | Aicinu ieņemt vietas Saeimas Sēžu zālē .  | {}             |        6 | I invite you to take seats in Saeima's meeting room.   |
|  2 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-LV.conllu/ParlaMint-LV.conllu/2017/ParlaMint-LV_2017-03-09-PT12-407.conllu | ParlaMint-LV_2017-03-09-PT12-407.conllu | ParlaMint-LV_2017-03-09-PT12-407-U1-P1.3 | Sāksim Saeimas 2017.gada 9.marta sēdi.  | Sāksim Saeimas 2017. gada 9. marta sēdi . | {}             |        5 | Let's start the sitting of the Saeima on 9 March 2017. |




The file is saved as /home/tajak/Parlamint-translation/results/LV/ParlaMint-LV-translated.csv
