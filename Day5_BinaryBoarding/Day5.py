import math
from itertools import combinations

def loadBoardingPasses(path):
    f = open(path)
    values = [x for x in f.readlines()]
    f.close()
    return values

def findValue(size,traverse):
    power = math.log2(size)
    if not power.is_integer() or not power == len(traverse):
        print('size not base 2 or traverse not long enough')
        return -1

    min = 0
    max = size-1
    for i,x in enumerate(traverse):
        if x:
            min = min + (size / (math.pow(2,i+1)))
        else:
            max = max - (size / (math.pow(2,i+1)))
    
    if min == max:
        return min
    return -1

def getBinary(data, char0, char1):
    return [0 if x == char0 else 1 for x in data if x in [char0, char1]]

def getId(row, column):
    return int(row * 8 + column)

def getIdFromCode(code):
    return getId(findValue(128,getBinary(code,'F','B')), findValue(8,getBinary(code,'L','R')))

def findFreeSeat(ids):
    return [sum(pair)/2 for pair in combinations(ids, 2) if abs(pair[0]-pair[1]) == 2 and sum(pair)/2 not in ids]

passes = loadBoardingPasses('Day5_BinaryBoarding/Input')
ids = [getIdFromCode(x) for x in passes]

#Part 1
print('Max id found: %i' % max(ids))

#Part 2
print('Free seat found: %i' % findFreeSeat(ids)[0])