import os
import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from read_set import *
from MLP.MLP import MLP



def MLP_test_one_bit_onehot(mlp, test_set, answer_set):
  try:
    success = 0
    for idx in tqdm(range(len(answer_set)), desc="TESTING", ncols=100, unit=" signal"):
      fail = False
      tmp_set = []
      for n in range(n_bit_data):
        if model_type == "one_bit":
          tmp_set.append(test_set[idx][int(n_bit*n):int(n_bit*(n+1))])
        elif model_type == "two_bit":
          tmp_set.append(test_set[idx][int(n_bit*2*n):int(n_bit*2*(n+1))])
      predict_set = mlp.test_model(np.array(tmp_set))

      for n in range(n_bit_data):
        #predict = mlp.test_model(np.array([test_set[idx][int(n_bit*n):int(n_bit*(n+1))]]))
        predict = predict_set[n]
        answer = answer_set[idx][n]
        predict = predict.argmax()

        if ((predict == 0 or predict == 1) and answer != 0) or ((predict == 2 or predict == 3) and answer != 1):
          fail = True
          break

      if fail is False:
        success += 1

    return success

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP_test_one_bit_onehot:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def MLP_test_one_bit_lowhigh(mlp, test_set, answer_set):
  try:
    success = 0
    for idx in tqdm(range(len(answer_set)), desc="TESTING", ncols=100, unit=" signal"):
      fail = False
      tmp_set = []
      for n in range(n_bit_data):
        if model_type == "one_bit":
          tmp_set.append(test_set[idx][int(n_bit*n):int(n_bit*(n+1))])
        elif model_type == "two_bit":
          tmp_set.append(test_set[idx][int(n_bit*2*n):int(n_bit*2*(n+1))])
      predict_set = mlp.test_model(np.array(tmp_set))

      for n in range(n_bit_data):
        #predict = mlp.test_model(np.array([test_set[idx][int(n_bit*n):int(n_bit*(n+1))]]))
        predict = predict_set[n]
        answer = answer_set[idx][n]

        threshold = 0.5
        if answer == 0:
          if (predict[0] < threshold and predict[1] < threshold) or (predict[0] > threshold and predict[1] > threshold):
            fail = True
            break
        elif answer == 1:
          if (predict[0] < threshold and predict[1] > threshold) or (predict[0] > threshold and predict[1] < threshold):
            fail = True
            break

      if fail is False:
        success += 1

    return success

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP_test_one_bit_lowhigh:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def MLP_test(path):
  try:
    mlp = MLP()
    tot_success = 0
    tot_size = 0

    log = open(log_full_path, "a")
    log.write("\t*** MLP_test *** model= " + model_type + model_postpix + " ***\n")

    if path == "":
      print("[Model path] " + str(os.listdir(model_path)) + "\n")
      model_name = input("Input the model name: ").rstrip("\n")
      path = model_path + model_name

    mlp.restore_model(path)
    log.write(path + " successfully loaded!\n")

    for file_name in file_name_list:
      try:
        print("\n\n\t*** " + file_name + " ***")
        log.write(file_name + " ")

        test_set = read_test_set(file_name, "_0")
        answer_set = read_answer_set(file_name)

        if (model_type == "one_bit" or model_type == "two_bit") and model_postpix == "_onehot":
          success = MLP_test_one_bit_onehot(mlp, test_set, answer_set)
        elif (model_type == "one_bit" or model_type == "two_bit") and model_postpix == "_lowhigh":
          success = MLP_test_one_bit_lowhigh(mlp, test_set, answer_set)
        elif model_type == "half_bit":
          success = MLP_test_half_bit(mlp, test_set, answer_set)
        else:
          raise ValueError("No function matching with model type named \"" + model_type + model_postpix + "\"!")

        print("\t\tSUCCESS= " + str(success) + " / " + str(len(answer_set)) + "\t(" + str(round(100 * success / len(answer_set), 2)) + "%)\n")
        log.write(str(success) + " " + str(len(answer_set)) + "\n")

        tot_success += success
        tot_size += len(answer_set)

      except Exception as ex:
        _, _, tb = sys.exc_info()
        print("[MLP_test:" + file_name + ":" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")

    print("\n\n\t\tTOTAL SUCCESS= " + str(tot_success) + " / " + str(tot_size) + "\t(" + str(round(100 * tot_success / tot_size, 2)) + "%)\n")
    log.write("TOTAL " + str(tot_success) + " " + str(tot_size) + "\n")
    log.close()
    return False

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP_test:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
