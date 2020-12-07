import numpy as np
import matplotlib.pyplot as plt

#data_path = "data/exp01_B_signal_std/"
data_path = "data/exp01_C_augment_random_x8/"
#file_name = "100_r100_45"
file_name = "100_0_0"
#postfix = "_signal.npy"
postfix = "_signal_51.1_test.npy"

signal = np.load(data_path + file_name + postfix)

plt.plot(signal[0])
plt.show()
plt.close()
