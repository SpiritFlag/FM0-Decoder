import sys
import numpy as np

from global_vars import *
from correlation.detect_preamble import *



def decode_data(file_name, mlp, signal):
  try:
    start = detect_preamble(signal)
    state = -1
    tot_shift = 0
    shift_list = []
    decoded_bit = []

    for bit in range(n_bit_data):
      cur_start = int(start + n_bit*bit) + tot_shift

      if state == 1:
        state0 = 1
        state1 = 3
      else:
        state0 = 0
        state1 = 2

      max_score0 = 0
      max_score1 = 0
      max_idx0 = 0
      max_idx1 = 0

      predict_set = []
      for shift in [-3, -2, -1, 0, 1, 2, 3]:
        idx = cur_start - n_half_bit + shift
        if idx + 2*n_bit >= len(signal): continue
        predict_set.append(signal[idx:int(idx+2*n_bit)])

      '''
      print(bit, start, tot_shift, n_bit*bit, cur_start, len(predict_set), end=" ")
      for i in range(len(predict_set)):
        print(len(predict_set[i]), end=" ")
      print("")
      '''

      if len(predict_set) == 0:
        decoded_bit.append(-1)
      else:
        predict = mlp.test_model(np.array(predict_set))

        for shift in range(len(predict)):
          if predict[shift][state0] > max_score0:
            max_score0 = predict[shift][state0]
            max_idx0 = shift - 3
          if predict[shift][state1] > max_score1:
            max_score1 = predict[shift][state1]
            max_idx1 = shift - 3

        if max_score0 > max_score1:
          decoded_bit.append(0)
          tot_shift += max_idx0
        else:
          decoded_bit.append(1)
          tot_shift += max_idx1
          state *= -1
        shift_list.append(tot_shift)

    '''
    file = open("data/tmp_shift_shift/" + file_name + "_shift", "a")
    file.write(str(start) + " ")
    for shift in shift_list:
      file.write(str(shift) + " ")
    file.write("\n")
    file.close()
    '''

    return decoded_bit

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[decode_data:" + str(tb.tb_lineno) + "] " + str(ex))
