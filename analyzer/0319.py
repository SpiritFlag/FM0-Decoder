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
output_path = "../data/Y_0319/"

n_signal = 600



if __name__ == "__main__":
  try:
    fileW = open(output_path + "0319", "w")

    for file_name in file_name_list:
      try:
        file = open(input_path + str(file_name), "r")
        fileW.write(file_name + "\t")

        for idx in tqdm(range(n_signal), desc=file_name, ncols=100, unit=" signal"):
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

        fileW.write("\n")
        file.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[main:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex))

    fileW.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex))
