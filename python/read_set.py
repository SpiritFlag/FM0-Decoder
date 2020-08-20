import sys
import numpy as np

from tqdm import tqdm
from global_vars import *



def shuffle_set(signal, answer):
  try:
    RNindex = np.arange(len(signal))
    np.random.shuffle(RNindex)

    new_signal = []
    new_answer = []

    for idx in range(len(RNindex)):
      new_signal.append(signal[RNindex[idx]])
      new_answer.append(answer[RNindex[idx]])

    return np.array(new_signal), np.array(new_answer)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[shuffle_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def read_set(signal_path, answer_path, answer_type, postfix, file_name_list, is_shuffle=False):
  try:
    signal = []
    answer = []

    for x in tqdm(range(len(file_name_list)), desc="READING", ncols=100, unit=" file"):
      file_name = file_name_list[x]

      try:
        if augment_training is False:
          signal.extend(np.load(signal_path + file_name + "_signal_" + postfix + ".npy"))
          answer.extend(np.load(answer_path + file_name + "_answer_" + answer_type + "_" + postfix + ".npy"))
        else:
          for augment in augment_list:
            signal.extend(np.load(signal_path + file_name + "_signal_" + str(augment) + "_" + postfix + ".npy"))
            answer.extend(np.load(answer_path + file_name + "_answer_" + answer_type + "_" + postfix + ".npy"))

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[read_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    if is_shuffle is True:
      return shuffle_set(signal, answer)
    else:
      return np.array(signal), np.array(answer)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[read_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
