from global_vars import *

signal_path = data_path_prefix + "B_signal/"
signal_path2 = data_path_prefix + "B_signal_std/"
signal_path3 = data_path_prefix + "B_signal_std_cliffing/"
answer_path = data_path_prefix + "B_answer/"

ratio_test = 0.2
ratio_validation = 0.2

n_signal_test = int(n_signal * ratio_test)
n_signal_validation = int(n_signal * (1 - ratio_test) * ratio_validation)
n_signal_train = n_signal - n_signal_test - n_signal_validation
