def loadData(path):
    f = open(path)
    rawData = [x.strip('\n') for x in f.readlines()]
    f.close()
    breaks = [i for i, x in enumerate(rawData) if x == '']
    breaks.insert(0,0)
    breaks.append(len(rawData))
    return [rawData[breaks[x-1] : breaks[x]] for x in range(1,len(breaks))]
    #return [''.join(p) for p in [rawData[breaks[x-1] : breaks[x]] for x in range(1,len(breaks))]]
        
data = loadData('Day6_CustomCustoms/Input')

#Part 1
def getUniqueCounts(data):
    return [len(list(set(x))) for x in [''.join(p) for p in data]]

uniqueCount = getUniqueCounts(data)
print('The sum of the answers: %i' % sum(uniqueCount))

#Part 2
def getEveryoneCounts(data):
    return [len(set.intersection(*[set(y) for y in x if y != ''])) for x in data]

everyoneCount = getEveryoneCounts(data)
print('Number of questions everyone answered: %i' % sum(everyoneCount))