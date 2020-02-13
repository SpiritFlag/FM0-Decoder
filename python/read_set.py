import sys

from tqdm import tqdm
from global_vars import *



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
