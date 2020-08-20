import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from A_IQconvert.global_vars import *
from A_IQconvert.read_signal import read_signal
from A_IQconvert.kalman_filter import kalman_filter



def process(file_name):
  try:
    Isignal, Qsignal, answer = read_signal(file_name)

    npy_signal = []
    npy_signal_std = []
    npy_signal_std_cliffing = []


    for idx in tqdm(range(n_signal), desc="PROCESSING", ncols=100, unit=" signal"):
      signal = []
      Icenter, Qcenter = kalman_filter(Isignal[idx], Qsignal[idx])

      for n in range(n_sample):
        signal.append(np.sqrt((Isignal[idx][n] - Icenter) ** 2 + (Qsignal[idx][n] - Qcenter) ** 2))

      signal = np.array(signal)
      npy_signal.append(signal)


      signal_std = []
      signal_std_cliffing = []
      avg = np.mean(signal)
      std = np.std(signal)

      for sample in signal:
        sample_std = (sample - avg) / std
        signal_std.append(sample_std)

        if sample_std > 1:
          signal_std_cliffing.append(1)
        elif sample_std < -1:
          signal_std_cliffing.append(-1)
        else:
          signal_std_cliffing.append(sample_std)

      npy_signal_std.append(signal_std)
      npy_signal_std_cliffing.append(signal_std_cliffing)

    np.save(output_path + file_name + "_signal", npy_signal)
    np.save(output_path2 + file_name + "_signal", npy_signal_std)
    np.save(output_path3 + file_name + "_signal", npy_signal_std_cliffing)
    np.save(answer_output_path + file_name + "_answer", answer)


  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[IQconvert:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
