data = list(open("day6.txt").read())

markerlen = 4
i = markerlen
buffer = data[:markerlen]

while True:
    if len(buffer) == len(set(buffer)):
        print("result: ", i)
        break
    else:
        buffer.pop(0)
        buffer.append(data[i])
        i += 1