import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from X_convert_answer.global_vars import *
from X_convert_answer.append_preamble import append_preamble
from X_convert_answer.encode_data import encode_data



def process(file_name):
  try:
    #postfix_list = ["train", "validation", "test"]
    postfix_list = ["test"]

    for postfix in postfix_list:
      answer = np.load(answer_path + file_name + "_answer_" + postfix + ".npy")

      for x in tqdm(range(len(answer_type_list)), desc=postfix.upper(), ncols=100, unit=" type"):
        answer_type = answer_type_list[x]
        ispreamble = ispreamble_list[x]
        encoding_unit = encoding_unit_list[x]
        encoding_type = encoding_type_list[x]

        np_answer = []

        for line in answer:
          result = encode_data(line, encoding_unit, encoding_type)
          if ispreamble is True:
            result = np.append(append_preamble(encoding_unit, encoding_type), result)
          np_answer.append(result)

        np.save(output_path + file_name + "_answer_" + answer_type + "_" + postfix, np_answer)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[convert_answer:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
