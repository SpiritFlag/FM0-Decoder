import sys
import timeit
import numpy as np

from global_vars import *
from MLP.global_vars import *
from MLP.MLP import MLP
from MLP.count_success import count_success



def process(model, file_name, test_set, answer_set):
  try:
    file = open(log_full_path + "_detail/" + file_name, "w")

    inference_time = timeit.default_timer()
    predict_set = model.test_model(test_set)
    inference_time = timeit.default_timer() - inference_time

    test_time = timeit.default_timer()
    success, error_idx, n_error = count_success(predict_set, np.hsplit(answer_set, int(size_output_layer / 4)), countBit=True)
    for idx in range(len(answer_set)):
      file.write(str(error_idx[idx]) + "\t" + str(n_error[idx]) + "\n")
    file.close()
    test_time = timeit.default_timer() - test_time

    return success, [inference_time, test_time]

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
