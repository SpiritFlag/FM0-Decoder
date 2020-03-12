import sys
import numpy as np

from tqdm import tqdm

file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name_list = ["100_0_90"]
file_name_list = file_name_list_all

signal_path = "../data/C_signal_std_full/"
signal_path_2 = "../data/XB_signal/"
output_path = "../data/Y_full_bitscore/"

n_signal = 600
n_sample = 6850
n_cw = 50
n_bit = 50
n_half_bit = int(n_bit / 2)
n_tolerance_bit = 2
n_bit_preamble = 6
n_bit_data = 128
n_extra = int(n_sample - n_bit * (n_bit_preamble + n_bit_data))



def detect_preamble(signal):
  mask = [1.0] * n_bit  # 1
  mask += [-1.0] * n_half_bit  # 2
  mask += [1.0] * n_half_bit
  mask += [-1.0] * n_bit  # 3
  mask += [1.0] * n_half_bit  # 4
  mask += [-1.0] * n_half_bit
  mask += [-1.0] * n_bit  # 5
  mask += [1.0] * n_bit  # 6

  try:
    max_score = -10000
    max_idx = 0

    for idx in range(n_cw, n_extra):
      score = 0
      for mask_idx in range(len(mask)):
        score += mask[mask_idx] * signal[idx + mask_idx]
      if score > max_score:
        max_score = score
        max_idx = idx

    return int(max_idx + n_bit * n_bit_preamble), max_score

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[detect_preamble:" + str(tb.tb_lineno) + "] " + str(ex))

def decode_data(signal):
  mask0L = [1.0] * n_half_bit
  mask0L += [-1.0] * n_half_bit
  mask0L += [1.0] * n_half_bit
  mask0L += [-1.0] * n_half_bit

  mask0H = [-1.0] * n_half_bit
  mask0H += [1.0] * n_half_bit
  mask0H += [-1.0] * n_half_bit
  mask0H += [1.0] * n_half_bit

  mask1L = [1.0] * n_half_bit
  mask1L += [-1.0] * n_bit
  mask1L += [1.0] * n_half_bit

  mask1H = [-1.0] * n_half_bit
  mask1H += [1.0] * n_bit
  mask1H += [-1.0] * n_half_bit

  try:
    start, pre_score = detect_preamble(signal)
    state = -1
    tot_shift = 0
    decoded_bit = []
    shift_list = [0]
    success_score = []
    fail_score = []

    for bit in range(n_bit_data):
      cur_start = int(start + n_bit*bit) + tot_shift

      if state == 1:
        mask0 = mask0H
        mask1 = mask1H
      else:
        mask0 = mask0L
        mask1 = mask1L

      max_score0 = -10000
      max_score1 = -10000
      max_idx0 = 0
      max_idx1 = 0

      for shift in [-3, -2, -1, 0, 1, 2, 3]:
        score0 = 0
        score1 = 0

        for mask_idx in range(2*n_bit):
          idx = cur_start - n_half_bit + mask_idx + shift
          if idx >= len(signal): continue
          score0 += mask0[mask_idx] * signal[idx]
          score1 += mask1[mask_idx] * signal[idx]

        if score0 > max_score0:
          max_score0 = score0
          max_idx0 = shift
        if score1 > max_score1:
          max_score1 = score1
          max_idx1 = shift

      if max_score0 > max_score1:
        decoded_bit.append(0)
        tot_shift += max_idx0
        success_score.append(max_score0)
        fail_score.append(max_score1)
      else:
        decoded_bit.append(1)
        tot_shift += max_idx1
        success_score.append(max_score1)
        fail_score.append(max_score0)
        state *= -1
      shift_list.append(tot_shift)

    return decoded_bit, start, pre_score, shift_list, success_score, fail_score

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[decode_data:" + str(tb.tb_lineno) + "] " + str(ex))

if __name__ == "__main__":
  try:
    for file_name in file_name_list:
      try:
        file = open(signal_path + file_name + "_RN0_signal_test", "r")
        signal = []

        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          line = file.readline().rstrip(" \n").split(" ")
          line = [float(i) for i in line]
          for n in range(n_half_bit):
            line.append(0)
          signal.append(line)
        file.close()

        file = open(signal_path_2 + file_name + "_RN0_signal_test", "r")
        signal_2 = []

        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          line = file.readline().rstrip(" \n").split(" ")
          line = [float(i) for i in line]
          for n in range(n_half_bit):
            line.append(0)
          signal_2.append(line)
        file.close()

        file = open(signal_path + file_name + "_RN0_databit_test", "r")
        databit = []

        for idx in range(n_signal):
          line = file.readline().rstrip(" \n")
          line = [int(i) for i in line]
          databit.append(line)
        file.close()

        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          predict, start, score, shift_list, success_score, fail_score = decode_data(signal[idx])
          predict_2, start_2, score_2, shift_list_2, success_score_2, fail_score_2 = decode_data(signal_2[idx])
          last_idx = 128
          level = -1

          for n in range(n_bit_data):
            if predict[n] != databit[idx][n]:
              last_idx = n
              break
            elif predict[n] == 1:
              level *= -1

          if last_idx > 0 and last_idx < 128:
            file = open(output_path + str(last_idx), "a")

            file.write(file_name + "\t" + str(idx+1) + "\t" + str(databit[idx][last_idx-1]) + "\t" + str(databit[idx][last_idx]) + "\t")
            error_prev_start = start + n_bit * (last_idx - 1) + shift_list[last_idx - 1]
            error_start = start + n_bit * last_idx + shift_list[last_idx]
            file.write(str(level) + "\t" + str(error_prev_start) + "\t" + str(error_start) + "\t")
            if success_score_2[last_idx] > fail_score_2[last_idx]:
              file.write("1\n")
            else:
              file.write("0\n")

            for n in range(last_idx):
              file.write(str(success_score[n]) + "\t")
            file.write(str(fail_score[last_idx]) + "\n")
            for n in range(last_idx):
              file.write(str(fail_score[n]) + "\t")
            file.write(str(success_score[last_idx]) + "\n")

            for bit in signal[idx][error_prev_start-n_half_bit:error_start+n_bit+n_half_bit]:
              file.write(str(bit) + "\t")
            file.write("\n")

            error_prev_start = start_2 + n_bit * (last_idx - 1) + shift_list_2[last_idx - 1]
            error_start = start_2 + n_bit * last_idx + shift_list_2[last_idx]
            for bit in signal_2[idx][error_prev_start-n_half_bit:error_start+n_bit+n_half_bit]:
              file.write(str(bit) + "\t")
            file.write("\n")

            file.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[main:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
