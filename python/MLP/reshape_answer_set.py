import sys

from tqdm import tqdm
from global_vars import *



def reshape_answer_set(answer_set):
  try:
    new_answer_set = []

    for idx in range(len(answer_set)):
      if (model_type == "one_bit" or model_type == "two_bit") and model_postpix == "_onehot":
        if answer_set[idx] == 0:
          new_answer_set.append([1, 0, 0, 0])
        elif answer_set[idx] == 1:
          new_answer_set.append([0, 1, 0, 0])
        elif answer_set[idx] == 2:
          new_answer_set.append([0, 0, 1, 0])
        elif answer_set[idx] == 3:
          new_answer_set.append([0, 0, 0, 1])
        else:
          raise ValueError("The value answer_set[" + str(idx) + "]= " + str(answer_set[idx]) + " must be within 0 to 3!")
      elif (model_type == "one_bit" or model_type == "two_bit") and model_postpix == "_lowhigh":
        if answer_set[idx] == 0:
          new_answer_set.append([0, 1])
        elif answer_set[idx] == 1:
          new_answer_set.append([1, 0])
        elif answer_set[idx] == 2:
          new_answer_set.append([0, 0])
        elif answer_set[idx] == 3:
          new_answer_set.append([1, 1])
        else:
          raise ValueError("The value answer_set[" + str(idx) + "]= " + str(answer_set[idx]) + " must be within 0 to 3!")
      elif model_type == "two_bit" and model_postpix == "_extendlowhigh":
        if answer_set[idx] == 0:
          new_answer_set.append([1, 0, 1, 0])
        elif answer_set[idx] == 1:
          new_answer_set.append([0, 1, 0, 1])
        elif answer_set[idx] == 2:
          new_answer_set.append([1, 0, 0, 1])
        elif answer_set[idx] == 3:
          new_answer_set.append([0, 1, 1, 0])
        else:
          raise ValueError("The value answer_set[" + str(idx) + "]= " + str(answer_set[idx]) + " must be within 0 to 3!")

    return new_answer_set

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[reshape_answer_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
