import sys

from global_vars import *
from B_half_bit_repitition.global_vars import *



def append_preamble(file):
  try:
    mask = [1] * 2 * repitition  # 1
    mask += [0] * repitition  # 2
    mask += [1] * repitition
    mask += [0] * 2 * repitition  # 3
    mask += [1] * repitition  # 4
    mask += [0] * repitition
    mask += [0] * 2 * repitition  # 5
    mask += [1] * 2 * repitition  # 6

    for sample in mask:
      file.write(str(sample))

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[B_half_bit_repitition:append_preamble:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
