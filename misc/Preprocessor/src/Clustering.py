import os
import configparser
import numpy as np
from tqdm import tqdm
from Preprocessor import Preprocessor
import timeit

from sklearn.cluster import KMeans

class Clustering(Preprocessor):

    def __init__(self):
        '''! The SignalAugmentation class initializer.
        '''
        super(Clustering, self).__init__()

        ## @var configSA
        # The configuration data read from the config file.
        self.configSA = configparser.ConfigParser()
        self.configSA.optionxform = lambda option: option
        self.configSA.read(self.configPath + "confSA.ini")

        assert len(self.configSA.sections()), "Fail to load config file.\n"

        ## @var signalPath
        # The path where the signal file is located.
        self.signalPath = "../data/exp12_B_signal/"
        ## @var outputPath
        # The path where the standardized signal file will be stored.
        self.outputPath = "../data/exp13_B_signal/"



    def main(self):
        '''! Defines the main procedures.
        '''
        assert os.path.isdir(self.signalPath),\
            f"signalPath= {self.signalPath} does not exist.\n"


        for fileName in self.fileNameList:
            i = np.load(self.signalPath + fileName + "_Isignal_test.npy")
            q = np.load(self.signalPath + fileName + "_Qsignal_test.npy")
            signal = np.swapaxes(np.array([i, q]).transpose(), 0, 1)
            labels_list = []

            for x in tqdm(range(3000), desc=fileName, ncols=100, unit=" signal"):
                kmeans = KMeans(n_clusters=2)
                kmeans.fit(signal[x])
                labels = kmeans.labels_

                if labels[0] == 1:
                    new_labels = []
                    for label in labels:
                        if label == 0:
                            new_labels.append(1)
                        else:
                            new_labels.append(0)
                    labels_list.append(np.array(new_labels))
                else:
                    labels_list.append(labels)

            np.save(self.outputPath + fileName + "_signal_test", np.array(labels_list))
