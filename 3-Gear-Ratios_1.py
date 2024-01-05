text_file = open("inputs/3-input.txt","r")
input = text_file.read().split('\n')[:-1]

# Part 1 --

# part number -> a number with any adjacent symbol (i.e. not ".")
# return sum of all part numbers

# helper to check if a number is a part number (check surrounding symbols)
def checkIfPartNumber(row, start_col, end_col, matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    for r in range(row - 1, row + 2):
        for c in range(start_col - 1, end_col + 2):
            if ROWS > r > 0 and COLS > c > 0 and not matrix[r][c].isdigit() and matrix[r][c] != '.':
                return True
    return False

def sumPartNumbers(input):
    res = 0
    ROWS, COLS = len(input), len(input[0])
    matrix =[list(line) for line in input]
    num, start = 0, 1
    for r in range(0, ROWS):
        num, start = 0, 0
        for c in range(0, COLS):
            if matrix[r][c].isdigit():
                num = (num * 10) + int(matrix[r][c])
                if c == COLS - 1:
                    res += num if checkIfPartNumber(r, start, c - 1, matrix) == True else 0
            else:
                if num != 0:
                    # found current number,  check surround to see if it's a "part number"
                    res += num if checkIfPartNumber(r, start, c - 1, matrix) == True else 0
                num, start = 0, c + 1
    return res

test = ["467..114..", "...*......", "..35..633.", "......#...", "617*......", 
        ".....+.58.", "..592.....", "......755.", "...$.*....", ".664.598.."]
print(sumPartNumbers(test))
print(sumPartNumbers(input))