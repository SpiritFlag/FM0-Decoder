import sys
import numpy as np



def append_preamble(encoding_unit, encoding_type):
  try:
    if encoding_type == "onehot":
      if encoding_unit == "bit":
        # L(10) H(01)
        # Preamble: HH LH LL HL LL HH
        return np.array([0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1])

      elif encoding_unit == "signal":
        # State 1: HH
        # State 2: HL
        # State 3: LH
        # State 4: LL
        # Preamble: HH LH LL HL LL HH
        # State: 1 3 4 2 4 1
        return np.array([1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0])

    elif encoding_type == "regression":
      # L(0) H(1)
      # Preamble: HH LH LL HL LL HH
      return np.array([1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1])

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[X_convert_answer:append_preamble:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
