##
# @mainpage Preprocessor
#
# @brief This program is a sub-program that pre-processes the dataset into a
# form suitable for machine learning.
#
# @section contents_main Contents
# The program consists of  main functions.
# - SignalDimensionalityReduction
#
# @section dependencies_main Dependencies
# - configparser, numpy, tqdm

##
# @file main.py
#
# @brief This file is the first to run in a program, where it receives a menu
# number from the user and executes the corresponding main function.

from SelectMenu import SelectMenu


if __name__ == "__main__":
    while True:
        try:
            print("")
            print("1. Signal Dimensionality Reduction")
            print("2. Signal Standardization")
            print("3. Signal Augmentation")
            print("4. Label Creation")
            print("5. Set Partition")
            print("")
            print("Input Menu Number: ", end="")
            menu = int(input())
            if menu == 0 or menu > 5:
                raise ValueError(f"invalid menu number: {menu}")
            print("")
            break
        except Exception as ex:
            print(ex)

    instance = SelectMenu()
    SelectMenu.executeMenu(menu)
