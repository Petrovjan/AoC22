import copy
field = open("day24.txt").read().split("\n")
field = [list(x) for x in field]
print(field)

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)] #R, L, U, D

storms = dict()

for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] == '>':
            storms[(i, j, 1)] = 0
        elif field[i][j] == '<':
            storms[(i, j, 1)] = 1
        elif field[i][j] == '^':
            storms[(i, j, 1)] = 2
        elif field[i][j] == 'v':
            storms[(i, j, 1)] = 3

print(storms)

def moveStorms(storms: dict, fW, fH) -> dict:
    newStorms = dict()
    for key, val in storms.items():
        if 0 < key[0] + dirs[val][0] < fH - 1 and 0 < key[1] + dirs[val][1] < fW - 1:
            if (key[0] + dirs[val][0], key[1] + dirs[val][1], 3) in newStorms.keys():
                newStorms[(key[0] + dirs[val][0], key[1] + dirs[val][1], 4)] = val
            elif (key[0] + dirs[val][0], key[1] + dirs[val][1], 2) in newStorms.keys():
                newStorms[(key[0] + dirs[val][0], key[1] + dirs[val][1], 3)] = val
            elif (key[0] + dirs[val][0], key[1] + dirs[val][1], 1) in newStorms.keys():
                newStorms[(key[0] + dirs[val][0], key[1] + dirs[val][1], 2)] = val
            else:
                newStorms[(key[0] + dirs[val][0], key[1] + dirs[val][1], 1)] = val
        elif 0 < key[0] + dirs[val][0] < fH - 1: #kolize vpravo nebo vlevo
            if (key[0], (key[1] + 2*dirs[val][1])%(fW-1), 3) in newStorms.keys():
                newStorms[(key[0], (key[1] + 2*dirs[val][1])%(fW-1), 4)] = val
            elif (key[0], (key[1] + 2*dirs[val][1])%(fW-1), 2) in newStorms.keys():
                newStorms[(key[0], (key[1] + 2*dirs[val][1])%(fW-1), 3)] = val
            elif (key[0], (key[1] + 2*dirs[val][1])%(fW-1), 1) in newStorms.keys():
                newStorms[(key[0], (key[1] + 2*dirs[val][1])%(fW-1), 2)] = val
            else:
                newStorms[(key[0], (key[1] + 2*dirs[val][1])%(fW-1), 1)] = val
        elif 0 < key[1] + dirs[val][1] < fW - 1: #kolize nahore ci dole
            if ((key[0] + 2*dirs[val][0])%(fH-1), key[1], 3) in newStorms.keys():
                newStorms[((key[0] + 2*dirs[val][0])%(fH-1), key[1], 4)] = val
            elif ((key[0] + 2*dirs[val][0])%(fH-1), key[1], 2) in newStorms.keys():
                newStorms[((key[0] + 2*dirs[val][0])%(fH-1), key[1], 3)] = val
            elif ((key[0] + 2*dirs[val][0])%(fH-1), key[1], 1) in newStorms.keys():
                newStorms[((key[0] + 2*dirs[val][0])%(fH-1), key[1], 2)] = val
            else:
                newStorms[((key[0] + 2*dirs[val][0])%(fH-1), key[1], 1)] = val
        else:
            print("error")
    return newStorms

paths = {(0, 1)}
fWidth = len(field[0])
fHeight = len(field)
endX = fWidth - 2
endY = fHeight - 1
newpaths = set()
minute = 0
while True:
    if (endY, endX) in paths:
        break
    minute += 1
    storms = moveStorms(storms, fWidth, fHeight)
    newpaths.clear()
    for path in paths:
        al1 = path + (1,)
        al2 = path + (2,)
        al3 = path + (3,)
        al4 = path + (4,)
        if al1 not in storms.keys() and al2 not in storms.keys() and al3 not in storms.keys() and al4 not in storms.keys():
            newpaths.add(path) #zustat na miste
        moves = []
        for dir in dirs:
            moves.append((path[0] + dir[0], path[1] + dir[1]))
        for move in moves:
            if field[move[0]][move[1]] == '#' or move[0] == -1:
                continue
            al1 = move + (1,)
            al2 = move + (2,)
            al3 = move + (3,)
            al4 = move + (4,)
            if al1 not in storms.keys() and al2 not in storms.keys() and al3 not in storms.keys() and al4 not in storms.keys():
                newpaths.add(move) #pohnout se
    paths = newpaths.copy()

print("tam:",minute) #delka cesty tam

paths = {(endY, endX)}

while True:
    if (0, 1) in paths:
        break
    minute += 1
    storms = moveStorms(storms, fWidth, fHeight)
    newpaths.clear()
    for path in paths:
        al1 = path + (1,)
        al2 = path + (2,)
        al3 = path + (3,)
        al4 = path + (4,)
        if al1 not in storms.keys() and al2 not in storms.keys() and al3 not in storms.keys() and al4 not in storms.keys():
            newpaths.add(path) #zustat na miste
        moves = []
        for dir in dirs:
            moves.append((path[0] + dir[0], path[1] + dir[1]))
        for move in moves:
            if move[0] == fHeight or field[move[0]][move[1]] == '#' or move[0] == -1:
                continue
            al1 = move + (1,)
            al2 = move + (2,)
            al3 = move + (3,)
            al4 = move + (4,)
            if al1 not in storms.keys() and al2 not in storms.keys() and al3 not in storms.keys() and al4 not in storms.keys():
                newpaths.add(move) #pohnout se
    paths = newpaths.copy()

print("tam a zpet:", minute)
paths = {(0, 1)}

while True:
    if (endY, endX) in paths:
        break
    minute += 1
    storms = moveStorms(storms, fWidth, fHeight)
    newpaths.clear()
    for path in paths:
        al1 = path + (1,)
        al2 = path + (2,)
        al3 = path + (3,)
        al4 = path + (4,)
        if al1 not in storms.keys() and al2 not in storms.keys() and al3 not in storms.keys() and al4 not in storms.keys():
            newpaths.add(path) #zustat na miste
        moves = []
        for dir in dirs:
            moves.append((path[0] + dir[0], path[1] + dir[1]))
        for move in moves:
            if field[move[0]][move[1]] == '#' or move[0] == -1:
                continue
            al1 = move + (1,)
            al2 = move + (2,)
            al3 = move + (3,)
            al4 = move + (4,)
            if al1 not in storms.keys() and al2 not in storms.keys() and al3 not in storms.keys() and al4 not in storms.keys():
                newpaths.add(move) #pohnout se
    paths = newpaths.copy()

print("tam, zpet a tam:", minute)
