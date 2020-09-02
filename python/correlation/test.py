import sys
import os

from global_vars import *
from common.test import common_test
from correlation.global_vars import *
from correlation.read_set import read_set
from correlation.process import process





def main_fnc(file_name, test_set, answer_set):
  try:
    return process(file_name, test_set, answer_set)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[correlation_test:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def correlation_test(path):
  try:
    if os.path.isdir(signal_path) is False:
      raise NameError("signal_path= " + signal_path + " does not exist!")

    if os.path.isdir(answer_path) is False:
      raise NameError("answer_path= " + answer_path + " does not exist!")

    if common_test(fnc_read_set=read_set, fnc=main_fnc):
      return False, True    # normal
    else:
      return False, False   # aborted

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[correlation_test:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
