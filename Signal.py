# -*- coding: utf-8 -*-
import math

class Signal:
  file_name = ""
  answer = ""
  samples = list()
  std_samples = list()

  def __init__(self, file_name, data):
    self.file_name = file_name
    self.answer = [int(i) for i in data[0]]
    self.samples = list()
    for idx in range(1, len(data)-1):  # -1은 제일 뒤의 '\n'을 제거해주기 위함
      self.samples.append(data[idx])
    self.samples = [float(i) for i in self.samples]

    avg = 0
    for sample in self.samples:
      avg += sample
    avg /= len(self.samples)

    std = 0
    for sample in self.samples:
      std += pow(sample - avg, 2)
    std /= len(self.samples)
    std = math.sqrt(std)

    self.std_samples = [((i - avg) / std) for i in self.samples]

    for idx in range(len(self.std_samples)):
      if self.std_samples[idx] > 1:
        self.std_samples[idx] = 1
      if self.std_samples[idx] < -1:
        self.std_samples[idx] = -1
