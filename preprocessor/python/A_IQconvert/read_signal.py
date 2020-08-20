import sys

from tqdm import tqdm
from global_vars import *
from A_IQconvert.global_vars import *



def read_signal(file_name):
  try:
    file = open(signal_path + file_name + "_Isignal", "r")
    Isignal = []
    for idx in tqdm(range(n_signal), desc="READING I", ncols=100, unit=" signal"):
      Isignal.append([float(i) for i in file.readline().rstrip(" \n").split(" ")])
    file.close()

    file = open(signal_path + file_name + "_Qsignal", "r")
    Qsignal = []
    for idx in tqdm(range(n_signal), desc="READING Q", ncols=100, unit=" signal"):
      Qsignal.append([float(i) for i in file.readline().rstrip(" \n").split(" ")])
    file.close()

    file = open(answer_path + file_name + "_answer", "r")
    answer = []
    for idx in tqdm(range(n_signal), desc="READING", ncols=100, unit=" answer"):
      answer.append([int(i) for i in file.readline().rstrip("\n")])
    file.close()

    return Isignal, Qsignal, answer

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[IQconvert:read_signal:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
