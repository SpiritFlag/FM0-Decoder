import sys
import timeit

from tqdm import tqdm
from global_vars import *
from read_set import *
from correlation.decode_data import *



def correlation_find_total_len(path):
  try:

    for file_name in file_name_list:
      try:
        print("\n\n\t*** " + file_name + " ***")
        test_set = read_test_set(file_name)
        answer_set = read_answer_set(file_name)

        cnt = 0
        for idx in tqdm(range(len(answer_set)), desc="TESTING", ncols=100, unit=" signal"):
          if len(test_set[idx]) == 1:
            continue

          predict, start, tot_shift = decode_data(test_set[idx])
          cnt += tot_shift
        print(cnt/200)

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[correlation_find_total_len:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    return False, False

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[correlation_find_total_len:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
