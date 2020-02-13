import os
import sys

from global_vars import *

def rename(ret):
  try:
    if ret is True:
      print("[Model path] " + str(os.listdir(model_path)))
      print("[Log path] " + str(os.listdir(log_path)) + "\n")
      new_name = input("Input the model and log name: ").rstrip("\n")
      os.rename(model_full_path, model_path + new_name)
      os.rename(log_full_path, log_path + new_name)
    else:
      print("[Log path] " + str(os.listdir(log_path)) + "\n")
      new_name = input("Input the log name: ").rstrip("\n")
      os.rename(log_full_path, log_path + new_name)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
