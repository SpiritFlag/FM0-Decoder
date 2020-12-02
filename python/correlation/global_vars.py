from global_vars import *

#signal_path = data_path_prefix + "B_signal_std/"
signal_path = data_path_prefix + "B_signal_std_cliffing/"
#signal_path = data_path_prefix + "B_signalAll/"
#signal_path = data_path_prefix + "C_augment_random_x4/"
answer_path = data_path_prefix + "X_answer/"
#answer_path = data_path_prefix + "B_signalAll/"
answer_type = "nopre_bit_regression"

augment_ratio = 1
augment_list = []
if augment_ratio > 1:
  signal_path = data_path_prefix + "C_augment_random_x" + str(augment_ratio) + "/"

  n_subset = 9
  if n_subset > 1:
    augment_ratio = int(augment_ratio * n_subset)

    signal_path = data_path_prefix + "C_augment_random_subset_" + str(n_subset)+ "_x" + str(augment_ratio) + "/"
    answer_path = data_path_prefix + "X_answer_subset_" + str(n_subset) + "/"

  augment_standard = 49.19
  augment_start = 48.1
  augment_end = 52.1
  augment_width = (augment_end - augment_start) / augment_ratio

  for x in range(augment_ratio):
    augment_list.append(augment_start + x * augment_width)

n_shift = 4
constant_bit_len = 50
