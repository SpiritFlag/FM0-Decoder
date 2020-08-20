import sys

from global_vars import *
from X_make_signal_answer.global_vars import *



def append_preamble(file):
  try:
    if encoding_type == "onehot":
      if encoding_unit == "bit":
        # L(10) H(01)
        # Preamble: HH LH LL HL LL HH
        file.write("0101")
        file.write("1001")
        file.write("1010")
        file.write("0110")
        file.write("1010")
        file.write("0101")
      elif encoding_unit == "signal":
        # State 1: HH
        # State 2: HL
        # State 3: LH
        # State 4: LL
        # Preamble: HH LH LL HL LL HH
        # State: 1 3 4 2 4 1
        file.write("1000")
        file.write("0010")
        file.write("0001")
        file.write("0100")
        file.write("0001")
        file.write("1000")
    elif encoding_type == "regression":
      # L(0) H(1)
      # Preamble: HH LH LL HL LL HH
      file.write("110100100011")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[X_make_signal_answer:append_preamble:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
