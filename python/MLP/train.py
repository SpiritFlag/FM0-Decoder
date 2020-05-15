import sys
import timeit
import numpy as np

from tqdm import tqdm
from global_vars import *
from MLP.global_vars import *
from read_set import *
from MLP.MLP import MLP
from MLP.reshape_answer_set import reshape_answer_set
from MLP.test import MLP_test



def MLP_train(path):
  try:
    mlp = MLP()
    train_set, answer_set = read_train_set(signal_path, "train", model_type)
    validation_train_set, validation_answer_set = read_train_set(signal_path, "validation", model_type)

    new_train_set = []
    new_answer_set = []
    random_index = np.arange(len(train_set))
    np.random.shuffle(random_index)
    for idx in tqdm(range(len(random_index)), desc="SHUFFLE", ncols=100, unit=" bit"):
      new_train_set.append(train_set[random_index[idx]])
      new_answer_set.append(answer_set[random_index[idx]])

    new_answer_set = reshape_answer_set(new_answer_set)
    validation_answer_set = reshape_answer_set(validation_answer_set)

    train_time = timeit.default_timer()
    hist = mlp.train_model(np.array(new_train_set), np.array(new_answer_set), (np.array(validation_train_set), np.array(validation_answer_set)))
    print("\t\tTRAIN TIME= " + str(round(timeit.default_timer() - train_time, 3)) + " (sec)\n")

    file = open(model_full_path + "/train_time", "w")
    file.write(str(timeit.default_timer() - train_time))
    file.close()

    ret = MLP_test(model_full_path)
    return True, ret[1]

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP_train:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
