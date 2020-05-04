from global_vars import *

output_path = "../data/B_RNindex/"

n_RNtrain = 640
n_RNvalidation = 160
n_RNtest = 200
n_RNset = n_RNtrain + n_RNvalidation + n_RNtest
n_RNsignal = int(n_signal/n_RNset)
