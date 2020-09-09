from global_vars import *

model_type = "signal"
#model_type = "bit"

if model_type == "signal":
  signal_path = data_path_prefix + "B_signal_std_cliffing/"
  signal_path = data_path_prefix + "C_augment_random_x4/"
  #signal_path = data_path_prefix + "C_augment_random_x8/"

  augment_list = []
  augment_list = [48.1, 49.1, 50.1, 51.1]
  #augment_list = [48.1, 48.6, 49.1, 49.6, 50.1, 50.6, 51.1, 51.6]

  #answer_type = "pre_bit_onehot"
  answer_type = "pre_signal_onehot"
  #answer_type = "pre_bit_regression"
  #answer_type = "nopre_bit_onehot"
  #answer_type = "nopre_signal_onehot"
  #answer_type = "nopre_bit_regression"

elif model_type == "bit":
  #signal_path = data_path_prefix + "C_bit_49.25/"
  signal_path = data_path_prefix + "C_bit_49.25_nocliffing/"
  answer_type = "nopre_bit_regression"

answer_path = data_path_prefix + "X_answer/"

train_learning_rate = False
#train_learning_rate = True



if answer_type == "pre_bit_onehot" or answer_type == "pre_signal_onehot" or answer_type == "pre_bit_regression":
  ispreamble = True
if answer_type == "nopre_bit_onehot" or answer_type == "nopre_signal_onehot" or answer_type == "nopre_bit_regression":
  ispreamble = False

if answer_type == "pre_bit_onehot" or answer_type == "nopre_bit_onehot"\
  or answer_type == "pre_bit_regression" or answer_type == "nopre_bit_regression":
  encoding_unit = "bit"
  size_slice = 2
if answer_type == "pre_signal_onehot" or answer_type == "nopre_signal_onehot":
  encoding_unit = "signal"
  size_slice = 4

if answer_type == "nopre_bit_onehot" or answer_type == "pre_bit_onehot"\
  or answer_type == "nopre_signal_onehot" or answer_type == "pre_signal_onehot":
  encoding_type = "onehot"
if answer_type == "pre_bit_regression" or answer_type == "nopre_bit_regression":
  encoding_type = "regression"



dropout_rate = 0.2
is_batch_normalization = False

layer_depth = 3
learning_rate = 1e-5
batch_size = 4096
patience = 5
learning_epoch = 1000

if model_type == "signal":
  size_input_layer = 7300

  size_hidden_layer = []
  for a in [6144, 5120, 4096, 3072, 2048, 1024]:
    for b in range(layer_depth):
      size_hidden_layer.append(a)

  if encoding_type == "onehot":
    if ispreamble is True:
      size_output_layer = 536
    else:
      size_output_layer = 512

    output_activation_function = "my_softmax"
    loss_function = "categorical_crossentropy"

  elif encoding_type == "regression":
    if ispreamble is True:
      size_output_layer = 268
    else:
      size_output_layer = 256

    output_activation_function = "relu"
    loss_function = "mse"

elif model_type == "bit":
  size_input_layer = 100
  size_hidden_layer = [100, 50]
  size_output_layer = 4

  output_activation_function = "softmax"
  loss_function = "categorical_crossentropy"
