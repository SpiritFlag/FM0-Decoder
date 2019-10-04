import tensorflow as tf
import matplotlib.pyplot as plt

import global_vars

size_input_layer = global_vars.size_input_layer
size_hidden_layer = global_vars.size_hidden_layer
size_output_layer = size_input_layer
learning_rate = 0.001
learning_epoch = 100


class Autoencoder(tf.keras.Model):
  def __init__(self):
    super(Autoencoder, self).__init__()
    self.input_layer = tf.keras.layers.Input(shape=(size_input_layer,))
    self.hidden_layer = tf.keras.layers.Dense(units=size_hidden_layer, activation=tf.nn.relu)
    self.output_layer = tf.keras.layers.Dense(units=size_output_layer)

    optimizer = tf.optimizers.Adam(learning_rate)
    self.model = self.build_model()
    self.model.compile(loss="mse", optimizer=optimizer)
    self.model.summary()

  def build_model(self):
    hidden = self.hidden_layer(self.input_layer)
    output = self.output_layer(hidden)
    return tf.keras.Model(self.input_layer, output)

  def train_model(self, input, answer):
    self.model.fit(input, answer, epochs=learning_epoch)

  def test_model(self, input, answer):
    output = self.model.predict(input)
    plt.plot(output[0])
    plt.show()
