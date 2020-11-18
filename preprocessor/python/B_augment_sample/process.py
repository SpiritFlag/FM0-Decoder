import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from B_augment_sample.global_vars import *



def process(file_name):
  try:
    postfix_list = ["train", "validation", "test"]

    for postfix in postfix_list:
      signal = np.load(signal_path + file_name + "_signal_" + postfix + ".npy")

      for augment in augment_list:
      #for augment_idx in tqdm(range(len(augment_list)), desc=postfix.upper(), ncols=100, unit=" subset"):
      #  augment = augment_list[augment_idx]
        npy_signal = []

        #for idx in range(len(signal)):
        for idx in tqdm(range(len(signal)), desc=postfix.upper()+" "+str(augment), ncols=100, unit=" signal"):
          result = []
          augment_coefficient = augment_standard / (augment + np.random.rand() * augment_width)

          if append_t1 is True:
            t1 = int(np.random.rand() * 50)
            for x in range(t1):             # append random T1
              result.append(signal[idx][0])
          else:
            t1 = 0

          if augment_coefficient < 1:     # size up
            conv_window = int(1 / (1 - augment_coefficient))

            if augment_mode == 2:
              margin_signal = []
              for x in range(augment_avg_window):
                margin_signal.append(signal[idx][0])
              margin_signal.extend(signal[idx])
              for x in range(augment_avg_window):
                margin_signal.append(signal[idx][-1])

            elif augment_mode == 3:
              margin_signal = []
              margin_signal.append(signal[idx][0])
              margin_signal.extend(signal[idx])
              margin_signal.append(signal[idx][-1])

            cur = 0
            for x in range(int(n_sample / conv_window)):
              cur = x
              if (t1 + (cur + 1) * conv_window) > n_sample:
                break

              if augment_mode == 1:
                window = signal[idx][int(x*(conv_window-1)):int((x+1)*(conv_window-1))]
                result.extend(window)
                result.append(window[-1])

              elif augment_mode == 2:
                window = margin_signal[int(x*(conv_window-1)):int((x+1)*(conv_window-1)+2*augment_avg_window)]
                target = int(np.random.rand()*(conv_window-1))
                result.extend(window[augment_avg_window:augment_avg_window+target])
                result.append(np.mean(window[target:target+int(2*augment_avg_window)+1]))
                result.extend(window[augment_avg_window+target:-augment_avg_window])

              elif augment_mode == 3:
                window = margin_signal[int(x*(conv_window-1)):int((x+1)*(conv_window-1)+2)]
                target = int(np.random.rand()*(conv_window-1))
                result.extend(window[1:1+target])
                result.append(np.mean(window[target:target+2]))
                result.extend(window[1+target:-1])

            size_rest = n_sample - len(result)
            start = int(cur * (conv_window - 1))
            result.extend(signal[idx][start:start+size_rest])

          elif augment_coefficient >= 1:  # size down
            conv_window = int(1 / (augment_coefficient - 1))

            cur = 0
            for x in range(int(n_sample / (conv_window+1))):
              cur = x
              if (t1 + (cur + 1) * (conv_window+1)) > n_sample:
                break

              window = signal[idx][int(x*(conv_window+1)):int((x+1)*(conv_window+1))]

              if augment_mode == 1:
                result.extend(window[:-1])

              elif augment_mode == 2 or augment_mode == 3:
                target = int(np.random.rand()*(conv_window+1))
                result.extend(window[:target])
                result.extend(window[target+1:])

            start = int((cur + 1) * (conv_window + 1))
            size_rest = np.min([n_sample - start, n_sample - len(result)])
            result.extend(signal[idx][start:start+size_rest])

            size_margin = n_sample - len(result)
            for x in range(size_margin):
              result.append(signal[idx][-1])

          if augment_noise_ratio > 0:
            for x in range(augment_noise_ratio):
              noise_result = result + augment_noise_level * np.random.normal(0, 1, len(result)) * np.random.randn()
              npy_signal.append(np.array(noise_result))
          else:
            npy_signal.append(np.array(result))

        np.save(output_path + file_name + "_signal_" + str(augment) + "_" + postfix, npy_signal)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[augment_sample:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
