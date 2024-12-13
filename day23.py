import operator
#check tiles around elf
#check positions is set order, create proposition
#check propositions for duplicates
#move elf
#move order of positions for all elves

#order - global
#positions shared
#two steps

elves = set() #{(ypos, xpos)}
propd = dict() #proposed positions - {1: (pyp, pxp)}
props = set()
nelves = set()

field = open("day23.txt").read().split("\n")
for i in range(len(field)):
    for j in range(len(field[0])):
        if field[i][j] == "#":
            elves.add((i, j))


udirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)] #0 - NW,1 - N,2 - NE,3 - E,4 - SE,5 - S,6 - SW,7 - W
# pdirs = [(-1, 0), (-1, 1), (-1, -1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, -1), (1, -1), (0, 1), (-1, 1), (1, 1)]
prdirs = [1, 0, 2, 5, 4, 6, 7, 0, 6, 3, 2, 4]
prmove = 0 #0 - N, 1 - S, 2 - W, 3 - E


round = 0
active = True
while active:
    active = False
    propd.clear()
    for elf in elves:
        nearTiles = []
        for d in udirs:
            nearTiles.append((elf[0] + d[0], elf[1] + d[1]))
        # print(nearTiles)

        nearElves = []
        for n in nearTiles:
            if n in elves:
                nearElves.append(0)
            else:
                nearElves.append(1)

        if nearElves == [1, 1, 1, 1, 1, 1, 1, 1]:
            continue

        # print(nearElves)

        for look in range(0, len(prdirs), 3):
            if nearElves[prdirs[look]] and nearElves[prdirs[look + 1]] and nearElves[prdirs[look + 2]]:
                move = (prmove + look // 3) % 4
                if move == 0:
                    potm = (elf[0] + udirs[1][0], elf[1] + udirs[1][1])
                elif move == 1:
                    potm = (elf[0] + udirs[5][0], elf[1] + udirs[5][1])
                elif move == 2:
                    potm = (elf[0] + udirs[7][0], elf[1] + udirs[7][1])
                elif move == 3:
                    potm = (elf[0] + udirs[3][0], elf[1] + udirs[3][1])
                if potm in propd.keys():
                    props.remove(propd[potm])
                    propd.pop(potm) #possible issue if 3 want to move to the same place
                else:
                    propd[potm] = elf
                    props.add(elf)
                break
        else:
            continue
    # print(props)
    nelves = elves.copy()
    for elv in elves:
        if elv in props:
            nelves.remove(elv)
            active = True

    for key in propd.keys():
        nelves.add(key)

    elves = nelves.copy()
    props.clear()


    for k in range(3): #move to end
        prdirs.append(prdirs.pop(0))
    prmove = (prmove + 1) % 4

    round += 1
    if round%100 == 0:
        print(round//100)

print(round)

# maxy = 5
# miny = 5
# maxx = 5
# minx = 5
# for val in elves:
#     if val[0] > maxy:
#         maxy = val[0]
#     if val[0] < miny:
#         miny = val[0]
#     if val[1] > maxx:
#         maxx = val[1]
#     if val[1] < minx:
#         minx = val[1]
# print(maxy, miny, maxx, minx, len(elves))
# print(((maxy - miny + 1) * (maxx - minx + 1)) - len(elves))
#
# grid = [["." for x in range(maxx - minx + 1)] for y in range(maxy - miny + 1)]
# for v in elves:
#     grid[v[0] - miny][v[1] - minx] = '#'
# print(grid)
