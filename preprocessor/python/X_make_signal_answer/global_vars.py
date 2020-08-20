databit_path = "../data/A_databit/"
RNindex_path = "../data/B_RNindex/"
#output_path = "../data/X_signal_answer/"
output_path = "../data/X_signal_answer_double/"

#exp_num = 3
#databit_path = "../data/J" + str(exp_num) + "_A_databit/"
#RNindex_path = "none"
#output_path = "../data/J" + str(exp_num) + "_X_signal_answer/"



#answer_type = "_pre_bit_onehot"
#answer_type = "_nopre_bit_onehot"
answer_type = "_pre_signal_onehot"
#answer_type = "_nopre_signal_onehot"
#answer_type = "_pre_bit_regression"
#answer_type = "_nopre_bit_regression"



if answer_type == "_pre_bit_onehot" or answer_type == "_pre_signal_onehot" or answer_type == "_pre_bit_regression":
  ispreamble = True
if answer_type == "_nopre_bit_onehot" or answer_type == "_nopre_signal_onehot" or answer_type == "_nopre_bit_regression":
  ispreamble = False

if answer_type == "_pre_bit_onehot" or answer_type == "_nopre_bit_onehot"\
  or answer_type == "_pre_bit_regression" or answer_type == "_nopre_bit_regression":
  encoding_unit = "bit"
if answer_type == "_pre_signal_onehot" or answer_type == "_nopre_signal_onehot":
  encoding_unit = "signal"

if answer_type == "_nopre_bit_onehot" or answer_type == "_pre_bit_onehot"\
  or answer_type == "_nopre_signal_onehot" or answer_type == "_pre_signal_onehot":
  encoding_type = "onehot"
if answer_type == "_pre_bit_regression" or answer_type == "_nopre_bit_regression":
  encoding_type = "regression"
