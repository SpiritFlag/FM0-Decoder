file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

#file_name_list = ["100_0_0"]
#file_name_list = ["100_0_0", "100_0_45", "100_0_90", "100_0_135"]
#file_name_list = ["100_0_90"]
file_name_list = file_name_list_all
RN_index = 0



import datetime
execute_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
model_path = "model/"
model_full_path = model_path + execute_time
log_path = "log/"
log_full_path = log_path + execute_time



n_sample = 6850
n_cw = 50
n_bit = 50
n_half_bit = int(n_bit / 2)
n_bit_preamble = 6
n_bit_data = 128
n_extra = int(n_sample - n_bit * (n_bit_preamble + n_bit_data))



'''
#signal_path = "data/C_signal_std/"
signal_path = "data/C_signal_std_full/"
#signal_path = "data/D_bit_unit_std_full/"
#signal_path = "data/XB_signal/"
#signal_path = "data/D_bit_unit_std_4924/"
#signal_path = "data/D_bit_unit_std_th0/"
#signal_path = "data/D_bit_unit_std_success/"
#test_path = "data/C_signal_std_full/"
#test_path = signal_path
#test_path = "data/D_bit_unit_std/"

#model_type = "bit_unit"     # select this model when using correlation
#test_type = "corr"
#test_type = "shift"
bit_unit = 1
model_postpix = "_" + str(bit_unit)
model_type = "whole"
databit_repitition = 1
model_postpix = "_rep_" + str(databit_repitition)





learning_rate = 0.001

loss_function = "mse"
learning_epoch = 100
isEarlyStop = True

#loss_function = "categorical_crossentropy"
#learning_epoch = 5
#isEarlyStop = False



'''
