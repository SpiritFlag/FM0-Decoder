import sys
import timeit
import numpy as np

from tqdm import tqdm
from global_vars import *
from read_set import *
from MLP.MLP import MLP
from MLP.test import MLP_test



def reshape_answer_set(answer_set):
  try:
    new_answer_set = []

    for idx in range(len(answer_set)):
      if (model_type == "one_bit" or model_type == "two_bit") and model_postpix == "_onehot":
        if answer_set[idx] == 0:
          new_answer_set.append([1, 0, 0, 0])
        elif answer_set[idx] == 1:
          new_answer_set.append([0, 1, 0, 0])
        elif answer_set[idx] == 2:
          new_answer_set.append([0, 0, 1, 0])
        elif answer_set[idx] == 3:
          new_answer_set.append([0, 0, 0, 1])
        else:
          raise ValueError("The value answer_set[" + str(idx) + "]= " + str(answer_set[idx]) + " must be within 0 to 3!")
      elif (model_type == "one_bit" or model_type == "two_bit") and model_postpix == "_lowhigh":
        if answer_set[idx] == 0:
          new_answer_set.append([0, 1])
        elif answer_set[idx] == 1:
          new_answer_set.append([1, 0])
        elif answer_set[idx] == 2:
          new_answer_set.append([0, 0])
        elif answer_set[idx] == 3:
          new_answer_set.append([1, 1])
        else:
          raise ValueError("The value answer_set[" + str(idx) + "]= " + str(answer_set[idx]) + " must be within 0 to 3!")
      elif model_type == "half_bit":
        if answer_set[idx] == 0:
          new_answer_set.append([0])
        elif answer_set[idx] == 1:
          new_answer_set.append([1])
        else:
          raise ValueError("The value answer_set[" + str(idx) + "]= " + str(answer_set[idx]) + " must be within 0 to 1!")

    return new_answer_set

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[reshape_answer_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def MLP_train(tmp):
  try:
    mlp = MLP()
    train_set, answer_set = read_train_set("train")
    validation_set, validation_answer_set = read_train_set("validation")
    answer_set = reshape_answer_set(answer_set)
    validation_answer_set = reshape_answer_set(validation_answer_set)

    train_time = timeit.default_timer()
    hist = mlp.train_model(np.array(train_set), np.array(answer_set), (np.array(validation_set), np.array(validation_answer_set)))
    print("\t\tTRAIN TIME= " + str(round(timeit.default_timer() - train_time, 3)) + " (sec)\n")

    MLP_test(model_full_path)
    return True

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP_train:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
