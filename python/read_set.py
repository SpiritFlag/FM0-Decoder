import sys

from tqdm import tqdm
from global_vars import *



def read_train_set(train_path, postfix):
  try:
    train_set = []
    answer_set = []

    for file_name in file_name_list:
      try:
        for x in range(4):
          n_lines = sum(1 for line in open(train_path + file_name + "_signal_" + postfix + "_" + str(x)))
          file = open(train_path + file_name + "_signal_" + postfix + "_" + str(x), "r")

          for idx in tqdm(range(n_lines), desc=file_name+" "+str(x), ncols=100, unit=" signal"):
            line = file.readline().rstrip(" \n").split(" ")
            train_set.append([float(i) for i in line])
            answer_set.append(x)

          file.close()


        '''
        n_lines = sum(1 for line in open(train_path + file_name + "_databit_" + postfix))
        file = open(train_path + file_name + "_databit_" + postfix, "r")

        for idx in range(n_lines):
          databit = file.readline().rstrip("\n")
          databit = [int(i) for i in databit]
          answer_set.append(databit)

        file.close()
        '''

        '''
        if model_type == "bit_unit":
          for x in range(4):
            n_lines = sum(1 for line in open(signal_path + file_name + "_RN" + str(RN_index) + "_signal_" + set_name + "_" + str(x)))
            file = open(signal_path + file_name + "_RN" + str(RN_index) + "_signal_" + set_name + "_" + str(x), "r")

            for idx in tqdm(range(n_lines), desc=file_name + " " + str(x+1), ncols=100, unit=" signal"):
              sample = file.readline().rstrip(" \n").split(" ")
              sample = [float(i) for i in sample]
              train_set.append(sample)
              answer_set.append(x)

            file.close()

        elif model_type == "whole":
          n_lines = sum(1 for line in open(signal_path + file_name + "_RN" + str(RN_index) + "_signal_" + set_name))

          file = open(signal_path + file_name + "_RN" + str(RN_index) + "_signal_" + set_name, "r")
          for idx in tqdm(range(n_lines), desc=file_name, ncols=100, unit=" signal"):
            sample = file.readline().rstrip(" \n").split(" ")
            sample = [float(i) for i in sample]
            train_set.append(sample)

          file = open(signal_path + file_name + "_RN" + str(RN_index) + "_databit_" + set_name + "_rep" + str(databit_repitition), "r")
          for idx in range(n_lines):
            databit = file.readline().rstrip(" \n")
            databit = [int(i) for i in databit]
            answer_set.append(databit)
          file.close()

        else:
          raise ValueError("No function matching with model type named \"" + model_type + "\"!")
        '''

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[read_train_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    return train_set, answer_set

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[read_train_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def read_test_set(test_path, file_name):
  try:
    test_set = []
    n_lines = sum(1 for line in open(test_path + file_name + "_signal_test"))
    file = open(test_path + file_name + "_signal_test", "r")

    for idx in tqdm(range(n_lines), desc="READING", ncols=100, unit=" signal"):
      sample = file.readline().rstrip(" \n").split(" ")
      sample = [float(i) for i in sample]
      test_set.append(sample)

    file.close()
    return test_set

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[read_test_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def read_answer_set(test_path, file_name):
  try:
    answer_set = []
    n_lines = sum(1 for line in open(test_path + file_name + "_databit_test"))
    file = open(test_path + file_name + "_databit_test", "r")

    for idx in tqdm(range(n_lines), desc="READING", ncols=100, unit=" signal"):
      databit = file.readline().rstrip("\n")
      databit = [int(i) for i in databit]
      answer_set.append(databit)

    file.close()
    return answer_set

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[read_answer_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
