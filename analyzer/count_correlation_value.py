import sys

file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name_list = ["100_0_0"]
file_name_list = file_name_list_all

log_path = "../data/tmp/"

n_signal = 600

if __name__ == "__main__":
  try:
    fileA = open(log_path + "_tot_success_idx", "w")
    success_idx = []

    for file_name in file_name_list:
      try:
        file = open(log_path + file_name + "_corr", "r")
        index = []
        success = []

        for idx in range(n_signal):
          line = file.readline().rstrip("\n").split("\t")
          index.append(int(line[0]))
          success.append(int(line[1]))
        file.close()

        for idx in range(n_signal):
          if success[idx] == 0:
            success_idx.append(index[idx])
            fileA.write(str(index[idx]) + "\t")

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[count_correlation_value:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    print(min(success_idx), max(success_idx))
    fileA.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[count_correlation_value:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
