# the calibration value can be found by combining the first digit and the last digit
# find the sum of each calibration value of each line
# e.g. 1abc2 -> 12 treb7uchet -> 77

text_file = open("1-input.txt","r")
input = text_file.read().split('\n')

# part 1
def findCalibrationSum(arr):
    res = 0
    for line in arr:
        first, last = -1, -1
        for i in range(len(line)):
            if first > -1 and last > -1:
                continue
            if first == -1 and line[i].isdigit():
                first = int(line[i])
                res += first * 10
            if last == - 1 and line[len(line) - 1 - i].isdigit():
                last = int(line[len(line) - 1 - i])
                res += last        
    return res

# test = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
# print(findCalibrationSum(test))
print(findCalibrationSum(input))

# part 2
def converDigits(arr):
    digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'}

    for n,line in enumerate(arr):
        i = 0
        newLine = ""
        for i in range(len(line)):
            if i+3 <= len(line) and line[i:i+3] in digits:
                newLine += digits[line[i:i+3]]
            elif i+4 <= len(line) and line[i:i+4] in digits:
                newLine += digits[line[i:i+4]]
            elif i+5 <= len(line) and line[i:i+5] in digits:
                newLine += digits[line[i:i+5]]
            else:
                newLine += line[i]
        arr[n] = newLine
    return arr

# test = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
# print(findCalibrationSum(converDigits(test)))
print(findCalibrationSum(converDigits(input)))
