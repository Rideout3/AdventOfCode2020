import itertools

def loadData(path):
    f = open(path)
    rawData = [x.strip('\n') for x in f.readlines()]
    f.close()
    return rawData

def buildDictionary(data):
    return {k:v for (k,v) in [getBagInfo(b) for b in data]}
        
def getStyle(inStyle):
    return inStyle.replace('bags','').replace('bag','').strip('.').strip()

def getBagCount(inBag):
    key = ' '.join([x for x in inBag.split() if not x.isdigit()])
    value = int(''.join([x for x in inBag.split() if x.isdigit()]))
    return getStyle(key),value

def getBagInfo(inBagData):
    key,rawvalue = inBagData.split('contain')
    value = {} if 'no other bag' in rawvalue else {k:v for (k,v) in [getBagCount(b) for b in rawvalue.split(',')]}
    return getStyle(key), value

def flatten(inList):
    return list(itertools.chain.from_iterable(inList))

def flattenDict(inList):
    out = {}
    for d in inList:
        for k,v in d.items():
            if k in out:
                out[k] += v
            else:
                out[k] = v
    return out

data = loadData('Day7_HandyHaversacks/Input')
bagDict = buildDictionary(data)

# Part 1
def getContainingBags(targetBag):
    return [k for k,v in bagDict.items() if targetBag in v.keys()]

def getNestedBags(targetBag):
    x = getContainingBags(targetBag)
    nested = []
    while len(x) > 0:
        nested.append(x)
        x = flatten([getContainingBags(y) for y in x])

    return list(set(flatten(nested)))

print('Shiny Gold Bags found nested in %i other bags' % len(getNestedBags('shiny gold')))

# Part 2
def getContainedBags(targetBag, data):
    x = data[targetBag]
    contained = []
    while len(x) > 0:
        contained.append(x)
        x = flattenDict([{ky : vy*v for ky,vy in data[k].items()} for k,v in x.items() if not v == ''])

    return contained

print('Shiny Gold Bag contains %i other bags' % sum([sum([v for k,v in x.items()]) for x in getContainedBags('shiny gold',bagDict)]))