from global_vars import *

#signal_path = data_path_prefix + "B_signal_std_cliffing/"
signal_path = data_path_prefix + "C_augment_random_x8/"
label_path = data_path_prefix + "X_label/"

train_set_prefix = "trainAll_IQ_2/"
output_path = signal_path + train_set_prefix
label_output_path = output_path + "label/"

split_ratio = 1000

augment_ratio = 8
if augment_ratio > 1:
  augment_standard = 49.19
  augment_start = 48.1
  augment_end = 52.1
  augment_width = (augment_end - augment_start) / augment_ratio

  augment_list = []
  for x in range(augment_ratio):
    augment_list.append(augment_start + x * augment_width)

label_type_list = ["pre_bit_onehot", "pre_signal_onehot", "pre_bit_regression", "pre_signal_binary",\
                  "nopre_bit_onehot", "nopre_signal_onehot", "nopre_bit_regression", "nopre_signal_binary"]
