raw = open("day14.txt").read().split("\n")
data = [x.split(' -> ') for x in raw]
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = [int(data[i][j].split(',')[0]), int(data[i][j].split(',')[1])]

print(data)

cave = [[0 for y in range(1000)] for x in range(200)]

for i in range(len(data)):
    for j in range(0, len(data[i]) - 1):
        if data[i][j][0] == data[i][j+1][0]: #498,4 -> 498,6
            star = data[i][j][1]
            endr = data[i][j+1][1]
            col = data[i][j][0]
            for r in range(min(star, endr), max(star, endr) + 1):
                cave[r][col] = 1
        elif data[i][j][1] == data[i][j+1][1]: #503,4 -> 502,4
            stac = data[i][j][0]
            endc = data[i][j+1][0]
            row = data[i][j][1]
            for c in range(min(stac, endc), max(stac, endc) + 1):
                cave[row][c] = 1

for s in range(len(cave) -1, -1, -1):
    if sum(cave[s]) > 0:
        bottom = s+2
        for t in range(len(cave[bottom])):
            cave[bottom][t] = 1
        break

# sandFinPos = []
# sandR = 0
# sandC = 500
# while True:
#     if sandR >= bottom - 1:
#         break
#     if cave[sandR + 1][sandC] == 0:
#         sandR += 1
#     elif cave[sandR + 1][sandC - 1] == 0:
#         sandR += 1
#         sandC -= 1
#     elif cave[sandR + 1][sandC + 1] == 0:
#         sandR += 1
#         sandC += 1
#     else:
#         cave[sandR][sandC] = 2
#         sandFinPos.append([sandR, sandC])
#         sandR = 0
#         sandC = 500
#
# print("part1: ",len(sandFinPos))

sandFinPos = []
sandR = 0
sandC = 500
while True:
    if cave[sandR + 1][sandC] == 0:
        sandR += 1
    elif cave[sandR + 1][sandC - 1] == 0:
        sandR += 1
        sandC -= 1
    elif cave[sandR + 1][sandC + 1] == 0:
        sandR += 1
        sandC += 1
    elif sandR == 0 and sandC == 500:
        cave[sandR][sandC] = 2
        sandFinPos.append([sandR, sandC])
        break
    else:
        cave[sandR][sandC] = 2
        sandFinPos.append([sandR, sandC])
        sandR = 0
        sandC = 500


print("part2: ",len(sandFinPos))