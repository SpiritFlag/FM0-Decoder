import sys

from A_IQconvert.main import main as IQconvert
from A_split_set.main import main as split_set
from X_convert_answer.main import main as convert_answer



if __name__ == "__main__":
  try:
    print("\n\n\t*** Select Menu ***")
    print("1. IQconvert")
    print("2. split_set")
    print("3. convert_answer")
    menu = int(input("\nSelect > "))

    if menu == 1:
      IQconvert()
    elif menu == 2:
      split_set()
    elif menu == 3:
      convert_answer()
    else:
      raise ValueError("Invalid menu number!")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
