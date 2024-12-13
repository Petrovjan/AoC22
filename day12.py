import string
raw = open("day12.txt").read().split("\n")
data = [list(x) for x in raw]


for i in range(len(data)):
    for j in range(len(data[0])):
        chVal = data[i][j]
        if chVal == "E":
            pass
        elif chVal == "S":
            pass
        else:
            data[i][j] = string.ascii_lowercase.index(chVal) + 1
print(data)

def findStart(data):
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == "S":
                return row, col

def findEnd(data):
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == "E":
                return row, col

scanned = []
Sx, Sy = findStart(data)
Ex, Ey = findEnd(data)
dist = dict()
dist[(Ex, Ey)] = 0
reached = {(Ex, Ey):0}
data[Sx][Sy] = 1
data[Ex][Ey] = 26

def run(Sx, Sy, reached, scanned, dist, data, part):
    while True:
        ch = min(reached, key=reached.get)
        reached.pop(ch)
        scanned.append(ch)

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            chN = (ch[0] + dx, ch[1] + dy)
            if 0 <= chN[0] < len(data) and 0 <= chN[1] < len(data[0]) and data[chN[0]][chN[1]] - data[ch[0]][ch[1]] >= -1:
                if chN in dist:
                    if dist[ch] + 1 <= dist[chN]:
                        dist[chN] = dist[ch] + 1
                else:
                    dist[chN] = dist[ch] + 1
                if chN not in scanned:
                    reached[chN] = dist[chN]
                height = data[chN[0]][chN[1]]
                if height == 1 and part == 2:
                    print(reached[chN])
                    return
        if (Sx, Sy) in reached:
            print(reached[(Sx, Sy)])
            return

run(Sx, Sy, reached, scanned, dist, data, 2)