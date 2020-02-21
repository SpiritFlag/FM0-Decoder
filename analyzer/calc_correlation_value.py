import sys
import numpy as np

from tqdm import tqdm

file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name_list = ["100_0_0"]
file_name_list = file_name_list_all

#signal_path = "../data/B_CW_kalman_std/"
#signal_path = "../data/C_RN_std/"
signal_path = "../data/C_RN_std_cliffing/"
#databit_path = "../data/A_databit/"
databit_path = "../data/C_RN_databit/"
#output_path = "../data/Z_correlation_value/"
output_path = "../data/tmp/"

#n_signal = 3000
n_signal = 10
n_sample = 6850
n_cw = 50
n_bit = 50
n_half_bit = int(n_bit / 2)
n_tolerance_bit = 2
n_bit_preamble = 6
n_bit_data = 128
n_extra = int(n_sample - n_bit * (n_bit_preamble + n_bit_data))



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
    if state == -1:
      mask0 = [1.0] * n_half_bit  # H(LH)L
      mask0 += [-1.0] * n_half_bit
      mask0 += [1.0] * n_half_bit
      mask0 += [-1.0] * n_half_bit
      mask1 = [1.0] * n_half_bit  # H(LL)H
      mask1 += [-1.0] * n_bit
      mask1 += [1.0] * n_half_bit
      type = [0, 2]
    elif state == 1:
      mask0 = [-1.0] * n_half_bit # L(HL)H
      mask0 += [1.0] * n_half_bit
      mask0 += [-1.0] * n_half_bit
      mask0 += [1.0] * n_half_bit
      mask1 = [-1.0] * n_half_bit # L(HH)L
      mask1 += [1.0] * n_bit
      mask1 += [-1.0] * n_half_bit
      type = [1, 3]

    if databit == 0:
      maskS = mask0
      maskF = mask1
      type = type[0]
    elif databit == 1:
      maskS = mask1
      maskF = mask0
      type = type[1]

    max_score = -10000
    max_idx = 0

    for idx in range(int(2 * n_tolerance_bit + 1)):
      score = 0
      for mask_idx in range(len(maskS)):
        score += maskS[mask_idx] * signal[idx + mask_idx]
      if score > max_score:
        max_score = score
        max_idx = idx

    score = 0
    for mask_idx in range(len(maskF)):
      score += maskF[mask_idx] * signal[max_idx + mask_idx]

    if max_score > score:
      return type, max_score, max_idx, True
    else:
      return type, max_score, max_idx, False

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[detect_bit:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



if __name__ == "__main__":
  try:
    tot_outlier = 0
    fileL = open(output_path + "_log", "w")

    for file_name in file_name_list:
      try:
        #file = open(signal_path + file_name + "_signal", "r")
        file = open(signal_path + file_name + "_RN0_validation", "r")
        signal = []
        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          line = file.readline().rstrip(" \n").split(" ")
          line = [float(i) for i in line]
          signal.append(line)
        file.close()

        #file = open(databit_path + file_name + "_databit", "r")
        file = open(databit_path + file_name + "_RN0_validation", "r")
        databit = []
        for idx in range(n_signal):
          line = file.readline().rstrip(" \n")
          line = [int(i) for i in line]
          databit.append(line)
        file.close()

        fileS = open(output_path + file_name + "_success", "w")
        fileF = open(output_path + file_name + "_fail", "w")

        outlier = 0
        threshold = 40
        count = np.zeros(4)

        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          start = detect_preamble(signal[idx])
          state = -1

          cur_count = np.zeros(4)

          for n in range(n_bit_data):
            end = start + n_bit + n_tolerance_bit
            #if end > n_sample:
            if end + n_half_bit > n_sample:
              start -= (end - n_sample)
              end -= (end - n_sample)
              outlier += 1
              count -= cur_count
              break

            type, score, shift, success = detect_bit(signal[idx][start-n_tolerance_bit:end+1], databit[idx][n], state)
            start += (shift - n_tolerance_bit)

            if success is True:
              fileS.write(str(score) + " ")
            else:
              fileF.write(str(score) + " ")

            if score >= 40:
              cur_count[type] += 1
              count[type] += 1

            start += n_bit
            if databit[idx][n] == 1:
              state *= -1

        fileS.close()
        fileF.close()

        tot_outlier += outlier
        #print(str(file_name) + "\t" + str(outlier) + "\n")
        print(count)
        fileL.write(str(count[0]) + "\t" + str(count[1]) + "\t" + str(count[2]) + "\t" + str(count[3]) + "\n")

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[calc_correlation_value:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    #print("TOTAL\t" + str(tot_outlier) + "\n")
    fileL.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[calc_correlation_value:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
