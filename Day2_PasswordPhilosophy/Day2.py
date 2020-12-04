def parsePasswordData(data):
    values = data.split(' ')
    minMax = values[0].split('-')
    char = values[1].strip(':')
    password = values[2].strip('\n')
    return {"Min" : int(minMax[0]), "Max" : int(minMax[1]), "Char" : char, "Pass" : password}

def loadPasswords(path):
    f = open(path)
    values = [parsePasswordData(x) for x in f.readlines()]
    f.close()
    return values

passwords = loadPasswords('Day2_PasswordPhilosophy/Input')

#Part 1
def validPasswordsLegacy(passwords):
    return [x['Pass'] for x in passwords if x['Min'] <= charFrequency(x['Pass'], x['Char']) <= x['Max']]

def charFrequency(inputString, char):
    return len([c for c in inputString if c == char])

print('Number of valid passwords(legacy): %i' % len(validPasswordsLegacy(passwords)))

#Part 2
def validPasswords(passwords):
    return [x['Pass'] for x in passwords if validPositions(x['Pass'], x['Char'], (x['Min']-1, x['Max']-1))]

def validPositions(password, char, positions):
    vals = [password[x] == char for x in positions if x <= len(password)-1]
    return sum(vals) == 1

print('Number of valid passwords: %i' % len(validPasswords(passwords)))