import sys
import numpy as np

file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name_list = ["100_0_0"]
file_name_list = file_name_list_all

input_path = "../data/Y_full_test/"
log_path = "../data/Y_0324/"

n_signal = 600



def process(file, file_name, index, corr, cmp):
  try:
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for idx in range(n_signal):
      if index[idx] >= 66 and index[idx] <= 79:
        if corr[idx] == 128:
          count[0] += 1 # index success + corr success
          if cmp[idx] == 0:
            count[1] += 1  # index success + corr success + cmp success
          else:
            count[2] += 1  # index success + corr success + cmp fail
        else:
          count[3] += 1 # index success + corr fail
          if cmp[idx] == 0:
            count[4] += 1  # index success + corr fail + cmp success
          else:
            count[5] += 1  # index success + corr fail + cmp fail
      else:
        count[6] += 1 # index fail + corr fail
        if cmp[idx] == 0:
          count[7] += 1  # index fail + corr fail + cmp success
        else:
          count[8] += 1  # index fail + corr fail + cmp success

    file.write(file_name + "\t")
    for i in range(9):
      file.write(str(count[i]) + "\t")
    file.write("\n")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



if __name__ == "__main__":
  try:
    fileB = open(log_path + "_bit_corr", "w")
    fileB2 = open(log_path + "_bit_shift", "w")
    fileM = open(log_path + "_mlp", "w")
    fileM2 = open(log_path + "_mlp25", "w")

    for file_name in file_name_list:
      try:
        file = open(input_path + file_name + "_corr", "r")
        index = []
        corr = []

        for idx in range(n_signal):
          line = file.readline().rstrip("\n").split("\t")
          index.append(int(line[0]))
          corr.append(int(line[2]))
        file.close()

        file = open(input_path + file_name + "_bit_corr", "r")
        bit_corr = file.readline().rstrip("\t").split("\t")
        bit_corr = [int(i) for i in bit_corr]
        file.close()

        process(fileB, file_name, index, corr, bit_corr)

        file = open(input_path + file_name + "_bit_shift", "r")
        bit_shift = file.readline().rstrip("\t").split("\t")
        bit_shift = [int(i) for i in bit_shift]
        file.close()

        process(fileB2, file_name, index, corr, bit_shift)

        file = open(input_path + file_name + "_mlp", "r")
        mlp = file.readline().rstrip("\t").split("\t")
        mlp = [int(i) for i in mlp]
        file.close()

        process(fileM, file_name, index, corr, mlp)

        file = open(input_path + file_name + "_mlp25", "r")
        mlp25 = file.readline().rstrip("\t").split("\t")
        mlp25 = [int(i) for i in mlp25]
        file.close()

        process(fileM2, file_name, index, corr, mlp25)

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[main:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    fileB.close()
    fileB2.close()
    fileM.close()
    fileM2.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
