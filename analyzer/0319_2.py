import sys
import numpy as np

from tqdm import tqdm

input_path = "../data/Y_0319/"
output_path = "../data/Y_0319/"

n_line = 48
n_bit = 128

postfix = "_indexF"



if __name__ == "__main__":
  try:
    fileR = open(input_path + "0319" + postfix, "r")
    fileW = open(output_path + "0319_2" + postfix, "w")

    for i in range(n_line):
      try:
        line = fileR.readline().rstrip("\t\n").split("\t")
        file_name = line[0]
        cnt = [int(i) for i in line[1:]]

        fileW.write(file_name + "\t")
        bit_cnt = np.zeros(n_bit+1, dtype="int")

        for x in cnt:
          bit_cnt[x] += 1

        for x in bit_cnt[1:]:
          fileW.write(str(x) + "\t")
        fileW.write("\n")

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[main:" + str(i) + ":" + str(tb.tb_lineno) + "] " + str(ex))

    fileR.close()
    fileW.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex))
