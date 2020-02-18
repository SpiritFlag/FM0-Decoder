import sys

from tqdm import tqdm
from global_vars import *



def generate_RNwhole_set(file_name):
  try:
    file = open(signal_path + file_name + "_signal", "r")
    signal = []
    for idx in range(n_signal):
      signal.append(file.readline())
    file.close()

    fileT = open(output_path + file_name + "_train", "w")
    fileV = open(output_path + file_name + "_validation", "w")

    for x in tqdm(range(n_RNsignal), desc="PROCESSING", ncols=100, unit=" signal"):
      file = open(index_path + "RN" + str(x) + "_train", "r")
      list = file.readline().rstrip(" \n").split(" ")
      list = [int(i) for i in list]
      file.close()

      for index in list:
        fileT.write(signal[index])

      file = open(index_path + "RN" + str(x) + "_validation", "r")
      list = file.readline().rstrip(" \n").split(" ")
      list = [int(i) for i in list]
      file.close()

      for index in list:
        fileV.write(signal[index])

      file = open(index_path + "RN" + str(x) + "_test", "r")
      list = file.readline().rstrip(" \n").split(" ")
      list = [int(i) for i in list]
      file.close()

      file = open(output_path + file_name + "_RN" + str(x) + "_test", "w")
      for index in list:
        file.write(signal[index])
      file.close()

    fileT.close()
    fileV.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[generate_RNwhole_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
