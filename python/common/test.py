import sys
import os
import timeit

from global_vars import *
from read_set import *



def common_test(test_path, fnc):
  try:
    if os.path.exists(log_path + "detail/"):
      select = input("The detailed log path is already exist. Press 'Y' if you want to rewrite. ")
      if select != 'Y':
        print("Execution aborted..")
        return False
      else:
        log_files = os.listdir(log_path + "detail/")
        for log in log_files:
          os.remove(log_path + "detail/" + log)
    else:
      os.mkdir(log_path + "detail/")

    tot_time = timeit.default_timer()
    log = open(log_full_path, "w")
    tot_success = 0
    tot_size = 0

    for file_name in file_name_list:
      try:
        print("\n\n\t*** " + file_name + " ***")
        log.write(file_name + "\t")
        test_set = read_test_set(test_path, file_name)
        answer_set = read_answer_set(test_path, file_name)

        time = timeit.default_timer()
        success, fnc_time = fnc(file_name, test_set, answer_set)

        if len(answer_set) != 0:
          print("\t\tSUCCESS= " + str(success) + " / " + str(len(answer_set)) + "\t(" + str(round(100 * success / len(answer_set), 2)) + "%)\n")
          log.write(str(success) + "\t" + str(len(answer_set)) + "\t")
        else:
          print("\t\tSUCCESS= 0 / 0 (- %)\n")
          log.write("0\t0\t")

        if len(fnc_time) > 0:
          log.write("\t".join([str(i) for i in fnc_time]))

        tot_success += success
        tot_size += len(answer_set)

        exec_time = timeit.default_timer() - time
        print("\n\t\tTEST TIME= " + str(round(exec_time, 3)) + " (sec)\n")
        log.write(str(exec_time) + "\n")

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[common_test:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    if tot_size != 0:
      print("\n\n\t\tTOTAL SUCCESS= " + str(tot_success) + " / " + str(tot_size) + "\t(" + str(round(100 * tot_success / tot_size, 2)) + "%)\n")
      log.write("TOTAL " + str(tot_success) + "\t" + str(tot_size) + "\n")
    else:
      print("\n\n\t\tTOTAL SUCCESS= 0 / 0 (- %)\n")
      log.write("TOTAL 0\t0\n")

    exec_time = timeit.default_timer() - tot_time
    print("\t\tTOTAL TEST TIME= " + str(round(exec_time, 3)) + " (sec)\n")
    log.write(str(exec_time) + "\n")
    log.close()

    return True

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[common_test:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
