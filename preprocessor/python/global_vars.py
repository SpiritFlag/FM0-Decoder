file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

file_name_list = []
#file_name_list = ["100_0_0"]
file_name_list = file_name_list_all



signal_path = "../data/A_IQsignal/"
output_path = "../data/B_CW_kalman/"



n_signal = 3000
n_sample = 6850
n_cw = 50
