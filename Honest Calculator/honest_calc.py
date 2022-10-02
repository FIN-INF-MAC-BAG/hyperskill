import sys


class data_collection:
    def __init__(self):
        self.memory = 0
        self.message()

    def message(self):
        number1, number2, calc = self.split()
        while self.check_digit(number1) and self.check_digit(number2):
            if self.check_string(calc):
                self.calculation(number1, number2, calc)
                sys.exit()
            else:
                print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
            self.message()

        print("Do you even know what numbers are? Stay focused!")
        self.message()

    def split(self):
        user_msg = input("Enter an equation \n")
        msg_splited = user_msg.split()
        number1 = msg_splited[0]
        number2 = msg_splited[2]py
        calc = msg_splited[1]
        return number1, number2, calc

    def check_digit(self, x):
        try:
            float(x)
            return True
        except ValueError:
            return False

    def check_string(self, x):

        try:
            str(x)
            return True
        except ValueError:
            return False

    def sum(self, number1, number2):
        return sum(number1, number2)

    def sub(self, number1, number2):
        return number1 - number2

    def multiply(self, number1, number2):
        return number1 * number2

    def divide(self, number1, number2):
        return number1 / number2

    def calculation(self, number1, number2, calc):

        functions = {
            "+": self.sum(number1, number2),
            "-": self.sub(number1, number2),
            "*": self.multiply(number1, number2),
            "/": self.divide(number1, number2),

        }
        if calc is not functions:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
            self.message()
        result = functions[calc]
        return result(number1, number2)



data_collection()
