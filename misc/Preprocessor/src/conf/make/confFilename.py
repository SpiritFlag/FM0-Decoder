from conf import *

if exp_num == 1:
    file_name_list_all = []
    # for a in ["100", "200"]:
    # for a in ["100"]:
    for a in ["100", "200", "300", "400"]:
        for b in ["0", "l100", "r100"]:
            for c in ["0", "45", "90", "135"]:
                file_name_list_all.append(a + "_" + b + "_" + c)

    # file_name_list = ["100_0_0"]
    # file_name_list = ["100_0_0", "100_0_45", "100_0_90", "100_0_135"]
    file_name_list = file_name_list_all

    n_signal = 3000

elif exp_num == 2 or exp_num == 3:
    file_name_list_all = []
    for a in ["45", "47", "107", "109"]:
    # for a in ["109"]:
        for b in ["100", "200", "300"]:
            for c in ["0"]:
                for d in ["0", "45", "90", "135"]:
                    file_name_list_all.append(a + "_" + b + "_" + c + "_" + d)
    for a in ["45", "47"]:
        for b in ["100", "200", "300"]:
            for c in ["l100", "r100"]:
                for d in ["0", "45", "90", "135"]:
                    file_name_list_all.append(a + "_" + b + "_" + c + "_" + d)
    # file_name_list = ["109_100_0_0"]
    file_name_list = file_name_list_all

    n_signal = 500

elif exp_num == 4:
    file_name_list_all = []
    for x in range(100, 450, 10):
        file_name_list_all.append(str(x))

    # file_name_list = ["100"]
    file_name_list = file_name_list_all

    n_signal = 100

elif exp_num == 5:
    file_name_list = ["center", "left", "right", "100", "200", "300"]
    n_signal = 500

elif exp_num == 6:
    file_name_list_all = []
    for a in ["100", "200", "300", "400"]:
        for b in ["0", "l100", "r100"]:
            for c in ["0", "45", "90", "135"]:
                file_name_list_all.append(a + "_" + b + "_" + c)
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

    # file_name_list = ["45_100_0_0"]
    file_name_list = file_name_list_all

elif exp_num == 7:
    file_name_list_all = []
    for x in range(0, 180, 10):
        file_name_list_all.append(str(x))

    # file_name_list = ["0"]
    file_name_list = file_name_list_all

    n_signal = 100

elif exp_num == 8:
    file_name_list_all = []

    for a in range(1, 4):
        for b in range(1, 6):
            file_name_list_all.append(str(a) + "_" + str(b))

    file_name_list = file_name_list_all

elif exp_num == 9:
    file_name_list_all = []

    for a in range(2):
        for b in range(1, 7):
            file_name_list_all.append(str(a) + "_" + str(b))

    file_name_list = file_name_list_all

    n_signal = 500

elif exp_num == 10:
    file_name_list_all = []

    for a in range(1, 5):
        for b in range(1, 11):
            file_name_list_all.append(str(a) + "_" + str(b))

    file_name_list = file_name_list_all

    n_signal = 200

elif exp_num == 11:
    file_name_list = ["tag1", "tag2", "tag3", "tag4"]

    n_signal = 500


elif exp_num == 12:
    file_name_list_all = []
    # for a in ["100", "200"]:
    # for a in ["100"]:
    for a in ["100", "200", "300", "400"]:
        for b in ["0", "l100", "r100"]:
            for c in ["0", "45", "90", "135"]:
                file_name_list_all.append(a + "_" + b + "_" + c)

    # file_name_list = ["100_0_0"]
    # file_name_list = ["100_0_0", "100_0_45", "100_0_90", "100_0_135"]
    file_name_list = file_name_list_all

    n_signal = 3000
