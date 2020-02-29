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
      if get_success is True:
        maskF = [1.0] * n_half_bit
        maskF += [-1.0] * n_bit
        maskF += [1.0] * n_half_bit
    elif databit == 0 and state == 1: # (L)HL(H)
      mask = [-1.0] * n_half_bit
      mask += [1.0] * n_half_bit
      mask += [-1.0] * n_half_bit
      mask += [1.0] * n_half_bit
      type = 1
      if get_success is True:
        maskF = [-1.0] * n_half_bit
        maskF += [1.0] * n_bit
        maskF += [-1.0] * n_half_bit
    elif databit == 1 and state == -1:  # (H)LL(H)
      mask = [1.0] * n_half_bit
      mask += [-1.0] * n_bit
      mask += [1.0] * n_half_bit
      type = 2
      if get_success is True:
        maskF = [1.0] * n_half_bit
        maskF += [-1.0] * n_half_bit
        maskF += [1.0] * n_half_bit
        maskF += [-1.0] * n_half_bit
    elif databit == 1 and state == 1: # (l)HH(L)
      mask = [-1.0] * n_half_bit
      mask += [1.0] * n_bit
      mask += [-1.0] * n_half_bit
      type = 3
      if get_success is True:
        maskF = [-1.0] * n_half_bit
        maskF += [1.0] * n_half_bit
        maskF += [-1.0] * n_half_bit
        maskF += [1.0] * n_half_bit
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

    if get_success is True:
      score = 0
      for mask_idx in range(len(maskF)):
        score += maskF[mask_idx] * signal[max_idx + mask_idx]

      if max_score > score:
        return max_score, max_idx, type, True
      else:
        return max_score, max_idx, type, False
    else:
      return max_score, max_idx, type, True

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[C_extract_bit_unit:detect_bit:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
