import sys
import numpy as np

from tqdm import tqdm
from global_vars import *

# train 40 + validation 10 + test 100 = one set 150
# set 150 × 20 = total 3000



def generate_RNindex(file_name):
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
    print("[generate_RNindex:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
