import sys
import tensorflow as tf

from global_vars import *
from MLP.global_vars import *
from MLP.count_success import count_success



class EarlyStoppingWithDecodingRate(tf.keras.callbacks.Callback):
  def __init__(self, patience=0, validation_data=[], log_path=""):
    try:
      super(EarlyStoppingWithDecodingRate, self).__init__()
      self.patience = patience
      self.validation_data = validation_data
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
      val_res = self.model.predict(self.validation_data[0])
      val_ans = self.validation_data[1]
      success = count_success(val_res, val_ans)

      self.fileL.write(str(logs.get('loss')) + "\t")
      self.fileS.write(str(success) + "\t")
      print("\t\tSUCCESS= " + str(success) + " / " + str(len(val_ans)) + "\t(" + str(round(100 * success / len(val_ans), 2)) + "%)")

      if success != 0:
        if success > self.best_success:
          self.best_wait = 0
          self.best_success = success
          self.best_epoch = epoch + 1

          print("\t\tStoring model weights..")
          self.best_weights = self.model.get_weights()
        else:
          self.best_wait += 1
          if self.best_wait >= self.patience:
            self.model.stop_training = True

      print("")

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[EarlyStoppingWithDecodingRate.on_epoch_end:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def on_train_end(self, epoch, logs=None):
    try:
      print("\n\nEarly stopping and restoring model weights from the epoch " + str(self.best_epoch) + ".")
      self.model.set_weights(self.best_weights)
      print("\t\tVALIDATION SUCCESS= " + str(self.best_success) + " / " + str(len(self.validation_data[1])) +
        "\t(" + str(round(100 * self.best_success / len(self.validation_data[1]), 2)) + "%)\n")

      self.fileL.close()
      self.fileS.write("\n" + str(self.best_epoch))
      self.fileS.close()

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[EarlyStoppingWithDecodingRate.on_train_end:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
