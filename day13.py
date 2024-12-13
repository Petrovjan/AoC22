import string
uraw = open("day13.txt").read()
raw = uraw.split("\n\n")
data = [x.split("\n") for x in raw]

goodPairs = []

def isOrderCorrect(first: list, second: list):
    for l in range(100):
        try:
            if isinstance(first[l], int) and isinstance(second[l], int):
                if first[l] < second[l]:
                    return 1
                elif first[l] > second[l]:
                    return 0
                else:
                    continue
            elif isinstance(first[l], int) and isinstance(second[l], list):
                return isOrderCorrect([first[l]], second[l])
            elif isinstance(first[l], list) and isinstance(second[l], int):
                return isOrderCorrect(first[l], [second[l]])
            elif isinstance(first[l], list) and isinstance(second[l], list):
                if isOrderCorrect(first[l], second[l]) in (0, 1):
                    return isOrderCorrect(first[l], second[l])
                else:
                    pass
            else:
                print("error")
        except IndexError:
            if len(first) < len(second):
                return 1
            elif len(first) > len(second):
                return 0
            else:
                return 2

for i in range(len(data)):
    first = eval(data[i][0])
    second = eval(data[i][1])
    if isOrderCorrect(first, second) == 1:
        goodPairs.append(i + 1)
    elif isOrderCorrect(first, second) == 2:
        print(first, " --- ", second)

print("part1: ",sum(goodPairs))


strdata = [x for x in uraw.split("\n")]
while '' in strdata:
    strdata.remove('')

lesstwo = 0
lesssix = 0
for line in strdata:
    pass
    if -1 < line.find(",") < line.find("]"):
        rp = line[:line.find(",")+1]
        rp = rp.replace(",", "]")
    else:
        rp = line[:line.find("]")+1]
    mp = eval(rp[rp.rindex("["):])
    if len(mp) > 0:
        firstnum = mp[0]
        if firstnum < 2:
            lesstwo += 1
        if firstnum < 6:
            lesssix += 1
    else:
        lesstwo += 1
        lesssix += 1

print("part2: ", (lesstwo + 1) * (lesssix + 2))