import sys

from tqdm import tqdm
from global_vars import *
from B_half_bit_repitition.global_vars import *
from B_half_bit_repitition.process import process

n_RNsignal = 1



def main(file_name):
  try:
    for x in tqdm(range(n_RNsignal), desc="PROCESSING", ncols=100, unit=" set"):
      process(file_name, x, "_train")
      process(file_name, x, "_validation")
      process(file_name, x, "_test")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[A_proportion:main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
