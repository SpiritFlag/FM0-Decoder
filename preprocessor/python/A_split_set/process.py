import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from A_split_set.global_vars import *



def subprocess(file_name, signal_path_list, signal_list, RNindex, postfix):
  try:
    npy_list = []
    for x in range(len(signal_list)):
      npy_list.append([])

    for idx in tqdm(range(len(RNindex)), desc=postfix.upper(), ncols=100, unit=" signal"):
      for x in range(len(signal_list)):
        signal = signal_list[x]
        npy_list[x].append(signal[RNindex[idx]])

    for x in range(len(signal_list)):
      signal_path = signal_path_list[x]
      if x < len(signal_list) - 1:
        np.save(signal_path + file_name + "_signal_" + postfix, npy_list[x])
      else:
        np.save(signal_path + file_name + "_answer_" + postfix, npy_list[x])

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[split_set:subprocess:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def process(file_name):
  try:
    signal = np.load(signal_path + file_name + "_signal.npy")
    signal_std = np.load(signal_path2 + file_name + "_signal.npy")
    signal_std_cliffing = np.load(signal_path3 + file_name + "_signal.npy")
    answer = np.load(answer_path + file_name + "_answer.npy")


    # please locate "answer" at the end of the list (according to line 23-26)
    signal_path_list = [signal_path, signal_path2, signal_path3, answer_path]
    signal_list = [signal, signal_std, signal_std_cliffing, answer]


    RNindex = np.arange(n_signal)
    np.random.shuffle(RNindex)
    RNtrain = RNindex[0:n_signal_train]
    RNvalidation = RNindex[n_signal_train:n_signal_train+n_signal_validation]
    RNtest = RNindex[n_signal_train+n_signal_validation:n_signal]


    subprocess(file_name, signal_path_list, signal_list, RNtrain, "train")
    subprocess(file_name, signal_path_list, signal_list, RNvalidation, "validation")
    subprocess(file_name, signal_path_list, signal_list, RNtest, "test")


  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[split_set:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
