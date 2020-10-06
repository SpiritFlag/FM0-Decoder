import sys
import numpy as np

from global_vars import *
from A_sub_split_set.global_vars import *



def process(file_name):
  try:
    postfix_list = ["train", "validation", "test"]

    for postfix in postfix_list:
      signal = np.load(signal_path + file_name + "_signal_" + postfix + ".npy")
      answer = np.load(answer_path + file_name + "_answer_" + postfix + ".npy")

      npy_signal = signal[:int(round(len(signal) / n_subset, 0))]
      npy_answer = answer[:int(round(len(answer) / n_subset, 0))]

      print(len(npy_signal), len(npy_answer))

      np.save(output_signal_path + file_name + "_signal_" + postfix, npy_signal)
      np.save(output_answer_path + file_name + "_answer_" + postfix, npy_answer)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[sub_split_set:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
