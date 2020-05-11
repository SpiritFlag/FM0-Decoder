import sys
import timeit
import numpy as np

from tqdm import tqdm
from sklearn.svm import SVC
from sklearn.externals import joblib
from global_vars import *
from SVM.global_vars import *
from read_set import *
from SVM.test import SVM_test



def SVM_train(path):
  try:
    train_set, answer_set = read_train_set(signal_path, "train")

    new_train_set = []
    new_answer_set = []
    random_index = np.arange(len(train_set))
    np.random.shuffle(random_index)
    for idx in tqdm(range(len(random_index)), desc="SHUFFLE", ncols=100, unit=" bit"):
      new_train_set.append(train_set[random_index[idx]])
      new_answer_set.append(answer_set[random_index[idx]])

    train_time = timeit.default_timer()
    clf = SVC(verbose=True)
    clf.fit(new_train_set, new_answer_set)
    joblib.dump(clf, model_full_path)
    print("\t\tTRAIN TIME= " + str(round(timeit.default_timer() - train_time, 3)) + " (sec)\n")

    return True, False

    #ret = SVM_test(model_full_path)
    #return True, ret[1]

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[SVM_train:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
