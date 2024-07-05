import math


class calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        num = self.num**2
        print(f"square of number is {num}")

    def cube(self):
        num = self.num**3
        print(f"cube of number is {num}")

    def square_root(self):
        sqrt_number_math = math.sqrt(self.num)
        print(f"square root of number is {sqrt_number_math}")


cal = calculator(16)
cal.square()
cal.cube()
cal.square_root()
