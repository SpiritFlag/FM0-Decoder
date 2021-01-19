data_path = "../data/"
exp_num = 1
if exp_num < 10:
  data_path_prefix = data_path + "exp0" + str(exp_num) + "_"
else:
  data_path_prefix = data_path + "exp" + str(exp_num) + "_"



if exp_num == 1:
  file_name_list_all = []
  for a in ["100", "200", "300", "400"]:
      for b in ["0", "l100", "r100"]:
          for c in ["0", "45", "90", "135"]:
              file_name_list_all.append(a + "_" + b + "_" + c)

  #file_name_list = ["100_0_0"]
  file_name_list = file_name_list_all

  n_signal = 3000

elif exp_num == 2 or exp_num == 3 or exp_num == 6:
  file_name_list_all = []
  for a in ["45", "47", "107", "109"]:
    for b in ["100", "200", "300"]:
      for c in ["0"]:
        for d in ["0", "45", "90", "135"]:
          file_name_list_all.append(a + "_" + b + "_" + c + "_" + d)
  for a in ["45", "47"]:
    for b in ["100", "200", "300"]:
      for c in ["l100", "r100"]:
        for d in ["0", "45", "90", "135"]:
          file_name_list_all.append(a + "_" + b + "_" + c + "_" + d)

  #file_name_list = ["45_100_0_0"]
  file_name_list = file_name_list_all

  n_signal = 500

elif exp_num == 4:
  file_name_list_all = []
  for x in range(100, 450, 10):
    file_name_list_all.append(str(x))

  #file_name_list = ["100"]
  file_name_list = file_name_list_all

  n_signal = 100

elif exp_num == 5:
  file_name_list = ["center", "left", "right", "100", "200", "300"]
  n_signal = 500



n_sample = 7300
n_cw = 50
n_bit = 50
n_half_bit = int(n_bit / 2)
n_bit_preamble = 6
n_bit_data = 128
n_extra = int(n_sample - n_bit * (n_bit_preamble + n_bit_data))
