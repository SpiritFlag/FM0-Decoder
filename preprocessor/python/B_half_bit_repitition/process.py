import sys

from global_vars import *
from B_half_bit_repitition.global_vars import *
from B_half_bit_repitition.load import load
from B_half_bit_repitition.append_preamble import append_preamble
from B_half_bit_repitition.enc_half_bit import enc_half_bit



def process(file_name, x, set_name):
  try:
    databit = load(file_name, x, set_name)

    file = open(output_path + file_name + "_RN" + str(x) + "_databit" + set_name + "_rep" + str(repitition), "w")
    for line in databit:
      append_preamble(file)
      enc_half_bit(file, line)
    file.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[B_half_bit_repitition:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
