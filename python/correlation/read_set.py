import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from correlation.global_vars import *



def read_set(file_name_list, postfix):
  try:
    signal = []
    answer = []

    for x in tqdm(range(len(file_name_list)), desc="READING", ncols=100, unit=" file"):
      try:
        file_name = file_name_list[x]

        if augment_list == []:
          signal.extend(np.load(signal_path + file_name + "_signal_" + postfix + ".npy"))
          answer.extend(np.load(answer_path + file_name + "_answer_" + answer_type + "_" + postfix + ".npy"))
        else:
          for augment in augment_list:
            signal.extend(np.load(signal_path + file_name + "_signal_" + str(augment) + "_" + postfix + ".npy"))
            answer.extend(np.load(answer_path + file_name + "_answer_" + answer_type + "_" + postfix + ".npy"))

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[correlation:read_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    return np.array(signal), np.array(answer)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[correlation:read_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
