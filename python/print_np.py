import numpy as np

path = "data/exp01_B_signal_std/"
file_name = "100_r100_45_Isignal.npy"
idx_list = np.arange(3000)

data = np.load(path + file_name)
file = open("print_npy", "w")

file.write("\t\t " + path + file_name + "\n")

for idx in idx_list:
  file.write("\tidx= " + str(idx) + "\n")
  file.write(" ".join([str(i) for i in data[idx]]) + "\n")
