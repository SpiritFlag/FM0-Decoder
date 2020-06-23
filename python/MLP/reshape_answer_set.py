import sys

from tqdm import tqdm
from global_vars import *
from MLP.global_vars import *



def reshape_answer_set(answer_set):
  try:
    new_answer_set = []

    if model_type == "bit":
      for answer in answer_set:
        if answer == 0:
          new_answer_set.append([1, 0, 0, 0])
        elif answer == 1:
          new_answer_set.append([0, 1, 0, 0])
        elif answer == 2:
          new_answer_set.append([0, 0, 1, 0])
        elif answer == 3:
          new_answer_set.append([0, 0, 0, 1])
        else:
          new_answer_set.append([0, 0, 0, 0])

    elif model_type == "signal":
      for answer_line in answer_set:
        new_answer = []

        # preamble
        new_answer = [1] * 2 * amp_rep
        new_answer += [0] * amp_rep  # 2
        new_answer += [1] * amp_rep
        new_answer += [0] * 2 * amp_rep  # 3
        new_answer += [1] * amp_rep  # 4
        new_answer += [0] * amp_rep
        new_answer += [0] * 2 * amp_rep  # 5
        new_answer += [1] * 2 * amp_rep  # 6

        # data
        level = 0

        for bit in answer_line:
          if bit == 1:
            new_answer += [level] * 2 * amp_rep
            if level == 0:
              level = 1
            elif level == 1:
              level = 0
          elif bit == 0:
            new_answer += [level] * amp_rep
            if level == 0:
              new_answer += [1] * amp_rep
            elif level == 1:
              new_answer += [0] * amp_rep

        new_answer_set.append(new_answer)

    return new_answer_set

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[reshape_answer_set:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
