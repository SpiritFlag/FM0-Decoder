import sys
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm

prefix = "_mlp25"
input_path = "../data/Y_0324/"
output_path = "../data/Y_0324/fig" + prefix + "/"

n_line = 48



if __name__ == "__main__":
  try:
    file = open(input_path + prefix + "_hist", "r")
    tot1 = np.zeros(129, dtype="int")
    tot2 = np.zeros(129, dtype="int")
    tot3 = np.zeros(129, dtype="int")

    for i in tqdm(range(n_line), desc="PROCESSING", ncols=100, unit=" file"):
      try:
        file_name = file.readline().rstrip("\n")
        cnt1 = file.readline().rstrip("\t\n").split("\t")
        cnt1 = [int(i) for i in cnt1]
        tot1 += cnt1
        cnt2 = file.readline().rstrip("\t\n").split("\t")
        cnt2 = [int(i) for i in cnt2]
        tot2 += cnt2
        cnt3 = file.readline().rstrip("\t\n").split("\t")
        cnt3 = [int(i) for i in cnt3]
        tot3 += cnt3
        max = np.max(np.array([np.max(np.array(cnt1)), np.max(np.array(cnt2)), np.max(np.array(cnt3))]))

        plt.subplot(311)
        plt.title(file_name)
        plt.bar(range(0, 129, 1), cnt1, alpha=0.5)
        plt.ylim(0, max)
        plt.subplot(312)
        plt.bar(range(0, 129, 1), cnt2, alpha=0.5)
        plt.ylim(0, max)
        plt.subplot(313)
        plt.bar(range(0, 129, 1), cnt3, alpha=0.5)
        plt.ylim(0, max)
        #plt.show()
        plt.savefig(output_path + file_name + ".png", dpi=300)
        plt.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[main:" + str(i) + ":" + str(tb.tb_lineno) + "] " + str(ex))

    max = np.max(np.array([np.max(np.array(tot1)), np.max(np.array(tot2)), np.max(np.array(tot3))]))
    plt.subplot(311)
    plt.title("TOTAL")
    plt.bar(range(0, 129, 1), tot1, alpha=0.5)
    plt.ylim(0, max)
    plt.subplot(312)
    plt.bar(range(0, 129, 1), tot2, alpha=0.5)
    plt.ylim(0, max)
    plt.subplot(313)
    plt.bar(range(0, 129, 1), tot3, alpha=0.5)
    plt.ylim(0, max)
    #plt.show()
    plt.savefig(output_path + "TOTAL.png", dpi=300)
    plt.close()

    file.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex))
