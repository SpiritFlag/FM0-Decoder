import tensorflow as tf
import datetime

import global_vars
tail = global_vars.tail
model_path = global_vars.model_path
model_full_path = global_vars.model_full_path
model_tail = global_vars.model_tail



learning_rate = 0.001
learning_epoch = 100

class Autoencoder(tf.keras.Model):
  def __init__(self):
    try:
      super(Autoencoder, self).__init__()

      optimizer = tf.keras.optimizers.Adam(learning_rate)
      self.model = eval("self.build_model" + tail + model_tail)()
      self.model.compile(loss="mse", optimizer=optimizer)
      self.model.summary()

    except Exception as ex:
      print("[Autoencoder.__init__]", end=" ")
      print(ex)



  def build_model_LH(self):
    try:
      size_input_layer = 6400
      size_hidden_layer = 3100
      size_output_layer = 256

      self.input_layer = tf.keras.layers.Input(shape=(size_input_layer,), name="input")
      self.hidden_layer1 = tf.keras.layers.Dense(units=size_hidden_layer, activation=tf.nn.relu, name="hidden1")
      self.hidden_layer2 = tf.keras.layers.Dense(units=size_hidden_layer, activation=tf.nn.relu, name="hidden2")
      self.hidden_layer3 = tf.keras.layers.Dense(units=size_hidden_layer, activation=tf.nn.relu, name="hidden3")
      self.hidden_layer4 = tf.keras.layers.Dense(units=size_hidden_layer, activation=tf.nn.relu, name="hidden4")
      self.output_layer = tf.keras.layers.Dense(units=size_output_layer, name="output")

      layer = self.hidden_layer1(self.input_layer)
      layer = self.hidden_layer2(layer)
      layer = self.hidden_layer3(layer)
      layer = self.hidden_layer4(layer)
      layer = self.output_layer(layer)
      return tf.keras.Model(self.input_layer, layer)

    except Exception as ex:
      print("[Autoencoder.build_model]", end=" ")
      print(ex)



  def train_model(self, input, answer, validation):
    try:
      early_stopping = tf.keras.callbacks.EarlyStopping(monitor="val_loss", min_delta=0, patience=5, verbose=1, mode="min")
      self.model.fit(input, answer, epochs=learning_epoch, validation_data=validation, callbacks=[early_stopping])
      #self.model.fit(input, answer, epochs=learning_epoch, validation_data=validation)
      tf.keras.experimental.export_saved_model(self.model, model_full_path)

    except Exception as ex:
      print("[Autoencoder.train_model]", end=" ")
      print(ex)



  def restore_model(self, path):
    try:
      self.model = tf.keras.experimental.load_from_saved_model(model_path + path)
      self.model.summary()

    except Exception as ex:
      print("[Autoencoder.restore_model]", end=" ")
      print(ex)



  def test_model(self, input):
    try:
      return self.model.predict(input)

    except Exception as ex:
      print("[Autoencoder.test_model]", end=" ")
      print(ex)
