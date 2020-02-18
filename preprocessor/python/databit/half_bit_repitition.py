import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from read_data import *



def half_bit_repitition(file_name):
  try:
    databit = read_databit(databit_path + file_name)
    file = open(output_path + file_name + "_databit_rep" + str(databit_repition), "w")

    for idx in range(n_signal):
      conv = []
      level = -1

      for sample in databit[idx]:
        if sample == 1:
          conv.append(level)
          conv.append(level)
          level *= -1
        else:
          conv.append(level)
          conv.append(level * -1)

      for sample in conv:
        if sample == -1:
          for x in range(databit_repition):
            file.write("0")
        else:
          for x in range(databit_repition):
            file.write("1")
      file.write("\n")

    file.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[half_bit_repitition:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
