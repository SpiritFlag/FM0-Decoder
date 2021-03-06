import sys
import numpy as np

from tqdm import tqdm
from global_vars import *
from A_split_set.global_vars import *



def subprocess(file_name, signal_path_list, signal_list, Isignal_list, Qsignal_list, label_output_path, label, RNindex, postfix):
  try:
    npy_list = []
    npy_Ilist = []
    npy_Qlist = []
    for x in range(len(signal_list)):
      npy_list.append([])
      npy_Ilist.append([])
      npy_Qlist.append([])
    npy_label = []

    for idx in tqdm(range(len(RNindex)), desc=postfix.upper(), ncols=100, unit=" signal"):
      for x in range(len(signal_list)):
        signal = signal_list[x]
        npy_list[x].append(signal[RNindex[idx]])
        Isignal = Isignal_list[x]
        npy_Ilist[x].append(Isignal[RNindex[idx]])
        Qsignal = Qsignal_list[x]
        npy_Qlist[x].append(Qsignal[RNindex[idx]])

      npy_label.append(label[RNindex[idx]])

    for x in range(len(signal_list)):
      signal_path = signal_path_list[x]
      np.save(signal_path + file_name + "_signal_" + postfix, npy_list[x])
      np.save(signal_path + file_name + "_Isignal_" + postfix, npy_Ilist[x])
      np.save(signal_path + file_name + "_Qsignal_" + postfix, npy_Qlist[x])

    np.save(label_output_path + file_name + "_label_" + postfix, npy_label)

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[split_set:subprocess:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")



def process(file_name):
  try:
    signal = np.load(signal_path + file_name + "_signal.npy")
    signal_std = np.load(signal_path2 + file_name + "_signal.npy")
    signal_std_cliffing = np.load(signal_path3 + file_name + "_signal.npy")
    Isignal = np.load(signal_path + file_name + "_Isignal.npy")
    Isignal_std = np.load(signal_path2 + file_name + "_Isignal.npy")
    Isignal_std_cliffing = np.load(signal_path3 + file_name + "_Isignal.npy")
    Qsignal = np.load(signal_path + file_name + "_Qsignal.npy")
    Qsignal_std = np.load(signal_path2 + file_name + "_Qsignal.npy")
    Qsignal_std_cliffing = np.load(signal_path3 + file_name + "_Qsignal.npy")
    label = np.load(label_path + file_name + "_label.npy")


    signal_path_list = [signal_path, signal_path2, signal_path3]
    signal_list = [signal, signal_std, signal_std_cliffing]
    Isignal_list = [Isignal, Isignal_std, Isignal_std_cliffing]
    Qsignal_list = [Qsignal, Qsignal_std, Qsignal_std_cliffing]


    if make_test_only is False:
      RNindex = np.arange(n_signal)
      np.random.shuffle(RNindex)
      RNtrain = RNindex[0:n_signal_train]
      RNvalidation = RNindex[n_signal_train:n_signal_train+n_signal_validation]
      RNtest = RNindex[n_signal_train+n_signal_validation:n_signal]
    else:
      RNtrain = [0]
      RNvalidation = [0]
      RNtest = [i for i in range(n_signal)]



    subprocess(file_name, signal_path_list, signal_list, Isignal_list, Qsignal_list, label_output_path, label, RNtrain, "train")
    subprocess(file_name, signal_path_list, signal_list, Isignal_list, Qsignal_list, label_output_path, label, RNvalidation, "validation")
    subprocess(file_name, signal_path_list, signal_list, Isignal_list, Qsignal_list, label_output_path, label, RNtest, "test")


  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[split_set:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
