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
output_path = "../data/Y_0316/"

n_signal = 600
n_sample = 6850
n_cw = 50
n_bit = 50
n_half_bit = int(n_bit / 2)
n_tolerance_bit = 2
n_bit_preamble = 6
n_bit_data = 128
n_extra = int(n_sample - n_bit * (n_bit_preamble + n_bit_data))

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

    return int(max_idx + n_bit * n_bit_preamble)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[detect_preamble:" + str(tb.tb_lineno) + "] " + str(ex))



if __name__ == "__main__":
  try:
    for file_name in file_name_list:
      try:
        file = open(signal_path + file_name + "_RN0_signal_test", "r")
        signal = []

        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          line = file.readline().rstrip(" \n").split(" ")
          line = [float(i) for i in line]
          signal.append(line)
        file.close()

        file = open(signal_path + file_name + "_RN0_databit_test", "r")
        databit = []

        for idx in range(n_signal):
          line = file.readline().rstrip(" \n")
          line = [int(i) for i in line]
          databit.append(line)
        file.close()



        file = open(output_path + file_name, "w")

        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          start = detect_preamble(signal[idx])
          state = -1
          tot_shift = 0
          success_score = []
          fail_score = []
          prev_idx = 0
          chk = False

          for bit in range(n_bit_data):
            cur_start = int(start + n_bit*bit) + tot_shift

            if state == 1:
              mask0 = mask0H
              mask1 = mask1H
            else:
              mask0 = mask0L
              mask1 = mask1L

            if databit[idx][bit] == 0:
              maskS = mask0
              maskF = mask1
            else:
              maskS = mask1
              maskF = mask0

            max_score = -10000
            cur_shift = 0

            for shift in [-3, -2, -1, 0, 1, 2, 3]:
              score = 0
              for mask_idx in range(2*n_bit):
                start_idx = cur_start - n_half_bit + mask_idx + shift
                if start_idx >= len(signal[idx]): continue
                score += maskS[mask_idx] * signal[idx][start_idx]

              if score > max_score:
                max_score = score
                cur_shift = shift

            scoreS = max_score
            scoreF = 0
            for mask_idx in range(2*n_bit):
              start_idx = cur_start - n_half_bit + mask_idx + cur_shift
              if start_idx >= len(signal[idx]): continue
              scoreF += maskF[mask_idx] * signal[idx][start_idx]

            success_score.append(scoreS)
            fail_score.append(scoreF)

            if scoreS > scoreF:
              prev_idx = cur_start
            elif bit == 0:
              file.write("1\t")
              file.write(str(databit[idx][bit]) + "\t")
              file.write(str(databit[idx][bit+1]) + "\t")
              file.write("75\t" + str(state) + "\n")
              for sample in signal[idx][cur_start-75:cur_start+cur_shift+125]:
                file.write(str(sample) + "\t")
              file.write("\n")
              chk = True
            elif chk is False:
              file.write(str(databit[idx][bit-1]) + "\t")
              file.write(str(databit[idx][bit]) + "\t")
              if bit < 127:
                file.write(str(databit[idx][bit+1]) + "\t")
              else:
                file.write("1\t")
              file.write(str(cur_start-prev_idx+25) + "\t" + str(state) + "\n")
              for sample in signal[idx][prev_idx-25:cur_start+cur_shift+125]:
                file.write(str(sample) + "\t")
              file.write("\n")
              chk = True

            tot_shift += cur_shift
            if databit[idx][bit] == 1:
              state *= -1

          if chk is False:
            file.write("\n\n")

          for score in success_score:
            file.write(str(score) + "\t")
          file.write("\n")
          for score in fail_score:
            file.write(str(score) + "\t")
          file.write("\n")

        file.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[main:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
