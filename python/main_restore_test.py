import os
import numpy as np

from Autoencoder import Autoencoder
from SignalSet import SignalSet

from read_file import read_file
from test_set import test_set

import global_vars
file_name_list = global_vars.file_name_list
model_path = global_vars.model_path




if __name__ == "__main__":
  model_name = ""

  try:
    print("\n\n\n" + str(os.listdir(model_path)))
    model_name = input("\n\n\nInput the model name you want to restore: ").rstrip("\n")
    if not os.path.exists(model_path + model_name):
      raise NameError("Model \"" + model_name + "\" does not exist")

    autoencoder = Autoencoder()
    input_set = []
    answer_set = []

    print("\n\n\n\t\t\t***** READING FILES *****")
    for file_name in file_name_list:
      input, answer = read_file(file_name)
      input_set += input
      answer_set += answer

    print("\n\n\n\t\t\t***** RESTORE MODEL *****")
    autoencoder.restore_model(model_name)

    success = test_set(autoencoder.test_model(np.array(input_set)), answer_set)
    print("\n\n\n\t\t\t***** TEST RESULT *****")
    print(str(success) + " / " + str(len(input_set)), end="\n\n\n")

  except Exception as ex:
    print("[main_restore_test.py]", end=" ")
    print(ex)
