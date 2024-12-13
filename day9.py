data = open("day9.txt").read().split("\n")

tailPath = {"1000:1000"}
TX = 1000
TY = 1000
HX = 1000
HY = 1000

def moveL(hx, hy, tx, ty):
    hx -= 1
    if abs(tx - hx) > 1:
        tx = hx + 1
        ty = hy
    return hx, hy, tx, ty

def moveR(hx, hy, tx, ty):
    hx += 1
    if abs(hx - tx) > 1:
        tx = hx - 1
        ty = hy
    return hx, hy, tx, ty

def moveU(hx, hy, tx, ty):
    hy += 1
    if abs(hy - ty) > 1:
        tx = hx
        ty = hy - 1
    return hx, hy, tx, ty

def moveD(hx, hy, tx, ty):
    hy -= 1
    if abs(hy - ty) > 1:
        tx = hx
        ty = hy + 1
    return hx, hy, tx, ty

for instr in data:
    rep = int(instr.split()[1])
    if instr.split()[0] == "L":
        while rep > 0:
            HX, HY, TX, TY = moveL(HX, HY, TX, TY)
            tailPath.add(str(TX) + ":" + str(TY))
            rep -= 1
    elif instr.split()[0] == "R":
        while rep > 0:
            HX, HY, TX, TY = moveR(HX, HY, TX, TY)
            tailPath.add(str(TX) + ":" + str(TY))
            rep -= 1
    elif instr.split()[0] == "U":
        while rep > 0:
            HX, HY, TX, TY = moveU(HX, HY, TX, TY)
            tailPath.add(str(TX) + ":" + str(TY))
            rep -= 1
    elif instr.split()[0] == "D":
        while rep > 0:
            HX, HY, TX, TY = moveD(HX, HY, TX, TY)
            tailPath.add(str(TX) + ":" + str(TY))
            rep -= 1

print(len(tailPath), 5619)

########

def follow(hx, hy, tx, ty):
    if abs(hy - ty) > 1:
        if abs(hx - tx) <= 1:
            tx = hx
        elif hx > tx:
            tx += 1
        else:
            tx -= 1

        if hy > ty:
            ty += 1
        else:
            ty -= 1
    elif abs(hx - tx) > 1:
        if abs(hy - ty) <= 1:
            ty = hy
        elif hy > ty:
            ty += 1
        else:
            ty -= 1

        if hx > tx:
            tx += 1
        else:
            tx -= 1
    return tx, ty

endpath = {"0:0"}

positions = [[0,0] for x in range(10)]

for instr in data:
    for rep in range(int(instr.split()[1])):
        if instr.split()[0] == "L":
            positions[0][0] -= 1
        elif instr.split()[0] == "R":
            positions[0][0] += 1
        elif instr.split()[0] == "U":
            positions[0][1] += 1
        elif instr.split()[0] == "D":
            positions[0][1] -= 1
        for knot in range(1, len(positions)):
            positions[knot][0], positions[knot][1] = follow(positions[knot - 1][0], positions[knot - 1][1], positions[knot][0], positions[knot][1])
        endpath.add(str(positions[9][0]) + ":" + str(positions[9][1]))

print(endpath)
print(len(endpath))

