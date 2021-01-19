import sys
import os

from global_vars import *
from common.test import common_test
from MLP.global_vars import *
from MLP.MLP import MLP
from MLP.CNN import CNN
from MLP.read_set import read_set
from MLP.process import process



def main_fnc(model, file_name, test_set, label_set):
  try:
    return process(model, file_name, test_set, label_set)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP_test:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def MLP_test(path):
  try:
    if os.path.isdir(signal_path) is False:
      raise NameError("signal_path= " + signal_path + " does not exist!")

    if os.path.isdir(label_path) is False:
      raise NameError("label_path= " + label_path + " does not exist!")

    if model_type != "CNN":
      mlp = MLP(size_hidden_layer, learning_rate)
    else:
      mlp = CNN()

    if path == "":
      print("[Model path] " + str(os.listdir(model_path)) + "\n")
      model_name = input("Input the model name: ").rstrip("\n")
      path = model_path + model_name
    mlp.restore_model(path)

    if common_test(model=mlp, fnc_read_set=read_set, fnc=main_fnc):
      return False, True    # normal
    else:
      return False, False   # aborted

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP_test:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
