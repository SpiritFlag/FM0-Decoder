import numpy as np

path = "../data/exp01_C_augment_random_x4/"
path2 = "../data/exp01_C_augment_random_x4_noise1/"

data = np.load(path + "100_0_0_signal_48.1_test.npy")
file = open("../log/tmp", "w")
file.write(" ".join([str(x) for x in data[0]]))
file.write("\n")

data = np.load(path2 + "100_0_0_signal_48.1_test.npy")
file.write(" ".join([str(x) for x in data[0]]))
file.close()
