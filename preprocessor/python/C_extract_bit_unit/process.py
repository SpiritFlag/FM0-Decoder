import sys

from tqdm import tqdm
from global_vars import *
from C_extract_bit_unit.global_vars import *
from C_extract_bit_unit.detect_preamble import detect_preamble
from C_extract_bit_unit.detect_bit import detect_bit



def process(signal, databit, file_name, set_name, set_size):
  try:
    if set_name == "_test":
      file = open(output_path + file_name + "_RN" + str(RN) + "_signal" + set_name, "w")
    else:
      file0 = open(output_path + file_name + "_RN" + str(RN) + "_signal" + set_name + "_0", "w")
      file1 = open(output_path + file_name + "_RN" + str(RN) + "_signal" + set_name + "_1", "w")
      file2 = open(output_path + file_name + "_RN" + str(RN) + "_signal" + set_name + "_2", "w")
      file3 = open(output_path + file_name + "_RN" + str(RN) + "_signal" + set_name + "_3", "w")
      file = [file0, file1, file2, file3]

    for idx in tqdm(range(set_size), desc="PROCESSING", ncols=100, unit=" signal"):
      start = detect_preamble(signal[idx])
      state = -1
      outlier = False

      list0 = []
      list1 = []
      list2 = []
      list3 = []
      list = [list0, list1, list2, list3]

      for n in range(n_bit_data):
        end = start + n_bit + n_tolerance_bit
        if end > n_sample:
          outlier = True
          break

        score, shift, type = detect_bit(signal[idx][start-n_half_bit-n_tolerance_bit:end+n_half_bit+1], databit[idx][n], state)
        start += (shift - n_tolerance_bit)

        if set_name == "_test":
          list[0].append(signal[idx][start-n_half_bit:start+n_bit+n_half_bit])
        elif score >= correlation_threshold:
          list[type].append(signal[idx][start-n_half_bit:start+n_bit+n_half_bit])

        start += n_bit
        if databit[idx][n] is 1:
          state *= -1

      if set_name == "_test":
        if outlier is False:
          for j in range(len(list[0])):
            for sample in list[0][j]:
              file.write(str(sample) + " ")
          file.write("\n")
        else:
          file.write(" \n")
      else:
        if outlier is False:
          for i in range(4):
            for j in range(len(list[i])):
              for sample in list[i][j]:
                file[i].write(str(sample) + " ")
              file[i].write("\n")

    if set_name == "_test":
      file.close()
    else:
      file0.close()
      file1.close()
      file2.close()
      file3.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[C_extract_bit_unit:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
