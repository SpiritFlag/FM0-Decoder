import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from MLP.determine_fail import determine_fail



def count_success(mlp, test_set, answer_set):
  try:
    if model_type == "whole":
      predict_set = mlp.test_model(np.array(test_set))

    success = 0
    for idx in tqdm(range(len(answer_set)), desc="TESTING", ncols=100, unit=" signal"):
      if len(test_set[idx]) == 0: # outlier
        continue

      fail = False

      if model_type == "bit_unit":
        tmp_set = []
        for n in range(n_bit_data):
          tmp_set.append(test_set[idx][int(n_bit*2*n):int(n_bit*2*(n+1))])
        predict_set = mlp.test_model(np.array(tmp_set))

        for n in range(n_bit_data):
          fail = determine_fail(predict_set[n], answer_set[idx][n])
          if fail is True:
            break

      elif model_type == "whole":
        for n in range(n_bit_preamble + n_bit_data):
          st = int(2*databit_repition*n)
          ed = int(2*databit_repition*(n+1))
          fail = determine_fail(predict_set[idx][st:ed], answer_set[idx][st:ed])
          if fail is True:
            break

      else:
        raise ValueError("No function matching with model type named \"" + model_type + "\"!")

      if fail is False:
        success += 1

    return success

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[count_success:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
