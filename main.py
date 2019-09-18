# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import sys
import os
from tqdm import tqdm

import global_vars
from read_file import read_file
from decoding import detect_data

bit_data = global_vars.bit_data
folder_path = "data/"  # 파일이 들어 있는 폴더 경로
log_path = "log/"
iteration = 2000



for a in ["50", "100", "150", "200", "250", "300", "350", "400"]:
  for b in ["l", "r"]:
    for c in ["20", "60", "100"]:
      file_name = a + "_" + b + c
      if os.path.exists(folder_path + file_name) and os.path.getsize(folder_path + file_name) > 0:
        print("")
        signals = read_file(folder_path, file_name, iteration)
        decoded_bit = [0] * (bit_data+1)

        for n in tqdm(range(iteration), desc="DECODING", ncols=80, unit="signal"):
          decoded_bit[detect_data(signals[n])] += 1

        file = open(log_path + file_name, "w")
        for d in decoded_bit:
          file.write(str(d) + "\n")

        print("SUCCESS: " + str(decoded_bit[bit_data]) + "\tFAIL: " + str(iteration - decoded_bit[bit_data]) + "\tRATE: " + str(round(100 * (decoded_bit[bit_data] / float(iteration)), 2)))

#        plt.plot(decoded_bit)
#        plt.show()
        plt.plot(decoded_bit)
        plt.savefig(log_path + file_name + ".png", dpi=1000)
        plt.clf()
