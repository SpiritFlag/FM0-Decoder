import sys
import os

from global_vars import *
from common.test import common_test
from clustering.global_vars import *
from clustering.read_set import read_set
from clustering.process import process





def main_fnc(file_name, test_set, label_set):
  try:
    return process(file_name, test_set, label_set)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[clustering_test:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def clustering_test(path):
  try:
    if os.path.isdir(signal_path) is False:
      raise NameError("signal_path= " + signal_path + " does not exist!")

    if os.path.isdir(label_path) is False:
      raise NameError("label_path= " + label_path + " does not exist!")

    if common_test(fnc_read_set=read_set, fnc=main_fnc):
      return False, True    # normal
    else:
      return False, False   # aborted

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[clustering_test:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
