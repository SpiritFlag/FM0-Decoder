import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

#
# path = "misc/data/exp01_A_signal/"
# file_name = "100_0_0_Isignal.npy"
# #idx_list = np.arange(3000)
# idx_list = [0]
#
# data = np.load(path + file_name)
# file = open("doc/print_npy", "w")
#
# #file.write("\t\t " + path + file_name + "\n")
#
# for idx in idx_list:
#   #file.write("\tidx= " + str(idx) + "\n")
#   file.write(" ".join([str(i) for i in data[idx]]) + "\n")

file_name_list_all = []
# for a in ["100", "200", "300", "400"]:
#     for b in ["0", "l100", "r100"]:
#         for c in ["0", "45", "90", "135"]:
#             file_name_list_all.append(a + "_" + b + "_" + c)

# for a in ["45"]:
#     for b in ["100", "200", "300"]:
#         for c in ["0"]:
#             for d in ["0", "45", "90", "135"]:
#                 file_name_list_all.append(a + "_" + b + "_" + c + "_" + d)
#
# file_name_list = file_name_list_all
#
# path = "misc/data/exp02_B_signal/"
# for file_name in file_name_list:
#     dataI = np.load(path+file_name+"_Isignal.npy")
#     dataQ = np.load(path+file_name+"_Qsignal.npy")
#     data = np.load(path+file_name+"_signal.npy")
#     plt.title(file_name)
#     # plt.plot(dataI[0], dataQ[0], "*")
#     plt.plot(data[0])
#     plt.show()
#     plt.close()

dataI = np.load("../misc/data/exp08_B_signal/1_1_Isignal.npy")
dataQ = np.load("../misc/data/exp08_B_signal/1_1_Qsignal.npy")

for x in tqdm(range(400), desc="PROCESSING", ncols=100, unit=" signal"):
    plt.plot(dataI[x], dataQ[x], "*")
    plt.title(x+1)
    plt.savefig("../misc/tmp/1_1/" + str(x+1))
    plt.close()
