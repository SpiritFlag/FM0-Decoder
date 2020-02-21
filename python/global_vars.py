file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name_list = ["100_0_0"]
file_name_list = file_name_list_all
RN_index = 0
databit_repition = 1



import datetime
execute_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
model_path = "model/"
model_full_path = model_path + execute_time
log_path = "log/"
log_full_path = log_path + execute_time



databit_path = "data/C_RN_databit/"
#databit_path = "data/C_RN_whole_databit/"
#databit_path = "data/C_RN_preamble_std_DF/"
#databit_path = "data/C_RN_corr_std_DF/"
#signal_path = "data/C_RN_std/"
#signal_path = "data/C_RN_std_cliffing/"
signal_path = "data/C_RN_2_bit_with_correlation_std/"
#signal_path = "data/C_RN_2_bit_with_correlation_std_cliffing/"
#signal_path = "data/C_RN_2_bit_40_std/"
#signal_path = "data/C_RN_2_bit_40_std_cliffing/"
#signal_path = "data/C_RN_preamble_std_F/"
#signal_path = "data/C_RN_corr_std_F/"
#signal_path = "data/C_RN_whole_std/"
#signal_path = "data/C_RN_whole_std_cliffing/"
#model_type = "one_bit"
model_type = "two_bit"
#model_type = "whole"
model_postpix = "_onehot"
#model_postpix = "_lowhigh"
#model_postpix = "_extendlowhigh"
#model_postpix = "_rep"



n_sample = 6850
n_cw = 50
n_bit = 50
n_half_bit = int(n_bit / 2)
n_bit_preamble = 6
n_bit_data = 128
n_extra = int(n_sample - n_bit * (n_bit_preamble + n_bit_data))



learning_rate = 0.001
learning_epoch = 100
isEarlyStop = True
