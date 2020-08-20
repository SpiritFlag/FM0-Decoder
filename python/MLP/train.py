import sys
import timeit
import numpy as np

from tqdm import tqdm
from global_vars import *
from MLP.global_vars import *
from read_set import read_set
from MLP.MLP import MLP
from MLP.test import MLP_test



def MLP_train(path):
  try:
    mlp = MLP(size_hidden_layer, learning_rate)
    train_set, answer_set = read_set(signal_path, answer_path, answer_type, "train", file_name_list, is_shuffle=True)
    validation_train_set, validation_answer_set = read_set(signal_path, answer_path, answer_type, "validation", file_name_list)

    train_time = timeit.default_timer()
    hist = mlp.train_model(train_set, answer_set, validation_train_set, validation_answer_set)
    print("\t\tTRAIN TIME= " + str(round(timeit.default_timer() - train_time, 3)) + " (sec)\n")

    file = open(model_full_path + "/train_time", "w")
    file.write(str(timeit.default_timer() - train_time))
    file.close()

    ret = MLP_test(model_full_path)
    return True, ret[1]

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP_train:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
