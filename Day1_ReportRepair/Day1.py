from itertools import combinations

def loadNumbers(path):
    f = open(path)
    numbers = [int(x) for x in f.readlines()]
    f.close()
    return numbers

def findSumCombinations(input, count, target):
    return [pair for pair in combinations(input, count) if sum(pair) == target]

targetValue = 2020
numbers = loadNumbers('Day1_ReportRepair/Input')

#PART 1
validPairs = findSumCombinations(numbers, 2, targetValue)
if validPairs:
    pair = validPairs[0]
    print('Found Pair: %i,%i\nPair Product: %i' % (pair[0], pair[1], pair[0] * pair[1]))

#PART 2
validTriplets = findSumCombinations(numbers, 3, targetValue)
if validTriplets:
    trip = validTriplets[0]
    print('Found Triplet: %i,%i,%i\nTriplet Product: %i' % (trip[0], trip[1], trip[2], trip[0] * trip[1] * trip[2]))