import math


class SquareGenerator:
    def e_squares(self, start, end):
        if start > end:
            raise Exception("The end of the range cannot be less than the start.")

        squares = [number * number for number in range(start, end)]
        return squares


starting_num = int(input("Enter the starting number: "))
ending_num = int(input("Enter the ending number: ")) + 1
square_generator = SquareGenerator()
square_root = [math.sqrt(number) for number in square_generator.e_squares(starting_num, ending_num)]
