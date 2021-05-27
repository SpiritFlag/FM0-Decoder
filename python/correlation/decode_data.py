import sys

from global_vars import *
from correlation.global_vars import *
from correlation.detect_preamble import detect_preamble



if use_extra_half_bit is True:
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
else:
    mask0L = [-1.0] * n_half_bit
    mask0L += [1.0] * n_half_bit

    mask0H = [1.0] * n_half_bit
    mask0H += [-1.0] * n_half_bit

    mask1L = [-1.0] * n_bit

    mask1H = [1.0] * n_bit



def decode_data(signal):
    try:
        pre_start, pre_score = detect_preamble(signal)
        
        state = -1
        tot_shift = 0
        decoded_bit = []
        bit_index = []
        bit_score = []

        for bit in range(n_bit_data):
            cur_start = int(pre_start + constant_bit_len*bit) + tot_shift

            if cur_start + 1.5*n_bit + n_shift >= len(signal):
                decoded_bit.append(-1)
                bit_index.append(-1)
                bit_score.append(-1)
                continue

            if state == 1:
                mask0 = mask0H
                mask1 = mask1H
            else:
                mask0 = mask0L
                mask1 = mask1L

            max_score0 = -10000
            max_score1 = -10000
            max_idx0 = 0
            max_idx1 = 0

            for shift in range(-n_shift, n_shift+1):
                if full_candidate is False:
                    score0 = 0
                    score1 = 0

                    if use_extra_half_bit is True:
                        for mask_idx in range(2*n_bit):
                            idx = cur_start - n_half_bit + mask_idx + shift
                            score0 += mask0[mask_idx] * signal[idx]
                            score1 += mask1[mask_idx] * signal[idx]
                    else:
                        for mask_idx in range(n_bit):
                            idx = cur_start + mask_idx + shift
                            score0 += mask0[mask_idx] * signal[idx]
                            score1 += mask1[mask_idx] * signal[idx]

                    if score0 > max_score0:
                        max_score0 = score0
                        max_idx0 = shift
                    if score1 > max_score1:
                        max_score1 = score1
                        max_idx1 = shift

                else:
                    score0L = 0
                    score0H = 0
                    score1L = 0
                    score1H = 0

                    if use_extra_half_bit is True:
                        for mask_idx in range(2*n_bit):
                            idx = cur_start - n_half_bit + mask_idx + shift
                            score0L += mask0L[mask_idx] * signal[idx]
                            score1L += mask1L[mask_idx] * signal[idx]
                            score0H += mask0H[mask_idx] * signal[idx]
                            score1H += mask1H[mask_idx] * signal[idx]
                    else:
                        for mask_idx in range(n_bit):
                            idx = cur_start + mask_idx + shift
                            score0L += mask0L[mask_idx] * signal[idx]
                            score1L += mask1L[mask_idx] * signal[idx]
                            score0H += mask0H[mask_idx] * signal[idx]
                            score1H += mask1H[mask_idx] * signal[idx]

                    if score0L > max_score0:
                        max_score0 = score0L
                        max_idx0 = shift
                    if score0H > max_score0:
                        max_score0 = score0H
                        max_idx0 = shift
                    if score1L > max_score1:
                        max_score1 = score1L
                        max_idx1 = shift
                    if score1H > max_score1:
                        max_score1 = score1H
                        max_idx1 = shift

            if max_score0 > max_score1:
                tot_shift += max_idx0
                decoded_bit.append(0)
                bit_index.append(cur_start + max_idx0)
                bit_score.append(max_score0)
                #print(bit, cur_start, 0, max_idx0, max_score0, max_idx1, max_score1)
            else:
                state *= -1
                tot_shift += max_idx1
                decoded_bit.append(1)
                bit_index.append(cur_start + max_idx1)
                bit_score.append(max_score1)
                #print(bit, cur_start, 1, max_idx0, max_score0, max_idx1, max_score1)

        return decoded_bit, (pre_start-n_bit*n_bit_preamble), pre_score, bit_index, bit_score

    except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[decode_data:" + str(tb.tb_lineno) + "] " + str(ex))
