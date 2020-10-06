import sys

from A_IQconvert.main import main as IQconvert
from A_split_set.main import main as split_set
from A_sub_split_set.main import main as sub_split_set
from B_augment_sample.main import main as augment_sample
from B_extract_bit.main import main as extract_bit
from B_simple_convert.main import main as simple_convert
from X_convert_answer.main import main as convert_answer
from Y_analysis.main import main as analysis



if __name__ == "__main__":
  try:
    print("\n\n\t*** Select Menu ***")
    print("1. IQconvert")
    print("2. split set")
    print("3. sub_split set")
    print("4. augment sample")
    print("5. extract bit")
    print("6. simple conver")
    print("7. analysis")
    print("8. convert answer")
    menu = int(input("\nSelect > "))

    if menu == 1:
      IQconvert()
    elif menu == 2:
      split_set()
    elif menu == 3:
      sub_split_set()
    elif menu == 4:
      augment_sample()
    elif menu == 5:
      extract_bit()
    elif menu == 6:
      simple_convert()
    elif menu == 7:
      analysis()
    elif menu == 8:
      convert_answer()
    else:
      raise ValueError("Invalid menu number!")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
