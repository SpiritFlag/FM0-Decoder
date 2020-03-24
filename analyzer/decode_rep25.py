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

signal_path = "../data/Y_full_rep25/"
databit_path = "../data/C_signal_std_full/"
output_path = "../data/Y_full_test/"

n_signal = 600
n_sample = 6700
n_bit = 50
n_half_bit = int(n_bit / 2)
n_bit_preamble = 6
n_bit_data = 128

mask0L = [1, 0, 1, 0]
mask0H = [0, 1, 0, 1]
mask1L = [1, 0, 0, 1]
mask1H = [0, 1, 1, 0]



if __name__ == "__main__":
  try:
    tot_success = []

    for file_name in file_name_list:
      try:
        file = open(signal_path + file_name, "r")
        signal = []

        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          line = file.readline().rstrip("\t\n").split("\t")
          line = [float(i) for i in line]
          new_line = []
          for x in range(int(n_sample / n_half_bit)):
            new_line.append(sum(line[int(x*n_half_bit):int((x+1)*n_half_bit)])/n_half_bit)
          new_line.append(0)
          signal.append(new_line)
        file.close()

        file = open(databit_path + file_name + "_RN0_databit_test", "r")
        databit = []

        for idx in range(n_signal):
          line = file.readline().rstrip(" \n")
          line = [int(i) for i in line]
          databit.append(line)
        file.close()



        file = open(output_path + file_name + "_mlp25_mask", "w")
        success = 0

        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          state = -1
          cnt = 0

          for bit in range(n_bit_data):
            if state == 1:
              mask0 = mask0H
              mask1 = mask1H
            else:
              mask0 = mask0L
              mask1 = mask1L

            score0 = 0
            score1 = 0
            for mask_idx in range(4):
              start_idx = 12 + 2*bit - 1 + mask_idx
              score0 += mask0[mask_idx] * signal[idx][start_idx]
              score1 += mask1[mask_idx] * signal[idx][start_idx]

            if score0 > score1 and databit[idx][bit] != 0:
              cnt += 1
            elif score1 > score0 and databit[idx][bit] != 1:
              cnt += 1
            if score1 > score0:
              state *= -1

          if cnt == 0:
            success += 1
          file.write(str(cnt) + "\t")

        print("\t\tSUCCESS= " + str(success) + " / " + str(600) + "\t(" + str(round(100 * success / 600, 2)) + "%)\n")
        tot_success.append(success)
        file.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[main:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    for x in tot_success:
      print(x, end="\t")
    print("")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
