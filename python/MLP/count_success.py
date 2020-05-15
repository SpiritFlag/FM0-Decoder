import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from MLP.global_vars import *
#from MLP.determine_fail import determine_fail
#from MLP.decode_data import decode_data



def count_success(predict_set, answer_set, countBit=False):
  try:
    if model_type == "signal":
      threshold = 0.5
      success = 0
      error_idx_list = []
      n_error_list = []

      for idx in tqdm(range(len(answer_set)), desc="TESTING", ncols=100, unit=" signal"):
        cur_fail = False
        error_idx = -1
        n_error = 0

        for bit in range(n_bit_preamble, n_bit_preamble+n_bit_data):
          predict = predict_set[idx][int(2*amp_rep*bit):int(2*amp_rep*(bit+1))]
          answer = answer_set[idx][int(2*amp_rep*bit):int(2*amp_rep*(bit+1))]

          count = 0
          for n in range(amp_rep):
            if (predict[n] < threshold and answer[n] < threshold) or (predict[n] > threshold and answer[n] > threshold):
              count += 1
          if count <= int(amp_rep / 2):
            if countBit is True:
              if cur_fail is False:
                error_idx = bit
                cur_fail = True
              n_error += 1
              continue
            else:
              cur_fail = True
              break

          count = 0
          for n in range(amp_rep, 2*amp_rep):
            if (predict[n] < threshold and answer[n] < threshold) or (predict[n] > threshold and answer[n] > threshold):
              count += 1
          if count <= int(amp_rep / 2):
            if countBit is True:
              if cur_fail is False:
                error_idx = bit
                cur_fail = True
              n_error += 1
            else:
              cur_fail = True
              break

        if cur_fail is False:
          success += 1
        if countBit is True:
          error_idx_list.append(error_idx)
          n_error_list.append(n_error)

      if countBit is True:
        return success, error_idx_list, n_error_list
      else:
        return success

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[count_success:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



'''
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
            cnt += 1
            fail = True
            #break
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
'''
