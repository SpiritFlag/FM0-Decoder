import configparser
from conf import *
from confFilename import *


config = configparser.ConfigParser()
config.optionxform = lambda option: option


'''
SECTION PATH
'''
config["PATH"] = {}

if exp_num < 10:
    data_path_prefix = data_path + "exp0" + str(exp_num) + "_"
else:
    data_path_prefix = data_path + "exp" + str(exp_num) + "_"

if augment_ratio > 1:
    signal_path = signal_augment_path + str(augment_ratio) + "/"

config["PATH"]["SignalPath"] = data_path_prefix + signal_path
config["PATH"]["LabelPath"] = data_path_prefix + label_path


'''
SECTION FILE_NAME
'''
config["FILE_NAME"] = {}

for i in range(len(file_name_list)):
    config["FILE_NAME"]["File_"+str(i+1)] = file_name_list[i]


'''
SECTION AUGMENTATION
'''
config["AUGMENTATION"] = {}

if augment_ratio == 1:
    config["AUGMENTATION"]["Augment_1"] = ""
else:
    augment_width = (augment_end - augment_start) / augment_ratio
    for i in range(augment_ratio):
        config["AUGMENTATION"]["Augment_"+str(i+1)]\
            = "_" + str(augment_start + i * augment_width)


'''
SECTION SET
'''
config["SET"] = {}

n_signal_test = int(n_signal * ratio_test)
n_signal_validation = int(n_signal * (1 - ratio_test) * ratio_validation)

config["SET"]["nSignal"] = str(n_signal)
config["SET"]["nTest"] = str(n_signal_test)
config["SET"]["nValidation"] = str(n_signal_validation)
config["SET"]["nTrain"] = str(n_signal - n_signal_test - n_signal_validation)


'''
SECTION SAMPLE
'''
config["SAMPLE"] = {}

n_extra = int(n_sample - n_bit * (n_bit_preamble + n_bit_data))

config["SAMPLE"]["nSample"] = str(n_sample)
config["SAMPLE"]["nCW"] = str(n_cw)
config["SAMPLE"]["nBit"] = str(n_bit)
config["SAMPLE"]["nHalfBit"] = str(int(n_bit / 2))
config["SAMPLE"]["nBitPreamble"] = str(n_bit_preamble)
config["SAMPLE"]["nBitData"] = str(n_bit_data)
config["SAMPLE"]["nExtra"] = str(n_extra)


'''
WRITE CONFIG
'''
with open("src/conf/confTranslator.ini", "w") as configfile:
    config.write(configfile)
