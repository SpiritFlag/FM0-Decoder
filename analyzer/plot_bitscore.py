import sys
import itertools
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm

input_path = "../data/Y_full_bitscore/"
file_name = 26

if __name__ == "__main__":
  try:
    file = open(input_path + str(file_name), "r")

    for idx in itertools.count():
      input = file.readline()
      if input == "":
        break

      input = input.split("\t")
      prev = int(input[2])
      cur = int(input[3])
      level = int(input[4])
      issuccess = int(input[7])

      success = file.readline().rstrip("\n").split("\t")
      success = [float(i) for i in success]
      fail = file.readline().rstrip("\n").split("\t")
      fail = [float(i) for i in fail]
      signal = file.readline().rstrip("\t\n").split("\t")
      signal = [float(i) for i in signal]
      signal_2 = file.readline().rstrip("\t\n").split("\t")
      signal_2 = [float(i) for i in signal_2]

      #if idx % 20 != 0:
      if issuccess == 0:
        continue

      if level == -1:
        if prev == 0:
          prev_mask = [1] * 25
          prev_mask += [-1] * 25
          prev_mask += [1] * 25
          prev_mask += [-1] * 25
        else:
          prev_mask = [-1] * 25
          prev_mask += [1] * 50
          prev_mask += [-1] * 25
        if cur == 0:
          cur_mask = [1] * 25
          cur_mask += [-1] * 25
          cur_mask += [1] * 25
          cur_mask += [-1] * 25
        else:
          cur_mask = [1] * 25
          cur_mask += [-1] * 50
          cur_mask += [1] * 25
      else:
        if prev == 0:
          prev_mask = [-1] * 25
          prev_mask += [1] * 25
          prev_mask += [-1] * 25
          prev_mask += [1] * 25
        else:
          prev_mask = [1] * 25
          prev_mask += [-1] * 50
          prev_mask += [1] * 25
        if cur == 0:
          cur_mask = [-1] * 25
          cur_mask += [1] * 25
          cur_mask += [-1] * 25
          cur_mask += [1] * 25
        else:
          cur_mask = [-1] * 25
          cur_mask += [1] * 50
          cur_mask += [-1] * 25

      plt.subplot(311)
      plt.axhline(y=100, color='r', linestyle='-')
      plt.axhline(y=0, color='r', linestyle='-')
      plt.plot(success)
      plt.plot(fail)
      if issuccess == 1:
        plt.title("success")
      else:
        plt.title("fail")

      plt.subplot(312)
      plt.plot(prev_mask)
      plt.plot([int(i) for i in range(len(signal)-100, len(signal))], cur_mask)
      plt.plot(signal, ".")
      plt.ylim([-1.5, 1.5])

      plt.subplot(313)
      plt.plot(prev_mask)
      plt.plot([int(i) for i in range(len(signal)-100, len(signal))], cur_mask)
      plt.plot(signal_2, ".")
      plt.ylim([-1.5, 1.5])

      plt.show()
      plt.close()

    file.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex))
