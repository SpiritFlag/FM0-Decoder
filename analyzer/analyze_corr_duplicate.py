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

log_path = "../data/Y_full_test/"

n_signal = 600
score_cut = 150
idx_min = 66
idx_max = 79

if __name__ == "__main__":
  try:
    fileA = open(log_path + "_dup_in_success", "w")
    fileB = open(log_path + "_dup_in_fail", "w")
    fileE = open(log_path + "_dup_out_success", "w")
    fileF = open(log_path + "_dup_out_fail", "w")

    for file_name in file_name_list:
      try:
        file = open(log_path + file_name + "_corr", "r")
        index = []
        score = []
        last_idx = []

        for idx in range(n_signal):
          line = file.readline().rstrip("\n").split("\t")
          index.append(int(line[0]))
          score.append(float(line[1]))
          last_idx.append(int(line[2]))
        file.close()

        file = open(log_path + file_name + "_mlp", "r")
        mlp = file.readline().rstrip("\t").split("\t")
        mlp = [int(i) for i in mlp]
        file.close()

        success = np.zeros(129, dtype="i")
        fail = np.zeros(129, dtype="i")
        success_out = np.zeros(129, dtype="i")
        fail_out = np.zeros(129, dtype="i")

        for idx in range(n_signal):
          if (index[idx] >= idx_min and index[idx] <= idx_max) and score[idx] >= score_cut:
            if mlp[idx] == 0:
              success[last_idx[idx]] += 1
            else:
              fail[last_idx[idx]] += 1
          elif (index[idx] < idx_min or index[idx] > idx_max) and score[idx] < score_cut:
            if mlp[idx] == 0:
              success_out[last_idx[idx]] += 1
            else:
              fail_out[last_idx[idx]] += 1

        fileA.write(file_name + "\t")
        for count in success:
          fileA.write(str(count) + "\t")
        fileA.write("\n")
        fileB.write(file_name + "\t")
        for count in fail:
          fileB.write(str(count) + "\t")
        fileB.write("\n")
        fileE.write(file_name + "\t")
        for count in success_out:
          fileE.write(str(count) + "\t")
        fileE.write("\n")
        fileF.write(file_name + "\t")
        for count in fail_out:
          fileF.write(str(count) + "\t")
        fileF.write("\n")

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[main:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(idx)+str(ex) + "\n\n")

    fileA.close()
    fileB.close()
    fileE.close()
    fileF.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
