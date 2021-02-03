##
# @file Preprocessor.py
#
# @brief Defines the Preprocessor class.


import configparser
import numpy as np
from tqdm import tqdm


class Preprocessor():
    '''! Defines the functions and variables commonly used.
    '''
    def __init__(self):
        '''! The Preprocessor class initializer.
        '''
        ## @var configPath
        # The config file path.
        self.configPath = "src/conf/"

        ## @var config
        # The configuration data read from the config file.
        self.config = configparser.ConfigParser()
        self.config.optionxform = lambda option: option
        self.config.read(self.configPath + "confPreprocessor.ini")

        assert len(self.config.sections()), "Fail to load config file.\n"

        ## @var fileNameList
        # The list of file name(s) of dataset.
        self.fileNameList = []
        for fileName in self.config["FILE_NAME"]:
            self.fileNameList.append(self.config["FILE_NAME"][fileName])

        ## @var nSignal
        # The number of signal(s) in single file.
        self.nSignal = int(self.config["SET"]["nSignal"])
        ## @var nTrain
        # The number of signal(s) in tarin set for single file.
        self.nTrain = int(self.config["SET"]["nTrain"])
        ## @var nValidation
        # The number of signal(s) in validation set for single file.
        self.nValidation = int(self.config["SET"]["nValidation"])
        ## @var nTest
        # The number of signal(s) in test set for single file.
        self.nTest = int(self.config["SET"]["nTest"])

        ## @var nSample
        # The number of total sample(s) in single signal.
        self.nSample = int(self.config["SAMPLE"]["nSample"])
        ## @var nCW
        # The number of sample(s) of continuous wave.
        self.nCW = int(self.config["SAMPLE"]["nCW"])
        ## @var nBit
        # The number of sample(s) representing single bit.
        self.nBit = int(self.config["SAMPLE"]["nBit"])
        ## @var nHalfBit
        # The number of sample(s) representing half bit.
        self.nHalfBit = int(self.config["SAMPLE"]["nHalfBit"])
        ## @var nBitPreamble
        # The number of bit(s) in preamble.
        self.nBitPreamble = int(self.config["SAMPLE"]["nBitPreamble"])
        ## @var nBitData
        # The number of bit(s) in data.
        self.nBitData = int(self.config["SAMPLE"]["nBitData"])
        ## @var nExtra
        # The number of sample(s) not corresponding to the priamble and data.
        self.nExtra = int(self.config["SAMPLE"]["nExtra"])

        ## @var augRatio
        # The ratio of augmentation.
        self.augRatio = int(self.config["ETC"]["augRatio"])

        self.printConfig()

    def printConfig(self):
        '''! Prints the configuration data.
        '''
        print("** CONFIG - COMMON **")
        print(f"fileNameList=\t{self.fileNameList}")
        print("")
        print(f"nSignal=\t{self.nSignal}")
        print(f"nTrain=\t\t{self.nTrain}")
        print(f"nValidation=\t{self.nValidation}")
        print(f"nTest=\t\t{self.nTest}")
        print("")
        print(f"nSample=\t{self.nSample}")
        print(f"nCW=\t\t{self.nCW}")
        print(f"nBit=\t\t{self.nBit}")
        print(f"nHalfBit=\t{self.nHalfBit}")
        print(f"nBitPreamble=\t{self.nBitPreamble}")
        print(f"nBitData=\t{self.nBitData}")
        print(f"nExtra=\t\t{self.nExtra}")
        print("")

    def readSignal(self, type, signalPath, postfix, fileName=""):
        '''! Reads the signal from signal file(s).

        @param type The type of the signal to read. Default value is used when
        the function is called from the RuleBased class.
        - "absolute" : The signal consists of a absolute value.
        - "complex" : The signal consists of a complex number.

        @param signalPath The path where the signal file is located.

        @param postfix The subset to read.
        - "all" : Reads all sets.
        - "train" : Reads train set.
        - "validatoin" : Reads validation set.
        - "test" : Reads test set.

        @param fileName The name of the signal file to read. If not defined,
        read all files in fileNameList.

        @return A list of signals read.
        '''
        if type == "absolute":
            signalList = []
        elif type == "complex":
            signalIList = []
            signalQList = []
        else:
            assert False, "Invalid type " + type + "\n"

        if postfix == "all":
            postfix = ""
        elif postfix == "train" or postfix == "validation"\
                or postfix == "test":
            postfix = "_" + postfix
        else:
            assert False, "Invalid postfix " + postfix + "\n"

        if fileName == "":
            fileNameList = self.fileNameList

            if self.augRatio == 1:
                augList = [""]
            else:
                augList = ["_" + str(i) for i in np.arange(self.augRatio)]
            curAugRatio = self.augRatio

            pbar = tqdm(
                total=int(len(fileNameList) * self.augRatio), desc="READING",
                ncols=100, unit=" file")
        else:
            fileNameList = [fileName]
            curAugRatio = 1
            augList = [""]

        for fileName in fileNameList:
            for x in range(curAugRatio):
                if type == "absolute":
                    signal = np.load(
                        self.signalPath + fileName + augList[x] + "_signal" +
                        postfix + ".npy")
                    signalList.extend(signal)

                elif type == "complex":
                    signalI = np.load(
                        self.signalPath + fileName + augList[x] + "_Isignal" +
                        postfix + ".npy")
                    signalIList.extend(signalI)

                    signalQ = np.load(
                        self.signalPath + fileName + augList[x] + "_Qsignal" +
                        postfix + ".npy")
                    signalQList.extend(signalQ)

                if len(fileNameList) > 1:
                    pbar.update(1)

        if len(fileNameList) > 1:
            pbar.close()

        if type == "absolute":
            return signalList
        elif type == "complex":
            return signalIList, signalQList

    def readLabel(self, type, labelPath, postfix, fileName=""):
        '''! Reads the signal from signal file(s).

        @param type The type of the label to read.
        - "", "org" : Origianl label.
        - "regression" : Regression label.
        - "classify" : Classify label.

        @param labelPath The path where the signal file is located.

        @param postfix The subset to read.
        - "all" : Reads all sets.
        - "train" : Reads train set.
        - "validatoin" : Reads validation set.
        - "test" : Reads test set.

        @param fileName The name of the label file to read. If not defined,
        read all files in fileNameList.

        @return A list of labels read.
        '''
        labelList = []

        if type == "":
            pass
        elif type == "org" or type == "regression" or type == "classify":
            type = "_" + type
        else:
            assert False, "Invalid type " + type + "\n"

        if postfix == "all":
            postfix = ""
        elif postfix == "train" or postfix == "validation"\
                or postfix == "test":
            postfix = "_" + postfix
        else:
            assert False, "Invalid postfix " + postfix + "\n"

        if fileName == "":
            fileNameList = self.fileNameList
            pbar = tqdm(
                total=len(fileNameList), desc="READING", ncols=100,
                unit=" file")
        else:
            fileNameList = [fileName]

        for fileName in fileNameList:
            label = np.load(
                self.labelPath + fileName + "_label" + type + postfix + ".npy")
            labelList.extend(label)

            if len(fileNameList) > 1:
                pbar.update(1)

        if len(fileNameList) > 1:
            pbar.close()

        return labelList
