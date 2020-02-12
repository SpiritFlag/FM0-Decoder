import sys

from tqdm import tqdm
from IQcomplex import IQcomplex
from global_vars import *



def read_databit(file_path):
  try:
    file = open(file_path + "_databit", "r")
    databit_list = []

    for idx in range(n_signal):
      databit = file.readline().rstrip(" \n")
      databit = [int(i) for i in databit]
      databit_list.append(databit)

    file.close()
    return databit_list

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[read_databit:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



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



def read_signal(file_path):
  try:
    file = open(file_path + "_signal", "r")
    signal_list = []

    for idx in tqdm(range(n_signal), desc="READING", ncols=100, unit=" signal"):
      signal = file.readline().rstrip(" \n").split(" ")
      signal = [float(i) for i in signal]
      signal_list.append(signal)

    file.close()
    return signal_list

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[read_signal:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
