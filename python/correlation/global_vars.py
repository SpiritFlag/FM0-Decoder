import numpy as np

from global_vars import *

signal_path = data_path_prefix + "B_signal/"
#signal_path = data_path_prefix + "B_signal_std_cliffing/"
label_path = data_path_prefix + "B_label/"
label_type = "org"

augment_ratio = 1
augment_list = []
if augment_ratio > 1:
  signal_path = data_path_prefix + "C_signal_augX" + str(augment_ratio) + "/"

  augment_standard = 49.19
  augment_start = 48.1
  augment_end = 52.1
  augment_width = (augment_end - augment_start) / augment_ratio

  augment_list = np.arange(augment_ratio)
  # augment_list = []
  # for x in range(augment_ratio):
  #   augment_list.append(augment_start + x * augment_width)

n_shift = 0
constant_bit_len = 48.89976

cliffing = False
# cliffing = True

# full_candidate = False
full_candidate = True

use_extra_half_bit = True
# use_extra_half_bit = False
