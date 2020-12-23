from global_vars import *

model_type = "signal"
#model_type = "bit"

if model_type == "signal":
  signal_path = data_path_prefix + "B_signal_std_cliffing/"
  answer_path = data_path_prefix + "X_answer/"

  augment_ratio = 8
  if augment_ratio > 1:
    signal_path = data_path_prefix + "C_augment_random_x" + str(augment_ratio) + "/"

    n_subset = 1
    augment_subset = False
    if n_subset > 1:
      if augment_subset is True:
        augment_ratio = int(augment_ratio * n_subset)

      signal_path = data_path_prefix + "C_augment_random_subset_" + str(n_subset)+ "_x" + str(augment_ratio) + "/"
      answer_path = data_path_prefix + "X_answer_subset_" + str(n_subset) + "/"

    augment_noise_ratio = 0
    augment_noise_level = 1
    if augment_noise_ratio > 0:
      signal_path = signal_path[:-1] + "_noise" + str(augment_noise_ratio) + "_" + str(augment_noise_level) + "/"

    augment_standard = 49.19
    augment_start = 48.1
    augment_end = 52.1
    augment_width = (augment_end - augment_start) / augment_ratio

    augment_list = []
    for x in range(augment_ratio):
      augment_list.append(augment_start + x * augment_width)

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



is_gaussian_noise = True
is_residual_network = False
dropout_rate = 0.2
is_batch_normalization = False

layer_depth = 1
learning_rate = 1e-4
batch_size = 2048
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

elif model_type == "bit":
  size_input_layer = 100
  size_hidden_layer = [100, 50]
  size_output_layer = 4

  output_activation_function = "softmax"
  loss_function = "categorical_crossentropy"
