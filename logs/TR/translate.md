2023-02-24 08:50:49.926471: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-02-24 08:50:50.624302: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-02-24 08:50:50.624383: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-02-24 08:50:50.624391: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
Entire corpus has 3609640 sentences and 46635165 words.
Translation started.
Translation completed. It took 1654.62 minutes for 3609640 instances - 0.0004583892022473155 minutes per one sentence.
|    | file_path                                                                                                                          | file                                    | sentence_id                               | text                                                           | tokenized_text                                                  | proper_nouns   |   length | translation                                                            |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------|:------------------------------------------|:---------------------------------------------------------------|:----------------------------------------------------------------|:---------------|---------:|:-----------------------------------------------------------------------|
|  0 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-TR.conllu/ParlaMint-TR.conllu/2013/ParlaMint-TR_2013-07-02-tbmm-T24.conllu | ParlaMint-TR_2013-07-02-tbmm-T24.conllu | tbmm-2013-07-02sit01spe0001par0001-000010 | Türkiye Büyük Millet Meclisinin 128’inci Birleşimini açıyorum. | Türkiye Büyük Millet Meclisinin 128’inci Birleşimini açıyorum . | {}             |        7 | I am opening the 128th Union of the Grand National Assembly of Turkey. |
|  1 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-TR.conllu/ParlaMint-TR.conllu/2013/ParlaMint-TR_2013-07-02-tbmm-T24.conllu | ParlaMint-TR_2013-07-02-tbmm-T24.conllu | tbmm-2013-07-02sit01spe0001par0002-000010 | Toplantı yeter sayısı vardır.                                  | Toplantı yeter sayısı var dır .                                 | {}             |        4 | There's enough for a meeting.                                          |
|  2 | /home/tajak/Parlamint-translation/Source-data/ParlaMint-TR.conllu/ParlaMint-TR.conllu/2013/ParlaMint-TR_2013-07-02-tbmm-T24.conllu | ParlaMint-TR_2013-07-02-tbmm-T24.conllu | tbmm-2013-07-02sit01spe0001par0003-000010 | Gündeme geçiyoruz.                                             | Gündeme geçiyoruz .                                             | {}             |        2 | We're going on the agenda.                                             |




The file is saved as /home/tajak/Parlamint-translation/results/TR/ParlaMint-TR-translated.csv