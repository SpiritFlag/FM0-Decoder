import sys
import os

from global_vars import *
from B_extract_bit.global_vars import *
from B_extract_bit.process import process
from Z_common.process import common_process



def main_fnc(file_name):
  try:
    process(file_name)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[extract_bit:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def main():
  try:
    if os.path.isdir(signal_path) is False:
      raise NameError("signal_path= " + signal_path + " does not exist!")

    if os.path.isdir(answer_path) is False:
      raise NameError("answer_path= " + answer_path + " does not exist!")

    if os.path.isdir(output_path) is False:
      os.mkdir(output_path)
      print("Successfuly created an unexist folder! output_path= " + output_path)

    common_process(output_path + file_name_list[0] + "_bit_train_1.npy", main_fnc, True)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[extract_bit:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
