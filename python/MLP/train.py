import sys
import os
import timeit
import numpy as np

from tqdm import tqdm
from global_vars import *
from MLP.global_vars import *
from MLP.MLP import MLP
from MLP.read_set import read_set
from MLP.test import MLP_test



def MLP_train(path):
  try:
    if os.path.isdir(signal_path) is False:
      raise NameError("signal_path= " + signal_path + " does not exist!")

    if os.path.isdir(label_path) is False:
      raise NameError("label_path= " + label_path + " does not exist!")

    mlp = MLP(size_hidden_layer, learning_rate)
    train_set, label_set = read_set(file_name_list, "train", is_shuffle=True)
    validation_train_set, validation_label_set = read_set(file_name_list, "validation")

    train_time = timeit.default_timer()
    hist = mlp.train_model(train_set, label_set, validation_train_set, validation_label_set)
    print("\t\tTRAIN TIME= " + str(round(timeit.default_timer() - train_time, 3)) + " (sec)\n")

    file = open(model_full_path + "/train_time", "w")
    file.write(str(timeit.default_timer() - train_time))
    file.close()

    ret = MLP_test(model_full_path)
    return True, ret[1]
    #return False, False

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP_train:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
