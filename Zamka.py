l = int(input())
d = int(input())
x = int(input())
lst = []
foundMin = False
foundMax = False

for i in range(l, d+1):
    z = str(i)
    y = 0
    for i in z:
        y += int(i)
    if y == x and foundMin == False:
        print(z)
        lst.append(z)
        foundMin = True

for i in range(-d, -l+1):
    z = str(-i)
    y = 0
    for i in z:
        y += int(i)
    if y == x and foundMax == False:
        print(z)
        lst.append(z)
        foundMax = True