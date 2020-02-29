import sys

from tqdm import tqdm
from global_vars import *
from B_split_set.global_vars import *
from B_split_set.load import load
from B_split_set.process import process

n_RNsignal = 3



def main(file_name):
  try:
    signal, databit = load(file_name)

    for x in tqdm(range(n_RNsignal), desc="PROCESSING", ncols=100, unit=" set"):
      process(signal, databit, file_name, x, "_train")
      process(signal, databit, file_name, x, "_validation")
      process(signal, databit, file_name, x, "_test")

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[B_split_set:main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
