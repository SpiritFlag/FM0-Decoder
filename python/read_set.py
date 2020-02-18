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
        for x in range(4):
          n_lines = sum(1 for line in open(signal_path + file_name + "_RN" + str(RN_index) + "_" + set_name + "_" + str(x)))
          file = open(signal_path + file_name + "_RN" + str(RN_index) + "_" + set_name + "_" + str(x), "r")

          for idx in range(n_lines):
            sample = file.readline().rstrip(" \n").split(" ")
            sample = [float(i) for i in sample]

            if model_type == "one_bit" or model_type == "two_bit":
              train_set.append(sample)
              answer_set.append(x)
            elif model_type == "half_bit":
              train_set.append(sample[0:n_half_bit])
              train_set.append(sample[n_half_bit:n_bit])
              if x == 0:
                answer_set.append(0)
                answer_set.append(1)
              elif x == 1:
                answer_set.append(1)
                answer_set.append(0)
              elif x == 2:
                answer_set.append(0)
                answer_set.append(0)
              elif x == 3:
                answer_set.append(1)
                answer_set.append(1)
            else:
              raise ValueError("No function matching with model type named \"" + model_type + "\"!")

          file.close()

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
    n_lines = sum(1 for line in open(databit_path + file_name + "_RN" + str(RN_index) + "_test"))
    file = open(databit_path + file_name + "_RN" + str(RN_index) + "_test", "r")

    for idx in range(n_lines):
      databit = file.readline().rstrip(" \n")
      databit = [int(i) for i in databit]
      answer_set.append(databit)

    file.close()
    return answer_set

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[read_answer_set:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
