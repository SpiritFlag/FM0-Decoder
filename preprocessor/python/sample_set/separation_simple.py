import sys
import itertools

from tqdm import tqdm
from global_vars import *
from read_data import *

ratio = 0.8



def separation_simple(file_name):
  try:
    for x in range(4):
      file = open(signal_path + file_name + "_" + str(x) + "_sample", "r")
      line_list = []
      for idx in itertools.count():
        line = file.readline()
        if line == "":
          break
        line_list.append(line)
      file.close()

      file = open(signal_path + file_name + "_" + str(x) + "_train", "w")
      for line in line_list[:int(len(line_list) * ratio)]:
        file.write(line)
      file.close()

      file = open(signal_path + file_name + "_" + str(x) + "_test", "w")
      for line in line_list[int(len(line_list) * ratio):]:
        file.write(line)
      file.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[separation:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
