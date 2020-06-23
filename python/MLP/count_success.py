import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from MLP.global_vars import *



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

        # reshape predcit set
        predict = []
        if test_type == 1 or test_type == 2:
          for bit in range(int(2*(n_bit_preamble + n_bit_data))):
            predict.append(predict_set[idx][int(amp_rep*bit)])
        elif test_type == 3:
          for bit in range(int(2*(n_bit_preamble + n_bit_data))):
            predict.append(np.mean(predict_set[idx][int(amp_rep*bit):int(amp_rep*(bit+1))]))

        # mask set
        if test_type == 2 or test_type == 3:
          mask0L = [1, 0, 1, 0]
          mask0H = [0, 1, 0, 1]
          mask1L = [1, 0, 0, 1]
          mask1H = [0, 1, 1, 0]
          level = -1
          predict.append(0.5)

        # decoding
        for bit in range(n_bit_data):
          answer = answer_set[idx][bit]

          if test_type == 1:
            level1 = predict[int(2 * (bit + n_bit_preamble))] - threshold
            level2 = predict[int(2 * (bit + n_bit_preamble) + 1)] - threshold

            if not((level1 * level2 < 0 and answer == 0) or (level1 * level2 > 0 and answer == 1)):
              if countBit is True:
                if cur_fail is False:
                  error_idx = bit
                  cur_fail = True
                n_error += 1
                continue
              else:
                cur_fail = True
                break

          elif test_type == 2 or test_type == 3:
            if level == -1:
              mask0 = mask0L
              mask1 = mask1L
            else:
              mask0 = mask0H
              mask1 = mask1H

            score0 = 0
            score1 = 0
            for x in range(4):
              score0 += mask0[x] * predict[2 * (bit + n_bit_preamble) - 1 + x]
              score1 += mask1[x] * predict[2 * (bit + n_bit_preamble) - 1 + x]

            if score1 >= score0:
              level *= -1

            if not ((score0 > score1 and answer == 0) or (score0 < score1 and answer == 1)):
              if countBit is True:
                if cur_fail is False:
                  error_idx = bit
                  cur_fail = True
                n_error += 1
                continue
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
