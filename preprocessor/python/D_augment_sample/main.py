import sys

from global_vars import *
from D_augment_sample.global_vars import *
from D_augment_sample.process import process
from Z_common.process import common_process



def main_fnc(file_name):
  try:
    process(file_name)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[Z_augment_sample:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def main():
  try:
    common_process(output_path + file_name_list[0] + "_signal_" + str(augment_list[0]) + "_train", main_fnc, True)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[Z_augment_sample:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
