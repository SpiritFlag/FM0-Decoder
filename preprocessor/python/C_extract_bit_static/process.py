import sys

from tqdm import tqdm
from global_vars import *
from C_extract_bit_static.global_vars import *
from C_extract_bit_static.load import load
from C_extract_bit_static.detect_preamble import detect_preamble



def process(file_name, set_name):
  try:
    signal, databit = load(file_name, set_name)

    if set_name == "_test":
      file = open(output_path + file_name + "_signal" + set_name, "w")
    else:
      file0 = open(output_path + file_name + "_signal" + set_name + "_0", "w")
      file1 = open(output_path + file_name + "_signal" + set_name + "_1", "w")
      file2 = open(output_path + file_name + "_signal" + set_name + "_2", "w")
      file3 = open(output_path + file_name + "_signal" + set_name + "_3", "w")
      file_list = [file0, file1, file2, file3]

    for idx in tqdm(range(len(signal)), desc="PROCESSING", ncols=100, unit=" signal"):
      pre_start = detect_preamble(signal[idx])
      level = -1

      for n in range(n_bit_data):
        if set_name != "_test":
          if level == -1:
            if databit[idx][n] == 0:
              index = 0  # (H)LH(L)
            else:
              index = 2  # (H)LL(H)
          else:
            if databit[idx][n] == 0:
              index = 1  # (L)HL(H)
            else:
              index = 3  # (L)HH(L)

        signal_start = pre_start + int(n*n_bit_static) - n_half_bit
        if set_name == "_test":
          file.write(" ".join([str(i) for i in signal[idx][signal_start:signal_start+int(2*n_bit)]]) + " ")
        else:
          file_list[index].write(" ".join([str(i) for i in signal[idx][signal_start:signal_start+int(2*n_bit)]]) + "\n")
          if databit[idx][n] == 1:
            level *= -1

      if set_name == "_test":
        file.write("\n")

    if set_name == "_test":
      file.close()
    else:
      for file in file_list:
        file.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[C_extract_bit_static:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
