import sys
import os

from global_vars import *
from A_IQconvert.global_vars import *
from A_IQconvert.process import process
from Z_common.process import common_process



def main_fnc(file_name):
  try:
    process(file_name)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[IQconvert:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def main():
  try:
    if os.path.isdir(signal_path) is False:
      raise NameError("signal_path= " + signal_path + " does not exist!")

    if os.path.isdir(answer_path) is False:
      raise NameError("answer_path= " + answer_path + " does not exist!")

    if os.path.isdir(output_path) is False:
      os.mkdir(output_path)
      print("Successfuly created an unexist folder! output_path= " + output_path)

    if os.path.isdir(output_path2) is False:
      os.mkdir(output_path2)
      print("Successfuly created an unexist folder! output_path2= " + output_path2)

    if os.path.isdir(output_path3) is False:
      os.mkdir(output_path3)
      print("Successfuly created an unexist folder! output_path3= " + output_path3)

    if os.path.isdir(answer_output_path) is False:
      os.mkdir(answer_output_path)
      print("Successfuly created an unexist folder! answer_output_path= " + answer_output_path)

    common_process(output_path + file_name_list[0] + "_signal.npy", main_fnc, True)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[IQconvert:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
