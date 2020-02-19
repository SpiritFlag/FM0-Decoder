import sys

from tqdm import tqdm

file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name_list = ["100_0_90"]
file_name_list = file_name_list_all

signal_path = "../data/B_CW_kalman_std/"
databit_path = "../data/A_databit/"
output_path = "../data/Z_correlation_value/"

n_signal = 3000
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
      mask0 = [-1.0] * n_half_bit
      mask0 += [1.0] * n_half_bit
      mask1 = [-1.0] * n_bit
    elif state == 1:
      mask0 = [1.0] * n_half_bit
      mask0 += [-1.0] * n_half_bit
      mask1 = [1.0] * n_bit

    if databit == 0:
      maskS = mask0
      maskF = mask1
    elif databit == 1:
      maskS = mask1
      maskF = mask0

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
      return max_score, max_idx, True
    else:
      return max_score, max_idx, False

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[detect_bit:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



if __name__ == "__main__":
  try:
    for file_name in file_name_list:
      try:
        file = open(signal_path + file_name + "_signal", "r")
        signal = []
        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          line = file.readline().rstrip(" \n").split(" ")
          line = [float(i) for i in line]
          signal.append(line)
        file.close()

        file = open(databit_path + file_name + "_databit", "r")
        databit = []
        for idx in range(n_signal):
          line = file.readline().rstrip(" \n")
          line = [int(i) for i in line]
          databit.append(line)
        file.close()

        fileS = open(output_path + file_name + "_success", "w")
        fileF = open(output_path + file_name + "_fail", "w")

        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          start = detect_preamble(signal[idx])
          state = -1

          for n in range(n_bit_data):
            end = start + n_bit + n_tolerance_bit
            if end > n_sample:
              start -= (end - n_sample)
              end -= (end - n_sample)

            score, shift, success = detect_bit(signal[idx][start-n_tolerance_bit:end+1], databit[idx][n], state)
            start += (shift - n_tolerance_bit)

            if success is True:
              fileS.write(str(score) + " ")
            else:
              fileF.write(str(score) + " ")

            start += n_bit
            if databit[idx][n] == 1:
              state *= -1

        fileS.close()
        fileF.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[calc_correlation_value:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[calc_correlation_value:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
