import sys
import timeit

from tqdm import tqdm
from global_vars import *
from read_set import *
from correlation.decode_data import *



def correlation_fix_shift_3(path):
  try:
    tot_success = 0
    tot_size = 0

    log = open(log_full_path, "a")
    log.write("\t*** correlation_fix_shift_3 ***\n")

    for file_name in file_name_list:
      try:
        print("\n\n\t*** " + file_name + " ***")
        log.write(file_name + " ")

        test_set = read_test_set(file_name)
        answer_set = read_answer_set(file_name)

        success = 0
        for idx in tqdm(range(len(answer_set)), desc="TESTING", ncols=100, unit=" signal"):
          if len(test_set[idx]) == 1:
            continue

          predict = decode_data(test_set[idx])
          fail = False

          for n in range(n_bit_data):
            if predict[n] != answer_set[idx][n]:
              fail = True
              break

          if fail is False:
            success += 1

        if len(answer_set) != 0:
          print("\t\tSUCCESS= " + str(success) + " / " + str(len(answer_set)) + "\t(" + str(round(100 * success / len(answer_set), 2)) + "%)\n")
          log.write(str(success) + " " + str(len(answer_set)) + "\n")
        else:
          print("\t\tSUCCESS= 0 / 0 (- %)\n")
          log.write("0 0\n")

        tot_success += success
        tot_size += len(answer_set)

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[correlation_fix_shift_3:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    if tot_size != 0:
      print("\n\n\t\tTOTAL SUCCESS= " + str(tot_success) + " / " + str(tot_size) + "\t(" + str(round(100 * tot_success / tot_size, 2)) + "%)\n")
      log.write("TOTAL " + str(tot_success) + " " + str(tot_size) + "\n")
    else:
      print("\n\n\t\tTOTAL SUCCESS= 0 / 0 (- %)\n")
      log.write("TOTAL 0 0\n")
    log.close()
    return False, True

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[correlation_fix_shift_3:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
