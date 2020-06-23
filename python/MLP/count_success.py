import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from MLP.global_vars import *



def count_success(predict_set, answer_set, countBit=False):
  try:
    success = 0
    error_idx_list = []
    n_error_list = []

    if model_type == "bit":
      for idx in tqdm(range(len(answer_set)), desc="TESTING", ncols=100, unit=" signal"):
        if predict_set[idx].argmax() == answer_set[idx].argmax():
          success += 1

    elif model_type == "signal":
      threshold = 0.5

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
