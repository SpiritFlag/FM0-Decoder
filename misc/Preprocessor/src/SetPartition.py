##
# @file SetPartition.py
#
# @brief Defines the SetPartition class.


import os
import configparser
import numpy as np
from tqdm import tqdm
from Preprocessor import Preprocessor


class SetPartition(Preprocessor):
    '''! Defines the creation procedures of label(s).
    '''

    def __init__(self):
        '''! The SetPartition class initializer.
        '''
        super(SetPartition, self).__init__()

        ## @var configSP
        # The configuration data read from the config file.
        self.configSP = configparser.ConfigParser()
        self.configSP.optionxform = lambda option: option
        self.configSP.read(self.configPath + "confSP.ini")

        assert len(self.configSP.sections()), "Fail to load config file.\n"

        ## @var signalPath
        # The path where the signal file is located.
        self.signalPath = self.configSP["PATH"]["signalPath"]
        ## @var labelPath
        # The path where the label file is located.
        self.labelPath = self.configSP["PATH"]["labelPath"]
        ## @var outputPath
        # The path where the index file is located.
        self.indexPath = self.configSP["PATH"]["indexPath"]
        ## @var onlyTest
        # If this value is true, makes all set to test set.
        self.onlyTest = bool(self.configSP["MODE"]["onlyTest"])

        self.printConfigSP()

    def printConfigSP(self):
        '''! Prints the configuration data.
        '''
        print("** CONFIG - Set Partition **")
        print(f"signalPath=\t{self.signalPath}")
        print(f"labelPath=\t{self.labelPath}")
        print(f"indexPath=\t{self.indexPath}")
        print(f"onlyTest=\t{self.onlyTest}")
        print("")

    def main(self):
        '''! Defines the main procedures.
        '''
        assert os.path.isdir(self.signalPath),\
            f"signalPath= {self.signalPath} does not exist.\n"

        assert os.path.isdir(self.labelPath),\
            f"labelPath= {self.labelPath} does not exist.\n"

        if os.path.isdir(self.indexPath) is False:
            os.mkdir(self.indexPath)
            print(
                "Successfuly created an unexist folder! index_path= " +
                self.indexPath)
            print("")


        if self.onlyTest is True:
            index = [[], [], np.arange(self.nSignal)]

        else:
            while True:
                try:
                    print("Input Index Number(0 to create new index): ", end="")
                    menu = int(input())
                    path = self.indexPath + str(menu)

                    if menu == 0:
                        index = self.makeIndex()
                        while True:
                            try:
                                print("Input Index Number to Save: ", end="")
                                saveIdx = int(input())
                                savePath = self.indexPath + str(saveIdx)
                                assert not os.path.isfile(savePath + "_1.npy"),\
                                    f"index file {saveIdx} does exist.\n"
                                np.save(savePath + "_1.npy", index[0])
                                np.save(savePath + "_2.npy", index[1])
                                np.save(savePath + "_3.npy", index[2])
                                break
                            except Exception as ex:
                                print(ex)
                    else:
                        assert os.path.isfile(path + "_1.npy"),\
                            f"index file {menu} does not exist.\n"
                        index = []
                        index.append(np.load(path + "_1.npy"))
                        index.append(np.load(path + "_2.npy"))
                        index.append(np.load(path + "_3.npy"))
                    break
                except Exception as ex:
                    print(ex)

        while True:
            try:
                print("Select (1:signal, 2:label): ", end="")
                menu = int(input())
                if menu != 1 and menu != 2:
                    raise ValueError(f"invalid menu number: {menu}")
                print("")
                break
            except Exception as ex:
                print(ex)

        if menu == 2:
            self.augRatio = 1

        pbar = tqdm(
            total=int(len(self.fileNameList) * self.augRatio),
            desc="PROCESSING", ncols=100, unit=" file")

        for fileName in self.fileNameList:
            if menu == 1:
                if self.augRatio == 1:
                    augList = [""]
                else:
                    augList = ["_" + str(i) for i in np.arange(self.augRatio)]

                for x in range(self.augRatio):
                    curName = fileName + augList[x]
                    signal = self.readSignal(
                        type="absolute", signalPath=self.signalPath, postfix="all",
                        fileName=curName)
                    signalI, signalQ = self.readSignal(
                        type="complex", signalPath=self.signalPath, postfix="all",
                        fileName=curName)

                    signalList = [signal, signalI, signalQ]
                    typeList = ["signal", "Isignal", "Qsignal"]
                    for x in range(len(typeList)):
                        signal = signalList[x]
                        type = typeList[x]
                        self.saveSet(
                            set=self.shuffleSet(set=signal, index=index),
                            path=self.signalPath, fileName=curName, type=type)

                    pbar.update(1)

            elif menu == 2:
                for type in ["org", "regression", "classify"]:
                    label = self.readLabel(
                        type=type, labelPath=self.labelPath, postfix="all",
                        fileName=fileName)
                    self.saveSet(
                        set=self.shuffleSet(set=label, index=index),
                        path=self.labelPath, fileName=fileName,
                        type="label_" + type)
                pbar.update(1)

        pbar.close()
        print("")

    def makeIndex(self):
        index = np.arange(self.nSignal)
        np.random.shuffle(index)

        shuffledIndex = []
        shuffledIndex.append(index[0:self.nTrain])
        shuffledIndex.append(index[self.nTrain:self.nTrain+self.nValidation])
        shuffledIndex.append(index[self.nTrain+self.nValidation:self.nSignal])

        return shuffledIndex

    def shuffleSet(self, set, index):
        shuffledSet = []
        for x in range(len(index)):
            curSet = []
            for idx in index[x]:
                curSet.append(set[idx])
            shuffledSet.append(np.array(curSet))
        return shuffledSet

    def saveSet(self, set, path, fileName, type):
        postfix_list = ["train", "validation", "test"]
        for x in range(len(postfix_list)):
            postfix = postfix_list[x]
            np.save(
                path + fileName + "_" + type + "_" + postfix,
                np.array(set[x]))
