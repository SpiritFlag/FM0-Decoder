import os
import sys
import pickle

from tqdm import tqdm
from sklearn import svm
from sklearn.externals import joblib
from global_vars import *
from read_set import *



def SVM_test_one_bit(clf, test_set, answer_set):
  try:
    success = 0
    for idx in tqdm(range(len(answer_set)), desc="TESTING", ncols=100, unit=" signal"):
      fail = False
      #print("!!!!!\t" + str(len(test_set[idx])))
      for n in range(n_bit_data):
        if model_type == "one_bit":
          predict = clf.predict([test_set[idx][int(n_bit*n):int(n_bit*(n+1))]])
        elif model_type == "two_bit":
          predict = clf.predict([test_set[idx][int(n_bit*2*n):int(n_bit*2*(n+1))]])
          #print([test_set[idx][int(n_bit*2*n):int(n_bit*2*(n+1))]])
          #print(predict)
        answer = answer_set[idx][n]
        if ((predict == 0 or predict == 1) and answer != 0) or ((predict == 2 or predict == 3) and answer != 1):
          fail = True
          break

      if fail is False:
        success += 1

    return success

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[SVM_test_one_bit:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def SVM_test_half_bit(clf, test_set, answer_set):
  try:
    success = 0
    for idx in tqdm(range(len(answer_set)), desc="TESTING", ncols=100, unit=" signal"):
      fail = False

      for n in range(n_bit_data):
        predict0 = clf.predict([test_set[idx][int(n_half_bit*2*n):int(n_half_bit*(2*n+1))]])
        predict1 = clf.predict([test_set[idx][int(n_half_bit*(2*n+1)):int(n_half_bit*(2*(n+1)))]])

        if predict0 == 0 and predict1 == 1:
          predict = 0
        elif predict0 == 1 and predict == 0:
          predict = 0
        elif predict0 == 0 and predict == 0:
          predict = 1
        elif predict0 == 1 and predict == 1:
          predict = 1
        else:
          predict = -1

        if predict != answer[idx][n]:
          fail = True
          break

      if fail is False:
        success += 1

    return success

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[SVM_test_half_bit:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



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
