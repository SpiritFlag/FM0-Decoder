##
# @file LabelCreation.py
#
# @brief Defines the LabelCreation class.


import os
import configparser
import numpy as np
from tqdm import tqdm
from Preprocessor import Preprocessor


class LabelCreation(Preprocessor):
    '''! Defines the creation procedures of label(s).
    '''

    def __init__(self):
        '''! The LabelCreation class initializer.
        '''
        super(LabelCreation, self).__init__()

        ## @var configLC
        # The configuration data read from the config file.
        self.configLC = configparser.ConfigParser()
        self.configLC.optionxform = lambda option: option
        self.configLC.read(self.configPath + "confLC.ini")

        assert len(self.configLC.sections()), "Fail to load config file.\n"

        ## @var labelPath
        # The path where the label file is located.
        self.labelPath = self.configLC["PATH"]["labelPath"]
        ## @var outputPath
        # The path where the created label file will be stored.
        self.outputPath = self.configLC["PATH"]["outputPath"]

        self.printConfigLC()

    def printConfigLC(self):
        '''! Prints the configuration data.
        '''
        print("** CONFIG - Label Creation **")
        print(f"labelPath=\t{self.labelPath}")
        print(f"outputPath=\t{self.outputPath}")
        print("")

    def main(self):
        '''! Defines the main procedures.
        '''
        assert os.path.isdir(self.labelPath),\
            f"labelPath= {self.labelPath} does not exist.\n"

        if os.path.isdir(self.outputPath) is False:
            os.mkdir(self.outputPath)
            print(
                "Successfuly created an unexist folder! output_path= " +
                self.outputPath)
            print("")

        for fileName in self.fileNameList:
            label = self.readLabel(
                type="", labelPath=self.labelPath, postfix="all",
                fileName=fileName)

            regressionLabel = np.zeros((self.nSignal, int(2 * self.nBitData)))
            classifyLabel = np.zeros((self.nSignal, int(4 * self.nBitData)))
            pbar = tqdm(
                total=self.nSignal, desc=fileName, ncols=100, unit=" label")

            for idx in range(self.nSignal):
                regressionLabel[idx] = self.makeRegressionLabel(label[idx])
                classifyLabel[idx] = self.makeClassifyLabel(label[idx])
                pbar.update(1)

            np.save(
                self.outputPath + fileName + "_label_org",
                np.array(label))
            np.save(
                self.outputPath + fileName + "_label_regression",
                np.array(regressionLabel))
            np.save(
                self.outputPath + fileName + "_label_classify",
                np.array(classifyLabel))
            pbar.close()
        print("")

    def makeRegressionLabel(self, label):
        '''! Creates and returns a half-bit amplitude regression label from the
        input label.

        @param label The label to convert.

        @return A label converted.
        '''
        regressionLabel = []
        level = -1

        for bit in label:
            # L(0) H(1)
            if bit == 1:
                if level == 1:
                    # State 1: HH
                    regressionLabel.extend([1, 1])
                else:
                    # State 4: LL
                    regressionLabel.extend([0, 0])
                level *= -1
            else:
                if level == 1:
                    # State 2: HL
                    regressionLabel.extend([1, 0])
                else:
                    # State 3: LH
                    regressionLabel.extend([0, 1])

        return np.array(regressionLabel)

    def makeClassifyLabel(self, label):
        '''! Creates and returns a FM-0 symbol classify label from the
        input label.

        @param label The label to convert.

        @return A label converted.
        '''
        classifyLabel = []
        level = -1

        for bit in label:
            # L(0) H(1)
            if bit == 1:
                if level == 1:
                    # State 1: HH
                    classifyLabel.extend([1, 0, 0, 0])
                else:
                    # State 4: LL
                    classifyLabel.extend([0, 0, 0, 1])
                level *= -1
            else:
                if level == 1:
                    # State 2: HL
                    classifyLabel.extend([0, 1, 0, 0])
                else:
                    # State 3: LH
                    classifyLabel.extend([0, 0, 1, 0])

        return np.array(classifyLabel)
