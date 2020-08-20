import sys
import os

from global_vars import *
from X_convert_answer.global_vars import *
from X_convert_answer.process import process
from Z_common.process import common_process



def main_fnc(file_name):
  try:
    process(file_name)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[convert_answer:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def main():
  try:
    if os.path.isdir(output_path) is False:
      os.mkdir(output_path)
      print("Successfuly created an unexist folder! output_path= " + output_path)

    common_process(output_path + file_name_list[0] + "_answer_" + answer_type_list[0] + "_train.npy", main_fnc, True)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[convert_answer:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
