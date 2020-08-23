import sys

from global_vars import *



mask = [1.0] * n_bit  # 1
mask += [-1.0] * n_half_bit  # 2
mask += [1.0] * n_half_bit
mask += [-1.0] * n_bit  # 3
mask += [1.0] * n_half_bit  # 4
mask += [-1.0] * n_half_bit
mask += [-1.0] * n_bit  # 5
mask += [1.0] * n_bit  # 6



def detect_preamble(signal):
  try:
    max_score = -10000
    max_idx = 0

    for idx in range(n_cw, n_extra):
      score = 0
      for mask_idx in range(len(mask)):
        score += mask[mask_idx] * signal[idx + mask_idx]
      if score > max_score:
        max_score = score
        max_idx = idx

    return int(max_idx + n_bit * n_bit_preamble)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[B_extract_bit:detect_preamble:" + str(tb.tb_lineno) + "] " + str(ex))
