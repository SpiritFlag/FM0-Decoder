# -*- coding: utf-8 -*-
from tqdm import tqdm

from Signal import Signal



def read_file(folder_path, file_name, size):
  file = open(folder_path + file_name, "r")
  signals = list()

  for n in tqdm(range(size), desc=file_name, ncols=80, unit="signal"):
    line = file.readline()
    if not line: break
    data = line.split(",")
    signals.append(Signal(file_name, data))

  return signals
