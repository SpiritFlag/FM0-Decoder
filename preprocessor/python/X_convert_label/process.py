import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from X_convert_label.global_vars import *
from X_convert_label.append_preamble import append_preamble
from X_convert_label.encode_data import encode_data



def process(file_name):
  try:
    postfix_list = ["train", "validation", "test"]

    for postfix in postfix_list:
      label = np.load(label_path + file_name + "_label_" + postfix + ".npy")

      for x in tqdm(range(len(label_type_list)), desc=postfix.upper(), ncols=100, unit=" type"):
        label_type = label_type_list[x]
        ispreamble = ispreamble_list[x]
        encoding_unit = encoding_unit_list[x]
        encoding_type = encoding_type_list[x]

        np_label = []

        for line in label:
          result = encode_data(line, encoding_unit, encoding_type)
          if ispreamble is True:
            result = np.append(append_preamble(encoding_unit, encoding_type), result)
          np_label.append(result)

        np.save(output_path + file_name + "_label_" + label_type + "_" + postfix, np_label)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[convert_label:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
