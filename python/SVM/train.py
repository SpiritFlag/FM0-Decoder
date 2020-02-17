import sys
import timeit
import pickle

from tqdm import tqdm
from sklearn import svm
from sklearn.externals import joblib
from global_vars import *
from read_set import *



def SVM_train():
  try:
    train_set, answer_set = read_train_set("train")

    train_time = timeit.default_timer()
    clf = svm.SVC(verbose=True)
    clf.fit(train_set, answer_set)
    joblib.dump(clf, model_full_path)
    print("\t\tTRAIN TIME= " + str(round(timeit.default_timer() - train_time, 3)) + " (sec)\n")

    return True

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[SVM_train:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
