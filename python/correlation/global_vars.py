from global_vars import *

#signal_path = data_path_prefix + "B_signal_std/"
#signal_path = data_path_prefix + "B_signal_std_cliffing/"
#signal_path = data_path_prefix + "B_signalAll/"
signal_path = data_path_prefix + "C_augment_random_x4/"
answer_path = data_path_prefix + "X_answer/"
#answer_path = data_path_prefix + "B_signalAll/"
answer_type = "nopre_bit_regression"

augment_list = []
augment_list = [48.1, 49.1, 50.1, 51.1]
#augment_list = [48.1, 48.6, 49.1, 49.6, 50.1, 50.6, 51.1, 51.6]

n_shift = 0
constant_bit_len = 49.19
