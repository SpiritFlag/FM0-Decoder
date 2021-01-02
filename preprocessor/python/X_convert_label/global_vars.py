from global_vars import *

label_path = data_path_prefix + "B_label/"
output_path = data_path_prefix + "X_label/"

label_type_list = ["pre_bit_onehot", "nopre_bit_onehot", "pre_signal_onehot", "nopre_signal_onehot",\
  "pre_bit_regression", "nopre_bit_regression"]
ispreamble_list = [True, False, True, False, True, False]
encoding_unit_list = ["bit", "bit", "signal", "signal", "bit", "bit"]
encoding_type_list = ["onehot", "onehot", "onehot", "onehot", "regression", "regression"]
