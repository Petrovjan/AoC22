data = open("day25.txt").read().split("\n")
print(data)

def snafuToDec(num):
    numsum = 0
    for n in range(len(num)-1,-1,-1):
        power = len(num)-n-1
        if num[n] == "=":
            transn = -2
        elif num[n] == "-":
            transn = -1
        else:
            transn = int(num[n])
        numsum += (5 ** power) * transn
    return numsum

sum = 0
for num in data:
    sum += snafuToDec(num)

print(sum)

def to_base_5(n):
    s = ""
    while n:
        s = str(n % 5) + s
        n = n // 5
    return s

def to_base_sn(n):
    add = 0
    while True:
        if n // (2 + 5*add) == 0:
            break
        else:
            add = (2 + 5*add)
    n = n + (2 + 5*add)
    s = ""
    while n:
        s = str(n % 5) + s
        n = n // 5
    s = s.replace("1", "-")
    s = s.replace("0", "=")
    s = s.replace("2", "0")
    s = s.replace("4", "2")
    s = s.replace("3", "1")

    return s

print(to_base_sn(sum))

#1 - 2: +2
#3 - 12: +12
#13 - 62: +62 vypada to na: 2 + 5*(prev x)
#63 - 312: +312