import sys
import timeit
import numpy as np

from tqdm import tqdm
from global_vars import *
from MLP.global_vars import *
from read_set import read_set
from MLP.MLP import MLP



def MLP_train_lr(path):
  try:
    train_set, answer_set = read_set(signal_path, answer_path, answer_type, "train", file_name_list, is_shuffle=True)
    validation_train_set, validation_answer_set = read_set(signal_path, answer_path, answer_type, "validation", file_name_list)

    size_hidden_layer_list = []
    for x in range(1,2):
      size_hidden_layer = []
      for a in [6144, 5120, 4096, 3072, 2048, 1024]:
        for b in range(x):
          size_hidden_layer.append(a)
      size_hidden_layer_list.append(size_hidden_layer)

    #learning_rate = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]
    learning_rate = [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]

    for hl in size_hidden_layer_list:
      for lr in learning_rate:
        mlp = MLP(hl, lr)
        print("\n\n\t\tTRAINING with learning rate= " + str(lr))
        print("\t\tHIDDEN LAYER= " + str(hl))
        mlp.train_model(train_set, answer_set, validation_train_set, validation_answer_set, save_model=False)

    return False, True

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP_train_lr:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
