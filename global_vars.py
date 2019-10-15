# -*- coding: utf-8 -*-
num_half_bit = 25  # half_bit의 sample 수
bit_preamble = 6  # preamble의 bit 수
bit_data = 128  # data의 bit 수
bit_extra = 12  # preamble, data를 제외하고 앞뒤 여백으로 포함된 sample의 bit 수

file_size = 2000
ratio_test_per_train = 0.2
ratio_validation_per_train = 0.2

test_size = int(file_size * ratio_test_per_train)
validation_size = int(file_size * (1-ratio_test_per_train) * ratio_validation_per_train)
train_size = int(file_size * (1-ratio_test_per_train) * (1-ratio_validation_per_train))

folder_path = "data_nopadding/"
