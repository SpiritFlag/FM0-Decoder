import sys

from tqdm import tqdm
from global_vars import *
from C_extract_bit_static.global_vars import *



def load(file_name, set_name):
  try:
    n_lines = sum(1 for line in open(signal_path + file_name + "_signal" + set_name))
    file = open(signal_path + file_name + "_signal" + set_name, "r")
    signal = []
    for idx in tqdm(range(n_lines), desc="READING", ncols=100, unit=" signal"):
      line = file.readline().rstrip(" \n").split(" ")
      signal.append([float(i) for i in line])
    file.close()

    n_lines = sum(1 for line in open(signal_path + file_name + "_databit" + set_name))
    file = open(signal_path + file_name + "_databit" + set_name, "r")
    databit = []
    for idx in range(n_lines):
      line = file.readline().rstrip("\n")
      databit.append([int(i) for i in line])
    file.close()

    return signal, databit

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[C_extract_bit_static:load:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
