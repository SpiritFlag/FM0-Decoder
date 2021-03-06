import os
import sys

from tqdm import tqdm
from global_vars import *

from rename import rename
from correlation.test import correlation_test
from SVM.train import SVM_train
from SVM.test import SVM_test
from MLP.train import MLP_train
from MLP.test import MLP_test



if __name__ == "__main__":
  try:
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICES"] = cuda_device_id

    print("\n\n\t*** Select Menu ***")
    print("1. correlation")
    print("2. SVM")
    print("3. MLP")
    menu = int(input("\nSelect > "))
    if menu < 1 or menu > 3:
      raise ValueError("Invalid menu number!")

    print("\n\n\t*** Select Function ***")
    if menu == 1:
      menu = correlation_test
    elif menu == 2:
      print("1. train")
      print("2. test")
      menu = int(input("\nSelect > "))
      if menu == 1:
        menu = SVM_train
      elif menu == 2:
        menu = SVM_test
      else:
        raise ValueError("Invalid menu number!")
    elif menu == 3:
      print("1. train")
      print("2. test")
      menu = int(input("\nSelect > "))
      if menu == 1:
        menu = MLP_train
      elif menu == 2:
        menu = MLP_test
      else:
        raise ValueError("Invalid menu number!")

    model, log = menu("")
    rename(model, log)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
