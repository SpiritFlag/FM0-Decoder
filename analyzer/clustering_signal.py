import sys
import numpy as np

from tqdm import tqdm

file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name_list = ["100_0_0"]
file_name_list = file_name_list_all

signal_path = "../data/XA_IQsignal/"
cluster_path = "../data/XA_kmeans/"
output_path = "../data/XB_signal/"

n_signal = 600
n_sample = 6850



if __name__ == "__main__":
  try:
    for file_name in file_name_list:
      try:
        file = open(signal_path + file_name + "_RN0_Isignal_test", "r")
        Isignal = []
        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          line = file.readline().rstrip(" \n").split(" ")
          line = [float(i) for i in line]
          Isignal.append(line)
        file.close()

        file = open(signal_path + file_name + "_RN0_Qsignal_test", "r")
        Qsignal = []
        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          line = file.readline().rstrip(" \n").split(" ")
          line = [float(i) for i in line]
          Qsignal.append(line)
        file.close()

        file = open(cluster_path + file_name + "_center", "r")
        center = []
        for idx in range(n_signal):
          line = file.readline().rstrip(" \n").split(" ")
          line = [float(i) for i in line]
          center.append(line)
        file.close()

        file = open(output_path + file_name + "_RN0_signal_test", "w")

        for idx in tqdm(range(n_signal), desc="PROCESSING", ncols=100, unit=" signal"):
          for n in range(n_sample):
            a = np.sqrt((Isignal[idx][n] - center[idx][0]) ** 2 + (Qsignal[idx][n] - center[idx][1]) ** 2)
            b = np.sqrt((Isignal[idx][n] - center[idx][2]) ** 2 + (Qsignal[idx][n] - center[idx][3]) ** 2)
            file.write(str((2*a/(a+b))-1) + " ")
          file.write("\n")
        file.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[main:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
