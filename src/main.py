##
# @mainpage FM0-Decoder
#
# @brief This is a program that trains and tests the Signal-to-Signal
# translator model for decoding backscatter signals.
#
# @section contents_main Contents
# The program consists of three main functions.
# - Train
#  - Learn the Signal-to-Signal translator model.
# - Test
#  - Test the Signal-to-Signal translator model.
# - RuleBased
#  - Decode the signal with conventional rule-based decoding method.
#
# @section dependencies_main Dependencies
# - configparser, tqdm

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
            print("1. Train")
            print("3. Rule-Based Decoding")
            print("")
            print("Input Menu Number: ", end="")
            menu = int(input())
            if menu == 0 or menu > 3:
                raise ValueError(f"invalid menu number: {menu}")
            print("")
            break
        except Exception as ex:
            print(ex)

    instance = SelectMenu()
    SelectMenu.executeMenu(menu)
