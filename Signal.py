# -*- coding: utf-8 -*-
import math

import global_vars

num_half_bit = global_vars.num_half_bit
num_bit_preamble = global_vars.bit_preamble * 2 * num_half_bit
num_bit_data = global_vars.bit_data * 2 * num_half_bit
num_bit_extra = global_vars.bit_extra * 2 * num_half_bit


class Signal:
  def __init__(self, file_name, data):
    self.file_name = file_name
    self.answer = [int(i) for i in data[0]]
    self.samples = list()
    for idx in range(1, len(data)-1):  # -1은 제일 뒤의 '\n'을 제거해주기 위함
      self.samples.append(data[idx])
    self.samples = [float(i) for i in self.samples]

    self.standardize_samples()
    self.index = self.detect_preamble()
    self.extract_data_samples()
    self.make_answer_samples()


  def standardize_samples(self):
    avg = 0
    for sample in self.samples:
      avg += sample
    avg /= len(self.samples)

    std = 0
    for sample in self.samples:
      std += pow(sample - avg, 2)
    std /= len(self.samples)
    std = math.sqrt(std)


    for idx in range(len(self.samples)):
      self.samples[idx] = (self.samples[idx] - avg) / std

    # cut
    for idx in range(len(self.samples)):
      if self.samples[idx] > 1:
        self.samples[idx] = 1
      elif self.samples[idx] < -1:
        self.samples[idx] = -1


  def detect_preamble(self):
    # preamble mask
    mask = [1.0] * 2 * num_half_bit  # 1
    mask += [-1.0] * num_half_bit  # 2
    mask += [1.0] * num_half_bit
    mask += [-1.0] * 2 * num_half_bit  # 3
    mask += [1.0] * num_half_bit  # 4
    mask += [-1.0] * num_half_bit
    mask += [-1.0] * 2 * num_half_bit  # 5
    mask += [1.0] * 2 * num_half_bit  # 6

    mask2 = mask[:]
    for idx in range(len(mask2)):
      mask2[idx] *= -1.0

    max_idx = 0
    max_score = 0
    self.state = 0

    for idx in range(num_bit_extra):
      score = 0
      score2 = 0
      for mask_idx in range(len(mask)):
        score += mask[mask_idx] * self.samples[idx+mask_idx]
        score2 += mask2[mask_idx] * self.samples[idx+mask_idx]
      if score > max_score:
        max_idx = idx
        max_score = score
        self.state = -1
      if score2 > max_score:
        max_idx = idx
        max_score = score2
        self.state = 1

    return max_idx + num_bit_preamble


  def extract_data_samples(self):
    self.data_samples = self.samples[self.index : self.index + num_bit_data]
    if self.state == 1:
      for idx in range(len(self.rev_cut_std_samples)):
        self.rev_cut_std_samples[idx] *= -1.0


  def make_answer_samples(self):
    self.answer_samples = list()
    level = -1
    for bit in self.answer:
      for i in range(0, num_half_bit):
        self.answer_samples.append(level)

      if bit:
        for i in range(0, num_half_bit):
          self.answer_samples.append(level)
      else:
        level *= -1
        for i in range(0, num_half_bit):
          self.answer_samples.append(level)
      level *= -1
