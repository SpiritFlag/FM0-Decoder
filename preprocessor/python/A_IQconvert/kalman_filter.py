import sys

from global_vars import *



def kalman_filter_process(signal):
  try:
    predict = signal[0]
    predict_error = 1
    kalman_gain = 1
    measurement_error = 1e-7

    for idx in range(1, n_cw+1):
      kalman_gain = predict_error / (predict_error + measurement_error)
      predict = predict * (1 - kalman_gain) + kalman_gain * signal[idx]
      predict_error = (1 - kalman_gain) * predict_error

    return predict

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[IQconvert:kalman_filter_process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def kalman_filter(Isignal, Qsignal):
  try:
    Ipredict = kalman_filter_process(Isignal)
    Qpredict = kalman_filter_process(Qsignal)

    return Ipredict, Qpredict

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[IQconvert:kalman_filter:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
