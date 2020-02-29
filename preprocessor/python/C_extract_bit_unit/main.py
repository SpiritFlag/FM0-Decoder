import sys

from global_vars import *
from C_extract_bit_unit.global_vars import *
from C_extract_bit_unit.load import load
from C_extract_bit_unit.process import process

set_name = ["_train", "_validation", "_test"]
set_size = [640, 160, 200]
#set_size = [1920, 480, 600]



def main(file_name):
  try:
    for idx in range(3):
      signal, databit = load(file_name, set_name[idx], set_size[idx])
      process(signal, databit, file_name, set_name[idx], set_size[idx])

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[C_extract_bit_unit:main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
