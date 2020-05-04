import sys

from global_vars import *
from A_generate_RNindex.global_vars import *



def process(RN, postfix, n1, n2):
  try:
    file = open(output_path + postfix, "w")
    list = []
    for x in range(n_RNsignal):
      filex = open(output_path + "_RN" + str(x) + postfix, "w")
      start = int(x*n_RNset + n1)
      listx = RN[start:start+n2]
      list.extend(listx)
      listx.sort()
      listx = [str(i) for i in listx]
      filex.write(" ".join(listx))
      filex.close()
    list.sort()
    list = [str(i) for i in list]
    file.write(" ".join(list))
    file.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[A_generate_RNindex:process:" + str(tb.tb_lineno) + "] " + str(ex) + "\n\n")
