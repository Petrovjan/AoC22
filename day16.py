import fnmatch

raw = open("day16.txt").read().split("\n")
rdata = [x.split(";") for x in raw]

data = list()
for i in range(len(rdata)):
    a = rdata[i][0][6:8]
    b = rdata[i][0].split("=")[1]
    c = rdata[i][1]
    c = c.replace(", ",",")
    d = c.split(" ")[-1].split(",")
    data.append([a, b, d])

datDict = dict()
valves = ["AA"]
for i in data:
    datDict[i[0]] = [i[1], i[2]]
    if int(i[1]) > 0:
        valves.append(i[0])


distances = dict()
distances = {('AA', 'WA'): 2, ('WA', 'AA'): 2, ('AA', 'PL'): 2, ('PL', 'AA'): 2, ('AA', 'PC'): 2, ('PC', 'AA'): 2, ('AA', 'YL'): 2, ('YL', 'AA'): 2, ('AA', 'TU'): 3, ('TU', 'AA'): 3, ('AA', 'IO'): 4, ('IO', 'AA'): 4, ('AA', 'OE'): 4, ('OE', 'AA'): 4, ('AA', 'PV'): 4, ('PV', 'AA'): 4, ('AA', 'OC'): 4, ('OC', 'AA'): 4, ('AA', 'RL'): 5, ('RL', 'AA'): 5, ('AA', 'RO'): 5, ('RO', 'AA'): 5, ('AA', 'PZ'): 5, ('PZ', 'AA'): 5, ('AA', 'RM'): 6, ('RM', 'AA'): 6, ('AA', 'JY'): 6, ('JY', 'AA'): 6, ('AA', 'PP'): 7, ('PP', 'AA'): 7, ('PL', 'TU'): 2, ('TU', 'PL'): 2, ('PL', 'WA'): 3, ('WA', 'PL'): 3, ('PL', 'YL'): 3, ('YL', 'PL'): 3, ('PL', 'RO'): 3, ('RO', 'PL'): 3, ('PL', 'PC'): 4, ('PC', 'PL'): 4, ('PL', 'IO'): 5, ('IO', 'PL'): 5, ('PL', 'OE'): 5, ('OE', 'PL'): 5, ('PL', 'JY'): 5, ('JY', 'PL'): 5, ('PL', 'RL'): 6, ('RL', 'PL'): 6, ('PL', 'PV'): 6, ('PV', 'PL'): 6, ('PL', 'OC'): 6, ('OC', 'PL'): 6, ('PL', 'RM'): 7, ('RM', 'PL'): 7, ('PL', 'PZ'): 7, ('PZ', 'PL'): 7, ('PL', 'PP'): 9, ('PP', 'PL'): 9, ('RM', 'OC'): 2, ('OC', 'RM'): 2, ('RM', 'JY'): 2, ('JY', 'RM'): 2, ('RM', 'PC'): 4, ('PC', 'RM'): 4, ('RM', 'RO'): 5, ('RO', 'RM'): 5, ('RM', 'TU'): 5, ('TU', 'RM'): 5, ('RM', 'PV'): 6, ('PV', 'RM'): 6, ('RM', 'PZ'): 7, ('PZ', 'RM'): 7, ('RM', 'WA'): 8, ('WA', 'RM'): 8, ('RM', 'YL'): 8, ('YL', 'RM'): 8, ('RM', 'PP'): 9, ('PP', 'RM'): 9, ('RM', 'IO'): 10, ('IO', 'RM'): 10, ('RM', 'OE'): 10, ('OE', 'RM'): 10, ('RM', 'RL'): 11, ('RL', 'RM'): 11, ('PZ', 'PP'): 2, ('PP', 'PZ'): 2, ('PZ', 'PC'): 3, ('PC', 'PZ'): 3, ('PZ', 'PV'): 5, ('PV', 'PZ'): 5, ('PZ', 'OC'): 5, ('OC', 'PZ'): 5, ('PZ', 'WA'): 7, ('WA', 'PZ'): 7, ('PZ', 'YL'): 7, ('YL', 'PZ'): 7, ('PZ', 'TU'): 8, ('TU', 'PZ'): 8, ('PZ', 'IO'): 9, ('IO', 'PZ'): 9, ('PZ', 'OE'): 9, ('OE', 'PZ'): 9, ('PZ', 'JY'): 9, ('JY', 'PZ'): 9, ('PZ', 'RL'): 10, ('RL', 'PZ'): 10, ('PZ', 'RO'): 10, ('RO', 'PZ'): 10, ('TU', 'RO'): 2, ('RO', 'TU'): 2, ('TU', 'JY'): 3, ('JY', 'TU'): 3, ('TU', 'YL'): 3, ('YL', 'TU'): 3, ('TU', 'WA'): 5, ('WA', 'TU'): 5, ('TU', 'PC'): 5, ('PC', 'TU'): 5, ('TU', 'OC'): 7, ('OC', 'TU'): 7, ('TU', 'IO'): 7, ('IO', 'TU'): 7, ('TU', 'OE'): 7, ('OE', 'TU'): 7, ('TU', 'PV'): 7, ('PV', 'TU'): 7, ('TU', 'RL'): 8, ('RL', 'TU'): 8, ('TU', 'PP'): 10, ('PP', 'TU'): 10, ('PC', 'PV'): 2, ('PV', 'PC'): 2, ('PC', 'OC'): 2, ('OC', 'PC'): 2, ('PC', 'WA'): 4, ('WA', 'PC'): 4, ('PC', 'YL'): 4, ('YL', 'PC'): 4, ('PC', 'PP'): 5, ('PP', 'PC'): 5, ('PC', 'IO'): 6, ('IO', 'PC'): 6, ('PC', 'OE'): 6, ('OE', 'PC'): 6, ('PC', 'JY'): 6, ('JY', 'PC'): 6, ('PC', 'RL'): 7, ('RL', 'PC'): 7, ('PC', 'RO'): 7, ('RO', 'PC'): 7, ('IO', 'WA'): 2, ('WA', 'IO'): 2, ('IO', 'OE'): 3, ('OE', 'IO'): 3, ('IO', 'RL'): 5, ('RL', 'IO'): 5, ('IO', 'YL'): 6, ('YL', 'IO'): 6, ('IO', 'RO'): 8, ('RO', 'IO'): 8, ('IO', 'PV'): 8, ('PV', 'IO'): 8, ('IO', 'OC'): 8, ('OC', 'IO'): 8, ('IO', 'JY'): 10, ('JY', 'IO'): 10, ('IO', 'PP'): 11, ('PP', 'IO'): 11, ('OC', 'JY'): 4, ('JY', 'OC'): 4, ('OC', 'PV'): 4, ('PV', 'OC'): 4, ('OC', 'WA'): 6, ('WA', 'OC'): 6, ('OC', 'YL'): 6, ('YL', 'OC'): 6, ('OC', 'RO'): 7, ('RO', 'OC'): 7, ('OC', 'PP'): 7, ('PP', 'OC'): 7, ('OC', 'OE'): 8, ('OE', 'OC'): 8, ('OC', 'RL'): 9, ('RL', 'OC'): 9, ('PV', 'WA'): 6, ('WA', 'PV'): 6, ('PV', 'YL'): 6, ('YL', 'PV'): 6, ('PV', 'PP'): 7, ('PP', 'PV'): 7, ('PV', 'OE'): 8, ('OE', 'PV'): 8, ('PV', 'JY'): 8, ('JY', 'PV'): 8, ('PV', 'RL'): 9, ('RL', 'PV'): 9, ('PV', 'RO'): 9, ('RO', 'PV'): 9, ('PP', 'WA'): 9, ('WA', 'PP'): 9, ('PP', 'YL'): 9, ('YL', 'PP'): 9, ('PP', 'OE'): 11, ('OE', 'PP'): 11, ('PP', 'JY'): 11, ('JY', 'PP'): 11, ('PP', 'RL'): 12, ('RL', 'PP'): 12, ('PP', 'RO'): 12, ('RO', 'PP'): 12, ('RL', 'WA'): 3, ('WA', 'RL'): 3, ('RL', 'OE'): 5, ('OE', 'RL'): 5, ('RL', 'YL'): 7, ('YL', 'RL'): 7, ('RL', 'RO'): 9, ('RO', 'RL'): 9, ('RL', 'JY'): 11, ('JY', 'RL'): 11, ('RO', 'YL'): 3, ('YL', 'RO'): 3, ('RO', 'JY'): 3, ('JY', 'RO'): 3, ('RO', 'WA'): 6, ('WA', 'RO'): 6, ('RO', 'OE'): 8, ('OE', 'RO'): 8, ('WA', 'OE'): 2, ('OE', 'WA'): 2, ('WA', 'YL'): 4, ('YL', 'WA'): 4, ('WA', 'JY'): 8, ('JY', 'WA'): 8, ('OE', 'YL'): 6, ('YL', 'OE'): 6, ('OE', 'JY'): 10, ('JY', 'OE'): 10, ('YL', 'JY'): 6, ('JY', 'YL'): 6}
if len(distances) == 0:
    for begin in valves:
        visited = [[begin]]
        found = []
        for t in range(1, 31):
            newsteps = []
            for w in range(len(visited)):
                if visited[w] == []:
                    continue
                laststep = visited[w][-1]
                for p in range(len(datDict[laststep][1])):
                    ns = datDict[laststep][1][p]
                    if ns in valves and ns not in found and begin != ns:
                        found.append(ns)
                        distances[begin, ns] = t
                        distances[ns, begin] = t
                    if len(visited[w]) == 1 or (len(visited[w]) > 1 and ns != visited[w][-2]):
                        newsteps.append(visited[w] + [ns])
            visited = newsteps[:]

print(distances) #{('AA', 'WA'): 2, ('WA', 'AA'): 2, ('AA', 'PL'): 2...

start = "AA"
explored = [[0, [start]]] #[[2, [AA, BB]],[3, [AA, DD]]]
opened = [start]
completed = []
while True:
    exl = len(explored)
    print(exl)
    print(explored[-1])
    newex = []
    for v in range(len(explored)):
        added = False
        for poss in distances.keys():
            if poss[1] not in explored[v][1] and explored[v][1][-1] == poss[0]: #nevracet se na navstivene misto
                if explored[v][0] + distances[poss] + 1 <= 30:
                    newex.append([explored[v][0] + distances[poss] + 1, explored[v][1] + [poss[1]]]) #pridat cas k otevreni
                    added = True
        if not added:
            completed.append(explored[v])
    explored = newex[:]
    if len(newex) == 0:
        break


maxscore = 0
for path in completed:
    curscore = 0
    curtime = 0
    for i in range(1, len(path[1])):
        curtime += (distances[(path[1][i-1], path[1][i])] + 1)
        sc = int(datDict[path[1][i]][0]) * (30 - curtime)
        curscore += sc
    if curscore > maxscore:
        maxscore = curscore
        bestpath = path
print(maxscore)
print(bestpath)


