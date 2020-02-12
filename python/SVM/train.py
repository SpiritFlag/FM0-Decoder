import itertools

from tqdm import tqdm
from sklearn import svm

signal_path = "data/C_bit_with_correlation/"

def SVM_train():
  X = []
  y = []

  for x in range(4):
    n_lines = sum(1 for line in open(signal_path + "100_0_0_" + str(x) + "_train"))
    file = open(signal_path + "100_0_0_" + str(x) + "_train", "r")

    for idx in tqdm(range(n_lines), desc="READING", ncols=100, unit=" signal"):
      sample = file.readline().rstrip(" \n").split(" ")
      sample = [float(i) for i in sample]
      X.append(sample)
      y.append(x)

  clf = svm.SVC(verbose=True)
  clf.fit(X, y)

  sample_list = []
  answer_list = []

  for x in range(4):
    n_lines = sum(1 for line in open(signal_path + "100_0_0_" + str(x) + "_test"))
    file = open(signal_path + "100_0_0_" + str(x) + "_test", "r")

    for idx in tqdm(range(n_lines), desc="READING", ncols=100, unit=" signal"):
      sample = file.readline().rstrip(" \n").split(" ")
      sample = [float(i) for i in sample]
      sample_list.append(sample)
      answer_list.append(x)

  clf.predict(sample_list)
