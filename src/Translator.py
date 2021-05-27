##
# @file Translator.py
#
# @brief Defines the Translator class.


import configparser
import numpy as np
from tqdm import tqdm


class Translator():
    '''! Defines the functions and variables commonly used in Train, Test, and
    RuleBased classes.
    '''
    def __init__(self):
        '''! The Translator class initializer.
        '''
        ## @var config
        # The configuration data read from the config file.
        self.config = configparser.ConfigParser()
        self.config.optionxform = lambda option: option
        self.config.read("src/conf/confTranslator.ini")

        assert len(self.config.sections()), "Fail to load config file.\n"


    def read_signal(self, type="absolute", signalPath="", fileNameList=[],\
        postfix="_test", augmentList=[], n_signal="", n_sample=""):
        '''! Reads the signal from signal file(s).

        @param type The type of the signal to read. Default value is used when
        the function is called from the RuleBased class.
        - "absolute" : The signal consists of a absolute value.
        - "complex" : The signal consists of a complex number.

        @param signalPath The path where the signal file is located.

        @param fileNameList The list of the file names to read.

        @param postfix The subset to read. Default value is used when the
        function is called from the RuleBased class.

        @param augmentList The list of the augment tags to read.

        @param n_signal The number of signals in one file.

        @param n_sample The number of samples in one signal.

        @return A list of signals read.
        '''
        signalPath = self.config["PATH"]["SignalPath"]

        for fileName in self.config["FILE_NAME"]:
            fileNameList.append(self.config["FILE_NAME"][fileName])

        for augment in self.config["AUGMENTATION"]:
            augmentList.append(self.config["AUGMENTATION"][augment])

        if postfix == "_train":
            n_signal = int(self.config["SET"]["nTrain"])
        elif postfix == "_validation":
            n_signal = int(self.config["SET"]["nValidation"])
        elif postfix == "_test":
            n_signal = int(self.config["SET"]["nTest"])
        else:
            assert False, "Invalid postfix " + postfix + "\n"

        n_sample = int(self.config["SAMPLE"]["nSample"])

        '''
        PRINT PARAM
        '''
        print("\n** PARAM read_signal **")
        print(f"type=\t\t{type}")
        print(f"signalPath=\t{signalPath}")
        print(f"fileNameList=\t{fileNameList}")
        print(f"postfix=\t{postfix}")
        print(f"augmentList=\t{augmentList}")
        print(f"n_signal=\t{n_signal}")
        print(f"n_sample=\t{n_sample}")
        print("")

        '''
        FUNCTION BODY
        '''
        if type == "absolute":
            signalList = np.zeros((int(len(fileNameList) * len(augmentList) * n_signal), n_sample))
        elif type == "complex":
            pass
        else:
            assert False, "Invalid type " + type + "\n"

        pbar = tqdm(total=int(len(fileNameList) * len(augmentList)),\
            desc="READING", ncols=100, unit=" file")
        x = 0

        for fileName in fileNameList:
            for augment in augmentList:
                if type == "absolute":
                    signal = np.load(signalPath + fileName + "_signal" + augment + postfix + ".npy")
                    signalList[int(x*n_signal):int((x+1)*n_signal)] = signal
                elif type == "complex":
                    pass
                pbar.update(1)
                x += 1

        pbar.close()
        return signalList


    def read_label(self, labelPath="", fileNameList=[],\
        labelType="nopre_signal_binary", postfix="_test", augmentRatio=""):
        '''! Reads the label from label file(s).

        @param labelPath The path where the label file is located.

        @param fileNameList The list of the file names to read.

        @param labelType The type of the label to read. Default value is used
        when the function is called from the RuleBased class.

        @param postfix The subset to read. Default value is used when the
        function is called from the RuleBased class.

        @param augmentRatio The number of times to read repeatedly.

        @return A list of labels read.
        '''
        labelPath = self.config["PATH"]["LabelPath"]

        for fileName in self.config["FILE_NAME"]:
            fileNameList.append(self.config["FILE_NAME"][fileName])

        augmentRatio = len(self.config["AUGMENTATION"])

        '''
        PRINT PARAM
        '''
        print("\n** PARAM read_label **")
        print(f"labelPath=\t{labelPath}")
        print(f"fileNameList=\t{fileNameList}")
        print(f"labelType=\t{labelType}")
        print(f"postfix=\t{postfix}")
        print(f"augmentRatio=\t{augmentRatio}")
        print("")

        '''
        FUNCTION BODY
        '''
        labelList = []
        pbar = tqdm(total=int(len(fileNameList) * augmentRatio),\
            desc="READING", ncols=100, unit=" file")

        for fileName in fileNameList:
            for i in range(augmentRatio):
                label = np.load(labelPath + fileName + "_label_" + labelType\
                    + postfix + ".npy")
                labelList.extend(label)
                pbar.update(1)

        pbar.close()

        return labelList
