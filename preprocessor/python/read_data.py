import sys

from tqdm import tqdm
from IQcomplex import IQcomplex
from global_vars import *



def read_IQsignal(file_path):
  try:
    fileI = open(file_path + "_Isignal", "r")
    fileQ = open(file_path + "_Qsignal", "r")
    signal_list = []

    for idx in tqdm(range(n_signal), desc="READING", ncols=100, unit=" signal"):
      signalI = fileI.readline().rstrip(" \n").split(" ")
      signalI = [float(i) for i in signalI]
      signalQ = fileQ.readline().rstrip(" \n").split(" ")
      signalQ = [float(i) for i in signalQ]

      signal = []
      for n in range(n_sample):
        signal.append(IQcomplex(signalI[n], signalQ[n]))
      signal_list.append(signal)

    fileI.close()
    fileQ.close()
    return signal_list

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[read_IQsignal:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
