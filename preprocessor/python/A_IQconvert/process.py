import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from A_IQconvert.global_vars import *
from A_IQconvert.read_signal import read_signal
from A_IQconvert.kalman_filter import kalman_filter



def process(file_name):
  try:
    Isignal, Qsignal = read_signal(file_name)

    file = open(output_path + file_name + "_signal", "w")
    file_s = open(output_path_std + file_name + "_signal", "w")
    file_c = open(output_path_std_cliffing + file_name + "_signal", "w")

    for idx in tqdm(range(n_signal), desc="PROCESSING", ncols=100, unit=" signal"):
      Icenter, Qcenter = kalman_filter(Isignal[idx], Qsignal[idx])
      convert = []
      for n in range(n_sample):
        convert.append(np.sqrt((Isignal[idx][n] - Icenter) ** 2 + (Qsignal[idx][n] - Qcenter) ** 2))
      file.write(" ".join([str(i) for i in convert]))
      file.write("\n")

      convert = np.array(convert)
      avg = np.mean(convert)
      std = np.std(convert)

      for sample in convert:
        result = (sample - avg) / std
        file_s.write(str(result) + " ")
        
        if result > 1:
          file_c.write("1 ")
        elif result < -1:
          file_c.write("-1 ")
        else:
          file_c.write(str(result) + " ")

      file_s.write("\r\n")
      file_c.write("\r\n")

    file.close()
    file_s.close()
    file_c.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[A_IQconvert:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
