from global_vars import *

answer_path = data_path_prefix + "B_answer/"
#answer_path = data_path_prefix + "B_signalAll/"
#output_path = data_path_prefix + "B_signalAll/"
output_path = data_path_prefix + "X_answer/"

n_subset = 27
if n_subset > 1:
  answer_path = data_path_prefix + "B_answer_subset_" + str(n_subset) + "/"
  output_path = data_path_prefix + "X_answer_subset_" + str(n_subset) + "/"

answer_type_list = ["pre_bit_onehot", "nopre_bit_onehot", "pre_signal_onehot", "nopre_signal_onehot",\
  "pre_bit_regression", "nopre_bit_regression"]
ispreamble_list = [True, False, True, False, True, False]
encoding_unit_list = ["bit", "bit", "signal", "signal", "bit", "bit"]
encoding_type_list = ["onehot", "onehot", "onehot", "onehot", "regression", "regression"]
