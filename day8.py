data = open("day8.txt").read().split("\n")

visible = set()

for i in range(len(data)):
    tallest = -1
    for j in range(len(data[i])):
        if int(data[i][j]) > tallest:
            tallest = int(data[i][j])
            visible.add(str(i) + ";" + str(j))
    tallest = -1
    for j in range(len(data[i]) - 1, -1, -1):
        if int(data[i][j]) > tallest:
            tallest = int(data[i][j])
            if i == 3 and j == 3:
                print("ouch")
            visible.add(str(i) + ";" + str(j))

for k in range(len(data[0])):
    tallest = -1
    for l in range(len(data)):
        if int(data[l][k]) > tallest:
            tallest = int(data[l][k])
            visible.add(str(l) + ";" + str(k))
    tallest = -1
    for l in range(len(data) - 1, -1, -1):
        if int(data[l][k]) > tallest:
            tallest = int(data[l][k])
            visible.add(str(l) + ";" + str(k))

print("Result 1: ", len(visible))

treescore = dict()

def countVisible(row, col):
    global data
    right = 0
    left = 0
    top = 0
    bot = 0
    for i in range(col + 1, len(data[0])):
        if int(data[row][i]) < int(data[row][col]):
            right += 1
        else:
            right += 1
            break
    for i in range(col - 1, -1, -1):
        if int(data[row][i]) < int(data[row][col]):
            left += 1
        else:
            left += 1
            break
    for l in range(row + 1, len(data)):
        if int(data[l][col]) < int(data[row][col]):
            bot += 1
        else:
            bot += 1
            break
    for l in range(row - 1, -1, -1):
        if int(data[l][col]) < int(data[row][col]):
            top += 1
        else:
            top += 1
            break
    return right * left * top * bot


for m in range(1, len(data) - 1):
    for n in range(1, len(data[0]) - 1):
        treescore[str(m) + ";" + str(n)] = countVisible(m, n)

print("Result 2: ",max(treescore.values()))