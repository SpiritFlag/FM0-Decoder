import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from D_augment_sample.global_vars import *
from D_augment_sample.load import load



def process(file_name):
  try:
    signal_list = load(file_name)

    for augment in augment_list:
      postfix_list = ["_train", "_validation", "_test"]
      for n_postfix in range(len(postfix_list)):
        postfix = postfix_list[n_postfix]

        file = open(output_path + file_name + "_signal_" + str(augment) + postfix, "w")
        for idx in tqdm(range(len(signal_list[n_postfix])), desc="PROCESSING "+str(augment), ncols=100, unit=" signal"):
          augment_coefficient = augment_standard / (augment + np.random.rand())
          conv_len = int(n_sample / augment_coefficient) + 1
          margin = new_n_sample - conv_len

          for x in range(conv_len):
            file.write(str(signal_list[n_postfix][idx][int(x*augment_coefficient)]) + " ")
          for x in range(int(margin)):
            file.write("-1 ")
          file.write("\n")

          # double (remove when finished)
          augment_coefficient = augment_standard / (augment + np.random.rand())
          conv_len = int(n_sample / augment_coefficient) + 1
          margin = new_n_sample - conv_len

          for x in range(conv_len):
            file.write(str(signal_list[n_postfix][idx][int(x*augment_coefficient)]) + " ")
          for x in range(int(margin)):
            file.write("-1 ")
          file.write("\n")
        file.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[D_augment_sample:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
