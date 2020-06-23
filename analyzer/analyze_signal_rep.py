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

input_path = "../log/output_ccc_5544332211/"
output_path = input_path + "stdev/"
output_path2 = input_path + "stdev_intra/"

n_signal = 600
rep = 25



if __name__ == "__main__":
  try:
    for file_name in file_name_list:
      try:
        output = []
        file = open(input_path + file_name, "r")
        for idx in range(n_signal):
          line = file.readline().rstrip("\n").split("\t")
          output.append([float(i) for i in line])
        file.close()

        file = open(output_path + file_name, "w")
        file2 = open(output_path2 + file_name, "w")
        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" data"):
          data = output[idx]
          avg_list = []
          for x in range(12, 268):  # except preamble
            avg = np.mean(data[x*rep:(x+1)*rep])
            avg_list.append(avg)
            stdev = np.std(data[x*rep:(x+1)*rep])
            file.write(str(stdev) + "\t")
          file.write("\n")
          stdev = np.std(avg_list)
          file2.write(str(stdev) + "\t")
        file.close()
        file2.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[main:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex))

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex))
