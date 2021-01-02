import sys
import os

from global_vars import *
from A_split_set.global_vars import *
from A_split_set.process import process
from Z_common.process import common_process



def main_fnc(file_name):
  try:
    process(file_name)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[split_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def main():
  try:
    if os.path.isdir(signal_path) is False:
      raise NameError("signal_path= " + signal_path + " does not exist!")

    if os.path.isdir(signal_path2) is False:
      raise NameError("signal_path2= " + signal_path2 + " does not exist!")

    if os.path.isdir(signal_path3) is False:
      raise NameError("signal_path3= " + signal_path3 + " does not exist!")

    if os.path.isdir(label_path) is False:
      raise NameError("label_path= " + label_path + " does not exist!")

    if os.path.isdir(label_output_path) is False:
      os.mkdir(label_output_path)
      print("Successfuly created an unexist folder! label_output_path= " + label_output_path)

    common_process(signal_path + file_name_list[0] + "_signal_train.npy", main_fnc, True)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[split_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
