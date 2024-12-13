import sys

data = open("day7.txt").read().split("\n")

dirSizeDict = dict()
def getDirSize(dirContent):
    global dirSizeDict
    dirSize = 0
    for i in range(len(dirContent)):
        if dirContent[i][0].isnumeric():
            filename = dirContent[i].split(" ")
            dirSize += int(filename[0])
        elif dirContent[i][0:3] == "dir":
            subDirName = dirContent[i][4:]

            getSubDirContent = getContent(subDirName)
            subDirSize = getDirSize(getSubDirContent)
            if subDirName in dirSizeDict.keys():
                dirSizeDict[subDirName + str(i)] = subDirSize
            else:
                dirSizeDict[subDirName] = subDirSize
            dirSize += subDirSize
        elif dirContent[i][0] == "$":
            return dirSize
    return dirSize

def getContent(dirName):
    content = []
    for j in range(len(data)):
        if data[j][0:4] == "$ cd" and data[j][5:] == dirName:
            data[j] = "nvm"
            j += 2
            while j <= (len(data) - 1) and data[j][0] != "$":
                content.append(data[j])
                j += 1
            return content

dirSizeDict["/"] = getDirSize(data[2:])
print(dirSizeDict)

result = 0
for k in dirSizeDict.values():
    if k <= 100000:
        result += k

print("part1: ", result)

size = 70000000
empty = size - dirSizeDict.get("/")
bestSize = 70000000
for dicts in dirSizeDict:
    if dirSizeDict[dicts] + empty > 30000000:
        if dirSizeDict[dicts] < bestSize:
            bestSize = dirSizeDict[dicts]
print("part2: ", bestSize)

