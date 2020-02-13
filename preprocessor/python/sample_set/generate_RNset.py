import sys

from tqdm import tqdm
from global_vars import *



def generate_RNset(file_name):
  try:
    file = open(signal_path + file_name + "_signal", "r")
    signal = []
    for idx in range(n_signal):
      signal.append(file.readline())
    file.close()

    for x in tqdm(range(n_RNsignal), desc="PROCESSING", ncols=100, unit=" signal"):
      file = open(index_path + "RN" + str(x) + "_train", "r")
      list = file.readline().rstrip(" \n").split(" ")
      list = [int(i) for i in list]
      file.close()

      file = open(output_path + file_name + "_RN" + str(x) + "_train", "w")
      for index in list:
        file.write(signal[index])
      file.close()

      file = open(index_path + "RN" + str(x) + "_validation", "r")
      list = file.readline().rstrip(" \n").split(" ")
      list = [int(i) for i in list]
      file.close()

      file = open(output_path + file_name + "_RN" + str(x) + "_validation", "w")
      for index in list:
        file.write(signal[index])
      file.close()

      file = open(index_path + "RN" + str(x) + "_test", "r")
      list = file.readline().rstrip(" \n").split(" ")
      list = [int(i) for i in list]
      file.close()

      file = open(output_path + file_name + "_RN" + str(x) + "_test", "w")
      for index in list:
        file.write(signal[index])
      file.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[generate_RNset:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
