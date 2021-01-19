import sys
import os
import gc
import timeit
import tensorflow as tf

from tqdm import tqdm
from global_vars import *
from MLP.global_vars import *
from MLP.count_success import count_success



class MyCallback(tf.keras.callbacks.Callback):
  def __init__(self, n_batch=0, patience=0, validation_data=[], test_fnc=None, log_path=""):
    try:
      super(MyCallback, self).__init__()
      self.n_batch = n_batch
      self.patience = patience
      self.validation_data = validation_data
      self.test_fnc = test_fnc
      self.log_path = log_path

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MyCallback.__init__:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def on_train_begin(self, epoch, logs=None):
    try:
      self.best_success = 0
      self.best_wait = 0
      self.best_epoch = 0
      self.best_weights = None

      self.n_val = len(self.validation_data[0])
      self.n_slice = len(self.validation_data[1])

      self.fileL = open(self.log_path + "/loss", "w")
      self.fileS = open(self.log_path + "/success", "w")

      print("\n\t*** TRAIN BEGIN ***", end="\n\n")

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MyCallback.on_train_begin:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def on_epoch_begin(self, epoch, logs=None):
    try:
      print(f"Epoch {epoch+1}/{learning_epoch}")
      self.pbar = tqdm(total=self.n_batch, desc="TRAINING", ncols=100, unit=" batch")
      self.epoch_time = timeit.default_timer()

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MyCallback.on_epoch_begin:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def on_train_batch_end(self, batch, logs=None):
    try:
      self.pbar.update(1)
      if batch+1 < self.n_batch:
        print(f" loss: {logs.get('loss'):.4f} - avg: {logs.get('loss')/self.n_slice:.4f}     ", end="\r")
      else:
        print("                              ", end="\r")

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MyCallback.on_train_batch_end:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def on_epoch_end(self, epoch, logs=None):
    try:
      self.pbar.close()

      val_res = self.test_fnc(self.validation_data[0])
      val_ans = self.validation_data[1]
      success = count_success(val_res, val_ans)

      self.fileL.write(str(logs.get('loss')) + "\t")
      self.fileS.write(str(success) + "\t")

      print(f"\t\tLOSS= {logs.get('loss'):.4f}\t\tAVG= {logs.get('loss')/self.n_slice:.4f}")
      print(f"\t\tVALIDATION SUCCESS=\t{success:5d} / {self.n_val:5d} ({100*success/self.n_val:2.2f}%)")

      if success != 0:
        if success > self.best_success:
          self.best_wait = 0
          self.best_success = success
          self.best_epoch = epoch + 1

          print("\tSTORING MODEL WEIGHTS..")
          self.best_weights = self.model.get_weights()

        else:
          self.best_wait += 1
          if self.best_wait >= self.patience:
            self.model.stop_training = True

          print(f"\t{self.best_wait} / {self.patience}\tWAITING PATIENCE..", end="\t")
          print(f"{self.best_success:5d} / {self.n_val:5d} ({100*self.best_success/self.n_val:2.2f}%)")

      gc.collect()
      print(f"\t\tEPOCH TIME= {timeit.default_timer()-self.epoch_time:.3f} (sec)")
      print("\n\n", end="")

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MyCallback.on_epoch_end:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def on_train_end(self, epoch, logs=None):
    try:
      print(f"\t*** Early stopping and restoring model weights from the epoch {self.best_epoch}. ***")
      self.model.set_weights(self.best_weights)
      print(f"\t\tVALIDATION SUCCESS=\t{self.best_success:5d} / {self.n_val:5d} ({100*self.best_success/self.n_val:2.2f}%)")
      print("\n\n", end="")

      self.fileL.close()
      self.fileS.write("\n" + str(self.best_epoch))
      self.fileS.close()

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MyCallback.on_train_end:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def on_predict_begin(self, logs=None):
    try:
      self.pbar_predict = tqdm(total=self.n_batch, desc="PREDICTING", ncols=100, unit=" batch")

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MyCallback.on_predict_begin:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def on_predict_batch_end(self, batch, logs=None):
    try:
      self.pbar_predict.update(1)

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MyCallback.on_predict_batch_end:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def on_predict_end(self, logs=None):
    try:
      self.pbar_predict.close()

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MyCallback.on_predict_end:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
