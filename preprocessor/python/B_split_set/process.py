import sys

from tqdm import tqdm
from global_vars import *
from B_split_set.global_vars import *



def process(signal, databit, file_name, x, postfix):
  try:
    file = open(index_path + "RN" + str(x) + postfix, "r")
    list = file.readline().rstrip(" \n").split(" ")
    list = [int(i) for i in list]
    file.close()

    fileS = open(output_path + file_name + "_RN" + str(x) + "_signal" + postfix, "w")
    fileD = open(output_path + file_name + "_RN" + str(x) + "_databit" + postfix, "w")
    for index in list:
      fileS.write(signal[index])
      fileD.write(databit[index])
    fileS.close()
    fileD.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[B_split_set:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
