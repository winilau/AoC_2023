text_file = open("inputs/3-input.txt", "r")
input = text_file.read().split('\n')[:-1]

# Part 2 --

# a gear is any * symbol that is adjacent to exactly two part numbers
# gear ratio is the result of multiplying those two numbers together

# helper to get gear ration from * symbol


def getGearRatio(symbol_row, symbol_col, matrix):
    count, gearRatio = 0, 0
    num_locations = []
    ROWS, COLS = len(matrix), len(matrix[0])
    for r in range(symbol_row - 1, symbol_row + 2):
        for c in range(symbol_col - 1, symbol_col + 2):
            if ROWS > r >= 0 and COLS > c >= 0 and matrix[r][c].isdigit() and (c < symbol_col or (c >= symbol_col and not matrix[r][c-1].isdigit())):
                num_locations.append((r, c))
                count += 1
    if count == 2:
        for r, c in num_locations:
            start = c
            while start >= 0 and matrix[r][start].isdigit():
                start -= 1

            start += 1
            num = 0
            while start < COLS and matrix[r][start].isdigit():
                num = num * 10 + int(matrix[r][start])
                start += 1
            gearRatio = num if gearRatio == 0 else num * gearRatio

    return gearRatio


def sumGearRation(input):
    res = 0
    ROWS, COLS = len(input), len(input[0])
    matrix = [list(line) for line in input]
    for r in range(0, ROWS):
        for c in range(0, COLS):
            if matrix[r][c] == '*':
                res += getGearRatio(r, c, matrix)
    return res


test = ["467..114..", "...*......", "..35..633.", "......#...", "617*......",
        ".....+.58.", "..592.....", "......755.", "...$.*....", ".664.598.."]
print(sumGearRation(test))
print(sumGearRation(input))
