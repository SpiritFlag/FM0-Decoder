import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from MLP.global_vars import *



def read_set_signal(file_name_list, postfix):
  try:
    signal = []
    answer = []

    #for file_name in file_name_list:
    for x in tqdm(range(len(file_name_list)), desc="READING", ncols=100, unit=" file"):
      try:
        file_name = file_name_list[x]

        if augment_ratio == 1:
          signal.extend(np.load(signal_path + file_name + "_signal_" + postfix + ".npy"))
          answer.extend(np.load(answer_path + file_name + "_answer_" + answer_type + "_" + postfix + ".npy"))
        else:
          for augment in augment_list:
          #for augment_idx in tqdm(range(len(augment_list)), desc=file_name, ncols=100, unit=" file"):
            #augment = augment_list[augment_idx]
            signal.extend(np.load(signal_path + file_name + "_signal_" + str(augment) + "_" + postfix + ".npy"))
            answer.extend(np.load(answer_path + file_name + "_answer_" + answer_type + "_" + postfix + ".npy"))

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[MLP:read_set_signal:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    if augment_ratio > 1 and augment_noise_ratio > 1:
      new_answer = []
      for x in answer:
        for y in range(augment_noise_ratio):
          new_answer.append(x)
      #print(len(signal), len(new_answer))
      return signal, new_answer
    else:
      #print(len(signal), len(answer))
      return signal, answer

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP:read_set_signal:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def read_set_bit(file_name_list, postfix):
  try:
    signal = []
    answer = []

    for x in tqdm(range(len(file_name_list)), desc="READING", ncols=100, unit=" file"):
      try:
        file_name = file_name_list[x]

        if postfix == "train":
          for x in range(1, 5):
            read = np.load(signal_path + file_name + "_bit_" + postfix + "_" + str(x) + ".npy")
            signal.extend(read)

            if x == 1:
              ans = [1, 0, 0, 0]
            elif x == 2:
              ans = [0, 1, 0, 0]
            elif x == 3:
              ans = [0, 0, 1, 0]
            elif x == 4:
              ans = [0, 0, 0, 1]

            for y in range(len(read)):
              answer.append(ans)

        else:
          signal.extend(np.load(signal_path + file_name + "_bit_" + postfix + ".npy"))
          answer.extend(np.load(answer_path + file_name + "_answer_" + answer_type + "_" + postfix + ".npy"))

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[MLP:read_set_bit:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    return signal, answer

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP:read_set_bit:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



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
    print("[MLP:shuffle_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def read_set(file_name_list, postfix, is_shuffle=False):
  try:
    if model_type == "signal":
      signal, answer = read_set_signal(file_name_list, postfix)
    elif model_type == "bit":
      signal, answer = read_set_bit(file_name_list, postfix)

    if is_shuffle is True:
      return shuffle_set(signal, answer)
    else:
      return np.array(signal), np.array(answer)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP:read_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
