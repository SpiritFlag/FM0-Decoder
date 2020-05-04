import sys

from tqdm import tqdm
from global_vars import *
from A_IQconvert.global_vars import *



def read_signal(file_name):
  try:
    file = open(signal_path + file_name + "_Isignal", "r")
    Isignal = []
    for idx in tqdm(range(n_signal), desc="READING", ncols=100, unit=" signal"):
      signal = file.readline().rstrip(" \n").split(" ")
      signal = [float(i) for i in signal]
      Isignal.append(signal)
    file.close()

    file = open(signal_path + file_name + "_Qsignal", "r")
    Qsignal = []
    for idx in tqdm(range(n_signal), desc="READING", ncols=100, unit=" signal"):
      signal = file.readline().rstrip(" \n").split(" ")
      signal = [float(i) for i in signal]
      Qsignal.append(signal)
    file.close()

    return Isignal, Qsignal

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[A_IQconvert:read_signal:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
