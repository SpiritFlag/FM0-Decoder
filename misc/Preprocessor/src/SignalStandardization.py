##
# @file SignalStandardization.py
#
# @brief Defines the SignalStandardization class.


import os
import configparser
import numpy as np
from tqdm import tqdm
from Preprocessor import Preprocessor
import timeit


class SignalStandardization(Preprocessor):
    '''! Defines the standardization procedures of signal(s).
    '''

    def __init__(self):
        '''! The SignalStandardization class initializer.
        '''
        super(SignalStandardization, self).__init__()

        ## @var configSS
        # The configuration data read from the config file.
        self.configSS = configparser.ConfigParser()
        self.configSS.optionxform = lambda option: option
        self.configSS.read(self.configPath + "confSS.ini")

        assert len(self.configSS.sections()), "Fail to load config file.\n"

        ## @var signalPath
        # The path where the signal file is located.
        self.signalPath = self.configSS["PATH"]["signalPath"]
        ## @var outputPath
        # The path where the standardized signal file will be stored.
        self.outputPath = self.configSS["PATH"]["outputPath"]

        self.printConfigSS()

    def printConfigSS(self):
        '''! Prints the configuration data.
        '''
        print("** CONFIG - Signal Standardization **")
        print(f"signalPath=\t{self.signalPath}")
        print(f"outputPath=\t{self.outputPath}")
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

        pbar = tqdm(
            total=len(self.fileNameList), desc="PROCESSING", ncols=100,
            unit=" signal")

        for fileName in self.fileNameList:
            signal = self.readSignal(
                type="absolute", signalPath=self.signalPath, postfix="all",
                fileName=fileName)
            signalI, signalQ = self.readSignal(
                type="complex", signalPath=self.signalPath, postfix="all",
                fileName=fileName)

            signal = self.standardization(signal)
            signalI = self.standardization(signalI)
            signalQ = self.standardization(signalQ)

            np.save(
                self.outputPath + fileName + "_signal", np.array(signal))
            np.save(
                self.outputPath + fileName + "_Isignal", np.array(signalI))
            np.save(
                self.outputPath + fileName + "_Qsignal", np.array(signalQ))

            pbar.update(1)

        pbar.close()
        print("")

    def standardization(self, signal):
        '''! Returns the standardized signal.

        @param signal The signal to standardize.

        @return A standardized signal.
        '''
        for idx in range(self.nSignal):
            signal[idx] =\
                (signal[idx] - np.mean(signal[idx])) / np.std(signal[idx])
        return signal
