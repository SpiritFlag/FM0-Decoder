import sys

from tqdm import tqdm

file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name_list = ["100_0_0"]
file_name_list = file_name_list_all

signal_path = "../data/C_RN_std/"
#signal_path = "../data/C_RN_std_cliffing/"
output_path = "../data/tmp/"

n_signal = 100
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

    return max_idx

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[detect_preamble:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



if __name__ == "__main__":
  try:
    fileL = open(output_path + "_log", "w")

    for file_name in file_name_list:
      try:
        file = open(signal_path + file_name + "_RN0_test", "r")
        signal = []
        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          line = file.readline().rstrip(" \n").split(" ")
          line = [float(i) for i in line]
          signal.append(line)
        file.close()

        fileS = open(output_path + file_name + "_indexS", "w")
        fileF = open(output_path + file_name + "_indexF", "w")

        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          start = detect_preamble(signal[idx])
          fileL.write(str(start) + " ")
          if start >= 70 and start <= 80:
            fileS.write(str(idx) + " ")
          else:
            fileF.write(str(idx) + " ")

        fileL.write("\n")
        fileS.close()
        fileF.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[extract_preamble_index:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    fileL.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[extract_preamble_index:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
