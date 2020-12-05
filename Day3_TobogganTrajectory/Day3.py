import math

def loadGeometry(path):
    f = open(path)
    values = [[int(y == '#') for y in x if y in '.#'] for x in f.readlines()]
    f.close()
    return values

def traverseCollisions(geometry, x, y):
    pos = 0
    trees = []
    for i in range(y, len(geometry), y):
        pos += x
        j = pos % len(geometry[i])
        trees.append(geometry[i][j])
    return trees

geometry = loadGeometry('Day3_TobogganTrajectory/input')

#Part 1
print('Collisions at angle(3,1): %i' % sum(traverseCollisions(geometry, 3, 1)))

#Part 2
Angles = [(1,1),(3,1),(5,1),(7,1),(1,2)]
print('Product of collisions at angles: %i' % math.prod([sum(traverseCollisions(geometry, x, y)) for x,y in Angles]))