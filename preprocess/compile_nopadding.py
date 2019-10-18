import os
from tqdm import tqdm
from Signal import Signal

folder_pathR = "data/"
folder_pathW = "data_nopadding/"
size = 2000

for a in ["50", "100", "150", "200", "250", "300", "350", "400"]:
  for b in ["l", "r"]:
    for c in ["20", "60", "100"]:
      file_name = a + "_" + b + c
      if os.path.exists(folder_pathR + file_name) and os.path.getsize(folder_pathR + file_name) > 0:
        fileR = open(folder_pathR + file_name, "r")
        fileR = open("data/50_l20", "r")
        signals = list()

        for n in tqdm(range(size), desc=file_name, ncols=80, unit="signal"):
          line = fileR.readline()
          if not line: break
          data = line.split(",")
          signals.append(Signal(file_name, data))

        fileWa = open(folder_pathW + file_name + "_a", "w")
        fileWs = open(folder_pathW + file_name + "_s", "w")
        for idx in tqdm(range(size), desc="WRITING", ncols=80, unit="signal"):
          fileWa.write(signals[idx].answer)
          fileWa.write("\n")

          for sample in range(len(signals[idx].rev_cut_std_samples)):
            fileWs.write(str(signals[idx].rev_cut_std_samples[sample]))
            fileWs.write(" ")
          fileWs.write("\n")
