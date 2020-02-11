import sys
import timeit
import numpy as np

from tqdm import tqdm
from global_vars import *

from sample.CW_kalman import CW_kalman

if __name__ == "__main__":
  try:
    print("\n\n\t*** Select Menu ***")
    print("1. sample")
    menu = int(input("\nSelect > "))
    if menu < 1 or menu > 1:
      raise ValueError("The index of menu must be in between 1 to 1.")

    print("\n\n\t*** Select Function ***")
    if menu == 1: # 1. sample
      print("1. CW_kalman")
      menu = int(input("\nSelect > "))
      if menu < 1 or menu > 1:
        raise ValueError("The index of function must be in between 1 to 1.")
      menu = CW_kalman

    print("\n\n\t*** Check Global Variables ***")
    print("file_name_list= " + str(file_name_list))
    print("signal_path= " + str(signal_path))
    print("output_path= " + str(output_path))
    print("n_signal= " + str(n_signal))
    print("n_sample= " + str(n_sample))
    print("n_cw= " + str(n_cw))

    print("\n" + str(menu))
    chk = input("\nPress Y(y) to continue.. > ")
    if chk != "Y" and chk != "y":
      raise ValueError("User Interrupt")

    tot_time = timeit.default_timer()
    for file_name in file_name_list:
      try:
        time = timeit.default_timer()
        print("\n\n\t*** " + file_name + " ***")
        menu(file_name)
        print("\n\t\tEXECUTION TIME= " + str(round(timeit.default_timer() - time, 3)) + " (sec)\n")

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[main:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
    print("\t\tTOTAL EXECUTION TIME= " + str(round(timeit.default_timer() - tot_time, 3)) + " (sec)\n")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
