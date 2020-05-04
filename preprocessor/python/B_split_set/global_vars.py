databit_path = "../data/A_databit/"
index_path = "../data/B_RNindex/"

#RNwhole = True    # load all RNset
RNwhole = False   # Load one RNset
n_RNset = 0

type_postfix = ""
#type_postfix = "_std"
#type_postfix = "_std_cliffing"

if RNwhole is False:
  RN_postfix = "_RN" + str(n_RNset)
else:
  RN_postfix = ""

signal_path = "../data/B_signal" + type_postfix + "/"
output_path = "../data/C_signal" + type_postfix + RN_postfix + "/"
