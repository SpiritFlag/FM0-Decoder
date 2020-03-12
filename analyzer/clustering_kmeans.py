import sys
import numpy as np

from tqdm import tqdm
from sklearn.cluster import KMeans

file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name_list = ["100_0_0"]
file_name_list = file_name_list_all

signal_path = "../data/XA_IQsignal/"
output_path = "../data/XA_kmeans/"

n_signal = 600



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

        fileI = open(output_path + file_name + "_index", "w")
        fileC = open(output_path + file_name + "_center", "w")
        for idx in tqdm(range(n_signal), desc="CLUSTERING", ncols=100, unit=" signal"):
          signal = np.transpose([Isignal[idx], Qsignal[idx]])
          kmeans = KMeans(n_clusters=2)
          kmeans = kmeans.fit(signal)
          labels = kmeans.predict(signal)
          centroids = kmeans.cluster_centers_

          cnt0 = 0
          cnt1 = 0
          for x in range(50):
            if labels[x] == 0:
              cnt0 += 1
            else:
              cnt1 += 1
          if cnt1 > cnt0:
            reverse = True
          else:
            reverse = False

          if reverse is False:
            fileC.write(str(centroids[0][0]) + " " + str(centroids[0][1]) + " " + str(centroids[1][0]) + " " + str(centroids[1][1]) + "\n")
          else:
            fileC.write(str(centroids[1][0]) + " " + str(centroids[1][1]) + " " + str(centroids[0][0]) + " " + str(centroids[0][1]) + "\n")

          for x in labels:
            if reverse is False:
              fileI.write(str(x) + " ")
            else:
              if x == 0:
                fileI.write("1 ")
              else:
                fileI.write("0 ")
          fileI.write("\n")

        fileI.close()
        fileC.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[main:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
