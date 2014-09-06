# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

# 1. Each column of the square contains
# each of the whole numbers from 1 to n exactly once.

# 2. Each row of the square contains each
# of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.


def inrange(num, rowlen):
    """
    Checks if the number is within a range from one to rowlen
    :param num: the number to check
    :param rowlen: the max range
    :return: True if within the range, False otherwise
    """
    return rowlen >= num > 0


def check_row(row):
    """
    Checks an array for Sudoku succes
    :param row: the array
    :return: True if all numbers are in range and occur only ones
    """
    usednum = []
    rowlen = len(row)

    for num in row:
        if num in usednum or not inrange(num, rowlen) or not isinstance(num, int):
            return False
        usednum.append(num)

    return True


def getcols(board):
    """
    Get all the columns on the board
    :param board: the Board
    :return: list of columnlists
    """
    collen = len(board[0])
    result = []
    colcounter = 0

    while colcounter < collen:
        rowcounter = 0
        col = []

        while rowcounter < collen:
            col.append(board[rowcounter][colcounter])
            rowcounter += 1
        result.append(col)
        colcounter += 1

    return result


def check_sudoku(board):
    """
    Checks if the board has a valid sudoku configuration
    :param board:
    :return: True if board is a valid sudoku config, otherwise False
    """
    for row in board:
        if not check_row(row):
            return False

    cols = getcols(board)

    for col in cols:
        if not check_row(col):
            return False

    return True


# tests
correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]

print check_sudoku(incorrect)
# >>> False

print check_sudoku(correct)
# >>> True

print check_sudoku(incorrect2)
# >>> False

print check_sudoku(incorrect3)
# >>> False

print check_sudoku(incorrect4)
# >>> False

print check_sudoku(incorrect5)
# >>> False


