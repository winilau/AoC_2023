input = open("inputs/5-input.txt", "r").read().split('\n')[:-1]
test_input = open("inputs/5-test.txt", "r").read().split('\n')[:-1]

# Part 1 --

# Given a list of seeds and multiple maps
# any source number that aren't mapped corresponds to the same destination number
# FInd the lowest location number


def findNextDestinations(prev, seeds, line):
    des, source, range = int(line.split()[0]), int(
        line.split()[1]), int(line.split()[2])
    for i, seed in enumerate(seeds):
        # if seed is in range of the map, change seed to the mapped destination
        if prev[i] == seed and source <= seed <= source + range:
            seeds[i] = des + (seed - source)
    return seeds  # if seed was never in range of any maps, it remains the same


def findLowestLocation(input):
    seeds = [int(n) for n in input[0].split(": ")[1].split()]
    for i in range(1, len(input)):
        line = input[i]
        if not line:
            prev = seeds.copy()  # keep track of prev iteration of seeds
            continue
        if line[0].isdigit():
            seeds = findNextDestinations(prev, seeds, line)
    return min(seeds)


# print(findLowestLocation(test_input))
# print(findLowestLocation(input))

# Part 2 --

# Instaed of individual seeds, teh seeds line actually stands for ranges of seeds
# i.e. [79, 14, 55, 13] would be 2 ranges of seeds being 79 - (79 + 14) and 55 - (55 + 13)
# issue would be run time, make cache for each map?


def findLocation(seed, input, cache):
    for line in input:
        if not line:
            prev = seed  # keep track of prev iteration of seed
            continue
        if not line[0].isdigit():
            if line == "seed-to-soil map:":
                curr_map = "seed-to-soil"
            elif line == "soil-to-fertilizer map:":
                curr_map = "soil-to-fertilizer map:"
            elif line == "fertilizer-to-water map:":
                curr_map = "fertilizer-to-water"
            elif line == "water-to-light map:":
                curr_map = "water-to-light"
            elif line == "light-to-temperature map:":
                curr_map = "light-to-temperature"
            elif line == "temperature-to-humidity map:":
                curr_map = "temperature-to-humidity"
            elif line == "humidity-to-location map:":
                curr_map = "humidity-to-location"
        else:
            des, source, range = int(line.split()[0]), int(
                line.split()[1]), int(line.split()[2])
            # if seed is in range of the map, change seed to the mapped destination
            if prev == seed and source <= seed <= source + range:
                seed = des + (seed - source)
    return seed  # if seed was never in range of any maps, it remains the same


def findLowestLocationTwo(input):
    first_line = input[0].split(": ")[1].split()
    ranges = [(int(first_line[i]), int(first_line[i+1]))
              for i in range(0, len(first_line), 2)]
    seeds, cache = {}, {}
    input = input[1:]
    for i in range(1, len(input)):
        visited = set()
        for start, seed_range in ranges:
            for i in range(seed_range):
                seed = start + i
                if seed in visited:
                    continue
                if seed not in seeds:
                    visited.add(seed)
                    seeds[seed] = findLocation(seed, input, cache)
    print(seeds)
    return min(seeds.values())


print(findLowestLocationTwo(test_input))
# print(findLowestLocationTwo(input))
