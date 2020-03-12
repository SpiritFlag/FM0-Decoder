import sys
import timeit

from global_vars import *
from A_proportion.main import main as proportion
from A_generate_RNindex.main import main as generate_RNindex
from B_split_set.main import main as split_set
from B_half_bit_repitition.main import main as half_bit_repitition
from C_extract_bit_unit.main import main as extract_bit_unit

if __name__ == "__main__":
  try:
    print("\n\n\t*** Select Menu ***")
    print("1. A_proportion")
    print("2. A_generate_RNindex")
    print("3. B_split_set")
    print("4. B_half_bit_repitition")
    print("5. C_extract_bit_unit")
    menu = int(input("\nSelect > "))

    if menu == 1:
      menu = A_proportion
      file = True
    elif menu == 2:
      menu = generate_RNindex
      file = False
    elif menu == 3:
      menu = split_set
      file = True
    elif menu == 4:
      menu = half_bit_repitition
      file = True
    elif menu == 5:
      menu = extract_bit_unit
      file = True
    else:
      raise ValueError("Invalid menu number!")

    tot_time = timeit.default_timer()
    if file is True:
      for file_name in file_name_list:
        try:
          time = timeit.default_timer()
          print("\n\n\t*** " + file_name + " ***")
          menu(file_name)
          print("\n\t\tEXECUTION TIME= " + str(round(timeit.default_timer() - time, 3)) + " (sec)\n")

        except Exception as ex:
          _, _, tb = sys.exc_info()
          print("[main:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
    else:
      menu("")
    print("\t\tTOTAL EXECUTION TIME= " + str(round(timeit.default_timer() - tot_time, 3)) + " (sec)\n")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
