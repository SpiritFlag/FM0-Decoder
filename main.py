import sys
import numpy as np

import global_vars
from main_fnc import set_file_name
from main_fnc import read_file
from main_fnc import grading
from SignalSet import SignalSet
from Autoencoder import Autoencoder

bit_data = global_vars.bit_data



def main_fnc(mode, folder_name):
  autoencoder = Autoencoder()
  file_name_list = set_file_name()
  input_set = SignalSet()
  answer_set = SignalSet()

  for file_name in file_name_list:
    input, answer = read_file(file_name)
    input_set.concatenate(input)
    answer_set.concatenate(answer)

  if mode == "train":
    autoencoder.train_model(np.array(input_set.train), np.array(answer_set.train), (np.array(input_set.validation), np.array(answer_set.validation)))
  elif mode == "restore":
    autoencoder.restore_model(folder_name)

  output = autoencoder.test_model(np.array(input_set.test))
  success = grading(output, answer_set.test)
  print(str(success) + " / " + str(len(answer_set.test)) + "\n\n")



if len(sys.argv) == 2 and sys.argv[1] == "1":
  main_fnc("train", "")
elif len(sys.argv) == 3 and sys.argv[1] == "2":
  main_fnc("restore", sys.argv[2])
elif len(sys.argv) > 1 and sys.argv[1] == "2":
  print("[Need parameter] Input model folder path")
else:
  print("[Need parameter] Select Mode (1:train model, 2:restore model)")
