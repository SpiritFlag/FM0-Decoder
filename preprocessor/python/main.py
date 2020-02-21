import sys
import timeit

from tqdm import tqdm
from global_vars import *

from sample.CW_kalman import CW_kalman
from sample.std_cliffing import std_cliffing
from sample_set.generate_RNindex import generate_RNindex
from sample_set.generate_RNdatabit import generate_RNdatabit
from sample_set.generate_RNset import generate_RNset
from sample_set.bit_with_correlation import bit_with_correlation
from sample_set.generate_RNwhole_databit import generate_RNwhole_databit
from sample_set.generate_RNwhole_set import generate_RNwhole_set
from sample_set.generate_RNpreamble_set import generate_RNpreamble_set
from databit.half_bit_repitition import half_bit_repitition



if __name__ == "__main__":
  try:
    print("\n\n\t*** Select Menu ***")
    print("1. sample")
    print("2. sample_set")
    print("3. databit")
    menu = int(input("\nSelect > "))
    if menu < 1 or menu > 3:
      raise ValueError("User Interrupt")



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
        raise ValueError("User Interrupt")
    elif menu == 2: # 2. sample_set
      print("1. generate_RNindex")
      print("2. generate_RNdatabit")
      print("3. generate_RNset")
      print("4. bit_with_correlation")
      print("5. generate_RNwhole_databit")
      print("6. generate_RNwhole_set")
      print("7. generate_RNpreamble_set")
      menu = int(input("\nSelect > "))
      if menu == 1:
        menu = generate_RNindex
      elif menu == 2:
        menu = generate_RNdatabit
      elif menu == 3:
        menu = generate_RNset
      elif menu == 4:
        menu = bit_with_correlation
      elif menu == 5:
        menu = generate_RNwhole_databit
      elif menu == 6:
        menu = generate_RNwhole_set
      elif menu == 7:
        menu = generate_RNpreamble_set
      else:
        raise ValueError("User Interrupt")
    elif menu == 3: # 3. databit
      print("1. half_bit_repitition")
      menu = int(input("\nSelect > "))
      if menu == 1:
        menu = half_bit_repitition
      else:
        raise ValueError("User Interrupt")



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
    print("")
    print("n_RNtrain= " + str(n_RNtrain))
    print("n_RNvalidation= " + str(n_RNvalidation))
    print("n_RNtest= " + str(n_RNtest))
    print("n_RNset= " + str(n_RNset))
    print("n_RNsignal= " + str(n_RNsignal))

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
