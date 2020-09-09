import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from Y_analysis.global_vars import *



def process(file_name):
  try:
    signal = np.load(signal_path + file_name + "_signal.npy")

    file = open(compare_path + file_name + "_signal", "r")
    c_signal = []
    for idx in tqdm(range(n_signal), desc="READING", ncols=100, unit=" signal"):
      c_signal.append([float(i) for i in file.readline().rstrip(" \n").split(" ")])
    file.close()

    n_error = 0
    for idx in tqdm(range(n_signal), desc="COMPARING", ncols=100, unit=" signal"):
      error = 0
      for x in range(n_sample):
        if signal[idx][x] != c_signal[idx][x]:
          error += 1
      if error != 0:
        n_error += 1
        print("\tERROR\t" + str(idx) + "\t" + str(x) + "\t" + str(error))
    print("\t\tERROR RATE= " + str(n_error) + " / " + str(n_signal) + "\t(" + str(round(100 * n_error / n_signal, 2)) + "%)\n")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[analysis:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
