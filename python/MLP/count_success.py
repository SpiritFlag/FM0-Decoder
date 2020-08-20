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
      if countBit is False:
        for idx in tqdm(range(len(answer_set)), desc="TESTING", ncols=100, unit=" signal"):
          if predict_set[idx].argmax() == answer_set[idx].argmax():
            success += 1
      else:
        for idx in tqdm(range(len(answer_set)), desc="TESTING", ncols=100, unit=" signal"):
          cur_fail = False
          error_idx = -1
          n_error = 0

          for bit in range(n_bit_data):
            predict = predict_set[idx][bit].argmax()
            answer = answer_set[idx][bit]

            if predict == 0 or predict == 1:
              predict_bit = 0
            elif predict == 2 or predict == 3:
              predict_bit = 1

            if predict_bit != answer:
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

    elif model_type == "signal":
      for idx in tqdm(range(len(predict_set)), desc="TESTING", ncols=100, unit=" signal"):
        cur_fail = False
        error_idx = -1
        n_error = 0

        if ispreamble is True:
          n_range = n_bit_preamble + n_bit_data
        else:
          n_range = n_bit_data

        if encoding_unit == "bit":
          n_range *= 2

        # decoding
        for bit in range(n_range):
          if encoding_type == "onehot":
            predict = np.array(predict_set[idx][int(size_slice*bit):int(size_slice*(bit+1))]).argmax()
            answer = np.array(answer_set[idx][int(size_slice*bit):int(size_slice*(bit+1))]).argmax()
          elif encoding_type == "regression":
            threshold = 0.5
            predict = predict_set[idx][bit]
            if predict < threshold:
              predict = 0
            else:
              predict = 1
            answer = answer_set[idx][bit]

          if predict != answer:
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
