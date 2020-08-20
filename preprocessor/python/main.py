import sys
import timeit

from global_vars import *
from A_IQconvert.main import main as IQconvert
from A_generate_RNindex.main import main as generate_RNindex
from B_split_set.main import main as split_set
from C_extract_bit_unit.main import main as extract_bit_unit
from C_extract_bit_static.main import main as extract_bit_static
from D_augment_sample.main import main as augment_sample
from X_make_signal_answer.main import main as make_signal_answer

if __name__ == "__main__":
  try:
    print("\n\n\t*** Select Menu ***")
    print("1. A_IQconvert")
    print("2. A_generate_RNindex")
    print("3. B_split_set")
    print("4. C_extract_bit_unit")
    print("5. C_extract_bit_static")
    print("6. D_augment_sample")
    print("7. X_make_signal_answer")
    menu = int(input("\nSelect > "))

    if menu == 1:
      IQconvert()
    elif menu == 2:
      generate_RNindex()
    elif menu == 3:
      split_set()
    elif menu == 4:
      extract_bit_unit()
    elif menu == 5:
      extract_bit_static()
    elif menu == 6:
      augment_sample()
    elif menu == 7:
      make_signal_answer()
    else:
      raise ValueError("Invalid menu number!")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
