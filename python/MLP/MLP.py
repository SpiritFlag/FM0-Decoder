import sys
import os
import numpy as np
import tensorflow as tf

from tqdm import tqdm
from global_vars import *
from MLP.global_vars import *
from MLP.MyCallback import MyCallback



def my_softmax(input):
  try:
    if input.shape[0] == None:
      return input

    result = tf.nn.softmax(tf.split(input, int(input.shape[1] / size_slice), axis=1))
    return tf.squeeze(tf.concat(tf.split(result, result.shape[0], axis=0), axis=2))

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP.my_softmax:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def my_categorical_crossentropy(y_true, y_pred):
  try:
    tot_loss = 0
    loss_function = tf.keras.losses.CategoricalCrossentropy()

    split_true = tf.split(y_true, int(y_true.shape[1] / size_slice), axis=1)
    split_pred = tf.split(y_pred, int(y_pred.shape[1] / size_slice), axis=1)

    return loss_function(split_true, split_pred)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[MLP.my_categorical_crossentropy:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



class MLP(tf.keras.Model):
  def __init__(self, size_hidden_layer, learning_rate):
    try:
      super(MLP, self).__init__()

      self.learning_rate = learning_rate
      optimizer = tf.keras.optimizers.Adam(self.learning_rate)
      self.model = self.build_model(size_hidden_layer)
      #self.model.compile(loss=loss_function, optimizer=optimizer)
      if output_activation_function == "my_softmax_2":
        self.model.compile(loss="categorical_crossentropy", optimizer=optimizer)
      else:
        self.model.compile(loss=my_categorical_crossentropy, optimizer=optimizer)
      self.model.summary()

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MLP.__init__:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def build_model(self, size_hidden_layer):
    try:
      self.input_layer = tf.keras.layers.Input(shape=(size_input_layer,), name="input")
      self.noise_layer = tf.keras.layers.GaussianNoise(stddev=1, name="gaussian_noise")
      self.output_layer = tf.keras.layers.Dense(units=size_output_layer, name="output")

      if output_activation_function == "my_softmax":
        self.output_activation_layer = tf.keras.layers.Activation(my_softmax, name="output_activation")
      elif output_activation_function == "relu":
        self.output_activation_layer = tf.keras.layers.Activation(tf.nn.relu, name="output_activation")
      elif output_activation_function == "softmax":
        self.output_activation_layer = tf.keras.layers.Activation(tf.nn.softmax, name="output_activation")


      if is_gaussian_noise is True:
        layer = self.noise_layer(self.input_layer)
      else:
        layer = self.input_layer

      for idx in range(len(size_hidden_layer)):
        hidden_layer = tf.keras.layers.Dense(units=size_hidden_layer[idx], name="hidden"+str(idx+1))
        if is_batch_normalization is True:
          batch_layer = tf.keras.layers.BatchNormalization(name="batch"+str(idx+1))
        activation_layer = tf.keras.layers.Activation(tf.nn.relu, name="activation"+str(idx+1))
        if dropout_rate > 0:
          dropout_layer = tf.keras.layers.Dropout(rate=dropout_rate, name="dropout"+str(idx+1))

        layer = hidden_layer(layer)

        if is_batch_normalization is True:
          layer = batch_layer(layer)

        layer = activation_layer(layer)

        if dropout_rate > 0:
          layer = dropout_layer(layer)

      if output_activation_function == "my_softmax_2":
        partial_layer_list = []

        for idx in range(int(size_output_layer / 4)):
          partial_layer = tf.keras.layers.Dense(units=4, activation=tf.nn.softmax, name="output"+str(idx+1))
          partial_layer_list.append(partial_layer(layer))

        return tf.keras.Model(self.input_layer, partial_layer_list)

      else:
        layer = self.output_activation_layer(self.output_layer(layer))

      return tf.keras.Model(self.input_layer, layer)

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MLP.build_model:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def train_model(self, input, label, val_input, val_label, save_model=True):
    try:
      if os.path.isdir(model_full_path) is False:
        os.mkdir(model_full_path)

      n_slice = int(size_output_layer / 4)
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
      print("[MLP.train_model:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def restore_model(self, path):
    try:
      self.model = tf.keras.models.load_model(path, compile=False)
      #self.model.summary()

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MLP.restore_model:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def test_model(self, input):
    try:
      if model_type == "signal":
        if len(input) % batch_size == 0:
          n_batch = int(len(input) / batch_size)
        else:
          n_batch = int(len(input) / batch_size) + 1

        return self.model.predict(input, batch_size=batch_size, callbacks=[MyCallback(n_batch=n_batch)])

      elif model_type == "bit":
        output = []

        test = []
        for idx in range(len(input)):
          for x in range(n_bit_data):
            test.append(input[idx][int(2*n_bit*x):int(2*n_bit*(x+1))])

        result = self.model.predict(np.array(test))

        for x in range(len(input)):
          output.append(result[int(n_bit_data*x):int(n_bit_data*(x+1))])

        return output

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MLP.test_model:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
