##
# @file RuleBased.py
#
# @brief Defines the RuleBased class.


from Translator import Translator


class RuleBased(Translator):
    '''! Defines the procedures for decoding the signal with conventional
    rule-based decoding method.
    '''

    def __init__(self):
        '''! The RuleBased class initializer.
        '''
        super(RuleBased, self).__init__()

    def main(self):
        '''! Defines the main procedures.
        '''
        print("Step 1. Read signals and labels.")
        self.read_signal()
        self.read_label()
