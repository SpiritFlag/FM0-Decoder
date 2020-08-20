import sys

from global_vars import *
from X_make_signal_answer.global_vars import *



def encode_data(file, databit):
  try:
    if encoding_type == "onehot":
      level = -1

      for bit in databit:
        if encoding_unit == "bit":
          # L(10) H(01)
          if bit == 1:
            if level == 1:
              # State 1: HH
              file.write("0101")
            else:
              # State 4: LL
              file.write("1010")
            level *= -1
          else:
            if level == 1:
              # State 2: HL
              file.write("0110")
            else:
              # State 3: LH
              file.write("1001")

        elif encoding_unit == "signal":
          if bit == 1:
            if level == 1:
              # State 1: HH
              file.write("1000")
            else:
              # State 4: LL
              file.write("0001")
            level *= -1
          else:
            if level == 1:
              # State 2: HL
              file.write("0100")
            else:
              # State 3: LH
              file.write("0010")

    elif encoding_type == "regression":
      level = -1

      for bit in databit:
        # L(0) H(1)
        if bit == 1:
          if level == 1:
            # State 1: HH
            file.write("11")
          else:
            # State 4: LL
            file.write("00")
          level *= -1
        else:
          if level == 1:
            # State 2: HL
            file.write("10")
          else:
            # State 3: LH
            file.write("01")

    file.write("\n")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[X_make_signal_answer:encode_data:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
