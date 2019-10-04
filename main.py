# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import sys
import os
from tqdm import tqdm
import tensorflow as tf
import numpy as np

import global_vars
from read_file import read_file
from decoding import detect_data
from Autoencoder import Autoencoder
import training

bit_data = global_vars.bit_data
folder_path = "data/"  # 파일이 들어 있는 폴더 경로
log_path = "log/"
iteration = 1000


autoencoder = Autoencoder()
signals = read_file(folder_path, "50_l20", iteration)

#plt.plot(signals[0].data_samples)
#plt.show()

input_signals = list()
answer_signals = list()
for idx in range(iteration):
  input_signals.append(signals[idx].data_samples)
  answer_signals.append(signals[idx].answer_samples)

train_input = np.array(input_signals[0:999])
train_answer = np.array(answer_signals[0:999])
test_input = np.array(input_signals[999:1000])
test_answer = np.array(answer_signals[999:1000])


autoencoder.train_model(train_input, train_answer)
autoencoder.test_model(test_input, test_answer)

'''
epoch = 10

for ep in range(epoch):
  ep_train_loss = 0
  for n in tqdm(range(len(train_input)), desc="TRAINING", ncols=80, unit="signal"):
    train_loss = training.train(autoencoder, train_input[n], train_answer[n])
    ep_train_loss += train_loss
  ep_train_loss /= len(train_input)

  ep_test_loss = 0
  for n in tqdm(range(len(test_input)), desc="TESTING", ncols=80, unit="signal"):
    test_loss = training.loss(autoencoder, test_input[n], test_answer[n])
    ep_test_loss += test_loss
  ep_test_loss /= len(test_input)

  print("EPOCH " + str(ep) + " / " + str(epoch) + "\tTRAIN LOSS= " + str(ep_train_loss) + "\tTEST LOSS= " + str(ep_test_loss) + "\n")
'''

'''
for a in ["50", "100", "150", "200", "250", "300", "350", "400"]:
  for b in ["l", "r"]:
    for c in ["20", "60", "100"]:
      file_name = a + "_" + b + c
      if os.path.exists(folder_path + file_name) and os.path.getsize(folder_path + file_name) > 0:
        print("")
        signals = read_file(folder_path, file_name, iteration)
#        plt.plot(signals[0].answer_samples)
#        plt.show()
        decoded_bit = [0] * (bit_data+1)

        low = 0
        high = 0
        for n in tqdm(range(iteration), desc="DECODING", ncols=80, unit="signal"):
          plt.plot(signals[n].rev_std_samples)
          plt.show()
          '''
'''          x, y = detect_preamble(signals[n])
          if y == -1:
            low += 1
          else:
            high += 1
        print("low: " + str(low) + "\thigh: " + str(high))
          decoded_bit[detect_data(signals[n])] += 1

        file = open(log_path + file_name, "w")
        for d in decoded_bit:
          file.write(str(d) + "\n")

        print("SUCCESS: " + str(decoded_bit[bit_data]) + "\tFAIL: " + str(iteration - decoded_bit[bit_data]) + "\tRATE: " + str(round(100 * (decoded_bit[bit_data] / float(iteration)), 2)))
'''
#        plt.plot(decoded_bit)
#        plt.show()
#        plt.plot(decoded_bit)
#        plt.savefig(log_path + file_name + ".png", dpi=1000)
#        plt.clf()
