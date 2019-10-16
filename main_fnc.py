# -*- coding: utf-8 -*-
import random
import numpy as np
from tqdm import tqdm

import global_vars
from Signal import Signal
from SignalSet import SignalSet

bit_data = global_vars.bit_data

file_size = global_vars.file_size
test_size = global_vars.test_size
train_size = global_vars.train_size
validation_size = global_vars.validation_size

folder_path = global_vars.folder_path



def set_file_name():
  file_name_list = []
  
  for a in ["50", "100", "150", "200", "250", "300", "350", "400"]:
    for b in ["l", "r"]:
      for c in ["20", "60", "100"]:
        file_name_list.append(a + "_" + b + c)

  #file_name_list.append("50_l20")
  #file_name_list.append("50_r20")

  return file_name_list



def read_file(file_name):
  try:
    file = open(folder_path + file_name + "_s", "r")
    input_signals = []

    for n in tqdm(range(file_size), desc=file_name, ncols=80, unit="signal"):
      line = file.readline().rstrip(" \n")
      if not line: break
      data = line.split(" ")
      data = [float(i) for i in data]
      input_signals.append(data)

    file.close()

    file = open(folder_path + file_name + "_alh", "r")
    answer_signals = []

    for n in range(file_size):
      line = file.readline().rstrip("\n")
      if not line: break
      data = [int(i) for i in line]
      answer_signals.append(data)

    file.close()

  except Exception as ex:
    print("[Error: read file " + file_name + "] ", end="")
    print(ex)


  try:
    random_index = []

    while len(random_index) != file_size:
      index = random.randrange(0, file_size)
      if index not in random_index:
        random_index.append(index)

    input_set = SignalSet()
    answer_set = SignalSet()

    for idx in range(0, train_size):
      input_set.train.append(input_signals[random_index[idx]])
      answer_set.train.append(answer_signals[random_index[idx]])

    for idx in range(train_size, train_size + validation_size):
      input_set.validation.append(input_signals[random_index[idx]])
      answer_set.validation.append(answer_signals[random_index[idx]])

    for idx in range(train_size + validation_size, train_size + validation_size + test_size):
      input_set.test.append(input_signals[random_index[idx]])
      answer_set.test.append(answer_signals[random_index[idx]])

  except Exception as ex:
    print("[Error: make set " + file_name + "] ", end="")
    print(ex)

  return input_set, answer_set



def is_true(test, answer):
  count = 0
  for idx in range(2*bit_data):
    if (test[idx] < 0.5 and answer[idx] == 0) or (test[idx] >= 0.5 and answer[idx] == 1):
      count += 1
  return count



def grading(test, answer):
  success = 0
  success_bit = np.zeros(2*bit_data + 1)

  for idx in range(len(answer)):
    count = is_true(test[idx], answer[idx])
    success_bit[count] += 1
    if count == 2*bit_data:
      success += 1

  file = open("test_result", "w")
  file.write(str(success) + " / " + str(len(answer)) + "\n\n")
  for n in range(2*bit_data + 1):
    file.write(str(int(success_bit[n])) + " ")

  return success
