import sys
import os
import timeit

from global_vars import *



def common_process(file, fnc, isFile):
  try:
    if os.path.exists(file):
      select = input("FILE is already exist. Press 'Y' if you want to rewrite. ")
      if select != 'Y':
        print("Execution aborted..")
        return

    tot_time = timeit.default_timer()

    if isFile is True:
      for file_name in file_name_list:
        try:
          time = timeit.default_timer()
          print("\n\n\t*** " + file_name + " ***")
          fnc(file_name)
          print("\n\t\tEXECUTION TIME= " + str(round(timeit.default_timer() - time, 3)) + " (sec)\n")

        except Exception as ex:
          _, _, tb = sys.exc_info()
          print("[common_process:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
    else:
      fnc()

    print("\t\tTOTAL EXECUTION TIME= " + str(round(timeit.default_timer() - tot_time, 3)) + " (sec)\n")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[common_process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
