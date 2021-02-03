##
# @file SignalAugmentation.py
#
# @brief Defines the SignalAugmentation class.


import os
import configparser
import numpy as np
from tqdm import tqdm
from Preprocessor import Preprocessor
import timeit


class SignalAugmentation(Preprocessor):
    '''! Defines the augmentation procedures of signal(s).
    '''

    def __init__(self):
        '''! The SignalAugmentation class initializer.
        '''
        super(SignalAugmentation, self).__init__()

        ## @var configSA
        # The configuration data read from the config file.
        self.configSA = configparser.ConfigParser()
        self.configSA.optionxform = lambda option: option
        self.configSA.read(self.configPath + "confSA.ini")

        assert len(self.configSA.sections()), "Fail to load config file.\n"

        ## @var signalPath
        # The path where the signal file is located.
        self.signalPath = self.configSA["PATH"]["signalPath"]
        ## @var outputPath
        # The path where the standardized signal file will be stored.
        self.outputPath = self.configSA["PATH"]["outputPath"]

        if self.augRatio > 1:
            ## @var augRef
            #
            self.augRef = float(self.configSA["AUGMENTATION"]["augRef"])
            self.augWidth = float(self.configSA["AUGMENTATION"]["augWidth"])

            self.augList = []
            for aug in self.configSA["AUG_LIST"]:
                self.augList.append(float(self.configSA["AUG_LIST"][aug]))

        self.printConfigSA()

    def printConfigSA(self):
        '''! Prints the configuration data.
        '''
        print("** CONFIG - Signal Augmentation **")
        print(f"signalPath=\t{self.signalPath}")
        print(f"outputPath=\t{self.outputPath}")
        if self.augRatio > 1:
            print(f"augRef=\t\t{self.augRef:.2f}")
            print(f"augWidth=\t{self.augWidth:.2f}")
            print(f"augList=\t{self.augList}")
        print("")

    def main(self):
        '''! Defines the main procedures.
        '''
        assert os.path.isdir(self.signalPath),\
            f"signalPath= {self.signalPath} does not exist.\n"

        if os.path.isdir(self.outputPath) is False:
            os.mkdir(self.outputPath)
            print(
                "Successfuly created an unexist folder! output_path= " +
                self.outputPath)
            print("")

        for fileName in self.fileNameList:
            print(f"** {fileName} **")

            signal = self.readSignal(
                type="absolute", signalPath=self.signalPath, postfix="all",
                fileName=fileName)
            signalI, signalQ = self.readSignal(
                type="complex", signalPath=self.signalPath, postfix="all",
                fileName=fileName)

            self.augmentation(
                fileName, [signal, signalI, signalQ],
                ["_signal", "_Isignal", "_Qsignal"])

            print("")

    def augmentation(self, fileName, signal, postfix):
        '''! Generates and saves the augmented signal.

        @param signal The list of signal to standardize.

        @return A standardized signal.
        '''
        for augIdx in range(len(self.augList)):
            aug = self.augList[augIdx]
            augmentedSignal = np.zeros(
                (len(signal), self.nSignal, self.nSample))

            pbar = tqdm(
                total=self.nSignal, desc=str(aug), ncols=100, unit=" signal")

            for idx in range(self.nSignal):
                augCoeff =\
                    self.augRef / (aug + np.random.rand() * self.augWidth)
                sizeWindow = int(1 / abs(1 - augCoeff))
                targetList = np.random.randint(
                    sizeWindow, size=(int(self.nSample / sizeWindow))
                )

                if augCoeff < 1:
                    instance = self.extendAugmentation
                else:
                    instance = self.shrinkAugmentation

                for x in range(len(signal)):
                    augmentedSignal[x][idx] =\
                        instance(signal[x][idx], sizeWindow, targetList)
                pbar.update(1)

            pbar.close()

            for x in range(len(signal)):
                np.save(
                    self.outputPath + fileName + "_" + str(augIdx) +
                    postfix[x], augmentedSignal[x])

    def extendAugmentation(self, signal, sizeWindow, targetList):
        augmentedSignal = []

        cur = 0
        for x in range(int(self.nSample / sizeWindow)):
            cur = x
            if (x + 1) * (sizeWindow + 1) > self.nSample:
                break

            st = int(x * sizeWindow)
            ed = int((x + 1) * sizeWindow)
            target = targetList[x]

            window = signal[st:ed]
            augmentedSignal.extend(window[:target + 1])
            augmentedSignal.append(np.mean(window[target:target + 2]))
            augmentedSignal.extend(window[target + 1:])

        remainder = signal[int(cur * sizeWindow):]
        size = self.nSample - len(augmentedSignal)
        augmentedSignal.extend(remainder[:size])

        return np.array(augmentedSignal)

    def shrinkAugmentation(self, signal, sizeWindow, targetList):
        augmentedSignal = []

        cur = 0
        for x in range(int(self.nSample / sizeWindow)):
            st = int(x * sizeWindow)
            ed = int((x + 1) * sizeWindow)
            target = targetList[x]

            window = signal[st:ed]
            augmentedSignal.extend(window[:target])
            augmentedSignal.extend(window[target + 1:])
            cur += 1

        remainder = signal[int(cur * sizeWindow):]
        augmentedSignal.extend(remainder)
        size = self.nSample - len(augmentedSignal)
        for x in range(size):
            augmentedSignal.append(signal[-1])

        return np.array(augmentedSignal)
