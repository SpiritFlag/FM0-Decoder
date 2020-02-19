import sys

from tqdm import tqdm
from global_vars import *



def read_train_set(set_name):
  try:
    train_set = []
    answer_set = []

    for f in tqdm(range(len(file_name_list)), desc="READING", ncols=100, unit=" file"):
      file_name = file_name_list[f]
      try:
        if model_type == "one_bit" or model_type == "two_bit":
          for x in range(4):
            n_lines = sum(1 for line in open(signal_path + file_name + "_RN" + str(RN_index) + "_" + set_name + "_" + str(x)))
            file = open(signal_path + file_name + "_RN" + str(RN_index) + "_" + set_name + "_" + str(x), "r")

            for idx in range(n_lines):
              sample = file.readline().rstrip(" \n").split(" ")
              sample = [float(i) for i in sample]
              if len(sample) < 100:
                print(file_name, x, idx, len(sample))
              train_set.append(sample)
              answer_set.append(x)

            file.close()

        elif model_type == "whole":
          n_lines = sum(1 for line in open(signal_path + file_name + "_" + set_name))

          file = open(signal_path + file_name + "_" + set_name, "r")
          for idx in range(n_lines):
            sample = file.readline().rstrip(" \n").split(" ")
            sample = [float(i) for i in sample]
            train_set.append(sample)

          file = open(databit_path + file_name + "_" + set_name + "_rep" + str(databit_repition), "r")
          for idx in range(n_lines):
            databit = file.readline().rstrip(" \n")
            databit = [int(i) for i in databit]
            answer_set.append(databit)
          file.close()

        else:
          raise ValueError("No function matching with model type named \"" + model_type + "\"!")

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[read_train_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    return train_set, answer_set

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[read_train_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def read_test_set(file_name, postpix):
  try:
    test_set = []
    n_lines = sum(1 for line in open(signal_path + file_name + "_RN" + str(RN_index) + "_test" + postpix))
    file = open(signal_path + file_name + "_RN" + str(RN_index) + "_test" + postpix, "r")

    for idx in tqdm(range(n_lines), desc="READING", ncols=100, unit=" signal"):
      sample = file.readline().rstrip(" \n").split(" ")
      sample = [float(i) for i in sample]
      test_set.append(sample)

    file.close()
    return test_set

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[read_test_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def read_answer_set(file_name):
  try:
    answer_set = []

    if model_type == "one_bit" or model_type == "two_bit":
      n_lines = sum(1 for line in open(databit_path + file_name + "_RN" + str(RN_index) + "_test"))
      file = open(databit_path + file_name + "_RN" + str(RN_index) + "_test", "r")
    elif model_type == "whole":
      n_lines = sum(1 for line in open(databit_path + file_name + "_RN" + str(RN_index) + "_test_rep" + str(databit_repition)))
      file = open(databit_path + file_name + "_RN" + str(RN_index) + "_test_rep" + str(databit_repition), "r")
    else:
      raise ValueError("No function matching with model type named \"" + model_type + "\"!")

    for idx in range(n_lines):
      databit = file.readline().rstrip(" \n")
      databit = [int(i) for i in databit]
      answer_set.append(databit)

    file.close()
    return answer_set

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[read_answer_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")