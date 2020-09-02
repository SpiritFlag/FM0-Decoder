import sys
import os

from global_vars import *
from B_simple_convert.global_vars import *
from B_simple_convert.process import process
from Z_common.process import common_process



def main_fnc(file_name):
  try:
    process(file_name)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[simple_convert:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def main():
  try:
    if os.path.isdir(signal_path) is False:
      raise NameError("signal_path= " + signal_path + " does not exist!")

    if os.path.isdir(answer_path) is False:
      raise NameError("answer_path= " + answer_path + " does not exist!")

    common_process(signal_path + file_name_list[0] + "_signal_test.npy", main_fnc, True)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[simple_convert:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
