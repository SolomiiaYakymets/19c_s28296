class SquareGenerator:
    def e_squares(self, start, end):
        if start > end:
            raise Exception("The end of the range cannot be less than the start.")

        squares = [number * number for number in range(start, end)]
        return squares
