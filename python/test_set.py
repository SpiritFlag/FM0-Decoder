import numpy as np

import test_sample

import global_vars
tail = global_vars.tail
log_path = global_vars.log_path



def test_set(test, answer):
  try:
    success = 0
    success_bit = np.zeros(len(test[0]) + 1)

    for idx in range(len(test)):
      count = eval("test_sample.test_sample" + tail)(test[idx], answer[idx])
      success_bit[count] += 1
      if count == len(test[0]):
        success += 1

    file = open(log_path, "w")
    file.write(str(success) + " / " + str(len(test)) + "\n\n")
    for idx in range(len(test[0]) + 1):
      file.write(str(int(success_bit[idx])) + " ")

    return success

  except Exception as ex:
    print("[test_set.py]", end=" ")
    print(ex)
