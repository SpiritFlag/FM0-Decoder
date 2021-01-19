import sys
import os

from global_vars import *
from A_train_set.global_vars import *
from A_train_set.process import process
from Z_common.process import common_process



def main_fnc():
  try:
    process()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[train_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def main():
  try:
    if os.path.isdir(signal_path) is False:
      raise NameError("signal_path= " + signal_path + " does not exist!")

    if os.path.isdir(label_path) is False:
      raise NameError("label_path= " + label_path + " does not exist!")

    if os.path.isdir(output_path) is False:
      os.mkdir(output_path)
      print("Successfuly created an unexist folder! output_path= " + output_path)

    if os.path.isdir(label_output_path) is False:
      os.mkdir(label_output_path)
      print("Successfuly created an unexist folder! label_output_path= " + label_output_path)

    common_process(output_path + "0.npy", main_fnc, False)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[train_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
