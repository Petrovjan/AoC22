raw = open("day4.txt").read().split("\n")
data = [x.split(",") for x in raw]

counter = 0

for i in range(len(data)):
    fp = data[i][0].split("-")
    sp = data[i][1].split("-")
    if int(fp[0]) <= int(sp[0]) and int(fp[1]) >= int(sp[1]):
        counter += 1
    elif int(sp[0]) <= int(fp[0]) and int(sp[1]) >= int(fp[1]):
        counter += 1
print("part1: ",counter)

counter2 = 0

for j in range(len(data)):
    fp = data[j][0].split("-")
    fe = [y for y in range(int(fp[0]), int(fp[1]) + 1)]
    sp = data[j][1].split("-")
    se = [y for y in range(int(sp[0]), int(sp[1]) + 1)]
    overlap = list(set(fe) & set(se))
    if len(overlap) > 0:
        counter2 += 1

print("part2: ",counter2)