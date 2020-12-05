import string

def loadPassports(path):
    f = open(path)
    rawData = [x.strip('\n') for x in f.readlines()]
    f.close()
    breaks = [i for i, x in enumerate(rawData) if x == '']
    breaks.insert(0,0)
    breaks.append(len(rawData))
    return [parsePassport(p) for p in [rawData[breaks[x-1] : breaks[x]] for x in range(1,len(breaks))]]

def parsePassport(data):
    passDict = {'byr' : '', 'iyr' : '', 'eyr' : '', 'hgt' : '', 'hcl' : '', 'ecl' : '', 'pid' : '', 'cid' : ''}
    stream = [z for y in (x.split(' ') for x in data) for z in y if z != '']
    for d in stream:
        keyVal = d.split(':')
        passDict[keyVal[0]] = keyVal[1]
    return passDict

passports = loadPassports('Day4_PassportProcessing/input')

# Part 1
def validatePassportFields(passport, ignoreFields=[]):
    requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
    validFields = [passport[field] != '' for field in requiredFields if field not in ignoreFields]
    return all(validFields)

print("Valid passports by field: %i" % sum([validatePassportFields(p, ignoreFields=['cid']) for p in passports]))

# Part 2
def validatePassportData(passport):
    byr = 1920 <= int(passport['byr']) <= 2002
    iyr = 2010 <= int(passport['iyr']) <= 2020
    eyr = 2020 <= int(passport['eyr']) <= 2030
    hgt = (passport['hgt'].endswith('cm') and 150 <= int(passport['hgt'][:-2]) <= 193) or (passport['hgt'].endswith('in') and 59 <= int(passport['hgt'][:-2]) <= 76)
    hcl = len(passport['hcl']) == 7 and passport['hcl'][0] == '#' and all([c in string.hexdigits for c in passport['hcl'][1:]])
    ecl = passport['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']
    pid = len(passport['pid']) == 9 and passport['pid'].isdigit()
    
    return all([byr,iyr,eyr,hgt,hcl,ecl,pid])

print('Valid passports by data: %i' % sum([validatePassportData(p) for p in passports if validatePassportFields(p, ignoreFields=['cid'])]))