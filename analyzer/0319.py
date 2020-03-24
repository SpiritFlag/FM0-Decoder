import sys

from tqdm import tqdm

file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name_list = ["100_0_90"]
file_name_list = file_name_list_all

input_path = "../data/Y_0316/"
input_path_2 = "../data/Y_full_test/"
output_path = "../data/Y_0319/"

n_signal = 600



if __name__ == "__main__":
  try:
    fileW = open(output_path + "0319", "w")
    fileBS = open(output_path + "0319_bit_corr_S", "w")
    fileBF = open(output_path + "0319_bit_corr_F", "w")
    fileB2S = open(output_path + "0319_bit_shift_S", "w")
    fileB2F = open(output_path + "0319_bit_shift_F", "w")
    fileMS = open(output_path + "0319_mlp_S", "w")
    fileMF = open(output_path + "0319_mlp_F", "w")
    fileM2S = open(output_path + "0319_mlp25_S", "w")
    fileM2F = open(output_path + "0319_mlp25_F", "w")

    for file_name in file_name_list:
      try:
        file = open(input_path + str(file_name), "r")
        fileC = open(input_path_2 + str(file_name) + "_corr", "r")
        fileB = open(input_path_2 + str(file_name) + "_bit_corr", "r")
        fileB2 = open(input_path_2 + str(file_name) + "_bit_shift", "r")
        fileM = open(input_path_2 + str(file_name) + "_mlp", "r")
        fileM2 = open(input_path_2 + str(file_name) + "_mlp25", "r")

        fileW.write(file_name + "\t")
        fileBS.write(file_name + "\t")
        fileBF.write(file_name + "\t")
        fileB2S.write(file_name + "\t")
        fileB2F.write(file_name + "\t")
        fileMS.write(file_name + "\t")
        fileMF.write(file_name + "\t")
        fileM2S.write(file_name + "\t")
        fileM2F.write(file_name + "\t")

        mlp = fileM.readline().rstrip("\t\n").split("\t")
        mlp = [int(i) for i in mlp]

        mlp = fileM.readline().rstrip("\t\n").split("\t")
        mlp = [int(i) for i in mlp]

        mlp25 = fileM2.readline().rstrip("\t\n").split("\t")
        mlp25 = [int(i) for i in mlp25]

        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
          corr = fileC.readline().rstrip("\n").split("\t")

          input = file.readline()
          if len(input) == 1:
            file.readline()
            file.readline()
            file.readline()
            continue

          file.readline()
          success = file.readline().rstrip("\t\n").split("\t")
          success = [float(i) for i in success]
          fail = file.readline().rstrip("\t\n").split("\t")
          fail = [float(i) for i in fail]

          cnt = 0
          for x in range(len(success)):
            if success[x] < fail[x]:
              cnt += 1
          fileW.write(str(cnt) + "\t")

          if int(corr[0]) >= 66 and int(corr[0]) <= 79:
            if mlp[idx] == 0: # within preamble index + mlp success
              fileWS.write(str(cnt) + "\t")
            else: # within preamble index + mlp fail
              fileWF.write(str(cnt) + "\t")
          else: # without preamble index
            fileWO.write(str(cnt) + "\t")

        fileW.write("\n")
        fileWS.write("\n")
        fileWF.write("\n")
        fileWO.write("\n")
        file.close()
        fileC.close()
        fileM.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[main:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex))

    fileW.close()
    fileWS.close()
    fileWF.close()
    fileWO.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex))
