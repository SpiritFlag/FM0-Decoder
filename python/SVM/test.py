import os
import sys
import pickle

from tqdm import tqdm
from sklearn import svm
from sklearn.externals import joblib
from global_vars import *
from read_set import *



def SVM_test():
  try:
    tot_success = 0
    tot_size = 0

    log = open(log_full_path, "a")
    log.write("\t*** SVM_test ***\n")

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

        success = 0
        for idx in tqdm(range(len(answer_set)), desc="TESTING", ncols=100, unit=" signal"):
          fail = False

          for n in range(n_bit_data):
            predict = clf.predict([test_set[idx][int(n_bit*n):int(n_bit*(n+1))]])
            answer = answer_set[idx][n]
            if ((predict == 0 or predict == 1) and answer != 0) or ((predict == 2 or predict == 3) and answer != 1):
              fail = True
              break

          if fail is False:
            success += 1

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
