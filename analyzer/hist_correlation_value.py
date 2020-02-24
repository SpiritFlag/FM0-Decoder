import sys
import matplotlib.pyplot as plt

from tqdm import tqdm

file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name_list = ["100_0_0"]
file_name_list = file_name_list_all

input_path = "../data/Z_C_signal_std_correlation_train/"
output_path = input_path + "plt/"



if __name__ == "__main__":
  try:
    tot_success = []
    tot_fail = []
    fileL = open(output_path + "log", "w")

    for f in tqdm(range(len(file_name_list)), desc="PROCESSING", ncols=100, unit=" file"):
      try:
        file_name = file_name_list[f]

        file = open(input_path + file_name + "_success", "r")
        success = file.readline().rstrip(" \n").split(" ")
        if len(success) == 1:
          success = []
        else:
          success = [float(i) for i in success]
        tot_success += success
        file.close()

        file = open(input_path + file_name + "_fail", "r")
        fail = file.readline().rstrip(" \n").split(" ")
        if len(fail) == 1:
          fail = []
        else:
          fail = [float(i) for i in fail]
        tot_fail += fail
        file.close()

        fileL.write(str(file_name) + "\t" + str(len(success)) + "\t" + str(len(fail)) + "\n")

        plt.hist(success, bins=range(-150, 160, 10), alpha=0.5, rwidth=0.8, label="success")
        plt.hist(fail, bins=range(-150, 160, 10), alpha=0.5, rwidth=0.8, label="fail")
        plt.title(file_name)
        plt.legend()
        #plt.show()
        plt.savefig(output_path + file_name + ".png", dpi=300)
        plt.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[hist_correlation_value:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex))

    fileL.write("TOTAL" + "\t" + str(len(tot_success)) + "\t" + str(len(tot_fail)) + "\n")
    fileL.close()

    plt.hist(tot_success, bins=range(-150, 160, 10), alpha=0.5, rwidth=0.8, label="success")
    plt.hist(tot_fail, bins=range(-150, 160, 10), alpha=0.5, rwidth=0.8, label="fail")
    plt.title("TOTAL")
    plt.legend()
    #plt.show()
    plt.savefig(output_path + "total.png", dpi=300)
    plt.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[hist_correlation_value:" + str(tb.tb_lineno) + "] " + str(ex))
