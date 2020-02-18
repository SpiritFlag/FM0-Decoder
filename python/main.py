import os
import sys
import timeit

from tqdm import tqdm
from global_vars import *

from rename import rename
from correlation.fix_shift_3 import correlation_fix_shift_3
from SVM.train import SVM_train
from SVM.test import SVM_test
from MLP.train import MLP_train
from MLP.test import MLP_test



if __name__ == "__main__":
  try:
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    print("\n\n\t*** Select Menu ***")
    print("1. correlation")
    print("2. SVM")
    print("3. MLP")
    menu = int(input("\nSelect > "))
    if menu < 1 or menu > 3:
      raise ValueError("User Interrupt")

    print("\n\n\t*** Select Function ***")
    if menu == 1: # 1. correlation
      print("1. fix_shift_3")
      menu = int(input("\nSelect > "))
      if menu == 1:
        menu = correlation_fix_shift_3
      else:
        raise ValueError("User Interrupt")
    elif menu == 2: # 2. SVM
      print("1. train")
      print("2. test")
      menu = int(input("\nSelect > "))
      if menu == 1:
        menu = SVM_train
      elif menu == 2:
        menu = SVM_test
      else:
        raise ValueError("User Interrupt")
    elif menu == 3: # 3. MLP
      print("1. train")
      print("2. test")
      menu = int(input("\nSelect > "))
      if menu == 1:
        menu = MLP_train
      elif menu == 2:
        menu = MLP_test
      else:
        raise ValueError("User Interrupt")

    print("\n\n\t*** Check Global Variables ***")
    print("file_name_list= " + str(file_name_list))
    print("RN_index= " + str(RN_index))
    print("")
    print("execute_time= " + str(execute_time))
    print("")
    print("databit_path= " + str(databit_path))
    print("signal_path= " + str(signal_path))
    print("model_type= " + str(model_type))
    print("")
    print("n_sample= " + str(n_sample))
    print("n_cw= " + str(n_cw))
    print("n_bit= " + str(n_bit))
    print("n_half_bit= " + str(n_half_bit))
    print("n_bit_preamble= " + str(n_bit_preamble))
    print("n_bit_data= " + str(n_bit_data))
    print("n_extra= " + str(n_extra))

    print("\n" + str(menu))
    chk = input("\nPress Y(y) to continue.. > ")
    if chk != "Y" and chk != "y":
      raise ValueError("User Interrupt")

    tot_time = timeit.default_timer()
    ret = menu("")
    print("\t\tTOTAL EXECUTION TIME= " + str(round(timeit.default_timer() - tot_time, 3)) + " (sec)\n")
    rename(ret)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
