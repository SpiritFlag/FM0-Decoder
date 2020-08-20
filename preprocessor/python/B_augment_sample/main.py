import sys
import os

from global_vars import *
from B_augment_sample.global_vars import *
from B_augment_sample.process import process
from Z_common.process import common_process



def main_fnc(file_name):
  try:
    process(file_name)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[augment_sample:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def main():
  try:
    if os.path.isdir(signal_path) is False:
      raise NameError("signal_path= " + signal_path + " does not exist!")

    if os.path.isdir(output_path) is False:
      os.mkdir(output_path)
      print("Successfuly created an unexist folder! output_path= " + output_path)

    common_process(output_path + file_name_list[0] + "_signal_" + str(augment_list[0]) + "_train.npy", main_fnc, True)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[augment_sample:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
