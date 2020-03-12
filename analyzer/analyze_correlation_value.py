import sys

file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name_list = ["100_0_0"]
file_name_list = file_name_list_all

file_path = "../data/Y_full_test/"
log_path = "../data/tmp/"

n_signal = 600
idx_min = 66
idx_max = 79

if __name__ == "__main__":
  try:
    fileA = open(log_path + "_compare_mlp_corr", "w")
    fileB = open(log_path + "_idx_mlp_corr", "w")
    mlp_idx = []

    for file_name in file_name_list:
      try:
        file = open(file_path + file_name + "_corr", "r")
        index = []
        corr = []

        for idx in range(n_signal):
          line = file.readline().rstrip("\n").split("\t")
          index.append(int(line[0]))
          corr.append(int(line[2]))
        file.close()

        file = open(file_path + file_name + "_mlp", "r")
        mlp = file.readline().rstrip("\t").split("\t")
        mlp = [int(i) for i in mlp]
        file.close()

        count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for idx in range(n_signal):
          if index[idx] >= idx_min and index[idx] <= idx_max:
            if corr[idx] == 128:
              count[0] += 1 # index success + corr success
              if mlp[idx] == 0:
                count[1] += 1  # index success + corr success + mlp success
              else:
                count[2] += 1  # index success + corr success + mlp fail
            else:
              count[3] += 1 # index success + corr fail
              if mlp[idx] == 0:
                count[4] += 1  # index success + corr fail + mlp success
              else:
                count[5] += 1  # index success + corr fail + mlp fail
          else:
            count[6] += 1 # index fail + corr fail
            if mlp[idx] == 0:
              count[7] += 1  # index fail + corr fail + mlp success
              mlp_idx.append(index[idx])
            else:
              count[8] += 1  # index fail + corr fail + mlp fail

        fileA.write(file_name + "\t")
        for i in range(9):
          fileA.write(str(count[i]) + "\t")
        fileA.write("\n")

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[count_correlation_value:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    print(min(mlp_idx), max(mlp_idx))
    for i in range(50, 150):
      fileB.write(str(mlp_idx.count(i)) + "\t")

    fileA.close()
    fileB.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[count_correlation_value:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
