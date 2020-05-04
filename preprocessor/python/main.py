import sys
import timeit

from global_vars import *
from A_IQconvert.main import main as IQconvert
from A_generate_RNindex.main import main as generate_RNindex
from B_split_set.main import main as split_set
from B_half_bit_repitition.main import main as half_bit_repitition
from C_extract_bit_unit.main import main as extract_bit_unit

if __name__ == "__main__":
  try:
    print("\n\n\t*** Select Menu ***")
    print("1. A_IQconvert")
    print("2. A_generate_RNindex")
    print("3. B_split_set")
    print("4. B_half_bit_repitition")
    print("5. C_extract_bit_unit")
    menu = int(input("\nSelect > "))

    if menu == 1:
      IQconvert()
    elif menu == 2:
      generate_RNindex()
    elif menu == 3:
      split_set()
    elif menu == 4:
      menu = half_bit_repitition
    elif menu == 5:
      menu = extract_bit_unit
    else:
      raise ValueError("Invalid menu number!")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
