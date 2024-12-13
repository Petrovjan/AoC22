raw = open("day20.txt").read().split("\n")


rdata = [int(x) for x in raw]
# rdata = [1,2,-3,3,-2,0,4]
data = []
for count, item in enumerate(rdata):
    data.append([count, item])
for k in range(len(data)):
    data[k][1] = data[k][1]*811589153
dlen = len(data)





for i in range(10):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[j][0] == i:
                inCur = j
                cur = data[j]
                if data[j][1] == 0:
                    zero = data[j]
        inNew = inCur + cur[1]
        if 0 <= inNew < dlen:
            moving = data.pop(inCur)
            data.insert(inNew, moving)
        else:
            moving = data.pop(inCur)
            data.insert(inNew % (dlen - 1) , moving)

oneK = (data.index(zero) + 1000)%(dlen)
twoK = (data.index(zero) + 2000)%(dlen)
thrK = (data.index(zero) + 3000)%(dlen)
print(data[oneK][1] + data[twoK][1] + data[thrK][1])


#5932 too high
#7686 too high
#5497 too high
