import sys
import numpy as np

from global_vars import *

n_RNtrain = 640
n_RNvalidation = 160
n_RNtest = 200
n_RNset = n_RNtrain + n_RNvalidation + n_RNtest
n_RNsignal = int(n_signal/n_RNset)

output_path = "../data/B_RNindex/"



def main(string):
  try:
    RN = np.arange(n_signal)
    np.random.shuffle(RN)

    for x in range(n_RNsignal):
      file = open(output_path + "RN" + str(x) + "_train", "w")
      list = RN[int(n_RNset*x):int(n_RNset*x+n_RNtrain)]
      list.sort()
      for index in list:
        file.write(str(index) + " ")
      file.close()

      file = open(output_path + "RN" + str(x) + "_validation", "w")
      list = RN[int(n_RNset*x+n_RNtrain):int(n_RNset*x+n_RNtrain+n_RNvalidation)]
      list.sort()
      for index in list:
        file.write(str(index) + " ")
      file.close()

      file = open(output_path + "RN" + str(x) + "_test", "w")
      list = RN[int(n_RNset*x+n_RNtrain+n_RNvalidation):int(n_RNset*(x+1))]
      list.sort()
      for index in list:
        file.write(str(index) + " ")
      file.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[A_generate_RNindex:main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
