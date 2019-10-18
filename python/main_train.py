import numpy as np

from Autoencoder import Autoencoder
from SignalSet import SignalSet

from read_file import read_file
from make_set import make_set
from test_set import test_set

import global_vars
file_name_list = global_vars.file_name_list



if __name__ == "__main__":
  try:
    autoencoder = Autoencoder()
    input_set = SignalSet()
    answer_set = SignalSet()

    print("\n\n\n\t\t\t***** READING FILES *****")
    for file_name in file_name_list:
      input, answer = read_file(file_name)
      input, answer = make_set(input, answer)
      input_set.concatenate(input)
      answer_set.concatenate(answer)

    print("\n\n\n\t\t\t***** TRAINING *****")
    autoencoder.train_model(np.array(input_set.train), np.array(answer_set.train), (np.array(input_set.validation), np.array(answer_set.validation)))

    success = test_set(autoencoder.test_model(np.array(input_set.test)), answer_set.test)
    print("\n\n\n\t\t\t***** TEST RESULT *****")
    print(str(success) + " / " + str(len(test_set.test)), end="\n\n\n")

  except Exception as ex:
    print("[main_train.py]", end=" ")
    print(ex)
