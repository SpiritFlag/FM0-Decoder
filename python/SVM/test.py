import sys
import os
#import pickle

#from sklearn import svm
#from sklearn.externals import joblib
from global_vars import *
from common.test import common_test




from tqdm import tqdm
from read_set import *
from SVM.count_success import count_success





def main_fnc(file_name, test_set, answer_set):
  try:
    return process(file_name, test_set, answer_set)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[correlation_test:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def SVM_test(path):
  try:
    if common_test(signal_path, main_fnc):
      return False, True    # normal
    else:
      return False, False   # aborted

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[correlation_test:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")










def SVM_test(path):
  try:
    tot_success = 0
    tot_size = 0

    log = open(log_full_path, "a")
    log.write("\t*** SVM_test *** model= " + model_type + " ***\n")

    print("[Model path] " + str(os.listdir(model_path)) + "\n")
    model_name = input("Input the model name: ").rstrip("\n")
    model_full_path = model_path + model_name

    clf = joblib.load(model_full_path)
    log.write(model_full_path + " successfully loaded!\n")

    for file_name in file_name_list:
      try:
        print("\n\n\t*** " + file_name + " ***")
        log.write(file_name + " ")

        test_set = read_test_set(file_name)
        answer_set = read_answer_set(file_name)
        success = count_success(clf, test_set, answer_set)

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
        print("[SVM_test:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

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
    print("[SVM_test:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
