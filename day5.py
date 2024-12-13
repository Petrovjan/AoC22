raw = open("day5a.txt").read().split("\n")
moves = [x.split(",") for x in raw]

raw = open("day5b.txt").read().split("\n")
stacks = [x.split(",") for x in raw]

for move in moves:
    froms = int(move[2]) - 1
    tos = int(move[1]) - 1
    for i in range(int(move[0])):
        moving = stacks[tos].pop()
        stacks[froms].append(moving)

result = ""
for i in stacks:
    result += i[-1]

print("part1: ",result)

raw = open("day5b.txt").read().split("\n")
stacks = [x.split(",") for x in raw]

for move in moves:
    j = -int(move[0])
    froms = int(move[2]) - 1
    tos = int(move[1]) - 1
    while j < 0:
        moving = stacks[tos].pop(j)
        stacks[froms].append(moving)
        j += 1


result = ""
for i in stacks:
    result += i[-1]

print("part2: ",result)