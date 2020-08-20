import sys

from tqdm import tqdm
from global_vars import *
from D_augment_sample.global_vars import *



def load(file_name):
  try:
    signal_list = []

    for postfix in ["_train", "_validation", "_test"]:
      n_lines = sum(1 for line in open(signal_path + file_name + "_signal" + postfix, "r"))
      file = open(signal_path + file_name + "_signal" + postfix, "r")

      signal = []
      for idx in tqdm(range(n_lines), desc="READING", ncols=100, unit=" signal"):
        signal.append([float(i) for i in file.readline().rstrip(" \n").split(" ")])
      signal_list.append(signal)

    return signal_list

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[D_augment_sample:load:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
