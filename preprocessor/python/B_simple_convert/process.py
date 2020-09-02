import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from B_simple_convert.global_vars import *



def process(file_name):
  try:
    file = open(signal_path + file_name + "_signal_test", "r")
    signal = []
    for idx in tqdm(range(n_signal), desc="READING", ncols=100, unit=" signal"):
      signal.append([float(i) for i in file.readline().rstrip(" \n").split(" ")])
    file.close()
    np.save(signal_path + file_name + "_signal_test", np.array(signal))

    file = open(answer_path + file_name + "_answer_test", "r")
    answer = []
    for idx in tqdm(range(n_signal), desc="READING", ncols=100, unit=" answer"):
      answer.append([int(i) for i in file.readline().rstrip("\n")])
    file.close()
    np.save(answer_path + file_name + "_answer_test", np.array(answer))

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[simple_convert:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
