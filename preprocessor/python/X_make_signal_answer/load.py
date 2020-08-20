import sys

from global_vars import *
from X_make_signal_answer.global_vars import *



def load(file_name):
  try:
    n_lines = sum(1 for line in open(databit_path + file_name + "_databit", "r"))
    file = open(databit_path + file_name + "_databit", "r")
    databit = []
    for idx in range(n_lines):
      databit.append([int(i) for i in file.readline().rstrip(" \n")])
    file.close()

    if RNindex_path != "none":
      databit_list = []

      for postfix in ["_train", "_validation", "_test"]:
        n_lines = sum(1 for line in open(RNindex_path + postfix, "r"))
        file = open(RNindex_path + postfix, "r")
        RNindex = [int(i) for i in file.readline().rstrip(" \n").split(" ")]

        new_databit = []
        for index in RNindex:
          new_databit.append(databit[index])
        databit_list.append(new_databit)

      return databit_list
    else:
      return databit

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[X_make_signal_answer:load:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
