import sys

from global_vars import *
from common.test import common_test
from correlation.global_vars import *
from correlation.process import *





def main_fnc(file_name, test_set, answer_set):
  try:
    return process(file_name, test_set, answer_set)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[correlation_test:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def correlation_test(path):
  try:
    if common_test(test_path=test_path, fnc=main_fnc):
      return False, True    # normal
    else:
      return False, False   # aborted

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[correlation_test:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
