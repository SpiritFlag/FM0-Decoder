import sys
import timeit
import numpy as np

from tqdm import tqdm
from global_vars import *
from read_set import *
from MLP.MLP import MLP
from MLP.reshape_answer_set import reshape_answer_set
from MLP.test import MLP_test



def MLP_train(tmp):
  try:
    mlp = MLP()
    train_set, answer_set = read_train_set("train")
    validation_set, validation_answer_set = read_train_set("validation")

    if (model_type == "one_bit" or model_type == "two_bit"):
      answer_set = reshape_answer_set(answer_set)
      validation_answer_set = reshape_answer_set(validation_answer_set)

    train_time = timeit.default_timer()
    hist = mlp.train_model(np.array(train_set), np.array(answer_set), (np.array(validation_set), np.array(validation_answer_set)))
    print("\t\tTRAIN TIME= " + str(round(timeit.default_timer() - train_time, 3)) + " (sec)\n")

    MLP_test(model_full_path)
    return True, True

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP_train:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
