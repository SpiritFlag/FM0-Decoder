import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from B_extract_bit.global_vars import *
from B_extract_bit.detect_preamble import detect_preamble



def process(file_name):
  try:
    postfix_list = ["train", "validation", "test"]

    for postfix in postfix_list:
      signal = np.load(signal_path + file_name + "_signal_" + postfix + ".npy")
      answer = np.load(answer_path + file_name + "_answer_" + postfix + ".npy")

      npy_signal1 = []
      npy_signal2 = []
      npy_signal3 = []
      npy_signal4 = []

      for idx in tqdm(range(len(signal)), desc=postfix.upper(), ncols=100, unit=" signal"):
        pre_start = detect_preamble(signal[idx])
        level = -1

        if postfix == "test":
          result = []

          for x in range(n_bit_data):
            signal_start = pre_start + int(x*n_bit_static) - n_half_bit
            result.extend(signal[idx][signal_start:signal_start+int(2*n_bit)])

          npy_signal1.append(np.array(result))

        else:
          for x in range(n_bit_data):
            signal_start = pre_start + int(x*n_bit_static) - n_half_bit
            sample = np.array(signal[idx][signal_start:signal_start+int(2*n_bit)])

            if level == -1:
              if answer[idx][x] == 0:  # (H)LH(L)
                npy_signal1.append(sample)
              else:                     # (H)LL(H)
                npy_signal3.append(sample)
                level *= -1
            else:
              if answer[idx][x] == 0:  # (L)HL(H)
                npy_signal2.append(sample)
              else:                     # (L)HH(L)
                npy_signal4.append(sample)
                level *= -1

      if postfix == "test":
        np.save(output_path + file_name + "_bit_" + postfix, npy_signal1)
      else:
        np.save(output_path + file_name + "_bit_" + postfix + "_1", npy_signal1)
        np.save(output_path + file_name + "_bit_" + postfix + "_2", npy_signal2)
        np.save(output_path + file_name + "_bit_" + postfix + "_3", npy_signal3)
        np.save(output_path + file_name + "_bit_" + postfix + "_4", npy_signal4)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[extract_bit:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
