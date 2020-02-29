import sys

from tqdm import tqdm
from global_vars import *



def determine_fail(predict, answer):
  try:
    if model_type == "bit_unit":
      if test_type == "corr":
        predict = predict.argmax()
        if ((predict == 0 or predict == 1) and answer != 0) or ((predict == 2 or predict == 3) and answer != 1):
          return True
      elif test_type == "shift":
        if (predict == 0 and answer != 0) or (predict == 1 and answer != 1):
          return True

    elif model_type == "whole":
      threshold = 0.5

      count = 0
      for n in range(databit_repitition):
        if (predict[n] < threshold and answer[n] < threshold) or (predict[n] > threshold and answer[n] > threshold):
          count += 1
      if count <= int(databit_repitition / 2):
        return True

      count = 0
      for n in range(databit_repitition, 2*databit_repitition):
        if (predict[n] < threshold and answer[n] < threshold) or (predict[n] > threshold and answer[n] > threshold):
          count += 1
      if count <= int(databit_repitition / 2):
        return True

    else:
      raise ValueError("No function matching with model type named \"" + model_type + model_postpix + "\"!")

    return False

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[determine_fail:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
