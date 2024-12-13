import string
from sympy import Symbol
from sympy.solvers import solve
from sympy import sympify

data = list(open("day21.txt").read().split("\n"))
rt = ""
fdic = dict()
for i in range(len(data)-1,-1,-1):
    data[i] = data[i].replace(":", " =")
    fdic[data[i][0:4]] = data[i].split()[2:]
    if data[i][0:4] == "root":
        rt = data.pop(i)
        continue
    elif not data[i][-1].isnumeric():
        data.append(data.pop(i))
    elif data[i][0:4] == "humn":
        hm = data[i]
data.append(rt)

numErr = 1
while numErr != 0:
    numErr = 0
    for d in data:
        try:
            exec(d)
        except NameError:
            numErr += 1
print("part1:", int(root))

data.remove(rt)
keyOne = rt.split()[2]
keyTwo = rt.split()[4]

data.remove(hm)
data.insert(0, "humn = 9999")
fdic['humn'] = ['9999']

rightside = int(eval(keyTwo))
equation = "(" + "".join(fdic[keyOne]) + ")"

found = 1
while found:
    found = 0
    for k in range(len(equation)):
        if equation[k] in string.ascii_lowercase:
            found = 1
            equation = equation[:k] + "(" + "".join(fdic[equation[k:k+4]]) + ")" + equation[k+4:]
            break

equation = equation.replace("9999", "humn")
equation = equation + "-" + str(rightside)

humn = Symbol('humn')
print("part2:", solve(sympify(equation), humn))