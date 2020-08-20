import numpy as np
import timeit
from tqdm import tqdm

data_path = "../data/C_signal_std_cliffing/"
target_path = "../data/ZZ_npy_test/"

n_signal = 600

file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name_list = ["100_0_0"]
file_name_list = file_name_list_all

'''
for file_name in file_name_list:


  file = open(data_path + file_name + "_signal_test")
  signal_list = []

  for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
    signal = np.array([float(i) for i in file.readline().rstrip(" \n").split(" ")])
    signal_list.append(signal)

  signal_list = np.array(signal_list)
  file.close()

  np.save(target_path + file_name + "_signal_test", signal_list)
'''

'''
time = timeit.default_timer()

for file_name in file_name_list:
  file = open(data_path + file_name + "_signal_test")
  signal_list = []

  for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
    signal = np.array([float(i) for i in file.readline().rstrip(" \n").split(" ")])
    signal_list.append(signal)

  signal_list = np.array(signal_list)
  file.close()

exec_time = timeit.default_timer() - time
print("\n\t\tBINARY TIME= " + str(round(exec_time, 3)) + " (sec)\n")
'''


time = timeit.default_timer()

for file_name in file_name_list:
  signal_list = np.load(target_path + file_name + "_signal_test.npy")

  print(file_name)
  print(len(signal_list), len(signal_list[0]))
  print(signal_list)
  print("")
  print(signal_list[0])
  print("")

exec_time = timeit.default_timer() - time
print("\n\t\tNPY TIME= " + str(round(exec_time, 3)) + " (sec)\n")
