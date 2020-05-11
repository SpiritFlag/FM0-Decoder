import sys

from tqdm import tqdm
from global_vars import *
from C_extract_bit_unit.global_vars import *
from C_extract_bit_unit.load import load
from C_extract_bit_unit.decode_data import decode_data



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
      decoded_bit, decoded_index = decode_data(signal[idx], databit[idx])

      if set_name == "_test":
        for n in range(n_bit_data):
          if len(decoded_bit[n]) == 0:
            file.write("-1 ")
            break
          else:
            file.write(" ".join([str(i) for i in decoded_bit[n]]) + " ")
        file.write("\n")
      else:
        for n in range(n_bit_data):
          if len(decoded_bit[n]) == 0:
            break
          else:
            file_list[decoded_index[n]].write(" ".join([str(i) for i in decoded_bit[n]]) + "\n")

    if set_name == "_test":
      file.close()
    else:
      for file in file_list:
        file.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[C_extract_bit_unit:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
