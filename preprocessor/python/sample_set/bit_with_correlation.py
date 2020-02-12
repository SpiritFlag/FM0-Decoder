import sys
import matplotlib.pyplot as plt

from tqdm import tqdm
from global_vars import *
from read_data import *



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

    return int(max_idx + n_bit * n_bit_preamble)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[detect_preamble:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def detect_bit(signal, databit, state):
  try:
    if databit == 0 and state == -1:
      mask = [-1.0] * n_half_bit
      mask += [1.0] * n_half_bit
      type = 0
    elif databit == 0 and state == 1:
      mask = [1.0] * n_half_bit
      mask += [-1.0] * n_half_bit
      type = 1
    elif databit == 1 and state == -1:
      mask = [-1.0] * n_bit
      type = 2
    elif databit == 1 and state == 1:
      mask = [1.0] * n_bit
      type = 3
    else:
      raise ValueError("Invalid databit and state")

    max_score = 0
    max_idx = 0

    for idx in range(int(2 * n_tolerance_bit + 1)):
      score = 0
      for mask_idx in range(len(mask)):
        score += mask[mask_idx] + signal[idx + mask_idx]
      if score > max_score:
        max_score = score
        max_idx = idx

    return max_idx, type

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[detect_bit:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def bit_with_correlation(file_name):
  try:
    databit = read_databit(databit_path + file_name)
    signal = read_signal(signal_path + file_name)

    file0 = open(output_path + file_name + "_0_sample", "w")
    file1 = open(output_path + file_name + "_1_sample", "w")
    file2 = open(output_path + file_name + "_2_sample", "w")
    file3 = open(output_path + file_name + "_3_sample", "w")
    file = [file0, file1, file2, file3]

    for idx in tqdm(range(n_signal), desc="PROCESSING", ncols=100, unit=" signal"):
      start = detect_preamble(signal[idx])
      state = -1

      for n in range(n_bit_data):
        shift, type = detect_bit(signal[idx][start-n_tolerance_bit:start+n_bit+n_tolerance_bit+1], databit[idx][n], state)
        start += (shift - n_tolerance_bit)

        for sample in signal[idx][start:start+n_bit]:
          file[type].write(str(sample) + " ")
        file[type].write("\n")

        start += n_bit
        if(databit[idx][n] == 1):
          state *= -1

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[bit_with_correlation:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
