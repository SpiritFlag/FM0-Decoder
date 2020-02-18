import sys

from tqdm import tqdm
from global_vars import *



def append_preamble(file):
  try:
    mask = [1] * 2 * databit_repition  # 1
    mask += [0] * databit_repition  # 2
    mask += [1] * databit_repition
    mask += [0] * 2 * databit_repition  # 3
    mask += [1] * databit_repition  # 4
    mask += [0] * databit_repition
    mask += [0] * 2 * databit_repition  # 5
    mask += [1] * 2 * databit_repition  # 6

    for sample in mask:
      file.write(str(sample))

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[append_preamble:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")


def generate_RNwhole_databit(file_name):
  try:
    file = open(databit_path + file_name + "_databit_rep" + str(databit_repition), "r")
    databit = []
    for idx in range(n_signal):
      databit.append(file.readline())
    file.close()

    fileT = open(output_path + file_name + "_train" + "_rep" + str(databit_repition), "w")
    fileV = open(output_path + file_name + "_validation" + "_rep" + str(databit_repition), "w")

    for x in tqdm(range(n_RNsignal), desc="PROCESSING", ncols=100, unit=" signal"):
      file = open(index_path + "RN" + str(x) + "_train", "r")
      list = file.readline().rstrip(" \n").split(" ")
      list = [int(i) for i in list]
      file.close()

      for index in list:
        append_preamble(fileT)
        fileT.write(databit[index])

      file = open(index_path + "RN" + str(x) + "_validation", "r")
      list = file.readline().rstrip(" \n").split(" ")
      list = [int(i) for i in list]
      file.close()

      for index in list:
        append_preamble(fileV)
        fileV.write(databit[index])

      file = open(index_path + "RN" + str(x) + "_test", "r")
      list = file.readline().rstrip(" \n").split(" ")
      list = [int(i) for i in list]
      file.close()

      file = open(output_path + file_name + "_RN" + str(x) + "_test" + "_rep" + str(databit_repition), "w")
      for index in list:
        append_preamble(file)
        file.write(databit[index])
      file.close()

    fileT.close()
    fileV.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[generate_RNwhole_datbit:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
