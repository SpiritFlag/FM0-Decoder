import sys
import matplotlib.pyplot as plt

rep = 25



if __name__ == "__main__":
  try:
    file = open("../test", "r")
    line = file.readline().rstrip(" \n").split(" ")
    line = ([int(i) for i in line])
    file.close()


    plt.hist(line, bins=range(0, rep+2, 1), alpha=0.5, rwidth=0.8, label="hist")
    #plt.show()
    plt.savefig("../fig.png", dpi=300)
    plt.close()

  except Exception as ex:
    _, _, tb = sys.exc_info()
    print("[main:" + str(tb.tb_lineno) + "] " + str(ex))
