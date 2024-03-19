import math

from square_generator.square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def e_squares(self, start, end):
        if start > end:
            raise Exception("The end of the range cannot be less than the start.")

        squares = [number * number for number in range(start, end)]
        return squares

    def cubes(self, start, end):
        cubes = [number ** 3 for number in range(start, end)]
        return cubes


starting_num = int(input("Enter the starting number: "))
ending_num = int(input("Enter the ending number: ")) + 1
cubic_generator = CubicGenerator()
print(cubic_generator.e_squares(starting_num, ending_num))
square_root = [math.sqrt(number) for number in cubic_generator.e_squares(starting_num, ending_num)]
print(square_root)
print(cubic_generator.cubes(starting_num, ending_num))
