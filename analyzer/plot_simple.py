import sys
import itertools
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm

input_path = "../data/C_bit_with_correlation/"
file_name = "100_0_0_3_sample"

if __name__ == "__main__":
  try:
    file = open(input_path + file_name, "r")

    for idx in itertools.count():
      input = file.readline()
      if input == "":
        break
      elif idx % 2000 != 0:
        continue
      else:
        input = input.rstrip(" \n").split(" ")
        input = [float(i) for i in input]
        plt.plot(input, ".")
        plt.ylim([-1.5, 1.5])
        plt.title(file_name + " " + str(idx))
        plt.show()
        plt.close()

    file.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[plot_simple:" + str(tb.tb_lineno) + "] " + str(ex))
