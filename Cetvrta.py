x = []
y = []
for _ in range(3):
    inpt = input()
    xn,yn = inpt.split(' ')
    xn = int(xn)
    yn = int(yn)
    x.append(xn)
    y.append(yn)
xCount = 0
yCount = 0
xCor = 0
yCor = 0
for i in x:
    if i == x[0]:
        xCount += 1
for i in y:
    if i == y[0]:
        yCount += 1
if xCount == 1:
    xCor = x[0]
else:
    if x[1] != x[0]:
        xCor = x[1]
    else:
        xCor = x[2]

if yCount == 1:
    yCor = y[0]
else:
    if y[1] != y[0]:
        yCor = y[1]
    else:
        yCor = y[2]
print(f'{xCor} {yCor}')