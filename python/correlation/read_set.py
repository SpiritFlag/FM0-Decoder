import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from correlation.global_vars import *



def read_set(file_name_list, postfix):
  try:
    signal = []
    label = []

    for x in tqdm(range(len(file_name_list)), desc="READING", ncols=100, unit=" file"):
      try:
        file_name = file_name_list[x]

        if augment_list == []:
          # signal.extend(np.load(signal_path + file_name + "_signal_train.npy"))
          # signal.extend(np.load(signal_path + file_name + "_signal_validation.npy"))
          signal.extend(np.load(signal_path + file_name + "_signal_test.npy"))
          # label.extend(np.load(label_path + file_name + "_label_" + label_type + "_train.npy"))
          # label.extend(np.load(label_path + file_name + "_label_" + label_type + "_validation.npy"))
          label.extend(np.load(label_path + file_name + "_label_" + label_type + "_test.npy"))
        else:
          for augment in augment_list:
            # signal.extend(np.load(signal_path + file_name + "_" + str(augment) + "_signal_train.npy"))
            # signal.extend(np.load(signal_path + file_name + "_" + str(augment) + "_signal_validation.npy"))
            signal.extend(np.load(signal_path + file_name + "_" + str(augment) + "_signal_test.npy"))
            # label.extend(np.load(label_path + file_name + "_label_" + label_type + "_train.npy"))
            # label.extend(np.load(label_path + file_name + "_label_" + label_type + "_validation.npy"))
            label.extend(np.load(label_path + file_name + "_label_" + label_type + "_test.npy"))

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[correlation:read_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    if cliffing is True:
        for x in signal:
            print(x)
            for idx in range(len(x)):
                if x[idx] > 1:
                    x[idx] = 1
                elif x[idx] < -1:
                    x[idx] = -1

    return np.array(signal), np.array(label)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[correlation:read_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
