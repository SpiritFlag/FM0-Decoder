import sys

from global_vars import *
from B_half_bit_repitition.global_vars import *



def enc_half_bit(file, databit):
  try:
    conv = []
    level = -1

    for sample in databit:
      if sample == 1:
        conv.append(level)
        conv.append(level)
        level *= -1
      else:
        conv.append(level)
        conv.append(level * -1)

    for sample in conv:
      if sample == -1:
        for x in range(repitition):
          file.write("0")
      else:
        for x in range(repitition):
          file.write("1")
    file.write("\n")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[B_half_bit_repitition:enc_half_bit:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
