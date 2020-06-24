import sys

from global_vars import *
from C_extract_bit_unit.global_vars import *
from C_extract_bit_unit.detect_preamble import detect_preamble



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



def decode_data(signal, databit, end=n_bit_data):
  try:
    pre_start = detect_preamble(signal)
    state = -1
    tot_shift = 0
    decoded_bit = []
    decoded_index = []

    for bit in range(end):
      cur_start = int(pre_start + n_bit*bit) + tot_shift
      if cur_start + 1.5*n_bit + n_shift >= len(signal):
        decoded_bit.append([])
        decoded_index.append(-1)
        continue

      if state == 1:
        if databit[bit] == 0:
          mask = mask0H
          decoded_index.append(1) # (L)HL(H)
        else:
          mask = mask1H
          decoded_index.append(3) # (L)HH(L)
      else:
        if databit[bit] == 0:
          mask = mask0L
          decoded_index.append(0) # (H)LH(L)
        else:
          mask = mask1L
          decoded_index.append(2) # (H)LL(H)

      max_score = -10000
      max_idx = 0

      for shift in range(-n_shift, n_shift+1):
        score = 0

        for mask_idx in range(2*n_bit):
          idx = cur_start - n_half_bit + mask_idx + shift
          score += mask[mask_idx] * signal[idx]

        if score > max_score:
          max_score = score
          max_idx = shift

      st = cur_start-n_half_bit+max_idx
      decoded_bit.append(signal[st:st+n_bit+n_bit])
      tot_shift += max_idx
      if databit[bit] == 1:
        state *= -1

    return decoded_bit, decoded_index

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[C_extract_bit_unit:decode_data:" + str(tb.tb_lineno) + "] " + str(ex))
