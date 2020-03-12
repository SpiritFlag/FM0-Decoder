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

signal_path = "../data/A_IQsignal/"
index_path = "../data/B_RNindex/"
output_path = "../data/XA_IQsignal/"

n_signal = 3000



if __name__ == "__main__":
  try:
    for file_name in file_name_list:
      try:
        file = open(signal_path + file_name + "_Isignal", "r")
        Isignal = []
        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          Isignal.append(file.readline())
        file.close()

        file = open(signal_path + file_name + "_Qsignal", "r")
        Qsignal = []
        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          Qsignal.append(file.readline())
        file.close()

        file = open(index_path + "RN0_test", "r")
        line = file.readline().rstrip(" \n").split(" ")
        list = [int(i) for i in line]
        file.close()

        file = open(index_path + "RN1_test", "r")
        line = file.readline().rstrip(" \n").split(" ")
        line = [int(i) for i in line]
        for x in line:
          list.append(x)
        file.close()

        file = open(index_path + "RN2_test", "r")
        line = file.readline().rstrip(" \n").split(" ")
        line = [int(i) for i in line]
        for x in line:
          list.append(x)
        file.close()

        file = open(output_path + file_name + "_RN0_Isignal_test", "w")
        for index in list:
          file.write(Isignal[index])
        file.close()

        file = open(output_path + file_name + "_RN0_Qsignal_test", "w")
        for index in list:
          file.write(Qsignal[index])
        file.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[main:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
