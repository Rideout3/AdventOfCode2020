def loadData(path):
    f = open(path)
    rawData = [[c,int(v)] for c,v in [x.strip('\n').split() for x in f.readlines()]]
    f.close()
    return rawData

def executeInstructions(instructions):
    executedInstructions = []
    accumulator = 0
    current = 0
    while current not in executedInstructions and current < len(instructions):
        inst,value = instructions[current]
        executedInstructions.append(current)
        if inst == 'jmp':
            current += value
        else:
            current += 1

        if inst == 'acc':
            accumulator += value
    
    return {'accumulator' : accumulator, 'executed' : executedInstructions, 'eof' : len(instructions) - 1 in executedInstructions}

instructions = loadData('Day8_HandheldHalting/Input')

#Part 1
print('Accumulator before looping = %i' % executeInstructions(instructions)['accumulator'])

#Part 2
def findCorruptLine(instructions):
    results = {'accumulator' : 0, 'executed' : [], 'eof' : False}
    for i,line in enumerate(instructions):
        if line[0] in ('nop','jmp'):
            testInstructions = instructions.copy()
            testInstructions[i] = ['nop' if line[0] == 'jmp' else 'jmp',line[1]]
            results = executeInstructions(testInstructions)
            if results['eof']:
                results['fixedLine'] = i
                return results

    results['fixedLine'] = -1
    return results

testResults = findCorruptLine(instructions)
print('Accumulator after successful fix at line %i: %i' % (testResults['fixedLine'], testResults['accumulator']))