data = [[2924811, 3544081, 3281893, 3687621], [2719183, 2520103, 2872326, 2415450],
        [3754787, 3322726, 3281893, 3687621], [1727202, 1485124, 1329230, 1133797],
        [2517008, 2991710, 2454257, 2594911], [1472321, 3123671, 2216279, 3414523],
        [3456453, 3959037, 3281893, 3687621], [3997648, 2624215, 4401794, 2000000], [463281, 967584, 1329230, 1133797],
        [2395529, 1897869, 2454257, 2594911], [3094466, 3888307, 3281893, 3687621],
        [2737812, 3928154, 2744537, 4159197], [813538, 3874308, 2216279, 3414523], [822358, 1997263, 1329230, 1133797],
        [3993754, 3951321, 3281893, 3687621], [2585409, 3541887, 2216279, 3414523],
        [3269796, 3730504, 3281893, 3687621], [3075750, 2873879, 2872326, 2415450], [1357, 2747918, -1077481, 3057204],
        [2256257, 344800, 1854450, -900998], [2779742, 2308087, 2872326, 2415450], [867692, 64146, 1329230, 1133797],
        [3454465, 966419, 4401794, 2000000], [1902550, 2398376, 2454257, 2594911]]

# row2M = set()
# for i in data:
#     dist = abs(i[1] - i[3]) + abs(i[0] - i[2])
#     extraDist = dist - abs(i[1] - 2000000)
#     if extraDist > 0:
#         aX2M = i[0] - extraDist
#         zX2M = i[0] + extraDist
#         for x in range(aX2M, zX2M + 1):
#             row2M.add(x)
# for i in data:
#     if i[3] == 2000000:
#         row2M.discard(i[2])
#     if i[1] == 2000000:
#         row2M.discard(i[0])
#
# print("part1: ", len(row2M))


size = 4000000

for y in range(size + 1):
    rowBlocks = []
    for i in data:
        borders = []
        dist = abs(i[1] - i[3]) + abs(i[0] - i[2])
        extraDist = dist - abs(i[1] - y)
        if extraDist > 0:
            aX2M = i[0] - extraDist
            zX2M = i[0] + extraDist
            if aX2M < 0:
                borders.append(0)
            elif aX2M <= size:
                borders.append(aX2M)
            if zX2M > size:
                borders.append(size)
            elif zX2M >= 0:
                borders.append(zX2M)
            if len(borders) == 2:
                rowBlocks.append(borders)
    mnozina = [[0,size]]
    for lim in rowBlocks:
        mToA = []
        for m in range(len(mnozina)):
            if lim[0] <= mnozina[m][0] and lim[1] >= mnozina[m][1]:
                mnozina[m] = [0,0]
            elif lim[0] > mnozina[m][0] and lim[0] > mnozina[m][1]:
                continue
            elif lim[1] < mnozina[m][0] and lim[1] < mnozina[m][1]:
                continue
            elif lim[0] <= mnozina[m][0] and lim[1] < mnozina[m][1]:
                mnozina[m][0] = lim[1]
            elif lim[0] > mnozina[m][0] and lim[1] >= mnozina[m][1]:
                mnozina[m][1] = lim[0]
            elif lim[0] > mnozina[m][0] and lim[1] < mnozina[m][1]:
                mToA.append([lim[1], mnozina[m][1]])
                mnozina[m][1] = lim[0]
        mnozina = mnozina + mToA
        try:
            while True:
                mnozina.remove([0,0])
        except ValueError:
            pass
    if len(mnozina) > 0:
        print(y, mnozina)
        break
    if y%40000 == 0:
        print(y/40000)
