import sys

from global_vars import *
from X_make_signal_answer.global_vars import *
from X_make_signal_answer.load import load
from X_make_signal_answer.append_preamble import append_preamble
from X_make_signal_answer.encode_data import encode_data



def process(file_name):
  try:
    databit_list = load(file_name)

    if RNindex_path != "none":
      postfix = ["_train", "_validation", "_test"]

      for x in range(3):
        file = open(output_path + file_name + "_answer" + answer_type + postfix[x], "w")
        for databit in databit_list[x]:
          if ispreamble is True:
            append_preamble(file)
          encode_data(file, databit)
          # double
          if ispreamble is True:
            append_preamble(file)
          encode_data(file, databit)
        file.close()
    else:
      file = open(output_path + file_name + "_answer" + answer_type + "_test", "w")
      for databit in databit_list:
        if ispreamble is True:
          append_preamble(file)
        encode_data(file, databit)
      file.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[X_make_signal_answer:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
