import sys
import os

from global_vars import *
from Y_analysis.global_vars import *
from Y_analysis.process import process
from Z_common.process import common_process



def main_fnc(file_name):
  try:
    process(file_name)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[analysis:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def main():
  try:
    if os.path.isdir(signal_path) is False:
      raise NameError("signal_path= " + signal_path + " does not exist!")

    if os.path.isdir(compare_path) is False:
      raise NameError("compare_path= " + compare_path + " does not exist!")

    common_process(None, main_fnc, True)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[analysis:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
