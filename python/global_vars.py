# select model
tail = "_LH"
#tail = "_01"



# data
num_half_bit = 25
bit_preamble = 6
bit_data = 128
bit_extra = 12

data_path = "data/190917_nopadding/"

file_name_list = []
'''
for a in ["50", "100", "150", "200", "250", "300", "350", "400"]:
  for b in ["l", "r"]:
    for c in ["20", "60", "100"]:
      file_name_list.append(a + "_" + b + c)
'''
file_name_list.append("50_l20")
file_name_list.append("50_r20")



# time & folder_path
import datetime
execute_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
model_path = "model/"
model_full_path = model_path + execute_time
log_path = "log/" + execute_time



# define set
file_size = 2000
ratio_test_per_train = 0.2
ratio_validation_per_train = 0.2

test_size = int(file_size * ratio_test_per_train)
validation_size = int(file_size * (1-ratio_test_per_train) * ratio_validation_per_train)
train_size = int(file_size * (1-ratio_test_per_train) * (1-ratio_validation_per_train))



# Autoencoder
model_tail = ""
