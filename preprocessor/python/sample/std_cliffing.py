import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from read_data import *



def std_cliffing(file_name):
  try:
    signal = read_signal(signal_path + file_name)

    file = open(output_path + file_name + "_signal", "w")
    file2 = open(output_path2 + file_name + "_signal", "w")
    for idx in tqdm(range(n_signal), desc="PROCESSING", ncols=100, unit=" signal"):
      avg = 0
      for sample in signal[idx]:
        avg += sample
      avg /= n_sample

      std = 0
      for sample in signal[idx]:
        std += (sample - avg) ** 2
      std = np.sqrt(std / n_sample)

      for sample in signal[idx]:
        value = (sample - avg) / std
        file.write(str(value) + " ")
        if value > 1:
          file2.write("1 ")
        elif value < -1:
          file2.write("-1 ")
        else:
          file2.write(str(value) + " ")
      file.write("\n")
      file2.write("\n")
    file.close()
    file2.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[std_cliffing:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
