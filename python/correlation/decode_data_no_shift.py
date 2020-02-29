import sys

from global_vars import *
from correlation.detect_preamble import *



mask0L = [1.0] * n_half_bit
mask0L += [-1.0] * n_half_bit
mask0L += [1.0] * n_half_bit
mask0L += [-1.0] * n_half_bit

mask0H = [-1.0] * n_half_bit
mask0H += [1.0] * n_half_bit
mask0H += [-1.0] * n_half_bit
mask0H += [1.0] * n_half_bit

mask1L = [1.0] * n_half_bit
mask1L += [-1.0] * n_bit
mask1L += [1.0] * n_half_bit

mask1H = [-1.0] * n_half_bit
mask1H += [1.0] * n_bit
mask1H += [-1.0] * n_half_bit



def decode_data(signal):
  try:
    start = detect_preamble(signal)
    state = -1
    decoded_bit = []
    len_bit = 49.29

    for bit in range(n_bit_data):
      cur_start = int(start + len_bit*bit)

      if state == 1:
        mask0 = mask0H
        mask1 = mask1H
      else:
        mask0 = mask0L
        mask1 = mask1L

      score0 = 0
      score1 = 0

      for mask_idx in range(2*n_bit):
        idx = cur_start - n_half_bit + mask_idx
        if idx >= len(signal): continue
        score0 += mask0[mask_idx] * signal[idx]
        score1 += mask1[mask_idx] * signal[idx]

      if score0 > score1:
        decoded_bit.append(0)
      else:
        decoded_bit.append(1)
        state *= -1

    return decoded_bit, start

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[decode_data:" + str(tb.tb_lineno) + "] " + str(ex))
