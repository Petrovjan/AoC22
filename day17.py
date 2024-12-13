import copy
flow = str(open("day17.txt").read().replace("\n", ""))
print(flow)

arena =  [[1,3,3,3,3,3,3,3,1]]
line =   [[1,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,1], [1,0,0,2,2,2,2,0,1]]
cross =  [[1,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,1], [1,0,0,0,2,0,0,0,1], [1,0,0,2,2,2,0,0,1], [1,0,0,0,2,0,0,0,1]]
revl =   [[1,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,1], [1,0,0,2,2,2,0,0,1], [1,0,0,0,0,2,0,0,1], [1,0,0,0,0,2,0,0,1]]
vert =   [[1,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,1], [1,0,0,2,0,0,0,0,1], [1,0,0,2,0,0,0,0,1], [1,0,0,2,0,0,0,0,1], [1,0,0,2,0,0,0,0,1]]
square = [[1,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,1], [1,0,0,2,2,0,0,0,1], [1,0,0,2,2,0,0,0,1]]

items = [line, cross, revl, vert, square]

def canBePushed(push, itemno, arena, bottom):
    for fl in range(bottom, len(arena)):
        if 2 not in arena[fl]:
            continue
        else:
            botleft = arena[fl].index(2)
            if itemno == 0: #line
                if push == ">" and arena[fl][botleft+4] != 0:
                    return False
                elif push == "<" and arena[fl][botleft-1] != 0:
                    return False
                return True
            elif itemno == 1: #cross
                if push == ">":
                    if arena[fl][botleft+1] != 0 or arena[fl+1][botleft+2] != 0 or arena[fl+2][botleft+1] != 0:
                        return False
                elif push == "<":
                    if arena[fl][botleft-1] != 0 or arena[fl+1][botleft-2] != 0 or arena[fl+2][botleft-1] != 0:
                        return False
                return True
            elif itemno == 2: #revl
                if push == ">":
                    if arena[fl][botleft+3] != 0 or arena[fl+1][botleft+3] != 0 or arena[fl+2][botleft+3] != 0:
                        return False
                elif push == "<":
                    if arena[fl][botleft-1] != 0 or arena[fl+1][botleft+1] != 0 or arena[fl+2][botleft+1] != 0:
                        return False
                return True
            elif itemno == 3: #vert
                if push == ">":
                    if arena[fl][botleft+1] != 0 or arena[fl+1][botleft+1] != 0 or arena[fl+2][botleft+1] != 0 or arena[fl+3][botleft+1] != 0:
                        return False
                elif push == "<":
                    if arena[fl][botleft-1] != 0 or arena[fl+1][botleft-1] != 0 or arena[fl+2][botleft-1] != 0 or arena[fl+3][botleft-1] != 0:
                        return False
                return True
            elif itemno == 4: #square
                if push == ">":
                    if arena[fl][botleft+2] != 0 or arena[fl+1][botleft+2] != 0:
                        return False
                elif push == "<":
                    if arena[fl][botleft-1] != 0 or arena[fl+1][botleft-1] != 0:
                        return False
                return True
    print("error cBP")

def canFall(itemno, arena, bottom):
    for fl in range(bottom, len(arena)):
        if 2 not in arena[fl]:
            continue
        else:
            botleft = arena[fl].index(2)
            if itemno == 0: #line
                if arena[fl-1][botleft] != 0 or arena[fl-1][botleft+1] != 0 or arena[fl-1][botleft+2] != 0 or arena[fl-1][botleft+3] != 0:
                    return False
                else:
                    return True
            elif itemno == 1: #cross
                if arena[fl-1][botleft] != 0 or arena[fl][botleft-1] != 0 or arena[fl][botleft+1] != 0:
                    return False
                else:
                    return True
            elif itemno == 2: #revl
                if arena[fl-1][botleft] != 0 or arena[fl-1][botleft+1] != 0 or arena[fl-1][botleft+2] != 0:
                    return False
                else:
                    return True
            elif itemno == 3: #vert
                if arena[fl-1][botleft] != 0:
                    return False
                else:
                    return True
            elif itemno == 4: #square
                if arena[fl-1][botleft] != 0 or arena[fl-1][botleft+1] != 0:
                    return False
                else:
                    return True
    print("error cF")


rocks = 0
steps = 0
bottom = 0
newbottom = 0
pushno = 0
cache = dict()
uniqueItem = 0
uniquePush = 0
found = 0
target = 2022 #change to select between part1/part2
totalHeight = -1
while True:
    if rocks == target:
        break

    #spawn rock
    itemno = rocks % 5
    rocks += 1
    newitem = copy.deepcopy(items[itemno])
    arena = arena + newitem

    #find current bottom
    for fl in range(len(arena) -1, bottom - 1, -1):
        if arena[fl] == [1,3,3,3,3,3,3,3,1]:
            bottom = fl
            if newbottom != bottom:
                newbottom = bottom
                if (itemno, pushno) in cache.keys() and found == 0:
                    uniqueItem = itemno
                    uniquePush = pushno
                    origRocks = rocks
                    origHeight = len(arena)-1
                    found += 1
                cache[itemno, pushno] = (rocks, len(arena)-1)
                if found >=1 and itemno == uniqueItem and pushno == uniquePush:
                    found += 1
                    if found == 3:
                        repRocks = cache[uniqueItem, uniquePush][0] - origRocks
                        repHeight = cache[uniqueItem, uniquePush][1] - origHeight
                        while (rocks + repRocks) < target:
                            rocks += repRocks
                            totalHeight += repHeight
            break

    #try to move sideways, then move down
    moving = True
    while moving:
        pushno = steps % len(flow)
        push = flow[pushno]
        steps += 1
        #push left/right
        pass
        if canBePushed(push, itemno, arena, bottom):
            for fl in range(bottom, len(arena)):
                if 2 not in arena[fl]:
                    continue
                else:
                    if push == ">":
                        for c in range(len(arena[fl]) - 1, -1, -1):
                            if arena[fl][c] == 2:
                                arena[fl][c+1] = 2
                                arena[fl][c] = 0
                    elif push == "<":
                        for c in range(len(arena[fl])):
                            if arena[fl][c] == 2:
                                arena[fl][c-1] = 2
                                arena[fl][c] = 0
        #fall
        if canFall(itemno, arena, bottom):
            for fl in range(bottom, len(arena)):
                if 2 not in arena[fl]:
                    continue
                else:
                    for c in range(len(arena[fl])):
                        if arena[fl][c] == 2:
                            arena[fl-1][c] = 2
                            arena[fl][c] = 0
        else:
            moving = False
            for fl in range(bottom, len(arena)):
                if 2 not in arena[fl]:
                    continue
                else:
                    for c in range(len(arena[fl])):
                        if arena[fl][c] == 2:
                            arena[fl][c] = 3
    #clean top
    while arena[-1] == [1,0,0,0,0,0,0,0,1]:
        arena.pop()
print("p2: ", len(arena) + totalHeight)