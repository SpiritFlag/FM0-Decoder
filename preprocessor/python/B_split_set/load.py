import sys

from tqdm import tqdm
from global_vars import *
from B_split_set.global_vars import *



def load(file_name):
  try:
    file = open(signal_path + file_name + "_signal", "r")
    signal = []
    for idx in tqdm(range(n_signal), desc="READING", ncols=100, unit=" signal"):
      signal.append(file.readline())
    file.close()

    file = open(databit_path + file_name + "_databit", "r")
    databit = []
    for idx in range(n_signal):
      databit.append(file.readline())
    file.close()

    return signal, databit

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[B_split_set:load:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
