import sys
import timeit
import numpy as np

from tqdm import tqdm
from global_vars import *

from sample.CW_kalman import CW_kalman
from sample.std_cliffing import std_cliffing
from sample_set.separation_simple import separation_simple
from sample_set.bit_with_correlation import bit_with_correlation

if __name__ == "__main__":
  try:
    print("\n\n\t*** Select Menu ***")
    print("1. sample")
    print("2. sample_set")
    menu = int(input("\nSelect > "))
    if menu < 1 or menu > 2:
      raise ValueError("The index of menu must be in between 1 to 2.")

    print("\n\n\t*** Select Function ***")
    if menu == 1: # 1. sample
      print("1. CW_kalman")
      print("2. std_cliffing")
      menu = int(input("\nSelect > "))
      if menu == 1:
        menu = CW_kalman
      elif menu == 2:
        menu = std_cliffing
      else:
        raise ValueError("The index of function must be in between 1 to 2.")
    elif menu == 2: # 2. sample_set
      print("1. separation_simple")
      print("2. bit_with_correlation")
      menu = int(input("\nSelect > "))
      if menu == 1:
        menu = separation_simple
      elif menu == 2:
        menu = bit_with_correlation
      else:
        raise ValueError("The index of function must be in between 1 to 2.")

    print("\n\n\t*** Check Global Variables ***")
    print("file_name_list= " + str(file_name_list))
    print("")
    print("databit_path= " + str(databit_path))
    print("signal_path= " + str(signal_path))
    print("output_path= " + str(output_path))
    print("output_path2= " + str(output_path2))
    print("")
    print("n_signal= " + str(n_signal))
    print("n_sample= " + str(n_sample))
    print("n_cw= " + str(n_cw))
    print("n_bit= " + str(n_bit))
    print("n_half_bit= " + str(n_half_bit))
    print("n_tolerance_bit= " + str(n_tolerance_bit))
    print("n_bit_preamble= " + str(n_bit_preamble))
    print("n_bit_data= " + str(n_bit_data))
    print("n_extra= " + str(n_extra))

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
