import sys
import os
import numpy as np
import tensorflow as tf

from tqdm import tqdm
from global_vars import *
from MLP.global_vars import *
from MLP.MyCallback import MyCallback



class CNN(tf.keras.Model):
  def __init__(self):
    try:
      super(CNN, self).__init__()

      optimizer = tf.keras.optimizers.Adam(learning_rate)
      self.model = self.build_model()
      self.model.compile(loss=loss_function, optimizer=optimizer)
      self.model.summary()

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[CNN.__init__:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def build_model(self):
    try:
      self.input_layer = tf.keras.layers.Input(shape=(1, size_input_layer, size_input_filter), name="input")
      self.noise_layer = tf.keras.layers.GaussianNoise(stddev=0.1, name="gaussian_noise")

      if is_gaussian_noise is True:
        layer = self.noise_layer(self.input_layer)
      else:
        layer = self.input_layer

      for idx in range(len(size_filter)):
        conv_layer = tf.keras.layers.Conv2D(filters=size_filter[idx], kernel_initializer='he_uniform', kernel_size=(1, size_conv_layer), name="conv"+str(idx+1))
        layer = conv_layer(layer)

        if is_batch_normalization is True:
          batch_layer = tf.keras.layers.BatchNormalization(name="conv_batch"+str(idx+1))
          layer = batch_layer(layer)

        activation_layer = tf.keras.layers.Activation(tf.nn.relu, name="conv_activation"+str(idx+1))
        layer = activation_layer(layer)

        # if dropout_rate > 0:
        #   dropout_layer = tf.keras.layers.Dropout(rate=dropout_rate, name="conv_dropout"+str(idx+1))
        #   layer = dropout_layer(layer)

        pool_layer = tf.keras.layers.MaxPooling2D(pool_size=(1, size_pool_layer), name="pool"+str(idx+1))
        layer = pool_layer(layer)

      self.flatten_layer = tf.keras.layers.Flatten(name="flatten")
      layer = self.flatten_layer(layer)

      for idx in range(len(size_dense_layer)):
        dense_layer = tf.keras.layers.Dense(units=size_dense_layer[idx], name="dense"+str(idx+1))
        layer = dense_layer(layer)

        if is_batch_normalization is True:
          batch_layer = tf.keras.layers.BatchNormalization(name="batch"+str(idx+1))
          layer = batch_layer(layer)

        activation_layer = tf.keras.layers.Activation(tf.nn.relu, name="activation"+str(idx+1))
        layer = activation_layer(layer)

        if dropout_rate > 0:
          dropout_layer = tf.keras.layers.Dropout(rate=dropout_rate, name="dropout"+str(idx+1))
          layer = dropout_layer(layer)

      partial_layer_list = []

      for idx in range(int(size_output_layer / size_slice)):
        if encoding_type == "onehot":
          partial_layer = tf.keras.layers.Dense(units=size_slice, activation=tf.nn.softmax, name="output"+str(idx+1))
        elif encoding_type == "binary":
          partial_layer = tf.keras.layers.Dense(units=size_slice, activation=tf.nn.sigmoid, name="output"+str(idx+1))
        partial_layer_list.append(partial_layer(layer))

      return tf.keras.Model(self.input_layer, partial_layer_list)

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[CNN.build_model:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def train_model(self, input, label, val_input, val_label, save_model=True):
    try:
      if os.path.isdir(model_full_path) is False:
        os.mkdir(model_full_path)

      n_slice = int(size_output_layer / size_slice)
      if len(input) % batch_size == 0:
        n_batch = int(len(input) / batch_size)
      else:
        n_batch = int(len(input) / batch_size) + 1

      hist = self.model.fit(input, np.hsplit(label, n_slice), epochs=learning_epoch, batch_size=batch_size, verbose=0,
        callbacks=[MyCallback(n_batch=n_batch, patience=patience, validation_data=[val_input, np.hsplit(val_label, n_slice)],\
          test_fnc=self.test_model, log_path=model_full_path)]\
        )

      if save_model is True:
        self.model.save(model_full_path)

      return hist

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[CNN.train_model:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def restore_model(self, path):
    try:
      self.model = tf.keras.models.load_model(path, compile=False)

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[CNN.restore_model:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def test_model(self, input):
    try:
      if len(input) % batch_size == 0:
        n_batch = int(len(input) / batch_size)
      else:
        n_batch = int(len(input) / batch_size) + 1

      return self.model.predict(input, batch_size=batch_size, callbacks=[MyCallback(n_batch=n_batch)])

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[CNN.test_model:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
