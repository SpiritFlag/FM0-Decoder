# -*- coding: utf-8 -*-
import global_vars

num_half_bit = global_vars.num_half_bit
bit_preamble = global_vars.bit_preamble
bit_data = global_vars.bit_data
bit_extra = global_vars.bit_extra






def detect_data(signal):
  mask0L = [1.0] * num_half_bit
  mask0L += [-1.0] * num_half_bit
  mask0L += [1.0] * num_half_bit
  mask0L += [-1.0] * num_half_bit

  mask0H = [-1.0] * num_half_bit
  mask0H += [1.0] * num_half_bit
  mask0H += [-1.0] * num_half_bit
  mask0H += [1.0] * num_half_bit

  mask1L = [1.0] * num_half_bit
  mask1L += [-1.0] * 2 * num_half_bit
  mask1L += [1.0] * num_half_bit

  mask1H = [-1.0] * num_half_bit
  mask1H += [1.0] * 2 * num_half_bit
  mask1H += [-1.0] * num_half_bit

  idx = signal.index
  state = signal.level
  shift = [-3, -2, -1, 0, 1, 2, 3]  # 디코딩 성공률이 떨어질 경우 shift 범위를 넓힐 수 있음
  cur_shift = 0
  success = 0

  for num_bits in range(bit_data):
    if state == 1:
      mask0 = mask0H
      mask1 = mask1H
    else:
      mask0 = mask0L
      mask1 = mask1L

    max_score = 0
    max_value = -1

    for s in shift:
      score0 = 0
      score1 = 0

      for mask_idx in range(4 * num_half_bit):  # 앞뒤로 half bit씩 확장한 mask와 비교하기 때문에 index에서 num_half_bit을 빼주는 것에 주의
        if idx-num_half_bit+mask_idx+s >= len(signal.std_samples):
          continue
        score0 += mask0[mask_idx] * signal.std_samples[idx-num_half_bit+mask_idx+s]
        score1 += mask1[mask_idx] * signal.std_samples[idx-num_half_bit+mask_idx+s]

      if score0 > max_score:
        max_score = score0
        max_value = 0
        cur_shift = s
      if score1 > max_score:
        max_score = score1
        max_value = 1
        cur_shift = s
      #print(num_bits, idx, cur_shift, score0, score1, signal.answer[num_bits])

    # 틀린 bit가 나오면 곧바로 종료할 때는 이곳을 주석해제하여 사용
    '''
      if max_value == 1:
        state *= -1  # bit가 1인 경우에만 다음 bit의 시작이 반전
        if signal.answer[num_bits] != 1:
          return False
      else:
        if signal.answer[num_bits] != 0:
          return False

      idx += 2 * num_half_bit + cur_shift  # 보정된 shift는 다음 bit 해독에도 반영

    return True
    '''

    # 틀린 bit가 나와도 끝가지 디코딩하여 성공한 개수를 셀 때는 이곳을 주석해제하여 사용
    if max_value == 1:
      state *= -1  # bit가 1인 경우에만 다음 bit의 시작이 반전
      if signal.answer[num_bits] == 1:
        success += 1
    else:
      if signal.answer[num_bits] == 0:
        success += 1

    idx += 2 * num_half_bit + cur_shift  # 보정된 shift는 다음 bit 해독에도 반영

  return success
