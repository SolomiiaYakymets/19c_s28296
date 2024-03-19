import math

from square_generator.square_generator import SquareGenerator

starting_num = int(input("Enter the starting number: "))
ending_num = int(input("Enter the ending number: ")) + 1
square_generator = SquareGenerator()
square_root = [math.sqrt(number) for number in square_generator.e_squares(starting_num, ending_num)]
