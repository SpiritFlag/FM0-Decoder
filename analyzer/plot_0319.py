import sys
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm

input_path = "../data/Y_0319/"
output_path = "../data/Y_0319/"

n_line = 48
n_bit = 128

postfix = "_indexF"



if __name__ == "__main__":
  try:
    file = open(input_path + "0319_2" + postfix, "r")
    tot_cnt = np.zeros(n_bit, dtype="int")

    for i in tqdm(range(n_line), desc="PROCESSING", ncols=100, unit=" file"):
      try:
        line = file.readline().rstrip("\t\n").split("\t")
        file_name = line[0]
        cnt = [int(i) for i in line[1:]]
        tot_cnt += cnt

        plt.bar(range(0, 128, 1), cnt, alpha=0.5)
        plt.title(file_name)
        #plt.show()
        plt.savefig(output_path + file_name + ".png", dpi=300)
        plt.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[main:" + str(i) + ":" + str(tb.tb_lineno) + "] " + str(ex))

    plt.bar(range(0, 128, 1), tot_cnt, alpha=0.5)
    plt.title("TOTAL")
    #plt.show()
    plt.savefig(output_path + "TOTAL.png", dpi=300)
    plt.close()

    file.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex))
