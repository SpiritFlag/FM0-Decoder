import sys
import os
import numpy as np

from global_vars import *
from read_set import *
from MLP.global_vars import *
from MLP.MLP import MLP



def MLP_output(path):
  try:
    mlp = MLP()
    print("[Model path] " + str(os.listdir(model_path)) + "\n")
    model_name = input("Input the model name: ").rstrip("\n")
    path = model_path + model_name
    mlp.restore_model(path)
    os.mkdir(log_full_path)

    for file_name in file_name_list:
      try:
        print("\n\n\t*** " + file_name + " ***")
        test_set = read_test_set(signal_path, file_name)
        predict_set = mlp.test_model(np.array(test_set))

        file = open(log_full_path + "/" + file_name, "w")
        for predict in predict_set:
          file.write("\t".join([str(i) for i in predict]) + "\n")
        file.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[MLP_output:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    return False, True

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP_output:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
