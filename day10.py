data = open("day10.txt").read().split("\n")
cycle = 1
x = 1
values = {1:1}

for op in data:
    if op.split()[0] == "noop":
        cycle += 1
        values[cycle] = x
    elif op.split()[0] == "addx":
        cycle += 1
        values[cycle] = x
        cycle += 1
        x += int(op.split()[1])
        values[cycle] = x

result = 0
for c in range(1, 221):
    if (c-20)%40 == 0:
        result += c * values[c]
print("part1: ", result)

crt = [["#" for v in range(40)] for w in range(6)]

for t in range(1, 241):
    if t % 40 == 0:
        horpoz = 40
    else:
        horpoz = t % 40
    verpoz = (t - 1) // 40
    sprite = [values[t] - 1, values[t], values[t] + 1]
    if (horpoz-1) in sprite:
        crt[verpoz][horpoz-1] = "██"
    else:
        crt[verpoz][horpoz-1] = "░░"

for i in range(6):
    print(''.join(crt[i]))