import numpy as np

for n_bit in np.arange(48, 52.09, 0.1):
  # make signal
  mask = [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1]
  signal = []

  for i in range(25):
    signal.append(0)

  for x in range(12):
    for i in range(int((n_bit/2)*x), int((n_bit/2)*(x+1))):
      signal.append(mask[x])

  for i in range(25):
    signal.append(0)

  # make preamble mask
  mask = [1] * 50  # 1
  mask += [-1] * 25  # 2
  mask += [1] * 25
  mask += [-1] * 50  # 3
  mask += [1] * 25  # 4
  mask += [-1] * 25
  mask += [-1] * 50  # 5
  mask += [1] * 50  # 6

  # find max correlation value
  max_score = -10000
  max_idx = -1

  for idx in range(15, 35):
    score = 0
    for i in range(len(mask)):
      score += mask[i] * signal[idx+i]
    if score > max_score:
      max_score = score
      max_idx = idx

  print(round(n_bit, 1), max_idx-25, end=" ")

  # make half preamble mask
  maskA = [1] * 50  # 1
  maskA += [-1] * 25  # 2
  maskA += [1] * 25
  maskA += [-1] * 50  # 3

  maskB = [1] * 25  # 4
  maskB += [-1] * 25
  maskB += [-1] * 50  # 5
  maskB += [1] * 50  # 6

  # find max correlation value
  max_score = -10000
  max_idx = -1

  for idx in range(40):
    score = 0
    for i in range(len(maskA)):
      score += maskA[i] * signal[idx+i]
    if score > max_score:
      max_score = score
      max_idx = idx
  start_idx = max_idx

  max_score = -10000
  max_idx = -1

  for idx in range(start_idx+290, start_idx+310):
    score = 0
    for i in range(len(maskB)):
      score += maskB[i] * signal[idx-len(maskB)+i]
    if score > max_score:
      max_score = score
      max_idx = idx
  end_idx = max_idx

  start_idx = start_idx - 25
  end_idx = end_idx - 25
  calc_preamble = end_idx - start_idx
  real_preamble = int((n_bit/2)*12)
  print(start_idx, end_idx, calc_preamble, real_preamble)
