import sys

from tqdm import tqdm
from global_vars import *
from B_split_set.global_vars import *
from B_split_set.load import load
from B_split_set.process import process
from Z_common.process import common_process



def main_fnc(file_name):
  try:
    signal, databit = load(file_name)
    process(signal, databit, file_name, "_train")
    process(signal, databit, file_name, "_validation")
    process(signal, databit, file_name, "_test")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[B_split_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def main():
  try:
    common_process(output_path + file_name_list[0] + "_signal_train", main_fnc, True)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[B_split_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
