##
# @file SelectMenu.py
#
# @brief Defines the SelectMenu class.


from SignalDimensionalityReduction import SignalDimensionalityReduction
from SignalStandardization import SignalStandardization
from SignalAugmentation import SignalAugmentation
from LabelCreation import LabelCreation
from SetPartition import SetPartition


class SelectMenu():
    '''!
    Executes the corresponding main function.
    '''

    def __init__(self):
        '''! The SelectMenu clss initializer.
        '''
        pass

    def executeMenu(menu):
        '''! Executes the corresponding main function.

        @param menu Decide the main function to be executed.
        '''
        if menu == 1:
            instance = SignalDimensionalityReduction()
        elif menu == 2:
            instance = SignalStandardization()
        elif menu == 3:
            instance = SignalAugmentation()
        elif menu == 4:
            instance = LabelCreation()
        elif menu == 5:
            instance = SetPartition()

        instance.main()
