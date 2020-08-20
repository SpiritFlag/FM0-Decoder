import sys
import numpy as np

from tqdm import tqdm
from global_vars import *



def shuffle_set(signal, answer):
  try:
    RNindex = np.arange(len(signal))
    np.random.shuffle(RNindex)

    new_signal = []
    new_answer = []

    for idx in range(len(RNindex)):
      new_signal.append(signal[RNindex[idx]])
      new_answer.append(answer[RNindex[idx]])

    return np.array(new_signal), np.array(new_answer)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[shuffle_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def read_set(signal_path, answer_path, answer_type, postfix, file_name_list, is_shuffle=False):
  try:
    signal = []
    answer = []

    for file_name in file_name_list:
      try:
        signal.extend(np.load(signal_path + file_name + "_signal_" + postfix + ".npy"))
        answer.extend(np.load(answer_path + file_name + "_answer_" + answer_type + "_" + postfix + ".npy"))

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[read_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    if is_shuffle is True:
      return shuffle_set(signal, answer)
    else:
      return np.array(signal), np.array(answer)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[read_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def read_train_set(train_path, answer_path, answer_type, postfix, model_type, file_name_list):
  try:
    train_set = []
    answer_set = []

    if postfix == "_test":
      ratio = 1
    else:
      ratio = 1
      #ratio = 0.25

    for file_name in file_name_list:
      try:
        if model_type == "bit":
          for x in range(4):
            n_lines = sum(1 for line in open(train_path + file_name + "_signal" + postfix + "_" + str(x)))
            file = open(train_path + file_name + "_signal" + postfix + "_" + str(x), "r")

            for idx in tqdm(range(n_lines), desc=file_name+" "+str(x), ncols=100, unit=" signal"):
              line = file.readline().rstrip(" \n").split(" ")
              train_set.append([float(i) for i in line])
              answer_set.append(x)

            file.close()

        elif model_type == "signal":
          if augment_training is True:
            for augment in augment_list:
              n_lines = sum(1 for line in open(train_path + file_name + "_signal_" + str(augment) + postfix))

              random_index = np.arange(n_lines)
              np.random.shuffle(random_index)
              reduced_index = np.sort(random_index[:int(ratio*n_lines)])

              fileA = open(train_path + file_name + "_signal_" + str(augment) + postfix, "r")
              fileB = open(answer_path + file_name + "_answer" + answer_type + postfix, "r")
              reduced_index_count = 0

              for idx in tqdm(range(n_lines), desc=file_name+" "+str(augment), ncols=100, unit=" signal"):
                if reduced_index_count >= int(ratio*n_lines):
                  break
                if idx != reduced_index[reduced_index_count]:
                  continue
                else:
                  train_set.append([float(i) for i in fileA.readline().rstrip(" \n").split(" ")])
                  answer_set.append([int(i) for i in fileB.readline().rstrip("\n")])
                  reduced_index_count += 1

              fileA.close()
              fileB.close()

          else:
            n_lines = sum(1 for line in open(train_path + file_name + "_signal" + postfix))
            if serach_hyperparameter is True:
              n_lines = int(n_lines * read_ratio)

            file = open(train_path + file_name + "_signal" + postfix, "r")
            for idx in tqdm(range(n_lines), desc=file_name, ncols=100, unit=" signal"):
              train_set.append([float(i) for i in file.readline().rstrip(" \n").split(" ")])
            file.close()

            file = open(answer_path + file_name + "_answer" + answer_type + postfix, "r")
            for idx in range(n_lines):
              answer_set.append([int(i) for i in file.readline().rstrip("\n")])
            file.close()

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[read_train_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    return train_set, answer_set

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[read_train_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def read_test_set(test_path, answer_type, file_name):
  try:
    if augment_training is True:
      for augment in augment_list:
        n_lines = sum(1 for line in open(test_path + file_name + "_signal_" + str(augment) + "_test"))

        file = open(test_path + file_name + "_signal_" + str(augment) + "_test", "r")
        for idx in tqdm(range(n_lines), desc=file_name+" "+str(augment), ncols=100, unit=" signal"):
          train_set.append([float(i) for i in file.readline().rstrip(" \n").split(" ")])
        file.close()

    else:
      if answer_type == "whole":
        n_lines = 500
        file = open(test_path + file_name + "_signal_test", "r")
      else:
        n_lines = sum(1 for line in open(test_path + file_name + "_signal_test"))
        file = open(test_path + file_name + "_signal_test", "r")

      test_set = []
      for idx in tqdm(range(n_lines), desc="READING", ncols=100, unit=" signal"):
        sample = file.readline().rstrip(" \n").split(" ")
        sample = [float(i) for i in sample]
        test_set.append(sample)

      file.close()
    return test_set

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[read_test_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def read_answer_set(answer_path, answer_type, file_name):
  try:
    if answer_type == "whole":
      n_lines = 500
      file = open(answer_path + file_name + "_databit", "r")
    else:
      n_lines = sum(1 for line in open(answer_path + file_name + "_answer" + answer_type + "_test"))
      file = open(answer_path + file_name + "_answer" + answer_type + "_test", "r")

    answer_set = []
    for idx in range(n_lines):
      answer_set.append([int(i) for i in file.readline().rstrip("\n")])
    file.close()

    return answer_set

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[read_answer_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
