import sys
import numpy as np

from tqdm import tqdm
from IQcomplex import IQcomplex
from global_vars import *
from read_data import *



def kalman_filter(signal):
  try:
    predict = IQcomplex(signal[0].real, signal[0].imag)
    predict_error = IQcomplex(1, 1)
    kalman_gain = IQcomplex(1, 1)
    measurement_error = 1e-7

    for idx in range(1, n_cw+1):
      kalman_gain = predict_error.div(predict_error.s_add(measurement_error))
      predict = predict.mul(kalman_gain.s_rev_sub(1)).add(kalman_gain.mul(signal[idx]))
      predict_error = kalman_gain.s_rev_sub(1).mul(predict_error)

    return predict

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[kalman_filter:" + str(tb.tb_lineno) + "] " + str(ex))



def CW_kalman(file_name):
  try:
    signal = read_IQsignal(signal_path + file_name)

    file = open(output_path + file_name + "_signal", "w")
    for idx in tqdm(range(n_signal), desc="PROCESSING", ncols=100, unit=" signal"):
      center = kalman_filter(signal[idx])

      for n in range(n_sample):
        file.write(str(center.distance(signal[idx][n])) + " ")
      file.write("\n")
    file.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[CW_kalman:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
