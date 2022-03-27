

class InputMask:

    def no(self): return ""
    def letter_required(self): return "A"
    def letter_not_required(self): return "a"
    def letter_and_number_required(self): return "N"
    def letter_and_number_not_required(self): return "n"
    def non_blank_required(self): return "X"
    def non_blank_not_required(self): return "x"
    def number_required(self): return "9"
    def number_not_required(self): return "0"
    def hexa_required(self): return "H"
    def hexa_not_required(self): return "h"
