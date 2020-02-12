file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name_list = ["100_0_0"]
file_name_list = file_name_list_all



databit_path = "../data/A_databit/"
#signal_path = "../data/A_IQsignal/"
#signal_path = "../data/B_CW_kalman/"
#signal_path = "../data/B_CW_kalman_std/"
#signal_path = "../data/B_CW_kalman_std_cliffing/"
#signal_path = "../data/C_bit_with_correlation/"
signal_path = "../data/C_bit_with_correlation_cliffing/"
#output_path = "../data/tmp/"
#output_path = "../data/B_CW_kalman_std/"
output_path = "../data/C_bit_with_correlation/"
#output_path = "../data/C_bit_with_correlation_cliffing/"
output_path2 = ""
#output_path2 = "../data/B_CW_kalman_std_cliffing/"



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
