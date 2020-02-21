file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name_list = ["100_0_0"]
file_name_list = file_name_list_all



index_path = "../data/C_RNindex/"
#databit_path = "../data/A_databit/"
#databit_path = "../data/B_databit_enc256/"
databit_path = "../data/C_RN_databit/"
#signal_path = "../data/A_IQsignal/"
#signal_path = "../data/B_CW_kalman/"
#signal_path = "../data/B_CW_kalman_std/"
#signal_path = "../data/B_CW_kalman_std_cliffing/"
signal_path = "../data/C_RN_std/"
#signal_path = "../data/C_RN_std_cliffing/"
#signal_path = "../data/C_RN_2_bit_with_correlation_std/"
#signal_path = "../data/C_RN_2_bit_with_correlation_std_cliffing/"
#output_path = "../data/C_RN_preamble_std_S/"
#output_path = "../data/tmp/"
#output_path = "../data/B_CW_kalman_std/"
#output_path = "../data/B_databit_enc256/"
#output_path = "../data/C_RNindex/"
#output_path = "../data/C_RN_databit/"
#output_path = "../data/C_RN_std/"
#output_path = "../data/C_RN_std_cliffing/"
#output_path = "../data/C_RN_2_bit_with_correlation_std/"
#output_path = "../data/C_RN_2_bit_with_correlation_std_cliffing/"
#output_path = "../data/C_RN_2_bit_40_std/"
#output_path = "../data/C_RN_2_bit_40_std_cliffing/"
#output_path = "../data/C_RN_whole_std/"
#output_path = "../data/C_RN_whole_std_cliffing/"
#output_path = "../data/C_RN_whole_databit/"
output_path = "../data/C_RN_corr_std_"
#output_path = "../data/C_RN_preamble_std_cliffing_S/"
output_path2 = ""
#output_path2 = "../data/B_CW_kalman_std_cliffing/"
#output_path2 = "../data/C_RN_preamble_std_cliffing_F/"



n_signal = 3000
#n_signal = 5
n_sample = 6850
n_cw = 50
n_bit = 50
n_half_bit = int(n_bit / 2)
n_tolerance_bit = 2
n_bit_preamble = 6
n_bit_data = 128
n_extra = int(n_sample - n_bit * (n_bit_preamble + n_bit_data))



n_RNtrain = 40
n_RNvalidation = 10
n_RNtest = 100
n_RNset = n_RNtrain + n_RNvalidation + n_RNtest
#n_RNsignal = int(n_signal/n_RNset)
n_RNsignal = 1



extra_half_bit = True
correlation_threshold = 40
databit_repition = 1
