import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from clustering.global_vars import *



def read_set(file_name_list, postfix):
  try:
    signal = []
    label = []

    for x in tqdm(range(len(file_name_list)), desc="READING", ncols=100, unit=" file"):
      try:
        file_name = file_name_list[x]

        signalI.extend(np.load(signal_path + file_name + "_Isignal_test.npy"))
        signalQ.extend(np.load(signal_path + file_name + "_Qsignal_test.npy"))
        label.extend(np.load(label_path + file_name + "_label_" + label_type + "_test.npy"))

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[clustering:read_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    return np.array(signalI), np.array(signalQ), np.array(label)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[clustering:read_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
