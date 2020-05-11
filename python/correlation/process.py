import sys

from tqdm import tqdm
from global_vars import *
from correlation.decode_data import decode_data



def process(file_name, test_set, answer_set):
  try:
    file = open(log_path + "detail/" + file_name, "w")
    success = 0

    for idx in tqdm(range(len(answer_set)), desc="TESTING", ncols=100, unit=" signal"):
      fail = False
      error_idx = -1
      n_error = 0

      predict, pre_start, pre_score, bit_index, bit_score = decode_data(test_set[idx])

      for n in range(n_bit_data):
        if predict[n] != answer_set[idx][n]:
          if fail is False:
            error_idx = n
            fail = True
          n_error += 1

      if fail is False:
        success += 1

      file.write(str(pre_start) + "\t" + str(pre_score) + "\t" + str(error_idx) + "\t" + str(n_error) + "\n")
      file.write(" ".join([str(i) for i in bit_index]))
      file.write("\n")
      file.write(" ".join([str(i) for i in bit_score]))
      file.write("\n")

    file.close()
    return success, []

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[correlation:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
