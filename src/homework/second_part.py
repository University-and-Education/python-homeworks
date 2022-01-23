import first_part as math_functions


class Fraction:

    def __init__(self, top=0, bottom=0):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def input_data(self):
        print('Введите числитель')
        self.num = input()
        math_functions.str_to_int(self.num)
        print('Введите знаменатель')
        self.den = input()
        math_functions.str_to_int(self.den)
        print('Ваша дробь: ' + self.__str__())
