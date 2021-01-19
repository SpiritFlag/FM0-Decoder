import sys
import numpy as np



def encode_data(answer, encoding_unit, encoding_type):
  try:
    result = []

    if encoding_type == "onehot":
      level = -1

      for bit in answer:
        if encoding_unit == "bit":
          # L(10) H(01)
          if bit == 1:
            if level == 1:
              # State 1: HH
              result.extend([0, 1, 0, 1])
            else:
              # State 4: LL
              result.extend([1, 0, 1, 0])
            level *= -1
          else:
            if level == 1:
              # State 2: HL
              result.extend([0, 1, 1, 0])
            else:
              # State 3: LH
              result.extend([1, 0, 0, 1])

        elif encoding_unit == "signal":
          if bit == 1:
            if level == 1:
              # State 1: HH
              result.extend([1, 0, 0, 0])
            else:
              # State 4: LL
              result.extend([0, 0, 0, 1])
            level *= -1
          else:
            if level == 1:
              # State 2: HL
              result.extend([0, 1, 0, 0])
            else:
              # State 3: LH
              result.extend([0, 0, 1, 0])

    elif encoding_type == "regression":
      level = -1

      for bit in answer:
        # L(0) H(1)
        if bit == 1:
          if level == 1:
            # State 1: HH
            result.extend([1, 1])
          else:
            # State 4: LL
            result.extend([0, 0])
          level *= -1
        else:
          if level == 1:
            # State 2: HL
            result.extend([1, 0])
          else:
            # State 3: LH
            result.extend([0, 1])

    elif encoding_type == "binary":
      result = answer

    return np.array(result)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[X_convert_label:encode_data:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
