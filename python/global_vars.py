file_name_list_all = []
for a in ["100", "200", "300", "400"]:
#for a in ["100"]:
#for a in ["100", "200"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

#file_name_list = ["100_0_0"]
#file_name_list = ["100_0_0", "100_0_45", "100_0_90", "100_0_135"]
file_name_list = file_name_list_all
#RN_index = 0

#file_name_list = ["045", "046", "047", "107", "108", "109", "143"]
#file_name_list = ["050", "060", "070", "080", "090", "100", "110", "120", "130", "140", "150", "160", "170", "190", "200"]



#cuda_device_id = "-1"
cuda_device_id = "0"
#cuda_device_id = "1"



# for augement training only
#augment_training = False
augment_training = True
#augment_list = [48, 49, 50, 51, 52]
augment_list = [48.1, 49.1, 50.1, 51.1]
#augment_list = [48.1, 49.1]
#augment_list = [49.1]

# for search hyperparameter only
serach_hyperparameter = False
#serach_hyperparameter = True
#read_ratio = 0.1
read_ratio = 1



import datetime
execute_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
model_path = "model/"
model_full_path = model_path + execute_time
log_path = "log/"
log_full_path = log_path + execute_time



n_sample = 7300
n_cw = 50
n_bit = 50
n_half_bit = int(n_bit / 2)
n_bit_preamble = 6
n_bit_data = 128
n_extra = int(n_sample - n_bit * (n_bit_preamble + n_bit_data))
