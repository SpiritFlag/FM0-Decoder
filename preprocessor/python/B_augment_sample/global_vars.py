from global_vars import *

augment_ratio = 4

signal_path = data_path_prefix + "B_signal_std_cliffing/"
output_path = data_path_prefix + "C_augment_random_x" + str(augment_ratio) + "/"

n_subset = 27
if n_subset > 1:
  augment_ratio = int(augment_ratio * n_subset)

  signal_path = data_path_prefix + "B_signal_std_cliffing_subset_" + str(n_subset) + "/"
  output_path = data_path_prefix + "C_augment_random_subset_" + str(n_subset)+ "_x" + str(augment_ratio) + "/"

augment_standard = 49.19
augment_start = 48.1
augment_end = 52.1
augment_width = (augment_end - augment_start) / augment_ratio

augment_list = []
for x in range(augment_ratio):
  augment_list.append(augment_start + x * augment_width)

append_t1 = False

augment_mode = 3
augment_avg_window = 2
