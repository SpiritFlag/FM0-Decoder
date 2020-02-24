import sys

from tqdm import tqdm
from global_vars import *
from C_extract_bit_unit.global_vars import *



def load(file_name, set_name, set_size):
  try:
    file = open(signal_path + file_name + "_RN" + str(RN) + "_signal" + set_name, "r")
    signal = []
    for idx in tqdm(range(set_size), desc="READING", ncols=100, unit=" signal"):
      line = file.readline().rstrip(" \n").split(" ")
      line = [float(i) for i in line]
      for n in range(n_half_bit):
        line.append(0)
      signal.append(line)
    file.close()

    file = open(signal_path + file_name + "_RN" + str(RN) + "_databit" + set_name, "r")
    databit = []
    for idx in range(n_signal):
      line = file.readline().rstrip(" \n")
      line = [int(i) for i in line]
      databit.append(line)
    file.close()

    return signal, databit

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[C_extract_bit_unit:load:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
