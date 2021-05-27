##
# @file SelectMenu.py
#
# @brief Defines the SelectMenu class.


from Train import Train
from RuleBased import RuleBased


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
            instance = Train()
        elif menu == 3:
            instance = RuleBased()

        instance.main()
