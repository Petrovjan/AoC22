data = open("day18.txt").read().split("\n")
for i in range(len(data)):
    data[i] = eval(data[i])

grid = [[[0 for x in range(23)] for y in range(23)] for z in range(23)]
for j in data:
    grid[j[2]][j[1]][j[0]] = 1
print(grid)

surfaces = 0
for c in data:
    for x, y, z in zip((-1, 1, 0, 0, 0, 0), (0, 0, -1, 1, 0, 0), (0, 0, 0, 0, -1, 1)):
        if grid[c[2] + x][c[1] + y][c[0] + z] == 0:
            surfaces += 1
print(surfaces)

for a in range(len(grid)):
    for b in range(len(grid[a])):
        for c in range(len(grid[a][b])):
            if (a == 0 or a == len(grid) - 1) or ((b == 0 or b == len(grid[a]) - 1)) or ((c == 0 or c == len(grid[a][b]) - 1)):
                if grid[a][b][c] == 0:
                    grid[a][b][c] = 2


updated = True
while updated:
    updated = False
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            for c in range(len(grid[a][b])):
                for u, v, w in zip((-1, 1, 0, 0, 0, 0), (0, 0, -1, 1, 0, 0), (0, 0, 0, 0, -1, 1)):
                    if grid[a][b][c] == 0 and grid[a + u][b + v][c + w] == 2:
                        grid[a][b][c] = 2
                        updated = True

print(grid)

surfaces = 0
for c in data:
    for x, y, z in zip((-1, 1, 0, 0, 0, 0), (0, 0, -1, 1, 0, 0), (0, 0, 0, 0, -1, 1)):
        if grid[c[2] + x][c[1] + y][c[0] + z] == 2:
            surfaces += 1
print(surfaces)
