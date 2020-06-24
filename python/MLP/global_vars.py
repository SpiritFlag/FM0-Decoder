#signal_path = "data/C_signal/"
#signal_path = "data/C_signal_std/"
#signal_path = "data/C_signal_std_cliffing/"
#signal_path = "data/D_signal_std_bit_RN0/"
signal_path = "data/D_signal_std_bit_16_RN0/"


model_type = "bit"
#model_type = "signal"

model_postpix = "_" + model_type



if model_type == "bit":
  size_hidden_layer = [100, 50]
  is_batch_normalization = True

  learning_rate = 0.001
  batch_size = 64
  patience = 5
  learning_epoch = 200
  loss_function = "categorical_crossentropy"



elif model_type == "signal":
  amp_rep = 1
  #amp_rep = 25

  #size_hidden_layer = [5000, 4000, 3000, 2000, 1000, 268, 1000, 2000, 3000, 4000, 5000]
  size_hidden_layer = [5000, 5000, 4000, 4000, 3000, 3000, 2000, 2000, 1000, 1000]
  is_batch_normalization = True

  learning_rate = 0.001
  batch_size = 64
  patience = 5
  learning_epoch = 200
  loss_function = "mse"

  test_type = 1
