##
# @file SignalDimensionalityReduction.py
#
# @brief Defines the SignalDimensionalityReduction class.


import os
import configparser
import numpy as np
from tqdm import tqdm
from Preprocessor import Preprocessor


class SignalDimensionalityReduction(Preprocessor):
    '''! Defines the dimensionality reduction procedures of signal(s).
    '''

    def __init__(self):
        '''! The SignalDimensionalityReduction class initializer.
        '''
        super(SignalDimensionalityReduction, self).__init__()

        ## @var configSDR
        # The configuration data read from the config file.
        self.configSDR = configparser.ConfigParser()
        self.configSDR.optionxform = lambda option: option
        self.configSDR.read(self.configPath + "confSDR.ini")

        assert len(self.configSDR.sections()), "Fail to load config file.\n"

        ## @var signalPath
        # The path where the signal file is located.
        self.signalPath = self.configSDR["PATH"]["signalPath"]

        self.printConfigSDR()

    def printConfigSDR(self):
        '''! Prints the configuration data.
        '''
        print("** CONFIG - Signal Dimensionality Reduction **")
        print(f"signalPath=\t{self.signalPath}")
        print("")

    def main(self):
        '''! Defines the main procedures.
        '''
        assert os.path.isdir(self.signalPath),\
            f"signalPath= {self.signalPath} does not exist.\n"

        for fileName in self.fileNameList:
            signalI, signalQ = self.readSignal(
                type="complex", signalPath=self.signalPath, postfix="all",
                fileName=fileName)

            reductedSignal = np.zeros((self.nSignal, self.nSample))
            pbar = tqdm(
                total=self.nSignal, desc=fileName, ncols=100, unit=" signal")

            for idx in range(self.nSignal):
                centerI = self.estimateCenter(signalI[idx])
                centerQ = self.estimateCenter(signalQ[idx])

                signal = np.zeros((self.nSample))
                for n in range(self.nSample):
                    signal[n] = np.sqrt(
                        (signalI[idx][n] - centerI) ** 2 +
                        (signalQ[idx][n] - centerQ) ** 2)
                reductedSignal[idx] = signal
                pbar.update(1)

            np.save(
                self.signalPath + fileName + "_signal",
                np.array(reductedSignal))
            pbar.close()
        print("")

    def estimateCenter(self, signal):
        '''! Returns the center value of the continuous wave of the input
        signal estimated using the Kalman Filter.

        @param signal The signal to estimate the center value.

        @return A center value estimated.
        '''
        predict = signal[0]
        predict_error = 1
        kalman_gain = 1
        measurement_error = 1e-7

        for idx in range(1, self.nCW + 1):
            kalman_gain = predict_error / (predict_error + measurement_error)
            predict = predict * (1 - kalman_gain) + kalman_gain * signal[idx]
            predict_error = (1 - kalman_gain) * predict_error

        return predict
