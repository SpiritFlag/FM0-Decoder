import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from A_IQconvert.global_vars import *
from A_IQconvert.kalman_filter import kalman_filter



def process(file_name):
  try:
    Isignal = np.load(signal_path + file_name + "_Isignal.npy")
    Qsignal = np.load(signal_path + file_name + "_Qsignal.npy")

    npy_signal = []
    npy_signal_std = []
    npy_signal_std_cliffing = []

    npy_Isignal = []
    npy_Qsignal = []
    npy_Isignal_std = []
    npy_Qsignal_std = []
    npy_Isignal_std_cliffing = []
    npy_Qsignal_std_cliffing = []


    for idx in tqdm(range(n_signal), desc="PROCESSING", ncols=100, unit=" signal"):
      signal = []
      Icenter, Qcenter = kalman_filter(Isignal[idx], Qsignal[idx])

      for n in range(n_sample):
        signal.append(np.sqrt((Isignal[idx][n] - Icenter) ** 2 + (Qsignal[idx][n] - Qcenter) ** 2))

      signal = np.array(signal)
      _Isignal = np.array(Isignal[idx])
      _Qsignal = np.array(Qsignal[idx])

      npy_signal.append(signal)
      npy_Isignal.append(_Isignal)
      npy_Qsignal.append(_Qsignal)


      signal_std = []
      signal_std_cliffing = []
      Isignal_std = []
      Isignal_std_cliffing = []
      Qsignal_std = []
      Qsignal_std_cliffing = []

      avg = np.mean(signal)
      std = np.std(signal)
      Iavg = np.mean(_Isignal)
      Istd = np.std(_Isignal)
      Qavg = np.mean(_Qsignal)
      Qstd = np.std(_Qsignal)

      for x in range(len(signal)):
        sample_std = (signal[x] - avg) / std
        Isample_std = (_Isignal[x] - Iavg) / Istd
        Qsample_std = (_Qsignal[x] - Qavg) / Qstd

        signal_std.append(sample_std)
        Isignal_std.append(Isample_std)
        Qsignal_std.append(Qsample_std)

        if sample_std > 1:
          signal_std_cliffing.append(1)
        elif sample_std < -1:
          signal_std_cliffing.append(-1)
        else:
          signal_std_cliffing.append(sample_std)

        if Isample_std > 1:
          Isignal_std_cliffing.append(1)
        elif Isample_std < -1:
          Isignal_std_cliffing.append(-1)
        else:
          Isignal_std_cliffing.append(Isample_std)

        if Qsample_std > 1:
          Qsignal_std_cliffing.append(1)
        elif Qsample_std < -1:
          Qsignal_std_cliffing.append(-1)
        else:
          Qsignal_std_cliffing.append(Qsample_std)

      npy_signal_std.append(signal_std)
      npy_signal_std_cliffing.append(signal_std_cliffing)
      npy_Isignal_std.append(Isignal_std)
      npy_Isignal_std_cliffing.append(Isignal_std_cliffing)
      npy_Qsignal_std.append(Qsignal_std)
      npy_Qsignal_std_cliffing.append(Qsignal_std_cliffing)

    np.save(output_path + file_name + "_signal", npy_signal)
    np.save(output_path2 + file_name + "_signal", npy_signal_std)
    np.save(output_path3 + file_name + "_signal", npy_signal_std_cliffing)
    np.save(output_path + file_name + "_Isignal", npy_Isignal)
    np.save(output_path2 + file_name + "_Isignal", npy_Isignal_std)
    np.save(output_path3 + file_name + "_Isignal", npy_Isignal_std_cliffing)
    np.save(output_path + file_name + "_Qsignal", npy_Qsignal)
    np.save(output_path2 + file_name + "_Qsignal", npy_Qsignal_std)
    np.save(output_path3 + file_name + "_Qsignal", npy_Qsignal_std_cliffing)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[IQconvert:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
