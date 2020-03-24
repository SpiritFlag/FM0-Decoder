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
input_path2 = "../data/Y_0316/"
log_path = "../data/Y_0324/"

n_signal = 600



def process(file, file_name, index, corr, cnt, cmp):
  try:
    tot = []
    success = []
    fail = []
    list = [tot, success, fail]

    for idx in range(n_signal):
      if index[idx] >= 66 and index[idx] <= 79 and corr[idx] != 128:
        tot.append(cnt[idx])  # index success + corr fail
        if cmp[idx] == 0:
          success.append(cnt[idx])  # index success + corr fail + cmp success
        else:
          fail.append(cnt[idx])  # index success + corr fail + cmp fail

    file.write(file_name + "\n")
    for n in range(3):
      bit_cnt = np.zeros(129, dtype="int")
      for x in list[n]:
        bit_cnt[x] += 1
      for x in bit_cnt:
        file.write(str(x) + "\t")
      file.write("\n")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



if __name__ == "__main__":
  try:
    fileB = open(log_path + "_bit_corr_hist", "w")
    fileB2 = open(log_path + "_bit_shift_hist", "w")
    fileM = open(log_path + "_mlp_hist", "w")
    fileM2 = open(log_path + "_mlp25_hist", "w")

    for file_name in file_name_list:
      try:
        file2 = open(input_path + file_name + "_corr", "r")
        index = []
        corr = []
        file = open(input_path2 + str(file_name), "r")
        cnt = []

        for idx in range(n_signal):
          line = file2.readline().rstrip("\n").split("\t")

          file.readline()
          file.readline()
          success = file.readline().rstrip("\t\n").split("\t")
          success = [float(i) for i in success]
          fail = file.readline().rstrip("\t\n").split("\t")
          fail = [float(i) for i in fail]

          cur_cnt = 0
          for x in range(len(success)):
            if success[x] < fail[x]:
              cur_cnt += 1

          index.append(int(line[0]))
          corr.append(int(line[2]))
          cnt.append(cur_cnt)
        file.close()
        file2.close()

        file = open(input_path + file_name + "_bit_corr", "r")
        bit_corr = file.readline().rstrip("\t").split("\t")
        bit_corr = [int(i) for i in bit_corr]
        file.close()

        process(fileB, file_name, index, corr, cnt, bit_corr)

        file = open(input_path + file_name + "_bit_shift", "r")
        bit_shift = file.readline().rstrip("\t").split("\t")
        bit_shift = [int(i) for i in bit_shift]
        file.close()

        process(fileB2, file_name, index, corr, cnt, bit_shift)

        file = open(input_path + file_name + "_mlp", "r")
        mlp = file.readline().rstrip("\t").split("\t")
        mlp = [int(i) for i in mlp]
        file.close()

        process(fileM, file_name, index, corr, cnt, mlp)

        file = open(input_path + file_name + "_mlp25", "r")
        mlp25 = file.readline().rstrip("\t").split("\t")
        mlp25 = [int(i) for i in mlp25]
        file.close()

        process(fileM2, file_name, index, corr, cnt, mlp25)

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
