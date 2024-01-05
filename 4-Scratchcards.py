text_file = open("inputs/4-input.txt", "r")
input = text_file.read().split('\n')[:-1]

# Part 1 --

# scratchcard -> winning numbers | your numbers
# first matching number = 1 point, every after that doubles the points
# get the sum of each card's point


def scratchcardPoints(input):
    res = 0
    for card in input:
        curr_point = 0
        card = card.split(": ")[1]
        win, have = card.split(" | ")
        win = set(win.split())
        have = have.split()

        for num in have:
            if num in win:
                if curr_point:
                    curr_point *= 2
                else:
                    curr_point = 1
        res += curr_point

    return res


test = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
        'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
        'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
        'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
        'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
        'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']

print(scratchcardPoints(test))
print(scratchcardPoints(input))

# Part 2 --

# instead of the point system, you win copies of the scratchcards below the winning card equal to the number of matches
# calculate how many of total scratch cards you have!


def scratchcardCopies(input):
    copies = {}

    for i, card in enumerate(input):
        if i not in copies:
            copies[i] = 1
        else:
            copies[i] += 1

        card = card.split(": ")[1]
        win, have = card.split(" | ")
        win = set(win.split())
        have = have.split()

        count = 0
        for num in have:
            if num in win:
                count += 1
                if i + count not in copies:
                    copies[i + count] = copies[i]
                else:
                    copies[i + count] += copies[i]

    return sum(list(copies.values()))


print(scratchcardCopies(test))
print(scratchcardCopies(input))
