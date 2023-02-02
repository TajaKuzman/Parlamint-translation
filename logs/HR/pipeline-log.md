6
2023-01-31 19:09:39.183354: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-01-31 19:09:40.123877: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2023-01-31 19:09:40.123969: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2023-01-31 19:09:40.123979: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/transformers/generation/utils.py:1273: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 512 (`generation_config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  warnings.warn(
2023-02-01 12:23:54 INFO: Checking for updates to resources.json in case models have been updated.  Note: this behavior can be turned off with download_method=None or download_method=DownloadMethod.REUSE_RESOURCES
Downloading https://raw.githubusercontent.com/stanfordnlp/stanza-resources/main/resources_1.4.1.json:   0%|          | 0.00/28.9k [00:00<?, ?B/s]Downloading https://raw.githubusercontent.com/stanfordnlp/stanza-resources/main/resources_1.4.1.json: 193kB [00:00, 44.1MB/s]                    
2023-02-01 12:23:55 INFO: Loading these models for language: en (English):
========================
| Processor | Package  |
------------------------
| tokenize  | combined |
========================

2023-02-01 12:23:56 INFO: Use device: gpu
2023-02-01 12:23:56 INFO: Loading: tokenize
2023-02-01 12:23:59 INFO: Done loading processors!
Traceback (most recent call last):
  File "4-word-alignment.py", line 387, in <module>
    df = tokenize_translation(translated_dataframe_path, translated_tokenized_dataframe_path)
  File "4-word-alignment.py", line 35, in tokenize_translation
    df = pd.read_csv("{}".format(translated_dataframe_path), sep="\t", index_col = 0)
  File "/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/pandas/util/_decorators.py", line 211, in wrapper
    return func(*args, **kwargs)
  File "/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/pandas/util/_decorators.py", line 331, in wrapper
    return func(*args, **kwargs)
  File "/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/pandas/io/parsers/readers.py", line 950, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/pandas/io/parsers/readers.py", line 605, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/pandas/io/parsers/readers.py", line 1442, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/pandas/io/parsers/readers.py", line 1735, in _make_engine
    self.handles = get_handle(
  File "/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/pandas/io/common.py", line 856, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: '/home/tajak/Parlamint-translation/results/HR/ParlaMint-HR-translated.csv'
Traceback (most recent call last):
  File "5-create-conllu.py", line 191, in <module>
    produce_final_conllu(lang_code, final_dataframe)
  File "5-create-conllu.py", line 167, in produce_final_conllu
    df = pd.read_csv("{}".format(final_dataframe), sep="\t", index_col=0)
  File "/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/pandas/util/_decorators.py", line 211, in wrapper
    return func(*args, **kwargs)
  File "/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/pandas/util/_decorators.py", line 331, in wrapper
    return func(*args, **kwargs)
  File "/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/pandas/io/parsers/readers.py", line 950, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/pandas/io/parsers/readers.py", line 605, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/pandas/io/parsers/readers.py", line 1442, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/pandas/io/parsers/readers.py", line 1735, in _make_engine
    self.handles = get_handle(
  File "/home/tajak/Parlamint-translation/parlamint_env/lib/python3.8/site-packages/pandas/io/common.py", line 856, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: '/home/tajak/Parlamint-translation/results/HR/ParlaMint-HR-final-dataframe.csv'
