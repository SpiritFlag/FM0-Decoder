import sys
import matplotlib.pyplot as plt

from tqdm import tqdm

path = "../data/D_bit_unit_std/"



if __name__ == "__main__":
  try:
    file = open(path + "_log", "r")
    value = file.readline().rstrip(" \n").split(" ")
    value = [float(i) for i in value]
    file.close()

    plt.hist(value, bins=range(-150, 160, 10), alpha=0.5, rwidth=0.8)
    plt.show()
    plt.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[hist_correlation_value:" + str(tb.tb_lineno) + "] " + str(ex))
