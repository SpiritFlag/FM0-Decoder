from global_vars import *

#model_type = "signal"
model_type = "CNN"
#model_type = "bit"

pre_shuffled = True
#pre_shuffled = False

if pre_shuffled is True:
  train_set_prefix = "trainAll_IQ_2/"
  n_file = 738
  split_ratio = 1000

if model_type == "signal" or model_type == "CNN":
  signal_path = data_path_prefix + "B_signal_std_cliffing/"
  label_path = data_path_prefix + "X_label/"

  augment_ratio = 8
  if augment_ratio > 1:
    signal_path = data_path_prefix + "C_augment_random_x" + str(augment_ratio) + "/"

    augment_standard = 49.19
    augment_start = 48.1
    augment_end = 52.1
    augment_width = (augment_end - augment_start) / augment_ratio

    augment_list = []
    for x in range(augment_ratio):
      augment_list.append(augment_start + x * augment_width)

  #label_type = "pre_bit_onehot"
  #label_type = "pre_signal_onehot"
  #label_type = "pre_signal_binary"
  #label_type = "pre_bit_regression"
  #label_type = "nopre_bit_onehot"
  #label_type = "nopre_signal_onehot"
  label_type = "nopre_signal_binary"
  #label_type = "nopre_bit_regression"

elif model_type == "bit":
  #signal_path = data_path_prefix + "C_bit_49.25/"
  signal_path = data_path_prefix + "C_bit_49.25_nocliffing/"
  label_type = "nopre_bit_regression"

  label_path = data_path_prefix + "X_label/"



if label_type == "pre_bit_onehot" or label_type == "pre_signal_onehot"\
  or label_type == "pre_signal_binary" or label_type == "pre_bit_regression":
  ispreamble = True
if label_type == "nopre_bit_onehot" or label_type == "nopre_signal_onehot"\
  or label_type == "nopre_signal_binary" or label_type == "nopre_bit_regression":
  ispreamble = False

if label_type == "pre_bit_onehot" or label_type == "nopre_bit_onehot"\
  or label_type == "pre_bit_regression" or label_type == "nopre_bit_regression":
  encoding_unit = "bit"
  size_slice = 2
if label_type == "pre_signal_onehot" or label_type == "nopre_signal_onehot":
  encoding_unit = "signal"
  size_slice = 4
if label_type == "pre_signal_binary" or label_type == "nopre_signal_binary":
  encoding_unit = "signal"
  size_slice = 1

if label_type == "nopre_bit_onehot" or label_type == "pre_bit_onehot"\
  or label_type == "nopre_signal_onehot" or label_type == "pre_signal_onehot":
  encoding_type = "onehot"
if label_type == "pre_bit_regression" or label_type == "nopre_bit_regression":
  encoding_type = "regression"
if label_type == "pre_signal_binary" or label_type == "nopre_signal_binary":
  encoding_type = "binary"



is_gaussian_noise = True
is_residual_network = False
dropout_rate = 0.2
is_batch_normalization = True

layer_depth = 3
learning_rate = 1e-4
batch_size = 64
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

    #output_activation_function = "my_softmax"
    output_activation_function = "my_softmax_2"
    loss_function = "categorical_crossentropy"

  elif encoding_type == "regression":
    if ispreamble is True:
      size_output_layer = 268
    else:
      size_output_layer = 256

    output_activation_function = "relu"
    loss_function = "mse"

elif model_type == "CNN":
  size_input_layer = 7300
  size_input_filter = 2

  size_filter = [32, 64, 128, 256, 512, 1024]
  size_conv_layer = 3
  size_pool_layer = 2
  size_dense_layer = [4096, 2048, 1024]

  if encoding_type == "onehot":
    if ispreamble is True:
      size_output_layer = 536
    else:
      size_output_layer = 512
    loss_function = "categorical_crossentropy"
  elif encoding_type == "regression":
    if ispreamble is True:
      size_output_layer = 268
    else:
      size_output_layer = 256
  elif encoding_type == "binary":
    if ispreamble is True:
      size_output_layer = 134
    else:
      size_output_layer = 128
    loss_function = "binary_crossentropy"

elif model_type == "bit":
  size_input_layer = 100
  size_hidden_layer = [100, 50]
  size_output_layer = 4

  output_activation_function = "softmax"
  loss_function = "categorical_crossentropy"
