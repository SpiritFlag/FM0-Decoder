import random

from SignalSet import SignalSet

import global_vars
file_size = global_vars.file_size
test_size = global_vars.test_size
train_size = global_vars.train_size
validation_size = global_vars.validation_size



def make_set(input_signals, answer_signals):
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

    return input_set, answer_set

  except Exception as ex:
    print("[make_set.py]", end=" ")
    print(ex)
