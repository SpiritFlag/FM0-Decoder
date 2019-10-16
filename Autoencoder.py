import time
import tensorflow as tf
import matplotlib.pyplot as plt

import global_vars

learning_rate = 0.001
learning_epoch = 1

size_input_layer = 6400
size_hidden_layer = 3100
size_output_layer = 256


class Autoencoder(tf.keras.Model):
  def __init__(self):
    super(Autoencoder, self).__init__()
    self.input_layer = tf.keras.layers.Input(shape=(size_input_layer,), name="input")
    self.hidden_layer1 = tf.keras.layers.Dense(units=size_hidden_layer, activation=tf.nn.relu, name="hidden1")
    self.hidden_layer2 = tf.keras.layers.Dense(units=size_hidden_layer, activation=tf.nn.relu, name="hidden2")
    self.hidden_layer3 = tf.keras.layers.Dense(units=size_hidden_layer, activation=tf.nn.relu, name="hidden3")
    self.hidden_layer4 = tf.keras.layers.Dense(units=size_hidden_layer, activation=tf.nn.relu, name="hidden4")
    self.hidden_layer5 = tf.keras.layers.Dense(units=size_hidden_layer, activation=tf.nn.relu, name="hidden5")
    self.output_layer = tf.keras.layers.Dense(units=size_output_layer, name="output")

    optimizer = tf.keras.optimizers.Adam(learning_rate)
    self.model = self.build_model()
    self.model.compile(loss="mse", optimizer=optimizer)
    self.model.summary()

  def build_model(self):
    layer = self.hidden_layer1(self.input_layer)
    layer = self.hidden_layer2(layer)
    layer = self.hidden_layer3(layer)
    layer = self.hidden_layer4(layer)
    #layer = self.hidden_layer5(layer)
    layer = self.output_layer(layer)
    return tf.keras.Model(self.input_layer, layer)

  def train_model(self, input, answer, validation):
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor="val_loss", min_delta=0, patience=5, verbose=1, mode="min")
    self.model.fit(input, answer, epochs=learning_epoch, validation_data=validation, callbacks=[early_stopping])

    saved_model_path = "saved_models/{}".format(int(time.time()))
    tf.keras.experimental.export_saved_model(self.model, saved_model_path)

  def restore_model(self, folder_name):
    self.model = tf.keras.experimental.load_from_saved_model("saved_models/" + folder_name)
    self.model.summary()

  def test_model(self, input):
    return self.model.predict(input)
