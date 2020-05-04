import sys

from tqdm import tqdm
from global_vars import *
from B_split_set.global_vars import *



def process(signal, databit, file_name, postfix):
  try:
    file = open(index_path + RN_postfix + postfix, "r")
    list = file.readline().rstrip("\n").split(" ")
    list = [int(i) for i in list]
    file.close()

    fileS = open(output_path + file_name + "_signal" + postfix, "w")
    fileD = open(output_path + file_name + "_databit" + postfix, "w")
    for idx in tqdm(range(len(list)), desc="PROCESSING", ncols=100, unit=" signal"):
      fileS.write(signal[list[idx]])
      fileD.write(databit[list[idx]])
    fileS.close()
    fileD.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[B_split_set:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
