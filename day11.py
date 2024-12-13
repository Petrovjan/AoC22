raw = open("day11.txt").read().split("\n\n")
data = [x.split("\n") for x in raw]

numMon = len(raw)

mOps = dict()
for m in range(numMon):
    mOps[m] = data[m][2].split(": ")[1].replace("old", "mItem").replace("new", "mItem")

mTests = dict()
for m in range(numMon):
    mTests[m] = int(data[m][3].split(" ")[-1])

mTarget = dict()
for m in range(numMon):
    mTarget[m] = [data[m][4].split(" ")[-1], data[m][5].split(" ")[-1]]

mItems = dict()
for m in range(numMon):
    itList = list(data[m][1].split(": ")[1].split(', '))
    itList = [int(x) for x in itList]
    mItems[m] = itList

mCounter = dict()
for m in range(numMon):
    mCounter[m] = 0

mTestsCom = 1
for i in mTests.values():
    mTestsCom *= i

for round in range(10000):
    for m in range(numMon):
        for mItem in mItems[m]:
            mCounter[m] += 1
            exec(mOps[m])
            mItem = mItem % mTestsCom
            if mItem % mTests[m] == 0:
                target = int(mTarget[m][0])
                curItems = mItems[target]
                curItems.append(mItem)
                mItems[target] = curItems
            else:
                target = int(mTarget[m][1])
                curItems = mItems[target]
                curItems.append(mItem)
                mItems[target] = curItems
        mItems[m] = []

results = list(mCounter.values())
res1 = max(results)
results.remove(res1)
res2 = max(results)
print("part2: ",res1*res2)