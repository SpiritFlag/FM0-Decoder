import sys
import os
import gc
import psutil
import timeit
import tensorflow as tf

from global_vars import *
from MLP.global_vars import *
from MLP.count_success import count_success



class EarlyStoppingWithDecodingRate(tf.keras.callbacks.Callback):
  def __init__(self, patience=0, train_data=[], validation_data=[], learning_rate=1, test_fnc=None, log_path=""):
    try:
      super(EarlyStoppingWithDecodingRate, self).__init__()
      self.patience = patience
      self.train_data = train_data
      self.validation_data = validation_data
      self.learning_rate = learning_rate
      self.test_fnc = test_fnc
      self.log_path = log_path

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[EarlyStoppingWithDecodingRate.__init__:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def on_train_begin(self, epoch, logs=None):
    try:
      self.best_success = 0
      self.best_wait = 0
      self.best_epoch = 0
      self.best_weights = None

      self.fileL = open(self.log_path + "/loss", "w")
      self.fileS = open(self.log_path + "/success", "w")
      if train_learning_rate is True:
        self.fileH = open(log_full_path, "a")
        self.fileH.write(str(self.learning_rate) + "\n")

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[EarlyStoppingWithDecodingRate.on_train_begin:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def on_epoch_begin(self, epoch, logs=None):
    try:
      print("")

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[EarlyStoppingWithDecodingRate.on_epoch_begin:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def on_epoch_end(self, epoch, logs=None):
    try:
      #val_res = self.model.predict(self.validation_data[0])
      val_res = self.test_fnc(self.validation_data[0])
      val_ans = self.validation_data[1]
      success = count_success(val_res, val_ans)

      self.fileL.write(str(logs.get('loss')) + "\t")
      self.fileS.write(str(success) + "\t")
      print("\t\tVALIDATION SUCCESS= " + str(success) + " / " + str(len(val_ans)) + "\t(" + str(round(100 * success / len(val_ans), 2)) + "%)")

      if train_learning_rate is True:
        self.fileH.write(str(epoch + 1) + "\t" + str(success) + "\n")

      if success != 0:
        if success > self.best_success:
          self.best_wait = 0
          self.best_success = success
          self.best_epoch = epoch + 1

          if train_learning_rate is False:
            print("\tSTORING MODEL WEIGHTS..")
            self.best_weights = self.model.get_weights()
        else:
          self.best_wait += 1
          if self.best_wait >= self.patience:
            self.model.stop_training = True

          if train_learning_rate is False:
            print("\t" + str(self.best_wait) + " / " + str(self.patience) + "\tWAITING PATIENCE..")

      if train_learning_rate is True and success == 0 and epoch == 29:
        self.model.stop_training = True

      print("\tGARVAGE COLLECTER WORKING..")
      print(f"\t\tBEFORE= {round(psutil.Process(os.getpid()).memory_info()[0] / 2.**30, 1): 5.1f} GB", end="\t")
      time = timeit.default_timer()
      gc.collect()
      print(f"AFTER= {round(psutil.Process(os.getpid()).memory_info()[0] / 2.**30, 1): 5.1f} GB")
      print("\t\tEXECUTE TIME= " + str(round(timeit.default_timer() - time, 3)) + " (sec)\n")

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[EarlyStoppingWithDecodingRate.on_epoch_end:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def on_train_end(self, epoch, logs=None):
    try:
      print("\n\nEarly stopping and restoring model weights from the epoch " + str(self.best_epoch) + ".")
      if serach_hyperparameter is False:
        self.model.set_weights(self.best_weights)
      print("\t\tVALIDATION SUCCESS= " + str(self.best_success) + " / " + str(len(self.validation_data[1])) +
        "\t(" + str(round(100 * self.best_success / len(self.validation_data[1]), 2)) + "%)\n")

      self.fileL.close()
      self.fileS.write("\n" + str(self.best_epoch))
      self.fileS.close()

      if train_learning_rate is True:
        self.fileH.write(str(self.best_epoch) + "\t" + str(self.best_success) + "\n")
        self.fileH.write("\t" + str(len(self.validation_data[1])) + "\n\n")
        self.fileH.close()

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[EarlyStoppingWithDecodingRate.on_train_end:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
