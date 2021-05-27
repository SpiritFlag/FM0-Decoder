import sys
import gc
import timeit
import numpy as np

from tqdm import tqdm
from global_vars import *
from MLP.global_vars import *



def read_set_train():
  try:
    remainder = len(np.load(signal_path + train_set_prefix + "label/" + label_type + "_" + str(n_file - 1) + ".npy"))
    signal = np.zeros((int(split_ratio*(n_file-1)+remainder), 1, n_sample, 2))
    label = np.zeros((int(split_ratio*(n_file-1)+remainder), size_output_layer))

    for x in tqdm(range(n_file), desc="READING", ncols=100, unit=" file"):
      st = int(x*split_ratio)
      ed = int((x+1)*split_ratio)
      signal[st:ed] = np.load(signal_path + train_set_prefix + str(x) + ".npy")
      label[st:ed] = np.load(signal_path + train_set_prefix + "label/" + label_type + "_" + str(x) + ".npy")

    return signal, label

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP:read_set_train:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def read_set_signal(file_name_list, postfix):
  try:
    signal = []
    label = []

    #for file_name in file_name_list:
    for x in tqdm(range(len(file_name_list)), desc="READING", ncols=100, unit=" file"):
      try:
        file_name = file_name_list[x]

        if augment_ratio == 1:
          signal.extend(np.load(signal_path + file_name + "_signal_" + postfix + ".npy"))
          label.extend(np.load(label_path + file_name + "_label_" + label_type + "_" + postfix + ".npy"))
        else:
          for augment in augment_list:
          #for augment_idx in tqdm(range(len(augment_list)), desc=file_name, ncols=100, unit=" file"):
            #augment = augment_list[augment_idx]
            signal.extend(np.load(signal_path + file_name + "_signal_" + str(augment) + "_" + postfix + ".npy"))
            label.extend(np.load(label_path + file_name + "_label_" + label_type + "_" + postfix + ".npy"))

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[MLP:read_set_signal:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    return np.array(signal), np.array(label)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP:read_set_signal:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def read_set_CNN(file_name_list, postfix):
  try:
    n_size = len(np.load(label_path + file_name_list[0] + "_label_" + label_type + "_" + postfix + ".npy"))
    signal = np.zeros((int(n_size * augment_ratio * len(file_name_list)), 1, n_sample, 2))
    label = np.zeros((int(n_size * augment_ratio * len(file_name_list)), size_output_layer))

    pbar = tqdm(total=int(augment_ratio * len(file_name_list)), desc="READING", ncols=100, unit=" file")
    x = 0

    for file_name in file_name_list:
      try:
        if augment_ratio == 1:
          i = np.load(signal_path + file_name + "_Isignal_" + postfix + ".npy")
          q = np.load(signal_path + file_name + "_Qsignal_" + postfix + ".npy")
          signal[int(x*n_size):int((x+1)*n_size)] = np.expand_dims(np.swapaxes(np.array([i, q]).transpose(), 0, 1), axis=1)
          label[int(x*n_size):int((x+1)*n_size)] = np.load(label_path + file_name + "_label_" + label_type + "_" + postfix + ".npy")
          x += 1
          pbar.update(1)
        else:
          for augment in augment_list:
            i = np.load(signal_path + file_name + "_" + str(augment) + "_Isignal_" + postfix + ".npy")
            q = np.load(signal_path + file_name + "_" + str(augment) + "_Qsignal_" + postfix + ".npy")
            signal[int(x*n_size):int((x+1)*n_size)] = np.expand_dims(np.swapaxes(np.array([i, q]).transpose(), 0, 1), axis=1)
            label[int(x*n_size):int((x+1)*n_size)] = np.load(label_path + file_name + "_label_" + label_type + "_" + postfix + ".npy")
            x += 1
            pbar.update(1)

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[MLP:read_set_CNN:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    pbar.close()

    return signal, label

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP:read_set_CNN:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def read_set_bit(file_name_list, postfix):
  try:
    signal = []
    label = []

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
              label.append(ans)

        else:
          signal.extend(np.load(signal_path + file_name + "_bit_" + postfix + ".npy"))
          label.extend(np.load(label_path + file_name + "_label_" + label_type + "_" + postfix + ".npy"))

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[MLP:read_set_bit:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    return signal, label

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP:read_set_bit:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def shuffle_set(signal, label):
  try:
    RNindex = np.arange(len(signal))
    np.random.shuffle(RNindex)

    return signal[RNindex], label[RNindex]

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP:shuffle_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def read_set(file_name_list, postfix, is_shuffle=False):
  try:

    if postfix == "train":
      if pre_shuffled is True:
        return read_set_train()
      else:
        signal, label = read_set_CNN(file_name_list, postfix)
        shuffle_time = timeit.default_timer()
        print("\tSHUFFLE TRAIN SET..")
        signal, label = shuffle_set(signal, label)
        print(f"\t\tSHUFFLE TIME= {timeit.default_timer()-shuffle_time:.3f} (sec)")
        return signal, label


    if model_type == "signal":
      return read_set_signal(file_name_list, postfix)
    elif model_type == "CNN":
      return read_set_CNN(file_name_list, postfix)
    elif model_type == "bit":
      return read_set_bit(file_name_list, postfix)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP:read_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
