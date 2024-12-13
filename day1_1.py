raw = open("day1a.txt").read()
semi = raw.split("\n\n")
data = []
for i in semi:
    data.append(i.split("\n"))
for j in range(len(data)):
    for k in range(len(data[j])):
        data[j][k] = int(data[j][k])
for l in range(len(data)):
    data[l]=sum(data[l])
a = max(data)
print("part1: ", a)
data.remove(a)
b = max(data)
data.remove(b)
c = max(data)
data.remove(c)
print("part2: ",a+b+c)