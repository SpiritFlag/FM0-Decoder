import sys
import os
import numpy as np
import tensorflow as tf

from tqdm import tqdm
from global_vars import *
from MLP.global_vars import *
from MLP.EarlyStoppingWithDecodingRate import EarlyStoppingWithDecodingRate



class MLP(tf.keras.Model):
  def __init__(self):
    try:
      super(MLP, self).__init__()

      optimizer = tf.keras.optimizers.Adam(learning_rate)
      self.model = eval("self.build_model" + model_postpix)()
      self.model.compile(loss=loss_function, optimizer=optimizer)
      self.model.summary()

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MLP.__init__:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def build_model_bit(self):
    try:
      size_input_layer = 100
      size_output_layer = 4

      self.input_layer = tf.keras.layers.Input(shape=(size_input_layer,), name="input")
      self.hidden_layer = []
      if is_batch_normalization is True:
        self.batch_layer = []
      self.activation_layer = []
      self.output_layer = tf.keras.layers.Dense(units=size_output_layer, name="output")
      self.output_activation_lyaer = tf.keras.layers.Activation(tf.nn.softmax, name="output_activation")

      layer = self.input_layer

      for idx in range(len(size_hidden_layer)):
        hidden_layer = tf.keras.layers.Dense(units=size_hidden_layer[idx], name="hidden"+str(idx+1))
        self.hidden_layer.append(hidden_layer)
        if is_batch_normalization is True:
          batch_layer = tf.keras.layers.BatchNormalization(name="batch"+str(idx+1))
          self.batch_layer.append(batch_layer)
        activation_layer = tf.keras.layers.Activation(tf.nn.relu, name="activation"+str(idx+1))
        self.activation_layer.append(activation_layer)

        layer = hidden_layer(layer)
        if is_batch_normalization is True:
          layer = batch_layer(layer)
        layer = activation_layer(layer)

      layer = self.output_activation_lyaer(self.output_layer(layer))
      return tf.keras.Model(self.input_layer, layer)

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MLP.build_model_bit:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def build_model_signal(self):
    try:
      size_input_layer = 6850
      size_output_layer = int(268 * amp_rep)

      self.input_layer = tf.keras.layers.Input(shape=(size_input_layer,), name="input")
      self.hidden_layer = []
      if is_batch_normalization is True:
        self.batch_layer = []
      self.activation_layer = []
      self.output_layer = tf.keras.layers.Dense(units=size_output_layer, name="output")

      layer = self.input_layer

      for idx in range(len(size_hidden_layer)):
        hidden_layer = tf.keras.layers.Dense(units=size_hidden_layer[idx], name="hidden"+str(idx+1))
        self.hidden_layer.append(hidden_layer)
        if is_batch_normalization is True:
          batch_layer = tf.keras.layers.BatchNormalization(name="batch"+str(idx+1))
          self.batch_layer.append(batch_layer)
        activation_layer = tf.keras.layers.Activation(tf.nn.relu, name="activation"+str(idx+1))
        self.activation_layer.append(activation_layer)

        layer = hidden_layer(layer)
        if is_batch_normalization is True:
          layer = batch_layer(layer)
        layer = activation_layer(layer)

      layer = self.output_layer(layer)
      return tf.keras.Model(self.input_layer, layer)

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MLP.build_model_signal:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def train_model(self, input, answer, validation):
    try:
      os.mkdir(model_full_path)
      hist = self.model.fit(input, answer, epochs=learning_epoch, batch_size=batch_size,
        callbacks=[EarlyStoppingWithDecodingRate(patience=patience, validation_data=validation, log_path=model_full_path)])
      self.model.save(model_full_path)

      return hist

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MLP.train_model:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def restore_model(self, path):
    try:
      self.model = tf.keras.models.load_model(path)
      self.model.summary()

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MLP.restore_model:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def test_model(self, input):
    try:
      if model_type == "bit":
        output = []

        for idx in tqdm(range(len(input)), desc="PREDICTING", ncols=100, unit=" signal"):
          test = []
          for x in range(n_bit_data):
            test.append(input[idx][int(100*x):int(100*(x+1))])
          result = self.model.predict(np.array(test))
          output.append(result)

        return output

      else:
        return self.model.predict(input)

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MLP.test_model:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
