import copy
raw = open("day19.txt").read().split("\n")
data =  [[x[x.index("costs ")+6:x.index(" ore.")], x[x.index("clay robot costs ")+17:x.index("clay robot costs ")+18],
          x[x.index("obsidian robot costs ")+21:x.index(" ore and")], x[x.index("obsidian robot costs ")+31:x.rindex(" clay")],
          x[x.index("geode robot costs ")+18:x.rindex(" ore")], x[x.rindex("ore and ")+8:x.rindex(" obsidian.")]] for x in raw]
print(data)

results = dict()
ind = 0
for cost in data:
    ind += 1
    newstep = True
    finished = set()
    explored = [[0, 1, 0, 0, 0, 0, 0, 0, 0]]  # [20; 1, 5, 2, 2; 10, 5, 1, 4] time, bots..., materials...
    topscore = 0
    qq = 0
    while len(explored) > 0:
        newpaths = []
        cur = explored.pop()

        if cur[0] == 32:
            if cur[8] > topscore:
                topscore = cur[8]
                finished.add(tuple(cur))
            continue
        if cur[3] >= 1 and cur[0] < 32: #build geode bot
            if cur[7] >= int(cost[5]) and cur[5] >= int(cost[4]):
                newpaths.append([cur[0] + 1, cur[1], cur[2], cur[3],cur[4] + 1, cur[5] - int(cost[4]) + cur[1], cur[6] + cur[2], cur[7] - int(cost[5]) + cur[3], cur[8] + cur[4]])
            else:
                wait = 0
                c7 = cur[7]
                c5 = cur[5]
                while c7 < int(cost[5]) or c5 < int(cost[4]):
                    if cur[0] + 1 + wait == 32:
                        newpaths.append([cur[0] + 1 + wait, cur[1], cur[2], cur[3], cur[4],
                                         cur[5] + cur[1] * (1 + wait), cur[6] + cur[2] * (1 + wait),
                                         cur[7] + cur[3] * (1 + wait), cur[8] + cur[4] * (1 + wait)])
                        break
                    wait += 1
                    c7 = cur[7] + cur[3]*wait
                    c5 = cur[5] + cur[1]*wait
                else:
                    newpaths.append([cur[0] + 1 + wait, cur[1], cur[2], cur[3], cur[4] + 1, cur[5] - int(cost[4]) + cur[1]*(1+wait), cur[6] + cur[2]*(1+wait), cur[7] - int(cost[5]) + cur[3]*(1+wait), cur[8] + cur[4]*(1+wait)])

        if cur[2] >= 1 and cur[0] < 32: #build obs bot
            if cur[6] >= int(cost[3]) and cur[5] >= int(cost[2]):
                newpaths.append([cur[0] + 1, cur[1], cur[2], cur[3] + 1, cur[4], cur[5] - int(cost[2]) + cur[1], cur[6] - int(cost[3]) + cur[2], cur[7] + cur[3], cur[8] + cur[4]])
            else:
                wait = 0
                c6 = cur[6]
                c5 = cur[5]
                while c6 < int(cost[3]) or c5 < int(cost[2]):
                    if cur[0] + 1 + wait == 32:
                        newpaths.append([cur[0] + 1 + wait, cur[1], cur[2], cur[3], cur[4],
                                         cur[5] + cur[1] * (1 + wait), cur[6] + cur[2] * (1 + wait),
                                         cur[7] + cur[3] * (1 + wait), cur[8] + cur[4] * (1 + wait)])
                        break
                    wait += 1
                    c6 = cur[6] + cur[2]*wait
                    c5 = cur[5] + cur[1]*wait
                else:
                    newpaths.append([cur[0] + 1 + wait, cur[1], cur[2], cur[3] + 1, cur[4], cur[5] - int(cost[2]) + cur[1]*(1+wait), cur[6] - int(cost[3]) + cur[2]*(1+wait), cur[7] + cur[3]*(1+wait), cur[8] + cur[4]*(1+wait)])

        if cur[0] < 32: #build clay bot
            if cur[5] >= int(cost[1]):
                newpaths.append([cur[0] + 1, cur[1], cur[2] + 1, cur[3], cur[4], cur[5] - int(cost[1]) + cur[1], cur[6] + cur[2], cur[7] + cur[3], cur[8] + cur[4]])
            else:
                wait = 0
                c5 = cur[5]
                while c5 < int(cost[1]):
                    if cur[0] + 1 + wait == 32:
                        newpaths.append([cur[0] + 1 + wait, cur[1], cur[2], cur[3], cur[4],
                                         cur[5] + cur[1] * (1 + wait), cur[6] + cur[2] * (1 + wait),
                                         cur[7] + cur[3] * (1 + wait), cur[8] + cur[4] * (1 + wait)])
                        break
                    wait += 1
                    c5 = cur[5] + cur[1] * wait
                else:
                    newpaths.append([cur[0] + 1 + wait, cur[1], cur[2] + 1, cur[3], cur[4], cur[5] - int(cost[1]) + cur[1] * (1 + wait), cur[6] + cur[2] * (1 + wait), cur[7] + cur[3] * (1 + wait), cur[8] + cur[4] * (1 + wait)])

        if cur[0] < 32 and cur[1] < 4: #build ore bot
            if cur[5] >= int(cost[0]):
                newpaths.append([cur[0] + 1, cur[1] + 1, cur[2], cur[3], cur[4], cur[5] - int(cost[0]) + cur[1], cur[6] + cur[2], cur[7] + cur[3], cur[8] + cur[4]])
            else:
                wait = 0
                c5 = cur[5]
                while c5 < int(cost[0]):
                    if cur[0] + 1 + wait == 32:
                        newpaths.append([cur[0] + 1 + wait, cur[1], cur[2], cur[3], cur[4],
                                         cur[5] + cur[1] * (1 + wait), cur[6] + cur[2] * (1 + wait),
                                         cur[7] + cur[3] * (1 + wait), cur[8] + cur[4] * (1 + wait)])
                        break
                    wait += 1
                    c5 = cur[5] + cur[1] * wait
                else:
                    newpaths.append([cur[0] + 1 + wait, cur[1] + 1, cur[2], cur[3], cur[4], cur[5] - int(cost[0]) + cur[1] * (1 + wait), cur[6] + cur[2] * (1 + wait), cur[7] + cur[3] * (1 + wait), cur[8] + cur[4] * (1 + wait)])

        if cur[0] < 32 and cur[4] > 0: #wait till end
            wait = 32 - cur[0]
            newpaths.append([cur[0] + wait, cur[1], cur[2], cur[3], cur[4],
                             cur[5] + cur[1] * wait, cur[6] + cur[2] * wait,
                             cur[7] + cur[3] * wait, cur[8] + cur[4] * wait])

        explored = explored + newpaths[:]
    print(topscore)
    results[ind] = topscore

print(results)

result = 1
for m in results.keys():
    result *= results[m]
print(result)
