import sys

from global_vars import *
from C_extract_bit_static.global_vars import *
from C_extract_bit_static.process import process
from Z_common.process import common_process



def main_fnc(file_name):
  try:
    process(file_name, "_train")
    process(file_name, "_validation")
    process(file_name, "_test")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[C_extract_bit_static:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def main():
  try:
    common_process(output_path + file_name_list[0] + "_signal_train_0", main_fnc, True)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[C_extract_bit_static:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
