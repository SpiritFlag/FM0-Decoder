import sys
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm

file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name_list = ["100_0_0"]
file_name_list = file_name_list_all

input_path = "../log/output_ccc_5544332211/stdev/"
input_path2 = "../log/output_ccc_5544332211/stdev_intra/"

n_signal = 600



if __name__ == "__main__":
  try:
    stdev = []
    stdev2 = []
    for file_name in file_name_list:
      try:
        file = open(input_path + file_name, "r")
        for idx in range(n_signal):
          line = file.readline().rstrip("\t\n").split("\t")
          stdev.extend([float(i) for i in line])
        file.close()

        file = open(input_path2 + file_name, "r")
        line = file.readline().rstrip("\t\n").split("\t")
        stdev2.extend([float(i) for i in line])
        file.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[main:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex))

    plt.hist(stdev, bins=np.arange(0, 0.5e-3, 1e-5), alpha=0.5, rwidth=0.8, label="stdev")
    #plt.show()
    plt.savefig(input_path + "fig1.png", dpi=300)
    plt.close()

    plt.hist(stdev2, bins=np.arange(0, 1, 1e-2), alpha=0.5, rwidth=0.8, label="stdev")
    #plt.show()
    plt.savefig(input_path + "fig2.png", dpi=300)
    plt.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex))
