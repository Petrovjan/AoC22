field = open("day22a.txt").read().split("\n")
rord = open("day22b.txt").read()

size = len(field[0])
for k in range(len(field)):
    missing = size - len(field[k])
    field[k] = field[k] + " "*missing

for l in range(len(field) - 1, -1, -1):
    field[l] = field[l].replace(" ", "0")
    field[l] = field[l].replace(".", "1")
    field[l] = field[l].replace("#", "2")
    field[l] = [int(x) for x in field[l]]

orders = []

dir = [[0,1],[1,0],[0,-1],[-1,0]] #right, down, left, up

stp = 0
enp = 0
for p in range(len(rord)):
    if rord[p] == "L" or rord[p] == "R":
        enp = p
        orders.append(rord[stp:enp])
        stp = p
orders.append(rord[stp:])

cd = 0
ypos = 0
xpos = field[ypos].index(1)

def list_rindex(li, x):
    for n in range(len(li)-1,-1,-1):
        if li[n] == x:
            return n
    raise ValueError("{} is not in list".format(x))

def list_uindex(li, col, x):
    for n in range(len(li)):
        if li[n][col] == x:
            return n
    raise ValueError("{} is not in list".format(x))

def list_lindex(li, col, x):
    for n in range(len(li)-1,-1,-1):
        if li[n][col] == x:
            return n
    raise ValueError("{} is not in list".format(x))

for order in orders:
    if order[0] == "R":
        cd = (cd + 1) % 4
        ord = int(order[1:])
    elif order[0] == "L":
        cd = (cd - 1) % 4
        ord = int(order[1:])
    else:
        ord = int(order[:])
    for mv in range(ord):
        if field[(ypos + dir[cd][0])%len(field)][(xpos + dir[cd][1])%len(field[0])] == 1:
            ypos = (ypos + dir[cd][0])%len(field)
            xpos = (xpos + dir[cd][1])%len(field[0])
        elif field[(ypos + dir[cd][0])%len(field)][(xpos + dir[cd][1])%len(field[0])] == 2:
            break
        elif field[(ypos + dir[cd][0])%len(field)][(xpos + dir[cd][1])%len(field[0])] == 0:
            if cd == 0:
                ypos = ypos
                if field[ypos].index(1) > field[ypos].index(2):
                    break
                else:
                    xpos = field[ypos].index(1)
            elif cd == 2:
                ypos = ypos
                if list_rindex(field[ypos],2) < list_rindex(field[ypos],2):
                    break
                else:
                    xpos = list_rindex(field[ypos],1)
            elif cd == 1:
                xpos = xpos
                if list_uindex(field, xpos, 1) > list_uindex(field, xpos, 2):
                    break
                else:
                    ypos = list_uindex(field, xpos, 1)
            else:
                xpos = xpos
                if list_lindex(field, xpos, 1) < list_lindex(field, xpos, 2):
                    break
                else:
                    ypos = list_lindex(field, xpos, 1)
frow = ypos + 1
fcol = xpos + 1
fdir = cd
fsum = (1000*frow) + (4*fcol) + fdir
print("part1:", fsum)

cd = 0
ypos = 0
xpos = field[ypos].index(1)

chunk = 50

def getPotPosAndDir(ypos, xpos, cd):
    if cd == 1:
        if 0 <= xpos < chunk:
            pxpos = xpos + chunk*2
            pypos = 0
            cd = 1
        elif chunk <= xpos < chunk*2:
            pypos = xpos + chunk*2
            pxpos = chunk-1
            cd = 2
        elif chunk*2 <= xpos < chunk*3:
            pypos = xpos - chunk
            pxpos = (chunk*2)-1
            cd = 2

    elif cd == 3:
        if 0 <= xpos < chunk:
            pypos = xpos + chunk
            pxpos = chunk
            cd = 0
        elif chunk <= xpos < chunk*2:
            pypos = xpos + chunk*2
            pxpos = 0
            cd = 0
        elif chunk*2 <= xpos < chunk*3:
            pypos = (chunk*4)-1
            pxpos = xpos - chunk*2
            cd = 3

    elif cd == 0:
        if 0 <= ypos < chunk:
            pypos = (chunk*3) - 1 - ypos
            pxpos = (chunk*2)-1
            cd = 2
        elif chunk <= ypos < chunk*2:
            pypos = chunk-1
            pxpos = ypos + chunk
            cd = 3
        elif chunk*2 <= ypos < chunk*3:
            pypos = (chunk*3) - 1 - ypos
            pxpos = (chunk*3) - 1
            cd = 2
        elif chunk*3 <= ypos < chunk*4:
            pypos = (chunk*3) - 1
            pxpos = ypos - chunk*2
            cd = 3

    elif cd == 2:
        if 0 <= ypos < chunk:
            pypos = (chunk*3) - 1 - ypos
            pxpos = 0
            cd = 0
        elif chunk <= ypos < chunk*2:
            pypos = chunk*2
            pxpos = ypos - chunk
            cd = 1
        elif chunk*2 <= ypos < chunk*3:
            pypos = (chunk*3) - 1 - ypos
            pxpos = chunk
            cd = 0
        elif chunk*3 <= ypos < chunk*4:
            pypos = 0
            pxpos = ypos - chunk*2
            cd = 1

    return pypos, pxpos, cd


for order in orders:
    if order[0] == "R":
        cd = (cd + 1) % 4
        ord = int(order[1:])
    elif order[0] == "L":
        cd = (cd - 1) % 4
        ord = int(order[1:])
    else:
        ord = int(order[:])
    for mv in range(ord):
        if xpos + dir[cd][1] < 0 or xpos + dir[cd][1] >= len(field[0]) or ypos + dir[cd][0] < 0 or ypos + dir[cd][0] >= len(field) or field[(ypos + dir[cd][0])][(xpos + dir[cd][1])] == 0:
            oldcd = cd
            pypos, pxpos, cd = getPotPosAndDir(ypos, xpos, cd)
            if field[pypos][pxpos] == 1:
                ypos = pypos
                xpos = pxpos
            else:
                cd = oldcd
                break
        elif field[(ypos + dir[cd][0])][(xpos + dir[cd][1])] == 1:
            ypos = (ypos + dir[cd][0])
            xpos = (xpos + dir[cd][1])
        elif field[(ypos + dir[cd][0])][(xpos + dir[cd][1])] == 2:
            break

srow = ypos + 1
scol = xpos + 1
sdir = cd
ssum = (1000*srow) + (4*scol) + sdir
print("part2:", ssum)


assert getPotPosAndDir(0, 51, 3) == (151, 0, 0)
assert getPotPosAndDir(151, 0, 2) == (0, 51, 1)
assert getPotPosAndDir(0, 101, 3) == (199, 1, 3)
assert getPotPosAndDir(199, 1, 1) == (0, 101, 1)
assert getPotPosAndDir(1, 149, 0) == (148, 99, 2)
assert getPotPosAndDir(148, 99, 0) == (1, 149, 2)
assert getPotPosAndDir(49, 148, 1) == (98, 99, 2)
assert getPotPosAndDir(98, 99, 0) == (49, 148, 3)
assert getPotPosAndDir(149, 51, 1) == (151, 49, 2)
assert getPotPosAndDir(151, 49, 0) == (149, 51, 3)
assert getPotPosAndDir(1, 50, 2) == (148, 0, 0)
assert getPotPosAndDir(148, 0, 2) == (1, 50, 0)
assert getPotPosAndDir(98, 50, 2) == (100, 48, 1)
assert getPotPosAndDir(100, 48, 3) == (98, 50, 0)