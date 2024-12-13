raw = open("day2.txt").read()
data = raw.split("\n")
print(data)
score = 0

def

for i in data:
    if i[0] == "A":
        if i[2] == "X":
            score += 4
        elif i[2] == "Y":
            score += 8
        else:
            score += 3
    elif i[0] == "B":
        if i[2] == "Y":
            score += 5
        elif i[2] == "Z":
            score += 9
        else:
            score += 1
    elif i[0] == "C":
        if i[2] == "Z":
            score += 6
        elif i[2] == "X":
            score += 7
        else:
            score += 2

two = 0
for i in data:
    if i[0] == "A":
        if i[2] == "X":
            two += 3
        elif i[2] == "Y":
            two += 4
        else:
            two += 8
    elif i[0] == "B":
        if i[2] == "X":
            two += 1
        elif i[2] == "Y":
            two += 5
        else:
            two += 9
    elif i[0] == "C":
        if i[2] == "X":
            two += 2
        elif i[2] == "Y":
            two += 6
        else:
            two += 7
print(score)
print(two)