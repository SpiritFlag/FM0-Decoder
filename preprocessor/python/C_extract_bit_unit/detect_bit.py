import sys

from global_vars import *
from C_extract_bit_unit.global_vars import *



def detect_bit(signal, databit, state):
  try:
    if databit == 0 and state == -1:  # (H)LH(L)
      mask = [1.0] * n_half_bit
      mask += [-1.0] * n_half_bit
      mask += [1.0] * n_half_bit
      mask += [-1.0] * n_half_bit
      type = 0
    elif databit == 0 and state == 1: # (L)HL(H)
      mask = [-1.0] * n_half_bit
      mask += [1.0] * n_half_bit
      mask += [-1.0] * n_half_bit
      mask += [1.0] * n_half_bit
      type = 1
    elif databit == 1 and state == -1:  # (H)LL(H)
      mask = [1.0] * n_half_bit
      mask += [-1.0] * n_bit
      mask += [1.0] * n_half_bit
      type = 2
    elif databit == 1 and state == 1: # (l)HH(L)
      mask = [-1.0] * n_half_bit
      mask += [1.0] * n_bit
      mask += [-1.0] * n_half_bit
      type = 3
    else:
      raise ValueError("Invalid databit and state")

    max_score = -10000
    max_idx = 0

    for idx in range(int(2 * n_tolerance_bit + 1)):
      score = 0
      for mask_idx in range(len(mask)):
        score += mask[mask_idx] * signal[idx + mask_idx]
      if score > max_score:
        max_score = score
        max_idx = idx

    return max_score, max_idx, type

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[C_extract_bit_unit:detect_bit:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
