import sys

from tqdm import tqdm
from global_vars import *



def process(file_name, test_set, label_set):
  try:
    file = open(log_full_path + "_detail/" + file_name, "w")
    success = 0
    tot_n_error = 0

    for idx in tqdm(range(len(label_set)), desc="TESTING", ncols=100, unit=" signal"):
      fail = False
      error_idx = -1
      n_error = 0

      predict, pre_start, pre_score, bit_index, bit_score = decode_data(test_set[idx])

      for n in range(n_bit_data):
        if predict[n] != label_set[idx][n]:
          if fail is False:
            error_idx = n
            fail = True
          n_error += 1
          file.write(str(n+1) + "\t")

      if fail is False:
        success += 1
      file.write("\n")

      #if idx == 0:
        #print(test_set[idx].tolist())
        # print("\n", predict, "\n", label_set[idx])
        # print(bit_index)
        # print(bit_score)
        # print(error_idx, n_error)

      tot_n_error += n_error
      print(f"\tacc: {success/(idx+1):6.4f}\tBER: {tot_n_error/((idx+1)*n_bit_data):6.4f}", end="\r")

      file.write(str(pre_start) + "\t" + str(pre_score) + "\t" + str(error_idx) + "\t" + str(n_error) + "\n")
      file.write(" ".join([str(i) for i in bit_index]))
      file.write("\n")
      file.write(" ".join([str(i) for i in bit_score]))
      file.write("\n")

    file.close()
    return success, tot_n_error, []

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[clustering:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
