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
file_path_2 = "../data/XY_full_test/"
file_path_3 = "../data/Y_full_bitscore_ver3/"
log_path = "../data/tmp/"

n_signal = 600
idx_min = 66
idx_max = 79

if __name__ == "__main__":
  try:
    fileA = open(log_path + "_corr_prop", "w")
    fileB = open(log_path + "_bit_score_props", "w")
    fileC = open(log_path + "_bit_score_propf", "w")
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

        file = open(file_path_2 + file_name + "_corr", "r")
        prop = []

        for idx in range(n_signal):
          line = file.readline().rstrip("\n").split("\t")
          prop.append(int(line[2]))
        file.close()

        file = open(file_path + file_name + "_mlp", "r")
        mlp = file.readline().rstrip("\t").split("\t")
        mlp = [int(i) for i in mlp]
        file.close()

        file = open(file_path_3 + file_name, "r")
        score = file.readline().rstrip("\t").split("\t")
        score = [float(i) for i in score]
        file.close()

        list1 = []
        list2 = []
        count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for idx in range(n_signal):
          if index[idx] >= idx_min and index[idx] <= idx_max:
            if corr[idx] == 128:
              count[0] += 1 # index success + corr success
            else:
              if mlp[idx] == 0:
                if prop[idx] == 0:
                  count[1] += 1  # index success + corr fail + mlp success + prop success
                  if score[idx] != -10000:
                    list1.append(score[idx])
                else:
                  count[2] += 1  # index success + corr fail + mlp success + prop fail
                  if score[idx] != -10000:
                    list2.append(score[idx])
              else:
                if prop[idx] == 0:
                  count[3] += 1  # index success + corr fail + mlp fail + prop success
                else:
                  count[4] += 1  # index success + corr fail + mlp fail + prop fail
          else:
            if mlp[idx] == 0:
              if prop[idx] == 0:
                count[5] += 1  # index fail + corr fail + mlp success + prop success
              else:
                count[6] += 1  # index fail + corr fail + mlp success + prop fail
            else:
              if prop[idx] == 0:
                count[7] += 1  # index fail + corr fail + mlp fail + prop success
              else:
                count[8] += 1  # index fail + corr fail + mlp fail + prop fail

        fileA.write(file_name + "\t")
        for i in range(9):
          fileA.write(str(count[i]) + "\t")

        if len(list1) > 0:
          avg = 0
          for x in list1:
            avg += x
            fileB.write(str(x) + "\t")
          avg /= len(list1)
          fileA.write(str(avg) + "\t")
        else:
          fileA.write("-10000\t")

        if len(list2) > 0:
          avg = 0
          for x in list2:
            avg += x
            fileC.write(str(x) + "\t")
          avg /= len(list2)
          fileA.write(str(avg) + "\t")
        else:
          fileA.write("-10000\t")

        fileA.write("\n")

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[count_correlation_value:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    fileA.close()
    fileB.close()
    fileC.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[count_correlation_value:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
