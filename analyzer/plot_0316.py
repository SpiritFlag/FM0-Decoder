import sys
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm

file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name = "100_0_90"
file_name_list = file_name_list_all

input_path = "../data/Y_0316/"
output_path = "../data/Y_0316/fig/"

n_signal = 600



def make_mask(bit, state):
  mask0L = [1] * 25
  mask0L += [-1] * 25
  mask0L += [1] * 25
  mask0L += [-1] * 25

  mask1L = [1] * 25
  mask1L += [-1] * 50
  mask1L += [1] * 25

  mask0H = [-1] * 25
  mask0H += [1] * 25
  mask0H += [-1] * 25
  mask0H += [1] * 25

  mask1H = [-1] * 25
  mask1H += [1] * 50
  mask1H += [-1] * 25

  if bit == 0:
    if state == -1:
      return mask0L
    else:
      return mask0H
  else:
    if state == -1:
      return mask1L
    else:
      return mask1H



if __name__ == "__main__":
  try:
    for file_name in file_name_list:
      try:
        file = open(input_path + str(file_name), "r")

        for idx in range(n_signal):
          input = file.readline()
          if len(input) == 1:
            file.readline()
            file.readline()
            file.readline()
            continue

          print(idx)
          print(input)
          input = input.rstrip("\n").split("\t")
          prev = int(input[0])
          cur = int(input[1])
          next = int(input[2])
          cursor = int(input[3])
          state = int(input[4])

          signal = file.readline().rstrip("\t\n").split("\t")
          signal = [float(i) for i in signal]
          success = file.readline().rstrip("\t\n").split("\t")
          success = [float(i) for i in success]
          fail = file.readline().rstrip("\t\n").split("\t")
          fail = [float(i) for i in fail]

          #if idx != 0:
          #  continue

          if prev == 0:
            prev_mask = make_mask(prev, state)
          else:
            prev_mask = make_mask(prev, state*-1)
          cur_mask = make_mask(cur, state)
          if cur == 0:
            next_mask = make_mask(next, state)
          else:
            next_mask = make_mask(next, state*-1)

          plt.subplot(211)
          plt.axhline(y=100, color='r', linestyle='-')
          plt.axhline(y=0, color='r', linestyle='-')
          plt.plot(success)
          plt.plot(fail)

          plt.subplot(212)
          plt.plot(prev_mask)
          plt.plot([int(i) for i in range(len(signal)-100, len(signal))], next_mask)
          plt.plot([int(i) for i in range(cursor-25, cursor+75)], cur_mask)
          plt.plot(signal, ".")
          plt.ylim([-1.5, 1.5])

          #plt.show()
          plt.savefig(output_path + file_name + "_" + str(idx) + ".png", dpi=300)
          plt.close()

        file.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[main:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex))

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex))
