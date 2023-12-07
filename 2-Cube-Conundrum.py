text_file = open("2-input.txt","r")
input = text_file.read().split('\n')


# Part 1 --

# which games are possible if there are only 12 red cubes, 13 green cubes, and 14 blue cubes
# return the sum of ID of the possible games
def possibleGames(input):
    res = 0
    possible = {'red': 12, 'green': 13, 'blue': 14}
    for i, game in enumerate(input):
        if not game:
            continue
        subsets = game.split(": ")[1].split("; ")
        for handfull in subsets:
            cubes = handfull.split(", ")
            for c in cubes:
                num, colour = c.split(" ")
                if possible[colour] < int(num):
                    break
            else:
                continue
            break
        else:
            res += i + 1
    return res

# print(possibleGames(input))

# Part 2 --

def fewestPossible(input):
    res = 0
    possible = {'red': 12, 'green': 13, 'blue': 14}
    for game in input:
        if not game:
            continue
        maxNums = {'red': 1, 'green': 1, 'blue': 1} 
        for handfull in game.split(": ")[1].split("; "):
            for c in handfull.split(", "):
                num, colour = c.split(" ")
                if maxNums[colour] < int(num):
                    maxNums[colour] = int(num)
        power = 1
        for c in maxNums:
            power = power * maxNums[c]
        res += power
    return res
    
test = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
# print(fewestPossible(test))
print(fewestPossible(input))