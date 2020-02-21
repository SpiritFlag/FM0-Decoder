import sys

from tqdm import tqdm
from global_vars import *



def detect_preamble(signal):
  try:
    mask = [1.0] * n_bit  # 1
    mask += [-1.0] * n_half_bit  # 2
    mask += [1.0] * n_half_bit
    mask += [-1.0] * n_bit  # 3
    mask += [1.0] * n_half_bit  # 4
    mask += [-1.0] * n_half_bit
    mask += [-1.0] * n_bit  # 5
    mask += [1.0] * n_bit  # 6

    max_score = 0
    max_idx = 0

    for idx in range(n_cw, n_extra):
      score = 0
      for mask_idx in range(len(mask)):
        score += mask[mask_idx] * signal[idx + mask_idx]
      if score > max_score:
        max_score = score
        max_idx = idx

    return max_idx

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[detect_preamble:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def generate_RNpreamble_set(file_name):
  try:
    file = open(signal_path + file_name + "_RN0_test", "r")
    fileD = open(databit_path + file_name + "_RN0_test", "r")
    fileS = open(output_path + "S/" + file_name + "_RN0_test", "w")
    fileF = open(output_path + "F/" + file_name + "_RN0_test", "w")
    fileDS = open(output_path + "DS/" + file_name + "_RN0_test", "w")
    fileDF = open(output_path + "DF/" + file_name + "_RN0_test", "w")

    fileIS = open("../data/tmp/" + file_name + "_indexS", "r")
    lineIS = fileIS.readline().rstrip(" ").split(" ")
    if len(lineIS) != 1:
      lineIS = [int(i) for i in lineIS]
    fileIS.close()

    fileIF = open("../data/tmp/" + file_name + "_indexF", "r")
    lineIF = fileIF.readline().rstrip(" ").split(" ")
    if len(lineIF) != 1:
      lineIF = [int(i) for i in lineIF]
    fileIF.close()

    curS = 0
    curF = 0

    for idx in range(n_RNtest):
      lineD = fileD.readline()
      line = file.readline()
      signal = line.rstrip(" \n").split(" ")

      if curS < len(lineIS) and idx == lineIS[curS]:
        if len(signal) != 1:
          fileS.write(line)
          fileDS.write(lineD)
        curS += 1
      if curF < len(lineIF) and idx == lineIF[curF]:
        if len(signal) != 1:
          fileF.write(line)
          fileDF.write(lineD)
        curF += 1

    file.close()
    fileD.close()
    fileS.close()
    fileF.close()
    fileDS.close()
    fileDF.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[generate_RNpreamble_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
