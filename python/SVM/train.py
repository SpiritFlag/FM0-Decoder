import sys
import timeit
import pickle

from tqdm import tqdm
from sklearn import svm
from sklearn.externals import joblib
from global_vars import *



def SVM_train():
  try:
    train_set = []
    answer_set = []

    log = open(log_full_path, "a")
    log.write("\t*** SVM_train ***\n")

    for f in tqdm(range(len(file_name_list)), desc="READING", ncols=100, unit=" file"):
      file_name = file_name_list[f]
      try:
        log.write(file_name + " ")

        for x in range(4):
          n_lines = sum(1 for line in open(signal_path + file_name + "_RN" + str(RN_index) + "_train_" + str(x)))
          log.write(str(n_lines) + " ")
          file = open(signal_path + file_name + "_RN" + str(RN_index) + "_train_" + str(x), "r")

          for idx in range(n_lines):
            sample = file.readline().rstrip(" \n").split(" ")
            sample = [float(i) for i in sample]
            train_set.append(sample)
            answer_set.append(x)

          file.close()
        log.write("\n")

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[SVM_train:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    train_time = timeit.default_timer()
    clf = svm.SVC(verbose=True)
    clf.fit(train_set, answer_set)
    joblib.dump(clf, model_full_path)
    print("\t\tTRAIN TIME= " + str(round(timeit.default_timer() - train_time, 3)) + " (sec)\n")
    log.write(model_full_path + " successfully trained!\n")

    print("\n\n")
    log.close()
    return True

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[SVM_train:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
