import string
raw = open("day3.txt").read()
data = raw.split("\n")
print(data)
score = 0
bag = []
for i in data:
    bagone = i[:len(i)//2]
    bagtwo = i[len(i)//2:]
    for j in bagone:
        if j in bagtwo:
            if j.islower():
                bag.append(string.ascii_lowercase.index(j) + 1)
            else:
                bag.append(string.ascii_uppercase.index(j) + 27)
            break
print("part1: ", sum(bag))

badge = []
for k in range(0, len(data), 3):
    for l in data[k]:
        if l in data[k+1] and l in data[k+2]:
            if l.islower():
                badge.append(string.ascii_lowercase.index(l) + 1)
            else:
                badge.append(string.ascii_uppercase.index(l) + 27)
            break

print("part2: ",sum(badge))