import sys
import numpy as np

from global_vars import *
from A_generate_RNindex.global_vars import *
from A_generate_RNindex.process import process
from Z_common.process import common_process



def main_fnc():
  try:
    RN = np.arange(n_signal)
    np.random.shuffle(RN)

    process(RN, "_train", 0, n_RNtrain)
    process(RN, "_validation", n_RNtrain, n_RNvalidation)
    process(RN, "_test", n_RNtrain+n_RNvalidation, n_RNtest)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[A_generate_RNindex:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def main():
  try:
    common_process(output_path + "_train", main_fnc, False)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[A_generate_RNindex:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
