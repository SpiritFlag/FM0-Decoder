import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from B_augment_sample.global_vars import *



def process(file_name):
  try:
    postfix_list = ["train", "validation", "test"]

    for postfix in postfix_list:
      signal = np.load(signal_path + file_name + "_signal_" + postfix + ".npy")

      for augment in augment_list:
        npy_signal = []

        for idx in tqdm(range(len(signal)), desc=postfix.upper()+" "+str(augment), ncols=100, unit=" signal"):
          augment_coefficient = augment_standard / (augment + np.random.rand())
          conv_len = int(n_sample / augment_coefficient) + 1
          margin = n_sample - conv_len
          if margin < 0:
            conv_len = n_sample

          result = []
          for x in range(conv_len):
            result.append(signal[idx][int(x*augment_coefficient)])

          end = result[-1]
          for x in range(margin):
            result.append(end)

          npy_signal.append(np.array(result))

        np.save(output_path + file_name + "_signal_" + str(augment) + "_" + postfix, npy_signal)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[augment_sample:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
