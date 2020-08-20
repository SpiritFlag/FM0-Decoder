file_name_list_all = []
for a in ["100", "200", "300", "400"]:
    for b in ["0", "l100", "r100"]:
        for c in ["0", "45", "90", "135"]:
            file_name_list_all.append(a + "_" + b + "_" + c)

#file_name_list = []
#file_name_list = ["100_0_0"]
#file_name_list = ["100_0_0", "100_0_45", "100_0_90", "100_0_135"]
file_name_list = file_name_list_all

#file_name_list = ["010", "020", "030", "040", "050", "060", "070", "080", "090", "100"]
#file_name_list = ["045", "046", "047", "107", "108", "109", "143"]
#file_name_list = ["050", "060", "070", "080", "090", "100", "110", "120", "130", "140", "150", "160", "170", "190", "200"]



#n_signal = 500
n_signal = 6000
n_sample = 6850
n_cw = 50
n_bit = 50
n_half_bit = int(n_bit / 2)
n_bit_preamble = 6
n_bit_data = 128
n_extra = int(n_sample - n_bit * (n_bit_preamble + n_bit_data))
