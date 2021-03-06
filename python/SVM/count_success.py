import sys

from tqdm import tqdm
from global_vars import *



def count_success(clf, test_set, answer_set):
  try:
    success = 0
    for idx in tqdm(range(len(answer_set)), desc="TESTING", ncols=100, unit=" signal"):
      if len(test_set[idx]) == 0: # outlier
        continue

      fail = False

      for n in range(n_bit_data):
        if model_type == "bit_unit":
          predict = clf.predict([test_set[idx][int(n_bit*2*n):int(n_bit*2*(n+1))]])
        else:
          raise ValueError("No function matching with model type named \"" + model_type + "\"!")

        answer = answer_set[idx][n]
        if ((predict == 0 or predict == 1) and answer != 0) or ((predict == 2 or predict == 3) and answer != 1):
          fail = True
          break

      if fail is False:
        success += 1

    return success

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[count_success:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
