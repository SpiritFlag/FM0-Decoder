#type_postfix = ""
type_postfix = "_std"
#type_postfix = "_std_cliffing"

n_shift = 3
n_RNset = 0
n_extract_bit = 128

signal_path = "../data/C_signal" + type_postfix + "_RN" + str(n_RNset) + "/"
if n_extract_bit == 128:
  output_path = "../data/D_signal" + type_postfix + "_bit_RN" + str(n_RNset) + "/"
else:
  output_path = "../data/D_signal" + type_postfix + "_bit_" + str(n_extract_bit) + "_RN" + str(n_RNset) + "/"
