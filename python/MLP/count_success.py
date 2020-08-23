import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from MLP.global_vars import *



def process_signal(predict_set, answer_set, countBit=False):
  try:
    cur_fail = False
    error_idx = -1
    n_error = 0

    if ispreamble is True:
      n_range = n_bit_preamble + n_bit_data
    else:
      n_range = n_bit_data

    if encoding_unit == "bit":
      n_range *= 2

    for bit in range(n_range):
      if encoding_type == "onehot":
        predict = np.array(predict_set[int(size_slice*bit):int(size_slice*(bit+1))]).argmax()
        answer = np.array(answer_set[int(size_slice*bit):int(size_slice*(bit+1))]).argmax()
      elif encoding_type == "regression":
        threshold = 0.5
        predict = predict_set[bit]
        if predict < threshold:
          predict = 0
        else:
          predict = 1
        answer = answer_set[bit]

      if predict == answer:
        continue

      if countBit is True:
        if cur_fail is False:
          error_idx = bit
          cur_fail = True
        n_error += 1
        continue
      else:
        cur_fail = True
        break

    return cur_fail, error_idx, n_error

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[count_success:process_signal:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def process_bit(predict_set, answer_set, countBit=False):
  try:
    cur_fail = False
    error_idx = -1
    n_error = 0

    for bit in range(n_bit_data):
      predict = predict_set[bit].argmax() + 1
      answer = answer_set[int(2*bit):int(2*(bit+1))]

      if (predict == 1 and answer[0] == 0 and answer[1] == 1) or\
        (predict == 2 and answer[0] == 1 and answer[1] == 0) or\
        (predict == 3 and answer[0] == 0 and answer[1] == 0) or\
        (predict == 4 and answer[0] == 1 and answer[1] == 1):
        continue

      if countBit is True:
        if cur_fail is False:
          error_idx = bit
          cur_fail = True
        n_error += 1
        continue
      else:
        cur_fail = True
        break

    return cur_fail, error_idx, n_error

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[count_success:process_bit:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def count_success(predict_set, answer_set, countBit=False):
  try:
    success = 0
    error_idx_list = []
    n_error_list = []

    for idx in tqdm(range(len(predict_set)), desc="TESTING", ncols=100, unit=" signal"):
      cur_fail = False
      error_idx = -1
      n_error = 0

      if model_type == "signal":
        cur_fail, error_idx, n_error = process_signal(predict_set[idx], answer_set[idx], countBit)
      elif model_type == "bit":
        cur_fail, error_idx, n_error = process_bit(predict_set[idx], answer_set[idx], countBit)

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
