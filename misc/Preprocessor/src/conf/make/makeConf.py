import configparser
from conf import *
from confFilename import *
from confSDR import *
from confSS import *
from confSA import *
from confLC import *
from confSP import *


'''
COMMON VALUE
'''
if exp_num < 10:
    data_path_prefix = data_path + "exp0" + str(exp_num) + "_"
else:
    data_path_prefix = data_path + "exp" + str(exp_num) + "_"

conf_path = "src/conf/"


'''
confPreprocessor.ini
'''
config = configparser.ConfigParser()
config.optionxform = lambda option: option


'''
SECTION FILE_NAME
'''
config["FILE_NAME"] = {}

for i in range(len(file_name_list)):
    config["FILE_NAME"]["File_" + str(i + 1)] = file_name_list[i]


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
SECTION ETC
'''
config["ETC"] = {}
config["ETC"]["augRatio"] = str(aug_ratio)


'''
WRITE CONFIG
'''
with open(conf_path + "confPreprocessor.ini", "w") as configfile:
    config.write(configfile)


'''
confSDR.ini
'''
configSDR = configparser.ConfigParser()
configSDR.optionxform = lambda option: option


'''
SECTION PATH
'''
configSDR["PATH"] = {}

configSDR["PATH"]["signalPath"] = data_path_prefix + SDR_signal_path


'''
WRITE CONFIG
'''
with open(conf_path + "confSDR.ini", "w") as configfile:
    configSDR.write(configfile)


'''
confSS.ini
'''
configSS = configparser.ConfigParser()
configSS.optionxform = lambda option: option


'''
SECTION PATH
'''
configSS["PATH"] = {}

configSS["PATH"]["signalPath"] = data_path_prefix + SS_signal_path
configSS["PATH"]["outputPath"] = data_path_prefix + SS_output_path


'''
WRITE CONFIG
'''
with open(conf_path + "confSS.ini", "w") as configfile:
    configSS.write(configfile)


'''
confSA.ini
'''
configSA = configparser.ConfigParser()
configSA.optionxform = lambda option: option


'''
SECTION PATH
'''
configSA["PATH"] = {}

configSA["PATH"]["signalPath"] = data_path_prefix + SA_signal_path
configSA["PATH"]["outputPath"] =\
    data_path_prefix + SA_output_path + str(aug_ratio) + "/"


'''
SECTION AUGMENTATION
'''
configSA["AUGMENTATION"] = {}

if aug_ratio > 1:
    aug_width = (aug_ed - aug_st) / aug_ratio
    configSA["AUGMENTATION"]["augRef"] = str(aug_ref)
    configSA["AUGMENTATION"]["augWidth"] = str(aug_width)


'''
SECTION AUG_LIST
'''
configSA["AUG_LIST"] = {}

if aug_ratio > 1:
    for i in range(aug_ratio):
        aug = aug_st + i * aug_width
        configSA["AUG_LIST"]["aug_" + str(i + 1)] = str(aug)


'''
WRITE CONFIG
'''
with open(conf_path + "confSA.ini", "w") as configfile:
    configSA.write(configfile)


'''
confLC.ini
'''
configLC = configparser.ConfigParser()
configLC.optionxform = lambda option: option


'''
SECTION PATH
'''
configLC["PATH"] = {}

configLC["PATH"]["labelPath"] = data_path_prefix + LC_label_path
configLC["PATH"]["outputPath"] = data_path_prefix + LC_output_path


'''
WRITE CONFIG
'''
with open(conf_path + "confLC.ini", "w") as configfile:
    configLC.write(configfile)


'''
confSP.ini
'''
configSP = configparser.ConfigParser()
configSP.optionxform = lambda option: option


'''
SECTION PATH
'''
configSP["PATH"] = {}

configSP["PATH"]["signalPath"] = data_path_prefix + SP_signal_path
configSP["PATH"]["labelPath"] = data_path_prefix + SP_label_path
configSP["PATH"]["indexPath"] = data_path_prefix + SP_index_path


'''
SECTION PATH
'''
configSP["MODE"] = {}

configSP["MODE"]["onlyTest"] = str(SP_only_test)


'''
WRITE CONFIG
'''
with open(conf_path + "confSP.ini", "w") as configfile:
    configSP.write(configfile)
