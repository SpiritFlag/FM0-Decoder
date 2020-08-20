#signal_path = "data/C_signal/"
#signal_path = "data/C_signal_std/"
signal_path = "data/exp01_B_signal_std_cliffing/"
signal_path = "data/exp01_C_augment_random_x4/"
#signal_path = "data/D_signal_std_bit_RN0/"
#signal_path = "data/D_signal_std_bit_49.24_RN0/"
#signal_path = "data/E_augment_static_5_center/"
#signal_path = "data/E_augment_random_4/"
#signal_path = "data/E_augment_random_49.1_double/"
answer_path = "data/exp01_X_answer/"
#answer_path = "data/X_signal_answer_double/"

#signal_path = "data/J1_B_signal_std_cliffing/"
#answer_path = "data/J1_X_signal_answer/"



#model_type = "bit"
model_type = "signal"

model_postpix = "_" + model_type



#answer_type = "pre_bit_onehot"
#answer_type = "nopre_bit_onehot"
answer_type = "pre_signal_onehot"
#answer_type = "nopre_signal_onehot"
#answer_type = "pre_bit_regression"
#answer_type = "nopre_bit_regression"



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



if model_type == "bit":
  size_hidden_layer = [100, 50]
  is_batch_normalization = True

  learning_rate = 0.001
  batch_size = 64
  #batch_size = 1024
  patience = 5
  learning_epoch = 200
  loss_function = "categorical_crossentropy"



elif model_type == "signal":
  size_hidden_layer = []
  for a in [5120, 4096, 3072, 2048, 1024]:
    for b in range(1):
      size_hidden_layer.append(a)

  is_batch_normalization = True

  learning_rate = 0.0001
  batch_size = 32
  patience = 5
  learning_epoch = 1000

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



lr_low = 1e-4
lr_high = 1e-3
lr_size = 30
