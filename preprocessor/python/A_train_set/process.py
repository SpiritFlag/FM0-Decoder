import sys
import gc
import numpy as np

from tqdm import tqdm
from global_vars import *
from A_train_set.global_vars import *



def process():
  try:
    signal = []
    label_list = []
    for x in range(len(label_type_list)):
      label_list.append([])

    for x in tqdm(range(len(file_name_list)), desc="READING", ncols=100, unit=" file"):
      try:
        file_name = file_name_list[x]

        if augment_ratio == 1:
          i = np.load(signal_path + file_name + "_Isignal_train.npy")
          q = np.load(signal_path + file_name + "_Qsignal_train.npy")
          for idx in range(len(i)):
            signal.append(np.array([np.array([i[idx], q[idx]]).transpose()]))
          for idx in range(len(label_type_list)):
            label_list[idx].extend(np.load(label_path + file_name + "_label_" + label_type_list[idx] + "_train.npy"))
        else:
          for augment in augment_list:
            i = np.load(signal_path + file_name + "_Isignal_" + str(augment) + "_train.npy")
            q = np.load(signal_path + file_name + "_Qsignal_" + str(augment) + "_train.npy")
            for idx in range(len(i)):
              signal.append(np.array([np.array([i[idx], q[idx]]).transpose()]))
            for idx in range(len(label_type_list)):
              label_list[idx].extend(np.load(label_path + file_name + "_label_" + label_type_list[idx] + "_train.npy"))

        gc.collect()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[train_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    RNindex = np.arange(len(signal))
    np.random.shuffle(RNindex)

    if len(signal) % split_ratio == 0:
      n_file = int(len(signal) / split_ratio)
    else:
      n_file = int(len(signal) / split_ratio) + 1

    for x in tqdm(range(n_file), desc="WRITING", ncols=100, unit=" file"):
      index = RNindex[int(x*split_ratio):int((x+1)*split_ratio)]

      np_signal = []
      for idx in index:
        np_signal.append(signal[idx])
      np.save(output_path + str(x), np.array(np_signal))

      for y in range(len(label_type_list)):
        np_label = []
        for idx in index:
          np_label.append(label_list[y][idx])
        np.save(label_output_path + label_type_list[y] + "_" + str(x), np.array(np_label))

      gc.collect()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[train_set:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
