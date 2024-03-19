import math


class SquareGenerator:
    def e_squares(self, start, end):
        squares = [number * number for number in range(start, end)]
        return squares


starting_num = int(input("Enter the starting number: "))
ending_num = int(input("Enter the ending number: "))
square_generator = SquareGenerator()
square_root = [math.sqrt(number) for number in square_generator.e_squares(starting_num, ending_num)]