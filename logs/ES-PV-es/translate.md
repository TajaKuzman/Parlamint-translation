2023-10-06 12:03:22.257910: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-10-06 12:03:23.031096: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-10-06 12:03:23.031183: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-10-06 12:03:23.031191: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Entire corpus has 410644 sentences and 10652354 words.
Translation started.
Translation completed. It took 230.11 minutes for 410644 instances - 0.0005603637213742318 minutes per one sentence.
|    | file_path                                                                                                                             | file                                 | sentence_id                         | text                                                                                                                                                                                                                                           | tokenized_text                                                                                                                                                                                                                                     | proper_nouns   |   length | lang   | translation                                                                                                                                                                                                                         |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------|:------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|---------:|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-ES-PV.conllu/ParlaMint-ES-PV.conllu/2017/ParlaMint-ES-PV_2017-03-23-es.conllu | ParlaMint-ES-PV_2017-03-23-es.conllu | ParlaMint-ES-PV_2017-03-23.seg20.s1 | Decía que ya son unos años en los que la juventud de este país está sufriendo más para intentar tener una vida digna, pero estructuralmente siempre ha sido un colectivo al que no le ponemos en el lugar que le toca ocupar.                  | Decía que ya son unos años en los que la juventud de este país está sufriendo más para intentar tener una vida digna , pero estructuralmente siempre ha sido un colectivo a el que no le ponemos en el lugar que le toca ocupar .                  | {}             |       42 | es     | He said that it is already a few years in which the youth of this country are suffering more in order to try to have a dignified life, but structurally it has always been a collective that we do not put in its place.            |
|  1 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-ES-PV.conllu/ParlaMint-ES-PV.conllu/2017/ParlaMint-ES-PV_2017-03-23-es.conllu | ParlaMint-ES-PV_2017-03-23-es.conllu | ParlaMint-ES-PV_2017-03-23.seg20.s2 | La juventud es el futuro de la sociedad, y como tal es deber apostar por ella.                                                                                                                                                                 | La juventud es el futuro de la sociedad , y como tal es deber apostar por ella .                                                                                                                                                                   | {}             |       16 | es     | Youth is the future of society, and as such it is a duty to bet on it.                                                                                                                                                              |
|  2 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-ES-PV.conllu/ParlaMint-ES-PV.conllu/2017/ParlaMint-ES-PV_2017-03-23-es.conllu | ParlaMint-ES-PV_2017-03-23-es.conllu | ParlaMint-ES-PV_2017-03-23.seg21.s1 | A mi generación se nos decía que estudiáramos para poder tener un futuro digno, que hincáramos los codos, que si estudiábamos una carrera o un grado superior tendríamos un empleo digno con el cual poder realizarnos y vivir tranquilamente. | A mi generación se nos decía que estudiáramos para poder tener un futuro digno , que hincáramos los codos , que si estudiábamos una carrera o un grado superior tendríamos un empleo digno con el cual poder realizar nos y vivir tranquilamente . | {}             |       39 | es     | My generation was told that we would study so that we could have a worthy future, that we would swell our elbows, that if we studied a career or a higher degree we would have a decent job with which to realize and live quietly. |




The file is saved as /home/tajak/Parlamint-translation/results/ES-PV-es/ParlaMint-ES-PV-es-translated.csv