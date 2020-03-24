import sys
import tensorflow as tf

from tensorflow.keras import backend as K
from global_vars import *



class MLP(tf.keras.Model):
  def __init__(self):
    try:
      super(MLP, self).__init__()

      optimizer = tf.keras.optimizers.Adam(learning_rate)
      self.model = eval("self.build_model_" + model_type + model_postpix)()
      self.model.compile(loss=loss_function, optimizer=optimizer)
      self.model.summary()

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MLP.__init__:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def build_model_bit_unit_1(self):
    try:
      size_input_layer = 100
      size_hidden_layer1 = 100
      size_hidden_layer2 = 50
      size_output_layer = 4

      self.input_layer = tf.keras.layers.Input(shape=(size_input_layer,), name="input")

      self.hidden_layer1 = tf.keras.layers.Dense(units=size_hidden_layer1, name="hidden1")
      self.batch_layer1 = tf.keras.layers.BatchNormalization(name="batch1")
      self.activation_layer1 = tf.keras.layers.Activation(tf.nn.relu, name="activation1")

      self.hidden_layer2 = tf.keras.layers.Dense(units=size_hidden_layer2, name="hidden2")
      self.batch_layer2 = tf.keras.layers.BatchNormalization(name="batch2")
      self.activation_layer2 = tf.keras.layers.Activation(tf.nn.relu, name="activation2")

      self.output_layer = tf.keras.layers.Dense(units=size_output_layer, name="output")
      self.output_activation_lyaer = tf.keras.layers.Activation(tf.nn.softmax, name="output_activation")

      layer = self.activation_layer1(self.batch_layer1(self.hidden_layer1(self.input_layer)))
      layer = self.activation_layer2(self.batch_layer2(self.hidden_layer2(layer)))
      #layer = self.output_layer(layer)
      layer = self.output_activation_lyaer(self.output_layer(layer))
      return tf.keras.Model(self.input_layer, layer)

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MLP.build_model_bit_unit_1:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def build_model_whole_rep_1(self):
    try:
      size_input_layer = 6850
      size_hidden_layer1 = 3350
      size_hidden_layer2 = 3350
      size_hidden_layer3 = 6700
      size_hidden_layer4 = 6700
      size_hidden_layer5 = 1340
      size_hidden_layer6 = 1340
      size_output_layer = int(268 * databit_repitition)

      self.input_layer = tf.keras.layers.Input(shape=(size_input_layer,), name="input")

      self.hidden_layer1 = tf.keras.layers.Dense(units=size_hidden_layer1, name="hidden1")
      self.batch_layer1 = tf.keras.layers.BatchNormalization(name="batch1")
      self.activation_layer1 = tf.keras.layers.Activation(tf.nn.relu, name="activation1")

      self.hidden_layer2 = tf.keras.layers.Dense(units=size_hidden_layer2, name="hidden2")
      self.batch_layer2 = tf.keras.layers.BatchNormalization(name="batch2")
      self.activation_layer2 = tf.keras.layers.Activation(tf.nn.relu, name="activation2")

      self.hidden_layer3 = tf.keras.layers.Dense(units=size_hidden_layer3, name="hidden3")
      self.batch_layer3 = tf.keras.layers.BatchNormalization(name="batch3")
      self.activation_layer3 = tf.keras.layers.Activation(tf.nn.relu, name="activation3")

      self.hidden_layer4 = tf.keras.layers.Dense(units=size_hidden_layer4, name="hidden4")
      self.batch_layer4 = tf.keras.layers.BatchNormalization(name="batch4")
      self.activation_layer4 = tf.keras.layers.Activation(tf.nn.relu, name="activation4")

      self.hidden_layer5 = tf.keras.layers.Dense(units=size_hidden_layer5, name="hidden5")
      self.batch_layer5 = tf.keras.layers.BatchNormalization(name="batch5")
      self.activation_layer5 = tf.keras.layers.Activation(tf.nn.relu, name="activation5")

      self.hidden_layer6 = tf.keras.layers.Dense(units=size_hidden_layer6, name="hidden6")
      self.batch_layer6 = tf.keras.layers.BatchNormalization(name="batch6")
      self.activation_layer6 = tf.keras.layers.Activation(tf.nn.relu, name="activation6")

      self.output_layer = tf.keras.layers.Dense(units=size_output_layer, name="output")
      self.output_activation_lyaer = tf.keras.layers.Activation(tf.nn.sigmoid, name="output_activation")

      layer = self.activation_layer1(self.batch_layer1(self.hidden_layer1(self.input_layer)))
      layer = self.activation_layer2(self.batch_layer2(self.hidden_layer2(layer)))
      layer = self.activation_layer3(self.batch_layer3(self.hidden_layer3(layer)))
      layer = self.activation_layer4(self.batch_layer4(self.hidden_layer4(layer)))
      layer = self.activation_layer5(self.batch_layer5(self.hidden_layer5(layer)))
      layer = self.activation_layer6(self.batch_layer6(self.hidden_layer6(layer)))
      layer = self.output_layer(layer)
      #layer = self.output_activation_lyaer(self.output_layer(layer))
      return tf.keras.Model(self.input_layer, layer)

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MLP.build_model_whole_rep:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def build_model_whole_rep_25(self):
    try:
      size_input_layer = 6850
      size_hidden_layer1 = 3350
      size_hidden_layer2 = 3350
      size_hidden_layer3 = 10050
      size_hidden_layer4 = 10050
      size_hidden_layer5 = 3350
      size_hidden_layer6 = 3350
      size_output_layer = 6700

      self.input_layer = tf.keras.layers.Input(shape=(size_input_layer,), name="input")

      self.hidden_layer1 = tf.keras.layers.Dense(units=size_hidden_layer1, name="hidden1")
      self.batch_layer1 = tf.keras.layers.BatchNormalization(name="batch1")
      self.activation_layer1 = tf.keras.layers.Activation(tf.nn.relu, name="activation1")

      self.hidden_layer2 = tf.keras.layers.Dense(units=size_hidden_layer2, name="hidden2")
      self.batch_layer2 = tf.keras.layers.BatchNormalization(name="batch2")
      self.activation_layer2 = tf.keras.layers.Activation(tf.nn.relu, name="activation2")

      self.hidden_layer3 = tf.keras.layers.Dense(units=size_hidden_layer3, name="hidden3")
      self.batch_layer3 = tf.keras.layers.BatchNormalization(name="batch3")
      self.activation_layer3 = tf.keras.layers.Activation(tf.nn.relu, name="activation3")

      self.hidden_layer4 = tf.keras.layers.Dense(units=size_hidden_layer4, name="hidden4")
      self.batch_layer4 = tf.keras.layers.BatchNormalization(name="batch4")
      self.activation_layer4 = tf.keras.layers.Activation(tf.nn.relu, name="activation4")

      self.hidden_layer5 = tf.keras.layers.Dense(units=size_hidden_layer5, name="hidden5")
      self.batch_layer5 = tf.keras.layers.BatchNormalization(name="batch5")
      self.activation_layer5 = tf.keras.layers.Activation(tf.nn.relu, name="activation5")

      self.hidden_layer6 = tf.keras.layers.Dense(units=size_hidden_layer6, name="hidden6")
      self.batch_layer6 = tf.keras.layers.BatchNormalization(name="batch6")
      self.activation_layer6 = tf.keras.layers.Activation(tf.nn.relu, name="activation6")

      self.output_layer = tf.keras.layers.Dense(units=size_output_layer, name="output")
      self.output_activation_lyaer = tf.keras.layers.Activation(tf.nn.sigmoid, name="output_activation")

      layer = self.activation_layer1(self.batch_layer1(self.hidden_layer1(self.input_layer)))
      layer = self.activation_layer2(self.batch_layer2(self.hidden_layer2(layer)))
      layer = self.activation_layer3(self.batch_layer3(self.hidden_layer3(layer)))
      layer = self.activation_layer4(self.batch_layer4(self.hidden_layer4(layer)))
      layer = self.activation_layer5(self.batch_layer5(self.hidden_layer5(layer)))
      layer = self.activation_layer6(self.batch_layer6(self.hidden_layer6(layer)))
      layer = self.output_layer(layer)
      #layer = self.output_activation_lyaer(self.output_layer(layer))
      return tf.keras.Model(self.input_layer, layer)

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MLP.build_model_whole_rep:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def train_model(self, input, answer, validation):
    try:
      if isEarlyStop:
        early_stopping = tf.keras.callbacks.EarlyStopping(monitor="val_loss", min_delta=0, patience=2, verbose=1, mode="min")
        hist = self.model.fit(input, answer, epochs=learning_epoch, validation_data=validation, callbacks=[early_stopping])
      else:
        hist = self.model.fit(input, answer, epochs=learning_epoch, validation_data=validation)
      tf.keras.experimental.export_saved_model(self.model, model_full_path)

      return hist

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MLP.train_model:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def restore_model(self, path):
    try:
      self.model = tf.keras.experimental.load_from_saved_model(path)
      self.model.summary()

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MLP.restore_model:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



  def test_model(self, input):
    try:
      #ret = self.model.predict(input)
      #a = self.get_layer("hidden6")
      #b = a.get_weights()

      #for y in b[0]:
      #  print(len(y))

      #intermediate_layer_model = tf.keras.Model(inputs=self.model.input, outputs=self.model.get_layer("output").output)
      #intermediate_output = intermediate_layer_model.predict(input)
      #for x in intermediate_output[0]:
      #  print(x, end=" ")
      #print("")

      #return ret
      return self.model.predict(input)

    except Exception as ex:
      _, _, tb = sys.exc_info()
      print("[MLP.test_model:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
