import sys

from global_vars import *
from B_half_bit_repitition.global_vars import *



def load(file_name, x, set_name):
  try:
    n_lines = sum(1 for line in open(databit_path + file_name + "_RN" + str(x) + "_databit" + set_name, "r"))
    file = open(databit_path + file_name + "_RN" + str(x) + "_databit" + set_name, "r")
    databit = []
    for idx in range(n_lines):
      line = file.readline().rstrip(" \n")
      line = [int(i) for i in line]
      databit.append(line)
    file.close()

    return databit

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[B_half_bit_repitition:load:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
