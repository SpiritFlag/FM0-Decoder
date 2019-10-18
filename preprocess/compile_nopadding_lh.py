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
        fileR = open(folder_pathW + file_name + "_a", "r")
        fileW = open(folder_pathW + file_name + "_alh", "w")

        for n in tqdm(range(size), desc=file_name, ncols=80, unit="signal"):
          line = fileR.readline().rstrip("\n")
          if not line: break
          data = [int(i) for i in line]

          conv = []
          level = -1
          for sample in data:
            if sample == 1:
              conv.append(level)
              conv.append(level)
              level *= -1
            else:
              conv.append(level)
              conv.append(level * -1)

          for sample in conv:
            if sample == -1:
              fileW.write("0")
            else:
              fileW.write("1")
          fileW.write("\n")
