import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from MLP.determine_fail import determine_fail
from MLP.decode_data import decode_data



def count_success(mlp, test_set, answer_set, file_name):
  try:
    if model_type == "whole":
      predict_set = mlp.test_model(np.array(test_set))

    file = open("data/Y_full_test/" + file_name + "_mlp25", "w")
    fileW = open("data/Y_full_rep25/" + file_name, "w")

    success = 0
    for idx in tqdm(range(len(answer_set)), desc="TESTING", ncols=100, unit=" signal"):
      if len(test_set[idx]) == 0: # outlier
        file.write("-1\t")
        continue

      fail = False
      cnt = 0

      if model_type == "bit_unit":
        if test_type == "corr":
          tmp_set = []
          for n in range(n_bit_data):
            tmp_set.append(test_set[idx][int(n_bit*2*n):int(n_bit*2*(n+1))])
          predict_set = mlp.test_model(np.array(tmp_set))

        elif test_type == "shift":
          predict_set = decode_data(file_name, mlp, test_set[idx])

        for n in range(n_bit_data):
          cur_fail = determine_fail(predict_set[n], answer_set[idx][n])
          if cur_fail is True:
            cnt += 1
            fail = True
            #break

      elif model_type == "whole":
        for n in range(n_bit_preamble, n_bit_preamble + n_bit_data):
          st = int(2*databit_repitition*n)
          ed = int(2*databit_repitition*(n+1))
          cur_fail = determine_fail(predict_set[idx][st:ed], answer_set[idx][st:ed])
          if cur_fail is True:
            fail = True
            break
        for x in predict_set[idx]:
          fileW.write(str(x) + "\t")
        fileW.write("\n")

      else:
        raise ValueError("No function matching with model type named \"" + model_type + "\"!")

      if fail is False:
        success += 1
      #  file.write("0\t")
      #else:
      #  file.write("1\t")
      file.write(str(cnt) + "\t")

    file.close()
    fileW.close()
    return success

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[count_success:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
