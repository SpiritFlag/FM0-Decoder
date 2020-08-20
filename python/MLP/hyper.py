import sys
import timeit
import numpy as np

from tqdm import tqdm
from global_vars import *
from MLP.global_vars import *
from read_set import *
from MLP.MLP import MLP



def MLP_hyper(path):
  try:
    train_set, answer_set = read_train_set(signal_path, answer_path, answer_type, "_train", model_type)
    validation_train_set, validation_answer_set = read_train_set(signal_path, answer_path, answer_type, "_validation", model_type)

    new_train_set = []
    new_answer_set = []
    random_index = np.arange(len(train_set))
    np.random.shuffle(random_index)
    for idx in tqdm(range(len(random_index)), desc="SHUFFLE", ncols=100, unit=" bit"):
      new_train_set.append(train_set[random_index[idx]])
      new_answer_set.append(answer_set[random_index[idx]])

    size_hidden_layer_list = []
    for x in range(5, 8):
      size_hidden_layer = []
      for a in [5120, 4096, 3072, 2048, 1024]:
        for b in range(x):
          size_hidden_layer.append(a)
      size_hidden_layer_list.append(size_hidden_layer)

    #learning_rate = np.random.uniform(lr_low, lr_high, lr_size)
    #learning_rate = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]
    learning_rate = [1e-3, 1e-4, 1e-5, 1e-6]
    #learning_rate = [1e-5, 1e-6]
    #learning_rate = [1e-3]

    for hl in size_hidden_layer_list:
      for lr in learning_rate:
        mlp = MLP(hl, lr)
        print("\n\n\t\tTRAINING with learning rate= " + str(lr))
        print("\t\tHIDDEN LAYER= " + str(hl))
        mlp.train_model(np.array(new_train_set), np.array(new_answer_set), (np.array(validation_train_set), np.array(validation_answer_set)), save_model=False)

    return False, True

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP_hyper:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
