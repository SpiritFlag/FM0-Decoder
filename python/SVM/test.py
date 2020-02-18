import os
import sys
import pickle

from tqdm import tqdm
from sklearn import svm
from sklearn.externals import joblib
from global_vars import *
from read_set import *
from SVM.count_success import count_success



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

        test_set = read_test_set(file_name, "_0")
        answer_set = read_answer_set(file_name)

        if model_type == "one_bit" or model_type == "two_bit":
          success = SVM_test_one_bit(clf, test_set, answer_set)
        elif model_type == "half_bit":
          success = SVM_test_half_bit(clf, test_set, answer_set)
        else:
          raise ValueError("No function matching with model type named \"" + model_type + "\"!")

        print("\t\tSUCCESS= " + str(success) + " / " + str(len(answer_set)) + "\t(" + str(round(100 * success / len(answer_set), 2)) + "%)\n")
        log.write(str(success) + " " + str(len(answer_set)) + "\n")

        tot_success += success
        tot_size += len(answer_set)

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[SVM_test:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    print("\n\n\t\tTOTAL SUCCESS= " + str(tot_success) + " / " + str(tot_size) + "\t(" + str(round(100 * tot_success / tot_size, 2)) + "%)\n")
    log.write("TOTAL " + str(tot_success) + " " + str(tot_size) + "\n")
    log.close()
    return False

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[SVM_test:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
